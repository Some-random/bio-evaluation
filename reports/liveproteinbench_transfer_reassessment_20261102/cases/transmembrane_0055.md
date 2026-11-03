# transmembrane_0055: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0055.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 278..290; 402..415

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MTRHLTLCFILLVMLIDKSEACFCDHYPWTHWSSCSKSCNSGTQSRQRQVVVNDYYWKNLCDKLCIKQETRECNLQTCPINCVLGDYGTWSDCDPCTEKQVKVKSVLRPSQFGGQPCTEPLVTFQPCVPSKLCKIEETNCKNKFLCDSGRCIPSKLECNGENDCGDNSDERNCGRTKPVCTRIYTPIPSVQLMGTGFHFLAGEPRGEVLDNSFTGGICKLVKTSRASNPYRVSANLENVNFEVQTIEDDLKTEFYKNLISFEKNKNEDSLSVDERTKFFPIPIFHFSEKNEHSHYSSAFNKVIKASHKKDSSFIRIHKLIKVLNFTMKATDLQLSDVFLKALVHLPLEYNSAVYSRIFDDFGTHYFTSGSLGGKYDLIYQFSRQELQNSGLTEEEAQNCVQYETKKLKFLYMEIHKEDTCTKNKLSEKYGGSFLQGSEKSISLVQGGRSQQAAALAWEKGTSGPEENVYSEWLESVKENPAVVDYKLAPITDLVRNIPCAVTKRNNLRRALQEYAAKFDPCQCAPCPNNGRPRLSGTECLCVCQSGTYGENCERRSPGYKSDAVDGNWGCWSSWSACNAAYRRSRTRECNNPAPQRGGQSCGGKDQQEEDCTVSIMENVGQPCINDDEEMKEVDLAEPEAESGCSQPPLPENAFTWNEKKLYSVGEEVEISCLTGFTAVGFQYLRCLPDRTWSQGDVECQRTSCLKPVVQDVLTISPFQRVYQIGESIELTCPRGFVVAGPSRYTCKEDSWTPPISNSLTCEQAILTKSKDLCPPGQKQSGSKCICMSPEEDCSAYSEDLCIFDGGSSQYFTSSACKFLAGKCLNNTQSHFVHSGSCQEGLQLEWGLERLKLAVNSTKRVSCGYNTCYDWENCSAHTSNCVCLLPPQCSKDENQLYCVKIGSSMREKTVNICTLGAVRCANIKVEILNPGRCPD

[Multiple Choices]
A. 281..291; 402..415
B. 278..290; 402..415
C. 278..290
D. 510..528
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates transmembrane beta-strands at 278..290 and 402..415, matching choice B. The annotation is transferred by similarity from UniProtKB:P13671, so it supports the key as a database annotation, not as independently verified experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The supplied sequence does not provide a reliable way to distinguish these precise beta-strand boundaries from the nearby alternative in choice A. The question's generic description of typically hydrophobic alpha-helices does not identify these annotated beta-strands.


**Missing item-specific fact**

> The sequence-specific transmembrane beta-strand annotations at 278..290 and 402..415, or equivalent protein-specific evidence.


**Reason**

> Choosing the exact intervals requires protein-specific annotation or evidence not supplied in the question. Recognizing the protein or retrieving its annotation would be lookup, not reasoning from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports B's annotated intervals; no other choice is established as an alternative transmembrane annotation. The lack of input-level grounds for choosing the exact intervals is captured by the lookup-dependence judgment.


### Important caveats

