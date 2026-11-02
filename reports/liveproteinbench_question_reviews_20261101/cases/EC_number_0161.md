# EC_number_0161

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.5.1.15

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSKIFGIVNITTDSFSDGGLYLDTDKAIEHALHLVEDGADVIDLGAASSNPDTTEVGVVEEIKRLKPVIKALKEKGISISVDTFKPEVQSFCIEQKVDFINDIQGFPYPEIYSGLAKSDCKLVLMHSVQRIGAATKVETNPEEVFTSMMEFFKERIAALVEAGVKRERIILDPGMGFFLGSNPETSILVLKRFPEIQEAFNLQVMIAVSRKSFLGKITGTDVKSRLAPTLAAEMYAYKKGADYLRTHDVKSLSDALKISKALG

[Multiple Choices]
A. 2.5.1.56
B. 3.1.26.3
C. 5.3.1.8
D. 2.5.1.15
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

> The supplied sequence exactly matches the UniProt entry annotated as dihydropteroate synthase type 3, EC 2.5.1.15. The catalytic-activity annotation cites experimental evidence (ECO:0000269) for the reaction assigned that EC number; the entry was also present in the historical record checked. The annotation additionally has computational RuleBase support.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could support a broad inference about enzyme family if recognized or compared with known homologs, but the prompt supplies no organism, reaction, or functional context that distinguishes the precise EC assignment from the alternatives.


**Missing item-specific fact**

> The protein-specific identification as dihydropteroate synthase type 3, and its catalyzed reaction corresponding to EC 2.5.1.15, is needed to select D.


**Reason**

> The exact EC assignment depends on protein-specific functional knowledge or external annotation not given in the input. Recognizing the sequence or predicting its family is not, by itself, reasoning from the supplied evidence to the complete EC number.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation and cited catalytic-activity evidence support D; no supplied evidence supports another listed EC number for this protein.


### Important caveats

