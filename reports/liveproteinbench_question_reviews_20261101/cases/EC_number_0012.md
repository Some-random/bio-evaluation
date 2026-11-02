# EC_number_0012

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.14.14.154

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSILWIVAYALLAFAASIALNLVYQFLYRTFNKSRPPLVFHWVPFIGSTIHYGMDPYNFFFSCREKYGDIFTFILLGRPTTVYLGTQGNEFILNGKLKDVNAEEVYSPLTTPVFGSDVVYDCPNSKLIEQKKFIKFGLSQAALEAHVPLIEKEVIDYLAQSPNFNGTAGTVDIASAMAEITIFTAGSTLQGEEVRSKLTTEFAVLYHDLDKGFTPINFMLPWAPLPHNKKRDAAHARMRAIYIDIINKRRKAGNAATGKPDMIENLMQCTYKNGQPLPDKEIAHIMITLLMAGQHSSSSIGSWIMLRLASQPAIVEELYQEQLANLERTANGSLPPLQFKDIENLPLHQNVIRETLRLHGSIHSLLRKVKNPLPVPGTPYIIPTSHVLLSAPGVTALSDEYFPNAMAWDPHRWETQAPEESKEDIVDYGYGAMSKGTSSPYLPFGAGRHRCIGEKFAYLNLTVIVATLVRHLRFHNLDGKKGVPGTDYTSLFSGPLKPTRVGWERRAAKSA

[Multiple Choices]
A. 1.14.14.126
B. 3.2.1.20
C. 1.1.1.336
D. 1.14.14.154
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

> The exact input sequence matches UniProt entry P0DXU9, which annotates it as sterol 14-alpha demethylase resB with EC 1.14.14.154. The annotation and catalytic-activity assignment are supported by transfer from homologous UniProt entries (ECO:0000250), so this supports the key as a database annotation but is not, in the supplied excerpts, proof of a direct experimental assay of this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a membrane-associated enzyme, and the sequence is compatible with a cytochrome P450 monooxygenase. That broad inference does not establish the specific steroid substrate or the precise EC assignment needed to choose between the P450-related options.


**Missing item-specific fact**

> The protein-specific functional assignment as sterol 14-alpha demethylase resB, or equivalent homolog/annotation knowledge linking this sequence to EC 1.14.14.154.


**Reason**

> The sequence and choices give some broad enzyme-family clues, but distinguishing the exact EC number requires an item-specific functional annotation or a reliable sequence-homology inference not provided in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone does not make the exact EC assignment transparent, but the supplied reviewer evidence assigns this matched sequence to EC 1.14.14.154; no alternative listed option is supported by that evidence.


### Important caveats

