# GO_cellular_component_0091: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0091.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **B** — plasma membrane

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
MAVMKFTWRSIIPRCSKGIEEAEAEAEAETKKQDSKQGSFSRLAMIDFSYPSSMFTEDLSTSLAGSNLYVFTLEELKVITQCFSSANFLGEGGFGPVHKGFIDDNLRPGLEAQPVAVKLLDLEGLQGHREWLTEVVFLAQLSHPHLVKLIGYCCEDENRLLVYEYMPRGSLENQLFAKYSVPLPWSTRMKIALGAAKGLAYLHEAEKPVIYRDFKASNILLDSDYSAKLSDFGLAKDGPEGDKTHVSTRVMGTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRSLDKSRSPREQNLAEWARPMLNESRRLARIMDPKLEGQYSETGARKAAALAYQCLSHRAKQRPKMSDVVNILEPLLDYGETSVASFVYTVPTHQKGGSPPKDDTDTKECEAKTELKKENGHHRNRHHHRRSHKSRDGHRHQNKSSSQSSVHSENDTSKQNLENGSNEECNID

[Multiple Choices]
A. inner membrane pellicle complex
B. plasma membrane
C. RQC complex
D. mitochondrial outer membrane
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the cotton protein record, which annotates it to the cell membrane and maps it to the plasma membrane. The location evidence is transferred or computationally inferred, not direct experimental evidence in the excerpts.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence appears kinase-like and lacks an obvious transmembrane segment, making a soluble cytoplasmic kinase that associates peripherally with a membrane plausible. The specialized pellicle and RQC choices are poor fits, but these features do not establish plasma-membrane localization over other possibilities.


**Missing item-specific fact**

> A protein-specific localization annotation or experimental localization result is needed to identify the plasma membrane as the protein’s primary compartment.


**Reason**

> General sequence features and the choices can make B plausible, but they do not determine this protein’s specific localization; the supporting plasma-membrane annotation is external to the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports B, and none of the alternatives is comparably supported for this protein.


### Important caveats

