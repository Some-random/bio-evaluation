# catalytic_activity_0038

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTAATLFESTDGTVVLLDLPRSIEDAQQHPAAVTLPEAPSLVTNSCRDGTSWTRRLISSPPPETPFVTPEPKNGPSPLPAAAQVAQLMIQASVTGALEELRTNYSGPYLLPRQLSPQRMIADGGKAVDDYKSPHACDLESCSTTAEDATKGRYYFPPESHHVLGTIQETKTLLLQSAPNFNVIVLDPPWPNRSAKRKKGGYKVATTTDDIRALLSDVPIPSLLARDGLVAIWVTNKPAFLDMLTSPRDGILSEWGLELVGEWSWLKITTSAEPILPIDSAHRKPWEPLLIAQRKGSKRVFPPFWRRRVIVSVPDTHSRKPNIRDLVNPMLPPRSRGLEIFARNLTAGWWAWGDDVLHFQERSNWVMAESKSPATGC

[Multiple Choices]
A. a phosphate monoester + H2O = an alcohol + phosphate
B. [thioredoxin]-dithiol + NADP(+) = [thioredoxin]-disulfide + NADPH + H(+)
C. an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)
D. L-isoleucyl-tRNA(Ile) + acetyl-CoA = N-acetyl-L-isoleucyl-tRNA(Ile) + CoA + H(+)
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

> The supplied sequence exactly matches the UniProt entry annotated as N6-methyladenosine RNA methyltransferase MTA1. Its catalytic-activity annotation gives choice C and cites experimental evidence codes, though the cited primary studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conserved DPPW motif associated with the MT-A70 family of SAM-dependent RNA methyltransferases. That makes the methyl-transfer reaction in C a meaningful fit and distinguishes it from the phosphatase, thioredoxin, and acetyltransferase alternatives.


**Missing item-specific fact**

> The exact RNA substrate specificity is not established by the motif alone, but it is not needed to distinguish C from the listed alternatives at the family-level choice resolution.


**Reason**

> A concrete sequence motif supports the relevant enzyme family and reaction class; this is more than remembering an exact sequence’s database entry or assuming a predictor could identify it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, C is the only SAM-dependent methyl-transfer reaction and is consistent with the sequence’s methyltransferase-family motif.


### Important caveats

