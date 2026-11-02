# EC_number_0053

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 2.7.13.3

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGLLLKMKMQNQHHPLASKLQEQTGNKRYTFIQAHRAWLLKLMFLWILLMALISRIIYSKMDVGTKVRRKEVLGSLCDQRARMLQDQFSVSVNHVHALAILVSTFHYYRNPSAIDQETFAEYTARTAFERPLLSGVAYAQRVVNSEREQFEKQHGVVIKTMEREASPVRDEYAPVIFAQETVSYLESIDMMSGEEDRENIMRARATGKAVLTSPFRLLGSHHLGVVLTFPVYKSKLPPNPTTEELIKATAGYVGGSFDVESLVENLLGQLAGHQAILVNVYDVTNSSDPLIMYGNQYEEGDVSLVHESKLDFGDPYRKHQMICRYHQKAPPNWTALSTAILFFVILLLIGYILYGAGNHIVKVEDDFHEMQELKVRAEAADVAKSQFLATVSHEIRTPMNGILGMLGLLLRTELNSTQRDYAQTAQACGKALIALINEVLDRAKIEAGKLELEAVPFDLRSILDDVLSLFSEKSRHKGLELAVFVSDKVPDIVMGDPGRFRQIVTNLVGNSVKFTERGHIFVKVHLSENRKPVTNGKHETYRNGGSEEVVHASGGYNLKTLSGYEAADERNNWDNFNHLIADEEFFCDASTKKVASNEFYEQVTLMVCVEDTGIGIPFSAQDRIFMPFVQADSSTSRNYGGTGIGLSISKCLVELMGGQINFISRPQVGSTFSFTADFGIFKKNPITEVKKVNYEDLPSSFRGLKAVVVDGKPVRAAVTRYHLKRLGIQVKVANAINKAVSLCGKNGASSTGLFQPDIIFVEKDSWVCGEDGIFSVRQLDWKQNGHIFKMPQMILLATNISNDEFDKAKSAGFSDTVIMKPLRASMVGACLQQVLGTGKKRQLGKEMPNGSTSVRSLLFGKKILVVDDNVVNRRVAAGALKNFGADVKCADSGKAALEMLQFPHKFDACFMDIQMPEMDGFEATRRIREMERTANEETNSECGERKSEFHLPILAMTADVIHATYEECLKCGMDGYVSKPFEEENLYQAVAKFFQTKPTSVDS

[Multiple Choices]
A. 2.7.13.3
B. 2.7.11.1
C. 5.6.2.4
D. 3.1.3.2
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

> The supplied sequence exactly matches the UniProt entry annotated as EC 2.7.13.3, with the catalytic activity annotation describing protein histidine phosphorylation. That annotation is transferred by similarity from Arabidopsis Q9C5U0, rather than direct experimental evidence for catalysis by this Medicago protein; the reported crystal structure does not by itself establish catalytic activity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a membrane receptor containing a histidine-kinase catalytic region and a receiver domain, the architecture of a hybrid histidine kinase. This distinguishes protein histidine kinase EC 2.7.13.3 from the serine/threonine kinase, isomerase, and phosphatase alternatives.


**Missing item-specific fact**

> No item-specific external fact is necessary to distinguish these listed classes, though confirming the precise protein annotation or its experimental activity would require external evidence.


**Reason**

> The sequence and choices provide a biologically meaningful route to the histidine-kinase class; this is not merely recognition of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the hybrid histidine-kinase interpretation supports A; the alternatives describe different catalytic classes.


### Important caveats

