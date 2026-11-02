# cofactor_0082

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — pyridoxal 5&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKIDESLNVHSSLLQLIGNTPLLELHKITKGLKGRYFAKLEAFNVGHSAKDRVAKYIVEDAERKGLLKPGSTIVETSSGNTGYSLAMISALRGYRCIIAISDKSSHDKVEMLQALGAEVHLCPANVAPDDPRSYYEVAKRIHNETPNSIYVNQYFNPLNPESHYQTGREIWEQTQGEITHVVVCSGTGGTISGIAHYLKEQNPRVQVLGVDAYGSAIKKYHETREFDPAEVYPYKIEGIGKNLIPTATDFDVIDEFIKVTDKDAALMARKLARTEGLFMGYTSGAAIQAVKQYAEAGKFDENSIVVVLFADHGSRYMNKIYSDDWMKKQGFID

[Multiple Choices]
A. cob(II)alamin
B. pyridoxal 5'-phosphate
C. Fe(2+)
D. tungstopterin
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

> The supplied sequence exactly matches the reviewed cysteate synthase entry, which annotates pyridoxal 5'-phosphate as its cofactor with experimental evidence cited to PubMed 35414181.

Citations as saved: [H4](#evidence-h4), [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could support identifying a PLP-dependent enzyme with suitable family or homology information, but the input gives no protein function, organism, or family annotation that meaningfully distinguishes PLP from the listed alternatives.


**Missing item-specific fact**

> The sequence-specific identification as cysteate synthase and the experimentally supported PLP cofactor annotation are absent from the input.


**Reason**

> Selecting B depends on knowing or deriving this protein's particular identity and cofactor; generic sequence heuristics do not establish that fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports PLP, and the evidence provides no support for another listed option.


### Important caveats

- The annotation cites experimental evidence, but the cited primary paper was not independently retrieved or validated here.
- The reviewer-only accession and annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could support identifying a PLP-dependent enzyme with suitable family or homology information, but the input gives no protein function, organism, or family annotation that meaningfully distinguishes PLP from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific identification as cysteate synthase and the experimentally supported PLP cofactor annotation are absent from the input.",
    "reason": "Selecting B depends on knowing or deriving this protein's particular identity and cofactor; generic sequence heuristics do not establish that fact."
  },
  "case_id": "cofactor_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed cysteate synthase entry, which annotates pyridoxal 5'-phosphate as its cofactor with experimental evidence cited to PubMed 35414181."
  },
  "important_caveats": [
    "The annotation cites experimental evidence, but the cited primary paper was not independently retrieved or validated here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports PLP, and the evidence provides no support for another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed cysteate synthase entry, which annotates pyridoxal 5'-phosphate as its cofactor with experimental evidence cited to PubMed 35414181.",
    "evidence_ids": ["H4", "H3", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could support identifying a PLP-dependent enzyme with suitable family or homology information, but the input gives no protein function, organism, or family annotation that meaningfully distinguishes PLP from the listed alternatives.",
    "missing_item_specific_fact": "The sequence-specific identification as cysteate synthase and the experimentally supported PLP cofactor annotation are absent from the input.",
    "reason": "Selecting B depends on knowing or deriving this protein's particular identity and cofactor; generic sequence heuristics do not establish that fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports PLP, and the evidence provides no support for another listed option."
  },
  "important_caveats": [
    "The annotation cites experimental evidence, but the cited primary paper was not independently retrieved or validated here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C7M8J5 (sequence SHA256 matched) annotates the protein as Cysteate synthase (EC 2.5.1.76) with cofactor pyridoxal 5'-phosphate, supported by experimental evidence (ECO:0000269, PubMed:35414181). The sequence itself contains canonical PLP-binding motifs: 'SGNTGY' (the catalytic lysine region forming the internal aldimine with PLP in fold-type I enzymes) and 'CSGTGG' (characteristic of the serine acetyltransferase/cysteine synthase fold-type I family). The expected answer B is well-supported by both database annotation and sequence-level evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the well-known 'SGNTGY' motif (around residues 115-120), which is the canonical PLP-binding signature in fold-type I PLP-dependent enzymes where the lysine forms a Schiff base (internal aldimine) with pyridoxal 5'-phosphate. Additionally, the 'CSGTGGTISGIA' stretch is a hallmark of the fold-type I PLP enzyme superfamily (serine acetyltransferase/cysteine synthase family). These motifs are standard textbook biochemistry knowledge. The distractors can be eliminated by general reasoning: cob(II)alamin requires B12-dependent enzyme architectures (e.g., methylmalonyl-CoA mutase-type folds), Fe(2+) is associated with dioxygenases/hydroxylases lacking PLP motifs, and tungstopterin is found only in rare tungsten-containing oxidoreductases with entirely different sequence signatures.


**Missing item-specific fact**

> None critical. The PLP-binding motifs are directly readable from the supplied sequence and are general biochemical knowledge, not protein-specific annotations.


**Reason**

> A model with standard biochemistry knowledge can identify the SGNTGY and CSGTGG motifs as PLP-binding signatures of fold-type I enzymes and eliminate all three distractors based on their incompatible cofactor-enzyme architectures. The reasoning does not require knowing that this specific protein is 'cysteate synthase' or its EC number.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PLP-binding motifs are unambiguous in the sequence. Cob(II)alamin, Fe(2+), and tungstopterin are all incompatible with the observed fold-type I PLP enzyme architecture. No alternative answer is defensible.


### Important caveats

- The specific protein (cysteate synthase, EC 2.5.1.76) is relatively obscure, but the question tests cofactor identification from sequence motifs, not enzyme name recall.
- The experimental evidence (ECO:0000269) confirms the cofactor assignment, but the sequence-level reasoning is independently sufficient.
- The identity origin note states the accession was inferred mechanically from dataset metadata and was absent from the evaluated model input; however, this does not affect the reasoning path since the sequence itself carries the diagnostic motifs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the well-known 'SGNTGY' motif (around residues 115-120), which is the canonical PLP-binding signature in fold-type I PLP-dependent enzymes where the lysine forms a Schiff base (internal aldimine) with pyridoxal 5'-phosphate. Additionally, the 'CSGTGGTISGIA' stretch is a hallmark of the fold-type I PLP enzyme superfamily (serine acetyltransferase/cysteine synthase family). These motifs are standard textbook biochemistry knowledge. The distractors can be eliminated by general reasoning: cob(II)alamin requires B12-dependent enzyme architectures (e.g., methylmalonyl-CoA mutase-type folds), Fe(2+) is associated with dioxygenases/hydroxylases lacking PLP motifs, and tungstopterin is found only in rare tungsten-containing oxidoreductases with entirely different sequence signatures.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PLP-binding motifs are directly readable from the supplied sequence and are general biochemical knowledge, not protein-specific annotations.",
    "reason": "A model with standard biochemistry knowledge can identify the SGNTGY and CSGTGG motifs as PLP-binding signatures of fold-type I enzymes and eliminate all three distractors based on their incompatible cofactor-enzyme architectures. The reasoning does not require knowing that this specific protein is 'cysteate synthase' or its EC number."
  },
  "case_id": "cofactor_0082",
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
    "reason": "The UniProt entry C7M8J5 (sequence SHA256 matched) annotates the protein as Cysteate synthase (EC 2.5.1.76) with cofactor pyridoxal 5'-phosphate, supported by experimental evidence (ECO:0000269, PubMed:35414181). The sequence itself contains canonical PLP-binding motifs: 'SGNTGY' (the catalytic lysine region forming the internal aldimine with PLP in fold-type I enzymes) and 'CSGTGG' (characteristic of the serine acetyltransferase/cysteine synthase fold-type I family). The expected answer B is well-supported by both database annotation and sequence-level evidence."
  },
  "important_caveats": [
    "The specific protein (cysteate synthase, EC 2.5.1.76) is relatively obscure, but the question tests cofactor identification from sequence motifs, not enzyme name recall.",
    "The experimental evidence (ECO:0000269) confirms the cofactor assignment, but the sequence-level reasoning is independently sufficient.",
    "The identity origin note states the accession was inferred mechanically from dataset metadata and was absent from the evaluated model input; however, this does not affect the reasoning path since the sequence itself carries the diagnostic motifs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PLP-binding motifs are unambiguous in the sequence. Cob(II)alamin, Fe(2+), and tungstopterin are all incompatible with the observed fold-type I PLP enzyme architecture. No alternative answer is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C7M8J5 (sequence SHA256 matched) annotates the protein as Cysteate synthase (EC 2.5.1.76) with cofactor pyridoxal 5'-phosphate, supported by experimental evidence (ECO:0000269, PubMed:35414181). The sequence itself contains canonical PLP-binding motifs: 'SGNTGY' (the catalytic lysine region forming the internal aldimine with PLP in fold-type I enzymes) and 'CSGTGG' (characteristic of the serine acetyltransferase/cysteine synthase fold-type I family). The expected answer B is well-supported by both database annotation and sequence-level evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the well-known 'SGNTGY' motif (around residues 115-120), which is the canonical PLP-binding signature in fold-type I PLP-dependent enzymes where the lysine forms a Schiff base (internal aldimine) with pyridoxal 5'-phosphate. Additionally, the 'CSGTGGTISGIA' stretch is a hallmark of the fold-type I PLP enzyme superfamily (serine acetyltransferase/cysteine synthase family). These motifs are standard textbook biochemistry knowledge. The distractors can be eliminated by general reasoning: cob(II)alamin requires B12-dependent enzyme architectures (e.g., methylmalonyl-CoA mutase-type folds), Fe(2+) is associated with dioxygenases/hydroxylases lacking PLP motifs, and tungstopterin is found only in rare tungsten-containing oxidoreductases with entirely different sequence signatures.",
    "missing_item_specific_fact": "None critical. The PLP-binding motifs are directly readable from the supplied sequence and are general biochemical knowledge, not protein-specific annotations.",
    "reason": "A model with standard biochemistry knowledge can identify the SGNTGY and CSGTGG motifs as PLP-binding signatures of fold-type I enzymes and eliminate all three distractors based on their incompatible cofactor-enzyme architectures. The reasoning does not require knowing that this specific protein is 'cysteate synthase' or its EC number."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PLP-binding motifs are unambiguous in the sequence. Cob(II)alamin, Fe(2+), and tungstopterin are all incompatible with the observed fold-type I PLP enzyme architecture. No alternative answer is defensible."
  },
  "important_caveats": [
    "The specific protein (cysteate synthase, EC 2.5.1.76) is relatively obscure, but the question tests cofactor identification from sequence motifs, not enzyme name recall.",
    "The experimental evidence (ECO:0000269) confirms the cofactor assignment, but the sequence-level reasoning is independently sufficient.",
    "The identity origin note states the accession was inferred mechanically from dataset metadata and was absent from the evaluated model input; however, this does not affect the reasoning path since the sequence itself carries the diagnostic motifs."
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

**Accession:** `C7M8J5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 65. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.457032+00:00.  

```json
"C7M8J5"
```

Source SHA-256: `74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.457032+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35414181","source":"PubMed"}],"value":"2.5.1.76"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35414181","source":"PubMed"}],"value":"Cysteate synthase"}}}
```

Source SHA-256: `74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.457032+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:597326"},"evidences":[{"evidenceCode":"ECO:0000269","id":"35414181","source":"PubMed"}],"name":"pyridoxal 5'-phosphate"}],"commentType":"COFACTOR"}
```

Source SHA-256: `74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.457032+00:00.  

