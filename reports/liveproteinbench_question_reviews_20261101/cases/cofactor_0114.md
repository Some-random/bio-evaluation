# cofactor_0114

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — pantetheine 4&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSPHISPSKDTPSQRLPIPLSLPTHLGLLAKAYGVPPASILQLAWGLVLRCYFTTSSSRWGTIDMAHEYKEKKNLPIRCEVLELDDTRSIGWILQNWNDPSVHRHLPAEEDTSNVPVSAGSIVILTEDAKDLEVLRDFELTAEWIICFSTSTEKPLLRLSWRPDVIHSELASHLAQLLERALDTTFLSPDIPLSQINLFSILDHQKLLQWNHQYPQSVNRLVHEMFEDMVAARPQATAVAAWDGEVTYQQLDRLSTRLAIKLQTIDLQPESIVALCFEKSVWAIVAMLGVLRAGGAFLHIDPKHPTARQQAMISTTAARIILCSEQTRDTVSRFDSESLSLVVDRKMFAQEPDHKQVALPSPNNLGPRNAAYIVCTSGSTGLPKAIVVEHVSLCTSVTAQAEAMAVGGESRILQYAAYTFDVSVGDVFTALTHGACVCIPSDWERTQDLVGAINRLDVNQACLTSTVASFLTPMNVPKLQKLTLGGEPASKQCIDLWSGKVALKNVYGPAECTVWCVIQKNASSEIPASNIGRGIGARTWIVHPENHNQLMPIGAVGELLIEGPLVARGYLNDAERTTAVFLERAPSWLATFGPLPPQTRFYKTGDLARFEQNGTLFFEGRKDTQVKLRGQRIELGEIEYQIQQACNPVPPLAVELIETKDLQAPLLGAFITWTGGLEISLDQSAVPNGLGPDLDARSHFNELVSRIQANIDRTLPPYMMPGLYIPVQKLPLSTSGKLDRKVLRQYCTQHTRSFLTASEAESSDVIADDATKDDVALHEIVNPGEITLAQLWAHALGRRMESINAKDNFLSLGGDSLAAMRLVNLAARDAQVTLTVANIFESPVLADQARLLRPLSKTKSLAPFELMTRGEASIEDIVGFAAQQCRLLPAQIEDVYPCTPLQEEMMRDSLSNDRTQMGQEVVQISEELDLVRYQVACASVYRRFPILRTRFIEHSGRLVQVVVREDLCWKQPTSLAEYKALDSRERPALGKPLTRWALTSDGTHFILSLHHAMFDGITLGQIQGAIYAVYQCIPLPPPSVSFATFLAHLDDQNAPLSQESQRFWQSYLCPSASLDASITPETQKIDRPRASCGTQRLVQFTSGEVSALQRHGLTEATLVRGAWACTLARHQQKPHASAFSDVIFGTMLTGRNFHLPGVDMLAAPSLTHVPIRIRIDEGDLNGHSARALLARVQADATAMIPYEHDGMNRIRSIEVQTRAVFNRIRTLLVIQPIPEGLTSVSTSPFPGSIVSGPRVEAKEMGHFHWYGLLVECTLLPTKGFFVRVSYDNKMFGTEQVESLLDDYSTTLHTLANGLMDTDIPASLHV

[Multiple Choices]
A. [2Fe-2S] cluster
B. pantetheine 4'-phosphate
C. Co(2+)
D. Fe(2+)
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

> The exact sequence matches the UniProt entry, whose cofactor annotation identifies pantetheine 4'-phosphate. The annotation is supported by a PROSITE-ProRule computational inference, not by the supplied evidence as a direct experimental measurement.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable nonribosomal peptide synthetase adenylation-domain motifs, including the YKTGDL region, consistent with an NRPS. NRPS carrier-protein domains are activated by attachment of a phosphopantetheine group, which distinguishes choice B from the listed metal-ion and iron-sulfur alternatives.


**Missing item-specific fact**

> No external protein-specific fact is strictly needed for this distinction; experimental confirmation of cofactor occupancy is not supplied.


**Reason**

