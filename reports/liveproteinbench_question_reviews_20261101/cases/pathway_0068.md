# pathway_0068

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Amino-acid degradation. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIETPYLLFLGDAPDMLAAKVAIGIRDWRPDHAVGQISLPGCGANLGLTEMTLEEAKAAGAKTLVIGVANRGGKISQEWKKVLVQALEEGFDLASGLHNLLRDEPDLAAVAEATGRTLHDVRVPSVQYPIADGVKRRGKRCLAVGTDCSVGKMYTALAMDAEMQARGIKSTFRATGQTGILITGDGVPLDAVIADFMAGSIEYLTPDNDDDHWDLIEGQGSLFHVSYSGVTMALVHGGQPDALILCHEPTRTHMRGLPDYDVPSLEELRDVALPLAQRANKDCKIVGISVNTQHLGEEEAVAYLKEVEGRMGLPAVDPYRHGAGRLVDALAAV

[Multiple Choices]
A. Secondary metabolite biosynthesis. .
B. CoA from (R)-pantothenate: step 3/5. .
C. N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2. .
D. Amino-acid degradation. .
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

> The exact sequence matches the UniProt entry for D-glutamate N-acetyltransferase, whose pathway annotation is amino-acid degradation. The entry cites a study reporting function and catalytic activity, though its pathway field is a database annotation rather than a direct experimental measurement of pathway membership.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently specific, defensible distinction among the listed pathways; identifying the enzyme's substrate specificity and function is needed.


**Missing item-specific fact**

> The protein-specific identification as D-glutamate N-acetyltransferase and its associated pathway assignment.


**Reason**

> The supplied input gives only sequence and pathway choices. The exact functional annotation needed to select amino-acid degradation is absent; recognizing the sequence from an external database would be lookup, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports D for this sequence; it does not establish another listed option as equally defensible.


### Important caveats

- The reviewer-only database evidence was not supplied to the evaluated model.
- The sequence match is exact, but the author's source snapshot is unknown.
- The cited study is evidence for reported experimental function and catalytic activity; the pathway label itself is a curated annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific, defensible distinction among the listed pathways; identifying the enzyme's substrate specificity and function is needed.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as D-glutamate N-acetyltransferase and its associated pathway assignment.",
    "reason": "The supplied input gives only sequence and pathway choices. The exact functional annotation needed to select amino-acid degradation is absent; recognizing the sequence from an external database would be lookup, not reasoning from the supplied information."
  },
  "case_id": "pathway_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for D-glutamate N-acetyltransferase, whose pathway annotation is amino-acid degradation. The entry cites a study reporting function and catalytic activity, though its pathway field is a database annotation rather than a direct experimental measurement of pathway membership."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not supplied to the evaluated model.",
    "The sequence match is exact, but the author's source snapshot is unknown.",
    "The cited study is evidence for reported experimental function and catalytic activity; the pathway label itself is a curated annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D for this sequence; it does not establish another listed option as equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for D-glutamate N-acetyltransferase, whose pathway annotation is amino-acid degradation. The entry cites a study reporting function and catalytic activity, though its pathway field is a database annotation rather than a direct experimental measurement of pathway membership.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific, defensible distinction among the listed pathways; identifying the enzyme's substrate specificity and function is needed.",
    "missing_item_specific_fact": "The protein-specific identification as D-glutamate N-acetyltransferase and its associated pathway assignment.",
    "reason": "The supplied input gives only sequence and pathway choices. The exact functional annotation needed to select amino-acid degradation is absent; recognizing the sequence from an external database would be lookup, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D for this sequence; it does not establish another listed option as equally defensible."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not supplied to the evaluated model.",
    "The sequence match is exact, but the author's source snapshot is unknown.",
    "The cited study is evidence for reported experimental function and catalytic activity; the pathway label itself is a curated annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A2T1AE85 (sequence matched exactly, 333 AA) annotates this protein as D-glutamate N-acetyltransferase (EC 2.3.1.312) with the pathway 'Amino-acid degradation' backed by experimental evidence (ECO:0000305|PubMed:36690779, a 2023 ISME J. paper on a novel D-glutamate catabolic pathway, with X-ray crystallography at 2.20 Å, mutagenesis, and catalytic activity data). The expected answer D matches the UniProt pathway annotation verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a GNAT-fold acetyltransferase signature (VANRGGKISQ… pattern, conserved GNAT motifs), which narrows the enzyme to an acetyltransferase. However, GNAT acetyltransferases participate in many pathways including secondary metabolite biosynthesis, amino-acid modification, and others. Distinguishing 'Amino-acid degradation' (D) from 'Secondary metabolite biosynthesis' (A) requires knowing the specific substrate is D-glutamate—an unusual D-stereoisomer of glutamate acetylated as part of a novel catabolic route reported in 2023. No general biological reasoning from the sequence alone can establish that this particular GNAT enzyme acetylates D-glutamate rather than a secondary-metabolite precursor.


**Missing item-specific fact**

