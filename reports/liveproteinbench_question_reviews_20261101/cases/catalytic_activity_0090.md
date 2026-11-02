# catalytic_activity_0090

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — peramine + 2-oxoglutarate + O2 = 8-hydroxyperamine + succinate + CO2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATDTAVTGAPETMQLRLASGNGPVTRTVLRTPLRDALPSEVPLIDISPIFSTSVADRKAVACKIHDAATNIGFFYIQNHRVPSRDTDMAYSASLDFFRQDMEAKMKADAKKGPFDSGYRGPGTQRVNPDEGADLRETYSILYDPMLDPTVPDPARIPEPASRFLHLGRAPFESTDTLPHFKDAFVRYFQACLALARALTRTFALSLDLPESAFDSKVQYPDASLEINFYPPISTGHAVSAPADPDTRVSIGSHTDFLLFTILWQDSNGGLQVLNREGQWIRASPVEGTFVVNIGDYLQRITNDKYVSTVHRAQNWSGRQRVSMPFFWGFGMHESCQVLESCCGEDGKSKYDEVRCVDWVSRRLGNLFDLSDKG

[Multiple Choices]
A. 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)
B. 2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O
C. N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
D. peramine + 2-oxoglutarate + O2 = 8-hydroxyperamine + succinate + CO2
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

> The supplied sequence exactly matches the 374-aa UniProt entry for PPZC, whose catalytic-activity annotation gives reaction D with ECO:0000269 evidence linked to a 2024 paper. The archived entry also contains this reaction annotation, though the underlying paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe different reaction types, and a sequence-based inference of a 2-oxoglutarate-dependent oxygenase could favor D over the hydrolase, synthetase, and methyltransferase options. That broad inference does not establish peramine as the substrate or the specific 8-hydroxylation product.


**Missing item-specific fact**

> The protein-specific catalytic activity linking this sequence to peramine 8-hydroxylation, established by annotation or experimental evidence.


**Reason**

> The exact substrate and product specificity required by the question is not supplied by the sequence or context in a way that can be reliably deduced from general biological knowledge alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices give distinct reaction types and D is supported for the sequence-matched protein by the reviewer-only evidence.


### Important caveats

