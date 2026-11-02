# transmembrane_0101

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 29..49; 153..173; 200..220; 399..419; 443..463; 479..499; 526..546; 569..586; 590..610; 635..665; 674..694

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVMSENSNISYCQAVANRTSFFTTAYNGIPETLILNTIFWVLLILLFTVLRHQAGDFGRLALVNSNGSKKRWTEIFYSRAASVVDPQPSTSTQVSPRPSTTSQGVPDSTPLSPIQPEEGLFGWIRVTLKLRKETILLHTGPDAVHYLSFQQHLMAVMALVTIVSLVIILPVNFLNGPKENPYDVNAFGRTTMANLSPDSPWLWVHTIITILYIPLVVLIMRRASGRNAFKKAATRTIMISNISSSDRNKTVVRNYMQELFPDVTIENVSIAYNISRLYVRNAEFERVHEARLYCEHHRNRDTLMVKPEMCSCKKENAYEYYQREERKLSGDVARLRASTMNEPLDIAFITVSTVQEAQNIVTHFTPGTYRQWHLVFAPSPDDLFWENLNVNKSHWYLKFFCVNAVLFLVLFFLSTPAMVVSLLNSRPWVKETEGKISPLVADFLPTLMLWTLSALMPVIVAISDKWMRHYTRSKQNYSIMTKCFGYLLMMIMILPSLGLTSAQALLEWGFLNQTDRWQCIFLPDRGSFYVNYIITAAFIGTALELLRFPELIVYIWSLLKAKSKAETPYIRKAILIEFPFGTHYAWTTLVFTIAIVYSVACPLIMPFAMIYICLKHFVDRHNLYFAYGPSNMISRKGGKIHSTAVTMTKFSVVILVLVMAMICFFRGDNGMARFLLLIISLAITLTLFTFMSPIKRCAATRRPSIVEIAGPAPIYVPDVLKDNGIRTSSVRPSAAAFGGYGSDSVSEYDSSQYSVNSVEA

[Multiple Choices]
A. 29..49; 153..173; 200..220; 399..419; 443..463; 479..499; 526..546; 569..586; 590..610; 635..665; 674..694
B. 20..40; 84..104; 119..139; 180..200; 210..230; 273..293; 304..324; 381..401
C. 29..49; 153..173; 399..419; 443..463; 479..499; 526..546; 569..586; 590..610; 635..665; 674..694
D. 29..49; 153..173; 200..220; 399..419; 443..463; 479..499; 526..546; 569..586; 585..608; 635..665; 674..694
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

