# pathway_0099

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Antibiotic biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNTQPLERALAAFREVLGTAHVSTDESARAAAETATFATTHRIPAIISPGSAAEVEACVRIAREHGVPLYPVSTGKNWGYGSRVPTSDGAIVLSLARMNRILDFNEELAYVAIEPGVTMRQLVAYLNDRGSRLMLSVTGSTPDSSVVGNICDRGFGAGVNAERIAHICNIEVVLPNGERLNTGFGRFPGAQTASIHRWGIGPQLDGLFTQSNLGIVTRMTIWLAPRPRHHEIFYFRLRDERRVEAVTDIIRDLKLQGLPRASVSLWNDYKLVSMKGQYPWQEAAGKTPLPEALLAKLRRAWGGAAWLGGGAILAASQDQIAAERAVIRKALHPHVDKLSFVGQRAARVARLLQRPVQRLTGFDLSEVVRAYEQSPHLGIPMERNIRSAYWRKKAPPPEQTDPDRDRCGAIWLAPAVPSTGKHVGTALRIVRERALAHAFEPGISVIFATERCANIVVALMYDRELPGEDGRAMACYQDIFDRLAAQGYLPYRLGIQSQSALPAAQSSYGTVVGALKRALDPDDILAPGRYDFRHEWPPADN

[Multiple Choices]
A. Antibiotic biosynthesis. .
B. Cell wall degradation
C. Protein biosynthesis
D. Protein modification
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

> The exact sequence matches the annotated 1′-carboxy-chondrochloren decarboxylase, whose pathway is listed as antibiotic biosynthesis. The annotation cites experimental evidence and publications on chondrochloren biosynthesis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein-specific functional and pathway annotation linking this enzyme to chondrochloren antibiotic biosynthesis.


**Reason**

> The sequence alone does not meaningfully distinguish antibiotic biosynthesis from the other broad pathway choices without identifying the specific enzyme and its biological role. That link is an item-specific fact absent from the prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched annotation assigns the protein to antibiotic biosynthesis; the supplied evidence does not support another listed choice as its primary pathway.


### Important caveats