- The UniProt EC and catalytic-activity evidence cited here is transferred from homologous entries rather than independently demonstrated in the supplied excerpts.
- The evidence is reviewer-only and was not available as input to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a membrane-associated enzyme, and the sequence is compatible with a cytochrome P450 monooxygenase. That broad inference does not establish the specific steroid substrate or the precise EC assignment needed to choose between the P450-related options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment as sterol 14-alpha demethylase resB, or equivalent homolog/annotation knowledge linking this sequence to EC 1.14.14.154.",
    "reason": "The sequence and choices give some broad enzyme-family clues, but distinguishing the exact EC number requires an item-specific functional annotation or a reliable sequence-homology inference not provided in the question."
  },
  "case_id": "EC_number_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact input sequence matches UniProt entry P0DXU9, which annotates it as sterol 14-alpha demethylase resB with EC 1.14.14.154. The annotation and catalytic-activity assignment are supported by transfer from homologous UniProt entries (ECO:0000250), so this supports the key as a database annotation but is not, in the supplied excerpts, proof of a direct experimental assay of this protein."
  },
  "important_caveats": [
    "The UniProt EC and catalytic-activity evidence cited here is transferred from homologous entries rather than independently demonstrated in the supplied excerpts.",
    "The evidence is reviewer-only and was not available as input to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not make the exact EC assignment transparent, but the supplied reviewer evidence assigns this matched sequence to EC 1.14.14.154; no alternative listed option is supported by that evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact input sequence matches UniProt entry P0DXU9, which annotates it as sterol 14-alpha demethylase resB with EC 1.14.14.154. The annotation and catalytic-activity assignment are supported by transfer from homologous UniProt entries (ECO:0000250), so this supports the key as a database annotation but is not, in the supplied excerpts, proof of a direct experimental assay of this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a membrane-associated enzyme, and the sequence is compatible with a cytochrome P450 monooxygenase. That broad inference does not establish the specific steroid substrate or the precise EC assignment needed to choose between the P450-related options.",
    "missing_item_specific_fact": "The protein-specific functional assignment as sterol 14-alpha demethylase resB, or equivalent homolog/annotation knowledge linking this sequence to EC 1.14.14.154.",
    "reason": "The sequence and choices give some broad enzyme-family clues, but distinguishing the exact EC number requires an item-specific functional annotation or a reliable sequence-homology inference not provided in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not make the exact EC assignment transparent, but the supplied reviewer evidence assigns this matched sequence to EC 1.14.14.154; no alternative listed option is supported by that evidence."
  },
  "important_caveats": [
    "The UniProt EC and catalytic-activity evidence cited here is transferred from homologous entries rather than independently demonstrated in the supplied excerpts.",
    "The evidence is reviewer-only and was not available as input to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXU9 (RESB_ASPSL, 511 aa, Aspergillus sclerotiorum) explicitly assigns EC 1.14.14.154 (Sterol 14-alpha demethylase resB). The sequence matches the benchmark input exactly. However, the EC annotation carries evidence code ECO:0000250 (similarity), meaning it was transferred by computational inference from related entries (A0A0L1JEW4, Q4WNT5, P10614) rather than from direct experimental characterization of this specific protein. The catalytic activity reactions (14α-methyl steroid → Δ14 steroid + formate, using NADPH-hemoprotein reductase and O2) are consistent with EC 1.14.14.154. The database annotation supports the key, but it is a similarity-based assignment, not independent experimental proof.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif (e.g., 'GAGRHRCIGEKFAYLNLTVIVATLVRHLRFHNLDGKKGVPGTDYTSLFSGPLKPTRVGWERRAAKSA' with the FxxGxRxCxG signature), which reliably identifies the protein as a P450 monooxygenase (EC 1.14.14.x). This eliminates B (3.2.1.20, α-glucosidase, a hydrolase) and C (1.1.1.336, a dehydrogenase/reductase) through general enzyme-class reasoning. However, the critical distinction between A (1.14.14.126) and D (1.14.14.154) hinges on the 4th EC digit, which encodes the specific substrate/reaction. Both are P450 monooxygenases; no general sequence feature visible in the input distinguishes which specific 4-digit EC assignment applies.


**Missing item-specific fact**

> The model must know the precise EC 4th-digit assignment for this particular P450: that EC 1.14.14.154 corresponds to fungal sterol 14α-demethylase while EC 1.14.14.126 corresponds to a different specific P450 reaction. This is a database annotation fact, not derivable from sequence motifs alone.


**Reason**

> General biological knowledge (P450 heme-binding motif recognition) narrows four choices to two (A and D), but the final A-vs-D discrimination requires memorizing or looking up which specific EC 4th-digit number corresponds to the sterol 14α-demethylase reaction versus the alternative P450 reaction. No sequence-derived argument from the supplied input can meaningfully separate 1.14.14.126 from 1.14.14.154.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (1.14.14.126) and D (1.14.14.154) are cytochrome P450 monooxygenases (EC class 1.14.14.x). Without external knowledge of what specific reaction each 4th digit encodes, the sequence alone cannot distinguish them. B and C are clearly eliminable as wrong enzyme classes, but A vs D is an annotation-level distinction.


### Important caveats

- The UniProt EC assignment (1.14.14.154) carries evidence code ECO:0000250 (similarity), indicating it was inferred by transfer from homologous entries rather than experimentally determined for P0DXU9 itself.
- The UniProt entry was first released 2025-02-05 (entry version 1); the author's source snapshot date is unknown. The sequence has not changed since release.
- The reviewer-only UniProt accession and metadata were absent from the evaluated model input; the model sees only the raw sequence and four EC-number choices.
- The protein is annotated as part of the restricticin biosynthesis cluster (resB) and also described as an ergosterol biosynthesis protein, consistent with a CYP51/sterol 14α-demethylase role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (e.g., 'GAGRHRCIGEKFAYLNLTVIVATLVRHLRFHNLDGKKGVPGTDYTSLFSGPLKPTRVGWERRAAKSA' with the FxxGxRxCxG signature), which reliably identifies the protein as a P450 monooxygenase (EC 1.14.14.x). This eliminates B (3.2.1.20, α-glucosidase, a hydrolase) and C (1.1.1.336, a dehydrogenase/reductase) through general enzyme-class reasoning. However, the critical distinction between A (1.14.14.126) and D (1.14.14.154) hinges on the 4th EC digit, which encodes the specific substrate/reaction. Both are P450 monooxygenases; no general sequence feature visible in the input distinguishes which specific 4-digit EC assignment applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The model must know the precise EC 4th-digit assignment for this particular P450: that EC 1.14.14.154 corresponds to fungal sterol 14α-demethylase while EC 1.14.14.126 corresponds to a different specific P450 reaction. This is a database annotation fact, not derivable from sequence motifs alone.",
    "reason": "General biological knowledge (P450 heme-binding motif recognition) narrows four choices to two (A and D), but the final A-vs-D discrimination requires memorizing or looking up which specific EC 4th-digit number corresponds to the sterol 14α-demethylase reaction versus the alternative P450 reaction. No sequence-derived argument from the supplied input can meaningfully separate 1.14.14.126 from 1.14.14.154."
  },
  "case_id": "EC_number_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H1",
      "H2",
      "H4",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXU9 (RESB_ASPSL, 511 aa, Aspergillus sclerotiorum) explicitly assigns EC 1.14.14.154 (Sterol 14-alpha demethylase resB). The sequence matches the benchmark input exactly. However, the EC annotation carries evidence code ECO:0000250 (similarity), meaning it was transferred by computational inference from related entries (A0A0L1JEW4, Q4WNT5, P10614) rather than from direct experimental characterization of this specific protein. The catalytic activity reactions (14α-methyl steroid → Δ14 steroid + formate, using NADPH-hemoprotein reductase and O2) are consistent with EC 1.14.14.154. The database annotation supports the key, but it is a similarity-based assignment, not independent experimental proof."
  },
  "important_caveats": [
    "The UniProt EC assignment (1.14.14.154) carries evidence code ECO:0000250 (similarity), indicating it was inferred by transfer from homologous entries rather than experimentally determined for P0DXU9 itself.",
    "The UniProt entry was first released 2025-02-05 (entry version 1); the author's source snapshot date is unknown. The sequence has not changed since release.",
    "The reviewer-only UniProt accession and metadata were absent from the evaluated model input; the model sees only the raw sequence and four EC-number choices.",
    "The protein is annotated as part of the restricticin biosynthesis cluster (resB) and also described as an ergosterol biosynthesis protein, consistent with a CYP51/sterol 14α-demethylase role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (1.14.14.126) and D (1.14.14.154) are cytochrome P450 monooxygenases (EC class 1.14.14.x). Without external knowledge of what specific reaction each 4th digit encodes, the sequence alone cannot distinguish them. B and C are clearly eliminable as wrong enzyme classes, but A vs D is an annotation-level distinction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXU9 (RESB_ASPSL, 511 aa, Aspergillus sclerotiorum) explicitly assigns EC 1.14.14.154 (Sterol 14-alpha demethylase resB). The sequence matches the benchmark input exactly. However, the EC annotation carries evidence code ECO:0000250 (similarity), meaning it was transferred by computational inference from related entries (A0A0L1JEW4, Q4WNT5, P10614) rather than from direct experimental characterization of this specific protein. The catalytic activity reactions (14α-methyl steroid → Δ14 steroid + formate, using NADPH-hemoprotein reductase and O2) are consistent with EC 1.14.14.154. The database annotation supports the key, but it is a similarity-based assignment, not independent experimental proof.",
    "evidence_ids": ["C4", "C5", "C9", "H1", "H2", "H4", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (e.g., 'GAGRHRCIGEKFAYLNLTVIVATLVRHLRFHNLDGKKGVPGTDYTSLFSGPLKPTRVGWERRAAKSA' with the FxxGxRxCxG signature), which reliably identifies the protein as a P450 monooxygenase (EC 1.14.14.x). This eliminates B (3.2.1.20, α-glucosidase, a hydrolase) and C (1.1.1.336, a dehydrogenase/reductase) through general enzyme-class reasoning. However, the critical distinction between A (1.14.14.126) and D (1.14.14.154) hinges on the 4th EC digit, which encodes the specific substrate/reaction. Both are P450 monooxygenases; no general sequence feature visible in the input distinguishes which specific 4-digit EC assignment applies.",
    "missing_item_specific_fact": "The model must know the precise EC 4th-digit assignment for this particular P450: that EC 1.14.14.154 corresponds to fungal sterol 14α-demethylase while EC 1.14.14.126 corresponds to a different specific P450 reaction. This is a database annotation fact, not derivable from sequence motifs alone.",
    "reason": "General biological knowledge (P450 heme-binding motif recognition) narrows four choices to two (A and D), but the final A-vs-D discrimination requires memorizing or looking up which specific EC 4th-digit number corresponds to the sterol 14α-demethylase reaction versus the alternative P450 reaction. No sequence-derived argument from the supplied input can meaningfully separate 1.14.14.126 from 1.14.14.154."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (1.14.14.126) and D (1.14.14.154) are cytochrome P450 monooxygenases (EC class 1.14.14.x). Without external knowledge of what specific reaction each 4th digit encodes, the sequence alone cannot distinguish them. B and C are clearly eliminable as wrong enzyme classes, but A vs D is an annotation-level distinction."
  },
  "important_caveats": [
    "The UniProt EC assignment (1.14.14.154) carries evidence code ECO:0000250 (similarity), indicating it was inferred by transfer from homologous entries rather than experimentally determined for P0DXU9 itself.",
    "The UniProt entry was first released 2025-02-05 (entry version 1); the author's source snapshot date is unknown. The sequence has not changed since release.",
    "The reviewer-only UniProt accession and metadata were absent from the evaluated model input; the model sees only the raw sequence and four EC-number choices.",
    "The protein is annotated as part of the restricticin biosynthesis cluster (resB) and also described as an ergosterol biosynthesis protein, consistent with a CYP51/sterol 14α-demethylase role."
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

**Accession:** `P0DXU9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.593366+00:00.  

```json
"P0DXU9"
```

Source SHA-256: `40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.593366+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase resB"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Ergosterol biosynthesis protein resB"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein B"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0L1JEW4","source":"UniProtKB"}],"value":"1.14.14.154"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Sterol 14-alpha demethylase resB"}}}
```

Source SHA-256: `40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.593366+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:54029"}}],"reaction":{"ecNumber":"1.14.14.154","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"name":"a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:54028"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:15740"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:138029"},{"database":"ChEBI","id":"CHEBI:138031"}]}}
```

Source SHA-256: `40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.593366+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:25287"}}],"reaction":{"ecNumber":"1.14.14.154","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"name":"lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:25286"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:15740"},{"database":"ChEBI","id":"CHEBI:16521"},{"database":"ChEBI","id":"CHEBI:17813"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"}]}}
```

Source SHA-256: `40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:47.314530+00:00.  