> The supplied sequence exactly matches the sequence in the current and historical UniProt records. Their transmembrane annotations match every interval in choice A. These are database annotations with computational evidence code ECO:0000255, not direct experimental determinations of each boundary.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H19](#evidence-h19), [H21](#evidence-h21), [H23](#evidence-h23), [H25](#evidence-h25).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long, strongly hydrophobic stretches consistent with membrane-spanning helices. In particular, the hydrophobic region around 200–220 supports the interval present in A but absent from C, while B's proposed intervals do not correspond to the evident pattern of hydrophobic spans. Near residues 569–610, a short interruption separates two candidate spans, making A's separate intervals more biologically coherent than D's overlapping interval.


**Missing item-specific fact**

> Exact residue boundaries are prediction-dependent; the sequence alone does not establish that the database uses precisely these endpoints.


**Reason**

> The hydrophobic pattern and the choices provide meaningful grounds to distinguish the set of spans, though the exact endpoints are not experimentally established by the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence's hydrophobic spans support A over the alternatives. Small boundary differences can be prediction-dependent, but D's overlapping interval is less consistent with the short interruption between the nearby candidate spans.


### Important caveats

- Reviewer-only database annotations support the expected answer but were not supplied to the evaluated model.
- The annotations are computational and do not independently establish experimentally measured membrane boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long, strongly hydrophobic stretches consistent with membrane-spanning helices. In particular, the hydrophobic region around 200–220 supports the interval present in A but absent from C, while B's proposed intervals do not correspond to the evident pattern of hydrophobic spans. Near residues 569–610, a short interruption separates two candidate spans, making A's separate intervals more biologically coherent than D's overlapping interval.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Exact residue boundaries are prediction-dependent; the sequence alone does not establish that the database uses precisely these endpoints.",
    "reason": "The hydrophobic pattern and the choices provide meaningful grounds to distinguish the set of spans, though the exact endpoints are not experimentally established by the supplied input."
  },
  "case_id": "transmembrane_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24",
      "C26",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17",
      "H19",
      "H21",
      "H23",
      "H25"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the current and historical UniProt records. Their transmembrane annotations match every interval in choice A. These are database annotations with computational evidence code ECO:0000255, not direct experimental determinations of each boundary."
  },
  "important_caveats": [
    "Reviewer-only database annotations support the expected answer but were not supplied to the evaluated model.",
    "The annotations are computational and do not independently establish experimentally measured membrane boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence's hydrophobic spans support A over the alternatives. Small boundary differences can be prediction-dependent, but D's overlapping interval is less consistent with the short interruption between the nearby candidate spans."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the current and historical UniProt records. Their transmembrane annotations match every interval in choice A. These are database annotations with computational evidence code ECO:0000255, not direct experimental determinations of each boundary.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26", "H5", "H7", "H9", "H11", "H13", "H15", "H17", "H19", "H21", "H23", "H25"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long, strongly hydrophobic stretches consistent with membrane-spanning helices. In particular, the hydrophobic region around 200–220 supports the interval present in A but absent from C, while B's proposed intervals do not correspond to the evident pattern of hydrophobic spans. Near residues 569–610, a short interruption separates two candidate spans, making A's separate intervals more biologically coherent than D's overlapping interval.",
    "missing_item_specific_fact": "Exact residue boundaries are prediction-dependent; the sequence alone does not establish that the database uses precisely these endpoints.",
    "reason": "The hydrophobic pattern and the choices provide meaningful grounds to distinguish the set of spans, though the exact endpoints are not experimentally established by the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence's hydrophobic spans support A over the alternatives. Small boundary differences can be prediction-dependent, but D's overlapping interval is less consistent with the short interruption between the nearby candidate spans."
  },
  "important_caveats": [
    "Reviewer-only database annotations support the expected answer but were not supplied to the evaluated model.",
    "The annotations are computational and do not independently establish experimentally measured membrane boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Choice A lists exactly 11 transmembrane regions (29..49; 153..173; 200..220; 399..419; 443..463; 479..499; 526..546; 569..586; 590..610; 635..665; 674..694) that match the UniProt annotation for Q6NP91 (Drosophila Tmem63) residue-for-residue (evidence C6-C26, H5-H25). The sequence match is confirmed (SHA-256 identical). Note: all TM annotations carry evidence code ECO:0000255 (automatic assertion from rule-based method), meaning these are computational predictions rather than experimentally determined boundaries.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H19](#evidence-h19), [H21](#evidence-h21), [H23](#evidence-h23), [H25](#evidence-h25).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could eliminate Choice B (positions like 20..40, 84..104 do not correspond to any hydrophobic stretch in this sequence) and might identify the most prominent TM helices via hydropathy analysis. However, distinguishing A from C requires confirming that positions 200-220 form a TM helix separated from TM1 by only a 26-residue extracellular loop (174-199), and distinguishing A from D requires resolving a 5-residue boundary shift (590..610 vs 585..608) for TM8. Neither distinction follows from general biological reasoning.


**Missing item-specific fact**

> The exact TM boundaries are determined by a specific rule-based prediction algorithm (ECO:0000255, e.g., TMHMM or similar). The 5-residue shift between 585..608 and 590..610 for TM8, and the decision to include/exclude 200..220, depend on the particular algorithm's hydrophobicity threshold, window size, and boundary-shifting rules—facts not derivable from general membrane biology knowledge.


**Reason**

> While hydrophobicity analysis can identify major TM helices, the precise start/end positions of 11 TM segments and the complete correct set cannot be reliably determined without a specific TM prediction tool or database annotation. The A-vs-D distinction (585 vs 590 start) is a 5-residue shift that no general biological principle resolves, and the A-vs-C distinction (presence/absence of 200..220) depends on algorithmic thresholding of a short extracellular loop.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Choices A and D differ only by the TM8 boundary (590..610 vs 585..608). Without a specific prediction algorithm's output or experimental data, both boundaries could be considered reasonable hydrophobic segments. Choice C (missing 200..220) is less defensible if a hydropathy scan reveals a hydrophobic stretch there, but the 26-residue extracellular loop makes this non-obvious. Choice B is clearly wrong.


### Important caveats

- All UniProt TM annotations for this entry carry ECO:0000255 (rule-based computational prediction), not experimental evidence. The 'correct' answer reflects a specific algorithm's output, not experimentally validated membrane topology.
- The protein is Drosophila melanogaster Tmem63 (Q6NP91), a mechanosensitive cation channel with 11 predicted TM helices. The 2024 Li et al. paper (PubMed:38388853) provided functional and subcellular localization data but the TM boundaries remain computational.
- The benchmark sequence SHA-256 matches the UniProt entry exactly (760 residues), confirming the annotation applies to the supplied sequence.
- The author's source snapshot is unknown; the annotation may have been added in a later UniProt release than when the benchmark was constructed, though the sequence itself has been unchanged since 2006.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could eliminate Choice B (positions like 20..40, 84..104 do not correspond to any hydrophobic stretch in this sequence) and might identify the most prominent TM helices via hydropathy analysis. However, distinguishing A from C requires confirming that positions 200-220 form a TM helix separated from TM1 by only a 26-residue extracellular loop (174-199), and distinguishing A from D requires resolving a 5-residue boundary shift (590..610 vs 585..608) for TM8. Neither distinction follows from general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM boundaries are determined by a specific rule-based prediction algorithm (ECO:0000255, e.g., TMHMM or similar). The 5-residue shift between 585..608 and 590..610 for TM8, and the decision to include/exclude 200..220, depend on the particular algorithm's hydrophobicity threshold, window size, and boundary-shifting rules—facts not derivable from general membrane biology knowledge.",
    "reason": "While hydrophobicity analysis can identify major TM helices, the precise start/end positions of 11 TM segments and the complete correct set cannot be reliably determined without a specific TM prediction tool or database annotation. The A-vs-D distinction (585 vs 590 start) is a 5-residue shift that no general biological principle resolves, and the A-vs-C distinction (presence/absence of 200..220) depends on algorithmic thresholding of a short extracellular loop."
  },
  "case_id": "transmembrane_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24",
      "C26",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17",
      "H19",
      "H21",
      "H23",
      "H25"
    ],
    "judgment": "supported",
    "reason": "Choice A lists exactly 11 transmembrane regions (29..49; 153..173; 200..220; 399..419; 443..463; 479..499; 526..546; 569..586; 590..610; 635..665; 674..694) that match the UniProt annotation for Q6NP91 (Drosophila Tmem63) residue-for-residue (evidence C6-C26, H5-H25). The sequence match is confirmed (SHA-256 identical). Note: all TM annotations carry evidence code ECO:0000255 (automatic assertion from rule-based method), meaning these are computational predictions rather than experimentally determined boundaries."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry carry ECO:0000255 (rule-based computational prediction), not experimental evidence. The 'correct' answer reflects a specific algorithm's output, not experimentally validated membrane topology.",
    "The protein is Drosophila melanogaster Tmem63 (Q6NP91), a mechanosensitive cation channel with 11 predicted TM helices. The 2024 Li et al. paper (PubMed:38388853) provided functional and subcellular localization data but the TM boundaries remain computational.",
    "The benchmark sequence SHA-256 matches the UniProt entry exactly (760 residues), confirming the annotation applies to the supplied sequence.",
    "The author's source snapshot is unknown; the annotation may have been added in a later UniProt release than when the benchmark was constructed, though the sequence itself has been unchanged since 2006."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Choices A and D differ only by the TM8 boundary (590..610 vs 585..608). Without a specific prediction algorithm's output or experimental data, both boundaries could be considered reasonable hydrophobic segments. Choice C (missing 200..220) is less defensible if a hydropathy scan reveals a hydrophobic stretch there, but the 26-residue extracellular loop makes this non-obvious. Choice B is clearly wrong."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice A lists exactly 11 transmembrane regions (29..49; 153..173; 200..220; 399..419; 443..463; 479..499; 526..546; 569..586; 590..610; 635..665; 674..694) that match the UniProt annotation for Q6NP91 (Drosophila Tmem63) residue-for-residue (evidence C6-C26, H5-H25). The sequence match is confirmed (SHA-256 identical). Note: all TM annotations carry evidence code ECO:0000255 (automatic assertion from rule-based method), meaning these are computational predictions rather than experimentally determined boundaries.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26", "H5", "H7", "H9", "H11", "H13", "H15", "H17", "H19", "H21", "H23", "H25"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could eliminate Choice B (positions like 20..40, 84..104 do not correspond to any hydrophobic stretch in this sequence) and might identify the most prominent TM helices via hydropathy analysis. However, distinguishing A from C requires confirming that positions 200-220 form a TM helix separated from TM1 by only a 26-residue extracellular loop (174-199), and distinguishing A from D requires resolving a 5-residue boundary shift (590..610 vs 585..608) for TM8. Neither distinction follows from general biological reasoning.",
    "missing_item_specific_fact": "The exact TM boundaries are determined by a specific rule-based prediction algorithm (ECO:0000255, e.g., TMHMM or similar). The 5-residue shift between 585..608 and 590..610 for TM8, and the decision to include/exclude 200..220, depend on the particular algorithm's hydrophobicity threshold, window size, and boundary-shifting rules—facts not derivable from general membrane biology knowledge.",
    "reason": "While hydrophobicity analysis can identify major TM helices, the precise start/end positions of 11 TM segments and the complete correct set cannot be reliably determined without a specific TM prediction tool or database annotation. The A-vs-D distinction (585 vs 590 start) is a 5-residue shift that no general biological principle resolves, and the A-vs-C distinction (presence/absence of 200..220) depends on algorithmic thresholding of a short extracellular loop."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Choices A and D differ only by the TM8 boundary (590..610 vs 585..608). Without a specific prediction algorithm's output or experimental data, both boundaries could be considered reasonable hydrophobic segments. Choice C (missing 200..220) is less defensible if a hydropathy scan reveals a hydrophobic stretch there, but the 26-residue extracellular loop makes this non-obvious. Choice B is clearly wrong."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry carry ECO:0000255 (rule-based computational prediction), not experimental evidence. The 'correct' answer reflects a specific algorithm's output, not experimentally validated membrane topology.",
    "The protein is Drosophila melanogaster Tmem63 (Q6NP91), a mechanosensitive cation channel with 11 predicted TM helices. The 2024 Li et al. paper (PubMed:38388853) provided functional and subcellular localization data but the TM boundaries remain computational.",
    "The benchmark sequence SHA-256 matches the UniProt entry exactly (760 residues), confirming the annotation applies to the supplied sequence.",
    "The author's source snapshot is unknown; the annotation may have been added in a later UniProt release than when the benchmark was constructed, though the sequence itself has been unchanged since 2006."
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

