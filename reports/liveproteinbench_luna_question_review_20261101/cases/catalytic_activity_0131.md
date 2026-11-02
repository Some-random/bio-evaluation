# catalytic_activity_0131

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MVIAVIPARSGSKGIKNKNLVLLNNQPLIYYTIKAALNSKCISKVLVSSDSEEILSYAKSQNVDILKRPIELAQDDTTSDKVLLHALEFYKDYEDVIFLQPTSPLRTNIHIDEAFKIYKNSDANALISVTECDNKILKAFICDNKGDLKGICDDEYPFMPRQKLPKTYMSNGAIYILSIKDFLNKPSFLQSKTKYFLMNKISSLDIDNLEDLKQVENIQKMKGCVVWISGLAGAGKTTISSGLYKKLKEKYNNSVLLDGDELRKIFKHTGYTREERLESAKKISSLCSFLAKNDIIVICATISLFEEIYLLNRNTIENYFEVFVDCPMEELILRDQKGLYSGALKGEIKDVVGVDIKYAKPNAHYIIDNSSKTDLEKKINNLYNEVELFFNKER

[Multiple Choices]
A. a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol
B. (2S)-3-(4-methoxyphenyl)-2-[(3S)-3-(methylamino)-8-oxo-1-azaspiro[4.5]decan-1-yl]propanal = (1S,3S,6S,7S,8R)-7-hydroxy-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecan-9-one
C. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
D. an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The supplied 394-residue sequence exactly matches the UniProt sequence annotated with reaction D. The annotation cites experimental evidence (ECO:0000269) for the N-acylneuraminate + CTP reaction, including its N-acetylneuraminate-specific form. This supports the key, while remaining an annotation tied to the cited study rather than an independent review of the experiment.

Cited evidence: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The reaction choices describe distinct enzyme activities, but the sequence and prompt provide no biological context or substrate information that identifies which activity this protein has. Generic sequence inspection does not establish the specific N-acylneuraminate substrate and CTP-dependent product.

**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence that this sequence encodes an N-acylneuraminate cytidylyltransferase.

**Reason**

> The key is supported by reviewer-only evidence, but that annotation and its cited experimental basis were not supplied to the evaluated model. Selecting D therefore depends on an external protein-specific fact, not merely on recognizing a general biochemical pattern.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The supplied evidence supports D, and the alternatives describe different reactions; no evidence makes another listed option defensible for this sequence.

### Important caveats

- The current and retrieved historical UniProt records both match the supplied sequence, but the author's exact source snapshot is unknown.
- The cited experimental evidence is reported in the database annotation; the underlying study was not independently reviewed here.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 394-residue sequence exactly matches the UniProt sequence annotated with reaction D. The annotation cites experimental evidence (ECO:0000269) for the N-acylneuraminate + CTP reaction, including its N-acetylneuraminate-specific form. This supports the key, while remaining an annotation tied to the cited study rather than an independent review of the experiment.",
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The reaction choices describe distinct enzyme activities, but the sequence and prompt provide no biological context or substrate information that identifies which activity this protein has. Generic sequence inspection does not establish the specific N-acylneuraminate substrate and CTP-dependent product.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence that this sequence encodes an N-acylneuraminate cytidylyltransferase.",
    "reason": "The key is supported by reviewer-only evidence, but that annotation and its cited experimental basis were not supplied to the evaluated model. Selecting D therefore depends on an external protein-specific fact, not merely on recognizing a general biochemical pattern."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D, and the alternatives describe different reactions; no evidence makes another listed option defensible for this sequence."
  },
  "important_caveats": [
    "The current and retrieved historical UniProt records both match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited experimental evidence is reported in the database annotation; the underlying study was not independently reviewed here."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `P0DY07`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 2. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:11345"}}],"reaction":{"ecNumber":"2.7.7.43","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:11344"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:37563"},{"database":"ChEBI","id":"CHEBI:60073"},{"database":"ChEBI","id":"CHEBI:68671"}]}}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:80844"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"N-acetylneuraminate + CTP = CMP-N-acetyl-beta-neuraminate + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80843"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:35418"},{"database":"ChEBI","id":"CHEBI:37563"},{"database":"ChEBI","id":"CHEBI:57812"}]}}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)  
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.379520+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate +
CC         diphosphate; Xref=Rhea:RHEA:11344, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:37563, ChEBI:CHEBI:60073, ChEBI:CHEBI:68671; EC=2.7.7.43;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:11345;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)  
**Locator:** `lines 47-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.379520+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N-acetylneuraminate + CTP = CMP-N-acetyl-beta-neuraminate +
CC         diphosphate; Xref=Rhea:RHEA:80843, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:35418, ChEBI:CHEBI:37563, ChEBI:CHEBI:57812;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80844;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 131). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
