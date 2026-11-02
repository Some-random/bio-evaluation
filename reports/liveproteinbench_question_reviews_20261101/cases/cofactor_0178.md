# cofactor_0178

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQKELAALVATRTSRKRTISSTSFSISTRTDPKSIIEIHIFNDSLPIKRACCEVENPTLKAEQRVQQEEESLGQVPPLTEEEQQRHDEFRNSGSIFLQDLPCFKLQQAQPIAGSSPIPKCRECRRRNLATTEGEPSSVSDVYCRFYEFRRLQFNENGELCVVGFPNPYSEPSPEDIAIWQPDKNTPPTSGYMDIQVCRYILLHAGDQFCYIWHQEAEALSLHQNTDGTIAWKKAVKGTREICDVCDTTLFNYHWTCRKCGFGVCLDCVKDRKEGLRLRRAENAAQKGCDEYHWLLCSDPSGPQEHVLTELMLTQIIAGDALNVLGRLLHEVRTLWQVPQVCGCLLSKQAIEDAQSKEVIQDMIKESQLKQHTSYSSLASEQKVHQQQRLDQLHATKLEFARELGVDYVPGRVWTKETLGKDPITTAFDNLKHINFLRKGLAGLRRFLPPRTMTFAYSTQLAPGVPHEFLCDGRLLRLTDAMHPDNRVLFQEVWKCGQPVMISEVARSLNLDLWHPQAFCRDFGDKPNDLINCLNGNLVPNQPMRHFWEGFQCMTKRLPDAYGKPMLLKLKDWPPGDDFAEILPTRFADLMKGLPMPEYTLRTGNLNIASCLPKMFVPPDLGPKMYNAYGSALHPDKGTTNLHLDISDAVNIMVYVGIPQDGDTRPQMAATQKAIEIGGCDYITRARCQSPDVLPGALWHIFPARDADKIRDLLNRVTLEKGFRLEPDHDPIHDQNWYLDDKLRARLFKEYGVEGHPIVQCLGDAVFIPAGAPHQVQNLHNCIKVAEDFVSPENITHCYHLTHEFRRLSHSHTNHEDKLQIKNIIYHAIKDCCTILTRAVDERLNAELTKLNAD

[Multiple Choices]
A. Mo-bis(molybdopterin guanine dinucleotide)
B. Zn(2+)
C. Fe(2+)
D. [4Fe-4S] cluster
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies this protein as lysine-specific demethylase 3 and lists Fe(2+) as its cofactor. The annotation is transferred by similarity from Q9Y4C1, rather than direct experimental evidence for this Drosophila sequence; nevertheless, the protein's JmjC demethylase identity is consistent with Fe(II)-dependent catalysis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a recognizable JmjC catalytic-domain pattern, including conserved histidine/aspartate features. JmjC demethylases are Fe(II)- and 2-oxoglutarate-dependent dioxygenases, making Fe(2+) the fitting choice among those offered.


**Missing item-specific fact**

> No item-specific annotation is necessary to make this family-based inference, though confirming the precise protein identity or its experimentally measured cofactor would require external evidence.


**Reason**

> The sequence and choices permit a concrete enzyme-family inference that distinguishes Fe(2+) from Zn(2+), Fe-S cluster, and molybdopterin options. The reviewer-only annotation supports the key but was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> For the listed choices, Fe(2+) is the distinctively appropriate cofactor for a JmjC demethylase; the other options do not fit this catalytic family.


### Important caveats

