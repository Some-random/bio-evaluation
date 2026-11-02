# transmembrane_0025

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSNFTPDACNVDSGLDSVLPPSLYALVFTLGLPANLLALWAAWLQVRKGRELGVYLLNLSLSDLLLICALPPWTDYYLRRDVWGYGPGACRLFGFVFYTNLYVGAAFLSCVSADRYLAVAHPLRFPGARPIRSAAAVSALIWMLELAANAPPLLGEAIHRDRYNHTFCYESYPLSGRGAALANVGRVLAGFLLPWGVMMLCYAGLLRALRGSASCEQRERRRVRRLALGLPCVALLCYGPYHALLLLRSLVFLVGGGSVDAGGGCALEERLFPAYHASLALATLNCLADPALYCLACPGARGEVAKVVGGVVAWAMGKERRAWGERGGNGRGCGEGEEVGMVELRGNGREFVV

[Multiple Choices]
A. 5..25
B. 9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296
C. 9..45; 50..80; 89..125; 130..156; 173..211; 216..251; 268..296
D. 9..45; 50..80; 86..121; 130..156; 173..211; 216..251
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the historical and current UniProt sequence. The matched entry annotates seven transmembrane helices at the coordinates listed in B, with ECO:0000269 evidence linked to the cited study. This supports B, though the primary study was not independently reviewed here.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic stretches and seven-helix pattern support a multi-pass, likely seven-transmembrane protein. They do not reliably establish the exact boundaries needed to distinguish B from C, which differ at the third segment.


**Missing item-specific fact**

> The protein-specific transmembrane boundary annotation or structural/topological evidence identifying the third helix as 86..121 rather than 89..125.


**Reason**

> Selecting the exact keyed intervals, especially between the near-identical B and C options, depends on item-specific boundary information not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup, not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> From the sequence alone, both options give seven largely hydrophobic segments, and the small shift in the third segment's boundaries is not decisively resolved by generic hydrophobicity reasoning. The reviewer-only annotation supports B.


### Important caveats

