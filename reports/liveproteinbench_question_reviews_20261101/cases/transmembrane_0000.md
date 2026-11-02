# transmembrane_0000

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 237..255; 289..311; 332..357; 363..382; 394..416; 436..455; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHQDNSMRRAINQSRNGGSDSCDINNDREHDNINRNSYINNFHIENINSDKNEQSYIYCSDRAQVTDSILGNRKYTHEENINSTEMFSRTNYEYSNKNNVDIEMYNISNNNFYNGNNNGHSNDIIDYINNNNVNKDLSNTSNNADINTYIKKLTSNQSTAYCDGKGYNESANGSNFDINFRDVIKNNNNKNYKNNNHVPDDMLELGDRSFDSSFYIHNNVEEIDTERSNRLSFMSKLKMYFNYFGPGWIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS

[Multiple Choices]
A. 298..318
B. 237..255; 289..311; 332..357; 363..382; 394..416; 436..455; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684
C. 237..255; 289..311; 332..357; 363..382; 394..416; 437..458; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684
D. 237..255; 289..311; 332..357; 363..382; 436..455; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684
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

> The supplied sequence exactly matches the source sequence, and both the current UniProt record and a historical record annotate the transmembrane intervals listed in B, including 436..455. These intervals are annotated as helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental mapping.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [C28](#evidence-c28), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has numerous hydrophobic stretches consistent with a multi-pass membrane protein, so general reasoning can identify likely transmembrane helices. It does not establish the exact annotated boundaries needed to distinguish the near-identical B and C lists.


**Missing item-specific fact**

> The protein-specific transmembrane-region annotation, especially the boundary assigned to the helix around residues 436..455.


**Reason**

> Choosing the keyed set of precise residue coordinates depends on a protein-specific annotation or equivalent item-specific boundary determination absent from the input. General hydropathy reasoning supports the broad topology but not these exact limits.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C list the same predicted helices except for the boundary of one interval: 436..455 versus 437..458. Both intervals include the same likely membrane-spanning helix, and the question gives no boundary convention that makes this small shift biologically unambiguous.


### Important caveats

- Reviewer-only database evidence supports B but was not available to the evaluated model.
- The cited transmembrane features are computationally annotated; they should not be described as experimentally established residue-level boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has numerous hydrophobic stretches consistent with a multi-pass membrane protein, so general reasoning can identify likely transmembrane helices. It does not establish the exact annotated boundaries needed to distinguish the near-identical B and C lists.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotation, especially the boundary assigned to the helix around residues 436..455.",
    "reason": "Choosing the keyed set of precise residue coordinates depends on a protein-specific annotation or equivalent item-specific boundary determination absent from the input. General hydropathy reasoning supports the broad topology but not these exact limits."
  },
  "case_id": "transmembrane_0000",
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
      "C28",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24",
      "H26"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the source sequence, and both the current UniProt record and a historical record annotate the transmembrane intervals listed in B, including 436..455. These intervals are annotated as helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental mapping."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports B but was not available to the evaluated model.",
    "The cited transmembrane features are computationally annotated; they should not be described as experimentally established residue-level boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C list the same predicted helices except for the boundary of one interval: 436..455 versus 437..458. Both intervals include the same likely membrane-spanning helix, and the question gives no boundary convention that makes this small shift biologically unambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the source sequence, and both the current UniProt record and a historical record annotate the transmembrane intervals listed in B, including 436..455. These intervals are annotated as helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental mapping.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26", "C28", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24", "H26"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has numerous hydrophobic stretches consistent with a multi-pass membrane protein, so general reasoning can identify likely transmembrane helices. It does not establish the exact annotated boundaries needed to distinguish the near-identical B and C lists.",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotation, especially the boundary assigned to the helix around residues 436..455.",
    "reason": "Choosing the keyed set of precise residue coordinates depends on a protein-specific annotation or equivalent item-specific boundary determination absent from the input. General hydropathy reasoning supports the broad topology but not these exact limits."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C list the same predicted helices except for the boundary of one interval: 436..455 versus 437..458. Both intervals include the same likely membrane-spanning helix, and the question gives no boundary convention that makes this small shift biologically unambiguous."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports B but was not available to the evaluated model.",
    "The cited transmembrane features are computationally annotated; they should not be described as experimentally established residue-level boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Choice B lists exactly 12 transmembrane regions (237..255; 289..311; 332..357; 363..382; 394..416; 436..455; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684) that match the UniProt annotation for A0A077Y877 (PyDMT1) residue-for-residue. All 12 TM features carry evidence code ECO:0000255 (similarity-based computational annotation), not experimental validation. The sequence match is confirmed (SHA256 identical). Choice C differs only at the 6th TM (437..458 vs 436..455), Choice D omits the 394..416 TM, and Choice A gives a single incorrect region. The database annotation unambiguously supports B.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [C28](#evidence-c28), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can plausibly use hydrophobicity analysis to identify ~12 TM helices in a 696-residue divalent metal transporter (Nramp family), ruling out A (single region) and D (only 11 regions, missing 394..416). However, the critical B-vs-C distinction is a 1-to-3 residue boundary shift at a single TM helix (436..455 vs 437..458). Both boundaries fall within the same hydrophobic stretch, and no general biological principle (helix length, hydrophobicity threshold, flanking charge) reliably selects 436 over 437 or 455 over 458. Distinguishing them requires reproducing the exact output of a specific TM prediction algorithm (e.g., TMHMM, Phobius) or recalling the UniProt annotation.


