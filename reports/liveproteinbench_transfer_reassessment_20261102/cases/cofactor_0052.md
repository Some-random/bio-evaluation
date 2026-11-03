# cofactor_0052: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0052.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **B** — Zn(2+)

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
MAGESTQVDLSVKAIGWGAKDASGILHPIKFSRRTPGERDVKIRVLYCGVCNFDMEMVRNKWGFTRYPYVFGHETAGEVVEVGSKVQKFKVGDKVAVGCMVGSCGKCYNCENGMENYCPEPNMADGSVYREQGERSYGGCSNVMVVDEKFVLRWPENLPQDTGVPLLCAGVVVYSPMKYMGLDKPGKHIGVFGLGGLGSVAVKFIKAFGGKATVISTSRRKEKEAIEEHGADAFVVNSDTEQLQALAGTMDGVVDTTPGGRTPMSLMLNLLKFDGSLILVGAPETLFELPVQPLILGRRKIIGSSTGGLKEYQEMLDFAAKHNILCDTEVIGIDYLSTAMERIKNLDVKYRFAIDIGNTLKYEE

[Multiple Choices]
A. [2Fe-2S] cluster
B. Zn(2+)
C. Co(2+)
D. Mn(2+)
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

> The sequence matches the UniProt entry for geissoschizine synthase, whose zinc cofactor annotation specifies two Zn(2+) ions per subunit. The annotation is transferred by similarity from UniProtKB:P06525, so it supports the key by inference rather than demonstrating zinc binding experimentally for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a dehydrogenase-family protein and contains cysteines, but those clues alone do not establish which listed metal is required.


**Missing item-specific fact**

> The protein's identity and family-specific cofactor assignment, or direct evidence of its metal requirement, are not supplied in the question.


**Reason**

> Choosing zinc depends on recognizing the protein or obtaining its cofactor annotation; the reviewer-only sequence match and database annotation were not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports zinc as the intended answer; the other choices are not supported by the supplied sequence alone.


### Important caveats

