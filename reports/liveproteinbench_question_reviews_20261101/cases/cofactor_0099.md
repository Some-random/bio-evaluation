# cofactor_0099

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — FAD

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPSAEGASGAPTPEDLKLHQLSQKYTAEAAKRFRPEGLGQFIRLKEVGNERFRALAEDPWVDHAALNAKEPVKDGSRYKFIILGAGYGGLLYAVRLAEAGLASGPDDILMVDAAGGFGGTWWWNRYPGLHCDVESYSYMPLLEETGYIPKSKYAAGPELLEHAYRIATQWKLHDKALFRSNVKTIRWDDESRLWSLEVTEGRGPGQQSRELKLQARYVLLASGILTNPQVPKIPGLETFTGPVFHTARWNYDVTGGSPTDEALNRLEGKRVGIIGTGATAIQVVPKLAKYAKELYVFQRTPSGVWWRGQRPTDPVEWKTKIARKKGWQRERMLNLDSYLTDAAEEGQENMVADGWTEMPAFSAVIGSPRHGIVEPTPEKIAEHLGRLYKLDLPHAEQVRARTDSIVKDPKTAAKLKAWYPTWCKRPTFSDEYLQTFNLPNVHLVDTDGKGVDAANPSGLVVADKEYPLDILVLSTGYVTPSIGGGSPAVRTGVDIYGRGGKSLDDKWQTHGAATLHGVCSNGFPNLFFTPLSQSSQAANNAFTLDVGTEHIVQVIKTAEDRVDGDALVEVTSEAEEAWSFEIMKHAGWFASVTGCTPGYITSEGEALRKSEDPMEMAKRARSGNLSQGMASYMKLLQEYRADGSLKGFDISSRA

[Multiple Choices]
A. Mn(2+)
B. FAD
C. [4Fe-4S] cluster
D. a divalent metal cation
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the protein sequence in the cited UniProt records. Those records annotate FAD as its cofactor with experimental evidence, and report a crystal structure in complex with FAD and NADPH. This supports choice B.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A glycine-rich sequence region could be consistent with a nucleotide-binding fold, but that generic pattern does not establish which cofactor this particular protein requires or distinguish FAD reliably from the alternatives.


**Missing item-specific fact**

> The protein-specific fact that this sequence is a Baeyer–Villiger monooxygenase whose required cofactor is FAD.


**Reason**

> The input provides only the sequence and choices; it does not identify the enzyme or provide functional or experimental context. Selecting FAD depends on protein-specific annotation or prior knowledge, not a sufficiently discriminating argument from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied input alone does not establish the cofactor, but the answer choices are distinguishable once the protein-specific evidence is consulted: the matched record supports FAD.


### Important caveats

- The reviewer-only evidence identifies the sequence as a matched UniProt record; that identity and annotation were not supplied to the evaluated model.
- The actual author source snapshot is unknown. The cited historical and current records both match the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A glycine-rich sequence region could be consistent with a nucleotide-binding fold, but that generic pattern does not establish which cofactor this particular protein requires or distinguish FAD reliably from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is a Baeyer–Villiger monooxygenase whose required cofactor is FAD.",
    "reason": "The input provides only the sequence and choices; it does not identify the enzyme or provide functional or experimental context. Selecting FAD depends on protein-specific annotation or prior knowledge, not a sufficiently discriminating argument from the supplied information."
  },
  "case_id": "cofactor_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the protein sequence in the cited UniProt records. Those records annotate FAD as its cofactor with experimental evidence, and report a crystal structure in complex with FAD and NADPH. This supports choice B."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies the sequence as a matched UniProt record; that identity and annotation were not supplied to the evaluated model.",
    "The actual author source snapshot is unknown. The cited historical and current records both match the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied input alone does not establish the cofactor, but the answer choices are distinguishable once the protein-specific evidence is consulted: the matched record supports FAD."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the protein sequence in the cited UniProt records. Those records annotate FAD as its cofactor with experimental evidence, and report a crystal structure in complex with FAD and NADPH. This supports choice B.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A glycine-rich sequence region could be consistent with a nucleotide-binding fold, but that generic pattern does not establish which cofactor this particular protein requires or distinguish FAD reliably from the alternatives.",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is a Baeyer–Villiger monooxygenase whose required cofactor is FAD.",
    "reason": "The input provides only the sequence and choices; it does not identify the enzyme or provide functional or experimental context. Selecting FAD depends on protein-specific annotation or prior knowledge, not a sufficiently discriminating argument from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied input alone does not establish the cofactor, but the answer choices are distinguishable once the protein-specific evidence is consulted: the matched record supports FAD."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies the sequence as a matched UniProt record; that identity and annotation were not supplied to the evaluated model.",
    "The actual author source snapshot is unknown. The cited historical and current records both match the sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G2QA95 (Polycyclic ketone monooxygenase / Baeyer-Villiger monooxygenase, EC 1.14.13.-) explicitly annotates FAD as the cofactor with ECO:0000269 (inferred from direct assay), supported by X-ray crystallography at 2.00 Å showing the enzyme in complex with FAD and NADPH (PDB 5MQ6, PubMed 28010060). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed). FAD is the primary flavin cofactor of BVMOs, and the experimental evidence directly confirms its presence in the active site.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold motif (GAGYGGL, residues ~80–86, following the GxGxxG pattern), which is the canonical dinucleotide-binding fold used for FAD and NAD(P) binding. Among the four choices, FAD (option B) is the only nucleotide-derived cofactor; Mn²⁺, &#91;4Fe-4S&#93;, and 'a divalent metal cation' are all metal-based cofactors that do not require a Rossmann fold. Recognizing the Rossmann fold and the overall ~655-aa two-domain architecture (FAD-binding Rossmann domain + NADPH-binding domain) is consistent with a flavin-dependent monooxygenase and provides a concrete general-biochemistry argument to select FAD over the three metal/cluster options.


