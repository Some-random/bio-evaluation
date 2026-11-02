# GO_molecular_function_0150

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — hormone activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFVYTTIMLLLLAEINHSQGCSGLCKINESPQTNIDYRICGDQITQKYTELCGNPAAGRRNRITGLDQRSIFESNLLAKRFLISRRQIVNNRRTDIVEECCAEGCKAEEVKEYCI

[Multiple Choices]
A. phospholipase A2 activity
B. hormone activity
C. misfolded protein binding
D. ubiquitin-like protein peptidase activity
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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry identifies the protein as an insulin-like peptide and assigns hormone activity by IEA:InterPro. This supports B as an annotation-level answer, but not as experimentally established native hormone activity: the entry describes the function as unknown and reports that a truncated synthetic analog did not bind the tested insulin receptors.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a signal peptide, followed by a cysteine-rich peptide precursor with features consistent with an insulin-like peptide. That secreted-peptide architecture favors hormone activity over the enzyme activities in A and D or the protein-binding activity in C.


**Missing item-specific fact**

> The sequence-based argument predicts an insulin-like hormone function; establishing the native peptide's actual receptor binding or regulatory activity would require item-specific experimental evidence.


**Reason**

> The sequence and choices provide a meaningful family-and-precursor-based rationale for B without needing to recognize the exact sequence or retrieve its database entry. The prediction remains uncertain because the native function is not experimentally established in the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the best-supported choice among those listed. The evidence leaves the peptide's native activity uncertain, but does not provide a comparably supported basis for A, C, or D.


### Important caveats

