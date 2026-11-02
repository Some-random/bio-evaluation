# catalytic_activity_0146

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHALRSSVLALWLCLHVSVRAWMTYRSANGLDEYEPEDRIIFLGTKWCGNGNVAEGPEDLGPLKETDACCREHDMCPDLIAAGQSKHGLTNTASYTRLNCGCDEKFYNCLKNSAETGSGAVRFTYFTVLGTKCYRNEHPLICVKKGWFSCSKYELDKSQPKRYQWFDVSSNFAFPRMLT

[Multiple Choices]
A. inosine(in) = inosine(out)
B. L-ornithine = L-proline + NH4(+)
C. K(+)(in) = K(+)(out)
D. a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)
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

> The supplied sequence exactly matches the UniProt entry annotated as phospholipase A2, and both current and historical records assign the reaction in D. The reaction annotation is computationally supported by a PROSITE rule; the EC assignment is transferred by similarity, so this supports D but is not direct experimental proof of activity for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal region and is cysteine-rich, which is compatible with a secreted venom protein, but those features alone do not establish phospholipase activity or the specific substrate transformation in D.


**Missing item-specific fact**

> The protein-specific identification as a phospholipase A2, including its assigned EC 3.1.1.4 reaction, is needed to select D; that functional annotation is not provided in the question.


**Reason**

> A familiar PLA2-family motif or sequence match could suggest the answer, but the supplied sequence and choices do not establish that identity through a sufficiently discriminating general biological argument without relying on protein-specific family knowledge or annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct activities; the uncertainty is whether the sequence alone identifies the enzyme, not whether the reaction choices overlap.


### Important caveats

