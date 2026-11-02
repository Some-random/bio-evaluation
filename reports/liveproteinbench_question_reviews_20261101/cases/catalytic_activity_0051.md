# catalytic_activity_0051

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLQPTATEVGTMYDQYTSLLTDVMAGFIHVGYWDDPEREDTIEVATERLTREIGERLSSVRGQRILDVGCGTGKSAVQIATAHDVHITGITVSNHQIELAQSQYESNTKAGQVNFLFANAMDLPFADASFDGAYAIESLVHMDDRRTALTNIARVLRPGSRLAIADLFLDAGCPNPEVLARFHELFQVPPMPSGDDLKALLHQTGFKVIEFTDIRDTSGLSANF

[Multiple Choices]
A. desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)
B. 3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = mescaline + S-adenosyl-L-homocysteine + H(+)
C. GTP + H2O = GDP + phosphate + H(+)
D. luteothin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = aureothin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O
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

> The exact input sequence matches the UniProt entry whose catalytic-activity annotation gives reaction A and cites PubMed evidence code ECO:0000269. The same reaction is present in the archived entry, so this is not merely a current annotation added after the historical cutoff. The evidence supports the key, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may permit a broad inference of an enzyme class, but that would not establish its specific substrate or distinguish the two SAM-dependent methylation reactions in A and B.


**Missing item-specific fact**

> The enzyme's experimentally characterized substrate specificity—specifically, that it methylates desmethylrestrictinol to form restrictinol—is not supplied in the question.


**Reason**

> Selecting A requires a protein-specific functional annotation or experimental result absent from the sequence and choices; recognizing the exact sequence from memory would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A and B describe SAM-dependent methylation. The supplied sequence and context do not provide a defensible basis to distinguish their substrate specificities, even though reviewer-only evidence supports A.


### Important caveats

