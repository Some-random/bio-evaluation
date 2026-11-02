# cofactor_0037

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQPEFTRSIVGASFLLPVINGAMHIPPAVSATRVTLEDNQPRDAPILVLLFALSVLIDVMDKAADLPRQTRKTWLMTIVVFASPFVVLAVYGTMHCGLLALLRLLGVPLLAVVHAMPLIPVYSWKTGSISTVKLKYFLGPFKSLFGATCIGLMDVTAVVLYLRGTMLHPENASSAGHFRVLMYTITYDFLWESICDVRDIQEDEQNNITTLATAFGVRPTLIFLGGSTMMGDLSITLLGGGSAVLSVVRSTVFWGAFAALALHKPRSAVYPWGLATLFGLLPVWLASLGART

[Multiple Choices]
A. a divalent metal cation
B. Mg(2+)
C. heme b
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

> The sequence exactly matches the UniProt entry for prenyltransferase vviA, whose cofactor is annotated as Mg(2+) with experimental evidence linked to PubMed 39310987. The primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The highly hydrophobic sequence is consistent with a membrane protein, but that does not distinguish Mg(2+) from other divalent ions or establish a specific cofactor. General enzyme knowledge is insufficient to identify this protein's particular cofactor.


**Missing item-specific fact**

> The protein-specific annotation or experimental finding that vviA requires Mg(2+), associated with PubMed 39310987, is absent from the question input.


**Reason**

> The sequence alone does not provide a decisive cofactor signature for the offered choices. The supported answer depends on protein-specific information not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A divalent metal cation is a broad description that includes Mg(2+). B is the more specific supported answer, but A is also compatible with that finding unless the choices are intended to be mutually exclusive.


### Important caveats

