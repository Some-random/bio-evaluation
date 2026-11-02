# catalytic_activity_0133

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1-&gt;4)-beta-linkages in chitin and chitodextrins.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLLYLVALFVASICSVTAQTWTSCNPLTTTCPPDQALGINTTFTFNKTLDDTIWNVTNGVLSHTDEGTEFTITGENQSPTMQSNFYIFFGIVESHVKMAKGAGIISSIVLQSDDLDEIDWEWVGYNTSEVQSNYFGKGNNETFNRGGYHYVPNADTEFHNYTTYWTQEKLEWWIDGKLARTLTYEDSQGAGKYYPQTPCNIRYGIWPAGIKGNAQGTIEWAGGLVDYSKAPFTMVLQSVRVHDFHTGKEYNYTDHSGSWQSIDVIAGNSTIANAIQNPPKSLSEKWAELPTGAKAGVYIGAGCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN

[Multiple Choices]
A. Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides.
B. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
C. 2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O
D. Fe(2+)(in) = Fe(2+)(out)
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

> The sequence-matched UniProt entry annotates this protein with the exact reaction in choice B. The annotation cites a publication, although its evidence code is a manual assertion rather than, by itself, proof of a direct experimental measurement.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The signal-peptide-like N-terminus and hydrophobic C-terminal region suggest a secreted or membrane-associated protein, but those features do not establish that it hydrolyzes chitin rather than another substrate.


**Missing item-specific fact**

> The protein-specific functional annotation or characterization identifying Crh3 as having chitinase activity is absent from the input.


**Reason**

> Choosing B depends on identifying the particular protein's function. The sequence alone, without recognizing a specific family or accessing its annotation, does not reliably distinguish the precise reaction from the other glycosidase option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, B matches the sequence-matched catalytic-activity annotation. The protein is also annotated as a chitin transglycosylase, but that additional activity is not one of the choices.


### Important caveats

