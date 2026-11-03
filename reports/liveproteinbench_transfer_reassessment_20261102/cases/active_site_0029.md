# active_site_0029: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0029.txt)

**Task:** `active_site`  
**Author key, unchanged:** **A** — Position 286 (Charge relay system)

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
MRTVFIYACIISLVLRTIPAHNDLMSKEKENKEKDVHKIIEDLRFLEKVDAILENSNMTIDDVKADADAYNPDEDAPKEELNKIEMEKKKAEEEAKNSKKKILERYLLDEKKKKSLRLIVSENHATSPSFFEESLIQEDFMSFIQSKGEIVNLKNLKSMIIELNSDMTDKELEAYITLLKKKGAHVESDELVGADSIYVDIIKDAVKRGDTSINFKKMQSNMLEVENKTYEKLNNNLKKSKNSYKKSFFNDEYRNLQWGLDLARLDDAQEMITTNSVETTKICVIDSGIDYNHPDLKGNIYVNLNELNGKEGIDDDNNGIIDDIYGVNYVNNTGDPWDDHNHGSHVSGIISAIGNNSIGVVGVNPSSKLVICKALDDKKLGRLGNIFKCIDYCINKKVNIINGSFSFDEYSTIFSSTIEYLARLGILFVVSSSNCSHPPSSIPDITRCDLSVNSKYPSVLSTQYDNMVVVANLKKKINGEYDISINSFYSDIYCQVSAPGANIYSTASRGSYMELSGTSMAAPHVAGIASIILSINPDLTYKQVVNILKNSVVKLSSHKNKIAWGGYIDILNAVKNAISSKNSYIRFQGIRMWKSKKRN

[Multiple Choices]
A. Position 286 (Charge relay system)
B. Position 180 (For beta-ketoacyl synthase activity)
C. Position 12 (Proton acceptor)
D. Position 365 (For beta-ketoacyl synthase 1 activity)
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

> The matched sequence's UniProt annotation identifies position 286 as an active-site residue in the charge relay system. This is a computational PROSITE-ProRule annotation, not direct experimental evidence for that residue.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not establish which exact position is annotated as part of this enzyme's catalytic charge relay system. Recognizing the protein family and using its catalytic-residue pattern could guide a prediction, but does not securely identify the listed position from the supplied information.


**Missing item-specific fact**

> The protein-specific active-site annotation assigning the charge relay system to position 286.


**Reason**

> Choosing A depends on the residue-level annotation for this particular protein, which is not supplied in the question; remembering the sequence's database entry would be lookup or memorization, not reasoning from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A among the listed options matches the supplied annotation for position 286. However, it names only one residue, not the full catalytic center.


### Important caveats