> The specific substrate identity (D-glutamate) and the fact that this enzyme participates in a novel D-glutamate catabolic pathway (Yu et al., ISME J. 2023, PDB 7XRJ) are protein-specific experimental findings not derivable from sequence-level general knowledge. Without this annotation, a GNAT acetyltransferase could plausibly be assigned to secondary metabolite biosynthesis.


**Reason**

> The GNAT fold is shared across dozens of pathways. The critical distinguishing fact—that this enzyme specifically acetylates D-glutamate as a step in amino-acid catabolism—was established experimentally in 2023 and is an item-specific database/experimental annotation. A model would need to recognize this exact protein or its close homologs to select D over A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Option A (Secondary metabolite biosynthesis) is a plausible alternative for a GNAT-family acetyltransferase, as many GNAT enzymes acetylate intermediates in secondary metabolite assembly (e.g., aminoglycoside modification, polyketide/NRPS tailoring). Without knowing the substrate is D-glutamate, a reasoning-based model could defensibly select A. Options B and C are clearly inappropriate for a GNAT acetyltransferase and serve as easy distractors.


### Important caveats

- The UniProt entry was first publicly released 2025-04-09; the underlying pathway paper is from 2023. Depending on the benchmark construction date, this annotation may or may not have been available in training data.
- The pathway annotation uses evidence code ECO:0000305 (curator inference from the primary publication), supported by X-ray crystallography and mutagenesis data (ECO:0007744, PDB 7XRJ), so it is experimentally grounded.
- The sequence is 333 AA and matches the UniProt entry exactly (SHA-256 confirmed in both current and historical snapshots).
- The 'novel' nature of the D-glutamate catabolic pathway (2023) means this enzyme was not annotated in most databases before that publication, increasing lookup dependence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GNAT-fold acetyltransferase signature (VANRGGKISQ… pattern, conserved GNAT motifs), which narrows the enzyme to an acetyltransferase. However, GNAT acetyltransferases participate in many pathways including secondary metabolite biosynthesis, amino-acid modification, and others. Distinguishing 'Amino-acid degradation' (D) from 'Secondary metabolite biosynthesis' (A) requires knowing the specific substrate is D-glutamate—an unusual D-stereoisomer of glutamate acetylated as part of a novel catabolic route reported in 2023. No general biological reasoning from the sequence alone can establish that this particular GNAT enzyme acetylates D-glutamate rather than a secondary-metabolite precursor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (D-glutamate) and the fact that this enzyme participates in a novel D-glutamate catabolic pathway (Yu et al., ISME J. 2023, PDB 7XRJ) are protein-specific experimental findings not derivable from sequence-level general knowledge. Without this annotation, a GNAT acetyltransferase could plausibly be assigned to secondary metabolite biosynthesis.",
    "reason": "The GNAT fold is shared across dozens of pathways. The critical distinguishing fact—that this enzyme specifically acetylates D-glutamate as a step in amino-acid catabolism—was established experimentally in 2023 and is an item-specific database/experimental annotation. A model would need to recognize this exact protein or its close homologs to select D over A."
  },
  "case_id": "pathway_0068",
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
    "reason": "The UniProt entry A0A2T1AE85 (sequence matched exactly, 333 AA) annotates this protein as D-glutamate N-acetyltransferase (EC 2.3.1.312) with the pathway 'Amino-acid degradation' backed by experimental evidence (ECO:0000305|PubMed:36690779, a 2023 ISME J. paper on a novel D-glutamate catabolic pathway, with X-ray crystallography at 2.20 Å, mutagenesis, and catalytic activity data). The expected answer D matches the UniProt pathway annotation verbatim."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released 2025-04-09; the underlying pathway paper is from 2023. Depending on the benchmark construction date, this annotation may or may not have been available in training data.",
    "The pathway annotation uses evidence code ECO:0000305 (curator inference from the primary publication), supported by X-ray crystallography and mutagenesis data (ECO:0007744, PDB 7XRJ), so it is experimentally grounded.",
    "The sequence is 333 AA and matches the UniProt entry exactly (SHA-256 confirmed in both current and historical snapshots).",
    "The 'novel' nature of the D-glutamate catabolic pathway (2023) means this enzyme was not annotated in most databases before that publication, increasing lookup dependence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Option A (Secondary metabolite biosynthesis) is a plausible alternative for a GNAT-family acetyltransferase, as many GNAT enzymes acetylate intermediates in secondary metabolite assembly (e.g., aminoglycoside modification, polyketide/NRPS tailoring). Without knowing the substrate is D-glutamate, a reasoning-based model could defensibly select A. Options B and C are clearly inappropriate for a GNAT acetyltransferase and serve as easy distractors."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A2T1AE85 (sequence matched exactly, 333 AA) annotates this protein as D-glutamate N-acetyltransferase (EC 2.3.1.312) with the pathway 'Amino-acid degradation' backed by experimental evidence (ECO:0000305|PubMed:36690779, a 2023 ISME J. paper on a novel D-glutamate catabolic pathway, with X-ray crystallography at 2.20 Å, mutagenesis, and catalytic activity data). The expected answer D matches the UniProt pathway annotation verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a GNAT-fold acetyltransferase signature (VANRGGKISQ… pattern, conserved GNAT motifs), which narrows the enzyme to an acetyltransferase. However, GNAT acetyltransferases participate in many pathways including secondary metabolite biosynthesis, amino-acid modification, and others. Distinguishing 'Amino-acid degradation' (D) from 'Secondary metabolite biosynthesis' (A) requires knowing the specific substrate is D-glutamate—an unusual D-stereoisomer of glutamate acetylated as part of a novel catabolic route reported in 2023. No general biological reasoning from the sequence alone can establish that this particular GNAT enzyme acetylates D-glutamate rather than a secondary-metabolite precursor.",
    "missing_item_specific_fact": "The specific substrate identity (D-glutamate) and the fact that this enzyme participates in a novel D-glutamate catabolic pathway (Yu et al., ISME J. 2023, PDB 7XRJ) are protein-specific experimental findings not derivable from sequence-level general knowledge. Without this annotation, a GNAT acetyltransferase could plausibly be assigned to secondary metabolite biosynthesis.",
    "reason": "The GNAT fold is shared across dozens of pathways. The critical distinguishing fact—that this enzyme specifically acetylates D-glutamate as a step in amino-acid catabolism—was established experimentally in 2023 and is an item-specific database/experimental annotation. A model would need to recognize this exact protein or its close homologs to select D over A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Option A (Secondary metabolite biosynthesis) is a plausible alternative for a GNAT-family acetyltransferase, as many GNAT enzymes acetylate intermediates in secondary metabolite assembly (e.g., aminoglycoside modification, polyketide/NRPS tailoring). Without knowing the substrate is D-glutamate, a reasoning-based model could defensibly select A. Options B and C are clearly inappropriate for a GNAT acetyltransferase and serve as easy distractors."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released 2025-04-09; the underlying pathway paper is from 2023. Depending on the benchmark construction date, this annotation may or may not have been available in training data.",
    "The pathway annotation uses evidence code ECO:0000305 (curator inference from the primary publication), supported by X-ray crystallography and mutagenesis data (ECO:0007744, PDB 7XRJ), so it is experimentally grounded.",
    "The sequence is 333 AA and matches the UniProt entry exactly (SHA-256 confirmed in both current and historical snapshots).",
    "The 'novel' nature of the D-glutamate catabolic pathway (2023) means this enzyme was not annotated in most databases before that publication, increasing lookup dependence."
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

