# active_site_0009: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0009.txt)

**Task:** `active_site`  
**Author key, unchanged:** **D** — Position 154 (Acyl-thioester intermediate)

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
MSTPSKKRCGVLGATGAVGTRFILLLEQSPLLELVAVGASERSAGKKYRDAVRWKQASPMPASVADLTVRRCAPSEFSDCDIIFSGLDPVAAGDIEMAFLKANFAVFSNAKNYRLDPIVPLVVPLVNAGHIDVIPAQRKHYGLDKGLIVCNSNCAVVGLVIPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPFIPGEEGKIATESRKILGNLNPDLAGFSDQQPLQVSVACNRVPVLDGHTVCASLRFVNRPAPTASQVRDALREYKSEVQLLGCPSAPRQAIHVLDDVDRPQPRLDRDTEAGYACSVGRIREDDSGVFDIQFVALSHNTVLGASGSSILNAESAILKGYI

[Multiple Choices]
A. Position 148 (Proton acceptor)
B. Position 159 (Proton donor)
C. Position 308 (Proton acceptor)
D. Position 154 (Acyl-thioester intermediate)
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

> The sequence-matched UniProt annotation assigns position 154 the active-site role “Acyl-thioester intermediate,” supporting D. This annotation is computationally inferred from a PIRSR rule, not direct experimental evidence for this residue.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Position 154 is cysteine, whose thiol can form an acyl-thioester intermediate, making D biochemically plausible and less plausible than the hydrophobic residues at positions 148 and 159 for the stated proton-transfer roles.


**Missing item-specific fact**

> The input does not establish that this particular enzyme uses Cys154 as its catalytic thioester-forming residue, nor resolve whether the Asp at position 308 has the stated proton-acceptor role; that requires enzyme-specific mechanism or active-site annotation.


**Reason**

> Residue chemistry provides a useful clue but does not by itself establish which listed position is an active-site residue. Selecting the annotated catalytic position depends on a protein-specific fact absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence alone leaves the precise active-site assignment underdetermined, but the reviewer evidence supports D and does not support another listed option as the correct annotated answer.


### Important caveats

- The sequence matches the cited UniProt record, but the exact source snapshot used by the question author is unknown.
- The supporting active-site annotation is computationally inferred; it should not be described as experimentally established by the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Position 154 is cysteine, whose thiol can form an acyl-thioester intermediate, making D biochemically plausible and less plausible than the hydrophobic residues at positions 148 and 159 for the stated proton-transfer roles.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The input does not establish that this particular enzyme uses Cys154 as its catalytic thioester-forming residue, nor resolve whether the Asp at position 308 has the stated proton-acceptor role; that requires enzyme-specific mechanism or active-site annotation.",
    "reason": "Residue chemistry provides a useful clue but does not by itself establish which listed position is an active-site residue. Selecting the annotated catalytic position depends on a protein-specific fact absent from the question."
  },
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 154 the active-site role “Acyl-thioester intermediate,” supporting D. This annotation is computationally inferred from a PIRSR rule, not direct experimental evidence for this residue."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the exact source snapshot used by the question author is unknown.",
    "The supporting active-site annotation is computationally inferred; it should not be described as experimentally established by the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone leaves the precise active-site assignment underdetermined, but the reviewer evidence supports D and does not support another listed option as the correct annotated answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 154 the active-site role “Acyl-thioester intermediate,” supporting D. This annotation is computationally inferred from a PIRSR rule, not direct experimental evidence for this residue.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Position 154 is cysteine, whose thiol can form an acyl-thioester intermediate, making D biochemically plausible and less plausible than the hydrophobic residues at positions 148 and 159 for the stated proton-transfer roles.",
    "missing_item_specific_fact": "The input does not establish that this particular enzyme uses Cys154 as its catalytic thioester-forming residue, nor resolve whether the Asp at position 308 has the stated proton-acceptor role; that requires enzyme-specific mechanism or active-site annotation.",
    "reason": "Residue chemistry provides a useful clue but does not by itself establish which listed position is an active-site residue. Selecting the annotated catalytic position depends on a protein-specific fact absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone leaves the precise active-site assignment underdetermined, but the reviewer evidence supports D and does not support another listed option as the correct annotated answer."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the exact source snapshot used by the question author is unknown.",
    "The supporting active-site annotation is computationally inferred; it should not be described as experimentally established by the supplied evidence."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A179UL48 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Blastomyces gilchristii, 362 aa, sequence matched) annotates position 154 as an active site forming an 'Acyl-thioester intermediate' (evidence ECO:0000255|PIRSR:PIRSR000148-1, i.e. pro-rule/similarity-based inference). The supplied sequence at position 154 is indeed Cys (C), consistent with the well-established ASADH catalytic mechanism in which a catalytic cysteine forms the acyl-thioester intermediate. The companion proton-acceptor active site is annotated at position 251 (His), not at any of the distractor positions. The annotation is computational (PIRSR) rather than directly experimentally validated on this ortholog, but the Cys-His dyad mechanism is a hallmark of the ASADH family and is corroborated by X-ray structures (PDB 6C8W) of this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The amino-acid identities at the four candidate positions, read directly from the supplied sequence, eliminate three of the four options on purely chemical grounds: position 148 is Ile (cannot serve as a proton acceptor), position 159 is Leu (cannot serve as a proton donor), and position 308 is Asp (not the catalytic proton acceptor in the ASADH Cys-His dyad; the actual proton acceptor is His-251). Only position 154 is a Cys, and formation of an acyl-thioester intermediate requires a thiol nucleophile, a property unique to cysteine among the standard amino acids. Thus, even without knowing the exact protein identity, a model applying general biochemistry (thioester chemistry requires Cys; Ile and Leu lack ionizable side chains suitable for proton transfer) can single out D.


