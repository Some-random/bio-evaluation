# cofactor_0028: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0028.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **C** — Zn(2+)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MVKPTKSNIGVYTNPAHDLWVAEAEPSLEQVQTGEKLAPGEVTVAVKSTGICGSDVHFWHAGCIGPMIVEDDHILGHESAGVVVAVHENVKSLKVGDRVAIEPNIICGECEPCLTGRYNGCDSVLFRSTPPVPGLLRRYVNHPAMWCHKIGDMSYENGSLLEPLSVALAGVQRAEVRLGDPILVCGAGPIGLVTLACVKAAGAEPIIITDIDEGRLAFAKEFCPSVRTHKVDFKHTPEDFAKAITELGGGVEPAIALECTGVESSIAGAIQTVKFGGKVFVIGVGKNEIKIPFMRLSTREVDLQFQYRYANTWPRAIRLLQGGVINLEKLVTHRFKIEDALEAFKTAADPKTGAIKVQIQSFEEGESR

[Multiple Choices]
A. Mg(2+)
B. Ca(2+)
C. Zn(2+)
D. Mo-bis(molybdopterin guanine dinucleotide)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches a UniProt entry annotated as L-arabinitol 4-dehydrogenase, with Zn(2+) listed as its cofactor. The annotation is transferred by similarity from UniProtKB:Q7SI09 (ECO:0000250), so it supports the key but is not direct experimental evidence for this particular protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently diagnostic basis to identify the required cofactor. Cysteine and histidine residues are not, by themselves, conclusive evidence for zinc binding.


**Missing item-specific fact**

> The protein's identity/function as L-arabinitol 4-dehydrogenase and the cofactor annotation transferred from a related protein are absent from the question.


**Reason**

> Distinguishing Zn(2+) requires protein-specific functional or annotation knowledge; recognizing the sequence or consulting its database record is lookup, not reasoning from information supplied.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports Zn(2+); it does not support another listed option. The evidence is inferential rather than direct experimental confirmation for this exact protein.


### Important caveats

