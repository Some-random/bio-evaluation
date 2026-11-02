# pathway_0199

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Carotenoid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQTVTLSIFRFNEFEKRLWVLGQMTANKLGMHYLPKAKFWKMFGSGTGQGFTPKPNWHVWSILAVWPDEETARREVAESPIYQRWTKMADESYTVLLQPTSAWGKWDGKEPFEPVKPASDVRPIAALTRATVKFWKAERFWAREPAISHMIGRNKDVVFKIGVGEVPFVQQVTFSIWPDARSMEEFARGAGGPHGEAIKAVRAENWFKEELYARFQILGTIGKWEGKDPVGEALTARPSEAPKPAPAPAAAQPAPAAEAPKPAPAPVAEKPALAVEMPKPAEPPKPVVEAPKPASAPVASKPMPQGGKPNFKGKPGKGGRKENA

[Multiple Choices]
A. Carotenoid biosynthesis
B. One-carbon metabolism
C. Amino-acid degradation. .
D. LPS O-antigen biosynthesis. .
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

> The exact sequence matches a UniProt entry annotated as spheroidene monooxygenase with a carotenoid-biosynthesis pathway annotation. The enzyme name and pathway assignment are partly similarity-transferred, so this supports the key without establishing that every annotation is based on direct experiments on this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The supplied sequence alone offers no clear, general biological feature that distinguishes carotenoid biosynthesis from the other listed pathways. Identifying it as a particular pathway enzyme requires recognizing or annotating the protein.


**Missing item-specific fact**

> That this exact sequence is CrtA, a spheroidene monooxygenase associated with spheroidene and carotenoid biosynthesis.


**Reason**

> The reviewer-only matched-sequence annotation supports the expected pathway, but that protein-specific identity and function are not supplied in the question. Inferring them from the raw sequence would depend on an external database or protein-specific knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available matched-sequence annotation supports carotenoid biosynthesis; no alternative listed pathway is comparably supported by the evidence.


### Important caveats

