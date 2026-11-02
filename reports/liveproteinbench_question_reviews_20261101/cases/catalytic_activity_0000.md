# catalytic_activity_0000

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — okaramine A + 2-oxoglutarate + AH2 + O2 = 12-deshydroxyl okaramine E + succinate + A + CO2 + H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTLTENVMKPQIQRFTRDHDPKVLWQVVEEDGAVIIEGFLPHEVIQKFDCELDVRSKATKGGEMNQEFYQMPVPTTTKWMNDLTATCPTFRHEILNNDILHSLCNVAFEPHGDYWLLNGMAMEMMPGNPTQQIHNDHGTHPILQYLRPDAPAPVFSIITAVTEFTESNGATRVILGSHRWPQGQKAKDDQAVRAALQPGDALVMHRSTKHGGAAHDADNQDHRRLLLTCMGTCQLAPYETNVTVPRPIVESMTPLAQKMIGWRSTRPVISNVTGLNTVRMKHLENQIELKSNVPLNVGGC

[Multiple Choices]
A. L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)
B. 3-phenylpropanoate + NAD(+) = (E)-cinnamate + NADH + H(+)
C. 4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NAD(+) + H2O
D. okaramine A + 2-oxoglutarate + AH2 + O2 = 12-deshydroxyl okaramine E + succinate + A + CO2 + H2O
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

> The exact 300-aa sequence matches the UniProt entry annotated as OkaE, an iron/2-oxoglutarate-dependent dioxygenase. Its catalytic-activity annotation gives the reaction in D and cites experimental evidence (ECO:0000269) from a publication.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an HxD(H)-like metal-binding motif consistent with a non-heme iron/2-oxoglutarate-dependent dioxygenase. Among the choices, D is the reaction using 2-oxoglutarate and O2; the other options describe phosphorylation, NAD+-dependent oxidation, or NADH-dependent reduction.


**Missing item-specific fact**

> The exact okaramine substrate and product identities are not derivable from the sequence motif alone; however, the reaction class distinguishes D from the supplied alternatives.


**Reason**

> A defensible sequence-to-enzyme-class inference, combined with the reaction cofactors in the choices, meaningfully distinguishes D without needing to recognize the exact sequence or retrieve its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D matches the inferred 2-oxoglutarate-dependent oxygenase reaction class.


### Important caveats

