# GO_biological_process_0181

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — sesquiterpenoid biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDMNTFPANTYCDSIVRFLDAIEYHDDNLTHDERVEGLRHVHSRTAQYFTEPLPRKVLKDVAPRRIAAVTRTISHFIVYCWSKLPREAQVDVSIYLSIINVLDDEISSEPSTQMATFWTDLVQGKQQKHPFWVLFNSHLPRLLRHYDSFCSFNIMRCTFDYFEGCWIEQHNFQGYPGADCYPLFLRRLNCLGGAVAGTIFPAAKFDEQKLFAEISCVMAQIDGPVALVNDLFSFYKEYDQDEANLVTNWCTVDGITMDQALTRLTDDTIHACVRILEILKDKDPDMLATIRGFIHGYVTWHICDFRYRLREIYDREDLGGSSAKFRDYFDTAINVGWVDVEEWTCQVQGFEVDGPVPKGSEIQAYRTNAFGFSVDTRRPHNMDYVGSSIISMFEWVTGYLKGKSR

[Multiple Choices]
A. negative regulation of gene expression
B. lysine biosynthetic process via aminoadipic acid
C. sesquiterpenoid biosynthetic process
D. bone mineralization
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact 405-aa sequence matches the historical UniProt entry for PbrA, annotated as part of the aspterric-acid sesquiterpenoid biosynthesis cluster. The record cites experimental evidence for cluster involvement and also carries a GO annotation for sesquiterpenoid biosynthesis, though that GO annotation is computational (IEA:InterPro).

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices span unrelated processes, but the supplied sequence alone does not establish this protein's specific role in sesquiterpenoid biosynthesis.


**Missing item-specific fact**

> The protein-specific annotation or experimental finding that this sequence is PbrA, a terpene cyclase in the aspterric-acid biosynthesis cluster.


**Reason**

> Identifying the precise biological process requires the protein-specific functional association. The reviewer-only database and publication-linked evidence supports the key, but was not available in the question input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports choice C; no evidence here supports another listed choice for this sequence.


### Important caveats

