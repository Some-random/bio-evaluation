# active_site_0122: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0122.txt)

**Task:** `active_site`  
**Author key, unchanged:** **B** — Position 109 (Nucleophile)

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
MMLPLLAVSAFASLGAAQTYTSCNPTNSLKTWSLSTDFTQGSSDGWTAISGNVTYGSNGAEFTINKRYDAPTLETNFYIFFGEVEVVMRAANGTGIVSSIVMESDDLDEIDWECTGTDTTQIQTNYFGKGNTTTYDRAIWETVSSPQDEFHTYKVVWTAAAITWYIDGTAVRTLEYADAVDGKNYPQTPMVVKLGIWAGGDPSNSEGTIEWAGGETDYDEVPFTMYVKSVNIINYNPAASYNYTDKTGSYTSIVASNSTTGSGIHSSNSVSVFAPSSSTSTFTSSRALIATASTYPASVQTSSSGVVSLSSSSASSSSAAASSTSGSASAVFTGAAVTNLPSFFFTVFFALAIALAF

[Multiple Choices]
A. Position 92 (Proton donor)
B. Position 109 (Nucleophile)
C. Position 975 (Proton acceptor; for dehydratase activity 1)
D. Position 151 (Proton acceptor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the UniProt entry, which annotates position 109 as the nucleophile. This annotation is transferred by similarity from another UniProt protein, so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently unambiguous general rule for assigning the catalytic role to residue 109 rather than the other listed positions; recognizing a family motif would require protein-specific interpretation.


**Missing item-specific fact**

> The catalytic-residue annotation or a sufficiently informative homolog/structure mapping identifying position 109 as the nucleophile.


**Reason**

> The key is supported by a sequence-matched database annotation, but that annotation and its homolog-based evidence were not supplied in the question. Exact catalytic roles and positions cannot be established from generic sequence heuristics alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports B. The annotated proton donor is at position 113, not the offered position 92, and position 975 exceeds the 357-residue sequence.


### Important caveats

- The active-site annotation is based on similarity to UniProtKB:P27051 (ECO:0000250), not shown here as direct experimental evidence for this sequence.
- The historical entry and current entry both match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently unambiguous general rule for assigning the catalytic role to residue 109 rather than the other listed positions; recognizing a family motif would require protein-specific interpretation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The catalytic-residue annotation or a sufficiently informative homolog/structure mapping identifying position 109 as the nucleophile.",
    "reason": "The key is supported by a sequence-matched database annotation, but that annotation and its homolog-based evidence were not supplied in the question. Exact catalytic roles and positions cannot be established from generic sequence heuristics alone."
  },
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry, which annotates position 109 as the nucleophile. This annotation is transferred by similarity from another UniProt protein, so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The active-site annotation is based on similarity to UniProtKB:P27051 (ECO:0000250), not shown here as direct experimental evidence for this sequence.",
    "The historical entry and current entry both match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B. The annotated proton donor is at position 113, not the offered position 92, and position 975 exceeds the 357-residue sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry, which annotates position 109 as the nucleophile. This annotation is transferred by similarity from another UniProt protein, so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently unambiguous general rule for assigning the catalytic role to residue 109 rather than the other listed positions; recognizing a family motif would require protein-specific interpretation.",
    "missing_item_specific_fact": "The catalytic-residue annotation or a sufficiently informative homolog/structure mapping identifying position 109 as the nucleophile.",
    "reason": "The key is supported by a sequence-matched database annotation, but that annotation and its homolog-based evidence were not supplied in the question. Exact catalytic roles and positions cannot be established from generic sequence heuristics alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B. The annotated proton donor is at position 113, not the offered position 92, and position 975 exceeds the 357-residue sequence."
  },
  "important_caveats": [
    "The active-site annotation is based on similarity to UniProtKB:P27051 (ECO:0000250), not shown here as direct experimental evidence for this sequence.",
    "The historical entry and current entry both match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WD22 (Crh-like protein 1, A. fumigatus) annotates position 109 as 'Nucleophile' active site (evidence C5/H3). The residue at position 109 in the supplied sequence is indeed E (glutamic acid), consistent with a nucleophile in glycosidase/transglycosylase catalysis. The protein is annotated as a chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-). However, the evidence code is ECO:0000250 (inferred by similarity from P27051), meaning this is a computational transfer annotation rather than direct experimental determination on this specific protein. The annotation is nonetheless consistent with the known catalytic mechanism of GH75-family transglycosylases.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains recognizable glycoside hydrolase/transglycosylase domain features (e.g., 'IVMESDDLDE' motif region around positions 100-109). Glycosidases and transglycosylases characteristically employ Glu or Asp as the catalytic nucleophile. Position 109 is E (glutamate) located in a conserved catalytic motif region, making it a strong nucleophile candidate. Option C (position 975) is impossible in a 357-residue protein. Option A (position 92 = N, asparagine) is not a typical proton-donating catalytic residue in glycosidases. Option D (position 151 = H, histidine as proton acceptor) is atypical for glycosidase/transglycosylase active sites, which rely on carboxylate residues. By elimination and general glycosidase biochemistry, B is the most defensible choice.


**Missing item-specific fact**

> The precise mechanistic distinction between E109 as 'nucleophile' versus E113 as 'proton donor' in the GH75/Crh family requires family-specific mechanistic knowledge not derivable from sequence alone. However, since position 113 is not offered as a competing option, this does not impede selecting B from the four choices.


**Reason**

> Options A and C are eliminable by basic checks (wrong residue chemistry; position exceeds protein length). Option D (His as proton acceptor) is inconsistent with glycosidase catalytic chemistry. Option B (Glu as nucleophile) aligns with general glycosidase/transglycosylase mechanism knowledge. A model with general enzyme biochemistry knowledge can meaningfully distinguish B from the distractors without memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (N92 as proton donor) and C (position 975 in a 357-aa protein) are clearly incorrect. Option D (H151 as proton acceptor) is inconsistent with glycosidase catalytic chemistry. Only B is biochemically defensible for a glycosidase/transglycosylase active site among the four choices.


### Important caveats

- The UniProt annotation for position 109 as nucleophile is by similarity (ECO:0000250 from P27051), not direct experimental evidence on Crh1 itself. The 2019 Nature Communications paper (PubMed:30971696) provides functional and disruption phenotype data but the active-site residue roles are transferred.
- The protein is a precursor (signal peptide present); numbering is canonical full-length, which matches the supplied sequence.
- The specific role labels 'nucleophile' vs 'proton donor' for E109 vs E113 are family-specific (GH75) assignments; a model distinguishing these two positions would need mechanistic knowledge of this particular enzyme family. However, since E113 is not a competing option, this does not affect answerability from the given choices.
- The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence analysis and general biochemical knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains recognizable glycoside hydrolase/transglycosylase domain features (e.g., 'IVMESDDLDE' motif region around positions 100-109). Glycosidases and transglycosylases characteristically employ Glu or Asp as the catalytic nucleophile. Position 109 is E (glutamate) located in a conserved catalytic motif region, making it a strong nucleophile candidate. Option C (position 975) is impossible in a 357-residue protein. Option A (position 92 = N, asparagine) is not a typical proton-donating catalytic residue in glycosidases. Option D (position 151 = H, histidine as proton acceptor) is atypical for glycosidase/transglycosylase active sites, which rely on carboxylate residues. By elimination and general glycosidase biochemistry, B is the most defensible choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise mechanistic distinction between E109 as 'nucleophile' versus E113 as 'proton donor' in the GH75/Crh family requires family-specific mechanistic knowledge not derivable from sequence alone. However, since position 113 is not offered as a competing option, this does not impede selecting B from the four choices.",
    "reason": "Options A and C are eliminable by basic checks (wrong residue chemistry; position exceeds protein length). Option D (His as proton acceptor) is inconsistent with glycosidase catalytic chemistry. Option B (Glu as nucleophile) aligns with general glycosidase/transglycosylase mechanism knowledge. A model with general enzyme biochemistry knowledge can meaningfully distinguish B from the distractors without memorizing this specific UniProt entry."
  },
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WD22 (Crh-like protein 1, A. fumigatus) annotates position 109 as 'Nucleophile' active site (evidence C5/H3). The residue at position 109 in the supplied sequence is indeed E (glutamic acid), consistent with a nucleophile in glycosidase/transglycosylase catalysis. The protein is annotated as a chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-). However, the evidence code is ECO:0000250 (inferred by similarity from P27051), meaning this is a computational transfer annotation rather than direct experimental determination on this specific protein. The annotation is nonetheless consistent with the known catalytic mechanism of GH75-family transglycosylases."
  },
  "important_caveats": [
    "The UniProt annotation for position 109 as nucleophile is by similarity (ECO:0000250 from P27051), not direct experimental evidence on Crh1 itself. The 2019 Nature Communications paper (PubMed:30971696) provides functional and disruption phenotype data but the active-site residue roles are transferred.",
    "The protein is a precursor (signal peptide present); numbering is canonical full-length, which matches the supplied sequence.",
    "The specific role labels 'nucleophile' vs 'proton donor' for E109 vs E113 are family-specific (GH75) assignments; a model distinguishing these two positions would need mechanistic knowledge of this particular enzyme family. However, since E113 is not a competing option, this does not affect answerability from the given choices.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence analysis and general biochemical knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (N92 as proton donor) and C (position 975 in a 357-aa protein) are clearly incorrect. Option D (H151 as proton acceptor) is inconsistent with glycosidase catalytic chemistry. Only B is biochemically defensible for a glycosidase/transglycosylase active site among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WD22 (Crh-like protein 1, A. fumigatus) annotates position 109 as 'Nucleophile' active site (evidence C5/H3). The residue at position 109 in the supplied sequence is indeed E (glutamic acid), consistent with a nucleophile in glycosidase/transglycosylase catalysis. The protein is annotated as a chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-). However, the evidence code is ECO:0000250 (inferred by similarity from P27051), meaning this is a computational transfer annotation rather than direct experimental determination on this specific protein. The annotation is nonetheless consistent with the known catalytic mechanism of GH75-family transglycosylases.",
    "evidence_ids": ["C5", "H3", "C4", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains recognizable glycoside hydrolase/transglycosylase domain features (e.g., 'IVMESDDLDE' motif region around positions 100-109). Glycosidases and transglycosylases characteristically employ Glu or Asp as the catalytic nucleophile. Position 109 is E (glutamate) located in a conserved catalytic motif region, making it a strong nucleophile candidate. Option C (position 975) is impossible in a 357-residue protein. Option A (position 92 = N, asparagine) is not a typical proton-donating catalytic residue in glycosidases. Option D (position 151 = H, histidine as proton acceptor) is atypical for glycosidase/transglycosylase active sites, which rely on carboxylate residues. By elimination and general glycosidase biochemistry, B is the most defensible choice.",
    "missing_item_specific_fact": "The precise mechanistic distinction between E109 as 'nucleophile' versus E113 as 'proton donor' in the GH75/Crh family requires family-specific mechanistic knowledge not derivable from sequence alone. However, since position 113 is not offered as a competing option, this does not impede selecting B from the four choices.",
    "reason": "Options A and C are eliminable by basic checks (wrong residue chemistry; position exceeds protein length). Option D (His as proton acceptor) is inconsistent with glycosidase catalytic chemistry. Option B (Glu as nucleophile) aligns with general glycosidase/transglycosylase mechanism knowledge. A model with general enzyme biochemistry knowledge can meaningfully distinguish B from the distractors without memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (N92 as proton donor) and C (position 975 in a 357-aa protein) are clearly incorrect. Option D (H151 as proton acceptor) is inconsistent with glycosidase catalytic chemistry. Only B is biochemically defensible for a glycosidase/transglycosylase active site among the four choices."
  },
  "important_caveats": [
    "The UniProt annotation for position 109 as nucleophile is by similarity (ECO:0000250 from P27051), not direct experimental evidence on Crh1 itself. The 2019 Nature Communications paper (PubMed:30971696) provides functional and disruption phenotype data but the active-site residue roles are transferred.",
    "The protein is a precursor (signal peptide present); numbering is canonical full-length, which matches the supplied sequence.",
    "The specific role labels 'nucleophile' vs 'proton donor' for E109 vs E113 are family-specific (GH75) assignments; a model distinguishing these two positions would need mechanistic knowledge of this particular enzyme family. However, since E113 is not a competing option, this does not affect answerability from the given choices.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence analysis and general biochemical knowledge."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies residue 109 as the nucleophile. This is a homology-transferred annotation, not direct experimental validation in this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conspicuous acidic motif around positions 109–113 (EIDWE), consistent with the conserved catalytic acidic region of related carbohydrate-active enzymes. Transferable family knowledge makes a catalytic glutamate at 109 a credible nucleophile candidate; among the choices, this favors B. The 975 option is also outside the 357-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A conserved catalytic motif and the offered residue/role pair provide a meaningful family-level inference without requiring the exact protein's annotation, though sequence alone does not prove the catalytic assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported: position 975 is beyond the sequence length, and the sequence motif supports the glutamate at 109 over the other listed positions.


### Important caveats

- The source annotation is supported by similarity evidence from another protein; it is not direct experimental evidence for residue 109 in this exact protein.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conspicuous acidic motif around positions 109–113 (EIDWE), consistent with the conserved catalytic acidic region of related carbohydrate-active enzymes. Transferable family knowledge makes a catalytic glutamate at 109 a credible nucleophile candidate; among the choices, this favors B. The 975 option is also outside the 357-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A conserved catalytic motif and the offered residue/role pair provide a meaningful family-level inference without requiring the exact protein's annotation, though sequence alone does not prove the catalytic assignment."
  },
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 109 as the nucleophile. This is a homology-transferred annotation, not direct experimental validation in this protein."
  },
  "important_caveats": [
    "The source annotation is supported by similarity evidence from another protein; it is not direct experimental evidence for residue 109 in this exact protein.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported: position 975 is beyond the sequence length, and the sequence motif supports the glutamate at 109 over the other listed positions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 109 as the nucleophile. This is a homology-transferred annotation, not direct experimental validation in this protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conspicuous acidic motif around positions 109–113 (EIDWE), consistent with the conserved catalytic acidic region of related carbohydrate-active enzymes. Transferable family knowledge makes a catalytic glutamate at 109 a credible nucleophile candidate; among the choices, this favors B. The 975 option is also outside the 357-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "A conserved catalytic motif and the offered residue/role pair provide a meaningful family-level inference without requiring the exact protein's annotation, though sequence alone does not prove the catalytic assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported: position 975 is beyond the sequence length, and the sequence motif supports the glutamate at 109 over the other listed positions."
  },
  "important_caveats": [
    "The source annotation is supported by similarity evidence from another protein; it is not direct experimental evidence for residue 109 in this exact protein.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WD22 annotates position 109 as 'Active site: Nucleophile' (evidence C5/H3). The evidence code is ECO:0000250 (inferred by similarity from P27051, another chitinase), making this a transfer annotation rather than direct experimental evidence for this exact protein. However, the protein (Crh1, a GH18 chitin transglycosylase) has been functionally characterized (PubMed:30971696), and the Glu nucleophile at position 109 in the 'DDE' motif is consistent with the well-established GH18 catalytic mechanism. The annotation is present and consistent with family-level biochemistry.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can recognize this as a GH18-family chitinase/chitin transglycosylase from sequence features: the N-terminal signal peptide, the conserved 'IWW' motif (~positions 156-158), the 'DGKNYPQTP' motif (~positions 182-190), and the Ser/Thr-rich C-terminal linker. GH18 enzymes use a retaining mechanism with a Glu nucleophile in a conserved 'DGXE' or 'DDE' motif and a Glu proton donor 4 residues downstream. In this sequence, positions 107-109 form 'DDE' (D107-D108-E109) and position 113 is E (the proton donor, 4 residues after E109). This matches the canonical GH18 catalytic arrangement. Option C (position 975) is eliminated because the protein is only 357 residues long. Option A (position 92 = Asn, 'proton donor') is inconsistent because Asn is not a proton-donating catalytic residue in glycosidases. Option D (position 151 = His, 'proton acceptor') is inconsistent because GH18 does not employ a separate proton acceptor; the nucleophile Glu serves as both nucleophile and general base in the deglycosylation step. Thus, family-level knowledge of GH18 catalytic mechanism meaningfully distinguishes B from the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH18 family catalytic mechanism (Glu nucleophile + Glu proton donor in a DxE/DDE context, 4-residue spacing) is well-established transferable knowledge from hundreds of characterized GH18 chitinases. The sequence motifs (IWW, DGKNYPQTP, signal peptide, Ser-rich linker) allow family assignment. The 'DDE' at 107-109 with E113 four residues downstream matches the canonical pattern. The distractors are eliminated by basic biochemistry (Asn ≠ proton donor; His ≠ proton acceptor in GH18; position 975 > protein length).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is impossible (position exceeds protein length). Option A assigns 'proton donor' to Asn, which is not a catalytic acid in glycosidases. Option D assigns 'proton acceptor' to His, which does not participate in the GH18 retaining mechanism. Only option B is consistent with both the sequence context and the established GH18 catalytic mechanism.


### Important caveats

- The UniProt annotation for position 109 uses evidence code ECO:0000250 (similarity-based transfer from P27051), not direct experimental mutagenesis evidence for Crh1 itself. However, functional characterization of Crh1 exists (PubMed:30971696).
- The annotation was first integrated into Swiss-Prot on 2025-06-18; the benchmark author's source snapshot is unknown. The sequence and annotation are stable (sequence version 1 since 2005).
- Option C (position 975) is a trivially eliminable distractor since the protein is 357 residues, which may reduce the question's difficulty beyond what the family-knowledge reasoning alone would require.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can recognize this as a GH18-family chitinase/chitin transglycosylase from sequence features: the N-terminal signal peptide, the conserved 'IWW' motif (~positions 156-158), the 'DGKNYPQTP' motif (~positions 182-190), and the Ser/Thr-rich C-terminal linker. GH18 enzymes use a retaining mechanism with a Glu nucleophile in a conserved 'DGXE' or 'DDE' motif and a Glu proton donor 4 residues downstream. In this sequence, positions 107-109 form 'DDE' (D107-D108-E109) and position 113 is E (the proton donor, 4 residues after E109). This matches the canonical GH18 catalytic arrangement. Option C (position 975) is eliminated because the protein is only 357 residues long. Option A (position 92 = Asn, 'proton donor') is inconsistent because Asn is not a proton-donating catalytic residue in glycosidases. Option D (position 151 = His, 'proton acceptor') is inconsistent because GH18 does not employ a separate proton acceptor; the nucleophile Glu serves as both nucleophile and general base in the deglycosylation step. Thus, family-level knowledge of GH18 catalytic mechanism meaningfully distinguishes B from the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH18 family catalytic mechanism (Glu nucleophile + Glu proton donor in a DxE/DDE context, 4-residue spacing) is well-established transferable knowledge from hundreds of characterized GH18 chitinases. The sequence motifs (IWW, DGKNYPQTP, signal peptide, Ser-rich linker) allow family assignment. The 'DDE' at 107-109 with E113 four residues downstream matches the canonical pattern. The distractors are eliminated by basic biochemistry (Asn ≠ proton donor; His ≠ proton acceptor in GH18; position 975 > protein length)."
  },
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WD22 annotates position 109 as 'Active site: Nucleophile' (evidence C5/H3). The evidence code is ECO:0000250 (inferred by similarity from P27051, another chitinase), making this a transfer annotation rather than direct experimental evidence for this exact protein. However, the protein (Crh1, a GH18 chitin transglycosylase) has been functionally characterized (PubMed:30971696), and the Glu nucleophile at position 109 in the 'DDE' motif is consistent with the well-established GH18 catalytic mechanism. The annotation is present and consistent with family-level biochemistry."
  },
  "important_caveats": [
    "The UniProt annotation for position 109 uses evidence code ECO:0000250 (similarity-based transfer from P27051), not direct experimental mutagenesis evidence for Crh1 itself. However, functional characterization of Crh1 exists (PubMed:30971696).",
    "The annotation was first integrated into Swiss-Prot on 2025-06-18; the benchmark author's source snapshot is unknown. The sequence and annotation are stable (sequence version 1 since 2005).",
    "Option C (position 975) is a trivially eliminable distractor since the protein is 357 residues, which may reduce the question's difficulty beyond what the family-knowledge reasoning alone would require."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is impossible (position exceeds protein length). Option A assigns 'proton donor' to Asn, which is not a catalytic acid in glycosidases. Option D assigns 'proton acceptor' to His, which does not participate in the GH18 retaining mechanism. Only option B is consistent with both the sequence context and the established GH18 catalytic mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WD22 annotates position 109 as 'Active site: Nucleophile' (evidence C5/H3). The evidence code is ECO:0000250 (inferred by similarity from P27051, another chitinase), making this a transfer annotation rather than direct experimental evidence for this exact protein. However, the protein (Crh1, a GH18 chitin transglycosylase) has been functionally characterized (PubMed:30971696), and the Glu nucleophile at position 109 in the 'DDE' motif is consistent with the well-established GH18 catalytic mechanism. The annotation is present and consistent with family-level biochemistry.",
    "evidence_ids": ["C5", "H3", "C6", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can recognize this as a GH18-family chitinase/chitin transglycosylase from sequence features: the N-terminal signal peptide, the conserved 'IWW' motif (~positions 156-158), the 'DGKNYPQTP' motif (~positions 182-190), and the Ser/Thr-rich C-terminal linker. GH18 enzymes use a retaining mechanism with a Glu nucleophile in a conserved 'DGXE' or 'DDE' motif and a Glu proton donor 4 residues downstream. In this sequence, positions 107-109 form 'DDE' (D107-D108-E109) and position 113 is E (the proton donor, 4 residues after E109). This matches the canonical GH18 catalytic arrangement. Option C (position 975) is eliminated because the protein is only 357 residues long. Option A (position 92 = Asn, 'proton donor') is inconsistent because Asn is not a proton-donating catalytic residue in glycosidases. Option D (position 151 = His, 'proton acceptor') is inconsistent because GH18 does not employ a separate proton acceptor; the nucleophile Glu serves as both nucleophile and general base in the deglycosylation step. Thus, family-level knowledge of GH18 catalytic mechanism meaningfully distinguishes B from the other options.",
    "missing_item_specific_fact": "",
    "reason": "The GH18 family catalytic mechanism (Glu nucleophile + Glu proton donor in a DxE/DDE context, 4-residue spacing) is well-established transferable knowledge from hundreds of characterized GH18 chitinases. The sequence motifs (IWW, DGKNYPQTP, signal peptide, Ser-rich linker) allow family assignment. The 'DDE' at 107-109 with E113 four residues downstream matches the canonical pattern. The distractors are eliminated by basic biochemistry (Asn ≠ proton donor; His ≠ proton acceptor in GH18; position 975 > protein length)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is impossible (position exceeds protein length). Option A assigns 'proton donor' to Asn, which is not a catalytic acid in glycosidases. Option D assigns 'proton acceptor' to His, which does not participate in the GH18 retaining mechanism. Only option B is consistent with both the sequence context and the established GH18 catalytic mechanism."
  },
  "important_caveats": [
    "The UniProt annotation for position 109 uses evidence code ECO:0000250 (similarity-based transfer from P27051), not direct experimental mutagenesis evidence for Crh1 itself. However, functional characterization of Crh1 exists (PubMed:30971696).",
    "The annotation was first integrated into Swiss-Prot on 2025-06-18; the benchmark author's source snapshot is unknown. The sequence and annotation are stable (sequence version 1 since 2005).",
    "Option C (position 975) is a trivially eliminable distractor since the protein is 357 residues, which may reduce the question's difficulty beyond what the family-knowledge reasoning alone would require."
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
  "requested_accession": "Q4WD22",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "ec9eee989d92a990718dcd7214cf49eeaec45c138b491bd8fd04ef815d8dc8af",
  "benchmark_sequence_length": 357,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 109,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "current_source_sequence_sha256": "ec9eee989d92a990718dcd7214cf49eeaec45c138b491bd8fd04ef815d8dc8af",
  "current_source_sequence_length": 357,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 107,
  "selected_historical_version": {
    "accession": "Q4WD22",
    "database": "Swiss-Prot",
    "entryVersion": 107,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH1_ASPFU",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "selected_historical_source_sequence_sha256": "ec9eee989d92a990718dcd7214cf49eeaec45c138b491bd8fd04ef815d8dc8af",
  "selected_historical_source_sequence_length": 357,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 107,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q4WD22\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":109,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitinase crh1\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitin transglycosylase crh1\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P27051\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":109},\"start\":{\"modifier\":\"EXACT\",\"value\":109}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P27051\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":113},\"start\":{\"modifier\":\"EXACT\",\"value\":113}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":113},\"start\":{\"modifier\":\"EXACT\",\"value\":113}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":193}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":197},\"start\":{\"modifier\":\"EXACT\",\"value\":197}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":208},\"start\":{\"modifier\":\"EXACT\",\"value\":208}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Fang W.\",\"Sanz A.B.\",\"Bartual S.G.\",\"Wang B.\",\"Ferenbach A.T.\",\"Farkas V.\",\"Hurtado-Guerrero R.\",\"Arroyo J.\",\"van Aalten D.M.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30971696\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-019-09674-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"1669\",\"id\":\"30971696\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"1669\",\"publicationDate\":\"2019\",\"title\":\"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh transglycosylases.\",\"volume\":\"10\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "source_locator": "lines 1-20",
  "excerpt": "ID   CRH1_ASPFU              Reviewed;         357 AA.\nAC   Q4WD22;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 107.\nDE   RecName: Full=Crh-like protein 1 {ECO:0000303|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitinase crh1 {ECO:0000303|PubMed:30971696};\nDE              EC=3.2.1.14 {ECO:0000305|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh1 {ECO:0000303|PubMed:30971696};\nDE              EC=2.4.-.- {ECO:0000269|PubMed:30971696};\nDE   Flags: Precursor;\nGN   Name=crh1 {ECO:0000303|PubMed:30971696}; ORFNames=AFUA_6G03230;\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 107,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "source_locator": "lines 46-53",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30971696; DOI=10.1038/s41467-019-09674-0;\nRA   Fang W., Sanz A.B., Bartual S.G., Wang B., Ferenbach A.T., Farkas V.,\nRA   Hurtado-Guerrero R., Arroyo J., van Aalten D.M.F.;\nRT   \"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh\nRT   transglycosylases.\";\nRL   Nat. Commun. 10:1669-1669(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 107,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "source_locator": "lines 132-134",
  "excerpt": "FT   ACT_SITE        109\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P27051\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 107,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "source_locator": "lines 135-137",
  "excerpt": "FT   ACT_SITE        113\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P27051\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 107,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "source_locator": "lines 138-141",
  "excerpt": "FT   BINDING         113\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 107,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "source_locator": "lines 142-145",
  "excerpt": "FT   BINDING         193\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 107,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "source_locator": "lines 146-149",
  "excerpt": "FT   BINDING         197\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 107,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "source_locator": "lines 150-153",
  "excerpt": "FT   BINDING         208\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 107,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 122. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
