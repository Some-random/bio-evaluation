# pathway_0013

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTPSKKRCGVLGATGAVGTRFILLLEQSPLLELVAVGASERSAGKKYRDAVRWKQASPMPASVADLTVRRCAPSEFSDCDIIFSGLDPVAAGDIEMAFLKANFAVFSNAKNYRLDPIVPLVVPLVNAGHIDVIPAQRKHYGLDKGLIVCNSNCAVVGLVIPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPFIPGEEGKIATESRKILGNLNPDLAGFSDQQPLQVSVACNRVPVLDGHTVCASLRFVNRPAPTASQVRDALREYKSEVQLLGCPSAPRQAIHVLDDVDRPQPRLDRDTEAGYACSVGRIREDDSGVFDIQFVALSHNTVLGASGSSILNAESAILKGYI

[Multiple Choices]
A. (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3. .
B. oxylipin biosynthesis. .
C. Amino-acid biosynthesis
D. L-histidine biosynthesis
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

> The supplied sequence exactly matches the reviewed UniProt entry for aspartate-semialdehyde dehydrogenase. That entry assigns it to amino-acid biosynthesis, including methionine and threonine biosynthesis, with pathway annotations carrying ECO:0000269 evidence linked to a publication. This supports choice C.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include several distinct pathway categories, but the sequence alone does not provide a clear, general biological clue that identifies this particular enzyme and its pathway. Knowing that aspartate-semialdehyde dehydrogenase participates in aspartate-family amino-acid biosynthesis would distinguish C, but that protein-specific identification is not supplied.


**Missing item-specific fact**

> The protein's identity as aspartate-semialdehyde dehydrogenase and its role in amino-acid biosynthesis, including methionine and threonine biosynthesis.


**Reason**

> Selecting C requires recognizing or looking up the sequence's protein-specific function; generic sequence-based reasoning does not meaningfully distinguish the pathway choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched annotation supports amino-acid biosynthesis rather than the specific histidine pathway or the unrelated pathways listed.


### Important caveats

- The reviewer-only evidence is absent from the evaluated input and supports the key without making the question reasoning-supported.
- The UniProt pathway annotations cite publication-based evidence, but the primary papers were not independently assessed here; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include several distinct pathway categories, but the sequence alone does not provide a clear, general biological clue that identifies this particular enzyme and its pathway. Knowing that aspartate-semialdehyde dehydrogenase participates in aspartate-family amino-acid biosynthesis would distinguish C, but that protein-specific identification is not supplied.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as aspartate-semialdehyde dehydrogenase and its role in amino-acid biosynthesis, including methionine and threonine biosynthesis.",
    "reason": "Selecting C requires recognizing or looking up the sequence's protein-specific function; generic sequence-based reasoning does not meaningfully distinguish the pathway choices."
  },
  "case_id": "pathway_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry for aspartate-semialdehyde dehydrogenase. That entry assigns it to amino-acid biosynthesis, including methionine and threonine biosynthesis, with pathway annotations carrying ECO:0000269 evidence linked to a publication. This supports choice C."
  },
  "important_caveats": [
    "The reviewer-only evidence is absent from the evaluated input and supports the key without making the question reasoning-supported.",
    "The UniProt pathway annotations cite publication-based evidence, but the primary papers were not independently assessed here; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation supports amino-acid biosynthesis rather than the specific histidine pathway or the unrelated pathways listed."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry for aspartate-semialdehyde dehydrogenase. That entry assigns it to amino-acid biosynthesis, including methionine and threonine biosynthesis, with pathway annotations carrying ECO:0000269 evidence linked to a publication. This supports choice C.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include several distinct pathway categories, but the sequence alone does not provide a clear, general biological clue that identifies this particular enzyme and its pathway. Knowing that aspartate-semialdehyde dehydrogenase participates in aspartate-family amino-acid biosynthesis would distinguish C, but that protein-specific identification is not supplied.",
    "missing_item_specific_fact": "The protein's identity as aspartate-semialdehyde dehydrogenase and its role in amino-acid biosynthesis, including methionine and threonine biosynthesis.",
    "reason": "Selecting C requires recognizing or looking up the sequence's protein-specific function; generic sequence-based reasoning does not meaningfully distinguish the pathway choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation supports amino-acid biosynthesis rather than the specific histidine pathway or the unrelated pathways listed."
  },
  "important_caveats": [
    "The reviewer-only evidence is absent from the evaluated input and supports the key without making the question reasoning-supported.",
    "The UniProt pathway annotations cite publication-based evidence, but the primary papers were not independently assessed here; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A179UL48 (sequence matched, 362 aa) identifies this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from Blastomyces gilchristii. Two pathway annotations explicitly place it under 'Amino-acid biosynthesis': (1) L-methionine biosynthesis via de novo pathway, L-homoserine from L-aspartate: step 2/3, and (2) L-threonine biosynthesis, L-threonine from L-aspartate: step 2/5. Both are experimentally supported (ECO:0000269, PubMed:30107909). Choice C 'Amino-acid biosynthesis' is the correct umbrella category.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold nucleotide-binding motif (GVLGATGAVGTR at positions ~10-21), identifying this as an NAD(P)-dependent dehydrogenase. This allows elimination of: (D) L-histidine biosynthesis, which proceeds via ATP/PRPP rearrangements and cyclization without NAD(P)-dependent dehydrogenase steps; (B) oxylipin biosynthesis, which involves lipoxygenases/cyclooxygenases (oxygenases, not dehydrogenases); and (A) HMG-CoA from isovaleryl-CoA (step 3/3), which is a carboxylation reaction, not a dehydrogenation. Multiple amino-acid biosynthesis pathways (aspartate→homoserine→methionine/threonine, glutamate→proline, etc.) do employ NAD(P)-dependent dehydrogenases, making C the consistent broad category.


**Missing item-specific fact**

> Precisely identifying the enzyme as aspartate-semialdehyde dehydrogenase (rather than glutamate-5-semialdehyde dehydrogenase or another family member) and specifying methionine/threonine over proline would require family-level sequence recognition or database lookup. However, the broad category 'Amino-acid biosynthesis' is defensible from the dehydrogenase identification alone.


**Reason**

> The Rossmann fold is a generalizable structural motif identifiable from sequence. Eliminating histidine biosynthesis (no dehydrogenase steps), oxylipin biosynthesis (oxygenases), and HMG-CoA carboxylation (carboxylase) from the presence of a dehydrogenase fold constitutes a concrete biological argument. The remaining option C is the only pathway category that commonly features NAD(P)-dependent dehydrogenases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated by enzyme class: A involves a carboxylase, B involves oxygenases, D involves transferases/isomerases/cyclases, and C encompasses dehydrogenases. The Rossmann fold clearly points to a dehydrogenase, uniquely consistent with C among the choices.


### Important caveats

- The Rossmann fold alone does not specify which amino-acid biosynthesis pathway; the broad category C is used, which is appropriate given the answer choices.
- The UniProt annotation is experimentally supported (ECO:0000269, PubMed:30107909 with X-ray crystallography PDB 6C85/6C8W), not merely computational.
- The sequence is 362 aa, matching the canonical entry exactly (SHA-256 match confirmed in both current and historical snapshots).
- The identity origin note states the accession was inferred mechanically from dataset metadata absent from the evaluated model input; the model must work from the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold nucleotide-binding motif (GVLGATGAVGTR at positions ~10-21), identifying this as an NAD(P)-dependent dehydrogenase. This allows elimination of: (D) L-histidine biosynthesis, which proceeds via ATP/PRPP rearrangements and cyclization without NAD(P)-dependent dehydrogenase steps; (B) oxylipin biosynthesis, which involves lipoxygenases/cyclooxygenases (oxygenases, not dehydrogenases); and (A) HMG-CoA from isovaleryl-CoA (step 3/3), which is a carboxylation reaction, not a dehydrogenation. Multiple amino-acid biosynthesis pathways (aspartate→homoserine→methionine/threonine, glutamate→proline, etc.) do employ NAD(P)-dependent dehydrogenases, making C the consistent broad category.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precisely identifying the enzyme as aspartate-semialdehyde dehydrogenase (rather than glutamate-5-semialdehyde dehydrogenase or another family member) and specifying methionine/threonine over proline would require family-level sequence recognition or database lookup. However, the broad category 'Amino-acid biosynthesis' is defensible from the dehydrogenase identification alone.",
    "reason": "The Rossmann fold is a generalizable structural motif identifiable from sequence. Eliminating histidine biosynthesis (no dehydrogenase steps), oxylipin biosynthesis (oxygenases), and HMG-CoA carboxylation (carboxylase) from the presence of a dehydrogenase fold constitutes a concrete biological argument. The remaining option C is the only pathway category that commonly features NAD(P)-dependent dehydrogenases."
  },
  "case_id": "pathway_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A179UL48 (sequence matched, 362 aa) identifies this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from Blastomyces gilchristii. Two pathway annotations explicitly place it under 'Amino-acid biosynthesis': (1) L-methionine biosynthesis via de novo pathway, L-homoserine from L-aspartate: step 2/3, and (2) L-threonine biosynthesis, L-threonine from L-aspartate: step 2/5. Both are experimentally supported (ECO:0000269, PubMed:30107909). Choice C 'Amino-acid biosynthesis' is the correct umbrella category."
  },
  "important_caveats": [
    "The Rossmann fold alone does not specify which amino-acid biosynthesis pathway; the broad category C is used, which is appropriate given the answer choices.",
    "The UniProt annotation is experimentally supported (ECO:0000269, PubMed:30107909 with X-ray crystallography PDB 6C85/6C8W), not merely computational.",
    "The sequence is 362 aa, matching the canonical entry exactly (SHA-256 match confirmed in both current and historical snapshots).",
    "The identity origin note states the accession was inferred mechanically from dataset metadata absent from the evaluated model input; the model must work from the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by enzyme class: A involves a carboxylase, B involves oxygenases, D involves transferases/isomerases/cyclases, and C encompasses dehydrogenases. The Rossmann fold clearly points to a dehydrogenase, uniquely consistent with C among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A179UL48 (sequence matched, 362 aa) identifies this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from Blastomyces gilchristii. Two pathway annotations explicitly place it under 'Amino-acid biosynthesis': (1) L-methionine biosynthesis via de novo pathway, L-homoserine from L-aspartate: step 2/3, and (2) L-threonine biosynthesis, L-threonine from L-aspartate: step 2/5. Both are experimentally supported (ECO:0000269, PubMed:30107909). Choice C 'Amino-acid biosynthesis' is the correct umbrella category.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold nucleotide-binding motif (GVLGATGAVGTR at positions ~10-21), identifying this as an NAD(P)-dependent dehydrogenase. This allows elimination of: (D) L-histidine biosynthesis, which proceeds via ATP/PRPP rearrangements and cyclization without NAD(P)-dependent dehydrogenase steps; (B) oxylipin biosynthesis, which involves lipoxygenases/cyclooxygenases (oxygenases, not dehydrogenases); and (A) HMG-CoA from isovaleryl-CoA (step 3/3), which is a carboxylation reaction, not a dehydrogenation. Multiple amino-acid biosynthesis pathways (aspartate→homoserine→methionine/threonine, glutamate→proline, etc.) do employ NAD(P)-dependent dehydrogenases, making C the consistent broad category.",
    "missing_item_specific_fact": "Precisely identifying the enzyme as aspartate-semialdehyde dehydrogenase (rather than glutamate-5-semialdehyde dehydrogenase or another family member) and specifying methionine/threonine over proline would require family-level sequence recognition or database lookup. However, the broad category 'Amino-acid biosynthesis' is defensible from the dehydrogenase identification alone.",
    "reason": "The Rossmann fold is a generalizable structural motif identifiable from sequence. Eliminating histidine biosynthesis (no dehydrogenase steps), oxylipin biosynthesis (oxygenases), and HMG-CoA carboxylation (carboxylase) from the presence of a dehydrogenase fold constitutes a concrete biological argument. The remaining option C is the only pathway category that commonly features NAD(P)-dependent dehydrogenases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by enzyme class: A involves a carboxylase, B involves oxygenases, D involves transferases/isomerases/cyclases, and C encompasses dehydrogenases. The Rossmann fold clearly points to a dehydrogenase, uniquely consistent with C among the choices."
  },
  "important_caveats": [
    "The Rossmann fold alone does not specify which amino-acid biosynthesis pathway; the broad category C is used, which is appropriate given the answer choices.",
    "The UniProt annotation is experimentally supported (ECO:0000269, PubMed:30107909 with X-ray crystallography PDB 6C85/6C8W), not merely computational.",
    "The sequence is 362 aa, matching the canonical entry exactly (SHA-256 match confirmed in both current and historical snapshots).",
    "The identity origin note states the accession was inferred mechanically from dataset metadata absent from the evaluated model input; the model must work from the raw sequence."
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

**Accession:** `A0A179UL48` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
"A0A179UL48"
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30107909","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30107909","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3"}]}
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30107909","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5"}]}
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
ID   DHAS_BLAGS              Reviewed;         362 AA.
AC   A0A179UL48;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 2.
DT   28-JAN-2026, entry version 26.
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};
GN   ORFNames=BDBG_16922 {ECO:0000312|EMBL:OAT07949.1};
OS   Blastomyces gilchristii (strain SLH14081) (Blastomyces dermatitidis).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Onygenales; Ajellomycetaceae; Blastomyces.
OX   NCBI_TaxID=559298 {ECO:0000312|Proteomes:UP000002038};
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 64-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo
CC       pathway; L-homoserine from L-aspartate: step 2/3.
CC       {ECO:0000269|PubMed:30107909}.
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 67-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine
CC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:30107909}.
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 13. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