**Missing item-specific fact**

> None critical. A model could also identify the protein as a BVMO (EC 1.14.13.-) by family-level sequence features, but the Rossmann-fold reasoning alone suffices to eliminate all metal-based choices.


**Reason**

> The presence of the GxGxxG Rossmann-fold motif is a well-established, general biochemical indicator of dinucleotide (FAD/NAD) binding. Since FAD is the sole nucleotide-derived cofactor among the options, this motif provides a meaningful, non-lookup biological argument for choosing FAD over Mn²⁺, &#91;4Fe-4S&#93;, or a generic divalent metal cation. The reasoning does not require memorizing the specific UniProt entry for G2QA95.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (Mn²⁺) and D (a divalent metal cation) overlap conceptually since Mn²⁺ is itself a divalent metal cation, but this does not create ambiguity for the correct answer. FAD is clearly distinct from all three metal-based options, and the Rossmann-fold evidence cleanly selects B. NADPH, the co-substrate of BVMOs, is not among the choices, so no competing nucleotide option exists.


### Important caveats

- BVMOs require both FAD (tightly bound cofactor) and NADPH (reducing co-substrate). The UniProt annotation lists only FAD as the 'cofactor,' which is the convention for the tightly bound prosthetic group. NADPH is not among the answer choices, so this does not create ambiguity.
- The Rossmann-fold heuristic distinguishes nucleotide-binding enzymes from metal-dependent enzymes, but does not by itself distinguish FAD from NAD or FMN. In this question that distinction is irrelevant because FAD is the only nucleotide-derived option.
- All UniProt evidence (C1–C6, H1–H4) is reviewer-only and was not available to the evaluated model; the reasoning-supported judgment is based solely on what can be inferred from the sequence and general biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold motif (GAGYGGL, residues ~80–86, following the GxGxxG pattern), which is the canonical dinucleotide-binding fold used for FAD and NAD(P) binding. Among the four choices, FAD (option B) is the only nucleotide-derived cofactor; Mn²⁺, [4Fe-4S], and 'a divalent metal cation' are all metal-based cofactors that do not require a Rossmann fold. Recognizing the Rossmann fold and the overall ~655-aa two-domain architecture (FAD-binding Rossmann domain + NADPH-binding domain) is consistent with a flavin-dependent monooxygenase and provides a concrete general-biochemistry argument to select FAD over the three metal/cluster options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. A model could also identify the protein as a BVMO (EC 1.14.13.-) by family-level sequence features, but the Rossmann-fold reasoning alone suffices to eliminate all metal-based choices.",
    "reason": "The presence of the GxGxxG Rossmann-fold motif is a well-established, general biochemical indicator of dinucleotide (FAD/NAD) binding. Since FAD is the sole nucleotide-derived cofactor among the options, this motif provides a meaningful, non-lookup biological argument for choosing FAD over Mn²⁺, [4Fe-4S], or a generic divalent metal cation. The reasoning does not require memorizing the specific UniProt entry for G2QA95."
  },
  "case_id": "cofactor_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G2QA95 (Polycyclic ketone monooxygenase / Baeyer-Villiger monooxygenase, EC 1.14.13.-) explicitly annotates FAD as the cofactor with ECO:0000269 (inferred from direct assay), supported by X-ray crystallography at 2.00 Å showing the enzyme in complex with FAD and NADPH (PDB 5MQ6, PubMed 28010060). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed). FAD is the primary flavin cofactor of BVMOs, and the experimental evidence directly confirms its presence in the active site."
  },
  "important_caveats": [
    "BVMOs require both FAD (tightly bound cofactor) and NADPH (reducing co-substrate). The UniProt annotation lists only FAD as the 'cofactor,' which is the convention for the tightly bound prosthetic group. NADPH is not among the answer choices, so this does not create ambiguity.",
    "The Rossmann-fold heuristic distinguishes nucleotide-binding enzymes from metal-dependent enzymes, but does not by itself distinguish FAD from NAD or FMN. In this question that distinction is irrelevant because FAD is the only nucleotide-derived option.",
    "All UniProt evidence (C1–C6, H1–H4) is reviewer-only and was not available to the evaluated model; the reasoning-supported judgment is based solely on what can be inferred from the sequence and general biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (Mn²⁺) and D (a divalent metal cation) overlap conceptually since Mn²⁺ is itself a divalent metal cation, but this does not create ambiguity for the correct answer. FAD is clearly distinct from all three metal-based options, and the Rossmann-fold evidence cleanly selects B. NADPH, the co-substrate of BVMOs, is not among the choices, so no competing nucleotide option exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G2QA95 (Polycyclic ketone monooxygenase / Baeyer-Villiger monooxygenase, EC 1.14.13.-) explicitly annotates FAD as the cofactor with ECO:0000269 (inferred from direct assay), supported by X-ray crystallography at 2.00 Å showing the enzyme in complex with FAD and NADPH (PDB 5MQ6, PubMed 28010060). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed). FAD is the primary flavin cofactor of BVMOs, and the experimental evidence directly confirms its presence in the active site.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold motif (GAGYGGL, residues ~80–86, following the GxGxxG pattern), which is the canonical dinucleotide-binding fold used for FAD and NAD(P) binding. Among the four choices, FAD (option B) is the only nucleotide-derived cofactor; Mn²⁺, [4Fe-4S], and 'a divalent metal cation' are all metal-based cofactors that do not require a Rossmann fold. Recognizing the Rossmann fold and the overall ~655-aa two-domain architecture (FAD-binding Rossmann domain + NADPH-binding domain) is consistent with a flavin-dependent monooxygenase and provides a concrete general-biochemistry argument to select FAD over the three metal/cluster options.",
    "missing_item_specific_fact": "None critical. A model could also identify the protein as a BVMO (EC 1.14.13.-) by family-level sequence features, but the Rossmann-fold reasoning alone suffices to eliminate all metal-based choices.",
    "reason": "The presence of the GxGxxG Rossmann-fold motif is a well-established, general biochemical indicator of dinucleotide (FAD/NAD) binding. Since FAD is the sole nucleotide-derived cofactor among the options, this motif provides a meaningful, non-lookup biological argument for choosing FAD over Mn²⁺, [4Fe-4S], or a generic divalent metal cation. The reasoning does not require memorizing the specific UniProt entry for G2QA95."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (Mn²⁺) and D (a divalent metal cation) overlap conceptually since Mn²⁺ is itself a divalent metal cation, but this does not create ambiguity for the correct answer. FAD is clearly distinct from all three metal-based options, and the Rossmann-fold evidence cleanly selects B. NADPH, the co-substrate of BVMOs, is not among the choices, so no competing nucleotide option exists."
  },
  "important_caveats": [
    "BVMOs require both FAD (tightly bound cofactor) and NADPH (reducing co-substrate). The UniProt annotation lists only FAD as the 'cofactor,' which is the convention for the tightly bound prosthetic group. NADPH is not among the answer choices, so this does not create ambiguity.",
    "The Rossmann-fold heuristic distinguishes nucleotide-binding enzymes from metal-dependent enzymes, but does not by itself distinguish FAD from NAD or FMN. In this question that distinction is irrelevant because FAD is the only nucleotide-derived option.",
    "All UniProt evidence (C1–C6, H1–H4) is reviewer-only and was not available to the evaluated model; the reasoning-supported judgment is based solely on what can be inferred from the sequence and general biochemistry."
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

**Accession:** `G2QA95` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 56. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2QA95.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.440589+00:00.  

```json
"G2QA95"
```

Source SHA-256: `d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2QA95.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.440589+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28010060","source":"PubMed"}],"value":"Baeyer-Villiger monooxygenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"28010060","source":"PubMed"}],"value":"BVMO"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28010060","source":"PubMed"}],"value":"1.14.13.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28010060","source":"PubMed"}],"value":"Polycyclic ketone monooxygenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"28010060","source":"PubMed"}],"value":"PockeMO"}]}}
```

Source SHA-256: `d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2QA95.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.440589+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:57692"},"evidences":[{"evidenceCode":"ECO:0000269","id":"28010060","source":"PubMed"}],"name":"FAD"}],"commentType":"COFACTOR"}
```

Source SHA-256: `d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2QA95.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.440589+00:00.  

```json
{"citation":{"authors":["Furst M.J.","Savino S.","Dudek H.M.","Gomez Castellanos J.R.","Gutierrez de Souza C.","Rovida S.","Fraaije M.W.","Mattevi A."],"citationCrossReferences":[{"database":"PubMed","id":"28010060"},{"database":"DOI","id":"10.1021/jacs.6b12246"}],"citationType":"journal article","firstPage":"627","id":"28010060","journal":"J. Am. Chem. Soc.","lastPage":"630","publicationDate":"2017","title":"Polycyclic Ketone Monooxygenase from the Thermophilic Fungus Thermothelomyces thermophila: A Structurally Distinct Biocatalyst for Bulky Substrates.","volume":"139"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5MQ6","source":"PDB"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) IN COMPLEX WITH FAD AND NADPH","DISULFIDE BONDS","COFACTOR","FUNCTION","CATALYTIC ACTIVITY","SUBSTRATE SPECIFICITY","BIOPHYSICOCHEMICAL PROPERTIES","BIOTECHNOLOGY"]}
```

Source SHA-256: `d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-01T06:28:01.571843+00:00.  

```text
ID   BVMO_THET4              Reviewed;         655 AA.
AC   G2QA95;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-NOV-2011, sequence version 1.
DT   28-JAN-2026, entry version 56.
DE   RecName: Full=Polycyclic ketone monooxygenase {ECO:0000303|PubMed:28010060};
DE            Short=PockeMO {ECO:0000303|PubMed:28010060};
DE            EC=1.14.13.- {ECO:0000269|PubMed:28010060};
DE   AltName: Full=Baeyer-Villiger monooxygenase {ECO:0000303|PubMed:28010060};
DE            Short=BVMO {ECO:0000303|PubMed:28010060};
GN   ORFNames=MYCTH_65400;
OS   Thermothelomyces thermophilus (strain ATCC 42464 / BCRC 31852 / DSM 1799)
OS   (Sporotrichum thermophile).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Thermothelomyces.
OX   NCBI_TaxID=573729;
```

Source SHA-256: `0318176fb6154b708d301de6d2e3ad08fef54e818227bdd198fb527dc3b65386`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-01T06:28:01.571843+00:00.  

```text
DE   RecName: Full=Polycyclic ketone monooxygenase {ECO:0000303|PubMed:28010060};
DE            Short=PockeMO {ECO:0000303|PubMed:28010060};
DE            EC=1.14.13.- {ECO:0000269|PubMed:28010060};
DE   AltName: Full=Baeyer-Villiger monooxygenase {ECO:0000303|PubMed:28010060};
DE            Short=BVMO {ECO:0000303|PubMed:28010060};
```

Source SHA-256: `0318176fb6154b708d301de6d2e3ad08fef54e818227bdd198fb527dc3b65386`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56)  
**Locator:** `lines 32-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-01T06:28:01.571843+00:00.  

```text
RN   [2] {ECO:0007744|PDB:5MQ6}
RP   X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) IN COMPLEX WITH FAD AND NADPH,
RP   DISULFIDE BONDS, COFACTOR, FUNCTION, CATALYTIC ACTIVITY, SUBSTRATE
RP   SPECIFICITY, BIOPHYSICOCHEMICAL PROPERTIES, AND BIOTECHNOLOGY.
RX   PubMed=28010060; DOI=10.1021/jacs.6b12246;
RA   Furst M.J., Savino S., Dudek H.M., Gomez Castellanos J.R.,
RA   Gutierrez de Souza C., Rovida S., Fraaije M.W., Mattevi A.;
RT   "Polycyclic Ketone Monooxygenase from the Thermophilic Fungus
RT   Thermothelomyces thermophila: A Structurally Distinct Biocatalyst for Bulky
RT   Substrates.";
RL   J. Am. Chem. Soc. 139:627-630(2017).
```

Source SHA-256: `0318176fb6154b708d301de6d2e3ad08fef54e818227bdd198fb527dc3b65386`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56)  
**Locator:** `lines 58-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-01T06:28:01.571843+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=FAD; Xref=ChEBI:CHEBI:57692;
CC         Evidence={ECO:0000269|PubMed:28010060};
```

Source SHA-256: `0318176fb6154b708d301de6d2e3ad08fef54e818227bdd198fb527dc3b65386`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
