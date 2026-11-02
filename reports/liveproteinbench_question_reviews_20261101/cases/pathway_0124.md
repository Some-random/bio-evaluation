# pathway_0124

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Lipid metabolism. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKIDESLNVHSSLLQLIGNTPLLELHKITKGLKGRYFAKLEAFNVGHSAKDRVAKYIVEDAERKGLLKPGSTIVETSSGNTGYSLAMISALRGYRCIIAISDKSSHDKVEMLQALGAEVHLCPANVAPDDPRSYYEVAKRIHNETPNSIYVNQYFNPLNPESHYQTGREIWEQTQGEITHVVVCSGTGGTISGIAHYLKEQNPRVQVLGVDAYGSAIKKYHETREFDPAEVYPYKIEGIGKNLIPTATDFDVIDEFIKVTDKDAALMARKLARTEGLFMGYTSGAAIQAVKQYAEAGKFDENSIVVVLFADHGSRYMNKIYSDDWMKKQGFID

[Multiple Choices]
A. Cell wall biogenesis
B. nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1. .
C. iron-sulfur cluster biosynthesis. .
D. Lipid metabolism. .
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

> The exact sequence matches the UniProt entry annotated as cysteate synthase (EC 2.5.1.76), with experimental evidence cited for the enzyme function. The entry assigns it to lipid metabolism, citing a study on the biosynthetic pathway of the sulfonolipid capnine. The pathway assignment is a database annotation, not itself an experimental evidence code, but it supports choice D.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The supplied sequence does not provide a defensible, specific basis for identifying its biochemical function or distinguishing lipid metabolism from the other listed pathways without protein-specific functional knowledge.


**Missing item-specific fact**

> The sequence's identity as cysteate synthase and its role in sulfonolipid capnine biosynthesis.


**Reason**

> The sequence is the only biological input, and recognizing it or its annotation requires an external protein-specific fact. The reviewer-only database evidence supports the key but was not supplied to the model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched database entry assigns the protein to lipid metabolism; none of the other choices is comparably supported by the provided evidence.


### Important caveats

