# EC_number_0055

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.1.1.17

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MSDMKAIHFGGGNIGRGFVAEFLHKSGYEVVFVDVMDAIINALQQNKSYTVTEVGTSETKSKTIDNYRAINSKTDEDKVVEEIATADIVTCAVGPNILKFIAPVIAKGIENRKKDSPIAVIACENAIGATDTLRKFIEEKLSDSTKSNIQDKARFANSAIDRIVPMQDENAGLNVKIEKFYEWCVESKPFLPSQPPKIEGVHFVEDLTPFIERKLFTVNTGHATAAYYGYNRGKECIHDVLQDKELNEIVRNTLKETAHLIVNKHEISEEDQNQYVEKIIKRISNPVLKDNVERVGRAPLRKLSRNERFIGPAAHLAEMGAKYDALLGGIEMCLRFQNVEGDDESFELAKILKENSSSDATEKITGLERNHTLFPAVEEVVKKVQA

[Multiple Choices]
A. 1.1.1.336
B. 5.6.1.1
C. 2.7.1.39
D. 1.1.1.17
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

## Luna’s full visible review

### Expected-answer support: supported

> The supplied sequence exactly matches the UniProt entry annotated as EC 1.1.1.17, mannitol-1-phosphate 5-dehydrogenase. The annotation and catalytic reaction are supported by a transferred annotation (ECO:0000250), not shown here as a direct experimental measurement on this protein.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support broad enzyme-family inference, but no supplied context establishes the specific substrate and reaction needed to distinguish EC 1.1.1.17 from another dehydrogenase option.

**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence identifying its catalytic reaction as mannitol-1-phosphate oxidation/reduction.

**Reason**

> The exact EC assignment relies on a protein-specific functional fact absent from the question. Identifying the sequence from memory or consulting its database record would be lookup, not reasoning from the provided input.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The choices specify distinct EC activities; the evidence supports D, although the sequence and context supplied to the model do not independently establish that exact activity.

### Important caveats

- The supporting UniProt EC annotation is transferred by similarity (ECO:0000250); it does not by itself establish direct experimental verification for this exact protein.
- The sequence match and historical annotation support the expected answer, but the author's exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "EC_number_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as EC 1.1.1.17, mannitol-1-phosphate 5-dehydrogenase. The annotation and catalytic reaction are supported by a transferred annotation (ECO:0000250), not shown here as a direct experimental measurement on this protein.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support broad enzyme-family inference, but no supplied context establishes the specific substrate and reaction needed to distinguish EC 1.1.1.17 from another dehydrogenase option.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence identifying its catalytic reaction as mannitol-1-phosphate oxidation/reduction.",
    "reason": "The exact EC assignment relies on a protein-specific functional fact absent from the question. Identifying the sequence from memory or consulting its database record would be lookup, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC activities; the evidence supports D, although the sequence and context supplied to the model do not independently establish that exact activity."
  },
  "important_caveats": [
    "The supporting UniProt EC annotation is transferred by similarity (ECO:0000250); it does not by itself establish direct experimental verification for this exact protein.",
    "The sequence match and historical annotation support the expected answer, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A223HDH4`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 15. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
"A0A223HDH4"
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1A4","source":"UniProtKB"}],"value":"1.1.1.17"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"Mannitol-1-phosphate 5-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"MPDH"}]}}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.17","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1A4","source":"UniProtKB"}],"name":"D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19661"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57634"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:61381"}]}}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
DE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};
DE            Short=MPDH {ECO:0000303|PubMed:32003433};
DE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 53-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate
CC         + NADH + H(+); Xref=Rhea:RHEA:19661, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57634, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:61381; EC=1.1.1.17;
CC         Evidence={ECO:0000250|UniProtKB:Q4X1A4};
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json) (zero-based source row 55). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