- The sequence match is exact, but the cofactor annotation has ECO:0000250 evidence and is transferred from UniProtKB:Q7SI09.
- The evidence supports the expected answer as an annotation; it does not establish that this specific protein's zinc requirement was experimentally measured.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently diagnostic basis to identify the required cofactor. Cysteine and histidine residues are not, by themselves, conclusive evidence for zinc binding.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity/function as L-arabinitol 4-dehydrogenase and the cofactor annotation transferred from a related protein are absent from the question.",
    "reason": "Distinguishing Zn(2+) requires protein-specific functional or annotation knowledge; recognizing the sequence or consulting its database record is lookup, not reasoning from information supplied."
  },
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated as L-arabinitol 4-dehydrogenase, with Zn(2+) listed as its cofactor. The annotation is transferred by similarity from UniProtKB:Q7SI09 (ECO:0000250), so it supports the key but is not direct experimental evidence for this particular protein."
  },
  "important_caveats": [
    "The sequence match is exact, but the cofactor annotation has ECO:0000250 evidence and is transferred from UniProtKB:Q7SI09.",
    "The evidence supports the expected answer as an annotation; it does not establish that this specific protein's zinc requirement was experimentally measured."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports Zn(2+); it does not support another listed option. The evidence is inferential rather than direct experimental confirmation for this exact protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated as L-arabinitol 4-dehydrogenase, with Zn(2+) listed as its cofactor. The annotation is transferred by similarity from UniProtKB:Q7SI09 (ECO:0000250), so it supports the key but is not direct experimental evidence for this particular protein.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently diagnostic basis to identify the required cofactor. Cysteine and histidine residues are not, by themselves, conclusive evidence for zinc binding.",
    "missing_item_specific_fact": "The protein's identity/function as L-arabinitol 4-dehydrogenase and the cofactor annotation transferred from a related protein are absent from the question.",
    "reason": "Distinguishing Zn(2+) requires protein-specific functional or annotation knowledge; recognizing the sequence or consulting its database record is lookup, not reasoning from information supplied."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports Zn(2+); it does not support another listed option. The evidence is inferential rather than direct experimental confirmation for this exact protein."
  },
  "important_caveats": [
    "The sequence match is exact, but the cofactor annotation has ECO:0000250 evidence and is transferred from UniProtKB:Q7SI09.",
    "The evidence supports the expected answer as an annotation; it does not establish that this specific protein's zinc requirement was experimentally measured."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A385XI11 (L-arabinitol 4-dehydrogenase, EC 1.1.1.12) explicitly annotates Zn(2+) as the cofactor (C5, H4). The evidence code ECO:0000250 indicates the annotation is transferred by similarity from Q7SI09 rather than directly experimentally determined for this protein, but EC 1.1.1.12 (L-arabinitol 4-dehydrogenase) belongs to the short-chain dehydrogenase/reductase (SDR) family, which is well-established in biochemistry as Zn(2+)-dependent. The sequence match is confirmed (SHA-256 identical across current and historical snapshots).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Rossmann-fold NAD(P)-binding motif (GAGPIGLVTLACVKAAG, residues ~175-192), identifying the protein as a NAD(P)-dependent dehydrogenase. The Cys-rich region (ICGECEPCLTG) and His residues (VHENV, VNHPAMWCHK) near the active site are characteristic of the SDR catalytic zinc-binding site. SDR dehydrogenases (the family to which L-arabinitol 4-dehydrogenase belongs) are textbook Zn(2+)-dependent enzymes. Mg(2+) is typical of kinases and polymerases, Ca(2+) of structural/signaling proteins, and Mo-bis(MGD) of specialized molybdoenzymes (xanthine oxidase, nitrate reductase)—none of which match an SDR dehydrogenase. The combination of Rossmann fold + Cys/His zinc-ligand pattern + dehydrogenase activity provides a concrete sequence-to-cofactor argument favoring Zn(2+).


**Missing item-specific fact**

> None critical. The Zn(2+) assignment for SDR dehydrogenases is general biochemical knowledge. One could argue that distinguishing SDR from other NAD-dependent dehydrogenase families (e.g., some aldehyde dehydrogenases that use Cys catalysis without Zn) requires family-level knowledge, but the Cys/His coordination pattern visible in the sequence is a strong SDR signature.


**Reason**

> A model with knowledge of enzyme superfamilies can identify the Rossmann fold, recognize the SDR zinc-binding Cys/His pattern, and apply the well-established rule that SDR dehydrogenases require Zn(2+). The distractors (Mg2+, Ca2+, Mo-bis(MGD)) are inconsistent with SDR dehydrogenase biochemistry. This is not mere memorization of a database entry but application of general enzymology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Zn(2+) is the only cofactor consistent with SDR dehydrogenase biochemistry. Mg(2+) is not used by SDR enzymes; Ca(2+) is irrelevant to dehydrogenase catalysis; Mo-bis(MGD) is restricted to molybdoenzymes with entirely different folds and chemistry. No other option is defensible.


### Important caveats

- The Zn(2+) annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity from Q7SI09), not direct experimental determination on this specific protein. However, the SDR Zn(2+) requirement is a robust general biochemical principle.
- The protein name 'L-arabinitol 4-dehydrogenase' and EC number 1.1.1.12 were derived from the annotation evidence; the evaluated model sees only the raw sequence and must infer function from sequence features.
- The Mo-bis(MGD) distractor is an extreme outlier (molybdoenzymes have entirely different folds), making the effective discrimination primarily between Zn(2+) and Mg(2+), which the SDR family knowledge resolves.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold NAD(P)-binding motif (GAGPIGLVTLACVKAAG, residues ~175-192), identifying the protein as a NAD(P)-dependent dehydrogenase. The Cys-rich region (ICGECEPCLTG) and His residues (VHENV, VNHPAMWCHK) near the active site are characteristic of the SDR catalytic zinc-binding site. SDR dehydrogenases (the family to which L-arabinitol 4-dehydrogenase belongs) are textbook Zn(2+)-dependent enzymes. Mg(2+) is typical of kinases and polymerases, Ca(2+) of structural/signaling proteins, and Mo-bis(MGD) of specialized molybdoenzymes (xanthine oxidase, nitrate reductase)—none of which match an SDR dehydrogenase. The combination of Rossmann fold + Cys/His zinc-ligand pattern + dehydrogenase activity provides a concrete sequence-to-cofactor argument favoring Zn(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The Zn(2+) assignment for SDR dehydrogenases is general biochemical knowledge. One could argue that distinguishing SDR from other NAD-dependent dehydrogenase families (e.g., some aldehyde dehydrogenases that use Cys catalysis without Zn) requires family-level knowledge, but the Cys/His coordination pattern visible in the sequence is a strong SDR signature.",
    "reason": "A model with knowledge of enzyme superfamilies can identify the Rossmann fold, recognize the SDR zinc-binding Cys/His pattern, and apply the well-established rule that SDR dehydrogenases require Zn(2+). The distractors (Mg2+, Ca2+, Mo-bis(MGD)) are inconsistent with SDR dehydrogenase biochemistry. This is not mere memorization of a database entry but application of general enzymology."
  },
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A385XI11 (L-arabinitol 4-dehydrogenase, EC 1.1.1.12) explicitly annotates Zn(2+) as the cofactor (C5, H4). The evidence code ECO:0000250 indicates the annotation is transferred by similarity from Q7SI09 rather than directly experimentally determined for this protein, but EC 1.1.1.12 (L-arabinitol 4-dehydrogenase) belongs to the short-chain dehydrogenase/reductase (SDR) family, which is well-established in biochemistry as Zn(2+)-dependent. The sequence match is confirmed (SHA-256 identical across current and historical snapshots)."
  },
  "important_caveats": [
    "The Zn(2+) annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity from Q7SI09), not direct experimental determination on this specific protein. However, the SDR Zn(2+) requirement is a robust general biochemical principle.",
    "The protein name 'L-arabinitol 4-dehydrogenase' and EC number 1.1.1.12 were derived from the annotation evidence; the evaluated model sees only the raw sequence and must infer function from sequence features.",
    "The Mo-bis(MGD) distractor is an extreme outlier (molybdoenzymes have entirely different folds), making the effective discrimination primarily between Zn(2+) and Mg(2+), which the SDR family knowledge resolves."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Zn(2+) is the only cofactor consistent with SDR dehydrogenase biochemistry. Mg(2+) is not used by SDR enzymes; Ca(2+) is irrelevant to dehydrogenase catalysis; Mo-bis(MGD) is restricted to molybdoenzymes with entirely different folds and chemistry. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A385XI11 (L-arabinitol 4-dehydrogenase, EC 1.1.1.12) explicitly annotates Zn(2+) as the cofactor (C5, H4). The evidence code ECO:0000250 indicates the annotation is transferred by similarity from Q7SI09 rather than directly experimentally determined for this protein, but EC 1.1.1.12 (L-arabinitol 4-dehydrogenase) belongs to the short-chain dehydrogenase/reductase (SDR) family, which is well-established in biochemistry as Zn(2+)-dependent. The sequence match is confirmed (SHA-256 identical across current and historical snapshots).",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold NAD(P)-binding motif (GAGPIGLVTLACVKAAG, residues ~175-192), identifying the protein as a NAD(P)-dependent dehydrogenase. The Cys-rich region (ICGECEPCLTG) and His residues (VHENV, VNHPAMWCHK) near the active site are characteristic of the SDR catalytic zinc-binding site. SDR dehydrogenases (the family to which L-arabinitol 4-dehydrogenase belongs) are textbook Zn(2+)-dependent enzymes. Mg(2+) is typical of kinases and polymerases, Ca(2+) of structural/signaling proteins, and Mo-bis(MGD) of specialized molybdoenzymes (xanthine oxidase, nitrate reductase)—none of which match an SDR dehydrogenase. The combination of Rossmann fold + Cys/His zinc-ligand pattern + dehydrogenase activity provides a concrete sequence-to-cofactor argument favoring Zn(2+).",
    "missing_item_specific_fact": "None critical. The Zn(2+) assignment for SDR dehydrogenases is general biochemical knowledge. One could argue that distinguishing SDR from other NAD-dependent dehydrogenase families (e.g., some aldehyde dehydrogenases that use Cys catalysis without Zn) requires family-level knowledge, but the Cys/His coordination pattern visible in the sequence is a strong SDR signature.",
    "reason": "A model with knowledge of enzyme superfamilies can identify the Rossmann fold, recognize the SDR zinc-binding Cys/His pattern, and apply the well-established rule that SDR dehydrogenases require Zn(2+). The distractors (Mg2+, Ca2+, Mo-bis(MGD)) are inconsistent with SDR dehydrogenase biochemistry. This is not mere memorization of a database entry but application of general enzymology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Zn(2+) is the only cofactor consistent with SDR dehydrogenase biochemistry. Mg(2+) is not used by SDR enzymes; Ca(2+) is irrelevant to dehydrogenase catalysis; Mo-bis(MGD) is restricted to molybdoenzymes with entirely different folds and chemistry. No other option is defensible."
  },
  "important_caveats": [
    "The Zn(2+) annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity from Q7SI09), not direct experimental determination on this specific protein. However, the SDR Zn(2+) requirement is a robust general biochemical principle.",
    "The protein name 'L-arabinitol 4-dehydrogenase' and EC number 1.1.1.12 were derived from the annotation evidence; the evaluated model sees only the raw sequence and must infer function from sequence features.",
    "The Mo-bis(MGD) distractor is an extreme outlier (molybdoenzymes have entirely different folds), making the effective discrimination primarily between Zn(2+) and Mg(2+), which the SDR family knowledge resolves."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a UniProt entry annotated with Zn(2+) as its cofactor. The annotation is transferred by similarity from Q7SI09 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a roughly 370-residue NAD-dependent polyol/alcohol dehydrogenase, with conserved histidine/cysteine-rich regions characteristic of zinc-dependent members of this enzyme family. That family-level pattern makes Zn a meaningful choice over Mg, Ca, or a molybdopterin cofactor, even without identifying the exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable dehydrogenase-family knowledge and the sequence’s metal-binding features provide a credible basis for choosing Zn among these alternatives. The exact protein’s annotation is not necessary for that inference, though it offers corroboration.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered choices distinguish zinc-dependent dehydrogenases from the other listed cofactor types; no alternative is comparably supported.


### Important caveats

- The cited cofactor annotation is computationally transferred from a related UniProt entry, not established here as a direct experimental measurement of this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a roughly 370-residue NAD-dependent polyol/alcohol dehydrogenase, with conserved histidine/cysteine-rich regions characteristic of zinc-dependent members of this enzyme family. That family-level pattern makes Zn a meaningful choice over Mg, Ca, or a molybdopterin cofactor, even without identifying the exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable dehydrogenase-family knowledge and the sequence’s metal-binding features provide a credible basis for choosing Zn among these alternatives. The exact protein’s annotation is not necessary for that inference, though it offers corroboration."
  },
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with Zn(2+) as its cofactor. The annotation is transferred by similarity from Q7SI09 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The cited cofactor annotation is computationally transferred from a related UniProt entry, not established here as a direct experimental measurement of this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices distinguish zinc-dependent dehydrogenases from the other listed cofactor types; no alternative is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with Zn(2+) as its cofactor. The annotation is transferred by similarity from Q7SI09 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a roughly 370-residue NAD-dependent polyol/alcohol dehydrogenase, with conserved histidine/cysteine-rich regions characteristic of zinc-dependent members of this enzyme family. That family-level pattern makes Zn a meaningful choice over Mg, Ca, or a molybdopterin cofactor, even without identifying the exact protein.",
    "missing_item_specific_fact": "",
    "reason": "Transferable dehydrogenase-family knowledge and the sequence’s metal-binding features provide a credible basis for choosing Zn among these alternatives. The exact protein’s annotation is not necessary for that inference, though it offers corroboration."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices distinguish zinc-dependent dehydrogenases from the other listed cofactor types; no alternative is comparably supported."
  },
  "important_caveats": [
    "The cited cofactor annotation is computationally transferred from a related UniProt entry, not established here as a direct experimental measurement of this exact protein."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates Zn(2+) as the cofactor for this L-arabinitol 4-dehydrogenase (EC 1.1.1.12), with evidence code ECO:0000250 (inferred by similarity from Q7SI09). While the annotation is computational rather than directly experimental, it is well-supported by the protein's membership in the medium-chain dehydrogenase/reductase (MDR) family, which universally uses a catalytic Zn(2+) ion coordinated by conserved Cys and His residues. The sequence contains the hallmark zinc-binding motifs 'ICGSDVHFWHAGC' (Cys-X-X-X-X-X-His-X-X-X-Cys) and 'CGAGPIGLVTLAC', consistent with the canonical MDR zinc site. The Zn(2+) assignment is therefore consistent with both the annotation and the visible sequence features.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two highly diagnostic motifs for the medium-chain dehydrogenase/reductase (MDR) family: (1) 'ICGSDVHFWHAGC' with the Cys-X-X-X-X-X-His-X-X-X-Cys pattern, which is the canonical zinc-coordination motif in MDR enzymes (analogous to Cys46/His67/Cys174 in horse liver alcohol dehydrogenase), and (2) 'CGAGPIGLVTLAC', the second Cys-rich zinc-ligand region. Additionally, the Rossmann-fold-like segment 'GGGVEPAIALECTGVESSIAGAIQTVKFGGKVFVIGVGKNEIKIPFMRLSTREV' indicates NAD(P)-dependent dehydrogenase activity. A knowledgeable model can recognize these Cys-His-Cys motifs as the zinc-binding site of the MDR family, which universally requires a catalytic Zn(2+). This directly eliminates Mg(2+) (found in kinases, polymerases, ATPases), Ca(2+) (found in EF-hand proteins, some proteases), and Mo-bis(molybdopterin guanine dinucleotide) (found in molybdoenzymes with entirely different folds and Moco-binding motifs absent here). The inference relies on well-established family-level sequence signatures shared across hundreds of MDR dehydrogenases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The zinc-binding Cys-His-Cys motif in the MDR family is a widely taught, transferable sequence feature. Recognizing 'ICGSDVHFWHAGC' and 'CGAGPIGLVTLAC' as zinc-coordination motifs in a dehydrogenase context is a legitimate family-level inference from other proteins, not a lookup of this specific entry's annotation. The four options are well-separated by family context: none of the distractors (Mg2+, Ca2+, Mo-bis-MGD) are associated with MDR dehydrogenases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Cys-His-Cys zinc-binding motif and the Rossmann-fold NAD-binding region uniquely identify this as an MDR-family dehydrogenase, which uses Zn(2+) as its catalytic cofactor. The other three options correspond to entirely different enzyme classes and structural folds not suggested by any feature in the sequence.


### Important caveats

- The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from Q7SI09), meaning it is a computational transfer rather than a direct experimental measurement on this exact protein.
- The organism identity (Aureobasidium melanogenum) and specific protein name (L-arabinitol 4-dehydrogenase) were not provided to the evaluated model; the reasoning must rely on sequence motifs alone.
- The Mo-bis(molybdopterin guanine dinucleotide) distractor is particularly easy to eliminate because molybdoenzymes have a completely different fold and Moco-binding motifs absent from this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two highly diagnostic motifs for the medium-chain dehydrogenase/reductase (MDR) family: (1) 'ICGSDVHFWHAGC' with the Cys-X-X-X-X-X-His-X-X-X-Cys pattern, which is the canonical zinc-coordination motif in MDR enzymes (analogous to Cys46/His67/Cys174 in horse liver alcohol dehydrogenase), and (2) 'CGAGPIGLVTLAC', the second Cys-rich zinc-ligand region. Additionally, the Rossmann-fold-like segment 'GGGVEPAIALECTGVESSIAGAIQTVKFGGKVFVIGVGKNEIKIPFMRLSTREV' indicates NAD(P)-dependent dehydrogenase activity. A knowledgeable model can recognize these Cys-His-Cys motifs as the zinc-binding site of the MDR family, which universally requires a catalytic Zn(2+). This directly eliminates Mg(2+) (found in kinases, polymerases, ATPases), Ca(2+) (found in EF-hand proteins, some proteases), and Mo-bis(molybdopterin guanine dinucleotide) (found in molybdoenzymes with entirely different folds and Moco-binding motifs absent here). The inference relies on well-established family-level sequence signatures shared across hundreds of MDR dehydrogenases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The zinc-binding Cys-His-Cys motif in the MDR family is a widely taught, transferable sequence feature. Recognizing 'ICGSDVHFWHAGC' and 'CGAGPIGLVTLAC' as zinc-coordination motifs in a dehydrogenase context is a legitimate family-level inference from other proteins, not a lookup of this specific entry's annotation. The four options are well-separated by family context: none of the distractors (Mg2+, Ca2+, Mo-bis-MGD) are associated with MDR dehydrogenases."
  },
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates Zn(2+) as the cofactor for this L-arabinitol 4-dehydrogenase (EC 1.1.1.12), with evidence code ECO:0000250 (inferred by similarity from Q7SI09). While the annotation is computational rather than directly experimental, it is well-supported by the protein's membership in the medium-chain dehydrogenase/reductase (MDR) family, which universally uses a catalytic Zn(2+) ion coordinated by conserved Cys and His residues. The sequence contains the hallmark zinc-binding motifs 'ICGSDVHFWHAGC' (Cys-X-X-X-X-X-His-X-X-X-Cys) and 'CGAGPIGLVTLAC', consistent with the canonical MDR zinc site. The Zn(2+) assignment is therefore consistent with both the annotation and the visible sequence features."
  },
  "important_caveats": [
    "The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from Q7SI09), meaning it is a computational transfer rather than a direct experimental measurement on this exact protein.",
    "The organism identity (Aureobasidium melanogenum) and specific protein name (L-arabinitol 4-dehydrogenase) were not provided to the evaluated model; the reasoning must rely on sequence motifs alone.",
    "The Mo-bis(molybdopterin guanine dinucleotide) distractor is particularly easy to eliminate because molybdoenzymes have a completely different fold and Moco-binding motifs absent from this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Cys-His-Cys zinc-binding motif and the Rossmann-fold NAD-binding region uniquely identify this as an MDR-family dehydrogenase, which uses Zn(2+) as its catalytic cofactor. The other three options correspond to entirely different enzyme classes and structural folds not suggested by any feature in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates Zn(2+) as the cofactor for this L-arabinitol 4-dehydrogenase (EC 1.1.1.12), with evidence code ECO:0000250 (inferred by similarity from Q7SI09). While the annotation is computational rather than directly experimental, it is well-supported by the protein's membership in the medium-chain dehydrogenase/reductase (MDR) family, which universally uses a catalytic Zn(2+) ion coordinated by conserved Cys and His residues. The sequence contains the hallmark zinc-binding motifs 'ICGSDVHFWHAGC' (Cys-X-X-X-X-X-His-X-X-X-Cys) and 'CGAGPIGLVTLAC', consistent with the canonical MDR zinc site. The Zn(2+) assignment is therefore consistent with both the annotation and the visible sequence features.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two highly diagnostic motifs for the medium-chain dehydrogenase/reductase (MDR) family: (1) 'ICGSDVHFWHAGC' with the Cys-X-X-X-X-X-His-X-X-X-Cys pattern, which is the canonical zinc-coordination motif in MDR enzymes (analogous to Cys46/His67/Cys174 in horse liver alcohol dehydrogenase), and (2) 'CGAGPIGLVTLAC', the second Cys-rich zinc-ligand region. Additionally, the Rossmann-fold-like segment 'GGGVEPAIALECTGVESSIAGAIQTVKFGGKVFVIGVGKNEIKIPFMRLSTREV' indicates NAD(P)-dependent dehydrogenase activity. A knowledgeable model can recognize these Cys-His-Cys motifs as the zinc-binding site of the MDR family, which universally requires a catalytic Zn(2+). This directly eliminates Mg(2+) (found in kinases, polymerases, ATPases), Ca(2+) (found in EF-hand proteins, some proteases), and Mo-bis(molybdopterin guanine dinucleotide) (found in molybdoenzymes with entirely different folds and Moco-binding motifs absent here). The inference relies on well-established family-level sequence signatures shared across hundreds of MDR dehydrogenases.",
    "missing_item_specific_fact": "",
    "reason": "The zinc-binding Cys-His-Cys motif in the MDR family is a widely taught, transferable sequence feature. Recognizing 'ICGSDVHFWHAGC' and 'CGAGPIGLVTLAC' as zinc-coordination motifs in a dehydrogenase context is a legitimate family-level inference from other proteins, not a lookup of this specific entry's annotation. The four options are well-separated by family context: none of the distractors (Mg2+, Ca2+, Mo-bis-MGD) are associated with MDR dehydrogenases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Cys-His-Cys zinc-binding motif and the Rossmann-fold NAD-binding region uniquely identify this as an MDR-family dehydrogenase, which uses Zn(2+) as its catalytic cofactor. The other three options correspond to entirely different enzyme classes and structural folds not suggested by any feature in the sequence."
  },
  "important_caveats": [
    "The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from Q7SI09), meaning it is a computational transfer rather than a direct experimental measurement on this exact protein.",
    "The organism identity (Aureobasidium melanogenum) and specific protein name (L-arabinitol 4-dehydrogenase) were not provided to the evaluated model; the reasoning must rely on sequence motifs alone.",
    "The Mo-bis(molybdopterin guanine dinucleotide) distractor is particularly easy to eliminate because molybdoenzymes have a completely different fold and Moco-binding motifs absent from this sequence."
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
  "requested_accession": "A0A385XI11",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "b6243c25f76bd5341c3276e5e72351d95b636da19da05dae2fa407490c6e3c1c",
  "benchmark_sequence_length": 368,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-12-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "current_source_sequence_sha256": "b6243c25f76bd5341c3276e5e72351d95b636da19da05dae2fa407490c6e3c1c",
  "current_source_sequence_length": 368,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 21,
  "selected_historical_version": {
    "accession": "A0A385XI11",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "LAD_AURME",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "selected_historical_source_sequence_sha256": "b6243c25f76bd5341c3276e5e72351d95b636da19da05dae2fa407490c6e3c1c",
  "selected_historical_source_sequence_length": 368,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 21,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A385XI11\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-12-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7SI09\",\"source\":\"UniProtKB\"}],\"value\":\"1.1.1.12\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"L-arabinitol 4-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"ArDH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7SI09\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   LAD_AURME               Reviewed;         368 AA.\nAC   A0A385XI11;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-DEC-2018, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=L-arabinitol 4-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=ArDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.12 {ECO:0000250|UniProtKB:Q7SI09};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 21,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=L-arabinitol 4-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=ArDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.12 {ECO:0000250|UniProtKB:Q7SI09};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 21,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "source_locator": "lines 31-37",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 21,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "source_locator": "lines 55-57",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:Q7SI09};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 21,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
