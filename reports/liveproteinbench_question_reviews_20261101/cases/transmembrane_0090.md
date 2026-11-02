# transmembrane_0090

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 478..498

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGRDARRLPLLPFLLLLLAAAAGVAESATDAEAIHDLARSVPALGWDGDNVCGFEGVTCERGGAGKVTELNLADRGLSGTLPDSLSSLTSLTALQLQGNALTGAVPSLARMGSLARLALDGNAFTSLPPDFLHGLTSLQYLTMENLPLPPWPVPDAIANCSSLDTFSASNASISGPFPAVLATLVSLRNLRLSYNNLTGGLPPELSSLIAMESLQLNNQRSDDKLSGPIDVIASMKSLKLLWIQSNKFTGPIPDLNGTQLEAFNVRDNMLTGVVPPSLTGLMSLKNVSLSNNNFQGPKPAFAAIPGQDEDSGNGFCLNTPGPCSPLTTTLLQVAEGFGYPYELAKTWKGNDPCSPAWVGIVCTSSDVSMINLSRKNLSGRISPALANLTRLARLDLSNNNLTGVIPDVLTTLPSLTVLNVANNRLTGEVPKFKPSVNVLAQGNLFGQSSGSSGGGGGSDGDSSSSDSAGGGKSKPNTGMIIGIIVAVIILFACIALLVHHRKKKNVEKFRPVSTKTSPAESEMMKIQVVGANGISNGSSAFPTELYSHVSAANSSNISELFESHGMQLSVEVLLKATNNFSEDCILGRGGFGVVFKGNLNGKLVAVKRCDSGTMGTKGQEEFLAEIDVLRKVRHRHLVALLGYCTHGNERLLVYEYMSGGTLREHLCDLQQSGFIPLTWTQRMTIALDVARGIEYLHGLAQETFIHRDLKPSNILLDQDLRAKVSDFGLVKLAKDTDKSLMTRIAGTFGYLAPEYATTGKVTTKVDVYAYGVILMEMITGRKVLDDSLPDDETHLVTIFRRNILDKEKFRKFVDPTLELSAEGWTSLLEVADLARHCTAREPYQRPDMCHCVNRLSSLVDQWKPTNIDEDDYEGETSEMGLHQQLEKWRCDDFTISDSDTFGSFNVPRKYNG

[Multiple Choices]
A. 478..498; 128..147
B. 13..35
C. 481..501
D. 478..498
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

> The matched-sequence UniProt annotation places a helical transmembrane region at 478..498, agreeing with D. Its evidence code (ECO:0000255) indicates computational annotation, not direct experimental confirmation.