> The sequence offers a biological basis for identifying an NRPS and applying the general requirement for phosphopantetheine-bearing carrier domains. Reviewer-only annotations support the key but are not needed as input for that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the NRPS sequence features and the listed alternatives, pantetheine 4'-phosphate is the defensible choice.


### Important caveats

- The sequence-matched UniProt cofactor annotation is computationally assigned under a PROSITE rule; the evidence provided does not establish direct experimental verification.
- The reviewer-only annotation describes a database claim and should not be treated as information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable nonribosomal peptide synthetase adenylation-domain motifs, including the YKTGDL region, consistent with an NRPS. NRPS carrier-protein domains are activated by attachment of a phosphopantetheine group, which distinguishes choice B from the listed metal-ion and iron-sulfur alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external protein-specific fact is strictly needed for this distinction; experimental confirmation of cofactor occupancy is not supplied.",
    "reason": "The sequence offers a biological basis for identifying an NRPS and applying the general requirement for phosphopantetheine-bearing carrier domains. Reviewer-only annotations support the key but are not needed as input for that inference."
  },
  "case_id": "cofactor_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, whose cofactor annotation identifies pantetheine 4'-phosphate. The annotation is supported by a PROSITE-ProRule computational inference, not by the supplied evidence as a direct experimental measurement."
  },
  "important_caveats": [
    "The sequence-matched UniProt cofactor annotation is computationally assigned under a PROSITE rule; the evidence provided does not establish direct experimental verification.",
    "The reviewer-only annotation describes a database claim and should not be treated as information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the NRPS sequence features and the listed alternatives, pantetheine 4'-phosphate is the defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, whose cofactor annotation identifies pantetheine 4'-phosphate. The annotation is supported by a PROSITE-ProRule computational inference, not by the supplied evidence as a direct experimental measurement.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable nonribosomal peptide synthetase adenylation-domain motifs, including the YKTGDL region, consistent with an NRPS. NRPS carrier-protein domains are activated by attachment of a phosphopantetheine group, which distinguishes choice B from the listed metal-ion and iron-sulfur alternatives.",
    "missing_item_specific_fact": "No external protein-specific fact is strictly needed for this distinction; experimental confirmation of cofactor occupancy is not supplied.",
    "reason": "The sequence offers a biological basis for identifying an NRPS and applying the general requirement for phosphopantetheine-bearing carrier domains. Reviewer-only annotations support the key but are not needed as input for that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the NRPS sequence features and the listed alternatives, pantetheine 4'-phosphate is the defensible choice."
  },
  "important_caveats": [
    "The sequence-matched UniProt cofactor annotation is computationally assigned under a PROSITE rule; the evidence provided does not establish direct experimental verification.",
    "The reviewer-only annotation describes a database claim and should not be treated as information supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) lists pantetheine 4'-phosphate as the cofactor with evidence code ECO:0000255 (inferred by similarity) via PROSITE-ProRule PRU00258. The protein is annotated as a nonribosomal peptide synthetase (NRPS, EC 6.3.2.-). The sequence contains the hallmark PCP (peptidyl carrier protein) domain motif 'GHHAMFDG' (visible in 'SLHHAMFDG'), which is the conserved serine-bearing motif that is post-translationally modified by 4'-phosphopantetheinyl transferase to attach PPT. The evidence is computational (pattern-based inference) rather than direct experimental measurement, but it is well-grounded: PPT is the universal prosthetic group of PCP domains in NRPS enzymes, and the sequence architecture (C-A-PCP multi-domain organization) is consistent with NRPS. The annotation applies to the exact supplied sequence (SHA-256 matched).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved PCP domain signature 'GHHAMFDG' (a well-known NRPS hallmark), along with adenylation-domain-like motifs (e.g., 'CSTSGSTGL') and condensation-domain-like features. A biochemist familiar with NRPS architecture can identify these domain signatures, conclude the protein is a nonribosomal peptide synthetase, and then apply the fundamental biochemical fact that NRPS PCP domains require pantetheine 4'-phosphate (PPT) as their essential cofactor/prosthetic group. The distractors (&#91;2Fe-2S&#93; for electron-transfer proteins, Co(2+) for B12/isomerase enzymes, Fe(2+) for oxidoreductases) are mechanistically incompatible with NRPS thioester-mediated peptide assembly.


**Missing item-specific fact**

> None critical. Recognition of the GHHAMFDG motif and the NRPS→PPT link are standard protein-biochemistry knowledge, not item-specific memorization.


**Reason**

> The sequence provides identifiable domain-level signatures (PCP GHHAMFDG, A-domain and C-domain motifs) that allow a knowledgeable reader to classify the protein as an NRPS and then deduce its cofactor from general NRPS biochemistry. This is a concrete biological reasoning chain, not a lookup of a single protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the protein is identified as an NRPS via its domain architecture, pantetheine 4'-phosphate is the only mechanistically consistent cofactor among the four options. The other three cofactors are associated with entirely different enzyme classes and have no role in NRPS thioester chemistry.


### Important caveats

- The UniProt cofactor annotation carries ECO:0000255 (inferred by similarity / PROSITE-ProRule), meaning it is a computational pattern-based assignment rather than a direct experimental demonstration of PPT attachment on this specific protein.
- The protein was first released in Swiss-Prot in January 2026; the author's exact source snapshot is unknown, but the sequence SHA-256 matches both the current and archived (v4) entries.
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning chain described in answerability_check relies solely on features visible in the supplied sequence and general NRPS biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved PCP domain signature 'GHHAMFDG' (a well-known NRPS hallmark), along with adenylation-domain-like motifs (e.g., 'CSTSGSTGL') and condensation-domain-like features. A biochemist familiar with NRPS architecture can identify these domain signatures, conclude the protein is a nonribosomal peptide synthetase, and then apply the fundamental biochemical fact that NRPS PCP domains require pantetheine 4'-phosphate (PPT) as their essential cofactor/prosthetic group. The distractors ([2Fe-2S] for electron-transfer proteins, Co(2+) for B12/isomerase enzymes, Fe(2+) for oxidoreductases) are mechanistically incompatible with NRPS thioester-mediated peptide assembly.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of the GHHAMFDG motif and the NRPS→PPT link are standard protein-biochemistry knowledge, not item-specific memorization.",
    "reason": "The sequence provides identifiable domain-level signatures (PCP GHHAMFDG, A-domain and C-domain motifs) that allow a knowledgeable reader to classify the protein as an NRPS and then deduce its cofactor from general NRPS biochemistry. This is a concrete biological reasoning chain, not a lookup of a single protein's database entry."
  },
  "case_id": "cofactor_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) lists pantetheine 4'-phosphate as the cofactor with evidence code ECO:0000255 (inferred by similarity) via PROSITE-ProRule PRU00258. The protein is annotated as a nonribosomal peptide synthetase (NRPS, EC 6.3.2.-). The sequence contains the hallmark PCP (peptidyl carrier protein) domain motif 'GHHAMFDG' (visible in 'SLHHAMFDG'), which is the conserved serine-bearing motif that is post-translationally modified by 4'-phosphopantetheinyl transferase to attach PPT. The evidence is computational (pattern-based inference) rather than direct experimental measurement, but it is well-grounded: PPT is the universal prosthetic group of PCP domains in NRPS enzymes, and the sequence architecture (C-A-PCP multi-domain organization) is consistent with NRPS. The annotation applies to the exact supplied sequence (SHA-256 matched)."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries ECO:0000255 (inferred by similarity / PROSITE-ProRule), meaning it is a computational pattern-based assignment rather than a direct experimental demonstration of PPT attachment on this specific protein.",
    "The protein was first released in Swiss-Prot in January 2026; the author's exact source snapshot is unknown, but the sequence SHA-256 matches both the current and archived (v4) entries.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning chain described in answerability_check relies solely on features visible in the supplied sequence and general NRPS biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is identified as an NRPS via its domain architecture, pantetheine 4'-phosphate is the only mechanistically consistent cofactor among the four options. The other three cofactors are associated with entirely different enzyme classes and have no role in NRPS thioester chemistry."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) lists pantetheine 4'-phosphate as the cofactor with evidence code ECO:0000255 (inferred by similarity) via PROSITE-ProRule PRU00258. The protein is annotated as a nonribosomal peptide synthetase (NRPS, EC 6.3.2.-). The sequence contains the hallmark PCP (peptidyl carrier protein) domain motif 'GHHAMFDG' (visible in 'SLHHAMFDG'), which is the conserved serine-bearing motif that is post-translationally modified by 4'-phosphopantetheinyl transferase to attach PPT. The evidence is computational (pattern-based inference) rather than direct experimental measurement, but it is well-grounded: PPT is the universal prosthetic group of PCP domains in NRPS enzymes, and the sequence architecture (C-A-PCP multi-domain organization) is consistent with NRPS. The annotation applies to the exact supplied sequence (SHA-256 matched).",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved PCP domain signature 'GHHAMFDG' (a well-known NRPS hallmark), along with adenylation-domain-like motifs (e.g., 'CSTSGSTGL') and condensation-domain-like features. A biochemist familiar with NRPS architecture can identify these domain signatures, conclude the protein is a nonribosomal peptide synthetase, and then apply the fundamental biochemical fact that NRPS PCP domains require pantetheine 4'-phosphate (PPT) as their essential cofactor/prosthetic group. The distractors ([2Fe-2S] for electron-transfer proteins, Co(2+) for B12/isomerase enzymes, Fe(2+) for oxidoreductases) are mechanistically incompatible with NRPS thioester-mediated peptide assembly.",
    "missing_item_specific_fact": "None critical. Recognition of the GHHAMFDG motif and the NRPS→PPT link are standard protein-biochemistry knowledge, not item-specific memorization.",
    "reason": "The sequence provides identifiable domain-level signatures (PCP GHHAMFDG, A-domain and C-domain motifs) that allow a knowledgeable reader to classify the protein as an NRPS and then deduce its cofactor from general NRPS biochemistry. This is a concrete biological reasoning chain, not a lookup of a single protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is identified as an NRPS via its domain architecture, pantetheine 4'-phosphate is the only mechanistically consistent cofactor among the four options. The other three cofactors are associated with entirely different enzyme classes and have no role in NRPS thioester chemistry."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries ECO:0000255 (inferred by similarity / PROSITE-ProRule), meaning it is a computational pattern-based assignment rather than a direct experimental demonstration of PPT attachment on this specific protein.",
    "The protein was first released in Swiss-Prot in January 2026; the author's exact source snapshot is unknown, but the sequence SHA-256 matches both the current and archived (v4) entries.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning chain described in answerability_check relies solely on features visible in the supplied sequence and general NRPS biochemistry."
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

