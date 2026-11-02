# EC_number_0000

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 3.1.3.16

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRTCGTSSEGQDECCLYGLSAMQGWRISMEDAHAAVLDLQAKSTGGSEKPTDPDKRLAFFGVYDGHGGDKVALFAGENVHKIVAKQEAFAKGDIEQALKDGFLATDRAILEDPKYEEEVSGCTAAVSVISKNKIWVANAGDSRSVLGVKGRAKPLSFDHKPQNEGEKARISAAGGFVDFGRVNGNLALSRAIGDFEFKKSPELSPEQQIVTAYPDVTVHEVTDDDEFLVIACDGIWDCQSSQSVVEFVRRGIAAKQELYRICENMMDNCLASNSETGGVGCDNMTMIIIGLLNGKTKEEWYNQISERVANGDGPCAPPEYGKSEFRGPGIRNQFEETPDNYDLENDRSRGFSVRSGRIILLGDGTELIPEQNDEELFDQREENRDVTNHLQHDKAEETSTAANLSESPSSANKNSSGSGTEATEKSASS

[Multiple Choices]
A. 3.1.1.4
B. 1.1.1.336
C. 3.1.3.16
D. 2.7.7.43
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

> The exact sequence matches UniProt entry Q4WTH5, annotated as a protein phosphatase 2C homolog with EC 3.1.3.16. The annotation is supported by transfer from another UniProt entry and a PROSITE rule, rather than evidence here of a direct experimental assay of this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has characteristic PP2C-family phosphatase motifs, including the DGHG-containing region and additional conserved acidic/glycine-rich regions consistent with the metal-dependent phosphatase fold. That supports a protein phosphatase activity (EC 3.1.3.16) over the listed lipase, dehydrogenase, and nucleotidyltransferase activities.


**Missing item-specific fact**

> No direct experimental measurement of this protein's catalytic activity is supplied; the database annotation and its supporting transferred/protein-rule evidence are reviewer-only.


**Reason**

> A family-level functional inference from conserved sequence motifs meaningfully distinguishes the phosphatase choice from the alternatives, without needing to recognize the exact sequence or recall its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed choices describe distinct enzyme activities, and the sequence motifs support the PP2C phosphatase choice.


### Important caveats