**Accession:** `A0A2T1AE85` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 17. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.195751+00:00.  

```json
"A0A2T1AE85"
```

Source SHA-256: `09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.195751+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"value":"2.3.1.312"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"D-glutamate N-acetyltransferase"}}}
```

Source SHA-256: `09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.195751+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"36690779","source":"PubMed"}],"value":"Amino-acid degradation"}]}
```

Source SHA-256: `09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.195751+00:00.  

```json
{"citation":{"authors":["Yu Y.","Wang P.","Cao H.Y.","Teng Z.J.","Zhu Y.","Wang M.","McMinn A.","Chen Y.","Xiang H.","Zhang Y.Z.","Chen X.L.","Zhang Y.Q."],"citationCrossReferences":[{"database":"PubMed","id":"36690779"},{"database":"DOI","id":"10.1038/s41396-023-01364-6"}],"citationType":"journal article","firstPage":"537","id":"36690779","journal":"ISME J.","lastPage":"548","publicationDate":"2023","title":"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.","volume":"17"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7XRJ","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 25328 / CCUG 55858 / LMG 24367 / R-28751"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190"]}
```

Source SHA-256: `09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:24:54.258050+00:00.  

```text
ID   DGCN_TRISK              Reviewed;         333 AA.
AC   A0A2T1AE85;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUL-2018, sequence version 1.
DT   28-JAN-2026, entry version 17.
DE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};
DE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};
GN   Name=dgcN {ECO:0000303|PubMed:36690779};
GN   ORFNames=CLV89_10851 {ECO:0000312|EMBL:PRZ46905.1};
OS   Tritonibacter scottomollicae (Epibacterium scottomollicae).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;
OC   Rhodobacterales; Paracoccaceae; Tritonibacter.
OX   NCBI_TaxID=483013;
```

Source SHA-256: `4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)  
**Locator:** `lines 21-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:24:54.258050+00:00.  

```text
RN   [2] {ECO:0007744|PDB:7XRJ}
RP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY, AND
RP   MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190.
RC   STRAIN=DSM 25328 / CCUG 55858 / LMG 24367 / R-28751;
RX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;
RA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,
RA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;
RT   "Novel D-glutamate catabolic pathway in marine Proteobacteria and
RT   halophilic archaea.";
RL   ISME J. 17:537-548(2023).
```

Source SHA-256: `4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)  
**Locator:** `lines 43-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:24:54.258050+00:00.  

```text
CC   -!- PATHWAY: Amino-acid degradation. {ECO:0000305|PubMed:36690779}.
```

Source SHA-256: `4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 68. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
