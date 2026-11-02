# transmembrane_0026

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 1404..1424

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAAKAIQYNIKVDLHEVKDLSFREAAGEKEIVPNPYIEVTVNGVTKTTIQKTQVVSATFNTSFNFTAYLTPDEFARSYVEVAVLHKYMLIGGVGLQSAVIGKYVFSFAYVYTKSQHWIYRQWVTLRNLDQPQDETGLLLITVGVFGPGDAMPVVDETVCVVNEGERTSTDVNVKLTHYSLSVNIFKGQDIPSVAGQFSTVLEPYVKVKHGGAELQTRPLPDSNPDWLASISIPACVPCFDGNVLVELWNGQDSSTAAGTLMGTVVLDYFQLIKNDLPPRWFNFYWRPPAEGLLGAVTDMMASAELREPIAYGGRILLSASAAKVQTPLPLGVRSARPIPDPATQECVWWLDLYEMTSATGYTSELRIEIAFGPHVIKTASLEANALGTYVIGDNLGRLPEMKIFAPVDEVQVWDVMMYVCSPPATTVAAGIADISNWFSGWGGSPTATQNTPEPAETPWTRLAWVRIPYDSRQFQNGKPQWYSLRSLDGSGTDMFSVLLGMEMFPTKAGKQRAPRLEYKLARFYFRALIYEGLHLPAVGYDVFPDPYIQVELASKTLRTSTIRQTLNPSYYEAYEIEIRLPENISLAPDINVEVISESNSLLSSDVVLGSVQYPIQKVPKEWTKAPVWLQLHSKAYPRCKARVLVAFELVPAEKAEDDTYPFYDDIRPSTKEGNIRLFLVGVRLFKPITQPFVTVCFGRDVENTAEPLWSQESSAPRTGEGGNWNFLEEFTVSVSLPKRMQHHSFLEVKIQDRTQGIGGESNVDVGMAYITLNPLLPWLDSRERAESLETFRLQMLEEVLIEDAENARRSADGGLAARTGGGSFDEDATKKKEMLAAERSRKMAIPYNDPDMANLKIEEVDDYVSFKVAPRPQASRLSREGTSRDERGKAPGKSLSGMPGPVARASPGAGEETEKKGDPVAEKKEGGAQAAPPVAPSAHQREALAASPEEETYGFTPEQLNFVLADLEEDDAEEMTRDEVPYELEADFTVDDLPYLRTPIFRPTDAGVPETVGYLKYVCRVFQSTDEDEGAEMDAVCKSLIETYNSTRDLVVRAYVLAARGLVPPSGASDIQTYVWIQDSENAATLPGGLSYNIRDTGYTKKQGFKPEFNRCYTLACSLPENSIVQIAVMNMGRLTDECIGRTYLDVEDRFFNKKVEQMVIEESTPIELRTLKNEGSTVSHGSLRGFFEIMRADYAQLHPPYTLASAEPDEYQLRVVIWRVKAVPLDDNSSISLFVRTIYQLEDSSEIVKDTDTHYNSTDGTAVYNWRMVFDVLIPAQIPVLKLQIWNYALLSSTEPIGEANFDLTADFFRARKRQQHYRVPRMWVRCSHPAHKGKLRGTIEIEASILPREEAEYTPVGNGRDEPNRDPFLPAVTTNRTYIDWQQIGETVGAASSAIMSGLKWTGVWMTVAGIIALVIFVMFLLK

[Multiple Choices]
A. 35..55
B. 1404..1424
C. 1408..1423
D. 1404..1424; 199..217
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

> The sequence-matched UniProt entry annotates residues 1404–1424 as a helical transmembrane region. This is computational annotation, not direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic C-terminal stretch supports a membrane-spanning helix and rules against the nonhydrophobic N-terminal option; it does not establish the exact annotated boundaries over the overlapping shorter choice.


**Missing item-specific fact**

> The protein-specific transmembrane boundaries, particularly whether the region begins at 1404 rather than 1408 and ends at 1424 rather than 1423.


**Reason**

> General sequence reasoning identifies the likely C-terminal transmembrane region, but selecting the exact coordinates requires an item-specific boundary annotation or measurement absent from the input. The reviewer-only database annotation cannot count as information supplied to the model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B matches the annotated 1404–1424 span. C is a shorter, overlapping hydrophobic segment that could also be regarded as membrane-spanning under a broad region-prediction wording; no boundary convention is given to distinguish them.


