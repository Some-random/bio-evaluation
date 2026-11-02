# catalytic_activity_0134

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — L-aspartate + ATP = 4-phospho-L-aspartate + ADP

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSASTPTAPYLEDLVRNSLDQNLPWVVQKYGGTSVGKSLDNITKIVGSYIDNGSKVAIVCSARSTQTKSLGTTNLLLQASREALQPAMSSSGDGRSGSMSGTATPFYPKRVGSGFFGKDQSTSMTSSVSSLSQLESQLGRSGSPSPFQSSSSRSPPRSPATPSQDSSISQEPAFHATVDLIKKGHLEAARASLKGGPLRDELEEEIERDCESLRSFLYAAQIIDEISPRSQDSIVGTGERLACKIVAAALRDRGVDSELVVLDNIVDASMSAASEAVSVDAGDQGVAQLGQEFYDQLSFRLGERLRECGQRVPVVTGYFGPVPGSLLAQIGRGYTDLCAALCAVGLKASELQVWKEVDGIFTADPRKVPSARLVPIITPDEAAELTYYGSEVIHPFTMEQVIRARIPIRIKNVENPSGAGTVIYPDVGFPRGLDTEPPKAERIVEGVDERMPTAVTIKDEIIVLNIHSNRKTLSHGFLARIFGTLDRAGVVVDLISTSEVHVSMAMQDFLNRKRLERLVKDLEKIGEVTVSKDMAILSLVGRNMRNAIGSAGLMFASLARAMINIEMISQGASEINISCVIENKDAIKALNVIHESCLSYPRSPATEMAGLQLQ

[Multiple Choices]
A. (sulfur carrier)-H + L-cysteine = (sulfur carrier)-SH + L-alanine
B. L-aspartate + ATP = 4-phospho-L-aspartate + ADP
C. a 14alpha-methyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
D. L-proline betaine + NADPH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NADP(+) + H2O
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

> The exact sequence matches a UniProt entry annotated as aspartokinase, with the reaction in choice B. The annotation assigns the EC number and catalytic activity by similarity to another UniProt entry, so this supports B as a database-based inference, not as direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice B is the only ATP-dependent phosphorylation, and the sequence may be compatible with a kinase. But the supplied input does not establish that aspartate is the substrate or identify the specific kinase activity.


**Missing item-specific fact**

> The protein-specific assignment of this sequence as an aspartokinase, including the reaction transferred by similarity from another entry.


**Reason**

> Choosing the precise reaction depends on a protein-specific functional annotation or equivalent homology evidence not supplied in the question; merely recognizing the sequence or using a predictor would not make the distinction reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports choice B, and the listed reactions describe distinct enzyme activities.


### Important caveats

- The reviewer-only annotation matches the sequence but was absent from the evaluated model input.
- The catalytic-activity evidence is transferred by similarity (ECO:0000250), not direct experimental validation of the reaction for this sequence.
- The author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice B is the only ATP-dependent phosphorylation, and the sequence may be compatible with a kinase. But the supplied input does not establish that aspartate is the substrate or identify the specific kinase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of this sequence as an aspartokinase, including the reaction transferred by similarity from another entry.",
    "reason": "Choosing the precise reaction depends on a protein-specific functional annotation or equivalent homology evidence not supplied in the question; merely recognizing the sequence or using a predictor would not make the distinction reasoning-supported."
  },
  "case_id": "catalytic_activity_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as aspartokinase, with the reaction in choice B. The annotation assigns the EC number and catalytic activity by similarity to another UniProt entry, so this supports B as a database-based inference, not as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the sequence but was absent from the evaluated model input.",
    "The catalytic-activity evidence is transferred by similarity (ECO:0000250), not direct experimental validation of the reaction for this sequence.",
    "The author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports choice B, and the listed reactions describe distinct enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as aspartokinase, with the reaction in choice B. The annotation assigns the EC number and catalytic activity by similarity to another UniProt entry, so this supports B as a database-based inference, not as direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice B is the only ATP-dependent phosphorylation, and the sequence may be compatible with a kinase. But the supplied input does not establish that aspartate is the substrate or identify the specific kinase activity.",
    "missing_item_specific_fact": "The protein-specific assignment of this sequence as an aspartokinase, including the reaction transferred by similarity from another entry.",
    "reason": "Choosing the precise reaction depends on a protein-specific functional annotation or equivalent homology evidence not supplied in the question; merely recognizing the sequence or using a predictor would not make the distinction reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports choice B, and the listed reactions describe distinct enzyme activities."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the sequence but was absent from the evaluated model input.",
    "The catalytic-activity evidence is transferred by similarity (ECO:0000250), not direct experimental validation of the reaction for this sequence.",
    "The author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry J9VS37 (sequence matched, 615 AA) annotates this protein as Aspartokinase (EC 2.7.2.4) with the catalytic reaction 'L-aspartate + ATP = 4-phospho-L-aspartate + ADP' (evidence codes C4, C5, H2, H4). The annotation is based on similarity (ECO:0000250 to P10869, the yeast aspartokinase), but the gene name HOM3 and the PubMed reference (18757810) on threonine biosynthetic genes in C. neoformans provide experimental context consistent with aspartokinase function. The expected answer B matches the annotated reaction exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four choices represent four very different enzyme classes: (A) a PLP-dependent cysteine desulfurase (~400 AA, requires PLP-binding motifs and a catalytic Cys), (C) a cytochrome P450 steroid 14α-demethylase (requires the canonical heme-binding motif FGxGxRxCxG), (D) an N-demethylase/FMO-type oxidase, and (B) an amino acid kinase. The 615-AA sequence lacks the P450 heme-binding signature (no FGxGxRxCxG), lacks PLP-binding motifs characteristic of cysteine desulfurases, and lacks FMO/demethylase architecture. Instead, the sequence size and internal motifs (e.g., 'AIGSAG' region, nucleotide-binding-like stretches) are consistent with the amino acid kinase family. Since B is the only kinase option, elimination of the other three enzyme classes by absence of their hallmark motifs, combined with positive recognition of amino acid kinase family features, provides a reasoning pathway to select B.