```json
{"citation":{"authors":["Liu Y.","Wei Y.","Teh T.M.","Liu D.","Zhou Y.","Zhao S.","Ang E.L.","Zhao H.","Zhang Y."],"citationCrossReferences":[{"database":"PubMed","id":"35414181"},{"database":"DOI","id":"10.1021/acs.biochem.2c00102"}],"citationType":"journal article","firstPage":"2861","id":"35414181","journal":"Biochemistry","lastPage":"2869","publicationDate":"2022","title":"Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine.","volume":"61"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF LYS-241"]}
```

Source SHA-256: `74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
ID   CAPA_CAPOD              Reviewed;         333 AA.
AC   C7M8J5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-OCT-2009, sequence version 1.
DT   28-JAN-2026, entry version 65.
DE   RecName: Full=Cysteate synthase {ECO:0000303|PubMed:35414181};
DE            EC=2.5.1.76 {ECO:0000269|PubMed:35414181};
GN   Name=capA {ECO:0000303|PubMed:35414181};
GN   OrderedLocusNames=Coch_1829 {ECO:0000312|EMBL:ACU93374.1};
OS   Capnocytophaga ochracea (strain ATCC 27872 / DSM 7271 / CCUG 9716 / JCM
OS   12966 / NCTC 12371 / SS31 / VPI 2845) (Bacteroides ochraceus).
OC   Bacteria; Pseudomonadati; Bacteroidota; Flavobacteriia; Flavobacteriales;
OC   Flavobacteriaceae; Capnocytophaga.
OX   NCBI_TaxID=521097;
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
DE   RecName: Full=Cysteate synthase {ECO:0000303|PubMed:35414181};
DE            EC=2.5.1.76 {ECO:0000269|PubMed:35414181};
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 29-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND
RP   MUTAGENESIS OF LYS-241.
RX   PubMed=35414181; DOI=10.1021/acs.biochem.2c00102;
RA   Liu Y., Wei Y., Teh T.M., Liu D., Zhou Y., Zhao S., Ang E.L., Zhao H.,
RA   Zhang Y.;
RT   "Identification and Characterization of the Biosynthetic Pathway of the
RT   Sulfonolipid Capnine.";
RL   Biochemistry 61:2861-2869(2022).
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 50-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;
CC         Evidence={ECO:0000269|PubMed:35414181};
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
