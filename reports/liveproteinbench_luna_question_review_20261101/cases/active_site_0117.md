# active_site_0117

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 299 (Proton acceptor)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MVCVPSSSSVMELANLISQSIPKLQDESPQRANDARGNVIEACSKMLALVTSPAEMLKEMVLINLASLQVINHYQIASVVPLNGHIPISELANKCGLPVDILRRILRQAMTYGAFSEPEPDCIAQTDVSREIPRLSPLLTYQLDVCLPSMVRLLDWLKDVDGEHACAYQIAHDTKDTWWSYASKRPELIENYGKYMALITSGGAHDVSYVLKGFAWEKLGNAVVVDVGGADGFVGISLAKEYPNLAVIVEDNLGLKDSADDNIPQHLKSRVVFLPHSFFKPQSALSRDADVFLLRHILHDWNDNDCRAILQALAASMKPGASILVAEQILQRPGAASWQRERVMRALDMQMMIQFGSKERAYEDWDALFKSVDPPLEIVDCVQPVGSADSFMELKRRA

[Multiple Choices]
A. Position 700 (For beta-ketoacyl synthase activity)
B. Position 6003 (For beta-ketoacyl synthase 4 activity)
C. Position 299 (Proton acceptor)
D. Position 2882 (Proton donor; for dehydratase activity 2)
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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence matches the 398-residue UniProt entry, which annotates position 299 as an active-site proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental confirmation.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence is 398 residues long. Positions 700, 6003, and 2882 in choices A, B, and D are outside the sequence, whereas position 299 in C is in range; this coordinate check distinguishes the only viable choice.

**Missing item-specific fact**

> The sequence and choices alone do not establish that residue 299 is chemically a proton acceptor; validating that role requires protein-specific annotation or experimental evidence.

**Reason**

> Although the catalytic role itself is not inferable from the input, the sequence length makes the other three listed positions impossible, providing a concrete basis to select C among these choices.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Only position 299 falls within the 398-residue sequence.

### Important caveats

- The active-site annotation is computationally assigned by PROSITE-ProRule, not shown here to be experimentally validated.
- The sequence-specific database match and annotation are reviewer-only evidence and were not supplied to the evaluated model.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "active_site_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the 398-residue UniProt entry, which annotates position 299 as an active-site proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental confirmation.",
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence is 398 residues long. Positions 700, 6003, and 2882 in choices A, B, and D are outside the sequence, whereas position 299 in C is in range; this coordinate check distinguishes the only viable choice.",
    "missing_item_specific_fact": "The sequence and choices alone do not establish that residue 299 is chemically a proton acceptor; validating that role requires protein-specific annotation or experimental evidence.",
    "reason": "Although the catalytic role itself is not inferable from the input, the sequence length makes the other three listed positions impossible, providing a concrete basis to select C among these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 299 falls within the 398-residue sequence."
  },
  "important_caveats": [
    "The active-site annotation is computationally assigned by PROSITE-ProRule, not shown here to be experimentally validated.",
    "The sequence-specific database match and annotation are reviewer-only evidence and were not supplied to the evaluated model."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q2TXQ1`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 93. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:40.416982+00:00.  

```json
"Q2TXQ1"
```

Source SHA-256: `fd213e19e4caadb8bee82031ee55fe37480732c62de951e9e10e42a1c1be159a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ1.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:40.416982+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01020","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":299},"start":{"modifier":"EXACT","value":299}},"type":"Active site"}
```

Source SHA-256: `fd213e19e4caadb8bee82031ee55fe37480732c62de951e9e10e42a1c1be159a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ1?format=txt&versions=93)  
**Locator:** `lines 87-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 93 / 1.  
**Retrieved:** 2026-11-02T04:30:42.439973+00:00.  

```text
FT   ACT_SITE        299
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01020"
```

Source SHA-256: `d7b4a437ade459e083a2ed6a8bb2cb9041984b055e171ef54deebbf8b9742453`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json) (zero-based source row 117). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
