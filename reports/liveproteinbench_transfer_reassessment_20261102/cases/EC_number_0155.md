# EC_number_0155: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0155.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **D** — 3.1.3.16

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
MAGVEEADKLKQLGNAAFSERKWHLAIDMYTKAIELTKTPTLFCNRALAELRAELPGAALADADAALGIEPTFAKAYYHKASAYLSLGKHKQALTNYKKVVDLAPQNSDAQAKVEFCKKEIRRINFENAIMTPDEAPLSQTIKLGSVRADYDGPRIENETVTVEFVEAMKEHFRLEKLIDRHDVIFILLEVQKILKKCPNFVSINVPVGEEITVCGDTHGQYYDLLNIFKLNGNPLETNRYLFNGDFVDRGSYSFENIMTLFAYKVLYPDHFFLSRGNHEGVSMNRMYGFEGEVTQKYNSEMFRLFTEVFNSLPIGHIINNEVFVVHGGLYSSDKVTLDDLQHPNRFRDIPESGLICESLWSDPQPMPGRAPSKRGVSCLSFGPDVTETFLNNNNLKLLVRSHEVKDEGYEIEHGGKCITVFSAPNYCDQMGNKGAFIRFTGGDMKPRFTTFTHVPHPGKRPMHYATGFGLF

[Multiple Choices]
A. 3.1.3.112
B. 5.3.1.8
C. 2.7.7.80
D. 3.1.3.16
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact sequence matches UniProt entry Q388N2, whose archived annotation assigns EC 3.1.3.16 and describes dephosphorylation of phosphoserine- and phosphothreonine-containing proteins, citing PubMed 11290414. This supports choice D, though the cited primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support inference of a phosphatase, but the exact EC requires knowing its substrate/reaction specificity; the supplied sequence and prompt do not establish that specificity.


**Missing item-specific fact**

> The protein-specific catalytic annotation or experimental characterization identifying this enzyme as a protein serine/threonine phosphatase (EC 3.1.3.16).


**Reason**

> Choosing the complete EC number depends on an item-specific function annotation or characterization absent from the input, rather than a sufficiently discriminating general biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only annotation supports D, and the listed alternatives correspond to different EC classifications; no evidence supplied supports another option for this sequence.


### Important caveats

