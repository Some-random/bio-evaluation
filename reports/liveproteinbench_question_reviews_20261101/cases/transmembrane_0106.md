# transmembrane_0106

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 32..52; 730..750; 795..815; 845..865; 1111..1131

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNELSVNDAFDDIEIESFDFIWEEWEEYKGDVPLWQHIFCGSIAGLMEHVFMYPLDTLKTYFQTNGHMKYNMIYDNCNTINNNNNNIYRGNNSSYKNTCDKNYKDMNNHRNMQTFKRNFCSSTNCDKCIINNFCKYKTNCYNVMAALHTKNNRYIHNIAEPLKNMANYKINTTNNNNVNNIINNNNNNNKKKSRNIFSYPSHTKQYRNVTYVVNKKMQQNLFNNYISNKCINDPFCCRTKTNVLNMKKDIHKFCHLSKEKYNNVFYQNDTYHPNIYGRKRKTLCRNKNNINLFKNHVHKKYCHSLDDQICHSKIKEDMRNLQNFKNYTCAKNMKRHLYSTVPFFNLKNKGNKNITLPYKEIRSKYILKNGYKSMYQRNAGYYKNLIKMQSAKKNRHQLLALRKCLMSEKKYTIIKNEPFIIRKKKNMRNEYFIGNMKGRCIINTSLNSYTLKRNCLDYHHFVNNLKNICYSIMNICYNIKNTILINPSLPINNNNNNNNNTKMDTFIKLINKCLYNNNAHKIDHKILLSNYLNLFKHTNYSYYYILNNFLKNNAPCTSRKNEWNIFSNFINVLKNKIITNNVDYIRNPNVRRNQILRNNYLYSFLRNYNKNLKRNTHMILNKLTSFKYSIPYIKNKYSNVLINNINTNNNTYSNRNVLNSIRYNNIYKNIMHPIFFPGYYNTIHFRYYNYFSRIIDDKDKGKNKNIINISTKRNNCSSIIRNNLSNLYKGVNVVVLGCIPAHALYFSTFEYSKKYFSRMTSNNSSLKMNNRNISTVSNDIKSEKSNFKLYDLNYFSIAVSGFLATLVHDLIITPIDTLKQRIQLGINKNSKDSLKLLKQNGIRSLYLSLPITLLMNIPYQIIMICTNEKMKKIYFEYICGLNTQNNKKNMENKVIDKVHDETRNQDNIGKDIKNDTYNMDKNGTFLRNQEMINKENRIYNSGALEKHVTSQEKEDKILQSVKQENVSSNNDIVNFYEGQSIYNNDAHNIIRDDINKMTHKNLENNIDNTINSNESDVNRIDNMTNDMNKECDIFSINKNNNSTVLYDQIMKRLEMNSSNKNFSLNFHDKIIRQESSPFEKENYNMNLKNIWIDNYKNDFFNKPFNHITSYFVCAGIGGGIAAVLTNPLDVIKTRIQTECFQTKGFNFFRIVSNIYYREGMRSFFKGSLARMALCIPASAVSWGTYETMKRFFKINFNTT

[Multiple Choices]
A. 32..52; 730..750; 795..815; 1111..1131
B. 25..45; 55..75; 80..100; 116..136; 175..195; 211..231
C. 32..52; 730..750; 795..815; 845..865; 1111..1131
D. 32..52; 730..750; 795..815; 845..865; 1111..1135
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

> The supplied sequence exactly matches the cited UniProt sequence, whose current and archived annotations list the five regions in choice C. These are computationally evidenced helical transmembrane annotations (ECO:0000255), not independent experimental measurements.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Hydrophobic sequence stretches can support approximate transmembrane-helix predictions, but they do not establish the exact annotated boundaries, especially the small endpoint difference between choices C and D.


**Missing item-specific fact**

> The protein-specific predicted transmembrane coordinates, particularly whether the final helix ends at residue 1131 or 1135.


**Reason**