- The source annotation is sequence-matched and cites experimental evidence, but the cited primary study was not independently validated in this review.
- Reviewer-only database evidence supports the expected answer but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may permit a broad inference of an enzyme class, but that would not establish its specific substrate or distinguish the two SAM-dependent methylation reactions in A and B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's experimentally characterized substrate specificity—specifically, that it methylates desmethylrestrictinol to form restrictinol—is not supplied in the question.",
    "reason": "Selecting A requires a protein-specific functional annotation or experimental result absent from the sequence and choices; recognizing the exact sequence from memory would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "catalytic_activity_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact input sequence matches the UniProt entry whose catalytic-activity annotation gives reaction A and cites PubMed evidence code ECO:0000269. The same reaction is present in the archived entry, so this is not merely a current annotation added after the historical cutoff. The evidence supports the key, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The source annotation is sequence-matched and cites experimental evidence, but the cited primary study was not independently validated in this review.",
    "Reviewer-only database evidence supports the expected answer but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A and B describe SAM-dependent methylation. The supplied sequence and context do not provide a defensible basis to distinguish their substrate specificities, even though reviewer-only evidence supports A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact input sequence matches the UniProt entry whose catalytic-activity annotation gives reaction A and cites PubMed evidence code ECO:0000269. The same reaction is present in the archived entry, so this is not merely a current annotation added after the historical cutoff. The evidence supports the key, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may permit a broad inference of an enzyme class, but that would not establish its specific substrate or distinguish the two SAM-dependent methylation reactions in A and B.",
    "missing_item_specific_fact": "The enzyme's experimentally characterized substrate specificity—specifically, that it methylates desmethylrestrictinol to form restrictinol—is not supplied in the question.",
    "reason": "Selecting A requires a protein-specific functional annotation or experimental result absent from the sequence and choices; recognizing the exact sequence from memory would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A and B describe SAM-dependent methylation. The supplied sequence and context do not provide a defensible basis to distinguish their substrate specificities, even though reviewer-only evidence supports A."
  },
  "important_caveats": [
    "The source annotation is sequence-matched and cites experimental evidence, but the cited primary study was not independently validated in this review.",
    "Reviewer-only database evidence supports the expected answer but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence (225 aa) matches UniProt entry A0A0L1JF88 (RSTN1_ASPN3) exactly. The entry is annotated as 'O-methyltransferase rstn1' (EC 2.1.1.-) with the catalytic activity explicitly stated as 'desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)' under evidence code ECO:0000269 (inferred from direct assay, PubMed:33857369, Liu et al. JACS 2021). This is experimental evidence, not mere computational inference. Both the current and historical (v23) entries confirm the same reaction. The expected answer Choice A matches this annotation verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a GCGTGKSA motif characteristic of SAM-binding methyltransferases, which allows elimination of Choice C (GTPase, no GTP-binding P-loop) and Choice D (ferredoxin-dependent P450, no heme-binding FGAGPRPCG motif). However, both remaining choices A and B are SAM-dependent methyltransferase reactions. Distinguishing an O-methyltransferase acting on desmethylrestrictinol (A) from an N-methyltransferase acting on 3-hydroxy-4,5-dimethoxyphenethylamine (B) requires knowledge of the specific active-site architecture and substrate-binding pocket, which cannot be reliably inferred from the primary sequence alone through general biological reasoning.


**Missing item-specific fact**

> The specific substrate identity (desmethylrestrictinol vs. 3-hydroxy-4,5-dimethoxyphenethylamine) and the regiochemistry of methylation (O- vs. N-methylation) are protein-specific facts derived from experimental characterization (Liu et al. 2021) and database annotation. No general sequence feature in the provided 225-aa sequence distinguishes these two methyltransferase substrates.


**Reason**

> While the SAM-binding motif narrows the answer to a methyltransferase (eliminating C and D), the final choice between A and B depends entirely on knowing the specific biosynthetic pathway (restricticin) and substrate of this particular protein. This is an item-specific annotation fact, not derivable from general biological principles applied to the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A and B describe SAM-dependent methyltransferase reactions. The GCGTGK motif in the sequence supports a methyltransferase classification but does not specify O- vs. N-methylation or identify the particular substrate. Without database lookup or prior knowledge of the restricticin biosynthetic pathway, a knowledgeable model could reasonably select B as well.


### Important caveats

- The annotation evidence code ECO:0000269 indicates experimental (direct assay) support from Liu et al. 2021 (JACS), not computational prediction, strengthening the expected-answer check.
- The identity origin note states the accession was inferred from dataset image-path metadata, not from the evaluated model input; the model receives only the raw sequence.
- The entry was first public in Swiss-Prot on 2025-02-05; depending on the author's data-construction date, this annotation may or may not have been available to the model's training data.
- The EC number is listed as 2.1.1.- (unassigned subclass), meaning the specific methyltransferase sub-class is not yet formally assigned, further underscoring the lookup dependence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GCGTGKSA motif characteristic of SAM-binding methyltransferases, which allows elimination of Choice C (GTPase, no GTP-binding P-loop) and Choice D (ferredoxin-dependent P450, no heme-binding FGAGPRPCG motif). However, both remaining choices A and B are SAM-dependent methyltransferase reactions. Distinguishing an O-methyltransferase acting on desmethylrestrictinol (A) from an N-methyltransferase acting on 3-hydroxy-4,5-dimethoxyphenethylamine (B) requires knowledge of the specific active-site architecture and substrate-binding pocket, which cannot be reliably inferred from the primary sequence alone through general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (desmethylrestrictinol vs. 3-hydroxy-4,5-dimethoxyphenethylamine) and the regiochemistry of methylation (O- vs. N-methylation) are protein-specific facts derived from experimental characterization (Liu et al. 2021) and database annotation. No general sequence feature in the provided 225-aa sequence distinguishes these two methyltransferase substrates.",
    "reason": "While the SAM-binding motif narrows the answer to a methyltransferase (eliminating C and D), the final choice between A and B depends entirely on knowing the specific biosynthetic pathway (restricticin) and substrate of this particular protein. This is an item-specific annotation fact, not derivable from general biological principles applied to the sequence."
  },
  "case_id": "catalytic_activity_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence (225 aa) matches UniProt entry A0A0L1JF88 (RSTN1_ASPN3) exactly. The entry is annotated as 'O-methyltransferase rstn1' (EC 2.1.1.-) with the catalytic activity explicitly stated as 'desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)' under evidence code ECO:0000269 (inferred from direct assay, PubMed:33857369, Liu et al. JACS 2021). This is experimental evidence, not mere computational inference. Both the current and historical (v23) entries confirm the same reaction. The expected answer Choice A matches this annotation verbatim."
  },
  "important_caveats": [
    "The annotation evidence code ECO:0000269 indicates experimental (direct assay) support from Liu et al. 2021 (JACS), not computational prediction, strengthening the expected-answer check.",
    "The identity origin note states the accession was inferred from dataset image-path metadata, not from the evaluated model input; the model receives only the raw sequence.",
    "The entry was first public in Swiss-Prot on 2025-02-05; depending on the author's data-construction date, this annotation may or may not have been available to the model's training data.",
    "The EC number is listed as 2.1.1.- (unassigned subclass), meaning the specific methyltransferase sub-class is not yet formally assigned, further underscoring the lookup dependence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A and B describe SAM-dependent methyltransferase reactions. The GCGTGK motif in the sequence supports a methyltransferase classification but does not specify O- vs. N-methylation or identify the particular substrate. Without database lookup or prior knowledge of the restricticin biosynthetic pathway, a knowledgeable model could reasonably select B as well."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence (225 aa) matches UniProt entry A0A0L1JF88 (RSTN1_ASPN3) exactly. The entry is annotated as 'O-methyltransferase rstn1' (EC 2.1.1.-) with the catalytic activity explicitly stated as 'desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)' under evidence code ECO:0000269 (inferred from direct assay, PubMed:33857369, Liu et al. JACS 2021). This is experimental evidence, not mere computational inference. Both the current and historical (v23) entries confirm the same reaction. The expected answer Choice A matches this annotation verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a GCGTGKSA motif characteristic of SAM-binding methyltransferases, which allows elimination of Choice C (GTPase, no GTP-binding P-loop) and Choice D (ferredoxin-dependent P450, no heme-binding FGAGPRPCG motif). However, both remaining choices A and B are SAM-dependent methyltransferase reactions. Distinguishing an O-methyltransferase acting on desmethylrestrictinol (A) from an N-methyltransferase acting on 3-hydroxy-4,5-dimethoxyphenethylamine (B) requires knowledge of the specific active-site architecture and substrate-binding pocket, which cannot be reliably inferred from the primary sequence alone through general biological reasoning.",
    "missing_item_specific_fact": "The specific substrate identity (desmethylrestrictinol vs. 3-hydroxy-4,5-dimethoxyphenethylamine) and the regiochemistry of methylation (O- vs. N-methylation) are protein-specific facts derived from experimental characterization (Liu et al. 2021) and database annotation. No general sequence feature in the provided 225-aa sequence distinguishes these two methyltransferase substrates.",
    "reason": "While the SAM-binding motif narrows the answer to a methyltransferase (eliminating C and D), the final choice between A and B depends entirely on knowing the specific biosynthetic pathway (restricticin) and substrate of this particular protein. This is an item-specific annotation fact, not derivable from general biological principles applied to the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A and B describe SAM-dependent methyltransferase reactions. The GCGTGK motif in the sequence supports a methyltransferase classification but does not specify O- vs. N-methylation or identify the particular substrate. Without database lookup or prior knowledge of the restricticin biosynthetic pathway, a knowledgeable model could reasonably select B as well."
  },
  "important_caveats": [
    "The annotation evidence code ECO:0000269 indicates experimental (direct assay) support from Liu et al. 2021 (JACS), not computational prediction, strengthening the expected-answer check.",
    "The identity origin note states the accession was inferred from dataset image-path metadata, not from the evaluated model input; the model receives only the raw sequence.",
    "The entry was first public in Swiss-Prot on 2025-02-05; depending on the author's data-construction date, this annotation may or may not have been available to the model's training data.",
    "The EC number is listed as 2.1.1.- (unassigned subclass), meaning the specific methyltransferase sub-class is not yet formally assigned, further underscoring the lookup dependence."
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

**Accession:** `A0A0L1JF88` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 23. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF88.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:15.624587+00:00.  

```json
"A0A0L1JF88"
```

Source SHA-256: `dda8c813658a8c709826544ad5ddbd2ae972d7bfe23bb0ae87e41d05627a6d20`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF88.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:15.624587+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"O-methyltransferase rstn1"}}}
```

Source SHA-256: `dda8c813658a8c709826544ad5ddbd2ae972d7bfe23bb0ae87e41d05627a6d20`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF88.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:15.624587+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81532"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"name":"desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81531"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:231922"},{"database":"ChEBI","id":"CHEBI:231923"}]}}
```

