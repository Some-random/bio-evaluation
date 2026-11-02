# GO_molecular_function_0174

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — ATP binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLPDTGILSPFTTAVNPDPPQSQTLRVPRPTPVLDRPTTDSTANKRVKLDPTVSKVPWEPSVKPSSSKVEGASGLEQDSFMPTLGSVFKKKKKDKEATRLKDSSGNPDTIIEDSPVTPSTERSLSQSLGSAPSTATTANSHGGLSTVTSATSQTPTSPIATGGQAEKDHPMTTPVNESAGHSRSDSQTLQKAENAVRATKGKYTLQDFNFQRTLGTGSFGRVHLVQSKHNLRFYAVKVLKKAQVVKMKQVEHTNDERRMLQRVKHPFLITLWGTFQDAKNLYMVMDFIEGGELFSLLRKSQRFPNPVAKFYAAEVALALDYLHSMNIIYRDLKPENLLLDRHGHLKITDFGFAKEVPDITWTLCGTPDYLAPEVVASKGYNKSVDWWSLGILIFEMLCGYTPFWDGGSPMKIYENILRGRVKYPAYIHPDAMNLLQQLITPDLTKRLGNLYHGSRSVLEHPWFAEVNWERLLSKQIEPPYVPPVRGGIGDASLFDKYPEETEEYGKDGPDQYGHFFTDF

[Multiple Choices]
A. histone deacetylase activity
B. ATP binding
C. large ribosomal subunit rRNA binding
D. methylated histone binding
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

> The sequence matches a cAMP-dependent protein kinase catalytic subunit. The annotation assigns ATP binding, and the annotated kinase reaction uses ATP to phosphorylate protein serine and threonine residues. The catalytic activity is supported by similarity-based evidence, while the ATP-binding GO annotation is computational; these are not presented as direct experimental measurements for this protein.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains a recognizable protein kinase catalytic domain, including conserved kinase motifs. General biological knowledge that protein kinases bind and use ATP to transfer phosphate meaningfully favors ATP binding over histone deacetylation or the listed ribosomal-RNA and methylated-histone binding functions.


**Missing item-specific fact**

> No item-specific annotation is needed to distinguish these choices; recognizing the kinase domain and its ATP-dependent catalytic role is sufficient.


**Reason**

> The sequence provides a concrete functional signature, and the distractors describe activities not indicated by that domain. This is a defensible sequence-based inference, not merely recollection of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, ATP binding is the clear match to a protein kinase catalytic sequence.


### Important caveats