**Accession:** `Q6NP91` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 147. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM0","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":49},"start":{"modifier":"EXACT","value":29}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM1","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":173},"start":{"modifier":"EXACT","value":153}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM2","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":220},"start":{"modifier":"EXACT","value":200}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM3","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":419},"start":{"modifier":"EXACT","value":399}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM4","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":463},"start":{"modifier":"EXACT","value":443}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM5","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":499},"start":{"modifier":"EXACT","value":479}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM6","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":546},"start":{"modifier":"EXACT","value":526}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM7","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":586},"start":{"modifier":"EXACT","value":569}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM8","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":610},"start":{"modifier":"EXACT","value":590}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM9","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":665},"start":{"modifier":"EXACT","value":635}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)  
**Locator:** `/features/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:44.009321+00:00.  

```json
{"description":"Helical; Name=TM10","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":694},"start":{"modifier":"EXACT","value":674}},"type":"Transmembrane"}
```

Source SHA-256: `e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 195-197`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        29..49
FT                   /note="Helical; Name=TM0"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 201-203`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        153..173
FT                   /note="Helical; Name=TM1"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 207-209`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        200..220
FT                   /note="Helical; Name=TM2"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 213-215`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        399..419
FT                   /note="Helical; Name=TM3"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 219-221`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        443..463
FT                   /note="Helical; Name=TM4"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 225-227`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        479..499
FT                   /note="Helical; Name=TM5"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 231-233`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        526..546
FT                   /note="Helical; Name=TM6"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 237-239`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        569..586
FT                   /note="Helical; Name=TM7"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 243-245`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        590..610
FT                   /note="Helical; Name=TM8"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 249-251`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        635..665
FT                   /note="Helical; Name=TM9"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)  
**Locator:** `lines 255-257`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:31:46.465310+00:00.  

```text
FT   TRANSMEM        674..694
FT                   /note="Helical; Name=TM10"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 101. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