**Missing item-specific fact**

> The precise residue-level boundary assignment (436..455 vs 437..458) produced by the particular computational predictor used to generate the UniProt annotation (ECO:0000255). This is an item-specific prediction output, not derivable from general hydrophobicity or helix-geometry reasoning.


**Reason**

> While the overall TM topology (12 helices, alternating cytoplasmic/vacuolar) is inferable from sequence hydrophobicity and Nramp-family knowledge, the 1-3 residue boundary perturbation in Choice C is indistinguishable by general biological reasoning. Selection of B over C depends on matching a specific computational prediction or database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C differ only in the 6th TM boundary (436..455 vs 437..458). Both boundaries lie within a continuous hydrophobic stretch, and no general sequence-analysis criterion uniquely selects one over the other. Without the specific prediction algorithm output, both are defensible hydrophobic-helix boundaries. The database annotation resolves this, but that resolution is lookup, not reasoning.


### Important caveats

- All 12 TM annotations carry ECO:0000255 (similarity-based computational inference), not experimental evidence (e.g., cryo-EM or mutagenesis). The boundaries are prediction outputs, not experimentally measured values.
- The UniProt entry was first public 2025-04-09; the author's source snapshot is unknown. The sequence is confirmed identical (SHA256 match), but the annotation version may differ from what the author consulted.
- The protein is a Nramp-family divalent metal transporter (PyDMT1) with 12 predicted TM helices, consistent with the Nramp fold. The alternating cytoplasmic/vacuolar topology is annotated but not independently verified by structural data in the supplied evidence.
- Choice A (298..318) is clearly wrong (single region, incorrect boundaries) and Choice D (missing 394..416) is distinguishable by hydrophobicity analysis, so the effective discrimination is B vs C.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can plausibly use hydrophobicity analysis to identify ~12 TM helices in a 696-residue divalent metal transporter (Nramp family), ruling out A (single region) and D (only 11 regions, missing 394..416). However, the critical B-vs-C distinction is a 1-to-3 residue boundary shift at a single TM helix (436..455 vs 437..458). Both boundaries fall within the same hydrophobic stretch, and no general biological principle (helix length, hydrophobicity threshold, flanking charge) reliably selects 436 over 437 or 455 over 458. Distinguishing them requires reproducing the exact output of a specific TM prediction algorithm (e.g., TMHMM, Phobius) or recalling the UniProt annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise residue-level boundary assignment (436..455 vs 437..458) produced by the particular computational predictor used to generate the UniProt annotation (ECO:0000255). This is an item-specific prediction output, not derivable from general hydrophobicity or helix-geometry reasoning.",
    "reason": "While the overall TM topology (12 helices, alternating cytoplasmic/vacuolar) is inferable from sequence hydrophobicity and Nramp-family knowledge, the 1-3 residue boundary perturbation in Choice C is indistinguishable by general biological reasoning. Selection of B over C depends on matching a specific computational prediction or database entry."
  },
  "case_id": "transmembrane_0000",
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
      "C28",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24",
      "H26"
    ],
    "judgment": "supported",
    "reason": "Choice B lists exactly 12 transmembrane regions (237..255; 289..311; 332..357; 363..382; 394..416; 436..455; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684) that match the UniProt annotation for A0A077Y877 (PyDMT1) residue-for-residue. All 12 TM features carry evidence code ECO:0000255 (similarity-based computational annotation), not experimental validation. The sequence match is confirmed (SHA256 identical). Choice C differs only at the 6th TM (437..458 vs 436..455), Choice D omits the 394..416 TM, and Choice A gives a single incorrect region. The database annotation unambiguously supports B."
  },
  "important_caveats": [
    "All 12 TM annotations carry ECO:0000255 (similarity-based computational inference), not experimental evidence (e.g., cryo-EM or mutagenesis). The boundaries are prediction outputs, not experimentally measured values.",
    "The UniProt entry was first public 2025-04-09; the author's source snapshot is unknown. The sequence is confirmed identical (SHA256 match), but the annotation version may differ from what the author consulted.",
    "The protein is a Nramp-family divalent metal transporter (PyDMT1) with 12 predicted TM helices, consistent with the Nramp fold. The alternating cytoplasmic/vacuolar topology is annotated but not independently verified by structural data in the supplied evidence.",
    "Choice A (298..318) is clearly wrong (single region, incorrect boundaries) and Choice D (missing 394..416) is distinguishable by hydrophobicity analysis, so the effective discrimination is B vs C."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C differ only in the 6th TM boundary (436..455 vs 437..458). Both boundaries lie within a continuous hydrophobic stretch, and no general sequence-analysis criterion uniquely selects one over the other. Without the specific prediction algorithm output, both are defensible hydrophobic-helix boundaries. The database annotation resolves this, but that resolution is lookup, not reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice B lists exactly 12 transmembrane regions (237..255; 289..311; 332..357; 363..382; 394..416; 436..455; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684) that match the UniProt annotation for A0A077Y877 (PyDMT1) residue-for-residue. All 12 TM features carry evidence code ECO:0000255 (similarity-based computational annotation), not experimental validation. The sequence match is confirmed (SHA256 identical). Choice C differs only at the 6th TM (437..458 vs 436..455), Choice D omits the 394..416 TM, and Choice A gives a single incorrect region. The database annotation unambiguously supports B.",
    "evidence_ids": ["C6","C8","C10","C12","C14","C16","C18","C20","C22","C24","C26","C28","H4","H6","H8","H10","H12","H14","H16","H18","H20","H22","H24","H26"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can plausibly use hydrophobicity analysis to identify ~12 TM helices in a 696-residue divalent metal transporter (Nramp family), ruling out A (single region) and D (only 11 regions, missing 394..416). However, the critical B-vs-C distinction is a 1-to-3 residue boundary shift at a single TM helix (436..455 vs 437..458). Both boundaries fall within the same hydrophobic stretch, and no general biological principle (helix length, hydrophobicity threshold, flanking charge) reliably selects 436 over 437 or 455 over 458. Distinguishing them requires reproducing the exact output of a specific TM prediction algorithm (e.g., TMHMM, Phobius) or recalling the UniProt annotation.",
    "missing_item_specific_fact": "The precise residue-level boundary assignment (436..455 vs 437..458) produced by the particular computational predictor used to generate the UniProt annotation (ECO:0000255). This is an item-specific prediction output, not derivable from general hydrophobicity or helix-geometry reasoning.",
    "reason": "While the overall TM topology (12 helices, alternating cytoplasmic/vacuolar) is inferable from sequence hydrophobicity and Nramp-family knowledge, the 1-3 residue boundary perturbation in Choice C is indistinguishable by general biological reasoning. Selection of B over C depends on matching a specific computational prediction or database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C differ only in the 6th TM boundary (436..455 vs 437..458). Both boundaries lie within a continuous hydrophobic stretch, and no general sequence-analysis criterion uniquely selects one over the other. Without the specific prediction algorithm output, both are defensible hydrophobic-helix boundaries. The database annotation resolves this, but that resolution is lookup, not reasoning."
  },
  "important_caveats": [
    "All 12 TM annotations carry ECO:0000255 (similarity-based computational inference), not experimental evidence (e.g., cryo-EM or mutagenesis). The boundaries are prediction outputs, not experimentally measured values.",
    "The UniProt entry was first public 2025-04-09; the author's source snapshot is unknown. The sequence is confirmed identical (SHA256 match), but the annotation version may differ from what the author consulted.",
    "The protein is a Nramp-family divalent metal transporter (PyDMT1) with 12 predicted TM helices, consistent with the Nramp fold. The alternating cytoplasmic/vacuolar topology is annotated but not independently verified by structural data in the supplied evidence.",
    "Choice A (298..318) is clearly wrong (single region, incorrect boundaries) and Choice D (missing 394..416) is distinguishable by hydrophobicity analysis, so the effective discrimination is B vs C."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `boundary_alternative_not_independently_validated`.

> Cited Transmembrane features match keyB including436..455. Original optionC changes only that interval to437..458, as the model states.

**Remaining uncertainty:** The cited annotations establish B as the database coordinate set, not independent validation that C is equally correct. Boundary tolerance remains an interpretive question.

Evidence checked: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [C28](#evidence-c28), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A077Y877` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":255},"start":{"modifier":"EXACT","value":237}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":311},"start":{"modifier":"EXACT","value":289}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":357},"start":{"modifier":"EXACT","value":332}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":382},"start":{"modifier":"EXACT","value":363}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":416},"start":{"modifier":"EXACT","value":394}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":455},"start":{"modifier":"EXACT","value":436}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":499},"start":{"modifier":"EXACT","value":476}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":546},"start":{"modifier":"EXACT","value":530}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":585},"start":{"modifier":"EXACT","value":567}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":615},"start":{"modifier":"EXACT","value":597}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":657},"start":{"modifier":"EXACT","value":635}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/features/24`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":684},"start":{"modifier":"EXACT","value":663}},"type":"Transmembrane"}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 94-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        237..255
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 100-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        289..311
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 106-108`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        332..357
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 112-114`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        363..382
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 118-120`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        394..416
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 124-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        436..455
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 130-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        476..499
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 136-138`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        530..546
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 142-144`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        567..585
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 148-150`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        597..615
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 154-156`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        635..657
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 160-162`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
FT   TRANSMEM        663..684
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