- The reviewer-only evidence is a UniProt annotation citing experimental evidence; the cited primary study was not independently validated.
- The sequence match establishes applicability of the annotation to the supplied sequence, but does not mean the annotation was available in the original question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The highly hydrophobic sequence is consistent with a membrane protein, but that does not distinguish Mg(2+) from other divalent ions or establish a specific cofactor. General enzyme knowledge is insufficient to identify this protein's particular cofactor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation or experimental finding that vviA requires Mg(2+), associated with PubMed 39310987, is absent from the question input.",
    "reason": "The sequence alone does not provide a decisive cofactor signature for the offered choices. The supported answer depends on protein-specific information not supplied to the evaluated model."
  },
  "case_id": "cofactor_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for prenyltransferase vviA, whose cofactor is annotated as Mg(2+) with experimental evidence linked to PubMed 39310987. The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only evidence is a UniProt annotation citing experimental evidence; the cited primary study was not independently validated.",
    "The sequence match establishes applicability of the annotation to the supplied sequence, but does not mean the annotation was available in the original question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A divalent metal cation is a broad description that includes Mg(2+). B is the more specific supported answer, but A is also compatible with that finding unless the choices are intended to be mutually exclusive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for prenyltransferase vviA, whose cofactor is annotated as Mg(2+) with experimental evidence linked to PubMed 39310987. The primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The highly hydrophobic sequence is consistent with a membrane protein, but that does not distinguish Mg(2+) from other divalent ions or establish a specific cofactor. General enzyme knowledge is insufficient to identify this protein's particular cofactor.",
    "missing_item_specific_fact": "The protein-specific annotation or experimental finding that vviA requires Mg(2+), associated with PubMed 39310987, is absent from the question input.",
    "reason": "The sequence alone does not provide a decisive cofactor signature for the offered choices. The supported answer depends on protein-specific information not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A divalent metal cation is a broad description that includes Mg(2+). B is the more specific supported answer, but A is also compatible with that finding unless the choices are intended to be mutually exclusive."
  },
  "important_caveats": [
    "The reviewer-only evidence is a UniProt annotation citing experimental evidence; the cited primary study was not independently validated.",
    "The sequence match establishes applicability of the annotation to the supplied sequence, but does not mean the annotation was available in the original question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A6A6H402 (Prenyltransferase vviA, EC 2.5.1.-, from Viridothelium virens) explicitly annotates Mg(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:39310987, Tang & Zou 2024, Org. Lett.). The sequence in the question matches the UniProt entry exactly (293 aa, SHA-256 match). The annotation is backed by functional and mutagenesis experiments from the cited paper.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 293-aa sequence is dominated by long hydrophobic stretches forming multiple transmembrane helices, characteristic of membrane-bound aromatic prenyltransferases (EC 2.5.1.-). Prenyltransferases catalyze the condensation of a prenyl diphosphate (e.g., FPP, DMAPP) with an aromatic acceptor; the canonical mechanism requires Mg(2+) to coordinate and stabilize the diphosphate leaving group. This is standard textbook biochemistry. Heme b (C) and Fe(2+) (D) are cofactors of oxidoreductases/oxygenases, not prenyltransferases. Between A ('a divalent metal cation') and B ('Mg(2+)'), the question asks for the specific cofactor, and Mg(2+) is the well-established, experimentally validated specific metal for prenyltransferases.


**Missing item-specific fact**

> None that is strictly required. The transmembrane architecture and general prenyltransferase biochemistry are sufficient to narrow to Mg(2+). However, confirming that this particular enzyme does not accept Mn(2+) or another divalent cation in vitro would require the specific experimental data from PubMed:39310987.


**Reason**

> A knowledgeable model can reason from the multi-TM-helix membrane architecture toward a membrane-bound prenyltransferase, then invoke the well-known Mg(2+)-dependent diphosphate-activation mechanism of EC 2.5.1.- enzymes. The distractors (heme b, Fe(2+)) are eliminated because they belong to entirely different enzyme classes. The distinction between A and B rests on the question asking for the 'specific' cofactor, and Mg(2+) is the canonical specific metal for prenyltransferases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Mg(2+) is itself a divalent metal cation, so option A ('a divalent metal cation') is not factually wrong—it is merely less specific. A cautious model that identifies the cofactor as a divalent cation but cannot commit to Mg(2+) over Mn(2+) might select A. However, the question stem asks for 'the specific cofactor,' which conventionally favors the more precise answer B. This is a standard MCQ specificity hierarchy, not a true factual ambiguity, but it introduces mild interpretive tension.


### Important caveats

- The cofactor annotation carries evidence code ECO:0000269 (experimental), sourced from PubMed:39310987 (Tang & Zou, Org. Lett. 2024), indicating the Mg(2+) requirement was demonstrated experimentally rather than inferred by similarity.
- The UniProt entry was first publicly released 2025-04-09; the benchmark author's exact source snapshot is unknown. The sequence match is exact (293 aa, SHA-256 identical) across both current (v13) and historical (v12) records.
- Option A is not factually false—Mg(2+) is a divalent metal cation—but it is less specific than the question demands.
- The reviewer-only evidence (UniProt accession, annotation excerpts) was not available to the evaluated model; the reasoning assessment considers only what could be inferred from the sequence and general biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 293-aa sequence is dominated by long hydrophobic stretches forming multiple transmembrane helices, characteristic of membrane-bound aromatic prenyltransferases (EC 2.5.1.-). Prenyltransferases catalyze the condensation of a prenyl diphosphate (e.g., FPP, DMAPP) with an aromatic acceptor; the canonical mechanism requires Mg(2+) to coordinate and stabilize the diphosphate leaving group. This is standard textbook biochemistry. Heme b (C) and Fe(2+) (D) are cofactors of oxidoreductases/oxygenases, not prenyltransferases. Between A ('a divalent metal cation') and B ('Mg(2+)'), the question asks for the specific cofactor, and Mg(2+) is the well-established, experimentally validated specific metal for prenyltransferases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is strictly required. The transmembrane architecture and general prenyltransferase biochemistry are sufficient to narrow to Mg(2+). However, confirming that this particular enzyme does not accept Mn(2+) or another divalent cation in vitro would require the specific experimental data from PubMed:39310987.",
    "reason": "A knowledgeable model can reason from the multi-TM-helix membrane architecture toward a membrane-bound prenyltransferase, then invoke the well-known Mg(2+)-dependent diphosphate-activation mechanism of EC 2.5.1.- enzymes. The distractors (heme b, Fe(2+)) are eliminated because they belong to entirely different enzyme classes. The distinction between A and B rests on the question asking for the 'specific' cofactor, and Mg(2+) is the canonical specific metal for prenyltransferases."
  },
  "case_id": "cofactor_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A6A6H402 (Prenyltransferase vviA, EC 2.5.1.-, from Viridothelium virens) explicitly annotates Mg(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:39310987, Tang & Zou 2024, Org. Lett.). The sequence in the question matches the UniProt entry exactly (293 aa, SHA-256 match). The annotation is backed by functional and mutagenesis experiments from the cited paper."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000269 (experimental), sourced from PubMed:39310987 (Tang & Zou, Org. Lett. 2024), indicating the Mg(2+) requirement was demonstrated experimentally rather than inferred by similarity.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's exact source snapshot is unknown. The sequence match is exact (293 aa, SHA-256 identical) across both current (v13) and historical (v12) records.",
    "Option A is not factually false—Mg(2+) is a divalent metal cation—but it is less specific than the question demands.",
    "The reviewer-only evidence (UniProt accession, annotation excerpts) was not available to the evaluated model; the reasoning assessment considers only what could be inferred from the sequence and general biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Mg(2+) is itself a divalent metal cation, so option A ('a divalent metal cation') is not factually wrong—it is merely less specific. A cautious model that identifies the cofactor as a divalent cation but cannot commit to Mg(2+) over Mn(2+) might select A. However, the question stem asks for 'the specific cofactor,' which conventionally favors the more precise answer B. This is a standard MCQ specificity hierarchy, not a true factual ambiguity, but it introduces mild interpretive tension."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A6A6H402 (Prenyltransferase vviA, EC 2.5.1.-, from Viridothelium virens) explicitly annotates Mg(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:39310987, Tang & Zou 2024, Org. Lett.). The sequence in the question matches the UniProt entry exactly (293 aa, SHA-256 match). The annotation is backed by functional and mutagenesis experiments from the cited paper.",
    "evidence_ids": ["C5", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 293-aa sequence is dominated by long hydrophobic stretches forming multiple transmembrane helices, characteristic of membrane-bound aromatic prenyltransferases (EC 2.5.1.-). Prenyltransferases catalyze the condensation of a prenyl diphosphate (e.g., FPP, DMAPP) with an aromatic acceptor; the canonical mechanism requires Mg(2+) to coordinate and stabilize the diphosphate leaving group. This is standard textbook biochemistry. Heme b (C) and Fe(2+) (D) are cofactors of oxidoreductases/oxygenases, not prenyltransferases. Between A ('a divalent metal cation') and B ('Mg(2+)'), the question asks for the specific cofactor, and Mg(2+) is the well-established, experimentally validated specific metal for prenyltransferases.",
    "missing_item_specific_fact": "None that is strictly required. The transmembrane architecture and general prenyltransferase biochemistry are sufficient to narrow to Mg(2+). However, confirming that this particular enzyme does not accept Mn(2+) or another divalent cation in vitro would require the specific experimental data from PubMed:39310987.",
    "reason": "A knowledgeable model can reason from the multi-TM-helix membrane architecture toward a membrane-bound prenyltransferase, then invoke the well-known Mg(2+)-dependent diphosphate-activation mechanism of EC 2.5.1.- enzymes. The distractors (heme b, Fe(2+)) are eliminated because they belong to entirely different enzyme classes. The distinction between A and B rests on the question asking for the 'specific' cofactor, and Mg(2+) is the canonical specific metal for prenyltransferases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Mg(2+) is itself a divalent metal cation, so option A ('a divalent metal cation') is not factually wrong—it is merely less specific. A cautious model that identifies the cofactor as a divalent cation but cannot commit to Mg(2+) over Mn(2+) might select A. However, the question stem asks for 'the specific cofactor,' which conventionally favors the more precise answer B. This is a standard MCQ specificity hierarchy, not a true factual ambiguity, but it introduces mild interpretive tension."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000269 (experimental), sourced from PubMed:39310987 (Tang & Zou, Org. Lett. 2024), indicating the Mg(2+) requirement was demonstrated experimentally rather than inferred by similarity.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's exact source snapshot is unknown. The sequence match is exact (293 aa, SHA-256 identical) across both current (v13) and historical (v12) records.",
    "Option A is not factually false—Mg(2+) is a divalent metal cation—but it is less specific than the question demands.",
    "The reviewer-only evidence (UniProt accession, annotation excerpts) was not available to the evaluated model; the reasoning assessment considers only what could be inferred from the sequence and general biochemistry."
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

**Accession:** `A0A6A6H402` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
"A0A6A6H402"
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39310987","source":"PubMed"}],"value":"Sporulositol A biosynthesis cluster protein A"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39310987","source":"PubMed"}],"value":"2.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39310987","source":"PubMed"}],"value":"Prenyltransferase vviA"}}}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000269","id":"39310987","source":"PubMed"}],"name":"Mg(2+)"}],"commentType":"COFACTOR"}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"citation":{"authors":["Tang Y.J.","Zou Y."],"citationCrossReferences":[{"database":"PubMed","id":"39310987"},{"database":"DOI","id":"10.1021/acs.orglett.4c03154"}],"citationType":"journal article","firstPage":"8366","id":"39310987","journal":"Org. Lett.","lastPage":"8370","publicationDate":"2024","title":"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.","volume":"26"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","PATHWAY","MUTAGENESIS OF LEU-17; ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND THR-277"]}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 29-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, PATHWAY, AND MUTAGENESIS OF LEU-17;
RP   ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND
RP   THR-277.
RX   PubMed=39310987; DOI=10.1021/acs.orglett.4c03154;
RA   Tang Y.J., Zou Y.;
RT   "Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.";
RL   Org. Lett. 26:8366-8370(2024).
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 55-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000269|PubMed:39310987};
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