### Important caveats

- The supplied sequence exactly matches the historical and current UniProt sequence, but the author’s source snapshot is unknown.
- The cited transmembrane annotation carries computational evidence code ECO:0000255; it should not be presented as an experimental measurement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic C-terminal stretch supports a membrane-spanning helix and rules against the nonhydrophobic N-terminal option; it does not establish the exact annotated boundaries over the overlapping shorter choice.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane boundaries, particularly whether the region begins at 1404 rather than 1408 and ends at 1424 rather than 1423.",
    "reason": "General sequence reasoning identifies the likely C-terminal transmembrane region, but selecting the exact coordinates requires an item-specific boundary annotation or measurement absent from the input. The reviewer-only database annotation cannot count as information supplied to the model."
  },
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates residues 1404–1424 as a helical transmembrane region. This is computational annotation, not direct experimental confirmation."
  },
  "important_caveats": [
    "The supplied sequence exactly matches the historical and current UniProt sequence, but the author’s source snapshot is unknown.",
    "The cited transmembrane annotation carries computational evidence code ECO:0000255; it should not be presented as an experimental measurement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B matches the annotated 1404–1424 span. C is a shorter, overlapping hydrophobic segment that could also be regarded as membrane-spanning under a broad region-prediction wording; no boundary convention is given to distinguish them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates residues 1404–1424 as a helical transmembrane region. This is computational annotation, not direct experimental confirmation.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic C-terminal stretch supports a membrane-spanning helix and rules against the nonhydrophobic N-terminal option; it does not establish the exact annotated boundaries over the overlapping shorter choice.",
    "missing_item_specific_fact": "The protein-specific transmembrane boundaries, particularly whether the region begins at 1404 rather than 1408 and ends at 1424 rather than 1423.",
    "reason": "General sequence reasoning identifies the likely C-terminal transmembrane region, but selecting the exact coordinates requires an item-specific boundary annotation or measurement absent from the input. The reviewer-only database annotation cannot count as information supplied to the model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B matches the annotated 1404–1424 span. C is a shorter, overlapping hydrophobic segment that could also be regarded as membrane-spanning under a broad region-prediction wording; no boundary convention is given to distinguish them."
  },
  "important_caveats": [
    "The supplied sequence exactly matches the historical and current UniProt sequence, but the author’s source snapshot is unknown.",
    "The cited transmembrane annotation carries computational evidence code ECO:0000255; it should not be presented as an experimental measurement."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7J6JXB6 (FER1_TOXGO, Toxoplasma gondii Ferlin 1, 1425 AA, sequence matched exactly) annotates a single transmembrane helix at positions 1404..1424 with evidence code ECO:0000255 (inferred by similarity). The sequence at 1404-1424 (TGVWMTVAGIIALVIFVMFLL) contains a clear hydrophobic core (WMTVAGIIALVIFVMFLL, ~18 residues) consistent with a single-pass TM helix. The annotation is computational/automatic rather than experimentally validated, but it is the authoritative database annotation supporting the key.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C1](#evidence-c1), [C2](#evidence-c2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Choice A (35..55) falls in a polar/charged N-terminal region (EKEIVPNPYIEVTVNGVTKTT) with no hydrophobic stretch—eliminated by hydrophobicity reasoning. Choice D adds a second TM at 199..217 (TVLEPYVKVKHGGAELQTR), which is dominated by charged/polar residues (E, K, K, H, Q, R)—clearly not a TM helix, eliminable by reasoning. The remaining B vs C distinction: the full ~21-residue hydrophobic stretch at the C-terminus (TGVWMTVAGIIALVIFVMFLL) matches the canonical 18-25 residue single-pass TM helix length, with Trp at position 1407 serving as a membrane-interface anchor. The broader definition (B, 1404-1424) captures the full helix including interface residues, while C (1408-1423, 16 residues) truncates the helix below the canonical minimum. A hydrophobicity window analysis of the C-terminal 25 residues identifies a ~20-residue hydrophobic segment consistent with B.


**Missing item-specific fact**

> The exact boundary between B (1404..1424) and C (1408..1423) is algorithm-dependent (ECO:0000255 = inferred by similarity). A different TM predictor might place the boundary at 1406 or 1407 rather than 1404. However, the broader 21-residue definition is defensible by canonical TM helix length arguments.


**Reason**

> A model can eliminate A and D by straightforward hydrophobicity reasoning (charged/polar regions cannot span a lipid bilayer). The B vs C distinction is fine but a reasonable biological argument exists: the 21-residue predominantly hydrophobic stretch at the C-terminus is the canonical TM helix length, and the Trp anchor at position 1407 supports including residues from 1404. The question is answerable by general membrane-biophysics reasoning, though the precise boundary is somewhat algorithm-sensitive.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The hydrophobic core (WMTVAGIIALVIFVMFLL, positions ~1407-1424) is unambiguous. The exact N-terminal boundary (whether to include T and G at 1404-1405, which are not strongly hydrophobic) is a matter of prediction-algorithm threshold. Both B and C capture the TM core; B is slightly more generous. The UniProt annotation favors B, but a strict hydrophobicity cutoff might yield something closer to C. This is a fine boundary issue, not a fundamental ambiguity about whether a TM exists.


### Important caveats

- The transmembrane annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction, not experimentally validated.
- The UniProt entry was first released 2025-02-05; the author's source snapshot is unknown but the sequence version (1) has been unchanged since 2021-04-07.
- The B/C boundary distinction is algorithm-sensitive; the question is answerable by reasoning but the precise residue-level boundary is not uniquely determined by biophysics alone.
- Choice D's second segment (199..217) is clearly non-hydrophobic and serves as an effective distractor eliminable by reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice A (35..55) falls in a polar/charged N-terminal region (EKEIVPNPYIEVTVNGVTKTT) with no hydrophobic stretch—eliminated by hydrophobicity reasoning. Choice D adds a second TM at 199..217 (TVLEPYVKVKHGGAELQTR), which is dominated by charged/polar residues (E, K, K, H, Q, R)—clearly not a TM helix, eliminable by reasoning. The remaining B vs C distinction: the full ~21-residue hydrophobic stretch at the C-terminus (TGVWMTVAGIIALVIFVMFLL) matches the canonical 18-25 residue single-pass TM helix length, with Trp at position 1407 serving as a membrane-interface anchor. The broader definition (B, 1404-1424) captures the full helix including interface residues, while C (1408-1423, 16 residues) truncates the helix below the canonical minimum. A hydrophobicity window analysis of the C-terminal 25 residues identifies a ~20-residue hydrophobic segment consistent with B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary between B (1404..1424) and C (1408..1423) is algorithm-dependent (ECO:0000255 = inferred by similarity). A different TM predictor might place the boundary at 1406 or 1407 rather than 1404. However, the broader 21-residue definition is defensible by canonical TM helix length arguments.",
    "reason": "A model can eliminate A and D by straightforward hydrophobicity reasoning (charged/polar regions cannot span a lipid bilayer). The B vs C distinction is fine but a reasonable biological argument exists: the 21-residue predominantly hydrophobic stretch at the C-terminus is the canonical TM helix length, and the Trp anchor at position 1407 supports including residues from 1404. The question is answerable by general membrane-biophysics reasoning, though the precise boundary is somewhat algorithm-sensitive."
  },
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C1",
      "C2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7J6JXB6 (FER1_TOXGO, Toxoplasma gondii Ferlin 1, 1425 AA, sequence matched exactly) annotates a single transmembrane helix at positions 1404..1424 with evidence code ECO:0000255 (inferred by similarity). The sequence at 1404-1424 (TGVWMTVAGIIALVIFVMFLL) contains a clear hydrophobic core (WMTVAGIIALVIFVMFLL, ~18 residues) consistent with a single-pass TM helix. The annotation is computational/automatic rather than experimentally validated, but it is the authoritative database annotation supporting the key."
  },
  "important_caveats": [
    "The transmembrane annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction, not experimentally validated.",
    "The UniProt entry was first released 2025-02-05; the author's source snapshot is unknown but the sequence version (1) has been unchanged since 2021-04-07.",
    "The B/C boundary distinction is algorithm-sensitive; the question is answerable by reasoning but the precise residue-level boundary is not uniquely determined by biophysics alone.",
    "Choice D's second segment (199..217) is clearly non-hydrophobic and serves as an effective distractor eliminable by reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The hydrophobic core (WMTVAGIIALVIFVMFLL, positions ~1407-1424) is unambiguous. The exact N-terminal boundary (whether to include T and G at 1404-1405, which are not strongly hydrophobic) is a matter of prediction-algorithm threshold. Both B and C capture the TM core; B is slightly more generous. The UniProt annotation favors B, but a strict hydrophobicity cutoff might yield something closer to C. This is a fine boundary issue, not a fundamental ambiguity about whether a TM exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7J6JXB6 (FER1_TOXGO, Toxoplasma gondii Ferlin 1, 1425 AA, sequence matched exactly) annotates a single transmembrane helix at positions 1404..1424 with evidence code ECO:0000255 (inferred by similarity). The sequence at 1404-1424 (TGVWMTVAGIIALVIFVMFLL) contains a clear hydrophobic core (WMTVAGIIALVIFVMFLL, ~18 residues) consistent with a single-pass TM helix. The annotation is computational/automatic rather than experimentally validated, but it is the authoritative database annotation supporting the key.",
    "evidence_ids": ["C5", "H4", "C1", "C2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Choice A (35..55) falls in a polar/charged N-terminal region (EKEIVPNPYIEVTVNGVTKTT) with no hydrophobic stretch—eliminated by hydrophobicity reasoning. Choice D adds a second TM at 199..217 (TVLEPYVKVKHGGAELQTR), which is dominated by charged/polar residues (E, K, K, H, Q, R)—clearly not a TM helix, eliminable by reasoning. The remaining B vs C distinction: the full ~21-residue hydrophobic stretch at the C-terminus (TGVWMTVAGIIALVIFVMFLL) matches the canonical 18-25 residue single-pass TM helix length, with Trp at position 1407 serving as a membrane-interface anchor. The broader definition (B, 1404-1424) captures the full helix including interface residues, while C (1408-1423, 16 residues) truncates the helix below the canonical minimum. A hydrophobicity window analysis of the C-terminal 25 residues identifies a ~20-residue hydrophobic segment consistent with B.",
    "missing_item_specific_fact": "The exact boundary between B (1404..1424) and C (1408..1423) is algorithm-dependent (ECO:0000255 = inferred by similarity). A different TM predictor might place the boundary at 1406 or 1407 rather than 1404. However, the broader 21-residue definition is defensible by canonical TM helix length arguments.",
    "reason": "A model can eliminate A and D by straightforward hydrophobicity reasoning (charged/polar regions cannot span a lipid bilayer). The B vs C distinction is fine but a reasonable biological argument exists: the 21-residue predominantly hydrophobic stretch at the C-terminus is the canonical TM helix length, and the Trp anchor at position 1407 supports including residues from 1404. The question is answerable by general membrane-biophysics reasoning, though the precise boundary is somewhat algorithm-sensitive."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The hydrophobic core (WMTVAGIIALVIFVMFLL, positions ~1407-1424) is unambiguous. The exact N-terminal boundary (whether to include T and G at 1404-1405, which are not strongly hydrophobic) is a matter of prediction-algorithm threshold. Both B and C capture the TM core; B is slightly more generous. The UniProt annotation favors B, but a strict hydrophobicity cutoff might yield something closer to C. This is a fine boundary issue, not a fundamental ambiguity about whether a TM exists."
  },
  "important_caveats": [
    "The transmembrane annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction, not experimentally validated.",
    "The UniProt entry was first released 2025-02-05; the author's source snapshot is unknown but the sequence version (1) has been unchanged since 2021-04-07.",
    "The B/C boundary distinction is algorithm-sensitive; the question is answerable by reasoning but the precise residue-level boundary is not uniquely determined by biophysics alone.",
    "Choice D's second segment (199..217) is clearly non-hydrophobic and serves as an effective distractor eliminable by reasoning."
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

**Accession:** `A0A7J6JXB6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 14. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:36.132368+00:00.  

```json
"A0A7J6JXB6"
```

Source SHA-256: `d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:36.132368+00:00.  

```json
{"entryVersion":15,"firstPublicDate":"2025-02-05","lastAnnotationUpdateDate":"2026-06-10","lastSequenceUpdateDate":"2021-04-07","sequenceVersion":1}
```

Source SHA-256: `d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:36.132368+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1424},"start":{"modifier":"EXACT","value":1404}},"type":"Transmembrane"}
```

Source SHA-256: `d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)  
**Locator:** `lines 95-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 14 / 1.  
**Retrieved:** 2026-11-02T04:25:38.159549+00:00.  

```text
FT   TRANSMEM        1404..1424
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