- The same matched-sequence annotation also lists charge-relay-system residues at positions 342 and 519; these are not options.
- The cited active-site assignment is computationally annotated, and the evidence provided does not independently establish it experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not establish which exact position is annotated as part of this enzyme's catalytic charge relay system. Recognizing the protein family and using its catalytic-residue pattern could guide a prediction, but does not securely identify the listed position from the supplied information.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning the charge relay system to position 286.",
    "reason": "Choosing A depends on the residue-level annotation for this particular protein, which is not supplied in the question; remembering the sequence's database entry would be lookup or memorization, not reasoning from the input."
  },
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The matched sequence's UniProt annotation identifies position 286 as an active-site residue in the charge relay system. This is a computational PROSITE-ProRule annotation, not direct experimental evidence for that residue."
  },
  "important_caveats": [
    "The same matched-sequence annotation also lists charge-relay-system residues at positions 342 and 519; these are not options.",
    "The cited active-site assignment is computationally annotated, and the evidence provided does not independently establish it experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the listed options matches the supplied annotation for position 286. However, it names only one residue, not the full catalytic center."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence's UniProt annotation identifies position 286 as an active-site residue in the charge relay system. This is a computational PROSITE-ProRule annotation, not direct experimental evidence for that residue.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not establish which exact position is annotated as part of this enzyme's catalytic charge relay system. Recognizing the protein family and using its catalytic-residue pattern could guide a prediction, but does not securely identify the listed position from the supplied information.",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning the charge relay system to position 286.",
    "reason": "Choosing A depends on the residue-level annotation for this particular protein, which is not supplied in the question; remembering the sequence's database entry would be lookup or memorization, not reasoning from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the listed options matches the supplied annotation for position 286. However, it names only one residue, not the full catalytic center."
  },
  "important_caveats": [
    "The same matched-sequence annotation also lists charge-relay-system residues at positions 342 and 519; these are not options.",
    "The cited active-site assignment is computationally annotated, and the evidence provided does not independently establish it experimentally."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A509AM03 (PbSUB1, subtilisin-like protease 1 from Plasmodium berghei) annotates position 286 as an Active site in the 'Charge relay system' (evidence ECO:0000255|PROSITE-ProRule:PRU01240). The sequence matches (599 aa, SHA-256 identical). The annotation is computational (PROSITE-ProRule pattern match) rather than directly experimental, but it is a legitimate database annotation consistent with the known subtilisin catalytic triad (Asp-His-Ser). The other three options (180, 12, 365) have no active-site annotation and reference 'beta-ketoacyl synthase activity' or 'proton acceptor' roles incompatible with a serine protease.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C4](#evidence-c4), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein contains recognizable subtilisin-family motifs: a GDS motif (~pos 158, catalytic Asp), a GSH motif (~pos 286, catalytic His), and a GTSMA motif (~pos 475, catalytic Ser). Subtilisin-like serine proteases (EC 3.4.21.62) catalyze via a charge-relay triad, not via beta-ketoacyl synthase chemistry. Options B and D invoke 'beta-ketoacyl synthase activity,' a fatty-acid biosynthesis function wholly unrelated to proteolysis. Option C places a 'proton acceptor' at position 12, which falls within the N-terminal signal peptide (cleaved at ~pos 19-20 per the precursor flag and the observed 'IPAHNDL' signal-peptide region), making it impossible for that residue to participate in catalysis. By elimination on enzyme-class grounds, only A (charge relay system, consistent with subtilisin catalysis) remains.


**Missing item-specific fact**

> Precise confirmation that the His of the triad falls exactly at residue 286 (rather than, say, 284 or 288) requires either residue-by-residue counting through 599 aa or knowledge of the specific PROSITE-ProRule PRU01240 hit position. However, the distractors are eliminable by general enzymology without this precision.


**Reason**

> The question is answerable by recognizing the protein as a subtilisin-like protease (from sequence motifs and overall architecture), applying the general fact that subtilisins use a charge-relay triad, and eliminating options that invoke an unrelated enzyme class (beta-ketoacyl synthase) or a signal-peptide position. This constitutes a concrete biological argument distinguishing the choices. The precise positional verification is somewhat lookup-assisted, but the elimination logic is robust.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A references a mechanism (charge relay system) consistent with the protein's actual enzymatic class. B and D invoke beta-ketoacyl synthase activity (fatty-acid biosynthesis), which is categorically incompatible with a serine protease. C places a catalytic role in the signal peptide. No other option is defensible.


### Important caveats

- The active-site annotation at position 286 is based on PROSITE-ProRule pattern matching (ECO:0000255), i.e., a computational inference from the subtilisin signature, not direct experimental mutagenesis or crystallographic evidence for this specific Plasmodium berghei protein.
- The full catalytic triad comprises positions 286, 342, and 519 (all annotated as charge relay system). The question singles out only 286; a model that identified 342 or 519 would not find a matching option, but those are not offered as choices.
- The protein is a precursor; the mature protease begins after signal-peptide cleavage (~pos 19-20) and further processing at pos 195-196. Residue numbering in the options refers to the full precursor sequence.
- The identity of the protein (PbSUB1) and its accession were not provided to the evaluated model; recognition must come from sequence analysis alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein contains recognizable subtilisin-family motifs: a GDS motif (~pos 158, catalytic Asp), a GSH motif (~pos 286, catalytic His), and a GTSMA motif (~pos 475, catalytic Ser). Subtilisin-like serine proteases (EC 3.4.21.62) catalyze via a charge-relay triad, not via beta-ketoacyl synthase chemistry. Options B and D invoke 'beta-ketoacyl synthase activity,' a fatty-acid biosynthesis function wholly unrelated to proteolysis. Option C places a 'proton acceptor' at position 12, which falls within the N-terminal signal peptide (cleaved at ~pos 19-20 per the precursor flag and the observed 'IPAHNDL' signal-peptide region), making it impossible for that residue to participate in catalysis. By elimination on enzyme-class grounds, only A (charge relay system, consistent with subtilisin catalysis) remains.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise confirmation that the His of the triad falls exactly at residue 286 (rather than, say, 284 or 288) requires either residue-by-residue counting through 599 aa or knowledge of the specific PROSITE-ProRule PRU01240 hit position. However, the distractors are eliminable by general enzymology without this precision.",
    "reason": "The question is answerable by recognizing the protein as a subtilisin-like protease (from sequence motifs and overall architecture), applying the general fact that subtilisins use a charge-relay triad, and eliminating options that invoke an unrelated enzyme class (beta-ketoacyl synthase) or a signal-peptide position. This constitutes a concrete biological argument distinguishing the choices. The precise positional verification is somewhat lookup-assisted, but the elimination logic is robust."
  },
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A509AM03 (PbSUB1, subtilisin-like protease 1 from Plasmodium berghei) annotates position 286 as an Active site in the 'Charge relay system' (evidence ECO:0000255|PROSITE-ProRule:PRU01240). The sequence matches (599 aa, SHA-256 identical). The annotation is computational (PROSITE-ProRule pattern match) rather than directly experimental, but it is a legitimate database annotation consistent with the known subtilisin catalytic triad (Asp-His-Ser). The other three options (180, 12, 365) have no active-site annotation and reference 'beta-ketoacyl synthase activity' or 'proton acceptor' roles incompatible with a serine protease."
  },
  "important_caveats": [
    "The active-site annotation at position 286 is based on PROSITE-ProRule pattern matching (ECO:0000255), i.e., a computational inference from the subtilisin signature, not direct experimental mutagenesis or crystallographic evidence for this specific Plasmodium berghei protein.",
    "The full catalytic triad comprises positions 286, 342, and 519 (all annotated as charge relay system). The question singles out only 286; a model that identified 342 or 519 would not find a matching option, but those are not offered as choices.",
    "The protein is a precursor; the mature protease begins after signal-peptide cleavage (~pos 19-20) and further processing at pos 195-196. Residue numbering in the options refers to the full precursor sequence.",
    "The identity of the protein (PbSUB1) and its accession were not provided to the evaluated model; recognition must come from sequence analysis alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A references a mechanism (charge relay system) consistent with the protein's actual enzymatic class. B and D invoke beta-ketoacyl synthase activity (fatty-acid biosynthesis), which is categorically incompatible with a serine protease. C places a catalytic role in the signal peptide. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A509AM03 (PbSUB1, subtilisin-like protease 1 from Plasmodium berghei) annotates position 286 as an Active site in the 'Charge relay system' (evidence ECO:0000255|PROSITE-ProRule:PRU01240). The sequence matches (599 aa, SHA-256 identical). The annotation is computational (PROSITE-ProRule pattern match) rather than directly experimental, but it is a legitimate database annotation consistent with the known subtilisin catalytic triad (Asp-His-Ser). The other three options (180, 12, 365) have no active-site annotation and reference 'beta-ketoacyl synthase activity' or 'proton acceptor' roles incompatible with a serine protease.",
    "evidence_ids": ["C5", "H6", "C4", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein contains recognizable subtilisin-family motifs: a GDS motif (~pos 158, catalytic Asp), a GSH motif (~pos 286, catalytic His), and a GTSMA motif (~pos 475, catalytic Ser). Subtilisin-like serine proteases (EC 3.4.21.62) catalyze via a charge-relay triad, not via beta-ketoacyl synthase chemistry. Options B and D invoke 'beta-ketoacyl synthase activity,' a fatty-acid biosynthesis function wholly unrelated to proteolysis. Option C places a 'proton acceptor' at position 12, which falls within the N-terminal signal peptide (cleaved at ~pos 19-20 per the precursor flag and the observed 'IPAHNDL' signal-peptide region), making it impossible for that residue to participate in catalysis. By elimination on enzyme-class grounds, only A (charge relay system, consistent with subtilisin catalysis) remains.",
    "missing_item_specific_fact": "Precise confirmation that the His of the triad falls exactly at residue 286 (rather than, say, 284 or 288) requires either residue-by-residue counting through 599 aa or knowledge of the specific PROSITE-ProRule PRU01240 hit position. However, the distractors are eliminable by general enzymology without this precision.",
    "reason": "The question is answerable by recognizing the protein as a subtilisin-like protease (from sequence motifs and overall architecture), applying the general fact that subtilisins use a charge-relay triad, and eliminating options that invoke an unrelated enzyme class (beta-ketoacyl synthase) or a signal-peptide position. This constitutes a concrete biological argument distinguishing the choices. The precise positional verification is somewhat lookup-assisted, but the elimination logic is robust."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A references a mechanism (charge relay system) consistent with the protein's actual enzymatic class. B and D invoke beta-ketoacyl synthase activity (fatty-acid biosynthesis), which is categorically incompatible with a serine protease. C places a catalytic role in the signal peptide. No other option is defensible."
  },
  "important_caveats": [
    "The active-site annotation at position 286 is based on PROSITE-ProRule pattern matching (ECO:0000255), i.e., a computational inference from the subtilisin signature, not direct experimental mutagenesis or crystallographic evidence for this specific Plasmodium berghei protein.",
    "The full catalytic triad comprises positions 286, 342, and 519 (all annotated as charge relay system). The question singles out only 286; a model that identified 342 or 519 would not find a matching option, but those are not offered as choices.",
    "The protein is a precursor; the mature protease begins after signal-peptide cleavage (~pos 19-20) and further processing at pos 195-196. Residue numbering in the options refers to the full precursor sequence.",
    "The identity of the protein (PbSUB1) and its accession were not provided to the evaluated model; recognition must come from sequence analysis alone."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates position 286 as part of the charge-relay system. This is a computational PROSITE-ProRule annotation, not direct experimental validation of that residue in this protein.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a secreted subtilisin-like serine protease: its N-terminal hydrophobic segment is signal-peptide-like, and the later enzyme region is compatible with a protease catalytic domain. Subtilisin-family proteases use a conserved Asp-His-Ser charge relay. Position 286 is a plausible catalytic charge-relay residue, whereas position 12 lies in the signal-peptide-like segment and the beta-ketoacyl-synthase choices name an unrelated enzyme activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the sequence context give a meaningful basis to select A among these alternatives without knowing this protein's database annotation. This supports a probabilistic inference, not experimental proof of the exact residue's role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A is compatible with the sequence-based subtilisin-protease inference among the offered choices. Although the full charge relay includes multiple residues, the other offered positions do not provide a comparably defensible alternative.


### Important caveats

- The supplied evidence supports position 286 through a computational annotation; it does not establish direct experimental confirmation.
- Position 286 is one component of a catalytic charge-relay system, not by itself the complete active site.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a secreted subtilisin-like serine protease: its N-terminal hydrophobic segment is signal-peptide-like, and the later enzyme region is compatible with a protease catalytic domain. Subtilisin-family proteases use a conserved Asp-His-Ser charge relay. Position 286 is a plausible catalytic charge-relay residue, whereas position 12 lies in the signal-peptide-like segment and the beta-ketoacyl-synthase choices name an unrelated enzyme activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the sequence context give a meaningful basis to select A among these alternatives without knowing this protein's database annotation. This supports a probabilistic inference, not experimental proof of the exact residue's role."
  },
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 286 as part of the charge-relay system. This is a computational PROSITE-ProRule annotation, not direct experimental validation of that residue in this protein."
  },
  "important_caveats": [
    "The supplied evidence supports position 286 through a computational annotation; it does not establish direct experimental confirmation.",
    "Position 286 is one component of a catalytic charge-relay system, not by itself the complete active site."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A is compatible with the sequence-based subtilisin-protease inference among the offered choices. Although the full charge relay includes multiple residues, the other offered positions do not provide a comparably defensible alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 286 as part of the charge-relay system. This is a computational PROSITE-ProRule annotation, not direct experimental validation of that residue in this protein.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a secreted subtilisin-like serine protease: its N-terminal hydrophobic segment is signal-peptide-like, and the later enzyme region is compatible with a protease catalytic domain. Subtilisin-family proteases use a conserved Asp-His-Ser charge relay. Position 286 is a plausible catalytic charge-relay residue, whereas position 12 lies in the signal-peptide-like segment and the beta-ketoacyl-synthase choices name an unrelated enzyme activity.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the sequence context give a meaningful basis to select A among these alternatives without knowing this protein's database annotation. This supports a probabilistic inference, not experimental proof of the exact residue's role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A is compatible with the sequence-based subtilisin-protease inference among the offered choices. Although the full charge relay includes multiple residues, the other offered positions do not provide a comparably defensible alternative."
  },
  "important_caveats": [
    "The supplied evidence supports position 286 through a computational annotation; it does not establish direct experimental confirmation.",
    "Position 286 is one component of a catalytic charge-relay system, not by itself the complete active site."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A509AM03 (Subtilisin-like protease 1, PbSUB1) explicitly annotates position 286 as an Active site with description 'Charge relay system' (evidence C5/H6). The protein is EC 3.4.21.62, a subtilisin-type serine protease whose catalytic triad (Asp286-His342-Ser519) constitutes the charge relay system. The annotation is based on PROSITE-ProRule (ECO:0000255, computational/prorule evidence), which is consistent with the well-established subtilisin mechanism. The sequence confirms: position 286 is Asp (in IDSG context), 342 is His (in NHGSHVSG context), and 519 is Ser (in GTSMA context), matching the canonical subtilisin triad.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'GTSMA' motif (positions 517-521: G-T-S-M-A), which is the hallmark signature of subtilisin-type serine proteases' catalytic serine. This is an extremely well-known family-level sequence feature. Subtilisins catalyze via an Asp-His-Ser 'charge relay system' — this is the standard mechanistic terminology for this enzyme family. Option A ('Position 286, Charge relay system') matches both the family identification (subtilisin) and the correct mechanistic description. Options B and D ('beta-ketoacyl synthase') refer to fatty acid synthase, a completely different enzyme class with a Cys-His-His active site and no sequence similarity to subtilisins. Option C ('Proton acceptor') is generic terminology not associated with subtilisin catalysis. A model recognizing the GTSMA motif and knowing subtilisin mechanism can confidently select A and eliminate the others.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GTSMA motif is a universally recognized family signature for subtilisin-type proteases, and 'charge relay system' is the standard mechanistic descriptor for the subtilisin catalytic triad. This combination of family recognition (from the sequence) and mechanistic knowledge (from other subtilisin proteins) meaningfully and uniquely identifies option A among the four choices. No target-specific annotation lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A identifies a position that is an annotated active site with the correct functional description. Positions 180, 12, and 365 are not active sites, and their associated functions (beta-ketoacyl synthase, proton acceptor) are inconsistent with a subtilisin-type protease. The distractors are clearly eliminable by family recognition.


### Important caveats

- The active site annotation at position 286 is based on PROSITE-ProRule (ECO:0000255), a computational/prorule inference, not direct experimental mutagenesis of this specific protein. However, it is consistent with the well-established subtilisin mechanism and the sequence context (IDSG motif).
- The question lists only one position per option, whereas the full catalytic center comprises three residues (286, 342, 519). The question format asks which single option correctly identifies an active site residue with its function, which is unambiguous.
- The protein identity (Plasmodium berghei SUB1) was not provided to the model; identification relies solely on sequence motif recognition, which is sufficient given the distinctive GTSMA motif.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'GTSMA' motif (positions 517-521: G-T-S-M-A), which is the hallmark signature of subtilisin-type serine proteases' catalytic serine. This is an extremely well-known family-level sequence feature. Subtilisins catalyze via an Asp-His-Ser 'charge relay system' — this is the standard mechanistic terminology for this enzyme family. Option A ('Position 286, Charge relay system') matches both the family identification (subtilisin) and the correct mechanistic description. Options B and D ('beta-ketoacyl synthase') refer to fatty acid synthase, a completely different enzyme class with a Cys-His-His active site and no sequence similarity to subtilisins. Option C ('Proton acceptor') is generic terminology not associated with subtilisin catalysis. A model recognizing the GTSMA motif and knowing subtilisin mechanism can confidently select A and eliminate the others.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GTSMA motif is a universally recognized family signature for subtilisin-type proteases, and 'charge relay system' is the standard mechanistic descriptor for the subtilisin catalytic triad. This combination of family recognition (from the sequence) and mechanistic knowledge (from other subtilisin proteins) meaningfully and uniquely identifies option A among the four choices. No target-specific annotation lookup is required."
  },
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A509AM03 (Subtilisin-like protease 1, PbSUB1) explicitly annotates position 286 as an Active site with description 'Charge relay system' (evidence C5/H6). The protein is EC 3.4.21.62, a subtilisin-type serine protease whose catalytic triad (Asp286-His342-Ser519) constitutes the charge relay system. The annotation is based on PROSITE-ProRule (ECO:0000255, computational/prorule evidence), which is consistent with the well-established subtilisin mechanism. The sequence confirms: position 286 is Asp (in IDSG context), 342 is His (in NHGSHVSG context), and 519 is Ser (in GTSMA context), matching the canonical subtilisin triad."
  },
  "important_caveats": [
    "The active site annotation at position 286 is based on PROSITE-ProRule (ECO:0000255), a computational/prorule inference, not direct experimental mutagenesis of this specific protein. However, it is consistent with the well-established subtilisin mechanism and the sequence context (IDSG motif).",
    "The question lists only one position per option, whereas the full catalytic center comprises three residues (286, 342, 519). The question format asks which single option correctly identifies an active site residue with its function, which is unambiguous.",
    "The protein identity (Plasmodium berghei SUB1) was not provided to the model; identification relies solely on sequence motif recognition, which is sufficient given the distinctive GTSMA motif."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A identifies a position that is an annotated active site with the correct functional description. Positions 180, 12, and 365 are not active sites, and their associated functions (beta-ketoacyl synthase, proton acceptor) are inconsistent with a subtilisin-type protease. The distractors are clearly eliminable by family recognition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A509AM03 (Subtilisin-like protease 1, PbSUB1) explicitly annotates position 286 as an Active site with description 'Charge relay system' (evidence C5/H6). The protein is EC 3.4.21.62, a subtilisin-type serine protease whose catalytic triad (Asp286-His342-Ser519) constitutes the charge relay system. The annotation is based on PROSITE-ProRule (ECO:0000255, computational/prorule evidence), which is consistent with the well-established subtilisin mechanism. The sequence confirms: position 286 is Asp (in IDSG context), 342 is His (in NHGSHVSG context), and 519 is Ser (in GTSMA context), matching the canonical subtilisin triad.",
    "evidence_ids": ["C5", "H6", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'GTSMA' motif (positions 517-521: G-T-S-M-A), which is the hallmark signature of subtilisin-type serine proteases' catalytic serine. This is an extremely well-known family-level sequence feature. Subtilisins catalyze via an Asp-His-Ser 'charge relay system' — this is the standard mechanistic terminology for this enzyme family. Option A ('Position 286, Charge relay system') matches both the family identification (subtilisin) and the correct mechanistic description. Options B and D ('beta-ketoacyl synthase') refer to fatty acid synthase, a completely different enzyme class with a Cys-His-His active site and no sequence similarity to subtilisins. Option C ('Proton acceptor') is generic terminology not associated with subtilisin catalysis. A model recognizing the GTSMA motif and knowing subtilisin mechanism can confidently select A and eliminate the others.",
    "missing_item_specific_fact": "",
    "reason": "The GTSMA motif is a universally recognized family signature for subtilisin-type proteases, and 'charge relay system' is the standard mechanistic descriptor for the subtilisin catalytic triad. This combination of family recognition (from the sequence) and mechanistic knowledge (from other subtilisin proteins) meaningfully and uniquely identifies option A among the four choices. No target-specific annotation lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A identifies a position that is an annotated active site with the correct functional description. Positions 180, 12, and 365 are not active sites, and their associated functions (beta-ketoacyl synthase, proton acceptor) are inconsistent with a subtilisin-type protease. The distractors are clearly eliminable by family recognition."
  },
  "important_caveats": [
    "The active site annotation at position 286 is based on PROSITE-ProRule (ECO:0000255), a computational/prorule inference, not direct experimental mutagenesis of this specific protein. However, it is consistent with the well-established subtilisin mechanism and the sequence context (IDSG motif).",
    "The question lists only one position per option, whereas the full catalytic center comprises three residues (286, 342, 519). The question format asks which single option correctly identifies an active site residue with its function, which is unambiguous.",
    "The protein identity (Plasmodium berghei SUB1) was not provided to the model; identification relies solely on sequence motif recognition, which is sufficient given the distinctive GTSMA motif."
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
  "requested_accession": "A0A509AM03",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "c5873da74b946ad1a9fd22f718bcaa153629124ee65112b496cac3092aaf6e26",
  "benchmark_sequence_length": 599,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 31,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-09-18",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "current_source_sequence_sha256": "c5873da74b946ad1a9fd22f718bcaa153629124ee65112b496cac3092aaf6e26",
  "current_source_sequence_length": 599,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 30,
  "selected_historical_version": {
    "accession": "A0A509AM03",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "SUB1_PLABA",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "selected_historical_source_sequence_sha256": "c5873da74b946ad1a9fd22f718bcaa153629124ee65112b496cac3092aaf6e26",
  "selected_historical_source_sequence_length": 599,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A509AM03\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":31,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-09-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000074855\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Vinckeia\"],\"scientificName\":\"Plasmodium berghei (strain Anka)\",\"taxonId\":5823}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24089525\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24348254\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30941868\",\"source\":\"PubMed\"}],\"value\":\"PbSUB1\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"}],\"value\":\"3.4.21.62\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24348254\",\"source\":\"PubMed\"}],\"value\":\"Subtilisin-like protease 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Charge relay system\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01240\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":286},\"start\":{\"modifier\":\"EXACT\",\"value\":286}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Charge relay system\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01240\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":342},\"start\":{\"modifier\":\"EXACT\",\"value\":342}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Charge relay system\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01240\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":519},\"start\":{\"modifier\":\"EXACT\",\"value\":519}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":123},\"start\":{\"modifier\":\"EXACT\",\"value\":123}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":126},\"start\":{\"modifier\":\"EXACT\",\"value\":126}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":128},\"start\":{\"modifier\":\"EXACT\",\"value\":128}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":183},\"start\":{\"modifier\":\"EXACT\",\"value\":183}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":251},\"start\":{\"modifier\":\"EXACT\",\"value\":251}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":295},\"start\":{\"modifier\":\"EXACT\",\"value\":295}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":306},\"start\":{\"modifier\":\"EXACT\",\"value\":306}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":306},\"start\":{\"modifier\":\"EXACT\",\"value\":306}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":314},\"start\":{\"modifier\":\"EXACT\",\"value\":314}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":315},\"start\":{\"modifier\":\"EXACT\",\"value\":315}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/18",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":316},\"start\":{\"modifier\":\"EXACT\",\"value\":316}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/19",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":318},\"start\":{\"modifier\":\"EXACT\",\"value\":318}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/20",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":320},\"start\":{\"modifier\":\"EXACT\",\"value\":320}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C21",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/21",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":322},\"start\":{\"modifier\":\"EXACT\",\"value\":322}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C22",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/22",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":323},\"start\":{\"modifier\":\"EXACT\",\"value\":323}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C23",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/23",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":353},\"start\":{\"modifier\":\"EXACT\",\"value\":353}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C24",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/24",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":356},\"start\":{\"modifier\":\"EXACT\",\"value\":356}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C25",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/25",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":358},\"start\":{\"modifier\":\"EXACT\",\"value\":358}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C26",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/26",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":360},\"start\":{\"modifier\":\"EXACT\",\"value\":360}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C27",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/features/27",
  "excerpt": "{\"description\":\"Cleavage\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":196},\"start\":{\"modifier\":\"EXACT\",\"value\":195}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C28",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Bouillon A.\",\"Giganti D.\",\"Benedet C.\",\"Gorgette O.\",\"Petres S.\",\"Crublet E.\",\"Girard-Blanc C.\",\"Witkowski B.\",\"Menard D.\",\"Nilges M.\",\"Mercereau-Puijalon O.\",\"Stoven V.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23653352\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m113.456764\"}],\"citationType\":\"journal article\",\"firstPage\":\"18561\",\"id\":\"23653352\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"18573\",\"publicationDate\":\"2013\",\"title\":\"In Silico screening on the three-dimensional model of the Plasmodium vivax SUB1 protease leads to the validation of a novel anti-parasite compound.\",\"volume\":\"288\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"PROTEOLYTIC CLEAVAGE\",\"CLEAVAGE SITE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C29",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Tawk L.\",\"Lacroix C.\",\"Gueirard P.\",\"Kent R.\",\"Gorgette O.\",\"Thiberge S.\",\"Mercereau-Puijalon O.\",\"Menard R.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24089525\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m113.513234\"}],\"citationType\":\"journal article\",\"firstPage\":\"33336\",\"id\":\"24089525\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"33346\",\"publicationDate\":\"2013\",\"title\":\"A key role for Plasmodium subtilisin-like SUB1 protease in egress of malaria parasites from host hepatocytes.\",\"volume\":\"288\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C30

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C30",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Suarez C.\",\"Volkmann K.\",\"Gomes A.R.\",\"Billker O.\",\"Blackman M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24348254\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1003811\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1003811\",\"id\":\"24348254\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1003811\",\"publicationDate\":\"2013\",\"title\":\"The malarial serine protease SUB1 plays an essential role in parasite liver stage development.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C31

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C31",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Pace T.\",\"Grasso F.\",\"Camarda G.\",\"Suarez C.\",\"Blackman M.J.\",\"Ponzi M.\",\"Olivieri A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30941868\"},{\"database\":\"DOI\",\"id\":\"10.1111/cmi.13028\"}],\"citationType\":\"journal article\",\"firstPage\":\"e13028\",\"id\":\"30941868\",\"journal\":\"Cell. Microbiol.\",\"lastPage\":\"e13028\",\"publicationDate\":\"2019\",\"title\":\"The Plasmodium berghei serine protease PbSUB1 plays an important role in male gamete egress.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   SUB1_PLABA              Reviewed;         599 AA.\nAC   A0A509AM03;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-SEP-2019, sequence version 1.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:24348254};\nDE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352};\nDE   AltName: Full=PbSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:24089525, ECO:0000303|PubMed:24348254, ECO:0000303|PubMed:30941868};\nDE   Flags: Precursor;\nGN   Name=SUB1 {ECO:0000305};\nGN   ORFNames=PBANKA_1107100 {ECO:0000312|EMBL:VUC56494.1};\nOS   Plasmodium berghei (strain Anka).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).\nOX   NCBI_TaxID=5823 {ECO:0000312|Proteomes:UP000074855};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 28-36",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, PROTEOLYTIC CLEAVAGE, AND CLEAVAGE SITE.\nRX   PubMed=23653352; DOI=10.1074/jbc.m113.456764;\nRA   Bouillon A., Giganti D., Benedet C., Gorgette O., Petres S., Crublet E.,\nRA   Girard-Blanc C., Witkowski B., Menard D., Nilges M., Mercereau-Puijalon O.,\nRA   Stoven V., Barale J.C.;\nRT   \"In Silico screening on the three-dimensional model of the Plasmodium vivax\nRT   SUB1 protease leads to the validation of a novel anti-parasite compound.\";\nRL   J. Biol. Chem. 288:18561-18573(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 37-44",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, DEVELOPMENTAL STAGE, AND DISRUPTION PHENOTYPE.\nRX   PubMed=24089525; DOI=10.1074/jbc.m113.513234;\nRA   Tawk L., Lacroix C., Gueirard P., Kent R., Gorgette O., Thiberge S.,\nRA   Mercereau-Puijalon O., Menard R., Barale J.C.;\nRT   \"A key role for Plasmodium subtilisin-like SUB1 protease in egress of\nRT   malaria parasites from host hepatocytes.\";\nRL   J. Biol. Chem. 288:33336-33346(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 45-52",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=24348254; DOI=10.1371/journal.ppat.1003811;\nRA   Suarez C., Volkmann K., Gomes A.R., Billker O., Blackman M.J.;\nRT   \"The malarial serine protease SUB1 plays an essential role in parasite\nRT   liver stage development.\";\nRL   PLoS Pathog. 9:e1003811-e1003811(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 53-61",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=30941868; DOI=10.1111/cmi.13028;\nRA   Pace T., Grasso F., Camarda G., Suarez C., Blackman M.J., Ponzi M.,\nRA   Olivieri A.;\nRT   \"The Plasmodium berghei serine protease PbSUB1 plays an important role in\nRT   male gamete egress.\";\nRL   Cell. Microbiol. 21:e13028-e13028(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 178-180",
  "excerpt": "FT   ACT_SITE        286\nFT                   /note=\"Charge relay system\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01240\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 181-183",
  "excerpt": "FT   ACT_SITE        342\nFT                   /note=\"Charge relay system\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01240\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 184-186",
  "excerpt": "FT   ACT_SITE        519\nFT                   /note=\"Charge relay system\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01240\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 187-191",
  "excerpt": "FT   BINDING         123\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 192-196",
  "excerpt": "FT   BINDING         126\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 197-201",
  "excerpt": "FT   BINDING         128\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 202-206",
  "excerpt": "FT   BINDING         183\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 207-211",
  "excerpt": "FT   BINDING         251\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 212-216",
  "excerpt": "FT   BINDING         295\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 217-221",
  "excerpt": "FT   BINDING         306\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 222-226",
  "excerpt": "FT   BINDING         306\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 227-231",
  "excerpt": "FT   BINDING         314\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 232-236",
  "excerpt": "FT   BINDING         315\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H19",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 237-241",
  "excerpt": "FT   BINDING         316\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H20",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 242-246",
  "excerpt": "FT   BINDING         318\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H21",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 247-251",
  "excerpt": "FT   BINDING         320\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H22",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 252-256",
  "excerpt": "FT   BINDING         322\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H23",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 257-261",
  "excerpt": "FT   BINDING         323\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H24",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 262-266",
  "excerpt": "FT   BINDING         353\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H25",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 267-271",
  "excerpt": "FT   BINDING         356\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H26",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 272-276",
  "excerpt": "FT   BINDING         358\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H27",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 277-281",
  "excerpt": "FT   BINDING         360\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H28

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "evidence_id": "H28",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "source_locator": "lines 282-284",
  "excerpt": "FT   SITE            195..196\nFT                   /note=\"Cleavage\"\nFT                   /evidence=\"ECO:0000269|PubMed:23653352\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 29. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
