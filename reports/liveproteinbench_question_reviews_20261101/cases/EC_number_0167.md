# EC_number_0167

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.5.1.32

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAISPEVEHPNKAFGFAARDPSGLLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSQDLENYCPDQILTYSATYTDGTTTYGGYSSLMVADEHFVIRWPENLPMDIGAPLLCAGITTYSPLRHFGLDKPGTHVGIVGLGGLGHVAVKFAKAFGAKVTVISTSEGKKQEAVEKLGADAFLVSRDPEQMQAAAATLDGIIDTVSAVHPILPLVNLLKSQGKLIMVGAPEKPIELPVFPLLLGRKIVAGSAIGGLKETQDMIDFAAKHNILPDVELIPMDYVNTAMERLLKADVKYRFVIDICNTLKSA

[Multiple Choices]
A. 1.5.1.32
B. 1.6.5.2
C. 1.14.18.1
D. 4.1.1.25
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

> The exact sequence matches the UniProt entry annotated as vomilenine reductase, EC 1.5.1.32. Its catalytic-activity annotation assigns that EC number and cites experimental evidence (ECO:0000269) from two publications. This supports choice A, while the underlying papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad enzyme-family inference, but it does not establish the particular substrate and reaction needed to assign this exact EC number over the other oxidoreductase choices.


**Missing item-specific fact**

> The sequence-specific functional annotation or experimental finding that this protein catalyzes the vomilenine-reduction reaction.


**Reason**

> The input supplies only a sequence and candidate EC numbers. Identifying this specific reaction requires a protein-specific functional fact absent from the question; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports A for the sequence-matched protein. No alternative option is supported by the supplied reviewer-only evidence.


### Important caveats