- The matched record’s cell-membrane annotation is transferred by similarity, and its GO plasma-membrane annotation is inferred; the excerpts do not establish direct experimental localization.
- The source snapshot available to the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence appears kinase-like and lacks an obvious transmembrane segment, making a soluble cytoplasmic kinase that associates peripherally with a membrane plausible. The specialized pellicle and RQC choices are poor fits, but these features do not establish plasma-membrane localization over other possibilities.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific localization annotation or experimental localization result is needed to identify the plasma membrane as the protein’s primary compartment.",
    "reason": "General sequence features and the choices can make B plausible, but they do not determine this protein’s specific localization; the supporting plasma-membrane annotation is external to the input."
  },
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cotton protein record, which annotates it to the cell membrane and maps it to the plasma membrane. The location evidence is transferred or computationally inferred, not direct experimental evidence in the excerpts."
  },
  "important_caveats": [
    "The matched record’s cell-membrane annotation is transferred by similarity, and its GO plasma-membrane annotation is inferred; the excerpts do not establish direct experimental localization.",
    "The source snapshot available to the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B, and none of the alternatives is comparably supported for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cotton protein record, which annotates it to the cell membrane and maps it to the plasma membrane. The location evidence is transferred or computationally inferred, not direct experimental evidence in the excerpts.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence appears kinase-like and lacks an obvious transmembrane segment, making a soluble cytoplasmic kinase that associates peripherally with a membrane plausible. The specialized pellicle and RQC choices are poor fits, but these features do not establish plasma-membrane localization over other possibilities.",
    "missing_item_specific_fact": "A protein-specific localization annotation or experimental localization result is needed to identify the plasma membrane as the protein’s primary compartment.",
    "reason": "General sequence features and the choices can make B plausible, but they do not determine this protein’s specific localization; the supporting plasma-membrane annotation is external to the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B, and none of the alternatives is comparably supported for this protein."
  },
  "important_caveats": [
    "The matched record’s cell-membrane annotation is transferred by similarity, and its GO plasma-membrane annotation is inferred; the excerpts do not establish direct experimental localization.",
    "The source snapshot available to the author is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB annotates this protein (A0A5J5NT52, GbEIR5D from Gossypium barbadense) with subcellular location 'Cell membrane' (C5, H3) and GO:0005886 'plasma membrane' (C6, H4). 'Cell membrane' is an EXACT synonym of GO:0005886 'plasma membrane' (GO2). The annotation is consistent with the protein being a receptor-like cytoplasmic kinase (RLCK), a family known to associate with the plasma membrane. However, the evidence code is ECO:0000250/ISS (similarity-based inference from Q9ZUF4), meaning this is computational transfer, not direct experimental localization.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Among the four options, three can be eliminated through general biological reasoning from the sequence: (A) inner membrane pellicle complex is specific to apicomplexan parasites (GO3 definition confirms 'apicomplexan parasite cell'), incompatible with a plant protein; (C) RQC complex is a defined ribosome-associated quality-control complex with specific protein components (Cdc48, Rkr1, etc., per GO4), not a kinase; (D) mitochondrial outer membrane requires an N-terminal mitochondrial targeting signal, which is absent from this sequence's N-terminus (no amphipathic cationic helix typical of mitochondrial precursors). The sequence clearly contains a serine/threonine kinase domain (recognizable GxGxxG, DFG, and activation loop motifs), making it a signaling kinase. With A, C, and D eliminated, B (plasma membrane) is the only remaining viable compartment for a membrane-associated kinase.


**Missing item-specific fact**

> The positive assignment to plasma membrane specifically (rather than cytoplasm, which is not offered as an option) relies on knowing that RLCKs associate with the plasma membrane via lipid modifications or protein interactions. However, since 'cytoplasm' is not among the choices, elimination reasoning suffices.


**Reason**

> The four options are sufficiently heterogeneous that general biological knowledge (apicomplexan specificity of pellicle, defined composition of RQC, requirement of MTS for mitochondrial outer membrane) eliminates three choices, leaving plasma membrane as the only viable answer. The kinase domain is identifiable from sequence motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are clearly incompatible with a plant serine/threonine kinase lacking mitochondrial targeting signals. Only B remains defensible among the four choices.


### Important caveats

- The plasma membrane annotation is ISS (Inferred from Sequence Similarity, ECO:0000250), transferred from an Arabidopsis RLCK homolog, not experimentally determined for this specific protein.
- The protein name includes 'cytoplasmic' (receptor-like cytoplasmic kinase), which could mislead toward a cytoplasmic localization, but RLCKs are membrane-associated despite lacking transmembrane domains.
- The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt entry A0A5J5NT52.
- The author's source snapshot is unknown; the entry was first public 2025-06-18, so the annotation may not have existed at the time the benchmark was constructed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Among the four options, three can be eliminated through general biological reasoning from the sequence: (A) inner membrane pellicle complex is specific to apicomplexan parasites (GO3 definition confirms 'apicomplexan parasite cell'), incompatible with a plant protein; (C) RQC complex is a defined ribosome-associated quality-control complex with specific protein components (Cdc48, Rkr1, etc., per GO4), not a kinase; (D) mitochondrial outer membrane requires an N-terminal mitochondrial targeting signal, which is absent from this sequence's N-terminus (no amphipathic cationic helix typical of mitochondrial precursors). The sequence clearly contains a serine/threonine kinase domain (recognizable GxGxxG, DFG, and activation loop motifs), making it a signaling kinase. With A, C, and D eliminated, B (plasma membrane) is the only remaining viable compartment for a membrane-associated kinase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The positive assignment to plasma membrane specifically (rather than cytoplasm, which is not offered as an option) relies on knowing that RLCKs associate with the plasma membrane via lipid modifications or protein interactions. However, since 'cytoplasm' is not among the choices, elimination reasoning suffices.",
    "reason": "The four options are sufficiently heterogeneous that general biological knowledge (apicomplexan specificity of pellicle, defined composition of RQC, requirement of MTS for mitochondrial outer membrane) eliminates three choices, leaving plasma membrane as the only viable answer. The kinase domain is identifiable from sequence motifs."
  },
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProtKB annotates this protein (A0A5J5NT52, GbEIR5D from Gossypium barbadense) with subcellular location 'Cell membrane' (C5, H3) and GO:0005886 'plasma membrane' (C6, H4). 'Cell membrane' is an EXACT synonym of GO:0005886 'plasma membrane' (GO2). The annotation is consistent with the protein being a receptor-like cytoplasmic kinase (RLCK), a family known to associate with the plasma membrane. However, the evidence code is ECO:0000250/ISS (similarity-based inference from Q9ZUF4), meaning this is computational transfer, not direct experimental localization."
  },
  "important_caveats": [
    "The plasma membrane annotation is ISS (Inferred from Sequence Similarity, ECO:0000250), transferred from an Arabidopsis RLCK homolog, not experimentally determined for this specific protein.",
    "The protein name includes 'cytoplasmic' (receptor-like cytoplasmic kinase), which could mislead toward a cytoplasmic localization, but RLCKs are membrane-associated despite lacking transmembrane domains.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt entry A0A5J5NT52.",
    "The author's source snapshot is unknown; the entry was first public 2025-06-18, so the annotation may not have existed at the time the benchmark was constructed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with a plant serine/threonine kinase lacking mitochondrial targeting signals. Only B remains defensible among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB annotates this protein (A0A5J5NT52, GbEIR5D from Gossypium barbadense) with subcellular location 'Cell membrane' (C5, H3) and GO:0005886 'plasma membrane' (C6, H4). 'Cell membrane' is an EXACT synonym of GO:0005886 'plasma membrane' (GO2). The annotation is consistent with the protein being a receptor-like cytoplasmic kinase (RLCK), a family known to associate with the plasma membrane. However, the evidence code is ECO:0000250/ISS (similarity-based inference from Q9ZUF4), meaning this is computational transfer, not direct experimental localization.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Among the four options, three can be eliminated through general biological reasoning from the sequence: (A) inner membrane pellicle complex is specific to apicomplexan parasites (GO3 definition confirms 'apicomplexan parasite cell'), incompatible with a plant protein; (C) RQC complex is a defined ribosome-associated quality-control complex with specific protein components (Cdc48, Rkr1, etc., per GO4), not a kinase; (D) mitochondrial outer membrane requires an N-terminal mitochondrial targeting signal, which is absent from this sequence's N-terminus (no amphipathic cationic helix typical of mitochondrial precursors). The sequence clearly contains a serine/threonine kinase domain (recognizable GxGxxG, DFG, and activation loop motifs), making it a signaling kinase. With A, C, and D eliminated, B (plasma membrane) is the only remaining viable compartment for a membrane-associated kinase.",
    "missing_item_specific_fact": "The positive assignment to plasma membrane specifically (rather than cytoplasm, which is not offered as an option) relies on knowing that RLCKs associate with the plasma membrane via lipid modifications or protein interactions. However, since 'cytoplasm' is not among the choices, elimination reasoning suffices.",
    "reason": "The four options are sufficiently heterogeneous that general biological knowledge (apicomplexan specificity of pellicle, defined composition of RQC, requirement of MTS for mitochondrial outer membrane) eliminates three choices, leaving plasma membrane as the only viable answer. The kinase domain is identifiable from sequence motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with a plant serine/threonine kinase lacking mitochondrial targeting signals. Only B remains defensible among the four choices."
  },
  "important_caveats": [
    "The plasma membrane annotation is ISS (Inferred from Sequence Similarity, ECO:0000250), transferred from an Arabidopsis RLCK homolog, not experimentally determined for this specific protein.",
    "The protein name includes 'cytoplasmic' (receptor-like cytoplasmic kinase), which could mislead toward a cytoplasmic localization, but RLCKs are membrane-associated despite lacking transmembrane domains.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt entry A0A5J5NT52.",
    "The author's source snapshot is unknown; the entry was first public 2025-06-18, so the annotation may not have existed at the time the benchmark was constructed."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns cell membrane localization by transfer from another protein and includes a plasma-membrane GO annotation with ISS evidence. The historical record also contains these annotations. This supports B as an annotation, but is not direct experimental localization evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable protein kinase catalytic domain but no long hydrophobic transmembrane segment or obvious mitochondrial targeting peptide. A soluble plant signaling kinase can associate with the plasma membrane through interactions or membrane-targeting features; that family-level pattern favors plasma membrane over mitochondrial outer membrane. The pellicle-complex option is specific to apicomplexan parasites, and RQC is a ribosome-quality-control complex, neither a natural fit for this sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable kinase and cellular-localization patterns give a meaningful, probabilistic basis for B among these choices. The sequence alone does not prove membrane localization, but exact-protein database recall is not necessary to distinguish the options plausibly.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence does not establish localization conclusively, but the offered alternatives and the signaling-kinase pattern favor plasma membrane; no alternative is comparably supported.


### Important caveats

- The supplied localization annotations are computational or transferred rather than direct experimental evidence for this exact protein.
- The kinase domain itself does not establish plasma-membrane localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable protein kinase catalytic domain but no long hydrophobic transmembrane segment or obvious mitochondrial targeting peptide. A soluble plant signaling kinase can associate with the plasma membrane through interactions or membrane-targeting features; that family-level pattern favors plasma membrane over mitochondrial outer membrane. The pellicle-complex option is specific to apicomplexan parasites, and RQC is a ribosome-quality-control complex, neither a natural fit for this sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase and cellular-localization patterns give a meaningful, probabilistic basis for B among these choices. The sequence alone does not prove membrane localization, but exact-protein database recall is not necessary to distinguish the options plausibly."
  },
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns cell membrane localization by transfer from another protein and includes a plasma-membrane GO annotation with ISS evidence. The historical record also contains these annotations. This supports B as an annotation, but is not direct experimental localization evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied localization annotations are computational or transferred rather than direct experimental evidence for this exact protein.",
    "The kinase domain itself does not establish plasma-membrane localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not establish localization conclusively, but the offered alternatives and the signaling-kinase pattern favor plasma membrane; no alternative is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns cell membrane localization by transfer from another protein and includes a plasma-membrane GO annotation with ISS evidence. The historical record also contains these annotations. This supports B as an annotation, but is not direct experimental localization evidence for this exact protein.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable protein kinase catalytic domain but no long hydrophobic transmembrane segment or obvious mitochondrial targeting peptide. A soluble plant signaling kinase can associate with the plasma membrane through interactions or membrane-targeting features; that family-level pattern favors plasma membrane over mitochondrial outer membrane. The pellicle-complex option is specific to apicomplexan parasites, and RQC is a ribosome-quality-control complex, neither a natural fit for this sequence.",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase and cellular-localization patterns give a meaningful, probabilistic basis for B among these choices. The sequence alone does not prove membrane localization, but exact-protein database recall is not necessary to distinguish the options plausibly."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not establish localization conclusively, but the offered alternatives and the signaling-kinase pattern favor plasma membrane; no alternative is comparably supported."
  },
  "important_caveats": [
    "The supplied localization annotations are computational or transferred rather than direct experimental evidence for this exact protein.",
    "The kinase domain itself does not establish plasma-membrane localization."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A5J5NT52) annotates the subcellular location as 'Cell membrane' (SL-0039) with evidence code ECO:0000250 (Inferred by Similarity to Q9ZUF4), and the GO cross-reference lists GO:0005886 (plasma membrane) with IEA:UniProtKB-SubCell. The evidence is computational/inference-based (ISS/IEA) rather than direct experimental measurement for this specific protein, but it does support the expected answer B (plasma membrane). The protein is an EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase, consistent with plasma membrane association in plant immune signaling.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an unambiguous Ser/Thr kinase domain (GxGxxG glycine-rich loop 'GGFGPVHKGF', DFG motif 'DFGLAKDG', activation segment, APE motif 'GTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRS'), which eliminates the RQC complex (a ribosome-associated quality-control assembly, not a kinase). The sequence lacks apicomplexan-specific features and the protein's overall composition is consistent with a plant/eukaryotic kinase, eliminating the inner membrane pellicle complex (a structure unique to apicomplexan parasites). The N-terminus lacks a canonical mitochondrial targeting signal (no amphipathic helix with clustered Arg/Lys and hydroxylated residues typical of MTS), making mitochondrial outer membrane unlikely. Critically, the protein belongs to the receptor-like cytoplasmic kinase (RLCK) family in plants: the N-terminal region contains potential N-acylation sites (Ala2 after Met cleavage, Cys residues around positions 16-17 in 'PRCSKGIEEAEAEAEAETKKQ') consistent with myristoylation/palmitoylation that anchors RLCKs (e.g., BIK1, PBS1 in Arabidopsis) to the plasma membrane. Plant RLCKs are well-characterized as plasma membrane-associated kinases in PAMP-triggered immunity, providing strong family-level transferable knowledge that distinguishes plasma membrane from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can identify the kinase domain to eliminate the RQC complex, recognize the absence of an apicomplexan context to eliminate the pellicle complex, note the absence of a mitochondrial targeting signal to disfavour mitochondrial outer membrane, and apply well-established RLCK family biology (N-terminal acylation, plasma membrane association in plant immunity) to select plasma membrane. This is a multi-step inference using conserved sequence motifs, family-level knowledge, and structural principles learned from other plant RLCKs, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated: the pellicle complex is apicomplexan-specific, the RQC complex is a ribosomal quality-control assembly incompatible with a kinase domain, and the mitochondrial outer membrane lacks supporting sequence features. The plasma membrane is the only option consistent with the RLCK family biology, N-terminal acylation potential, and absence of organellar targeting signals.


