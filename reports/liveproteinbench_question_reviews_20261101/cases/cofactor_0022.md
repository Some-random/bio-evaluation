# cofactor_0022

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Cu(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGDSSELNVRRSVRDLQAEYDRGNRKPLEDLIRAWKGIQELPPDDKRSFFILGGYHGEPFDYRNAVDALPPDDIYTYWGGWCNHGNVLFPTWHRIYILKLEEALQSIVPGVTLPFWDETSEETVKKGIPDVLTREYFELDGENIKNPLYSYTLPLSLSDNVPGDNKAYEKPAGYETVRYPLSGLVGTPEARAATAKHNAKYPNPIENTQLLNKNIIAWLHGSGKDEEGPTTTDPNPKGRGVKWMYEKCLSAPNYTVFSNTTSAGQWNLDHPAKSVVALEQPHNDVHLAVGGFDIPGQGESGQVADANGDMGENNTAALDPIFFFHHCNVDRMFWLWQKQNGFINKLEVITGYYGTNSSDSQGPTPGIPPGTPLDLNTPLNPFIKDEFGNPFTSMDCINIEEQLGYTYGPGSLDEVPKPEPITGGSTKKLTVRGINRGLFDGSFVIRAYASVPDAQGQLTEYYLGDHAVLSRRNVVKCANCLTHLEVIAHFPLDTLSADLVDKAEYWITIQHRGHSKRMKVDKDTGQSEKALLAQRAELPEKLKYSISVTD

[Multiple Choices]
A. Mo-bis(molybdopterin guanine dinucleotide)
B. heme b
C. NAD(+)
D. Cu(2+)
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

> The exact sequence matches the UniProt entry for tyrosinase HcTyr2, which annotates Cu(2+) as its cofactor and cites experimental evidence (ECO:0000269). The entry also notes two copper ions per subunit.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple histidine-rich regions consistent with the conserved copper-binding sites of tyrosinases. Tyrosinases are copper-dependent enzymes, which distinguishes Cu(2+) from the listed alternatives.


**Missing item-specific fact**

> The protein's annotated identity and direct experimental cofactor evidence are not provided in the question; however, the sequence offers a biologically meaningful family/cofactor inference.


**Reason**

> This is not merely an exact-sequence lookup: recognizing the tyrosinase-like copper-binding pattern supports Cu(2+) using general biochemical knowledge, although it may be challenging.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited cofactor annotation specifies Cu(2+); the sequence-based tyrosinase inference is consistent with that choice.


### Important caveats

- The reviewer-only database annotation and cited study were not supplied to the evaluated model.
- The primary paper was not independently retrieved or assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple histidine-rich regions consistent with the conserved copper-binding sites of tyrosinases. Tyrosinases are copper-dependent enzymes, which distinguishes Cu(2+) from the listed alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The protein's annotated identity and direct experimental cofactor evidence are not provided in the question; however, the sequence offers a biologically meaningful family/cofactor inference.",
    "reason": "This is not merely an exact-sequence lookup: recognizing the tyrosinase-like copper-binding pattern supports Cu(2+) using general biochemical knowledge, although it may be challenging."
  },
  "case_id": "cofactor_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for tyrosinase HcTyr2, which annotates Cu(2+) as its cofactor and cites experimental evidence (ECO:0000269). The entry also notes two copper ions per subunit."
  },
  "important_caveats": [
    "The reviewer-only database annotation and cited study were not supplied to the evaluated model.",
    "The primary paper was not independently retrieved or assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited cofactor annotation specifies Cu(2+); the sequence-based tyrosinase inference is consistent with that choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for tyrosinase HcTyr2, which annotates Cu(2+) as its cofactor and cites experimental evidence (ECO:0000269). The entry also notes two copper ions per subunit.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple histidine-rich regions consistent with the conserved copper-binding sites of tyrosinases. Tyrosinases are copper-dependent enzymes, which distinguishes Cu(2+) from the listed alternatives.",
    "missing_item_specific_fact": "The protein's annotated identity and direct experimental cofactor evidence are not provided in the question; however, the sequence offers a biologically meaningful family/cofactor inference.",
    "reason": "This is not merely an exact-sequence lookup: recognizing the tyrosinase-like copper-binding pattern supports Cu(2+) using general biochemical knowledge, although it may be challenging."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited cofactor annotation specifies Cu(2+); the sequence-based tyrosinase inference is consistent with that choice."
  },
  "important_caveats": [
    "The reviewer-only database annotation and cited study were not supplied to the evaluated model.",
    "The primary paper was not independently retrieved or assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A261GVB1 (Tyrosinase HcTyr2, EC 1.14.18.1, Hahella sp. CCB-MM4) explicitly annotates Cu(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed 39382070, 2024 FEBS Open Bio characterization paper). The note 'Binds 2 copper ions per subunit' is supported by similarity to Q9ZP19 (ECO:0000250). Tyrosinase EC 1.14.18.1 is a textbook copper-containing enzyme. The sequence matches exactly (SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the CANCL motif (residues ~'CANCLTHLEVIAHFPLDTL') and the HHCNVDRM motif, both of which are well-characterized copper-binding signatures in the tyrosinase/catechol oxidase/hemocyanin superfamily (type-3 dicopper center). These motifs are general metalloprotein knowledge, not specific to this protein. Additionally, the absence of CXXCH heme-binding motifs rules out heme b, the absence of a Rossmann-fold GxGxxG motif argues against NAD(+), and the absence of molybdopterin-binding motifs (e.g., conserved cysteine pairs in a molybdoenzyme context) argues against Mo-bis(MGD). A model with knowledge of common copper-binding sequence motifs could reasonably select Cu(2+).


**Missing item-specific fact**

> None strictly required; the CANCL and HHC motifs are general diagnostic features of copper-binding proteins in the tyrosinase superfamily, accessible through general biochemistry knowledge.


**Reason**

> While identifying the exact protein (Tyrosinase HcTyr2) would confirm the answer, the sequence itself carries recognizable copper-binding motifs (CANCL, HHC) that are general biological knowledge about metalloprotein architecture. The four options span very different cofactor classes, and the sequence features meaningfully distinguish Cu(2+) from the alternatives. This is not pure lookup; the motifs provide concrete, general grounds for the selection.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent structurally and functionally distinct cofactor classes (molybdoenzyme cofactor, heme, dinucleotide, metal ion). The CANCL/HHC copper-binding motifs in the sequence are inconsistent with heme (no CXXCH), NAD+ (no Rossmann fold), or molybdopterin (no Mo-binding cysteine pair in a molybdoenzyme scaffold). Cu(2+) is the only option consistent with the observed sequence features.


### Important caveats

- The COFACTOR annotation carries experimental evidence (ECO:0000269) from a 2024 paper, but the '2 copper ions per subunit' stoichiometry note is inferred by similarity (ECO:0000250) to Q9ZP19, not directly measured for this protein.
- The reviewer-only evidence was retrieved from the current UniProt snapshot (2026-03 release, entry version 19) and an archived version 18; the author's original source snapshot is unknown, though sequence match is confirmed.
- The CANCL motif recognition, while general knowledge, still requires the model to have encountered this motif in training data; a model unfamiliar with metalloprotein motifs might not identify it.
- The protein was only integrated into Swiss-Prot on 2025-02-05; if the benchmark was constructed before that date, the annotation may have been derived from TrEMBL or the primary literature directly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the CANCL motif (residues ~'CANCLTHLEVIAHFPLDTL') and the HHCNVDRM motif, both of which are well-characterized copper-binding signatures in the tyrosinase/catechol oxidase/hemocyanin superfamily (type-3 dicopper center). These motifs are general metalloprotein knowledge, not specific to this protein. Additionally, the absence of CXXCH heme-binding motifs rules out heme b, the absence of a Rossmann-fold GxGxxG motif argues against NAD(+), and the absence of molybdopterin-binding motifs (e.g., conserved cysteine pairs in a molybdoenzyme context) argues against Mo-bis(MGD). A model with knowledge of common copper-binding sequence motifs could reasonably select Cu(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; the CANCL and HHC motifs are general diagnostic features of copper-binding proteins in the tyrosinase superfamily, accessible through general biochemistry knowledge.",
    "reason": "While identifying the exact protein (Tyrosinase HcTyr2) would confirm the answer, the sequence itself carries recognizable copper-binding motifs (CANCL, HHC) that are general biological knowledge about metalloprotein architecture. The four options span very different cofactor classes, and the sequence features meaningfully distinguish Cu(2+) from the alternatives. This is not pure lookup; the motifs provide concrete, general grounds for the selection."
  },
  "case_id": "cofactor_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A261GVB1 (Tyrosinase HcTyr2, EC 1.14.18.1, Hahella sp. CCB-MM4) explicitly annotates Cu(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed 39382070, 2024 FEBS Open Bio characterization paper). The note 'Binds 2 copper ions per subunit' is supported by similarity to Q9ZP19 (ECO:0000250). Tyrosinase EC 1.14.18.1 is a textbook copper-containing enzyme. The sequence matches exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The COFACTOR annotation carries experimental evidence (ECO:0000269) from a 2024 paper, but the '2 copper ions per subunit' stoichiometry note is inferred by similarity (ECO:0000250) to Q9ZP19, not directly measured for this protein.",
    "The reviewer-only evidence was retrieved from the current UniProt snapshot (2026-03 release, entry version 19) and an archived version 18; the author's original source snapshot is unknown, though sequence match is confirmed.",
    "The CANCL motif recognition, while general knowledge, still requires the model to have encountered this motif in training data; a model unfamiliar with metalloprotein motifs might not identify it.",
    "The protein was only integrated into Swiss-Prot on 2025-02-05; if the benchmark was constructed before that date, the annotation may have been derived from TrEMBL or the primary literature directly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and functionally distinct cofactor classes (molybdoenzyme cofactor, heme, dinucleotide, metal ion). The CANCL/HHC copper-binding motifs in the sequence are inconsistent with heme (no CXXCH), NAD+ (no Rossmann fold), or molybdopterin (no Mo-binding cysteine pair in a molybdoenzyme scaffold). Cu(2+) is the only option consistent with the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A261GVB1 (Tyrosinase HcTyr2, EC 1.14.18.1, Hahella sp. CCB-MM4) explicitly annotates Cu(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed 39382070, 2024 FEBS Open Bio characterization paper). The note 'Binds 2 copper ions per subunit' is supported by similarity to Q9ZP19 (ECO:0000250). Tyrosinase EC 1.14.18.1 is a textbook copper-containing enzyme. The sequence matches exactly (SHA-256 confirmed).",
    "evidence_ids": ["C5", "C6", "H4", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the CANCL motif (residues ~'CANCLTHLEVIAHFPLDTL') and the HHCNVDRM motif, both of which are well-characterized copper-binding signatures in the tyrosinase/catechol oxidase/hemocyanin superfamily (type-3 dicopper center). These motifs are general metalloprotein knowledge, not specific to this protein. Additionally, the absence of CXXCH heme-binding motifs rules out heme b, the absence of a Rossmann-fold GxGxxG motif argues against NAD(+), and the absence of molybdopterin-binding motifs (e.g., conserved cysteine pairs in a molybdoenzyme context) argues against Mo-bis(MGD). A model with knowledge of common copper-binding sequence motifs could reasonably select Cu(2+).",
    "missing_item_specific_fact": "None strictly required; the CANCL and HHC motifs are general diagnostic features of copper-binding proteins in the tyrosinase superfamily, accessible through general biochemistry knowledge.",
    "reason": "While identifying the exact protein (Tyrosinase HcTyr2) would confirm the answer, the sequence itself carries recognizable copper-binding motifs (CANCL, HHC) that are general biological knowledge about metalloprotein architecture. The four options span very different cofactor classes, and the sequence features meaningfully distinguish Cu(2+) from the alternatives. This is not pure lookup; the motifs provide concrete, general grounds for the selection."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and functionally distinct cofactor classes (molybdoenzyme cofactor, heme, dinucleotide, metal ion). The CANCL/HHC copper-binding motifs in the sequence are inconsistent with heme (no CXXCH), NAD+ (no Rossmann fold), or molybdopterin (no Mo-binding cysteine pair in a molybdoenzyme scaffold). Cu(2+) is the only option consistent with the observed sequence features."
  },
  "important_caveats": [
    "The COFACTOR annotation carries experimental evidence (ECO:0000269) from a 2024 paper, but the '2 copper ions per subunit' stoichiometry note is inferred by similarity (ECO:0000250) to Q9ZP19, not directly measured for this protein.",
    "The reviewer-only evidence was retrieved from the current UniProt snapshot (2026-03 release, entry version 19) and an archived version 18; the author's original source snapshot is unknown, though sequence match is confirmed.",
    "The CANCL motif recognition, while general knowledge, still requires the model to have encountered this motif in training data; a model unfamiliar with metalloprotein motifs might not identify it.",
    "The protein was only integrated into Swiss-Prot on 2025-02-05; if the benchmark was constructed before that date, the annotation may have been derived from TrEMBL or the primary literature directly."
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

**Accession:** `A0A261GVB1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GVB1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.082570+00:00.  

```json
"A0A261GVB1"
```

Source SHA-256: `09d130bfdce053511ac8c67319a6b3e3b5ffbca8bcd3153677567a716e079201`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GVB1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.082570+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"value":"1.14.18.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39382070","source":"PubMed"}],"value":"Tyrosinase HcTyr2"}}}
```

Source SHA-256: `09d130bfdce053511ac8c67319a6b3e3b5ffbca8bcd3153677567a716e079201`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GVB1.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.082570+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29036"},"evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"name":"Cu(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9ZP19","source":"UniProtKB"}],"value":"Binds 2 copper ions per subunit."}]}}
```

Source SHA-256: `09d130bfdce053511ac8c67319a6b3e3b5ffbca8bcd3153677567a716e079201`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GVB1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.082570+00:00.  

```json
{"citation":{"authors":["de Almeida Santos G.","Englund A.N.B.","Dalleywater E.L.","Roehr A.K."],"citationCrossReferences":[{"database":"PubMed","id":"39382070"},{"database":"DOI","id":"10.1002/2211-5463.13906"}],"citationType":"journal article","firstPage":"0","id":"39382070","journal":"FEBS Open Bio","lastPage":"0","publicationDate":"2024","title":"Characterization of two bacterial tyrosinases from the halophilic bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in wetlands.","volume":"0"},"referenceComments":[{"type":"STRAIN","value":"CCB-MM4"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","DOMAIN","MUTAGENESIS OF 426-THR--ASP-550"]}
```

Source SHA-256: `09d130bfdce053511ac8c67319a6b3e3b5ffbca8bcd3153677567a716e079201`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GVB1?format=txt&versions=18)  
**Locator:** `lines 21-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-01T06:27:24.733923+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES,
RP   DOMAIN, AND MUTAGENESIS OF 426-THR--ASP-550.
RC   STRAIN=CCB-MM4;
RX   PubMed=39382070; DOI=10.1002/2211-5463.13906;
RA   de Almeida Santos G., Englund A.N.B., Dalleywater E.L., Roehr A.K.;
RT   "Characterization of two bacterial tyrosinases from the halophilic
RT   bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in
RT   wetlands.";
RL   FEBS Open Bio 0:0-0(2024).
```

Source SHA-256: `4c794a3cbf945cd4e479d9430b2d9c1e3d32924055d9812812fc36602c8f48b9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GVB1?format=txt&versions=18)  
**Locator:** `lines 51-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-01T06:27:24.733923+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Cu(2+); Xref=ChEBI:CHEBI:29036;
CC         Evidence={ECO:0000269|PubMed:39382070};
CC       Note=Binds 2 copper ions per subunit. {ECO:0000250|UniProtKB:Q9ZP19};
```

Source SHA-256: `4c794a3cbf945cd4e479d9430b2d9c1e3d32924055d9812812fc36602c8f48b9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 22. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