> The sequence allows broad membrane-spanning regions to be inferred, but selecting the exact listed set and boundaries depends on a protein-specific annotation or prediction not supplied to the model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> C matches the cited annotation exactly. D differs only by extending the final region four residues; given that these boundaries are computational predictions and helix boundaries can be uncertain, that near-identical interval may also be defensible as an approximate transmembrane segment.


### Important caveats

- The reviewer-only accession and annotations were not part of the evaluated input.
- The cited transmembrane coordinates are computational annotations, not evidence of experimentally mapped membrane boundaries.
- The author’s exact source snapshot is unknown, although the matching sequence and an archived annotation support the expected choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Hydrophobic sequence stretches can support approximate transmembrane-helix predictions, but they do not establish the exact annotated boundaries, especially the small endpoint difference between choices C and D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific predicted transmembrane coordinates, particularly whether the final helix ends at residue 1131 or 1135.",
    "reason": "The sequence allows broad membrane-spanning regions to be inferred, but selecting the exact listed set and boundaries depends on a protein-specific annotation or prediction not supplied to the model."
  },
  "case_id": "transmembrane_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited UniProt sequence, whose current and archived annotations list the five regions in choice C. These are computationally evidenced helical transmembrane annotations (ECO:0000255), not independent experimental measurements."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not part of the evaluated input.",
    "The cited transmembrane coordinates are computational annotations, not evidence of experimentally mapped membrane boundaries.",
    "The author’s exact source snapshot is unknown, although the matching sequence and an archived annotation support the expected choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "C matches the cited annotation exactly. D differs only by extending the final region four residues; given that these boundaries are computational predictions and helix boundaries can be uncertain, that near-identical interval may also be defensible as an approximate transmembrane segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited UniProt sequence, whose current and archived annotations list the five regions in choice C. These are computationally evidenced helical transmembrane annotations (ECO:0000255), not independent experimental measurements.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Hydrophobic sequence stretches can support approximate transmembrane-helix predictions, but they do not establish the exact annotated boundaries, especially the small endpoint difference between choices C and D.",
    "missing_item_specific_fact": "The protein-specific predicted transmembrane coordinates, particularly whether the final helix ends at residue 1131 or 1135.",
    "reason": "The sequence allows broad membrane-spanning regions to be inferred, but selecting the exact listed set and boundaries depends on a protein-specific annotation or prediction not supplied to the model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "C matches the cited annotation exactly. D differs only by extending the final region four residues; given that these boundaries are computational predictions and helix boundaries can be uncertain, that near-identical interval may also be defensible as an approximate transmembrane segment."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not part of the evaluated input.",
    "The cited transmembrane coordinates are computational annotations, not evidence of experimentally mapped membrane boundaries.",
    "The author’s exact source snapshot is unknown, although the matching sequence and an archived annotation support the expected choice."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q8I397 (Putative mitoferrin, MFRN_PLAF7) lists exactly five transmembrane helical segments at 32..52, 730..750, 795..815, 845..865, and 1111..1131, all annotated with evidence code ECO:0000255 (inferred by similarity). This matches choice C precisely. The sequence in the benchmark (1199 AA, SHA256 matched) corresponds exactly to the annotated entry. The annotation is computational (similarity-based) rather than experimentally determined, but it is the authoritative database annotation and is consistent across both current (v137) and historical (v135) snapshots.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option B (positions 25-231) can be confidently eliminated: the N-terminal ~700 residues are overwhelmingly hydrophilic (dominated by N, K, S, D, E residues in long stretches like 'NNNNNNNNNNIYRGNNSSYKNTCDKNYKDMNNHRNMQTFKRNFCSSTNCDKCIINNFCKYKTNCYNVMAALHTKNNRYIHNIAEPLKNMANYKINTTNNNNVNNIINNNNNNNKKKSRN...'), making transmembrane helices at those positions biologically implausible. The first TM at 32..52 (VPLWQHIFCGSIAGLMEHVFMY region) is a recognizable hydrophobic stretch. In the C-terminal region, multiple hydrophobic segments are identifiable (e.g., 'IAVSGFLATLVHDLIITPIDTLKQRI', 'LYLSLPITLLMNIPYQIIMIC', 'FVCAGIGGGIAAVLTN', 'MRSFFKGSLARMALCIPASAVSWGTYETMKRFF'). The critical C-vs-D distinction (1111..1131 vs 1111..1135) is argumentable from sequence: positions 1132-1135 encode K, T, R, I — introducing two charged residues (K, R) and a polar residue (T) that break the hydrophobic character, making 1131 (ending at hydrophobic I) the natural TM boundary. The C-vs-A distinction (presence of 845..865) requires identifying a fifth hydrophobic segment in the C-terminal region, which is harder but consistent with the mitochondrial carrier fold requiring multiple TM helices.