- The cited UniProt entry matches the supplied sequence, but its source identity was inferred by reviewers and was not supplied to the evaluated model.
- The annotation supports D computationally; the cited sequence-identification and mass-spectrometry reference does not itself establish catalytic activity experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal region and is cysteine-rich, which is compatible with a secreted venom protein, but those features alone do not establish phospholipase activity or the specific substrate transformation in D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as a phospholipase A2, including its assigned EC 3.1.1.4 reaction, is needed to select D; that functional annotation is not provided in the question.",
    "reason": "A familiar PLA2-family motif or sequence match could suggest the answer, but the supplied sequence and choices do not establish that identity through a sufficiently discriminating general biological argument without relying on protein-specific family knowledge or annotation."
  },
  "case_id": "catalytic_activity_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as phospholipase A2, and both current and historical records assign the reaction in D. The reaction annotation is computationally supported by a PROSITE rule; the EC assignment is transferred by similarity, so this supports D but is not direct experimental proof of activity for this protein."
  },
  "important_caveats": [
    "The cited UniProt entry matches the supplied sequence, but its source identity was inferred by reviewers and was not supplied to the evaluated model.",
    "The annotation supports D computationally; the cited sequence-identification and mass-spectrometry reference does not itself establish catalytic activity experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct activities; the uncertainty is whether the sequence alone identifies the enzyme, not whether the reaction choices overlap."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as phospholipase A2, and both current and historical records assign the reaction in D. The reaction annotation is computationally supported by a PROSITE rule; the EC assignment is transferred by similarity, so this supports D but is not direct experimental proof of activity for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal region and is cysteine-rich, which is compatible with a secreted venom protein, but those features alone do not establish phospholipase activity or the specific substrate transformation in D.",
    "missing_item_specific_fact": "The protein-specific identification as a phospholipase A2, including its assigned EC 3.1.1.4 reaction, is needed to select D; that functional annotation is not provided in the question.",
    "reason": "A familiar PLA2-family motif or sequence match could suggest the answer, but the supplied sequence and choices do not establish that identity through a sufficiently discriminating general biological argument without relying on protein-specific family knowledge or annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct activities; the uncertainty is whether the sequence alone identifies the enzyme, not whether the reaction choices overlap."
  },
  "important_caveats": [
    "The cited UniProt entry matches the supplied sequence, but its source identity was inferred by reviewers and was not supplied to the evaluated model.",
    "The annotation supports D computationally; the cited sequence-identification and mass-spectrometry reference does not itself establish catalytic activity experimentally."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXZ6 (PA2_XYLAR) annotates this sequence as Phospholipase A2 (EC 3.1.1.4) with the exact catalytic reaction matching option D. The EC number is assigned by similarity (ECO:0000250 to P00630) and the catalytic activity by PROSITE-ProRule PRU10035 (ECO:0000255). The sequence matches the UniProt record (179 aa, sha256 confirmed). The protein was identified by mass spectrometry from venom gland tissue (PubMed:36550366). While the annotation is computational/similarity-based rather than a direct enzyme assay on this specific protein, the PLA2 family assignment is strongly supported by characteristic sequence motifs (GTKWCG, GTKCYR, catalytic His-Asp region, multiple disulfide-bonding cysteines) and the PROSITE-ProRule match.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark PLA2-family motifs: the 'IIFLGTKWCG' segment (residues ~27-34) is the classic PLA2 superfamily signature, and the later 'GTKCYR' motif reinforces this assignment. The N-terminal hydrophobic stretch (MHALRSSVLALWLCLHVSVRAW) is a cleavable signal peptide indicating a secreted protein, which eliminates membrane transporters (options A and C). The catalytic region 'NCGCDEK' and 'CYRNEHPLICV' contain the PLA2 His-Asp catalytic dyad. The multiple cysteines (forming 6-7 disulfide bonds) are characteristic of the PLA2 fold. Option B (ornithine cyclodeaminase) is a cytosolic enzyme with a completely unrelated fold and no sequence resemblance. These are general biochemical facts about well-characterized enzyme families, not item-specific database lookups.


**Missing item-specific fact**

> None critical. The PLA2 GTKWCG/GTKCYR motifs and the signal-peptide/cysteine-rich secreted-enzyme pattern are standard biochemistry knowledge sufficient to distinguish D from the other three choices.


**Reason**

> A knowledgeable biochemist can recognize the PLA2 signature motifs (GTKWCG, GTKCYR), the signal peptide, the catalytic His-Asp dyad region, and the disulfide-bonding cysteine pattern from the raw sequence. These motifs are general knowledge in enzymology, not protein-specific memorization. The distractors (nucleoside transporter, ornithine cyclodeaminase, potassium channel) are eliminated by the absence of transmembrane domains (ruling out A, C) and by the complete lack of similarity to ornithine cyclodeaminase (ruling out B).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C require transmembrane topology absent from this small secreted protein. Option B (ornithine cyclodeaminase) is a ~400-residue cytosolic enzyme with no resemblance to this sequence. Option D is the only choice consistent with the PLA2-family sequence signatures present. No ambiguity among the choices.


### Important caveats

- The EC 3.1.1.4 assignment is by similarity to P00630 (ECO:0000250), not a direct enzyme assay on this specific Xylocopa aruana protein.
- The catalytic activity annotation relies on PROSITE-ProRule PRU10035 (ECO:0000255), a computational family rule, not site-directed mutagenesis or kinetic characterization of this particular enzyme.
- The protein was identified by mass spectrometry from venom gland tissue, confirming its presence and secretion, but the evidence excerpts do not include a direct phospholipase assay on this protein.
- Despite the computational basis of the annotation, PLA2 family recognition from the GTKWCG motif is well-established and the distractors are clearly non-PLA2, making the expected answer robust.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark PLA2-family motifs: the 'IIFLGTKWCG' segment (residues ~27-34) is the classic PLA2 superfamily signature, and the later 'GTKCYR' motif reinforces this assignment. The N-terminal hydrophobic stretch (MHALRSSVLALWLCLHVSVRAW) is a cleavable signal peptide indicating a secreted protein, which eliminates membrane transporters (options A and C). The catalytic region 'NCGCDEK' and 'CYRNEHPLICV' contain the PLA2 His-Asp catalytic dyad. The multiple cysteines (forming 6-7 disulfide bonds) are characteristic of the PLA2 fold. Option B (ornithine cyclodeaminase) is a cytosolic enzyme with a completely unrelated fold and no sequence resemblance. These are general biochemical facts about well-characterized enzyme families, not item-specific database lookups.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PLA2 GTKWCG/GTKCYR motifs and the signal-peptide/cysteine-rich secreted-enzyme pattern are standard biochemistry knowledge sufficient to distinguish D from the other three choices.",
    "reason": "A knowledgeable biochemist can recognize the PLA2 signature motifs (GTKWCG, GTKCYR), the signal peptide, the catalytic His-Asp dyad region, and the disulfide-bonding cysteine pattern from the raw sequence. These motifs are general knowledge in enzymology, not protein-specific memorization. The distractors (nucleoside transporter, ornithine cyclodeaminase, potassium channel) are eliminated by the absence of transmembrane domains (ruling out A, C) and by the complete lack of similarity to ornithine cyclodeaminase (ruling out B)."
  },
  "case_id": "catalytic_activity_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXZ6 (PA2_XYLAR) annotates this sequence as Phospholipase A2 (EC 3.1.1.4) with the exact catalytic reaction matching option D. The EC number is assigned by similarity (ECO:0000250 to P00630) and the catalytic activity by PROSITE-ProRule PRU10035 (ECO:0000255). The sequence matches the UniProt record (179 aa, sha256 confirmed). The protein was identified by mass spectrometry from venom gland tissue (PubMed:36550366). While the annotation is computational/similarity-based rather than a direct enzyme assay on this specific protein, the PLA2 family assignment is strongly supported by characteristic sequence motifs (GTKWCG, GTKCYR, catalytic His-Asp region, multiple disulfide-bonding cysteines) and the PROSITE-ProRule match."
  },
  "important_caveats": [
    "The EC 3.1.1.4 assignment is by similarity to P00630 (ECO:0000250), not a direct enzyme assay on this specific Xylocopa aruana protein.",
    "The catalytic activity annotation relies on PROSITE-ProRule PRU10035 (ECO:0000255), a computational family rule, not site-directed mutagenesis or kinetic characterization of this particular enzyme.",
    "The protein was identified by mass spectrometry from venom gland tissue, confirming its presence and secretion, but the evidence excerpts do not include a direct phospholipase assay on this protein.",
    "Despite the computational basis of the annotation, PLA2 family recognition from the GTKWCG motif is well-established and the distractors are clearly non-PLA2, making the expected answer robust."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C require transmembrane topology absent from this small secreted protein. Option B (ornithine cyclodeaminase) is a ~400-residue cytosolic enzyme with no resemblance to this sequence. Option D is the only choice consistent with the PLA2-family sequence signatures present. No ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXZ6 (PA2_XYLAR) annotates this sequence as Phospholipase A2 (EC 3.1.1.4) with the exact catalytic reaction matching option D. The EC number is assigned by similarity (ECO:0000250 to P00630) and the catalytic activity by PROSITE-ProRule PRU10035 (ECO:0000255). The sequence matches the UniProt record (179 aa, sha256 confirmed). The protein was identified by mass spectrometry from venom gland tissue (PubMed:36550366). While the annotation is computational/similarity-based rather than a direct enzyme assay on this specific protein, the PLA2 family assignment is strongly supported by characteristic sequence motifs (GTKWCG, GTKCYR, catalytic His-Asp region, multiple disulfide-bonding cysteines) and the PROSITE-ProRule match.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark PLA2-family motifs: the 'IIFLGTKWCG' segment (residues ~27-34) is the classic PLA2 superfamily signature, and the later 'GTKCYR' motif reinforces this assignment. The N-terminal hydrophobic stretch (MHALRSSVLALWLCLHVSVRAW) is a cleavable signal peptide indicating a secreted protein, which eliminates membrane transporters (options A and C). The catalytic region 'NCGCDEK' and 'CYRNEHPLICV' contain the PLA2 His-Asp catalytic dyad. The multiple cysteines (forming 6-7 disulfide bonds) are characteristic of the PLA2 fold. Option B (ornithine cyclodeaminase) is a cytosolic enzyme with a completely unrelated fold and no sequence resemblance. These are general biochemical facts about well-characterized enzyme families, not item-specific database lookups.",
    "missing_item_specific_fact": "None critical. The PLA2 GTKWCG/GTKCYR motifs and the signal-peptide/cysteine-rich secreted-enzyme pattern are standard biochemistry knowledge sufficient to distinguish D from the other three choices.",
    "reason": "A knowledgeable biochemist can recognize the PLA2 signature motifs (GTKWCG, GTKCYR), the signal peptide, the catalytic His-Asp dyad region, and the disulfide-bonding cysteine pattern from the raw sequence. These motifs are general knowledge in enzymology, not protein-specific memorization. The distractors (nucleoside transporter, ornithine cyclodeaminase, potassium channel) are eliminated by the absence of transmembrane domains (ruling out A, C) and by the complete lack of similarity to ornithine cyclodeaminase (ruling out B)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C require transmembrane topology absent from this small secreted protein. Option B (ornithine cyclodeaminase) is a ~400-residue cytosolic enzyme with no resemblance to this sequence. Option D is the only choice consistent with the PLA2-family sequence signatures present. No ambiguity among the choices."
  },
  "important_caveats": [
    "The EC 3.1.1.4 assignment is by similarity to P00630 (ECO:0000250), not a direct enzyme assay on this specific Xylocopa aruana protein.",
    "The catalytic activity annotation relies on PROSITE-ProRule PRU10035 (ECO:0000255), a computational family rule, not site-directed mutagenesis or kinetic characterization of this particular enzyme.",
    "The protein was identified by mass spectrometry from venom gland tissue, confirming its presence and secretion, but the evidence excerpts do not include a direct phospholipase assay on this protein.",
    "Despite the computational basis of the annotation, PLA2 family recognition from the GTKWCG motif is well-established and the distractors are clearly non-PLA2, making the expected answer robust."
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

**Accession:** `P0DXZ6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
"P0DXZ6"
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Phosphatidylcholine 2-acylhydrolase"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P00630","source":"UniProtKB"}],"value":"3.1.1.4"}],"fullName":{"value":"Phospholipase A2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PA2"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"36550366","source":"PubMed"}],"value":"PLA2"}]}}
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.1.1.4","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10035","source":"PROSITE-ProRule"}],"name":"a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:15801"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:28868"},{"database":"ChEBI","id":"CHEBI:57643"},{"database":"ChEBI","id":"CHEBI:58168"}]}}
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
{"citation":{"authors":["Shi N.","Szanto T.G.","He J.","Schroeder C.I.","Walker A.A.","Deuis J.R.","Vetter I.","Panyi G.","King G.F.","Robinson S.D."],"citationCrossReferences":[{"database":"PubMed","id":"36550366"},{"database":"DOI","id":"10.1038/s41598-022-26867-8"}],"citationType":"journal article","firstPage":"22168","id":"36550366","journal":"Sci. Rep.","lastPage":"22168","publicationDate":"2022","title":"Venom composition and pain-causing toxins of the Australian great carpenter bee Xylocopa aruana.","volume":"12"},"referenceComments":[{"type":"TISSUE","value":"Venom"},{"type":"TISSUE","value":"Venom gland"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","IDENTIFICATION BY MASS SPECTROMETRY","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:30:01.445083+00:00.  

```text
DE   RecName: Full=Phospholipase A2;
DE            Short=PA2 {ECO:0000305};
DE            Short=PLA2 {ECO:0000303|PubMed:36550366};
DE            EC=3.1.1.4 {ECO:0000250|UniProtKB:P00630};
DE   AltName: Full=Phosphatidylcholine 2-acylhydrolase;
DE   Flags: Precursor;
```

Source SHA-256: `ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)  
**Locator:** `lines 35-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:30:01.445083+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-
CC         glycero-3-phosphocholine + a fatty acid + H(+); Xref=Rhea:RHEA:15801,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:28868,
CC         ChEBI:CHEBI:57643, ChEBI:CHEBI:58168; EC=3.1.1.4;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10035};
```

Source SHA-256: `ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