- The UniProt EC and catalytic-activity annotations are similarity-transferred from Q9C5U0, not direct evidence of enzymatic activity for this exact sequence.
- The reviewer-only source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a membrane receptor containing a histidine-kinase catalytic region and a receiver domain, the architecture of a hybrid histidine kinase. This distinguishes protein histidine kinase EC 2.7.13.3 from the serine/threonine kinase, isomerase, and phosphatase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific external fact is necessary to distinguish these listed classes, though confirming the precise protein annotation or its experimental activity would require external evidence.",
    "reason": "The sequence and choices provide a biologically meaningful route to the histidine-kinase class; this is not merely recognition of a database entry."
  },
  "case_id": "EC_number_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as EC 2.7.13.3, with the catalytic activity annotation describing protein histidine phosphorylation. That annotation is transferred by similarity from Arabidopsis Q9C5U0, rather than direct experimental evidence for catalysis by this Medicago protein; the reported crystal structure does not by itself establish catalytic activity."
  },
  "important_caveats": [
    "The UniProt EC and catalytic-activity annotations are similarity-transferred from Q9C5U0, not direct evidence of enzymatic activity for this exact sequence.",
    "The reviewer-only source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the hybrid histidine-kinase interpretation supports A; the alternatives describe different catalytic classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as EC 2.7.13.3, with the catalytic activity annotation describing protein histidine phosphorylation. That annotation is transferred by similarity from Arabidopsis Q9C5U0, rather than direct experimental evidence for catalysis by this Medicago protein; the reported crystal structure does not by itself establish catalytic activity.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a membrane receptor containing a histidine-kinase catalytic region and a receiver domain, the architecture of a hybrid histidine kinase. This distinguishes protein histidine kinase EC 2.7.13.3 from the serine/threonine kinase, isomerase, and phosphatase alternatives.",
    "missing_item_specific_fact": "No item-specific external fact is necessary to distinguish these listed classes, though confirming the precise protein annotation or its experimental activity would require external evidence.",
    "reason": "The sequence and choices provide a biologically meaningful route to the histidine-kinase class; this is not merely recognition of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the hybrid histidine-kinase interpretation supports A; the alternatives describe different catalytic classes."
  },
  "important_caveats": [
    "The UniProt EC and catalytic-activity annotations are similarity-transferred from Q9C5U0, not direct evidence of enzymatic activity for this exact sequence.",
    "The reviewer-only source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G7LCC3 (CRE1_MEDTR, Medicago truncatula) is annotated with EC 2.7.13.3 (histidine kinase). The catalytic activity is listed as ATP + protein L-histidine = ADP + protein N-phospho-L-histidine. However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity from UniProtKB:Q9C5U0, the Arabidopsis ortholog), not direct experimental measurement for this specific protein. A PDB structure (7P8E) confirms the receiver domain fold by X-ray crystallography, but does not directly demonstrate kinase catalysis. The annotation is consistent with the protein's identity as a cytokinin receptor histidine kinase.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a multi-domain architecture diagnostic of a two-component system histidine kinase: (1) an N-terminal transmembrane helix (hydrophobic stretch ~residues 15-45), (2) a kinase domain containing multiple conserved histidines in H-box-like contexts (e.g., 'HRAWLL', 'NHVHAL', 'SHHLGVVLTFP'), and (3) a C-terminal receiver domain with conserved Asp (e.g., 'VVEDTG', 'VDGKPVRAAVTRYHLKRLGIQVKVANAINKAVSLCGK'), Ser/Thr, and Lys motifs. The presence of a receiver domain is the strongest distinguishing feature: receiver domains accept phosphoryl groups from histidine kinases in two-component systems, not from Ser/Thr kinases (EC 2.7.11.1). This architecture excludes options B (Ser/Thr kinase), C (DNA helicase), and D (acid phosphatase), which lack receiver domains and do not feature His-rich kinase domains.


**Missing item-specific fact**

> None critical. Recognizing the specific conserved His in the H-box and the exact ATP-binding motifs (GxFS, N-box) requires domain expertise, but the overall TM+kinase+receiver architecture is sufficient to identify a two-component histidine kinase.


**Reason**

> The domain architecture (transmembrane sensor + histidine kinase + C-terminal receiver domain) provides a concrete, identifiable biological argument for EC 2.7.13.3 over the other three options. The receiver domain is a well-known structural hallmark of two-component systems that use histidine phosphoryl transfer, distinguishing this from Ser/Thr kinases, helicases, and phosphatases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span entirely different EC classes (transferase with His acceptor, transferase with Ser/Thr acceptor, isomerase/helicase, hydrolase). The receiver domain and His-rich kinase motifs unambiguously point to 2.7.13.3. No other option is defensible given the domain architecture.


### Important caveats

- The EC 2.7.13.3 annotation for G7LCC3 is based on similarity inference (ECO:0000250) from the Arabidopsis ortholog Q9C5U0, not on direct experimental kinetic characterization of this Medicago protein.
- The PDB structure 7P8E confirms the receiver domain fold (residues 351-994) by X-ray crystallography but does not demonstrate histidine kinase catalytic activity.
- Recognizing the receiver domain and histidine kinase motifs from sequence alone requires specialized knowledge of two-component signal transduction; this is domain-specific rather than general biological knowledge, but it constitutes a concrete structural/biological argument rather than pure lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a multi-domain architecture diagnostic of a two-component system histidine kinase: (1) an N-terminal transmembrane helix (hydrophobic stretch ~residues 15-45), (2) a kinase domain containing multiple conserved histidines in H-box-like contexts (e.g., 'HRAWLL', 'NHVHAL', 'SHHLGVVLTFP'), and (3) a C-terminal receiver domain with conserved Asp (e.g., 'VVEDTG', 'VDGKPVRAAVTRYHLKRLGIQVKVANAINKAVSLCGK'), Ser/Thr, and Lys motifs. The presence of a receiver domain is the strongest distinguishing feature: receiver domains accept phosphoryl groups from histidine kinases in two-component systems, not from Ser/Thr kinases (EC 2.7.11.1). This architecture excludes options B (Ser/Thr kinase), C (DNA helicase), and D (acid phosphatase), which lack receiver domains and do not feature His-rich kinase domains.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognizing the specific conserved His in the H-box and the exact ATP-binding motifs (GxFS, N-box) requires domain expertise, but the overall TM+kinase+receiver architecture is sufficient to identify a two-component histidine kinase.",
    "reason": "The domain architecture (transmembrane sensor + histidine kinase + C-terminal receiver domain) provides a concrete, identifiable biological argument for EC 2.7.13.3 over the other three options. The receiver domain is a well-known structural hallmark of two-component systems that use histidine phosphoryl transfer, distinguishing this from Ser/Thr kinases, helicases, and phosphatases."
  },
  "case_id": "EC_number_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G7LCC3 (CRE1_MEDTR, Medicago truncatula) is annotated with EC 2.7.13.3 (histidine kinase). The catalytic activity is listed as ATP + protein L-histidine = ADP + protein N-phospho-L-histidine. However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity from UniProtKB:Q9C5U0, the Arabidopsis ortholog), not direct experimental measurement for this specific protein. A PDB structure (7P8E) confirms the receiver domain fold by X-ray crystallography, but does not directly demonstrate kinase catalysis. The annotation is consistent with the protein's identity as a cytokinin receptor histidine kinase."
  },
  "important_caveats": [
    "The EC 2.7.13.3 annotation for G7LCC3 is based on similarity inference (ECO:0000250) from the Arabidopsis ortholog Q9C5U0, not on direct experimental kinetic characterization of this Medicago protein.",
    "The PDB structure 7P8E confirms the receiver domain fold (residues 351-994) by X-ray crystallography but does not demonstrate histidine kinase catalytic activity.",
    "Recognizing the receiver domain and histidine kinase motifs from sequence alone requires specialized knowledge of two-component signal transduction; this is domain-specific rather than general biological knowledge, but it constitutes a concrete structural/biological argument rather than pure lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different EC classes (transferase with His acceptor, transferase with Ser/Thr acceptor, isomerase/helicase, hydrolase). The receiver domain and His-rich kinase motifs unambiguously point to 2.7.13.3. No other option is defensible given the domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G7LCC3 (CRE1_MEDTR, Medicago truncatula) is annotated with EC 2.7.13.3 (histidine kinase). The catalytic activity is listed as ATP + protein L-histidine = ADP + protein N-phospho-L-histidine. However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity from UniProtKB:Q9C5U0, the Arabidopsis ortholog), not direct experimental measurement for this specific protein. A PDB structure (7P8E) confirms the receiver domain fold by X-ray crystallography, but does not directly demonstrate kinase catalysis. The annotation is consistent with the protein's identity as a cytokinin receptor histidine kinase.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a multi-domain architecture diagnostic of a two-component system histidine kinase: (1) an N-terminal transmembrane helix (hydrophobic stretch ~residues 15-45), (2) a kinase domain containing multiple conserved histidines in H-box-like contexts (e.g., 'HRAWLL', 'NHVHAL', 'SHHLGVVLTFP'), and (3) a C-terminal receiver domain with conserved Asp (e.g., 'VVEDTG', 'VDGKPVRAAVTRYHLKRLGIQVKVANAINKAVSLCGK'), Ser/Thr, and Lys motifs. The presence of a receiver domain is the strongest distinguishing feature: receiver domains accept phosphoryl groups from histidine kinases in two-component systems, not from Ser/Thr kinases (EC 2.7.11.1). This architecture excludes options B (Ser/Thr kinase), C (DNA helicase), and D (acid phosphatase), which lack receiver domains and do not feature His-rich kinase domains.",
    "missing_item_specific_fact": "None critical. Recognizing the specific conserved His in the H-box and the exact ATP-binding motifs (GxFS, N-box) requires domain expertise, but the overall TM+kinase+receiver architecture is sufficient to identify a two-component histidine kinase.",
    "reason": "The domain architecture (transmembrane sensor + histidine kinase + C-terminal receiver domain) provides a concrete, identifiable biological argument for EC 2.7.13.3 over the other three options. The receiver domain is a well-known structural hallmark of two-component systems that use histidine phosphoryl transfer, distinguishing this from Ser/Thr kinases, helicases, and phosphatases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different EC classes (transferase with His acceptor, transferase with Ser/Thr acceptor, isomerase/helicase, hydrolase). The receiver domain and His-rich kinase motifs unambiguously point to 2.7.13.3. No other option is defensible given the domain architecture."
  },
  "important_caveats": [
    "The EC 2.7.13.3 annotation for G7LCC3 is based on similarity inference (ECO:0000250) from the Arabidopsis ortholog Q9C5U0, not on direct experimental kinetic characterization of this Medicago protein.",
    "The PDB structure 7P8E confirms the receiver domain fold (residues 351-994) by X-ray crystallography but does not demonstrate histidine kinase catalytic activity.",
    "Recognizing the receiver domain and histidine kinase motifs from sequence alone requires specialized knowledge of two-component signal transduction; this is domain-specific rather than general biological knowledge, but it constitutes a concrete structural/biological argument rather than pure lookup."
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

**Accession:** `G7LCC3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 84. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.681318+00:00.  

```json
"G7LCC3"
```

Source SHA-256: `d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.681318+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34630499","source":"PubMed"}],"value":"Cytokinin receptor CYTOKININ RESPONSE 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34630499","source":"PubMed"}],"value":"Cytokinin receptor CRE1"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"34630499","source":"PubMed"}],"value":"MtCRE1"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9C5U0","source":"UniProtKB"}],"value":"2.7.13.3"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34630499","source":"PubMed"}],"value":"Histidine kinase CRE1"}}}
```

Source SHA-256: `d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.681318+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.13.3","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9C5U0","source":"UniProtKB"}],"name":"ATP + protein L-histidine = ADP + protein N-phospho-L-histidine."}}
```

Source SHA-256: `d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.681318+00:00.  