- The matching database annotation is not presented as direct experimental validation for this exact protein.
- The annotation cites similarity-based transfer and a PROSITE rule; the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has characteristic PP2C-family phosphatase motifs, including the DGHG-containing region and additional conserved acidic/glycine-rich regions consistent with the metal-dependent phosphatase fold. That supports a protein phosphatase activity (EC 3.1.3.16) over the listed lipase, dehydrogenase, and nucleotidyltransferase activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No direct experimental measurement of this protein's catalytic activity is supplied; the database annotation and its supporting transferred/protein-rule evidence are reviewer-only.",
    "reason": "A family-level functional inference from conserved sequence motifs meaningfully distinguishes the phosphatase choice from the alternatives, without needing to recognize the exact sequence or recall its database entry."
  },
  "case_id": "EC_number_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q4WTH5, annotated as a protein phosphatase 2C homolog with EC 3.1.3.16. The annotation is supported by transfer from another UniProt entry and a PROSITE rule, rather than evidence here of a direct experimental assay of this protein."
  },
  "important_caveats": [
    "The matching database annotation is not presented as direct experimental validation for this exact protein.",
    "The annotation cites similarity-based transfer and a PROSITE rule; the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed choices describe distinct enzyme activities, and the sequence motifs support the PP2C phosphatase choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q4WTH5, annotated as a protein phosphatase 2C homolog with EC 3.1.3.16. The annotation is supported by transfer from another UniProt entry and a PROSITE rule, rather than evidence here of a direct experimental assay of this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has characteristic PP2C-family phosphatase motifs, including the DGHG-containing region and additional conserved acidic/glycine-rich regions consistent with the metal-dependent phosphatase fold. That supports a protein phosphatase activity (EC 3.1.3.16) over the listed lipase, dehydrogenase, and nucleotidyltransferase activities.",
    "missing_item_specific_fact": "No direct experimental measurement of this protein's catalytic activity is supplied; the database annotation and its supporting transferred/protein-rule evidence are reviewer-only.",
    "reason": "A family-level functional inference from conserved sequence motifs meaningfully distinguishes the phosphatase choice from the alternatives, without needing to recognize the exact sequence or recall its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed choices describe distinct enzyme activities, and the sequence motifs support the PP2C phosphatase choice."
  },
  "important_caveats": [
    "The matching database annotation is not presented as direct experimental validation for this exact protein.",
    "The annotation cites similarity-based transfer and a PROSITE rule; the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WTH5 (PP2C2_ASPFU, sequence exactly matched at 429 AA) is annotated with EC 3.1.3.16. The annotation is based on similarity transfer from P39966 (ECO:0000250) and PROSITE-ProRule PP2C domain signature PRU01082 (ECO:0000255). The protein is named 'Protein phosphatase 2C homolog 2' (gene ptcB), and a 2015 Mol. Microbiol. publication (PubMed:25597841) confirms its function as a PtcB phosphatase in the HOG pathway. The EC 3.1.3.16 assignment is consistent with the PP2C domain architecture visible in the sequence (conserved Asp-rich motifs, 'DGIWDC' and 'GDGTE' regions). The annotation is computational/similarity-based rather than direct enzyme kinetics on this specific protein, but the domain-level evidence is solid.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The PP2C domain is recognizable from sequence: it features a metal-dependent (Mn2+/Mg2+) catalytic mechanism with conserved aspartate residues (e.g., the 'DGIWDC' and 'GDGTE' motifs), a ~250–300-residue domain fold, and lacks the Cys-His catalytic motif characteristic of PPP-family phosphatases (PP1/PP2A, EC 3.1.3.16 vs 3.1.3.48). This domain is clearly a phosphomonoesterase acting on protein substrates (EC 3.1.3.x), ruling out 3.1.1.4 (carboxylic-ester hydrolase/phospholipase A), 1.1.1.336 (oxidoreductase, wrong EC class), and 2.7.7.43 (transferase, wrong EC class). Among phosphatase subclasses, the aspartate-rich, metal-dependent PP2C fold specifically maps to EC 3.1.3.16.


**Missing item-specific fact**

> None critical. The PP2C domain signature (PROSITE PRU01082) is a well-known, generalizable sequence pattern. Distinguishing 3.1.3.16 from other 3.1.3.x phosphatases (e.g., PP1/PP2A at 3.1.3.16 vs 3.1.3.48) relies on recognizing the PP2C-specific fold rather than a protein-specific experimental measurement.


**Reason**

> A model with knowledge of protein domain architectures can identify the PP2C domain from conserved motifs in the sequence, then map it to the standard EC classification 3.1.3.16. The three distractors fall in entirely different EC top-level classes (oxidoreductase, transferase) or a different hydrolase sub-subclass (esterase vs phosphomonoesterase), making them distinguishable by recognizing the phosphatase domain. This is generalizable domain-recognition reasoning, not a single-protein lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different EC top-level classes (1, 2, 3) and two different EC second-level classes (3.1.1 vs 3.1.3). Only 3.1.3.16 is consistent with a PP2C-domain protein phosphatase. No other option is defensible for this sequence.


### Important caveats

- The UniProt EC annotation is based on similarity transfer (ECO:0000250 from P39966) and PROSITE-ProRule domain matching (ECO:0000255), not on direct in vitro enzyme kinetics of this specific A. fumigatus protein.
- The PROSITE-ProRule evidence (PRU01082) supports the PP2C domain identification at the fold level; the exact substrate specificity (Ser/Thr protein phosphatase vs. other PP2C substrates) is inferred from homology.
- The reviewer-only evidence confirms the sequence matches Q4WTH5 exactly (SHA256 match, 429 AA), but the accession was inferred from dataset metadata and was not provided to the evaluated model.
- The 2015 publication (PubMed:25597841) describes PtcB as a phosphatase in the HOG pathway in A. fumigatus, providing functional context consistent with EC 3.1.3.16.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The PP2C domain is recognizable from sequence: it features a metal-dependent (Mn2+/Mg2+) catalytic mechanism with conserved aspartate residues (e.g., the 'DGIWDC' and 'GDGTE' motifs), a ~250–300-residue domain fold, and lacks the Cys-His catalytic motif characteristic of PPP-family phosphatases (PP1/PP2A, EC 3.1.3.16 vs 3.1.3.48). This domain is clearly a phosphomonoesterase acting on protein substrates (EC 3.1.3.x), ruling out 3.1.1.4 (carboxylic-ester hydrolase/phospholipase A), 1.1.1.336 (oxidoreductase, wrong EC class), and 2.7.7.43 (transferase, wrong EC class). Among phosphatase subclasses, the aspartate-rich, metal-dependent PP2C fold specifically maps to EC 3.1.3.16.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PP2C domain signature (PROSITE PRU01082) is a well-known, generalizable sequence pattern. Distinguishing 3.1.3.16 from other 3.1.3.x phosphatases (e.g., PP1/PP2A at 3.1.3.16 vs 3.1.3.48) relies on recognizing the PP2C-specific fold rather than a protein-specific experimental measurement.",
    "reason": "A model with knowledge of protein domain architectures can identify the PP2C domain from conserved motifs in the sequence, then map it to the standard EC classification 3.1.3.16. The three distractors fall in entirely different EC top-level classes (oxidoreductase, transferase) or a different hydrolase sub-subclass (esterase vs phosphomonoesterase), making them distinguishable by recognizing the phosphatase domain. This is generalizable domain-recognition reasoning, not a single-protein lookup."
  },
  "case_id": "EC_number_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WTH5 (PP2C2_ASPFU, sequence exactly matched at 429 AA) is annotated with EC 3.1.3.16. The annotation is based on similarity transfer from P39966 (ECO:0000250) and PROSITE-ProRule PP2C domain signature PRU01082 (ECO:0000255). The protein is named 'Protein phosphatase 2C homolog 2' (gene ptcB), and a 2015 Mol. Microbiol. publication (PubMed:25597841) confirms its function as a PtcB phosphatase in the HOG pathway. The EC 3.1.3.16 assignment is consistent with the PP2C domain architecture visible in the sequence (conserved Asp-rich motifs, 'DGIWDC' and 'GDGTE' regions). The annotation is computational/similarity-based rather than direct enzyme kinetics on this specific protein, but the domain-level evidence is solid."
  },
  "important_caveats": [
    "The UniProt EC annotation is based on similarity transfer (ECO:0000250 from P39966) and PROSITE-ProRule domain matching (ECO:0000255), not on direct in vitro enzyme kinetics of this specific A. fumigatus protein.",
    "The PROSITE-ProRule evidence (PRU01082) supports the PP2C domain identification at the fold level; the exact substrate specificity (Ser/Thr protein phosphatase vs. other PP2C substrates) is inferred from homology.",
    "The reviewer-only evidence confirms the sequence matches Q4WTH5 exactly (SHA256 match, 429 AA), but the accession was inferred from dataset metadata and was not provided to the evaluated model.",
    "The 2015 publication (PubMed:25597841) describes PtcB as a phosphatase in the HOG pathway in A. fumigatus, providing functional context consistent with EC 3.1.3.16."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC top-level classes (1, 2, 3) and two different EC second-level classes (3.1.1 vs 3.1.3). Only 3.1.3.16 is consistent with a PP2C-domain protein phosphatase. No other option is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WTH5 (PP2C2_ASPFU, sequence exactly matched at 429 AA) is annotated with EC 3.1.3.16. The annotation is based on similarity transfer from P39966 (ECO:0000250) and PROSITE-ProRule PP2C domain signature PRU01082 (ECO:0000255). The protein is named 'Protein phosphatase 2C homolog 2' (gene ptcB), and a 2015 Mol. Microbiol. publication (PubMed:25597841) confirms its function as a PtcB phosphatase in the HOG pathway. The EC 3.1.3.16 assignment is consistent with the PP2C domain architecture visible in the sequence (conserved Asp-rich motifs, 'DGIWDC' and 'GDGTE' regions). The annotation is computational/similarity-based rather than direct enzyme kinetics on this specific protein, but the domain-level evidence is solid.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The PP2C domain is recognizable from sequence: it features a metal-dependent (Mn2+/Mg2+) catalytic mechanism with conserved aspartate residues (e.g., the 'DGIWDC' and 'GDGTE' motifs), a ~250–300-residue domain fold, and lacks the Cys-His catalytic motif characteristic of PPP-family phosphatases (PP1/PP2A, EC 3.1.3.16 vs 3.1.3.48). This domain is clearly a phosphomonoesterase acting on protein substrates (EC 3.1.3.x), ruling out 3.1.1.4 (carboxylic-ester hydrolase/phospholipase A), 1.1.1.336 (oxidoreductase, wrong EC class), and 2.7.7.43 (transferase, wrong EC class). Among phosphatase subclasses, the aspartate-rich, metal-dependent PP2C fold specifically maps to EC 3.1.3.16.",
    "missing_item_specific_fact": "None critical. The PP2C domain signature (PROSITE PRU01082) is a well-known, generalizable sequence pattern. Distinguishing 3.1.3.16 from other 3.1.3.x phosphatases (e.g., PP1/PP2A at 3.1.3.16 vs 3.1.3.48) relies on recognizing the PP2C-specific fold rather than a protein-specific experimental measurement.",
    "reason": "A model with knowledge of protein domain architectures can identify the PP2C domain from conserved motifs in the sequence, then map it to the standard EC classification 3.1.3.16. The three distractors fall in entirely different EC top-level classes (oxidoreductase, transferase) or a different hydrolase sub-subclass (esterase vs phosphomonoesterase), making them distinguishable by recognizing the phosphatase domain. This is generalizable domain-recognition reasoning, not a single-protein lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC top-level classes (1, 2, 3) and two different EC second-level classes (3.1.1 vs 3.1.3). Only 3.1.3.16 is consistent with a PP2C-domain protein phosphatase. No other option is defensible for this sequence."
  },
  "important_caveats": [
    "The UniProt EC annotation is based on similarity transfer (ECO:0000250 from P39966) and PROSITE-ProRule domain matching (ECO:0000255), not on direct in vitro enzyme kinetics of this specific A. fumigatus protein.",
    "The PROSITE-ProRule evidence (PRU01082) supports the PP2C domain identification at the fold level; the exact substrate specificity (Ser/Thr protein phosphatase vs. other PP2C substrates) is inferred from homology.",
    "The reviewer-only evidence confirms the sequence matches Q4WTH5 exactly (SHA256 match, 429 AA), but the accession was inferred from dataset metadata and was not provided to the evaluated model.",
    "The 2015 publication (PubMed:25597841) describes PtcB as a phosphatase in the HOG pathway in A. fumigatus, providing functional context consistent with EC 3.1.3.16."
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

**Accession:** `Q4WTH5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 119. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
"Q4WTH5"
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Protein phosphatase 2C homolog 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PP2C-2"}]}}
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01082","source":"PROSITE-ProRule"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:47005"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"name":"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:47004"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:61977"}]}}
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
DE   RecName: Full=Protein phosphatase 2C homolog 2 {ECO:0000305};
DE            Short=PP2C-2 {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000250|UniProtKB:P39966};
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 42-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, AND DISRUPTION PHENOTYPE.
RX   PubMed=25597841; DOI=10.1111/mmi.12919;
RA   Winkelstroeter L.K., Bom V.L., de Castro P.A., Ramalho L.N., Goldman M.H.,
RA   Brown N.A., Rajendran R., Ramage G., Bovier E., Dos Reis T.F., Savoldi M.,
RA   Hagiwara D., Goldman G.H.;
RT   "High osmolarity glycerol response PtcB phosphatase is important for
RT   Aspergillus fumigatus virulence.";
RL   Mol. Microbiol. 96:42-54(2015).
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 55-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16; Evidence={ECO:0000255|PROSITE-
CC         ProRule:PRU01082};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000305};
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 63-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:61977; EC=3.1.3.16;
CC         Evidence={ECO:0000250|UniProtKB:P39966};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;
CC         Evidence={ECO:0000250|UniProtKB:P39966};
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
