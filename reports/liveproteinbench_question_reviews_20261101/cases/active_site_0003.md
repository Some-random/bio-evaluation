# active_site_0003

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 118 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVAFSSLFLGASIAATALAAPGELPGMHLNKRQTYTQSATGTHDGYYFSFWTDGGPNVRYTNEAGGQYSVTWSGNGNWVGGKGWNPGAARTINYTGTYQPNGNSYLAVYGWTRNPLVEYYVVENFGTYDPSTGAQRLGSINVDGSTYNVYRTRRTNAPSIEGTRSFDQYWSVRVNKRVGGSVDMNAHFNAWRQAGLTLGTHDYQIVATEGYFSSGSARINVGGGSTGGGNNGGGNNGGNPGGNPGGNPGGNPGGNCSPRWGQCGGQGWNGPTCCESGTTCRQQNQWYSQCL

[Multiple Choices]
A. Position 2153 (For beta-ketoacyl synthase 2 activity)
B. Position 161 (Lowers pKa of active site Tyr)
C. Position 118 (Nucleophile)
D. Position 209 (Proton donor)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The exact matched sequence has a UniProt active-site annotation identifying position 118 as the nucleophile, matching choice C. This annotation is attributed to a PROSITE rule, so it supports the key as a database annotation but is not direct experimental evidence for that residue.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General glycosidase chemistry may suggest catalytic residues, but it does not establish which numbered residues in this particular sequence have the stated roles.


**Missing item-specific fact**

> The protein-specific mapping of catalytic roles to residue positions, including that position 118 is annotated as the nucleophile and position 209 as the proton donor.


**Reason**

> The input provides a sequence but no protein identity, family annotation, structural evidence, or experimentally established residue assignments. Selecting the exact positions depends on item-specific information not supplied.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both position 118 (nucleophile) and position 209 (proton donor) are annotated as active-site residues for the exact matched sequence. The question asks for residues constituting the catalytic center, so both choices fit.


### Important caveats