- The database annotation cites experimental evidence, but the cited primary paper was not independently reviewed here.
- The sequence match establishes applicability of the annotation to this sequence; it does not mean the annotation or identity was supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an HxD(H)-like metal-binding motif consistent with a non-heme iron/2-oxoglutarate-dependent dioxygenase. Among the choices, D is the reaction using 2-oxoglutarate and O2; the other options describe phosphorylation, NAD+-dependent oxidation, or NADH-dependent reduction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact okaramine substrate and product identities are not derivable from the sequence motif alone; however, the reaction class distinguishes D from the supplied alternatives.",
    "reason": "A defensible sequence-to-enzyme-class inference, combined with the reaction cofactors in the choices, meaningfully distinguishes D without needing to recognize the exact sequence or retrieve its database entry."
  },
  "case_id": "catalytic_activity_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 300-aa sequence matches the UniProt entry annotated as OkaE, an iron/2-oxoglutarate-dependent dioxygenase. Its catalytic-activity annotation gives the reaction in D and cites experimental evidence (ECO:0000269) from a publication."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the cited primary paper was not independently reviewed here.",
    "The sequence match establishes applicability of the annotation to this sequence; it does not mean the annotation or identity was supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D matches the inferred 2-oxoglutarate-dependent oxygenase reaction class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 300-aa sequence matches the UniProt entry annotated as OkaE, an iron/2-oxoglutarate-dependent dioxygenase. Its catalytic-activity annotation gives the reaction in D and cites experimental evidence (ECO:0000269) from a publication.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an HxD(H)-like metal-binding motif consistent with a non-heme iron/2-oxoglutarate-dependent dioxygenase. Among the choices, D is the reaction using 2-oxoglutarate and O2; the other options describe phosphorylation, NAD+-dependent oxidation, or NADH-dependent reduction.",
    "missing_item_specific_fact": "The exact okaramine substrate and product identities are not derivable from the sequence motif alone; however, the reaction class distinguishes D from the supplied alternatives.",
    "reason": "A defensible sequence-to-enzyme-class inference, combined with the reaction cofactors in the choices, meaningfully distinguishes D without needing to recognize the exact sequence or retrieve its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D matches the inferred 2-oxoglutarate-dependent oxygenase reaction class."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the cited primary paper was not independently reviewed here.",
    "The sequence match establishes applicability of the annotation to this sequence; it does not mean the annotation or identity was supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence (300 AA, SHA256 match) corresponds to UniProt A0A2Z5U507 (OKAE_PENOH), annotated as 'Iron/alpha-ketoglutarate-dependent dioxygenase okaE' (EC 1.14.20.-). The catalytic activity comment (C5/H4) explicitly lists the reaction 'okaramine A + 2-oxoglutarate + AH2 + O2 = 12-deshydroxyl okaramine E + succinate + A + CO2 + H2O' with experimental evidence code ECO:0000269 from PubMed:28631282 (Lai et al., Angew. Chem. Int. Ed. 2017). The expected answer matches the annotated reaction verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four choices represent clearly distinct enzyme classes: (A) protein kinase, (B) FAD-dependent dehydrogenase, (C) nitroreductase, (D) Fe(II)/2-oxoglutarate-dependent dioxygenase. The supplied 300-aa sequence contains His-rich regions (e.g., 'GSHRW…HRSTKHGGAAHDADNQDHRRLLLTCMGTCQL') consistent with the 2-His-1-carboxylate facial triad of Fe(II)/2-OG dioxygenases, and lacks canonical kinase motifs (VAIK, HRD, DFG) that would support choice A, and lacks Rossmann-fold FAD/NAD-binding motifs that would support choices B or C. Choice D is the only option whose stoichiometry (2-oxoglutarate → succinate + CO2, O2 consumption) matches the Fe(II)/2-OG dioxygenase class identifiable from the sequence. A model can eliminate A, B, C on the basis of absent cofactor-binding motifs and select D on the basis of the facial-triad signature.


**Missing item-specific fact**

> None strictly required. The specific substrate name 'okaramine A' and product '12-deshydroxyl okaramine E' cannot be derived from sequence alone, but they need not be: the reasoning path identifies the enzyme class from motifs and then selects the only option belonging to that class.


**Reason**

> General knowledge of enzyme-family sequence signatures (kinase catalytic core, Rossmann fold, HxD/E facial triad) allows a knowledgeable model to eliminate three of four choices and select D without memorizing this particular protein's UniProt entry. The specificity of the substrate name is embedded in the answer text and does not need to be independently predicted.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four unrelated enzyme classes (kinase, FAD-dehydrogenase, nitroreductase, Fe(II)/2-OG dioxygenase). The sequence motifs clearly exclude A, B, and C, leaving D as the only class-consistent option.


### Important caveats