- The reviewer-only ATP-binding GO annotation is computationally assigned, and the listed catalytic reactions are supported by similarity evidence; neither establishes a direct experimental binding measurement for this exact protein.
- ATP binding is a broad molecular function, whereas the sequence indicates a more specific kinase activity that is not offered as an option.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains a recognizable protein kinase catalytic domain, including conserved kinase motifs. General biological knowledge that protein kinases bind and use ATP to transfer phosphate meaningfully favors ATP binding over histone deacetylation or the listed ribosomal-RNA and methylated-histone binding functions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific annotation is needed to distinguish these choices; recognizing the kinase domain and its ATP-dependent catalytic role is sufficient.",
    "reason": "The sequence provides a concrete functional signature, and the distractors describe activities not indicated by that domain. This is a defensible sequence-based inference, not merely recollection of a database entry."
  },
  "case_id": "GO_molecular_function_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "C7",
      "C8",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches a cAMP-dependent protein kinase catalytic subunit. The annotation assigns ATP binding, and the annotated kinase reaction uses ATP to phosphorylate protein serine and threonine residues. The catalytic activity is supported by similarity-based evidence, while the ATP-binding GO annotation is computational; these are not presented as direct experimental measurements for this protein."
  },
  "important_caveats": [
    "The reviewer-only ATP-binding GO annotation is computationally assigned, and the listed catalytic reactions are supported by similarity evidence; neither establishes a direct experimental binding measurement for this exact protein.",
    "ATP binding is a broad molecular function, whereas the sequence indicates a more specific kinase activity that is not offered as an option."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, ATP binding is the clear match to a protein kinase catalytic sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches a cAMP-dependent protein kinase catalytic subunit. The annotation assigns ATP binding, and the annotated kinase reaction uses ATP to phosphorylate protein serine and threonine residues. The catalytic activity is supported by similarity-based evidence, while the ATP-binding GO annotation is computational; these are not presented as direct experimental measurements for this protein.",
    "evidence_ids": ["C4", "C6", "C7", "C8", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence contains a recognizable protein kinase catalytic domain, including conserved kinase motifs. General biological knowledge that protein kinases bind and use ATP to transfer phosphate meaningfully favors ATP binding over histone deacetylation or the listed ribosomal-RNA and methylated-histone binding functions.",
    "missing_item_specific_fact": "No item-specific annotation is needed to distinguish these choices; recognizing the kinase domain and its ATP-dependent catalytic role is sufficient.",
    "reason": "The sequence provides a concrete functional signature, and the distractors describe activities not indicated by that domain. This is a defensible sequence-based inference, not merely recollection of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, ATP binding is the clear match to a protein kinase catalytic sequence."
  },
  "important_caveats": [
    "The reviewer-only ATP-binding GO annotation is computationally assigned, and the listed catalytic reactions are supported by similarity evidence; neither establishes a direct experimental binding measurement for this exact protein.",
    "ATP binding is a broad molecular function, whereas the sequence indicates a more specific kinase activity that is not offered as an option."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (UniProt G1X456) is annotated as a cAMP-dependent protein kinase catalytic subunit (EC 2.7.11.11). GO:0005524 (ATP binding) is explicitly assigned to this entry (evidence IEA:InterPro / UniProtKB-KW). The catalytic reactions (C6, C7, H4, H5) confirm ATP is a required substrate. Among the four options, only ATP binding is consistent with a protein kinase; the other three (histone deacetylase activity, large ribosomal subunit rRNA binding, methylated histone binding) are mechanistically incompatible with a kinase. The answer is supported, though the GO annotation evidence code is computational (IEA), not experimental.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical protein kinase motifs: the glycine-rich loop (GTLGTGSFGRV, residues ~170-180), the catalytic HRD-equivalent region (YRDLKPEN), the DFG motif (KITDFG), and the APE motif (LAPE). The overall ~519-residue architecture matches the bilobal kinase fold. A model recognizing these motifs can infer the protein is a Ser/Thr kinase, which obligately binds ATP as a phosphate donor. Among the four options, only ATP binding (B) is compatible with kinase catalysis; histone deacetylase activity (A) requires a zinc-dependent or NAD+-dependent hydrolytic mechanism with entirely different folds, large ribosomal subunit rRNA binding (C) requires ribosomal protein domains, and methylated histone binding (D) requires chromodomain/Tudor/MBT modules. None of these alternative folds or motifs are present.


**Missing item-specific fact**

> None. The kinase motifs are visible in the supplied sequence, and the inference 'kinase → binds ATP' is general biochemistry.


**Reason**

> The conserved kinase subdomains (Gly-rich loop, VAIK, HRD, DFG, APE) are identifiable by pattern matching within the provided sequence, and the functional link between kinase activity and ATP binding is textbook biochemistry. No protein-specific database lookup is required to eliminate the three distractors.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> ATP binding is the only option mechanistically consistent with a protein kinase. The other three options describe functions (HDAC catalysis, rRNA binding, methyl-lysine recognition) that require entirely different structural folds and catalytic mechanisms absent from this sequence. No ambiguity exists among the choices.


### Important caveats

- The GO:0005524 (ATP binding) annotation carries evidence code IEA (Inferred from Electronic Annotation) via InterPro/UniProtKB-KW, not direct experimental binding data. However, ATP binding by kinases is an extremely well-established general biochemical fact.
- The more precise molecular function would be 'cAMP-dependent protein kinase activity' (GO:0004691) or 'protein serine kinase activity' (GO:0106310), but these are not offered as options. ATP binding is the best available choice among the four.
- The EC assignment (2.7.11.11) is transferred by similarity from P17612 (mouse PKA-Cα, ECO:0000250), not experimentally determined for this fungal protein. The experimental evidence (PubMed 35993904) supports the protein's role in the cAMP-PKA pathway but does not independently confirm ATP-binding kinetics for this specific ortholog.
- The UniProt entry was first publicly released in April 2025; the benchmark construction date is unknown. The sequence itself has been unchanged since November 2011.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: the glycine-rich loop (GTLGTGSFGRV, residues ~170-180), the catalytic HRD-equivalent region (YRDLKPEN), the DFG motif (KITDFG), and the APE motif (LAPE). The overall ~519-residue architecture matches the bilobal kinase fold. A model recognizing these motifs can infer the protein is a Ser/Thr kinase, which obligately binds ATP as a phosphate donor. Among the four options, only ATP binding (B) is compatible with kinase catalysis; histone deacetylase activity (A) requires a zinc-dependent or NAD+-dependent hydrolytic mechanism with entirely different folds, large ribosomal subunit rRNA binding (C) requires ribosomal protein domains, and methylated histone binding (D) requires chromodomain/Tudor/MBT modules. None of these alternative folds or motifs are present.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None. The kinase motifs are visible in the supplied sequence, and the inference 'kinase → binds ATP' is general biochemistry.",
    "reason": "The conserved kinase subdomains (Gly-rich loop, VAIK, HRD, DFG, APE) are identifiable by pattern matching within the provided sequence, and the functional link between kinase activity and ATP binding is textbook biochemistry. No protein-specific database lookup is required to eliminate the three distractors."
  },
  "case_id": "GO_molecular_function_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "C7",
      "C8",
      "H4",
      "H5",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein (UniProt G1X456) is annotated as a cAMP-dependent protein kinase catalytic subunit (EC 2.7.11.11). GO:0005524 (ATP binding) is explicitly assigned to this entry (evidence IEA:InterPro / UniProtKB-KW). The catalytic reactions (C6, C7, H4, H5) confirm ATP is a required substrate. Among the four options, only ATP binding is consistent with a protein kinase; the other three (histone deacetylase activity, large ribosomal subunit rRNA binding, methylated histone binding) are mechanistically incompatible with a kinase. The answer is supported, though the GO annotation evidence code is computational (IEA), not experimental."
  },
  "important_caveats": [
    "The GO:0005524 (ATP binding) annotation carries evidence code IEA (Inferred from Electronic Annotation) via InterPro/UniProtKB-KW, not direct experimental binding data. However, ATP binding by kinases is an extremely well-established general biochemical fact.",
    "The more precise molecular function would be 'cAMP-dependent protein kinase activity' (GO:0004691) or 'protein serine kinase activity' (GO:0106310), but these are not offered as options. ATP binding is the best available choice among the four.",
    "The EC assignment (2.7.11.11) is transferred by similarity from P17612 (mouse PKA-Cα, ECO:0000250), not experimentally determined for this fungal protein. The experimental evidence (PubMed 35993904) supports the protein's role in the cAMP-PKA pathway but does not independently confirm ATP-binding kinetics for this specific ortholog.",
    "The UniProt entry was first publicly released in April 2025; the benchmark construction date is unknown. The sequence itself has been unchanged since November 2011."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "ATP binding is the only option mechanistically consistent with a protein kinase. The other three options describe functions (HDAC catalysis, rRNA binding, methyl-lysine recognition) that require entirely different structural folds and catalytic mechanisms absent from this sequence. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (UniProt G1X456) is annotated as a cAMP-dependent protein kinase catalytic subunit (EC 2.7.11.11). GO:0005524 (ATP binding) is explicitly assigned to this entry (evidence IEA:InterPro / UniProtKB-KW). The catalytic reactions (C6, C7, H4, H5) confirm ATP is a required substrate. Among the four options, only ATP binding is consistent with a protein kinase; the other three (histone deacetylase activity, large ribosomal subunit rRNA binding, methylated histone binding) are mechanistically incompatible with a kinase. The answer is supported, though the GO annotation evidence code is computational (IEA), not experimental.",
    "evidence_ids": ["C4", "C6", "C7", "C8", "H4", "H5", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: the glycine-rich loop (GTLGTGSFGRV, residues ~170-180), the catalytic HRD-equivalent region (YRDLKPEN), the DFG motif (KITDFG), and the APE motif (LAPE). The overall ~519-residue architecture matches the bilobal kinase fold. A model recognizing these motifs can infer the protein is a Ser/Thr kinase, which obligately binds ATP as a phosphate donor. Among the four options, only ATP binding (B) is compatible with kinase catalysis; histone deacetylase activity (A) requires a zinc-dependent or NAD+-dependent hydrolytic mechanism with entirely different folds, large ribosomal subunit rRNA binding (C) requires ribosomal protein domains, and methylated histone binding (D) requires chromodomain/Tudor/MBT modules. None of these alternative folds or motifs are present.",
    "missing_item_specific_fact": "None. The kinase motifs are visible in the supplied sequence, and the inference 'kinase → binds ATP' is general biochemistry.",
    "reason": "The conserved kinase subdomains (Gly-rich loop, VAIK, HRD, DFG, APE) are identifiable by pattern matching within the provided sequence, and the functional link between kinase activity and ATP binding is textbook biochemistry. No protein-specific database lookup is required to eliminate the three distractors."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "ATP binding is the only option mechanistically consistent with a protein kinase. The other three options describe functions (HDAC catalysis, rRNA binding, methyl-lysine recognition) that require entirely different structural folds and catalytic mechanisms absent from this sequence. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The GO:0005524 (ATP binding) annotation carries evidence code IEA (Inferred from Electronic Annotation) via InterPro/UniProtKB-KW, not direct experimental binding data. However, ATP binding by kinases is an extremely well-established general biochemical fact.",
    "The more precise molecular function would be 'cAMP-dependent protein kinase activity' (GO:0004691) or 'protein serine kinase activity' (GO:0106310), but these are not offered as options. ATP binding is the best available choice among the four.",
    "The EC assignment (2.7.11.11) is transferred by similarity from P17612 (mouse PKA-Cα, ECO:0000250), not experimentally determined for this fungal protein. The experimental evidence (PubMed 35993904) supports the protein's role in the cAMP-PKA pathway but does not independently confirm ATP-binding kinetics for this specific ortholog.",
    "The UniProt entry was first publicly released in April 2025; the benchmark construction date is unknown. The sequence itself has been unchanged since November 2011."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:31.104931+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.11","evidences":[{"evidenceCode":"ECO:0000250","id":"P17612","source":"UniProtKB"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:31.104931+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.11","evidences":[{"evidenceCode":"ECO:0000250","id":"P17612","source":"UniProtKB"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X456.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:31.104931+00:00.  

```json
{"database":"GO","id":"GO:0005524","properties":[{"key":"GoTerm","value":"F:ATP binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `01bb4f79b0689d92b35fa3e5580b08b462a731e6219eb2c6ab2904056425dbc5`.

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

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X456?format=txt&versions=68)  
**Locator:** `lines 77-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:28:35.157757+00:00.  

```text
DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW.
```

Source SHA-256: `1f01b8001fbe7a90ea3f867d72854d5f067cc8fa40465fd612961c21d685324a`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 57041-57052`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005524
name: ATP binding
namespace: molecular_function
def: "Binding to ATP, adenosine 5'-triphosphate, a universally important coenzyme and enzyme regulator." [ISBN:0198506732]
synonym: "Mg-ATP binding" EXACT []
synonym: "MgATP binding" EXACT []
xref: Reactome:R-HSA-265682 "KCNJ11 tetramer:ABCC8 tetramer binds 4xATP, closing the channel"
is_a: GO:0032559 ! adenyl ribonucleotide binding
is_a: GO:0035639 ! purine ribonucleoside triphosphate binding
is_a: GO:0043168 ! anion binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 174. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