**Missing item-specific fact**

> The exact inclusion of the 845..865 segment as a fifth TM (distinguishing C from A) requires precise hydrophobicity profiling of that specific region, which is borderline from sequence alone. However, the overall pattern of 21-residue helices and the mitochondrial carrier fold context support its inclusion.


**Reason**

> The question provides sufficient sequence information to eliminate B (hydrophilic N-terminus), identify the first TM at 32-52, recognize multiple hydrophobic stretches in the C-terminal region, and argue the 1131 vs 1135 boundary from the presence of charged residues (K, R) at positions 1132-1135. The 4-vs-5 TM distinction is the most challenging element but is supported by the mitochondrial carrier fold requiring multiple TM helices and the presence of identifiable hydrophobic segments. General hydrophobicity analysis and structural biology knowledge provide meaningful grounds to distinguish the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The distinction between C (1111..1131) and D (1111..1135) is the most subtle. While positions 1132-1135 contain charged/polar residues (K, T, R) that argue against extending the TM helix, a model using a simple hydrophobicity window might still include L and V at 1132-1133 as part of the helix. However, the inclusion of K and R at 1132 and 1134 makes 1135 clearly less defensible. The C-vs-A distinction (4 vs 5 TM regions) is also somewhat arguable if a model misses the hydrophobic segment at 845-865, but the 21-residue periodic pattern and mitochondrial carrier fold context favor C.


### Important caveats

