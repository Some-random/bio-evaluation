# EC_number_0116

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 2.7.11.11

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLPDTGILSPFTTAVNPDPPQSQTLRVPRPTPVLDRPTTDSTANKRVKLDPTVSKVPWEPSVKPSSSKVEGASGLEQDSFMPTLGSVFKKKKKDKEATRLKDSSGNPDTIIEDSPVTPSTERSLSQSLGSAPSTATTANSHGGLSTVTSATSQTPTSPIATGGQAEKDHPMTTPVNESAGHSRSDSQTLQKAENAVRATKGKYTLQDFNFQRTLGTGSFGRVHLVQSKHNLRFYAVKVLKKAQVVKMKQVEHTNDERRMLQRVKHPFLITLWGTFQDAKNLYMVMDFIEGGELFSLLRKSQRFPNPVAKFYAAEVALALDYLHSMNIIYRDLKPENLLLDRHGHLKITDFGFAKEVPDITWTLCGTPDYLAPEVVASKGYNKSVDWWSLGILIFEMLCGYTPFWDGGSPMKIYENILRGRVKYPAYIHPDAMNLLQQLITPDLTKRLGNLYHGSRSVLEHPWFAEVNWERLLSKQIEPPYVPPVRGGIGDASLFDKYPEETEEYGKDGPDQYGHFFTDF

[Multiple Choices]
A. 2.7.11.11
B. 2.7.11.24
C. 2.3.1.322
D. 1.5.1.38
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

> The exact sequence matches a UniProt entry annotated as a cAMP-dependent protein kinase catalytic subunit with EC 2.7.11.11. The EC assignment and catalytic reactions are supported by similarity transfer from UniProtKB:P17612 (ECO:0000250), rather than demonstrated here by direct experimental evidence on this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a protein-kinase catalytic domain, supporting a kinase classification and making the transferase and oxidoreductase choices poor fits. That broad inference does not establish the specific kinase subtype required to distinguish EC 2.7.11.11 from EC 2.7.11.24.


**Missing item-specific fact**

> The protein-specific identification or functional annotation as a cAMP-dependent protein kinase catalytic subunit, or equivalent evidence distinguishing it from other serine/threonine kinases.


**Reason**

> The exact four-part EC number depends on a subtype assignment not established by the supplied sequence and choices alone; recognizing or retrieving the protein-specific annotation would resolve it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched annotation supports A. The input alone does not securely distinguish the two kinase subtypes, but that uncertainty does not make another option an established alternative.


### Important caveats

