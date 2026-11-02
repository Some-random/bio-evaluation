# EC_number_0036

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.1.1.12

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVKPTKSNIGVYTNPAHDLWVAEAEPSLEQVQTGEKLAPGEVTVAVKSTGICGSDVHFWHAGCIGPMIVEDDHILGHESAGVVVAVHENVKSLKVGDRVAIEPNIICGECEPCLTGRYNGCDSVLFRSTPPVPGLLRRYVNHPAMWCHKIGDMSYENGSLLEPLSVALAGVQRAEVRLGDPILVCGAGPIGLVTLACVKAAGAEPIIITDIDEGRLAFAKEFCPSVRTHKVDFKHTPEDFAKAITELGGGVEPAIALECTGVESSIAGAIQTVKFGGKVFVIGVGKNEIKIPFMRLSTREVDLQFQYRYANTWPRAIRLLQGGVINLEKLVTHRFKIEDALEAFKTAADPKTGAIKVQIQSFEEGESR

[Multiple Choices]
A. 1.1.1.12
B. 1.1.1.336
C. 2.3.1.318
D. 2.3.1.319
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

> The exact supplied sequence matches UniProt entry A0A385XI11, which annotates it as L-arabinitol 4-dehydrogenase, EC 1.1.1.12. The EC and catalytic-activity annotations are transferred by similarity from UniProtKB:Q7SI09 (ECO:0000250), rather than shown here as direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may support an enzyme-family or broad oxidoreductase inference, but they do not establish the specific substrate and reaction needed to distinguish EC 1.1.1.12 from the other candidate EC numbers.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental identification of its substrate and catalyzed reaction.


**Reason**

> The supplied sequence and choices do not provide a defensible basis for the exact EC assignment; selecting A requires protein-specific functional information absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports A, while no evidence supplied with the question supports another option. The exact answer is not inferable from the supplied information alone.


### Important caveats

