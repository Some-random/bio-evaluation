# transmembrane_0110

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 20..40; 84..104; 119..139; 180..200; 210..230; 273..293; 304..324; 381..401

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKSMISGISSKIVESKKAKIFLLGTRILWIITTIIYIVLFYFITNKYVSLSEDDIDEYNIKGNEEELLKDDKIFNNYYKSYNKINAICGTFLILLCIVNIISSFYSKLNRGYMLYYKRMIGFVSLHLQLLFIAIMFLQNHENELFFCNINKYIYWFEDYDNKTDLFINSGENLCKVHNYSYIFPACFLFFSLIEFVVLYFKIEKHFRKKFLIFYIKMGTGIMYLALFYIFLKSKSFYNNILSEYNIFTLDDYSDPIKIIIFATQKQKMYYFQLLLVSTVSSAIVFCLLGYFDIYTIMKSCRFSLLVNIPISVFTMIVVFSQLLFSSYILETSAFFCAYEEFIEIHKRDQKASNKMIAPSNITETDWFCNLKSFDYIYFTNISTCLVIFGSDFIVSLYLVFSKKYAPKTS

[Multiple Choices]
A. 20..40; 84..104; 119..139; 180..200; 210..230; 273..293; 304..324; 381..401
B. 15..36; 84..104; 119..139; 180..200; 210..230; 273..293; 304..324; 381..401
C. 20..40; 84..104; 119..139; 210..230; 273..293; 304..324; 381..401
D. 9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296
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

> The supplied sequence matches the annotated 409-aa protein sequence. The annotation lists transmembrane helices at all eight ranges in choice A; these features carry computational evidence code ECO:0000255, so they support the key as annotation rather than establishing independent experimental validation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated, roughly 20-residue hydrophobic stretches characteristic of membrane-spanning helices, with more polar or charged regions between them. In particular, residues 20–40 form a much more plausible hydrophobic span than 15–36, which includes charged residues near its start and omits hydrophobic residues at its end; the other choices omit a clear hydrophobic span or give substantially mismatched regions.


**Missing item-specific fact**

> No protein-specific external fact is necessary to distinguish these choices at the level of predicted spans, though exact boundaries are predictions rather than experimentally established from the sequence alone.


**Reason**

> The sequence itself supplies meaningful hydropathy and spacing evidence for the set in A. The reviewer-only annotation corroborates the answer but is not needed as input for this distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives differ in ways the sequence can distinguish: B shifts the first interval into less hydrophobic residues, C omits a strongly hydrophobic candidate span, and D proposes broadly misplaced or excessive regions.


### Important caveats

