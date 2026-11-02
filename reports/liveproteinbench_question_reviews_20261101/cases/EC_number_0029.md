# EC_number_0029

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.14.11.65

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQKELAALVATRTSRKRTISSTSFSISTRTDPKSIIEIHIFNDSLPIKRACCEVENPTLKAEQRVQQEEESLGQVPPLTEEEQQRHDEFRNSGSIFLQDLPCFKLQQAQPIAGSSPIPKCRECRRRNLATTEGEPSSVSDVYCRFYEFRRLQFNENGELCVVGFPNPYSEPSPEDIAIWQPDKNTPPTSGYMDIQVCRYILLHAGDQFCYIWHQEAEALSLHQNTDGTIAWKKAVKGTREICDVCDTTLFNYHWTCRKCGFGVCLDCVKDRKEGLRLRRAENAAQKGCDEYHWLLCSDPSGPQEHVLTELMLTQIIAGDALNVLGRLLHEVRTLWQVPQVCGCLLSKQAIEDAQSKEVIQDMIKESQLKQHTSYSSLASEQKVHQQQRLDQLHATKLEFARELGVDYVPGRVWTKETLGKDPITTAFDNLKHINFLRKGLAGLRRFLPPRTMTFAYSTQLAPGVPHEFLCDGRLLRLTDAMHPDNRVLFQEVWKCGQPVMISEVARSLNLDLWHPQAFCRDFGDKPNDLINCLNGNLVPNQPMRHFWEGFQCMTKRLPDAYGKPMLLKLKDWPPGDDFAEILPTRFADLMKGLPMPEYTLRTGNLNIASCLPKMFVPPDLGPKMYNAYGSALHPDKGTTNLHLDISDAVNIMVYVGIPQDGDTRPQMAATQKAIEIGGCDYITRARCQSPDVLPGALWHIFPARDADKIRDLLNRVTLEKGFRLEPDHDPIHDQNWYLDDKLRARLFKEYGVEGHPIVQCLGDAVFIPAGAPHQVQNLHNCIKVAEDFVSPENITHCYHLTHEFRRLSHSHTNHEDKLQIKNIIYHAIKDCCTILTRAVDERLNAELTKLNAD

[Multiple Choices]
A. 1.14.11.65
B. 1.14.11.63
C. 2.1.1.34
D. 1.97.1.14
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

> The sequence matches the Drosophila KDM3 entry, whose annotated EC number is 1.14.11.65. The annotation assigns histone H3 lysine demethylation to this enzyme, supporting choice A. However, the EC assignment is transferred by similarity from UniProtKB Q9Y4C1 (ECO:0000250), not shown here as direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a JmjC-family, 2-oxoglutarate-dependent demethylase, which helps distinguish it from the methyltransferase option. That general evidence does not establish the precise substrate-specific EC subclass.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence assigning this KDM3 protein to EC 1.14.11.65 rather than the closely related listed EC 1.14.11.63.


**Reason**

> Choosing between the similar demethylase EC options depends on protein-specific substrate/function information absent from the supplied sequence and choices; recognizing or retrieving the exact protein annotation is lookup, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The sequence-level evidence supplied supports a JmjC demethylase but does not distinguish the substrate-specific EC assignments represented by A and B. The reviewer-only annotation supports A, but that annotation was not part of the evaluated input.


### Important caveats