- The annotation evidence code is ECO:0000269 (experimental evidence from the 2017 Lai et al. paper), so the catalytic activity is experimentally established, not merely computational.
- While the enzyme class (Fe(II)/2-OG dioxygenase) is inferable from sequence motifs, the exact substrate 'okaramine A' is a highly specialized fungal indole alkaloid; a model that cannot recognize the facial triad would need to rely on memorizing this specific protein's annotation.
- The sequence is 300 aa and matches the UniProt canonical entry exactly (SHA256 confirmed), so no numbering or isoform ambiguity exists.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices represent clearly distinct enzyme classes: (A) protein kinase, (B) FAD-dependent dehydrogenase, (C) nitroreductase, (D) Fe(II)/2-oxoglutarate-dependent dioxygenase. The supplied 300-aa sequence contains His-rich regions (e.g., 'GSHRW…HRSTKHGGAAHDADNQDHRRLLLTCMGTCQL') consistent with the 2-His-1-carboxylate facial triad of Fe(II)/2-OG dioxygenases, and lacks canonical kinase motifs (VAIK, HRD, DFG) that would support choice A, and lacks Rossmann-fold FAD/NAD-binding motifs that would support choices B or C. Choice D is the only option whose stoichiometry (2-oxoglutarate → succinate + CO2, O2 consumption) matches the Fe(II)/2-OG dioxygenase class identifiable from the sequence. A model can eliminate A, B, C on the basis of absent cofactor-binding motifs and select D on the basis of the facial-triad signature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The specific substrate name 'okaramine A' and product '12-deshydroxyl okaramine E' cannot be derived from sequence alone, but they need not be: the reasoning path identifies the enzyme class from motifs and then selects the only option belonging to that class.",
    "reason": "General knowledge of enzyme-family sequence signatures (kinase catalytic core, Rossmann fold, HxD/E facial triad) allows a knowledgeable model to eliminate three of four choices and select D without memorizing this particular protein's UniProt entry. The specificity of the substrate name is embedded in the answer text and does not need to be independently predicted."
  },
  "case_id": "catalytic_activity_0000",
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
    "reason": "The protein sequence (300 AA, SHA256 match) corresponds to UniProt A0A2Z5U507 (OKAE_PENOH), annotated as 'Iron/alpha-ketoglutarate-dependent dioxygenase okaE' (EC 1.14.20.-). The catalytic activity comment (C5/H4) explicitly lists the reaction 'okaramine A + 2-oxoglutarate + AH2 + O2 = 12-deshydroxyl okaramine E + succinate + A + CO2 + H2O' with experimental evidence code ECO:0000269 from PubMed:28631282 (Lai et al., Angew. Chem. Int. Ed. 2017). The expected answer matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The annotation evidence code is ECO:0000269 (experimental evidence from the 2017 Lai et al. paper), so the catalytic activity is experimentally established, not merely computational.",
    "While the enzyme class (Fe(II)/2-OG dioxygenase) is inferable from sequence motifs, the exact substrate 'okaramine A' is a highly specialized fungal indole alkaloid; a model that cannot recognize the facial triad would need to rely on memorizing this specific protein's annotation.",
    "The sequence is 300 aa and matches the UniProt canonical entry exactly (SHA256 confirmed), so no numbering or isoform ambiguity exists."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four unrelated enzyme classes (kinase, FAD-dehydrogenase, nitroreductase, Fe(II)/2-OG dioxygenase). The sequence motifs clearly exclude A, B, and C, leaving D as the only class-consistent option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence (300 AA, SHA256 match) corresponds to UniProt A0A2Z5U507 (OKAE_PENOH), annotated as 'Iron/alpha-ketoglutarate-dependent dioxygenase okaE' (EC 1.14.20.-). The catalytic activity comment (C5/H4) explicitly lists the reaction 'okaramine A + 2-oxoglutarate + AH2 + O2 = 12-deshydroxyl okaramine E + succinate + A + CO2 + H2O' with experimental evidence code ECO:0000269 from PubMed:28631282 (Lai et al., Angew. Chem. Int. Ed. 2017). The expected answer matches the annotated reaction verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four choices represent clearly distinct enzyme classes: (A) protein kinase, (B) FAD-dependent dehydrogenase, (C) nitroreductase, (D) Fe(II)/2-oxoglutarate-dependent dioxygenase. The supplied 300-aa sequence contains His-rich regions (e.g., 'GSHRW…HRSTKHGGAAHDADNQDHRRLLLTCMGTCQL') consistent with the 2-His-1-carboxylate facial triad of Fe(II)/2-OG dioxygenases, and lacks canonical kinase motifs (VAIK, HRD, DFG) that would support choice A, and lacks Rossmann-fold FAD/NAD-binding motifs that would support choices B or C. Choice D is the only option whose stoichiometry (2-oxoglutarate → succinate + CO2, O2 consumption) matches the Fe(II)/2-OG dioxygenase class identifiable from the sequence. A model can eliminate A, B, C on the basis of absent cofactor-binding motifs and select D on the basis of the facial-triad signature.",
    "missing_item_specific_fact": "None strictly required. The specific substrate name 'okaramine A' and product '12-deshydroxyl okaramine E' cannot be derived from sequence alone, but they need not be: the reasoning path identifies the enzyme class from motifs and then selects the only option belonging to that class.",
    "reason": "General knowledge of enzyme-family sequence signatures (kinase catalytic core, Rossmann fold, HxD/E facial triad) allows a knowledgeable model to eliminate three of four choices and select D without memorizing this particular protein's UniProt entry. The specificity of the substrate name is embedded in the answer text and does not need to be independently predicted."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four unrelated enzyme classes (kinase, FAD-dehydrogenase, nitroreductase, Fe(II)/2-OG dioxygenase). The sequence motifs clearly exclude A, B, and C, leaving D as the only class-consistent option."
  },
  "important_caveats": [
    "The annotation evidence code is ECO:0000269 (experimental evidence from the 2017 Lai et al. paper), so the catalytic activity is experimentally established, not merely computational.",
    "While the enzyme class (Fe(II)/2-OG dioxygenase) is inferable from sequence motifs, the exact substrate 'okaramine A' is a highly specialized fungal indole alkaloid; a model that cannot recognize the facial triad would need to rely on memorizing this specific protein's annotation.",
    "The sequence is 300 aa and matches the UniProt canonical entry exactly (SHA256 confirmed), so no numbering or isoform ambiguity exists."
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

**Accession:** `A0A2Z5U507` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 21. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:53.902384+00:00.  

```json
"A0A2Z5U507"
```

Source SHA-256: `9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:53.902384+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Okaramines biosynthesis cluster protein E"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"value":"1.14.20.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Iron/alpha-ketoglutarate-dependent dioxygenase okaE"}}}
```

Source SHA-256: `9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:53.902384+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:82720"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"name":"okaramine A + 2-oxoglutarate + AH2 + O2 = 12-deshydroxyl okaramine E + succinate + A + CO2 + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:82719"},{"database":"ChEBI","id":"CHEBI:13193"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:16810"},{"database":"ChEBI","id":"CHEBI:17499"},{"database":"ChEBI","id":"CHEBI:30031"},{"database":"ChEBI","id":"CHEBI:232464"},{"database":"ChEBI","id":"CHEBI:232466"}]}}
```

Source SHA-256: `9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:24:56.491248+00:00.  

```text
ID   OKAE_PENOH              Reviewed;         300 AA.
AC   A0A2Z5U507;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-OCT-2018, sequence version 1.
DT   28-JAN-2026, entry version 21.
DE   RecName: Full=Iron/alpha-ketoglutarate-dependent dioxygenase okaE {ECO:0000303|PubMed:28631282};
DE            EC=1.14.20.- {ECO:0000269|PubMed:28631282};
DE   AltName: Full=Okaramines biosynthesis cluster protein E {ECO:0000303|PubMed:28631282};
GN   Name=okaE {ECO:0000303|PubMed:28631282};
OS   Penicillium ochrochloron.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=69780;
```

Source SHA-256: `64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:24:56.491248+00:00.  

```text
DE   RecName: Full=Iron/alpha-ketoglutarate-dependent dioxygenase okaE {ECO:0000303|PubMed:28631282};
DE            EC=1.14.20.- {ECO:0000269|PubMed:28631282};
DE   AltName: Full=Okaramines biosynthesis cluster protein E {ECO:0000303|PubMed:28631282};
```

Source SHA-256: `64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)  
**Locator:** `lines 60-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:24:56.491248+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=okaramine A + 2-oxoglutarate + AH2 + O2 = 12-deshydroxyl
CC         okaramine E + succinate + A + CO2 + H2O; Xref=Rhea:RHEA:82719,
CC         ChEBI:CHEBI:13193, ChEBI:CHEBI:15377, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:16526, ChEBI:CHEBI:16810, ChEBI:CHEBI:17499,
CC         ChEBI:CHEBI:30031, ChEBI:CHEBI:232464, ChEBI:CHEBI:232466;
CC         Evidence={ECO:0000269|PubMed:28631282};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82720;
CC         Evidence={ECO:0000269|PubMed:28631282};
```

Source SHA-256: `64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
