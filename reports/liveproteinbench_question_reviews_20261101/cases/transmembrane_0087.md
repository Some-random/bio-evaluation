# transmembrane_0087

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 1599..1619; 1662..1682; 1704..1724; 1763..1783; 1796..1816

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKFKKELINILALIFVLKKNIFAQSICPTGYQMTQGSCTAIQCPNGQYYDSNLGLCANCDQACSACNYYPTYCTQCQNGFYLYQNQCLTQCPQAQTYVSCSGSSCICQACDSSCTQCFGNKNTQCLACSVGFYYNQINSSCLKQCEDGYTQQIVNIGASQQLLCIPCDNNCRTCSQTNAQQCLTCKDNMYLNTATNQCVSTCPQLQYKINGICKICPTGCQTCYNTNPSNPSTVESCLSCVSGYFLDIENQLCVKNCVSGYVVDAATQRCLPCNATCKNCSDQTNQGCLQCQNGYSLTSGSPSSCQNNCPNGNYQNSSLCLSCNTACSECFGADNQQCTACKTGYYLYKTQCLVICPVGFYTFARQYADPLKQPICDYCPNEMEQCEQDKSNFDLIKPILCKRGYYLYNGTCVKTCPDQTYYQDEATRSCLPCVFPCQTCLSASVCLTCATYTPNGQVQGQTYIFAQITYNGPQGTVFQQNCVPACPKGFYQNSKNNSCQVCNQQCQTCQGPAQTDCITCQIYDSNNMLFKYNNQCYYTCPSSQNNPMYGDKTTQACLPCSQECSSCFNGNNKSCYSCMNGYFLEYLKPECKSFCASDGTYMNSSTNQCSLCGFGCSSCTNGTFNSCISCLNGYYLQQNYNVCYPCPQQCASCTDMNTCQSCNQGYFLYSQTNSCVQQCPLIGFYVDTTQQACIPCDASCLECYGGANNQCISCPKGSYLKTDGTCQQCSQCSSNNECLGPNITDCLNQPICKPGQYLYDGQCLTCFPYCSTCSGTTYDSCISCQTTTDYTLLFDVCKKKVSQTDTQCDIGFYYDSVNKQCYSCHQNCIQCFGKSSSQCTKCSSGYLLHLDITTCSSTCLDGYYQQDPSIPQCSPCLYNCINGCSSGYQFLLGLCFTQCPFGTTAQKENCSFNSKPSIQFAQNLGNSVNNNSQTISLQLLVYSKNLFSIKWRLFTGNTDISNGPIQSYIQNRFDYIVFPPKSLQSNTQYTIQASILDLANNCQNENDCMVQQTFQTMNAITKGNFNIEINSAYLQLTLIISGWLFNSVPDNISFDLYVKLTGNDYFFFDKGQNYQDGRFTYLIPNLSYDLQDNKAQFFLVIYNDFDVQIQQLLIALNLNLQQTTISIDEFLDSVYSKITTLQQIQSLSYQFYSQMQNLMSSQTTSQTIFNRHLFYQVYSSLKGVQIPCDSNINCSGNGKCLWSQDNYNEILCICNINYAGRYCEFQSYQLDIARQHLIALTDLISNIPLNKSSDLFFTIEVLLELTYFYSIFDEFTLNTLINVYFQVFNQLQRVQSNISDEKILFKISKLTSQLINLINEDQTLSYNDQQSLLMKTMNDFDSQINLYLQNFAKSFDDLKSQEQVQTSFQTDISNINLNLIYQNDLLDAFMSNNGASDGQQQTPIVFYGDQISYTFDITQFSPKSSLSTAVIKWNSNPFLSQSQYQAPFISCITELVIYSQQTEIQISTVSQIVEIAIPKILPTPILSVIRPFYQPYTCIYFDSVSQVYKQDGVQYLRENSTHVICGSEQISGNYGVIVNQEYIDPNLSLTVIWNATQQIYANDQQFINFINQLINSNNNNGTNENPQVSQSSFNPNLSLLYALLIYIIFITIFIVISIIRDRKDQETYIKESDSYWLVHPIYSLIFGPYSSFFPRLQRSINYAQLIINLFLYNAIFVLVYSLPSEQELQQNVGKRQIISIQISSTSVACSIVTYYLTICMVNLFKMKWYIKQKWLDFKQDKITTEIVEQVTKSLKIFHLMNYGLVFMLQAGMGIPIIILILSFNSQQNQFFFTSVFASFVIDNILDIIILISFCFIKIFSQSEKSKIILLFTLRGFYYPVYEFLDIEDKIKEYQQKGEVLPAEEANNQSDDEDIFEINDHMNTPKRIFKKNEEKIDKAQEEIQLNEFVNNLKTNQ

