# EC_number_0127: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0127.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **D** — 2.7.11.1

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNVALVFLLFQVQDGTGITLGPSKLDSKPTSLDSQQHVADKRWLATVGHYKHLAGATESTRDVSLLEERAQHRVNAQETNQRRTIFQRLLNLLRRRERDGEVSGSAADSSSRPRLSVRQRLAQLWRRAKSLFKRGIRRYFPQGRNRQRSLRAQRRRSELVFEKADSGCVIGKRILAHMQEQIGQPQALENSERLDRILTVAAWPPDVPKRFVSVTTGETRTLVRGAPLGSGGFATVYEATDVETNEELAVKVFMSEKEPTDETMLDLQRESSCYRNFSLAKTAKDAQESCRFMVPSDVVMLEGQPASTEVVIGLTTRWVPNYFLLMMRAEADMSKVISWVFGDASVNKSEFGLVVRMYLSSQAIKLVANVQAQGIVHTDIKPANFLLLKDGRLFLGDFGTYRINNSVGRAIGTPGYEPPERPFQATGITYTFPTDAWQLGITLYCIWCKERPTPADGIWDYLHFADCPSTPELVQDLIRSLLNRDPQKRMLPLQALETAAFKEMDSVVKGAAQNFEQQEHLHTE

[Multiple Choices]
A. 2.7.13.3
B. 2.8.1.7
C. 2.7.11.24
D. 2.7.11.1
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the 554-aa UniProt Q2PAY2 sequence. Its annotated EC number is 2.7.11.1, with catalytic-activity annotations for serine and threonine phosphorylation citing experimental evidence (alongside a curator-evidence citation).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a protein-kinase domain, which supports kinase activity and makes the kinase choices plausible. That alone does not establish this protein's precise substrate specificity or distinguish the broad serine/threonine kinase EC number from a more specific kinase subclass.


**Missing item-specific fact**

> The protein-specific functional assignment that ROP18 phosphorylates protein serine and threonine residues, needed to establish EC 2.7.11.1 rather than merely infer kinase activity.


**Reason**

> The exact EC assignment is supported by reviewer-only database and cited experimental evidence, but that annotation and the relevant functional measurements are absent from the question. Recognizing the kinase fold does not supply the item-specific specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports D for this sequence. The other kinase choices describe different substrate or enzyme subclasses; the sequence alone may not decisively rule them out, but the supplied reviewer-only evidence identifies the protein's EC number as 2.7.11.1.


### Important caveats

