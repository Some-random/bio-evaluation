# catalytic_activity_0160

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAEFVRAQIFGTTFEITSRYTELAPVGMGAFGLVCSAKDQLTNQAVAVKKIMKPFSTPVLSKRTYRELKLLKHLRHENVISLSDIFISPLEDIYFVTELLGTDLHRLLTSRPLEKQFIQYFLYQILRGLKYVHSAGVVHRDLKPSNILVNENCDLKICDFGLARIQDPQMTGYVSTRYYRAPEIMLTWQKYDVEVDIWSVGCIFAEMLEGKPLFPGKDHVNQFSIITELLGTPPDDVIQTICSENTLRFVQSLPKRERQPLTKKFKNADPQAIELLERMLVFDPRTRIRAGDALADPYLAPYHDPTDEPEAEEKFDWSFNDADLPVDTWKIMMYSEILDYHNVDAQNGEEVGVPQ

[Multiple Choices]
A. (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH
B. 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O
C. L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)
D. Cs(+)(in) = Cs(+)(out)
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

> The exact sequence matches a HOG1 MAP kinase. UniProt annotates it with the serine-phosphorylation reaction in C, but the cited evidence transfers the annotation by similarity from P32485 (ECO:0000250), rather than documenting a direct assay of this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a protein-kinase catalytic domain, including the characteristic HRD catalytic-loop and DFG motifs. That supports ATP-dependent protein phosphorylation, distinguishing C from the alkaloid oxidation, polyketide synthesis, and ion-transport choices.


**Missing item-specific fact**

> No item-specific fact is needed to distinguish C among these choices. Establishing this protein's exact physiological substrate sites or experimentally measured specificity would require additional evidence.


**Reason**

> The sequence and options provide a meaningful family-level biological basis for selecting protein phosphorylation. The annotation supports the exact serine reaction, while its evidence is similarity-based rather than direct experimental verification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is the only option consistent with a protein kinase. MAP kinases can phosphorylate both serine and threonine, but the options do not offer a competing threonine-phosphorylation reaction.


### Important caveats