[Multiple Choices]
A. 1599..1619; 1704..1724; 1763..1783; 1796..1816
B. 1599..1619; 1662..1682; 1704..1724; 1758..1784; 1796..1816
C. 25..45; 55..75; 80..100; 116..136; 175..195; 211..231
D. 1599..1619; 1662..1682; 1704..1724; 1763..1783; 1796..1816
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

> The sequence-matched historical UniProt record annotates all five intervals in D as transmembrane helices. These annotations carry evidence code ECO:0000255, so they support the key as database computational annotations, not as independent experimental confirmation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, distinguishing that region from the cysteine-rich N-terminal region. This supports the general location and likely number of spans, but not the exact boundaries in the choices.


**Missing item-specific fact**

> The precise annotated endpoints, especially whether the last interval is 1763..1783 or the broader 1758..1784, and the exact set of annotated spans.


**Reason**

> Choosing the precise interval set requires protein-specific boundary information not reliably determined from general sequence heuristics. The matching database annotation supports D, but reviewer-only evidence does not make the original input alone sufficient to resolve exact endpoints.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D include the same hydrophobic core at the final span, with B giving a broader interval. Because membrane-span boundaries can be uncertain and the wording does not specify a boundary convention, both could identify a segment crossing the membrane; D matches the database annotation more exactly.


### Important caveats

- The historical and current UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.
- The cited transmembrane features are computational annotations, not evidence of experimental measurement of the exact boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, distinguishing that region from the cysteine-rich N-terminal region. This supports the general location and likely number of spans, but not the exact boundaries in the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise annotated endpoints, especially whether the last interval is 1763..1783 or the broader 1758..1784, and the exact set of annotated spans.",
    "reason": "Choosing the precise interval set requires protein-specific boundary information not reliably determined from general sequence heuristics. The matching database annotation supports D, but reviewer-only evidence does not make the original input alone sufficient to resolve exact endpoints."
  },
  "case_id": "transmembrane_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all five intervals in D as transmembrane helices. These annotations carry evidence code ECO:0000255, so they support the key as database computational annotations, not as independent experimental confirmation."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The cited transmembrane features are computational annotations, not evidence of experimental measurement of the exact boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D include the same hydrophobic core at the final span, with B giving a broader interval. Because membrane-span boundaries can be uncertain and the wording does not specify a boundary convention, both could identify a segment crossing the membrane; D matches the database annotation more exactly."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all five intervals in D as transmembrane helices. These annotations carry evidence code ECO:0000255, so they support the key as database computational annotations, not as independent experimental confirmation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, distinguishing that region from the cysteine-rich N-terminal region. This supports the general location and likely number of spans, but not the exact boundaries in the choices.",
    "missing_item_specific_fact": "The precise annotated endpoints, especially whether the last interval is 1763..1783 or the broader 1758..1784, and the exact set of annotated spans.",
    "reason": "Choosing the precise interval set requires protein-specific boundary information not reliably determined from general sequence heuristics. The matching database annotation supports D, but reviewer-only evidence does not make the original input alone sufficient to resolve exact endpoints."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D include the same hydrophobic core at the final span, with B giving a broader interval. Because membrane-span boundaries can be uncertain and the wording does not specify a boundary convention, both could identify a segment crossing the membrane; D matches the database annotation more exactly."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The cited transmembrane features are computational annotations, not evidence of experimental measurement of the exact boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q22HI5 (Cysteine repeat modular protein 2, Tetrahymena thermophila, 1915 AA, sequence matched) annotates exactly five transmembrane helical regions: 1599..1619, 1662..1682, 1704..1724, 1763..1783, 1796..1816, all with evidence code ECO:0000255 (inferred by similarity). This matches Choice D precisely. The sequence SHA256 of the benchmark input matches the UniProt record.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice C (positions 25-231) can be eliminated by reasoning: that region is dominated by cysteine-rich EGF-like domains (repeated C-x-x-C motifs with N/Q/Y residues), which are hydrophilic extracellular domains incompatible with membrane-spanning helices. The general C-terminal location of TMs is also identifiable by hydrophobicity scanning. However, distinguishing D from A (whether 1662..1682 constitutes a fifth TM) and from B (whether the fourth TM boundary is 1763..1783 or 1758..1784) requires knowledge of the specific prediction algorithm's output for this protein.


