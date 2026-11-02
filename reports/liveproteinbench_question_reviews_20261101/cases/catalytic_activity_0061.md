# catalytic_activity_0061

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — (1S,3S,6S,7S,8S,9S)-6-&#91;(4-methoxyphenyl)methyl&#93;-3-(methylamino)-5-azatricyclo&#91;6.3.1.0(1,5)&#93;dodecane-7,9-diol + ATP = (-)-FR901483 + ADP + 2 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGTTERESDPIAALILDRLSCTEYACSSLSRVNGGLMNFIYRGTLSRPLPDGATTVIVKHAEEYLSGIEGLSLSTYRSVIAAITLSFGYCVMDVESVQTNRYCVALDEVEVAVPRVYKFDAESNTQILEDITGYITVCEFLTSRCTQSTSPAFTTRLGFRLGSWLGGLHAWGEGRSPAEIIGGVEENQEAQDGSFDFFYGNPVRRVEQFPHLLGDCKEVLEQIRDRAAREQKSRTGEKFGFVHGDILSRKSVLIPGDSVTRDQHLRFVIIDWELSQYECHFRECGEVLGDLYLLKRFQDIDGAMSIIQGFLEGYPPLNEDAIFRTAIYLGLFLLANEVTLSTDYPKQQIEDFVILARDLVLAGWHKDRETLAKTVFGPVFFRAMN

[Multiple Choices]
A. (1S,3S,6S,7S,8S,9S)-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecane-7,9-diol + ATP = (-)-FR901483 + ADP + 2 H(+)
B. spirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2-hydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
C. O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate
D. L-histidine = D-histidine
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

> The supplied sequence exactly matches the UniProt entry annotated as phosphotransferase FrzJ, whose catalytic reaction is choice A. The reaction annotation carries ECO:0000269 and cites a paper whose reference includes function and catalytic activity; this supports the key, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct reaction classes, but the sequence and prompt provide no biological context or sufficiently specific, recognizable feature that identifies FrzJ's particular substrate and product.


**Missing item-specific fact**

> The protein-specific catalytic annotation or experimental identification of FrzJ's reaction with the FR901483 precursor and ATP.


**Reason**

> Selecting the precise reaction requires a protein-specific functional fact absent from the input. A general sequence-based guess about enzyme class would not establish this specific substrate-to-product transformation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options state distinct reactions, and the matched annotation supports choice A; no evidence indicates that another listed reaction is also catalyzed by this protein.


### Important caveats

