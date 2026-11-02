# pathway_0122

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Purine metabolism

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MCGVLALILANQSSSAANDLHEALYVLQHRGQDAAGIATSTSSGHIHIRKKNGMAADVFQSGARLANLFGSMGIAHLRYPTAGGSANTEAQPFYVNSPYGICFAHNGNLINTVELRRYLDFEIHRHINSDSDSELMLNIFADELSETKKARVNTEDIFNGLSKMYQRCEGAWACTAMLAGFGVIGFRDAYGIRPLVMGSRPSSDGDGLDYMIASESIALDRLGFTNVRDIQPGEAVIVAKGAEPVFCQVAPRKSYTPDLFEYVYFARPDSVIDGISVYQSRQRMGRYLAARLLEVLGPEGIKEIDVVIPVPETSSPAAASVAHALNKPYCAGYIRNPYVFRTFIMPGQATRQKGVRRKLSAVKEEFKNRTILLVDDSIARGTTSREAISMAREAGVKKIIAACCSPEITYPHIYGIDLPSPHEMVAYERDNNDIAQNLGADRIVYQTLEDLQASCAEIARENDFQEPHTFENGVFSGQYVTPVPEGYFALLEKIRGTGRKEALDKSSKRL

[Multiple Choices]
A. Purine metabolism
B. Cofactor biosynthesis
C. CoA from (R)-pantothenate: step 3/5. .
D. peptidoglycan biosynthesis. .
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

> The exact sequence matches a UniProt entry annotated as phosphoribosylpyrophosphate amidotransferase FrzK (EC 2.4.2.14), with a pathway annotation placing it in de novo purine/IMP biosynthesis. The enzyme annotation cites functional evidence; the pathway annotation is separately marked as curated evidence, so it should not be treated as a direct experimental measurement of pathway membership.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Identifying a glutamine-dependent phosphoribosylpyrophosphate amidotransferase from the sequence would point toward de novo purine biosynthesis, but the input does not provide that protein-family or enzyme identification.


**Missing item-specific fact**

> The protein-specific assignment of this sequence to phosphoribosylpyrophosphate amidotransferase FrzK and its associated pathway is needed to select A.


**Reason**

> The raw sequence and choices do not directly state the enzyme function or pathway. Distinguishing A relies on identifying this particular sequence through domain/homology knowledge or an external annotation; simply recalling or retrieving its database entry is not reasoning supplied by the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports purine metabolism; no supplied evidence supports another listed pathway.


### Important caveats