- The position 118 and 209 annotations are attributed to PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.
- The sequence match and residue numbering are for the canonical 291-residue entry; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General glycosidase chemistry may suggest catalytic residues, but it does not establish which numbered residues in this particular sequence have the stated roles.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific mapping of catalytic roles to residue positions, including that position 118 is annotated as the nucleophile and position 209 as the proton donor.",
    "reason": "The input provides a sequence but no protein identity, family annotation, structural evidence, or experimentally established residue assignments. Selecting the exact positions depends on item-specific information not supplied."
  },
  "case_id": "active_site_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact matched sequence has a UniProt active-site annotation identifying position 118 as the nucleophile, matching choice C. This annotation is attributed to a PROSITE rule, so it supports the key as a database annotation but is not direct experimental evidence for that residue."
  },
  "important_caveats": [
    "The position 118 and 209 annotations are attributed to PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.",
    "The sequence match and residue numbering are for the canonical 291-residue entry; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both position 118 (nucleophile) and position 209 (proton donor) are annotated as active-site residues for the exact matched sequence. The question asks for residues constituting the catalytic center, so both choices fit."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact matched sequence has a UniProt active-site annotation identifying position 118 as the nucleophile, matching choice C. This annotation is attributed to a PROSITE rule, so it supports the key as a database annotation but is not direct experimental evidence for that residue.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General glycosidase chemistry may suggest catalytic residues, but it does not establish which numbered residues in this particular sequence have the stated roles.",
    "missing_item_specific_fact": "The protein-specific mapping of catalytic roles to residue positions, including that position 118 is annotated as the nucleophile and position 209 as the proton donor.",
    "reason": "The input provides a sequence but no protein identity, family annotation, structural evidence, or experimentally established residue assignments. Selecting the exact positions depends on item-specific information not supplied."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both position 118 (nucleophile) and position 209 (proton donor) are annotated as active-site residues for the exact matched sequence. The question asks for residues constituting the catalytic center, so both choices fit."
  },
  "important_caveats": [
    "The position 118 and 209 annotations are attributed to PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.",
    "The sequence match and residue numbering are for the canonical 291-residue entry; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0B5JC15 (Endo-1,4-beta-xylanase 11B, GH11, EC 3.2.1.8, from Humicola insolens) annotates position 118 as 'Nucleophile' (type: Active site) and position 209 as 'Proton donor' (type: Active site). The benchmark sequence (291 AA, SHA256 matched) contains Glu at both positions, consistent with the GH11 double-displacement mechanism. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU01097), a computational sequence-similarity inference rather than direct experimental determination, but it is consistent with well-established GH11 catalytic architecture. The reference PubMed:25629035 provides FUNCTION and CATALYTIC ACTIVITY data for this enzyme. Choice A (position 2153) is invalid since the protein is only 291 residues. Choice B (position 161, 'Lowers pKa of active site Tyr') matches no annotated feature. Choice C is supported by the annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could recognize the sequence as a fungal GH11 xylanase (length, fungal signal peptide, conserved xylanase motifs) and deduce that the catalytic mechanism involves two Glu residues acting as nucleophile and proton donor. Positions 118 (E) and 209 (E) are the only plausible catalytic Glu candidates. However, assigning which Glu is the nucleophile versus the proton donor requires knowledge of the specific GH11 β-jelly-roll fold topology (the nucleophile sits in the 'thumb' region, the proton donor in a distinct loop). The sequence context around position 118 (WTRNPLVEYY) and position 209 (IVATEG) does not, by general biological reasoning alone, unambiguously indicate which is the nucleophile without prior knowledge of GH11 structural motifs or the PROSITE-ProRule pattern.


**Missing item-specific fact**

> The specific assignment of position 118 as the nucleophile and position 209 as the proton donor depends on the PROSITE-ProRule PRU01097 pattern match for GH11 glycoside hydrolases, which encodes the known spatial arrangement of the two catalytic Glu residues in the GH11 β-jelly-roll fold. This fold-specific positional information is not derivable from the raw sequence by general biological reasoning alone.


**Reason**

> While general GH11 knowledge narrows the answer to two Glu residues, the precise positional distinction between nucleophile (118) and proton donor (209) requires item-specific structural knowledge of the GH11 fold or memorization of the PROSITE annotation. The distractors A (nonexistent position) and B (unannotated feature) are easily eliminated, but C vs. D hinges on a fold-architecture fact not inferable from the sequence text.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both position 118 (Nucleophile) and position 209 (Proton donor) are annotated as 'Active site' in UniProt and are both part of the enzyme's catalytic machinery. The question asks for 'the enzyme's catalytic center,' which could encompass both residues. The nucleophile (C) is the more precise answer for 'catalytic center' since it performs the direct chemical attack, but the proton donor (D) is also a catalytic residue. The singular phrasing ('the option') and the term 'catalytic center' favor C, but D is not clearly wrong.


### Important caveats

- The active-site annotations carry evidence code ECO:0000255 (PROSITE-ProRule), meaning they are computational sequence-similarity inferences, not experimentally determined positions. The reference paper (PubMed:25629035) reports catalytic activity and function but the specific residue assignments derive from pattern matching.
- The UniProt accession (A0A0B5JC15) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model sees only the raw sequence and choices.
- The sequence is a precursor (includes a signal peptide); position numbering is in canonical UniProt coordinates, which match the provided sequence length of 291 AA.
- Choice A references 'beta-ketoacyl synthase 2 activity' at a nonexistent position (2153 in a 291-residue protein), making it an obviously invalid distractor unrelated to this enzyme's function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could recognize the sequence as a fungal GH11 xylanase (length, fungal signal peptide, conserved xylanase motifs) and deduce that the catalytic mechanism involves two Glu residues acting as nucleophile and proton donor. Positions 118 (E) and 209 (E) are the only plausible catalytic Glu candidates. However, assigning which Glu is the nucleophile versus the proton donor requires knowledge of the specific GH11 β-jelly-roll fold topology (the nucleophile sits in the 'thumb' region, the proton donor in a distinct loop). The sequence context around position 118 (WTRNPLVEYY) and position 209 (IVATEG) does not, by general biological reasoning alone, unambiguously indicate which is the nucleophile without prior knowledge of GH11 structural motifs or the PROSITE-ProRule pattern.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific assignment of position 118 as the nucleophile and position 209 as the proton donor depends on the PROSITE-ProRule PRU01097 pattern match for GH11 glycoside hydrolases, which encodes the known spatial arrangement of the two catalytic Glu residues in the GH11 β-jelly-roll fold. This fold-specific positional information is not derivable from the raw sequence by general biological reasoning alone.",
    "reason": "While general GH11 knowledge narrows the answer to two Glu residues, the precise positional distinction between nucleophile (118) and proton donor (209) requires item-specific structural knowledge of the GH11 fold or memorization of the PROSITE annotation. The distractors A (nonexistent position) and B (unannotated feature) are easily eliminated, but C vs. D hinges on a fold-architecture fact not inferable from the sequence text."
  },
  "case_id": "active_site_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0B5JC15 (Endo-1,4-beta-xylanase 11B, GH11, EC 3.2.1.8, from Humicola insolens) annotates position 118 as 'Nucleophile' (type: Active site) and position 209 as 'Proton donor' (type: Active site). The benchmark sequence (291 AA, SHA256 matched) contains Glu at both positions, consistent with the GH11 double-displacement mechanism. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU01097), a computational sequence-similarity inference rather than direct experimental determination, but it is consistent with well-established GH11 catalytic architecture. The reference PubMed:25629035 provides FUNCTION and CATALYTIC ACTIVITY data for this enzyme. Choice A (position 2153) is invalid since the protein is only 291 residues. Choice B (position 161, 'Lowers pKa of active site Tyr') matches no annotated feature. Choice C is supported by the annotation."
  },
  "important_caveats": [
    "The active-site annotations carry evidence code ECO:0000255 (PROSITE-ProRule), meaning they are computational sequence-similarity inferences, not experimentally determined positions. The reference paper (PubMed:25629035) reports catalytic activity and function but the specific residue assignments derive from pattern matching.",
    "The UniProt accession (A0A0B5JC15) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model sees only the raw sequence and choices.",
    "The sequence is a precursor (includes a signal peptide); position numbering is in canonical UniProt coordinates, which match the provided sequence length of 291 AA.",
    "Choice A references 'beta-ketoacyl synthase 2 activity' at a nonexistent position (2153 in a 291-residue protein), making it an obviously invalid distractor unrelated to this enzyme's function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both position 118 (Nucleophile) and position 209 (Proton donor) are annotated as 'Active site' in UniProt and are both part of the enzyme's catalytic machinery. The question asks for 'the enzyme's catalytic center,' which could encompass both residues. The nucleophile (C) is the more precise answer for 'catalytic center' since it performs the direct chemical attack, but the proton donor (D) is also a catalytic residue. The singular phrasing ('the option') and the term 'catalytic center' favor C, but D is not clearly wrong."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0B5JC15 (Endo-1,4-beta-xylanase 11B, GH11, EC 3.2.1.8, from Humicola insolens) annotates position 118 as 'Nucleophile' (type: Active site) and position 209 as 'Proton donor' (type: Active site). The benchmark sequence (291 AA, SHA256 matched) contains Glu at both positions, consistent with the GH11 double-displacement mechanism. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU01097), a computational sequence-similarity inference rather than direct experimental determination, but it is consistent with well-established GH11 catalytic architecture. The reference PubMed:25629035 provides FUNCTION and CATALYTIC ACTIVITY data for this enzyme. Choice A (position 2153) is invalid since the protein is only 291 residues. Choice B (position 161, 'Lowers pKa of active site Tyr') matches no annotated feature. Choice C is supported by the annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could recognize the sequence as a fungal GH11 xylanase (length, fungal signal peptide, conserved xylanase motifs) and deduce that the catalytic mechanism involves two Glu residues acting as nucleophile and proton donor. Positions 118 (E) and 209 (E) are the only plausible catalytic Glu candidates. However, assigning which Glu is the nucleophile versus the proton donor requires knowledge of the specific GH11 β-jelly-roll fold topology (the nucleophile sits in the 'thumb' region, the proton donor in a distinct loop). The sequence context around position 118 (WTRNPLVEYY) and position 209 (IVATEG) does not, by general biological reasoning alone, unambiguously indicate which is the nucleophile without prior knowledge of GH11 structural motifs or the PROSITE-ProRule pattern.",
    "missing_item_specific_fact": "The specific assignment of position 118 as the nucleophile and position 209 as the proton donor depends on the PROSITE-ProRule PRU01097 pattern match for GH11 glycoside hydrolases, which encodes the known spatial arrangement of the two catalytic Glu residues in the GH11 β-jelly-roll fold. This fold-specific positional information is not derivable from the raw sequence by general biological reasoning alone.",
    "reason": "While general GH11 knowledge narrows the answer to two Glu residues, the precise positional distinction between nucleophile (118) and proton donor (209) requires item-specific structural knowledge of the GH11 fold or memorization of the PROSITE annotation. The distractors A (nonexistent position) and B (unannotated feature) are easily eliminated, but C vs. D hinges on a fold-architecture fact not inferable from the sequence text."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both position 118 (Nucleophile) and position 209 (Proton donor) are annotated as 'Active site' in UniProt and are both part of the enzyme's catalytic machinery. The question asks for 'the enzyme's catalytic center,' which could encompass both residues. The nucleophile (C) is the more precise answer for 'catalytic center' since it performs the direct chemical attack, but the proton donor (D) is also a catalytic residue. The singular phrasing ('the option') and the term 'catalytic center' favor C, but D is not clearly wrong."
  },
  "important_caveats": [
    "The active-site annotations carry evidence code ECO:0000255 (PROSITE-ProRule), meaning they are computational sequence-similarity inferences, not experimentally determined positions. The reference paper (PubMed:25629035) reports catalytic activity and function but the specific residue assignments derive from pattern matching.",
    "The UniProt accession (A0A0B5JC15) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model sees only the raw sequence and choices.",
    "The sequence is a precursor (includes a signal peptide); position numbering is in canonical UniProt coordinates, which match the provided sequence length of 291 AA.",
    "Choice A references 'beta-ketoacyl synthase 2 activity' at a nonexistent position (2153 in a 291-residue protein), making it an obviously invalid distractor unrelated to this enzyme's function."
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

**Accession:** `A0A0B5JC15` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 34. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.597840+00:00.  

```json
"A0A0B5JC15"
```

Source SHA-256: `a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.597840+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1,4-beta-D-xylan xylanohydrolase 11B"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25629035","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25629035","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase 11B"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"25629035","source":"PubMed"}],"value":"Xylanase 11B"}]}}
```

Source SHA-256: `a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.597840+00:00.  

```json
{"description":"Nucleophile","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":118},"start":{"modifier":"EXACT","value":118}},"type":"Active site"}
```

Source SHA-256: `a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.597840+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":209},"start":{"modifier":"EXACT","value":209}},"type":"Active site"}
```

Source SHA-256: `a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 34 / 1.  
**Retrieved:** 2026-11-01T06:27:16.201745+00:00.  

