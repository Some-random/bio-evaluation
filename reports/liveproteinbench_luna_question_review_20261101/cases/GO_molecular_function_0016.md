# GO_molecular_function_0016

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — beta-lactamase activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MKLLKILSLVCLSISIGACAEHSMSRAKTSTIPQVNNSIIDQNVQALFNEISADAVFVTYDGQNIKKYGTHLDRAKTAYIPASTFKIANALIGLENHKATSTEIFKWDGKPRFFKAWDKDFTLGEAMQASTVPVYQELARRIGPSLMQSELQRIGYGNMQIGTEVDQFWLKGPLTITPIQEVKFVYDLAQGQLPFKPEVQQQVKEMLYVERRGENRLYAKSGWGMAVDPQVGWYVGFVEKADGQVVAFALNMQMKAGDDIALRKQLSLDVLDKLGVFHYL

[Multiple Choices]
A. mRNA binding
B. beta-glucuronidase activity
C. oxidoreductase activity, acting on NAD(P)H
D. beta-lactamase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The supplied sequence matches the historical OXA-58 record, which reports beta-lactam hydrolysis and beta-lactamase activity with experimental evidence. This supports choice D.

Cited evidence: [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the characteristic STFK motif of class D beta-lactamases, along with a YGN motif; these sequence features support beta-lactamase activity over the listed binding, glucuronidase, and NAD(P)H-dependent oxidoreductase alternatives.

**Missing item-specific fact**

> No item-specific annotation is necessary for the broad distinction if the characteristic motifs are recognized; exact OXA-58 identity and experimentally documented substrate activity are not supplied.

**Reason**

> The sequence provides recognizable enzyme-family evidence that meaningfully favors beta-lactamase activity. The reviewer-only database evidence supports the key but is not needed as input to this inference.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The listed alternatives describe distinct functions, and the sequence motifs support beta-lactamase activity.

### Important caveats

- The historical UniProt record and experimental evidence support this exact sequence; this does not imply that every listed substrate is hydrolyzed equally or in every biological context.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the historical OXA-58 record, which reports beta-lactam hydrolysis and beta-lactamase activity with experimental evidence. This supports choice D.",
    "evidence_ids": [
      "H5",
      "H6",
      "H7"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the characteristic STFK motif of class D beta-lactamases, along with a YGN motif; these sequence features support beta-lactamase activity over the listed binding, glucuronidase, and NAD(P)H-dependent oxidoreductase alternatives.",
    "missing_item_specific_fact": "No item-specific annotation is necessary for the broad distinction if the characteristic motifs are recognized; exact OXA-58 identity and experimentally documented substrate activity are not supplied.",
    "reason": "The sequence provides recognizable enzyme-family evidence that meaningfully favors beta-lactamase activity. The reviewer-only database evidence supports the key but is not needed as input to this inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives describe distinct functions, and the sequence motifs support beta-lactamase activity."
  },
  "important_caveats": [
    "The historical UniProt record and experimental evidence support this exact sequence; this does not imply that every listed substrate is hydrolyzed equally or in every biological context."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q2TR58`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 133. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 257-265`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
CC   -!- FUNCTION: Class D beta-lactamase which confers resistance to the beta-
CC       lactam antibiotics, including penicillins and oxacillin, and moderate
CC       resistance to carbapenems such as imipenem; in the DH10B strain of
CC       E.coli (PubMed:15616297). Acts via hydrolysis of the beta-lactam ring
CC       (PubMed:15616297, PubMed:26459904, PubMed:26701320). Has
CC       benzylpenicillin-, oxacillin-, cephalothin- and imipenem-hydrolyzing
CC       activities (PubMed:15616297, PubMed:26459904, PubMed:26701320).
CC       {ECO:0000269|PubMed:15616297, ECO:0000269|PubMed:26459904,
CC       ECO:0000269|PubMed:26701320}.
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 266-271`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a beta-lactam + H2O = a substituted beta-amino acid;
CC         Xref=Rhea:RHEA:20401, ChEBI:CHEBI:15377, ChEBI:CHEBI:35627,
CC         ChEBI:CHEBI:140347; EC=3.5.2.6;
CC         Evidence={ECO:0000269|PubMed:15616297, ECO:0000269|PubMed:26459904,
CC         ECO:0000269|PubMed:26701320};
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 429-429`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
DR   GO; GO:0008800; F:beta-lactamase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 16). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