- The cited UniProt catalytic-activity annotations are inferred by similarity to P32485; they should not be represented as direct experimental evidence for this sequence.
- The sequence match and accession identification come from reviewer-only evidence, not information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a protein-kinase catalytic domain, including the characteristic HRD catalytic-loop and DFG motifs. That supports ATP-dependent protein phosphorylation, distinguishing C from the alkaloid oxidation, polyketide synthesis, and ion-transport choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is needed to distinguish C among these choices. Establishing this protein's exact physiological substrate sites or experimentally measured specificity would require additional evidence.",
    "reason": "The sequence and options provide a meaningful family-level biological basis for selecting protein phosphorylation. The annotation supports the exact serine reaction, while its evidence is similarity-based rather than direct experimental verification."
  },
  "case_id": "catalytic_activity_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a HOG1 MAP kinase. UniProt annotates it with the serine-phosphorylation reaction in C, but the cited evidence transfers the annotation by similarity from P32485 (ECO:0000250), rather than documenting a direct assay of this protein."
  },
  "important_caveats": [
    "The cited UniProt catalytic-activity annotations are inferred by similarity to P32485; they should not be represented as direct experimental evidence for this sequence.",
    "The sequence match and accession identification come from reviewer-only evidence, not information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the only option consistent with a protein kinase. MAP kinases can phosphorylate both serine and threonine, but the options do not offer a competing threonine-phosphorylation reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a HOG1 MAP kinase. UniProt annotates it with the serine-phosphorylation reaction in C, but the cited evidence transfers the annotation by similarity from P32485 (ECO:0000250), rather than documenting a direct assay of this protein.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a protein-kinase catalytic domain, including the characteristic HRD catalytic-loop and DFG motifs. That supports ATP-dependent protein phosphorylation, distinguishing C from the alkaloid oxidation, polyketide synthesis, and ion-transport choices.",
    "missing_item_specific_fact": "No item-specific fact is needed to distinguish C among these choices. Establishing this protein's exact physiological substrate sites or experimentally measured specificity would require additional evidence.",
    "reason": "The sequence and options provide a meaningful family-level biological basis for selecting protein phosphorylation. The annotation supports the exact serine reaction, while its evidence is similarity-based rather than direct experimental verification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the only option consistent with a protein kinase. MAP kinases can phosphorylate both serine and threonine, but the options do not offer a competing threonine-phosphorylation reaction."
  },
  "important_caveats": [
    "The cited UniProt catalytic-activity annotations are inferred by similarity to P32485; they should not be represented as direct experimental evidence for this sequence.",
    "The sequence match and accession identification come from reviewer-only evidence, not information supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A5B9GBF0 (HOG1_AURME), annotated as Mitogen-activated protein kinase HOG1 with EC 2.7.11.24. The listed catalytic activity is exactly 'L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)'. The evidence code is ECO:0000250 (inferred by similarity from P32485, yeast HOG1), so this is computational/similarity-based annotation rather than direct experimental measurement on this specific protein, but the sequence clearly exhibits canonical protein kinase domain architecture, making the annotation well-founded.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable protein kinase structural motifs identifiable by general biological knowledge: (1) a glycine-rich loop 'GAFGLV' near the N-terminus (GxGxxG-like), (2) the catalytic HRD motif 'HRDLKPSN', (3) the DFG motif 'CDFGLARI', (4) the APE motif 'RAPEIML' in the activation segment, and (5) the VAIK lysine region 'AVKK'. These hallmarks are diagnostic of the protein kinase superfamily fold. None of the distractors (A: plant alkaloid oxidase, B: polyketide synthase, D: cesium ion channel) involve protein kinase catalysis. A biologist familiar with kinase motifs can confidently identify this as a protein kinase and select the phosphorylation transfer reaction (C) over the other unrelated reactions.


**Missing item-specific fact**

> None critical. The kinase motifs are general and do not require knowing this specific protein's identity. The distinction between MAP kinase (EC 2.7.11.24) and other kinase subclasses is not needed here since all other options are non-kinase reactions.


**Reason**

> The protein kinase domain motifs (HRD, DFG, APE, glycine-rich loop) are well-known general features that any trained biologist can recognize from the sequence. The distractors represent entirely different enzyme classes (oxidoreductase, polyketide synthase, ion transporter) with no kinase-like features, making the discrimination straightforward through general knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A, B, and D describe reactions catalyzed by completely different enzyme classes (alkaloid oxidase, polyketide synthase, ion transporter) that share no structural or mechanistic features with the supplied sequence. Only C describes a protein kinase reaction consistent with the kinase motifs present. Although EC 2.7.11.24 also covers threonine phosphorylation, the serine reaction (C) is one of the two canonical reactions for this EC number, and no threonine-specific option is offered, so no ambiguity arises.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000250 (similarity to P32485), meaning the catalytic activity assignment is inferred by homology rather than directly measured on A0A5B9GBF0. However, the sequence's kinase motifs independently support the kinase classification.
- EC 2.7.11.24 encompasses both serine and threonine phosphorylation; the question only offers the serine reaction. This is a minor incompleteness but does not create ambiguity since no threonine option is provided.
- The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the model must rely on sequence motif recognition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase structural motifs identifiable by general biological knowledge: (1) a glycine-rich loop 'GAFGLV' near the N-terminus (GxGxxG-like), (2) the catalytic HRD motif 'HRDLKPSN', (3) the DFG motif 'CDFGLARI', (4) the APE motif 'RAPEIML' in the activation segment, and (5) the VAIK lysine region 'AVKK'. These hallmarks are diagnostic of the protein kinase superfamily fold. None of the distractors (A: plant alkaloid oxidase, B: polyketide synthase, D: cesium ion channel) involve protein kinase catalysis. A biologist familiar with kinase motifs can confidently identify this as a protein kinase and select the phosphorylation transfer reaction (C) over the other unrelated reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The kinase motifs are general and do not require knowing this specific protein's identity. The distinction between MAP kinase (EC 2.7.11.24) and other kinase subclasses is not needed here since all other options are non-kinase reactions.",
    "reason": "The protein kinase domain motifs (HRD, DFG, APE, glycine-rich loop) are well-known general features that any trained biologist can recognize from the sequence. The distractors represent entirely different enzyme classes (oxidoreductase, polyketide synthase, ion transporter) with no kinase-like features, making the discrimination straightforward through general knowledge."
  },
  "case_id": "catalytic_activity_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A5B9GBF0 (HOG1_AURME), annotated as Mitogen-activated protein kinase HOG1 with EC 2.7.11.24. The listed catalytic activity is exactly 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)'. The evidence code is ECO:0000250 (inferred by similarity from P32485, yeast HOG1), so this is computational/similarity-based annotation rather than direct experimental measurement on this specific protein, but the sequence clearly exhibits canonical protein kinase domain architecture, making the annotation well-founded."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity to P32485), meaning the catalytic activity assignment is inferred by homology rather than directly measured on A0A5B9GBF0. However, the sequence's kinase motifs independently support the kinase classification.",
    "EC 2.7.11.24 encompasses both serine and threonine phosphorylation; the question only offers the serine reaction. This is a minor incompleteness but does not create ambiguity since no threonine option is provided.",
    "The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the model must rely on sequence motif recognition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, B, and D describe reactions catalyzed by completely different enzyme classes (alkaloid oxidase, polyketide synthase, ion transporter) that share no structural or mechanistic features with the supplied sequence. Only C describes a protein kinase reaction consistent with the kinase motifs present. Although EC 2.7.11.24 also covers threonine phosphorylation, the serine reaction (C) is one of the two canonical reactions for this EC number, and no threonine-specific option is offered, so no ambiguity arises."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A5B9GBF0 (HOG1_AURME), annotated as Mitogen-activated protein kinase HOG1 with EC 2.7.11.24. The listed catalytic activity is exactly 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)'. The evidence code is ECO:0000250 (inferred by similarity from P32485, yeast HOG1), so this is computational/similarity-based annotation rather than direct experimental measurement on this specific protein, but the sequence clearly exhibits canonical protein kinase domain architecture, making the annotation well-founded.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase structural motifs identifiable by general biological knowledge: (1) a glycine-rich loop 'GAFGLV' near the N-terminus (GxGxxG-like), (2) the catalytic HRD motif 'HRDLKPSN', (3) the DFG motif 'CDFGLARI', (4) the APE motif 'RAPEIML' in the activation segment, and (5) the VAIK lysine region 'AVKK'. These hallmarks are diagnostic of the protein kinase superfamily fold. None of the distractors (A: plant alkaloid oxidase, B: polyketide synthase, D: cesium ion channel) involve protein kinase catalysis. A biologist familiar with kinase motifs can confidently identify this as a protein kinase and select the phosphorylation transfer reaction (C) over the other unrelated reactions.",
    "missing_item_specific_fact": "None critical. The kinase motifs are general and do not require knowing this specific protein's identity. The distinction between MAP kinase (EC 2.7.11.24) and other kinase subclasses is not needed here since all other options are non-kinase reactions.",
    "reason": "The protein kinase domain motifs (HRD, DFG, APE, glycine-rich loop) are well-known general features that any trained biologist can recognize from the sequence. The distractors represent entirely different enzyme classes (oxidoreductase, polyketide synthase, ion transporter) with no kinase-like features, making the discrimination straightforward through general knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, B, and D describe reactions catalyzed by completely different enzyme classes (alkaloid oxidase, polyketide synthase, ion transporter) that share no structural or mechanistic features with the supplied sequence. Only C describes a protein kinase reaction consistent with the kinase motifs present. Although EC 2.7.11.24 also covers threonine phosphorylation, the serine reaction (C) is one of the two canonical reactions for this EC number, and no threonine-specific option is offered, so no ambiguity arises."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity to P32485), meaning the catalytic activity assignment is inferred by homology rather than directly measured on A0A5B9GBF0. However, the sequence's kinase motifs independently support the kinase classification.",
    "EC 2.7.11.24 encompasses both serine and threonine phosphorylation; the question only offers the serine reaction. This is a minor incompleteness but does not create ambiguity since no threonine option is provided.",
    "The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the model must rely on sequence motif recognition."
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