- The cited database cofactor annotation is similarity-transferred from Q9Y4C1; it is not direct experimental evidence for the supplied Drosophila protein.
- JmjC catalysis also requires 2-oxoglutarate, which is not among the answer choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a recognizable JmjC catalytic-domain pattern, including conserved histidine/aspartate features. JmjC demethylases are Fe(II)- and 2-oxoglutarate-dependent dioxygenases, making Fe(2+) the fitting choice among those offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific annotation is necessary to make this family-based inference, though confirming the precise protein identity or its experimentally measured cofactor would require external evidence.",
    "reason": "The sequence and choices permit a concrete enzyme-family inference that distinguishes Fe(2+) from Zn(2+), Fe-S cluster, and molybdopterin options. The reviewer-only annotation supports the key but was not available to the evaluated model."
  },
  "case_id": "cofactor_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies this protein as lysine-specific demethylase 3 and lists Fe(2+) as its cofactor. The annotation is transferred by similarity from Q9Y4C1, rather than direct experimental evidence for this Drosophila sequence; nevertheless, the protein's JmjC demethylase identity is consistent with Fe(II)-dependent catalysis."
  },
  "important_caveats": [
    "The cited database cofactor annotation is similarity-transferred from Q9Y4C1; it is not direct experimental evidence for the supplied Drosophila protein.",
    "JmjC catalysis also requires 2-oxoglutarate, which is not among the answer choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "For the listed choices, Fe(2+) is the distinctively appropriate cofactor for a JmjC demethylase; the other options do not fit this catalytic family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies this protein as lysine-specific demethylase 3 and lists Fe(2+) as its cofactor. The annotation is transferred by similarity from Q9Y4C1, rather than direct experimental evidence for this Drosophila sequence; nevertheless, the protein's JmjC demethylase identity is consistent with Fe(II)-dependent catalysis.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a recognizable JmjC catalytic-domain pattern, including conserved histidine/aspartate features. JmjC demethylases are Fe(II)- and 2-oxoglutarate-dependent dioxygenases, making Fe(2+) the fitting choice among those offered.",
    "missing_item_specific_fact": "No item-specific annotation is necessary to make this family-based inference, though confirming the precise protein identity or its experimentally measured cofactor would require external evidence.",
    "reason": "The sequence and choices permit a concrete enzyme-family inference that distinguishes Fe(2+) from Zn(2+), Fe-S cluster, and molybdopterin options. The reviewer-only annotation supports the key but was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "For the listed choices, Fe(2+) is the distinctively appropriate cofactor for a JmjC demethylase; the other options do not fit this catalytic family."
  },
  "important_caveats": [
    "The cited database cofactor annotation is similarity-transferred from Q9Y4C1; it is not direct experimental evidence for the supplied Drosophila protein.",
    "JmjC catalysis also requires 2-oxoglutarate, which is not among the answer choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VHC5 (Drosophila melanogaster Lysine-specific demethylase 3, KDM3, EC 1.14.11.65) annotates Fe(2+) as the cofactor (CHEBI:29033, 'Binds 1 Fe(2+) ion per subunit'), with evidence code ECO:0000250 (inferred by similarity from human KDM3A Q9Y4C1). This is a computational/similarity annotation rather than direct experimental evidence on the fly protein, but it is consistent with the well-established biochemistry of the JmjC-domain (JmjC/KDM) family of lysine demethylases, which are Fe(2+)/2-oxoglutarate-dependent dioxygenases. The EC number 1.14.11.65 itself designates a 2-oxoglutarate-dependent dioxygenase, reinforcing Fe(2+) coordination. The answer is scientifically well-supported.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable JmjC-domain region characterized by a 2-His-1-carboxylate facial triad pattern (e.g., the stretch 'HAGDQFCYIWHQEAEALSLHQNTDGTIAWKKAVKGTREICDVCDTTLFNYHWTCRKCGFGVCLDCVKDRKEG' with multiple His residues interspersed with Asp/Glu). JmjC-domain proteins are a textbook class of Fe(2+)/2-oxoglutarate-dependent dioxygenases. This distinguishes Fe(2+) from Zn(2+) (which would be expected in hydrolases or structural zinc-finger contexts), from Mo-bis(molybdopterin) (molybdoenzymes), and from &#91;4Fe-4S&#93; clusters (electron-transfer proteins). While the sequence also contains Cys-rich motifs (PHD fingers, JmjN-like regions), these are structural/zinc-finger-like motifs, not catalytic metal sites. Recognizing the JmjC domain and its Fe(2+) dependence is general biochemistry knowledge.


**Missing item-specific fact**

> None strictly required. The JmjC domain's Fe(2+) requirement is standard enzymology. However, the presence of multiple Cys-rich motifs (e.g., 'RACCEVEN', 'CRECRRR', 'CDVCDTTL', 'CGFGVCLDCV', 'VCGCLLSK') could mislead a model toward Zn(2+) or &#91;4Fe-4S&#93; without domain-level understanding.


**Reason**

> A model with knowledge of JmjC-domain biology can identify the His/Asp-Glu triad pattern in the sequence, recognize the protein as a JmjC-family lysine demethylase, and deduce Fe(2+) as the catalytic cofactor. The distractors (Mo cofactor, Zn, &#91;4Fe-4S&#93;) are eliminable through domain-specific reasoning about which metal-binding motifs serve catalytic versus structural roles. This is general biological reasoning rather than memorizing a single database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the sequence contains Cys-rich motifs that could superficially suggest Zn(2+) or &#91;4Fe-4S&#93;, these correspond to structural domains (PHD fingers, JmjN) rather than catalytic metal sites. The JmjC domain's His/Asp-Glu triad is mechanistically specific to Fe(2+)-dependent dioxygenase chemistry. Mo-bis(molybdopterin) has no plausible binding context in this sequence. The options are distinguishable through domain biology.


### Important caveats

- The UniProt Fe(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from human KDM3A), not direct experimental measurement on the Drosophila protein. However, the JmjC/Fe(2+) relationship is robustly established across the family.
- The sequence contains numerous Cys-rich regions (PHD fingers, JmjN) that could mislead a model lacking domain-level knowledge toward Zn(2+) or &#91;4Fe-4S&#93;.
- The accession Q9VHC5 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must rely solely on the sequence.
- The annotation is a computational transfer from the human homolog; no fly-specific crystallographic or spectroscopic data confirming the single Fe(2+) site per subunit was cited in the evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable JmjC-domain region characterized by a 2-His-1-carboxylate facial triad pattern (e.g., the stretch 'HAGDQFCYIWHQEAEALSLHQNTDGTIAWKKAVKGTREICDVCDTTLFNYHWTCRKCGFGVCLDCVKDRKEG' with multiple His residues interspersed with Asp/Glu). JmjC-domain proteins are a textbook class of Fe(2+)/2-oxoglutarate-dependent dioxygenases. This distinguishes Fe(2+) from Zn(2+) (which would be expected in hydrolases or structural zinc-finger contexts), from Mo-bis(molybdopterin) (molybdoenzymes), and from [4Fe-4S] clusters (electron-transfer proteins). While the sequence also contains Cys-rich motifs (PHD fingers, JmjN-like regions), these are structural/zinc-finger-like motifs, not catalytic metal sites. Recognizing the JmjC domain and its Fe(2+) dependence is general biochemistry knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The JmjC domain's Fe(2+) requirement is standard enzymology. However, the presence of multiple Cys-rich motifs (e.g., 'RACCEVEN', 'CRECRRR', 'CDVCDTTL', 'CGFGVCLDCV', 'VCGCLLSK') could mislead a model toward Zn(2+) or [4Fe-4S] without domain-level understanding.",
    "reason": "A model with knowledge of JmjC-domain biology can identify the His/Asp-Glu triad pattern in the sequence, recognize the protein as a JmjC-family lysine demethylase, and deduce Fe(2+) as the catalytic cofactor. The distractors (Mo cofactor, Zn, [4Fe-4S]) are eliminable through domain-specific reasoning about which metal-binding motifs serve catalytic versus structural roles. This is general biological reasoning rather than memorizing a single database entry."
  },
  "case_id": "cofactor_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VHC5 (Drosophila melanogaster Lysine-specific demethylase 3, KDM3, EC 1.14.11.65) annotates Fe(2+) as the cofactor (CHEBI:29033, 'Binds 1 Fe(2+) ion per subunit'), with evidence code ECO:0000250 (inferred by similarity from human KDM3A Q9Y4C1). This is a computational/similarity annotation rather than direct experimental evidence on the fly protein, but it is consistent with the well-established biochemistry of the JmjC-domain (JmjC/KDM) family of lysine demethylases, which are Fe(2+)/2-oxoglutarate-dependent dioxygenases. The EC number 1.14.11.65 itself designates a 2-oxoglutarate-dependent dioxygenase, reinforcing Fe(2+) coordination. The answer is scientifically well-supported."
  },
  "important_caveats": [
    "The UniProt Fe(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from human KDM3A), not direct experimental measurement on the Drosophila protein. However, the JmjC/Fe(2+) relationship is robustly established across the family.",
    "The sequence contains numerous Cys-rich regions (PHD fingers, JmjN) that could mislead a model lacking domain-level knowledge toward Zn(2+) or [4Fe-4S].",
    "The accession Q9VHC5 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must rely solely on the sequence.",
    "The annotation is a computational transfer from the human homolog; no fly-specific crystallographic or spectroscopic data confirming the single Fe(2+) site per subunit was cited in the evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the sequence contains Cys-rich motifs that could superficially suggest Zn(2+) or [4Fe-4S], these correspond to structural domains (PHD fingers, JmjN) rather than catalytic metal sites. The JmjC domain's His/Asp-Glu triad is mechanistically specific to Fe(2+)-dependent dioxygenase chemistry. Mo-bis(molybdopterin) has no plausible binding context in this sequence. The options are distinguishable through domain biology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VHC5 (Drosophila melanogaster Lysine-specific demethylase 3, KDM3, EC 1.14.11.65) annotates Fe(2+) as the cofactor (CHEBI:29033, 'Binds 1 Fe(2+) ion per subunit'), with evidence code ECO:0000250 (inferred by similarity from human KDM3A Q9Y4C1). This is a computational/similarity annotation rather than direct experimental evidence on the fly protein, but it is consistent with the well-established biochemistry of the JmjC-domain (JmjC/KDM) family of lysine demethylases, which are Fe(2+)/2-oxoglutarate-dependent dioxygenases. The EC number 1.14.11.65 itself designates a 2-oxoglutarate-dependent dioxygenase, reinforcing Fe(2+) coordination. The answer is scientifically well-supported.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable JmjC-domain region characterized by a 2-His-1-carboxylate facial triad pattern (e.g., the stretch 'HAGDQFCYIWHQEAEALSLHQNTDGTIAWKKAVKGTREICDVCDTTLFNYHWTCRKCGFGVCLDCVKDRKEG' with multiple His residues interspersed with Asp/Glu). JmjC-domain proteins are a textbook class of Fe(2+)/2-oxoglutarate-dependent dioxygenases. This distinguishes Fe(2+) from Zn(2+) (which would be expected in hydrolases or structural zinc-finger contexts), from Mo-bis(molybdopterin) (molybdoenzymes), and from [4Fe-4S] clusters (electron-transfer proteins). While the sequence also contains Cys-rich motifs (PHD fingers, JmjN-like regions), these are structural/zinc-finger-like motifs, not catalytic metal sites. Recognizing the JmjC domain and its Fe(2+) dependence is general biochemistry knowledge.",
    "missing_item_specific_fact": "None strictly required. The JmjC domain's Fe(2+) requirement is standard enzymology. However, the presence of multiple Cys-rich motifs (e.g., 'RACCEVEN', 'CRECRRR', 'CDVCDTTL', 'CGFGVCLDCV', 'VCGCLLSK') could mislead a model toward Zn(2+) or [4Fe-4S] without domain-level understanding.",
    "reason": "A model with knowledge of JmjC-domain biology can identify the His/Asp-Glu triad pattern in the sequence, recognize the protein as a JmjC-family lysine demethylase, and deduce Fe(2+) as the catalytic cofactor. The distractors (Mo cofactor, Zn, [4Fe-4S]) are eliminable through domain-specific reasoning about which metal-binding motifs serve catalytic versus structural roles. This is general biological reasoning rather than memorizing a single database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the sequence contains Cys-rich motifs that could superficially suggest Zn(2+) or [4Fe-4S], these correspond to structural domains (PHD fingers, JmjN) rather than catalytic metal sites. The JmjC domain's His/Asp-Glu triad is mechanistically specific to Fe(2+)-dependent dioxygenase chemistry. Mo-bis(molybdopterin) has no plausible binding context in this sequence. The options are distinguishable through domain biology."
  },
  "important_caveats": [
    "The UniProt Fe(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from human KDM3A), not direct experimental measurement on the Drosophila protein. However, the JmjC/Fe(2+) relationship is robustly established across the family.",
    "The sequence contains numerous Cys-rich regions (PHD fingers, JmjN) that could mislead a model lacking domain-level knowledge toward Zn(2+) or [4Fe-4S].",
    "The accession Q9VHC5 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must rely solely on the sequence.",
    "The annotation is a computational transfer from the human homolog; no fly-specific crystallographic or spectroscopic data confirming the single Fe(2+) site per subunit was cited in the evidence."
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
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:18.636093+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29033"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9Y4C1","source":"UniProtKB"}],"name":"Fe(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9Y4C1","source":"UniProtKB"}],"value":"Binds 1 Fe(2+) ion per subunit."}]}}
```

Source SHA-256: `988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 180 / 1.  
**Retrieved:** 2026-11-02T04:33:24.066442+00:00.  

```text
ID   KDM3_DROME              Reviewed;         854 AA.
AC   Q9VHC5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 180.
DE   RecName: Full=Lysine-specific demethylase 3 {ECO:0000312|FlyBase:FBgn0037703};
DE            EC=1.14.11.65 {ECO:0000250|UniProtKB:Q9Y4C1};
GN   Name=Kdm3 {ECO:0000312|FlyBase:FBgn0037703};
GN   Synonyms=JHDM2 {ECO:0000312|FlyBase:FBgn0037703};
GN   ORFNames=CG8165 {ECO:0000312|FlyBase:FBgn0037703};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd`.

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
**Locator:** `lines 130-133`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 180 / 1.  
**Retrieved:** 2026-11-02T04:33:24.066442+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;
CC         Evidence={ECO:0000250|UniProtKB:Q9Y4C1};
CC       Note=Binds 1 Fe(2+) ion per subunit. {ECO:0000250|UniProtKB:Q9Y4C1};
```

Source SHA-256: `f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 178. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