- All five TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries.
- The protein is a 'Putative mitoferrin' (mitochondrial carrier protein MRS3) from Plasmodium falciparum; its TM topology is predicted rather than confirmed by structural or experimental data.
- The exact TM boundaries (particularly 1131 vs 1135 and the inclusion of 845-865) depend on the specific prediction algorithm used by the annotator; different hydrophobicity scales or window sizes could yield slightly different boundaries.
- The reviewer-only UniProt evidence confirms the key but was not available to the evaluated model; the model must work from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option B (positions 25-231) can be confidently eliminated: the N-terminal ~700 residues are overwhelmingly hydrophilic (dominated by N, K, S, D, E residues in long stretches like 'NNNNNNNNNNIYRGNNSSYKNTCDKNYKDMNNHRNMQTFKRNFCSSTNCDKCIINNFCKYKTNCYNVMAALHTKNNRYIHNIAEPLKNMANYKINTTNNNNVNNIINNNNNNNKKKSRN...'), making transmembrane helices at those positions biologically implausible. The first TM at 32..52 (VPLWQHIFCGSIAGLMEHVFMY region) is a recognizable hydrophobic stretch. In the C-terminal region, multiple hydrophobic segments are identifiable (e.g., 'IAVSGFLATLVHDLIITPIDTLKQRI', 'LYLSLPITLLMNIPYQIIMIC', 'FVCAGIGGGIAAVLTN', 'MRSFFKGSLARMALCIPASAVSWGTYETMKRFF'). The critical C-vs-D distinction (1111..1131 vs 1111..1135) is argumentable from sequence: positions 1132-1135 encode K, T, R, I — introducing two charged residues (K, R) and a polar residue (T) that break the hydrophobic character, making 1131 (ending at hydrophobic I) the natural TM boundary. The C-vs-A distinction (presence of 845..865) requires identifying a fifth hydrophobic segment in the C-terminal region, which is harder but consistent with the mitochondrial carrier fold requiring multiple TM helices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact inclusion of the 845..865 segment as a fifth TM (distinguishing C from A) requires precise hydrophobicity profiling of that specific region, which is borderline from sequence alone. However, the overall pattern of 21-residue helices and the mitochondrial carrier fold context support its inclusion.",
    "reason": "The question provides sufficient sequence information to eliminate B (hydrophilic N-terminus), identify the first TM at 32-52, recognize multiple hydrophobic stretches in the C-terminal region, and argue the 1131 vs 1135 boundary from the presence of charged residues (K, R) at positions 1132-1135. The 4-vs-5 TM distinction is the most challenging element but is supported by the mitochondrial carrier fold requiring multiple TM helices and the presence of identifiable hydrophobic segments. General hydrophobicity analysis and structural biology knowledge provide meaningful grounds to distinguish the choices."
  },
  "case_id": "transmembrane_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8I397 (Putative mitoferrin, MFRN_PLAF7) lists exactly five transmembrane helical segments at 32..52, 730..750, 795..815, 845..865, and 1111..1131, all annotated with evidence code ECO:0000255 (inferred by similarity). This matches choice C precisely. The sequence in the benchmark (1199 AA, SHA256 matched) corresponds exactly to the annotated entry. The annotation is computational (similarity-based) rather than experimentally determined, but it is the authoritative database annotation and is consistent across both current (v137) and historical (v135) snapshots."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries.",
    "The protein is a 'Putative mitoferrin' (mitochondrial carrier protein MRS3) from Plasmodium falciparum; its TM topology is predicted rather than confirmed by structural or experimental data.",
    "The exact TM boundaries (particularly 1131 vs 1135 and the inclusion of 845-865) depend on the specific prediction algorithm used by the annotator; different hydrophobicity scales or window sizes could yield slightly different boundaries.",
    "The reviewer-only UniProt evidence confirms the key but was not available to the evaluated model; the model must work from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The distinction between C (1111..1131) and D (1111..1135) is the most subtle. While positions 1132-1135 contain charged/polar residues (K, T, R) that argue against extending the TM helix, a model using a simple hydrophobicity window might still include L and V at 1132-1133 as part of the helix. However, the inclusion of K and R at 1132 and 1134 makes 1135 clearly less defensible. The C-vs-A distinction (4 vs 5 TM regions) is also somewhat arguable if a model misses the hydrophobic segment at 845-865, but the 21-residue periodic pattern and mitochondrial carrier fold context favor C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8I397 (Putative mitoferrin, MFRN_PLAF7) lists exactly five transmembrane helical segments at 32..52, 730..750, 795..815, 845..865, and 1111..1131, all annotated with evidence code ECO:0000255 (inferred by similarity). This matches choice C precisely. The sequence in the benchmark (1199 AA, SHA256 matched) corresponds exactly to the annotated entry. The annotation is computational (similarity-based) rather than experimentally determined, but it is the authoritative database annotation and is consistent across both current (v137) and historical (v135) snapshots.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option B (positions 25-231) can be confidently eliminated: the N-terminal ~700 residues are overwhelmingly hydrophilic (dominated by N, K, S, D, E residues in long stretches like 'NNNNNNNNNNIYRGNNSSYKNTCDKNYKDMNNHRNMQTFKRNFCSSTNCDKCIINNFCKYKTNCYNVMAALHTKNNRYIHNIAEPLKNMANYKINTTNNNNVNNIINNNNNNNKKKSRN...'), making transmembrane helices at those positions biologically implausible. The first TM at 32..52 (VPLWQHIFCGSIAGLMEHVFMY region) is a recognizable hydrophobic stretch. In the C-terminal region, multiple hydrophobic segments are identifiable (e.g., 'IAVSGFLATLVHDLIITPIDTLKQRI', 'LYLSLPITLLMNIPYQIIMIC', 'FVCAGIGGGIAAVLTN', 'MRSFFKGSLARMALCIPASAVSWGTYETMKRFF'). The critical C-vs-D distinction (1111..1131 vs 1111..1135) is argumentable from sequence: positions 1132-1135 encode K, T, R, I — introducing two charged residues (K, R) and a polar residue (T) that break the hydrophobic character, making 1131 (ending at hydrophobic I) the natural TM boundary. The C-vs-A distinction (presence of 845..865) requires identifying a fifth hydrophobic segment in the C-terminal region, which is harder but consistent with the mitochondrial carrier fold requiring multiple TM helices.",
    "missing_item_specific_fact": "The exact inclusion of the 845..865 segment as a fifth TM (distinguishing C from A) requires precise hydrophobicity profiling of that specific region, which is borderline from sequence alone. However, the overall pattern of 21-residue helices and the mitochondrial carrier fold context support its inclusion.",
    "reason": "The question provides sufficient sequence information to eliminate B (hydrophilic N-terminus), identify the first TM at 32-52, recognize multiple hydrophobic stretches in the C-terminal region, and argue the 1131 vs 1135 boundary from the presence of charged residues (K, R) at positions 1132-1135. The 4-vs-5 TM distinction is the most challenging element but is supported by the mitochondrial carrier fold requiring multiple TM helices and the presence of identifiable hydrophobic segments. General hydrophobicity analysis and structural biology knowledge provide meaningful grounds to distinguish the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The distinction between C (1111..1131) and D (1111..1135) is the most subtle. While positions 1132-1135 contain charged/polar residues (K, T, R) that argue against extending the TM helix, a model using a simple hydrophobicity window might still include L and V at 1132-1133 as part of the helix. However, the inclusion of K and R at 1132 and 1134 makes 1135 clearly less defensible. The C-vs-A distinction (4 vs 5 TM regions) is also somewhat arguable if a model misses the hydrophobic segment at 845-865, but the 21-residue periodic pattern and mitochondrial carrier fold context favor C."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries.",
    "The protein is a 'Putative mitoferrin' (mitochondrial carrier protein MRS3) from Plasmodium falciparum; its TM topology is predicted rather than confirmed by structural or experimental data.",
    "The exact TM boundaries (particularly 1131 vs 1135 and the inclusion of 845-865) depend on the specific prediction algorithm used by the annotator; different hydrophobicity scales or window sizes could yield slightly different boundaries.",
    "The reviewer-only UniProt evidence confirms the key but was not available to the evaluated model; the model must work from the sequence alone."
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

