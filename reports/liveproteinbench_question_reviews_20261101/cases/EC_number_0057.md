# EC_number_0057

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.2.1.11

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTPSKKRCGVLGATGAVGTRFILLLEQSPLLELVAVGASERSAGKKYRDAVRWKQASPMPASVADLTVRRCAPSEFSDCDIIFSGLDPVAAGDIEMAFLKANFAVFSNAKNYRLDPIVPLVVPLVNAGHIDVIPAQRKHYGLDKGLIVCNSNCAVVGLVIPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPFIPGEEGKIATESRKILGNLNPDLAGFSDQQPLQVSVACNRVPVLDGHTVCASLRFVNRPAPTASQVRDALREYKSEVQLLGCPSAPRQAIHVLDDVDRPQPRLDRDTEAGYACSVGRIREDDSGVFDIQFVALSHNTVLGASGSSILNAESAILKGYI

[Multiple Choices]
A. 1.2.1.46
B. 2.7.8.7
C. 2.3.1.31
D. 1.2.1.11
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

> The supplied sequence exactly matches the reviewed UniProt sequence annotated as aspartate-semialdehyde dehydrogenase, EC 1.2.1.11. The catalytic activity annotation cites experimental evidence (ECO:0000269) for the reaction corresponding to that EC number, so choice D is supported for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may permit homology-based identification of an enzyme family, but the input supplies no organism, functional annotation, or reaction data that establish this specific enzyme's substrate and EC classification.


**Missing item-specific fact**

> The protein-specific identification as aspartate-semialdehyde dehydrogenase, or evidence for its catalyzed reaction, is needed to select EC 1.2.1.11 over the alternatives.


**Reason**

> The correct option is supported by reviewer-only sequence-matched annotation and cited experimental evidence, but that information is absent from the evaluated input. Inferring the exact EC classification would depend on protein-specific functional identification, not a general biological deduction from the choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation and catalytic activity evidence support D; the supplied evidence does not support another listed option.


### Important caveats