- The sequence match is exact, and a historical UniProt entry available by the stated cutoff also records choice A.
- The UniProt evidence code and citation support an experimental basis for the annotation, but the cited primary study was not independently examined.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct reaction classes, but the sequence and prompt provide no biological context or sufficiently specific, recognizable feature that identifies FrzJ's particular substrate and product.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental identification of FrzJ's reaction with the FR901483 precursor and ATP.",
    "reason": "Selecting the precise reaction requires a protein-specific functional fact absent from the input. A general sequence-based guess about enzyme class would not establish this specific substrate-to-product transformation."
  },
  "case_id": "catalytic_activity_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as phosphotransferase FrzJ, whose catalytic reaction is choice A. The reaction annotation carries ECO:0000269 and cites a paper whose reference includes function and catalytic activity; this supports the key, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact, and a historical UniProt entry available by the stated cutoff also records choice A.",
    "The UniProt evidence code and citation support an experimental basis for the annotation, but the cited primary study was not independently examined.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options state distinct reactions, and the matched annotation supports choice A; no evidence indicates that another listed reaction is also catalyzed by this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as phosphotransferase FrzJ, whose catalytic reaction is choice A. The reaction annotation carries ECO:0000269 and cites a paper whose reference includes function and catalytic activity; this supports the key, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct reaction classes, but the sequence and prompt provide no biological context or sufficiently specific, recognizable feature that identifies FrzJ's particular substrate and product.",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental identification of FrzJ's reaction with the FR901483 precursor and ATP.",
    "reason": "Selecting the precise reaction requires a protein-specific functional fact absent from the input. A general sequence-based guess about enzyme class would not establish this specific substrate-to-product transformation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options state distinct reactions, and the matched annotation supports choice A; no evidence indicates that another listed reaction is also catalyzed by this protein."
  },
  "important_caveats": [
    "The sequence match is exact, and a historical UniProt entry available by the stated cutoff also records choice A.",
    "The UniProt evidence code and citation support an experimental basis for the annotation, but the cited primary study was not independently examined.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt entry A0A7T8F1J6 (FRZJ_CLASX, Phosphotransferase FrzJ, EC 2.7.1.-). The catalytic activity is annotated with experimental evidence (ECO:0000269|PubMed:33372776, Zhang et al. 2021 JACS) as precisely the reaction in Choice A. Both current and historical (entry version 6) UniProt records confirm the identical reaction string.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly argue by elimination: the sequence lacks a canonical P450 heme-binding motif (CXXGXXC) or ferredoxin-interaction surface expected for a carotenoid hydroxylase (B); it lacks the DXD…GD…HG…GD phosphatase motif of a Ser/Thr protein phosphatase (C); and it lacks PLP-dependent enzyme signatures expected for a histidine racemase (D). A fragment 'HGD' in 'VHGDILSRK' is superficially kinase-like, hinting at a phosphotransferase (A). However, this reasoning is extremely weak and speculative.


**Missing item-specific fact**

> The specific identity of the substrate (the named azatricyclo-dodecane diol) and the product (FR901483) cannot be inferred from the amino acid sequence. Even correctly classifying the enzyme as a kinase does not reveal that it phosphorylates this particular exotic natural-product precursor in the FR901483 biosynthetic pathway. This requires the item-specific annotation of FrzJ from the 2021 JACS paper.


**Reason**

> The positive identification of the exact reaction—specifically the exotic named substrate and FR901483 product—depends entirely on knowing the protein's database annotation or the published biosynthetic pathway. General sequence-based reasoning cannot predict that a 385-residue fungal phosphotransferase acts on this particular complex organic molecule. The elimination of distractors B, C, D by motif absence is suggestive but insufficient for confident positive identification of A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span fundamentally different enzyme classes (kinase, carotenoid hydroxylase, protein phosphatase, racemase), making them structurally distinct. The correct answer is unambiguous given the annotation; the distractors are not genuinely competitive once the enzyme class is known.


### Important caveats

- The UniProt entry was first public in June 2025 and the experimental paper is from 2021; the annotation carries experimental evidence (ECO:0000269), not merely computational inference.
- The sequence match between the benchmark input and the UniProt entry is confirmed by SHA-256 hash.
- The identity origin (accession inferred from dataset image-path metadata) is reviewer-only and was absent from the evaluated model input.
- While weak motif-based elimination of B, C, D is possible, it does not constitute reliable reasoning to positively select A over any other phosphotransferase reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly argue by elimination: the sequence lacks a canonical P450 heme-binding motif (CXXGXXC) or ferredoxin-interaction surface expected for a carotenoid hydroxylase (B); it lacks the DXD…GD…HG…GD phosphatase motif of a Ser/Thr protein phosphatase (C); and it lacks PLP-dependent enzyme signatures expected for a histidine racemase (D). A fragment 'HGD' in 'VHGDILSRK' is superficially kinase-like, hinting at a phosphotransferase (A). However, this reasoning is extremely weak and speculative.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of the substrate (the named azatricyclo-dodecane diol) and the product (FR901483) cannot be inferred from the amino acid sequence. Even correctly classifying the enzyme as a kinase does not reveal that it phosphorylates this particular exotic natural-product precursor in the FR901483 biosynthetic pathway. This requires the item-specific annotation of FrzJ from the 2021 JACS paper.",
    "reason": "The positive identification of the exact reaction—specifically the exotic named substrate and FR901483 product—depends entirely on knowing the protein's database annotation or the published biosynthetic pathway. General sequence-based reasoning cannot predict that a 385-residue fungal phosphotransferase acts on this particular complex organic molecule. The elimination of distractors B, C, D by motif absence is suggestive but insufficient for confident positive identification of A."
  },
  "case_id": "catalytic_activity_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A0A7T8F1J6 (FRZJ_CLASX, Phosphotransferase FrzJ, EC 2.7.1.-). The catalytic activity is annotated with experimental evidence (ECO:0000269|PubMed:33372776, Zhang et al. 2021 JACS) as precisely the reaction in Choice A. Both current and historical (entry version 6) UniProt records confirm the identical reaction string."
  },
  "important_caveats": [
    "The UniProt entry was first public in June 2025 and the experimental paper is from 2021; the annotation carries experimental evidence (ECO:0000269), not merely computational inference.",
    "The sequence match between the benchmark input and the UniProt entry is confirmed by SHA-256 hash.",
    "The identity origin (accession inferred from dataset image-path metadata) is reviewer-only and was absent from the evaluated model input.",
    "While weak motif-based elimination of B, C, D is possible, it does not constitute reliable reasoning to positively select A over any other phosphotransferase reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span fundamentally different enzyme classes (kinase, carotenoid hydroxylase, protein phosphatase, racemase), making them structurally distinct. The correct answer is unambiguous given the annotation; the distractors are not genuinely competitive once the enzyme class is known."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A0A7T8F1J6 (FRZJ_CLASX, Phosphotransferase FrzJ, EC 2.7.1.-). The catalytic activity is annotated with experimental evidence (ECO:0000269|PubMed:33372776, Zhang et al. 2021 JACS) as precisely the reaction in Choice A. Both current and historical (entry version 6) UniProt records confirm the identical reaction string.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly argue by elimination: the sequence lacks a canonical P450 heme-binding motif (CXXGXXC) or ferredoxin-interaction surface expected for a carotenoid hydroxylase (B); it lacks the DXD…GD…HG…GD phosphatase motif of a Ser/Thr protein phosphatase (C); and it lacks PLP-dependent enzyme signatures expected for a histidine racemase (D). A fragment 'HGD' in 'VHGDILSRK' is superficially kinase-like, hinting at a phosphotransferase (A). However, this reasoning is extremely weak and speculative.",
    "missing_item_specific_fact": "The specific identity of the substrate (the named azatricyclo-dodecane diol) and the product (FR901483) cannot be inferred from the amino acid sequence. Even correctly classifying the enzyme as a kinase does not reveal that it phosphorylates this particular exotic natural-product precursor in the FR901483 biosynthetic pathway. This requires the item-specific annotation of FrzJ from the 2021 JACS paper.",
    "reason": "The positive identification of the exact reaction—specifically the exotic named substrate and FR901483 product—depends entirely on knowing the protein's database annotation or the published biosynthetic pathway. General sequence-based reasoning cannot predict that a 385-residue fungal phosphotransferase acts on this particular complex organic molecule. The elimination of distractors B, C, D by motif absence is suggestive but insufficient for confident positive identification of A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span fundamentally different enzyme classes (kinase, carotenoid hydroxylase, protein phosphatase, racemase), making them structurally distinct. The correct answer is unambiguous given the annotation; the distractors are not genuinely competitive once the enzyme class is known."
  },
  "important_caveats": [
    "The UniProt entry was first public in June 2025 and the experimental paper is from 2021; the annotation carries experimental evidence (ECO:0000269), not merely computational inference.",
    "The sequence match between the benchmark input and the UniProt entry is confirmed by SHA-256 hash.",
    "The identity origin (accession inferred from dataset image-path metadata) is reviewer-only and was absent from the evaluated model input.",
    "While weak motif-based elimination of B, C, D is possible, it does not constitute reliable reasoning to positively select A over any other phosphotransferase reaction."
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

**Accession:** `A0A7T8F1J6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 6. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.675828+00:00.  

```json
"A0A7T8F1J6"
```

Source SHA-256: `c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.675828+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis clusters protein J"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"2.7.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Phosphotransferase FrzJ"}}}
```

Source SHA-256: `c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.675828+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:83616"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"name":"(1S,3S,6S,7S,8S,9S)-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecane-7,9-diol + ATP = (-)-FR901483 + ADP + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:83615"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:233173"},{"database":"ChEBI","id":"CHEBI:233182"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.675828+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Tamura Y.","Tang M.","Qiao T.","Sato M.","Otsu Y.","Sasamura S.","Taniguchi M.","Watanabe K.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33372776"},{"database":"DOI","id":"10.1021/jacs.0c12352"}],"citationType":"journal article","firstPage":"132","id":"33372776","journal":"J. Am. Chem. Soc.","lastPage":"136","publicationDate":"2021","title":"Biosynthesis of the Immunosuppressant (-)-FR901483.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"11231"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1J6?format=txt&versions=6)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-01T06:27:33.489845+00:00.  