**Accession:** `Q8I397` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 135. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.528080+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":52},"start":{"modifier":"EXACT","value":32}},"type":"Transmembrane"}
```

Source SHA-256: `64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.528080+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":750},"start":{"modifier":"EXACT","value":730}},"type":"Transmembrane"}
```

Source SHA-256: `64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.528080+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":815},"start":{"modifier":"EXACT","value":795}},"type":"Transmembrane"}
```

Source SHA-256: `64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.528080+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":865},"start":{"modifier":"EXACT","value":845}},"type":"Transmembrane"}
```

Source SHA-256: `64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.528080+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1131},"start":{"modifier":"EXACT","value":1111}},"type":"Transmembrane"}
```

Source SHA-256: `64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 135 / 1.  
**Retrieved:** 2026-11-02T04:32:05.771018+00:00.  

```text
FT   TRANSMEM        32..52
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 135 / 1.  
**Retrieved:** 2026-11-02T04:32:05.771018+00:00.  

```text
FT   TRANSMEM        730..750
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)  
**Locator:** `lines 113-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 135 / 1.  
**Retrieved:** 2026-11-02T04:32:05.771018+00:00.  

```text
FT   TRANSMEM        795..815
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)  
**Locator:** `lines 116-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 135 / 1.  
**Retrieved:** 2026-11-02T04:32:05.771018+00:00.  

```text
FT   TRANSMEM        845..865
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 135 / 1.  
**Retrieved:** 2026-11-02T04:32:05.771018+00:00.  

```text
FT   TRANSMEM        1111..1131
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
