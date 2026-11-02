# catalytic_activity_0027

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLSNKLAITDVDLKDKRVLIRVDFNVPLDADKKITNNQRIVGALPTIKYAIENGAKAVVLMSHLGRPDGKANPKYSLKPVATELEKLLSKSVIFAENCVGKETEEIVNKATGGQVILLENLRFHAEEEGSSKDAEGKKVKADKEKVEEFRKGLTALGDVYINDAFGTAHRAHSSMVGVDLPQKASGFLVKKELEYFAKALESPQRPFLAILGGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKKTLENVKIGNSLFDEAGSKIVGDIVEKAKKNNVKIVLPVDYVTADKFAADAKTGYATDADGIPDGYMGLDVGEKSVELYKKTIAEAKTILWNGPPGVFELEPFANATKKTLDAAVAAAQSGSIVIIGGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK

[Multiple Choices]
A. ATP + protein L-histidine = ADP + protein N-phospho-L-histidine.
B. L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)
C. (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP
D. (2R,3R,5S)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)
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

> The supplied sequence exactly matches the 417-aa UniProt entry annotated as phosphoglycerate kinase, with reaction C. The annotation is supported by transfer from a reference UniProt protein (ECO:0000250), rather than direct experimental evidence for this exact protein in the supplied evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Reaction C is the characteristic reaction of phosphoglycerate kinase, but the input gives no organism, pathway, enzyme name, or other context tying this sequence to that enzyme. Identifying the sequence as phosphoglycerate kinase requires protein-specific sequence-family recognition or annotation, not a general argument from the reaction choices alone.


**Missing item-specific fact**

> That this sequence is a phosphoglycerate kinase (and therefore is assigned the 3-phosphoglycerate/ATP reaction).


**Reason**

> The sequence is the only possible clue, but the needed link from this particular sequence to an enzyme family is not established by explicit context or a uniquely interpretable sequence feature in the prompt. Knowing the database annotation or recognizing the exact protein would supply that link.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe distinct enzyme reactions; given the phosphoglycerate kinase assignment, choice C is the matching reaction.


### Important caveats