Source SHA-256: `dda8c813658a8c709826544ad5ddbd2ae972d7bfe23bb0ae87e41d05627a6d20`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF88?format=txt&versions=23)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:17.437797+00:00.  

```text
ID   RSTN1_ASPN3             Reviewed;         225 AA.
AC   A0A0L1JF88;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   11-NOV-2015, sequence version 1.
DT   28-JAN-2026, entry version 23.
DE   RecName: Full=O-methyltransferase rstn1 {ECO:0000303|PubMed:33857369};
DE            EC=2.1.1.- {ECO:0000269|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};
GN   Name=rstn1 {ECO:0000303|PubMed:33857369}; ORFNames=ANOM_001442;
OS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /
OS   M93).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=1509407;
```

Source SHA-256: `79e66fc3e8c4ef26bf02567903ff65dcc83c5c855359b04ab315caa7a97c6612`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF88?format=txt&versions=23)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:17.437797+00:00.  

```text
DE   RecName: Full=O-methyltransferase rstn1 {ECO:0000303|PubMed:33857369};
DE            EC=2.1.1.- {ECO:0000269|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};
```

Source SHA-256: `79e66fc3e8c4ef26bf02567903ff65dcc83c5c855359b04ab315caa7a97c6612`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF88?format=txt&versions=23)  
**Locator:** `lines 49-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:17.437797+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol
CC         + S-adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81531,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:231922, ChEBI:CHEBI:231923;
CC         Evidence={ECO:0000269|PubMed:33857369};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81532;
CC         Evidence={ECO:0000269|PubMed:33857369};
```

Source SHA-256: `79e66fc3e8c4ef26bf02567903ff65dcc83c5c855359b04ab315caa7a97c6612`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 51. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
