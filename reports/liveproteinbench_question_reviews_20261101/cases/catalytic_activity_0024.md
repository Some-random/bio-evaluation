# catalytic_activity_0024

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQIKPPYLLFIGDATDKLSIKMAQSLADWRAELCVGELSVNGCTVSTGLNQCSICEAAKLGAKTFVLGFANSGGVLDKKWLPIISEAIENGMNIVSGLHDKLTNFDELVSLSQKHNTNLLDIRHPSTAFATGKGYKRKGKRLLTVGTDCSVGKMYTSLSLEKAMKEQNIDVDFRATGQCGILISGSGVAIDCVIADFISGAAESLSPDAEETHWDIIEGQGSLSHPAFAGVSLGLLHGSQPDALVICHALNRTHMRGLLHTSFPSIETTIELNIAAAKLTNPDVQVVGISVNTSSVSIEQGNEICERLSQTFGVPCVDPLRDGVDSIVANLC

[Multiple Choices]
A. (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O
B. D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)
C. N-acetyl-D-glutamate = N-acetyl-L-glutamate
D. 2-hydroxyspheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
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

> The exact 332-aa sequence matches UniProt entry P0DXZ1, which annotates D-glutamate N-acetyltransferase and gives choice B as a catalytic reaction with ECO:0000269 evidence linked to a publication. This supports the key, though the underlying paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence provides no clear, general biological basis to infer the precise substrate and product in choice B over the other reactions. Identifying a specific enzyme family or homolog could help, but that would require protein-specific identification or external analysis not supplied in the question.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental finding that this enzyme acetylates D-glutamate using acetyl-CoA.


**Reason**

> The keyed reaction is supported by reviewer-only database and publication-linked evidence, but that information is absent from the model input. Recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the supplied sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, B is the reaction supported by the matched-sequence annotation. The entry also annotates acetylation of other D-amino-acid substrates, but those reactions are not listed as choices.


### Important caveats