- The sequence match and historical UniProt annotation support the key, but the cited catalytic-activity evidence is transferred from UniProtKB:P00560; it is not direct experimental validation of this exact protein in the supplied evidence.
- The author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Reaction C is the characteristic reaction of phosphoglycerate kinase, but the input gives no organism, pathway, enzyme name, or other context tying this sequence to that enzyme. Identifying the sequence as phosphoglycerate kinase requires protein-specific sequence-family recognition or annotation, not a general argument from the reaction choices alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence is a phosphoglycerate kinase (and therefore is assigned the 3-phosphoglycerate/ATP reaction).",
    "reason": "The sequence is the only possible clue, but the needed link from this particular sequence to an enzyme family is not established by explicit context or a uniquely interpretable sequence feature in the prompt. Knowing the database annotation or recognizing the exact protein would supply that link."
  },
  "case_id": "catalytic_activity_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 417-aa UniProt entry annotated as phosphoglycerate kinase, with reaction C. The annotation is supported by transfer from a reference UniProt protein (ECO:0000250), rather than direct experimental evidence for this exact protein in the supplied evidence."
  },
  "important_caveats": [
    "The sequence match and historical UniProt annotation support the key, but the cited catalytic-activity evidence is transferred from UniProtKB:P00560; it is not direct experimental validation of this exact protein in the supplied evidence.",
    "The author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct enzyme reactions; given the phosphoglycerate kinase assignment, choice C is the matching reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 417-aa UniProt entry annotated as phosphoglycerate kinase, with reaction C. The annotation is supported by transfer from a reference UniProt protein (ECO:0000250), rather than direct experimental evidence for this exact protein in the supplied evidence.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Reaction C is the characteristic reaction of phosphoglycerate kinase, but the input gives no organism, pathway, enzyme name, or other context tying this sequence to that enzyme. Identifying the sequence as phosphoglycerate kinase requires protein-specific sequence-family recognition or annotation, not a general argument from the reaction choices alone.",
    "missing_item_specific_fact": "That this sequence is a phosphoglycerate kinase (and therefore is assigned the 3-phosphoglycerate/ATP reaction).",
    "reason": "The sequence is the only possible clue, but the needed link from this particular sequence to an enzyme family is not established by explicit context or a uniquely interpretable sequence feature in the prompt. Knowing the database annotation or recognizing the exact protein would supply that link."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct enzyme reactions; given the phosphoglycerate kinase assignment, choice C is the matching reaction."
  },
  "important_caveats": [
    "The sequence match and historical UniProt annotation support the key, but the cited catalytic-activity evidence is transferred from UniProtKB:P00560; it is not direct experimental validation of this exact protein in the supplied evidence.",
    "The author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence (417 AA) matches UniProt entry A0A7G5KET3 (PGK1_ASPFN) exactly. The entry is annotated as Phosphoglycerate kinase (EC 2.7.2.3) with the catalytic activity reaction (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP, matching choice C verbatim. The annotation evidence code is ECO:0000250 (similarity-based transfer from P00560, the well-characterized human PGK), supplemented by a RuleBase motif annotation (ECO:0000255). PGK is a universally conserved glycolytic enzyme, and the sequence contains multiple canonical PGK signature motifs (e.g., GGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKK and the C-terminal GGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK), making the annotation highly reliable even though it is not a direct experimental measurement on this specific fungal protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Phosphoglycerate kinase is one of the most conserved and universally taught glycolytic enzymes. The supplied sequence contains multiple well-known PGK signature motifs: the nucleotide-binding/substrate-binding region 'GGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKK' and the C-terminal 'GGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK' are textbook PGK hallmarks present across all domains of life. The four distractors belong to entirely different enzyme classes: (A) a histidine protein kinase, (B) a lysine acetyltransferase, (D) a radical-SAM carbapenam methyltransferase. None of these share sequence architecture with the supplied protein. A model with general biochemistry knowledge of glycolysis and conserved enzyme motifs can distinguish PGK from these unrelated enzyme families without needing to recall a specific database entry.


**Missing item-specific fact**

> None identified. The conserved PGK motifs are part of general biochemistry knowledge, and the distractors are from unrelated enzyme classes with no sequence overlap.


**Reason**

> The question provides a full amino acid sequence containing multiple canonical PGK motifs that are part of standard biochemistry education. The distractors span four unrelated enzyme classes (kinase, acetyltransferase, phosphotransferase, radical-SAM methyltransferase), so general knowledge of glycolytic enzyme architecture and conserved motifs is sufficient to identify the correct answer. This does not require memorizing a specific UniProt accession or obscure annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four distinct enzyme classes with no functional overlap. The PGK motifs in the sequence unambiguously point to a phosphoglycerate kinase. No other choice is plausible given the sequence architecture.


### Important caveats

- The UniProt catalytic activity annotation is evidence-code ECO:0000250 (similarity-based transfer from human PGK P00560), not a direct experimental assay on this Aspergillus flavus protein. However, PGK is among the most conserved enzymes known, and the sequence contains all canonical PGK motifs, making the transfer annotation highly reliable.
- The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical, 417 AA), but the evaluated model had no access to the UniProt annotation; it must rely on sequence motifs and general knowledge.
- The historical entry (version 18, Swiss-Prot) was first released in January 2026; the author's data-construction snapshot is unknown, though the sequence has been stable since version 1 (2021).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Phosphoglycerate kinase is one of the most conserved and universally taught glycolytic enzymes. The supplied sequence contains multiple well-known PGK signature motifs: the nucleotide-binding/substrate-binding region 'GGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKK' and the C-terminal 'GGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK' are textbook PGK hallmarks present across all domains of life. The four distractors belong to entirely different enzyme classes: (A) a histidine protein kinase, (B) a lysine acetyltransferase, (D) a radical-SAM carbapenam methyltransferase. None of these share sequence architecture with the supplied protein. A model with general biochemistry knowledge of glycolysis and conserved enzyme motifs can distinguish PGK from these unrelated enzyme families without needing to recall a specific database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None identified. The conserved PGK motifs are part of general biochemistry knowledge, and the distractors are from unrelated enzyme classes with no sequence overlap.",
    "reason": "The question provides a full amino acid sequence containing multiple canonical PGK motifs that are part of standard biochemistry education. The distractors span four unrelated enzyme classes (kinase, acetyltransferase, phosphotransferase, radical-SAM methyltransferase), so general knowledge of glycolytic enzyme architecture and conserved motifs is sufficient to identify the correct answer. This does not require memorizing a specific UniProt accession or obscure annotation."
  },
  "case_id": "catalytic_activity_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence (417 AA) matches UniProt entry A0A7G5KET3 (PGK1_ASPFN) exactly. The entry is annotated as Phosphoglycerate kinase (EC 2.7.2.3) with the catalytic activity reaction (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP, matching choice C verbatim. The annotation evidence code is ECO:0000250 (similarity-based transfer from P00560, the well-characterized human PGK), supplemented by a RuleBase motif annotation (ECO:0000255). PGK is a universally conserved glycolytic enzyme, and the sequence contains multiple canonical PGK signature motifs (e.g., GGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKK and the C-terminal GGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK), making the annotation highly reliable even though it is not a direct experimental measurement on this specific fungal protein."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation is evidence-code ECO:0000250 (similarity-based transfer from human PGK P00560), not a direct experimental assay on this Aspergillus flavus protein. However, PGK is among the most conserved enzymes known, and the sequence contains all canonical PGK motifs, making the transfer annotation highly reliable.",
    "The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical, 417 AA), but the evaluated model had no access to the UniProt annotation; it must rely on sequence motifs and general knowledge.",
    "The historical entry (version 18, Swiss-Prot) was first released in January 2026; the author's data-construction snapshot is unknown, though the sequence has been stable since version 1 (2021)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes with no functional overlap. The PGK motifs in the sequence unambiguously point to a phosphoglycerate kinase. No other choice is plausible given the sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence (417 AA) matches UniProt entry A0A7G5KET3 (PGK1_ASPFN) exactly. The entry is annotated as Phosphoglycerate kinase (EC 2.7.2.3) with the catalytic activity reaction (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP, matching choice C verbatim. The annotation evidence code is ECO:0000250 (similarity-based transfer from P00560, the well-characterized human PGK), supplemented by a RuleBase motif annotation (ECO:0000255). PGK is a universally conserved glycolytic enzyme, and the sequence contains multiple canonical PGK signature motifs (e.g., GGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKK and the C-terminal GGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK), making the annotation highly reliable even though it is not a direct experimental measurement on this specific fungal protein.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Phosphoglycerate kinase is one of the most conserved and universally taught glycolytic enzymes. The supplied sequence contains multiple well-known PGK signature motifs: the nucleotide-binding/substrate-binding region 'GGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKK' and the C-terminal 'GGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK' are textbook PGK hallmarks present across all domains of life. The four distractors belong to entirely different enzyme classes: (A) a histidine protein kinase, (B) a lysine acetyltransferase, (D) a radical-SAM carbapenam methyltransferase. None of these share sequence architecture with the supplied protein. A model with general biochemistry knowledge of glycolysis and conserved enzyme motifs can distinguish PGK from these unrelated enzyme families without needing to recall a specific database entry.",
    "missing_item_specific_fact": "None identified. The conserved PGK motifs are part of general biochemistry knowledge, and the distractors are from unrelated enzyme classes with no sequence overlap.",
    "reason": "The question provides a full amino acid sequence containing multiple canonical PGK motifs that are part of standard biochemistry education. The distractors span four unrelated enzyme classes (kinase, acetyltransferase, phosphotransferase, radical-SAM methyltransferase), so general knowledge of glycolytic enzyme architecture and conserved motifs is sufficient to identify the correct answer. This does not require memorizing a specific UniProt accession or obscure annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes with no functional overlap. The PGK motifs in the sequence unambiguously point to a phosphoglycerate kinase. No other choice is plausible given the sequence architecture."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation is evidence-code ECO:0000250 (similarity-based transfer from human PGK P00560), not a direct experimental assay on this Aspergillus flavus protein. However, PGK is among the most conserved enzymes known, and the sequence contains all canonical PGK motifs, making the transfer annotation highly reliable.",
    "The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical, 417 AA), but the evaluated model had no access to the UniProt annotation; it must rely on sequence motifs and general knowledge.",
    "The historical entry (version 18, Swiss-Prot) was first released in January 2026; the author's data-construction snapshot is unknown, though the sequence has been stable since version 1 (2021)."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