- The zinc annotation is based on similarity to another protein, not independently verified experimental evidence for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a dehydrogenase-family protein and contains cysteines, but those clues alone do not establish which listed metal is required.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and family-specific cofactor assignment, or direct evidence of its metal requirement, are not supplied in the question.",
    "reason": "Choosing zinc depends on recognizing the protein or obtaining its cofactor annotation; the reviewer-only sequence match and database annotation were not available to the evaluated model."
  },
  "case_id": "cofactor_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for geissoschizine synthase, whose zinc cofactor annotation specifies two Zn(2+) ions per subunit. The annotation is transferred by similarity from UniProtKB:P06525, so it supports the key by inference rather than demonstrating zinc binding experimentally for this exact protein."
  },
  "important_caveats": [
    "The zinc annotation is based on similarity to another protein, not independently verified experimental evidence for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports zinc as the intended answer; the other choices are not supported by the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for geissoschizine synthase, whose zinc cofactor annotation specifies two Zn(2+) ions per subunit. The annotation is transferred by similarity from UniProtKB:P06525, so it supports the key by inference rather than demonstrating zinc binding experimentally for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a dehydrogenase-family protein and contains cysteines, but those clues alone do not establish which listed metal is required.",
    "missing_item_specific_fact": "The protein's identity and family-specific cofactor assignment, or direct evidence of its metal requirement, are not supplied in the question.",
    "reason": "Choosing zinc depends on recognizing the protein or obtaining its cofactor annotation; the reviewer-only sequence match and database annotation were not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports zinc as the intended answer; the other choices are not supported by the supplied sequence alone."
  },
  "important_caveats": [
    "The zinc annotation is based on similarity to another protein, not independently verified experimental evidence for this exact sequence."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7LUR3 annotates Zn(2+) as the cofactor, stating 'Binds 2 Zn(2+) ions per subunit' (C5, H4). The sequence matches the benchmark exactly. However, the evidence code is ECO:0000250 (similarity), transferred from horse liver alcohol dehydrogenase (P06525), not a direct experimental determination on this specific geissoschizine synthase. The protein's alternative name 'Alcohol dehydrogenase GS' and its ADH-superfamily fold features (Rossmann motif GLGSVAVK, GAPET nucleotide-binding motif, cysteine-rich regions) are consistent with the canonical Zn(2+) cofactor of the ADH superfamily. The annotation is a computational inference by similarity, but the ADH-superfamily Zn dependence is well-established biochemistry.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark features of the alcohol dehydrogenase/reductase (ADH/R) superfamily: a canonical Rossmann-fold NAD(P)-binding motif (GLGSVAVK), a secondary nucleotide-binding motif (GAPET), a ~364-residue length typical of ADH monomers, and multiple cysteine-rich stretches (e.g., CGVCNFDMEM, GCMVGSCGKCYNC) consistent with zinc-coordination sites. The ADH superfamily is one of the best-characterized enzyme families in biochemistry, and Zn(2+) is its defining catalytic cofactor (typically two Zn ions per subunit, one catalytic and one structural). A biochemist recognizing the ADH fold could reasonably infer Zn(2+) over &#91;2Fe-2S&#93; (which requires a distinct Cys cluster pattern in ferredoxin-type proteins), Co(2+) (characteristic of corrinoid-dependent mutases and some diol dehydratases), or Mn(2+) (typical of superoxide dismutases and certain glycosyltransferases). The cysteine density and spacing in the sequence are more consistent with Zn tetrahedral coordination than with Fe-S cluster assembly motifs.


**Missing item-specific fact**

> The protein is actually EC 1.3.1.36 (geissoschizine synthase), a terpene indole alkaloid biosynthesis enzyme, not a classical alcohol dehydrogenase. The Zn annotation is transferred by similarity from horse liver ADH (P06525) rather than experimentally confirmed for this specific enzyme. Direct experimental cofactor determination for geissoschizine synthase would strengthen the answer, but the ADH-fold reasoning provides a defensible general-knowledge pathway.


**Reason**

> The ADH-superfamily sequence signatures (Rossmann motif, catalytic Cys/His patterns, overall fold architecture) are recognizable from the raw sequence and map to well-established general knowledge about Zn dependence in this superfamily. This constitutes a concrete biological argument rather than pure memorization of a database entry. The reasoning is indirect (fold-based family assignment → family-typical cofactor) but is standard practice in enzymology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four distractors (Fe-S cluster, Co, Mn) are mechanistically and structurally inconsistent with the ADH-like fold features present in the sequence. No other option is defensible given the recognizable Rossmann fold, ADH-typical cysteine spacing, and absence of motifs characteristic of Fe-S proteins, corrinoid enzymes, or Mn-dependent oxidoreductases.


### Important caveats

- The Zn(2+) annotation carries evidence code ECO:0000250 (similarity transfer from P06525, horse liver ADH), not direct experimental evidence for geissoschizine synthase itself. The actual catalytic mechanism of EC 1.3.1.36 may differ from classical ADH chemistry.
- The protein's primary name is 'Geissoschizine synthase' (EC 1.3.1.36); 'Alcohol dehydrogenase GS' is an alternative name reflecting fold similarity, not necessarily classical ADH function.
- The UniProt entry was first released in 2025-06-18 (Swiss-Prot 2026_01); the benchmark's construction date is unknown, so the annotation may not have existed when the question was authored.
- The reviewer identified the accession via dataset image-path metadata, not from the model input; the model saw only the raw sequence and four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark features of the alcohol dehydrogenase/reductase (ADH/R) superfamily: a canonical Rossmann-fold NAD(P)-binding motif (GLGSVAVK), a secondary nucleotide-binding motif (GAPET), a ~364-residue length typical of ADH monomers, and multiple cysteine-rich stretches (e.g., CGVCNFDMEM, GCMVGSCGKCYNC) consistent with zinc-coordination sites. The ADH superfamily is one of the best-characterized enzyme families in biochemistry, and Zn(2+) is its defining catalytic cofactor (typically two Zn ions per subunit, one catalytic and one structural). A biochemist recognizing the ADH fold could reasonably infer Zn(2+) over [2Fe-2S] (which requires a distinct Cys cluster pattern in ferredoxin-type proteins), Co(2+) (characteristic of corrinoid-dependent mutases and some diol dehydratases), or Mn(2+) (typical of superoxide dismutases and certain glycosyltransferases). The cysteine density and spacing in the sequence are more consistent with Zn tetrahedral coordination than with Fe-S cluster assembly motifs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The protein is actually EC 1.3.1.36 (geissoschizine synthase), a terpene indole alkaloid biosynthesis enzyme, not a classical alcohol dehydrogenase. The Zn annotation is transferred by similarity from horse liver ADH (P06525) rather than experimentally confirmed for this specific enzyme. Direct experimental cofactor determination for geissoschizine synthase would strengthen the answer, but the ADH-fold reasoning provides a defensible general-knowledge pathway.",
    "reason": "The ADH-superfamily sequence signatures (Rossmann motif, catalytic Cys/His patterns, overall fold architecture) are recognizable from the raw sequence and map to well-established general knowledge about Zn dependence in this superfamily. This constitutes a concrete biological argument rather than pure memorization of a database entry. The reasoning is indirect (fold-based family assignment → family-typical cofactor) but is standard practice in enzymology."
  },
  "case_id": "cofactor_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7LUR3 annotates Zn(2+) as the cofactor, stating 'Binds 2 Zn(2+) ions per subunit' (C5, H4). The sequence matches the benchmark exactly. However, the evidence code is ECO:0000250 (similarity), transferred from horse liver alcohol dehydrogenase (P06525), not a direct experimental determination on this specific geissoschizine synthase. The protein's alternative name 'Alcohol dehydrogenase GS' and its ADH-superfamily fold features (Rossmann motif GLGSVAVK, GAPET nucleotide-binding motif, cysteine-rich regions) are consistent with the canonical Zn(2+) cofactor of the ADH superfamily. The annotation is a computational inference by similarity, but the ADH-superfamily Zn dependence is well-established biochemistry."
  },
  "important_caveats": [
    "The Zn(2+) annotation carries evidence code ECO:0000250 (similarity transfer from P06525, horse liver ADH), not direct experimental evidence for geissoschizine synthase itself. The actual catalytic mechanism of EC 1.3.1.36 may differ from classical ADH chemistry.",
    "The protein's primary name is 'Geissoschizine synthase' (EC 1.3.1.36); 'Alcohol dehydrogenase GS' is an alternative name reflecting fold similarity, not necessarily classical ADH function.",
    "The UniProt entry was first released in 2025-06-18 (Swiss-Prot 2026_01); the benchmark's construction date is unknown, so the annotation may not have existed when the question was authored.",
    "The reviewer identified the accession via dataset image-path metadata, not from the model input; the model saw only the raw sequence and four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four distractors (Fe-S cluster, Co, Mn) are mechanistically and structurally inconsistent with the ADH-like fold features present in the sequence. No other option is defensible given the recognizable Rossmann fold, ADH-typical cysteine spacing, and absence of motifs characteristic of Fe-S proteins, corrinoid enzymes, or Mn-dependent oxidoreductases."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7LUR3 annotates Zn(2+) as the cofactor, stating 'Binds 2 Zn(2+) ions per subunit' (C5, H4). The sequence matches the benchmark exactly. However, the evidence code is ECO:0000250 (similarity), transferred from horse liver alcohol dehydrogenase (P06525), not a direct experimental determination on this specific geissoschizine synthase. The protein's alternative name 'Alcohol dehydrogenase GS' and its ADH-superfamily fold features (Rossmann motif GLGSVAVK, GAPET nucleotide-binding motif, cysteine-rich regions) are consistent with the canonical Zn(2+) cofactor of the ADH superfamily. The annotation is a computational inference by similarity, but the ADH-superfamily Zn dependence is well-established biochemistry.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark features of the alcohol dehydrogenase/reductase (ADH/R) superfamily: a canonical Rossmann-fold NAD(P)-binding motif (GLGSVAVK), a secondary nucleotide-binding motif (GAPET), a ~364-residue length typical of ADH monomers, and multiple cysteine-rich stretches (e.g., CGVCNFDMEM, GCMVGSCGKCYNC) consistent with zinc-coordination sites. The ADH superfamily is one of the best-characterized enzyme families in biochemistry, and Zn(2+) is its defining catalytic cofactor (typically two Zn ions per subunit, one catalytic and one structural). A biochemist recognizing the ADH fold could reasonably infer Zn(2+) over [2Fe-2S] (which requires a distinct Cys cluster pattern in ferredoxin-type proteins), Co(2+) (characteristic of corrinoid-dependent mutases and some diol dehydratases), or Mn(2+) (typical of superoxide dismutases and certain glycosyltransferases). The cysteine density and spacing in the sequence are more consistent with Zn tetrahedral coordination than with Fe-S cluster assembly motifs.",
    "missing_item_specific_fact": "The protein is actually EC 1.3.1.36 (geissoschizine synthase), a terpene indole alkaloid biosynthesis enzyme, not a classical alcohol dehydrogenase. The Zn annotation is transferred by similarity from horse liver ADH (P06525) rather than experimentally confirmed for this specific enzyme. Direct experimental cofactor determination for geissoschizine synthase would strengthen the answer, but the ADH-fold reasoning provides a defensible general-knowledge pathway.",
    "reason": "The ADH-superfamily sequence signatures (Rossmann motif, catalytic Cys/His patterns, overall fold architecture) are recognizable from the raw sequence and map to well-established general knowledge about Zn dependence in this superfamily. This constitutes a concrete biological argument rather than pure memorization of a database entry. The reasoning is indirect (fold-based family assignment → family-typical cofactor) but is standard practice in enzymology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four distractors (Fe-S cluster, Co, Mn) are mechanistically and structurally inconsistent with the ADH-like fold features present in the sequence. No other option is defensible given the recognizable Rossmann fold, ADH-typical cysteine spacing, and absence of motifs characteristic of Fe-S proteins, corrinoid enzymes, or Mn-dependent oxidoreductases."
  },
  "important_caveats": [
    "The Zn(2+) annotation carries evidence code ECO:0000250 (similarity transfer from P06525, horse liver ADH), not direct experimental evidence for geissoschizine synthase itself. The actual catalytic mechanism of EC 1.3.1.36 may differ from classical ADH chemistry.",
    "The protein's primary name is 'Geissoschizine synthase' (EC 1.3.1.36); 'Alcohol dehydrogenase GS' is an alternative name reflecting fold similarity, not necessarily classical ADH function.",
    "The UniProt entry was first released in 2025-06-18 (Swiss-Prot 2026_01); the benchmark's construction date is unknown, so the annotation may not have existed when the question was authored.",
    "The reviewer identified the accession via dataset image-path metadata, not from the model input; the model saw only the raw sequence and four choices."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched UniProt entry annotates Zn(2+) and says the subunit binds two Zn(2+) ions. This supports the key, though the annotation is transferred by similarity rather than direct evidence shown here for this exact protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has features consistent with a zinc-dependent alcohol dehydrogenase-family enzyme, including cysteine-rich regions characteristic of metal-binding sites in this family. Transferable family knowledge makes Zn(2+) a meaningful choice over an iron-sulfur cluster, Co(2+), or Mn(2+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and options provide a credible family-level inference for Zn without needing the exact protein's database record. This is a probabilistic inference, not direct proof of the metal bound in this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence's family-level metal-binding features favor Zn(2+) among the offered choices.


### Important caveats

- The supplied source annotation is based on similarity to another UniProt entry; the excerpts do not show direct experimental verification of cofactor binding for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a zinc-dependent alcohol dehydrogenase-family enzyme, including cysteine-rich regions characteristic of metal-binding sites in this family. Transferable family knowledge makes Zn(2+) a meaningful choice over an iron-sulfur cluster, Co(2+), or Mn(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and options provide a credible family-level inference for Zn without needing the exact protein's database record. This is a probabilistic inference, not direct proof of the metal bound in this particular protein."
  },
  "case_id": "cofactor_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates Zn(2+) and says the subunit binds two Zn(2+) ions. This supports the key, though the annotation is transferred by similarity rather than direct evidence shown here for this exact protein."
  },
  "important_caveats": [
    "The supplied source annotation is based on similarity to another UniProt entry; the excerpts do not show direct experimental verification of cofactor binding for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence's family-level metal-binding features favor Zn(2+) among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates Zn(2+) and says the subunit binds two Zn(2+) ions. This supports the key, though the annotation is transferred by similarity rather than direct evidence shown here for this exact protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has features consistent with a zinc-dependent alcohol dehydrogenase-family enzyme, including cysteine-rich regions characteristic of metal-binding sites in this family. Transferable family knowledge makes Zn(2+) a meaningful choice over an iron-sulfur cluster, Co(2+), or Mn(2+).",
    "missing_item_specific_fact": "",
    "reason": "The sequence and options provide a credible family-level inference for Zn without needing the exact protein's database record. This is a probabilistic inference, not direct proof of the metal bound in this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence's family-level metal-binding features favor Zn(2+) among the offered choices."
  },
  "important_caveats": [
    "The supplied source annotation is based on similarity to another UniProt entry; the excerpts do not show direct experimental verification of cofactor binding for this exact sequence."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (A0A9E7LUR3, Geissoschizine synthase / Alcohol dehydrogenase GS, EC 1.3.1.36) annotates Zn(2+) as the cofactor, binding 2 Zn(2+) ions per subunit. The evidence code is ECO:0000250 (similarity to P06525, horse liver alcohol dehydrogenase), so the annotation is a family-level inference rather than direct experimental proof for this specific protein. However, the protein is explicitly named 'Alcohol dehydrogenase GS' and belongs to the medium-chain ADH family, for which Zn(2+) is the canonical catalytic cofactor. The expected answer B (Zn(2+)) is scientifically well-supported by the family assignment.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD(P)-binding motif ('IGWGAKDASGIL' with the GxGxxG pattern at GAKDASG, and a second 'GVFGLGGLGSVAVKFI' motif), identifying it as a medium-chain alcohol dehydrogenase/reductase (MDR). The MDR family is overwhelmingly associated with Zn(2+) as its catalytic cofactor. Additionally, the sequence contains multiple cysteine residues in positions consistent with zinc coordination in ADHs (e.g., 'LYCGVCNFDMEM' near the N-terminus and 'AVGCMVGSCGKCYNCENGMENYCPEPN' in the middle region), matching the Cys-His/Cys zinc-binding pattern seen in horse liver ADH and related enzymes. Against the distractors: &#91;2Fe-2S&#93; clusters require specific Cys-X2-Cys spacing in ferredoxin-like scaffolds, which the Rossmann-fold context excludes; Co(2+) is characteristic of B12-dependent enzymes or a few specialized dehydrogenases, not the MDR family; Mn(2+) occurs in some dehydrogenases but not the classical zinc-dependent ADH fold. The family-level inference from Rossmann fold + cysteine arrangement to Zn(2+) is a well-established, transferable pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the Rossmann fold and ADH-family cysteine arrangement from the sequence alone and apply the well-known family-level rule that medium-chain alcohol dehydrogenases require Zn(2+). This distinguishes B from A (no ferredoxin/Rieske motifs), C (no corrinoid or Co-specific motifs), and D (Mn is atypical for this fold). No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Rossmann-fold ADH signature and cysteine coordination pattern strongly favor Zn(2+). The other three choices lack supporting sequence features: no ferredoxin-type Cys spacing for &#91;2Fe-2S&#93;, no corrinoid-binding context for Co(2+), and no Mn-specific motif. The choices are sufficiently distinguishable by family-level inference.


### Important caveats

- The UniProt cofactor annotation is by similarity (ECO:0000250 to P06525), not by direct experimental determination on this specific protein. However, the family-level Zn(2+) assignment for MDRs is robust.
- The protein's primary EC assignment is 1.3.1.36 (Geissoschizine synthase), an atypical dehydrogenase/reductase in monoterpene indole alkaloid biosynthesis. Its cofactor requirement is inherited from the ADH fold architecture.
- The reviewer-only evidence (accession, organism, UniProt annotation) was not available to the evaluated model; the reasoning above relies solely on sequence features and general biochemistry knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif ('IGWGAKDASGIL' with the GxGxxG pattern at GAKDASG, and a second 'GVFGLGGLGSVAVKFI' motif), identifying it as a medium-chain alcohol dehydrogenase/reductase (MDR). The MDR family is overwhelmingly associated with Zn(2+) as its catalytic cofactor. Additionally, the sequence contains multiple cysteine residues in positions consistent with zinc coordination in ADHs (e.g., 'LYCGVCNFDMEM' near the N-terminus and 'AVGCMVGSCGKCYNCENGMENYCPEPN' in the middle region), matching the Cys-His/Cys zinc-binding pattern seen in horse liver ADH and related enzymes. Against the distractors: [2Fe-2S] clusters require specific Cys-X2-Cys spacing in ferredoxin-like scaffolds, which the Rossmann-fold context excludes; Co(2+) is characteristic of B12-dependent enzymes or a few specialized dehydrogenases, not the MDR family; Mn(2+) occurs in some dehydrogenases but not the classical zinc-dependent ADH fold. The family-level inference from Rossmann fold + cysteine arrangement to Zn(2+) is a well-established, transferable pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann fold and ADH-family cysteine arrangement from the sequence alone and apply the well-known family-level rule that medium-chain alcohol dehydrogenases require Zn(2+). This distinguishes B from A (no ferredoxin/Rieske motifs), C (no corrinoid or Co-specific motifs), and D (Mn is atypical for this fold). No target-specific database lookup is required."
  },
  "case_id": "cofactor_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A9E7LUR3, Geissoschizine synthase / Alcohol dehydrogenase GS, EC 1.3.1.36) annotates Zn(2+) as the cofactor, binding 2 Zn(2+) ions per subunit. The evidence code is ECO:0000250 (similarity to P06525, horse liver alcohol dehydrogenase), so the annotation is a family-level inference rather than direct experimental proof for this specific protein. However, the protein is explicitly named 'Alcohol dehydrogenase GS' and belongs to the medium-chain ADH family, for which Zn(2+) is the canonical catalytic cofactor. The expected answer B (Zn(2+)) is scientifically well-supported by the family assignment."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is by similarity (ECO:0000250 to P06525), not by direct experimental determination on this specific protein. However, the family-level Zn(2+) assignment for MDRs is robust.",
    "The protein's primary EC assignment is 1.3.1.36 (Geissoschizine synthase), an atypical dehydrogenase/reductase in monoterpene indole alkaloid biosynthesis. Its cofactor requirement is inherited from the ADH fold architecture.",
    "The reviewer-only evidence (accession, organism, UniProt annotation) was not available to the evaluated model; the reasoning above relies solely on sequence features and general biochemistry knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann-fold ADH signature and cysteine coordination pattern strongly favor Zn(2+). The other three choices lack supporting sequence features: no ferredoxin-type Cys spacing for [2Fe-2S], no corrinoid-binding context for Co(2+), and no Mn-specific motif. The choices are sufficiently distinguishable by family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A9E7LUR3, Geissoschizine synthase / Alcohol dehydrogenase GS, EC 1.3.1.36) annotates Zn(2+) as the cofactor, binding 2 Zn(2+) ions per subunit. The evidence code is ECO:0000250 (similarity to P06525, horse liver alcohol dehydrogenase), so the annotation is a family-level inference rather than direct experimental proof for this specific protein. However, the protein is explicitly named 'Alcohol dehydrogenase GS' and belongs to the medium-chain ADH family, for which Zn(2+) is the canonical catalytic cofactor. The expected answer B (Zn(2+)) is scientifically well-supported by the family assignment.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif ('IGWGAKDASGIL' with the GxGxxG pattern at GAKDASG, and a second 'GVFGLGGLGSVAVKFI' motif), identifying it as a medium-chain alcohol dehydrogenase/reductase (MDR). The MDR family is overwhelmingly associated with Zn(2+) as its catalytic cofactor. Additionally, the sequence contains multiple cysteine residues in positions consistent with zinc coordination in ADHs (e.g., 'LYCGVCNFDMEM' near the N-terminus and 'AVGCMVGSCGKCYNCENGMENYCPEPN' in the middle region), matching the Cys-His/Cys zinc-binding pattern seen in horse liver ADH and related enzymes. Against the distractors: [2Fe-2S] clusters require specific Cys-X2-Cys spacing in ferredoxin-like scaffolds, which the Rossmann-fold context excludes; Co(2+) is characteristic of B12-dependent enzymes or a few specialized dehydrogenases, not the MDR family; Mn(2+) occurs in some dehydrogenases but not the classical zinc-dependent ADH fold. The family-level inference from Rossmann fold + cysteine arrangement to Zn(2+) is a well-established, transferable pattern.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann fold and ADH-family cysteine arrangement from the sequence alone and apply the well-known family-level rule that medium-chain alcohol dehydrogenases require Zn(2+). This distinguishes B from A (no ferredoxin/Rieske motifs), C (no corrinoid or Co-specific motifs), and D (Mn is atypical for this fold). No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann-fold ADH signature and cysteine coordination pattern strongly favor Zn(2+). The other three choices lack supporting sequence features: no ferredoxin-type Cys spacing for [2Fe-2S], no corrinoid-binding context for Co(2+), and no Mn-specific motif. The choices are sufficiently distinguishable by family-level inference."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is by similarity (ECO:0000250 to P06525), not by direct experimental determination on this specific protein. However, the family-level Zn(2+) assignment for MDRs is robust.",
    "The protein's primary EC assignment is 1.3.1.36 (Geissoschizine synthase), an atypical dehydrogenase/reductase in monoterpene indole alkaloid biosynthesis. Its cofactor requirement is inherited from the ADH fold architecture.",
    "The reviewer-only evidence (accession, organism, UniProt annotation) was not available to the evaluated model; the reasoning above relies solely on sequence features and general biochemistry knowledge."
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
  "requested_accession": "A0A9E7LUR3",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "6b2d31d337a1bc9f1e5478cf9eeafb327d5b0429e737e3aae6290d6c0ee2da2e",
  "benchmark_sequence_length": 364,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "current_source_sequence_sha256": "6b2d31d337a1bc9f1e5478cf9eeafb327d5b0429e737e3aae6290d6c0ee2da2e",
  "current_source_sequence_length": 364,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 12,
  "selected_historical_version": {
    "accession": "A0A9E7LUR3",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GS_ALSSC",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "selected_historical_source_sequence_sha256": "6b2d31d337a1bc9f1e5478cf9eeafb327d5b0429e737e3aae6290d6c0ee2da2e",
  "selected_historical_source_sequence_length": 364,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A9E7LUR3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Alcohol dehydrogenase GS\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.3.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Geissoschizine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsGS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P06525\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P06525\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 2 Zn(2+) ions per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65381.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12",
  "source_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "retrieved_utc": "2026-11-02T04:26:15.563182+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   GS_ALSSC                Reviewed;         364 AA.\nAC   A0A9E7LUR3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:36349266};\nDE            Short=AsGS {ECO:0000303|PubMed:36349266};\nDE            EC=1.3.1.36 {ECO:0000269|PubMed:36349266};\nDE   AltName: Full=Alcohol dehydrogenase GS {ECO:0000305};\nGN   Name=GS {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12",
  "source_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "retrieved_utc": "2026-11-02T04:26:15.563182+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:36349266};\nDE            Short=AsGS {ECO:0000303|PubMed:36349266};\nDE            EC=1.3.1.36 {ECO:0000269|PubMed:36349266};\nDE   AltName: Full=Alcohol dehydrogenase GS {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12",
  "source_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "retrieved_utc": "2026-11-02T04:26:15.563182+00:00",
  "source_locator": "lines 17-23",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65381.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12",
  "source_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "retrieved_utc": "2026-11-02T04:26:15.563182+00:00",
  "source_locator": "lines 50-53",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:P06525};\nCC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000250|UniProtKB:P06525};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 52. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
