# EC_number_0163

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.7.1.52

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQKLLSLPSNLVQSFHELERVNRTDWFCTSDPVGKKLGSGGGTSWLLEECYNEYSDGATFGEWLEKEKRILLHAGGQSRRLPGYAPSGKILTPVPVFRWERGQHLGQNLLSLQLPLYEKIMSLAPDKLHTLIASGDVYIRSEKPLQSIPEADVVCYGLWVDPSLATHHGVFASDRKHPEQLDFMLQKPSLAELESLSKTHLFLMDIGIWLLSDRAVEILMKRSHKESSEELKYYDLYSDFGLALGTHPRIEDEEVNTLSVAILPLPGGEFYHYGTSKELISSTLSVQNKVYDQRRIMHRKVKPNPAMFVQNAVVRIPLCAENADLWIENSHIGPKWKIASRHIITGVPENDWSLAVPAGVCVDVVPMGDKGFVARPYGLDDVFKGDLRDSKTTLTGIPFGEWMSKRGLSYTDLKGRTDDLQAVSVFPMVNSVEELGLVLRWMLSEPELEEGKNIWLRSEHFSADEISAGANLKRLYAQREEFRKGNWKALAVNHEKSVFYQLDLADAAEDFVRLGLDMPELLPEDALQMSRIHNRMLRARILKLDGKDYRPEEQAAFDLLRDGLLDGISNRKSTPKLDVYSDQIVWGRSPVRIDMAGGWTDTPPYSLYSGGNVVNLAIELNGQPPLQVYVKPCKDFHIVLRSIDMGAMEIVSTFDELQDYKKIGSPFSIPKAALSLAGFAPAFSAVSYASLEEQLKDFGAGIEVTLLAAIPAGSGLGTSSILASTVLGAINDFCGLAWDKNEICQRTLVLEQLLTTGGGWQDQYGGVLQGVKLLQTEAGFAQSPLVRWLPDHLFTHPEYKDCHLLYYTGITRTAKGILAEIVSSMFLNSSLHLNLLSEMKAHALDMNEAIQRGSFVEFGRLVGKTWEQNKALDSGTNPPAVEAIIDLIKDYTLGYKLPGAGGGGYLYMVAKDPQAAVRIRKILTENAPNPRARFVEMTLSDKGFQVSRS

[Multiple Choices]
A. 2.7.2.4
B. 3.2.2.5
C. 2.7.1.52
D. 2.7.8.43
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

> The exact sequence matches the Bacteroides fragilis FKP entry, which assigns EC 2.7.1.52 to its L-fucokinase activity. The annotation cites experimental evidence, though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support broad functional clues, but those do not establish that this protein phosphorylates L-fucose specifically rather than catalyzing another reaction in the listed EC classes.


**Missing item-specific fact**

> The protein-specific substrate and reaction assignment identifying its L-fucokinase activity as EC 2.7.1.52.


**Reason**

> Choosing C requires a specific functional assignment not supplied in the prompt; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only C is supported by the cited L-fucokinase activity. However, the protein is bifunctional and also has EC 2.7.7.30 activity, which is not offered.


### Important caveats