- The sequence match and source identity are established by reviewer-only evidence, not by information supplied to the evaluated model.
- The EC annotation is similarity-transferred; the excerpts do not establish direct experimental validation for this particular Drosophila protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a JmjC-family, 2-oxoglutarate-dependent demethylase, which helps distinguish it from the methyltransferase option. That general evidence does not establish the precise substrate-specific EC subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence assigning this KDM3 protein to EC 1.14.11.65 rather than the closely related listed EC 1.14.11.63.",
    "reason": "Choosing between the similar demethylase EC options depends on protein-specific substrate/function information absent from the supplied sequence and choices; recognizing or retrieving the exact protein annotation is lookup, not reasoning from the provided input."
  },
  "case_id": "EC_number_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila KDM3 entry, whose annotated EC number is 1.14.11.65. The annotation assigns histone H3 lysine demethylation to this enzyme, supporting choice A. However, the EC assignment is transferred by similarity from UniProtKB Q9Y4C1 (ECO:0000250), not shown here as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The sequence match and source identity are established by reviewer-only evidence, not by information supplied to the evaluated model.",
    "The EC annotation is similarity-transferred; the excerpts do not establish direct experimental validation for this particular Drosophila protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The sequence-level evidence supplied supports a JmjC demethylase but does not distinguish the substrate-specific EC assignments represented by A and B. The reviewer-only annotation supports A, but that annotation was not part of the evaluated input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila KDM3 entry, whose annotated EC number is 1.14.11.65. The annotation assigns histone H3 lysine demethylation to this enzyme, supporting choice A. However, the EC assignment is transferred by similarity from UniProtKB Q9Y4C1 (ECO:0000250), not shown here as direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a JmjC-family, 2-oxoglutarate-dependent demethylase, which helps distinguish it from the methyltransferase option. That general evidence does not establish the precise substrate-specific EC subclass.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence assigning this KDM3 protein to EC 1.14.11.65 rather than the closely related listed EC 1.14.11.63.",
    "reason": "Choosing between the similar demethylase EC options depends on protein-specific substrate/function information absent from the supplied sequence and choices; recognizing or retrieving the exact protein annotation is lookup, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The sequence-level evidence supplied supports a JmjC demethylase but does not distinguish the substrate-specific EC assignments represented by A and B. The reviewer-only annotation supports A, but that annotation was not part of the evaluated input."
  },
  "important_caveats": [
    "The sequence match and source identity are established by reviewer-only evidence, not by information supplied to the evaluated model.",
    "The EC annotation is similarity-transferred; the excerpts do not establish direct experimental validation for this particular Drosophila protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry Q9VHC5 (KDM3_DROME, Drosophila melanogaster) with identical SHA256. The annotation assigns EC 1.14.11.65 (Lysine-specific demethylase 3) with evidence code ECO:0000250 (transferred by similarity from human KDM3A/Q9Y4C1). The catalytic reaction (H3K9me2 demethylation via 2-oxoglutarate-dependent dioxygenase mechanism) is consistent with EC 1.14.11.65. The annotation is computational/similarity-based rather than directly experimental on the fly protein, but it is the established database assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a JmjN-JmjC-PHD domain architecture, which is characteristic of 2-oxoglutarate-dependent histone lysine demethylases (EC 1.14.11.x). This reasoning eliminates option C (2.1.1.34, a methyltransferase) and option D (1.97.1.14, a reductase). However, distinguishing between EC 1.14.11.65 (KDM3, H3K9me2 demethylase) and EC 1.14.11.63 (KDM4B, H3K36me3/me2 demethylase) requires knowing the specific substrate residue targeted by this particular JmjC domain variant. Both share the same domain architecture (JmjN-JmjC-PHD) and catalytic mechanism; the substrate specificity is determined by subtle active-site residue differences not reliably inferable from linear sequence alone.


**Missing item-specific fact**

> The specific histone lysine residue (H3K9 vs H3K36) demethylated by this particular JmjC-domain protein, which determines the final two digits of the EC number. This is a protein-specific experimental/biochemical fact not derivable from general domain recognition.


**Reason**

> While general biological knowledge about JmjC-domain proteins can narrow the answer to the 1.14.11.x class and eliminate options C and D, the final choice between 1.14.11.65 and 1.14.11.63 depends on recognizing this specific protein (Drosophila Kdm3) and recalling its experimentally determined substrate specificity (H3K9me2). The domain architectures of KDM3 and KDM4 families are too similar for reliable sequence-based discrimination at the EC sub-subclass level.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 1.14.11.65 (KDM3, H3K9me2 demethylase) and 1.14.11.63 (KDM4B, H3K36me3/me2 demethylase) describe JmjC-domain 2-oxoglutarate-dependent lysine demethylases with similar domain architectures. Without protein-specific substrate data, a knowledgeable model could reasonably assign either EC number based on general JmjC-domain features. The distinction requires item-specific knowledge of which histone residue this particular enzyme targets.


### Important caveats

- The EC annotation is transferred by similarity (ECO:0000250) from human KDM3A (Q9Y4C1), not from direct experimental characterization of the Drosophila protein.
- The sequence match is exact (SHA256 identical) between the benchmark input and UniProt Q9VHC5.
- The historical annotation (entry version 180, released Jan 2026) already carried EC 1.14.11.65, so the key was available at the time of benchmark construction.
- Options C and D are clearly eliminable by domain recognition, reducing the effective discrimination to a binary A vs B choice that requires protein-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a JmjN-JmjC-PHD domain architecture, which is characteristic of 2-oxoglutarate-dependent histone lysine demethylases (EC 1.14.11.x). This reasoning eliminates option C (2.1.1.34, a methyltransferase) and option D (1.97.1.14, a reductase). However, distinguishing between EC 1.14.11.65 (KDM3, H3K9me2 demethylase) and EC 1.14.11.63 (KDM4B, H3K36me3/me2 demethylase) requires knowing the specific substrate residue targeted by this particular JmjC domain variant. Both share the same domain architecture (JmjN-JmjC-PHD) and catalytic mechanism; the substrate specificity is determined by subtle active-site residue differences not reliably inferable from linear sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific histone lysine residue (H3K9 vs H3K36) demethylated by this particular JmjC-domain protein, which determines the final two digits of the EC number. This is a protein-specific experimental/biochemical fact not derivable from general domain recognition.",
    "reason": "While general biological knowledge about JmjC-domain proteins can narrow the answer to the 1.14.11.x class and eliminate options C and D, the final choice between 1.14.11.65 and 1.14.11.63 depends on recognizing this specific protein (Drosophila Kdm3) and recalling its experimentally determined substrate specificity (H3K9me2). The domain architectures of KDM3 and KDM4 families are too similar for reliable sequence-based discrimination at the EC sub-subclass level."
  },
  "case_id": "EC_number_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry Q9VHC5 (KDM3_DROME, Drosophila melanogaster) with identical SHA256. The annotation assigns EC 1.14.11.65 (Lysine-specific demethylase 3) with evidence code ECO:0000250 (transferred by similarity from human KDM3A/Q9Y4C1). The catalytic reaction (H3K9me2 demethylation via 2-oxoglutarate-dependent dioxygenase mechanism) is consistent with EC 1.14.11.65. The annotation is computational/similarity-based rather than directly experimental on the fly protein, but it is the established database assignment."
  },
  "important_caveats": [
    "The EC annotation is transferred by similarity (ECO:0000250) from human KDM3A (Q9Y4C1), not from direct experimental characterization of the Drosophila protein.",
    "The sequence match is exact (SHA256 identical) between the benchmark input and UniProt Q9VHC5.",
    "The historical annotation (entry version 180, released Jan 2026) already carried EC 1.14.11.65, so the key was available at the time of benchmark construction.",
    "Options C and D are clearly eliminable by domain recognition, reducing the effective discrimination to a binary A vs B choice that requires protein-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 1.14.11.65 (KDM3, H3K9me2 demethylase) and 1.14.11.63 (KDM4B, H3K36me3/me2 demethylase) describe JmjC-domain 2-oxoglutarate-dependent lysine demethylases with similar domain architectures. Without protein-specific substrate data, a knowledgeable model could reasonably assign either EC number based on general JmjC-domain features. The distinction requires item-specific knowledge of which histone residue this particular enzyme targets."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry Q9VHC5 (KDM3_DROME, Drosophila melanogaster) with identical SHA256. The annotation assigns EC 1.14.11.65 (Lysine-specific demethylase 3) with evidence code ECO:0000250 (transferred by similarity from human KDM3A/Q9Y4C1). The catalytic reaction (H3K9me2 demethylation via 2-oxoglutarate-dependent dioxygenase mechanism) is consistent with EC 1.14.11.65. The annotation is computational/similarity-based rather than directly experimental on the fly protein, but it is the established database assignment.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a JmjN-JmjC-PHD domain architecture, which is characteristic of 2-oxoglutarate-dependent histone lysine demethylases (EC 1.14.11.x). This reasoning eliminates option C (2.1.1.34, a methyltransferase) and option D (1.97.1.14, a reductase). However, distinguishing between EC 1.14.11.65 (KDM3, H3K9me2 demethylase) and EC 1.14.11.63 (KDM4B, H3K36me3/me2 demethylase) requires knowing the specific substrate residue targeted by this particular JmjC domain variant. Both share the same domain architecture (JmjN-JmjC-PHD) and catalytic mechanism; the substrate specificity is determined by subtle active-site residue differences not reliably inferable from linear sequence alone.",
    "missing_item_specific_fact": "The specific histone lysine residue (H3K9 vs H3K36) demethylated by this particular JmjC-domain protein, which determines the final two digits of the EC number. This is a protein-specific experimental/biochemical fact not derivable from general domain recognition.",
    "reason": "While general biological knowledge about JmjC-domain proteins can narrow the answer to the 1.14.11.x class and eliminate options C and D, the final choice between 1.14.11.65 and 1.14.11.63 depends on recognizing this specific protein (Drosophila Kdm3) and recalling its experimentally determined substrate specificity (H3K9me2). The domain architectures of KDM3 and KDM4 families are too similar for reliable sequence-based discrimination at the EC sub-subclass level."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 1.14.11.65 (KDM3, H3K9me2 demethylase) and 1.14.11.63 (KDM4B, H3K36me3/me2 demethylase) describe JmjC-domain 2-oxoglutarate-dependent lysine demethylases with similar domain architectures. Without protein-specific substrate data, a knowledgeable model could reasonably assign either EC number based on general JmjC-domain features. The distinction requires item-specific knowledge of which histone residue this particular enzyme targets."
  },
  "important_caveats": [
    "The EC annotation is transferred by similarity (ECO:0000250) from human KDM3A (Q9Y4C1), not from direct experimental characterization of the Drosophila protein.",
    "The sequence match is exact (SHA256 identical) between the benchmark input and UniProt Q9VHC5.",
    "The historical annotation (entry version 180, released Jan 2026) already carried EC 1.14.11.65, so the key was available at the time of benchmark construction.",
    "Options C and D are clearly eliminable by domain recognition, reducing the effective discrimination to a binary A vs B choice that requires protein-specific knowledge."
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

**Accession:** `Q9VHC5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 180. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:18.636093+00:00.  

```json
"Q9VHC5"
```

Source SHA-256: `988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:18.636093+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9Y4C1","source":"UniProtKB"}],"value":"1.14.11.65"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0037703","source":"FlyBase"}],"value":"Lysine-specific demethylase 3"}}}
```

Source SHA-256: `988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:18.636093+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.14.11.65","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9Y4C1","source":"UniProtKB"}],"name":"N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2 CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:60188"},{"database":"Rhea","id":"RHEA-COMP:15541"},{"database":"Rhea","id":"RHEA-COMP:15546"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:16810"},{"database":"ChEBI","id":"CHEBI:16842"},{"database":"ChEBI","id":"CHEBI:29969"},{"database":"ChEBI","id":"CHEBI:30031"},{"database":"ChEBI","id":"CHEBI:61976"}]}}
```

Source SHA-256: `988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 180 / 1.  
**Retrieved:** 2026-11-02T04:33:24.066442+00:00.  

```text
DE   RecName: Full=Lysine-specific demethylase 3 {ECO:0000312|FlyBase:FBgn0037703};
DE            EC=1.14.11.65 {ECO:0000250|UniProtKB:Q9Y4C1};
```

Source SHA-256: `f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180)  
**Locator:** `lines 122-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 180 / 1.  
**Retrieved:** 2026-11-02T04:33:24.066442+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate
CC         + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2
CC         CO2; Xref=Rhea:RHEA:60188, Rhea:RHEA-COMP:15541, Rhea:RHEA-
CC         COMP:15546, ChEBI:CHEBI:15379, ChEBI:CHEBI:16526, ChEBI:CHEBI:16810,
CC         ChEBI:CHEBI:16842, ChEBI:CHEBI:29969, ChEBI:CHEBI:30031,
CC         ChEBI:CHEBI:61976; EC=1.14.11.65;
CC         Evidence={ECO:0000250|UniProtKB:Q9Y4C1};
```

Source SHA-256: `f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 29. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