- The UniProt entry is a database annotation supported by cited publications; the primary papers were not independently reviewed here.
- The exact sequence match is established, but the author's original database snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a protein-kinase domain, which supports kinase activity and makes the kinase choices plausible. That alone does not establish this protein's precise substrate specificity or distinguish the broad serine/threonine kinase EC number from a more specific kinase subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment that ROP18 phosphorylates protein serine and threonine residues, needed to establish EC 2.7.11.1 rather than merely infer kinase activity.",
    "reason": "The exact EC assignment is supported by reviewer-only database and cited experimental evidence, but that annotation and the relevant functional measurements are absent from the question. Recognizing the kinase fold does not supply the item-specific specificity."
  },
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 554-aa UniProt Q2PAY2 sequence. Its annotated EC number is 2.7.11.1, with catalytic-activity annotations for serine and threonine phosphorylation citing experimental evidence (alongside a curator-evidence citation)."
  },
  "important_caveats": [
    "The UniProt entry is a database annotation supported by cited publications; the primary papers were not independently reviewed here.",
    "The exact sequence match is established, but the author's original database snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D for this sequence. The other kinase choices describe different substrate or enzyme subclasses; the sequence alone may not decisively rule them out, but the supplied reviewer-only evidence identifies the protein's EC number as 2.7.11.1."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 554-aa UniProt Q2PAY2 sequence. Its annotated EC number is 2.7.11.1, with catalytic-activity annotations for serine and threonine phosphorylation citing experimental evidence (alongside a curator-evidence citation).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a protein-kinase domain, which supports kinase activity and makes the kinase choices plausible. That alone does not establish this protein's precise substrate specificity or distinguish the broad serine/threonine kinase EC number from a more specific kinase subclass.",
    "missing_item_specific_fact": "The protein-specific functional assignment that ROP18 phosphorylates protein serine and threonine residues, needed to establish EC 2.7.11.1 rather than merely infer kinase activity.",
    "reason": "The exact EC assignment is supported by reviewer-only database and cited experimental evidence, but that annotation and the relevant functional measurements are absent from the question. Recognizing the kinase fold does not supply the item-specific specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D for this sequence. The other kinase choices describe different substrate or enzyme subclasses; the sequence alone may not decisively rule them out, but the supplied reviewer-only evidence identifies the protein's EC number as 2.7.11.1."
  },
  "important_caveats": [
    "The UniProt entry is a database annotation supported by cited publications; the primary papers were not independently reviewed here.",
    "The exact sequence match is established, but the author's original database snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q2PAY2 (ROP18_TOXGO) assigns EC 2.7.11.1 with multiple experimental evidence codes (ECO:0000269 direct assay from PubMed 21147463, 21203588, 24129568; ECO:0000305 from PubMed 23144612). Catalytic activities are documented for both threonyl and seryl phosphorylation of protein substrates using ATP. X-ray crystallography (PDB 4JRN) confirms the kinase domain structure with ATP-analog and Mg²⁺ binding. The sequence matches exactly (SHA-256 confirmed). The evidence is experimental, not merely computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [C11](#evidence-c11), [H1](#evidence-h1), [H2](#evidence-h2), [H8](#evidence-h8), [H9](#evidence-h9), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical protein kinase motifs: a glycine-rich loop (GTPGYEPPER region), the DFG motif (GDFGTYRIN), and a catalytic loop (GKRILAH). These identify it as a protein kinase, eliminating B (2.8.1.7, cystine synthase, a transferase unrelated to phosphorylation). The catalytic architecture is Ser/Thr-type (aspartate in catalytic loop, activation loop), eliminating A (2.7.13.3, histidine kinase, which uses a His-Asp phosphorelay mechanism and lacks the bilobal kinase fold). To distinguish C (2.7.11.24, CDK) from D (2.7.11.1, non-specific Ser/Thr kinase): CDKs are ~300 aa standalone proteins with the PSTAIRE helix-C motif, cyclin-binding interfaces, and cell-cycle regulatory context. This protein is 554 aa with an N-terminal signal peptide (MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNV…) indicating secretion, belongs to the rhoptry kinase family of a parasitic apicomplexan, and lacks CDK-specific sequence signatures. These general architectural and contextual features argue against CDK classification, leaving 2.7.11.1 as the appropriate non-specific Ser/Thr kinase EC number.


**Missing item-specific fact**

> None strictly required. Distinguishing C from D relies on general knowledge of CDK structural signatures (PSTAIRE, cyclin-binding, ~300 aa standalone domain) and recognizing the signal peptide and multi-domain architecture as incompatible with CDK classification.


**Reason**

> The sequence provides identifiable kinase motifs that support protein kinase classification, and the overall architecture (signal peptide, 554 aa length, parasitic origin, absence of CDK-specific motifs) provides biological grounds to eliminate CDK (C) in favor of non-specific Ser/Thr kinase (D). This is general kinase-family knowledge rather than a protein-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (histidine kinase) and B (cystine synthase) are clearly eliminated by the kinase fold and Ser/Thr catalytic mechanism. Option C (CDK) is eliminated by the absence of CDK-specific features and the presence of a secretion signal peptide. Option D is the only remaining defensible choice.


### Important caveats

- The reviewer evidence confirms the EC assignment experimentally, but the evaluated model only sees the raw sequence and four options.
- Distinguishing 2.7.11.1 from 2.7.11.24 requires familiarity with CDK-specific sequence/structural signatures; a model lacking this knowledge might struggle between C and D.
- EC 2.7.11.1 is a broad 'non-specific' catch-all category; the assignment reflects the absence of a more specific EC entry rather than a unique mechanistic distinction.
- The signal peptide at the N-terminus is a general eukaryotic secretion signal and does not uniquely identify ROP18; it simply argues against a nuclear/cytoplasmic cell-cycle kinase.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: a glycine-rich loop (GTPGYEPPER region), the DFG motif (GDFGTYRIN), and a catalytic loop (GKRILAH). These identify it as a protein kinase, eliminating B (2.8.1.7, cystine synthase, a transferase unrelated to phosphorylation). The catalytic architecture is Ser/Thr-type (aspartate in catalytic loop, activation loop), eliminating A (2.7.13.3, histidine kinase, which uses a His-Asp phosphorelay mechanism and lacks the bilobal kinase fold). To distinguish C (2.7.11.24, CDK) from D (2.7.11.1, non-specific Ser/Thr kinase): CDKs are ~300 aa standalone proteins with the PSTAIRE helix-C motif, cyclin-binding interfaces, and cell-cycle regulatory context. This protein is 554 aa with an N-terminal signal peptide (MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNV…) indicating secretion, belongs to the rhoptry kinase family of a parasitic apicomplexan, and lacks CDK-specific sequence signatures. These general architectural and contextual features argue against CDK classification, leaving 2.7.11.1 as the appropriate non-specific Ser/Thr kinase EC number.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Distinguishing C from D relies on general knowledge of CDK structural signatures (PSTAIRE, cyclin-binding, ~300 aa standalone domain) and recognizing the signal peptide and multi-domain architecture as incompatible with CDK classification.",
    "reason": "The sequence provides identifiable kinase motifs that support protein kinase classification, and the overall architecture (signal peptide, 554 aa length, parasitic origin, absence of CDK-specific motifs) provides biological grounds to eliminate CDK (C) in favor of non-specific Ser/Thr kinase (D). This is general kinase-family knowledge rather than a protein-specific database lookup."
  },
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "C9",
      "C11",
      "H1",
      "H2",
      "H8",
      "H9",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q2PAY2 (ROP18_TOXGO) assigns EC 2.7.11.1 with multiple experimental evidence codes (ECO:0000269 direct assay from PubMed 21147463, 21203588, 24129568; ECO:0000305 from PubMed 23144612). Catalytic activities are documented for both threonyl and seryl phosphorylation of protein substrates using ATP. X-ray crystallography (PDB 4JRN) confirms the kinase domain structure with ATP-analog and Mg²⁺ binding. The sequence matches exactly (SHA-256 confirmed). The evidence is experimental, not merely computational inference."
  },
  "important_caveats": [
    "The reviewer evidence confirms the EC assignment experimentally, but the evaluated model only sees the raw sequence and four options.",
    "Distinguishing 2.7.11.1 from 2.7.11.24 requires familiarity with CDK-specific sequence/structural signatures; a model lacking this knowledge might struggle between C and D.",
    "EC 2.7.11.1 is a broad 'non-specific' catch-all category; the assignment reflects the absence of a more specific EC entry rather than a unique mechanistic distinction.",
    "The signal peptide at the N-terminus is a general eukaryotic secretion signal and does not uniquely identify ROP18; it simply argues against a nuclear/cytoplasmic cell-cycle kinase."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (histidine kinase) and B (cystine synthase) are clearly eliminated by the kinase fold and Ser/Thr catalytic mechanism. Option C (CDK) is eliminated by the absence of CDK-specific features and the presence of a secretion signal peptide. Option D is the only remaining defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q2PAY2 (ROP18_TOXGO) assigns EC 2.7.11.1 with multiple experimental evidence codes (ECO:0000269 direct assay from PubMed 21147463, 21203588, 24129568; ECO:0000305 from PubMed 23144612). Catalytic activities are documented for both threonyl and seryl phosphorylation of protein substrates using ATP. X-ray crystallography (PDB 4JRN) confirms the kinase domain structure with ATP-analog and Mg²⁺ binding. The sequence matches exactly (SHA-256 confirmed). The evidence is experimental, not merely computational inference.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "C9", "C11", "H1", "H2", "H8", "H9", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: a glycine-rich loop (GTPGYEPPER region), the DFG motif (GDFGTYRIN), and a catalytic loop (GKRILAH). These identify it as a protein kinase, eliminating B (2.8.1.7, cystine synthase, a transferase unrelated to phosphorylation). The catalytic architecture is Ser/Thr-type (aspartate in catalytic loop, activation loop), eliminating A (2.7.13.3, histidine kinase, which uses a His-Asp phosphorelay mechanism and lacks the bilobal kinase fold). To distinguish C (2.7.11.24, CDK) from D (2.7.11.1, non-specific Ser/Thr kinase): CDKs are ~300 aa standalone proteins with the PSTAIRE helix-C motif, cyclin-binding interfaces, and cell-cycle regulatory context. This protein is 554 aa with an N-terminal signal peptide (MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNV…) indicating secretion, belongs to the rhoptry kinase family of a parasitic apicomplexan, and lacks CDK-specific sequence signatures. These general architectural and contextual features argue against CDK classification, leaving 2.7.11.1 as the appropriate non-specific Ser/Thr kinase EC number.",
    "missing_item_specific_fact": "None strictly required. Distinguishing C from D relies on general knowledge of CDK structural signatures (PSTAIRE, cyclin-binding, ~300 aa standalone domain) and recognizing the signal peptide and multi-domain architecture as incompatible with CDK classification.",
    "reason": "The sequence provides identifiable kinase motifs that support protein kinase classification, and the overall architecture (signal peptide, 554 aa length, parasitic origin, absence of CDK-specific motifs) provides biological grounds to eliminate CDK (C) in favor of non-specific Ser/Thr kinase (D). This is general kinase-family knowledge rather than a protein-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (histidine kinase) and B (cystine synthase) are clearly eliminated by the kinase fold and Ser/Thr catalytic mechanism. Option C (CDK) is eliminated by the absence of CDK-specific features and the presence of a secretion signal peptide. Option D is the only remaining defensible choice."
  },
  "important_caveats": [
    "The reviewer evidence confirms the EC assignment experimentally, but the evaluated model only sees the raw sequence and four options.",
    "Distinguishing 2.7.11.1 from 2.7.11.24 requires familiarity with CDK-specific sequence/structural signatures; a model lacking this knowledge might struggle between C and D.",
    "EC 2.7.11.1 is a broad 'non-specific' catch-all category; the assignment reflects the absence of a more specific EC entry rather than a unique mechanistic distinction.",
    "The signal peptide at the N-terminus is a general eukaryotic secretion signal and does not uniquely identify ROP18; it simply argues against a nuclear/cytoplasmic cell-cycle kinase."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches the reviewed protein record. That record assigns EC 2.7.11.1 and specifies protein serine/threonine phosphorylation; the catalytic-activity annotations cite experimental evidence. This supports choice D.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable eukaryotic protein-kinase catalytic domain, including conserved kinase-family motifs, making a protein kinase a credible inference. Its N-terminal signal-peptide-like hydrophobic segment and long arginine-rich extension are unlike a typical cyclin-dependent kinase, so the general serine/threonine protein kinase category in D is more plausible than the more specialized kinase choice C. The kinase-domain evidence also distinguishes these choices from A and B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable kinase-family sequence features meaningfully favor the broad serine/threonine protein kinase classification over the offered alternatives. The exact substrate specificity and experimentally assigned EC number are not proven from sequence alone, but that limitation does not prevent a credible choice among these options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports a protein kinase, and the unusual N-terminal features make the specialized kinase alternative less plausible than the general serine/threonine protein kinase category.


### Important caveats

- Sequence motifs support family-level inference but do not alone establish the exact catalytic activity.
- The reviewer-only record supports D for this sequence; its protein identity and annotation were not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable eukaryotic protein-kinase catalytic domain, including conserved kinase-family motifs, making a protein kinase a credible inference. Its N-terminal signal-peptide-like hydrophobic segment and long arginine-rich extension are unlike a typical cyclin-dependent kinase, so the general serine/threonine protein kinase category in D is more plausible than the more specialized kinase choice C. The kinase-domain evidence also distinguishes these choices from A and B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase-family sequence features meaningfully favor the broad serine/threonine protein kinase classification over the offered alternatives. The exact substrate specificity and experimentally assigned EC number are not proven from sequence alone, but that limitation does not prevent a credible choice among these options."
  },
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed protein record. That record assigns EC 2.7.11.1 and specifies protein serine/threonine phosphorylation; the catalytic-activity annotations cite experimental evidence. This supports choice D."
  },
  "important_caveats": [
    "Sequence motifs support family-level inference but do not alone establish the exact catalytic activity.",
    "The reviewer-only record supports D for this sequence; its protein identity and annotation were not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a protein kinase, and the unusual N-terminal features make the specialized kinase alternative less plausible than the general serine/threonine protein kinase category."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed protein record. That record assigns EC 2.7.11.1 and specifies protein serine/threonine phosphorylation; the catalytic-activity annotations cite experimental evidence. This supports choice D.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable eukaryotic protein-kinase catalytic domain, including conserved kinase-family motifs, making a protein kinase a credible inference. Its N-terminal signal-peptide-like hydrophobic segment and long arginine-rich extension are unlike a typical cyclin-dependent kinase, so the general serine/threonine protein kinase category in D is more plausible than the more specialized kinase choice C. The kinase-domain evidence also distinguishes these choices from A and B.",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase-family sequence features meaningfully favor the broad serine/threonine protein kinase classification over the offered alternatives. The exact substrate specificity and experimentally assigned EC number are not proven from sequence alone, but that limitation does not prevent a credible choice among these options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a protein kinase, and the unusual N-terminal features make the specialized kinase alternative less plausible than the general serine/threonine protein kinase category."
  },
  "important_caveats": [
    "Sequence motifs support family-level inference but do not alone establish the exact catalytic activity.",
    "The reviewer-only record supports D for this sequence; its protein identity and annotation were not part of the original input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q2PAY2 annotates EC 2.7.11.1 with experimental evidence codes (ECO:0000269) from multiple independent publications (PubMed 21147463, 21203588, 24129568) demonstrating phosphorylation of threonine and serine residues on protein substrates. The catalytic activity reactions (L-threonyl-&#91;protein&#93; + ATP = O-phospho-L-threonyl-&#91;protein&#93; + ADP + H+ and L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H+) are consistent with EC 2.7.11.1 (non-specific serine/threonine protein kinase). An X-ray crystal structure (4JRN) in complex with ATP analog and magnesium ion further supports the kinase assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [C11](#evidence-c11), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical protein kinase motifs: a glycine-rich loop region (GKRI near the kinase domain start), a DFG motif (GDFGTYRINNSVG), and catalytic loop features consistent with a eukaryotic protein kinase. This eliminates option B (2.8.1.7, a sulfurtransferase/CoA ligase with entirely different catalytic chemistry). The Ser/Thr kinase architecture (as opposed to tyrosine kinase features) narrows the answer to the 2.7.11.x subclass, eliminating A (2.7.13.3, a different phosphotransferase subclass). To distinguish D (2.7.11.1, non-specific Ser/Thr kinase) from C (2.7.11.24, MAPK): (1) The N-terminal hydrophobic region (MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNVALVFLLFQVQDG...) is a signal peptide indicating a secreted protein—MAPKs are cytoplasmic/nuclear signaling kinases and are never secreted. (2) The kinase domain lacks the characteristic MAPK activation loop 'TXY' motif and the D-recruitment site/DEF docking motifs that define the MAPK family. (3) The long N-terminal extension (~180 residues) before the kinase domain is atypical for MAPKs, which have compact kinase domains. These transferable features—signal peptide recognition, MAPK family signature motifs, and subcellular localization inference from sequence—meaningfully favor D over C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify kinase motifs to eliminate B, recognize Ser/Thr kinase architecture to eliminate A, and use the presence of a signal peptide (secreted effector) plus absence of MAPK-specific activation loop and docking motifs to favor the general Ser/Thr kinase (2.7.11.1) over MAPK (2.7.11.24). These are transferable principles from general protein kinase biology and secreted effector protein knowledge learned from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the C vs D distinction requires some care, the signal peptide and absence of MAPK-specific motifs provide a clear basis for choosing D over C. The other options (A and B) are readily eliminated by basic kinase motif recognition.


### Important caveats

- The distinction between 2.7.11.1 and 2.7.11.24 relies on recognizing the absence of MAPK-specific features rather than a positive identifying motif for 2.7.11.1. A model unfamiliar with MAPK signature motifs might find C and D harder to separate.
- The signal peptide inference from the N-terminal hydrophobic stretch is a reasonable but not absolute indicator; however, combined with the absence of MAPK motifs, it provides a strong cumulative argument.
- EC 2.7.13.3 is a somewhat obscure EC number; its elimination relies primarily on recognizing the kinase domain as a protein kinase rather than a nitrogenous-group phosphotransferase.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: a glycine-rich loop region (GKRI near the kinase domain start), a DFG motif (GDFGTYRINNSVG), and catalytic loop features consistent with a eukaryotic protein kinase. This eliminates option B (2.8.1.7, a sulfurtransferase/CoA ligase with entirely different catalytic chemistry). The Ser/Thr kinase architecture (as opposed to tyrosine kinase features) narrows the answer to the 2.7.11.x subclass, eliminating A (2.7.13.3, a different phosphotransferase subclass). To distinguish D (2.7.11.1, non-specific Ser/Thr kinase) from C (2.7.11.24, MAPK): (1) The N-terminal hydrophobic region (MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNVALVFLLFQVQDG...) is a signal peptide indicating a secreted protein—MAPKs are cytoplasmic/nuclear signaling kinases and are never secreted. (2) The kinase domain lacks the characteristic MAPK activation loop 'TXY' motif and the D-recruitment site/DEF docking motifs that define the MAPK family. (3) The long N-terminal extension (~180 residues) before the kinase domain is atypical for MAPKs, which have compact kinase domains. These transferable features—signal peptide recognition, MAPK family signature motifs, and subcellular localization inference from sequence—meaningfully favor D over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify kinase motifs to eliminate B, recognize Ser/Thr kinase architecture to eliminate A, and use the presence of a signal peptide (secreted effector) plus absence of MAPK-specific activation loop and docking motifs to favor the general Ser/Thr kinase (2.7.11.1) over MAPK (2.7.11.24). These are transferable principles from general protein kinase biology and secreted effector protein knowledge learned from other proteins."
  },
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "C9",
      "C11",
      "H2",
      "H4",
      "H5",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q2PAY2 annotates EC 2.7.11.1 with experimental evidence codes (ECO:0000269) from multiple independent publications (PubMed 21147463, 21203588, 24129568) demonstrating phosphorylation of threonine and serine residues on protein substrates. The catalytic activity reactions (L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H+ and L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H+) are consistent with EC 2.7.11.1 (non-specific serine/threonine protein kinase). An X-ray crystal structure (4JRN) in complex with ATP analog and magnesium ion further supports the kinase assignment."
  },
  "important_caveats": [
    "The distinction between 2.7.11.1 and 2.7.11.24 relies on recognizing the absence of MAPK-specific features rather than a positive identifying motif for 2.7.11.1. A model unfamiliar with MAPK signature motifs might find C and D harder to separate.",
    "The signal peptide inference from the N-terminal hydrophobic stretch is a reasonable but not absolute indicator; however, combined with the absence of MAPK motifs, it provides a strong cumulative argument.",
    "EC 2.7.13.3 is a somewhat obscure EC number; its elimination relies primarily on recognizing the kinase domain as a protein kinase rather than a nitrogenous-group phosphotransferase."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the C vs D distinction requires some care, the signal peptide and absence of MAPK-specific motifs provide a clear basis for choosing D over C. The other options (A and B) are readily eliminated by basic kinase motif recognition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q2PAY2 annotates EC 2.7.11.1 with experimental evidence codes (ECO:0000269) from multiple independent publications (PubMed 21147463, 21203588, 24129568) demonstrating phosphorylation of threonine and serine residues on protein substrates. The catalytic activity reactions (L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H+ and L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H+) are consistent with EC 2.7.11.1 (non-specific serine/threonine protein kinase). An X-ray crystal structure (4JRN) in complex with ATP analog and magnesium ion further supports the kinase assignment.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "C9", "C11", "H2", "H4", "H5", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: a glycine-rich loop region (GKRI near the kinase domain start), a DFG motif (GDFGTYRINNSVG), and catalytic loop features consistent with a eukaryotic protein kinase. This eliminates option B (2.8.1.7, a sulfurtransferase/CoA ligase with entirely different catalytic chemistry). The Ser/Thr kinase architecture (as opposed to tyrosine kinase features) narrows the answer to the 2.7.11.x subclass, eliminating A (2.7.13.3, a different phosphotransferase subclass). To distinguish D (2.7.11.1, non-specific Ser/Thr kinase) from C (2.7.11.24, MAPK): (1) The N-terminal hydrophobic region (MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNVALVFLLFQVQDG...) is a signal peptide indicating a secreted protein—MAPKs are cytoplasmic/nuclear signaling kinases and are never secreted. (2) The kinase domain lacks the characteristic MAPK activation loop 'TXY' motif and the D-recruitment site/DEF docking motifs that define the MAPK family. (3) The long N-terminal extension (~180 residues) before the kinase domain is atypical for MAPKs, which have compact kinase domains. These transferable features—signal peptide recognition, MAPK family signature motifs, and subcellular localization inference from sequence—meaningfully favor D over C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify kinase motifs to eliminate B, recognize Ser/Thr kinase architecture to eliminate A, and use the presence of a signal peptide (secreted effector) plus absence of MAPK-specific activation loop and docking motifs to favor the general Ser/Thr kinase (2.7.11.1) over MAPK (2.7.11.24). These are transferable principles from general protein kinase biology and secreted effector protein knowledge learned from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the C vs D distinction requires some care, the signal peptide and absence of MAPK-specific motifs provide a clear basis for choosing D over C. The other options (A and B) are readily eliminated by basic kinase motif recognition."
  },
  "important_caveats": [
    "The distinction between 2.7.11.1 and 2.7.11.24 relies on recognizing the absence of MAPK-specific features rather than a positive identifying motif for 2.7.11.1. A model unfamiliar with MAPK signature motifs might find C and D harder to separate.",
    "The signal peptide inference from the N-terminal hydrophobic stretch is a reasonable but not absolute indicator; however, combined with the absence of MAPK motifs, it provides a strong cumulative argument.",
    "EC 2.7.13.3 is a somewhat obscure EC number; its elimination relies primarily on recognizing the kinase domain as a protein kinase rather than a nitrogenous-group phosphotransferase."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q2PAY2",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "23a91ed0d6e99d0f09325c5abf040761e96412e54fbc46c403d922a62ec3475e",
  "benchmark_sequence_length": 554,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 130,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-02-07",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "current_source_sequence_sha256": "23a91ed0d6e99d0f09325c5abf040761e96412e54fbc46c403d922a62ec3475e",
  "current_source_sequence_length": 554,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 128,
  "selected_historical_version": {
    "accession": "Q2PAY2",
    "database": "Swiss-Prot",
    "entryVersion": 128,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ROP18_TOXGO",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700",
  "selected_historical_source_sequence_sha256": "23a91ed0d6e99d0f09325c5abf040761e96412e54fbc46c403d922a62ec3475e",
  "selected_historical_source_sequence_length": 554,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 128,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q2PAY2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":130,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-02-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAJ27113.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii\",\"taxonId\":5811}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54811.1\",\"source\":\"EMBL\"}],\"value\":\"Rhoptry kinase family protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAJ27113.1\",\"source\":\"EMBL\"}],\"value\":\"Rhoptry protein 18\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"KAF4642700.1\",\"source\":\"EMBL\"}],\"value\":\"Rhoptry protein ROP18\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21147463\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21203588\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24129568\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23144612\",\"source\":\"PubMed\"}],\"value\":\"2.7.11.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"19266027\",\"source\":\"PubMed\"}],\"value\":\"Serine/threonine-protein kinase ROP18\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.11.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21147463\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21203588\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24129568\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23144612\",\"source\":\"PubMed\"}],\"name\":\"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:46608\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11605\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30013\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61977\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.11.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23144612\",\"source\":\"PubMed\"}],\"name\":\"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:17989\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9863\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11604\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:83421\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Khan A.\",\"Taylor S.\",\"Ajioka J.W.\",\"Rosenthal B.M.\",\"Sibley L.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19266027\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pgen.1000404\"}],\"citationType\":\"journal article\",\"firstPage\":\"E1000404\",\"id\":\"19266027\",\"journal\":\"PLoS Genet.\",\"lastPage\":\"E1000404\",\"publicationDate\":\"2009\",\"title\":\"Selection at a single locus leads to widespread expansion of Toxoplasma gondii lineages that are virulent in mice.\",\"volume\":\"5\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54811.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54819.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 50869 / FOU\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54818.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"BOF\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54815.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"ENT\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54816.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"GT1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54813.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"MOR\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54812.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"NED\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54811.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"OH3\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54817.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"RH\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54820.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"TgCatBr2\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFO54814.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"VEL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"POLYMORPHISM\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Fentress S.J.\",\"Behnke M.S.\",\"Dunay I.R.\",\"Mashayekhi M.\",\"Rommereim L.M.\",\"Fox B.A.\",\"Bzik D.J.\",\"Taylor G.A.\",\"Turk B.E.\",\"Lichti C.F.\",\"Townsend R.R.\",\"Qiu W.\",\"Hui R.\",\"Beatty W.L.\",\"Sibley L.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21147463\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.chom.2010.11.005\"}],\"citationType\":\"journal article\",\"firstPage\":\"484\",\"id\":\"21147463\",\"journal\":\"Cell Host Microbe\",\"lastPage\":\"495\",\"publicationDate\":\"2010\",\"title\":\"Phosphorylation of immunity-related GTPases by a Toxoplasma gondii-secreted kinase promotes macrophage survival and virulence.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"INTERACTION WITH MOUSE IRGB6 (TGTP1/TGTP2)\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF ASP-409\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Steinfeldt T.\",\"Koenen-Waisman S.\",\"Tong L.\",\"Pawlowski N.\",\"Lamkemeyer T.\",\"Sibley L.D.\",\"Hunn J.P.\",\"Howard J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21203588\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pbio.1000576\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1000576\",\"id\":\"21203588\",\"journal\":\"PLoS Biol.\",\"lastPage\":\"e1000576\",\"publicationDate\":\"2010\",\"title\":\"Phosphorylation of mouse immunity-related GTPase (IRG) resistance proteins is an evasion strategy for virulent Toxoplasma gondii.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF ASP-409\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/references/8",
  "excerpt": "{\"citation\":{\"authors\":[\"Behnke M.S.\",\"Fentress S.J.\",\"Mashayekhi M.\",\"Li L.X.\",\"Taylor G.A.\",\"Sibley L.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23144612\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1002992\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1002992\",\"id\":\"23144612\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1002992\",\"publicationDate\":\"2012\",\"title\":\"The polymorphic pseudokinase ROP5 controls virulence in Toxoplasma gondii by regulating the active kinase ROP18.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":9,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY2.json",
  "source_sha256": "8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c",
  "retrieved_utc": "2026-11-01T06:25:20.547223+00:00",
  "json_pointer": "/references/13",
  "excerpt": "{\"citation\":{\"authors\":[\"Lim D.\",\"Gold D.A.\",\"Julien L.\",\"Rosowski E.E.\",\"Niedelman W.\",\"Yaffe M.B.\",\"Saeij J.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24129568\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m113.523266\"}],\"citationType\":\"journal article\",\"firstPage\":\"34968\",\"id\":\"24129568\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"34980\",\"publicationDate\":\"2013\",\"title\":\"Structure of the Toxoplasma gondii ROP18 kinase domain reveals a second ligand binding pocket required for acute virulence.\",\"volume\":\"288\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4JRN\",\"source\":\"PDB\"}],\"referenceNumber\":14,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.71 ANGSTROMS) OF 187-554 IN COMPLEX WITH ATP ANALOG AND MAGNESIUM ION\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DOMAIN\",\"DISULFIDE BOND\",\"MUTAGENESIS OF ASP-409\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128",
  "source_sha256": "d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700",
  "retrieved_utc": "2026-11-01T06:28:30.449896+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   ROP18_TOXGO             Reviewed;         554 AA.\nAC   Q2PAY2; B9Q063; S7W304;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-FEB-2006, sequence version 1.\nDT   28-JAN-2026, entry version 128.\nDE   RecName: Full=Serine/threonine-protein kinase ROP18 {ECO:0000303|PubMed:19266027};\nDE            EC=2.7.11.1 {ECO:0000269|PubMed:21147463, ECO:0000269|PubMed:21203588, ECO:0000269|PubMed:24129568, ECO:0000305|PubMed:23144612};\nDE   AltName: Full=Rhoptry kinase family protein {ECO:0000312|EMBL:AFO54811.1};\nDE   AltName: Full=Rhoptry protein 18 {ECO:0000312|EMBL:CAJ27113.1};\nDE   AltName: Full=Rhoptry protein ROP18 {ECO:0000312|EMBL:KAF4642700.1};\nGN   Name=ROP18 {ECO:0000312|EMBL:AFO54811.1};\nGN   ORFNames=TGRH88_034260 {ECO:0000312|EMBL:KAF4642700.1};\nOS   Toxoplasma gondii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=5811 {ECO:0000312|EMBL:CAJ27113.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 128,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128",
  "source_sha256": "d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700",
  "retrieved_utc": "2026-11-01T06:28:30.449896+00:00",
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Serine/threonine-protein kinase ROP18 {ECO:0000303|PubMed:19266027};\nDE            EC=2.7.11.1 {ECO:0000269|PubMed:21147463, ECO:0000269|PubMed:21203588, ECO:0000269|PubMed:24129568, ECO:0000305|PubMed:23144612};\nDE   AltName: Full=Rhoptry kinase family protein {ECO:0000312|EMBL:AFO54811.1};\nDE   AltName: Full=Rhoptry protein 18 {ECO:0000312|EMBL:CAJ27113.1};\nDE   AltName: Full=Rhoptry protein ROP18 {ECO:0000312|EMBL:KAF4642700.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 128,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128",
  "source_sha256": "d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700",
  "retrieved_utc": "2026-11-01T06:28:30.449896+00:00",
  "source_locator": "lines 17-30",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AFO54811.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, SUBCELLULAR LOCATION, AND\nRP   POLYMORPHISM.\nRC   STRAIN=ATCC 50869 / FOU {ECO:0000312|EMBL:AFO54819.1},\nRC   BOF {ECO:0000312|EMBL:AFO54818.1}, ENT {ECO:0000312|EMBL:AFO54815.1},\nRC   GT1 {ECO:0000312|EMBL:AFO54816.1}, MOR {ECO:0000312|EMBL:AFO54813.1},\nRC   NED {ECO:0000312|EMBL:AFO54812.1}, OH3 {ECO:0000312|EMBL:AFO54811.1},\nRC   RH {ECO:0000312|EMBL:AFO54817.1}, TgCatBr2 {ECO:0000312|EMBL:AFO54820.1},\nRC   and VEL {ECO:0000312|EMBL:AFO54814.1};\nRX   PubMed=19266027; DOI=10.1371/journal.pgen.1000404;\nRA   Khan A., Taylor S., Ajioka J.W., Rosenthal B.M., Sibley L.D.;\nRT   \"Selection at a single locus leads to widespread expansion of Toxoplasma\nRT   gondii lineages that are virulent in mice.\";\nRL   PLoS Genet. 5:E1000404-E1000404(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 128,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128",
  "source_sha256": "d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700",
  "retrieved_utc": "2026-11-01T06:28:30.449896+00:00",
  "source_locator": "lines 45-54",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, INTERACTION WITH MOUSE IRGB6 (TGTP1/TGTP2),\nRP   DISRUPTION PHENOTYPE, AND MUTAGENESIS OF ASP-409.\nRX   PubMed=21147463; DOI=10.1016/j.chom.2010.11.005;\nRA   Fentress S.J., Behnke M.S., Dunay I.R., Mashayekhi M., Rommereim L.M.,\nRA   Fox B.A., Bzik D.J., Taylor G.A., Turk B.E., Lichti C.F., Townsend R.R.,\nRA   Qiu W., Hui R., Beatty W.L., Sibley L.D.;\nRT   \"Phosphorylation of immunity-related GTPases by a Toxoplasma gondii-\nRT   secreted kinase promotes macrophage survival and virulence.\";\nRL   Cell Host Microbe 8:484-495(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 128,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128",
  "source_sha256": "d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700",
  "retrieved_utc": "2026-11-01T06:28:30.449896+00:00",
  "source_locator": "lines 55-62",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF ASP-409.\nRX   PubMed=21203588; DOI=10.1371/journal.pbio.1000576;\nRA   Steinfeldt T., Koenen-Waisman S., Tong L., Pawlowski N., Lamkemeyer T.,\nRA   Sibley L.D., Hunn J.P., Howard J.C.;\nRT   \"Phosphorylation of mouse immunity-related GTPase (IRG) resistance proteins\nRT   is an evasion strategy for virulent Toxoplasma gondii.\";\nRL   PLoS Biol. 8:e1000576-e1000576(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 128,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128",
  "source_sha256": "d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700",
  "retrieved_utc": "2026-11-01T06:28:30.449896+00:00",
  "source_locator": "lines 84-92",
  "excerpt": "RN   [9] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, SUBCELLULAR LOCATION,\nRP   AND DISRUPTION PHENOTYPE.\nRX   PubMed=23144612; DOI=10.1371/journal.ppat.1002992;\nRA   Behnke M.S., Fentress S.J., Mashayekhi M., Li L.X., Taylor G.A.,\nRA   Sibley L.D.;\nRT   \"The polymorphic pseudokinase ROP5 controls virulence in Toxoplasma gondii\nRT   by regulating the active kinase ROP18.\";\nRL   PLoS Pathog. 8:e1002992-e1002992(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 128,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128",
  "source_sha256": "d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700",
  "retrieved_utc": "2026-11-01T06:28:30.449896+00:00",
  "source_locator": "lines 124-133",
  "excerpt": "RN   [14] {ECO:0007744|PDB:4JRN}\nRP   X-RAY CRYSTALLOGRAPHY (2.71 ANGSTROMS) OF 187-554 IN COMPLEX WITH ATP\nRP   ANALOG AND MAGNESIUM ION, FUNCTION, CATALYTIC ACTIVITY, DOMAIN, DISULFIDE\nRP   BOND, AND MUTAGENESIS OF ASP-409.\nRX   PubMed=24129568; DOI=10.1074/jbc.m113.523266;\nRA   Lim D., Gold D.A., Julien L., Rosowski E.E., Niedelman W., Yaffe M.B.,\nRA   Saeij J.P.;\nRT   \"Structure of the Toxoplasma gondii ROP18 kinase domain reveals a second\nRT   ligand binding pocket required for acute virulence.\";\nRL   J. Biol. Chem. 288:34968-34980(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 128,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128",
  "source_sha256": "d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700",
  "retrieved_utc": "2026-11-01T06:28:30.449896+00:00",
  "source_locator": "lines 158-164",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +\nCC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-\nCC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;\nCC         Evidence={ECO:0000269|PubMed:21147463, ECO:0000269|PubMed:21203588,\nCC         ECO:0000269|PubMed:24129568, ECO:0000305|PubMed:23144612};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 128,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128",
  "source_sha256": "d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700",
  "retrieved_utc": "2026-11-01T06:28:30.449896+00:00",
  "source_locator": "lines 165-170",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +\nCC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-\nCC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;\nCC         Evidence={ECO:0000305|PubMed:23144612};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 128,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 127. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