- Reviewer-only database and literature evidence supports the key but was not part of the evaluated model input.
- The UniProt annotation includes both computational and experimental evidence; the cited experimental evidence is reported in the entry, not independently validated here.
- The exact author source snapshot is unknown, although the sequence matched both current and checked historical records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could support a broad inference about enzyme family if recognized or compared with known homologs, but the prompt supplies no organism, reaction, or functional context that distinguishes the precise EC assignment from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as dihydropteroate synthase type 3, and its catalyzed reaction corresponding to EC 2.5.1.15, is needed to select D.",
    "reason": "The exact EC assignment depends on protein-specific functional knowledge or external annotation not given in the input. Recognizing the sequence or predicting its family is not, by itself, reasoning from the supplied evidence to the complete EC number."
  },
  "case_id": "EC_number_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as dihydropteroate synthase type 3, EC 2.5.1.15. The catalytic-activity annotation cites experimental evidence (ECO:0000269) for the reaction assigned that EC number; the entry was also present in the historical record checked. The annotation additionally has computational RuleBase support."
  },
  "important_caveats": [
    "Reviewer-only database and literature evidence supports the key but was not part of the evaluated model input.",
    "The UniProt annotation includes both computational and experimental evidence; the cited experimental evidence is reported in the entry, not independently validated here.",
    "The exact author source snapshot is unknown, although the sequence matched both current and checked historical records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation and cited catalytic-activity evidence support D; no supplied evidence supports another listed EC number for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as dihydropteroate synthase type 3, EC 2.5.1.15. The catalytic-activity annotation cites experimental evidence (ECO:0000269) for the reaction assigned that EC number; the entry was also present in the historical record checked. The annotation additionally has computational RuleBase support.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could support a broad inference about enzyme family if recognized or compared with known homologs, but the prompt supplies no organism, reaction, or functional context that distinguishes the precise EC assignment from the alternatives.",
    "missing_item_specific_fact": "The protein-specific identification as dihydropteroate synthase type 3, and its catalyzed reaction corresponding to EC 2.5.1.15, is needed to select D.",
    "reason": "The exact EC assignment depends on protein-specific functional knowledge or external annotation not given in the input. Recognizing the sequence or predicting its family is not, by itself, reasoning from the supplied evidence to the complete EC number."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation and cited catalytic-activity evidence support D; no supplied evidence supports another listed EC number for this protein."
  },
  "important_caveats": [
    "Reviewer-only database and literature evidence supports the key but was not part of the evaluated model input.",
    "The UniProt annotation includes both computational and experimental evidence; the cited experimental evidence is reported in the entry, not independently validated here.",
    "The exact author source snapshot is unknown, although the sequence matched both current and checked historical records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt C0HMD9 (DHP3_ECOLX, sul3 gene, E. coli plasmid pVP440) exactly (SHA-256 match confirmed). The entry is annotated EC=2.5.1.15 (dihydropteroate synthase type-3) with both computational (RuleBase RU361205) and experimental evidence (PubMed:37419898, X-ray crystallography PDB 7S2L/7S2M/8SCD). The catalytic reaction (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate → 7,8-dihydropteroate + diphosphate is experimentally confirmed. The answer D (2.5.1.15) is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the conserved 'DPGMG' motif (visible as DPGMGFFLGSNPETS), which is a recognized signature of dihydropteroate synthases. This could narrow the class to transferases (EC 2.x) and eliminate B (3.1.26.3, endoribonuclease) and C (5.3.1.8, isomerase). However, distinguishing between A (2.5.1.56) and D (2.5.1.15)—both in the same EC 2.5.1.x subclass—requires knowing the specific substrate/reaction catalyzed by EC 2.5.1.56, which is not derivable from the sequence by general reasoning.


**Missing item-specific fact**

> The identity and reaction catalyzed by EC 2.5.1.56 (the key distractor in the same 2.5.1.x subclass) is not provided in the question. Without knowing what 2.5.1.56 catalyzes, a reasoner cannot definitively exclude it based on sequence features alone. Recognizing the DPGMG motif as DHPS-specific is specialized pattern knowledge rather than general biological deduction.


**Reason**

> While B and C can be eliminated by class-level reasoning (the sequence lacks ribonuclease or isomerase hallmarks), the critical discrimination between A and D requires memorized knowledge of what EC 2.5.1.56 catalyzes and why the DPGMG motif is specific to DHPS rather than other 2.5.1.x transferases. This is an item-specific annotation lookup, not a general reasoning exercise.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the DPGMG motif and overall sequence architecture consistent with DHPS, D (2.5.1.15) is the most defensible answer. B and C are clearly wrong enzyme classes. A (2.5.1.56) is a plausible distractor but is not supported by the sequence features present. No genuine ambiguity remains once the DPGMG motif is recognized.


### Important caveats

- The EC annotation carries both RuleBase (computational) and PubMed (experimental, X-ray crystallography) evidence codes, strengthening confidence in the key.
- The protein is a plasmid-borne sulfonamide resistance gene (sul3), and its DHPS function was experimentally validated in a 2023 Nature Communications paper.
- The DPGMG motif recognition is specialized biochemistry knowledge; a model without training on this motif would struggle to distinguish A from D.
- The historical UniProt entry (version 2, released 2026-01) already contained the EC=2.5.1.15 annotation, so the key was available at the approximate benchmark construction date.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conserved 'DPGMG' motif (visible as DPGMGFFLGSNPETS), which is a recognized signature of dihydropteroate synthases. This could narrow the class to transferases (EC 2.x) and eliminate B (3.1.26.3, endoribonuclease) and C (5.3.1.8, isomerase). However, distinguishing between A (2.5.1.56) and D (2.5.1.15)—both in the same EC 2.5.1.x subclass—requires knowing the specific substrate/reaction catalyzed by EC 2.5.1.56, which is not derivable from the sequence by general reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity and reaction catalyzed by EC 2.5.1.56 (the key distractor in the same 2.5.1.x subclass) is not provided in the question. Without knowing what 2.5.1.56 catalyzes, a reasoner cannot definitively exclude it based on sequence features alone. Recognizing the DPGMG motif as DHPS-specific is specialized pattern knowledge rather than general biological deduction.",
    "reason": "While B and C can be eliminated by class-level reasoning (the sequence lacks ribonuclease or isomerase hallmarks), the critical discrimination between A and D requires memorized knowledge of what EC 2.5.1.56 catalyzes and why the DPGMG motif is specific to DHPS rather than other 2.5.1.x transferases. This is an item-specific annotation lookup, not a general reasoning exercise."
  },
  "case_id": "EC_number_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt C0HMD9 (DHP3_ECOLX, sul3 gene, E. coli plasmid pVP440) exactly (SHA-256 match confirmed). The entry is annotated EC=2.5.1.15 (dihydropteroate synthase type-3) with both computational (RuleBase RU361205) and experimental evidence (PubMed:37419898, X-ray crystallography PDB 7S2L/7S2M/8SCD). The catalytic reaction (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate → 7,8-dihydropteroate + diphosphate is experimentally confirmed. The answer D (2.5.1.15) is well-supported."
  },
  "important_caveats": [
    "The EC annotation carries both RuleBase (computational) and PubMed (experimental, X-ray crystallography) evidence codes, strengthening confidence in the key.",
    "The protein is a plasmid-borne sulfonamide resistance gene (sul3), and its DHPS function was experimentally validated in a 2023 Nature Communications paper.",
    "The DPGMG motif recognition is specialized biochemistry knowledge; a model without training on this motif would struggle to distinguish A from D.",
    "The historical UniProt entry (version 2, released 2026-01) already contained the EC=2.5.1.15 annotation, so the key was available at the approximate benchmark construction date."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the DPGMG motif and overall sequence architecture consistent with DHPS, D (2.5.1.15) is the most defensible answer. B and C are clearly wrong enzyme classes. A (2.5.1.56) is a plausible distractor but is not supported by the sequence features present. No genuine ambiguity remains once the DPGMG motif is recognized."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt C0HMD9 (DHP3_ECOLX, sul3 gene, E. coli plasmid pVP440) exactly (SHA-256 match confirmed). The entry is annotated EC=2.5.1.15 (dihydropteroate synthase type-3) with both computational (RuleBase RU361205) and experimental evidence (PubMed:37419898, X-ray crystallography PDB 7S2L/7S2M/8SCD). The catalytic reaction (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate → 7,8-dihydropteroate + diphosphate is experimentally confirmed. The answer D (2.5.1.15) is well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the conserved 'DPGMG' motif (visible as DPGMGFFLGSNPETS), which is a recognized signature of dihydropteroate synthases. This could narrow the class to transferases (EC 2.x) and eliminate B (3.1.26.3, endoribonuclease) and C (5.3.1.8, isomerase). However, distinguishing between A (2.5.1.56) and D (2.5.1.15)—both in the same EC 2.5.1.x subclass—requires knowing the specific substrate/reaction catalyzed by EC 2.5.1.56, which is not derivable from the sequence by general reasoning.",
    "missing_item_specific_fact": "The identity and reaction catalyzed by EC 2.5.1.56 (the key distractor in the same 2.5.1.x subclass) is not provided in the question. Without knowing what 2.5.1.56 catalyzes, a reasoner cannot definitively exclude it based on sequence features alone. Recognizing the DPGMG motif as DHPS-specific is specialized pattern knowledge rather than general biological deduction.",
    "reason": "While B and C can be eliminated by class-level reasoning (the sequence lacks ribonuclease or isomerase hallmarks), the critical discrimination between A and D requires memorized knowledge of what EC 2.5.1.56 catalyzes and why the DPGMG motif is specific to DHPS rather than other 2.5.1.x transferases. This is an item-specific annotation lookup, not a general reasoning exercise."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the DPGMG motif and overall sequence architecture consistent with DHPS, D (2.5.1.15) is the most defensible answer. B and C are clearly wrong enzyme classes. A (2.5.1.56) is a plausible distractor but is not supported by the sequence features present. No genuine ambiguity remains once the DPGMG motif is recognized."
  },
  "important_caveats": [
    "The EC annotation carries both RuleBase (computational) and PubMed (experimental, X-ray crystallography) evidence codes, strengthening confidence in the key.",
    "The protein is a plasmid-borne sulfonamide resistance gene (sul3), and its DHPS function was experimentally validated in a 2023 Nature Communications paper.",
    "The DPGMG motif recognition is specialized biochemistry knowledge; a model without training on this motif would struggle to distinguish A from D.",
    "The historical UniProt entry (version 2, released 2026-01) already contained the EC=2.5.1.15 annotation, so the key was available at the approximate benchmark construction date."
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

**Accession:** `C0HMD9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:26.472274+00:00.  

```json
"C0HMD9"
```

Source SHA-256: `ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:26.472274+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P0C002","source":"UniProtKB"}],"value":"Dihydropteroate pyrophosphorylase type III"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P0C002","source":"UniProtKB"}],"value":"Dihydropteroate synthase type III"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361205","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"37419898","source":"PubMed"}],"value":"2.5.1.15"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361205","source":"RuleBase"},{"evidenceCode":"ECO:0000303","id":"37419898","source":"PubMed"}],"value":"Dihydropteroate synthase type-3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361205","source":"RuleBase"},{"evidenceCode":"ECO:0000303","id":"37419898","source":"PubMed"}],"value":"DHPS"}]}}
```

Source SHA-256: `ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:26.472274+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.5.1.15","evidences":[{"evidenceCode":"ECO:0000269","id":"37419898","source":"PubMed"}],"name":"(7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19949"},{"database":"ChEBI","id":"CHEBI:17836"},{"database":"ChEBI","id":"CHEBI:17839"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:72950"}]}}
```

Source SHA-256: `ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:26.472274+00:00.  