- The database evidence is reviewer-only and was not supplied to the evaluated model.
- The UniProt catalytic-activity annotation cites experimental evidence, but the primary studies were not independently validated here.
- The sequence match supports applying that entry’s annotation to this sequence; it does not by itself demonstrate every detail of the reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conserved DPPW motif associated with the MT-A70 family of SAM-dependent RNA methyltransferases. That makes the methyl-transfer reaction in C a meaningful fit and distinguishes it from the phosphatase, thioredoxin, and acetyltransferase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact RNA substrate specificity is not established by the motif alone, but it is not needed to distinguish C from the listed alternatives at the family-level choice resolution.",
    "reason": "A concrete sequence motif supports the relevant enzyme family and reaction class; this is more than remembering an exact sequence’s database entry or assuming a predictor could identify it."
  },
  "case_id": "catalytic_activity_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as N6-methyladenosine RNA methyltransferase MTA1. Its catalytic-activity annotation gives choice C and cites experimental evidence codes, though the cited primary studies were not independently reviewed here."
  },
  "important_caveats": [
    "The database evidence is reviewer-only and was not supplied to the evaluated model.",
    "The UniProt catalytic-activity annotation cites experimental evidence, but the primary studies were not independently validated here.",
    "The sequence match supports applying that entry’s annotation to this sequence; it does not by itself demonstrate every detail of the reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, C is the only SAM-dependent methyl-transfer reaction and is consistent with the sequence’s methyltransferase-family motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as N6-methyladenosine RNA methyltransferase MTA1. Its catalytic-activity annotation gives choice C and cites experimental evidence codes, though the cited primary studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conserved DPPW motif associated with the MT-A70 family of SAM-dependent RNA methyltransferases. That makes the methyl-transfer reaction in C a meaningful fit and distinguishes it from the phosphatase, thioredoxin, and acetyltransferase alternatives.",
    "missing_item_specific_fact": "The exact RNA substrate specificity is not established by the motif alone, but it is not needed to distinguish C from the listed alternatives at the family-level choice resolution.",
    "reason": "A concrete sequence motif supports the relevant enzyme family and reaction class; this is more than remembering an exact sequence’s database entry or assuming a predictor could identify it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, C is the only SAM-dependent methyl-transfer reaction and is consistent with the sequence’s methyltransferase-family motif."
  },
  "important_caveats": [
    "The database evidence is reviewer-only and was not supplied to the evaluated model.",
    "The UniProt catalytic-activity annotation cites experimental evidence, but the primary studies were not independently validated here.",
    "The sequence match supports applying that entry’s annotation to this sequence; it does not by itself demonstrate every detail of the reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G4MSY9 (MTA1_PYRO7) is annotated as N6-methyladenosine RNA methyltransferase MTA1 (EC 2.1.1.348), with the catalytic activity exactly matching option C. The evidence is backed by experimental data (ECO:0000269) from PubMed:30535195 and PubMed:35338654. The benchmark sequence (376 AA) matches the UniProt sequence exactly (SHA256 confirmed). The reaction 'an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)' is the documented catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'DPPW' motif (in 'VIVLDPPWPNR') and the 'WWAWGDD' motif (in 'NLTAGWWAWGDD'), which are well-known family-level signatures of m6A RNA methyltransferases (METTL3/METTL14-like family). The overall architecture is consistent with a Rossmann-fold SAM-dependent methyltransferase. These motifs specifically distinguish m6A writers from other methyltransferase classes, phosphatases (option A), thioredoxin reductases (option B, which require FAD/NADPH-binding motifs absent here), and GNAT-fold acetyltransferases (option D, which require acetyl-CoA-binding motifs absent here). A biologist familiar with methyltransferase family motifs could identify the enzyme class from these sequence features.


**Missing item-specific fact**

> None critical. The WWAWGDD and DPPW motifs are general family signatures for m6A methyltransferases, not protein-specific annotations. However, recognizing these motifs as diagnostic of m6A writers (rather than generic methyltransferases) requires specialized knowledge of RNA modification enzyme families.


**Reason**

> The sequence provides identifiable family-level motifs (WWAWGDD, DPPW, Rossmann-like fold architecture) that allow a knowledgeable biologist to narrow the enzyme to an RNA methyltransferase using SAM, specifically an m6A writer. This distinguishes option C from the other choices through structural/motif reasoning rather than requiring recall of this particular protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct enzyme classes (phosphatase, oxidoreductase, methyltransferase, acetyltransferase). The sequence lacks phosphatase motifs, FAD/NADPH-binding motifs, and GNAT-fold features, leaving the SAM-dependent methyltransferase reaction (C) as the only option consistent with the observed WWAWGDD/DPPW motifs and overall fold.


### Important caveats

- The WWAWGDD motif recognition as specifically diagnostic of m6A writers (vs. other SAM-dependent methyltransferases) requires specialized knowledge of RNA modification enzyme families, which is borderline between general knowledge and expert-level recognition.
- The UniProt annotation is backed by experimental evidence (ECO:0000269) from two independent publications, strengthening the key's validity.
- The sequence is from a fungal protein (Pyricularia oryzae); the m6A methylation machinery is conserved across eukaryotes, so the motifs are transferable knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'DPPW' motif (in 'VIVLDPPWPNR') and the 'WWAWGDD' motif (in 'NLTAGWWAWGDD'), which are well-known family-level signatures of m6A RNA methyltransferases (METTL3/METTL14-like family). The overall architecture is consistent with a Rossmann-fold SAM-dependent methyltransferase. These motifs specifically distinguish m6A writers from other methyltransferase classes, phosphatases (option A), thioredoxin reductases (option B, which require FAD/NADPH-binding motifs absent here), and GNAT-fold acetyltransferases (option D, which require acetyl-CoA-binding motifs absent here). A biologist familiar with methyltransferase family motifs could identify the enzyme class from these sequence features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The WWAWGDD and DPPW motifs are general family signatures for m6A methyltransferases, not protein-specific annotations. However, recognizing these motifs as diagnostic of m6A writers (rather than generic methyltransferases) requires specialized knowledge of RNA modification enzyme families.",
    "reason": "The sequence provides identifiable family-level motifs (WWAWGDD, DPPW, Rossmann-like fold architecture) that allow a knowledgeable biologist to narrow the enzyme to an RNA methyltransferase using SAM, specifically an m6A writer. This distinguishes option C from the other choices through structural/motif reasoning rather than requiring recall of this particular protein's database entry."
  },
  "case_id": "catalytic_activity_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4MSY9 (MTA1_PYRO7) is annotated as N6-methyladenosine RNA methyltransferase MTA1 (EC 2.1.1.348), with the catalytic activity exactly matching option C. The evidence is backed by experimental data (ECO:0000269) from PubMed:30535195 and PubMed:35338654. The benchmark sequence (376 AA) matches the UniProt sequence exactly (SHA256 confirmed). The reaction 'an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)' is the documented catalytic activity."
  },
  "important_caveats": [
    "The WWAWGDD motif recognition as specifically diagnostic of m6A writers (vs. other SAM-dependent methyltransferases) requires specialized knowledge of RNA modification enzyme families, which is borderline between general knowledge and expert-level recognition.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from two independent publications, strengthening the key's validity.",
    "The sequence is from a fungal protein (Pyricularia oryzae); the m6A methylation machinery is conserved across eukaryotes, so the motifs are transferable knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes (phosphatase, oxidoreductase, methyltransferase, acetyltransferase). The sequence lacks phosphatase motifs, FAD/NADPH-binding motifs, and GNAT-fold features, leaving the SAM-dependent methyltransferase reaction (C) as the only option consistent with the observed WWAWGDD/DPPW motifs and overall fold."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G4MSY9 (MTA1_PYRO7) is annotated as N6-methyladenosine RNA methyltransferase MTA1 (EC 2.1.1.348), with the catalytic activity exactly matching option C. The evidence is backed by experimental data (ECO:0000269) from PubMed:30535195 and PubMed:35338654. The benchmark sequence (376 AA) matches the UniProt sequence exactly (SHA256 confirmed). The reaction 'an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)' is the documented catalytic activity.",
    "evidence_ids": ["C4", "C5", "H2", "H5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'DPPW' motif (in 'VIVLDPPWPNR') and the 'WWAWGDD' motif (in 'NLTAGWWAWGDD'), which are well-known family-level signatures of m6A RNA methyltransferases (METTL3/METTL14-like family). The overall architecture is consistent with a Rossmann-fold SAM-dependent methyltransferase. These motifs specifically distinguish m6A writers from other methyltransferase classes, phosphatases (option A), thioredoxin reductases (option B, which require FAD/NADPH-binding motifs absent here), and GNAT-fold acetyltransferases (option D, which require acetyl-CoA-binding motifs absent here). A biologist familiar with methyltransferase family motifs could identify the enzyme class from these sequence features.",
    "missing_item_specific_fact": "None critical. The WWAWGDD and DPPW motifs are general family signatures for m6A methyltransferases, not protein-specific annotations. However, recognizing these motifs as diagnostic of m6A writers (rather than generic methyltransferases) requires specialized knowledge of RNA modification enzyme families.",
    "reason": "The sequence provides identifiable family-level motifs (WWAWGDD, DPPW, Rossmann-like fold architecture) that allow a knowledgeable biologist to narrow the enzyme to an RNA methyltransferase using SAM, specifically an m6A writer. This distinguishes option C from the other choices through structural/motif reasoning rather than requiring recall of this particular protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes (phosphatase, oxidoreductase, methyltransferase, acetyltransferase). The sequence lacks phosphatase motifs, FAD/NADPH-binding motifs, and GNAT-fold features, leaving the SAM-dependent methyltransferase reaction (C) as the only option consistent with the observed WWAWGDD/DPPW motifs and overall fold."
  },
  "important_caveats": [
    "The WWAWGDD motif recognition as specifically diagnostic of m6A writers (vs. other SAM-dependent methyltransferases) requires specialized knowledge of RNA modification enzyme families, which is borderline between general knowledge and expert-level recognition.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from two independent publications, strengthening the key's validity.",
    "The sequence is from a fungal protein (Pyricularia oryzae); the m6A methylation machinery is conserved across eukaryotes, so the motifs are transferable knowledge."
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

**Accession:** `G4MSY9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 55. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.225373+00:00.  

```json
"G4MSY9"
```

Source SHA-256: `af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.225373+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"M6A writer MTA1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35338654","source":"PubMed"}],"value":"2.1.1.348"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35338654","source":"PubMed"}],"value":"N6-methyladenosine RNA methyltransferase MTA1"}}}
```

Source SHA-256: `af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.225373+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"30535195","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"35338654","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:55585"}}],"reaction":{"ecNumber":"2.1.1.348","evidences":[{"evidenceCode":"ECO:0000269","id":"30535195","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"35338654","source":"PubMed"}],"name":"an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:55584"},{"database":"Rhea","id":"RHEA-COMP:12414"},{"database":"Rhea","id":"RHEA-COMP:12417"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:74411"},{"database":"ChEBI","id":"CHEBI:74449"}]}}
```

Source SHA-256: `af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:05.307350+00:00.  

```text
DE   RecName: Full=N6-methyladenosine RNA methyltransferase MTA1 {ECO:0000303|PubMed:35338654};
DE            EC=2.1.1.348 {ECO:0000269|PubMed:35338654};
DE   AltName: Full=M6A writer MTA1 {ECO:0000305};
```

Source SHA-256: `b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)  
**Locator:** `lines 28-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:05.307350+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.
RX   PubMed=30535195; DOI=10.1093/femsle/fny286;
RA   Shi Y., Wang H., Wang J., Liu X., Lin F., Lu J.;
RT   "N6-methyladenosine RNA methylation is involved in virulence of the rice
RT   blast fungus Pyricularia oryzae (syn. Magnaporthe oryzae).";
RL   FEMS Microbiol. Lett. 366:0-0(2019).
```

Source SHA-256: `b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)  
**Locator:** `lines 35-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:05.307350+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.
RX   PubMed=35338654; DOI=10.1111/nph.18117;
RA   Ren Z., Tang B., Xing J., Liu C., Cai X., Hendy A., Kamran M., Liu H.,
RA   Zheng L., Huang J., Chen X.L.;
RT   "MTA1-mediated RNA m6 A modification regulates autophagy and is required
RT   for infection of the rice blast fungus.";
RL   New Phytol. 235:247-262(2022).
```

Source SHA-256: `b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)  
**Locator:** `lines 55-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:05.307350+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-
CC         methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+);
CC         Xref=Rhea:RHEA:55584, Rhea:RHEA-COMP:12414, Rhea:RHEA-COMP:12417,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:74411, ChEBI:CHEBI:74449; EC=2.1.1.348;
CC         Evidence={ECO:0000269|PubMed:30535195, ECO:0000269|PubMed:35338654};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:55585;
CC         Evidence={ECO:0000269|PubMed:30535195, ECO:0000269|PubMed:35338654};
```

Source SHA-256: `b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
