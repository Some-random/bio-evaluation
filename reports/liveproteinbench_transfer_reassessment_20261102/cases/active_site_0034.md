# active_site_0034: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0034.txt)

**Task:** `active_site`  
**Author key, unchanged:** **C** — Position 143 (Proton donor)

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
MNPPPSLLDKAAIVTGGSRGIGAAIAIELARRGAHVLITYNTASHKAQLVAEEIQKLGRKATVVQASSTDREGPNRIVQAAVSQYGRIDIIVNNAGMADDCLLQDLTHEFWDRIMDVNLRLPAFLVQAALQHLGPAPRIVNISSLAARAGYNATSVYAASKAALEGMTRAWATELGHRYNVTVNCVNPGPVDTDIMAVDENTDAEVVAYWNAKVKETPAAPRVGTPGDIAQIVAFLCEEGSRWCTGSVVNANGGLVTV

[Multiple Choices]
A. Position 357 (For beta-ketoacyl synthase activity)
B. Position 1008 (Proton acceptor; for dehydratase activity 1)
C. Position 143 (Proton donor)
D. Position 27 (Proton acceptor)
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

> The exact input sequence matches the UniProt entry, which annotates position 143 as a proton donor. This annotation is transferred by similarity from UniProtKB:O93868 (ECO:0000250), not shown here as a direct experimental determination for this protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is 258 residues long, so positions 357 and 1008 are out of range; position 27 is isoleucine, making the proposed proton-acceptor role implausible. But these eliminations do not establish that position 143 is a proton donor.


**Missing item-specific fact**

> The identity and catalytic role of the specific residue at position 143, which the annotation assigns by similarity to a homolog.


**Reason**

> The sequence alone does not establish the precise catalytic role at position 143. Selecting C requires protein-specific annotation or comparable homology knowledge, rather than general reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, C is the only one supported by the supplied reviewer-only annotation; A and B give positions beyond the sequence length, and D assigns a proton-acceptor role to an isoleucine.


### Important caveats

