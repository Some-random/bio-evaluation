# transmembrane_0051

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 222..242

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MALSTLWLVLMLWTSLFSDSQCSTLSQAELQELEQIHTWVVSRSFPCSVTCGLGLLTQELCPIGVTRNISTSSCKLRTISCLDSWQCGLKTQTATVGRRLVLDCLEEVMEAMGRFSFVVSWRFAFAIITTDDSLFTRYEALSLDKVVLDPLREEDSGTYRCDVLDTGKRRVKRMYKGVKVLSPKDLSLDFAQGLIHWEIPESRFANLTSSRKVYSSSTIRNIVIISVPLSFAIAVVIFIFLFCYSRRARRAAHLCQDNI

[Multiple Choices]
A. 218..242
B. 222..242; 622..644
C. 222..242
D. 100..120; 135..155; 182..202; 228..248; 263..283; 293..313; 329..349
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

> The supplied sequence matches the UniProt sequence, whose annotation identifies residues 222–242 as a helical transmembrane region. This annotation is computationally evidenced (ECO:0000255), not reported here as experimental validation.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly hydrophobic stretch around the proposed region, consistent with a membrane-spanning helix. The residues just before it include polar and charged residues, making the longer 218–242 option less plausible as the membrane-crossing segment.


**Missing item-specific fact**

> The database-assigned exact boundary at residue 222 is not supplied; sequence-based hydropathy supports the region but does not establish a uniquely precise annotation boundary.


**Reason**

> General sequence reasoning meaningfully favors C over the alternatives, although the exact coordinate boundary is less certain from sequence alone than the existence of the hydrophobic segment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A extends the segment into preceding polar/charged residues, while the other options do not match the single evident hydrophobic stretch.


### Important caveats