**Missing item-specific fact**

> None essential. Recognizing the protein as ASADH would confirm the Cys-His dyad mechanism, but the chemical logic of thioester formation from a cysteine thiol is sufficient to distinguish the correct answer from the distractors given the residue identities visible in the sequence.


**Reason**

> The question supplies the full sequence, so the model can count to each candidate position and read the residue type. General biochemical knowledge (only Cys forms thioesters; Ile and Leu are non-polar aliphatic residues incapable of proton transfer; the catalytic proton acceptor in a dehydrogenase acting via a thioester intermediate is typically His, not Asp at a distant position) meaningfully separates the four choices without requiring recall of a specific database annotation for this ortholog.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor assigns a catalytic role to an amino acid that is chemically incapable of performing that role (Ile as proton acceptor, Leu as proton donor, Asp at a non-catalytic position as the proton acceptor). Only Cys-154 can form an acyl-thioester intermediate. The options are cleanly distinguishable.


### Important caveats

- The active-site annotation carries evidence code ECO:0000255 (by similarity / PIRSR pro-rule), meaning it is a computational/pro-rule inference transferred from the ASADH family pattern, not a site-directed mutagenesis or kinetic measurement on this specific Blastomyces ortholog.
- The UniProt entry was first released in February 2025 (sequence version 2); the author's construction snapshot is unknown, though the sequence matches the current and historical (entry v26) records.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning-supported judgment rests solely on information present in the original question (sequence + choices).
- The question lists a single residue per option rather than the full catalytic dyad (Cys-154 + His-251); this is a simplification but does not create ambiguity among the four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The amino-acid identities at the four candidate positions, read directly from the supplied sequence, eliminate three of the four options on purely chemical grounds: position 148 is Ile (cannot serve as a proton acceptor), position 159 is Leu (cannot serve as a proton donor), and position 308 is Asp (not the catalytic proton acceptor in the ASADH Cys-His dyad; the actual proton acceptor is His-251). Only position 154 is a Cys, and formation of an acyl-thioester intermediate requires a thiol nucleophile, a property unique to cysteine among the standard amino acids. Thus, even without knowing the exact protein identity, a model applying general biochemistry (thioester chemistry requires Cys; Ile and Leu lack ionizable side chains suitable for proton transfer) can single out D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None essential. Recognizing the protein as ASADH would confirm the Cys-His dyad mechanism, but the chemical logic of thioester formation from a cysteine thiol is sufficient to distinguish the correct answer from the distractors given the residue identities visible in the sequence.",
    "reason": "The question supplies the full sequence, so the model can count to each candidate position and read the residue type. General biochemical knowledge (only Cys forms thioesters; Ile and Leu are non-polar aliphatic residues incapable of proton transfer; the catalytic proton acceptor in a dehydrogenase acting via a thioester intermediate is typically His, not Asp at a distant position) meaningfully separates the four choices without requiring recall of a specific database annotation for this ortholog."
  },
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H4",
      "H5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A179UL48 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Blastomyces gilchristii, 362 aa, sequence matched) annotates position 154 as an active site forming an 'Acyl-thioester intermediate' (evidence ECO:0000255|PIRSR:PIRSR000148-1, i.e. pro-rule/similarity-based inference). The supplied sequence at position 154 is indeed Cys (C), consistent with the well-established ASADH catalytic mechanism in which a catalytic cysteine forms the acyl-thioester intermediate. The companion proton-acceptor active site is annotated at position 251 (His), not at any of the distractor positions. The annotation is computational (PIRSR) rather than directly experimentally validated on this ortholog, but the Cys-His dyad mechanism is a hallmark of the ASADH family and is corroborated by X-ray structures (PDB 6C8W) of this protein."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (by similarity / PIRSR pro-rule), meaning it is a computational/pro-rule inference transferred from the ASADH family pattern, not a site-directed mutagenesis or kinetic measurement on this specific Blastomyces ortholog.",
    "The UniProt entry was first released in February 2025 (sequence version 2); the author's construction snapshot is unknown, though the sequence matches the current and historical (entry v26) records.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning-supported judgment rests solely on information present in the original question (sequence + choices).",
    "The question lists a single residue per option rather than the full catalytic dyad (Cys-154 + His-251); this is a simplification but does not create ambiguity among the four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor assigns a catalytic role to an amino acid that is chemically incapable of performing that role (Ile as proton acceptor, Leu as proton donor, Asp at a non-catalytic position as the proton acceptor). Only Cys-154 can form an acyl-thioester intermediate. The options are cleanly distinguishable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A179UL48 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Blastomyces gilchristii, 362 aa, sequence matched) annotates position 154 as an active site forming an 'Acyl-thioester intermediate' (evidence ECO:0000255|PIRSR:PIRSR000148-1, i.e. pro-rule/similarity-based inference). The supplied sequence at position 154 is indeed Cys (C), consistent with the well-established ASADH catalytic mechanism in which a catalytic cysteine forms the acyl-thioester intermediate. The companion proton-acceptor active site is annotated at position 251 (His), not at any of the distractor positions. The annotation is computational (PIRSR) rather than directly experimentally validated on this ortholog, but the Cys-His dyad mechanism is a hallmark of the ASADH family and is corroborated by X-ray structures (PDB 6C8W) of this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H4", "H5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The amino-acid identities at the four candidate positions, read directly from the supplied sequence, eliminate three of the four options on purely chemical grounds: position 148 is Ile (cannot serve as a proton acceptor), position 159 is Leu (cannot serve as a proton donor), and position 308 is Asp (not the catalytic proton acceptor in the ASADH Cys-His dyad; the actual proton acceptor is His-251). Only position 154 is a Cys, and formation of an acyl-thioester intermediate requires a thiol nucleophile, a property unique to cysteine among the standard amino acids. Thus, even without knowing the exact protein identity, a model applying general biochemistry (thioester chemistry requires Cys; Ile and Leu lack ionizable side chains suitable for proton transfer) can single out D.",
    "missing_item_specific_fact": "None essential. Recognizing the protein as ASADH would confirm the Cys-His dyad mechanism, but the chemical logic of thioester formation from a cysteine thiol is sufficient to distinguish the correct answer from the distractors given the residue identities visible in the sequence.",
    "reason": "The question supplies the full sequence, so the model can count to each candidate position and read the residue type. General biochemical knowledge (only Cys forms thioesters; Ile and Leu are non-polar aliphatic residues incapable of proton transfer; the catalytic proton acceptor in a dehydrogenase acting via a thioester intermediate is typically His, not Asp at a distant position) meaningfully separates the four choices without requiring recall of a specific database annotation for this ortholog."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor assigns a catalytic role to an amino acid that is chemically incapable of performing that role (Ile as proton acceptor, Leu as proton donor, Asp at a non-catalytic position as the proton acceptor). Only Cys-154 can form an acyl-thioester intermediate. The options are cleanly distinguishable."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (by similarity / PIRSR pro-rule), meaning it is a computational/pro-rule inference transferred from the ASADH family pattern, not a site-directed mutagenesis or kinetic measurement on this specific Blastomyces ortholog.",
    "The UniProt entry was first released in February 2025 (sequence version 2); the author's construction snapshot is unknown, though the sequence matches the current and historical (entry v26) records.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning-supported judgment rests solely on information present in the original question (sequence + choices).",
    "The question lists a single residue per option rather than the full catalytic dyad (Cys-154 + His-251); this is a simplification but does not create ambiguity among the four choices."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates position 154 as the acyl-thioester intermediate site, matching option D. This is a computational PIRSR annotation, not direct experimental evidence for that residue in this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable solver could recognize the sequence as consistent with the aspartate-semialdehyde dehydrogenase family. In this enzyme family, a conserved catalytic cysteine attacks the substrate and forms a covalent acyl-thioester intermediate. The cysteine at position 154 is therefore a credible match for D, distinguishing it from the offered proton-transfer roles.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level catalytic mechanism and conserved cysteine feature provide a transferable basis for selecting D; the exact protein annotation is not necessary to make that inference, though it would strengthen it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered roles distinguish the catalytic cysteine intermediate from the proton-transfer alternatives.