- The evidence is a database annotation linked to a publication and marked with an experimental evidence code; the primary study was not independently assessed.
- The author’s exact database snapshot is unknown, although the sequence-matched historical entry also supports choice B.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence provides no clear, general biological basis to infer the precise substrate and product in choice B over the other reactions. Identifying a specific enzyme family or homolog could help, but that would require protein-specific identification or external analysis not supplied in the question.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this enzyme acetylates D-glutamate using acetyl-CoA.",
    "reason": "The keyed reaction is supported by reviewer-only database and publication-linked evidence, but that information is absent from the model input. Recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the supplied sequence and choices."
  },
  "case_id": "catalytic_activity_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 332-aa sequence matches UniProt entry P0DXZ1, which annotates D-glutamate N-acetyltransferase and gives choice B as a catalytic reaction with ECO:0000269 evidence linked to a publication. This supports the key, though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The evidence is a database annotation linked to a publication and marked with an experimental evidence code; the primary study was not independently assessed.",
    "The author’s exact database snapshot is unknown, although the sequence-matched historical entry also supports choice B."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B is the reaction supported by the matched-sequence annotation. The entry also annotates acetylation of other D-amino-acid substrates, but those reactions are not listed as choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 332-aa sequence matches UniProt entry P0DXZ1, which annotates D-glutamate N-acetyltransferase and gives choice B as a catalytic reaction with ECO:0000269 evidence linked to a publication. This supports the key, though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence provides no clear, general biological basis to infer the precise substrate and product in choice B over the other reactions. Identifying a specific enzyme family or homolog could help, but that would require protein-specific identification or external analysis not supplied in the question.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this enzyme acetylates D-glutamate using acetyl-CoA.",
    "reason": "The keyed reaction is supported by reviewer-only database and publication-linked evidence, but that information is absent from the model input. Recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the supplied sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B is the reaction supported by the matched-sequence annotation. The entry also annotates acetylation of other D-amino-acid substrates, but those reactions are not listed as choices."
  },
  "important_caveats": [
    "The evidence is a database annotation linked to a publication and marked with an experimental evidence code; the primary study was not independently assessed.",
    "The author’s exact database snapshot is unknown, although the sequence-matched historical entry also supports choice B."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXZ1 (sequence SHA256 match confirmed) annotates this 332-aa protein as D-glutamate N-acetyltransferase (EC 2.3.1.312). The primary catalytic activity is listed as 'D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)', exactly matching choice B. This annotation carries experimental evidence (ECO:0000269, PubMed:36690779, Yu et al. 2023 ISME J.), indicating the reaction was biochemically characterized. The historical entry version 3 (released 2026-01-28) also contains this annotation, confirming it was present well before the benchmark cutoff.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a region 'ISGSGVAID' (~residues 165-173) that is loosely reminiscent of the GNAT (GCN5-related N-acetyltransferase) P-loop motif, which could tentatively suggest an acetyltransferase. Among the four choices, only B is an acetyltransferase reaction; A is a lipoxygenase, C is a racemase/isomerase, and D is a carotenoid hydroxylase. However, the GSG motif is not exclusive to GNATs, the 332-residue length is atypical for a canonical GNAT (~150-250 aa), and the overall fold cannot be confidently assigned from primary sequence alone. Even if one tentatively identifies an acetyltransferase character, the specific substrate (D-glutamate vs. hundreds of other acetyltransferase substrates) cannot be deduced from sequence without database knowledge.


**Missing item-specific fact**

> The specific annotation of this protein as EC 2.3.1.312 (D-glutamate N-acetyltransferase), a novel activity first characterized in 2023 (PubMed:36690779), is the decisive fact. The sequence lacks well-known, unambiguous catalytic motifs that would allow confident identification of this particular enzyme and its D-glutamate substrate specificity from primary sequence alone.


**Reason**

> Identifying this enzyme's catalytic activity requires recognizing a novel GNAT-family member with an unusual substrate (D-glutamate) characterized only in 2023. While the GSG-like motif weakly hints at acetyltransferase activity, this is insufficient to confidently select B over other possibilities without knowing the specific UniProt annotation. The answer depends on item-specific database knowledge rather than generalizable sequence reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent clearly distinct enzyme classes (lipoxygenase, acetyltransferase, racemase, carotenoid hydroxylase). Given the confirmed annotation, only B is correct. Choice C involves N-acetyl-D-glutamate but as a racemase substrate (different reaction type), so it does not create genuine ambiguity with B.


### Important caveats

- The UniProt entry was first public on 2025-04-09, after the 2023 primary publication. The benchmark author may have sourced from the primary paper or an earlier annotation.
- The protein also exhibits activity on D-aspartate and D-glutamine (evidence C6, C7), but the primary/physiological reaction is D-glutamate acetylation, matching choice B.
- The GNAT-fold identification from primary sequence is suggestive but not definitive; the 332-residue length and novel substrate make confident sequence-based reasoning difficult.
- The identity_origin note indicates the accession was inferred from dataset metadata, not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a region 'ISGSGVAID' (~residues 165-173) that is loosely reminiscent of the GNAT (GCN5-related N-acetyltransferase) P-loop motif, which could tentatively suggest an acetyltransferase. Among the four choices, only B is an acetyltransferase reaction; A is a lipoxygenase, C is a racemase/isomerase, and D is a carotenoid hydroxylase. However, the GSG motif is not exclusive to GNATs, the 332-residue length is atypical for a canonical GNAT (~150-250 aa), and the overall fold cannot be confidently assigned from primary sequence alone. Even if one tentatively identifies an acetyltransferase character, the specific substrate (D-glutamate vs. hundreds of other acetyltransferase substrates) cannot be deduced from sequence without database knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific annotation of this protein as EC 2.3.1.312 (D-glutamate N-acetyltransferase), a novel activity first characterized in 2023 (PubMed:36690779), is the decisive fact. The sequence lacks well-known, unambiguous catalytic motifs that would allow confident identification of this particular enzyme and its D-glutamate substrate specificity from primary sequence alone.",
    "reason": "Identifying this enzyme's catalytic activity requires recognizing a novel GNAT-family member with an unusual substrate (D-glutamate) characterized only in 2023. While the GSG-like motif weakly hints at acetyltransferase activity, this is insufficient to confidently select B over other possibilities without knowing the specific UniProt annotation. The answer depends on item-specific database knowledge rather than generalizable sequence reasoning."
  },
  "case_id": "catalytic_activity_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ1 (sequence SHA256 match confirmed) annotates this 332-aa protein as D-glutamate N-acetyltransferase (EC 2.3.1.312). The primary catalytic activity is listed as 'D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)', exactly matching choice B. This annotation carries experimental evidence (ECO:0000269, PubMed:36690779, Yu et al. 2023 ISME J.), indicating the reaction was biochemically characterized. The historical entry version 3 (released 2026-01-28) also contains this annotation, confirming it was present well before the benchmark cutoff."
  },
  "important_caveats": [
    "The UniProt entry was first public on 2025-04-09, after the 2023 primary publication. The benchmark author may have sourced from the primary paper or an earlier annotation.",
    "The protein also exhibits activity on D-aspartate and D-glutamine (evidence C6, C7), but the primary/physiological reaction is D-glutamate acetylation, matching choice B.",
    "The GNAT-fold identification from primary sequence is suggestive but not definitive; the 332-residue length and novel substrate make confident sequence-based reasoning difficult.",
    "The identity_origin note indicates the accession was inferred from dataset metadata, not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent clearly distinct enzyme classes (lipoxygenase, acetyltransferase, racemase, carotenoid hydroxylase). Given the confirmed annotation, only B is correct. Choice C involves N-acetyl-D-glutamate but as a racemase substrate (different reaction type), so it does not create genuine ambiguity with B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ1 (sequence SHA256 match confirmed) annotates this 332-aa protein as D-glutamate N-acetyltransferase (EC 2.3.1.312). The primary catalytic activity is listed as 'D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)', exactly matching choice B. This annotation carries experimental evidence (ECO:0000269, PubMed:36690779, Yu et al. 2023 ISME J.), indicating the reaction was biochemically characterized. The historical entry version 3 (released 2026-01-28) also contains this annotation, confirming it was present well before the benchmark cutoff.",
    "evidence_ids": ["C4", "C5", "C8", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a region 'ISGSGVAID' (~residues 165-173) that is loosely reminiscent of the GNAT (GCN5-related N-acetyltransferase) P-loop motif, which could tentatively suggest an acetyltransferase. Among the four choices, only B is an acetyltransferase reaction; A is a lipoxygenase, C is a racemase/isomerase, and D is a carotenoid hydroxylase. However, the GSG motif is not exclusive to GNATs, the 332-residue length is atypical for a canonical GNAT (~150-250 aa), and the overall fold cannot be confidently assigned from primary sequence alone. Even if one tentatively identifies an acetyltransferase character, the specific substrate (D-glutamate vs. hundreds of other acetyltransferase substrates) cannot be deduced from sequence without database knowledge.",
    "missing_item_specific_fact": "The specific annotation of this protein as EC 2.3.1.312 (D-glutamate N-acetyltransferase), a novel activity first characterized in 2023 (PubMed:36690779), is the decisive fact. The sequence lacks well-known, unambiguous catalytic motifs that would allow confident identification of this particular enzyme and its D-glutamate substrate specificity from primary sequence alone.",
    "reason": "Identifying this enzyme's catalytic activity requires recognizing a novel GNAT-family member with an unusual substrate (D-glutamate) characterized only in 2023. While the GSG-like motif weakly hints at acetyltransferase activity, this is insufficient to confidently select B over other possibilities without knowing the specific UniProt annotation. The answer depends on item-specific database knowledge rather than generalizable sequence reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent clearly distinct enzyme classes (lipoxygenase, acetyltransferase, racemase, carotenoid hydroxylase). Given the confirmed annotation, only B is correct. Choice C involves N-acetyl-D-glutamate but as a racemase substrate (different reaction type), so it does not create genuine ambiguity with B."
  },
  "important_caveats": [
    "The UniProt entry was first public on 2025-04-09, after the 2023 primary publication. The benchmark author may have sourced from the primary paper or an earlier annotation.",
    "The protein also exhibits activity on D-aspartate and D-glutamine (evidence C6, C7), but the primary/physiological reaction is D-glutamate acetylation, matching choice B.",
    "The GNAT-fold identification from primary sequence is suggestive but not definitive; the 332-residue length and novel substrate make confident sequence-based reasoning difficult.",
    "The identity_origin note indicates the accession was inferred from dataset metadata, not provided to the evaluated model."
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

**Accession:** `P0DXZ1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
"P0DXZ1"
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"value":"2.3.1.312"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"D-glutamate N-acetyltransferase"}}}
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:76496"}}],"reaction":{"ecNumber":"2.3.1.312","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"name":"D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:76495"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29986"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:195260"}]}}
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.312","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"name":"D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:76551"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29990"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:195274"}]}}
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.312","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"name":"D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:76547"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:58000"},{"database":"ChEBI","id":"CHEBI:143880"}]}}
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
{"citation":{"authors":["Yu Y.","Wang P.","Cao H.Y.","Teng Z.J.","Zhu Y.","Wang M.","McMinn A.","Chen Y.","Xiang H.","Zhang Y.Z.","Chen X.L.","Zhang Y.Q."],"citationCrossReferences":[{"database":"PubMed","id":"36690779"},{"database":"DOI","id":"10.1038/s41396-023-01364-6"}],"citationType":"journal article","firstPage":"537","id":"36690779","journal":"ISME J.","lastPage":"548","publicationDate":"2023","title":"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.","volume":"17"},"referenceComments":[{"type":"STRAIN","value":"CF6-2"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","INDUCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:00.858326+00:00.  

```text
DE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};
DE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};
```

Source SHA-256: `f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:00.858326+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+);
CC         Xref=Rhea:RHEA:76495, ChEBI:CHEBI:15378, ChEBI:CHEBI:29986,
CC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195260;
CC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:76496;
CC         Evidence={ECO:0000269|PubMed:36690779};
```

Source SHA-256: `f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 24. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
