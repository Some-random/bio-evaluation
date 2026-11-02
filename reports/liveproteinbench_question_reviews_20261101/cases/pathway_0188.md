# pathway_0188

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEIMNFSLNSPVFLLLSFFFLLMVLMQLTGSRKYKGKRLPPGPKKLPIIGNLHQMVGSLPHRVLKNLADQYGPVMHLQIGELSAIVISSADKAKEVLNTHGILVADRPQTTVAKIMLYNSLGATFAPYGDYLKQLRQIYALELLSPKTVRSFWTIMEDELSTMVTSVKAEAGQPIVLHDRMLTYLYATLCRATVGSVCNGRETLIMAAKETSALSAAIRIEDLFPSVKILPVVSGLRTRLTNLLKQLDTVLEDIIGEREKKMFSSNNIQPSTEEEDMLGVLLLYKNGKGKDTKFRITNNDIKAIIFELILAGTLSSSAIVEWCMSEMIKNPRVMKKAQDEVRQVLKDKKKVSGSDLAKLEYVKMVIKESVRLHPPAPLLFPREVREDFEMDGMIIPKKSWVIINYWAVGIDPKIWDDAERFEPERFSNSPIDFYGSHFELIPFGAGRRICPGILFGTTNVELLLASFLYHFDWKLPGGMKPEELDMNELFGAGCIRENPLCLIPSISVAGN

[Multiple Choices]
A. Protein modification
B. Alkaloid biosynthesis
C. dTTP biosynthesis. .
D. 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the UniProt entry annotated with the pathway “Alkaloid biosynthesis; ajmaline biosynthesis.” The annotation carries ECO:0000269 and cites a study whose stated subject is ajmaline biosynthesis, supporting choice B for this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a membrane-associated cytochrome P450, but that broad protein class does not establish a specific metabolic pathway or distinguish alkaloid biosynthesis from other possible P450 roles.


**Missing item-specific fact**

> The protein-specific link between this sequence (Sarpagan bridge enzyme 2) and ajmaline/alkaloid biosynthesis.


**Reason**

> Identifying the pathway requires an item-specific functional annotation or experimental finding not supplied in the question. Recognizing general P450 sequence features does not resolve the pathway choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched annotation supports B; the choices do not provide another comparably supported pathway for this protein.


### Important caveats

