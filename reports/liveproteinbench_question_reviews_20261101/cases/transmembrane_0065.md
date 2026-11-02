# transmembrane_0065

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 18..41; 48..72; 93..113; 135..154; 176..194; 224..244; 258..282

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MWPPVDVRSLTAESLGRASLILAVDLLLFVTSILNITVIAFTPDLSDVIGCYLISLSVADLLTAIFVIPLSIYSTLEGNWRIGGDNSIICKSAAYLQIALFCSTVYTFAWICIDRYSAMMKPSRYSEQSLTRCKCWIVFSWLTSMLLCCPIIVARMQVVFYPDAQLCVLDWSATSAYSVTLLLLVFVPTLVTVFNTGWKIWSAMRNPAALDDSQRMLVETDPNFVLTGFLFVTFFLSWLPLITLKVCELIWGPFDMDLSMLTFFFVWLAVSGPCCKFLIYMFTNHQFRRSFLSYISCSMCCSSRSRYEYHDIGNNSFL

[Multiple Choices]
A. 18..41; 48..72; 93..113; 135..154; 176..194; 224..244; 258..282
B. 18..41; 48..72; 93..113; 135..154; 176..194; 227..248; 258..282
C. 3..23
D. 18..41; 48..72; 93..113; 135..154; 176..194; 258..282
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

> The sequence matches the cited UniProt record, whose seven transmembrane annotations match Choice A, including the 224..244 segment. These annotations are computationally supported (ECO:0000255), not presented as direct experimental measurements.