- The GO annotation itself is computationally assigned (IEA:InterPro); the UniProt functional description separately cites experimental evidence for cluster involvement.
- The detailed PbrA-to-daucane reaction is described as inferred by similarity, so it should not be treated as independently established experimental evidence here.
- The primary paper was not independently reviewed in the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices span unrelated processes, but the supplied sequence alone does not establish this protein's specific role in sesquiterpenoid biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation or experimental finding that this sequence is PbrA, a terpene cyclase in the aspterric-acid biosynthesis cluster.",
    "reason": "Identifying the precise biological process requires the protein-specific functional association. The reviewer-only database and publication-linked evidence supports the key, but was not available in the question input."
  },
  "case_id": "GO_biological_process_0181",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3",
      "H4",
      "H5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact 405-aa sequence matches the historical UniProt entry for PbrA, annotated as part of the aspterric-acid sesquiterpenoid biosynthesis cluster. The record cites experimental evidence for cluster involvement and also carries a GO annotation for sesquiterpenoid biosynthesis, though that GO annotation is computational (IEA:InterPro)."
  },
  "important_caveats": [
    "The GO annotation itself is computationally assigned (IEA:InterPro); the UniProt functional description separately cites experimental evidence for cluster involvement.",
    "The detailed PbrA-to-daucane reaction is described as inferred by similarity, so it should not be treated as independently established experimental evidence here.",
    "The primary paper was not independently reviewed in the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports choice C; no evidence here supports another listed choice for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0181",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 405-aa sequence matches the historical UniProt entry for PbrA, annotated as part of the aspterric-acid sesquiterpenoid biosynthesis cluster. The record cites experimental evidence for cluster involvement and also carries a GO annotation for sesquiterpenoid biosynthesis, though that GO annotation is computational (IEA:InterPro).",
    "evidence_ids": ["H1", "H3", "H4", "H5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices span unrelated processes, but the supplied sequence alone does not establish this protein's specific role in sesquiterpenoid biosynthesis.",
    "missing_item_specific_fact": "The protein-specific annotation or experimental finding that this sequence is PbrA, a terpene cyclase in the aspterric-acid biosynthesis cluster.",
    "reason": "Identifying the precise biological process requires the protein-specific functional association. The reviewer-only database and publication-linked evidence supports the key, but was not available in the question input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports choice C; no evidence here supports another listed choice for this sequence."
  },
  "important_caveats": [
    "The GO annotation itself is computationally assigned (IEA:InterPro); the UniProt functional description separately cites experimental evidence for cluster involvement.",
    "The detailed PbrA-to-daucane reaction is described as inferred by similarity, so it should not be treated as independently established experimental evidence here.",
    "The primary paper was not independently reviewed in the supplied evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0F7TWX5 (sequence matched, 405 aa) is annotated as 'Terpene cyclase pbrA' from Penicillium brasilianum. Its function (C5, H3) explicitly states it is a terpene cyclase in the gene cluster mediating biosynthesis of the sesquiterpenoid aspterric acid, cyclizing FPP to (-)-daucane. The pathway (C6, H4) is 'terpenoid biosynthesis.' The GO cross-reference (C7, H5) assigns GO:0016106 'sesquiterpenoid biosynthetic process' (IEA:InterPro), and the PubMed reference 39511739 provides experimental evidence for the terpene cyclase function in sesquiterpenoid biosynthesis. The expected answer C is directly supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains aspartate-rich motifs characteristic of class I terpene cyclases (e.g., NDD-like 'NMDY' near the C-terminus and DDxxD-like 'TDDT' in the central region), and the ~405 aa length is consistent with fungal sesquiterpene cyclases. More critically, the distractors are eliminable by general biological reasoning: (D) bone mineralization is impossible for a fungal protein; (A) negative regulation of gene expression requires DNA/RNA-binding or transcription-factor domains absent here; (B) lysine biosynthesis via aminoadipic acid involves entirely different enzyme classes (homocitrate synthase, aminoadipate reductase, etc.). Once the sequence is recognized as a terpene cyclase (or at least a small-molecule cyclase with aspartate-rich catalytic motifs), C is the only terpenoid-related option.


**Missing item-specific fact**

> Precise motif identification (NDD, DDxxD) from a raw 405-aa sequence is specialized but falls within general biochemical knowledge of terpene cyclase catalytic signatures. No protein-specific experimental measurement is needed beyond recognizing the enzyme class.


**Reason**

> A model with knowledge of terpene cyclase catalytic motifs (NDD, DDxxD) and the biology of fungal secondary metabolism can positively identify the enzyme class and eliminate the three clearly inappropriate distractors. The absence of competing terpenoid options means any terpene-cyclase identification maps uniquely to C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span vastly different biological domains (gene regulation, amino acid biosynthesis, terpenoid biosynthesis, bone mineralization). For a fungal enzyme with terpene cyclase-like motifs, only C is biologically plausible. No other option is defensible.


### Important caveats

- The GO annotation is IEA:InterPro (automated), not a direct experimental GO assignment; however, the underlying PubMed:39511739 provides experimental evidence for the terpene cyclase function in sesquiterpenoid biosynthesis.
- The NDD and DDxxD motifs in this sequence are somewhat degenerate (e.g., 'NMDY' rather than canonical 'NDD'), making motif-based identification less straightforward than for textbook examples.
- The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence-derived reasoning and general biochemical knowledge.
- The specific 'sesquiterpenoid' (C15) designation vs. other terpenoid classes is not independently derivable from the sequence alone, but is rendered unambiguous by the absence of competing terpenoid options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains aspartate-rich motifs characteristic of class I terpene cyclases (e.g., NDD-like 'NMDY' near the C-terminus and DDxxD-like 'TDDT' in the central region), and the ~405 aa length is consistent with fungal sesquiterpene cyclases. More critically, the distractors are eliminable by general biological reasoning: (D) bone mineralization is impossible for a fungal protein; (A) negative regulation of gene expression requires DNA/RNA-binding or transcription-factor domains absent here; (B) lysine biosynthesis via aminoadipic acid involves entirely different enzyme classes (homocitrate synthase, aminoadipate reductase, etc.). Once the sequence is recognized as a terpene cyclase (or at least a small-molecule cyclase with aspartate-rich catalytic motifs), C is the only terpenoid-related option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise motif identification (NDD, DDxxD) from a raw 405-aa sequence is specialized but falls within general biochemical knowledge of terpene cyclase catalytic signatures. No protein-specific experimental measurement is needed beyond recognizing the enzyme class.",
    "reason": "A model with knowledge of terpene cyclase catalytic motifs (NDD, DDxxD) and the biology of fungal secondary metabolism can positively identify the enzyme class and eliminate the three clearly inappropriate distractors. The absence of competing terpenoid options means any terpene-cyclase identification maps uniquely to C."
  },
  "case_id": "GO_biological_process_0181",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F7TWX5 (sequence matched, 405 aa) is annotated as 'Terpene cyclase pbrA' from Penicillium brasilianum. Its function (C5, H3) explicitly states it is a terpene cyclase in the gene cluster mediating biosynthesis of the sesquiterpenoid aspterric acid, cyclizing FPP to (-)-daucane. The pathway (C6, H4) is 'terpenoid biosynthesis.' The GO cross-reference (C7, H5) assigns GO:0016106 'sesquiterpenoid biosynthetic process' (IEA:InterPro), and the PubMed reference 39511739 provides experimental evidence for the terpene cyclase function in sesquiterpenoid biosynthesis. The expected answer C is directly supported."
  },
  "important_caveats": [
    "The GO annotation is IEA:InterPro (automated), not a direct experimental GO assignment; however, the underlying PubMed:39511739 provides experimental evidence for the terpene cyclase function in sesquiterpenoid biosynthesis.",
    "The NDD and DDxxD motifs in this sequence are somewhat degenerate (e.g., 'NMDY' rather than canonical 'NDD'), making motif-based identification less straightforward than for textbook examples.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence-derived reasoning and general biochemical knowledge.",
    "The specific 'sesquiterpenoid' (C15) designation vs. other terpenoid classes is not independently derivable from the sequence alone, but is rendered unambiguous by the absence of competing terpenoid options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span vastly different biological domains (gene regulation, amino acid biosynthesis, terpenoid biosynthesis, bone mineralization). For a fungal enzyme with terpene cyclase-like motifs, only C is biologically plausible. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0181",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F7TWX5 (sequence matched, 405 aa) is annotated as 'Terpene cyclase pbrA' from Penicillium brasilianum. Its function (C5, H3) explicitly states it is a terpene cyclase in the gene cluster mediating biosynthesis of the sesquiterpenoid aspterric acid, cyclizing FPP to (-)-daucane. The pathway (C6, H4) is 'terpenoid biosynthesis.' The GO cross-reference (C7, H5) assigns GO:0016106 'sesquiterpenoid biosynthetic process' (IEA:InterPro), and the PubMed reference 39511739 provides experimental evidence for the terpene cyclase function in sesquiterpenoid biosynthesis. The expected answer C is directly supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains aspartate-rich motifs characteristic of class I terpene cyclases (e.g., NDD-like 'NMDY' near the C-terminus and DDxxD-like 'TDDT' in the central region), and the ~405 aa length is consistent with fungal sesquiterpene cyclases. More critically, the distractors are eliminable by general biological reasoning: (D) bone mineralization is impossible for a fungal protein; (A) negative regulation of gene expression requires DNA/RNA-binding or transcription-factor domains absent here; (B) lysine biosynthesis via aminoadipic acid involves entirely different enzyme classes (homocitrate synthase, aminoadipate reductase, etc.). Once the sequence is recognized as a terpene cyclase (or at least a small-molecule cyclase with aspartate-rich catalytic motifs), C is the only terpenoid-related option.",
    "missing_item_specific_fact": "Precise motif identification (NDD, DDxxD) from a raw 405-aa sequence is specialized but falls within general biochemical knowledge of terpene cyclase catalytic signatures. No protein-specific experimental measurement is needed beyond recognizing the enzyme class.",
    "reason": "A model with knowledge of terpene cyclase catalytic motifs (NDD, DDxxD) and the biology of fungal secondary metabolism can positively identify the enzyme class and eliminate the three clearly inappropriate distractors. The absence of competing terpenoid options means any terpene-cyclase identification maps uniquely to C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span vastly different biological domains (gene regulation, amino acid biosynthesis, terpenoid biosynthesis, bone mineralization). For a fungal enzyme with terpene cyclase-like motifs, only C is biologically plausible. No other option is defensible."
  },
  "important_caveats": [
    "The GO annotation is IEA:InterPro (automated), not a direct experimental GO assignment; however, the underlying PubMed:39511739 provides experimental evidence for the terpene cyclase function in sesquiterpenoid biosynthesis.",
    "The NDD and DDxxD motifs in this sequence are somewhat degenerate (e.g., 'NMDY' rather than canonical 'NDD'), making motif-based identification less straightforward than for textbook examples.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence-derived reasoning and general biochemical knowledge.",
    "The specific 'sesquiterpenoid' (C15) designation vs. other terpenoid classes is not independently derivable from the sequence alone, but is rendered unambiguous by the absence of competing terpenoid options."
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

**Accession:** `A0A0F7TWX5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWX5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.624982+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein A"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39511739","source":"PubMed"}],"value":"4.2.3.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Terpene cyclase pbrA"}}}
```

Source SHA-256: `e5c7bc5d6c9449056bcb179284140dfad029fb97ea3206db0ebed6688d6396d9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWX5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.624982+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q0CPG8","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"39511739","source":"PubMed"}],"value":"Terpene cyclase; part of the gene cluster that mediates the biosynthesis of the sesquiterpenoid aspterric acid (AA), an inhibitor of dihydroxy-acid dehydratase (DHAD) effective as an herbicide (PubMed:39511739). PbrA cyclizes farnesyl diphosphate (FPP) to produce (-)-daucane (By similarity). The cytochrome P450 monooxygenase pbrBB then converts (-)-daucane into the alpha-epoxy carboxylate intermediate which is further converted into the tricyclic aspterric acid by the cytochrome P450 monooxygenase pbrC (By similarity)"}]}
```

Source SHA-256: `e5c7bc5d6c9449056bcb179284140dfad029fb97ea3206db0ebed6688d6396d9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWX5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.624982+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39511739","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `e5c7bc5d6c9449056bcb179284140dfad029fb97ea3206db0ebed6688d6396d9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWX5.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.624982+00:00.  

```json
{"database":"GO","id":"GO:0016106","properties":[{"key":"GoTerm","value":"P:sesquiterpenoid biosynthetic process"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `e5c7bc5d6c9449056bcb179284140dfad029fb97ea3206db0ebed6688d6396d9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWX5?format=txt&versions=30)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:17.746470+00:00.  