```text
ID   FRZJ_CLASX              Reviewed;         385 AA.
AC   A0A7T8F1J6;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-JUN-2021, sequence version 1.
DT   28-JAN-2026, entry version 6.
DE   RecName: Full=Phosphotransferase FrzJ {ECO:0000303|PubMed:33372776};
DE            EC=2.7.1.- {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis clusters protein J {ECO:0000303|PubMed:33372776};
GN   Name=FrzJ {ECO:0000303|PubMed:33372776};
OS   Cladobotryum sp.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.
OX   NCBI_TaxID=2040732;
```

Source SHA-256: `a3c8964073737ce02aefe4d7b1c7dc5803711f2bade9edceed980e3bae3f99f8`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1J6?format=txt&versions=6)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-01T06:27:33.489845+00:00.  

```text
DE   RecName: Full=Phosphotransferase FrzJ {ECO:0000303|PubMed:33372776};
DE            EC=2.7.1.- {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis clusters protein J {ECO:0000303|PubMed:33372776};
```

Source SHA-256: `a3c8964073737ce02aefe4d7b1c7dc5803711f2bade9edceed980e3bae3f99f8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1J6?format=txt&versions=6)  
**Locator:** `lines 14-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-01T06:27:33.489845+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND
RP   PATHWAY.
RC   STRAIN=11231;
RX   PubMed=33372776; DOI=10.1021/jacs.0c12352;
RA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,
RA   Taniguchi M., Watanabe K., Tang Y.;
RT   "Biosynthesis of the Immunosuppressant (-)-FR901483.";
RL   J. Am. Chem. Soc. 143:132-136(2021).
```

Source SHA-256: `a3c8964073737ce02aefe4d7b1c7dc5803711f2bade9edceed980e3bae3f99f8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1J6?format=txt&versions=6)  
**Locator:** `lines 53-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-01T06:27:33.489845+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(1S,3S,6S,7S,8S,9S)-6-[(4-methoxyphenyl)methyl]-3-
CC         (methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecane-7,9-diol + ATP =
CC         (-)-FR901483 + ADP + 2 H(+); Xref=Rhea:RHEA:83615, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:233173, ChEBI:CHEBI:233182,
CC         ChEBI:CHEBI:456216; Evidence={ECO:0000269|PubMed:33372776};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83616;
CC         Evidence={ECO:0000269|PubMed:33372776};
```

Source SHA-256: `a3c8964073737ce02aefe4d7b1c7dc5803711f2bade9edceed980e3bae3f99f8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 61. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