Citations as saved: [C1](#evidence-c1), [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices. In the disputed region, 224..244 covers a strongly hydrophobic stretch, whereas Choice B extends farther into less hydrophobic residues; Choice C identifies only an N-terminal segment, and Choice D omits a span.


**Missing item-specific fact**

> The exact annotated boundaries are protein-specific, but the choices provide enough sequence evidence to favor the hydrophobic 224..244 segment over the shifted alternative.


**Reason**

> General hydropathy reasoning meaningfully distinguishes the options, though it does not establish experimentally precise boundaries.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice B is a nearby boundary alternative, but its extension into less hydrophobic residues makes it less defensible than Choice A from the supplied sequence.


### Important caveats

- The cited UniProt transmembrane features are computationally supported annotations, not independent experimental confirmation.
- Reviewer-only database evidence supports the key but was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices. In the disputed region, 224..244 covers a strongly hydrophobic stretch, whereas Choice B extends farther into less hydrophobic residues; Choice C identifies only an N-terminal segment, and Choice D omits a span.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact annotated boundaries are protein-specific, but the choices provide enough sequence evidence to favor the hydrophobic 224..244 segment over the shifted alternative.",
    "reason": "General hydropathy reasoning meaningfully distinguishes the options, though it does not establish experimentally precise boundaries."
  },
  "case_id": "transmembrane_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose seven transmembrane annotations match Choice A, including the 224..244 segment. These annotations are computationally supported (ECO:0000255), not presented as direct experimental measurements."
  },
  "important_caveats": [
    "The cited UniProt transmembrane features are computationally supported annotations, not independent experimental confirmation.",
    "Reviewer-only database evidence supports the key but was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice B is a nearby boundary alternative, but its extension into less hydrophobic residues makes it less defensible than Choice A from the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose seven transmembrane annotations match Choice A, including the 224..244 segment. These annotations are computationally supported (ECO:0000255), not presented as direct experimental measurements.",
    "evidence_ids": ["C1", "C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices. In the disputed region, 224..244 covers a strongly hydrophobic stretch, whereas Choice B extends farther into less hydrophobic residues; Choice C identifies only an N-terminal segment, and Choice D omits a span.",
    "missing_item_specific_fact": "The exact annotated boundaries are protein-specific, but the choices provide enough sequence evidence to favor the hydrophobic 224..244 segment over the shifted alternative.",
    "reason": "General hydropathy reasoning meaningfully distinguishes the options, though it does not establish experimentally precise boundaries."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice B is a nearby boundary alternative, but its extension into less hydrophobic residues makes it less defensible than Choice A from the supplied sequence."
  },
  "important_caveats": [
    "The cited UniProt transmembrane features are computationally supported annotations, not independent experimental confirmation.",
    "Reviewer-only database evidence supports the key but was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt O17899 (PCDR1_CAEEL) annotates exactly seven transmembrane helices at 18..41, 48..72, 93..113, 135..154, 176..194, 224..244, 258..282, matching option A precisely. These annotations carry evidence code ECO:0000255 (similarity/automatic annotation), indicating computational/curator-inferred boundaries rather than experimental determination. The sequence matches the benchmark input (SHA-256 confirmed). Both the current entry (v150) and the historical entry (v149, released 2026-01-28) contain identical TM coordinates.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 318-residue sequence contains seven distinct hydrophobic stretches of ~20-25 residues each, consistent with a 7-TM (GPCR-like) topology. Option C (single 21-residue TM at 3..23) is implausible for a protein of this length with multiple long hydrophobic segments. Option D omits the sixth TM region (around residues 224-244), which corresponds to a clear hydrophobic stretch (FVLTGFLFVTFFLSWLPLITLK), leaving only 6 TM helices inconsistent with the observed hydrophobicity pattern. Between A and B, the critical distinction is TM6 boundaries: option B extends TM6 to position 248, which would place Glu247 (a negatively charged residue) and Cys246 within the membrane-spanning helix. Charged/polar residues buried in the hydrophobic core of a lipid bilayer are energetically highly unfavorable unless part of a specific functional site, making option B's boundary at 248 less plausible than option A's boundary at 244 (ending at Lys, a residue commonly found at helix termini per the positive-inside rule).


**Missing item-specific fact**

> None strictly required. The hydrophobicity pattern, helix-length constraints (~19-25 residues for a TM helix), and the energetic penalty of placing a charged Glu within the membrane interior provide sufficient grounds to prefer A over B. However, the 3-residue boundary shift is within the typical uncertainty of TM prediction tools, making this a fine-grained distinction.


**Reason**

> A model can identify multiple hydrophobic stretches from the sequence to infer 7 TM regions (eliminating C and D), and can apply the principle that charged residues (Glu247) are disfavored within the hydrophobic membrane core to prefer TM6 ending at 244 (option A) over 248 (option B). The GPCR 7-TM topology is inferable from the hydrophobicity pattern without prior knowledge of the specific protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the A vs B distinction is subtle (3-residue shift), the presence of Glu247 within option B's proposed TM helix provides a concrete biophysical argument against it. Options C and D are clearly eliminable by hydrophobicity analysis and TM count. No other option is defensible.


### Important caveats

- The UniProt TM annotations use ECO:0000255 (similarity/automatic annotation), meaning boundaries are computationally predicted, not experimentally validated. Exact residue boundaries carry inherent uncertainty of ±3-5 residues.
- The protein is annotated as an 'orphan GPCR' (melatonin receptor pdcr-1), which may lack canonical GPCR sequence motifs (e.g., DRY), making GPCR identification from sequence alone more challenging.
- The distinction between options A and B (TM6 at 224..244 vs 227..248) is within the typical error margin of TM prediction algorithms; a model relying solely on hydropathy plots might not reliably resolve this 3-residue difference.
- The reviewer-only UniProt evidence confirms the key but was not available to the evaluated model; the reasoning assessment is based on what can be inferred from the sequence and general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 318-residue sequence contains seven distinct hydrophobic stretches of ~20-25 residues each, consistent with a 7-TM (GPCR-like) topology. Option C (single 21-residue TM at 3..23) is implausible for a protein of this length with multiple long hydrophobic segments. Option D omits the sixth TM region (around residues 224-244), which corresponds to a clear hydrophobic stretch (FVLTGFLFVTFFLSWLPLITLK), leaving only 6 TM helices inconsistent with the observed hydrophobicity pattern. Between A and B, the critical distinction is TM6 boundaries: option B extends TM6 to position 248, which would place Glu247 (a negatively charged residue) and Cys246 within the membrane-spanning helix. Charged/polar residues buried in the hydrophobic core of a lipid bilayer are energetically highly unfavorable unless part of a specific functional site, making option B's boundary at 248 less plausible than option A's boundary at 244 (ending at Lys, a residue commonly found at helix termini per the positive-inside rule).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The hydrophobicity pattern, helix-length constraints (~19-25 residues for a TM helix), and the energetic penalty of placing a charged Glu within the membrane interior provide sufficient grounds to prefer A over B. However, the 3-residue boundary shift is within the typical uncertainty of TM prediction tools, making this a fine-grained distinction.",
    "reason": "A model can identify multiple hydrophobic stretches from the sequence to infer 7 TM regions (eliminating C and D), and can apply the principle that charged residues (Glu247) are disfavored within the hydrophobic membrane core to prefer TM6 ending at 244 (option A) over 248 (option B). The GPCR 7-TM topology is inferable from the hydrophobicity pattern without prior knowledge of the specific protein."
  },
  "case_id": "transmembrane_0065",
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
    "reason": "UniProt O17899 (PCDR1_CAEEL) annotates exactly seven transmembrane helices at 18..41, 48..72, 93..113, 135..154, 176..194, 224..244, 258..282, matching option A precisely. These annotations carry evidence code ECO:0000255 (similarity/automatic annotation), indicating computational/curator-inferred boundaries rather than experimental determination. The sequence matches the benchmark input (SHA-256 confirmed). Both the current entry (v150) and the historical entry (v149, released 2026-01-28) contain identical TM coordinates."
  },
  "important_caveats": [
    "The UniProt TM annotations use ECO:0000255 (similarity/automatic annotation), meaning boundaries are computationally predicted, not experimentally validated. Exact residue boundaries carry inherent uncertainty of ±3-5 residues.",
    "The protein is annotated as an 'orphan GPCR' (melatonin receptor pdcr-1), which may lack canonical GPCR sequence motifs (e.g., DRY), making GPCR identification from sequence alone more challenging.",
    "The distinction between options A and B (TM6 at 224..244 vs 227..248) is within the typical error margin of TM prediction algorithms; a model relying solely on hydropathy plots might not reliably resolve this 3-residue difference.",
    "The reviewer-only UniProt evidence confirms the key but was not available to the evaluated model; the reasoning assessment is based on what can be inferred from the sequence and general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the A vs B distinction is subtle (3-residue shift), the presence of Glu247 within option B's proposed TM helix provides a concrete biophysical argument against it. Options C and D are clearly eliminable by hydrophobicity analysis and TM count. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt O17899 (PCDR1_CAEEL) annotates exactly seven transmembrane helices at 18..41, 48..72, 93..113, 135..154, 176..194, 224..244, 258..282, matching option A precisely. These annotations carry evidence code ECO:0000255 (similarity/automatic annotation), indicating computational/curator-inferred boundaries rather than experimental determination. The sequence matches the benchmark input (SHA-256 confirmed). Both the current entry (v150) and the historical entry (v149, released 2026-01-28) contain identical TM coordinates.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 318-residue sequence contains seven distinct hydrophobic stretches of ~20-25 residues each, consistent with a 7-TM (GPCR-like) topology. Option C (single 21-residue TM at 3..23) is implausible for a protein of this length with multiple long hydrophobic segments. Option D omits the sixth TM region (around residues 224-244), which corresponds to a clear hydrophobic stretch (FVLTGFLFVTFFLSWLPLITLK), leaving only 6 TM helices inconsistent with the observed hydrophobicity pattern. Between A and B, the critical distinction is TM6 boundaries: option B extends TM6 to position 248, which would place Glu247 (a negatively charged residue) and Cys246 within the membrane-spanning helix. Charged/polar residues buried in the hydrophobic core of a lipid bilayer are energetically highly unfavorable unless part of a specific functional site, making option B's boundary at 248 less plausible than option A's boundary at 244 (ending at Lys, a residue commonly found at helix termini per the positive-inside rule).",
    "missing_item_specific_fact": "None strictly required. The hydrophobicity pattern, helix-length constraints (~19-25 residues for a TM helix), and the energetic penalty of placing a charged Glu within the membrane interior provide sufficient grounds to prefer A over B. However, the 3-residue boundary shift is within the typical uncertainty of TM prediction tools, making this a fine-grained distinction.",
    "reason": "A model can identify multiple hydrophobic stretches from the sequence to infer 7 TM regions (eliminating C and D), and can apply the principle that charged residues (Glu247) are disfavored within the hydrophobic membrane core to prefer TM6 ending at 244 (option A) over 248 (option B). The GPCR 7-TM topology is inferable from the hydrophobicity pattern without prior knowledge of the specific protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the A vs B distinction is subtle (3-residue shift), the presence of Glu247 within option B's proposed TM helix provides a concrete biophysical argument against it. Options C and D are clearly eliminable by hydrophobicity analysis and TM count. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt TM annotations use ECO:0000255 (similarity/automatic annotation), meaning boundaries are computationally predicted, not experimentally validated. Exact residue boundaries carry inherent uncertainty of ±3-5 residues.",
    "The protein is annotated as an 'orphan GPCR' (melatonin receptor pdcr-1), which may lack canonical GPCR sequence motifs (e.g., DRY), making GPCR identification from sequence alone more challenging.",
    "The distinction between options A and B (TM6 at 224..244 vs 227..248) is within the typical error margin of TM prediction algorithms; a model relying solely on hydropathy plots might not reliably resolve this 3-residue difference.",
    "The reviewer-only UniProt evidence confirms the key but was not available to the evaluated model; the reasoning assessment is based on what can be inferred from the sequence and general biology."
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

**Accession:** `O17899` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 149. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
"O17899"
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
{"description":"Helical; Name=1","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":41},"start":{"modifier":"EXACT","value":18}},"type":"Transmembrane"}
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
{"description":"Helical; Name=2","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":72},"start":{"modifier":"EXACT","value":48}},"type":"Transmembrane"}
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
{"description":"Helical; Name=3","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":113},"start":{"modifier":"EXACT","value":93}},"type":"Transmembrane"}
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
{"description":"Helical; Name=4","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":154},"start":{"modifier":"EXACT","value":135}},"type":"Transmembrane"}
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
{"description":"Helical; Name=5","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":194},"start":{"modifier":"EXACT","value":176}},"type":"Transmembrane"}
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
{"description":"Helical; Name=6","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":244},"start":{"modifier":"EXACT","value":224}},"type":"Transmembrane"}
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
{"description":"Helical; Name=7","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":282},"start":{"modifier":"EXACT","value":258}},"type":"Transmembrane"}
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O17899?format=txt&versions=149)  
**Locator:** `lines 111-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 149 / 1.  
**Retrieved:** 2026-11-02T04:29:13.646977+00:00.  

```text
FT   TRANSMEM        18..41
FT                   /note="Helical; Name=1"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d19df2056192527093f5764fb03d847f2eb72aec7681a596ae2cab0c45472c70`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O17899?format=txt&versions=149)  
**Locator:** `lines 117-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 149 / 1.  
**Retrieved:** 2026-11-02T04:29:13.646977+00:00.  