- The annotation is a similarity-based transfer, not direct experimental confirmation for this mouse sequence.
- The reviewer-only database evidence was not available to the evaluated model.
- The annotated regions are beta-stranded, whereas the prompt describes transmembrane domains in terms of typical hydrophobic alpha-helices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence does not provide a reliable way to distinguish these precise beta-strand boundaries from the nearby alternative in choice A. The question's generic description of typically hydrophobic alpha-helices does not identify these annotated beta-strands.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific transmembrane beta-strand annotations at 278..290 and 402..415, or equivalent protein-specific evidence.",
    "reason": "Choosing the exact intervals requires protein-specific annotation or evidence not supplied in the question. Recognizing the protein or retrieving its annotation would be lookup, not reasoning from the input."
  },
  "case_id": "transmembrane_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates transmembrane beta-strands at 278..290 and 402..415, matching choice B. The annotation is transferred by similarity from UniProtKB:P13671, so it supports the key as a database annotation, not as independently verified experimental evidence."
  },
  "important_caveats": [
    "The annotation is a similarity-based transfer, not direct experimental confirmation for this mouse sequence.",
    "The reviewer-only database evidence was not available to the evaluated model.",
    "The annotated regions are beta-stranded, whereas the prompt describes transmembrane domains in terms of typical hydrophobic alpha-helices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B's annotated intervals; no other choice is established as an alternative transmembrane annotation. The lack of input-level grounds for choosing the exact intervals is captured by the lookup-dependence judgment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates transmembrane beta-strands at 278..290 and 402..415, matching choice B. The annotation is transferred by similarity from UniProtKB:P13671, so it supports the key as a database annotation, not as independently verified experimental evidence.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The supplied sequence does not provide a reliable way to distinguish these precise beta-strand boundaries from the nearby alternative in choice A. The question's generic description of typically hydrophobic alpha-helices does not identify these annotated beta-strands.",
    "missing_item_specific_fact": "The sequence-specific transmembrane beta-strand annotations at 278..290 and 402..415, or equivalent protein-specific evidence.",
    "reason": "Choosing the exact intervals requires protein-specific annotation or evidence not supplied in the question. Recognizing the protein or retrieving its annotation would be lookup, not reasoning from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B's annotated intervals; no other choice is established as an alternative transmembrane annotation. The lack of input-level grounds for choosing the exact intervals is captured by the lookup-dependence judgment."
  },
  "important_caveats": [
    "The annotation is a similarity-based transfer, not direct experimental confirmation for this mouse sequence.",
    "The reviewer-only database evidence was not available to the evaluated model.",
    "The annotated regions are beta-stranded, whereas the prompt describes transmembrane domains in terms of typical hydrophobic alpha-helices."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E9Q6D8 (Mouse Complement component C6, sequence matched by SHA256) annotates two transmembrane features at exactly 278..290 and 402..415, both described as 'Beta stranded' with evidence code ECO:0000250 (inferred by similarity from P13671, human C6). Both the current entry (C5, C6) and the historical entry version 99 (H2, H3) confirm these coordinates. The expected answer B matches these annotations exactly. However, the annotation is computational inference by similarity, not direct experimental evidence, and describes beta-stranded (not alpha-helical) membrane-spanning regions.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The prompt instructs the solver to look for 'hydrophobic alpha-helices' typical of transmembrane domains, but the actual annotated regions are 'Beta stranded' and only 13–14 residues long (well below the 18–25 residue threshold for alpha-helical TM). Standard hydrophobicity-window analysis would not cleanly distinguish positions 278–290 from 281–291 (option A), nor confirm the existence of a second TM at 402–415 rather than at 510–528 (option D). The protein is a secreted complement component (C6), making the presence of transmembrane segments itself counterintuitive without prior knowledge of this specific annotation.


**Missing item-specific fact**

> The exact UniProt annotation coordinates (278..290 and 402..415), the fact that these are beta-stranded rather than alpha-helical membrane regions, and the knowledge that this secreted complement precursor carries two such annotated segments transferred by similarity from human C6 (P13671). Without this protein-specific annotation, general hydrophobicity reasoning cannot resolve the 3-residue boundary shift between A and B or confirm the dual-region topology.


**Reason**

> Selecting B over A requires knowing the exact start position (278 vs 281), which is a boundary-level annotation detail not derivable from general TM prediction heuristics. Selecting B over C requires knowing there are two TM segments at these specific locations. The 'beta stranded' character contradicts the prompt's alpha-helix framing, further undermining general reasoning. The answer depends on recalling or accessing the specific UniProt feature table for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Option A (281..291; 402..415) differs from B by only a 3-residue shift in the first region; without exact annotation knowledge, a hydrophobicity-based analysis could plausibly select either boundary. Option C (278..290 only) is defensible if a solver identifies only one TM segment. The prompt's description of TM domains as 'hydrophobic alpha-helices' conflicts with the actual 'Beta stranded' annotation, making the reasoning path ambiguous.


### Important caveats

- The transmembrane annotations carry evidence code ECO:0000250 (inferred by similarity from P13671), not direct experimental evidence.
- The annotated regions are 'Beta stranded,' contradicting the prompt's description of TM domains as 'hydrophobic alpha-helices.' This is unusual for a secreted complement protein.
- The identity origin note states the UniProt accession was inferred mechanically from dataset metadata and was absent from the evaluated model input.
- The historical entry (v99) and current entry (v101) both carry the same TM annotations with the same similarity-transfer evidence code; no experimental validation was found in the retrieved excerpts.
- The benchmark sequence SHA256 matches both current and historical source sequences (934 AA, sequence version 2).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The prompt instructs the solver to look for 'hydrophobic alpha-helices' typical of transmembrane domains, but the actual annotated regions are 'Beta stranded' and only 13–14 residues long (well below the 18–25 residue threshold for alpha-helical TM). Standard hydrophobicity-window analysis would not cleanly distinguish positions 278–290 from 281–291 (option A), nor confirm the existence of a second TM at 402–415 rather than at 510–528 (option D). The protein is a secreted complement component (C6), making the presence of transmembrane segments itself counterintuitive without prior knowledge of this specific annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact UniProt annotation coordinates (278..290 and 402..415), the fact that these are beta-stranded rather than alpha-helical membrane regions, and the knowledge that this secreted complement precursor carries two such annotated segments transferred by similarity from human C6 (P13671). Without this protein-specific annotation, general hydrophobicity reasoning cannot resolve the 3-residue boundary shift between A and B or confirm the dual-region topology.",
    "reason": "Selecting B over A requires knowing the exact start position (278 vs 281), which is a boundary-level annotation detail not derivable from general TM prediction heuristics. Selecting B over C requires knowing there are two TM segments at these specific locations. The 'beta stranded' character contradicts the prompt's alpha-helix framing, further undermining general reasoning. The answer depends on recalling or accessing the specific UniProt feature table for this protein."
  },
  "case_id": "transmembrane_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E9Q6D8 (Mouse Complement component C6, sequence matched by SHA256) annotates two transmembrane features at exactly 278..290 and 402..415, both described as 'Beta stranded' with evidence code ECO:0000250 (inferred by similarity from P13671, human C6). Both the current entry (C5, C6) and the historical entry version 99 (H2, H3) confirm these coordinates. The expected answer B matches these annotations exactly. However, the annotation is computational inference by similarity, not direct experimental evidence, and describes beta-stranded (not alpha-helical) membrane-spanning regions."
  },
  "important_caveats": [
    "The transmembrane annotations carry evidence code ECO:0000250 (inferred by similarity from P13671), not direct experimental evidence.",
    "The annotated regions are 'Beta stranded,' contradicting the prompt's description of TM domains as 'hydrophobic alpha-helices.' This is unusual for a secreted complement protein.",
    "The identity origin note states the UniProt accession was inferred mechanically from dataset metadata and was absent from the evaluated model input.",
    "The historical entry (v99) and current entry (v101) both carry the same TM annotations with the same similarity-transfer evidence code; no experimental validation was found in the retrieved excerpts.",
    "The benchmark sequence SHA256 matches both current and historical source sequences (934 AA, sequence version 2)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Option A (281..291; 402..415) differs from B by only a 3-residue shift in the first region; without exact annotation knowledge, a hydrophobicity-based analysis could plausibly select either boundary. Option C (278..290 only) is defensible if a solver identifies only one TM segment. The prompt's description of TM domains as 'hydrophobic alpha-helices' conflicts with the actual 'Beta stranded' annotation, making the reasoning path ambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E9Q6D8 (Mouse Complement component C6, sequence matched by SHA256) annotates two transmembrane features at exactly 278..290 and 402..415, both described as 'Beta stranded' with evidence code ECO:0000250 (inferred by similarity from P13671, human C6). Both the current entry (C5, C6) and the historical entry version 99 (H2, H3) confirm these coordinates. The expected answer B matches these annotations exactly. However, the annotation is computational inference by similarity, not direct experimental evidence, and describes beta-stranded (not alpha-helical) membrane-spanning regions.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The prompt instructs the solver to look for 'hydrophobic alpha-helices' typical of transmembrane domains, but the actual annotated regions are 'Beta stranded' and only 13–14 residues long (well below the 18–25 residue threshold for alpha-helical TM). Standard hydrophobicity-window analysis would not cleanly distinguish positions 278–290 from 281–291 (option A), nor confirm the existence of a second TM at 402–415 rather than at 510–528 (option D). The protein is a secreted complement component (C6), making the presence of transmembrane segments itself counterintuitive without prior knowledge of this specific annotation.",
    "missing_item_specific_fact": "The exact UniProt annotation coordinates (278..290 and 402..415), the fact that these are beta-stranded rather than alpha-helical membrane regions, and the knowledge that this secreted complement precursor carries two such annotated segments transferred by similarity from human C6 (P13671). Without this protein-specific annotation, general hydrophobicity reasoning cannot resolve the 3-residue boundary shift between A and B or confirm the dual-region topology.",
    "reason": "Selecting B over A requires knowing the exact start position (278 vs 281), which is a boundary-level annotation detail not derivable from general TM prediction heuristics. Selecting B over C requires knowing there are two TM segments at these specific locations. The 'beta stranded' character contradicts the prompt's alpha-helix framing, further undermining general reasoning. The answer depends on recalling or accessing the specific UniProt feature table for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Option A (281..291; 402..415) differs from B by only a 3-residue shift in the first region; without exact annotation knowledge, a hydrophobicity-based analysis could plausibly select either boundary. Option C (278..290 only) is defensible if a solver identifies only one TM segment. The prompt's description of TM domains as 'hydrophobic alpha-helices' conflicts with the actual 'Beta stranded' annotation, making the reasoning path ambiguous."
  },
  "important_caveats": [
    "The transmembrane annotations carry evidence code ECO:0000250 (inferred by similarity from P13671), not direct experimental evidence.",
    "The annotated regions are 'Beta stranded,' contradicting the prompt's description of TM domains as 'hydrophobic alpha-helices.' This is unusual for a secreted complement protein.",
    "The identity origin note states the UniProt accession was inferred mechanically from dataset metadata and was absent from the evaluated model input.",
    "The historical entry (v99) and current entry (v101) both carry the same TM annotations with the same similarity-transfer evidence code; no experimental validation was found in the retrieved excerpts.",
    "The benchmark sequence SHA256 matches both current and historical source sequences (934 AA, sequence version 2)."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates beta-stranded transmembrane regions at 278–290 and 402–415, matching B. The annotation is supported by transfer from another UniProt entry (ECO:0000250), not by direct experimental evidence shown here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a secreted, cysteine-rich complement-like protein. Transferable knowledge about MACPF-family pore formation can motivate two membrane-inserting beta-strand regions and favors the paired regions over a single unrelated segment. But that family-level reasoning does not reliably distinguish A from B, whose first intervals differ only slightly.


**Missing item-specific fact**

> The precise boundary convention or homolog-based annotation that places the first beta-strand region at 278–290 rather than 281–291.


**Reason**

> Family and mechanism knowledge provide a credible approximate prediction, but the offered choices include near-identical alternatives. Selecting B exactly requires the fine boundary information not established by those transferable features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A and B share the 402–415 region, and their first intervals substantially overlap. Since the prompt does not specify a boundary convention or tolerance, both can describe the same membrane-inserting beta-strand region approximately, although only B matches the cited annotation exactly.


### Important caveats

- The database evidence is sequence-matched, but the cited support is transferred by similarity; it should not be represented as direct experimental validation.
- Beta-stranded membrane-inserting regions in pore-forming proteins are not necessarily equivalent to conventional hydrophobic alpha-helical transmembrane segments.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a secreted, cysteine-rich complement-like protein. Transferable knowledge about MACPF-family pore formation can motivate two membrane-inserting beta-strand regions and favors the paired regions over a single unrelated segment. But that family-level reasoning does not reliably distinguish A from B, whose first intervals differ only slightly.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise boundary convention or homolog-based annotation that places the first beta-strand region at 278–290 rather than 281–291.",
    "reason": "Family and mechanism knowledge provide a credible approximate prediction, but the offered choices include near-identical alternatives. Selecting B exactly requires the fine boundary information not established by those transferable features."
  },
  "case_id": "transmembrane_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates beta-stranded transmembrane regions at 278–290 and 402–415, matching B. The annotation is supported by transfer from another UniProt entry (ECO:0000250), not by direct experimental evidence shown here."
  },
  "important_caveats": [
    "The database evidence is sequence-matched, but the cited support is transferred by similarity; it should not be represented as direct experimental validation.",
    "Beta-stranded membrane-inserting regions in pore-forming proteins are not necessarily equivalent to conventional hydrophobic alpha-helical transmembrane segments."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A and B share the 402–415 region, and their first intervals substantially overlap. Since the prompt does not specify a boundary convention or tolerance, both can describe the same membrane-inserting beta-strand region approximately, although only B matches the cited annotation exactly."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates beta-stranded transmembrane regions at 278–290 and 402–415, matching B. The annotation is supported by transfer from another UniProt entry (ECO:0000250), not by direct experimental evidence shown here.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a secreted, cysteine-rich complement-like protein. Transferable knowledge about MACPF-family pore formation can motivate two membrane-inserting beta-strand regions and favors the paired regions over a single unrelated segment. But that family-level reasoning does not reliably distinguish A from B, whose first intervals differ only slightly.",
    "missing_item_specific_fact": "The precise boundary convention or homolog-based annotation that places the first beta-strand region at 278–290 rather than 281–291.",
    "reason": "Family and mechanism knowledge provide a credible approximate prediction, but the offered choices include near-identical alternatives. Selecting B exactly requires the fine boundary information not established by those transferable features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A and B share the 402–415 region, and their first intervals substantially overlap. Since the prompt does not specify a boundary convention or tolerance, both can describe the same membrane-inserting beta-strand region approximately, although only B matches the cited annotation exactly."
  },
  "important_caveats": [
    "The database evidence is sequence-matched, but the cited support is transferred by similarity; it should not be represented as direct experimental validation.",
    "Beta-stranded membrane-inserting regions in pore-forming proteins are not necessarily equivalent to conventional hydrophobic alpha-helical transmembrane segments."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (Complement component C6, mouse, E9Q6D8) annotates exactly two transmembrane regions: 278..290 and 402..415, both labeled 'Beta stranded'. Evidence IDs C5, C6, H2, and H3 confirm these coordinates match the author's expected answer B. The evidence code is ECO:0000250 (inferred by similarity from UniProtKB:P13671, human C6), so the annotation is computational/transferred rather than experimentally determined, but it is the recorded annotation and matches the key exactly.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple CCP/SCR (complement control protein/short consensus repeat) domains and a C-terminal MAC perforin domain architecture, identifying it as a membrane-attack-complex (MAC) component. Well-established family knowledge (from C6, C7, C8α, C8β, C9 across species) dictates that MAC perforin-domain proteins carry exactly TWO beta-stranded transmembrane hairpins in the C-terminal domain. This eliminates option C (single TM region) and option D (single TM region at position 510..528, which is also 19 residues—longer than typical TM beta-strands of 13–15 residues). For the A-vs-B distinction: option A gives an 11-residue first TM segment (281..291), while B gives 13 residues (278..290). Beta-stranded TM hairpins in MAC proteins are consistently ~13–15 residues per strand (e.g., human C6 P13671, C7, C9 crystal structures). An 11-residue beta-strand is atypically short for spanning a lipid bilayer, making B the more consistent choice with family-level structural regularity. Additionally, a hydrophobicity scan of the C-terminal MAC perforin region should reveal two hydrophobic stretches whose boundaries align more naturally with 278..290 than 281..291.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level knowledge of MAC proteins (two beta-stranded TM hairpins in the perforin domain, typical strand length 13–15 residues) meaningfully eliminates C and D, and provides a probabilistic but credible basis for preferring B (13-residue strand) over A (11-residue strand). The 3-residue boundary shift is within typical prediction uncertainty, but the strand-length argument and hydrophobicity profile give a defensible generalization. No target-specific memorization is strictly required, though the fine boundary distinction is at the edge of what sequence-based reasoning can resolve.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The distinction between A (281..291) and B (278..290) is a 3-residue shift, which falls within the typical ±2–3 residue uncertainty of transmembrane boundary prediction, especially for beta-stranded TM regions annotated by similarity (ECO:0000250). A model could reasonably argue either boundary based on hydrophobicity profile. However, the strand-length regularity argument (13 vs 11 residues) modestly favors B, so both are not equally defensible, but the margin is narrow.


### Important caveats

- The UniProt TM annotation uses ECO:0000250 (inferred by similarity from human C6 P13671), not experimental evidence. The exact boundaries are therefore computational predictions transferred by homology, not independently validated for this mouse sequence.
- The 3-residue boundary difference between options A and B is within the typical uncertainty range of TM region predictors, making this the hardest aspect of the question.
- The protein is a precursor (signal peptide present); coordinates are canonical UniProt numbering.
- Beta-stranded TM regions are structurally distinct from the alpha-helical TM domains described in the system prompt; the prompt's description of 'hydrophobic alpha-helices' is slightly misleading for this particular protein family.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple CCP/SCR (complement control protein/short consensus repeat) domains and a C-terminal MAC perforin domain architecture, identifying it as a membrane-attack-complex (MAC) component. Well-established family knowledge (from C6, C7, C8α, C8β, C9 across species) dictates that MAC perforin-domain proteins carry exactly TWO beta-stranded transmembrane hairpins in the C-terminal domain. This eliminates option C (single TM region) and option D (single TM region at position 510..528, which is also 19 residues—longer than typical TM beta-strands of 13–15 residues). For the A-vs-B distinction: option A gives an 11-residue first TM segment (281..291), while B gives 13 residues (278..290). Beta-stranded TM hairpins in MAC proteins are consistently ~13–15 residues per strand (e.g., human C6 P13671, C7, C9 crystal structures). An 11-residue beta-strand is atypically short for spanning a lipid bilayer, making B the more consistent choice with family-level structural regularity. Additionally, a hydrophobicity scan of the C-terminal MAC perforin region should reveal two hydrophobic stretches whose boundaries align more naturally with 278..290 than 281..291.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of MAC proteins (two beta-stranded TM hairpins in the perforin domain, typical strand length 13–15 residues) meaningfully eliminates C and D, and provides a probabilistic but credible basis for preferring B (13-residue strand) over A (11-residue strand). The 3-residue boundary shift is within typical prediction uncertainty, but the strand-length argument and hydrophobicity profile give a defensible generalization. No target-specific memorization is strictly required, though the fine boundary distinction is at the edge of what sequence-based reasoning can resolve."
  },
  "case_id": "transmembrane_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Complement component C6, mouse, E9Q6D8) annotates exactly two transmembrane regions: 278..290 and 402..415, both labeled 'Beta stranded'. Evidence IDs C5, C6, H2, and H3 confirm these coordinates match the author's expected answer B. The evidence code is ECO:0000250 (inferred by similarity from UniProtKB:P13671, human C6), so the annotation is computational/transferred rather than experimentally determined, but it is the recorded annotation and matches the key exactly."
  },
  "important_caveats": [
    "The UniProt TM annotation uses ECO:0000250 (inferred by similarity from human C6 P13671), not experimental evidence. The exact boundaries are therefore computational predictions transferred by homology, not independently validated for this mouse sequence.",
    "The 3-residue boundary difference between options A and B is within the typical uncertainty range of TM region predictors, making this the hardest aspect of the question.",
    "The protein is a precursor (signal peptide present); coordinates are canonical UniProt numbering.",
    "Beta-stranded TM regions are structurally distinct from the alpha-helical TM domains described in the system prompt; the prompt's description of 'hydrophobic alpha-helices' is slightly misleading for this particular protein family."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The distinction between A (281..291) and B (278..290) is a 3-residue shift, which falls within the typical ±2–3 residue uncertainty of transmembrane boundary prediction, especially for beta-stranded TM regions annotated by similarity (ECO:0000250). A model could reasonably argue either boundary based on hydrophobicity profile. However, the strand-length regularity argument (13 vs 11 residues) modestly favors B, so both are not equally defensible, but the margin is narrow."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Complement component C6, mouse, E9Q6D8) annotates exactly two transmembrane regions: 278..290 and 402..415, both labeled 'Beta stranded'. Evidence IDs C5, C6, H2, and H3 confirm these coordinates match the author's expected answer B. The evidence code is ECO:0000250 (inferred by similarity from UniProtKB:P13671, human C6), so the annotation is computational/transferred rather than experimentally determined, but it is the recorded annotation and matches the key exactly.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple CCP/SCR (complement control protein/short consensus repeat) domains and a C-terminal MAC perforin domain architecture, identifying it as a membrane-attack-complex (MAC) component. Well-established family knowledge (from C6, C7, C8α, C8β, C9 across species) dictates that MAC perforin-domain proteins carry exactly TWO beta-stranded transmembrane hairpins in the C-terminal domain. This eliminates option C (single TM region) and option D (single TM region at position 510..528, which is also 19 residues—longer than typical TM beta-strands of 13–15 residues). For the A-vs-B distinction: option A gives an 11-residue first TM segment (281..291), while B gives 13 residues (278..290). Beta-stranded TM hairpins in MAC proteins are consistently ~13–15 residues per strand (e.g., human C6 P13671, C7, C9 crystal structures). An 11-residue beta-strand is atypically short for spanning a lipid bilayer, making B the more consistent choice with family-level structural regularity. Additionally, a hydrophobicity scan of the C-terminal MAC perforin region should reveal two hydrophobic stretches whose boundaries align more naturally with 278..290 than 281..291.",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of MAC proteins (two beta-stranded TM hairpins in the perforin domain, typical strand length 13–15 residues) meaningfully eliminates C and D, and provides a probabilistic but credible basis for preferring B (13-residue strand) over A (11-residue strand). The 3-residue boundary shift is within typical prediction uncertainty, but the strand-length argument and hydrophobicity profile give a defensible generalization. No target-specific memorization is strictly required, though the fine boundary distinction is at the edge of what sequence-based reasoning can resolve."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The distinction between A (281..291) and B (278..290) is a 3-residue shift, which falls within the typical ±2–3 residue uncertainty of transmembrane boundary prediction, especially for beta-stranded TM regions annotated by similarity (ECO:0000250). A model could reasonably argue either boundary based on hydrophobicity profile. However, the strand-length regularity argument (13 vs 11 residues) modestly favors B, so both are not equally defensible, but the margin is narrow."
  },
  "important_caveats": [
    "The UniProt TM annotation uses ECO:0000250 (inferred by similarity from human C6 P13671), not experimental evidence. The exact boundaries are therefore computational predictions transferred by homology, not independently validated for this mouse sequence.",
    "The 3-residue boundary difference between options A and B is within the typical uncertainty range of TM region predictors, making this the hardest aspect of the question.",
    "The protein is a precursor (signal peptide present); coordinates are canonical UniProt numbering.",
    "Beta-stranded TM regions are structurally distinct from the alpha-helical TM domains described in the system prompt; the prompt's description of 'hydrophobic alpha-helices' is slightly misleading for this particular protein family."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "E9Q6D8",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "8886931fba31717048f68746485603eba835719d0ab9ad67408064a7be8af267",
  "benchmark_sequence_length": 934,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 101,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-02-28",
    "sequenceVersion": 2
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "4ab2ff8c634de0b89fdc8ef96721bd2d2e212b3c99707b0a066f82eb2a76e11f",
  "current_source_sequence_sha256": "8886931fba31717048f68746485603eba835719d0ab9ad67408064a7be8af267",
  "current_source_sequence_length": 934,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 99,
  "selected_historical_version": {
    "accession": "E9Q6D8",
    "database": "Swiss-Prot",
    "entryVersion": 99,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CO6_MOUSE",
    "sequenceVersion": 2
  },
  "selected_historical_record_sha256": "91cb7e42a331a9224499c3b00d14730203dbf91c7234b33358bef2146f9087f9",
  "selected_historical_source_sequence_sha256": "8886931fba31717048f68746485603eba835719d0ab9ad67408064a7be8af267",
  "selected_historical_source_sequence_length": 934,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 99,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q6D8.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q6D8.json",
  "source_sha256": "4ab2ff8c634de0b89fdc8ef96721bd2d2e212b3c99707b0a066f82eb2a76e11f",
  "retrieved_utc": "2026-11-02T04:28:07.887054+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"E9Q6D8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q6D8.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q6D8.json",
  "source_sha256": "4ab2ff8c634de0b89fdc8ef96721bd2d2e212b3c99707b0a066f82eb2a76e11f",
  "retrieved_utc": "2026-11-02T04:28:07.887054+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":101,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-02-28\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q6D8.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q6D8.json",
  "source_sha256": "4ab2ff8c634de0b89fdc8ef96721bd2d2e212b3c99707b0a066f82eb2a76e11f",
  "retrieved_utc": "2026-11-02T04:28:07.887054+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Mouse\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Mus\",\"Mus\"],\"scientificName\":\"Mus musculus\",\"taxonId\":10090}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q6D8.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q6D8.json",
  "source_sha256": "4ab2ff8c634de0b89fdc8ef96721bd2d2e212b3c99707b0a066f82eb2a76e11f",
  "retrieved_utc": "2026-11-02T04:28:07.887054+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Complement component C6\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q6D8.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q6D8.json",
  "source_sha256": "4ab2ff8c634de0b89fdc8ef96721bd2d2e212b3c99707b0a066f82eb2a76e11f",
  "retrieved_utc": "2026-11-02T04:28:07.887054+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Beta stranded\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P13671\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":290},\"start\":{\"modifier\":\"EXACT\",\"value\":278}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q6D8.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q6D8.json",
  "source_sha256": "4ab2ff8c634de0b89fdc8ef96721bd2d2e212b3c99707b0a066f82eb2a76e11f",
  "retrieved_utc": "2026-11-02T04:28:07.887054+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Beta stranded\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P13671\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":415},\"start\":{\"modifier\":\"EXACT\",\"value\":402}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q6D8?format=txt&versions=99)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E9Q6D8?format=txt&versions=99",
  "source_sha256": "91cb7e42a331a9224499c3b00d14730203dbf91c7234b33358bef2146f9087f9",
  "retrieved_utc": "2026-11-02T04:28:10.587277+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   CO6_MOUSE               Reviewed;         934 AA.\nAC   E9Q6D8; Q8BRY4; Q91X70; Q9QXT7;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-FEB-2018, sequence version 2.\nDT   28-JAN-2026, entry version 99.\nDE   RecName: Full=Complement component C6 {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=C6 {ECO:0000312|MGI:MGI:88233};\nOS   Mus musculus (Mouse).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Mus; Mus.\nOX   NCBI_TaxID=10090;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q6D8?format=txt&versions=99)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E9Q6D8?format=txt&versions=99",
  "source_sha256": "91cb7e42a331a9224499c3b00d14730203dbf91c7234b33358bef2146f9087f9",
  "retrieved_utc": "2026-11-02T04:28:10.587277+00:00",
  "source_locator": "lines 238-240",
  "excerpt": "FT   TRANSMEM        278..290\nFT                   /note=\"Beta stranded\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P13671\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q6D8?format=txt&versions=99)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E9Q6D8?format=txt&versions=99",
  "source_sha256": "91cb7e42a331a9224499c3b00d14730203dbf91c7234b33358bef2146f9087f9",
  "retrieved_utc": "2026-11-02T04:28:10.587277+00:00",
  "source_locator": "lines 241-243",
  "excerpt": "FT   TRANSMEM        402..415\nFT                   /note=\"Beta stranded\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P13671\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
