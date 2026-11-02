# cofactor_0090

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVFPLSAKHRKYALRALAVSIILVSAAYIALTERTERVRPQRVEQNLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGGAREVQFFTDEDGERNLVALEKKGGIWRRSASEADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLIYDSLYFHGQQVAAGDILAAEVVKGGTRHQAFYYRSDKEGGGGGNYYDEDGRVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAQGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. tungstopterin
B. Na(+)
C. Co(2+)
D. Zn(2+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact-matched protein record identifies Zn(2+) as its cofactor based on experimental evidence, while qualifying that Zn is probable in vivo; nickel was observed in the crystal structure. This supports choice D as the likely physiological cofactor, not as the metal observed in that crystal.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Histidines in the sequence could be consistent with metal binding, and zinc is a common metalloprotease cofactor. But the input does not establish the protein's function or show a uniquely diagnostic zinc-binding feature that distinguishes zinc from the other listed choices.


**Missing item-specific fact**

> The protein-specific finding that it is a metallopeptidase whose likely in-vivo metal cofactor is Zn(2+); the supplied sequence and choices do not provide the experimental cofactor assignment.


**Reason**

> Selecting Zn depends on the absent protein-specific annotation or experimental evidence, rather than a sufficiently discriminating argument available from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports Zn(2+) as the likely in-vivo cofactor among the listed options. Nickel is reported in the crystal structure but is not a listed choice and is not identified as the likely physiological cofactor.


### Important caveats

- Reviewer-only evidence matches the supplied sequence exactly but was not available to the evaluated model.
- The source says Zn(2+) is probable in vivo and reports Ni(2+) in the crystal structure; these are distinct claims.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Histidines in the sequence could be consistent with metal binding, and zinc is a common metalloprotease cofactor. But the input does not establish the protein's function or show a uniquely diagnostic zinc-binding feature that distinguishes zinc from the other listed choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that it is a metallopeptidase whose likely in-vivo metal cofactor is Zn(2+); the supplied sequence and choices do not provide the experimental cofactor assignment.",
    "reason": "Selecting Zn depends on the absent protein-specific annotation or experimental evidence, rather than a sufficiently discriminating argument available from the input."
  },
  "case_id": "cofactor_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact-matched protein record identifies Zn(2+) as its cofactor based on experimental evidence, while qualifying that Zn is probable in vivo; nickel was observed in the crystal structure. This supports choice D as the likely physiological cofactor, not as the metal observed in that crystal."
  },
  "important_caveats": [
    "Reviewer-only evidence matches the supplied sequence exactly but was not available to the evaluated model.",
    "The source says Zn(2+) is probable in vivo and reports Ni(2+) in the crystal structure; these are distinct claims."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports Zn(2+) as the likely in-vivo cofactor among the listed options. Nickel is reported in the crystal structure but is not a listed choice and is not identified as the likely physiological cofactor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched protein record identifies Zn(2+) as its cofactor based on experimental evidence, while qualifying that Zn is probable in vivo; nickel was observed in the crystal structure. This supports choice D as the likely physiological cofactor, not as the metal observed in that crystal.",
    "evidence_ids": ["C5", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Histidines in the sequence could be consistent with metal binding, and zinc is a common metalloprotease cofactor. But the input does not establish the protein's function or show a uniquely diagnostic zinc-binding feature that distinguishes zinc from the other listed choices.",
    "missing_item_specific_fact": "The protein-specific finding that it is a metallopeptidase whose likely in-vivo metal cofactor is Zn(2+); the supplied sequence and choices do not provide the experimental cofactor assignment.",
    "reason": "Selecting Zn depends on the absent protein-specific annotation or experimental evidence, rather than a sufficiently discriminating argument available from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports Zn(2+) as the likely in-vivo cofactor among the listed options. Nickel is reported in the crystal structure but is not a listed choice and is not identified as the likely physiological cofactor."
  },
  "important_caveats": [
    "Reviewer-only evidence matches the supplied sequence exactly but was not available to the evaluated model.",
    "The source says Zn(2+) is probable in vivo and reports Ni(2+) in the crystal structure; these are distinct claims."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt E0N688 (MPG_NEIM3) is annotated as a zinc-dependent metallopeptidase (DD-carboxypeptidase/endopeptidase Mpg) with cofactor Zn(2+) supported by experimental evidence (ECO:0000269, PubMed:22046377). The annotation states 'Binds 1 zinc ion per subunit. Binds a divalent metal cation, probably Zn(2+) in vivo.' The protein is explicitly named 'Zinc metallopeptidase' and 'Zinc-dependent metallopeptidase.' While the crystal structure (PDB 3SLU) contains Ni(2+), the physiological cofactor is annotated as Zn(2+). The expected answer D (Zn(2+)) is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the conserved HxxH motif (visible in 'HPILHT' region: H-P-I-L-H) characteristic of M23-family zinc metalloproteases. This motif is a well-established zinc-coordinating signature in peptidase biochemistry. Combined with the N-terminal signal peptide (suggesting a secreted/outer-membrane peptidoglycan-degrading enzyme in a Gram-negative bacterium), a knowledgeable model can identify this as a zinc metalloprotease. Tungstopterin (A) requires tungsten enzyme motifs (e.g., MGD tungstopterin-binding domains) absent here; Na(+) (B) is not a peptidase catalytic cofactor; Co(2+) (C) is not a recognized catalytic cofactor for peptidases. The HxxH→Zn(2+) inference is standard general biochemistry.


**Missing item-specific fact**

> None strictly required. The HxxH motif is general knowledge for metalloprotease families. However, confidently assigning this specific sequence to the M23 family (rather than another HxxH-containing family that might use a different metal) requires some familiarity with peptidase classification.


**Reason**

> The HxxH zinc-binding motif is a textbook feature of zinc metalloproteases. The elimination of tungstopterin (no tungsten enzyme architecture), Na+ (not a peptidase cofactor), and Co2+ (not a recognized peptidase cofactor) is achievable through general biological reasoning. The positive identification of Zn(2+) via the HxxH motif in a peptidase-like sequence constitutes a concrete biological argument distinguishable from memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the annotation notes Ni(2+) was found in the crystal structure and the metal is described as 'probably Zn(2+) in vivo,' Ni(2+) is not among the options. Among the four choices, Zn(2+) is the only divalent cation with established roles as a peptidase catalytic cofactor. Co(2+) is not a recognized peptidase cofactor, and the HxxH motif specifically coordinates zinc in metalloproteases. No genuine ambiguity exists among the provided options.


### Important caveats

- The crystal structure (PDB 3SLU) contains Ni(2+) rather than Zn(2+); the annotation qualifies Zn(2+) as 'probably' the physiological cofactor. This does not change the answer among the given options but introduces a minor evidential nuance.
- The HxxH motif identification relies on the model recognizing the specific sequence pattern 'HPILHT' as HxxH; a model that misses this pattern would default to lookup.
- The protein was integrated into Swiss-Prot on 2025-02-05 (entry version 53 current); the benchmark construction date is unknown, so the annotation may or may not have been available to the author at construction time.
- EC numbers (3.4.17.-, 3.4.24.-) are assigned by similarity (ECO:0000250 from Q5F676), not direct experiment, though the cofactor annotation itself carries experimental evidence (ECO:0000269).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conserved HxxH motif (visible in 'HPILHT' region: H-P-I-L-H) characteristic of M23-family zinc metalloproteases. This motif is a well-established zinc-coordinating signature in peptidase biochemistry. Combined with the N-terminal signal peptide (suggesting a secreted/outer-membrane peptidoglycan-degrading enzyme in a Gram-negative bacterium), a knowledgeable model can identify this as a zinc metalloprotease. Tungstopterin (A) requires tungsten enzyme motifs (e.g., MGD tungstopterin-binding domains) absent here; Na(+) (B) is not a peptidase catalytic cofactor; Co(2+) (C) is not a recognized catalytic cofactor for peptidases. The HxxH→Zn(2+) inference is standard general biochemistry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The HxxH motif is general knowledge for metalloprotease families. However, confidently assigning this specific sequence to the M23 family (rather than another HxxH-containing family that might use a different metal) requires some familiarity with peptidase classification.",
    "reason": "The HxxH zinc-binding motif is a textbook feature of zinc metalloproteases. The elimination of tungstopterin (no tungsten enzyme architecture), Na+ (not a peptidase cofactor), and Co2+ (not a recognized peptidase cofactor) is achievable through general biological reasoning. The positive identification of Zn(2+) via the HxxH motif in a peptidase-like sequence constitutes a concrete biological argument distinguishable from memorization."
  },
  "case_id": "cofactor_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt E0N688 (MPG_NEIM3) is annotated as a zinc-dependent metallopeptidase (DD-carboxypeptidase/endopeptidase Mpg) with cofactor Zn(2+) supported by experimental evidence (ECO:0000269, PubMed:22046377). The annotation states 'Binds 1 zinc ion per subunit. Binds a divalent metal cation, probably Zn(2+) in vivo.' The protein is explicitly named 'Zinc metallopeptidase' and 'Zinc-dependent metallopeptidase.' While the crystal structure (PDB 3SLU) contains Ni(2+), the physiological cofactor is annotated as Zn(2+). The expected answer D (Zn(2+)) is well-supported."
  },
  "important_caveats": [
    "The crystal structure (PDB 3SLU) contains Ni(2+) rather than Zn(2+); the annotation qualifies Zn(2+) as 'probably' the physiological cofactor. This does not change the answer among the given options but introduces a minor evidential nuance.",
    "The HxxH motif identification relies on the model recognizing the specific sequence pattern 'HPILHT' as HxxH; a model that misses this pattern would default to lookup.",
    "The protein was integrated into Swiss-Prot on 2025-02-05 (entry version 53 current); the benchmark construction date is unknown, so the annotation may or may not have been available to the author at construction time.",
    "EC numbers (3.4.17.-, 3.4.24.-) are assigned by similarity (ECO:0000250 from Q5F676), not direct experiment, though the cofactor annotation itself carries experimental evidence (ECO:0000269)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the annotation notes Ni(2+) was found in the crystal structure and the metal is described as 'probably Zn(2+) in vivo,' Ni(2+) is not among the options. Among the four choices, Zn(2+) is the only divalent cation with established roles as a peptidase catalytic cofactor. Co(2+) is not a recognized peptidase cofactor, and the HxxH motif specifically coordinates zinc in metalloproteases. No genuine ambiguity exists among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt E0N688 (MPG_NEIM3) is annotated as a zinc-dependent metallopeptidase (DD-carboxypeptidase/endopeptidase Mpg) with cofactor Zn(2+) supported by experimental evidence (ECO:0000269, PubMed:22046377). The annotation states 'Binds 1 zinc ion per subunit. Binds a divalent metal cation, probably Zn(2+) in vivo.' The protein is explicitly named 'Zinc metallopeptidase' and 'Zinc-dependent metallopeptidase.' While the crystal structure (PDB 3SLU) contains Ni(2+), the physiological cofactor is annotated as Zn(2+). The expected answer D (Zn(2+)) is well-supported.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the conserved HxxH motif (visible in 'HPILHT' region: H-P-I-L-H) characteristic of M23-family zinc metalloproteases. This motif is a well-established zinc-coordinating signature in peptidase biochemistry. Combined with the N-terminal signal peptide (suggesting a secreted/outer-membrane peptidoglycan-degrading enzyme in a Gram-negative bacterium), a knowledgeable model can identify this as a zinc metalloprotease. Tungstopterin (A) requires tungsten enzyme motifs (e.g., MGD tungstopterin-binding domains) absent here; Na(+) (B) is not a peptidase catalytic cofactor; Co(2+) (C) is not a recognized catalytic cofactor for peptidases. The HxxH→Zn(2+) inference is standard general biochemistry.",
    "missing_item_specific_fact": "None strictly required. The HxxH motif is general knowledge for metalloprotease families. However, confidently assigning this specific sequence to the M23 family (rather than another HxxH-containing family that might use a different metal) requires some familiarity with peptidase classification.",
    "reason": "The HxxH zinc-binding motif is a textbook feature of zinc metalloproteases. The elimination of tungstopterin (no tungsten enzyme architecture), Na+ (not a peptidase cofactor), and Co2+ (not a recognized peptidase cofactor) is achievable through general biological reasoning. The positive identification of Zn(2+) via the HxxH motif in a peptidase-like sequence constitutes a concrete biological argument distinguishable from memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the annotation notes Ni(2+) was found in the crystal structure and the metal is described as 'probably Zn(2+) in vivo,' Ni(2+) is not among the options. Among the four choices, Zn(2+) is the only divalent cation with established roles as a peptidase catalytic cofactor. Co(2+) is not a recognized peptidase cofactor, and the HxxH motif specifically coordinates zinc in metalloproteases. No genuine ambiguity exists among the provided options."
  },
  "important_caveats": [
    "The crystal structure (PDB 3SLU) contains Ni(2+) rather than Zn(2+); the annotation qualifies Zn(2+) as 'probably' the physiological cofactor. This does not change the answer among the given options but introduces a minor evidential nuance.",
    "The HxxH motif identification relies on the model recognizing the specific sequence pattern 'HPILHT' as HxxH; a model that misses this pattern would default to lookup.",
    "The protein was integrated into Swiss-Prot on 2025-02-05 (entry version 53 current); the benchmark construction date is unknown, so the annotation may or may not have been available to the author at construction time.",
    "EC numbers (3.4.17.-, 3.4.24.-) are assigned by similarity (ECO:0000250 from Q5F676), not direct experiment, though the cofactor annotation itself carries experimental evidence (ECO:0000269)."
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

**Accession:** `E0N688` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5F676","source":"UniProtKB"}],"value":"Metalloprotease active against peptidoglycan"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"value":"Outer membrane protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"value":"OMP"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Zinc metallopeptidase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Zinc metalloprotease"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"value":"Zinc-dependent metallopeptidase"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5F676","source":"UniProtKB"}],"value":"3.4.17.-"},{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5F676","source":"UniProtKB"}],"value":"3.4.24.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"DD-carboxypeptidase/endopeptidase Mpg"}}}
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000269","id":"22046377","source":"PubMed"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22046377","source":"PubMed"}],"value":"Binds 1 zinc ion per subunit. Binds a divalent metal cation, probably Zn(2+) in vivo, Ni(2+) ion is found in the crystal structure."}]}}
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
{"citation":{"authors":["Wang X.","Yang X.","Yang C.","Wu Z.","Xu H.","Shen Y."],"citationCrossReferences":[{"database":"PubMed","id":"22046377"},{"database":"DOI","id":"10.1371/journal.pone.0026845"}],"citationType":"journal article","firstPage":"e26845","id":"22046377","journal":"PLoS ONE","lastPage":"e26845","publicationDate":"2011","title":"Crystal structure of outer membrane protein NMB0315 from Neisseria meningitidis.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0007744","id":"3SLU","source":"PDB"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"type":"STRAIN","value":"ATCC 13091 / M2091"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.41 ANGSTROMS) OF 54-420 IN COMPLEX WITH NICKEL","COFACTOR","SUBUNIT","SUBCELLULAR LOCATION","PTM"]}
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)  
**Locator:** `lines 6-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:01.531640+00:00.  

```text
DE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};
DE            EC=3.4.17.- {ECO:0000250|UniProtKB:Q5F676};
DE            EC=3.4.24.- {ECO:0000250|UniProtKB:Q5F676};
DE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000250|UniProtKB:Q5F676};
DE   AltName: Full=Outer membrane protein {ECO:0000303|PubMed:22046377};
DE            Short=OMP {ECO:0000303|PubMed:22046377};
DE   AltName: Full=Zinc metallopeptidase {ECO:0000305};
DE   AltName: Full=Zinc metalloprotease {ECO:0000305};
DE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000303|PubMed:22046377};
DE   Flags: Precursor;
```

Source SHA-256: `6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)  
**Locator:** `lines 49-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:01.531640+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000269|PubMed:22046377};
CC       Note=Binds 1 zinc ion per subunit. Binds a divalent metal cation,
CC       probably Zn(2+) in vivo, Ni(2+) ion is found in the crystal structure.
CC       {ECO:0000269|PubMed:22046377};
```

Source SHA-256: `6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 90. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
