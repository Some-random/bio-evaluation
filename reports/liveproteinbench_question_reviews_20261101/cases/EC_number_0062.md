# EC_number_0062

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.7.2.3

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLSNKLAITDVDLKDKRVLIRVDFNVPLDADKKITNNQRIVGALPTIKYAIENGAKAVVLMSHLGRPDGKANPKYSLKPVATELEKLLSKSVIFAENCVGKETEEIVNKATGGQVILLENLRFHAEEEGSSKDAEGKKVKADKEKVEEFRKGLTALGDVYINDAFGTAHRAHSSMVGVDLPQKASGFLVKKELEYFAKALESPQRPFLAILGGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKKTLENVKIGNSLFDEAGSKIVGDIVEKAKKNNVKIVLPVDYVTADKFAADAKTGYATDADGIPDGYMGLDVGEKSVELYKKTIAEAKTILWNGPPGVFELEPFANATKKTLDAAVAAAQSGSIVIIGGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK

[Multiple Choices]
A. 2.7.1.39
B. 2.1.1.348
C. 2.7.2.3
D. 6.3.5.1
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

> The exact sequence matches the UniProt entry annotated as phosphoglycerate kinase, EC 2.7.2.3, with the reaction of 3-phosphoglycerate and ATP also assigned that EC number. The annotation is transferred by similarity from UniProtKB:P00560, so this supports the key but is not direct experimental evidence for this particular protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 417-aa sequence has an overall pattern consistent with the phosphoglycerate kinase family, including a conserved glycine-rich region near the C-terminus (`...SIVIIGGGDTATV...`). That family assignment supports EC 2.7.2.3 and distinguishes it from the unrelated methyltransferase and ligase choices, as well as the distinct kinase in A.


**Missing item-specific fact**

> No external item-specific fact is necessary for a defensible family-level inference from the sequence, though confirming the exact annotation would ordinarily rely on sequence-family or database analysis.


**Reason**

> The sequence provides meaningful family-level evidence for phosphoglycerate kinase rather than requiring memorization of this exact protein's database entry. The inference is not equivalent to direct experimental verification of its reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports the phosphoglycerate kinase family, and the listed EC number for that enzyme is 2.7.2.3.


### Important caveats

