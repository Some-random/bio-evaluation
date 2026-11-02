# EC_number_0194

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHLASSLFLLATLPFGFAAGKGKGKGKDNSDVGLDVLAKKAGLKYFGAATDTPGQRERAGLEDKYPEYDRIMWHSPEFGSTTPTNGQKWLFVEPERGVFNFTEGDVVASKARQHGKLLRCHALVWHSQLAPWVEETEWTPEELRKVIVDHITAVAGHYKGQCYAWDVVNEALNEDGTYRESVFYKVLGEEYIKLAFETAAKVDPKAKLYYNDYNLEWPSAKTEGAKRIVKLLKDAKIPIHGVGLQAHLIAEQHPTLDDHIAAIRGFTQLGVEVALTELDIRLKTPATEENLALQREAYKNVVGACVQVCGCVGVTIWDFYDPFSWVPYFFEGEGAPLLWFEDFSKHPAYYGVVEALTNKTRRSKRSISDRRAKLLA

[Multiple Choices]
A. 3.2.1.105
B. 3.2.1.8
C. 2.7.7.80
D. 2.7.7.43
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

> The exact supplied sequence matches the UniProt entry annotating EC 3.2.1.8, with catalytic activity evidence linked to PubMed 23306124. The annotation identifies endohydrolysis of beta-D-xylosidic linkages in xylans, supporting choice B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a likely secretion signal and is compatible with a secreted glycoside hydrolase, which may make the hydrolase choices more plausible than the nucleotidyl-transferase choices. Those broad clues do not establish the precise substrate specificity needed to choose EC 3.2.1.8 over another glycosidase.


**Missing item-specific fact**

> The protein-specific catalytic activity—endo-1,4-beta-xylanase activity—needed to distinguish the glycosidase choices is not stated in the input.


**Reason**

> Selecting the exact EC number depends on a protein-specific functional annotation or experimental characterization absent from the sequence and choices; recognizing the exact sequence from a database would be lookup, not reasoning from supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence catalytic annotation supports choice B; the supplied evidence does not establish another listed choice as defensible.


### Important caveats