### Important caveats

- The supporting residue annotation is computationally transferred by a family rule; the supplied evidence does not independently establish it through a direct experiment on this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable solver could recognize the sequence as consistent with the aspartate-semialdehyde dehydrogenase family. In this enzyme family, a conserved catalytic cysteine attacks the substrate and forms a covalent acyl-thioester intermediate. The cysteine at position 154 is therefore a credible match for D, distinguishing it from the offered proton-transfer roles.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level catalytic mechanism and conserved cysteine feature provide a transferable basis for selecting D; the exact protein annotation is not necessary to make that inference, though it would strengthen it."
  },
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 154 as the acyl-thioester intermediate site, matching option D. This is a computational PIRSR annotation, not direct experimental evidence for that residue in this protein."
  },
  "important_caveats": [
    "The supporting residue annotation is computationally transferred by a family rule; the supplied evidence does not independently establish it through a direct experiment on this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered roles distinguish the catalytic cysteine intermediate from the proton-transfer alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 154 as the acyl-thioester intermediate site, matching option D. This is a computational PIRSR annotation, not direct experimental evidence for that residue in this protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable solver could recognize the sequence as consistent with the aspartate-semialdehyde dehydrogenase family. In this enzyme family, a conserved catalytic cysteine attacks the substrate and forms a covalent acyl-thioester intermediate. The cysteine at position 154 is therefore a credible match for D, distinguishing it from the offered proton-transfer roles.",
    "missing_item_specific_fact": "",
    "reason": "The family-level catalytic mechanism and conserved cysteine feature provide a transferable basis for selecting D; the exact protein annotation is not necessary to make that inference, though it would strengthen it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered roles distinguish the catalytic cysteine intermediate from the proton-transfer alternatives."
  },
  "important_caveats": [
    "The supporting residue annotation is computationally transferred by a family rule; the supplied evidence does not independently establish it through a direct experiment on this protein."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5/H4) explicitly annotates position 154 as 'Acyl-thioester intermediate' active site with evidence code ECO:0000255 (PIRSR curated annotation). The residue at position 154 in the provided sequence is Cysteine (C), which is chemically consistent with forming an acyl-thioester intermediate. The protein is identified as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism involves a Cys-His dyad where the Cys forms the thioester. The annotation is a curated computational assignment (PIRSR000148-1) rather than direct experimental mutagenesis on this specific protein, but it is well-supported by the conserved mechanism across the ASADH family and corroborated by PDB structures (6C8W, 6C85) of the same enzyme.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable knowledge pathways converge on D: (1) The N-terminal region (GATGAVGT around positions 12-19) shows a degenerate Rossmann-fold motif indicating an NAD(P)-binding dehydrogenase. (2) The 'CNSNCA' motif at positions 151-156 is a well-known ASADH family signature observed across E. coli, M. tuberculosis, and other ASADH orthologs. (3) ASADH mechanism (known from multiple family members): the catalytic Cys in this motif attacks the substrate carboxyl to form an acyl-thioester intermediate, while a His (here at position 251 in the 'HTVCASL' context) acts as proton acceptor. (4) Even without family identification, chemical consistency eliminates alternatives: position 148 is Ile (cannot be proton acceptor), position 159 is Leu (cannot be proton donor), position 308 is Asp (not the catalytic proton acceptor in this enzyme class). Only position 154 (Cys) is chemically compatible with forming a thioester intermediate, which is the hallmark of Cys-dependent dehydrogenase catalysis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of dehydrogenase families, the Cys-His catalytic dyad mechanism, and the CNSNCA ASADH signature can identify position 154 (Cys) as the thioester-forming residue. The other options are eliminated by basic residue chemistry (Ile, Leu, Asp cannot perform the stated roles in this enzyme context). The inference relies on family-level mechanism knowledge transferable from other ASADH proteins, not on memorizing this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D presents a chemically consistent residue-role pair (Cys-thioester). Options A (Ile as proton acceptor), B (Leu as proton donor), and C (Asp as proton acceptor in this enzyme context) are all chemically implausible for the described roles. No ambiguity exists among the offered choices.