- The pathway annotation is database evidence, not information available to the evaluated model.
- The cited primary study was not independently reviewed here; the historical UniProt record attributes the pathway annotation to it.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a membrane-associated cytochrome P450, but that broad protein class does not establish a specific metabolic pathway or distinguish alkaloid biosynthesis from other possible P450 roles.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific link between this sequence (Sarpagan bridge enzyme 2) and ajmaline/alkaloid biosynthesis.",
    "reason": "Identifying the pathway requires an item-specific functional annotation or experimental finding not supplied in the question. Recognizing general P450 sequence features does not resolve the pathway choice."
  },
  "case_id": "pathway_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated with the pathway “Alkaloid biosynthesis; ajmaline biosynthesis.” The annotation carries ECO:0000269 and cites a study whose stated subject is ajmaline biosynthesis, supporting choice B for this protein."
  },
  "important_caveats": [
    "The pathway annotation is database evidence, not information available to the evaluated model.",
    "The cited primary study was not independently reviewed here; the historical UniProt record attributes the pathway annotation to it."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports B; the choices do not provide another comparably supported pathway for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated with the pathway “Alkaloid biosynthesis; ajmaline biosynthesis.” The annotation carries ECO:0000269 and cites a study whose stated subject is ajmaline biosynthesis, supporting choice B for this protein.",
    "evidence_ids": ["C5", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a membrane-associated cytochrome P450, but that broad protein class does not establish a specific metabolic pathway or distinguish alkaloid biosynthesis from other possible P450 roles.",
    "missing_item_specific_fact": "The protein-specific link between this sequence (Sarpagan bridge enzyme 2) and ajmaline/alkaloid biosynthesis.",
    "reason": "Identifying the pathway requires an item-specific functional annotation or experimental finding not supplied in the question. Recognizing general P450 sequence features does not resolve the pathway choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports B; the choices do not provide another comparably supported pathway for this protein."
  },
  "important_caveats": [
    "The pathway annotation is database evidence, not information available to the evaluated model.",
    "The cited primary study was not independently reviewed here; the historical UniProt record attributes the pathway annotation to it."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXJ2 (Sarpagan bridge enzyme 2, RsSBE2) from Rauvolfia serpentina is explicitly annotated with PATHWAY: 'Alkaloid biosynthesis; ajmaline biosynthesis' (ECO:0000269, experimental evidence from PubMed:38212296, Guo et al. Nat. Commun. 2024). Ajmaline is a terpenoid indole alkaloid, so the broader pathway category 'Alkaloid biosynthesis' is correct. The EC number 1.14.14.- (cytochrome P450 monooxygenase) is consistent with a P450 catalyzing a biosynthetic step in alkaloid production.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region contains the canonical cytochrome P450 heme-binding motif (FGAGRRICPGILFGTTNVELLLASFLYHFDWKLPGGMKPEELDMNELFGAGCIRENPLCLIPSISVAGN), with the critical FxxGxxxCxG signature. Cytochrome P450s are NOT the catalytic enzymes in protein modification (kinases/phosphatases), dTTP biosynthesis (thymidylate synthase, nucleotide kinases), or dihydrofolate synthesis (dihydropteroate synthase, folylpolyglutamate synthase). In contrast, P450s are the primary oxidoreductases in plant secondary-metabolite and alkaloid biosynthetic pathways. Thus, identifying the P450 signature from the sequence allows elimination of options A, C, and D, leaving B as the only pathway in which a P450 serves as the principal catalytic enzyme.


**Missing item-specific fact**

> None strictly required; the reasoning path from P450 identification to pathway elimination uses general enzymology and plant biochemistry knowledge rather than a protein-specific database lookup.


**Reason**

> A knowledgeable model can recognize the P450 heme-binding domain in the sequence and apply general knowledge that P450s catalyze oxidations in alkaloid/secondary-metabolite biosynthesis but are not the operative enzymes in protein modification, nucleotide biosynthesis, or folate synthesis. This provides a concrete, sequence-grounded biological argument that distinguishes option B from the distractors without memorizing this particular entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mechanistically distinct pathway types. A cytochrome P450 is not a plausible catalytic enzyme for protein modification, dTTP biosynthesis, or dihydrofolate synthesis. Only alkaloid biosynthesis is a pathway where P450s are the principal catalytic enzymes, so the sequence-derived P450 identification cleanly selects option B.


### Important caveats

- The UniProt annotation carries ECO:0000269 (experimental evidence) from a 2024 Nature Communications paper, lending strong support to the pathway assignment.
- The EC number is assigned by similarity (ECO:0000250, transferred from P0DO13), not experimentally determined for this specific enzyme, though the pathway comment itself is experimentally supported.
- The reasoning path relies on recognizing the P450 motif and knowing general catalytic roles; a model that fails to identify the P450 signature would lack the basis for elimination.
- The specific alkaloid (ajmaline) and the exact enzymatic step (sarpagan bridge formation) are not inferable from the sequence alone, but the broader pathway category 'Alkaloid biosynthesis' is reachable via P450-based reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains the canonical cytochrome P450 heme-binding motif (FGAGRRICPGILFGTTNVELLLASFLYHFDWKLPGGMKPEELDMNELFGAGCIRENPLCLIPSISVAGN), with the critical FxxGxxxCxG signature. Cytochrome P450s are NOT the catalytic enzymes in protein modification (kinases/phosphatases), dTTP biosynthesis (thymidylate synthase, nucleotide kinases), or dihydrofolate synthesis (dihydropteroate synthase, folylpolyglutamate synthase). In contrast, P450s are the primary oxidoreductases in plant secondary-metabolite and alkaloid biosynthetic pathways. Thus, identifying the P450 signature from the sequence allows elimination of options A, C, and D, leaving B as the only pathway in which a P450 serves as the principal catalytic enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; the reasoning path from P450 identification to pathway elimination uses general enzymology and plant biochemistry knowledge rather than a protein-specific database lookup.",
    "reason": "A knowledgeable model can recognize the P450 heme-binding domain in the sequence and apply general knowledge that P450s catalyze oxidations in alkaloid/secondary-metabolite biosynthesis but are not the operative enzymes in protein modification, nucleotide biosynthesis, or folate synthesis. This provides a concrete, sequence-grounded biological argument that distinguishes option B from the distractors without memorizing this particular entry's annotation."
  },
  "case_id": "pathway_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ2 (Sarpagan bridge enzyme 2, RsSBE2) from Rauvolfia serpentina is explicitly annotated with PATHWAY: 'Alkaloid biosynthesis; ajmaline biosynthesis' (ECO:0000269, experimental evidence from PubMed:38212296, Guo et al. Nat. Commun. 2024). Ajmaline is a terpenoid indole alkaloid, so the broader pathway category 'Alkaloid biosynthesis' is correct. The EC number 1.14.14.- (cytochrome P450 monooxygenase) is consistent with a P450 catalyzing a biosynthetic step in alkaloid production."
  },
  "important_caveats": [
    "The UniProt annotation carries ECO:0000269 (experimental evidence) from a 2024 Nature Communications paper, lending strong support to the pathway assignment.",
    "The EC number is assigned by similarity (ECO:0000250, transferred from P0DO13), not experimentally determined for this specific enzyme, though the pathway comment itself is experimentally supported.",
    "The reasoning path relies on recognizing the P450 motif and knowing general catalytic roles; a model that fails to identify the P450 signature would lack the basis for elimination.",
    "The specific alkaloid (ajmaline) and the exact enzymatic step (sarpagan bridge formation) are not inferable from the sequence alone, but the broader pathway category 'Alkaloid biosynthesis' is reachable via P450-based reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct pathway types. A cytochrome P450 is not a plausible catalytic enzyme for protein modification, dTTP biosynthesis, or dihydrofolate synthesis. Only alkaloid biosynthesis is a pathway where P450s are the principal catalytic enzymes, so the sequence-derived P450 identification cleanly selects option B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ2 (Sarpagan bridge enzyme 2, RsSBE2) from Rauvolfia serpentina is explicitly annotated with PATHWAY: 'Alkaloid biosynthesis; ajmaline biosynthesis' (ECO:0000269, experimental evidence from PubMed:38212296, Guo et al. Nat. Commun. 2024). Ajmaline is a terpenoid indole alkaloid, so the broader pathway category 'Alkaloid biosynthesis' is correct. The EC number 1.14.14.- (cytochrome P450 monooxygenase) is consistent with a P450 catalyzing a biosynthetic step in alkaloid production.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region contains the canonical cytochrome P450 heme-binding motif (FGAGRRICPGILFGTTNVELLLASFLYHFDWKLPGGMKPEELDMNELFGAGCIRENPLCLIPSISVAGN), with the critical FxxGxxxCxG signature. Cytochrome P450s are NOT the catalytic enzymes in protein modification (kinases/phosphatases), dTTP biosynthesis (thymidylate synthase, nucleotide kinases), or dihydrofolate synthesis (dihydropteroate synthase, folylpolyglutamate synthase). In contrast, P450s are the primary oxidoreductases in plant secondary-metabolite and alkaloid biosynthetic pathways. Thus, identifying the P450 signature from the sequence allows elimination of options A, C, and D, leaving B as the only pathway in which a P450 serves as the principal catalytic enzyme.",
    "missing_item_specific_fact": "None strictly required; the reasoning path from P450 identification to pathway elimination uses general enzymology and plant biochemistry knowledge rather than a protein-specific database lookup.",
    "reason": "A knowledgeable model can recognize the P450 heme-binding domain in the sequence and apply general knowledge that P450s catalyze oxidations in alkaloid/secondary-metabolite biosynthesis but are not the operative enzymes in protein modification, nucleotide biosynthesis, or folate synthesis. This provides a concrete, sequence-grounded biological argument that distinguishes option B from the distractors without memorizing this particular entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct pathway types. A cytochrome P450 is not a plausible catalytic enzyme for protein modification, dTTP biosynthesis, or dihydrofolate synthesis. Only alkaloid biosynthesis is a pathway where P450s are the principal catalytic enzymes, so the sequence-derived P450 identification cleanly selects option B."
  },
  "important_caveats": [
    "The UniProt annotation carries ECO:0000269 (experimental evidence) from a 2024 Nature Communications paper, lending strong support to the pathway assignment.",
    "The EC number is assigned by similarity (ECO:0000250, transferred from P0DO13), not experimentally determined for this specific enzyme, though the pathway comment itself is experimentally supported.",
    "The reasoning path relies on recognizing the P450 motif and knowing general catalytic roles; a model that fails to identify the P450 signature would lack the basis for elimination.",
    "The specific alkaloid (ajmaline) and the exact enzymatic step (sarpagan bridge formation) are not inferable from the sequence alone, but the broader pathway category 'Alkaloid biosynthesis' is reachable via P450-based reasoning."
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

**Accession:** `P0DXJ2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.229898+00:00.  

```json
"P0DXJ2"
```

Source SHA-256: `0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.229898+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cytochrome P450 SBE2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P0DO13","source":"UniProtKB"}],"value":"1.14.14.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Sarpagan bridge enzyme 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsSBE2"}]}}
```

Source SHA-256: `0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.229898+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.229898+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.434063+00:00.  

```text
ID   SBE2_RAUSE              Reviewed;         511 AA.
AC   P0DXJ2;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=Sarpagan bridge enzyme 2 {ECO:0000303|PubMed:38212296};
DE            Short=RsSBE2 {ECO:0000303|PubMed:38212296};
DE            EC=1.14.14.- {ECO:0000250|UniProtKB:P0DO13};
DE   AltName: Full=Cytochrome P450 SBE2 {ECO:0000305};
GN   Name=SBE2 {ECO:0000303|PubMed:38212296};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2)  
**Locator:** `lines 17-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.434063+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, PATHWAY, TISSUE SPECIFICITY, AND
RP   BIOTECHNOLOGY.
RX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;
RA   Guo J., Gao D., Lian J., Qu Y.;
RT   "De novo biosynthesis of antiarrhythmic alkaloid ajmaline.";
RL   Nat. Commun. 15:457-457(2024).
```

Source SHA-256: `e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2)  
**Locator:** `lines 69-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.434063+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 188. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