- The historical and current records both match the supplied sequence, but the author's exact source snapshot is unknown.
- The pathway annotation is curated evidence (ECO:0000305), while the enzyme EC annotation cites functional evidence (ECO:0000269); these evidence types should not be conflated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Identifying a glutamine-dependent phosphoribosylpyrophosphate amidotransferase from the sequence would point toward de novo purine biosynthesis, but the input does not provide that protein-family or enzyme identification.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of this sequence to phosphoribosylpyrophosphate amidotransferase FrzK and its associated pathway is needed to select A.",
    "reason": "The raw sequence and choices do not directly state the enzyme function or pathway. Distinguishing A relies on identifying this particular sequence through domain/homology knowledge or an external annotation; simply recalling or retrieving its database entry is not reasoning supplied by the question."
  },
  "case_id": "pathway_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as phosphoribosylpyrophosphate amidotransferase FrzK (EC 2.4.2.14), with a pathway annotation placing it in de novo purine/IMP biosynthesis. The enzyme annotation cites functional evidence; the pathway annotation is separately marked as curated evidence, so it should not be treated as a direct experimental measurement of pathway membership."
  },
  "important_caveats": [
    "The historical and current records both match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The pathway annotation is curated evidence (ECO:0000305), while the enzyme EC annotation cites functional evidence (ECO:0000269); these evidence types should not be conflated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports purine metabolism; no supplied evidence supports another listed pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as phosphoribosylpyrophosphate amidotransferase FrzK (EC 2.4.2.14), with a pathway annotation placing it in de novo purine/IMP biosynthesis. The enzyme annotation cites functional evidence; the pathway annotation is separately marked as curated evidence, so it should not be treated as a direct experimental measurement of pathway membership.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Identifying a glutamine-dependent phosphoribosylpyrophosphate amidotransferase from the sequence would point toward de novo purine biosynthesis, but the input does not provide that protein-family or enzyme identification.",
    "missing_item_specific_fact": "The protein-specific assignment of this sequence to phosphoribosylpyrophosphate amidotransferase FrzK and its associated pathway is needed to select A.",
    "reason": "The raw sequence and choices do not directly state the enzyme function or pathway. Distinguishing A relies on identifying this particular sequence through domain/homology knowledge or an external annotation; simply recalling or retrieving its database entry is not reasoning supplied by the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports purine metabolism; no supplied evidence supports another listed pathway."
  },
  "important_caveats": [
    "The historical and current records both match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The pathway annotation is curated evidence (ECO:0000305), while the enzyme EC annotation cites functional evidence (ECO:0000269); these evidence types should not be conflated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (A0A7T8J1U7, sequence matched exactly) explicitly states the pathway as 'Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2' with evidence code ECO:0000305 from PubMed:33372776. The enzyme is named Phosphoribosylpyrophosphate amidotransferase FrzK (EC 2.4.2.14), which catalyzes the first committed step of de novo purine biosynthesis. Choice A 'Purine metabolism' directly matches this annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable class I glutamine amidotransferase (GAT) domain motif (the 'GAWACT' sequence around residues ~140-150) combined with a PRPP-binding domain architecture in a single polypeptide. This GAT + PRPP-binding tandem arrangement is the hallmark structural signature of phosphoribosylpyrophosphate amidotransferase (PurF-type), which catalyzes the first committed step of de novo purine (IMP) biosynthesis. Peptidoglycan biosynthesis (D) involves Mur ligases/transpeptidases with entirely different domain architectures. CoA biosynthesis from pantothenate (C) involves pantothenate kinase, phosphopantothenate synthetase, and CoA synthase — none of which are GAT+PRPP enzymes. Cofactor biosynthesis (B) is vague but GAT+PRPP single-chain enzymes are not characteristic of common cofactor pathways (NAD, FAD, etc.).


**Missing item-specific fact**

> None strictly required. The domain-architecture argument (GAT motif + PRPP-binding domain in one polypeptide → PurF-type → purine biosynthesis) is general biochemistry. A model would not need to recall the specific UniProt entry or the FR901483 paper.


**Reason**

> A biologist familiar with amidotransferase domain families can identify the GAWACT GAT motif and the PRPP-binding fold in the sequence, then use the well-established rule that a single-chain GAT+PRPP enzyme is a phosphoribosylpyrophosphate amidotransferase functioning in de novo purine biosynthesis. The distractors are eliminated by incompatible domain architectures. This constitutes concrete reasoning from sequence features rather than memorization of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices target distinct biochemical pathways with incompatible enzyme architectures. The GAT+PRPP single-polypeptide signature specifically points to purine biosynthesis and does not fit peptidoglycan, CoA-from-pantothenate, or generic cofactor pathways. The protein's role in FR901483 natural-product biosynthesis is not offered as a distractor, so no ambiguity arises from its dual annotation context.


### Important caveats

- The protein was originally characterized in the FR901483 immunosuppressant biosynthesis cluster (PubMed:33372776). Its biological role in Cladobotryum sp. may be specifically for FR901483 biosynthesis rather than general purine metabolism, but UniProt and the EC classification place it under 'Purine metabolism' because the catalytic reaction (PRPP → 5-phospho-β-D-ribosylamine) is the same purine-biosynthetic step.
- The GAT domain is shared across many amidotransferases (HisH, TrpG, PyrG, etc.); the specific assignment to purine biosynthesis relies on recognizing the PRPP-binding domain co-occurrence, which is a well-established but non-trivial inference.
- All reviewer evidence is from UniProt annotation (ECO:0000305 curator inference from publication); no independent enzymatic assay data was provided in the evidence excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable class I glutamine amidotransferase (GAT) domain motif (the 'GAWACT' sequence around residues ~140-150) combined with a PRPP-binding domain architecture in a single polypeptide. This GAT + PRPP-binding tandem arrangement is the hallmark structural signature of phosphoribosylpyrophosphate amidotransferase (PurF-type), which catalyzes the first committed step of de novo purine (IMP) biosynthesis. Peptidoglycan biosynthesis (D) involves Mur ligases/transpeptidases with entirely different domain architectures. CoA biosynthesis from pantothenate (C) involves pantothenate kinase, phosphopantothenate synthetase, and CoA synthase — none of which are GAT+PRPP enzymes. Cofactor biosynthesis (B) is vague but GAT+PRPP single-chain enzymes are not characteristic of common cofactor pathways (NAD, FAD, etc.).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The domain-architecture argument (GAT motif + PRPP-binding domain in one polypeptide → PurF-type → purine biosynthesis) is general biochemistry. A model would not need to recall the specific UniProt entry or the FR901483 paper.",
    "reason": "A biologist familiar with amidotransferase domain families can identify the GAWACT GAT motif and the PRPP-binding fold in the sequence, then use the well-established rule that a single-chain GAT+PRPP enzyme is a phosphoribosylpyrophosphate amidotransferase functioning in de novo purine biosynthesis. The distractors are eliminated by incompatible domain architectures. This constitutes concrete reasoning from sequence features rather than memorization of a database entry."
  },
  "case_id": "pathway_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (A0A7T8J1U7, sequence matched exactly) explicitly states the pathway as 'Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2' with evidence code ECO:0000305 from PubMed:33372776. The enzyme is named Phosphoribosylpyrophosphate amidotransferase FrzK (EC 2.4.2.14), which catalyzes the first committed step of de novo purine biosynthesis. Choice A 'Purine metabolism' directly matches this annotation."
  },
  "important_caveats": [
    "The protein was originally characterized in the FR901483 immunosuppressant biosynthesis cluster (PubMed:33372776). Its biological role in Cladobotryum sp. may be specifically for FR901483 biosynthesis rather than general purine metabolism, but UniProt and the EC classification place it under 'Purine metabolism' because the catalytic reaction (PRPP → 5-phospho-β-D-ribosylamine) is the same purine-biosynthetic step.",
    "The GAT domain is shared across many amidotransferases (HisH, TrpG, PyrG, etc.); the specific assignment to purine biosynthesis relies on recognizing the PRPP-binding domain co-occurrence, which is a well-established but non-trivial inference.",
    "All reviewer evidence is from UniProt annotation (ECO:0000305 curator inference from publication); no independent enzymatic assay data was provided in the evidence excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices target distinct biochemical pathways with incompatible enzyme architectures. The GAT+PRPP single-polypeptide signature specifically points to purine biosynthesis and does not fit peptidoglycan, CoA-from-pantothenate, or generic cofactor pathways. The protein's role in FR901483 natural-product biosynthesis is not offered as a distractor, so no ambiguity arises from its dual annotation context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (A0A7T8J1U7, sequence matched exactly) explicitly states the pathway as 'Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2' with evidence code ECO:0000305 from PubMed:33372776. The enzyme is named Phosphoribosylpyrophosphate amidotransferase FrzK (EC 2.4.2.14), which catalyzes the first committed step of de novo purine biosynthesis. Choice A 'Purine metabolism' directly matches this annotation.",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable class I glutamine amidotransferase (GAT) domain motif (the 'GAWACT' sequence around residues ~140-150) combined with a PRPP-binding domain architecture in a single polypeptide. This GAT + PRPP-binding tandem arrangement is the hallmark structural signature of phosphoribosylpyrophosphate amidotransferase (PurF-type), which catalyzes the first committed step of de novo purine (IMP) biosynthesis. Peptidoglycan biosynthesis (D) involves Mur ligases/transpeptidases with entirely different domain architectures. CoA biosynthesis from pantothenate (C) involves pantothenate kinase, phosphopantothenate synthetase, and CoA synthase — none of which are GAT+PRPP enzymes. Cofactor biosynthesis (B) is vague but GAT+PRPP single-chain enzymes are not characteristic of common cofactor pathways (NAD, FAD, etc.).",
    "missing_item_specific_fact": "None strictly required. The domain-architecture argument (GAT motif + PRPP-binding domain in one polypeptide → PurF-type → purine biosynthesis) is general biochemistry. A model would not need to recall the specific UniProt entry or the FR901483 paper.",
    "reason": "A biologist familiar with amidotransferase domain families can identify the GAWACT GAT motif and the PRPP-binding fold in the sequence, then use the well-established rule that a single-chain GAT+PRPP enzyme is a phosphoribosylpyrophosphate amidotransferase functioning in de novo purine biosynthesis. The distractors are eliminated by incompatible domain architectures. This constitutes concrete reasoning from sequence features rather than memorization of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices target distinct biochemical pathways with incompatible enzyme architectures. The GAT+PRPP single-polypeptide signature specifically points to purine biosynthesis and does not fit peptidoglycan, CoA-from-pantothenate, or generic cofactor pathways. The protein's role in FR901483 natural-product biosynthesis is not offered as a distractor, so no ambiguity arises from its dual annotation context."
  },
  "important_caveats": [
    "The protein was originally characterized in the FR901483 immunosuppressant biosynthesis cluster (PubMed:33372776). Its biological role in Cladobotryum sp. may be specifically for FR901483 biosynthesis rather than general purine metabolism, but UniProt and the EC classification place it under 'Purine metabolism' because the catalytic reaction (PRPP → 5-phospho-β-D-ribosylamine) is the same purine-biosynthetic step.",
    "The GAT domain is shared across many amidotransferases (HisH, TrpG, PyrG, etc.); the specific assignment to purine biosynthesis relies on recognizing the PRPP-binding domain co-occurrence, which is a well-established but non-trivial inference.",
    "All reviewer evidence is from UniProt annotation (ECO:0000305 curator inference from publication); no independent enzymatic assay data was provided in the evidence excerpts."
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

**Accession:** `A0A7T8J1U7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 16. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:51.826168+00:00.  

```json
"A0A7T8J1U7"
```

Source SHA-256: `56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:51.826168+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis clusters protein K"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Glutamine phosphoribosylpyrophosphate amidotransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"2.4.2.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Phosphoribosylpyrophosphate amidotransferase FrzK"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"ATase FrzK"}]}}
```

Source SHA-256: `56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:51.826168+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33372776","source":"PubMed"}],"value":"Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2"}]}
```

Source SHA-256: `56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-02T04:25:55.036238+00:00.  

```text
ID   FRZK_CLASX              Reviewed;         510 AA.
AC   A0A7T8J1U7;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-JUN-2021, sequence version 1.
DT   28-JAN-2026, entry version 16.
DE   RecName: Full=Phosphoribosylpyrophosphate amidotransferase FrzK {ECO:0000303|PubMed:33372776};
DE            Short=ATase FrzK {ECO:0000303|PubMed:33372776};
DE            EC=2.4.2.14 {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis clusters protein K {ECO:0000303|PubMed:33372776};
DE   AltName: Full=Glutamine phosphoribosylpyrophosphate amidotransferase {ECO:0000303|PubMed:33372776};
GN   Name=FrzK {ECO:0000303|PubMed:33372776};
OS   Cladobotryum sp.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.
OX   NCBI_TaxID=2040732;
```

Source SHA-256: `578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)  
**Locator:** `lines 53-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-02T04:25:55.036238+00:00.  

```text
CC   -!- PATHWAY: Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-
CC       (5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-
CC       diphosphate: step 1/2. {ECO:0000305|PubMed:33372776}.
```

Source SHA-256: `578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 122. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