- The evidence matches the supplied sequence and attributes EC 2.7.1.52 to one of the protein's activities; it does not imply that this is the protein's only EC number.
- The evidence is a database annotation citing a publication with experimental evidence codes; the underlying paper was not independently examined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support broad functional clues, but those do not establish that this protein phosphorylates L-fucose specifically rather than catalyzing another reaction in the listed EC classes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate and reaction assignment identifying its L-fucokinase activity as EC 2.7.1.52.",
    "reason": "Choosing C requires a specific functional assignment not supplied in the prompt; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the provided input."
  },
  "case_id": "EC_number_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Bacteroides fragilis FKP entry, which assigns EC 2.7.1.52 to its L-fucokinase activity. The annotation cites experimental evidence, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The evidence matches the supplied sequence and attributes EC 2.7.1.52 to one of the protein's activities; it does not imply that this is the protein's only EC number.",
    "The evidence is a database annotation citing a publication with experimental evidence codes; the underlying paper was not independently examined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only C is supported by the cited L-fucokinase activity. However, the protein is bifunctional and also has EC 2.7.7.30 activity, which is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Bacteroides fragilis FKP entry, which assigns EC 2.7.1.52 to its L-fucokinase activity. The annotation cites experimental evidence, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support broad functional clues, but those do not establish that this protein phosphorylates L-fucose specifically rather than catalyzing another reaction in the listed EC classes.",
    "missing_item_specific_fact": "The protein-specific substrate and reaction assignment identifying its L-fucokinase activity as EC 2.7.1.52.",
    "reason": "Choosing C requires a specific functional assignment not supplied in the prompt; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only C is supported by the cited L-fucokinase activity. However, the protein is bifunctional and also has EC 2.7.7.30 activity, which is not offered."
  },
  "important_caveats": [
    "The evidence matches the supplied sequence and attributes EC 2.7.1.52 to one of the protein's activities; it does not imply that this is the protein's only EC number.",
    "The evidence is a database annotation citing a publication with experimental evidence codes; the underlying paper was not independently examined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q58T34 (FKP_BACFG) is annotated with EC 2.7.1.52 (L-fucokinase) with experimental evidence (ECO:0000269|PubMed:30242642). The catalytic activity 'beta-L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H+' is confirmed. The protein is bifunctional (also EC 2.7.7.30), but 2.7.7.30 is not among the answer choices, so C is the only option matching a verified annotation for this sequence. Sequence match is confirmed (949 aa, SHA-256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a glycine-rich P-loop-like motif ('GSGGGTSWLLEECYNEYSDGATFGEWLE') suggestive of kinase/phosphotransferase activity, which could eliminate option B (EC 3.2.2.5, a glycosylase/hydrolase). However, the remaining three options (A: 2.7.2.4, C: 2.7.1.52, D: 2.7.8.43) are all phosphotransferases (class 2.7) differing only in acceptor group type (nitrogenous, alcohol, phosphatidyl). No general sequence feature reliably distinguishes L-fucokinase (2.7.1.52) from a phosphotransferase with nitrogenous acceptor (2.7.2.4) or a phosphatidyltransferase (2.7.8.43) without database-level identification of this specific protein.


**Missing item-specific fact**

> The specific identification of this 949-aa Bacteroides fragilis protein as L-fucokinase/GDP-fucose pyrophosphorylase (FKP), which requires recognizing the protein family or looking up the UniProt entry Q58T34. The substrate specificity for L-fucose (vs. other alcohol-group acceptors, nitrogenous acceptors, or phosphatidyl acceptors) cannot be inferred from general sequence motifs alone.


**Reason**

> While the P-loop motif weakly supports a phosphotransferase (eliminating B), distinguishing among the three EC 2.7 subclasses requires protein-specific annotation or memorization of this particular enzyme's identity. No general biological reasoning path from the raw sequence reliably selects 2.7.1.52 over 2.7.2.4 or 2.7.8.43.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is bifunctional (EC 2.7.1.52 and EC 2.7.7.30), only 2.7.1.52 appears among the four choices, so no two options are simultaneously defensible. The singular phrasing 'the complete 4-digit EC number' is slightly imprecise for a bifunctional enzyme but does not create ambiguity among the given options.


### Important caveats

- The protein is bifunctional; the question asks for a single EC number. EC 2.7.7.30 (the other activity) is not offered as an option, so the expected answer is unambiguous among the choices but incomplete as a full functional description.
- The EC 2.7.1.52 annotation carries experimental evidence (ECO:0000269) from a 2019 cryo-EM and biochemical study (PubMed:30242642), not merely computational transfer.
- The UniProt entry was first integrated in Feb 2025; the benchmark author's source snapshot date is unknown, so the annotation may not have been available at the time the question was constructed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a glycine-rich P-loop-like motif ('GSGGGTSWLLEECYNEYSDGATFGEWLE') suggestive of kinase/phosphotransferase activity, which could eliminate option B (EC 3.2.2.5, a glycosylase/hydrolase). However, the remaining three options (A: 2.7.2.4, C: 2.7.1.52, D: 2.7.8.43) are all phosphotransferases (class 2.7) differing only in acceptor group type (nitrogenous, alcohol, phosphatidyl). No general sequence feature reliably distinguishes L-fucokinase (2.7.1.52) from a phosphotransferase with nitrogenous acceptor (2.7.2.4) or a phosphatidyltransferase (2.7.8.43) without database-level identification of this specific protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this 949-aa Bacteroides fragilis protein as L-fucokinase/GDP-fucose pyrophosphorylase (FKP), which requires recognizing the protein family or looking up the UniProt entry Q58T34. The substrate specificity for L-fucose (vs. other alcohol-group acceptors, nitrogenous acceptors, or phosphatidyl acceptors) cannot be inferred from general sequence motifs alone.",
    "reason": "While the P-loop motif weakly supports a phosphotransferase (eliminating B), distinguishing among the three EC 2.7 subclasses requires protein-specific annotation or memorization of this particular enzyme's identity. No general biological reasoning path from the raw sequence reliably selects 2.7.1.52 over 2.7.2.4 or 2.7.8.43."
  },
  "case_id": "EC_number_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q58T34 (FKP_BACFG) is annotated with EC 2.7.1.52 (L-fucokinase) with experimental evidence (ECO:0000269|PubMed:30242642). The catalytic activity 'beta-L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H+' is confirmed. The protein is bifunctional (also EC 2.7.7.30), but 2.7.7.30 is not among the answer choices, so C is the only option matching a verified annotation for this sequence. Sequence match is confirmed (949 aa, SHA-256 identical)."
  },
  "important_caveats": [
    "The protein is bifunctional; the question asks for a single EC number. EC 2.7.7.30 (the other activity) is not offered as an option, so the expected answer is unambiguous among the choices but incomplete as a full functional description.",
    "The EC 2.7.1.52 annotation carries experimental evidence (ECO:0000269) from a 2019 cryo-EM and biochemical study (PubMed:30242642), not merely computational transfer.",
    "The UniProt entry was first integrated in Feb 2025; the benchmark author's source snapshot date is unknown, so the annotation may not have been available at the time the question was constructed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (EC 2.7.1.52 and EC 2.7.7.30), only 2.7.1.52 appears among the four choices, so no two options are simultaneously defensible. The singular phrasing 'the complete 4-digit EC number' is slightly imprecise for a bifunctional enzyme but does not create ambiguity among the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q58T34 (FKP_BACFG) is annotated with EC 2.7.1.52 (L-fucokinase) with experimental evidence (ECO:0000269|PubMed:30242642). The catalytic activity 'beta-L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H+' is confirmed. The protein is bifunctional (also EC 2.7.7.30), but 2.7.7.30 is not among the answer choices, so C is the only option matching a verified annotation for this sequence. Sequence match is confirmed (949 aa, SHA-256 identical).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a glycine-rich P-loop-like motif ('GSGGGTSWLLEECYNEYSDGATFGEWLE') suggestive of kinase/phosphotransferase activity, which could eliminate option B (EC 3.2.2.5, a glycosylase/hydrolase). However, the remaining three options (A: 2.7.2.4, C: 2.7.1.52, D: 2.7.8.43) are all phosphotransferases (class 2.7) differing only in acceptor group type (nitrogenous, alcohol, phosphatidyl). No general sequence feature reliably distinguishes L-fucokinase (2.7.1.52) from a phosphotransferase with nitrogenous acceptor (2.7.2.4) or a phosphatidyltransferase (2.7.8.43) without database-level identification of this specific protein.",
    "missing_item_specific_fact": "The specific identification of this 949-aa Bacteroides fragilis protein as L-fucokinase/GDP-fucose pyrophosphorylase (FKP), which requires recognizing the protein family or looking up the UniProt entry Q58T34. The substrate specificity for L-fucose (vs. other alcohol-group acceptors, nitrogenous acceptors, or phosphatidyl acceptors) cannot be inferred from general sequence motifs alone.",
    "reason": "While the P-loop motif weakly supports a phosphotransferase (eliminating B), distinguishing among the three EC 2.7 subclasses requires protein-specific annotation or memorization of this particular enzyme's identity. No general biological reasoning path from the raw sequence reliably selects 2.7.1.52 over 2.7.2.4 or 2.7.8.43."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (EC 2.7.1.52 and EC 2.7.7.30), only 2.7.1.52 appears among the four choices, so no two options are simultaneously defensible. The singular phrasing 'the complete 4-digit EC number' is slightly imprecise for a bifunctional enzyme but does not create ambiguity among the given options."
  },
  "important_caveats": [
    "The protein is bifunctional; the question asks for a single EC number. EC 2.7.7.30 (the other activity) is not offered as an option, so the expected answer is unambiguous among the choices but incomplete as a full functional description.",
    "The EC 2.7.1.52 annotation carries experimental evidence (ECO:0000269) from a 2019 cryo-EM and biochemical study (PubMed:30242642), not merely computational transfer.",
    "The UniProt entry was first integrated in Feb 2025; the benchmark author's source snapshot date is unknown, so the annotation may not have been available at the time the question was constructed."
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

**Accession:** `Q58T34` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 87. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
"Q58T34"
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"L-fucokinase/GDP-fucose pyrophosphorylase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"FKP"}]}],"includes":[{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"GDP-fucose pyrophosphorylase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"value":"2.7.7.30"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"30242642","source":"PubMed"}],"value":"Fucose-1-phosphate guanylyltransferase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"value":"2.7.1.52"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"L-fucokinase"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"30242642","source":"PubMed"}],"value":"L-fucokinase/L-fucose-1-P guanylyltransferase"}}}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"30242642","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13242"}}],"reaction":{"ecNumber":"2.7.1.52","evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"name":"beta-L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13241"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:42589"},{"database":"ChEBI","id":"CHEBI:57268"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)  
**Locator:** `lines 6-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:31:04.760170+00:00.  

```text
DE   RecName: Full=L-fucokinase/L-fucose-1-P guanylyltransferase {ECO:0000305|PubMed:30242642};
DE   AltName: Full=L-fucokinase/GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};
DE            Short=FKP {ECO:0000303|PubMed:30242642};
DE   Includes:
DE     RecName: Full=Fucose-1-phosphate guanylyltransferase {ECO:0000305|PubMed:30242642};
DE              EC=2.7.7.30 {ECO:0000269|PubMed:30242642};
DE     AltName: Full=GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};
DE   Includes:
DE     RecName: Full=L-fucokinase {ECO:0000303|PubMed:30242642};
DE              EC=2.7.1.52 {ECO:0000269|PubMed:30242642};
```

Source SHA-256: `3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)  
**Locator:** `lines 54-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:31:04.760170+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+);
CC         Xref=Rhea:RHEA:13241, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:57268, ChEBI:CHEBI:456216;
CC         EC=2.7.1.52; Evidence={ECO:0000269|PubMed:30242642};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13242;
CC         Evidence={ECO:0000305|PubMed:30242642};
```

Source SHA-256: `3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 163. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