- The UniProt evidence links the annotation to a publication, but the publication was not independently reviewed here.
- The reviewer-only accession and database annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a likely secretion signal and is compatible with a secreted glycoside hydrolase, which may make the hydrolase choices more plausible than the nucleotidyl-transferase choices. Those broad clues do not establish the precise substrate specificity needed to choose EC 3.2.1.8 over another glycosidase.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—endo-1,4-beta-xylanase activity—needed to distinguish the glycosidase choices is not stated in the input.",
    "reason": "Selecting the exact EC number depends on a protein-specific functional annotation or experimental characterization absent from the sequence and choices; recognizing the exact sequence from a database would be lookup, not reasoning from supplied information."
  },
  "case_id": "EC_number_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotating EC 3.2.1.8, with catalytic activity evidence linked to PubMed 23306124. The annotation identifies endohydrolysis of beta-D-xylosidic linkages in xylans, supporting choice B."
  },
  "important_caveats": [
    "The UniProt evidence links the annotation to a publication, but the publication was not independently reviewed here.",
    "The reviewer-only accession and database annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence catalytic annotation supports choice B; the supplied evidence does not establish another listed choice as defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotating EC 3.2.1.8, with catalytic activity evidence linked to PubMed 23306124. The annotation identifies endohydrolysis of beta-D-xylosidic linkages in xylans, supporting choice B.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a likely secretion signal and is compatible with a secreted glycoside hydrolase, which may make the hydrolase choices more plausible than the nucleotidyl-transferase choices. Those broad clues do not establish the precise substrate specificity needed to choose EC 3.2.1.8 over another glycosidase.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—endo-1,4-beta-xylanase activity—needed to distinguish the glycosidase choices is not stated in the input.",
    "reason": "Selecting the exact EC number depends on a protein-specific functional annotation or experimental characterization absent from the sequence and choices; recognizing the exact sequence from a database would be lookup, not reasoning from supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence catalytic annotation supports choice B; the supplied evidence does not establish another listed choice as defensible."
  },
  "important_caveats": [
    "The UniProt evidence links the annotation to a publication, but the publication was not independently reviewed here.",
    "The reviewer-only accession and database annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry M4MGK7 (XYNA_HUMIN) is annotated as Endo-1,4-beta-xylanase A with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed:23306124). The sequence matches exactly (SHA256 confirmed). The catalytic activity comment explicitly states 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' with EC 3.2.1.8. This is experimentally verified, not merely computational annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a hydrophobic N-terminal signal peptide (MHLASSLFLLATLPFGFAAG) indicating a secreted protein, followed by a catalytic domain with characteristic glycoside hydrolase family 10 (GH10) motifs: the 'GHY' motif in 'VIVDHITAVAGHYKGQCYAWDVVNE' and 'GHL' in 'GVGLQAHLIAEQ'. GH10 is specifically associated with endo-1,4-beta-xylanase (EC 3.2.1.8). Options C (2.7.7.80) and D (2.7.7.43) are transferases (nucleotidyltransferases) with entirely different structural requirements (nucleotide-binding P-loop motifs, Rossmann-like folds) incompatible with the observed glycosidase architecture. The GH10 identification provides a concrete biological argument linking the sequence to xylanase activity rather than other glycosidase subclasses.


**Missing item-specific fact**

> The precise identity and substrate specificity of EC 3.2.1.105 (option A) is not derivable from the sequence alone; distinguishing 3.2.1.8 from 3.2.1.105 requires knowing that 3.2.1.105 is not a GH10 enzyme or has different substrate specificity. However, the positive identification of GH10 features pointing to xylanase provides a defensible argument for B over A.


**Reason**

> Eliminating transferases (C, D) is straightforward from sequence architecture. The GH10 motif identification provides a positive biological argument for xylanase (3.2.1.8). The A vs B distinction is somewhat harder but the GH10→xylanase→3.2.1.8 chain is a legitimate biological inference rather than pure memorization of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While distinguishing 3.2.1.8 from 3.2.1.105 requires some specific knowledge about what 3.2.1.105 represents, the strong GH10 signature and the clear elimination of transferases make B the most defensible answer. No other option has a comparable level of sequence-based support.


### Important caveats

- The distinction between 3.2.1.8 (option B) and 3.2.1.105 (option A) relies on the model knowing what 3.2.1.105 is and that it is not a GH10 xylanase; this is a specific knowledge requirement beyond general GH family identification.
- The GH10 motif identification ('GHY'/'GHL') is a recognized but not perfectly unique signature; some related enzymes share partial motifs.
- The UniProt annotation is experimentally supported (ECO:0000269), making the expected answer well-grounded, but the question tests sequence-to-function inference rather than annotation recall.
- The sequence is a precursor (includes signal peptide and linker region); the mature catalytic domain starts after the 'KGKGKGK' linker.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a hydrophobic N-terminal signal peptide (MHLASSLFLLATLPFGFAAG) indicating a secreted protein, followed by a catalytic domain with characteristic glycoside hydrolase family 10 (GH10) motifs: the 'GHY' motif in 'VIVDHITAVAGHYKGQCYAWDVVNE' and 'GHL' in 'GVGLQAHLIAEQ'. GH10 is specifically associated with endo-1,4-beta-xylanase (EC 3.2.1.8). Options C (2.7.7.80) and D (2.7.7.43) are transferases (nucleotidyltransferases) with entirely different structural requirements (nucleotide-binding P-loop motifs, Rossmann-like folds) incompatible with the observed glycosidase architecture. The GH10 identification provides a concrete biological argument linking the sequence to xylanase activity rather than other glycosidase subclasses.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise identity and substrate specificity of EC 3.2.1.105 (option A) is not derivable from the sequence alone; distinguishing 3.2.1.8 from 3.2.1.105 requires knowing that 3.2.1.105 is not a GH10 enzyme or has different substrate specificity. However, the positive identification of GH10 features pointing to xylanase provides a defensible argument for B over A.",
    "reason": "Eliminating transferases (C, D) is straightforward from sequence architecture. The GH10 motif identification provides a positive biological argument for xylanase (3.2.1.8). The A vs B distinction is somewhat harder but the GH10→xylanase→3.2.1.8 chain is a legitimate biological inference rather than pure memorization of this specific protein's annotation."
  },
  "case_id": "EC_number_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry M4MGK7 (XYNA_HUMIN) is annotated as Endo-1,4-beta-xylanase A with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed:23306124). The sequence matches exactly (SHA256 confirmed). The catalytic activity comment explicitly states 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' with EC 3.2.1.8. This is experimentally verified, not merely computational annotation."
  },
  "important_caveats": [
    "The distinction between 3.2.1.8 (option B) and 3.2.1.105 (option A) relies on the model knowing what 3.2.1.105 is and that it is not a GH10 xylanase; this is a specific knowledge requirement beyond general GH family identification.",
    "The GH10 motif identification ('GHY'/'GHL') is a recognized but not perfectly unique signature; some related enzymes share partial motifs.",
    "The UniProt annotation is experimentally supported (ECO:0000269), making the expected answer well-grounded, but the question tests sequence-to-function inference rather than annotation recall.",
    "The sequence is a precursor (includes signal peptide and linker region); the mature catalytic domain starts after the 'KGKGKGK' linker."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While distinguishing 3.2.1.8 from 3.2.1.105 requires some specific knowledge about what 3.2.1.105 represents, the strong GH10 signature and the clear elimination of transferases make B the most defensible answer. No other option has a comparable level of sequence-based support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry M4MGK7 (XYNA_HUMIN) is annotated as Endo-1,4-beta-xylanase A with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed:23306124). The sequence matches exactly (SHA256 confirmed). The catalytic activity comment explicitly states 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' with EC 3.2.1.8. This is experimentally verified, not merely computational annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a hydrophobic N-terminal signal peptide (MHLASSLFLLATLPFGFAAG) indicating a secreted protein, followed by a catalytic domain with characteristic glycoside hydrolase family 10 (GH10) motifs: the 'GHY' motif in 'VIVDHITAVAGHYKGQCYAWDVVNE' and 'GHL' in 'GVGLQAHLIAEQ'. GH10 is specifically associated with endo-1,4-beta-xylanase (EC 3.2.1.8). Options C (2.7.7.80) and D (2.7.7.43) are transferases (nucleotidyltransferases) with entirely different structural requirements (nucleotide-binding P-loop motifs, Rossmann-like folds) incompatible with the observed glycosidase architecture. The GH10 identification provides a concrete biological argument linking the sequence to xylanase activity rather than other glycosidase subclasses.",
    "missing_item_specific_fact": "The precise identity and substrate specificity of EC 3.2.1.105 (option A) is not derivable from the sequence alone; distinguishing 3.2.1.8 from 3.2.1.105 requires knowing that 3.2.1.105 is not a GH10 enzyme or has different substrate specificity. However, the positive identification of GH10 features pointing to xylanase provides a defensible argument for B over A.",
    "reason": "Eliminating transferases (C, D) is straightforward from sequence architecture. The GH10 motif identification provides a positive biological argument for xylanase (3.2.1.8). The A vs B distinction is somewhat harder but the GH10→xylanase→3.2.1.8 chain is a legitimate biological inference rather than pure memorization of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While distinguishing 3.2.1.8 from 3.2.1.105 requires some specific knowledge about what 3.2.1.105 represents, the strong GH10 signature and the clear elimination of transferases make B the most defensible answer. No other option has a comparable level of sequence-based support."
  },
  "important_caveats": [
    "The distinction between 3.2.1.8 (option B) and 3.2.1.105 (option A) relies on the model knowing what 3.2.1.105 is and that it is not a GH10 xylanase; this is a specific knowledge requirement beyond general GH family identification.",
    "The GH10 motif identification ('GHY'/'GHL') is a recognized but not perfectly unique signature; some related enzymes share partial motifs.",
    "The UniProt annotation is experimentally supported (ECO:0000269), making the expected answer well-grounded, but the question tests sequence-to-function inference rather than annotation recall.",
    "The sequence is a precursor (includes signal peptide and linker region); the mature catalytic domain starts after the 'KGKGKGK' linker."
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

**Accession:** `M4MGK7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1,4-beta-D-xylan xylanohydrolase A"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23306124","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase A"}}}
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
{"citation":{"authors":["Du Y.","Shi P.","Huang H.","Zhang X.","Luo H.","Wang Y.","Yao B."],"citationCrossReferences":[{"database":"PubMed","id":"23306124"},{"database":"DOI","id":"10.1016/j.biortech.2012.12.067"}],"citationType":"journal article","firstPage":"161","id":"23306124","journal":"Bioresour. Technol.","lastPage":"167","publicationDate":"2013","title":"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.","volume":"130"},"referenceComments":[{"type":"STRAIN","value":"Y1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBSTRATE SPECIFICITY","ACTIVITY REGULATION","BIOTECHNOLOGY"]}
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:29:07.720781+00:00.  

```text
ID   XYNA_HUMIN              Reviewed;         376 AA.
AC   M4MGK7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-MAY-2013, sequence version 1.
DT   28-JAN-2026, entry version 31.
DE   RecName: Full=Endo-1,4-beta-xylanase A {ECO:0000303|PubMed:23306124};
DE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};
DE   AltName: Full=1,4-beta-D-xylan xylanohydrolase A {ECO:0000305};
DE   Flags: Precursor;
GN   Name=XynA {ECO:0000303|PubMed:23306124};
OS   Humicola insolens (Soft-rot fungus).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.
OX   NCBI_TaxID=85995;
```

Source SHA-256: `7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:29:07.720781+00:00.  

```text
DE   RecName: Full=Endo-1,4-beta-xylanase A {ECO:0000303|PubMed:23306124};
DE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};
DE   AltName: Full=1,4-beta-D-xylan xylanohydrolase A {ECO:0000305};
DE   Flags: Precursor;
```

Source SHA-256: `7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)  
**Locator:** `lines 45-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:29:07.720781+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:23306124};
```

Source SHA-256: `7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 194. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