```json
{"citation":{"authors":["Venkatesan M.","Fruci M.","Verellen L.A.","Skarina T.","Mesa N.","Flick R.","Pham C.","Mahadevan R.","Stogios P.J.","Savchenko A."],"citationCrossReferences":[{"database":"PubMed","id":"37419898"},{"database":"DOI","id":"10.1038/s41467-023-39778-7"}],"citationType":"journal article","firstPage":"4031","id":"37419898","journal":"Nat. Commun.","lastPage":"4031","publicationDate":"2023","title":"Molecular mechanism of plasmid-borne resistance to sulfonamide antibiotics.","volume":"14"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7S2L","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7S2M","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8SCD","source":"PDB"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.06 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH MG(2+) AND WITH SUBSTRATES","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF PHE-177 AND LEU-179"]}
```

Source SHA-256: `ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:27:30.074117+00:00.  

```text
DE   RecName: Full=Dihydropteroate synthase type-3 {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};
DE            Short=DHPS {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};
DE            EC=2.5.1.15 {ECO:0000255|RuleBase:RU361205, ECO:0000269|PubMed:37419898};
DE   AltName: Full=Dihydropteroate pyrophosphorylase type III {ECO:0000250|UniProtKB:P0C002};
DE   AltName: Full=Dihydropteroate synthase type III {ECO:0000250|UniProtKB:P0C002};
```

Source SHA-256: `471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)  
**Locator:** `lines 44-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:27:30.074117+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate =
CC         7,8-dihydropteroate + diphosphate; Xref=Rhea:RHEA:19949,
CC         ChEBI:CHEBI:17836, ChEBI:CHEBI:17839, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:72950; EC=2.5.1.15;
CC         Evidence={ECO:0000269|PubMed:37419898};
```

Source SHA-256: `471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 161. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