- The annotation is similarity-based, not direct experimental evidence for this exact protein.
- The historical sequence match is confirmed, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a protein-kinase catalytic domain, supporting a kinase classification and making the transferase and oxidoreductase choices poor fits. That broad inference does not establish the specific kinase subtype required to distinguish EC 2.7.11.11 from EC 2.7.11.24.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification or functional annotation as a cAMP-dependent protein kinase catalytic subunit, or equivalent evidence distinguishing it from other serine/threonine kinases.",
    "reason": "The exact four-part EC number depends on a subtype assignment not established by the supplied sequence and choices alone; recognizing or retrieving the protein-specific annotation would resolve it."
  },
  "case_id": "EC_number_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a cAMP-dependent protein kinase catalytic subunit with EC 2.7.11.11. The EC assignment and catalytic reactions are supported by similarity transfer from UniProtKB:P17612 (ECO:0000250), rather than demonstrated here by direct experimental evidence on this protein."
  },
  "important_caveats": [
    "The annotation is similarity-based, not direct experimental evidence for this exact protein.",
    "The historical sequence match is confirmed, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports A. The input alone does not securely distinguish the two kinase subtypes, but that uncertainty does not make another option an established alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a cAMP-dependent protein kinase catalytic subunit with EC 2.7.11.11. The EC assignment and catalytic reactions are supported by similarity transfer from UniProtKB:P17612 (ECO:0000250), rather than demonstrated here by direct experimental evidence on this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a protein-kinase catalytic domain, supporting a kinase classification and making the transferase and oxidoreductase choices poor fits. That broad inference does not establish the specific kinase subtype required to distinguish EC 2.7.11.11 from EC 2.7.11.24.",
    "missing_item_specific_fact": "The protein-specific identification or functional annotation as a cAMP-dependent protein kinase catalytic subunit, or equivalent evidence distinguishing it from other serine/threonine kinases.",
    "reason": "The exact four-part EC number depends on a subtype assignment not established by the supplied sequence and choices alone; recognizing or retrieving the protein-specific annotation would resolve it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports A. The input alone does not securely distinguish the two kinase subtypes, but that uncertainty does not make another option an established alternative."
  },
  "important_caveats": [
    "The annotation is similarity-based, not direct experimental evidence for this exact protein.",
    "The historical sequence match is confirmed, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G1X456 (KAPB_ARTOA, Arthrobotrys oligospora) is annotated with EC 2.7.11.11 (cAMP-dependent protein kinase catalytic subunit). The evidence code is ECO:0000250 (inferred by similarity to UniProtKB:P17612), meaning the assignment is computational transfer rather than direct experimental characterization. Nevertheless, the sequence contains canonical AGC-family protein kinase motifs (GxGxxG glycine-rich loop 'GTGSFG', VAIK lysine, HRD catalytic loop 'YRDLKPEN', DFG motif 'DFGFAKE', APE motif 'DYLAPE', DYG motif 'DYGKDGPDQYGHFFTDF'), confirming it is a protein-serine/threonine kinase consistent with EC 2.7.11.x. The specific assignment to 2.7.11.11 is a database annotation by similarity, not an independently validated experimental determination.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable protein kinase catalytic domain motifs (glycine-rich loop, VAIK lysine, HRD catalytic loop, DFG, APE, DYG), immediately eliminating C (acyltransferase, EC 2.3.1.322) and D (oxidoreductase, EC 1.5.1.38). Within EC 2.7.11.x, the sequence exhibits AGC-kinase family architecture: a long N-terminal regulatory extension, the canonical AGC glycine-rich loop 'GTGSFG', and the overall domain organization consistent with cAMP-dependent protein kinase (PKA). A trained biologist could argue for PKA (2.7.11.11) over a non-AGC kinase (2.7.11.24) based on these family-specific sequence signatures.


**Missing item-specific fact**

> The precise identity of EC 2.7.11.24 and the specific residue-level criteria that exclude it (e.g., whether 2.7.11.24 belongs to a different kinase superfamily such as CAMK, STE, or TKL) are not provided in the question. Without knowing what 2.7.11.24 represents, a solver must rely on recognizing AGC/PKA features rather than explicitly ruling out 2.7.11.24 by name.


**Reason**

> The sequence provides strong positive evidence for a protein kinase of the AGC/PKA family, which meaningfully distinguishes A from C and D and provides a defensible biological argument for A over B. However, the A-vs-B distinction is not airtight from sequence alone without knowing the substrate-specificity class of 2.7.11.24; it leans on expert recognition of AGC-family architecture. This is predictive difficulty rather than a wholly missing item-specific fact, so it remains reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are unambiguously wrong given the kinase motifs. Between A and B, both are protein-serine/threonine kinases, but the AGC-family sequence architecture visible in the input provides a defensible biological argument for PKA (2.7.11.11) over a kinase from a different family. No other option is equally defensible.


### Important caveats

- The UniProt EC assignment carries evidence code ECO:0000250 (inferred by similarity to P17612), not direct experimental validation. The annotation is a computational transfer.
- The specific identity and substrate specificity of EC 2.7.11.24 are not stated in the question, so the A-vs-B distinction relies on the solver's knowledge of kinase-family sequence signatures.
- The N-terminal region is unusually long and proline-rich for a canonical PKA catalytic subunit, reflecting fungal-specific features; this does not invalidate the kinase assignment but adds noise to family-level identification.
- All reviewer evidence is annotation-based (UniProt/Swiss-Prot); no independent enzymatic assay data was retrieved.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase catalytic domain motifs (glycine-rich loop, VAIK lysine, HRD catalytic loop, DFG, APE, DYG), immediately eliminating C (acyltransferase, EC 2.3.1.322) and D (oxidoreductase, EC 1.5.1.38). Within EC 2.7.11.x, the sequence exhibits AGC-kinase family architecture: a long N-terminal regulatory extension, the canonical AGC glycine-rich loop 'GTGSFG', and the overall domain organization consistent with cAMP-dependent protein kinase (PKA). A trained biologist could argue for PKA (2.7.11.11) over a non-AGC kinase (2.7.11.24) based on these family-specific sequence signatures.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise identity of EC 2.7.11.24 and the specific residue-level criteria that exclude it (e.g., whether 2.7.11.24 belongs to a different kinase superfamily such as CAMK, STE, or TKL) are not provided in the question. Without knowing what 2.7.11.24 represents, a solver must rely on recognizing AGC/PKA features rather than explicitly ruling out 2.7.11.24 by name.",
    "reason": "The sequence provides strong positive evidence for a protein kinase of the AGC/PKA family, which meaningfully distinguishes A from C and D and provides a defensible biological argument for A over B. However, the A-vs-B distinction is not airtight from sequence alone without knowing the substrate-specificity class of 2.7.11.24; it leans on expert recognition of AGC-family architecture. This is predictive difficulty rather than a wholly missing item-specific fact, so it remains reasoning-supported."
  },
  "case_id": "EC_number_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G1X456 (KAPB_ARTOA, Arthrobotrys oligospora) is annotated with EC 2.7.11.11 (cAMP-dependent protein kinase catalytic subunit). The evidence code is ECO:0000250 (inferred by similarity to UniProtKB:P17612), meaning the assignment is computational transfer rather than direct experimental characterization. Nevertheless, the sequence contains canonical AGC-family protein kinase motifs (GxGxxG glycine-rich loop 'GTGSFG', VAIK lysine, HRD catalytic loop 'YRDLKPEN', DFG motif 'DFGFAKE', APE motif 'DYLAPE', DYG motif 'DYGKDGPDQYGHFFTDF'), confirming it is a protein-serine/threonine kinase consistent with EC 2.7.11.x. The specific assignment to 2.7.11.11 is a database annotation by similarity, not an independently validated experimental determination."
  },
  "important_caveats": [
    "The UniProt EC assignment carries evidence code ECO:0000250 (inferred by similarity to P17612), not direct experimental validation. The annotation is a computational transfer.",
    "The specific identity and substrate specificity of EC 2.7.11.24 are not stated in the question, so the A-vs-B distinction relies on the solver's knowledge of kinase-family sequence signatures.",
    "The N-terminal region is unusually long and proline-rich for a canonical PKA catalytic subunit, reflecting fungal-specific features; this does not invalidate the kinase assignment but adds noise to family-level identification.",
    "All reviewer evidence is annotation-based (UniProt/Swiss-Prot); no independent enzymatic assay data was retrieved."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are unambiguously wrong given the kinase motifs. Between A and B, both are protein-serine/threonine kinases, but the AGC-family sequence architecture visible in the input provides a defensible biological argument for PKA (2.7.11.11) over a kinase from a different family. No other option is equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G1X456 (KAPB_ARTOA, Arthrobotrys oligospora) is annotated with EC 2.7.11.11 (cAMP-dependent protein kinase catalytic subunit). The evidence code is ECO:0000250 (inferred by similarity to UniProtKB:P17612), meaning the assignment is computational transfer rather than direct experimental characterization. Nevertheless, the sequence contains canonical AGC-family protein kinase motifs (GxGxxG glycine-rich loop 'GTGSFG', VAIK lysine, HRD catalytic loop 'YRDLKPEN', DFG motif 'DFGFAKE', APE motif 'DYLAPE', DYG motif 'DYGKDGPDQYGHFFTDF'), confirming it is a protein-serine/threonine kinase consistent with EC 2.7.11.x. The specific assignment to 2.7.11.11 is a database annotation by similarity, not an independently validated experimental determination.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase catalytic domain motifs (glycine-rich loop, VAIK lysine, HRD catalytic loop, DFG, APE, DYG), immediately eliminating C (acyltransferase, EC 2.3.1.322) and D (oxidoreductase, EC 1.5.1.38). Within EC 2.7.11.x, the sequence exhibits AGC-kinase family architecture: a long N-terminal regulatory extension, the canonical AGC glycine-rich loop 'GTGSFG', and the overall domain organization consistent with cAMP-dependent protein kinase (PKA). A trained biologist could argue for PKA (2.7.11.11) over a non-AGC kinase (2.7.11.24) based on these family-specific sequence signatures.",
    "missing_item_specific_fact": "The precise identity of EC 2.7.11.24 and the specific residue-level criteria that exclude it (e.g., whether 2.7.11.24 belongs to a different kinase superfamily such as CAMK, STE, or TKL) are not provided in the question. Without knowing what 2.7.11.24 represents, a solver must rely on recognizing AGC/PKA features rather than explicitly ruling out 2.7.11.24 by name.",
    "reason": "The sequence provides strong positive evidence for a protein kinase of the AGC/PKA family, which meaningfully distinguishes A from C and D and provides a defensible biological argument for A over B. However, the A-vs-B distinction is not airtight from sequence alone without knowing the substrate-specificity class of 2.7.11.24; it leans on expert recognition of AGC-family architecture. This is predictive difficulty rather than a wholly missing item-specific fact, so it remains reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are unambiguously wrong given the kinase motifs. Between A and B, both are protein-serine/threonine kinases, but the AGC-family sequence architecture visible in the input provides a defensible biological argument for PKA (2.7.11.11) over a kinase from a different family. No other option is equally defensible."
  },
  "important_caveats": [
    "The UniProt EC assignment carries evidence code ECO:0000250 (inferred by similarity to P17612), not direct experimental validation. The annotation is a computational transfer.",
    "The specific identity and substrate specificity of EC 2.7.11.24 are not stated in the question, so the A-vs-B distinction relies on the solver's knowledge of kinase-family sequence signatures.",
    "The N-terminal region is unusually long and proline-rich for a canonical PKA catalytic subunit, reflecting fungal-specific features; this does not invalidate the kinase assignment but adds noise to family-level identification.",
    "All reviewer evidence is annotation-based (UniProt/Swiss-Prot); no independent enzymatic assay data was retrieved."
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

**Accession:** `G1X456` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 68. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:31.104931+00:00.  

```json
"G1X456"
```

Source SHA-256: `01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:31.104931+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P17612","source":"UniProtKB"}],"value":"2.7.11.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"cAMP-dependent protein kinase catalytic subunit"}}}
```

Source SHA-256: `01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:31.104931+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.11","evidences":[{"evidenceCode":"ECO:0000250","id":"P17612","source":"UniProtKB"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:31.104931+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.11","evidences":[{"evidenceCode":"ECO:0000250","id":"P17612","source":"UniProtKB"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:28:35.157757+00:00.  

```text
DE   RecName: Full=cAMP-dependent protein kinase catalytic subunit {ECO:0000305};
DE            EC=2.7.11.11 {ECO:0000250|UniProtKB:P17612};
```

Source SHA-256: `1f01b8001fbe7a90ea3f867d72854d5f067cc8fa40465fd612961c21d685324a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68)  
**Locator:** `lines 35-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:28:35.157757+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.11;
CC         Evidence={ECO:0000250|UniProtKB:P17612};
```

Source SHA-256: `1f01b8001fbe7a90ea3f867d72854d5f067cc8fa40465fd612961c21d685324a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68)  
**Locator:** `lines 41-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:28:35.157757+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.11;
CC         Evidence={ECO:0000250|UniProtKB:P17612};
```

Source SHA-256: `1f01b8001fbe7a90ea3f867d72854d5f067cc8fa40465fd612961c21d685324a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 116. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