**Missing item-specific fact**

> The exact TM helix boundaries (e.g., 1763 vs 1758 as start, 1783 vs 1784 as end) and the decision to include 1662..1682 as a TM depend on the particular similarity-based prediction (ECO:0000255) used by UniProt curators for this protein. These boundary choices are within the typical uncertainty range of TM prediction and cannot be reliably resolved by hydrophobicity analysis of the sequence alone.


**Reason**

> While general reasoning eliminates C and identifies the C-terminal region as TM-containing, the fine distinctions among A, B, and D (number of TMs and exact helix boundaries differing by 5 residues) depend on the specific computational prediction recorded in the database entry, not on general biological principles applicable to the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The difference between B and D is a 5-residue boundary shift on one TM (1758..1784 vs 1763..1783). TM helix boundaries are inherently fuzzy, and both ranges fall within the plausible hydrophobic core of the same helix. Without knowing which prediction algorithm or similarity template was used, a careful hydrophobicity analysis might yield either boundary. However, D matches the UniProt annotation exactly, making it the intended answer.


### Important caveats

- All TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally verified membrane-spanning regions.
- The UniProt entry was first publicly released in February 2025; the author's source snapshot date is unknown. The sequence version (2) and content match the benchmark input.
- The protein is from Tetrahymena thermophila, a ciliate with unusual genetic code features, but the sequence itself matches the canonical entry.
- The N-terminal ~1500 residues consist of multiple cysteine-rich EGF-like domains, making the protein predominantly extracellular/secreted with a C-terminal TM domain architecture.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice C (positions 25-231) can be eliminated by reasoning: that region is dominated by cysteine-rich EGF-like domains (repeated C-x-x-C motifs with N/Q/Y residues), which are hydrophilic extracellular domains incompatible with membrane-spanning helices. The general C-terminal location of TMs is also identifiable by hydrophobicity scanning. However, distinguishing D from A (whether 1662..1682 constitutes a fifth TM) and from B (whether the fourth TM boundary is 1763..1783 or 1758..1784) requires knowledge of the specific prediction algorithm's output for this protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM helix boundaries (e.g., 1763 vs 1758 as start, 1783 vs 1784 as end) and the decision to include 1662..1682 as a TM depend on the particular similarity-based prediction (ECO:0000255) used by UniProt curators for this protein. These boundary choices are within the typical uncertainty range of TM prediction and cannot be reliably resolved by hydrophobicity analysis of the sequence alone.",
    "reason": "While general reasoning eliminates C and identifies the C-terminal region as TM-containing, the fine distinctions among A, B, and D (number of TMs and exact helix boundaries differing by 5 residues) depend on the specific computational prediction recorded in the database entry, not on general biological principles applicable to the sequence."
  },
  "case_id": "transmembrane_0087",
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
    "reason": "UniProt entry Q22HI5 (Cysteine repeat modular protein 2, Tetrahymena thermophila, 1915 AA, sequence matched) annotates exactly five transmembrane helical regions: 1599..1619, 1662..1682, 1704..1724, 1763..1783, 1796..1816, all with evidence code ECO:0000255 (inferred by similarity). This matches Choice D precisely. The sequence SHA256 of the benchmark input matches the UniProt record."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally verified membrane-spanning regions.",
    "The UniProt entry was first publicly released in February 2025; the author's source snapshot date is unknown. The sequence version (2) and content match the benchmark input.",
    "The protein is from Tetrahymena thermophila, a ciliate with unusual genetic code features, but the sequence itself matches the canonical entry.",
    "The N-terminal ~1500 residues consist of multiple cysteine-rich EGF-like domains, making the protein predominantly extracellular/secreted with a C-terminal TM domain architecture."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The difference between B and D is a 5-residue boundary shift on one TM (1758..1784 vs 1763..1783). TM helix boundaries are inherently fuzzy, and both ranges fall within the plausible hydrophobic core of the same helix. Without knowing which prediction algorithm or similarity template was used, a careful hydrophobicity analysis might yield either boundary. However, D matches the UniProt annotation exactly, making it the intended answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q22HI5 (Cysteine repeat modular protein 2, Tetrahymena thermophila, 1915 AA, sequence matched) annotates exactly five transmembrane helical regions: 1599..1619, 1662..1682, 1704..1724, 1763..1783, 1796..1816, all with evidence code ECO:0000255 (inferred by similarity). This matches Choice D precisely. The sequence SHA256 of the benchmark input matches the UniProt record.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice C (positions 25-231) can be eliminated by reasoning: that region is dominated by cysteine-rich EGF-like domains (repeated C-x-x-C motifs with N/Q/Y residues), which are hydrophilic extracellular domains incompatible with membrane-spanning helices. The general C-terminal location of TMs is also identifiable by hydrophobicity scanning. However, distinguishing D from A (whether 1662..1682 constitutes a fifth TM) and from B (whether the fourth TM boundary is 1763..1783 or 1758..1784) requires knowledge of the specific prediction algorithm's output for this protein.",
    "missing_item_specific_fact": "The exact TM helix boundaries (e.g., 1763 vs 1758 as start, 1783 vs 1784 as end) and the decision to include 1662..1682 as a TM depend on the particular similarity-based prediction (ECO:0000255) used by UniProt curators for this protein. These boundary choices are within the typical uncertainty range of TM prediction and cannot be reliably resolved by hydrophobicity analysis of the sequence alone.",
    "reason": "While general reasoning eliminates C and identifies the C-terminal region as TM-containing, the fine distinctions among A, B, and D (number of TMs and exact helix boundaries differing by 5 residues) depend on the specific computational prediction recorded in the database entry, not on general biological principles applicable to the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The difference between B and D is a 5-residue boundary shift on one TM (1758..1784 vs 1763..1783). TM helix boundaries are inherently fuzzy, and both ranges fall within the plausible hydrophobic core of the same helix. Without knowing which prediction algorithm or similarity template was used, a careful hydrophobicity analysis might yield either boundary. However, D matches the UniProt annotation exactly, making it the intended answer."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally verified membrane-spanning regions.",
    "The UniProt entry was first publicly released in February 2025; the author's source snapshot date is unknown. The sequence version (2) and content match the benchmark input.",
    "The protein is from Tetrahymena thermophila, a ciliate with unusual genetic code features, but the sequence itself matches the canonical entry.",
    "The N-terminal ~1500 residues consist of multiple cysteine-rich EGF-like domains, making the protein predominantly extracellular/secreted with a C-terminal TM domain architecture."
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