- The annotation evidence is linked to a publication using ECO:0000269, but the primary paper was not independently validated here.
- The exact author source snapshot is unknown; the sequence matches the available historical and current records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic stretches and seven-helix pattern support a multi-pass, likely seven-transmembrane protein. They do not reliably establish the exact boundaries needed to distinguish B from C, which differ at the third segment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane boundary annotation or structural/topological evidence identifying the third helix as 86..121 rather than 89..125.",
    "reason": "Selecting the exact keyed intervals, especially between the near-identical B and C options, depends on item-specific boundary information not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup, not sequence-based reasoning."
  },
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence. The matched entry annotates seven transmembrane helices at the coordinates listed in B, with ECO:0000269 evidence linked to the cited study. This supports B, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The annotation evidence is linked to a publication using ECO:0000269, but the primary paper was not independently validated here.",
    "The exact author source snapshot is unknown; the sequence matches the available historical and current records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "From the sequence alone, both options give seven largely hydrophobic segments, and the small shift in the third segment's boundaries is not decisively resolved by generic hydrophobicity reasoning. The reviewer-only annotation supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence. The matched entry annotates seven transmembrane helices at the coordinates listed in B, with ECO:0000269 evidence linked to the cited study. This supports B, though the primary study was not independently reviewed here.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16", "C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic stretches and seven-helix pattern support a multi-pass, likely seven-transmembrane protein. They do not reliably establish the exact boundaries needed to distinguish B from C, which differ at the third segment.",
    "missing_item_specific_fact": "The protein-specific transmembrane boundary annotation or structural/topological evidence identifying the third helix as 86..121 rather than 89..125.",
    "reason": "Selecting the exact keyed intervals, especially between the near-identical B and C options, depends on item-specific boundary information not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup, not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "From the sequence alone, both options give seven largely hydrophobic segments, and the small shift in the third segment's boundaries is not decisively resolved by generic hydrophobicity reasoning. The reviewer-only annotation supports B."
  },
  "important_caveats": [
    "The annotation evidence is linked to a publication using ECO:0000269, but the primary paper was not independently validated here.",
    "The exact author source snapshot is unknown; the sequence matches the available historical and current records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The expected answer B (9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296) matches exactly the seven transmembrane helix boundaries annotated in UniProt entry A0A6I8PUB9 (Xenopus tropicalis GPR4). Each TM segment is annotated with evidence code ECO:0000269 (experimental evidence) from PubMed:39753131, a cryo-EM structure paper (Wen et al., Cell 2025). The sequence in the question matches the UniProt sequence (353 AA, SHA-256 confirmed). Option C differs in TM3 boundaries (89..125 vs 86..121), option D omits TM7 (268..296), and option A is a single short segment incompatible with a 7TM receptor.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General GPCR biology (7 transmembrane helices) allows elimination of option A (single 21-residue segment) and option D (only 6 TMs). The approximate positions of the seven hydrophobic stretches can be estimated from the sequence, broadly matching both B and C. However, the critical distinction between B and C is the exact boundary of TM3: B gives 86..121 while C gives 89..125. This 3-residue N-terminal shift and 4-residue C-terminal shift cannot be resolved by hydrophobicity analysis or helix-propensity reasoning. The region 86–88 (GPG) and 122–125 (PLRF) are neither clearly hydrophobic nor clearly helix-breaking in a way that definitively favors one boundary. The correct boundaries (86..121) were determined by cryo-EM structural analysis (PubMed:39753131), an item-specific experimental measurement not derivable from the sequence alone.


**Missing item-specific fact**

> The exact cryo-EM–determined boundaries of TM3 (residues 86–121) for this specific Xenopus tropicalis GPR4 structure, which distinguish option B (86..121) from option C (89..125). No general biological principle or sequence heuristic reliably resolves a 3–4 residue boundary shift in a GPCR TM helix containing multiple polar/charged residues.


**Reason**

> While recognizing the protein as a 7TM GPCR and estimating approximate TM positions is reasoning-supported, the final choice between B and C hinges on the precise experimentally determined TM3 boundaries from a specific cryo-EM study. A sequence-only analysis cannot distinguish GPG at position 86–88 (included in B's TM3) from their exclusion (C's TM3 starting at 89), nor can it determine whether the TM3 helix terminates at H121 or F125.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Options B and C differ only in TM3 boundaries (86..121 vs 89..125). From the sequence alone, the residues GPG(86–88) and PLRF(122–125) are ambiguous as TM-inclusive or loop residues. A hydrophobicity or helix-propensity analysis could plausibly favor either boundary. Without the cryo-EM structural determination, both B and C are defensible. Options A and D are clearly eliminable (wrong number of TMs).


### Important caveats

- The UniProt TM annotations carry experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131), making the boundaries experimentally determined rather than purely computational predictions.
- The question wording says 'a segment that crosses the membrane' (singular) but the answer choices list all seven TM segments. The intent is clearly to identify the complete set of TM regions.
- The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the annotation was present in the historical snapshot (entry version 25, released 2026-01-28), which is within the benchmark construction window.
- The GPG motif at positions 86–88 within TM3 is unusual for a transmembrane helix (proline is a helix breaker), yet the cryo-EM structure includes it within the TM helix, illustrating that simple helix-propensity heuristics would not reproduce the experimental boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General GPCR biology (7 transmembrane helices) allows elimination of option A (single 21-residue segment) and option D (only 6 TMs). The approximate positions of the seven hydrophobic stretches can be estimated from the sequence, broadly matching both B and C. However, the critical distinction between B and C is the exact boundary of TM3: B gives 86..121 while C gives 89..125. This 3-residue N-terminal shift and 4-residue C-terminal shift cannot be resolved by hydrophobicity analysis or helix-propensity reasoning. The region 86–88 (GPG) and 122–125 (PLRF) are neither clearly hydrophobic nor clearly helix-breaking in a way that definitively favors one boundary. The correct boundaries (86..121) were determined by cryo-EM structural analysis (PubMed:39753131), an item-specific experimental measurement not derivable from the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact cryo-EM–determined boundaries of TM3 (residues 86–121) for this specific Xenopus tropicalis GPR4 structure, which distinguish option B (86..121) from option C (89..125). No general biological principle or sequence heuristic reliably resolves a 3–4 residue boundary shift in a GPCR TM helix containing multiple polar/charged residues.",
    "reason": "While recognizing the protein as a 7TM GPCR and estimating approximate TM positions is reasoning-supported, the final choice between B and C hinges on the precise experimentally determined TM3 boundaries from a specific cryo-EM study. A sequence-only analysis cannot distinguish GPG at position 86–88 (included in B's TM3) from their exclusion (C's TM3 starting at 89), nor can it determine whether the TM3 helix terminates at H121 or F125."
  },
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The expected answer B (9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296) matches exactly the seven transmembrane helix boundaries annotated in UniProt entry A0A6I8PUB9 (Xenopus tropicalis GPR4). Each TM segment is annotated with evidence code ECO:0000269 (experimental evidence) from PubMed:39753131, a cryo-EM structure paper (Wen et al., Cell 2025). The sequence in the question matches the UniProt sequence (353 AA, SHA-256 confirmed). Option C differs in TM3 boundaries (89..125 vs 86..121), option D omits TM7 (268..296), and option A is a single short segment incompatible with a 7TM receptor."
  },
  "important_caveats": [
    "The UniProt TM annotations carry experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131), making the boundaries experimentally determined rather than purely computational predictions.",
    "The question wording says 'a segment that crosses the membrane' (singular) but the answer choices list all seven TM segments. The intent is clearly to identify the complete set of TM regions.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the annotation was present in the historical snapshot (entry version 25, released 2026-01-28), which is within the benchmark construction window.",
    "The GPG motif at positions 86–88 within TM3 is unusual for a transmembrane helix (proline is a helix breaker), yet the cryo-EM structure includes it within the TM helix, illustrating that simple helix-propensity heuristics would not reproduce the experimental boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Options B and C differ only in TM3 boundaries (86..121 vs 89..125). From the sequence alone, the residues GPG(86–88) and PLRF(122–125) are ambiguous as TM-inclusive or loop residues. A hydrophobicity or helix-propensity analysis could plausibly favor either boundary. Without the cryo-EM structural determination, both B and C are defensible. Options A and D are clearly eliminable (wrong number of TMs)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The expected answer B (9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296) matches exactly the seven transmembrane helix boundaries annotated in UniProt entry A0A6I8PUB9 (Xenopus tropicalis GPR4). Each TM segment is annotated with evidence code ECO:0000269 (experimental evidence) from PubMed:39753131, a cryo-EM structure paper (Wen et al., Cell 2025). The sequence in the question matches the UniProt sequence (353 AA, SHA-256 confirmed). Option C differs in TM3 boundaries (89..125 vs 86..121), option D omits TM7 (268..296), and option A is a single short segment incompatible with a 7TM receptor.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General GPCR biology (7 transmembrane helices) allows elimination of option A (single 21-residue segment) and option D (only 6 TMs). The approximate positions of the seven hydrophobic stretches can be estimated from the sequence, broadly matching both B and C. However, the critical distinction between B and C is the exact boundary of TM3: B gives 86..121 while C gives 89..125. This 3-residue N-terminal shift and 4-residue C-terminal shift cannot be resolved by hydrophobicity analysis or helix-propensity reasoning. The region 86–88 (GPG) and 122–125 (PLRF) are neither clearly hydrophobic nor clearly helix-breaking in a way that definitively favors one boundary. The correct boundaries (86..121) were determined by cryo-EM structural analysis (PubMed:39753131), an item-specific experimental measurement not derivable from the sequence alone.",
    "missing_item_specific_fact": "The exact cryo-EM–determined boundaries of TM3 (residues 86–121) for this specific Xenopus tropicalis GPR4 structure, which distinguish option B (86..121) from option C (89..125). No general biological principle or sequence heuristic reliably resolves a 3–4 residue boundary shift in a GPCR TM helix containing multiple polar/charged residues.",
    "reason": "While recognizing the protein as a 7TM GPCR and estimating approximate TM positions is reasoning-supported, the final choice between B and C hinges on the precise experimentally determined TM3 boundaries from a specific cryo-EM study. A sequence-only analysis cannot distinguish GPG at position 86–88 (included in B's TM3) from their exclusion (C's TM3 starting at 89), nor can it determine whether the TM3 helix terminates at H121 or F125."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Options B and C differ only in TM3 boundaries (86..121 vs 89..125). From the sequence alone, the residues GPG(86–88) and PLRF(122–125) are ambiguous as TM-inclusive or loop residues. A hydrophobicity or helix-propensity analysis could plausibly favor either boundary. Without the cryo-EM structural determination, both B and C are defensible. Options A and D are clearly eliminable (wrong number of TMs)."
  },
  "important_caveats": [
    "The UniProt TM annotations carry experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131), making the boundaries experimentally determined rather than purely computational predictions.",
    "The question wording says 'a segment that crosses the membrane' (singular) but the answer choices list all seven TM segments. The intent is clearly to identify the complete set of TM regions.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the annotation was present in the historical snapshot (entry version 25, released 2026-01-28), which is within the benchmark construction window.",
    "The GPG motif at positions 86–88 within TM3 is unusual for a transmembrane helix (proline is a helix breaker), yet the cryo-EM structure includes it within the TM helix, illustrating that simple helix-propensity heuristics would not reproduce the experimental boundaries."
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

**Accession:** `A0A6I8PUB9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 25. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:33.494326+00:00.  

```json
{"description":"Helical; Name=1","evidences":[{"evidenceCode":"ECO:0000269","id":"39753131","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":45},"start":{"modifier":"EXACT","value":9}},"type":"Transmembrane"}
```

Source SHA-256: `a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:33.494326+00:00.  

```json
{"description":"Helical; Name=2","evidences":[{"evidenceCode":"ECO:0000269","id":"39753131","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":80},"start":{"modifier":"EXACT","value":50}},"type":"Transmembrane"}
```

Source SHA-256: `a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:33.494326+00:00.  

```json
{"description":"Helical; Name=3","evidences":[{"evidenceCode":"ECO:0000269","id":"39753131","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":121},"start":{"modifier":"EXACT","value":86}},"type":"Transmembrane"}
```

Source SHA-256: `a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:33.494326+00:00.  

```json
{"description":"Helical; Name=4","evidences":[{"evidenceCode":"ECO:0000269","id":"39753131","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":156},"start":{"modifier":"EXACT","value":130}},"type":"Transmembrane"}
```

Source SHA-256: `a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:33.494326+00:00.  

```json
{"description":"Helical; Name=5","evidences":[{"evidenceCode":"ECO:0000269","id":"39753131","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":211},"start":{"modifier":"EXACT","value":173}},"type":"Transmembrane"}
```

Source SHA-256: `a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:33.494326+00:00.  

```json
{"description":"Helical; Name=6","evidences":[{"evidenceCode":"ECO:0000269","id":"39753131","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":251},"start":{"modifier":"EXACT","value":216}},"type":"Transmembrane"}
```

Source SHA-256: `a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:33.494326+00:00.  

```json
{"description":"Helical; Name=7","evidences":[{"evidenceCode":"ECO:0000269","id":"39753131","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":296},"start":{"modifier":"EXACT","value":268}},"type":"Transmembrane"}
```

Source SHA-256: `a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)  
**Locator:** `lines 142-144`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:39.964772+00:00.  