### Important caveats

- The active site annotation uses evidence code ECO:0000255 (PIRSR), which is a curated computational/protein-family assignment rather than site-directed mutagenesis on this exact protein. However, the mechanism is well-established across the ASADH family and supported by crystal structures of this enzyme.
- The UniProt entry was first released in January 2026; the benchmark author's source snapshot timing is unknown, though the sequence matches.
- Position numbering is canonical (362 aa full-length); no construct or isoform adjustments apply.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable knowledge pathways converge on D: (1) The N-terminal region (GATGAVGT around positions 12-19) shows a degenerate Rossmann-fold motif indicating an NAD(P)-binding dehydrogenase. (2) The 'CNSNCA' motif at positions 151-156 is a well-known ASADH family signature observed across E. coli, M. tuberculosis, and other ASADH orthologs. (3) ASADH mechanism (known from multiple family members): the catalytic Cys in this motif attacks the substrate carboxyl to form an acyl-thioester intermediate, while a His (here at position 251 in the 'HTVCASL' context) acts as proton acceptor. (4) Even without family identification, chemical consistency eliminates alternatives: position 148 is Ile (cannot be proton acceptor), position 159 is Leu (cannot be proton donor), position 308 is Asp (not the catalytic proton acceptor in this enzyme class). Only position 154 (Cys) is chemically compatible with forming a thioester intermediate, which is the hallmark of Cys-dependent dehydrogenase catalysis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of dehydrogenase families, the Cys-His catalytic dyad mechanism, and the CNSNCA ASADH signature can identify position 154 (Cys) as the thioester-forming residue. The other options are eliminated by basic residue chemistry (Ile, Leu, Asp cannot perform the stated roles in this enzyme context). The inference relies on family-level mechanism knowledge transferable from other ASADH proteins, not on memorizing this specific entry's annotation."
  },
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H4) explicitly annotates position 154 as 'Acyl-thioester intermediate' active site with evidence code ECO:0000255 (PIRSR curated annotation). The residue at position 154 in the provided sequence is Cysteine (C), which is chemically consistent with forming an acyl-thioester intermediate. The protein is identified as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism involves a Cys-His dyad where the Cys forms the thioester. The annotation is a curated computational assignment (PIRSR000148-1) rather than direct experimental mutagenesis on this specific protein, but it is well-supported by the conserved mechanism across the ASADH family and corroborated by PDB structures (6C8W, 6C85) of the same enzyme."
  },
  "important_caveats": [
    "The active site annotation uses evidence code ECO:0000255 (PIRSR), which is a curated computational/protein-family assignment rather than site-directed mutagenesis on this exact protein. However, the mechanism is well-established across the ASADH family and supported by crystal structures of this enzyme.",
    "The UniProt entry was first released in January 2026; the benchmark author's source snapshot timing is unknown, though the sequence matches.",
    "Position numbering is canonical (362 aa full-length); no construct or isoform adjustments apply."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D presents a chemically consistent residue-role pair (Cys-thioester). Options A (Ile as proton acceptor), B (Leu as proton donor), and C (Asp as proton acceptor in this enzyme context) are all chemically implausible for the described roles. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H4) explicitly annotates position 154 as 'Acyl-thioester intermediate' active site with evidence code ECO:0000255 (PIRSR curated annotation). The residue at position 154 in the provided sequence is Cysteine (C), which is chemically consistent with forming an acyl-thioester intermediate. The protein is identified as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism involves a Cys-His dyad where the Cys forms the thioester. The annotation is a curated computational assignment (PIRSR000148-1) rather than direct experimental mutagenesis on this specific protein, but it is well-supported by the conserved mechanism across the ASADH family and corroborated by PDB structures (6C8W, 6C85) of the same enzyme.",
    "evidence_ids": ["C5", "H4", "C4", "C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable knowledge pathways converge on D: (1) The N-terminal region (GATGAVGT around positions 12-19) shows a degenerate Rossmann-fold motif indicating an NAD(P)-binding dehydrogenase. (2) The 'CNSNCA' motif at positions 151-156 is a well-known ASADH family signature observed across E. coli, M. tuberculosis, and other ASADH orthologs. (3) ASADH mechanism (known from multiple family members): the catalytic Cys in this motif attacks the substrate carboxyl to form an acyl-thioester intermediate, while a His (here at position 251 in the 'HTVCASL' context) acts as proton acceptor. (4) Even without family identification, chemical consistency eliminates alternatives: position 148 is Ile (cannot be proton acceptor), position 159 is Leu (cannot be proton donor), position 308 is Asp (not the catalytic proton acceptor in this enzyme class). Only position 154 (Cys) is chemically compatible with forming a thioester intermediate, which is the hallmark of Cys-dependent dehydrogenase catalysis.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of dehydrogenase families, the Cys-His catalytic dyad mechanism, and the CNSNCA ASADH signature can identify position 154 (Cys) as the thioester-forming residue. The other options are eliminated by basic residue chemistry (Ile, Leu, Asp cannot perform the stated roles in this enzyme context). The inference relies on family-level mechanism knowledge transferable from other ASADH proteins, not on memorizing this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D presents a chemically consistent residue-role pair (Cys-thioester). Options A (Ile as proton acceptor), B (Leu as proton donor), and C (Asp as proton acceptor in this enzyme context) are all chemically implausible for the described roles. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The active site annotation uses evidence code ECO:0000255 (PIRSR), which is a curated computational/protein-family assignment rather than site-directed mutagenesis on this exact protein. However, the mechanism is well-established across the ASADH family and supported by crystal structures of this enzyme.",
    "The UniProt entry was first released in January 2026; the benchmark author's source snapshot timing is unknown, though the sequence matches.",
    "Position numbering is canonical (362 aa full-length); no construct or isoform adjustments apply."
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
  "requested_accession": "A0A179UL48",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "benchmark_sequence_length": 362,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "current_source_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "current_source_sequence_length": 362,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 26,
  "selected_historical_version": {
    "accession": "A0A179UL48",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_BLAGS",
    "sequenceVersion": 2
  },
  "selected_historical_record_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "selected_historical_source_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "selected_historical_source_sequence_length": 362,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A179UL48\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Blastomyces dermatitidis\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002038\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Onygenales\",\"Ajellomycetaceae\",\"Blastomyces\"],\"scientificName\":\"Blastomyces gilchristii (strain SLH14081)\",\"taxonId\":559298}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Acyl-thioester intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":154},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":251},\"start\":{\"modifier\":\"EXACT\",\"value\":251}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":15},\"start\":{\"modifier\":\"EXACT\",\"value\":15}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":16},\"start\":{\"modifier\":\"EXACT\",\"value\":16}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":17},\"start\":{\"modifier\":\"EXACT\",\"value\":17}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":18},\"start\":{\"modifier\":\"EXACT\",\"value\":18}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":40},\"start\":{\"modifier\":\"EXACT\",\"value\":40}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":43},\"start\":{\"modifier\":\"EXACT\",\"value\":43}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":87},\"start\":{\"modifier\":\"EXACT\",\"value\":87}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":88},\"start\":{\"modifier\":\"EXACT\",\"value\":88}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":340},\"start\":{\"modifier\":\"EXACT\",\"value\":340}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30107909\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbrc.2018.08.053\"}],\"citationType\":\"journal article\",\"firstPage\":\"2848\",\"id\":\"30107909\",\"journal\":\"Biochem. Biophys. Res. Commun.\",\"lastPage\":\"2854\",\"publicationDate\":\"2018\",\"title\":\"Structural insights into inhibitor binding to a fungal ortholog of aspartate semialdehyde dehydrogenase.\",\"volume\":\"503\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C85\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND NADP(+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   DHAS_BLAGS              Reviewed;         362 AA.\nAC   A0A179UL48;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};\nGN   ORFNames=BDBG_16922 {ECO:0000312|EMBL:OAT07949.1};\nOS   Blastomyces gilchristii (strain SLH14081) (Blastomyces dermatitidis).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Onygenales; Ajellomycetaceae; Blastomyces.\nOX   NCBI_TaxID=559298 {ECO:0000312|Proteomes:UP000002038};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 25-31",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 32-40",
  "excerpt": "RN   [3] {ECO:0007744|PDB:6C85, ECO:0007744|PDB:6C8W}\nRP   X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND\nRP   NADP(+), FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=30107909; DOI=10.1016/j.bbrc.2018.08.053;\nRA   Dahal G.P., Viola R.E.;\nRT   \"Structural insights into inhibitor binding to a fungal ortholog of\nRT   aspartate semialdehyde dehydrogenase.\";\nRL   Biochem. Biophys. Res. Commun. 503:2848-2854(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 133-135",
  "excerpt": "FT   ACT_SITE        154\nFT                   /note=\"Acyl-thioester intermediate\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 136-138",
  "excerpt": "FT   ACT_SITE        251\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 139-143",
  "excerpt": "FT   BINDING         15\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 144-147",
  "excerpt": "FT   BINDING         16\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 148-152",
  "excerpt": "FT   BINDING         17\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 153-157",
  "excerpt": "FT   BINDING         18\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 158-162",
  "excerpt": "FT   BINDING         40\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 163-167",
  "excerpt": "FT   BINDING         43\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 168-172",
  "excerpt": "FT   BINDING         87\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 173-176",
  "excerpt": "FT   BINDING         88\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 177-180",
  "excerpt": "FT   BINDING         186\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "source_locator": "lines 181-185",
  "excerpt": "FT   BINDING         340\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