```text
ID   RESB_ASPSL              Reviewed;         511 AA.
AC   P0DXU9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Sterol 14-alpha demethylase resB {ECO:0000303|PubMed:39105744};
DE            EC=1.14.14.154 {ECO:0000250|UniProtKB:A0A0L1JEW4};
DE   AltName: Full=Cytochrome P450 monooxygenase resB {ECO:0000303|PubMed:39105744};
DE   AltName: Full=Ergosterol biosynthesis protein resB {ECO:0000303|PubMed:39105744};
DE   AltName: Full=Restricticin biosynthesis cluster protein B {ECO:0000303|PubMed:39105744};
GN   Name=resB {ECO:0000303|PubMed:39105744};
OS   Aspergillus sclerotiorum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=138282;
```

Source SHA-256: `2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:47.314530+00:00.  

```text
DE   RecName: Full=Sterol 14-alpha demethylase resB {ECO:0000303|PubMed:39105744};
DE            EC=1.14.14.154 {ECO:0000250|UniProtKB:A0A0L1JEW4};
DE   AltName: Full=Cytochrome P450 monooxygenase resB {ECO:0000303|PubMed:39105744};
DE   AltName: Full=Ergosterol biosynthesis protein resB {ECO:0000303|PubMed:39105744};
DE   AltName: Full=Restricticin biosynthesis cluster protein B {ECO:0000303|PubMed:39105744};
```

Source SHA-256: `2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)  
**Locator:** `lines 36-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:47.314530+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein
CC         reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized
CC         [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);
CC         Xref=Rhea:RHEA:54028, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:15740, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,
CC         ChEBI:CHEBI:138029, ChEBI:CHEBI:138031; EC=1.14.14.154;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:54029;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
```

Source SHA-256: `2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)  
**Locator:** `lines 77-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:47.314530+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 =
CC         4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3
CC         oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);
CC         Xref=Rhea:RHEA:25286, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:15740, ChEBI:CHEBI:16521, ChEBI:CHEBI:17813,
CC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210; EC=1.14.14.154;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:25287;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
```

Source SHA-256: `2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