- Reviewer-only evidence was not supplied to the evaluated model.
- The evidence supports the key for the exact sequence, but does not make the answer derivable from the sequence and choices alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional and pathway annotation linking this enzyme to chondrochloren antibiotic biosynthesis.",
    "reason": "The sequence alone does not meaningfully distinguish antibiotic biosynthesis from the other broad pathway choices without identifying the specific enzyme and its biological role. That link is an item-specific fact absent from the prompt."
  },
  "case_id": "pathway_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated 1′-carboxy-chondrochloren decarboxylase, whose pathway is listed as antibiotic biosynthesis. The annotation cites experimental evidence and publications on chondrochloren biosynthesis."
  },
  "important_caveats": [
    "Reviewer-only evidence was not supplied to the evaluated model.",
    "The evidence supports the key for the exact sequence, but does not make the answer derivable from the sequence and choices alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation assigns the protein to antibiotic biosynthesis; the supplied evidence does not support another listed choice as its primary pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated 1′-carboxy-chondrochloren decarboxylase, whose pathway is listed as antibiotic biosynthesis. The annotation cites experimental evidence and publications on chondrochloren biosynthesis.",
    "evidence_ids": ["C4", "C5", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein-specific functional and pathway annotation linking this enzyme to chondrochloren antibiotic biosynthesis.",
    "reason": "The sequence alone does not meaningfully distinguish antibiotic biosynthesis from the other broad pathway choices without identifying the specific enzyme and its biological role. That link is an item-specific fact absent from the prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation assigns the protein to antibiotic biosynthesis; the supplied evidence does not support another listed choice as its primary pathway."
  },
  "important_caveats": [
    "Reviewer-only evidence was not supplied to the evaluated model.",
    "The evidence supports the key for the exact sequence, but does not make the answer derivable from the sequence and choices alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B9ZUK6 (CndG, 1'-carboxy-chondrochloren decarboxylase, EC 4.1.1.129) from Chondromyces crocatus is explicitly annotated with PATHWAY: 'Antibiotic biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:20080978) and inferential evidence (ECO:0000305, PubMed:19171307). The reference paper titles confirm chondrochlorens are antibiotics. The benchmark sequence SHA256 matches the UniProt sequence exactly (541 AA, sequence version 1).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Partial elimination is possible from general biochemistry: a decarboxylase (EC 4.1.x) is a biosynthetic/catabolic enzyme, not involved in protein biosynthesis (C), protein modification (D), or cell wall degradation (B). This narrows toward a biosynthetic pathway. However, the specific qualifier 'antibiotic' cannot be derived from the sequence alone.


**Missing item-specific fact**

> The fact that this protein (CndG) participates in the chondrochloren biosynthetic gene cluster of Chondromyces crocatus, and that chondrochlorens are antibiotic compounds, is an organism- and pathway-specific annotation not inferable from the amino acid sequence or general enzymology of decarboxylases.


**Reason**

> While rough elimination of B, C, D is possible (the enzyme is clearly not a ribosomal component, kinase, or hydrolase acting on peptidoglycan), confirming the pathway is specifically 'antibiotic biosynthesis' rather than, say, amino acid metabolism or another secondary-metabolite pathway requires knowing the identity of the substrate (chondrochloren) and its biological role as an antibiotic. This is an item-specific database/experimental fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, B (cell wall degradation), C (protein biosynthesis), and D (protein modification) are clearly incompatible with a decarboxylase acting on a small-molecule carboxylated intermediate. A is the only biosynthetic option, making it the best fit by elimination even without knowing the exact substrate. No other option is defensible.


### Important caveats

- The pathway annotation carries experimental evidence (ECO:0000269) from the 2010 JBC paper, confirming CndG's role in chondrochloren biosynthesis via in vitro characterization.
- The organism (Chondromyces crocatus) and the specific compound (chondrochloren) are not provided in the question prompt, so the model must either recognize the sequence or rely on general elimination among the four choices.
- The question provides no organism name, gene name, or substrate information, making the 'antibiotic' qualifier dependent on protein-specific knowledge.
- The UniProt entry was first publicly released 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2009-04-14.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Partial elimination is possible from general biochemistry: a decarboxylase (EC 4.1.x) is a biosynthetic/catabolic enzyme, not involved in protein biosynthesis (C), protein modification (D), or cell wall degradation (B). This narrows toward a biosynthetic pathway. However, the specific qualifier 'antibiotic' cannot be derived from the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The fact that this protein (CndG) participates in the chondrochloren biosynthetic gene cluster of Chondromyces crocatus, and that chondrochlorens are antibiotic compounds, is an organism- and pathway-specific annotation not inferable from the amino acid sequence or general enzymology of decarboxylases.",
    "reason": "While rough elimination of B, C, D is possible (the enzyme is clearly not a ribosomal component, kinase, or hydrolase acting on peptidoglycan), confirming the pathway is specifically 'antibiotic biosynthesis' rather than, say, amino acid metabolism or another secondary-metabolite pathway requires knowing the identity of the substrate (chondrochloren) and its biological role as an antibiotic. This is an item-specific database/experimental fact."
  },
  "case_id": "pathway_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B9ZUK6 (CndG, 1'-carboxy-chondrochloren decarboxylase, EC 4.1.1.129) from Chondromyces crocatus is explicitly annotated with PATHWAY: 'Antibiotic biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:20080978) and inferential evidence (ECO:0000305, PubMed:19171307). The reference paper titles confirm chondrochlorens are antibiotics. The benchmark sequence SHA256 matches the UniProt sequence exactly (541 AA, sequence version 1)."
  },
  "important_caveats": [
    "The pathway annotation carries experimental evidence (ECO:0000269) from the 2010 JBC paper, confirming CndG's role in chondrochloren biosynthesis via in vitro characterization.",
    "The organism (Chondromyces crocatus) and the specific compound (chondrochloren) are not provided in the question prompt, so the model must either recognize the sequence or rely on general elimination among the four choices.",
    "The question provides no organism name, gene name, or substrate information, making the 'antibiotic' qualifier dependent on protein-specific knowledge.",
    "The UniProt entry was first publicly released 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2009-04-14."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, B (cell wall degradation), C (protein biosynthesis), and D (protein modification) are clearly incompatible with a decarboxylase acting on a small-molecule carboxylated intermediate. A is the only biosynthetic option, making it the best fit by elimination even without knowing the exact substrate. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B9ZUK6 (CndG, 1'-carboxy-chondrochloren decarboxylase, EC 4.1.1.129) from Chondromyces crocatus is explicitly annotated with PATHWAY: 'Antibiotic biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:20080978) and inferential evidence (ECO:0000305, PubMed:19171307). The reference paper titles confirm chondrochlorens are antibiotics. The benchmark sequence SHA256 matches the UniProt sequence exactly (541 AA, sequence version 1).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Partial elimination is possible from general biochemistry: a decarboxylase (EC 4.1.x) is a biosynthetic/catabolic enzyme, not involved in protein biosynthesis (C), protein modification (D), or cell wall degradation (B). This narrows toward a biosynthetic pathway. However, the specific qualifier 'antibiotic' cannot be derived from the sequence alone.",
    "missing_item_specific_fact": "The fact that this protein (CndG) participates in the chondrochloren biosynthetic gene cluster of Chondromyces crocatus, and that chondrochlorens are antibiotic compounds, is an organism- and pathway-specific annotation not inferable from the amino acid sequence or general enzymology of decarboxylases.",
    "reason": "While rough elimination of B, C, D is possible (the enzyme is clearly not a ribosomal component, kinase, or hydrolase acting on peptidoglycan), confirming the pathway is specifically 'antibiotic biosynthesis' rather than, say, amino acid metabolism or another secondary-metabolite pathway requires knowing the identity of the substrate (chondrochloren) and its biological role as an antibiotic. This is an item-specific database/experimental fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, B (cell wall degradation), C (protein biosynthesis), and D (protein modification) are clearly incompatible with a decarboxylase acting on a small-molecule carboxylated intermediate. A is the only biosynthetic option, making it the best fit by elimination even without knowing the exact substrate. No other option is defensible."
  },
  "important_caveats": [
    "The pathway annotation carries experimental evidence (ECO:0000269) from the 2010 JBC paper, confirming CndG's role in chondrochloren biosynthesis via in vitro characterization.",
    "The organism (Chondromyces crocatus) and the specific compound (chondrochloren) are not provided in the question prompt, so the model must either recognize the sequence or rely on general elimination among the four choices.",
    "The question provides no organism name, gene name, or substrate information, making the 'antibiotic' qualifier dependent on protein-specific knowledge.",
    "The UniProt entry was first publicly released 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2009-04-14."
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

**Accession:** `B9ZUK6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 61. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20080978","source":"PubMed"}],"value":"Oxidative decarboxylase CndG"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20080978","source":"PubMed"}],"value":"4.1.1.129"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1'-carboxy-chondrochloren decarboxylase"}}}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20080978","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"19171307","source":"PubMed"}],"value":"Antibiotic biosynthesis"}]}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"citation":{"authors":["Rachid S.","Scharfe M.","Bloecker H.","Weissman K.J.","Mueller R."],"citationCrossReferences":[{"database":"PubMed","id":"19171307"},{"database":"DOI","id":"10.1016/j.chembiol.2008.11.005"}],"citationType":"journal article","firstPage":"70","id":"19171307","journal":"Chem. Biol.","lastPage":"81","publicationDate":"2009","title":"Unusual chemistry in the biosynthesis of the antibiotic chondrochlorens.","volume":"16"},"evidences":[{"evidenceCode":"ECO:0000312","id":"CAQ43085.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"DSM 14714 / JCM 12616 / Cm c5"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","GENE CLUSTER","PATHWAY"]}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"citation":{"authors":["Rachid S.","Revermann O.","Dauth C.","Kazmaier U.","Mueller R."],"citationCrossReferences":[{"database":"PubMed","id":"20080978"},{"database":"DOI","id":"10.1074/jbc.m109.079707"}],"citationType":"journal article","firstPage":"12482","id":"20080978","journal":"J. Biol. Chem.","lastPage":"12489","publicationDate":"2010","title":"Characterization of a novel type of oxidative decarboxylase involved in the biosynthesis of the styryl moiety of chondrochloren from an acylated tyrosine.","volume":"285"},"referenceComments":[{"type":"STRAIN","value":"DSM 14714 / JCM 12616 / Cm c5"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","MASS SPECTROMETRY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
ID   CNDG_CHOCO              Reviewed;         541 AA.
AC   B9ZUK6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   14-APR-2009, sequence version 1.
DT   28-JAN-2026, entry version 61.
DE   RecName: Full=1'-carboxy-chondrochloren decarboxylase {ECO:0000305};
DE            EC=4.1.1.129 {ECO:0000269|PubMed:20080978};
DE   AltName: Full=Oxidative decarboxylase CndG {ECO:0000303|PubMed:20080978};
GN   Name=cndG {ECO:0000303|PubMed:19171307};
GN   ORFNames=CMC5_053350 {ECO:0000312|EMBL:AKT41174.1};
OS   Chondromyces crocatus.
OC   Bacteria; Pseudomonadati; Myxococcota; Polyangia; Polyangiales;
OC   Polyangiaceae; Chondromyces.
OX   NCBI_TaxID=52;
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 15-21`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:CAQ43085.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], GENE CLUSTER, AND PATHWAY.
RC   STRAIN=DSM 14714 / JCM 12616 / Cm c5;
RX   PubMed=19171307; DOI=10.1016/j.chembiol.2008.11.005;
RA   Rachid S., Scharfe M., Bloecker H., Weissman K.J., Mueller R.;
RT   "Unusual chemistry in the biosynthesis of the antibiotic chondrochlorens.";
RL   Chem. Biol. 16:70-81(2009).
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, PATHWAY, MASS SPECTROMETRY, AND DISRUPTION PHENOTYPE.
RC   STRAIN=DSM 14714 / JCM 12616 / Cm c5;
RX   PubMed=20080978; DOI=10.1074/jbc.m109.079707;
RA   Rachid S., Revermann O., Dauth C., Kazmaier U., Mueller R.;
RT   "Characterization of a novel type of oxidative decarboxylase involved in
RT   the biosynthesis of the styryl moiety of chondrochloren from an acylated
RT   tyrosine.";
RL   J. Biol. Chem. 285:12482-12489(2010).
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 74-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
CC   -!- PATHWAY: Antibiotic biosynthesis. {ECO:0000269|PubMed:20080978,
CC       ECO:0000305|PubMed:19171307}.
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