```json
{"citation":{"authors":["Tran L.H.","Urbanowicz A.","Jasinski M.","Jaskolski M.","Ruszkowski M."],"citationCrossReferences":[{"database":"PubMed","id":"34630499"},{"database":"DOI","id":"10.3389/fpls.2021.756341"}],"citationType":"journal article","firstPage":"756341","id":"34630499","journal":"Front. Plant Sci.","lastPage":"756341","publicationDate":"2021","title":"3D domain swapping dimerization of the receiver domain of cytokinin receptor CRE1 from Arabidopsis thaliana and Medicago truncatula.","volume":"12"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7P8E","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.50 ANGSTROMS) OF 351-994 IN COMPLEX WITH CA(2+)"]}
```

Source SHA-256: `d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7LCC3?format=txt&versions=84)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 2.  
**Retrieved:** 2026-11-01T06:28:06.918748+00:00.  

```text
DE   RecName: Full=Histidine kinase CRE1 {ECO:0000303|PubMed:34630499};
DE            EC=2.7.13.3 {ECO:0000250|UniProtKB:Q9C5U0};
DE   AltName: Full=Cytokinin receptor CYTOKININ RESPONSE 1 {ECO:0000303|PubMed:34630499};
DE            Short=Cytokinin receptor CRE1 {ECO:0000303|PubMed:34630499};
DE            Short=MtCRE1 {ECO:0000303|PubMed:34630499};
```

Source SHA-256: `026a53a56a232a58bac5538cce4d8ffd143200e6dd576544a82b544bfe64f8af`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7LCC3?format=txt&versions=84)  
**Locator:** `lines 85-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 2.  
**Retrieved:** 2026-11-01T06:28:06.918748+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP + protein L-histidine = ADP + protein N-phospho-L-
CC         histidine.; EC=2.7.13.3; Evidence={ECO:0000250|UniProtKB:Q9C5U0};
```

Source SHA-256: `026a53a56a232a58bac5538cce4d8ffd143200e6dd576544a82b544bfe64f8af`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 53. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