```text
ID   XY11B_HUMIN             Reviewed;         291 AA.
AC   A0A0B5JC15;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-APR-2015, sequence version 1.
DT   28-JAN-2026, entry version 34.
DE   RecName: Full=Endo-1,4-beta-xylanase 11B {ECO:0000303|PubMed:25629035};
DE            Short=Xylanase 11B {ECO:0000303|PubMed:25629035};
DE            EC=3.2.1.8 {ECO:0000269|PubMed:25629035};
DE   AltName: Full=1,4-beta-D-xylan xylanohydrolase 11B {ECO:0000305};
DE   Flags: Precursor;
GN   Name=Xyn11B {ECO:0000303|PubMed:25629035};
GN   Synonyms=Xyl2 {ECO:0000303|PubMed:8190078};
OS   Humicola insolens (Soft-rot fungus).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.
OX   NCBI_TaxID=85995;
```

Source SHA-256: `ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)  
**Locator:** `lines 126-128`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 34 / 1.  
**Retrieved:** 2026-11-01T06:27:16.201745+00:00.  

```text
FT   ACT_SITE        118
FT                   /note="Nucleophile"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01097"
```

Source SHA-256: `ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)  
**Locator:** `lines 129-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 34 / 1.  
**Retrieved:** 2026-11-01T06:27:16.201745+00:00.  

```text
FT   ACT_SITE        209
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01097"
```

Source SHA-256: `ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