- The reviewer-only sequence match supports applying the annotation to this sequence; the accession and annotation were not supplied to the evaluated model.
- The cited annotation does not alone establish the experimental basis or conditions for the hydrolysis activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The signal-peptide-like N-terminus and hydrophobic C-terminal region suggest a secreted or membrane-associated protein, but those features do not establish that it hydrolyzes chitin rather than another substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or characterization identifying Crh3 as having chitinase activity is absent from the input.",
    "reason": "Choosing B depends on identifying the particular protein's function. The sequence alone, without recognizing a specific family or accessing its annotation, does not reliably distinguish the precise reaction from the other glycosidase option."
  },
  "case_id": "catalytic_activity_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein with the exact reaction in choice B. The annotation cites a publication, although its evidence code is a manual assertion rather than, by itself, proof of a direct experimental measurement."
  },
  "important_caveats": [
    "The reviewer-only sequence match supports applying the annotation to this sequence; the accession and annotation were not supplied to the evaluated model.",
    "The cited annotation does not alone establish the experimental basis or conditions for the hydrolysis activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B matches the sequence-matched catalytic-activity annotation. The protein is also annotated as a chitin transglycosylase, but that additional activity is not one of the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein with the exact reaction in choice B. The annotation cites a publication, although its evidence code is a manual assertion rather than, by itself, proof of a direct experimental measurement.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The signal-peptide-like N-terminus and hydrophobic C-terminal region suggest a secreted or membrane-associated protein, but those features do not establish that it hydrolyzes chitin rather than another substrate.",
    "missing_item_specific_fact": "The protein-specific functional annotation or characterization identifying Crh3 as having chitinase activity is absent from the input.",
    "reason": "Choosing B depends on identifying the particular protein's function. The sequence alone, without recognizing a specific family or accessing its annotation, does not reliably distinguish the precise reaction from the other glycosidase option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B matches the sequence-matched catalytic-activity annotation. The protein is also annotated as a chitin transglycosylase, but that additional activity is not one of the choices."
  },
  "important_caveats": [
    "The reviewer-only sequence match supports applying the annotation to this sequence; the accession and annotation were not supplied to the evaluated model.",
    "The cited annotation does not alone establish the experimental basis or conditions for the hydrolysis activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 363-aa sequence exactly matches UniProt Q4WXE6 (CRH3_ASPFU, Aspergillus fumigatus). The entry annotates a CATALYTIC ACTIVITY comment stating 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' (EC 3.2.1.14), which is verbatim Choice B. The evidence code for this EC assignment is ECO:0000305 (inferred from electronic annotation), while the protein name is supported by ECO:0000303 from PubMed:30971696. Notably, the same entry also annotates a chitin transglycosylase activity (EC 2.4.-.-, ECO:0000269, inferred from direct assay) for the same protein, meaning the experimentally demonstrated activity is transglycosylase and the chitinase assignment is computationally inferred. Nevertheless, the annotation explicitly supports Choice B.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains features broadly consistent with a glycoside hydrolase (e.g., a hydrophobic N-terminal signal peptide, a C-terminal transmembrane anchor, and internal regions with partial similarity to the GH18 DXXDXDXE catalytic motif such as 'DWEWVGYNTSEV'). These features could help a knowledgeable model narrow from four choices to two glycoside-hydrolase options (A and B). However, distinguishing arabinofuranosidase (GH43/GH51/GH54 families, Choice A) from chitinase (GH18 family, Choice B) requires recognizing specific family-level catalytic motifs and domain architectures that are not unambiguously resolvable from this sequence by general first-principles reasoning.


**Missing item-specific fact**

> The specific protein-family assignment (GH18 chitinase vs. GH43/GH51/GH54 arabinofuranosidase) and the particular catalytic motif topology that definitively distinguishes the two glycoside-hydrolase options. The GH18 DXXDXDXE motif is only partially and ambiguously present in the supplied sequence, so family-level identification relies on pattern recognition of this specific sequence rather than deductive reasoning from general biochemistry.


**Reason**

> Choices C (FMN-dependent indigoidine synthetase) and D (iron transporter) are trivially eliminable by any model recognizing the absence of FMN-binding or metal-transport motifs. The real discrimination is between A and B, both plausible glycoside hydrolases. The sequence does not present a textbook-perfect, unambiguous GH18 catalytic motif; resolving A vs. B effectively requires recognizing this protein's family or memorizing its annotation, which constitutes lookup/memorization dependence rather than general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices C and D are clearly unrelated to the sequence (no FMN-binding, no transmembrane iron-transport architecture). Between A and B, the UniProt annotation unambiguously assigns chitinase activity (EC 3.2.1.14) and not arabinofuranosidase activity, so only B is supported. The co-annotated transglycosylase activity (EC 2.4.-.-) is not among the choices, so it does not introduce ambiguity within the provided options.


### Important caveats

- The chitinase EC assignment (3.2.1.14) carries evidence code ECO:0000305 (inferred from electronic annotation), not direct experimental evidence. The experimentally demonstrated activity (ECO:0000269) is chitin transglycosylase (EC 2.4.-.-), which is not among the answer choices.
- The 2019 Fang et al. paper (PubMed:30971696, Nat. Commun.) characterizes Crh transglycosylases and their redundancy/specificity in A. fumigatus cell-wall remodeling; the chitinase activity annotation may reflect computational transfer rather than a dedicated hydrolysis assay.
- The reviewer-only evidence confirms sequence identity (SHA-256 match) and annotation, but the evaluated model had no access to UniProt or the primary publication.
- The protein is a precursor (signal peptide + transmembrane anchor), meaning the mature catalytic domain is a subset of the supplied sequence, which further complicates motif identification from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features broadly consistent with a glycoside hydrolase (e.g., a hydrophobic N-terminal signal peptide, a C-terminal transmembrane anchor, and internal regions with partial similarity to the GH18 DXXDXDXE catalytic motif such as 'DWEWVGYNTSEV'). These features could help a knowledgeable model narrow from four choices to two glycoside-hydrolase options (A and B). However, distinguishing arabinofuranosidase (GH43/GH51/GH54 families, Choice A) from chitinase (GH18 family, Choice B) requires recognizing specific family-level catalytic motifs and domain architectures that are not unambiguously resolvable from this sequence by general first-principles reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific protein-family assignment (GH18 chitinase vs. GH43/GH51/GH54 arabinofuranosidase) and the particular catalytic motif topology that definitively distinguishes the two glycoside-hydrolase options. The GH18 DXXDXDXE motif is only partially and ambiguously present in the supplied sequence, so family-level identification relies on pattern recognition of this specific sequence rather than deductive reasoning from general biochemistry.",
    "reason": "Choices C (FMN-dependent indigoidine synthetase) and D (iron transporter) are trivially eliminable by any model recognizing the absence of FMN-binding or metal-transport motifs. The real discrimination is between A and B, both plausible glycoside hydrolases. The sequence does not present a textbook-perfect, unambiguous GH18 catalytic motif; resolving A vs. B effectively requires recognizing this protein's family or memorizing its annotation, which constitutes lookup/memorization dependence rather than general biological reasoning."
  },
  "case_id": "catalytic_activity_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 363-aa sequence exactly matches UniProt Q4WXE6 (CRH3_ASPFU, Aspergillus fumigatus). The entry annotates a CATALYTIC ACTIVITY comment stating 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' (EC 3.2.1.14), which is verbatim Choice B. The evidence code for this EC assignment is ECO:0000305 (inferred from electronic annotation), while the protein name is supported by ECO:0000303 from PubMed:30971696. Notably, the same entry also annotates a chitin transglycosylase activity (EC 2.4.-.-, ECO:0000269, inferred from direct assay) for the same protein, meaning the experimentally demonstrated activity is transglycosylase and the chitinase assignment is computationally inferred. Nevertheless, the annotation explicitly supports Choice B."
  },
  "important_caveats": [
    "The chitinase EC assignment (3.2.1.14) carries evidence code ECO:0000305 (inferred from electronic annotation), not direct experimental evidence. The experimentally demonstrated activity (ECO:0000269) is chitin transglycosylase (EC 2.4.-.-), which is not among the answer choices.",
    "The 2019 Fang et al. paper (PubMed:30971696, Nat. Commun.) characterizes Crh transglycosylases and their redundancy/specificity in A. fumigatus cell-wall remodeling; the chitinase activity annotation may reflect computational transfer rather than a dedicated hydrolysis assay.",
    "The reviewer-only evidence confirms sequence identity (SHA-256 match) and annotation, but the evaluated model had no access to UniProt or the primary publication.",
    "The protein is a precursor (signal peptide + transmembrane anchor), meaning the mature catalytic domain is a subset of the supplied sequence, which further complicates motif identification from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices C and D are clearly unrelated to the sequence (no FMN-binding, no transmembrane iron-transport architecture). Between A and B, the UniProt annotation unambiguously assigns chitinase activity (EC 3.2.1.14) and not arabinofuranosidase activity, so only B is supported. The co-annotated transglycosylase activity (EC 2.4.-.-) is not among the choices, so it does not introduce ambiguity within the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 363-aa sequence exactly matches UniProt Q4WXE6 (CRH3_ASPFU, Aspergillus fumigatus). The entry annotates a CATALYTIC ACTIVITY comment stating 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' (EC 3.2.1.14), which is verbatim Choice B. The evidence code for this EC assignment is ECO:0000305 (inferred from electronic annotation), while the protein name is supported by ECO:0000303 from PubMed:30971696. Notably, the same entry also annotates a chitin transglycosylase activity (EC 2.4.-.-, ECO:0000269, inferred from direct assay) for the same protein, meaning the experimentally demonstrated activity is transglycosylase and the chitinase assignment is computationally inferred. Nevertheless, the annotation explicitly supports Choice B.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains features broadly consistent with a glycoside hydrolase (e.g., a hydrophobic N-terminal signal peptide, a C-terminal transmembrane anchor, and internal regions with partial similarity to the GH18 DXXDXDXE catalytic motif such as 'DWEWVGYNTSEV'). These features could help a knowledgeable model narrow from four choices to two glycoside-hydrolase options (A and B). However, distinguishing arabinofuranosidase (GH43/GH51/GH54 families, Choice A) from chitinase (GH18 family, Choice B) requires recognizing specific family-level catalytic motifs and domain architectures that are not unambiguously resolvable from this sequence by general first-principles reasoning.",
    "missing_item_specific_fact": "The specific protein-family assignment (GH18 chitinase vs. GH43/GH51/GH54 arabinofuranosidase) and the particular catalytic motif topology that definitively distinguishes the two glycoside-hydrolase options. The GH18 DXXDXDXE motif is only partially and ambiguously present in the supplied sequence, so family-level identification relies on pattern recognition of this specific sequence rather than deductive reasoning from general biochemistry.",
    "reason": "Choices C (FMN-dependent indigoidine synthetase) and D (iron transporter) are trivially eliminable by any model recognizing the absence of FMN-binding or metal-transport motifs. The real discrimination is between A and B, both plausible glycoside hydrolases. The sequence does not present a textbook-perfect, unambiguous GH18 catalytic motif; resolving A vs. B effectively requires recognizing this protein's family or memorizing its annotation, which constitutes lookup/memorization dependence rather than general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices C and D are clearly unrelated to the sequence (no FMN-binding, no transmembrane iron-transport architecture). Between A and B, the UniProt annotation unambiguously assigns chitinase activity (EC 3.2.1.14) and not arabinofuranosidase activity, so only B is supported. The co-annotated transglycosylase activity (EC 2.4.-.-) is not among the choices, so it does not introduce ambiguity within the provided options."
  },
  "important_caveats": [
    "The chitinase EC assignment (3.2.1.14) carries evidence code ECO:0000305 (inferred from electronic annotation), not direct experimental evidence. The experimentally demonstrated activity (ECO:0000269) is chitin transglycosylase (EC 2.4.-.-), which is not among the answer choices.",
    "The 2019 Fang et al. paper (PubMed:30971696, Nat. Commun.) characterizes Crh transglycosylases and their redundancy/specificity in A. fumigatus cell-wall remodeling; the chitinase activity annotation may reflect computational transfer rather than a dedicated hydrolysis assay.",
    "The reviewer-only evidence confirms sequence identity (SHA-256 match) and annotation, but the evaluated model had no access to UniProt or the primary publication.",
    "The protein is a precursor (signal peptide + transmembrane anchor), meaning the mature catalytic domain is a subset of the supplied sequence, which further complicates motif identification from the raw sequence alone."
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

**Accession:** `Q4WXE6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 98. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.355475+00:00.  

```json
"Q4WXE6"
```

Source SHA-256: `e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.355475+00:00.  

```json
{"flag":"Precursor","includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30971696","source":"PubMed"}],"value":"3.2.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Chitinase crh3"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30971696","source":"PubMed"}],"value":"2.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Chitin transglycosylase crh3"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Crh-like protein 3"}}}
```

Source SHA-256: `e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.355475+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.14","evidences":[{"evidenceCode":"ECO:0000305","id":"30971696","source":"PubMed"}],"name":"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins."}}
```

Source SHA-256: `e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)  
**Locator:** `lines 1-20`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 2.  
**Retrieved:** 2026-11-02T04:31:00.140024+00:00.  

```text
ID   CRH3_ASPFU              Reviewed;         363 AA.
AC   Q4WXE6;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   17-APR-2007, sequence version 2.
DT   28-JAN-2026, entry version 98.
DE   RecName: Full=Crh-like protein 3 {ECO:0000303|PubMed:30971696};
DE   Includes:
DE     RecName: Full=Chitinase crh3 {ECO:0000303|PubMed:30971696};
DE              EC=3.2.1.14 {ECO:0000305|PubMed:30971696};
DE   Includes:
DE     RecName: Full=Chitin transglycosylase crh3 {ECO:0000303|PubMed:30971696};
DE              EC=2.4.-.- {ECO:0000269|PubMed:30971696};
DE   Flags: Precursor;
GN   Name=crh3 {ECO:0000303|PubMed:30971696}; ORFNames=AFUA_3G09250;
OS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /
OS   Af293) (Neosartorya fumigata).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Fumigati.
OX   NCBI_TaxID=330879;
```

Source SHA-256: `af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)  
**Locator:** `lines 61-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 2.  
**Retrieved:** 2026-11-02T04:31:00.140024+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide
CC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;
CC         Evidence={ECO:0000305|PubMed:30971696};
```

Source SHA-256: `af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