- The matching annotation also assigns a proton-donor role to position 144, which is not offered as a choice.
- The cited evidence is a similarity-based annotation, not evidence of direct experimental verification for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 258 residues long, so positions 357 and 1008 are out of range; position 27 is isoleucine, making the proposed proton-acceptor role implausible. But these eliminations do not establish that position 143 is a proton donor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity and catalytic role of the specific residue at position 143, which the annotation assigns by similarity to a homolog.",
    "reason": "The sequence alone does not establish the precise catalytic role at position 143. Selecting C requires protein-specific annotation or comparable homology knowledge, rather than general reasoning from the provided input."
  },
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact input sequence matches the UniProt entry, which annotates position 143 as a proton donor. This annotation is transferred by similarity from UniProtKB:O93868 (ECO:0000250), not shown here as a direct experimental determination for this protein."
  },
  "important_caveats": [
    "The matching annotation also assigns a proton-donor role to position 144, which is not offered as a choice.",
    "The cited evidence is a similarity-based annotation, not evidence of direct experimental verification for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, C is the only one supported by the supplied reviewer-only annotation; A and B give positions beyond the sequence length, and D assigns a proton-acceptor role to an isoleucine."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact input sequence matches the UniProt entry, which annotates position 143 as a proton donor. This annotation is transferred by similarity from UniProtKB:O93868 (ECO:0000250), not shown here as a direct experimental determination for this protein.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is 258 residues long, so positions 357 and 1008 are out of range; position 27 is isoleucine, making the proposed proton-acceptor role implausible. But these eliminations do not establish that position 143 is a proton donor.",
    "missing_item_specific_fact": "The identity and catalytic role of the specific residue at position 143, which the annotation assigns by similarity to a homolog.",
    "reason": "The sequence alone does not establish the precise catalytic role at position 143. Selecting C requires protein-specific annotation or comparable homology knowledge, rather than general reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, C is the only one supported by the supplied reviewer-only annotation; A and B give positions beyond the sequence length, and D assigns a proton-acceptor role to an isoleucine."
  },
  "important_caveats": [
    "The matching annotation also assigns a proton-donor role to position 144, which is not offered as a choice.",
    "The cited evidence is a similarity-based annotation, not evidence of direct experimental verification for this exact protein."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7T8F1N2 (FRZI_CLASX, 258 aa, sequence matched) annotates position 143 as an Active site with description 'Proton donor' (evidence ECO:0000250, similarity transfer from O93868). This is confirmed in both the current entry (C5) and the historical archived version 16 (H3). The expected answer C (Position 143, Proton donor) matches the database annotation exactly. However, the evidence code ECO:0000250 indicates computational similarity-based transfer, not direct experimental validation for this specific protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 258 residues long, immediately eliminating options A (position 357) and B (position 1008) as beyond the sequence length. Between the remaining options, position 27 is Ile (a hydrophobic, non-catalytic residue) while position 143 is Ser. The sequence contains recognizable SDR (short-chain dehydrogenase/reductase) features: a Rossmann-fold NAD(P)-binding motif near the N-terminus (TGxxxGxG around residues 16-24) and a catalytic triad region (Ser-Tyr-Lys) around residues 143-161. Knowledge that SDR catalytic triads involve Ser (~140-145), Tyr (~150-160), and Lys (~155-165) allows identification of position 143 (Ser) as the catalytic residue, while position 27 (Ile) has no plausible catalytic role. The 'Proton donor' label for Ser is consistent with Ser's role in the SDR proton-relay mechanism.


**Missing item-specific fact**

> None critical. The specific assignment of 'Proton donor' to Ser (rather than the more commonly described 'proton acceptor' role for Ser in canonical SDR oxidation) follows a particular annotation convention, but the primary discrimination (Ser at 143 vs Ile at 27) is achievable through general SDR biochemistry knowledge.


**Reason**

> Two of four options are trivially eliminable by protein length. The remaining choice between Ile-27 and Ser-143 is resolvable through general knowledge of SDR catalytic triads and the recognition of SDR sequence signatures. The specific proton-donor/acceptor labeling adds minor complexity but does not require item-specific lookup to identify the correct position.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B reference positions (357, 1008) far exceeding the 258-residue protein, making them unambiguously incorrect. Option D (position 27, Ile) is not a plausible catalytic residue. Only option C (position 143, Ser) corresponds to a residue within the SDR catalytic triad. No genuine ambiguity exists among the choices.


### Important caveats

- The active-site annotation at position 143 is based on similarity transfer (ECO:0000250 to O93868), not direct experimental measurement on this protein.
- The 'Proton donor' label for Ser at position 143 is somewhat counterintuitive relative to the most commonly described SDR mechanism where Tyr is the proton donor to the substrate; however, this reflects a specific annotation convention (Ser donating a proton to the catalytic Tyr during the catalytic cycle).
- The protein identity (FrzI, a short-chain dehydrogenase/reductase in FR901483 biosynthesis) was not provided to the evaluated model; recognition relies on sequence-level SDR motif identification.
- The annotation also lists position 144 as a second 'Proton donor' and position 157 as 'Proton acceptor' (Tyr), but these are not offered as alternative options, so they do not create ambiguity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 258 residues long, immediately eliminating options A (position 357) and B (position 1008) as beyond the sequence length. Between the remaining options, position 27 is Ile (a hydrophobic, non-catalytic residue) while position 143 is Ser. The sequence contains recognizable SDR (short-chain dehydrogenase/reductase) features: a Rossmann-fold NAD(P)-binding motif near the N-terminus (TGxxxGxG around residues 16-24) and a catalytic triad region (Ser-Tyr-Lys) around residues 143-161. Knowledge that SDR catalytic triads involve Ser (~140-145), Tyr (~150-160), and Lys (~155-165) allows identification of position 143 (Ser) as the catalytic residue, while position 27 (Ile) has no plausible catalytic role. The 'Proton donor' label for Ser is consistent with Ser's role in the SDR proton-relay mechanism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific assignment of 'Proton donor' to Ser (rather than the more commonly described 'proton acceptor' role for Ser in canonical SDR oxidation) follows a particular annotation convention, but the primary discrimination (Ser at 143 vs Ile at 27) is achievable through general SDR biochemistry knowledge.",
    "reason": "Two of four options are trivially eliminable by protein length. The remaining choice between Ile-27 and Ser-143 is resolvable through general knowledge of SDR catalytic triads and the recognition of SDR sequence signatures. The specific proton-donor/acceptor labeling adds minor complexity but does not require item-specific lookup to identify the correct position."
  },
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7T8F1N2 (FRZI_CLASX, 258 aa, sequence matched) annotates position 143 as an Active site with description 'Proton donor' (evidence ECO:0000250, similarity transfer from O93868). This is confirmed in both the current entry (C5) and the historical archived version 16 (H3). The expected answer C (Position 143, Proton donor) matches the database annotation exactly. However, the evidence code ECO:0000250 indicates computational similarity-based transfer, not direct experimental validation for this specific protein."
  },
  "important_caveats": [
    "The active-site annotation at position 143 is based on similarity transfer (ECO:0000250 to O93868), not direct experimental measurement on this protein.",
    "The 'Proton donor' label for Ser at position 143 is somewhat counterintuitive relative to the most commonly described SDR mechanism where Tyr is the proton donor to the substrate; however, this reflects a specific annotation convention (Ser donating a proton to the catalytic Tyr during the catalytic cycle).",
    "The protein identity (FrzI, a short-chain dehydrogenase/reductase in FR901483 biosynthesis) was not provided to the evaluated model; recognition relies on sequence-level SDR motif identification.",
    "The annotation also lists position 144 as a second 'Proton donor' and position 157 as 'Proton acceptor' (Tyr), but these are not offered as alternative options, so they do not create ambiguity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B reference positions (357, 1008) far exceeding the 258-residue protein, making them unambiguously incorrect. Option D (position 27, Ile) is not a plausible catalytic residue. Only option C (position 143, Ser) corresponds to a residue within the SDR catalytic triad. No genuine ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7T8F1N2 (FRZI_CLASX, 258 aa, sequence matched) annotates position 143 as an Active site with description 'Proton donor' (evidence ECO:0000250, similarity transfer from O93868). This is confirmed in both the current entry (C5) and the historical archived version 16 (H3). The expected answer C (Position 143, Proton donor) matches the database annotation exactly. However, the evidence code ECO:0000250 indicates computational similarity-based transfer, not direct experimental validation for this specific protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 258 residues long, immediately eliminating options A (position 357) and B (position 1008) as beyond the sequence length. Between the remaining options, position 27 is Ile (a hydrophobic, non-catalytic residue) while position 143 is Ser. The sequence contains recognizable SDR (short-chain dehydrogenase/reductase) features: a Rossmann-fold NAD(P)-binding motif near the N-terminus (TGxxxGxG around residues 16-24) and a catalytic triad region (Ser-Tyr-Lys) around residues 143-161. Knowledge that SDR catalytic triads involve Ser (~140-145), Tyr (~150-160), and Lys (~155-165) allows identification of position 143 (Ser) as the catalytic residue, while position 27 (Ile) has no plausible catalytic role. The 'Proton donor' label for Ser is consistent with Ser's role in the SDR proton-relay mechanism.",
    "missing_item_specific_fact": "None critical. The specific assignment of 'Proton donor' to Ser (rather than the more commonly described 'proton acceptor' role for Ser in canonical SDR oxidation) follows a particular annotation convention, but the primary discrimination (Ser at 143 vs Ile at 27) is achievable through general SDR biochemistry knowledge.",
    "reason": "Two of four options are trivially eliminable by protein length. The remaining choice between Ile-27 and Ser-143 is resolvable through general knowledge of SDR catalytic triads and the recognition of SDR sequence signatures. The specific proton-donor/acceptor labeling adds minor complexity but does not require item-specific lookup to identify the correct position."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B reference positions (357, 1008) far exceeding the 258-residue protein, making them unambiguously incorrect. Option D (position 27, Ile) is not a plausible catalytic residue. Only option C (position 143, Ser) corresponds to a residue within the SDR catalytic triad. No genuine ambiguity exists among the choices."
  },
  "important_caveats": [
    "The active-site annotation at position 143 is based on similarity transfer (ECO:0000250 to O93868), not direct experimental measurement on this protein.",
    "The 'Proton donor' label for Ser at position 143 is somewhat counterintuitive relative to the most commonly described SDR mechanism where Tyr is the proton donor to the substrate; however, this reflects a specific annotation convention (Ser donating a proton to the catalytic Tyr during the catalytic cycle).",
    "The protein identity (FrzI, a short-chain dehydrogenase/reductase in FR901483 biosynthesis) was not provided to the evaluated model; recognition relies on sequence-level SDR motif identification.",
    "The annotation also lists position 144 as a second 'Proton donor' and position 157 as 'Proton acceptor' (Tyr), but these are not offered as alternative options, so they do not create ambiguity."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies position 143 as a proton donor. This is a similarity-based annotation, not direct experimental verification in the supplied evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 258-residue sequence has an N-terminal TGxxGxG-like motif characteristic of the cofactor-binding region of short-chain dehydrogenase/reductases, and contains Ser at position 143 alongside a TyrxxxLys motif consistent with the conserved SDR catalytic machinery. Position 27 is Ile, while positions 357 and 1008 are outside the sequence. Transferable SDR family knowledge therefore gives a meaningful basis for choosing C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features distinguish the offered option without needing to recall this exact protein's database record. The inference is credible, though it does not independently prove the precise catalytic role experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, only C gives an in-range position with a plausible catalytic residue and role.


### Important caveats

- The supporting annotation is inferred by similarity to another protein rather than shown here to be experimentally measured for this sequence.
- A separate annotation also assigns proton-donor activity to position 144, but that position is not an offered choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 258-residue sequence has an N-terminal TGxxGxG-like motif characteristic of the cofactor-binding region of short-chain dehydrogenase/reductases, and contains Ser at position 143 alongside a TyrxxxLys motif consistent with the conserved SDR catalytic machinery. Position 27 is Ile, while positions 357 and 1008 are outside the sequence. Transferable SDR family knowledge therefore gives a meaningful basis for choosing C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features distinguish the offered option without needing to recall this exact protein's database record. The inference is credible, though it does not independently prove the precise catalytic role experimentally."
  },
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 143 as a proton donor. This is a similarity-based annotation, not direct experimental verification in the supplied evidence."
  },
  "important_caveats": [
    "The supporting annotation is inferred by similarity to another protein rather than shown here to be experimentally measured for this sequence.",
    "A separate annotation also assigns proton-donor activity to position 144, but that position is not an offered choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only C gives an in-range position with a plausible catalytic residue and role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 143 as a proton donor. This is a similarity-based annotation, not direct experimental verification in the supplied evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 258-residue sequence has an N-terminal TGxxGxG-like motif characteristic of the cofactor-binding region of short-chain dehydrogenase/reductases, and contains Ser at position 143 alongside a TyrxxxLys motif consistent with the conserved SDR catalytic machinery. Position 27 is Ile, while positions 357 and 1008 are outside the sequence. Transferable SDR family knowledge therefore gives a meaningful basis for choosing C.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features distinguish the offered option without needing to recall this exact protein's database record. The inference is credible, though it does not independently prove the precise catalytic role experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only C gives an in-range position with a plausible catalytic residue and role."
  },
  "important_caveats": [
    "The supporting annotation is inferred by similarity to another protein rather than shown here to be experimentally measured for this sequence.",
    "A separate annotation also assigns proton-donor activity to position 144, but that position is not an offered choice."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (evidence C5/H3) explicitly lists Position 143 as 'Proton donor' active site. The evidence code ECO:0000250 indicates this is inferred by similarity to O93868 (another SDR), not direct experimental evidence for this exact protein. However, the annotation is consistent with the well-established SDR catalytic tetrad (S-S-Y-K) and the sequence context (Ser at 143, Ser at 144, Tyr at 157, Lys at 161). The answer is supported by the database annotation, albeit as a computational/similarity-based assignment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [C7](#evidence-c7), [H5](#evidence-h5), [C8](#evidence-c8), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A (position 357) and B (position 1008) are immediately eliminated because the protein is only 258 residues long—these positions do not exist. Between C (position 143, Proton donor) and D (position 27, Proton acceptor): Position 27 in the sequence is Isoleucine (I), which has no ionizable side chain and cannot function as a proton acceptor in enzyme catalysis. Position 143 is Serine (S), a canonical catalytic residue. Furthermore, the N-terminal region contains the SDR-family Rossmann-fold motif TGxxxGG (TGSRGIG at positions 16-22), identifying this as a short-chain dehydrogenase/reductase. SDR enzymes universally employ a catalytic tetrad (Ser-Tyr-Lys) located in the C-terminal half of the protein. The Ser at 143, Tyr at 157, and Lys at 161 match this conserved SDR catalytic architecture. A model recognizing the SDR family from the TGxxxGG motif and knowing the conserved catalytic tetrad positions would confidently select C over D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of A and B relies on protein length (trivially derivable from the input). The elimination of D relies on recognizing that Isoleucine cannot be a proton acceptor—a basic biochemistry fact. The positive identification of C relies on recognizing the SDR family signature (TGxxxGG Rossmann motif) and the conserved S-Y-K catalytic tetrad, which are well-known transferable features across the SDR superfamily. No target-specific memorization is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are impossible (positions exceed protein length). Option D is biochemically nonsensical (Isoleucine cannot be a proton acceptor). Only C is consistent with both the sequence and SDR family catalytic architecture.


### Important caveats

- The UniProt annotation for position 143 carries evidence code ECO:0000250 (inferred by similarity to O93868), not direct experimental evidence for this specific protein. The annotation is a computational transfer within the SDR family.
- Options A and B appear to be distractors drawn from an entirely different protein (possibly a fatty acid synthase or dehydratase with >1000 residues), making them trivially eliminable.
- The SDR catalytic tetrad assignment (S143/S144-Y157-K161) is a family-level inference; individual SDR members may show variation in which Ser of the pair acts as the primary proton donor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A (position 357) and B (position 1008) are immediately eliminated because the protein is only 258 residues long—these positions do not exist. Between C (position 143, Proton donor) and D (position 27, Proton acceptor): Position 27 in the sequence is Isoleucine (I), which has no ionizable side chain and cannot function as a proton acceptor in enzyme catalysis. Position 143 is Serine (S), a canonical catalytic residue. Furthermore, the N-terminal region contains the SDR-family Rossmann-fold motif TGxxxGG (TGSRGIG at positions 16-22), identifying this as a short-chain dehydrogenase/reductase. SDR enzymes universally employ a catalytic tetrad (Ser-Tyr-Lys) located in the C-terminal half of the protein. The Ser at 143, Tyr at 157, and Lys at 161 match this conserved SDR catalytic architecture. A model recognizing the SDR family from the TGxxxGG motif and knowing the conserved catalytic tetrad positions would confidently select C over D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A and B relies on protein length (trivially derivable from the input). The elimination of D relies on recognizing that Isoleucine cannot be a proton acceptor—a basic biochemistry fact. The positive identification of C relies on recognizing the SDR family signature (TGxxxGG Rossmann motif) and the conserved S-Y-K catalytic tetrad, which are well-known transferable features across the SDR superfamily. No target-specific memorization is needed."
  },
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4",
      "C7",
      "H5",
      "C8",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5/H3) explicitly lists Position 143 as 'Proton donor' active site. The evidence code ECO:0000250 indicates this is inferred by similarity to O93868 (another SDR), not direct experimental evidence for this exact protein. However, the annotation is consistent with the well-established SDR catalytic tetrad (S-S-Y-K) and the sequence context (Ser at 143, Ser at 144, Tyr at 157, Lys at 161). The answer is supported by the database annotation, albeit as a computational/similarity-based assignment."
  },
  "important_caveats": [
    "The UniProt annotation for position 143 carries evidence code ECO:0000250 (inferred by similarity to O93868), not direct experimental evidence for this specific protein. The annotation is a computational transfer within the SDR family.",
    "Options A and B appear to be distractors drawn from an entirely different protein (possibly a fatty acid synthase or dehydratase with >1000 residues), making them trivially eliminable.",
    "The SDR catalytic tetrad assignment (S143/S144-Y157-K161) is a family-level inference; individual SDR members may show variation in which Ser of the pair acts as the primary proton donor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are impossible (positions exceed protein length). Option D is biochemically nonsensical (Isoleucine cannot be a proton acceptor). Only C is consistent with both the sequence and SDR family catalytic architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5/H3) explicitly lists Position 143 as 'Proton donor' active site. The evidence code ECO:0000250 indicates this is inferred by similarity to O93868 (another SDR), not direct experimental evidence for this exact protein. However, the annotation is consistent with the well-established SDR catalytic tetrad (S-S-Y-K) and the sequence context (Ser at 143, Ser at 144, Tyr at 157, Lys at 161). The answer is supported by the database annotation, albeit as a computational/similarity-based assignment.",
    "evidence_ids": ["C5", "H3", "C6", "H4", "C7", "H5", "C8", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A (position 357) and B (position 1008) are immediately eliminated because the protein is only 258 residues long—these positions do not exist. Between C (position 143, Proton donor) and D (position 27, Proton acceptor): Position 27 in the sequence is Isoleucine (I), which has no ionizable side chain and cannot function as a proton acceptor in enzyme catalysis. Position 143 is Serine (S), a canonical catalytic residue. Furthermore, the N-terminal region contains the SDR-family Rossmann-fold motif TGxxxGG (TGSRGIG at positions 16-22), identifying this as a short-chain dehydrogenase/reductase. SDR enzymes universally employ a catalytic tetrad (Ser-Tyr-Lys) located in the C-terminal half of the protein. The Ser at 143, Tyr at 157, and Lys at 161 match this conserved SDR catalytic architecture. A model recognizing the SDR family from the TGxxxGG motif and knowing the conserved catalytic tetrad positions would confidently select C over D.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A and B relies on protein length (trivially derivable from the input). The elimination of D relies on recognizing that Isoleucine cannot be a proton acceptor—a basic biochemistry fact. The positive identification of C relies on recognizing the SDR family signature (TGxxxGG Rossmann motif) and the conserved S-Y-K catalytic tetrad, which are well-known transferable features across the SDR superfamily. No target-specific memorization is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are impossible (positions exceed protein length). Option D is biochemically nonsensical (Isoleucine cannot be a proton acceptor). Only C is consistent with both the sequence and SDR family catalytic architecture."
  },
  "important_caveats": [
    "The UniProt annotation for position 143 carries evidence code ECO:0000250 (inferred by similarity to O93868), not direct experimental evidence for this specific protein. The annotation is a computational transfer within the SDR family.",
    "Options A and B appear to be distractors drawn from an entirely different protein (possibly a fatty acid synthase or dehydratase with >1000 residues), making them trivially eliminable.",
    "The SDR catalytic tetrad assignment (S143/S144-Y157-K161) is a family-level inference; individual SDR members may show variation in which Ser of the pair acts as the primary proton donor."
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
  "requested_accession": "A0A7T8F1N2",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "900848c2f83044ac5f5a81d57e8b7d27cd6bc66d8b0cdb266bed700cbb1522de",
  "benchmark_sequence_length": 258,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "current_source_sequence_sha256": "900848c2f83044ac5f5a81d57e8b7d27cd6bc66d8b0cdb266bed700cbb1522de",
  "current_source_sequence_length": 258,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 16,
  "selected_historical_version": {
    "accession": "A0A7T8F1N2",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZI_CLASX",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "selected_historical_source_sequence_sha256": "900848c2f83044ac5f5a81d57e8b7d27cd6bc66d8b0cdb266bed700cbb1522de",
  "selected_historical_source_sequence_length": 258,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 16,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A7T8F1N2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis clusters protein I\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Short-chain dehydrogenase/reductase FrzI\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":143},\"start\":{\"modifier\":\"EXACT\",\"value\":143}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":144},\"start\":{\"modifier\":\"EXACT\",\"value\":144}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10001\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":157},\"start\":{\"modifier\":\"EXACT\",\"value\":157}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Lowers pKa of active site Tyr\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":161},\"start\":{\"modifier\":\"EXACT\",\"value\":161}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":21},\"start\":{\"modifier\":\"EXACT\",\"value\":21}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":41},\"start\":{\"modifier\":\"EXACT\",\"value\":41}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":94},\"start\":{\"modifier\":\"EXACT\",\"value\":94}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":157},\"start\":{\"modifier\":\"EXACT\",\"value\":157}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":161},\"start\":{\"modifier\":\"EXACT\",\"value\":161}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":191},\"start\":{\"modifier\":\"EXACT\",\"value\":191}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":193}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   FRZI_CLASX              Reviewed;         258 AA.\nAC   A0A7T8F1N2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=Short-chain dehydrogenase/reductase FrzI {ECO:0000303|PubMed:33372776};\nDE            EC=1.1.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis clusters protein I {ECO:0000303|PubMed:33372776};\nGN   Name=FrzI {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 14-22",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 93-95",
  "excerpt": "FT   ACT_SITE        143\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 96-98",
  "excerpt": "FT   ACT_SITE        144\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 99-101",
  "excerpt": "FT   ACT_SITE        157\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU10001\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 102-104",
  "excerpt": "FT   ACT_SITE        161\nFT                   /note=\"Lowers pKa of active site Tyr\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 105-108",
  "excerpt": "FT   BINDING         21\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 109-112",
  "excerpt": "FT   BINDING         41\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 113-116",
  "excerpt": "FT   BINDING         94\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 117-120",
  "excerpt": "FT   BINDING         157\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 121-124",
  "excerpt": "FT   BINDING         161\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 125-128",
  "excerpt": "FT   BINDING         191\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "source_locator": "lines 129-132",
  "excerpt": "FT   BINDING         193\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