```text
ID   PBRA_PENBI              Reviewed;         405 AA.
AC   A0A0F7TWX5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   22-JUL-2015, sequence version 1.
DT   28-JAN-2026, entry version 30.
DE   RecName: Full=Terpene cyclase pbrA {ECO:0000303|PubMed:39511739};
DE            EC=4.2.3.- {ECO:0000305|PubMed:39511739};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein A {ECO:0000303|PubMed:39511739};
GN   Name=pbrA {ECO:0000303|PubMed:39511739}; ORFNames=PMG11_09714;
OS   Penicillium brasilianum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=104259;
```

Source SHA-256: `384a95ec3352046b0f3464b2a89ebb41f2b203da008eaf15f997962c8728120c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWX5?format=txt&versions=30)  
**Locator:** `lines 28-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:17.746470+00:00.  

```text
CC   -!- FUNCTION: Terpene cyclase; part of the gene cluster that mediates the
CC       biosynthesis of the sesquiterpenoid aspterric acid (AA), an inhibitor
CC       of dihydroxy-acid dehydratase (DHAD) effective as an herbicide
CC       (PubMed:39511739). PbrA cyclizes farnesyl diphosphate (FPP) to produce
CC       (-)-daucane (By similarity). The cytochrome P450 monooxygenase pbrBB
CC       then converts (-)-daucane into the alpha-epoxy carboxylate intermediate
CC       which is further converted into the tricyclic aspterric acid by the
CC       cytochrome P450 monooxygenase pbrC (By similarity).
CC       {ECO:0000250|UniProtKB:Q0CPG8, ECO:0000269|PubMed:39511739}.
```

Source SHA-256: `384a95ec3352046b0f3464b2a89ebb41f2b203da008eaf15f997962c8728120c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWX5?format=txt&versions=30)  
**Locator:** `lines 40-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:17.746470+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39511739}.
```

Source SHA-256: `384a95ec3352046b0f3464b2a89ebb41f2b203da008eaf15f997962c8728120c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWX5?format=txt&versions=30)  
**Locator:** `lines 63-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:17.746470+00:00.  

```text
DR   GO; GO:0016106; P:sesquiterpenoid biosynthetic process; IEA:InterPro.
```

Source SHA-256: `384a95ec3352046b0f3464b2a89ebb41f2b203da008eaf15f997962c8728120c`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 123514-123525`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016106
name: sesquiterpenoid biosynthetic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the formation of sesquiterpenoid compounds, terpenoids with three isoprene units." [GOC:curators]
synonym: "sesquiterpenoid anabolism" EXACT []
synonym: "sesquiterpenoid biosynthesis" EXACT []
synonym: "sesquiterpenoid formation" EXACT []
synonym: "sesquiterpenoid synthesis" EXACT []
is_a: GO:0006714 ! sesquiterpenoid metabolic process
is_a: GO:0016114 ! terpenoid biosynthetic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 181. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