```text
FT   TRANSMEM        48..72
FT                   /note="Helical; Name=2"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d19df2056192527093f5764fb03d847f2eb72aec7681a596ae2cab0c45472c70`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O17899?format=txt&versions=149)  
**Locator:** `lines 123-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 149 / 1.  
**Retrieved:** 2026-11-02T04:29:13.646977+00:00.  

```text
FT   TRANSMEM        93..113
FT                   /note="Helical; Name=3"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d19df2056192527093f5764fb03d847f2eb72aec7681a596ae2cab0c45472c70`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O17899?format=txt&versions=149)  
**Locator:** `lines 129-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 149 / 1.  
**Retrieved:** 2026-11-02T04:29:13.646977+00:00.  

```text
FT   TRANSMEM        135..154
FT                   /note="Helical; Name=4"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d19df2056192527093f5764fb03d847f2eb72aec7681a596ae2cab0c45472c70`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O17899?format=txt&versions=149)  
**Locator:** `lines 135-137`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 149 / 1.  
**Retrieved:** 2026-11-02T04:29:13.646977+00:00.  

```text
FT   TRANSMEM        176..194
FT                   /note="Helical; Name=5"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d19df2056192527093f5764fb03d847f2eb72aec7681a596ae2cab0c45472c70`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O17899?format=txt&versions=149)  
**Locator:** `lines 141-143`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 149 / 1.  
**Retrieved:** 2026-11-02T04:29:13.646977+00:00.  

```text
FT   TRANSMEM        224..244
FT                   /note="Helical; Name=6"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d19df2056192527093f5764fb03d847f2eb72aec7681a596ae2cab0c45472c70`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O17899?format=txt&versions=149)  
**Locator:** `lines 147-149`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 149 / 1.  
**Retrieved:** 2026-11-02T04:29:13.646977+00:00.  

```text
FT   TRANSMEM        258..282
FT                   /note="Helical; Name=7"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d19df2056192527093f5764fb03d847f2eb72aec7681a596ae2cab0c45472c70`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 65. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
