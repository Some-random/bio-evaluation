# catalytic_activity_0175

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)

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
A. 3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = 3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
B. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
C. O-phospho-L-homoserine + H2O = L-threonine + phosphate
D. L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)
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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry annotates this protein as a cAMP-dependent protein kinase catalytic subunit and lists the serine-phosphorylation reaction in choice D. The annotation is transferred by similarity (ECO:0000250), not evidence of a direct experiment on this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a protein-kinase catalytic domain, including characteristic kinase motifs such as the glycine-rich ATP-binding loop, the catalytic-loop HRD motif, and the DFG motif. That supports ATP-dependent phosphorylation of protein residues, distinguishing choice D from the methyltransferase and small-molecule reactions.


**Missing item-specific fact**

> The exact protein identity and its database-assigned reaction are absent from the input, but are not necessary to distinguish D among these choices based on the kinase-domain evidence.


**Reason**

> The sequence provides meaningful evidence for kinase activity and a protein substrate. The precise annotation is item-specific, but broad biological reasoning distinguishes the listed reaction class.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation also lists phosphorylation of protein threonine, but that reaction is not among the choices. Of the listed options, only D is a protein-kinase reaction.


### Important caveats

- The database annotation is similarity-transferred from UniProtKB:P17612, so it supports the expected answer but does not establish direct experimental verification for this particular protein.
- The annotated enzyme phosphorylates both serine and threonine residues; choice D represents one of its listed activities.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a protein-kinase catalytic domain, including characteristic kinase motifs such as the glycine-rich ATP-binding loop, the catalytic-loop HRD motif, and the DFG motif. That supports ATP-dependent phosphorylation of protein residues, distinguishing choice D from the methyltransferase and small-molecule reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein identity and its database-assigned reaction are absent from the input, but are not necessary to distinguish D among these choices based on the kinase-domain evidence.",
    "reason": "The sequence provides meaningful evidence for kinase activity and a protein substrate. The precise annotation is item-specific, but broad biological reasoning distinguishes the listed reaction class."
  },
  "case_id": "catalytic_activity_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein as a cAMP-dependent protein kinase catalytic subunit and lists the serine-phosphorylation reaction in choice D. The annotation is transferred by similarity (ECO:0000250), not evidence of a direct experiment on this protein."
  },
  "important_caveats": [
    "The database annotation is similarity-transferred from UniProtKB:P17612, so it supports the expected answer but does not establish direct experimental verification for this particular protein.",
    "The annotated enzyme phosphorylates both serine and threonine residues; choice D represents one of its listed activities."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation also lists phosphorylation of protein threonine, but that reaction is not among the choices. Of the listed options, only D is a protein-kinase reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein as a cAMP-dependent protein kinase catalytic subunit and lists the serine-phosphorylation reaction in choice D. The annotation is transferred by similarity (ECO:0000250), not evidence of a direct experiment on this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a protein-kinase catalytic domain, including characteristic kinase motifs such as the glycine-rich ATP-binding loop, the catalytic-loop HRD motif, and the DFG motif. That supports ATP-dependent phosphorylation of protein residues, distinguishing choice D from the methyltransferase and small-molecule reactions.",
    "missing_item_specific_fact": "The exact protein identity and its database-assigned reaction are absent from the input, but are not necessary to distinguish D among these choices based on the kinase-domain evidence.",
    "reason": "The sequence provides meaningful evidence for kinase activity and a protein substrate. The precise annotation is item-specific, but broad biological reasoning distinguishes the listed reaction class."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation also lists phosphorylation of protein threonine, but that reaction is not among the choices. Of the listed options, only D is a protein-kinase reaction."
  },
  "important_caveats": [
    "The database annotation is similarity-transferred from UniProtKB:P17612, so it supports the expected answer but does not establish direct experimental verification for this particular protein.",
    "The annotated enzyme phosphorylates both serine and threonine residues; choice D represents one of its listed activities."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G1X456 (KAPB_ARTOA, Arthrobotrys oligospora) is annotated as cAMP-dependent protein kinase catalytic subunit (EC 2.7.11.11). The catalytic activity comment explicitly lists 'L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)' matching option D. The annotation is based on similarity transfer (ECO:0000250 to P17612, human PKA catalytic subunit), which is standard for fungal orthologs. The sequence (519 aa, SHA-256 matched) contains canonical protein kinase motifs (GTGSFGRV glycine-rich loop, RDLKPEN catalytic loop, TDFGFAKEV DFG motif, GTPDYLAPEV activation segment), consistent with a Ser/Thr protein kinase. The entry also lists threonine phosphorylation as a second catalytic activity, but that reaction is not among the choices.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable protein kinase catalytic domain motifs: a glycine-rich loop (GTGSFGRVHLV), a β3 lysine, the catalytic loop with HRD-like motif (RDLKPEN), the DFG motif (TDFGFAKEV), and the activation segment (GTPDYLAPEV). These identify the protein as a member of the protein kinase superfamily (EC 2.7.11.x), which transfers phosphate from ATP to protein hydroxyl groups. Among the four options, only D represents a protein kinase reaction (phosphorylation of a protein substrate using ATP). Options A (methyltransferase/COMT), B (dehydratase/lyase), and C (phosphatase/hydrolase) belong to entirely different enzyme classes with no kinase motifs. A biologist recognizing the kinase fold can eliminate A, B, and C and select D.


**Missing item-specific fact**

> None critical. The specific assignment to cAMP-dependent PKA (vs. another Ser/Thr kinase) is supported by the full motif architecture but is not strictly needed to choose D, since D is the only kinase reaction offered.


**Reason**

> The kinase domain motifs are clearly present and identifiable from the primary sequence. The four options span four distinct enzyme classes (methyltransferase, dehydratase, phosphatase, kinase), so recognizing the kinase fold is sufficient to select the correct answer without memorizing this particular organism's entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D is a protein kinase reaction. Although the UniProt entry also lists threonine phosphorylation as a catalytic activity (C6/H5), that reaction is not among the choices. The remaining options (methyltransferase, dehydratase, phosphatase) are categorically incompatible with the kinase motifs present in the sequence. No ambiguity exists.


### Important caveats

- The EC assignment and catalytic activity annotations carry evidence code ECO:0000250 (inferred by similarity to human PKA catalytic subunit P17612), not direct experimental characterization of the A. oligospora protein.
- The entry also annotates L-threonyl-&#91;protein&#93; phosphorylation as a second catalytic activity; the question selects only the serine reaction, which is valid but does not capture the full substrate range of this Ser/Thr kinase.
- Sequence match between the benchmark input and UniProt G1X456 is confirmed (SHA-256 identical, 519 aa).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase catalytic domain motifs: a glycine-rich loop (GTGSFGRVHLV), a β3 lysine, the catalytic loop with HRD-like motif (RDLKPEN), the DFG motif (TDFGFAKEV), and the activation segment (GTPDYLAPEV). These identify the protein as a member of the protein kinase superfamily (EC 2.7.11.x), which transfers phosphate from ATP to protein hydroxyl groups. Among the four options, only D represents a protein kinase reaction (phosphorylation of a protein substrate using ATP). Options A (methyltransferase/COMT), B (dehydratase/lyase), and C (phosphatase/hydrolase) belong to entirely different enzyme classes with no kinase motifs. A biologist recognizing the kinase fold can eliminate A, B, and C and select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific assignment to cAMP-dependent PKA (vs. another Ser/Thr kinase) is supported by the full motif architecture but is not strictly needed to choose D, since D is the only kinase reaction offered.",
    "reason": "The kinase domain motifs are clearly present and identifiable from the primary sequence. The four options span four distinct enzyme classes (methyltransferase, dehydratase, phosphatase, kinase), so recognizing the kinase fold is sufficient to select the correct answer without memorizing this particular organism's entry."
  },
  "case_id": "catalytic_activity_0175",
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
    "reason": "UniProt entry G1X456 (KAPB_ARTOA, Arthrobotrys oligospora) is annotated as cAMP-dependent protein kinase catalytic subunit (EC 2.7.11.11). The catalytic activity comment explicitly lists 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)' matching option D. The annotation is based on similarity transfer (ECO:0000250 to P17612, human PKA catalytic subunit), which is standard for fungal orthologs. The sequence (519 aa, SHA-256 matched) contains canonical protein kinase motifs (GTGSFGRV glycine-rich loop, RDLKPEN catalytic loop, TDFGFAKEV DFG motif, GTPDYLAPEV activation segment), consistent with a Ser/Thr protein kinase. The entry also lists threonine phosphorylation as a second catalytic activity, but that reaction is not among the choices."
  },
  "important_caveats": [
    "The EC assignment and catalytic activity annotations carry evidence code ECO:0000250 (inferred by similarity to human PKA catalytic subunit P17612), not direct experimental characterization of the A. oligospora protein.",
    "The entry also annotates L-threonyl-[protein] phosphorylation as a second catalytic activity; the question selects only the serine reaction, which is valid but does not capture the full substrate range of this Ser/Thr kinase.",
    "Sequence match between the benchmark input and UniProt G1X456 is confirmed (SHA-256 identical, 519 aa)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D is a protein kinase reaction. Although the UniProt entry also lists threonine phosphorylation as a catalytic activity (C6/H5), that reaction is not among the choices. The remaining options (methyltransferase, dehydratase, phosphatase) are categorically incompatible with the kinase motifs present in the sequence. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G1X456 (KAPB_ARTOA, Arthrobotrys oligospora) is annotated as cAMP-dependent protein kinase catalytic subunit (EC 2.7.11.11). The catalytic activity comment explicitly lists 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)' matching option D. The annotation is based on similarity transfer (ECO:0000250 to P17612, human PKA catalytic subunit), which is standard for fungal orthologs. The sequence (519 aa, SHA-256 matched) contains canonical protein kinase motifs (GTGSFGRV glycine-rich loop, RDLKPEN catalytic loop, TDFGFAKEV DFG motif, GTPDYLAPEV activation segment), consistent with a Ser/Thr protein kinase. The entry also lists threonine phosphorylation as a second catalytic activity, but that reaction is not among the choices.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase catalytic domain motifs: a glycine-rich loop (GTGSFGRVHLV), a β3 lysine, the catalytic loop with HRD-like motif (RDLKPEN), the DFG motif (TDFGFAKEV), and the activation segment (GTPDYLAPEV). These identify the protein as a member of the protein kinase superfamily (EC 2.7.11.x), which transfers phosphate from ATP to protein hydroxyl groups. Among the four options, only D represents a protein kinase reaction (phosphorylation of a protein substrate using ATP). Options A (methyltransferase/COMT), B (dehydratase/lyase), and C (phosphatase/hydrolase) belong to entirely different enzyme classes with no kinase motifs. A biologist recognizing the kinase fold can eliminate A, B, and C and select D.",
    "missing_item_specific_fact": "None critical. The specific assignment to cAMP-dependent PKA (vs. another Ser/Thr kinase) is supported by the full motif architecture but is not strictly needed to choose D, since D is the only kinase reaction offered.",
    "reason": "The kinase domain motifs are clearly present and identifiable from the primary sequence. The four options span four distinct enzyme classes (methyltransferase, dehydratase, phosphatase, kinase), so recognizing the kinase fold is sufficient to select the correct answer without memorizing this particular organism's entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D is a protein kinase reaction. Although the UniProt entry also lists threonine phosphorylation as a catalytic activity (C6/H5), that reaction is not among the choices. The remaining options (methyltransferase, dehydratase, phosphatase) are categorically incompatible with the kinase motifs present in the sequence. No ambiguity exists."
  },
  "important_caveats": [
    "The EC assignment and catalytic activity annotations carry evidence code ECO:0000250 (inferred by similarity to human PKA catalytic subunit P17612), not direct experimental characterization of the A. oligospora protein.",
    "The entry also annotates L-threonyl-[protein] phosphorylation as a second catalytic activity; the question selects only the serine reaction, which is valid but does not capture the full substrate range of this Ser/Thr kinase.",
    "Sequence match between the benchmark input and UniProt G1X456 is confirmed (SHA-256 identical, 519 aa)."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 175. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