### Important caveats

- The UniProt annotation for this protein's localization is ISS (inferred by similarity to Q9ZUF4) and IEA, not direct experimental evidence for this specific protein.
- The N-terminal Ala2 is a non-canonical myristoylation site (Gly is typical); membrane association may also be mediated by palmitoylation at internal Cys residues or protein-protein interaction with receptor kinases.
- The model is not given the protein name, organism, or family label; it must infer the RLCK family context from sequence features alone.
- The reviewer-only evidence confirms sequence match to UniProt A0A5J5NT52, but this accession and organism identity were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an unambiguous Ser/Thr kinase domain (GxGxxG glycine-rich loop 'GGFGPVHKGF', DFG motif 'DFGLAKDG', activation segment, APE motif 'GTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRS'), which eliminates the RQC complex (a ribosome-associated quality-control assembly, not a kinase). The sequence lacks apicomplexan-specific features and the protein's overall composition is consistent with a plant/eukaryotic kinase, eliminating the inner membrane pellicle complex (a structure unique to apicomplexan parasites). The N-terminus lacks a canonical mitochondrial targeting signal (no amphipathic helix with clustered Arg/Lys and hydroxylated residues typical of MTS), making mitochondrial outer membrane unlikely. Critically, the protein belongs to the receptor-like cytoplasmic kinase (RLCK) family in plants: the N-terminal region contains potential N-acylation sites (Ala2 after Met cleavage, Cys residues around positions 16-17 in 'PRCSKGIEEAEAEAEAETKKQ') consistent with myristoylation/palmitoylation that anchors RLCKs (e.g., BIK1, PBS1 in Arabidopsis) to the plasma membrane. Plant RLCKs are well-characterized as plasma membrane-associated kinases in PAMP-triggered immunity, providing strong family-level transferable knowledge that distinguishes plasma membrane from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the kinase domain to eliminate the RQC complex, recognize the absence of an apicomplexan context to eliminate the pellicle complex, note the absence of a mitochondrial targeting signal to disfavour mitochondrial outer membrane, and apply well-established RLCK family biology (N-terminal acylation, plasma membrane association in plant immunity) to select plasma membrane. This is a multi-step inference using conserved sequence motifs, family-level knowledge, and structural principles learned from other plant RLCKs, not a lookup of this protein's specific annotation."
  },
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A5J5NT52) annotates the subcellular location as 'Cell membrane' (SL-0039) with evidence code ECO:0000250 (Inferred by Similarity to Q9ZUF4), and the GO cross-reference lists GO:0005886 (plasma membrane) with IEA:UniProtKB-SubCell. The evidence is computational/inference-based (ISS/IEA) rather than direct experimental measurement for this specific protein, but it does support the expected answer B (plasma membrane). The protein is an EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase, consistent with plasma membrane association in plant immune signaling."
  },
  "important_caveats": [
    "The UniProt annotation for this protein's localization is ISS (inferred by similarity to Q9ZUF4) and IEA, not direct experimental evidence for this specific protein.",
    "The N-terminal Ala2 is a non-canonical myristoylation site (Gly is typical); membrane association may also be mediated by palmitoylation at internal Cys residues or protein-protein interaction with receptor kinases.",
    "The model is not given the protein name, organism, or family label; it must infer the RLCK family context from sequence features alone.",
    "The reviewer-only evidence confirms sequence match to UniProt A0A5J5NT52, but this accession and organism identity were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: the pellicle complex is apicomplexan-specific, the RQC complex is a ribosomal quality-control assembly incompatible with a kinase domain, and the mitochondrial outer membrane lacks supporting sequence features. The plasma membrane is the only option consistent with the RLCK family biology, N-terminal acylation potential, and absence of organellar targeting signals."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A5J5NT52) annotates the subcellular location as 'Cell membrane' (SL-0039) with evidence code ECO:0000250 (Inferred by Similarity to Q9ZUF4), and the GO cross-reference lists GO:0005886 (plasma membrane) with IEA:UniProtKB-SubCell. The evidence is computational/inference-based (ISS/IEA) rather than direct experimental measurement for this specific protein, but it does support the expected answer B (plasma membrane). The protein is an EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase, consistent with plasma membrane association in plant immune signaling.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an unambiguous Ser/Thr kinase domain (GxGxxG glycine-rich loop 'GGFGPVHKGF', DFG motif 'DFGLAKDG', activation segment, APE motif 'GTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRS'), which eliminates the RQC complex (a ribosome-associated quality-control assembly, not a kinase). The sequence lacks apicomplexan-specific features and the protein's overall composition is consistent with a plant/eukaryotic kinase, eliminating the inner membrane pellicle complex (a structure unique to apicomplexan parasites). The N-terminus lacks a canonical mitochondrial targeting signal (no amphipathic helix with clustered Arg/Lys and hydroxylated residues typical of MTS), making mitochondrial outer membrane unlikely. Critically, the protein belongs to the receptor-like cytoplasmic kinase (RLCK) family in plants: the N-terminal region contains potential N-acylation sites (Ala2 after Met cleavage, Cys residues around positions 16-17 in 'PRCSKGIEEAEAEAEAETKKQ') consistent with myristoylation/palmitoylation that anchors RLCKs (e.g., BIK1, PBS1 in Arabidopsis) to the plasma membrane. Plant RLCKs are well-characterized as plasma membrane-associated kinases in PAMP-triggered immunity, providing strong family-level transferable knowledge that distinguishes plasma membrane from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the kinase domain to eliminate the RQC complex, recognize the absence of an apicomplexan context to eliminate the pellicle complex, note the absence of a mitochondrial targeting signal to disfavour mitochondrial outer membrane, and apply well-established RLCK family biology (N-terminal acylation, plasma membrane association in plant immunity) to select plasma membrane. This is a multi-step inference using conserved sequence motifs, family-level knowledge, and structural principles learned from other plant RLCKs, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: the pellicle complex is apicomplexan-specific, the RQC complex is a ribosomal quality-control assembly incompatible with a kinase domain, and the mitochondrial outer membrane lacks supporting sequence features. The plasma membrane is the only option consistent with the RLCK family biology, N-terminal acylation potential, and absence of organellar targeting signals."
  },
  "important_caveats": [
    "The UniProt annotation for this protein's localization is ISS (inferred by similarity to Q9ZUF4) and IEA, not direct experimental evidence for this specific protein.",
    "The N-terminal Ala2 is a non-canonical myristoylation site (Gly is typical); membrane association may also be mediated by palmitoylation at internal Cys residues or protein-protein interaction with receptor kinases.",
    "The model is not given the protein name, organism, or family label; it must infer the RLCK family context from sequence features alone.",
    "The reviewer-only evidence confirms sequence match to UniProt A0A5J5NT52, but this accession and organism identity were not provided to the evaluated model."
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
  "requested_accession": "A0A5J5NT52",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "d7e15719160373fd4dde713a8a3f3afa041b4c4e33dab33f3231fec4ccd04df4",
  "benchmark_sequence_length": 460,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-12-11",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "current_source_sequence_sha256": "d7e15719160373fd4dde713a8a3f3afa041b4c4e33dab33f3231fec4ccd04df4",
  "current_source_sequence_length": 460,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 17,
  "selected_historical_version": {
    "accession": "A0A5J5NT52",
    "database": "Swiss-Prot",
    "entryVersion": 17,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIR5D_GOSBA",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a",
  "selected_historical_source_sequence_sha256": "d7e15719160373fd4dde713a8a3f3afa041b4c4e33dab33f3231fec4ccd04df4",
  "selected_historical_source_sequence_length": 460,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 17,
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A5J5NT52\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-12-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Sea Island cotton\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"malvids\",\"Malvales\",\"Malvaceae\",\"Malvoideae\",\"Gossypium\"],\"scientificName\":\"Gossypium barbadense\",\"synonyms\":[\"Hibiscus barbadensis\"],\"taxonId\":3634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10027\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"2.7.11.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39488762\",\"source\":\"PubMed\"}],\"value\":\"EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5D\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39488762\",\"source\":\"PubMed\"}],\"value\":\"GbEIR5D\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9ZUF4\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Sun L.\",\"Li X.\",\"Zhong J.\",\"Wang Y.\",\"Li B.\",\"Ye Z.\",\"Zhang J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39488762\"},{\"database\":\"DOI\",\"id\":\"10.1002/advs.202407787\"}],\"citationType\":\"journal article\",\"firstPage\":\"e2407787\",\"id\":\"39488762\",\"journal\":\"Adv. Sci.\",\"lastPage\":\"e2407787\",\"publicationDate\":\"2025\",\"title\":\"Recognition of a fungal effector potentiates pathogen-associated molecular pattern-triggered immunity in cotton.\",\"volume\":\"12\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Hai7124\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"INTERACTION WITH V.DAHLIAE EPD1\",\"INDUCTION BY V.DAHLIAE EPD1\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17",
  "source_sha256": "e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a",
  "retrieved_utc": "2026-11-02T04:25:32.436038+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   EIR5D_GOSBA             Reviewed;         460 AA.\nAC   A0A5J5NT52;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-DEC-2019, sequence version 1.\nDT   28-JAN-2026, entry version 17.\nDE   RecName: Full=EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5D {ECO:0000303|PubMed:39488762};\nDE            Short=GbEIR5D {ECO:0000303|PubMed:39488762};\nDE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};\nGN   Name=EIR5D {ECO:0000303|PubMed:39488762};\nGN   ORFNames=ES319_D13G225100v1 {ECO:0000312|EMBL:KAB1996350.1};\nOS   Gossypium barbadense (Sea Island cotton) (Hibiscus barbadensis).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; malvids; Malvales; Malvaceae; Malvoideae; Gossypium.\nOX   NCBI_TaxID=3634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 17,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17",
  "source_sha256": "e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a",
  "retrieved_utc": "2026-11-02T04:25:32.436038+00:00",
  "source_locator": "lines 29-37",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, INTERACTION WITH V.DAHLIAE EPD1, INDUCTION\nRP   BY V.DAHLIAE EPD1, AND TISSUE SPECIFICITY.\nRC   STRAIN=cv. Hai7124;\nRX   PubMed=39488762; DOI=10.1002/advs.202407787;\nRA   Sun L., Li X., Zhong J., Wang Y., Li B., Ye Z., Zhang J.;\nRT   \"Recognition of a fungal effector potentiates pathogen-associated molecular\nRT   pattern-triggered immunity in cotton.\";\nRL   Adv. Sci. 12:e2407787-e2407787(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 17,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17",
  "source_sha256": "e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a",
  "retrieved_utc": "2026-11-02T04:25:32.436038+00:00",
  "source_locator": "lines 64-64",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:Q9ZUF4}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 17,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17",
  "source_sha256": "e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a",
  "retrieved_utc": "2026-11-02T04:25:32.436038+00:00",
  "source_locator": "lines 90-90",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 17,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 59009-59021",
  "excerpt": "[Term]\nid: GO:0005741\nname: mitochondrial outer membrane\nnamespace: cellular_component\ndef: \"The outer, i.e. cytoplasm-facing, lipid bilayer of the mitochondrial envelope.\" [GOC:ai]\nsynonym: \"mitochondrion outer membrane\" EXACT []\nsynonym: \"outer mitochondrial membrane\" EXACT []\nsynonym: \"outer mitochondrion membrane\" EXACT []\nxref: NIF_Subcellular:sao1289741256\nxref: Wikipedia:Outer_mitochondrial_membrane\nis_a: GO:0031966 ! mitochondrial membrane\nis_a: GO:0031968 ! organelle outer membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005741"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 60420-60454",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005886"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 365849-365857",
  "excerpt": "[Term]\nid: GO:0070258\nname: inner membrane pellicle complex\nnamespace: cellular_component\ndef: \"A membrane structure formed of two closely aligned lipid bilayers that lie beneath the plasma membrane and form part of the pellicle surrounding an apicomplexan parasite cell.\" [GOC:mah, PMID:12456714]\nsynonym: \"inner membrane complex\" BROAD []\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0020039 ! pellicle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0070258"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 549333-549341",
  "excerpt": "[Term]\nid: GO:1990112\nname: RQC complex\nnamespace: cellular_component\ndef: \"A multiprotein complex that forms a stable complex with large ribosomal subunits (60S in eukaryotes and 50S in prokaryotes) containing stalled polypeptides and triggers their degradation (ribosomal quality control). In budding yeast, this complex includes Cdc48p, Rkr1p, Tae2p, Rqc1p, Npl4p and Ufd1p proteins.\" [GOC:rb, PMID:23178123, PMID:23232563]\nsynonym: \"ribosome quality control complex\" EXACT [PMID:23178123, PMID:23232563]\nsynonym: \"ribosome-bound quality control complex\" EXACT []\nis_a: GO:0032991 ! protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:1990112"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