Citations as saved: [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a pronounced hydrophobic stretch around 478..498, followed by the basic HHRKKK flank. D includes the hydrophobic stretch; C shifts the interval and includes the basic flank. The earlier hydrophobic N-terminus is consistent with a signal peptide, while the long extracellular region followed by this hydrophobic segment and a cytoplasmic kinase domain supports a C-terminal membrane anchor.


**Missing item-specific fact**

> No protein-specific annotation is needed to distinguish these choices from the sequence, although the exact annotated residue boundaries are not experimentally established by the input alone.


**Reason**

> The sequence and domain context provide a concrete basis for identifying the membrane-spanning segment and favor D over the shifted alternative.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The prominent C-terminal hydrophobic interval and its flanking basic residues distinguish D from the shifted interval in C; the other choices do not identify that segment alone.


### Important caveats

- The supporting UniProt feature is computationally annotated; it should not be described as direct experimental evidence.
- Reviewer-only database evidence supports the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a pronounced hydrophobic stretch around 478..498, followed by the basic HHRKKK flank. D includes the hydrophobic stretch; C shifts the interval and includes the basic flank. The earlier hydrophobic N-terminus is consistent with a signal peptide, while the long extracellular region followed by this hydrophobic segment and a cytoplasmic kinase domain supports a C-terminal membrane anchor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is needed to distinguish these choices from the sequence, although the exact annotated residue boundaries are not experimentally established by the input alone.",
    "reason": "The sequence and domain context provide a concrete basis for identifying the membrane-spanning segment and favor D over the shifted alternative."
  },
  "case_id": "transmembrane_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation places a helical transmembrane region at 478..498, agreeing with D. Its evidence code (ECO:0000255) indicates computational annotation, not direct experimental confirmation."
  },
  "important_caveats": [
    "The supporting UniProt feature is computationally annotated; it should not be described as direct experimental evidence.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The prominent C-terminal hydrophobic interval and its flanking basic residues distinguish D from the shifted interval in C; the other choices do not identify that segment alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation places a helical transmembrane region at 478..498, agreeing with D. Its evidence code (ECO:0000255) indicates computational annotation, not direct experimental confirmation.",
    "evidence_ids": ["H4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a pronounced hydrophobic stretch around 478..498, followed by the basic HHRKKK flank. D includes the hydrophobic stretch; C shifts the interval and includes the basic flank. The earlier hydrophobic N-terminus is consistent with a signal peptide, while the long extracellular region followed by this hydrophobic segment and a cytoplasmic kinase domain supports a C-terminal membrane anchor.",
    "missing_item_specific_fact": "No protein-specific annotation is needed to distinguish these choices from the sequence, although the exact annotated residue boundaries are not experimentally established by the input alone.",
    "reason": "The sequence and domain context provide a concrete basis for identifying the membrane-spanning segment and favor D over the shifted alternative."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The prominent C-terminal hydrophobic interval and its flanking basic residues distinguish D from the shifted interval in C; the other choices do not identify that segment alone."
  },
  "important_caveats": [
    "The supporting UniProt feature is computationally annotated; it should not be described as direct experimental evidence.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2R560 (WSS1_ORYSJ) annotates a single transmembrane helix at exactly 478..498 (ECO:0000255, by similarity), flanked by an extracellular topological domain (28..477) and a cytoplasmic domain (499..912). The sequence at that position contains a highly hydrophobic stretch (MIIGIIVAVIILFACIALL…) consistent with a TM alpha-helix. Option D matches the annotation exactly.

Citations as saved: [C6](#evidence-c6), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is a single-pass receptor-like kinase (LRR extracellular domain + intracellular kinase domain). A model can (1) identify the N-terminal signal peptide (residues ~1-27, rich in hydrophobic residues at the very start) and eliminate option B (13..35, which falls within the signal peptide, not a TM helix); (2) recognize there is only one TM segment in a type-I receptor kinase, eliminating option A which lists a spurious second region at 128..147 (within the extracellular LRR domain); (3) locate the prominent hydrophobic stretch in the middle of the sequence (MIIGIIVAVIILFACIALL…) as the sole TM helix. Distinguishing D (478..498) from C (481..501) relies on boundary placement: the hydrophobic core begins at a Met (position ~478) immediately after a polar linker (GKSKPNTG), and the standard TM-helix boundary rule (include the first fully hydrophobic residue, exclude the first polar/charged residue) favors starting at 478 rather than 481. The flanking polar residues (HHRKKK) also support an end near 498.


**Missing item-specific fact**

> The exact 3-residue boundary shift between options C and D is within the typical ±2-3 residue uncertainty of computational TM prediction. A model relying solely on hydrophobicity windows could plausibly select either C or D. However, the broader topological reasoning (single-pass receptor kinase, signal peptide exclusion, LRR domain position) meaningfully eliminates A and B, and the hydrophobicity boundary argument provides a defensible (though fine-grained) preference for D over C.


**Reason**

> General knowledge of receptor-like kinase topology (one TM helix separating extracellular LRR from intracellular kinase), signal peptide recognition, and hydrophobicity-based TM helix identification allow a knowledgeable model to eliminate A and B and narrow to the correct hydrophobic segment. The final C-vs-D distinction is fine-grained but has a defensible biological basis in boundary placement rules.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Options C (481..501) and D (478..498) differ by only 3 residues and both fall within the annotated hydrophobic TM segment. Standard TM prediction tools routinely produce boundary variations of ±2-3 residues. While the hydrophobicity argument slightly favors D (starting at Met after a polar linker), a reasonable model using a hydrophobicity window might select C. This is a fine-grained boundary issue rather than a fundamental biological disagreement.


### Important caveats

- The UniProt TM annotation carries evidence code ECO:0000255 (by similarity), meaning it is computationally inferred rather than experimentally determined.
- The C-vs-D distinction (3-residue shift) is within the normal uncertainty range of TM helix boundary prediction; this makes the question somewhat sensitive to the exact prediction algorithm used.
- The author source snapshot is unknown; the annotation has been present since at least entry version 23 (June 2025 release).
- Option A's inclusion of a non-existent second TM region (128..147) makes it a clearly eliminable distractor via topological reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a single-pass receptor-like kinase (LRR extracellular domain + intracellular kinase domain). A model can (1) identify the N-terminal signal peptide (residues ~1-27, rich in hydrophobic residues at the very start) and eliminate option B (13..35, which falls within the signal peptide, not a TM helix); (2) recognize there is only one TM segment in a type-I receptor kinase, eliminating option A which lists a spurious second region at 128..147 (within the extracellular LRR domain); (3) locate the prominent hydrophobic stretch in the middle of the sequence (MIIGIIVAVIILFACIALL…) as the sole TM helix. Distinguishing D (478..498) from C (481..501) relies on boundary placement: the hydrophobic core begins at a Met (position ~478) immediately after a polar linker (GKSKPNTG), and the standard TM-helix boundary rule (include the first fully hydrophobic residue, exclude the first polar/charged residue) favors starting at 478 rather than 481. The flanking polar residues (HHRKKK) also support an end near 498.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact 3-residue boundary shift between options C and D is within the typical ±2-3 residue uncertainty of computational TM prediction. A model relying solely on hydrophobicity windows could plausibly select either C or D. However, the broader topological reasoning (single-pass receptor kinase, signal peptide exclusion, LRR domain position) meaningfully eliminates A and B, and the hydrophobicity boundary argument provides a defensible (though fine-grained) preference for D over C.",
    "reason": "General knowledge of receptor-like kinase topology (one TM helix separating extracellular LRR from intracellular kinase), signal peptide recognition, and hydrophobicity-based TM helix identification allow a knowledgeable model to eliminate A and B and narrow to the correct hydrophobic segment. The final C-vs-D distinction is fine-grained but has a defensible biological basis in boundary placement rules."
  },
  "case_id": "transmembrane_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C5",
      "C7",
      "H4",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2R560 (WSS1_ORYSJ) annotates a single transmembrane helix at exactly 478..498 (ECO:0000255, by similarity), flanked by an extracellular topological domain (28..477) and a cytoplasmic domain (499..912). The sequence at that position contains a highly hydrophobic stretch (MIIGIIVAVIILFACIALL…) consistent with a TM alpha-helix. Option D matches the annotation exactly."
  },
  "important_caveats": [
    "The UniProt TM annotation carries evidence code ECO:0000255 (by similarity), meaning it is computationally inferred rather than experimentally determined.",
    "The C-vs-D distinction (3-residue shift) is within the normal uncertainty range of TM helix boundary prediction; this makes the question somewhat sensitive to the exact prediction algorithm used.",
    "The author source snapshot is unknown; the annotation has been present since at least entry version 23 (June 2025 release).",
    "Option A's inclusion of a non-existent second TM region (128..147) makes it a clearly eliminable distractor via topological reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Options C (481..501) and D (478..498) differ by only 3 residues and both fall within the annotated hydrophobic TM segment. Standard TM prediction tools routinely produce boundary variations of ±2-3 residues. While the hydrophobicity argument slightly favors D (starting at Met after a polar linker), a reasonable model using a hydrophobicity window might select C. This is a fine-grained boundary issue rather than a fundamental biological disagreement."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2R560 (WSS1_ORYSJ) annotates a single transmembrane helix at exactly 478..498 (ECO:0000255, by similarity), flanked by an extracellular topological domain (28..477) and a cytoplasmic domain (499..912). The sequence at that position contains a highly hydrophobic stretch (MIIGIIVAVIILFACIALL…) consistent with a TM alpha-helix. Option D matches the annotation exactly.",
    "evidence_ids": ["C6", "C5", "C7", "H4", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is a single-pass receptor-like kinase (LRR extracellular domain + intracellular kinase domain). A model can (1) identify the N-terminal signal peptide (residues ~1-27, rich in hydrophobic residues at the very start) and eliminate option B (13..35, which falls within the signal peptide, not a TM helix); (2) recognize there is only one TM segment in a type-I receptor kinase, eliminating option A which lists a spurious second region at 128..147 (within the extracellular LRR domain); (3) locate the prominent hydrophobic stretch in the middle of the sequence (MIIGIIVAVIILFACIALL…) as the sole TM helix. Distinguishing D (478..498) from C (481..501) relies on boundary placement: the hydrophobic core begins at a Met (position ~478) immediately after a polar linker (GKSKPNTG), and the standard TM-helix boundary rule (include the first fully hydrophobic residue, exclude the first polar/charged residue) favors starting at 478 rather than 481. The flanking polar residues (HHRKKK) also support an end near 498.",
    "missing_item_specific_fact": "The exact 3-residue boundary shift between options C and D is within the typical ±2-3 residue uncertainty of computational TM prediction. A model relying solely on hydrophobicity windows could plausibly select either C or D. However, the broader topological reasoning (single-pass receptor kinase, signal peptide exclusion, LRR domain position) meaningfully eliminates A and B, and the hydrophobicity boundary argument provides a defensible (though fine-grained) preference for D over C.",
    "reason": "General knowledge of receptor-like kinase topology (one TM helix separating extracellular LRR from intracellular kinase), signal peptide recognition, and hydrophobicity-based TM helix identification allow a knowledgeable model to eliminate A and B and narrow to the correct hydrophobic segment. The final C-vs-D distinction is fine-grained but has a defensible biological basis in boundary placement rules."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Options C (481..501) and D (478..498) differ by only 3 residues and both fall within the annotated hydrophobic TM segment. Standard TM prediction tools routinely produce boundary variations of ±2-3 residues. While the hydrophobicity argument slightly favors D (starting at Met after a polar linker), a reasonable model using a hydrophobicity window might select C. This is a fine-grained boundary issue rather than a fundamental biological disagreement."
  },
  "important_caveats": [
    "The UniProt TM annotation carries evidence code ECO:0000255 (by similarity), meaning it is computationally inferred rather than experimentally determined.",
    "The C-vs-D distinction (3-residue shift) is within the normal uncertainty range of TM helix boundary prediction; this makes the question somewhat sensitive to the exact prediction algorithm used.",
    "The author source snapshot is unknown; the annotation has been present since at least entry version 23 (June 2025 release).",
    "Option A's inclusion of a non-existent second TM region (128..147) makes it a clearly eliminable distractor via topological reasoning."
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

**Accession:** `Q2R560` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 23. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"description":"Extracellular","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":477},"start":{"modifier":"EXACT","value":28}},"type":"Topological domain"}
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":498},"start":{"modifier":"EXACT","value":478}},"type":"Transmembrane"}
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":912},"start":{"modifier":"EXACT","value":499}},"type":"Topological domain"}
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2R560?format=txt&versions=23)  
**Locator:** `lines 178-180`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-01T06:28:32.565844+00:00.  

```text
FT   TOPO_DOM        28..477
FT                   /note="Extracellular"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `8a1500792a74c38b22c2f5627966de80a760b1fed597a74e00b3d2510fcaa15a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2R560?format=txt&versions=23)  
**Locator:** `lines 181-183`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-01T06:28:32.565844+00:00.  

```text
FT   TRANSMEM        478..498
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `8a1500792a74c38b22c2f5627966de80a760b1fed597a74e00b3d2510fcaa15a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2R560?format=txt&versions=23)  
**Locator:** `lines 184-186`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-01T06:28:32.565844+00:00.  

```text
FT   TOPO_DOM        499..912
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `8a1500792a74c38b22c2f5627966de80a760b1fed597a74e00b3d2510fcaa15a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 90. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
