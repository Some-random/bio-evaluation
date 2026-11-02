# cofactor_0084

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSRVQLALRVPDLEASIGFYSKLFGTGPAKVRPGYANFAIAEPPLKLVLIEGAGEDATRLDHLGVEVEDSAQVGHAARRLKESGLATVEENDTACCYAVQDKVWVTGPGGEPWEVYVVKGDADTLAKADDSACCTPRDSGSAGAAVGADCC

[Multiple Choices]
A. Na(+)
B. heme b
C. Mg(2+)
D. Fe(2+)
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

> The sequence exactly matches the ArsI entry, whose cofactor annotation identifies Fe(2+) and cites experimental evidence (ECO:0000269, PubMed:35487149).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C8](#evidence-c8), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone offers no decisive general motif or contextual clue that distinguishes Fe(2+) from the listed alternatives.


**Missing item-specific fact**

> The protein-specific identity/function as ArsI and its experimentally supported Fe(2+) cofactor annotation.


**Reason**

> Selecting the keyed cofactor requires protein-specific knowledge or external annotation; the sequence and choices do not meaningfully establish which ion is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports Fe(2+) for this protein, although the supplied input does not itself distinguish it.


### Important caveats

- The cofactor annotation is database evidence citing a 2022 publication; the primary paper was not independently reviewed here.
- The reviewer-only source identity and cofactor annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone offers no decisive general motif or contextual clue that distinguishes Fe(2+) from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity/function as ArsI and its experimentally supported Fe(2+) cofactor annotation.",
    "reason": "Selecting the keyed cofactor requires protein-specific knowledge or external annotation; the sequence and choices do not meaningfully establish which ion is required."
  },
  "case_id": "cofactor_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C8",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the ArsI entry, whose cofactor annotation identifies Fe(2+) and cites experimental evidence (ECO:0000269, PubMed:35487149)."
  },
  "important_caveats": [
    "The cofactor annotation is database evidence citing a 2022 publication; the primary paper was not independently reviewed here.",
    "The reviewer-only source identity and cofactor annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports Fe(2+) for this protein, although the supplied input does not itself distinguish it."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the ArsI entry, whose cofactor annotation identifies Fe(2+) and cites experimental evidence (ECO:0000269, PubMed:35487149).",
    "evidence_ids": ["C1", "C5", "C8", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone offers no decisive general motif or contextual clue that distinguishes Fe(2+) from the listed alternatives.",
    "missing_item_specific_fact": "The protein-specific identity/function as ArsI and its experimentally supported Fe(2+) cofactor annotation.",
    "reason": "Selecting the keyed cofactor requires protein-specific knowledge or external annotation; the sequence and choices do not meaningfully establish which ion is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports Fe(2+) for this protein, although the supplied input does not itself distinguish it."
  },
  "important_caveats": [
    "The cofactor annotation is database evidence citing a 2022 publication; the primary paper was not independently reviewed here.",
    "The reviewer-only source identity and cofactor annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> UniProt entry D1A230 (ArsI C-As lyase, Thermomonospora curvata) explicitly annotates Fe(2+) as the cofactor with experimental evidence code ECO:0000269 (inferred from direct assay) citing PubMed:35487149. X-ray crystallography structures (PDB 5V0F, 6XA0, 6XCK) show Fe(2+) in complex with substrate roxarsone (III). The 2022 Nadar et al. paper directly established Fe(2+) as the catalytic cofactor. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly argue that the protein's small size, cysteine-rich C-terminal region, and D/E/H residue spacing might suggest a metal-binding site, and that organoarsenical cleavage (if the function were known) would favor Fe(2+) dioxygenase chemistry. However, the sequence alone does not reveal the protein's identity, EC class, or catalytic mechanism. The 2-His-1-carboxylate facial triad characteristic of Fe(2+)-dependent dioxygenases is present in the structure but is not unambiguously identifiable from the raw 151-aa sequence without prior knowledge of the ArsI fold.


**Missing item-specific fact**

> The protein's identity as ArsI C-As lyase (a trivalent organoarsenical cleaving enzyme, EC 1.13.11.-) and its classification as a Fe(2+)-dependent dioxygenase. Without knowing the protein family, the sequence does not uniquely distinguish Fe(2+) from Mg(2+), both of which are common catalytic metal cofactors. The specific experimental determination of Fe(2+) as the physiologically relevant cofactor (as opposed to Fe(3+) observed in earlier crystal structures) requires the 2022 Nadar et al. study.


**Reason**

> The protein is from an obscure actinobacterium (Thermomonospora curvata) and was only integrated into Swiss-Prot in April 2025. Recognizing the exact 151-aa sequence and recalling its Fe(2+) cofactor assignment constitutes memorization of a database entry. General sequence analysis cannot reliably distinguish Fe(2+) from Mg(2+) for this protein without knowing it is a C-As lyase/dioxygenase. The absence of CXXCH heme motifs mildly disfavors heme b, and Na(+) is rarely a catalytic cofactor for lyases, but these eliminations still leave Mg(2+) vs Fe(2+) as a near coin-flip from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C (Mg(2+))",
  "D (Fe(2+))"
]
```

> Without protein identity or functional context, Mg(2+) is a plausible cofactor for many small lyases and is not excluded by the sequence. Fe(2+) is correct per experimental data, but the sequence does not provide a general biological argument that uniquely excludes Mg(2+). Heme b is weakly disfavored by absence of canonical CXXCH heme-anchoring motifs, and Na(+) is an unusual catalytic cofactor, but these eliminations are insufficient to resolve C vs D without lookup.


### Important caveats

- The UniProt entry was only first published 2025-04-09, making this a very recent annotation. The author's source snapshot date is unknown.
- Earlier crystallography (2016, PubMed:27107642) observed Fe(3+) in wild-type structures; the definitive assignment of Fe(2+) as the catalytically relevant cofactor came from the 2022 study (PubMed:35487149) with substrate-bound Fe(2+) complexes.
- The sequence-match is confirmed (SHA-256 identical to UniProt D1A230, 151 aa), so the annotation applies directly to the supplied sequence.
- The reviewer-only evidence establishes the key is correct but does not make the question reasoning-supported; the evaluated model received only the raw sequence and four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly argue that the protein's small size, cysteine-rich C-terminal region, and D/E/H residue spacing might suggest a metal-binding site, and that organoarsenical cleavage (if the function were known) would favor Fe(2+) dioxygenase chemistry. However, the sequence alone does not reveal the protein's identity, EC class, or catalytic mechanism. The 2-His-1-carboxylate facial triad characteristic of Fe(2+)-dependent dioxygenases is present in the structure but is not unambiguously identifiable from the raw 151-aa sequence without prior knowledge of the ArsI fold.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as ArsI C-As lyase (a trivalent organoarsenical cleaving enzyme, EC 1.13.11.-) and its classification as a Fe(2+)-dependent dioxygenase. Without knowing the protein family, the sequence does not uniquely distinguish Fe(2+) from Mg(2+), both of which are common catalytic metal cofactors. The specific experimental determination of Fe(2+) as the physiologically relevant cofactor (as opposed to Fe(3+) observed in earlier crystal structures) requires the 2022 Nadar et al. study.",
    "reason": "The protein is from an obscure actinobacterium (Thermomonospora curvata) and was only integrated into Swiss-Prot in April 2025. Recognizing the exact 151-aa sequence and recalling its Fe(2+) cofactor assignment constitutes memorization of a database entry. General sequence analysis cannot reliably distinguish Fe(2+) from Mg(2+) for this protein without knowing it is a C-As lyase/dioxygenase. The absence of CXXCH heme motifs mildly disfavors heme b, and Na(+) is rarely a catalytic cofactor for lyases, but these eliminations still leave Mg(2+) vs Fe(2+) as a near coin-flip from sequence alone."
  },
  "case_id": "cofactor_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry D1A230 (ArsI C-As lyase, Thermomonospora curvata) explicitly annotates Fe(2+) as the cofactor with experimental evidence code ECO:0000269 (inferred from direct assay) citing PubMed:35487149. X-ray crystallography structures (PDB 5V0F, 6XA0, 6XCK) show Fe(2+) in complex with substrate roxarsone (III). The 2022 Nadar et al. paper directly established Fe(2+) as the catalytic cofactor. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt entry was only first published 2025-04-09, making this a very recent annotation. The author's source snapshot date is unknown.",
    "Earlier crystallography (2016, PubMed:27107642) observed Fe(3+) in wild-type structures; the definitive assignment of Fe(2+) as the catalytically relevant cofactor came from the 2022 study (PubMed:35487149) with substrate-bound Fe(2+) complexes.",
    "The sequence-match is confirmed (SHA-256 identical to UniProt D1A230, 151 aa), so the annotation applies directly to the supplied sequence.",
    "The reviewer-only evidence establishes the key is correct but does not make the question reasoning-supported; the evaluated model received only the raw sequence and four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C (Mg(2+))",
      "D (Fe(2+))"
    ],
    "reason": "Without protein identity or functional context, Mg(2+) is a plausible cofactor for many small lyases and is not excluded by the sequence. Fe(2+) is correct per experimental data, but the sequence does not provide a general biological argument that uniquely excludes Mg(2+). Heme b is weakly disfavored by absence of canonical CXXCH heme-anchoring motifs, and Na(+) is an unusual catalytic cofactor, but these eliminations are insufficient to resolve C vs D without lookup."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry D1A230 (ArsI C-As lyase, Thermomonospora curvata) explicitly annotates Fe(2+) as the cofactor with experimental evidence code ECO:0000269 (inferred from direct assay) citing PubMed:35487149. X-ray crystallography structures (PDB 5V0F, 6XA0, 6XCK) show Fe(2+) in complex with substrate roxarsone (III). The 2022 Nadar et al. paper directly established Fe(2+) as the catalytic cofactor. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed).",
    "evidence_ids": ["C5", "C8", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly argue that the protein's small size, cysteine-rich C-terminal region, and D/E/H residue spacing might suggest a metal-binding site, and that organoarsenical cleavage (if the function were known) would favor Fe(2+) dioxygenase chemistry. However, the sequence alone does not reveal the protein's identity, EC class, or catalytic mechanism. The 2-His-1-carboxylate facial triad characteristic of Fe(2+)-dependent dioxygenases is present in the structure but is not unambiguously identifiable from the raw 151-aa sequence without prior knowledge of the ArsI fold.",
    "missing_item_specific_fact": "The protein's identity as ArsI C-As lyase (a trivalent organoarsenical cleaving enzyme, EC 1.13.11.-) and its classification as a Fe(2+)-dependent dioxygenase. Without knowing the protein family, the sequence does not uniquely distinguish Fe(2+) from Mg(2+), both of which are common catalytic metal cofactors. The specific experimental determination of Fe(2+) as the physiologically relevant cofactor (as opposed to Fe(3+) observed in earlier crystal structures) requires the 2022 Nadar et al. study.",
    "reason": "The protein is from an obscure actinobacterium (Thermomonospora curvata) and was only integrated into Swiss-Prot in April 2025. Recognizing the exact 151-aa sequence and recalling its Fe(2+) cofactor assignment constitutes memorization of a database entry. General sequence analysis cannot reliably distinguish Fe(2+) from Mg(2+) for this protein without knowing it is a C-As lyase/dioxygenase. The absence of CXXCH heme motifs mildly disfavors heme b, and Na(+) is rarely a catalytic cofactor for lyases, but these eliminations still leave Mg(2+) vs Fe(2+) as a near coin-flip from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C (Mg(2+))", "D (Fe(2+))"],
    "reason": "Without protein identity or functional context, Mg(2+) is a plausible cofactor for many small lyases and is not excluded by the sequence. Fe(2+) is correct per experimental data, but the sequence does not provide a general biological argument that uniquely excludes Mg(2+). Heme b is weakly disfavored by absence of canonical CXXCH heme-anchoring motifs, and Na(+) is an unusual catalytic cofactor, but these eliminations are insufficient to resolve C vs D without lookup."
  },
  "important_caveats": [
    "The UniProt entry was only first published 2025-04-09, making this a very recent annotation. The author's source snapshot date is unknown.",
    "Earlier crystallography (2016, PubMed:27107642) observed Fe(3+) in wild-type structures; the definitive assignment of Fe(2+) as the catalytically relevant cofactor came from the 2022 study (PubMed:35487149) with substrate-bound Fe(2+) complexes.",
    "The sequence-match is confirmed (SHA-256 identical to UniProt D1A230, 151 aa), so the annotation applies directly to the supplied sequence.",
    "The reviewer-only evidence establishes the key is correct but does not make the question reasoning-supported; the evaluated model received only the raw sequence and four choices."
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

**Accession:** `D1A230` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 77. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:37.960057+00:00.  

```json
"D1A230"
```

Source SHA-256: `b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:37.960057+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29033"},"evidences":[{"evidenceCode":"ECO:0000269","id":"35487149","source":"PubMed"}],"name":"Fe(2+)"}],"commentType":"COFACTOR"}
```

Source SHA-256: `b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:37.960057+00:00.  

```json
{"citation":{"authors":["Nadar V.S.","Kandavelu P.","Sankaran B.","Rosen B.P.","Yoshinaga M."],"citationCrossReferences":[{"database":"PubMed","id":"35487149"},{"database":"DOI","id":"10.1016/j.jinorgbio.2022.111836"}],"citationType":"journal article","firstPage":"111836","id":"35487149","journal":"J. Inorg. Biochem.","lastPage":"111836","publicationDate":"2022","title":"The ArsI C-As lyase: Elucidating the catalytic mechanism of degradation of organoarsenicals.","volume":"232"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5V0F","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6XA0","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6XCK","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 19995 / DSM 43183 / JCM 3096 / KCTC 9072 / NBRC 15933 / NCIMB 10081 / Henssen B9"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.15 ANGSTROMS) OF 1-123 OF MUTANT ALA-102 IN COMPLEX WITH SUBSTRATE ROXARSONE (III) AND FE(2+); MUTANT ARG-102 IN COMPLEX WITH NI(2+) AND MUTANT GLU-102","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","REACTION MECHANISM","MUTAGENESIS OF TYR-35; GLN-100 AND LYS-102"]}
```

Source SHA-256: `b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)  
**Locator:** `lines 52-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 77 / 1.  
**Retrieved:** 2026-11-02T04:27:46.748619+00:00.  

```text
RN   [4] {ECO:0007744|PDB:5V0F, ECO:0007744|PDB:6XA0, ECO:0007744|PDB:6XCK}
RP   X-RAY CRYSTALLOGRAPHY (2.15 ANGSTROMS) OF 1-123 OF MUTANT ALA-102 IN
RP   COMPLEX WITH SUBSTRATE ROXARSONE (III) AND FE(2+); MUTANT ARG-102 IN
RP   COMPLEX WITH NI(2+) AND MUTANT GLU-102, FUNCTION, CATALYTIC ACTIVITY,
RP   COFACTOR, REACTION MECHANISM, AND MUTAGENESIS OF TYR-35; GLN-100 AND
RP   LYS-102.
RC   STRAIN=ATCC 19995 / DSM 43183 / JCM 3096 / KCTC 9072 / NBRC 15933 / NCIMB
RC   10081 / Henssen B9;
RX   PubMed=35487149; DOI=10.1016/j.jinorgbio.2022.111836;
RA   Nadar V.S., Kandavelu P., Sankaran B., Rosen B.P., Yoshinaga M.;
RT   "The ArsI C-As lyase: Elucidating the catalytic mechanism of degradation of
RT   organoarsenicals.";
RL   J. Inorg. Biochem. 232:111836-111836(2022).
```

Source SHA-256: `64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 77 / 1.  
**Retrieved:** 2026-11-02T04:27:46.748619+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;
CC         Evidence={ECO:0000269|PubMed:35487149};
```

Source SHA-256: `64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