- The hormone-activity GO annotation is computational (IEA:InterPro), not experimental evidence.
- The reported receptor-binding and channel assays concern a truncated synthetic analog, not demonstrated activity of the intact native peptide.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, followed by a cysteine-rich peptide precursor with features consistent with an insulin-like peptide. That secreted-peptide architecture favors hormone activity over the enzyme activities in A and D or the protein-binding activity in C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence-based argument predicts an insulin-like hormone function; establishing the native peptide's actual receptor binding or regulatory activity would require item-specific experimental evidence.",
    "reason": "The sequence and choices provide a meaningful family-and-precursor-based rationale for B without needing to recognize the exact sequence or retrieve its database entry. The prediction remains uncertain because the native function is not experimentally established in the supplied evidence."
  },
  "case_id": "GO_molecular_function_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry identifies the protein as an insulin-like peptide and assigns hormone activity by IEA:InterPro. This supports B as an annotation-level answer, but not as experimentally established native hormone activity: the entry describes the function as unknown and reports that a truncated synthetic analog did not bind the tested insulin receptors."
  },
  "important_caveats": [
    "The hormone-activity GO annotation is computational (IEA:InterPro), not experimental evidence.",
    "The reported receptor-binding and channel assays concern a truncated synthetic analog, not demonstrated activity of the intact native peptide."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the best-supported choice among those listed. The evidence leaves the peptide's native activity uncertain, but does not provide a comparably supported basis for A, C, or D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry identifies the protein as an insulin-like peptide and assigns hormone activity by IEA:InterPro. This supports B as an annotation-level answer, but not as experimentally established native hormone activity: the entry describes the function as unknown and reports that a truncated synthetic analog did not bind the tested insulin receptors.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, followed by a cysteine-rich peptide precursor with features consistent with an insulin-like peptide. That secreted-peptide architecture favors hormone activity over the enzyme activities in A and D or the protein-binding activity in C.",
    "missing_item_specific_fact": "The sequence-based argument predicts an insulin-like hormone function; establishing the native peptide's actual receptor binding or regulatory activity would require item-specific experimental evidence.",
    "reason": "The sequence and choices provide a meaningful family-and-precursor-based rationale for B without needing to recognize the exact sequence or retrieve its database entry. The prediction remains uncertain because the native function is not experimentally established in the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the best-supported choice among those listed. The evidence leaves the peptide's native activity uncertain, but does not provide a comparably supported basis for A, C, or D."
  },
  "important_caveats": [
    "The hormone-activity GO annotation is computational (IEA:InterPro), not experimental evidence.",
    "The reported receptor-binding and channel assays concern a truncated synthetic analog, not demonstrated activity of the intact native peptide."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt P0DY19 (sequence matched, 115 aa) is annotated with GO:0005179 'hormone activity' via IEA:InterPro (evidence C6/H4). The protein is named 'Insulin-like peptide IlO1_i1' with A and B chains, consistent with the insulin-family of peptide hormones. The GO definition (GO2) includes regulatory compounds in lower animals. However, the annotation is computational (IEA:InterPro), and the FUNCTION comment (C5/H3) explicitly states 'Heterodimer with unknown function (Probable)' and that the truncated analog does not bind insulin/IGF-1 receptors. The key is database-supported but rests on family-membership inference rather than direct experimental confirmation of hormonal activity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 115-aa sequence contains a hydrophobic N-terminal signal peptide (MFVYTTIMLLLLAE), multiple cysteines in patterns compatible with insulin-like disulfide bonding, and a small two-chain architecture reminiscent of insulin/IGF peptides. Among the four choices: (A) PLA2 requires a specific catalytic His/Asp dyad and Ca²⁺-binding loop absent here; (C) misfolded protein binding is a property of large chaperones (HSP70/HSP90, >400 aa); (D) ubiquitin-like peptidase activity requires a Cys-His-Asp catalytic triad in a much larger protease fold. All three distractors describe functions of substantially larger enzymes with specific catalytic motifs not present in this small secreted cysteine-rich peptide. The remaining option, hormone activity, is consistent with a small secreted peptide bearing disulfide-linked chains—the hallmark of peptide hormones such as insulin.


**Missing item-specific fact**

> None strictly required to eliminate the three distractors, though confirming the specific 'insulin-like' identity (vs. the alternative UniProt annotations of 'toxin activity' and 'ion channel regulator activity') relies on recognizing the insulin-like fold family, which is a general-knowledge pattern rather than an obscure item-specific fact.


**Reason**

> General structural knowledge (signal peptide, cysteine-rich small secreted peptide, absence of catalytic residues for hydrolases/proteases, absence of chaperone domains) provides a concrete elimination pathway that distinguishes B from A, C, and D without needing to memorize the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four provided choices, only B is consistent with the sequence architecture. The protein is also annotated with 'toxin activity' (GO:0090729) and 'ion channel regulator activity' (GO:0099106) in UniProt, but neither appears as an option, so no ambiguity arises within the given choice set.


### Important caveats

- The 'hormone activity' annotation is IEA:InterPro (electronic inference from domain family), not experimentally validated. The UniProt FUNCTION comment explicitly states the function is 'unknown (Probable)' and that the truncated analog failed to bind insulin or IGF-1 receptors.
- The protein is also annotated with 'toxin activity' and 'ion channel regulator activity' in UniProt, reflecting the dual nature of many sea anemone peptides. These alternatives are not among the choices.
- The sequence is 115 aa (precursor); the mature chains (27-58 and 94-115) are much smaller, which further supports a peptide-hormone interpretation over enzyme-like functions.
- Evidence is reviewer-only; the evaluated model sees only the raw sequence and four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 115-aa sequence contains a hydrophobic N-terminal signal peptide (MFVYTTIMLLLLAE), multiple cysteines in patterns compatible with insulin-like disulfide bonding, and a small two-chain architecture reminiscent of insulin/IGF peptides. Among the four choices: (A) PLA2 requires a specific catalytic His/Asp dyad and Ca²⁺-binding loop absent here; (C) misfolded protein binding is a property of large chaperones (HSP70/HSP90, >400 aa); (D) ubiquitin-like peptidase activity requires a Cys-His-Asp catalytic triad in a much larger protease fold. All three distractors describe functions of substantially larger enzymes with specific catalytic motifs not present in this small secreted cysteine-rich peptide. The remaining option, hormone activity, is consistent with a small secreted peptide bearing disulfide-linked chains—the hallmark of peptide hormones such as insulin.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required to eliminate the three distractors, though confirming the specific 'insulin-like' identity (vs. the alternative UniProt annotations of 'toxin activity' and 'ion channel regulator activity') relies on recognizing the insulin-like fold family, which is a general-knowledge pattern rather than an obscure item-specific fact.",
    "reason": "General structural knowledge (signal peptide, cysteine-rich small secreted peptide, absence of catalytic residues for hydrolases/proteases, absence of chaperone domains) provides a concrete elimination pathway that distinguishes B from A, C, and D without needing to memorize the specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt P0DY19 (sequence matched, 115 aa) is annotated with GO:0005179 'hormone activity' via IEA:InterPro (evidence C6/H4). The protein is named 'Insulin-like peptide IlO1_i1' with A and B chains, consistent with the insulin-family of peptide hormones. The GO definition (GO2) includes regulatory compounds in lower animals. However, the annotation is computational (IEA:InterPro), and the FUNCTION comment (C5/H3) explicitly states 'Heterodimer with unknown function (Probable)' and that the truncated analog does not bind insulin/IGF-1 receptors. The key is database-supported but rests on family-membership inference rather than direct experimental confirmation of hormonal activity."
  },
  "important_caveats": [
    "The 'hormone activity' annotation is IEA:InterPro (electronic inference from domain family), not experimentally validated. The UniProt FUNCTION comment explicitly states the function is 'unknown (Probable)' and that the truncated analog failed to bind insulin or IGF-1 receptors.",
    "The protein is also annotated with 'toxin activity' and 'ion channel regulator activity' in UniProt, reflecting the dual nature of many sea anemone peptides. These alternatives are not among the choices.",
    "The sequence is 115 aa (precursor); the mature chains (27-58 and 94-115) are much smaller, which further supports a peptide-hormone interpretation over enzyme-like functions.",
    "Evidence is reviewer-only; the evaluated model sees only the raw sequence and four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided choices, only B is consistent with the sequence architecture. The protein is also annotated with 'toxin activity' (GO:0090729) and 'ion channel regulator activity' (GO:0099106) in UniProt, but neither appears as an option, so no ambiguity arises within the given choice set."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt P0DY19 (sequence matched, 115 aa) is annotated with GO:0005179 'hormone activity' via IEA:InterPro (evidence C6/H4). The protein is named 'Insulin-like peptide IlO1_i1' with A and B chains, consistent with the insulin-family of peptide hormones. The GO definition (GO2) includes regulatory compounds in lower animals. However, the annotation is computational (IEA:InterPro), and the FUNCTION comment (C5/H3) explicitly states 'Heterodimer with unknown function (Probable)' and that the truncated analog does not bind insulin/IGF-1 receptors. The key is database-supported but rests on family-membership inference rather than direct experimental confirmation of hormonal activity.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 115-aa sequence contains a hydrophobic N-terminal signal peptide (MFVYTTIMLLLLAE), multiple cysteines in patterns compatible with insulin-like disulfide bonding, and a small two-chain architecture reminiscent of insulin/IGF peptides. Among the four choices: (A) PLA2 requires a specific catalytic His/Asp dyad and Ca²⁺-binding loop absent here; (C) misfolded protein binding is a property of large chaperones (HSP70/HSP90, >400 aa); (D) ubiquitin-like peptidase activity requires a Cys-His-Asp catalytic triad in a much larger protease fold. All three distractors describe functions of substantially larger enzymes with specific catalytic motifs not present in this small secreted cysteine-rich peptide. The remaining option, hormone activity, is consistent with a small secreted peptide bearing disulfide-linked chains—the hallmark of peptide hormones such as insulin.",
    "missing_item_specific_fact": "None strictly required to eliminate the three distractors, though confirming the specific 'insulin-like' identity (vs. the alternative UniProt annotations of 'toxin activity' and 'ion channel regulator activity') relies on recognizing the insulin-like fold family, which is a general-knowledge pattern rather than an obscure item-specific fact.",
    "reason": "General structural knowledge (signal peptide, cysteine-rich small secreted peptide, absence of catalytic residues for hydrolases/proteases, absence of chaperone domains) provides a concrete elimination pathway that distinguishes B from A, C, and D without needing to memorize the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided choices, only B is consistent with the sequence architecture. The protein is also annotated with 'toxin activity' (GO:0090729) and 'ion channel regulator activity' (GO:0099106) in UniProt, but neither appears as an option, so no ambiguity arises within the given choice set."
  },
  "important_caveats": [
    "The 'hormone activity' annotation is IEA:InterPro (electronic inference from domain family), not experimentally validated. The UniProt FUNCTION comment explicitly states the function is 'unknown (Probable)' and that the truncated analog failed to bind insulin or IGF-1 receptors.",
    "The protein is also annotated with 'toxin activity' and 'ion channel regulator activity' in UniProt, reflecting the dual nature of many sea anemone peptides. These alternatives are not among the choices.",
    "The sequence is 115 aa (precursor); the mature chains (27-58 and 94-115) are much smaller, which further supports a peptide-hormone interpretation over enzyme-like functions.",
    "Evidence is reviewer-only; the evaluated model sees only the raw sequence and four choices."
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

**Accession:** `P0DY19` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY19.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:04.985926+00:00.  

```json
"P0DY19"
```

Source SHA-256: `b171bc146a2b2fc84da78c613bc174bb9b5938d7fc08431b99b3eab1b9963508`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY19.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:04.985926+00:00.  

```json
{"contains":[{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34944429","source":"PubMed"}],"value":"ILP IlO1_i1 B chain"}}},{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34944429","source":"PubMed"}],"value":"ILP IlO1_i1 A chain"}}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34944429","source":"PubMed"}],"value":"Insulin-like peptide IlO1_i1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34944429","source":"PubMed"}],"value":"ILP IlO1_i1"}]}}
```

Source SHA-256: `b171bc146a2b2fc84da78c613bc174bb9b5938d7fc08431b99b3eab1b9963508`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY19.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:04.985926+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34944429","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Heterodimer with unknown function (Probable). Surprisingly, the truncated synthetic analog (dimer of 27-58 and 94-115) does not bind to long insulin receptor (HIR-B) and insulin-like growth factor 1 receptor. This truncated synthetic analog shows very weak inhibitory activity on different voltage-gated channels (PubMed:34944429)"}]}
```

Source SHA-256: `b171bc146a2b2fc84da78c613bc174bb9b5938d7fc08431b99b3eab1b9963508`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY19.json)  
**Locator:** `/uniProtKBCrossReferences/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:04.985926+00:00.  

```json
{"database":"GO","id":"GO:0005179","properties":[{"key":"GoTerm","value":"F:hormone activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `b171bc146a2b2fc84da78c613bc174bb9b5938d7fc08431b99b3eab1b9963508`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY19.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:04.985926+00:00.  

```json
{"citation":{"authors":["Mitchell M.L.","Hossain M.A.","Lin F.","Pinheiro-Junior E.L.","Peigneur S.","Wai D.C.C.","Delaine C.","Blyth A.J.","Forbes B.E.","Tytgat J.","Wade J.D.","Norton R.S."],"citationCrossReferences":[{"database":"PubMed","id":"34944429"},{"database":"DOI","id":"10.3390/biom11121785"}],"citationType":"journal article","firstPage":"0","id":"34944429","journal":"Biomolecules","lastPage":"0","publicationDate":"2021","title":"Identification, synthesis, conformation and activity of an insulin-like peptide from a sea anemone.","volume":"11"},"referenceComments":[{"type":"TISSUE","value":"Tentacle"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION OF TRUNCATED SYNTHETIC PEPTIDE","TISSUE SPECIFICITY","SYNTHESIS OF 27-58 AND 94-115","CIRCULAR DICHROISM ANALYSIS OF TRUNCATED SYNTHETIC PEPTIDE"]}
```

Source SHA-256: `b171bc146a2b2fc84da78c613bc174bb9b5938d7fc08431b99b3eab1b9963508`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY19?format=txt&versions=3)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:06.647073+00:00.  

```text
ID   INS_OULSP               Reviewed;         115 AA.
AC   P0DY19; A0A8K1XL00;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=Insulin-like peptide IlO1_i1 {ECO:0000303|PubMed:34944429};
DE            Short=ILP IlO1_i1 {ECO:0000303|PubMed:34944429};
DE   Contains:
DE     RecName: Full=ILP IlO1_i1 B chain {ECO:0000303|PubMed:34944429};
DE   Contains:
DE     RecName: Full=ILP IlO1_i1 A chain {ECO:0000303|PubMed:34944429};
DE   Flags: Precursor;
OS   Oulactis sp. (Sea anemone).
OC   Eukaryota; Metazoa; Cnidaria; Anthozoa; Hexacorallia; Actiniaria;
OC   Actiniidae; Oulactis.
OX   NCBI_TaxID=2093647;
```

Source SHA-256: `bf207732ca74b1af30190c96bdb36a4c1d80a278baf4561d922e531f0d51cb38`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY19?format=txt&versions=3)  
**Locator:** `lines 29-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:06.647073+00:00.  

```text
CC   -!- FUNCTION: Heterodimer with unknown function (Probable). Surprisingly,
CC       the truncated synthetic analog (dimer of 27-58 and 94-115) does not
CC       bind to long insulin receptor (HIR-B) and insulin-like growth factor 1
CC       receptor. This truncated synthetic analog shows very weak inhibitory
CC       activity on different voltage-gated channels (PubMed:34944429).
CC       {ECO:0000269|PubMed:34944429, ECO:0000305}.
```

Source SHA-256: `bf207732ca74b1af30190c96bdb36a4c1d80a278baf4561d922e531f0d51cb38`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY19?format=txt&versions=3)  
**Locator:** `lines 58-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:06.647073+00:00.  

```text
DR   GO; GO:0005179; F:hormone activity; IEA:InterPro.
```

Source SHA-256: `bf207732ca74b1af30190c96bdb36a4c1d80a278baf4561d922e531f0d51cb38`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 54512-54524`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005179
name: hormone activity
namespace: molecular_function
def: "The action characteristic of a hormone, any substance formed in very small amounts in one specialized organ or group of cells and carried (sometimes in the bloodstream) to another organ or group of cells in the same organism, upon which it has a specific regulatory action. The term was originally applied to agents with a stimulatory physiological action in vertebrate animals (as opposed to a chalone, which has a depressant action). Usage is now extended to regulatory compounds in lower animals and plants, and to synthetic substances having comparable effects; all bind receptors and trigger some biological process." [GOC:dph, GOC:mah, ISBN:0198506732]
comment: Also consider annotating to 'receptor agonist activity ; GO:0048018'.
subset: goslim_chembl
synonym: "cAMP generating peptide activity" NARROW []
synonym: "glycopeptide hormone" NARROW []
synonym: "lipopeptide hormone" NARROW []
synonym: "peptide hormone" NARROW []
is_a: GO:0048018 ! receptor ligand activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 150. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