**Accession:** `A0A5B9GBF0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 29. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5B9GBF0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:49.473180+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33375973","source":"PubMed"}],"value":"High osmolarity glycerol response protein 1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"value":"2.7.11.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33375973","source":"PubMed"}],"value":"Mitogen-activated protein kinase HOG1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33375973","source":"PubMed"}],"value":"MAP kinase HOG1"}]}}
```

Source SHA-256: `fba079004196dc4aa9a4146777e2ad8ed7d3390b474caa53a6cffcdd32fef7bf`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5B9GBF0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:49.473180+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:17990"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `fba079004196dc4aa9a4146777e2ad8ed7d3390b474caa53a6cffcdd32fef7bf`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5B9GBF0?format=txt&versions=29)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-01T06:27:31.440600+00:00.  

```text
ID   HOG1_AURME              Reviewed;         355 AA.
AC   A0A5B9GBF0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-NOV-2019, sequence version 1.
DT   28-JAN-2026, entry version 29.
DE   RecName: Full=Mitogen-activated protein kinase HOG1 {ECO:0000303|PubMed:33375973};
DE            Short=MAP kinase HOG1 {ECO:0000303|PubMed:33375973};
DE            EC=2.7.11.24 {ECO:0000250|UniProtKB:P32485};
DE   AltName: Full=High osmolarity glycerol response protein 1 {ECO:0000303|PubMed:33375973};
GN   Name=HOG1 {ECO:0000303|PubMed:33375973};
GN   ORFNames=KCU76_g14496, KCU76_g8675, KCV03_g1946;
OS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.
OX   NCBI_TaxID=46634;
```

Source SHA-256: `b41aad72deba1b2a50b4811f2707c4302afb398ce10bc95f1c81941f78b1051a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5B9GBF0?format=txt&versions=29)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-01T06:27:31.440600+00:00.  

```text
DE   RecName: Full=Mitogen-activated protein kinase HOG1 {ECO:0000303|PubMed:33375973};
DE            Short=MAP kinase HOG1 {ECO:0000303|PubMed:33375973};
DE            EC=2.7.11.24 {ECO:0000250|UniProtKB:P32485};
DE   AltName: Full=High osmolarity glycerol response protein 1 {ECO:0000303|PubMed:33375973};
```

Source SHA-256: `b41aad72deba1b2a50b4811f2707c4302afb398ce10bc95f1c81941f78b1051a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5B9GBF0?format=txt&versions=29)  
**Locator:** `lines 57-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-01T06:27:31.440600+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:17990;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
```

Source SHA-256: `b41aad72deba1b2a50b4811f2707c4302afb398ce10bc95f1c81941f78b1051a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 160. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
