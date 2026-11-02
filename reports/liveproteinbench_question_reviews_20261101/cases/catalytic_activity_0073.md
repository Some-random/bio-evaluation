# catalytic_activity_0073

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATYALSQAHREQMEKSLVDSDPEIAQIMEKEIQRQRESILLIASENVTSRAVFDALGSPMSNKYSEGYPGARYYGGNQHIDAIELTCQARALKAFNLDPEKWGVNVQCLSGSPANLEVYQALMRPHDRLMGLDLPHGGHLSHGYQTPSRKISAVSTYFETFPYRVNTETGIIDYDTLEANAELYRPKCLVAGTSAYCRLIDYGRMRKIADKVGAYLIVDMAHISGLVAAGVIPSPFEYADVVTTTTHKSLRGPRGAMIFFRKGVRSTDPKTGKEIMYDLEGPINFSVFPGHQGGPHNHTITALAVALKQAATPEFRQYQEQVLKNAKALEVEFKALGHKLVSDGTDSHMVLLDLRPKGLDGARVEAVLEQINIACNKNSIPGDKSALTPCGIRIGTPAMTSRGMSEEDFKRVARYIDQVINLCKSIQADLPKEANKLKDFKAKVASGSVPEILALRKEVAEWASTYPLPV

[Multiple Choices]
A. UTP + H2O = UDP + phosphate + H(+)
B. (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine
C. (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)
D. UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-mannosamine
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

> The exact sequence matches the UniProt entry annotated as cytosolic serine hydroxymethyltransferase, with the reaction in choice B. The annotation is supported by a similarity transfer (ECO:0000250), not direct experimental evidence for this specific protein in the cited record.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices are distinct enzymatic reactions, but the supplied sequence and context provide no clear, self-contained basis to identify this particular enzyme's substrate transformation.


**Missing item-specific fact**

> The needed fact is that this sequence is annotated as serine hydroxymethyltransferase, catalyzing the glycine-to-serine reaction with methylene-tetrahydrofolate.


**Reason**

> Identifying the protein family from sequence could aid prediction, but selecting this specific reaction depends on protein-specific functional annotation or equivalent prior knowledge absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reaction choices are chemically distinct, and the matched protein annotation specifically corresponds to choice B.


### Important caveats

- The reviewer-only sources match the supplied sequence, including a historical entry available by the stated cutoff.
- The catalytic-activity annotation cites evidence transferred by similarity from UniProtKB:P34896; it should not be represented as direct experimental validation of this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices are distinct enzymatic reactions, but the supplied sequence and context provide no clear, self-contained basis to identify this particular enzyme's substrate transformation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The needed fact is that this sequence is annotated as serine hydroxymethyltransferase, catalyzing the glycine-to-serine reaction with methylene-tetrahydrofolate.",
    "reason": "Identifying the protein family from sequence could aid prediction, but selecting this specific reaction depends on protein-specific functional annotation or equivalent prior knowledge absent from the input."
  },
  "case_id": "catalytic_activity_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as cytosolic serine hydroxymethyltransferase, with the reaction in choice B. The annotation is supported by a similarity transfer (ECO:0000250), not direct experimental evidence for this specific protein in the cited record."
  },
  "important_caveats": [
    "The reviewer-only sources match the supplied sequence, including a historical entry available by the stated cutoff.",
    "The catalytic-activity annotation cites evidence transferred by similarity from UniProtKB:P34896; it should not be represented as direct experimental validation of this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction choices are chemically distinct, and the matched protein annotation specifically corresponds to choice B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as cytosolic serine hydroxymethyltransferase, with the reaction in choice B. The annotation is supported by a similarity transfer (ECO:0000250), not direct experimental evidence for this specific protein in the cited record.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices are distinct enzymatic reactions, but the supplied sequence and context provide no clear, self-contained basis to identify this particular enzyme's substrate transformation.",
    "missing_item_specific_fact": "The needed fact is that this sequence is annotated as serine hydroxymethyltransferase, catalyzing the glycine-to-serine reaction with methylene-tetrahydrofolate.",
    "reason": "Identifying the protein family from sequence could aid prediction, but selecting this specific reaction depends on protein-specific functional annotation or equivalent prior knowledge absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction choices are chemically distinct, and the matched protein annotation specifically corresponds to choice B."
  },
  "important_caveats": [
    "The reviewer-only sources match the supplied sequence, including a historical entry available by the stated cutoff.",
    "The catalytic-activity annotation cites evidence transferred by similarity from UniProtKB:P34896; it should not be represented as direct experimental validation of this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4WXF4 (sequence exact match, 471 aa) is annotated as 'Serine hydroxymethyltransferase, cytosolic' with EC 2.1.2.1. The catalytic activity comment (C5/H4) states the exact reaction in Choice B: (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine. The EC assignment carries evidence code ECO:0000250 (similarity to P34896, a well-characterized E. coli SHMT), but the protein's function is additionally supported by experimental evidence from PubMed:39825596 (Alharthi et al., Virulence 2025), which reports FUNCTION data for this protein. The expected answer is scientifically supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four choices represent four fundamentally different enzyme classes and folds: (A) a nucleotide phosphatase (requires nucleotide-binding motifs/P-loop), (B) a PLP-dependent amino acid hydroxymethyltransferase, (C) a SAM-dependent methyltransferase (requires Rossmann-like methyltransferase fold and SAM-binding motifs), and (D) a sugar-nucleotide epimerase. The supplied 471-aa sequence lacks nucleotide-binding P-loops or Rossmann folds (ruling out A and C), lacks epimerase signatures (ruling out D), and instead displays features consistent with a fold-type I PLP-dependent enzyme: appropriate length (~470 aa), glycine-rich N-terminal region ('GSPMSNKYSEGYPGARYYGG'), a conserved 'DLPHGGHLSHGY' motif reminiscent of PLP-binding loops in aminotransferase-family enzymes, and internal lysine residues in contexts compatible with the PLP Schiff-base lysine. By elimination of three clearly mismatched enzyme classes and recognition of PLP-dependent enzyme characteristics, Choice B is the only viable option.


**Missing item-specific fact**

> None strictly required; however, positive confirmation of SHMT identity (vs. another PLP enzyme) benefits from recognizing SHMT-specific motifs or database annotation, though the elimination strategy suffices given the extreme divergence of the distractors.


**Reason**

> The distractors belong to entirely different enzyme superfamilies (nucleotide phosphatase, SAM-methyltransferase, sugar epimerase) whose structural and sequence signatures are absent from the input. Identifying the protein as a PLP-dependent enzyme and then selecting the only PLP-dependent amino acid metabolism reaction among the choices constitutes a defensible reasoning path based on general enzymology and fold recognition, without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four unrelated enzyme classes. A PLP-dependent amino acid metabolism enzyme cannot catalyze a nucleotide phosphatase reaction, a SAM-dependent methylation of a spiro compound, or a sugar-nucleotide epimerization. No alternative choice is defensible given the sequence characteristics.


### Important caveats

- The EC 2.1.2.1 assignment carries evidence code ECO:0000250 (transferred by similarity to P34896), meaning the annotation is computational by default; however, PubMed:39825596 provides experimental functional characterization of this specific protein.
- The reasoning path relies primarily on elimination of three clearly mismatched enzyme classes rather than positive motif-level identification of SHMT specifically; a model lacking PLP-enzyme recognition might struggle with positive identification even if elimination is feasible.
- The UniProt entry was first released 2025-06-18; the benchmark construction date is unknown, but the sequence itself (version 1, 2005) predates the annotation, so the sequence was available in databases well before the Swiss-Prot entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices represent four fundamentally different enzyme classes and folds: (A) a nucleotide phosphatase (requires nucleotide-binding motifs/P-loop), (B) a PLP-dependent amino acid hydroxymethyltransferase, (C) a SAM-dependent methyltransferase (requires Rossmann-like methyltransferase fold and SAM-binding motifs), and (D) a sugar-nucleotide epimerase. The supplied 471-aa sequence lacks nucleotide-binding P-loops or Rossmann folds (ruling out A and C), lacks epimerase signatures (ruling out D), and instead displays features consistent with a fold-type I PLP-dependent enzyme: appropriate length (~470 aa), glycine-rich N-terminal region ('GSPMSNKYSEGYPGARYYGG'), a conserved 'DLPHGGHLSHGY' motif reminiscent of PLP-binding loops in aminotransferase-family enzymes, and internal lysine residues in contexts compatible with the PLP Schiff-base lysine. By elimination of three clearly mismatched enzyme classes and recognition of PLP-dependent enzyme characteristics, Choice B is the only viable option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, positive confirmation of SHMT identity (vs. another PLP enzyme) benefits from recognizing SHMT-specific motifs or database annotation, though the elimination strategy suffices given the extreme divergence of the distractors.",
    "reason": "The distractors belong to entirely different enzyme superfamilies (nucleotide phosphatase, SAM-methyltransferase, sugar epimerase) whose structural and sequence signatures are absent from the input. Identifying the protein as a PLP-dependent enzyme and then selecting the only PLP-dependent amino acid metabolism reaction among the choices constitutes a defensible reasoning path based on general enzymology and fold recognition, without requiring memorization of this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXF4 (sequence exact match, 471 aa) is annotated as 'Serine hydroxymethyltransferase, cytosolic' with EC 2.1.2.1. The catalytic activity comment (C5/H4) states the exact reaction in Choice B: (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine. The EC assignment carries evidence code ECO:0000250 (similarity to P34896, a well-characterized E. coli SHMT), but the protein's function is additionally supported by experimental evidence from PubMed:39825596 (Alharthi et al., Virulence 2025), which reports FUNCTION data for this protein. The expected answer is scientifically supported."
  },
  "important_caveats": [
    "The EC 2.1.2.1 assignment carries evidence code ECO:0000250 (transferred by similarity to P34896), meaning the annotation is computational by default; however, PubMed:39825596 provides experimental functional characterization of this specific protein.",
    "The reasoning path relies primarily on elimination of three clearly mismatched enzyme classes rather than positive motif-level identification of SHMT specifically; a model lacking PLP-enzyme recognition might struggle with positive identification even if elimination is feasible.",
    "The UniProt entry was first released 2025-06-18; the benchmark construction date is unknown, but the sequence itself (version 1, 2005) predates the annotation, so the sequence was available in databases well before the Swiss-Prot entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four unrelated enzyme classes. A PLP-dependent amino acid metabolism enzyme cannot catalyze a nucleotide phosphatase reaction, a SAM-dependent methylation of a spiro compound, or a sugar-nucleotide epimerization. No alternative choice is defensible given the sequence characteristics."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXF4 (sequence exact match, 471 aa) is annotated as 'Serine hydroxymethyltransferase, cytosolic' with EC 2.1.2.1. The catalytic activity comment (C5/H4) states the exact reaction in Choice B: (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine. The EC assignment carries evidence code ECO:0000250 (similarity to P34896, a well-characterized E. coli SHMT), but the protein's function is additionally supported by experimental evidence from PubMed:39825596 (Alharthi et al., Virulence 2025), which reports FUNCTION data for this protein. The expected answer is scientifically supported.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four choices represent four fundamentally different enzyme classes and folds: (A) a nucleotide phosphatase (requires nucleotide-binding motifs/P-loop), (B) a PLP-dependent amino acid hydroxymethyltransferase, (C) a SAM-dependent methyltransferase (requires Rossmann-like methyltransferase fold and SAM-binding motifs), and (D) a sugar-nucleotide epimerase. The supplied 471-aa sequence lacks nucleotide-binding P-loops or Rossmann folds (ruling out A and C), lacks epimerase signatures (ruling out D), and instead displays features consistent with a fold-type I PLP-dependent enzyme: appropriate length (~470 aa), glycine-rich N-terminal region ('GSPMSNKYSEGYPGARYYGG'), a conserved 'DLPHGGHLSHGY' motif reminiscent of PLP-binding loops in aminotransferase-family enzymes, and internal lysine residues in contexts compatible with the PLP Schiff-base lysine. By elimination of three clearly mismatched enzyme classes and recognition of PLP-dependent enzyme characteristics, Choice B is the only viable option.",
    "missing_item_specific_fact": "None strictly required; however, positive confirmation of SHMT identity (vs. another PLP enzyme) benefits from recognizing SHMT-specific motifs or database annotation, though the elimination strategy suffices given the extreme divergence of the distractors.",
    "reason": "The distractors belong to entirely different enzyme superfamilies (nucleotide phosphatase, SAM-methyltransferase, sugar epimerase) whose structural and sequence signatures are absent from the input. Identifying the protein as a PLP-dependent enzyme and then selecting the only PLP-dependent amino acid metabolism reaction among the choices constitutes a defensible reasoning path based on general enzymology and fold recognition, without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four unrelated enzyme classes. A PLP-dependent amino acid metabolism enzyme cannot catalyze a nucleotide phosphatase reaction, a SAM-dependent methylation of a spiro compound, or a sugar-nucleotide epimerization. No alternative choice is defensible given the sequence characteristics."
  },
  "important_caveats": [
    "The EC 2.1.2.1 assignment carries evidence code ECO:0000250 (transferred by similarity to P34896), meaning the annotation is computational by default; however, PubMed:39825596 provides experimental functional characterization of this specific protein.",
    "The reasoning path relies primarily on elimination of three clearly mismatched enzyme classes rather than positive motif-level identification of SHMT specifically; a model lacking PLP-enzyme recognition might struggle with positive identification even if elimination is feasible.",
    "The UniProt entry was first released 2025-06-18; the benchmark construction date is unknown, but the sequence itself (version 1, 2005) predates the annotation, so the sequence was available in databases well before the Swiss-Prot entry."
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

**Accession:** `Q4WXF4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 122. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
"Q4WXF4"
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P34896","source":"UniProtKB"}],"value":"2.1.2.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39825596","source":"PubMed"}],"value":"Serine hydroxymethyltransferase, cytosolic"}}}
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.1.2.1","evidences":[{"evidenceCode":"ECO:0000250","id":"P34896","source":"UniProtKB"}],"name":"(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:15481"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15636"},{"database":"ChEBI","id":"CHEBI:33384"},{"database":"ChEBI","id":"CHEBI:57305"},{"database":"ChEBI","id":"CHEBI:57453"}]}}
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
{"citation":{"authors":["Alharthi R.","Sueiro-Olivares M.","Storer I.","Bin Shuraym H.","Scott J.","Al-Shidhani R.","Fortune-Grant R.","Bignell E.","Tabernero L.","Bromley M.","Zhao C.","Amich J."],"citationCrossReferences":[{"database":"PubMed","id":"39825596"},{"database":"DOI","id":"10.1080/21505594.2024.2449075"}],"citationType":"journal article","firstPage":"2449075","id":"39825596","journal":"Virulence","lastPage":"2449075","publicationDate":"2025","title":"The sulfur-related metabolic status of Aspergillus fumigatus during infection reveals cytosolic serine hydroxymethyltransferase as a promising antifungal target.","volume":"16"},"referenceNumber":2,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","INDUCTION","DISRUPTION PHENOTYPE","BIOTECHNOLOGY"]}
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
DE   RecName: Full=Serine hydroxymethyltransferase, cytosolic {ECO:0000303|PubMed:39825596};
DE            EC=2.1.2.1 {ECO:0000250|UniProtKB:P34896};
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 40-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
RN   [2]
RP   FUNCTION, SUBCELLULAR LOCATION, INDUCTION, DISRUPTION PHENOTYPE, AND
RP   BIOTECHNOLOGY.
RX   PubMed=39825596; DOI=10.1080/21505594.2024.2449075;
RA   Alharthi R., Sueiro-Olivares M., Storer I., Bin Shuraym H., Scott J.,
RA   Al-Shidhani R., Fortune-Grant R., Bignell E., Tabernero L., Bromley M.,
RA   Zhao C., Amich J.;
RT   "The sulfur-related metabolic status of Aspergillus fumigatus during
RT   infection reveals cytosolic serine hydroxymethyltransferase as a promising
RT   antifungal target.";
RL   Virulence 16:2449075-2449075(2025).
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 55-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O =
CC         (6S)-5,6,7,8-tetrahydrofolate + L-serine; Xref=Rhea:RHEA:15481,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15636, ChEBI:CHEBI:33384,
CC         ChEBI:CHEBI:57305, ChEBI:CHEBI:57453; EC=2.1.2.1;
CC         Evidence={ECO:0000250|UniProtKB:P34896};
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 73. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