- The accession and database annotation are reviewer-only information, not information supplied to the evaluated model.
- UniProt cites experimental evidence for the catalytic activity, but the primary study was not independently validated in this audit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe different reaction types, and a sequence-based inference of a 2-oxoglutarate-dependent oxygenase could favor D over the hydrolase, synthetase, and methyltransferase options. That broad inference does not establish peramine as the substrate or the specific 8-hydroxylation product.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity linking this sequence to peramine 8-hydroxylation, established by annotation or experimental evidence.",
    "reason": "The exact substrate and product specificity required by the question is not supplied by the sequence or context in a way that can be reliably deduced from general biological knowledge alone."
  },
  "case_id": "catalytic_activity_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 374-aa UniProt entry for PPZC, whose catalytic-activity annotation gives reaction D with ECO:0000269 evidence linked to a 2024 paper. The archived entry also contains this reaction annotation, though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The accession and database annotation are reviewer-only information, not information supplied to the evaluated model.",
    "UniProt cites experimental evidence for the catalytic activity, but the primary study was not independently validated in this audit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices give distinct reaction types and D is supported for the sequence-matched protein by the reviewer-only evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 374-aa UniProt entry for PPZC, whose catalytic-activity annotation gives reaction D with ECO:0000269 evidence linked to a 2024 paper. The archived entry also contains this reaction annotation, though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C5", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe different reaction types, and a sequence-based inference of a 2-oxoglutarate-dependent oxygenase could favor D over the hydrolase, synthetase, and methyltransferase options. That broad inference does not establish peramine as the substrate or the specific 8-hydroxylation product.",
    "missing_item_specific_fact": "The protein-specific catalytic activity linking this sequence to peramine 8-hydroxylation, established by annotation or experimental evidence.",
    "reason": "The exact substrate and product specificity required by the question is not supplied by the sequence or context in a way that can be reliably deduced from general biological knowledge alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices give distinct reaction types and D is supported for the sequence-matched protein by the reviewer-only evidence."
  },
  "important_caveats": [
    "The accession and database annotation are reviewer-only information, not information supplied to the evaluated model.",
    "UniProt cites experimental evidence for the catalytic activity, but the primary study was not independently validated in this audit."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A455ZKR7 (PPZC_METMF, 374 AA, exact sequence match) explicitly annotates the catalytic activity as 'peramine + 2-oxoglutarate + O2 = 8-hydroxyperamine + succinate + CO2' (Rhea:RHEA:82167) with experimental evidence code ECO:0000269 from PubMed:38578094 (Rothchild et al., JACS 2024). The protein is named '2-oxoglutarate-Fe(II) type oxidoreductase ppzC' with EC 1.14.11.-. Both current (entry v22) and historical (entry v21) records confirm this annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable motifs of the 2-His-1-carboxylate facial triad characteristic of 2-oxoglutarate/Fe(II) oxygenases: 'IGSHTDF' (HxD motif), 'VHRAQ' (second His), and 'MHESC' (third His). Among the four choices, only D involves 2-oxoglutarate + O2 as substrates yielding succinate + CO2 as byproducts, which is the hallmark reaction chemistry of the 2OG/Fe(II) oxygenase superfamily. Choices A (ADP-ribosylhydrolase), B (FMN/ATP-dependent synthetase), and C (SAM-dependent methyltransferase) require entirely different cofactors and catalytic mechanisms inconsistent with the identified facial-triad motif.


**Missing item-specific fact**

> The specific substrate identity 'peramine' and the regiochemistry of hydroxylation at C-8 cannot be predicted from sequence alone; this requires knowledge of the PPZ biosynthetic pathway or the 2024 experimental characterization. However, this fact is not needed to distinguish D from A, B, and C, since only D is mechanistically consistent with a 2OG/Fe(II) oxygenase.


**Reason**

> A model with knowledge of the 2-His-1-carboxylate facial triad motif and the general reaction chemistry of 2OG-dependent dioxygenases (2OG + O2 → succinate + CO2 + substrate hydroxylation) can eliminate choices A, B, and C based on their incompatible cofactor requirements and reaction stoichiometries. The sequence provides concrete motif evidence for the enzyme class, and the mechanistic signature uniquely identifies D among the four options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor belongs to a fundamentally different enzyme class (hydrolase, synthetase, methyltransferase) with incompatible cofactors (ADP-ribose, FMN/ATP, SAM) and reaction mechanisms. The 2OG/Fe(II) oxygenase motif in the sequence and the 2OG + O2 → succinate + CO2 stoichiometry in D create a clear mechanistic distinction. No other option is consistent with the identified enzyme fold.


### Important caveats

- The specific substrate name 'peramine' and product '8-hydroxyperamine' are pathway-specific facts that cannot be deduced from sequence alone; they were confirmed experimentally (ECO:0000269) only in 2024 (PubMed:38578094). The UniProt entry was first released in February 2025.
- The facial-triad motif identification requires familiarity with 2OG/Fe(II) oxygenase structural biology; while well-established, it is specialized enzymology knowledge rather than general biology.
- The identity of this sequence as PPZC was inferred by the reviewer from dataset metadata (accession A0A455ZKR7); this accession was not provided to the evaluated model.
- The sequence match is exact (374 AA, identical SHA256) across both current and historical UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable motifs of the 2-His-1-carboxylate facial triad characteristic of 2-oxoglutarate/Fe(II) oxygenases: 'IGSHTDF' (HxD motif), 'VHRAQ' (second His), and 'MHESC' (third His). Among the four choices, only D involves 2-oxoglutarate + O2 as substrates yielding succinate + CO2 as byproducts, which is the hallmark reaction chemistry of the 2OG/Fe(II) oxygenase superfamily. Choices A (ADP-ribosylhydrolase), B (FMN/ATP-dependent synthetase), and C (SAM-dependent methyltransferase) require entirely different cofactors and catalytic mechanisms inconsistent with the identified facial-triad motif.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity 'peramine' and the regiochemistry of hydroxylation at C-8 cannot be predicted from sequence alone; this requires knowledge of the PPZ biosynthetic pathway or the 2024 experimental characterization. However, this fact is not needed to distinguish D from A, B, and C, since only D is mechanistically consistent with a 2OG/Fe(II) oxygenase.",
    "reason": "A model with knowledge of the 2-His-1-carboxylate facial triad motif and the general reaction chemistry of 2OG-dependent dioxygenases (2OG + O2 → succinate + CO2 + substrate hydroxylation) can eliminate choices A, B, and C based on their incompatible cofactor requirements and reaction stoichiometries. The sequence provides concrete motif evidence for the enzyme class, and the mechanistic signature uniquely identifies D among the four options."
  },
  "case_id": "catalytic_activity_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A455ZKR7 (PPZC_METMF, 374 AA, exact sequence match) explicitly annotates the catalytic activity as 'peramine + 2-oxoglutarate + O2 = 8-hydroxyperamine + succinate + CO2' (Rhea:RHEA:82167) with experimental evidence code ECO:0000269 from PubMed:38578094 (Rothchild et al., JACS 2024). The protein is named '2-oxoglutarate-Fe(II) type oxidoreductase ppzC' with EC 1.14.11.-. Both current (entry v22) and historical (entry v21) records confirm this annotation."
  },
  "important_caveats": [
    "The specific substrate name 'peramine' and product '8-hydroxyperamine' are pathway-specific facts that cannot be deduced from sequence alone; they were confirmed experimentally (ECO:0000269) only in 2024 (PubMed:38578094). The UniProt entry was first released in February 2025.",
    "The facial-triad motif identification requires familiarity with 2OG/Fe(II) oxygenase structural biology; while well-established, it is specialized enzymology knowledge rather than general biology.",
    "The identity of this sequence as PPZC was inferred by the reviewer from dataset metadata (accession A0A455ZKR7); this accession was not provided to the evaluated model.",
    "The sequence match is exact (374 AA, identical SHA256) across both current and historical UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor belongs to a fundamentally different enzyme class (hydrolase, synthetase, methyltransferase) with incompatible cofactors (ADP-ribose, FMN/ATP, SAM) and reaction mechanisms. The 2OG/Fe(II) oxygenase motif in the sequence and the 2OG + O2 → succinate + CO2 stoichiometry in D create a clear mechanistic distinction. No other option is consistent with the identified enzyme fold."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A455ZKR7 (PPZC_METMF, 374 AA, exact sequence match) explicitly annotates the catalytic activity as 'peramine + 2-oxoglutarate + O2 = 8-hydroxyperamine + succinate + CO2' (Rhea:RHEA:82167) with experimental evidence code ECO:0000269 from PubMed:38578094 (Rothchild et al., JACS 2024). The protein is named '2-oxoglutarate-Fe(II) type oxidoreductase ppzC' with EC 1.14.11.-. Both current (entry v22) and historical (entry v21) records confirm this annotation.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable motifs of the 2-His-1-carboxylate facial triad characteristic of 2-oxoglutarate/Fe(II) oxygenases: 'IGSHTDF' (HxD motif), 'VHRAQ' (second His), and 'MHESC' (third His). Among the four choices, only D involves 2-oxoglutarate + O2 as substrates yielding succinate + CO2 as byproducts, which is the hallmark reaction chemistry of the 2OG/Fe(II) oxygenase superfamily. Choices A (ADP-ribosylhydrolase), B (FMN/ATP-dependent synthetase), and C (SAM-dependent methyltransferase) require entirely different cofactors and catalytic mechanisms inconsistent with the identified facial-triad motif.",
    "missing_item_specific_fact": "The specific substrate identity 'peramine' and the regiochemistry of hydroxylation at C-8 cannot be predicted from sequence alone; this requires knowledge of the PPZ biosynthetic pathway or the 2024 experimental characterization. However, this fact is not needed to distinguish D from A, B, and C, since only D is mechanistically consistent with a 2OG/Fe(II) oxygenase.",
    "reason": "A model with knowledge of the 2-His-1-carboxylate facial triad motif and the general reaction chemistry of 2OG-dependent dioxygenases (2OG + O2 → succinate + CO2 + substrate hydroxylation) can eliminate choices A, B, and C based on their incompatible cofactor requirements and reaction stoichiometries. The sequence provides concrete motif evidence for the enzyme class, and the mechanistic signature uniquely identifies D among the four options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor belongs to a fundamentally different enzyme class (hydrolase, synthetase, methyltransferase) with incompatible cofactors (ADP-ribose, FMN/ATP, SAM) and reaction mechanisms. The 2OG/Fe(II) oxygenase motif in the sequence and the 2OG + O2 → succinate + CO2 stoichiometry in D create a clear mechanistic distinction. No other option is consistent with the identified enzyme fold."
  },
  "important_caveats": [
    "The specific substrate name 'peramine' and product '8-hydroxyperamine' are pathway-specific facts that cannot be deduced from sequence alone; they were confirmed experimentally (ECO:0000269) only in 2024 (PubMed:38578094). The UniProt entry was first released in February 2025.",
    "The facial-triad motif identification requires familiarity with 2OG/Fe(II) oxygenase structural biology; while well-established, it is specialized enzymology knowledge rather than general biology.",
    "The identity of this sequence as PPZC was inferred by the reviewer from dataset metadata (accession A0A455ZKR7); this accession was not provided to the evaluated model.",
    "The sequence match is exact (374 AA, identical SHA256) across both current and historical UniProt records."
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

**Accession:** `A0A455ZKR7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 21. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.380201+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"Pyrrolopyrazine biosynthesis cluster protein C"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"value":"1.14.11.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"2-oxoglutarate-Fe(II) type oxidoreductase ppzC"}}}
```

Source SHA-256: `6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.380201+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:82168"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"name":"peramine + 2-oxoglutarate + O2 = 8-hydroxyperamine + succinate + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:82167"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:16810"},{"database":"ChEBI","id":"CHEBI:30031"},{"database":"ChEBI","id":"CHEBI:232088"},{"database":"ChEBI","id":"CHEBI:232097"}]}}
```

Source SHA-256: `6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.380201+00:00.  

```json
{"citation":{"authors":["Rothchild K.W.","Hagar M.","Berry D.","Ryan K.S."],"citationCrossReferences":[{"database":"PubMed","id":"38578094"},{"database":"DOI","id":"10.1021/jacs.4c01419"}],"citationType":"journal article","firstPage":"10263","id":"38578094","journal":"J. Am. Chem. Soc.","lastPage":"10267","publicationDate":"2024","title":"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.","volume":"146"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:18.441147+00:00.  

```text
DE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzC {ECO:0000303|PubMed:30452111};
DE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};
DE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein C {ECO:0000303|PubMed:30452111};
```

Source SHA-256: `a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)  
**Locator:** `lines 51-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:18.441147+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=peramine + 2-oxoglutarate + O2 = 8-hydroxyperamine + succinate
CC         + CO2; Xref=Rhea:RHEA:82167, ChEBI:CHEBI:15379, ChEBI:CHEBI:16526,
CC         ChEBI:CHEBI:16810, ChEBI:CHEBI:30031, ChEBI:CHEBI:232088,
CC         ChEBI:CHEBI:232097; Evidence={ECO:0000269|PubMed:38578094};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82168;
CC         Evidence={ECO:0000269|PubMed:38578094};
```

Source SHA-256: `a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 90. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
