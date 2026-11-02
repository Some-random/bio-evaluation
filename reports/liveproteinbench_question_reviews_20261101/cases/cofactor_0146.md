# cofactor_0146

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVFPLSAKHRKYALRALAVSIILVSAAYIASTEGTERVRPQRVEQKLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGSAREVQFFTDEDGERNLVALEKKGGIWRRSASDADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLLYDSLYFHGQQVAAGDILAAEVVKGGTTHQAFYYRSDKEGGGGGNYYDEDGRVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAQGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. pantetheine 4'-phosphate
B. Zn(2+)
C. Mo-bis(molybdopterin guanine dinucleotide)
D. Na(+)
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

> The exact sequence matches the annotated Neisseria gonorrhoeae Mpg protein. UniProt annotates Zn(2+) as its cofactor and says it binds one zinc ion per subunit; the cofactor evidence is transferred by similarity (ECO:0000250), not a direct measurement established here for this exact protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C4](#evidence-c4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A zinc metalloprotease would use Zn(2+), but identifying this sequence as that particular metalloprotease requires recognizing its protein family or obtaining its annotation; the input supplies no function or organism context.


**Missing item-specific fact**

> The protein-specific identity/function and its zinc-cofactor annotation are absent from the question.


**Reason**

> The sequence alone does not provide an unambiguous, readily interpretable basis for identifying the enzyme family and its cofactor. Remembering or retrieving the exact sequence's annotation would distinguish the options, but that is lookup or memorization rather than reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports Zn(2+); the other listed options are not supported by the supplied reviewer evidence.


### Important caveats

- The cofactor annotation is similarity-transferred; the evidence excerpts do not establish a direct zinc-binding experiment on this exact protein.
- The reviewer-only accession and annotations were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A zinc metalloprotease would use Zn(2+), but identifying this sequence as that particular metalloprotease requires recognizing its protein family or obtaining its annotation; the input supplies no function or organism context.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity/function and its zinc-cofactor annotation are absent from the question.",
    "reason": "The sequence alone does not provide an unambiguous, readily interpretable basis for identifying the enzyme family and its cofactor. Remembering or retrieving the exact sequence's annotation would distinguish the options, but that is lookup or memorization rather than reasoning from supplied context."
  },
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Neisseria gonorrhoeae Mpg protein. UniProt annotates Zn(2+) as its cofactor and says it binds one zinc ion per subunit; the cofactor evidence is transferred by similarity (ECO:0000250), not a direct measurement established here for this exact protein."
  },
  "important_caveats": [
    "The cofactor annotation is similarity-transferred; the evidence excerpts do not establish a direct zinc-binding experiment on this exact protein.",
    "The reviewer-only accession and annotations were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports Zn(2+); the other listed options are not supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Neisseria gonorrhoeae Mpg protein. UniProt annotates Zn(2+) as its cofactor and says it binds one zinc ion per subunit; the cofactor evidence is transferred by similarity (ECO:0000250), not a direct measurement established here for this exact protein.",
    "evidence_ids": ["C1", "C5", "C4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A zinc metalloprotease would use Zn(2+), but identifying this sequence as that particular metalloprotease requires recognizing its protein family or obtaining its annotation; the input supplies no function or organism context.",
    "missing_item_specific_fact": "The protein-specific identity/function and its zinc-cofactor annotation are absent from the question.",
    "reason": "The sequence alone does not provide an unambiguous, readily interpretable basis for identifying the enzyme family and its cofactor. Remembering or retrieving the exact sequence's annotation would distinguish the options, but that is lookup or memorization rather than reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports Zn(2+); the other listed options are not supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The cofactor annotation is similarity-transferred; the evidence excerpts do not establish a direct zinc-binding experiment on this exact protein.",
    "The reviewer-only accession and annotations were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5F676 explicitly annotates Zn(2+) as the cofactor (CHEBI:29105, 'Binds 1 zinc ion per subunit'). The protein is named 'Zinc metallopeptidase'/'Zinc metalloprotease' with EC 3.4.24.- (metalloendopeptidase). The M23B family designation (PubMed:22334697) and mutagenesis of His-295, Asp-299, His-373, His-375 confirm zinc coordination. The cofactor annotation itself uses ECO:0000250 (similarity to E0N688), but the referenced experimental work on the M23B family and the His/Asp/H/H mutagenesis data provide strong indirect experimental support. The His-rich motif (HANGVETLYAHLSAF...GPHLHYEARING) visible in the sequence is consistent with the M23 zinc-binding architecture.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence contains a conserved His-Asp-His-His cluster (HANGVETLYAHLSAF...GPHLHYEARING) characteristic of the M23-family zinc-binding site. A model with general metalloenzyme knowledge can recognize this His cluster as a metal-coordination motif. Additionally, the N-terminal hydrophobic signal peptide suggests a secreted/exported protein, and many exported peptidases (especially those acting on peptidoglycan) are zinc-dependent. The other three options are cofactors for entirely different enzyme classes: pantetheine 4'-phosphate for acyl-transfer reactions, Mo-bis-MGD for molybdenum oxidoreductases, and Na+ is not a recognized catalytic cofactor for peptidases. Eliminating these leaves Zn(2+) as the only chemically plausible cofactor for a peptidase.


**Missing item-specific fact**

> None strictly required. Identifying the exact M23B family assignment would benefit from database lookup, but the His/Asp zinc-binding motif is visible in the sequence and general knowledge of metallopeptidase cofactor requirements suffices to select Zn(2+) over the other options.


**Reason**

> The zinc-binding His cluster is present in the supplied sequence and recognizable through pattern recognition. The elimination of pantetheine, Mo-bis-MGD, and Na+ relies on general knowledge of which enzyme classes use those cofactors. A model need not know the specific protein name to reason that a peptidase-like domain with a His/Asp cluster requires zinc.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (pantetheine 4'-phosphate, Mo-bis-MGD, Na+) are cofactors for acyltransferases, molybdenum oxidoreductases, and non-enzymatic/transport roles respectively—none are associated with peptidase catalysis. Zn(2+) is the only cofactor consistent with a metallopeptidase. No ambiguity exists.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to E0N688), not direct experimental determination on this protein. However, the M23B family is well-established as zinc-dependent, and the mutagenesis data on the His/Asp residues (PubMed:22334697) provide strong experimental corroboration.
- The protein was only integrated into Swiss-Prot in February 2025; at the time of benchmark construction, the author may have relied on TrEMBL annotation or literature rather than a curated Swiss-Prot entry.
- The sequence-match between the benchmark input and UniProt Q5F676 is confirmed (430 aa, SHA-256 match).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a conserved His-Asp-His-His cluster (HANGVETLYAHLSAF...GPHLHYEARING) characteristic of the M23-family zinc-binding site. A model with general metalloenzyme knowledge can recognize this His cluster as a metal-coordination motif. Additionally, the N-terminal hydrophobic signal peptide suggests a secreted/exported protein, and many exported peptidases (especially those acting on peptidoglycan) are zinc-dependent. The other three options are cofactors for entirely different enzyme classes: pantetheine 4'-phosphate for acyl-transfer reactions, Mo-bis-MGD for molybdenum oxidoreductases, and Na+ is not a recognized catalytic cofactor for peptidases. Eliminating these leaves Zn(2+) as the only chemically plausible cofactor for a peptidase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Identifying the exact M23B family assignment would benefit from database lookup, but the His/Asp zinc-binding motif is visible in the sequence and general knowledge of metallopeptidase cofactor requirements suffices to select Zn(2+) over the other options.",
    "reason": "The zinc-binding His cluster is present in the supplied sequence and recognizable through pattern recognition. The elimination of pantetheine, Mo-bis-MGD, and Na+ relies on general knowledge of which enzyme classes use those cofactors. A model need not know the specific protein name to reason that a peptidase-like domain with a His/Asp cluster requires zinc."
  },
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5F676 explicitly annotates Zn(2+) as the cofactor (CHEBI:29105, 'Binds 1 zinc ion per subunit'). The protein is named 'Zinc metallopeptidase'/'Zinc metalloprotease' with EC 3.4.24.- (metalloendopeptidase). The M23B family designation (PubMed:22334697) and mutagenesis of His-295, Asp-299, His-373, His-375 confirm zinc coordination. The cofactor annotation itself uses ECO:0000250 (similarity to E0N688), but the referenced experimental work on the M23B family and the His/Asp/H/H mutagenesis data provide strong indirect experimental support. The His-rich motif (HANGVETLYAHLSAF...GPHLHYEARING) visible in the sequence is consistent with the M23 zinc-binding architecture."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to E0N688), not direct experimental determination on this protein. However, the M23B family is well-established as zinc-dependent, and the mutagenesis data on the His/Asp residues (PubMed:22334697) provide strong experimental corroboration.",
    "The protein was only integrated into Swiss-Prot in February 2025; at the time of benchmark construction, the author may have relied on TrEMBL annotation or literature rather than a curated Swiss-Prot entry.",
    "The sequence-match between the benchmark input and UniProt Q5F676 is confirmed (430 aa, SHA-256 match)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (pantetheine 4'-phosphate, Mo-bis-MGD, Na+) are cofactors for acyltransferases, molybdenum oxidoreductases, and non-enzymatic/transport roles respectively—none are associated with peptidase catalysis. Zn(2+) is the only cofactor consistent with a metallopeptidase. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5F676 explicitly annotates Zn(2+) as the cofactor (CHEBI:29105, 'Binds 1 zinc ion per subunit'). The protein is named 'Zinc metallopeptidase'/'Zinc metalloprotease' with EC 3.4.24.- (metalloendopeptidase). The M23B family designation (PubMed:22334697) and mutagenesis of His-295, Asp-299, His-373, His-375 confirm zinc coordination. The cofactor annotation itself uses ECO:0000250 (similarity to E0N688), but the referenced experimental work on the M23B family and the His/Asp/H/H mutagenesis data provide strong indirect experimental support. The His-rich motif (HANGVETLYAHLSAF...GPHLHYEARING) visible in the sequence is consistent with the M23 zinc-binding architecture.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a conserved His-Asp-His-His cluster (HANGVETLYAHLSAF...GPHLHYEARING) characteristic of the M23-family zinc-binding site. A model with general metalloenzyme knowledge can recognize this His cluster as a metal-coordination motif. Additionally, the N-terminal hydrophobic signal peptide suggests a secreted/exported protein, and many exported peptidases (especially those acting on peptidoglycan) are zinc-dependent. The other three options are cofactors for entirely different enzyme classes: pantetheine 4'-phosphate for acyl-transfer reactions, Mo-bis-MGD for molybdenum oxidoreductases, and Na+ is not a recognized catalytic cofactor for peptidases. Eliminating these leaves Zn(2+) as the only chemically plausible cofactor for a peptidase.",
    "missing_item_specific_fact": "None strictly required. Identifying the exact M23B family assignment would benefit from database lookup, but the His/Asp zinc-binding motif is visible in the sequence and general knowledge of metallopeptidase cofactor requirements suffices to select Zn(2+) over the other options.",
    "reason": "The zinc-binding His cluster is present in the supplied sequence and recognizable through pattern recognition. The elimination of pantetheine, Mo-bis-MGD, and Na+ relies on general knowledge of which enzyme classes use those cofactors. A model need not know the specific protein name to reason that a peptidase-like domain with a His/Asp cluster requires zinc."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (pantetheine 4'-phosphate, Mo-bis-MGD, Na+) are cofactors for acyltransferases, molybdenum oxidoreductases, and non-enzymatic/transport roles respectively—none are associated with peptidase catalysis. Zn(2+) is the only cofactor consistent with a metallopeptidase. No ambiguity exists."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to E0N688), not direct experimental determination on this protein. However, the M23B family is well-established as zinc-dependent, and the mutagenesis data on the His/Asp residues (PubMed:22334697) provide strong experimental corroboration.",
    "The protein was only integrated into Swiss-Prot in February 2025; at the time of benchmark construction, the author may have relied on TrEMBL annotation or literature rather than a curated Swiss-Prot entry.",
    "The sequence-match between the benchmark input and UniProt Q5F676 is confirmed (430 aa, SHA-256 match)."
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

**Accession:** `Q5F676` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 88. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:11.230902+00:00.  

```json
"Q5F676"
```

Source SHA-256: `fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:11.230902+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23839218","source":"PubMed"}],"value":"Metalloprotease NGO1686"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23839218","source":"PubMed"}],"value":"Metalloprotease active against peptidoglycan"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Outer membrane protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"OMP"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22334697","source":"PubMed"}],"value":"Virulence factor NG1686"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22334697","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"23839218","source":"PubMed"}],"value":"Zinc metallopeptidase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16194237","source":"PubMed"}],"value":"Zinc metalloprotease"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Zinc-dependent metallopeptidase"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22334697","source":"PubMed"}],"value":"3.4.17.-"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"22334697","source":"PubMed"}],"value":"3.4.24.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"DD-carboxypeptidase/endopeptidase Mpg"}}}
```

Source SHA-256: `fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:11.230902+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000250","id":"E0N688","source":"UniProtKB"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"E0N688","source":"UniProtKB"}],"value":"Binds 1 zinc ion per subunit."}]}}
```

Source SHA-256: `fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:11.230902+00:00.  

```json
{"citation":{"authors":["Stohl E.A.","Chan Y.A.","Hackett K.T.","Kohler P.L.","Dillard J.P.","Seifert H.S."],"citationCrossReferences":[{"database":"PubMed","id":"22334697"},{"database":"DOI","id":"10.1074/jbc.m111.338830"}],"citationType":"journal article","firstPage":"11222","id":"22334697","journal":"J. Biol. Chem.","lastPage":"11233","publicationDate":"2012","title":"Neisseria gonorrhoeae virulence factor NG1686 is a bifunctional M23B family metallopeptidase that influences resistance to hydrogen peroxide and colony morphology.","volume":"287"},"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22334697","source":"PubMed"}],"type":"STRAIN","value":"ATCC 700825 / FA 1090"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","DISRUPTION PHENOTYPE","MUTAGENESIS OF HIS-295; ASP-299; HIS-373 AND HIS-375"]}
```

Source SHA-256: `fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)  
**Locator:** `lines 6-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 88 / 1.  
**Retrieved:** 2026-11-02T04:31:15.062188+00:00.  

```text
DE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};
DE            EC=3.4.17.- {ECO:0000269|PubMed:22334697};
DE            EC=3.4.24.- {ECO:0000269|PubMed:22334697};
DE   AltName: Full=Metalloprotease NGO1686 {ECO:0000303|PubMed:23839218};
DE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000303|PubMed:23839218};
DE   AltName: Full=Outer membrane protein {ECO:0000305};
DE            Short=OMP {ECO:0000305};
DE   AltName: Full=Virulence factor NG1686 {ECO:0000303|PubMed:22334697};
DE   AltName: Full=Zinc metallopeptidase {ECO:0000303|PubMed:22334697, ECO:0000303|PubMed:23839218};
DE   AltName: Full=Zinc metalloprotease {ECO:0000303|PubMed:16194237};
DE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000305};
DE   Flags: Precursor;
```

Source SHA-256: `1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)  
**Locator:** `lines 50-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 88 / 1.  
**Retrieved:** 2026-11-02T04:31:15.062188+00:00.  

```text
RN   [4]
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, DISRUPTION PHENOTYPE,
RP   AND MUTAGENESIS OF HIS-295; ASP-299; HIS-373 AND HIS-375.
RC   STRAIN=ATCC 700825 / FA 1090 {ECO:0000303|PubMed:22334697};
RX   PubMed=22334697; DOI=10.1074/jbc.m111.338830;
RA   Stohl E.A., Chan Y.A., Hackett K.T., Kohler P.L., Dillard J.P.,
RA   Seifert H.S.;
RT   "Neisseria gonorrhoeae virulence factor NG1686 is a bifunctional M23B
RT   family metallopeptidase that influences resistance to hydrogen peroxide and
RT   colony morphology.";
RL   J. Biol. Chem. 287:11222-11233(2012).
```

Source SHA-256: `1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)  
**Locator:** `lines 96-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 88 / 1.  
**Retrieved:** 2026-11-02T04:31:15.062188+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000250|UniProtKB:E0N688};
CC       Note=Binds 1 zinc ion per subunit. {ECO:0000250|UniProtKB:E0N688};
```

Source SHA-256: `1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