- The sequence match applies to the supplied 368-residue sequence.
- The supporting UniProt EC annotation is similarity-based, not direct experimental confirmation for this protein.
- Reviewer-only database evidence establishes support for the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may support an enzyme-family or broad oxidoreductase inference, but they do not establish the specific substrate and reaction needed to distinguish EC 1.1.1.12 from the other candidate EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of its substrate and catalyzed reaction.",
    "reason": "The supplied sequence and choices do not provide a defensible basis for the exact EC assignment; selecting A requires protein-specific functional information absent from the input."
  },
  "case_id": "EC_number_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches UniProt entry A0A385XI11, which annotates it as L-arabinitol 4-dehydrogenase, EC 1.1.1.12. The EC and catalytic-activity annotations are transferred by similarity from UniProtKB:Q7SI09 (ECO:0000250), rather than shown here as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The sequence match applies to the supplied 368-residue sequence.",
    "The supporting UniProt EC annotation is similarity-based, not direct experimental confirmation for this protein.",
    "Reviewer-only database evidence establishes support for the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports A, while no evidence supplied with the question supports another option. The exact answer is not inferable from the supplied information alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches UniProt entry A0A385XI11, which annotates it as L-arabinitol 4-dehydrogenase, EC 1.1.1.12. The EC and catalytic-activity annotations are transferred by similarity from UniProtKB:Q7SI09 (ECO:0000250), rather than shown here as direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may support an enzyme-family or broad oxidoreductase inference, but they do not establish the specific substrate and reaction needed to distinguish EC 1.1.1.12 from the other candidate EC numbers.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of its substrate and catalyzed reaction.",
    "reason": "The supplied sequence and choices do not provide a defensible basis for the exact EC assignment; selecting A requires protein-specific functional information absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports A, while no evidence supplied with the question supports another option. The exact answer is not inferable from the supplied information alone."
  },
  "important_caveats": [
    "The sequence match applies to the supplied 368-residue sequence.",
    "The supporting UniProt EC annotation is similarity-based, not direct experimental confirmation for this protein.",
    "Reviewer-only database evidence establishes support for the key but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A385XI11 (sequence matched, 368 aa) annotates this protein as L-arabinitol 4-dehydrogenase with EC 1.1.1.12 (evidence IDs C4, C5, H1-H4). The EC assignment carries evidence code ECO:0000250 (transferred by similarity from Q7SI09), while the protein name is supported by PubMed:32003433 (genetic evidence in liamocin biosynthesis context). The catalytic activity (L-arabinitol + NAD+ = L-xylulose + NADH + H+) is consistent with EC 1.1.1.12. The annotation is a database claim via similarity transfer rather than direct experimental characterization of this specific protein, but it is the authoritative current annotation for the matched sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains hallmark short-chain dehydrogenase/reductase (SDR) family motifs: a Rossmann-fold NAD-binding motif (GAGPIGLVTLA, resembling TGxxxGxG), the catalytic tetrad region (TDIDEGRLAF), and a C-terminal RY motif (QYRY). These features are diagnostic of EC 1.1.1.x oxidoreductases and effectively eliminate options C (2.3.1.318) and D (2.3.1.319), which are acyltransferases (EC 2.3.x) lacking NAD-binding and SDR catalytic motifs. This is a genuine reasoning-based discrimination.


**Missing item-specific fact**

> Distinguishing EC 1.1.1.12 (L-arabinitol 4-dehydrogenase) from EC 1.1.1.336 (another CH-OH/NAD+ oxidoreductase, also an SDR) requires knowing the specific substrate and regiochemistry (C4 vs C2 oxidation of L-arabinitol, or a different substrate entirely). Both are SDR-family enzymes with overlapping sequence features. The specific residues in the substrate-binding pocket that determine whether oxidation occurs at C4 vs C2 of L-arabinitol are not identifiable from general biological knowledge without protein-specific annotation or structural data.


**Reason**

> The SDR motifs provide a solid argument to eliminate the two acyltransferase distractors (C, D), narrowing the answer to two oxidoreductase options. However, the final A-vs-B distinction (1.1.1.12 vs 1.1.1.336) hinges on the specific substrate/regiochemistry of this particular enzyme, which is an item-specific annotation fact not derivable from the sequence by general reasoning. Selecting the correct 4-digit EC number among the remaining two SDR dehydrogenases depends on knowing the database annotation or the liamocin biosynthesis pathway context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both EC 1.1.1.12 and EC 1.1.1.336 are CH-OH/NAD+ oxidoreductases within the SDR superfamily. Without the specific substrate-binding pocket analysis or pathway context (liamocin biosynthesis involving L-arabinitol metabolism), a model cannot reliably distinguish which specific dehydrogenase activity this sequence encodes. The SDR motifs confirm EC 1.1.1.x but do not resolve the final digit.


### Important caveats

- The EC 1.1.1.12 annotation is based on similarity transfer (ECO:0000250 from Q7SI09), not direct experimental characterization of A0A385XI11 itself. The PubMed reference (32003433) provides genetic evidence in the liamocin biosynthesis pathway context.
- The UniProt entry was first publicly released on 2025-02-05; the author's source snapshot date is unknown, so the annotation may have been assigned after the benchmark was constructed.
- The sequence-match is exact (SHA256 confirmed) for both current and historical (entry version 21) records.
- The reviewer-only evidence was absent from the evaluated model's input; the model must work from the raw sequence and four choices alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark short-chain dehydrogenase/reductase (SDR) family motifs: a Rossmann-fold NAD-binding motif (GAGPIGLVTLA, resembling TGxxxGxG), the catalytic tetrad region (TDIDEGRLAF), and a C-terminal RY motif (QYRY). These features are diagnostic of EC 1.1.1.x oxidoreductases and effectively eliminate options C (2.3.1.318) and D (2.3.1.319), which are acyltransferases (EC 2.3.x) lacking NAD-binding and SDR catalytic motifs. This is a genuine reasoning-based discrimination.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Distinguishing EC 1.1.1.12 (L-arabinitol 4-dehydrogenase) from EC 1.1.1.336 (another CH-OH/NAD+ oxidoreductase, also an SDR) requires knowing the specific substrate and regiochemistry (C4 vs C2 oxidation of L-arabinitol, or a different substrate entirely). Both are SDR-family enzymes with overlapping sequence features. The specific residues in the substrate-binding pocket that determine whether oxidation occurs at C4 vs C2 of L-arabinitol are not identifiable from general biological knowledge without protein-specific annotation or structural data.",
    "reason": "The SDR motifs provide a solid argument to eliminate the two acyltransferase distractors (C, D), narrowing the answer to two oxidoreductase options. However, the final A-vs-B distinction (1.1.1.12 vs 1.1.1.336) hinges on the specific substrate/regiochemistry of this particular enzyme, which is an item-specific annotation fact not derivable from the sequence by general reasoning. Selecting the correct 4-digit EC number among the remaining two SDR dehydrogenases depends on knowing the database annotation or the liamocin biosynthesis pathway context."
  },
  "case_id": "EC_number_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A385XI11 (sequence matched, 368 aa) annotates this protein as L-arabinitol 4-dehydrogenase with EC 1.1.1.12 (evidence IDs C4, C5, H1-H4). The EC assignment carries evidence code ECO:0000250 (transferred by similarity from Q7SI09), while the protein name is supported by PubMed:32003433 (genetic evidence in liamocin biosynthesis context). The catalytic activity (L-arabinitol + NAD+ = L-xylulose + NADH + H+) is consistent with EC 1.1.1.12. The annotation is a database claim via similarity transfer rather than direct experimental characterization of this specific protein, but it is the authoritative current annotation for the matched sequence."
  },
  "important_caveats": [
    "The EC 1.1.1.12 annotation is based on similarity transfer (ECO:0000250 from Q7SI09), not direct experimental characterization of A0A385XI11 itself. The PubMed reference (32003433) provides genetic evidence in the liamocin biosynthesis pathway context.",
    "The UniProt entry was first publicly released on 2025-02-05; the author's source snapshot date is unknown, so the annotation may have been assigned after the benchmark was constructed.",
    "The sequence-match is exact (SHA256 confirmed) for both current and historical (entry version 21) records.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must work from the raw sequence and four choices alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both EC 1.1.1.12 and EC 1.1.1.336 are CH-OH/NAD+ oxidoreductases within the SDR superfamily. Without the specific substrate-binding pocket analysis or pathway context (liamocin biosynthesis involving L-arabinitol metabolism), a model cannot reliably distinguish which specific dehydrogenase activity this sequence encodes. The SDR motifs confirm EC 1.1.1.x but do not resolve the final digit."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A385XI11 (sequence matched, 368 aa) annotates this protein as L-arabinitol 4-dehydrogenase with EC 1.1.1.12 (evidence IDs C4, C5, H1-H4). The EC assignment carries evidence code ECO:0000250 (transferred by similarity from Q7SI09), while the protein name is supported by PubMed:32003433 (genetic evidence in liamocin biosynthesis context). The catalytic activity (L-arabinitol + NAD+ = L-xylulose + NADH + H+) is consistent with EC 1.1.1.12. The annotation is a database claim via similarity transfer rather than direct experimental characterization of this specific protein, but it is the authoritative current annotation for the matched sequence.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains hallmark short-chain dehydrogenase/reductase (SDR) family motifs: a Rossmann-fold NAD-binding motif (GAGPIGLVTLA, resembling TGxxxGxG), the catalytic tetrad region (TDIDEGRLAF), and a C-terminal RY motif (QYRY). These features are diagnostic of EC 1.1.1.x oxidoreductases and effectively eliminate options C (2.3.1.318) and D (2.3.1.319), which are acyltransferases (EC 2.3.x) lacking NAD-binding and SDR catalytic motifs. This is a genuine reasoning-based discrimination.",
    "missing_item_specific_fact": "Distinguishing EC 1.1.1.12 (L-arabinitol 4-dehydrogenase) from EC 1.1.1.336 (another CH-OH/NAD+ oxidoreductase, also an SDR) requires knowing the specific substrate and regiochemistry (C4 vs C2 oxidation of L-arabinitol, or a different substrate entirely). Both are SDR-family enzymes with overlapping sequence features. The specific residues in the substrate-binding pocket that determine whether oxidation occurs at C4 vs C2 of L-arabinitol are not identifiable from general biological knowledge without protein-specific annotation or structural data.",
    "reason": "The SDR motifs provide a solid argument to eliminate the two acyltransferase distractors (C, D), narrowing the answer to two oxidoreductase options. However, the final A-vs-B distinction (1.1.1.12 vs 1.1.1.336) hinges on the specific substrate/regiochemistry of this particular enzyme, which is an item-specific annotation fact not derivable from the sequence by general reasoning. Selecting the correct 4-digit EC number among the remaining two SDR dehydrogenases depends on knowing the database annotation or the liamocin biosynthesis pathway context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both EC 1.1.1.12 and EC 1.1.1.336 are CH-OH/NAD+ oxidoreductases within the SDR superfamily. Without the specific substrate-binding pocket analysis or pathway context (liamocin biosynthesis involving L-arabinitol metabolism), a model cannot reliably distinguish which specific dehydrogenase activity this sequence encodes. The SDR motifs confirm EC 1.1.1.x but do not resolve the final digit."
  },
  "important_caveats": [
    "The EC 1.1.1.12 annotation is based on similarity transfer (ECO:0000250 from Q7SI09), not direct experimental characterization of A0A385XI11 itself. The PubMed reference (32003433) provides genetic evidence in the liamocin biosynthesis pathway context.",
    "The UniProt entry was first publicly released on 2025-02-05; the author's source snapshot date is unknown, so the annotation may have been assigned after the benchmark was constructed.",
    "The sequence-match is exact (SHA256 confirmed) for both current and historical (entry version 21) records.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must work from the raw sequence and four choices alone."
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

**Accession:** `A0A385XI11` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 21. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:01.614534+00:00.  

```json
"A0A385XI11"
```

Source SHA-256: `c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:01.614534+00:00.  

```json
{"entryVersion":22,"firstPublicDate":"2025-02-05","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"2018-12-05","sequenceVersion":1}
```

Source SHA-256: `c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:01.614534+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q7SI09","source":"UniProtKB"}],"value":"1.1.1.12"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"L-arabinitol 4-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"ArDH"}]}}
```

Source SHA-256: `c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:01.614534+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.12","evidences":[{"evidenceCode":"ECO:0000250","id":"Q7SI09","source":"UniProtKB"}],"name":"L-arabinitol + NAD(+) = L-xylulose + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:16381"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17399"},{"database":"ChEBI","id":"CHEBI:18403"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"}]}}
```

Source SHA-256: `c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:08.764058+00:00.  

```text
ID   LAD_AURME               Reviewed;         368 AA.
AC   A0A385XI11;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-DEC-2018, sequence version 1.
DT   28-JAN-2026, entry version 21.
DE   RecName: Full=L-arabinitol 4-dehydrogenase {ECO:0000303|PubMed:32003433};
DE            Short=ArDH {ECO:0000303|PubMed:32003433};
DE            EC=1.1.1.12 {ECO:0000250|UniProtKB:Q7SI09};
OS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.
OX   NCBI_TaxID=46634;
```

Source SHA-256: `5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:08.764058+00:00.  

```text
DE   RecName: Full=L-arabinitol 4-dehydrogenase {ECO:0000303|PubMed:32003433};
DE            Short=ArDH {ECO:0000303|PubMed:32003433};
DE            EC=1.1.1.12 {ECO:0000250|UniProtKB:Q7SI09};
```

Source SHA-256: `5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)  
**Locator:** `lines 50-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:08.764058+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-arabinitol + NAD(+) = L-xylulose + NADH + H(+);
CC         Xref=Rhea:RHEA:16381, ChEBI:CHEBI:15378, ChEBI:CHEBI:17399,
CC         ChEBI:CHEBI:18403, ChEBI:CHEBI:57540, ChEBI:CHEBI:57945; EC=1.1.1.12;
CC         Evidence={ECO:0000250|UniProtKB:Q7SI09};
```

Source SHA-256: `5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 36. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