- The UniProt EC annotation cites experimental evidence, but the cited primary papers were not independently retrieved or validated here.
- The sequence match is exact in both the current entry and the historical entry checked; the author's actual source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may permit homology-based identification of an enzyme family, but the input supplies no organism, functional annotation, or reaction data that establish this specific enzyme's substrate and EC classification.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as aspartate-semialdehyde dehydrogenase, or evidence for its catalyzed reaction, is needed to select EC 1.2.1.11 over the alternatives.",
    "reason": "The correct option is supported by reviewer-only sequence-matched annotation and cited experimental evidence, but that information is absent from the evaluated input. Inferring the exact EC classification would depend on protein-specific functional identification, not a general biological deduction from the choices alone."
  },
  "case_id": "EC_number_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence annotated as aspartate-semialdehyde dehydrogenase, EC 1.2.1.11. The catalytic activity annotation cites experimental evidence (ECO:0000269) for the reaction corresponding to that EC number, so choice D is supported for this sequence."
  },
  "important_caveats": [
    "The UniProt EC annotation cites experimental evidence, but the cited primary papers were not independently retrieved or validated here.",
    "The sequence match is exact in both the current entry and the historical entry checked; the author's actual source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and catalytic activity evidence support D; the supplied evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence annotated as aspartate-semialdehyde dehydrogenase, EC 1.2.1.11. The catalytic activity annotation cites experimental evidence (ECO:0000269) for the reaction corresponding to that EC number, so choice D is supported for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may permit homology-based identification of an enzyme family, but the input supplies no organism, functional annotation, or reaction data that establish this specific enzyme's substrate and EC classification.",
    "missing_item_specific_fact": "The protein-specific identification as aspartate-semialdehyde dehydrogenase, or evidence for its catalyzed reaction, is needed to select EC 1.2.1.11 over the alternatives.",
    "reason": "The correct option is supported by reviewer-only sequence-matched annotation and cited experimental evidence, but that information is absent from the evaluated input. Inferring the exact EC classification would depend on protein-specific functional identification, not a general biological deduction from the choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and catalytic activity evidence support D; the supplied evidence does not support another listed option."
  },
  "important_caveats": [
    "The UniProt EC annotation cites experimental evidence, but the cited primary papers were not independently retrieved or validated here.",
    "The sequence match is exact in both the current entry and the historical entry checked; the author's actual source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> The UniProt entry A0A179UL48 (sequence SHA256 matched, 362 aa) annotates this protein as Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, with experimental evidence codes ECO:0000269 (PubMed) from two independent studies (PMID 29608391, 30107909) and X-ray crystallography at 2.4 Å in complex with inhibitor and NADP+ (PDB 6C85, 6C8W). The catalytic activity (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is confirmed experimentally. The annotation is not merely computational; it is backed by functional assays and structural characterization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal motif 'CGVLGATGAVGTR' is a classic Rossmann-fold nucleotide-binding signature (GxGxxG), indicating an NAD(P)+-dependent oxidoreductase (EC 1.x.x.x). The 'GDI' motif at ~residue 100 ('GDIEMAFL') together with a catalytic cysteine is characteristic of the aldehyde dehydrogenase superfamily (EC 1.2.x.x). Critically, the GDI motif is a hallmark of aspartate-semialdehyde dehydrogenase specifically: in ASADH, the second catalytic step uses inorganic phosphate (rather than water) as the nucleophile to form 4-phospho-L-aspartate, and the GDI region is part of the phosphate-binding/substrate-specificity pocket. General aldehyde dehydrogenases (EC 1.2.1.46) hydrolyze the thioacyl intermediate with water and lack the phosphate-acceptor architecture encoded by this motif context. The overall ~362-residue homodimeric fold and the specific arrangement of substrate-binding residues (amino-acid recognition pocket for the aspartate moiety) further favor EC 1.2.1.11 over the generic EC 1.2.1.46. Options B (2.7.8.7, a transferase) and C (2.3.1.31, a transferase) are readily excluded by the oxidoreductase architecture.


**Missing item-specific fact**

> None that is strictly indispensable. The GDI motif and phosphate-acceptor architecture are recognizable from sequence to a knowledgeable enzymologist, though the distinction from EC 1.2.1.46 requires familiarity with ASADH active-site architecture beyond generic aldehyde dehydrogenase motifs.


**Reason**

> The sequence provides identifiable Rossmann-fold, catalytic Cys, and GDI-motif features that allow a trained biologist to reason toward EC 1.2.1.11 specifically rather than the generic EC 1.2.1.46. The GDI motif's role in phosphate-dependent (rather than hydrolytic) resolution of the thioacyl intermediate is a concrete mechanistic argument distinguishing ASADH from general aldehyde dehydrogenases. While the distinction is non-trivial, it rests on general enzymology rather than a single memorized database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (1.2.1.46)"
]
```

> EC 1.2.1.46 (aldehyde dehydrogenase, NADP+) is a closely related general aldehyde dehydrogenase that shares the Rossmann fold and catalytic Cys. Without detailed active-site mapping, a model could argue for the general EC 1.2.1.46. However, the GDI motif and phosphate-acceptor architecture provide a defensible basis for preferring the specific ASADH assignment (D). The ambiguity is mild; the sequence features do favor D over A for a knowledgeable reader.


### Important caveats

- The reviewer-only UniProt annotation confirms EC 1.2.1.11 with experimental evidence (PubMed, PDB), but this annotation was not available to the evaluated model.
- The distinction between EC 1.2.1.46 and EC 1.2.1.11 from raw sequence alone is challenging; the GDI-motif argument is sound but requires specialized knowledge of ASADH catalytic mechanism.
- The sequence-match is exact (SHA256 identical) between the benchmark input and the UniProt entry A0A179UL48.
- EC 1.2.1.46 is a valid EC number (aldehyde dehydrogenase NADP+), making it a plausible but less specific distractor rather than an obviously wrong answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal motif 'CGVLGATGAVGTR' is a classic Rossmann-fold nucleotide-binding signature (GxGxxG), indicating an NAD(P)+-dependent oxidoreductase (EC 1.x.x.x). The 'GDI' motif at ~residue 100 ('GDIEMAFL') together with a catalytic cysteine is characteristic of the aldehyde dehydrogenase superfamily (EC 1.2.x.x). Critically, the GDI motif is a hallmark of aspartate-semialdehyde dehydrogenase specifically: in ASADH, the second catalytic step uses inorganic phosphate (rather than water) as the nucleophile to form 4-phospho-L-aspartate, and the GDI region is part of the phosphate-binding/substrate-specificity pocket. General aldehyde dehydrogenases (EC 1.2.1.46) hydrolyze the thioacyl intermediate with water and lack the phosphate-acceptor architecture encoded by this motif context. The overall ~362-residue homodimeric fold and the specific arrangement of substrate-binding residues (amino-acid recognition pocket for the aspartate moiety) further favor EC 1.2.1.11 over the generic EC 1.2.1.46. Options B (2.7.8.7, a transferase) and C (2.3.1.31, a transferase) are readily excluded by the oxidoreductase architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is strictly indispensable. The GDI motif and phosphate-acceptor architecture are recognizable from sequence to a knowledgeable enzymologist, though the distinction from EC 1.2.1.46 requires familiarity with ASADH active-site architecture beyond generic aldehyde dehydrogenase motifs.",
    "reason": "The sequence provides identifiable Rossmann-fold, catalytic Cys, and GDI-motif features that allow a trained biologist to reason toward EC 1.2.1.11 specifically rather than the generic EC 1.2.1.46. The GDI motif's role in phosphate-dependent (rather than hydrolytic) resolution of the thioacyl intermediate is a concrete mechanistic argument distinguishing ASADH from general aldehyde dehydrogenases. While the distinction is non-trivial, it rests on general enzymology rather than a single memorized database entry."
  },
  "case_id": "EC_number_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A179UL48 (sequence SHA256 matched, 362 aa) annotates this protein as Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, with experimental evidence codes ECO:0000269 (PubMed) from two independent studies (PMID 29608391, 30107909) and X-ray crystallography at 2.4 Å in complex with inhibitor and NADP+ (PDB 6C85, 6C8W). The catalytic activity (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is confirmed experimentally. The annotation is not merely computational; it is backed by functional assays and structural characterization."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation confirms EC 1.2.1.11 with experimental evidence (PubMed, PDB), but this annotation was not available to the evaluated model.",
    "The distinction between EC 1.2.1.46 and EC 1.2.1.11 from raw sequence alone is challenging; the GDI-motif argument is sound but requires specialized knowledge of ASADH catalytic mechanism.",
    "The sequence-match is exact (SHA256 identical) between the benchmark input and the UniProt entry A0A179UL48.",
    "EC 1.2.1.46 is a valid EC number (aldehyde dehydrogenase NADP+), making it a plausible but less specific distractor rather than an obviously wrong answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (1.2.1.46)"
    ],
    "reason": "EC 1.2.1.46 (aldehyde dehydrogenase, NADP+) is a closely related general aldehyde dehydrogenase that shares the Rossmann fold and catalytic Cys. Without detailed active-site mapping, a model could argue for the general EC 1.2.1.46. However, the GDI motif and phosphate-acceptor architecture provide a defensible basis for preferring the specific ASADH assignment (D). The ambiguity is mild; the sequence features do favor D over A for a knowledgeable reader."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A179UL48 (sequence SHA256 matched, 362 aa) annotates this protein as Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, with experimental evidence codes ECO:0000269 (PubMed) from two independent studies (PMID 29608391, 30107909) and X-ray crystallography at 2.4 Å in complex with inhibitor and NADP+ (PDB 6C85, 6C8W). The catalytic activity (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is confirmed experimentally. The annotation is not merely computational; it is backed by functional assays and structural characterization.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal motif 'CGVLGATGAVGTR' is a classic Rossmann-fold nucleotide-binding signature (GxGxxG), indicating an NAD(P)+-dependent oxidoreductase (EC 1.x.x.x). The 'GDI' motif at ~residue 100 ('GDIEMAFL') together with a catalytic cysteine is characteristic of the aldehyde dehydrogenase superfamily (EC 1.2.x.x). Critically, the GDI motif is a hallmark of aspartate-semialdehyde dehydrogenase specifically: in ASADH, the second catalytic step uses inorganic phosphate (rather than water) as the nucleophile to form 4-phospho-L-aspartate, and the GDI region is part of the phosphate-binding/substrate-specificity pocket. General aldehyde dehydrogenases (EC 1.2.1.46) hydrolyze the thioacyl intermediate with water and lack the phosphate-acceptor architecture encoded by this motif context. The overall ~362-residue homodimeric fold and the specific arrangement of substrate-binding residues (amino-acid recognition pocket for the aspartate moiety) further favor EC 1.2.1.11 over the generic EC 1.2.1.46. Options B (2.7.8.7, a transferase) and C (2.3.1.31, a transferase) are readily excluded by the oxidoreductase architecture.",
    "missing_item_specific_fact": "None that is strictly indispensable. The GDI motif and phosphate-acceptor architecture are recognizable from sequence to a knowledgeable enzymologist, though the distinction from EC 1.2.1.46 requires familiarity with ASADH active-site architecture beyond generic aldehyde dehydrogenase motifs.",
    "reason": "The sequence provides identifiable Rossmann-fold, catalytic Cys, and GDI-motif features that allow a trained biologist to reason toward EC 1.2.1.11 specifically rather than the generic EC 1.2.1.46. The GDI motif's role in phosphate-dependent (rather than hydrolytic) resolution of the thioacyl intermediate is a concrete mechanistic argument distinguishing ASADH from general aldehyde dehydrogenases. While the distinction is non-trivial, it rests on general enzymology rather than a single memorized database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (1.2.1.46)"],
    "reason": "EC 1.2.1.46 (aldehyde dehydrogenase, NADP+) is a closely related general aldehyde dehydrogenase that shares the Rossmann fold and catalytic Cys. Without detailed active-site mapping, a model could argue for the general EC 1.2.1.46. However, the GDI motif and phosphate-acceptor architecture provide a defensible basis for preferring the specific ASADH assignment (D). The ambiguity is mild; the sequence features do favor D over A for a knowledgeable reader."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation confirms EC 1.2.1.11 with experimental evidence (PubMed, PDB), but this annotation was not available to the evaluated model.",
    "The distinction between EC 1.2.1.46 and EC 1.2.1.11 from raw sequence alone is challenging; the GDI-motif argument is sound but requires specialized knowledge of ASADH catalytic mechanism.",
    "The sequence-match is exact (SHA256 identical) between the benchmark input and the UniProt entry A0A179UL48.",
    "EC 1.2.1.46 is a valid EC number (aldehyde dehydrogenase NADP+), making it a plausible but less specific distractor rather than an obviously wrong answer."
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

**Accession:** `A0A179UL48` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
"A0A179UL48"
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30107909","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30107909","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24286"}}],"reaction":{"ecNumber":"1.2.1.11","evidences":[{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30107909","source":"PubMed"}],"name":"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24284"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:537519"}]}}
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
{"citation":{"authors":["Dahal G.P.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"29608391"},{"database":"DOI","id":"10.1177/2472555218767844"}],"citationType":"journal article","firstPage":"520","id":"29608391","journal":"SLAS Discovery","lastPage":"531","publicationDate":"2018","title":"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.","volume":"23"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION"]}
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
{"citation":{"authors":["Dahal G.P.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"30107909"},{"database":"DOI","id":"10.1016/j.bbrc.2018.08.053"}],"citationType":"journal article","firstPage":"2848","id":"30107909","journal":"Biochem. Biophys. Res. Commun.","lastPage":"2854","publicationDate":"2018","title":"Structural insights into inhibitor binding to a fungal ortholog of aspartate semialdehyde dehydrogenase.","volume":"503"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6C85","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6C8W","source":"PDB"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND NADP(+)","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT"]}
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 25-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.
RX   PubMed=29608391; DOI=10.1177/2472555218767844;
RA   Dahal G.P., Viola R.E.;
RT   "A Fragment Library Screening Approach to Identify Selective Inhibitors
RT   against an Essential Fungal Enzyme.";
RL   SLAS Discovery 23:520-531(2018).
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 32-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
RN   [3] {ECO:0007744|PDB:6C85, ECO:0007744|PDB:6C8W}
RP   X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND
RP   NADP(+), FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION,
RP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.
RX   PubMed=30107909; DOI=10.1016/j.bbrc.2018.08.053;
RA   Dahal G.P., Viola R.E.;
RT   "Structural insights into inhibitor binding to a fungal ortholog of
RT   aspartate semialdehyde dehydrogenase.";
RL   Biochem. Biophys. Res. Commun. 503:2848-2854(2018).
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 48-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-
CC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;
CC         Evidence={ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;
CC         Evidence={ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 57. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