**Accession:** `Q22HI5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 82. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.342521+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1619},"start":{"modifier":"EXACT","value":1599}},"type":"Transmembrane"}
```

Source SHA-256: `dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.342521+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1682},"start":{"modifier":"EXACT","value":1662}},"type":"Transmembrane"}
```

Source SHA-256: `dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.342521+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1724},"start":{"modifier":"EXACT","value":1704}},"type":"Transmembrane"}
```

Source SHA-256: `dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.342521+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1783},"start":{"modifier":"EXACT","value":1763}},"type":"Transmembrane"}
```

Source SHA-256: `dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.342521+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1816},"start":{"modifier":"EXACT","value":1796}},"type":"Transmembrane"}
```

Source SHA-256: `dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)  
**Locator:** `lines 88-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 2.  
**Retrieved:** 2026-11-01T06:28:29.712799+00:00.  

```text
FT   TRANSMEM        1599..1619
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)  
**Locator:** `lines 91-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 2.  
**Retrieved:** 2026-11-01T06:28:29.712799+00:00.  

```text
FT   TRANSMEM        1662..1682
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)  
**Locator:** `lines 94-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 2.  
**Retrieved:** 2026-11-01T06:28:29.712799+00:00.  

```text
FT   TRANSMEM        1704..1724
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)  
**Locator:** `lines 97-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 2.  
**Retrieved:** 2026-11-01T06:28:29.712799+00:00.  

```text
FT   TRANSMEM        1763..1783
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)  
**Locator:** `lines 100-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 2.  
**Retrieved:** 2026-11-01T06:28:29.712799+00:00.  

```text
FT   TRANSMEM        1796..1816
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