**Missing item-specific fact**

> Precise identification as aspartokinase specifically (rather than glutamate 5-kinase or N-acetylglutamate kinase, also amino acid kinase family members) would require recognizing the aspartate-binding sub-motif. However, since B is the sole kinase among the four choices, the broader family-level recognition suffices to distinguish the answer.


**Reason**

> The distractors span entirely different enzyme classes (P450, PLP-dependent desulfurase, FMO-type demethylase) whose diagnostic motifs are absent from the sequence, while the sequence is consistent with an amino acid kinase. This provides a concrete, general biological reasoning pathway to eliminate A, C, and D and select B without needing to memorize the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices belong to four distinct enzyme classes with well-defined structural signatures. The sequence clearly lacks P450 heme-binding motifs (eliminates C), PLP-binding motifs (eliminates A), and FMO/demethylase features (eliminates D). Only B (amino acid kinase) is consistent with the observed sequence architecture and size.


### Important caveats

- The UniProt annotation for J9VS37 is based on similarity (ECO:0000250 to P10869), not direct experimental enzymatic assay. The PubMed reference (18757810) supports the gene's role in threonine biosynthesis but does not necessarily constitute a purified-enzyme kinetics study.
- The sequence-to-accession match was confirmed by the reviewer (615 AA, SHA256 match), but the evaluated model received only the raw sequence without any database identifier.
- The reasoning pathway relies on recognizing the absence of P450/PLP/FMO motifs and the presence of amino acid kinase family features; a model unfamiliar with these motif signatures would struggle.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices represent four very different enzyme classes: (A) a PLP-dependent cysteine desulfurase (~400 AA, requires PLP-binding motifs and a catalytic Cys), (C) a cytochrome P450 steroid 14α-demethylase (requires the canonical heme-binding motif FGxGxRxCxG), (D) an N-demethylase/FMO-type oxidase, and (B) an amino acid kinase. The 615-AA sequence lacks the P450 heme-binding signature (no FGxGxRxCxG), lacks PLP-binding motifs characteristic of cysteine desulfurases, and lacks FMO/demethylase architecture. Instead, the sequence size and internal motifs (e.g., 'AIGSAG' region, nucleotide-binding-like stretches) are consistent with the amino acid kinase family. Since B is the only kinase option, elimination of the other three enzyme classes by absence of their hallmark motifs, combined with positive recognition of amino acid kinase family features, provides a reasoning pathway to select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification as aspartokinase specifically (rather than glutamate 5-kinase or N-acetylglutamate kinase, also amino acid kinase family members) would require recognizing the aspartate-binding sub-motif. However, since B is the sole kinase among the four choices, the broader family-level recognition suffices to distinguish the answer.",
    "reason": "The distractors span entirely different enzyme classes (P450, PLP-dependent desulfurase, FMO-type demethylase) whose diagnostic motifs are absent from the sequence, while the sequence is consistent with an amino acid kinase. This provides a concrete, general biological reasoning pathway to eliminate A, C, and D and select B without needing to memorize the specific UniProt entry."
  },
  "case_id": "catalytic_activity_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry J9VS37 (sequence matched, 615 AA) annotates this protein as Aspartokinase (EC 2.7.2.4) with the catalytic reaction 'L-aspartate + ATP = 4-phospho-L-aspartate + ADP' (evidence codes C4, C5, H2, H4). The annotation is based on similarity (ECO:0000250 to P10869, the yeast aspartokinase), but the gene name HOM3 and the PubMed reference (18757810) on threonine biosynthetic genes in C. neoformans provide experimental context consistent with aspartokinase function. The expected answer B matches the annotated reaction exactly."
  },
  "important_caveats": [
    "The UniProt annotation for J9VS37 is based on similarity (ECO:0000250 to P10869), not direct experimental enzymatic assay. The PubMed reference (18757810) supports the gene's role in threonine biosynthesis but does not necessarily constitute a purified-enzyme kinetics study.",
    "The sequence-to-accession match was confirmed by the reviewer (615 AA, SHA256 match), but the evaluated model received only the raw sequence without any database identifier.",
    "The reasoning pathway relies on recognizing the absence of P450/PLP/FMO motifs and the presence of amino acid kinase family features; a model unfamiliar with these motif signatures would struggle."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices belong to four distinct enzyme classes with well-defined structural signatures. The sequence clearly lacks P450 heme-binding motifs (eliminates C), PLP-binding motifs (eliminates A), and FMO/demethylase features (eliminates D). Only B (amino acid kinase) is consistent with the observed sequence architecture and size."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry J9VS37 (sequence matched, 615 AA) annotates this protein as Aspartokinase (EC 2.7.2.4) with the catalytic reaction 'L-aspartate + ATP = 4-phospho-L-aspartate + ADP' (evidence codes C4, C5, H2, H4). The annotation is based on similarity (ECO:0000250 to P10869, the yeast aspartokinase), but the gene name HOM3 and the PubMed reference (18757810) on threonine biosynthetic genes in C. neoformans provide experimental context consistent with aspartokinase function. The expected answer B matches the annotated reaction exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four choices represent four very different enzyme classes: (A) a PLP-dependent cysteine desulfurase (~400 AA, requires PLP-binding motifs and a catalytic Cys), (C) a cytochrome P450 steroid 14α-demethylase (requires the canonical heme-binding motif FGxGxRxCxG), (D) an N-demethylase/FMO-type oxidase, and (B) an amino acid kinase. The 615-AA sequence lacks the P450 heme-binding signature (no FGxGxRxCxG), lacks PLP-binding motifs characteristic of cysteine desulfurases, and lacks FMO/demethylase architecture. Instead, the sequence size and internal motifs (e.g., 'AIGSAG' region, nucleotide-binding-like stretches) are consistent with the amino acid kinase family. Since B is the only kinase option, elimination of the other three enzyme classes by absence of their hallmark motifs, combined with positive recognition of amino acid kinase family features, provides a reasoning pathway to select B.",
    "missing_item_specific_fact": "Precise identification as aspartokinase specifically (rather than glutamate 5-kinase or N-acetylglutamate kinase, also amino acid kinase family members) would require recognizing the aspartate-binding sub-motif. However, since B is the sole kinase among the four choices, the broader family-level recognition suffices to distinguish the answer.",
    "reason": "The distractors span entirely different enzyme classes (P450, PLP-dependent desulfurase, FMO-type demethylase) whose diagnostic motifs are absent from the sequence, while the sequence is consistent with an amino acid kinase. This provides a concrete, general biological reasoning pathway to eliminate A, C, and D and select B without needing to memorize the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices belong to four distinct enzyme classes with well-defined structural signatures. The sequence clearly lacks P450 heme-binding motifs (eliminates C), PLP-binding motifs (eliminates A), and FMO/demethylase features (eliminates D). Only B (amino acid kinase) is consistent with the observed sequence architecture and size."
  },
  "important_caveats": [
    "The UniProt annotation for J9VS37 is based on similarity (ECO:0000250 to P10869), not direct experimental enzymatic assay. The PubMed reference (18757810) supports the gene's role in threonine biosynthesis but does not necessarily constitute a purified-enzyme kinetics study.",
    "The sequence-to-accession match was confirmed by the reviewer (615 AA, SHA256 match), but the evaluated model received only the raw sequence without any database identifier.",
    "The reasoning pathway relies on recognizing the absence of P450/PLP/FMO motifs and the presence of amino acid kinase family features; a model unfamiliar with these motif signatures would struggle."
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

**Accession:** `J9VS37` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 66. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
"J9VS37"
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"value":"2.7.2.4"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartokinase"}}}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23777"}}],"reaction":{"ecNumber":"2.7.2.4","evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"name":"L-aspartate + ATP = 4-phospho-L-aspartate + ADP","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23776"},{"database":"ChEBI","id":"CHEBI:29991"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
DE   RecName: Full=Aspartokinase {ECO:0000305};
DE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 35-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.
RX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;
RA   Kingsbury J.M., McCusker J.H.;
RT   "Threonine biosynthetic genes are essential in Cryptococcus neoformans.";
RL   Microbiology 154:2767-2775(2008).
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 45-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;
CC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;
CC         Evidence={ECO:0000250|UniProtKB:P10869};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;
CC         Evidence={ECO:0000250|UniProtKB:P10869};
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