- The current and archived UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.
- The UniProt functional annotation cites a publication; that primary evidence was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support inference of a phosphatase, but the exact EC requires knowing its substrate/reaction specificity; the supplied sequence and prompt do not establish that specificity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental characterization identifying this enzyme as a protein serine/threonine phosphatase (EC 3.1.3.16).",
    "reason": "Choosing the complete EC number depends on an item-specific function annotation or characterization absent from the input, rather than a sufficiently discriminating general biological argument."
  },
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q388N2, whose archived annotation assigns EC 3.1.3.16 and describes dephosphorylation of phosphoserine- and phosphothreonine-containing proteins, citing PubMed 11290414. This supports choice D, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The current and archived UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The UniProt functional annotation cites a publication; that primary evidence was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports D, and the listed alternatives correspond to different EC classifications; no evidence supplied supports another option for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q388N2, whose archived annotation assigns EC 3.1.3.16 and describes dephosphorylation of phosphoserine- and phosphothreonine-containing proteins, citing PubMed 11290414. This supports choice D, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support inference of a phosphatase, but the exact EC requires knowing its substrate/reaction specificity; the supplied sequence and prompt do not establish that specificity.",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental characterization identifying this enzyme as a protein serine/threonine phosphatase (EC 3.1.3.16).",
    "reason": "Choosing the complete EC number depends on an item-specific function annotation or characterization absent from the input, rather than a sufficiently discriminating general biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports D, and the listed alternatives correspond to different EC classifications; no evidence supplied supports another option for this sequence."
  },
  "important_caveats": [
    "The current and archived UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The UniProt functional annotation cites a publication; that primary evidence was not independently assessed."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q388N2 (PPP5_TRYB2, Trypanosoma brucei brucei) with identical SHA-256. The entry is annotated as Serine/threonine-protein phosphatase T with EC=3.1.3.16, supported by catalytic activity reactions (O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate and the threonyl equivalent). The evidence code is ECO:0000305 (curator inference) backed by PubMed:11290414 (Chaudhuri, 2001, Gene 266:1-13), a cloning and characterization paper. The annotation is a curator-assigned EC number based on sequence similarity to the PP5 family with experimental characterization in the reference, not a direct kinetic measurement, but it is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical PPP-family phosphatase catalytic motifs: GDTHGQ (GD…HG motif), EHGGKC (HGG motif), NGDFVDRGS (GDF motif), and HGGLYSSD. These are well-known, textbook hallmarks of the PPP superfamily of serine/threonine protein phosphatases (PP1, PP2A, PP5, PP7, etc.). Recognizing these motifs identifies the enzyme as a PPP-family protein phosphatase, which is classified under EC 3.1.3.16 (protein serine/threonine phosphatase). This eliminates B (5.3.1.8, an isomerase), C (2.7.7.80, a nucleotidyltransferase), and A (3.1.3.112, a lipid phosphatase acting on phosphatidylinositol phosphates, which lacks PPP-family motifs and belongs to a different structural class). The distinction between protein phosphatases (PPP motifs) and lipid phosphatases (e.g., PTEN/SH2-domain-containing phosphatases) is general biochemical knowledge.


**Missing item-specific fact**

> None critical. The PPP-family motifs are directly observable in the supplied sequence, and their association with EC 3.1.3.16 is standard biochemical knowledge.


**Reason**

> A model with knowledge of phosphatase superfamily architecture can identify the GD, HGG, and GDF motifs in the sequence and conclude the protein is a PPP-family serine/threonine protein phosphatase (EC 3.1.3.16), distinguishing it from the lipid phosphatase (3.1.3.112), isomerase (5.3.1.8), and transferase (2.7.7.80) options. This is general domain-knowledge reasoning, not item-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PPP-family motifs unambiguously indicate a serine/threonine protein phosphatase. Options B and C belong to entirely different EC classes (isomerase, transferase). Option A (3.1.3.112) is a lipid phosphatase with a completely different fold and no PPP motifs. Only D is consistent with the observed catalytic motifs.


### Important caveats

- The UniProt EC assignment uses evidence code ECO:0000305 (curator inference from sequence similarity to characterized PP5 homologs), supported by a 2001 cloning/characterization paper. It is not a direct experimental kinetic assay result, but the PPP-family assignment is robust.
- The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical) but was not available to the evaluated model.
- The model must recognize PPP-family motifs (GD, HGG, GDF) from the raw sequence without database access; this is feasible for a model trained on protein biochemistry but represents a non-trivial recognition task for less specialized models.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical PPP-family phosphatase catalytic motifs: GDTHGQ (GD…HG motif), EHGGKC (HGG motif), NGDFVDRGS (GDF motif), and HGGLYSSD. These are well-known, textbook hallmarks of the PPP superfamily of serine/threonine protein phosphatases (PP1, PP2A, PP5, PP7, etc.). Recognizing these motifs identifies the enzyme as a PPP-family protein phosphatase, which is classified under EC 3.1.3.16 (protein serine/threonine phosphatase). This eliminates B (5.3.1.8, an isomerase), C (2.7.7.80, a nucleotidyltransferase), and A (3.1.3.112, a lipid phosphatase acting on phosphatidylinositol phosphates, which lacks PPP-family motifs and belongs to a different structural class). The distinction between protein phosphatases (PPP motifs) and lipid phosphatases (e.g., PTEN/SH2-domain-containing phosphatases) is general biochemical knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PPP-family motifs are directly observable in the supplied sequence, and their association with EC 3.1.3.16 is standard biochemical knowledge.",
    "reason": "A model with knowledge of phosphatase superfamily architecture can identify the GD, HGG, and GDF motifs in the sequence and conclude the protein is a PPP-family serine/threonine protein phosphatase (EC 3.1.3.16), distinguishing it from the lipid phosphatase (3.1.3.112), isomerase (5.3.1.8), and transferase (2.7.7.80) options. This is general domain-knowledge reasoning, not item-specific lookup."
  },
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q388N2 (PPP5_TRYB2, Trypanosoma brucei brucei) with identical SHA-256. The entry is annotated as Serine/threonine-protein phosphatase T with EC=3.1.3.16, supported by catalytic activity reactions (O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate and the threonyl equivalent). The evidence code is ECO:0000305 (curator inference) backed by PubMed:11290414 (Chaudhuri, 2001, Gene 266:1-13), a cloning and characterization paper. The annotation is a curator-assigned EC number based on sequence similarity to the PP5 family with experimental characterization in the reference, not a direct kinetic measurement, but it is well-supported."
  },
  "important_caveats": [
    "The UniProt EC assignment uses evidence code ECO:0000305 (curator inference from sequence similarity to characterized PP5 homologs), supported by a 2001 cloning/characterization paper. It is not a direct experimental kinetic assay result, but the PPP-family assignment is robust.",
    "The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical) but was not available to the evaluated model.",
    "The model must recognize PPP-family motifs (GD, HGG, GDF) from the raw sequence without database access; this is feasible for a model trained on protein biochemistry but represents a non-trivial recognition task for less specialized models."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PPP-family motifs unambiguously indicate a serine/threonine protein phosphatase. Options B and C belong to entirely different EC classes (isomerase, transferase). Option A (3.1.3.112) is a lipid phosphatase with a completely different fold and no PPP motifs. Only D is consistent with the observed catalytic motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q388N2 (PPP5_TRYB2, Trypanosoma brucei brucei) with identical SHA-256. The entry is annotated as Serine/threonine-protein phosphatase T with EC=3.1.3.16, supported by catalytic activity reactions (O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate and the threonyl equivalent). The evidence code is ECO:0000305 (curator inference) backed by PubMed:11290414 (Chaudhuri, 2001, Gene 266:1-13), a cloning and characterization paper. The annotation is a curator-assigned EC number based on sequence similarity to the PP5 family with experimental characterization in the reference, not a direct kinetic measurement, but it is well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical PPP-family phosphatase catalytic motifs: GDTHGQ (GD…HG motif), EHGGKC (HGG motif), NGDFVDRGS (GDF motif), and HGGLYSSD. These are well-known, textbook hallmarks of the PPP superfamily of serine/threonine protein phosphatases (PP1, PP2A, PP5, PP7, etc.). Recognizing these motifs identifies the enzyme as a PPP-family protein phosphatase, which is classified under EC 3.1.3.16 (protein serine/threonine phosphatase). This eliminates B (5.3.1.8, an isomerase), C (2.7.7.80, a nucleotidyltransferase), and A (3.1.3.112, a lipid phosphatase acting on phosphatidylinositol phosphates, which lacks PPP-family motifs and belongs to a different structural class). The distinction between protein phosphatases (PPP motifs) and lipid phosphatases (e.g., PTEN/SH2-domain-containing phosphatases) is general biochemical knowledge.",
    "missing_item_specific_fact": "None critical. The PPP-family motifs are directly observable in the supplied sequence, and their association with EC 3.1.3.16 is standard biochemical knowledge.",
    "reason": "A model with knowledge of phosphatase superfamily architecture can identify the GD, HGG, and GDF motifs in the sequence and conclude the protein is a PPP-family serine/threonine protein phosphatase (EC 3.1.3.16), distinguishing it from the lipid phosphatase (3.1.3.112), isomerase (5.3.1.8), and transferase (2.7.7.80) options. This is general domain-knowledge reasoning, not item-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PPP-family motifs unambiguously indicate a serine/threonine protein phosphatase. Options B and C belong to entirely different EC classes (isomerase, transferase). Option A (3.1.3.112) is a lipid phosphatase with a completely different fold and no PPP motifs. Only D is consistent with the observed catalytic motifs."
  },
  "important_caveats": [
    "The UniProt EC assignment uses evidence code ECO:0000305 (curator inference from sequence similarity to characterized PP5 homologs), supported by a 2001 cloning/characterization paper. It is not a direct experimental kinetic assay result, but the PPP-family assignment is robust.",
    "The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical) but was not available to the evaluated model.",
    "The model must recognize PPP-family motifs (GD, HGG, GDF) from the raw sequence without database access; this is feasible for a model trained on protein biochemistry but represents a non-trivial recognition task for less specialized models."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched-sequence UniProt entry assigns EC 3.1.3.16 and describes dephosphorylation of protein serine and threonine residues. The annotation cites a characterization paper; this supports D, though the excerpts do not independently establish the experiments' details.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a protein phosphatase 5: an N-terminal alpha-helical repeat region followed by a conserved metal-dependent protein phosphatase catalytic domain, including characteristic catalytic-domain motifs. Family knowledge links this architecture to serine/threonine protein dephosphorylation, corresponding to EC 3.1.3.16 (D), rather than the isomerase or nucleotide-transferase alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the phosphatase family from transferable sequence and domain patterns meaningfully distinguishes D among these choices. This is a family-level inference, not proof of every substrate or activity detail for this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives classify substantially different reaction types, and the sequence-family inference favors only the protein serine/threonine phosphatase EC number.


### Important caveats

- The supporting database annotation is literature-cited and applies to a sequence-matched entry; the supplied excerpts do not provide the primary experimental data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a protein phosphatase 5: an N-terminal alpha-helical repeat region followed by a conserved metal-dependent protein phosphatase catalytic domain, including characteristic catalytic-domain motifs. Family knowledge links this architecture to serine/threonine protein dephosphorylation, corresponding to EC 3.1.3.16 (D), rather than the isomerase or nucleotide-transferase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the phosphatase family from transferable sequence and domain patterns meaningfully distinguishes D among these choices. This is a family-level inference, not proof of every substrate or activity detail for this particular protein."
  },
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt entry assigns EC 3.1.3.16 and describes dephosphorylation of protein serine and threonine residues. The annotation cites a characterization paper; this supports D, though the excerpts do not independently establish the experiments' details."
  },
  "important_caveats": [
    "The supporting database annotation is literature-cited and applies to a sequence-matched entry; the supplied excerpts do not provide the primary experimental data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives classify substantially different reaction types, and the sequence-family inference favors only the protein serine/threonine phosphatase EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt entry assigns EC 3.1.3.16 and describes dephosphorylation of protein serine and threonine residues. The annotation cites a characterization paper; this supports D, though the excerpts do not independently establish the experiments' details.",
    "evidence_ids": ["C4", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a protein phosphatase 5: an N-terminal alpha-helical repeat region followed by a conserved metal-dependent protein phosphatase catalytic domain, including characteristic catalytic-domain motifs. Family knowledge links this architecture to serine/threonine protein dephosphorylation, corresponding to EC 3.1.3.16 (D), rather than the isomerase or nucleotide-transferase alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the phosphatase family from transferable sequence and domain patterns meaningfully distinguishes D among these choices. This is a family-level inference, not proof of every substrate or activity detail for this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives classify substantially different reaction types, and the sequence-family inference favors only the protein serine/threonine phosphatase EC number."
  },
  "important_caveats": [
    "The supporting database annotation is literature-cited and applies to a sequence-matched entry; the supplied excerpts do not provide the primary experimental data."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q388N2 (sequence matched exactly) annotates this protein as Serine/threonine-protein phosphatase T (TbPP5) with EC 3.1.3.16, supported by experimental evidence (ECO:0000305, PubMed:11290414, Chaudhuri 2001). The catalytic activities listed are dephosphorylation of O-phospho-L-seryl-&#91;protein&#93; and O-phospho-L-threonyl-&#91;protein&#93;, both under EC 3.1.3.16. The evidence is from a primary characterization paper.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark GDxVHG-like motif of the PPP (phosphoprotein phosphatase) superfamily: 'GDFVDRGS' near the middle of the sequence and 'VVHGGL' further downstream, corresponding to the conserved GDxVHG catalytic motif. The PPP superfamily (PP1, PP2A, PP5, PP6, PP7) is specifically composed of serine/threonine protein phosphatases (EC 3.1.3.16) that use a binuclear metal center for catalysis. This distinguishes them from tyrosine phosphatases (which would correspond to EC 3.1.3.112), as PTP-family enzymes use a completely different cysteine-based catalytic mechanism with a CxxRxxG signature motif, which is absent here. Options B (EC 5.3.1.8, glucose-6-phosphate isomerase) and C (EC 2.7.7.80, nucleotidyltransferase) belong to entirely different EC classes (isomerase, transferase) and lack any phosphatase catalytic motifs. Thus, recognizing the PPP-family GDxVHG motif from general protein-family knowledge meaningfully distinguishes D (3.1.3.16) from A (3.1.3.112, tyrosine phosphatase) and eliminates B and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PPP superfamily GDxVHG motif is a well-established, transferable sequence signature shared across PP1, PP2A, PP5, and related Ser/Thr phosphatases. A knowledgeable model recognizing this motif can infer Ser/Thr phosphatase activity (EC 3.1.3.16) and exclude tyrosine phosphatases (different catalytic mechanism and motif), isomerases, and transferases without needing to recall this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (hydrolase, isomerase, transferase) and within hydrolases distinguish Ser/Thr vs. Tyr phosphatases. The PPP-family motif clearly points to Ser/Thr phosphatase, making D the uniquely defensible choice.


### Important caveats

- The GDxVHG motif in this sequence is a PP5-family variant (GDFVDRGS rather than the canonical GDxVHG of PP1/PP2A), but the key catalytic residues (G, D, V, H, G) are conserved, consistent with PPP superfamily membership.
- The evidence code ECO:0000305 indicates the EC assignment derives from the primary experimental paper (PubMed 11290414), not merely computational inference.
- EC 3.1.3.112 is a relatively obscure EC entry; its exact identity as a tyrosine phosphatase or other phosphatase subtype is assumed from general EC classification knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark GDxVHG-like motif of the PPP (phosphoprotein phosphatase) superfamily: 'GDFVDRGS' near the middle of the sequence and 'VVHGGL' further downstream, corresponding to the conserved GDxVHG catalytic motif. The PPP superfamily (PP1, PP2A, PP5, PP6, PP7) is specifically composed of serine/threonine protein phosphatases (EC 3.1.3.16) that use a binuclear metal center for catalysis. This distinguishes them from tyrosine phosphatases (which would correspond to EC 3.1.3.112), as PTP-family enzymes use a completely different cysteine-based catalytic mechanism with a CxxRxxG signature motif, which is absent here. Options B (EC 5.3.1.8, glucose-6-phosphate isomerase) and C (EC 2.7.7.80, nucleotidyltransferase) belong to entirely different EC classes (isomerase, transferase) and lack any phosphatase catalytic motifs. Thus, recognizing the PPP-family GDxVHG motif from general protein-family knowledge meaningfully distinguishes D (3.1.3.16) from A (3.1.3.112, tyrosine phosphatase) and eliminates B and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PPP superfamily GDxVHG motif is a well-established, transferable sequence signature shared across PP1, PP2A, PP5, and related Ser/Thr phosphatases. A knowledgeable model recognizing this motif can infer Ser/Thr phosphatase activity (EC 3.1.3.16) and exclude tyrosine phosphatases (different catalytic mechanism and motif), isomerases, and transferases without needing to recall this exact protein's database annotation."
  },
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q388N2 (sequence matched exactly) annotates this protein as Serine/threonine-protein phosphatase T (TbPP5) with EC 3.1.3.16, supported by experimental evidence (ECO:0000305, PubMed:11290414, Chaudhuri 2001). The catalytic activities listed are dephosphorylation of O-phospho-L-seryl-[protein] and O-phospho-L-threonyl-[protein], both under EC 3.1.3.16. The evidence is from a primary characterization paper."
  },
  "important_caveats": [
    "The GDxVHG motif in this sequence is a PP5-family variant (GDFVDRGS rather than the canonical GDxVHG of PP1/PP2A), but the key catalytic residues (G, D, V, H, G) are conserved, consistent with PPP superfamily membership.",
    "The evidence code ECO:0000305 indicates the EC assignment derives from the primary experimental paper (PubMed 11290414), not merely computational inference.",
    "EC 3.1.3.112 is a relatively obscure EC entry; its exact identity as a tyrosine phosphatase or other phosphatase subtype is assumed from general EC classification knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (hydrolase, isomerase, transferase) and within hydrolases distinguish Ser/Thr vs. Tyr phosphatases. The PPP-family motif clearly points to Ser/Thr phosphatase, making D the uniquely defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q388N2 (sequence matched exactly) annotates this protein as Serine/threonine-protein phosphatase T (TbPP5) with EC 3.1.3.16, supported by experimental evidence (ECO:0000305, PubMed:11290414, Chaudhuri 2001). The catalytic activities listed are dephosphorylation of O-phospho-L-seryl-[protein] and O-phospho-L-threonyl-[protein], both under EC 3.1.3.16. The evidence is from a primary characterization paper.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark GDxVHG-like motif of the PPP (phosphoprotein phosphatase) superfamily: 'GDFVDRGS' near the middle of the sequence and 'VVHGGL' further downstream, corresponding to the conserved GDxVHG catalytic motif. The PPP superfamily (PP1, PP2A, PP5, PP6, PP7) is specifically composed of serine/threonine protein phosphatases (EC 3.1.3.16) that use a binuclear metal center for catalysis. This distinguishes them from tyrosine phosphatases (which would correspond to EC 3.1.3.112), as PTP-family enzymes use a completely different cysteine-based catalytic mechanism with a CxxRxxG signature motif, which is absent here. Options B (EC 5.3.1.8, glucose-6-phosphate isomerase) and C (EC 2.7.7.80, nucleotidyltransferase) belong to entirely different EC classes (isomerase, transferase) and lack any phosphatase catalytic motifs. Thus, recognizing the PPP-family GDxVHG motif from general protein-family knowledge meaningfully distinguishes D (3.1.3.16) from A (3.1.3.112, tyrosine phosphatase) and eliminates B and C.",
    "missing_item_specific_fact": "",
    "reason": "The PPP superfamily GDxVHG motif is a well-established, transferable sequence signature shared across PP1, PP2A, PP5, and related Ser/Thr phosphatases. A knowledgeable model recognizing this motif can infer Ser/Thr phosphatase activity (EC 3.1.3.16) and exclude tyrosine phosphatases (different catalytic mechanism and motif), isomerases, and transferases without needing to recall this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (hydrolase, isomerase, transferase) and within hydrolases distinguish Ser/Thr vs. Tyr phosphatases. The PPP-family motif clearly points to Ser/Thr phosphatase, making D the uniquely defensible choice."
  },
  "important_caveats": [
    "The GDxVHG motif in this sequence is a PP5-family variant (GDFVDRGS rather than the canonical GDxVHG of PP1/PP2A), but the key catalytic residues (G, D, V, H, G) are conserved, consistent with PPP superfamily membership.",
    "The evidence code ECO:0000305 indicates the EC assignment derives from the primary experimental paper (PubMed 11290414), not merely computational inference.",
    "EC 3.1.3.112 is a relatively obscure EC entry; its exact identity as a tyrosine phosphatase or other phosphatase subtype is assumed from general EC classification knowledge."
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
  "requested_accession": "Q388N2",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "cc9358577e82c28a804de40071ec7b0e03104416e51a61cdb314664011a043f5",
  "benchmark_sequence_length": 472,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 116,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-11-22",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "current_source_sequence_sha256": "cc9358577e82c28a804de40071ec7b0e03104416e51a61cdb314664011a043f5",
  "current_source_sequence_length": 472,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 114,
  "selected_historical_version": {
    "accession": "Q388N2",
    "database": "Swiss-Prot",
    "entryVersion": 114,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PPP5_TRYB2",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "selected_historical_source_sequence_sha256": "cc9358577e82c28a804de40071ec7b0e03104416e51a61cdb314664011a043f5",
  "selected_historical_source_sequence_length": 472,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 114,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q388N2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":116,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-11-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008524\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Trypanosoma\"],\"scientificName\":\"Trypanosoma brucei brucei (strain 927/4 GUTat10.1)\",\"taxonId\":185431}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"value\":\"TbPP5\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"value\":\"3.1.3.16\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Serine/threonine-protein phosphatase T\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PPT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:20630\"}}],\"reaction\":{\"ecNumber\":\"3.1.3.16\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"name\":\"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:20629\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9863\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11604\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:83421\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:47005\"}}],\"reaction\":{\"ecNumber\":\"3.1.3.16\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"name\":\"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:47004\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11605\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30013\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61977\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Chaudhuri M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11290414\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0378-1119(01)00367-5\"}],\"citationType\":\"journal article\",\"firstPage\":\"1\",\"id\":\"11290414\",\"journal\":\"Gene\",\"lastPage\":\"13\",\"publicationDate\":\"2001\",\"title\":\"Cloning and characterization of a novel serine/threonine protein phosphatase type 5 from Trypanosoma brucei.\",\"volume\":\"266\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"LUMP 1026\"}],\"referenceNumber\":2,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   PPP5_TRYB2              Reviewed;         472 AA.\nAC   Q388N2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-NOV-2005, sequence version 1.\nDT   28-JAN-2026, entry version 114.\nDE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000305};\nDE            Short=PPT {ECO:0000305};\nDE            EC=3.1.3.16 {ECO:0000305|PubMed:11290414};\nDE   AltName: Full=TbPP5 {ECO:0000303|PubMed:11290414};\nGN   Name=PPT1 {ECO:0000305};\nGN   ORFNames=Tb10.05.0110 {ECO:0000312|EMBL:EAN78738.1};\nOS   Trypanosoma brucei brucei (strain 927/4 GUTat10.1).\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Trypanosoma.\nOX   NCBI_TaxID=185431 {ECO:0000312|Proteomes:UP000008524};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000305};\nDE            Short=PPT {ECO:0000305};\nDE            EC=3.1.3.16 {ECO:0000305|PubMed:11290414};\nDE   AltName: Full=TbPP5 {ECO:0000303|PubMed:11290414};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "source_locator": "lines 40-48",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   SUBCELLULAR LOCATION.\nRC   STRAIN=LUMP 1026 {ECO:0000303|PubMed:11290414};\nRX   PubMed=11290414; DOI=10.1016/s0378-1119(01)00367-5;\nRA   Chaudhuri M.;\nRT   \"Cloning and characterization of a novel serine/threonine protein\nRT   phosphatase type 5 from Trypanosoma brucei.\";\nRL   Gene 266:1-13(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "source_locator": "lines 51-58",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +\nCC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-\nCC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:83421; EC=3.1.3.16;\nCC         Evidence={ECO:0000305|PubMed:11290414};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;\nCC         Evidence={ECO:0000305|PubMed:11290414};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "source_locator": "lines 59-66",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +\nCC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-\nCC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:61977; EC=3.1.3.16;\nCC         Evidence={ECO:0000305|PubMed:11290414};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;\nCC         Evidence={ECO:0000305|PubMed:11290414};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 155. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