- The annotation evidence for the transmembrane features is computational (ECO:0000255), not direct experimental evidence.
- Sequence-based hydropathy supports predicted membrane-spanning segments but does not by itself prove exact residue boundaries or topology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated, roughly 20-residue hydrophobic stretches characteristic of membrane-spanning helices, with more polar or charged regions between them. In particular, residues 20–40 form a much more plausible hydrophobic span than 15–36, which includes charged residues near its start and omits hydrophobic residues at its end; the other choices omit a clear hydrophobic span or give substantially mismatched regions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific external fact is necessary to distinguish these choices at the level of predicted spans, though exact boundaries are predictions rather than experimentally established from the sequence alone.",
    "reason": "The sequence itself supplies meaningful hydropathy and spacing evidence for the set in A. The reviewer-only annotation corroborates the answer but is not needed as input for this distinction."
  },
  "case_id": "transmembrane_0110",
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
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated 409-aa protein sequence. The annotation lists transmembrane helices at all eight ranges in choice A; these features carry computational evidence code ECO:0000255, so they support the key as annotation rather than establishing independent experimental validation."
  },
  "important_caveats": [
    "The annotation evidence for the transmembrane features is computational (ECO:0000255), not direct experimental evidence.",
    "Sequence-based hydropathy supports predicted membrane-spanning segments but does not by itself prove exact residue boundaries or topology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ in ways the sequence can distinguish: B shifts the first interval into less hydrophobic residues, C omits a strongly hydrophobic candidate span, and D proposes broadly misplaced or excessive regions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated 409-aa protein sequence. The annotation lists transmembrane helices at all eight ranges in choice A; these features carry computational evidence code ECO:0000255, so they support the key as annotation rather than establishing independent experimental validation.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated, roughly 20-residue hydrophobic stretches characteristic of membrane-spanning helices, with more polar or charged regions between them. In particular, residues 20–40 form a much more plausible hydrophobic span than 15–36, which includes charged residues near its start and omits hydrophobic residues at its end; the other choices omit a clear hydrophobic span or give substantially mismatched regions.",
    "missing_item_specific_fact": "No protein-specific external fact is necessary to distinguish these choices at the level of predicted spans, though exact boundaries are predictions rather than experimentally established from the sequence alone.",
    "reason": "The sequence itself supplies meaningful hydropathy and spacing evidence for the set in A. The reviewer-only annotation corroborates the answer but is not needed as input for this distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ in ways the sequence can distinguish: B shifts the first interval into less hydrophobic residues, C omits a strongly hydrophobic candidate span, and D proposes broadly misplaced or excessive regions."
  },
  "important_caveats": [
    "The annotation evidence for the transmembrane features is computational (ECO:0000255), not direct experimental evidence.",
    "Sequence-based hydropathy supports predicted membrane-spanning segments but does not by itself prove exact residue boundaries or topology."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q8II12 (PMRT1_PLAF7, Plasmodium falciparum) lists exactly eight transmembrane helices at 20..40, 84..104, 119..139, 180..200, 210..230, 273..293, 304..324, 381..401, matching Choice A precisely. The sequence in the question matches the UniProt entry (409 AA, SHA256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (by similarity), indicating computational/predictive annotation rather than direct experimental measurement. The topological domain boundaries flanking these TMs are annotated with ECO:0000305 (curator inference) or ECO:0000303 (PubMed 35404116).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Choice B starts TM1 at position 15, which includes the residues SKIVESKKAK (positions 15-19) containing multiple charged/polar residues (K, E, K, K, K) incompatible with a transmembrane helix core; starting at position 20 (I) gives a clean hydrophobic stretch IFLLGTRILWIITTIIYIVLF. Choice D uses boundaries like 9..45 and 50..80 that encompass clearly hydrophilic/charged segments (e.g., the cytoplasmic N-terminus MKSMISGISSKIVESKKAK and the extracellular loop YFITNKYVSLSEDDIDEYNIKGNEEELLKDDKIFNNYYKSYNKINAICGTFLILLCIVNIISSFYSKL), contradicting the requirement for ~20-residue hydrophobic helices. Choice C omits the 180..200 segment; a hydrophobicity scan of that region should reveal a ~20-residue nonpolar stretch consistent with a TM helix, supporting its inclusion. Thus, general hydrophobicity reasoning and the principle that TM helices avoid charged residues meaningfully distinguish A from B, C, and D.


**Missing item-specific fact**

> Exact boundary precision (e.g., whether TM1 truly begins at 20 vs 19 or 21) relies on the UniProt by-similarity annotation rather than experimental determination. The inclusion of 180..200 as a TM is annotated by similarity and may not be obvious to all hydrophobicity predictors.


**Reason**

> The primary distinctions between the four options are addressable through standard biological reasoning: charged residues disqualify B's TM1 start; D's boundaries include clearly hydrophilic regions; C's omission of a hydrophobic segment at ~180-200 is inconsistent with a hydrophobicity-based scan. Exact residue-level boundary precision has some annotation dependence, but among the presented choices, A is the most hydrophobically consistent and biologically defensible.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While exact TM boundaries (±1-2 residues) are inherently uncertain without experimental data, the four choices differ substantially enough (different start positions for TM1, presence/absence of a full TM segment, completely different boundary scheme in D) that hydrophobicity reasoning should select A over the others. No two options are equally defensible given the sequence.


### Important caveats

- All TM annotations carry ECO:0000255 (by similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a prediction tool's output propagated by similarity.
- The UniProt entry was first public in 2025-04-09; the author's source snapshot is unknown. The sequence itself (version 1, 2003) is stable.
- The A vs C distinction (whether 180..200 is a TM) is the most uncertain element of reasoning; a model might miss this segment if the hydrophobic stretch is borderline.
- The reviewer-only evidence confirms sequence match but was not available to the evaluated model; the model must work from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice B starts TM1 at position 15, which includes the residues SKIVESKKAK (positions 15-19) containing multiple charged/polar residues (K, E, K, K, K) incompatible with a transmembrane helix core; starting at position 20 (I) gives a clean hydrophobic stretch IFLLGTRILWIITTIIYIVLF. Choice D uses boundaries like 9..45 and 50..80 that encompass clearly hydrophilic/charged segments (e.g., the cytoplasmic N-terminus MKSMISGISSKIVESKKAK and the extracellular loop YFITNKYVSLSEDDIDEYNIKGNEEELLKDDKIFNNYYKSYNKINAICGTFLILLCIVNIISSFYSKL), contradicting the requirement for ~20-residue hydrophobic helices. Choice C omits the 180..200 segment; a hydrophobicity scan of that region should reveal a ~20-residue nonpolar stretch consistent with a TM helix, supporting its inclusion. Thus, general hydrophobicity reasoning and the principle that TM helices avoid charged residues meaningfully distinguish A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Exact boundary precision (e.g., whether TM1 truly begins at 20 vs 19 or 21) relies on the UniProt by-similarity annotation rather than experimental determination. The inclusion of 180..200 as a TM is annotated by similarity and may not be obvious to all hydrophobicity predictors.",
    "reason": "The primary distinctions between the four options are addressable through standard biological reasoning: charged residues disqualify B's TM1 start; D's boundaries include clearly hydrophilic regions; C's omission of a hydrophobic segment at ~180-200 is inconsistent with a hydrophobicity-based scan. Exact residue-level boundary precision has some annotation dependence, but among the presented choices, A is the most hydrophobically consistent and biologically defensible."
  },
  "case_id": "transmembrane_0110",
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
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8II12 (PMRT1_PLAF7, Plasmodium falciparum) lists exactly eight transmembrane helices at 20..40, 84..104, 119..139, 180..200, 210..230, 273..293, 304..324, 381..401, matching Choice A precisely. The sequence in the question matches the UniProt entry (409 AA, SHA256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (by similarity), indicating computational/predictive annotation rather than direct experimental measurement. The topological domain boundaries flanking these TMs are annotated with ECO:0000305 (curator inference) or ECO:0000303 (PubMed 35404116)."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (by similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a prediction tool's output propagated by similarity.",
    "The UniProt entry was first public in 2025-04-09; the author's source snapshot is unknown. The sequence itself (version 1, 2003) is stable.",
    "The A vs C distinction (whether 180..200 is a TM) is the most uncertain element of reasoning; a model might miss this segment if the hydrophobic stretch is borderline.",
    "The reviewer-only evidence confirms sequence match but was not available to the evaluated model; the model must work from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While exact TM boundaries (±1-2 residues) are inherently uncertain without experimental data, the four choices differ substantially enough (different start positions for TM1, presence/absence of a full TM segment, completely different boundary scheme in D) that hydrophobicity reasoning should select A over the others. No two options are equally defensible given the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8II12 (PMRT1_PLAF7, Plasmodium falciparum) lists exactly eight transmembrane helices at 20..40, 84..104, 119..139, 180..200, 210..230, 273..293, 304..324, 381..401, matching Choice A precisely. The sequence in the question matches the UniProt entry (409 AA, SHA256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (by similarity), indicating computational/predictive annotation rather than direct experimental measurement. The topological domain boundaries flanking these TMs are annotated with ECO:0000305 (curator inference) or ECO:0000303 (PubMed 35404116).",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Choice B starts TM1 at position 15, which includes the residues SKIVESKKAK (positions 15-19) containing multiple charged/polar residues (K, E, K, K, K) incompatible with a transmembrane helix core; starting at position 20 (I) gives a clean hydrophobic stretch IFLLGTRILWIITTIIYIVLF. Choice D uses boundaries like 9..45 and 50..80 that encompass clearly hydrophilic/charged segments (e.g., the cytoplasmic N-terminus MKSMISGISSKIVESKKAK and the extracellular loop YFITNKYVSLSEDDIDEYNIKGNEEELLKDDKIFNNYYKSYNKINAICGTFLILLCIVNIISSFYSKL), contradicting the requirement for ~20-residue hydrophobic helices. Choice C omits the 180..200 segment; a hydrophobicity scan of that region should reveal a ~20-residue nonpolar stretch consistent with a TM helix, supporting its inclusion. Thus, general hydrophobicity reasoning and the principle that TM helices avoid charged residues meaningfully distinguish A from B, C, and D.",
    "missing_item_specific_fact": "Exact boundary precision (e.g., whether TM1 truly begins at 20 vs 19 or 21) relies on the UniProt by-similarity annotation rather than experimental determination. The inclusion of 180..200 as a TM is annotated by similarity and may not be obvious to all hydrophobicity predictors.",
    "reason": "The primary distinctions between the four options are addressable through standard biological reasoning: charged residues disqualify B's TM1 start; D's boundaries include clearly hydrophilic regions; C's omission of a hydrophobic segment at ~180-200 is inconsistent with a hydrophobicity-based scan. Exact residue-level boundary precision has some annotation dependence, but among the presented choices, A is the most hydrophobically consistent and biologically defensible."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While exact TM boundaries (±1-2 residues) are inherently uncertain without experimental data, the four choices differ substantially enough (different start positions for TM1, presence/absence of a full TM segment, completely different boundary scheme in D) that hydrophobicity reasoning should select A over the others. No two options are equally defensible given the sequence."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (by similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a prediction tool's output propagated by similarity.",
    "The UniProt entry was first public in 2025-04-09; the author's source snapshot is unknown. The sequence itself (version 1, 2003) is stable.",
    "The A vs C distinction (whether 180..200 is a TM) is the most uncertain element of reasoning; a model might miss this segment if the hydrophobic stretch is borderline.",
    "The reviewer-only evidence confirms sequence match but was not available to the evaluated model; the model must work from the raw sequence alone."
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

**Accession:** `Q8II12` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 86. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":40},"start":{"modifier":"EXACT","value":20}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":104},"start":{"modifier":"EXACT","value":84}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":139},"start":{"modifier":"EXACT","value":119}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":200},"start":{"modifier":"EXACT","value":180}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":230},"start":{"modifier":"EXACT","value":210}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":293},"start":{"modifier":"EXACT","value":273}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":324},"start":{"modifier":"EXACT","value":304}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":401},"start":{"modifier":"EXACT","value":381}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 83-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        20..40
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        84..104
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 95-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        119..139
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 101-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        180..200
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        210..230
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 113-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        273..293
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        304..324
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 125-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        381..401
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 110. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