```text
FT   TRANSMEM        9..45
FT                   /note="Helical; Name=1"
FT                   /evidence="ECO:0000269|PubMed:39753131"
```

Source SHA-256: `57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)  
**Locator:** `lines 148-150`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:39.964772+00:00.  

```text
FT   TRANSMEM        50..80
FT                   /note="Helical; Name=2"
FT                   /evidence="ECO:0000269|PubMed:39753131"
```

Source SHA-256: `57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)  
**Locator:** `lines 154-156`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:39.964772+00:00.  

```text
FT   TRANSMEM        86..121
FT                   /note="Helical; Name=3"
FT                   /evidence="ECO:0000269|PubMed:39753131"
```

Source SHA-256: `57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)  
**Locator:** `lines 160-162`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:39.964772+00:00.  

```text
FT   TRANSMEM        130..156
FT                   /note="Helical; Name=4"
FT                   /evidence="ECO:0000269|PubMed:39753131"
```

Source SHA-256: `57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)  
**Locator:** `lines 166-168`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:39.964772+00:00.  

```text
FT   TRANSMEM        173..211
FT                   /note="Helical; Name=5"
FT                   /evidence="ECO:0000269|PubMed:39753131"
```

Source SHA-256: `57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)  
**Locator:** `lines 172-174`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:39.964772+00:00.  

```text
FT   TRANSMEM        216..251
FT                   /note="Helical; Name=6"
FT                   /evidence="ECO:0000269|PubMed:39753131"
```

Source SHA-256: `57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)  
**Locator:** `lines 178-180`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:39.964772+00:00.  

```text
FT   TRANSMEM        268..296
FT                   /note="Helical; Name=7"
FT                   /evidence="ECO:0000269|PubMed:39753131"
```

Source SHA-256: `57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