**Accession:** `P0DXV4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:46.025798+00:00.  

```json
"P0DXV4"
```

Source SHA-256: `6306f5ce87df5ee04db986988c948755e8b2c4fe4ace8282933e84b394cf62fd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:46.025798+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Lanomycin biosynthesis cluster protein 1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"6.3.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Nonribosomal peptide synthetase"}}}
```

Source SHA-256: `6306f5ce87df5ee04db986988c948755e8b2c4fe4ace8282933e84b394cf62fd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:46.025798+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:47942"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00258","source":"PROSITE-ProRule"}],"name":"pantetheine 4'-phosphate"}],"commentType":"COFACTOR"}
```

Source SHA-256: `6306f5ce87df5ee04db986988c948755e8b2c4fe4ace8282933e84b394cf62fd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV4?format=txt&versions=4)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:48.541613+00:00.  

```text
DE   RecName: Full=Nonribosomal peptide synthetase {ECO:0000303|PubMed:33857369};
DE            EC=6.3.2.- {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Lanomycin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};
```

Source SHA-256: `ba16325a29b0d20c33cbeceb3d33ee2d578da70c3cbda9228dab9fae89b8c8fd`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV4?format=txt&versions=4)  
**Locator:** `lines 34-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:48.541613+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00258};
```

Source SHA-256: `ba16325a29b0d20c33cbeceb3d33ee2d578da70c3cbda9228dab9fae89b8c8fd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 114. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
