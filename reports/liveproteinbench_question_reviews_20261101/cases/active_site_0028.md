# active_site_0028

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 92 (Proton donor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSSEPASPEIEQQANSAPRRPRILLAASGSVAAIKFGNLCHSFSEWAEVKAVATRASLHFIDRASLPKDVILYTEEDEWSTWNKVGDSVLHIELRSWADILVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWKNPFTEQHIMSIDELGVSLIPPVTKRLACGDYGNGAMAEPSVIYSTVRLFFESRVQQSGNIVQQPV

[Multiple Choices]
A. Position 418 (For beta-ketoacyl synthase activity)
B. Position 21 (Proton acceptor)
C. Position 92 (Proton donor)
D. Position 1160 (Proton donor; for dehydratase activity)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The exact-match UniProt record annotates position 92 as a proton donor. The annotation is transferred by similarity from Q9SWE5 (ECO:0000250), rather than shown here as direct experimental evidence for this sequence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is 214 residues long, which rules out the positions 418 and 1160, but sequence length and general biological reasoning do not distinguish position 92 from position 21 as the specified catalytic residue.


**Missing item-specific fact**

> A protein-specific active-site annotation or equivalent structural or experimental evidence identifying position 92 as a proton donor.


**Reason**

> Selecting C depends on knowing a position-specific catalytic annotation absent from the input. Recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only C is supported by the matched record. However, the wording suggests the catalytic center's residues collectively, while another proton donor at position 177 is annotated for this protein and is not offered as a choice.


### Important caveats

- The archived record also annotates position 177 as a proton donor, with the same similarity-based evidence; the choices therefore do not enumerate all annotated proton-donor residues (H4).
- The reviewed annotation is sequence-matched, but its evidence code indicates transfer by similarity, not independent experimental validation of position 92 in this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 214 residues long, which rules out the positions 418 and 1160, but sequence length and general biological reasoning do not distinguish position 92 from position 21 as the specified catalytic residue.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific active-site annotation or equivalent structural or experimental evidence identifying position 92 as a proton donor.",
    "reason": "Selecting C depends on knowing a position-specific catalytic annotation absent from the input. Recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied sequence."
  },
  "case_id": "active_site_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-match UniProt record annotates position 92 as a proton donor. The annotation is transferred by similarity from Q9SWE5 (ECO:0000250), rather than shown here as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The archived record also annotates position 177 as a proton donor, with the same similarity-based evidence; the choices therefore do not enumerate all annotated proton-donor residues (H4).",
    "The reviewed annotation is sequence-matched, but its evidence code indicates transfer by similarity, not independent experimental validation of position 92 in this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only C is supported by the matched record. However, the wording suggests the catalytic center's residues collectively, while another proton donor at position 177 is annotated for this protein and is not offered as a choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-match UniProt record annotates position 92 as a proton donor. The annotation is transferred by similarity from Q9SWE5 (ECO:0000250), rather than shown here as direct experimental evidence for this sequence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is 214 residues long, which rules out the positions 418 and 1160, but sequence length and general biological reasoning do not distinguish position 92 from position 21 as the specified catalytic residue.",
    "missing_item_specific_fact": "A protein-specific active-site annotation or equivalent structural or experimental evidence identifying position 92 as a proton donor.",
    "reason": "Selecting C depends on knowing a position-specific catalytic annotation absent from the input. Recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only C is supported by the matched record. However, the wording suggests the catalytic center's residues collectively, while another proton donor at position 177 is annotated for this protein and is not offered as a choice."
  },
  "important_caveats": [
    "The archived record also annotates position 177 as a proton donor, with the same similarity-based evidence; the choices therefore do not enumerate all annotated proton-donor residues (H4).",
    "The reviewed annotation is sequence-matched, but its evidence code indicates transfer by similarity, not independent experimental validation of position 92 in this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A498JQK2 (Phosphopantothenoylcysteine decarboxylase HAL3, EC 4.1.1.36, Malus domestica) annotates position 92 as 'Active site – Proton donor' (evidence C5/H3). The sequence matches the benchmark (214 AA, SHA256 identical). However, the evidence code is ECO:0000250 (similarity to Q9SWE5, Arabidopsis HAL3), meaning this is a computational inference transferred by homology, not an experimentally determined catalytic residue. The annotation is nonetheless the current database record. Distractors A (position 418) and D (position 1160) reference positions far exceeding the 214-residue sequence length, making them trivially invalid.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C1](#evidence-c1), [C3](#evidence-c3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A (position 418) and D (position 1160) are immediately eliminated because the protein is only 214 residues long. Between B (position 21, Arginine, 'Proton acceptor') and C (position 92, Histidine, 'Proton donor'), general enzymology provides meaningful discrimination: (1) Histidine's imidazole (pKa ~6) is the canonical catalytic proton donor/acceptor at physiological pH, whereas Arginine's guanidinium (pKa ~12.5) is constitutively protonated and functions as a positive-charge anchor, not a catalytic proton acceptor; (2) for a decarboxylase (EC 4.1.1.36), proton donation to stabilize the carbanion intermediate or protonate the departing CO2 is mechanistically central; (3) position 21 lies in the N-terminal basic/signal-like region (MTSSEPASPEIEQQANSAPRR…), unlikely to form the catalytic center, whereas position 92 falls within the core catalytic domain flanked by FMN-binding motifs (residues 30–32, 55–57, 108–111, 142). These arguments favor C over B without requiring memorization of the UniProt entry.


**Missing item-specific fact**

> The precise assignment of position 92 (rather than the other annotated proton donor at position 177) as THE active-site residue is a similarity-based annotation (ECO:0000250 from Q9SWE5). However, since position 177 is not among the choices, the B-vs-C discrimination is achievable through general catalytic reasoning.


**Reason**

> The two impossible options (A, D) are eliminated by sequence length. The remaining B-vs-C choice is meaningfully distinguished by well-established biochemical principles (His vs Arg catalytic roles, N-terminal targeting region vs core domain, proton donation in decarboxylation). The annotation is similarity-based, but the reasoning path is defensible from general knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A and D are invalid (positions exceed 214 AA). B is weakly defensible only if one ignores that Arginine is not a typical catalytic proton acceptor and that position 21 is in a non-catalytic N-terminal region. C is the only biochemically coherent answer among the choices. No genuine ambiguity remains after applying basic enzymology.


### Important caveats

- The active-site annotation (ECO:0000250) is transferred by similarity to Arabidopsis Q9SWE5, not experimentally validated for the Malus domestica protein.
- Position 177 is also annotated as a proton donor (C6/H4) but is not offered as a choice, so it does not create ambiguity within this question.
- The protein identity (PPCDC/HAL3) is not stated in the question; a model must infer function from sequence or recognize the protein. The reasoning path relies on recognizing the enzyme class or applying general active-site principles to the sequence.
- The N-terminal region (positions 1–25) resembles a chloroplast transit peptide, supporting the argument that position 21 is unlikely to be catalytic, but this is inferential rather than definitively proven from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A (position 418) and D (position 1160) are immediately eliminated because the protein is only 214 residues long. Between B (position 21, Arginine, 'Proton acceptor') and C (position 92, Histidine, 'Proton donor'), general enzymology provides meaningful discrimination: (1) Histidine's imidazole (pKa ~6) is the canonical catalytic proton donor/acceptor at physiological pH, whereas Arginine's guanidinium (pKa ~12.5) is constitutively protonated and functions as a positive-charge anchor, not a catalytic proton acceptor; (2) for a decarboxylase (EC 4.1.1.36), proton donation to stabilize the carbanion intermediate or protonate the departing CO2 is mechanistically central; (3) position 21 lies in the N-terminal basic/signal-like region (MTSSEPASPEIEQQANSAPRR…), unlikely to form the catalytic center, whereas position 92 falls within the core catalytic domain flanked by FMN-binding motifs (residues 30–32, 55–57, 108–111, 142). These arguments favor C over B without requiring memorization of the UniProt entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise assignment of position 92 (rather than the other annotated proton donor at position 177) as THE active-site residue is a similarity-based annotation (ECO:0000250 from Q9SWE5). However, since position 177 is not among the choices, the B-vs-C discrimination is achievable through general catalytic reasoning.",
    "reason": "The two impossible options (A, D) are eliminated by sequence length. The remaining B-vs-C choice is meaningfully distinguished by well-established biochemical principles (His vs Arg catalytic roles, N-terminal targeting region vs core domain, proton donation in decarboxylation). The annotation is similarity-based, but the reasoning path is defensible from general knowledge."
  },
  "case_id": "active_site_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C1",
      "C3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A498JQK2 (Phosphopantothenoylcysteine decarboxylase HAL3, EC 4.1.1.36, Malus domestica) annotates position 92 as 'Active site – Proton donor' (evidence C5/H3). The sequence matches the benchmark (214 AA, SHA256 identical). However, the evidence code is ECO:0000250 (similarity to Q9SWE5, Arabidopsis HAL3), meaning this is a computational inference transferred by homology, not an experimentally determined catalytic residue. The annotation is nonetheless the current database record. Distractors A (position 418) and D (position 1160) reference positions far exceeding the 214-residue sequence length, making them trivially invalid."
  },
  "important_caveats": [
    "The active-site annotation (ECO:0000250) is transferred by similarity to Arabidopsis Q9SWE5, not experimentally validated for the Malus domestica protein.",
    "Position 177 is also annotated as a proton donor (C6/H4) but is not offered as a choice, so it does not create ambiguity within this question.",
    "The protein identity (PPCDC/HAL3) is not stated in the question; a model must infer function from sequence or recognize the protein. The reasoning path relies on recognizing the enzyme class or applying general active-site principles to the sequence.",
    "The N-terminal region (positions 1–25) resembles a chloroplast transit peptide, supporting the argument that position 21 is unlikely to be catalytic, but this is inferential rather than definitively proven from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and D are invalid (positions exceed 214 AA). B is weakly defensible only if one ignores that Arginine is not a typical catalytic proton acceptor and that position 21 is in a non-catalytic N-terminal region. C is the only biochemically coherent answer among the choices. No genuine ambiguity remains after applying basic enzymology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A498JQK2 (Phosphopantothenoylcysteine decarboxylase HAL3, EC 4.1.1.36, Malus domestica) annotates position 92 as 'Active site – Proton donor' (evidence C5/H3). The sequence matches the benchmark (214 AA, SHA256 identical). However, the evidence code is ECO:0000250 (similarity to Q9SWE5, Arabidopsis HAL3), meaning this is a computational inference transferred by homology, not an experimentally determined catalytic residue. The annotation is nonetheless the current database record. Distractors A (position 418) and D (position 1160) reference positions far exceeding the 214-residue sequence length, making them trivially invalid.",
    "evidence_ids": ["C5", "H3", "C4", "C1", "C3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A (position 418) and D (position 1160) are immediately eliminated because the protein is only 214 residues long. Between B (position 21, Arginine, 'Proton acceptor') and C (position 92, Histidine, 'Proton donor'), general enzymology provides meaningful discrimination: (1) Histidine's imidazole (pKa ~6) is the canonical catalytic proton donor/acceptor at physiological pH, whereas Arginine's guanidinium (pKa ~12.5) is constitutively protonated and functions as a positive-charge anchor, not a catalytic proton acceptor; (2) for a decarboxylase (EC 4.1.1.36), proton donation to stabilize the carbanion intermediate or protonate the departing CO2 is mechanistically central; (3) position 21 lies in the N-terminal basic/signal-like region (MTSSEPASPEIEQQANSAPRR…), unlikely to form the catalytic center, whereas position 92 falls within the core catalytic domain flanked by FMN-binding motifs (residues 30–32, 55–57, 108–111, 142). These arguments favor C over B without requiring memorization of the UniProt entry.",
    "missing_item_specific_fact": "The precise assignment of position 92 (rather than the other annotated proton donor at position 177) as THE active-site residue is a similarity-based annotation (ECO:0000250 from Q9SWE5). However, since position 177 is not among the choices, the B-vs-C discrimination is achievable through general catalytic reasoning.",
    "reason": "The two impossible options (A, D) are eliminated by sequence length. The remaining B-vs-C choice is meaningfully distinguished by well-established biochemical principles (His vs Arg catalytic roles, N-terminal targeting region vs core domain, proton donation in decarboxylation). The annotation is similarity-based, but the reasoning path is defensible from general knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and D are invalid (positions exceed 214 AA). B is weakly defensible only if one ignores that Arginine is not a typical catalytic proton acceptor and that position 21 is in a non-catalytic N-terminal region. C is the only biochemically coherent answer among the choices. No genuine ambiguity remains after applying basic enzymology."
  },
  "important_caveats": [
    "The active-site annotation (ECO:0000250) is transferred by similarity to Arabidopsis Q9SWE5, not experimentally validated for the Malus domestica protein.",
    "Position 177 is also annotated as a proton donor (C6/H4) but is not offered as a choice, so it does not create ambiguity within this question.",
    "The protein identity (PPCDC/HAL3) is not stated in the question; a model must infer function from sequence or recognize the protein. The reasoning path relies on recognizing the enzyme class or applying general active-site principles to the sequence.",
    "The N-terminal region (positions 1–25) resembles a chloroplast transit peptide, supporting the argument that position 21 is unlikely to be catalytic, but this is inferential rather than definitively proven from the sequence alone."
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

**Accession:** `A0A498JQK2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
"A0A498JQK2"
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"commonName":"Apple","lineage":["Eukaryota","Viridiplantae","Streptophyta","Embryophyta","Tracheophyta","Spermatophyta","Magnoliopsida","eudicotyledons","Gunneridae","Pentapetalae","rosids","fabids","Rosales","Rosaceae","Amygdaloideae","Maleae","Malus"],"scientificName":"Malus domestica","synonyms":["Pyrus malus"],"taxonId":3750}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32761275","source":"PubMed"}],"value":"Halotolerance protein 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32761275","source":"PubMed"}],"value":"MdHAL3"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32761275","source":"PubMed"}],"value":"4.1.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Phosphopantothenoylcysteine decarboxylase HAL3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32761275","source":"PubMed"}],"value":"PPCDC"}]}}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":92},"start":{"modifier":"EXACT","value":92}},"type":"Active site"}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":177},"start":{"modifier":"EXACT","value":177}},"type":"Active site"}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)  
**Locator:** `lines 105-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:31.570388+00:00.  

```text
FT   ACT_SITE        92
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000250|UniProtKB:Q9SWE5"
```

Source SHA-256: `0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)  
**Locator:** `lines 108-110`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:31.570388+00:00.  

```text
FT   ACT_SITE        177
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000250|UniProtKB:Q9SWE5"
```

Source SHA-256: `0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