- The pathway annotation is marked as transferred by similarity (ECO:0000250), rather than established here as a direct experimental result for this exact protein.
- The author's exact source snapshot is unknown, although the sequence matches both current and historical UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence alone offers no clear, general biological feature that distinguishes carotenoid biosynthesis from the other listed pathways. Identifying it as a particular pathway enzyme requires recognizing or annotating the protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this exact sequence is CrtA, a spheroidene monooxygenase associated with spheroidene and carotenoid biosynthesis.",
    "reason": "The reviewer-only matched-sequence annotation supports the expected pathway, but that protein-specific identity and function are not supplied in the question. Inferring them from the raw sequence would depend on an external database or protein-specific knowledge."
  },
  "case_id": "pathway_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as spheroidene monooxygenase with a carotenoid-biosynthesis pathway annotation. The enzyme name and pathway assignment are partly similarity-transferred, so this supports the key without establishing that every annotation is based on direct experiments on this exact protein."
  },
  "important_caveats": [
    "The pathway annotation is marked as transferred by similarity (ECO:0000250), rather than established here as a direct experimental result for this exact protein.",
    "The author's exact source snapshot is unknown, although the sequence matches both current and historical UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available matched-sequence annotation supports carotenoid biosynthesis; no alternative listed pathway is comparably supported by the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as spheroidene monooxygenase with a carotenoid-biosynthesis pathway annotation. The enzyme name and pathway assignment are partly similarity-transferred, so this supports the key without establishing that every annotation is based on direct experiments on this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The supplied sequence alone offers no clear, general biological feature that distinguishes carotenoid biosynthesis from the other listed pathways. Identifying it as a particular pathway enzyme requires recognizing or annotating the protein.",
    "missing_item_specific_fact": "That this exact sequence is CrtA, a spheroidene monooxygenase associated with spheroidene and carotenoid biosynthesis.",
    "reason": "The reviewer-only matched-sequence annotation supports the expected pathway, but that protein-specific identity and function are not supplied in the question. Inferring them from the raw sequence would depend on an external database or protein-specific knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available matched-sequence annotation supports carotenoid biosynthesis; no alternative listed pathway is comparably supported by the evidence."
  },
  "important_caveats": [
    "The pathway annotation is marked as transferred by similarity (ECO:0000250), rather than established here as a direct experimental result for this exact protein.",
    "The author's exact source snapshot is unknown, although the sequence matches both current and historical UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q3J189 (CRTA_CERS4) is annotated as Spheroidene monooxygenase (EC 1.14.15.9) from Cereibacter sphaeroides. The pathway comment explicitly states 'Carotenoid biosynthesis; spheroidene biosynthesis.' The protein name is supported by experimental evidence (PubMed:20851979, ECO:0000303), while the pathway annotation is transferred by similarity to P17055 (ECO:0000250). The EC number assignment is also by similarity. Nonetheless, the experimental paper (Lee et al. 2010, Appl. Environ. Microbiol.) directly characterized the spheroidene monooxygenase activity of CrtA expressed in E. coli, confirming its role in carotenoid/spheroidene biosynthesis. Choice A is well supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a GxGxxG-like motif (MFGSGTGQG) suggestive of a dinucleotide-binding/Rossmann fold, and scattered Glu/His residues that could indicate a di-iron carboxylate monooxygenase active site. However, these features are shared across many oxidoreductase families. The C-terminal proline/alanine-rich linker is unusual but not pathway-specific. No sequence feature uniquely points to carotenoid substrates rather than amino-acid or one-carbon metabolites.


**Missing item-specific fact**

> The specific substrate specificity of this di-iron monooxygenase for spheroidene (a carotenoid) cannot be inferred from sequence alone. Distinguishing carotenoid biosynthesis from amino-acid degradation or one-carbon metabolism requires knowing that this particular enzyme is CrtA/spheroidene monooxygenase, whose substrate pocket accommodates the C40 carotenoid spheroidene—a fact established experimentally (Lee et al. 2010) and not deducible from the ~324-residue sequence without prior identification.


**Reason**

> While one could infer 'monooxygenase' from the GxGxxG motif and metal-binding residues, the leap from 'monooxygenase' to 'carotenoid biosynthesis' (as opposed to amino-acid degradation or one-carbon metabolism, which also employ monooxygenases) requires the specific item-level knowledge that this is CrtA acting on spheroidene. No general biological reasoning from the sequence alone meaningfully eliminates choices B, C, or D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the confirmed identity of the protein as spheroidene monooxygenase, only choice A is correct. The other options (one-carbon metabolism, amino-acid degradation, LPS O-antigen biosynthesis) are not pathways in which CrtA functions. There is no genuine ambiguity in the correct answer, though without protein identification the question is effectively unanswerable by reasoning.


### Important caveats

- The pathway annotation in UniProt (ECO:0000250) is transferred by similarity to P17055 (Rhodobacter capsulatus CrtA), not independently derived for this entry. However, the experimental paper (PubMed:20851979) directly demonstrated spheroidene monooxygenase activity of CrtA from R. sphaeroides.
- The sequence-match is confirmed (SHA256 identical between benchmark and UniProt entry Q3J189, sequence version 1).
- The proline-rich C-terminal region (~120 residues) is unusual for a monooxygenase and its functional role is not annotated; it does not aid pathway assignment.
- The benchmark provides only the sequence with no organism context, making identification of this as a Rhodobacter/Cereibacter carotenoid enzyme reliant on memorization of the specific entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GxGxxG-like motif (MFGSGTGQG) suggestive of a dinucleotide-binding/Rossmann fold, and scattered Glu/His residues that could indicate a di-iron carboxylate monooxygenase active site. However, these features are shared across many oxidoreductase families. The C-terminal proline/alanine-rich linker is unusual but not pathway-specific. No sequence feature uniquely points to carotenoid substrates rather than amino-acid or one-carbon metabolites.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this di-iron monooxygenase for spheroidene (a carotenoid) cannot be inferred from sequence alone. Distinguishing carotenoid biosynthesis from amino-acid degradation or one-carbon metabolism requires knowing that this particular enzyme is CrtA/spheroidene monooxygenase, whose substrate pocket accommodates the C40 carotenoid spheroidene—a fact established experimentally (Lee et al. 2010) and not deducible from the ~324-residue sequence without prior identification.",
    "reason": "While one could infer 'monooxygenase' from the GxGxxG motif and metal-binding residues, the leap from 'monooxygenase' to 'carotenoid biosynthesis' (as opposed to amino-acid degradation or one-carbon metabolism, which also employ monooxygenases) requires the specific item-level knowledge that this is CrtA acting on spheroidene. No general biological reasoning from the sequence alone meaningfully eliminates choices B, C, or D."
  },
  "case_id": "pathway_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q3J189 (CRTA_CERS4) is annotated as Spheroidene monooxygenase (EC 1.14.15.9) from Cereibacter sphaeroides. The pathway comment explicitly states 'Carotenoid biosynthesis; spheroidene biosynthesis.' The protein name is supported by experimental evidence (PubMed:20851979, ECO:0000303), while the pathway annotation is transferred by similarity to P17055 (ECO:0000250). The EC number assignment is also by similarity. Nonetheless, the experimental paper (Lee et al. 2010, Appl. Environ. Microbiol.) directly characterized the spheroidene monooxygenase activity of CrtA expressed in E. coli, confirming its role in carotenoid/spheroidene biosynthesis. Choice A is well supported."
  },
  "important_caveats": [
    "The pathway annotation in UniProt (ECO:0000250) is transferred by similarity to P17055 (Rhodobacter capsulatus CrtA), not independently derived for this entry. However, the experimental paper (PubMed:20851979) directly demonstrated spheroidene monooxygenase activity of CrtA from R. sphaeroides.",
    "The sequence-match is confirmed (SHA256 identical between benchmark and UniProt entry Q3J189, sequence version 1).",
    "The proline-rich C-terminal region (~120 residues) is unusual for a monooxygenase and its functional role is not annotated; it does not aid pathway assignment.",
    "The benchmark provides only the sequence with no organism context, making identification of this as a Rhodobacter/Cereibacter carotenoid enzyme reliant on memorization of the specific entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the confirmed identity of the protein as spheroidene monooxygenase, only choice A is correct. The other options (one-carbon metabolism, amino-acid degradation, LPS O-antigen biosynthesis) are not pathways in which CrtA functions. There is no genuine ambiguity in the correct answer, though without protein identification the question is effectively unanswerable by reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q3J189 (CRTA_CERS4) is annotated as Spheroidene monooxygenase (EC 1.14.15.9) from Cereibacter sphaeroides. The pathway comment explicitly states 'Carotenoid biosynthesis; spheroidene biosynthesis.' The protein name is supported by experimental evidence (PubMed:20851979, ECO:0000303), while the pathway annotation is transferred by similarity to P17055 (ECO:0000250). The EC number assignment is also by similarity. Nonetheless, the experimental paper (Lee et al. 2010, Appl. Environ. Microbiol.) directly characterized the spheroidene monooxygenase activity of CrtA expressed in E. coli, confirming its role in carotenoid/spheroidene biosynthesis. Choice A is well supported.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a GxGxxG-like motif (MFGSGTGQG) suggestive of a dinucleotide-binding/Rossmann fold, and scattered Glu/His residues that could indicate a di-iron carboxylate monooxygenase active site. However, these features are shared across many oxidoreductase families. The C-terminal proline/alanine-rich linker is unusual but not pathway-specific. No sequence feature uniquely points to carotenoid substrates rather than amino-acid or one-carbon metabolites.",
    "missing_item_specific_fact": "The specific substrate specificity of this di-iron monooxygenase for spheroidene (a carotenoid) cannot be inferred from sequence alone. Distinguishing carotenoid biosynthesis from amino-acid degradation or one-carbon metabolism requires knowing that this particular enzyme is CrtA/spheroidene monooxygenase, whose substrate pocket accommodates the C40 carotenoid spheroidene—a fact established experimentally (Lee et al. 2010) and not deducible from the ~324-residue sequence without prior identification.",
    "reason": "While one could infer 'monooxygenase' from the GxGxxG motif and metal-binding residues, the leap from 'monooxygenase' to 'carotenoid biosynthesis' (as opposed to amino-acid degradation or one-carbon metabolism, which also employ monooxygenases) requires the specific item-level knowledge that this is CrtA acting on spheroidene. No general biological reasoning from the sequence alone meaningfully eliminates choices B, C, or D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the confirmed identity of the protein as spheroidene monooxygenase, only choice A is correct. The other options (one-carbon metabolism, amino-acid degradation, LPS O-antigen biosynthesis) are not pathways in which CrtA functions. There is no genuine ambiguity in the correct answer, though without protein identification the question is effectively unanswerable by reasoning."
  },
  "important_caveats": [
    "The pathway annotation in UniProt (ECO:0000250) is transferred by similarity to P17055 (Rhodobacter capsulatus CrtA), not independently derived for this entry. However, the experimental paper (PubMed:20851979) directly demonstrated spheroidene monooxygenase activity of CrtA from R. sphaeroides.",
    "The sequence-match is confirmed (SHA256 identical between benchmark and UniProt entry Q3J189, sequence version 1).",
    "The proline-rich C-terminal region (~120 residues) is unusual for a monooxygenase and its functional role is not annotated; it does not aid pathway assignment.",
    "The benchmark provides only the sequence with no organism context, making identification of this as a Rhodobacter/Cereibacter carotenoid enzyme reliant on memorization of the specific entry."
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

**Accession:** `Q3J189` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 74. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.651114+00:00.  

```json
"Q3J189"
```

Source SHA-256: `bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.651114+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P17055","source":"UniProtKB"}],"value":"1.14.15.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20851979","source":"PubMed"}],"value":"Spheroidene monooxygenase"}}}
```

Source SHA-256: `bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)  
**Locator:** `/comments/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.651114+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P17055","source":"UniProtKB"}],"value":"Carotenoid biosynthesis; spheroidene biosynthesis"}]}
```

Source SHA-256: `bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.651114+00:00.  

```json
{"citation":{"authors":["Lee P.C.","Holtzapple E.","Schmidt-Dannert C."],"citationCrossReferences":[{"database":"PubMed","id":"20851979"},{"database":"DOI","id":"10.1128/aem.01606-10"}],"citationType":"journal article","firstPage":"7328","id":"20851979","journal":"Appl. Environ. Microbiol.","lastPage":"7331","publicationDate":"2010","title":"Novel activity of Rhodobacter sphaeroides spheroidene monooxygenase CrtA expressed in Escherichia coli.","volume":"76"},"referenceNumber":3,"referencePositions":["FUNCTION","COFACTOR","SUBSTRATE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:30:50.636898+00:00.  

```text
ID   CRTA_CERS4              Reviewed;         324 AA.
AC   Q3J189; Q54790;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   08-NOV-2005, sequence version 1.
DT   28-JAN-2026, entry version 74.
DE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:20851979};
DE            EC=1.14.15.9 {ECO:0000250|UniProtKB:P17055};
GN   Name=crtA {ECO:0000303|PubMed:7721699};
GN   OrderedLocusNames=RHOS4_18770 {ECO:0000305};
GN   ORFNames=RSP_0272 {ECO:0000312|EMBL:ABA79445.1};
OS   Cereibacter sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG
OS   31486 / LMG 2827 / NBRC 12203 / NCIMB 8253 / ATH 2.4.1.) (Rhodobacter
OS   sphaeroides).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;
OC   Rhodobacterales; Paracoccaceae; Cereibacter.
OX   NCBI_TaxID=272943;
```

Source SHA-256: `f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)  
**Locator:** `lines 35-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:30:50.636898+00:00.  

```text
RN   [3]
RP   FUNCTION, COFACTOR, SUBSTRATE SPECIFICITY, AND BIOTECHNOLOGY.
RX   PubMed=20851979; DOI=10.1128/aem.01606-10;
RA   Lee P.C., Holtzapple E., Schmidt-Dannert C.;
RT   "Novel activity of Rhodobacter sphaeroides spheroidene monooxygenase CrtA
RT   expressed in Escherichia coli.";
RL   Appl. Environ. Microbiol. 76:7328-7331(2010).
```

Source SHA-256: `f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)  
**Locator:** `lines 87-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:30:50.636898+00:00.  

```text
CC   -!- PATHWAY: Carotenoid biosynthesis; spheroidene biosynthesis.
CC       {ECO:0000250|UniProtKB:P17055}.
```

Source SHA-256: `f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 199. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