- The sequence match applies to the exact 333-residue sequence supplied.
- The lipid-metabolism pathway statement is a UniProt annotation citing a 2022 study; it should be distinguished from the experimentally supported enzyme-function annotation.
- Reviewer-only evidence establishes support for the key but does not make the original sequence-only question reasoning-supported.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence does not provide a defensible, specific basis for identifying its biochemical function or distinguishing lipid metabolism from the other listed pathways without protein-specific functional knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's identity as cysteate synthase and its role in sulfonolipid capnine biosynthesis.",
    "reason": "The sequence is the only biological input, and recognizing it or its annotation requires an external protein-specific fact. The reviewer-only database evidence supports the key but was not supplied to the model."
  },
  "case_id": "pathway_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as cysteate synthase (EC 2.5.1.76), with experimental evidence cited for the enzyme function. The entry assigns it to lipid metabolism, citing a study on the biosynthetic pathway of the sulfonolipid capnine. The pathway assignment is a database annotation, not itself an experimental evidence code, but it supports choice D."
  },
  "important_caveats": [
    "The sequence match applies to the exact 333-residue sequence supplied.",
    "The lipid-metabolism pathway statement is a UniProt annotation citing a 2022 study; it should be distinguished from the experimentally supported enzyme-function annotation.",
    "Reviewer-only evidence establishes support for the key but does not make the original sequence-only question reasoning-supported."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database entry assigns the protein to lipid metabolism; none of the other choices is comparably supported by the provided evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as cysteate synthase (EC 2.5.1.76), with experimental evidence cited for the enzyme function. The entry assigns it to lipid metabolism, citing a study on the biosynthetic pathway of the sulfonolipid capnine. The pathway assignment is a database annotation, not itself an experimental evidence code, but it supports choice D.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The supplied sequence does not provide a defensible, specific basis for identifying its biochemical function or distinguishing lipid metabolism from the other listed pathways without protein-specific functional knowledge.",
    "missing_item_specific_fact": "The sequence's identity as cysteate synthase and its role in sulfonolipid capnine biosynthesis.",
    "reason": "The sequence is the only biological input, and recognizing it or its annotation requires an external protein-specific fact. The reviewer-only database evidence supports the key but was not supplied to the model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database entry assigns the protein to lipid metabolism; none of the other choices is comparably supported by the provided evidence."
  },
  "important_caveats": [
    "The sequence match applies to the exact 333-residue sequence supplied.",
    "The lipid-metabolism pathway statement is a UniProt annotation citing a 2022 study; it should be distinguished from the experimentally supported enzyme-function annotation.",
    "Reviewer-only evidence establishes support for the key but does not make the original sequence-only question reasoning-supported."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry C7M8J5 (sequence matched, 333 aa) explicitly annotates the pathway as 'Lipid metabolism' (ECO:0000305, PubMed:35414181). The protein is cysteate synthase (EC 2.5.1.76), characterized in the 2022 paper on sulfonolipid capnine biosynthesis. Sulfonolipids are a lipid class, making 'Lipid metabolism' a valid pathway assignment. The evidence code is curator inference (ECO:0000305), but the underlying enzyme function was experimentally validated (ECO:0000269, direct assay).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence resembles members of the cysteine synthase / serine acetyltransferase superfamily (PLP-dependent, ~330 aa, conserved catalytic residues). A model reasoning from sequence alone would most naturally associate this fold with amino acid biosynthesis (cysteine biosynthesis), not lipid metabolism. The link to lipid metabolism arises solely from the specific, recently characterized (2022) role of cysteate synthase in sulfonolipid capnine biosynthesis — a fact not inferable from sequence features.


**Missing item-specific fact**

> The knowledge that this particular cysteine-synthase-family enzyme catalyzes the first committed step in sulfonolipid (capnine) biosynthesis, thereby placing it in lipid metabolism rather than amino acid metabolism. This was established experimentally only in 2022 (PubMed:35414181) and is not deducible from general sequence features.


**Reason**

> Distractors B (a specific reaction step, not a pathway) and C (iron-sulfur cluster biosynthesis) can be eliminated by general knowledge, but positively identifying 'Lipid metabolism' from a cysteine-synthase-like sequence requires the item-specific fact that this enzyme feeds sulfonolipid biosynthesis. Without that annotation or memorized association, the most defensible inference from sequence homology would be amino acid metabolism, which is not among the options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, D is the only one that matches the UniProt annotation. Choices A, B, and C are clearly wrong for this enzyme (no cell-wall, NAD-salvage, or Fe-S cluster features). However, the absence of an 'amino acid metabolism' option (the most intuitive prediction from sequence) means the question is answerable by elimination even without positive lipid-metabolism reasoning, though the positive reasoning chain is still lookup-dependent.


### Important caveats

- The pathway annotation uses ECO:0000305 (curator inference), not a direct experimental pathway measurement; the enzyme assay (ECO:0000269) confirmed catalytic function, and the pathway assignment follows from the broader sulfonolipid biosynthesis study.
- The 2022 publication post-dates many training data cutoffs, making memorization of this specific annotation less likely for older models but not impossible for newer ones.
- The sequence is a Swiss-Prot reviewed entry (first public 2025-04-09); the author's source snapshot is unknown but the historical version 65 (2026-01-28) already carried the same pathway annotation.
- Choice B is phrased as a single reaction step rather than a named pathway, making it an unusually easy distractor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence resembles members of the cysteine synthase / serine acetyltransferase superfamily (PLP-dependent, ~330 aa, conserved catalytic residues). A model reasoning from sequence alone would most naturally associate this fold with amino acid biosynthesis (cysteine biosynthesis), not lipid metabolism. The link to lipid metabolism arises solely from the specific, recently characterized (2022) role of cysteate synthase in sulfonolipid capnine biosynthesis — a fact not inferable from sequence features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The knowledge that this particular cysteine-synthase-family enzyme catalyzes the first committed step in sulfonolipid (capnine) biosynthesis, thereby placing it in lipid metabolism rather than amino acid metabolism. This was established experimentally only in 2022 (PubMed:35414181) and is not deducible from general sequence features.",
    "reason": "Distractors B (a specific reaction step, not a pathway) and C (iron-sulfur cluster biosynthesis) can be eliminated by general knowledge, but positively identifying 'Lipid metabolism' from a cysteine-synthase-like sequence requires the item-specific fact that this enzyme feeds sulfonolipid biosynthesis. Without that annotation or memorized association, the most defensible inference from sequence homology would be amino acid metabolism, which is not among the options."
  },
  "case_id": "pathway_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry C7M8J5 (sequence matched, 333 aa) explicitly annotates the pathway as 'Lipid metabolism' (ECO:0000305, PubMed:35414181). The protein is cysteate synthase (EC 2.5.1.76), characterized in the 2022 paper on sulfonolipid capnine biosynthesis. Sulfonolipids are a lipid class, making 'Lipid metabolism' a valid pathway assignment. The evidence code is curator inference (ECO:0000305), but the underlying enzyme function was experimentally validated (ECO:0000269, direct assay)."
  },
  "important_caveats": [
    "The pathway annotation uses ECO:0000305 (curator inference), not a direct experimental pathway measurement; the enzyme assay (ECO:0000269) confirmed catalytic function, and the pathway assignment follows from the broader sulfonolipid biosynthesis study.",
    "The 2022 publication post-dates many training data cutoffs, making memorization of this specific annotation less likely for older models but not impossible for newer ones.",
    "The sequence is a Swiss-Prot reviewed entry (first public 2025-04-09); the author's source snapshot is unknown but the historical version 65 (2026-01-28) already carried the same pathway annotation.",
    "Choice B is phrased as a single reaction step rather than a named pathway, making it an unusually easy distractor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, D is the only one that matches the UniProt annotation. Choices A, B, and C are clearly wrong for this enzyme (no cell-wall, NAD-salvage, or Fe-S cluster features). However, the absence of an 'amino acid metabolism' option (the most intuitive prediction from sequence) means the question is answerable by elimination even without positive lipid-metabolism reasoning, though the positive reasoning chain is still lookup-dependent."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry C7M8J5 (sequence matched, 333 aa) explicitly annotates the pathway as 'Lipid metabolism' (ECO:0000305, PubMed:35414181). The protein is cysteate synthase (EC 2.5.1.76), characterized in the 2022 paper on sulfonolipid capnine biosynthesis. Sulfonolipids are a lipid class, making 'Lipid metabolism' a valid pathway assignment. The evidence code is curator inference (ECO:0000305), but the underlying enzyme function was experimentally validated (ECO:0000269, direct assay).",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence resembles members of the cysteine synthase / serine acetyltransferase superfamily (PLP-dependent, ~330 aa, conserved catalytic residues). A model reasoning from sequence alone would most naturally associate this fold with amino acid biosynthesis (cysteine biosynthesis), not lipid metabolism. The link to lipid metabolism arises solely from the specific, recently characterized (2022) role of cysteate synthase in sulfonolipid capnine biosynthesis — a fact not inferable from sequence features.",
    "missing_item_specific_fact": "The knowledge that this particular cysteine-synthase-family enzyme catalyzes the first committed step in sulfonolipid (capnine) biosynthesis, thereby placing it in lipid metabolism rather than amino acid metabolism. This was established experimentally only in 2022 (PubMed:35414181) and is not deducible from general sequence features.",
    "reason": "Distractors B (a specific reaction step, not a pathway) and C (iron-sulfur cluster biosynthesis) can be eliminated by general knowledge, but positively identifying 'Lipid metabolism' from a cysteine-synthase-like sequence requires the item-specific fact that this enzyme feeds sulfonolipid biosynthesis. Without that annotation or memorized association, the most defensible inference from sequence homology would be amino acid metabolism, which is not among the options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, D is the only one that matches the UniProt annotation. Choices A, B, and C are clearly wrong for this enzyme (no cell-wall, NAD-salvage, or Fe-S cluster features). However, the absence of an 'amino acid metabolism' option (the most intuitive prediction from sequence) means the question is answerable by elimination even without positive lipid-metabolism reasoning, though the positive reasoning chain is still lookup-dependent."
  },
  "important_caveats": [
    "The pathway annotation uses ECO:0000305 (curator inference), not a direct experimental pathway measurement; the enzyme assay (ECO:0000269) confirmed catalytic function, and the pathway assignment follows from the broader sulfonolipid biosynthesis study.",
    "The 2022 publication post-dates many training data cutoffs, making memorization of this specific annotation less likely for older models but not impossible for newer ones.",
    "The sequence is a Swiss-Prot reviewed entry (first public 2025-04-09); the author's source snapshot is unknown but the historical version 65 (2026-01-28) already carried the same pathway annotation.",
    "Choice B is phrased as a single reaction step rather than a named pathway, making it an unusually easy distractor."
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
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.457032+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"35414181","source":"PubMed"}],"value":"Lipid metabolism"}]}
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 62-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
CC   -!- PATHWAY: Lipid metabolism. {ECO:0000305|PubMed:35414181}.
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