- The supporting UniProt feature is computationally evidenced rather than shown here to be experimentally validated.
- The reviewer-only database annotation was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic stretch around the proposed region, consistent with a membrane-spanning helix. The residues just before it include polar and charged residues, making the longer 218–242 option less plausible as the membrane-crossing segment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The database-assigned exact boundary at residue 222 is not supplied; sequence-based hydropathy supports the region but does not establish a uniquely precise annotation boundary.",
    "reason": "General sequence reasoning meaningfully favors C over the alternatives, although the exact coordinate boundary is less certain from sequence alone than the existence of the hydrophobic segment."
  },
  "case_id": "transmembrane_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt sequence, whose annotation identifies residues 222–242 as a helical transmembrane region. This annotation is computationally evidenced (ECO:0000255), not reported here as experimental validation."
  },
  "important_caveats": [
    "The supporting UniProt feature is computationally evidenced rather than shown here to be experimentally validated.",
    "The reviewer-only database annotation was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A extends the segment into preceding polar/charged residues, while the other options do not match the single evident hydrophobic stretch."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt sequence, whose annotation identifies residues 222–242 as a helical transmembrane region. This annotation is computationally evidenced (ECO:0000255), not reported here as experimental validation.",
    "evidence_ids": ["C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic stretch around the proposed region, consistent with a membrane-spanning helix. The residues just before it include polar and charged residues, making the longer 218–242 option less plausible as the membrane-crossing segment.",
    "missing_item_specific_fact": "The database-assigned exact boundary at residue 222 is not supplied; sequence-based hydropathy supports the region but does not establish a uniquely precise annotation boundary.",
    "reason": "General sequence reasoning meaningfully favors C over the alternatives, although the exact coordinate boundary is less certain from sequence alone than the existence of the hydrophobic segment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A extends the segment into preceding polar/charged residues, while the other options do not match the single evident hydrophobic stretch."
  },
  "important_caveats": [
    "The supporting UniProt feature is computationally evidenced rather than shown here to be experimentally validated.",
    "The reviewer-only database annotation was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (B8JI67, Swiss-Prot) explicitly annotates TRANSMEM 222..242 (Helical) with evidence code ECO:0000255 (inferred by similarity). The sequence at positions 222-242 (IVIISVPLSFAIAVVIFIFLF) is a 21-residue contiguous hydrophobic stretch consistent with a single-pass transmembrane helix. The topological domain annotations (extracellular 19-221, cytoplasmic 243-259) are consistent with this single TM assignment. The annotation is computational (ECO:0000255) rather than experimentally validated, but the hydrophobic character of the segment is directly observable in the supplied sequence.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 259 residues long. Option B includes range 622..644 and option D includes ranges 263..283, 293..313, 329..349, all exceeding the protein length—immediately eliminable. Option D also proposes 7 TM segments (GPCR topology) inconsistent with the sequence. Between A (218..242) and C (222..242): residues 218-221 are T-I-R-N, containing two strongly polar/charged residues (Arg, Asn) that would not be stably embedded in the lipid bilayer. Positions 222-242 (I-V-I-I-S-V-P-L-S-F-A-I-A-V-V-I-F-I-F-L-F) form a continuous hydrophobic stretch of ~21 residues, the hallmark of a single-pass TM helix. Standard TM prediction requires ~18-25 hydrophobic residues without strongly polar interruptions, which cleanly selects C over A.


**Missing item-specific fact**

> None required. The protein length (259 aa) is directly countable from the sequence, and the hydrophobicity profile at positions 218-242 is self-evident from the amino acid identities.


**Reason**

> A model can eliminate B and D by noting ranges exceed the 259-residue protein length. Distinguishing A from C requires only recognizing that Thr-Ile-Arg-Asn (218-221) are too polar for the hydrophobic core of a TM helix, while residues 222 onward are uniformly hydrophobic. This is general transmembrane biology applied to the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D contain ranges exceeding the protein length (259 aa), making them physically impossible. Option A includes polar residues (Arg, Asn) at positions 219-221 that are inconsistent with a membrane-embedded helix core. Only C presents a contiguous hydrophobic segment of appropriate length (21 residues) with no strongly polar interruptions.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary assignment is computational/predicted rather than experimentally determined (e.g., crystallography or cryo-EM).
- TM helix boundaries in practice can vary by 1-3 residues depending on the prediction algorithm; however, the multiple-choice format and the clear hydrophobicity contrast between positions 218-221 and 222-242 make C the unambiguously best answer among the given options.
- The sequence is confirmed as a 259-residue precursor of zebrafish Transmembrane protein 81 (TMM81_DANRE, B8JI67), a single-pass membrane protein, consistent with one TM domain.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 259 residues long. Option B includes range 622..644 and option D includes ranges 263..283, 293..313, 329..349, all exceeding the protein length—immediately eliminable. Option D also proposes 7 TM segments (GPCR topology) inconsistent with the sequence. Between A (218..242) and C (222..242): residues 218-221 are T-I-R-N, containing two strongly polar/charged residues (Arg, Asn) that would not be stably embedded in the lipid bilayer. Positions 222-242 (I-V-I-I-S-V-P-L-S-F-A-I-A-V-V-I-F-I-F-L-F) form a continuous hydrophobic stretch of ~21 residues, the hallmark of a single-pass TM helix. Standard TM prediction requires ~18-25 hydrophobic residues without strongly polar interruptions, which cleanly selects C over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The protein length (259 aa) is directly countable from the sequence, and the hydrophobicity profile at positions 218-242 is self-evident from the amino acid identities.",
    "reason": "A model can eliminate B and D by noting ranges exceed the 259-residue protein length. Distinguishing A from C requires only recognizing that Thr-Ile-Arg-Asn (218-221) are too polar for the hydrophobic core of a TM helix, while residues 222 onward are uniformly hydrophobic. This is general transmembrane biology applied to the supplied sequence."
  },
  "case_id": "transmembrane_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3",
      "C5",
      "C7",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (B8JI67, Swiss-Prot) explicitly annotates TRANSMEM 222..242 (Helical) with evidence code ECO:0000255 (inferred by similarity). The sequence at positions 222-242 (IVIISVPLSFAIAVVIFIFLF) is a 21-residue contiguous hydrophobic stretch consistent with a single-pass transmembrane helix. The topological domain annotations (extracellular 19-221, cytoplasmic 243-259) are consistent with this single TM assignment. The annotation is computational (ECO:0000255) rather than experimentally validated, but the hydrophobic character of the segment is directly observable in the supplied sequence."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary assignment is computational/predicted rather than experimentally determined (e.g., crystallography or cryo-EM).",
    "TM helix boundaries in practice can vary by 1-3 residues depending on the prediction algorithm; however, the multiple-choice format and the clear hydrophobicity contrast between positions 218-221 and 222-242 make C the unambiguously best answer among the given options.",
    "The sequence is confirmed as a 259-residue precursor of zebrafish Transmembrane protein 81 (TMM81_DANRE, B8JI67), a single-pass membrane protein, consistent with one TM domain."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D contain ranges exceeding the protein length (259 aa), making them physically impossible. Option A includes polar residues (Arg, Asn) at positions 219-221 that are inconsistent with a membrane-embedded helix core. Only C presents a contiguous hydrophobic segment of appropriate length (21 residues) with no strongly polar interruptions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (B8JI67, Swiss-Prot) explicitly annotates TRANSMEM 222..242 (Helical) with evidence code ECO:0000255 (inferred by similarity). The sequence at positions 222-242 (IVIISVPLSFAIAVVIFIFLF) is a 21-residue contiguous hydrophobic stretch consistent with a single-pass transmembrane helix. The topological domain annotations (extracellular 19-221, cytoplasmic 243-259) are consistent with this single TM assignment. The annotation is computational (ECO:0000255) rather than experimentally validated, but the hydrophobic character of the segment is directly observable in the supplied sequence.",
    "evidence_ids": ["C6", "H3", "C5", "C7", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 259 residues long. Option B includes range 622..644 and option D includes ranges 263..283, 293..313, 329..349, all exceeding the protein length—immediately eliminable. Option D also proposes 7 TM segments (GPCR topology) inconsistent with the sequence. Between A (218..242) and C (222..242): residues 218-221 are T-I-R-N, containing two strongly polar/charged residues (Arg, Asn) that would not be stably embedded in the lipid bilayer. Positions 222-242 (I-V-I-I-S-V-P-L-S-F-A-I-A-V-V-I-F-I-F-L-F) form a continuous hydrophobic stretch of ~21 residues, the hallmark of a single-pass TM helix. Standard TM prediction requires ~18-25 hydrophobic residues without strongly polar interruptions, which cleanly selects C over A.",
    "missing_item_specific_fact": "None required. The protein length (259 aa) is directly countable from the sequence, and the hydrophobicity profile at positions 218-242 is self-evident from the amino acid identities.",
    "reason": "A model can eliminate B and D by noting ranges exceed the 259-residue protein length. Distinguishing A from C requires only recognizing that Thr-Ile-Arg-Asn (218-221) are too polar for the hydrophobic core of a TM helix, while residues 222 onward are uniformly hydrophobic. This is general transmembrane biology applied to the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D contain ranges exceeding the protein length (259 aa), making them physically impossible. Option A includes polar residues (Arg, Asn) at positions 219-221 that are inconsistent with a membrane-embedded helix core. Only C presents a contiguous hydrophobic segment of appropriate length (21 residues) with no strongly polar interruptions."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary assignment is computational/predicted rather than experimentally determined (e.g., crystallography or cryo-EM).",
    "TM helix boundaries in practice can vary by 1-3 residues depending on the prediction algorithm; however, the multiple-choice format and the clear hydrophobicity contrast between positions 218-221 and 222-242 make C the unambiguously best answer among the given options.",
    "The sequence is confirmed as a 259-residue precursor of zebrafish Transmembrane protein 81 (TMM81_DANRE, B8JI67), a single-pass membrane protein, consistent with one TM domain."
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

**Accession:** `B8JI67` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 92. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8JI67.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.144269+00:00.  

```json
{"description":"Extracellular","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":221},"start":{"modifier":"EXACT","value":19}},"type":"Topological domain"}
```

Source SHA-256: `f3f8005091c0912014ebf7b5bc0c98ba1bc6db24e53c5e397e47069aca9c868a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8JI67.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.144269+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":242},"start":{"modifier":"EXACT","value":222}},"type":"Transmembrane"}
```

Source SHA-256: `f3f8005091c0912014ebf7b5bc0c98ba1bc6db24e53c5e397e47069aca9c868a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8JI67.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.144269+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":259},"start":{"modifier":"EXACT","value":243}},"type":"Topological domain"}
```

Source SHA-256: `f3f8005091c0912014ebf7b5bc0c98ba1bc6db24e53c5e397e47069aca9c868a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8JI67?format=txt&versions=92)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-01T06:27:55.829977+00:00.  

```text
FT   TOPO_DOM        19..221
FT                   /note="Extracellular"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `9a37db43c6aecf1d426aa96f8d8451400e467b3d3dd8984eb6e99dc85bc8509d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8JI67?format=txt&versions=92)  
**Locator:** `lines 122-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-01T06:27:55.829977+00:00.  

```text
FT   TRANSMEM        222..242
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `9a37db43c6aecf1d426aa96f8d8451400e467b3d3dd8984eb6e99dc85bc8509d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8JI67?format=txt&versions=92)  
**Locator:** `lines 125-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-01T06:27:55.829977+00:00.  

```text
FT   TOPO_DOM        243..259
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `9a37db43c6aecf1d426aa96f8d8451400e467b3d3dd8984eb6e99dc85bc8509d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 51. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