- The annotation is sequence-matched in both current UniProt and a historical entry available by the stated cutoff, but the author's exact source snapshot is unknown.
- The functional and catalytic-activity annotations cite experimental evidence, but those primary publications were not independently validated in this audit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad enzyme-family inference, but it does not establish the particular substrate and reaction needed to assign this exact EC number over the other oxidoreductase choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific functional annotation or experimental finding that this protein catalyzes the vomilenine-reduction reaction.",
    "reason": "The input supplies only a sequence and candidate EC numbers. Identifying this specific reaction requires a protein-specific functional fact absent from the question; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as vomilenine reductase, EC 1.5.1.32. Its catalytic-activity annotation assigns that EC number and cites experimental evidence (ECO:0000269) from two publications. This supports choice A, while the underlying papers were not independently reviewed here."
  },
  "important_caveats": [
    "The annotation is sequence-matched in both current UniProt and a historical entry available by the stated cutoff, but the author's exact source snapshot is unknown.",
    "The functional and catalytic-activity annotations cite experimental evidence, but those primary publications were not independently validated in this audit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports A for the sequence-matched protein. No alternative option is supported by the supplied reviewer-only evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as vomilenine reductase, EC 1.5.1.32. Its catalytic-activity annotation assigns that EC number and cites experimental evidence (ECO:0000269) from two publications. This supports choice A, while the underlying papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad enzyme-family inference, but it does not establish the particular substrate and reaction needed to assign this exact EC number over the other oxidoreductase choices.",
    "missing_item_specific_fact": "The sequence-specific functional annotation or experimental finding that this protein catalyzes the vomilenine-reduction reaction.",
    "reason": "The input supplies only a sequence and candidate EC numbers. Identifying this specific reaction requires a protein-specific functional fact absent from the question; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports A for the sequence-matched protein. No alternative option is supported by the supplied reviewer-only evidence."
  },
  "important_caveats": [
    "The annotation is sequence-matched in both current UniProt and a historical entry available by the stated cutoff, but the author's exact source snapshot is unknown.",
    "The functional and catalytic-activity annotations cite experimental evidence, but those primary publications were not independently validated in this audit."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXJ3 (VOR1_RAUSE, Vomilenine reductase) is annotated with EC 1.5.1.32, supported by experimental evidence codes (ECO:0000269) from two independent publications (PubMed:11937349 and PubMed:38212296). The catalytic reaction is (2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+). Sequence match between the benchmark 360-aa sequence and the UniProt entry is confirmed (SHA256 identical). The annotation is backed by direct experimental characterization, not merely computational transfer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD(P)H-binding motif (GGLGHVAVK) and a zinc-binding region (GICHSDLHM), consistent with the medium-chain dehydrogenase/reductase (MDR/CAD) family. This eliminates D (EC 4.1.1.25, pyruvate decarboxylase: TPP-dependent, no NAD(P)H cofactor) and C (EC 1.14.18.1, laccase: requires multi-copper-oxidase HCHH motifs, absent here). Between A and B: the protein is 360 aa, lacks transmembrane helices, has a single NAD(P)H-binding domain, and exhibits plant-specific sequence context — all inconsistent with EC 1.6.5.2 (NADH:ubiquinone oxidoreductase / Complex I subunit), which is a membrane-integrated, highly conserved respiratory-chain component with distinct multi-domain architecture. The soluble, single-domain, plant-biosynthetic reductase architecture favors A over B.


**Missing item-specific fact**

> The exact 4th digit (32) and even the 3rd digit (1) of EC 1.5.1.32 encode the specific substrate (vomilenine) and reaction chemistry (CH-NH group oxidation), which cannot be deduced from sequence motifs alone. However, within the constrained four-choice set, sequence-based reasoning meaningfully eliminates C and D and provides architectural arguments favoring A over B.


**Reason**

> While the precise 4-digit EC number cannot be derived from sequence features alone (the substrate-specificity encoded in digits 3-4 requires experimental or database knowledge), the multiple-choice format allows reasoning from sequence architecture to eliminate three of four options. NAD(P)H motifs exclude the lyase; absence of copper motifs excludes laccase; small soluble single-domain plant protein architecture is inconsistent with a membrane-bound Complex I subunit. This constitutes meaningful biological reasoning that distinguishes A from the alternatives, even if the exact EC number's specificity is not fully derivable.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (1, 4) and different sub-classes (1.5 vs 1.6 vs 1.14 vs 4.1). Sequence-based elimination of C (no copper motifs) and D (has NAD(P)H motifs, no TPP) is clear. The A vs B distinction, while requiring architectural reasoning, is resolvable: a 360-aa soluble plant protein with a single Rossmann fold is not a plausible Complex I subunit. No two options are equally defensible given the sequence features.


### Important caveats

- The UniProt entry P0DXJ3 was first public on 2025-06-18; the benchmark author's data-construction date is unknown. If the benchmark was constructed before this date, the annotation may not have been available to the author, though the sequence itself was in public databases.
- The exact EC number 1.5.1.32 (vomilenine reductase) is a very specific, recently characterized enzyme. A model selecting this answer likely benefits from training data exposure to this entry rather than pure de novo reasoning.
- The reviewer-only evidence confirms the annotation with experimental evidence codes, but the evaluated model had no access to this information.
- The CAD2-homolog annotation is a family-level assignment; recognizing CAD-family motifs from sequence is general protein-structure knowledge, but linking CAD-family to EC 1.5.1 specifically (rather than EC 1.1.1 for canonical CAD) requires substrate-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)H-binding motif (GGLGHVAVK) and a zinc-binding region (GICHSDLHM), consistent with the medium-chain dehydrogenase/reductase (MDR/CAD) family. This eliminates D (EC 4.1.1.25, pyruvate decarboxylase: TPP-dependent, no NAD(P)H cofactor) and C (EC 1.14.18.1, laccase: requires multi-copper-oxidase HCHH motifs, absent here). Between A and B: the protein is 360 aa, lacks transmembrane helices, has a single NAD(P)H-binding domain, and exhibits plant-specific sequence context — all inconsistent with EC 1.6.5.2 (NADH:ubiquinone oxidoreductase / Complex I subunit), which is a membrane-integrated, highly conserved respiratory-chain component with distinct multi-domain architecture. The soluble, single-domain, plant-biosynthetic reductase architecture favors A over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact 4th digit (32) and even the 3rd digit (1) of EC 1.5.1.32 encode the specific substrate (vomilenine) and reaction chemistry (CH-NH group oxidation), which cannot be deduced from sequence motifs alone. However, within the constrained four-choice set, sequence-based reasoning meaningfully eliminates C and D and provides architectural arguments favoring A over B.",
    "reason": "While the precise 4-digit EC number cannot be derived from sequence features alone (the substrate-specificity encoded in digits 3-4 requires experimental or database knowledge), the multiple-choice format allows reasoning from sequence architecture to eliminate three of four options. NAD(P)H motifs exclude the lyase; absence of copper motifs excludes laccase; small soluble single-domain plant protein architecture is inconsistent with a membrane-bound Complex I subunit. This constitutes meaningful biological reasoning that distinguishes A from the alternatives, even if the exact EC number's specificity is not fully derivable."
  },
  "case_id": "EC_number_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ3 (VOR1_RAUSE, Vomilenine reductase) is annotated with EC 1.5.1.32, supported by experimental evidence codes (ECO:0000269) from two independent publications (PubMed:11937349 and PubMed:38212296). The catalytic reaction is (2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+). Sequence match between the benchmark 360-aa sequence and the UniProt entry is confirmed (SHA256 identical). The annotation is backed by direct experimental characterization, not merely computational transfer."
  },
  "important_caveats": [
    "The UniProt entry P0DXJ3 was first public on 2025-06-18; the benchmark author's data-construction date is unknown. If the benchmark was constructed before this date, the annotation may not have been available to the author, though the sequence itself was in public databases.",
    "The exact EC number 1.5.1.32 (vomilenine reductase) is a very specific, recently characterized enzyme. A model selecting this answer likely benefits from training data exposure to this entry rather than pure de novo reasoning.",
    "The reviewer-only evidence confirms the annotation with experimental evidence codes, but the evaluated model had no access to this information.",
    "The CAD2-homolog annotation is a family-level assignment; recognizing CAD-family motifs from sequence is general protein-structure knowledge, but linking CAD-family to EC 1.5.1 specifically (rather than EC 1.1.1 for canonical CAD) requires substrate-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (1, 4) and different sub-classes (1.5 vs 1.6 vs 1.14 vs 4.1). Sequence-based elimination of C (no copper motifs) and D (has NAD(P)H motifs, no TPP) is clear. The A vs B distinction, while requiring architectural reasoning, is resolvable: a 360-aa soluble plant protein with a single Rossmann fold is not a plausible Complex I subunit. No two options are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ3 (VOR1_RAUSE, Vomilenine reductase) is annotated with EC 1.5.1.32, supported by experimental evidence codes (ECO:0000269) from two independent publications (PubMed:11937349 and PubMed:38212296). The catalytic reaction is (2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+). Sequence match between the benchmark 360-aa sequence and the UniProt entry is confirmed (SHA256 identical). The annotation is backed by direct experimental characterization, not merely computational transfer.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)H-binding motif (GGLGHVAVK) and a zinc-binding region (GICHSDLHM), consistent with the medium-chain dehydrogenase/reductase (MDR/CAD) family. This eliminates D (EC 4.1.1.25, pyruvate decarboxylase: TPP-dependent, no NAD(P)H cofactor) and C (EC 1.14.18.1, laccase: requires multi-copper-oxidase HCHH motifs, absent here). Between A and B: the protein is 360 aa, lacks transmembrane helices, has a single NAD(P)H-binding domain, and exhibits plant-specific sequence context — all inconsistent with EC 1.6.5.2 (NADH:ubiquinone oxidoreductase / Complex I subunit), which is a membrane-integrated, highly conserved respiratory-chain component with distinct multi-domain architecture. The soluble, single-domain, plant-biosynthetic reductase architecture favors A over B.",
    "missing_item_specific_fact": "The exact 4th digit (32) and even the 3rd digit (1) of EC 1.5.1.32 encode the specific substrate (vomilenine) and reaction chemistry (CH-NH group oxidation), which cannot be deduced from sequence motifs alone. However, within the constrained four-choice set, sequence-based reasoning meaningfully eliminates C and D and provides architectural arguments favoring A over B.",
    "reason": "While the precise 4-digit EC number cannot be derived from sequence features alone (the substrate-specificity encoded in digits 3-4 requires experimental or database knowledge), the multiple-choice format allows reasoning from sequence architecture to eliminate three of four options. NAD(P)H motifs exclude the lyase; absence of copper motifs excludes laccase; small soluble single-domain plant protein architecture is inconsistent with a membrane-bound Complex I subunit. This constitutes meaningful biological reasoning that distinguishes A from the alternatives, even if the exact EC number's specificity is not fully derivable."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (1, 4) and different sub-classes (1.5 vs 1.6 vs 1.14 vs 4.1). Sequence-based elimination of C (no copper motifs) and D (has NAD(P)H motifs, no TPP) is clear. The A vs B distinction, while requiring architectural reasoning, is resolvable: a 360-aa soluble plant protein with a single Rossmann fold is not a plausible Complex I subunit. No two options are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt entry P0DXJ3 was first public on 2025-06-18; the benchmark author's data-construction date is unknown. If the benchmark was constructed before this date, the annotation may not have been available to the author, though the sequence itself was in public databases.",
    "The exact EC number 1.5.1.32 (vomilenine reductase) is a very specific, recently characterized enzyme. A model selecting this answer likely benefits from training data exposure to this entry rather than pure de novo reasoning.",
    "The reviewer-only evidence confirms the annotation with experimental evidence codes, but the evaluated model had no access to this information.",
    "The CAD2-homolog annotation is a family-level assignment; recognizing CAD-family motifs from sequence is general protein-structure knowledge, but linking CAD-family to EC 1.5.1 specifically (rather than EC 1.1.1 for canonical CAD) requires substrate-level knowledge."
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

**Accession:** `P0DXJ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
"P0DXJ3"
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"CAD2-homolog protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Protein RR6-2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsRR6-2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11937349","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.5.1.32"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"38212296","source":"PubMed"}],"value":"Vomilenine reductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"38212296","source":"PubMed"}],"value":"RsVR"}]}}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"11937349","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:16411"}}],"reaction":{"ecNumber":"1.5.1.32","evidences":[{"evidenceCode":"ECO:0000269","id":"11937349","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"name":"(2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:16409"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16408"},{"database":"ChEBI","id":"CHEBI:17372"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WKU61927.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"citation":{"authors":["von Schumann G.","Gao S.","Stoeckigt J."],"citationCrossReferences":[{"database":"PubMed","id":"11937349"},{"database":"DOI","id":"10.1016/s0968-0896(01)00435-7"}],"citationType":"journal article","firstPage":"1913","id":"11937349","journal":"Bioorg. Med. Chem.","lastPage":"1918","publicationDate":"2002","title":"Vomilenine reductase--a novel enzyme catalyzing a crucial step in the biosynthesis of the therapeutically applied antiarrhythmic alkaloid ajmaline.","volume":"10"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","ACTIVITY REGULATION","TISSUE SPECIFICITY"]}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.682731+00:00.  

```text
ID   VOR1_RAUSE              Reviewed;         360 AA.
AC   P0DXJ3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};
DE            Short=RsVR {ECO:0000305|PubMed:38212296};
DE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};
DE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};
DE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};
DE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};
GN   Name=VR {ECO:0000305|PubMed:38212296};
GN   Synonyms=RR6-2 {ECO:0000303|PubMed:38212296};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.682731+00:00.  

```text
DE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};
DE            Short=RsVR {ECO:0000305|PubMed:38212296};
DE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};
DE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};
DE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};
DE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};
```

Source SHA-256: `8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)  
**Locator:** `lines 51-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.682731+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH +
CC         H(+); Xref=Rhea:RHEA:16409, ChEBI:CHEBI:15378, ChEBI:CHEBI:16408,
CC         ChEBI:CHEBI:17372, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349; EC=1.5.1.32;
CC         Evidence={ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:16411;
CC         Evidence={ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};
```

Source SHA-256: `8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 167. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