- The UniProt EC and catalytic-activity annotations cite transfer by similarity from P00560 (ECO:0000250), not direct experimental evidence for this exact sequence.
- The reviewer-only evidence matches the supplied sequence, but the author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 417-aa sequence has an overall pattern consistent with the phosphoglycerate kinase family, including a conserved glycine-rich region near the C-terminus (`...SIVIIGGGDTATV...`). That family assignment supports EC 2.7.2.3 and distinguishes it from the unrelated methyltransferase and ligase choices, as well as the distinct kinase in A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external item-specific fact is necessary for a defensible family-level inference from the sequence, though confirming the exact annotation would ordinarily rely on sequence-family or database analysis.",
    "reason": "The sequence provides meaningful family-level evidence for phosphoglycerate kinase rather than requiring memorization of this exact protein's database entry. The inference is not equivalent to direct experimental verification of its reaction."
  },
  "case_id": "EC_number_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as phosphoglycerate kinase, EC 2.7.2.3, with the reaction of 3-phosphoglycerate and ATP also assigned that EC number. The annotation is transferred by similarity from UniProtKB:P00560, so this supports the key but is not direct experimental evidence for this particular protein."
  },
  "important_caveats": [
    "The UniProt EC and catalytic-activity annotations cite transfer by similarity from P00560 (ECO:0000250), not direct experimental evidence for this exact sequence.",
    "The reviewer-only evidence matches the supplied sequence, but the author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports the phosphoglycerate kinase family, and the listed EC number for that enzyme is 2.7.2.3."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as phosphoglycerate kinase, EC 2.7.2.3, with the reaction of 3-phosphoglycerate and ATP also assigned that EC number. The annotation is transferred by similarity from UniProtKB:P00560, so this supports the key but is not direct experimental evidence for this particular protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 417-aa sequence has an overall pattern consistent with the phosphoglycerate kinase family, including a conserved glycine-rich region near the C-terminus (`...SIVIIGGGDTATV...`). That family assignment supports EC 2.7.2.3 and distinguishes it from the unrelated methyltransferase and ligase choices, as well as the distinct kinase in A.",
    "missing_item_specific_fact": "No external item-specific fact is necessary for a defensible family-level inference from the sequence, though confirming the exact annotation would ordinarily rely on sequence-family or database analysis.",
    "reason": "The sequence provides meaningful family-level evidence for phosphoglycerate kinase rather than requiring memorization of this exact protein's database entry. The inference is not equivalent to direct experimental verification of its reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports the phosphoglycerate kinase family, and the listed EC number for that enzyme is 2.7.2.3."
  },
  "important_caveats": [
    "The UniProt EC and catalytic-activity annotations cite transfer by similarity from P00560 (ECO:0000250), not direct experimental evidence for this exact sequence.",
    "The reviewer-only evidence matches the supplied sequence, but the author's source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7G5KET3 (PGK1_ASPFN) is annotated as Phosphoglycerate kinase with EC 2.7.2.3, confirmed by both the current entry (C4, C5) and the archived Swiss-Prot record (H1, H2, H4). The sequence matches exactly (417 AA). The annotation is supported by similarity to P00560 (yeast PGK, ECO:0000250) and RuleBase (ECO:0000255), and further corroborated by experimental work (PubMed:37754565, H3) demonstrating PGK1 function in Aspergillus flavus. The catalytic reaction (3-phosphoglycerate + ATP → 3-phosphoglyceroyl phosphate + ADP) is correctly assigned to EC 2.7.2.3.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved PGK signature motif 'GGAKVSDK' (residues ~245-252), the 'WNGPPGVFELE' motif, and the C-terminal 'GGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK' segment, all hallmarks of the phosphoglycerate kinase fold. The two-domain architecture (N-terminal and C-terminal lobes) visible in the sequence is characteristic of PGK. PGK transfers phosphate to the carboxyl group of 3-phosphoglycerate, placing it in sub-subclass 2.7.2 (phosphotransferases with a carboxyl group as acceptor), not 2.7.1 (alcohol group acceptor, Choice A). Choices B (methyltransferase, class 2.1) and D (ligase, class 6) are eliminated by the presence of kinase/transferase motifs and the absence of methyltransferase or ligase signatures.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PGK signature motif 'GGAKVSDK' is one of the most well-known sequence signatures in biochemistry (PROSITE PS00069), and PGK is a textbook glycolytic enzyme. A model with general biochemical knowledge can recognize the PGK fold from these motifs and apply the EC classification logic: phosphotransferase (2.7) → carboxyl group acceptor (2.7.2) → specific enzyme (2.7.2.3). The distinction from 2.7.1.39 relies on knowing PGK phosphorylates a carboxyl group, which is standard biochemical knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices B (methyltransferase) and D (ligase) are eliminated by the obvious kinase/transferase character of the sequence. Choice A (2.7.1.39) is distinguishable from C (2.7.2.3) because the PGK-specific motifs and the carboxyl-group-acceptor mechanism are well-established. No other option is defensible given the sequence evidence.


### Important caveats

- The UniProt annotation is primarily based on similarity to P00560 (yeast PGK, ECO:0000250) and RuleBase (ECO:0000255), not direct experimental kinetics on this specific Aspergillus protein. However, the 2023 MBio paper (H3) provides experimental functional characterization of PGK1 in A. flavus.
- The identity of this protein as PGK relies on recognizing well-known sequence motifs; a model lacking biochemical training would struggle, but this is a knowledge requirement rather than a missing item-specific fact.
- The reviewer-only evidence was absent from the model input; the model must rely on sequence motifs and general biochemistry knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved PGK signature motif 'GGAKVSDK' (residues ~245-252), the 'WNGPPGVFELE' motif, and the C-terminal 'GGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK' segment, all hallmarks of the phosphoglycerate kinase fold. The two-domain architecture (N-terminal and C-terminal lobes) visible in the sequence is characteristic of PGK. PGK transfers phosphate to the carboxyl group of 3-phosphoglycerate, placing it in sub-subclass 2.7.2 (phosphotransferases with a carboxyl group as acceptor), not 2.7.1 (alcohol group acceptor, Choice A). Choices B (methyltransferase, class 2.1) and D (ligase, class 6) are eliminated by the presence of kinase/transferase motifs and the absence of methyltransferase or ligase signatures.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PGK signature motif 'GGAKVSDK' is one of the most well-known sequence signatures in biochemistry (PROSITE PS00069), and PGK is a textbook glycolytic enzyme. A model with general biochemical knowledge can recognize the PGK fold from these motifs and apply the EC classification logic: phosphotransferase (2.7) → carboxyl group acceptor (2.7.2) → specific enzyme (2.7.2.3). The distinction from 2.7.1.39 relies on knowing PGK phosphorylates a carboxyl group, which is standard biochemical knowledge."
  },
  "case_id": "EC_number_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7G5KET3 (PGK1_ASPFN) is annotated as Phosphoglycerate kinase with EC 2.7.2.3, confirmed by both the current entry (C4, C5) and the archived Swiss-Prot record (H1, H2, H4). The sequence matches exactly (417 AA). The annotation is supported by similarity to P00560 (yeast PGK, ECO:0000250) and RuleBase (ECO:0000255), and further corroborated by experimental work (PubMed:37754565, H3) demonstrating PGK1 function in Aspergillus flavus. The catalytic reaction (3-phosphoglycerate + ATP → 3-phosphoglyceroyl phosphate + ADP) is correctly assigned to EC 2.7.2.3."
  },
  "important_caveats": [
    "The UniProt annotation is primarily based on similarity to P00560 (yeast PGK, ECO:0000250) and RuleBase (ECO:0000255), not direct experimental kinetics on this specific Aspergillus protein. However, the 2023 MBio paper (H3) provides experimental functional characterization of PGK1 in A. flavus.",
    "The identity of this protein as PGK relies on recognizing well-known sequence motifs; a model lacking biochemical training would struggle, but this is a knowledge requirement rather than a missing item-specific fact.",
    "The reviewer-only evidence was absent from the model input; the model must rely on sequence motifs and general biochemistry knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B (methyltransferase) and D (ligase) are eliminated by the obvious kinase/transferase character of the sequence. Choice A (2.7.1.39) is distinguishable from C (2.7.2.3) because the PGK-specific motifs and the carboxyl-group-acceptor mechanism are well-established. No other option is defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7G5KET3 (PGK1_ASPFN) is annotated as Phosphoglycerate kinase with EC 2.7.2.3, confirmed by both the current entry (C4, C5) and the archived Swiss-Prot record (H1, H2, H4). The sequence matches exactly (417 AA). The annotation is supported by similarity to P00560 (yeast PGK, ECO:0000250) and RuleBase (ECO:0000255), and further corroborated by experimental work (PubMed:37754565, H3) demonstrating PGK1 function in Aspergillus flavus. The catalytic reaction (3-phosphoglycerate + ATP → 3-phosphoglyceroyl phosphate + ADP) is correctly assigned to EC 2.7.2.3.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved PGK signature motif 'GGAKVSDK' (residues ~245-252), the 'WNGPPGVFELE' motif, and the C-terminal 'GGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK' segment, all hallmarks of the phosphoglycerate kinase fold. The two-domain architecture (N-terminal and C-terminal lobes) visible in the sequence is characteristic of PGK. PGK transfers phosphate to the carboxyl group of 3-phosphoglycerate, placing it in sub-subclass 2.7.2 (phosphotransferases with a carboxyl group as acceptor), not 2.7.1 (alcohol group acceptor, Choice A). Choices B (methyltransferase, class 2.1) and D (ligase, class 6) are eliminated by the presence of kinase/transferase motifs and the absence of methyltransferase or ligase signatures.",
    "missing_item_specific_fact": "",
    "reason": "The PGK signature motif 'GGAKVSDK' is one of the most well-known sequence signatures in biochemistry (PROSITE PS00069), and PGK is a textbook glycolytic enzyme. A model with general biochemical knowledge can recognize the PGK fold from these motifs and apply the EC classification logic: phosphotransferase (2.7) → carboxyl group acceptor (2.7.2) → specific enzyme (2.7.2.3). The distinction from 2.7.1.39 relies on knowing PGK phosphorylates a carboxyl group, which is standard biochemical knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B (methyltransferase) and D (ligase) are eliminated by the obvious kinase/transferase character of the sequence. Choice A (2.7.1.39) is distinguishable from C (2.7.2.3) because the PGK-specific motifs and the carboxyl-group-acceptor mechanism are well-established. No other option is defensible given the sequence evidence."
  },
  "important_caveats": [
    "The UniProt annotation is primarily based on similarity to P00560 (yeast PGK, ECO:0000250) and RuleBase (ECO:0000255), not direct experimental kinetics on this specific Aspergillus protein. However, the 2023 MBio paper (H3) provides experimental functional characterization of PGK1 in A. flavus.",
    "The identity of this protein as PGK relies on recognizing well-known sequence motifs; a model lacking biochemical training would struggle, but this is a knowledge requirement rather than a missing item-specific fact.",
    "The reviewer-only evidence was absent from the model input; the model must rely on sequence motifs and general biochemistry knowledge."
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

**Accession:** `A0A7G5KET3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:35.568831+00:00.  

```json
"A0A7G5KET3"
```

Source SHA-256: `79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:35.568831+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P00560","source":"UniProtKB"}],"value":"2.7.2.3"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU000532","source":"RuleBase"}],"value":"Phosphoglycerate kinase"}}}
```

Source SHA-256: `79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:35.568831+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.2.3","evidences":[{"evidenceCode":"ECO:0000250","id":"P00560","source":"UniProtKB"}],"name":"(2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14801"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:57604"},{"database":"ChEBI","id":"CHEBI:58272"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:37.377118+00:00.  

```text
ID   PGK1_ASPFN              Reviewed;         417 AA.
AC   A0A7G5KET3; B8NIQ9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-FEB-2021, sequence version 1.
DT   28-JAN-2026, entry version 18.
DE   RecName: Full=Phosphoglycerate kinase {ECO:0000255|RuleBase:RU000532};
DE            EC=2.7.2.3 {ECO:0000250|UniProtKB:P00560};
GN   Name=pgk1 {ECO:0000303|PubMed:37754565};
GN   ORFNames=F9C07_8361 {ECO:0000312|EMBL:QRD93909.1};
OS   Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357
OS   / JCM 12722 / SRRC 167).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=332952 {ECO:0000312|Proteomes:UP000596276};
```

Source SHA-256: `b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:37.377118+00:00.  

```text
DE   RecName: Full=Phosphoglycerate kinase {ECO:0000255|RuleBase:RU000532};
DE            EC=2.7.2.3 {ECO:0000250|UniProtKB:P00560};
```

Source SHA-256: `b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)  
**Locator:** `lines 26-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:37.377118+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, PHOSPHORYLATION AT
RP   SER-203, AND MUTAGENESIS OF SER-203.
RX   PubMed=37754565; DOI=10.1128/mbio.00977-23;
RA   Zhu Z., Yang M., Yang G., Zhang B., Cao X., Yuan J., Ge F., Wang S.;
RT   "PP2C phosphatases Ptc1 and Ptc2 dephosphorylate PGK1 to regulate autophagy
RT   and aflatoxin synthesis in the pathogenic fungus Aspergillus flavus.";
RL   MBio 14:e0097723-e0097723(2023).
```

Source SHA-256: `b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)  
**Locator:** `lines 43-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:37.377118+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl
CC         phosphate + ADP; Xref=Rhea:RHEA:14801, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:57604, ChEBI:CHEBI:58272, ChEBI:CHEBI:456216; EC=2.7.2.3;
CC         Evidence={ECO:0000250|UniProtKB:P00560};
```

Source SHA-256: `b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 62. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
