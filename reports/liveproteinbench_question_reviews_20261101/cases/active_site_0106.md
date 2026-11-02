# active_site_0106

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **A** — Position 237 (Proton donor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTGFLPEPLRMLVTSPALLDFTSDGPLPYALRQKFTGKPPPVTSNLSLASQTVLVTGATSGVGLEAARQLAQLGPRLLILGVRNASKAEQIKSELERDTPNLTVQVAELDLESLLSVDRFVDELSANSIRLDLALLNAGFFAHDDRITDDGYSPLFQVNFLSTAYLTLKLLPLLHTTAPPHPPGTTTPPGPRLVLVTSEAHAWTTFPDVPRPTENRTQPILSVFQDKNTLGSADDQYARAKLLLALFGKELSRRLTAAENDTTVVITTPGFCASNFFPDGMMTRLIQLTSARSVQQGGALHVFAATAPGPEIHGAYLRDGKPTGLSKFAQGPQGQILQERLWGEMEEFFMQRGGSPLGM

[Multiple Choices]
A. Position 237 (Proton donor)
B. Position 154 (Acyl-thioester intermediate)
C. Position 458 (For beta-ketoacyl synthase activity)
D. Position 215 (Charge relay system)
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The supplied sequence has leucine at position 237, whose side chain is not a plausible catalytic proton donor. UniProt annotates that position as a proton donor, but the feature is transferred by similarity from another protein, not direct experimental evidence for this sequence; the annotation conflicts with the residue identity.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a dehydrogenase, which makes a proton-donor role broadly plausible, but it does not provide a defensible basis for assigning that role to position 237; that residue is leucine.


**Missing item-specific fact**

> A reliable, sequence-specific experimental or validated annotation of the active-site residues is absent. The available position-237 annotation is homology-transferred and conflicts with the sequence residue.


**Reason**

> Identifying a precise active-site position requires protein-specific information not established by the prompt. Recognizing a broad enzyme family or using generic catalytic-residue patterns cannot justify the listed position.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence does not support the keyed proton-donor assignment at position 237, and no other option is established by the supplied information. Position 458 also lies beyond the 359-residue sequence.


### Important caveats

- The database annotation explicitly labels position 237 as a proton donor, but its evidence is transferred from UniProtKB:O93868 rather than shown to be experimentally verified in this protein.
- The sequence match and annotation do not resolve the discrepancy between the annotated role and leucine at position 237.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a dehydrogenase, which makes a proton-donor role broadly plausible, but it does not provide a defensible basis for assigning that role to position 237; that residue is leucine.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A reliable, sequence-specific experimental or validated annotation of the active-site residues is absent. The available position-237 annotation is homology-transferred and conflicts with the sequence residue.",
    "reason": "Identifying a precise active-site position requires protein-specific information not established by the prompt. Recognizing a broad enzyme family or using generic catalytic-residue patterns cannot justify the listed position."
  },
  "case_id": "active_site_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "contradicted",
    "reason": "The supplied sequence has leucine at position 237, whose side chain is not a plausible catalytic proton donor. UniProt annotates that position as a proton donor, but the feature is transferred by similarity from another protein, not direct experimental evidence for this sequence; the annotation conflicts with the residue identity."
  },
  "important_caveats": [
    "The database annotation explicitly labels position 237 as a proton donor, but its evidence is transferred from UniProtKB:O93868 rather than shown to be experimentally verified in this protein.",
    "The sequence match and annotation do not resolve the discrepancy between the annotated role and leucine at position 237."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not support the keyed proton-donor assignment at position 237, and no other option is established by the supplied information. Position 458 also lies beyond the 359-residue sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0106",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The supplied sequence has leucine at position 237, whose side chain is not a plausible catalytic proton donor. UniProt annotates that position as a proton donor, but the feature is transferred by similarity from another protein, not direct experimental evidence for this sequence; the annotation conflicts with the residue identity.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a dehydrogenase, which makes a proton-donor role broadly plausible, but it does not provide a defensible basis for assigning that role to position 237; that residue is leucine.",
    "missing_item_specific_fact": "A reliable, sequence-specific experimental or validated annotation of the active-site residues is absent. The available position-237 annotation is homology-transferred and conflicts with the sequence residue.",
    "reason": "Identifying a precise active-site position requires protein-specific information not established by the prompt. Recognizing a broad enzyme family or using generic catalytic-residue patterns cannot justify the listed position."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not support the keyed proton-donor assignment at position 237, and no other option is established by the supplied information. Position 458 also lies beyond the 359-residue sequence."
  },
  "important_caveats": [
    "The database annotation explicitly labels position 237 as a proton donor, but its evidence is transferred from UniProtKB:O93868 rather than shown to be experimentally verified in this protein.",
    "The sequence match and annotation do not resolve the discrepancy between the annotated role and leucine at position 237."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXW2 (RESG_ASPSL, short-chain dehydrogenase resG from Aspergillus sclerotiorum) annotates position 237 as an Active site with description 'Proton donor' (evidence ECO:0000250, transferred by similarity from O93868). The residue at position 237 in the supplied 359-aa sequence is Tyrosine (Y), consistent with the well-established SDR catalytic Tyr that acts as the proton donor/acceptor in the NAD(P)-dependent oxidation-reduction mechanism. Position 241 (Lys) is annotated as 'Lowers pKa of active site Tyr,' completing the canonical SDR Tyr-Lys dyad. The annotation is similarity-based (ECO:0000250), not direct experimental evidence for this specific protein, but the SDR catalytic mechanism is well-established biochemistry.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [C4](#evidence-c4), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable SDR/Rossmann-fold motifs (e.g., GATSG at ~57-61, GVRNASKAEQ at ~81-90), indicating an NAD(P)-dependent short-chain dehydrogenase/reductase. SDR enzymes use a well-characterized catalytic tetrad (Ser-Tyr-Lys-Asn) in which the Tyr acts as the proton donor and the Lys lowers its pKa. Option A ('Proton donor') matches this mechanism exactly. Option B ('Acyl-thioester intermediate') describes a mechanism of fatty-acid synthases or thioesterases, not SDRs. Option D ('Charge relay system') describes the Ser-His-Asp triad of serine proteases, not SDRs. Option C references position 458, which exceeds the 359-residue sequence length and is trivially eliminable. Thus, recognizing the SDR fold and knowing its catalytic mechanism provides concrete grounds to select A and reject B, C, and D.


**Missing item-specific fact**

> Pinpointing the exact residue number 237 (rather than another Tyr in the sequence) benefits from structural knowledge of where the catalytic Tyr-Lys dyad sits relative to the NAD-binding Rossmann fold, but the mechanistic labels in the options allow elimination of all other choices even without independently identifying the exact position.


**Reason**

> The question is answerable through general SDR biochemistry: fold recognition from sequence motifs, knowledge that the catalytic Tyr is the proton donor, and elimination of distractors using incompatible enzyme-class terminology or an out-of-range position. This constitutes a concrete biological argument rather than pure memorization of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is eliminated by sequence length (359 < 458). Options B and D use mechanistic terminology (acyl-thioester intermediate, charge relay system) that belongs to entirely different enzyme classes (FAS/thioesterases and serine proteases, respectively) and is incompatible with SDR catalysis. Only option A uses terminology ('Proton donor') consistent with the SDR Tyr mechanism. No ambiguity among the remaining choices.


### Important caveats

- The UniProt annotation for position 237 carries evidence code ECO:0000250 (similarity), meaning it is transferred from O93868 by computational inference, not directly experimentally validated for this specific protein.
- The protein was first publicly released in UniProt on 2025-02-05; the author's source snapshot date is unknown, so the annotation available at benchmark construction time may differ from the current entry.
- The sequence-match is confirmed (SHA-256 identical between benchmark input and UniProt entry), so positional numbering is consistent.
- The question asks for 'the enzyme's catalytic center' but only one residue is listed per option; the full SDR catalytic tetrad (Ser, Tyr, Lys, Asn) is not represented in any single option, though the question's format (single best answer) accommodates this.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable SDR/Rossmann-fold motifs (e.g., GATSG at ~57-61, GVRNASKAEQ at ~81-90), indicating an NAD(P)-dependent short-chain dehydrogenase/reductase. SDR enzymes use a well-characterized catalytic tetrad (Ser-Tyr-Lys-Asn) in which the Tyr acts as the proton donor and the Lys lowers its pKa. Option A ('Proton donor') matches this mechanism exactly. Option B ('Acyl-thioester intermediate') describes a mechanism of fatty-acid synthases or thioesterases, not SDRs. Option D ('Charge relay system') describes the Ser-His-Asp triad of serine proteases, not SDRs. Option C references position 458, which exceeds the 359-residue sequence length and is trivially eliminable. Thus, recognizing the SDR fold and knowing its catalytic mechanism provides concrete grounds to select A and reject B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Pinpointing the exact residue number 237 (rather than another Tyr in the sequence) benefits from structural knowledge of where the catalytic Tyr-Lys dyad sits relative to the NAD-binding Rossmann fold, but the mechanistic labels in the options allow elimination of all other choices even without independently identifying the exact position.",
    "reason": "The question is answerable through general SDR biochemistry: fold recognition from sequence motifs, knowledge that the catalytic Tyr is the proton donor, and elimination of distractors using incompatible enzyme-class terminology or an out-of-range position. This constitutes a concrete biological argument rather than pure memorization of a database entry."
  },
  "case_id": "active_site_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4",
      "C4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXW2 (RESG_ASPSL, short-chain dehydrogenase resG from Aspergillus sclerotiorum) annotates position 237 as an Active site with description 'Proton donor' (evidence ECO:0000250, transferred by similarity from O93868). The residue at position 237 in the supplied 359-aa sequence is Tyrosine (Y), consistent with the well-established SDR catalytic Tyr that acts as the proton donor/acceptor in the NAD(P)-dependent oxidation-reduction mechanism. Position 241 (Lys) is annotated as 'Lowers pKa of active site Tyr,' completing the canonical SDR Tyr-Lys dyad. The annotation is similarity-based (ECO:0000250), not direct experimental evidence for this specific protein, but the SDR catalytic mechanism is well-established biochemistry."
  },
  "important_caveats": [
    "The UniProt annotation for position 237 carries evidence code ECO:0000250 (similarity), meaning it is transferred from O93868 by computational inference, not directly experimentally validated for this specific protein.",
    "The protein was first publicly released in UniProt on 2025-02-05; the author's source snapshot date is unknown, so the annotation available at benchmark construction time may differ from the current entry.",
    "The sequence-match is confirmed (SHA-256 identical between benchmark input and UniProt entry), so positional numbering is consistent.",
    "The question asks for 'the enzyme's catalytic center' but only one residue is listed per option; the full SDR catalytic tetrad (Ser, Tyr, Lys, Asn) is not represented in any single option, though the question's format (single best answer) accommodates this."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is eliminated by sequence length (359 < 458). Options B and D use mechanistic terminology (acyl-thioester intermediate, charge relay system) that belongs to entirely different enzyme classes (FAS/thioesterases and serine proteases, respectively) and is incompatible with SDR catalysis. Only option A uses terminology ('Proton donor') consistent with the SDR Tyr mechanism. No ambiguity among the remaining choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXW2 (RESG_ASPSL, short-chain dehydrogenase resG from Aspergillus sclerotiorum) annotates position 237 as an Active site with description 'Proton donor' (evidence ECO:0000250, transferred by similarity from O93868). The residue at position 237 in the supplied 359-aa sequence is Tyrosine (Y), consistent with the well-established SDR catalytic Tyr that acts as the proton donor/acceptor in the NAD(P)-dependent oxidation-reduction mechanism. Position 241 (Lys) is annotated as 'Lowers pKa of active site Tyr,' completing the canonical SDR Tyr-Lys dyad. The annotation is similarity-based (ECO:0000250), not direct experimental evidence for this specific protein, but the SDR catalytic mechanism is well-established biochemistry.",
    "evidence_ids": ["C5", "H3", "C6", "H4", "C4", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable SDR/Rossmann-fold motifs (e.g., GATSG at ~57-61, GVRNASKAEQ at ~81-90), indicating an NAD(P)-dependent short-chain dehydrogenase/reductase. SDR enzymes use a well-characterized catalytic tetrad (Ser-Tyr-Lys-Asn) in which the Tyr acts as the proton donor and the Lys lowers its pKa. Option A ('Proton donor') matches this mechanism exactly. Option B ('Acyl-thioester intermediate') describes a mechanism of fatty-acid synthases or thioesterases, not SDRs. Option D ('Charge relay system') describes the Ser-His-Asp triad of serine proteases, not SDRs. Option C references position 458, which exceeds the 359-residue sequence length and is trivially eliminable. Thus, recognizing the SDR fold and knowing its catalytic mechanism provides concrete grounds to select A and reject B, C, and D.",
    "missing_item_specific_fact": "Pinpointing the exact residue number 237 (rather than another Tyr in the sequence) benefits from structural knowledge of where the catalytic Tyr-Lys dyad sits relative to the NAD-binding Rossmann fold, but the mechanistic labels in the options allow elimination of all other choices even without independently identifying the exact position.",
    "reason": "The question is answerable through general SDR biochemistry: fold recognition from sequence motifs, knowledge that the catalytic Tyr is the proton donor, and elimination of distractors using incompatible enzyme-class terminology or an out-of-range position. This constitutes a concrete biological argument rather than pure memorization of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is eliminated by sequence length (359 < 458). Options B and D use mechanistic terminology (acyl-thioester intermediate, charge relay system) that belongs to entirely different enzyme classes (FAS/thioesterases and serine proteases, respectively) and is incompatible with SDR catalysis. Only option A uses terminology ('Proton donor') consistent with the SDR Tyr mechanism. No ambiguity among the remaining choices."
  },
  "important_caveats": [
    "The UniProt annotation for position 237 carries evidence code ECO:0000250 (similarity), meaning it is transferred from O93868 by computational inference, not directly experimentally validated for this specific protein.",
    "The protein was first publicly released in UniProt on 2025-02-05; the author's source snapshot date is unknown, so the annotation available at benchmark construction time may differ from the current entry.",
    "The sequence-match is confirmed (SHA-256 identical between benchmark input and UniProt entry), so positional numbering is consistent.",
    "The question asks for 'the enzyme's catalytic center' but only one residue is listed per option; the full SDR catalytic tetrad (Ser, Tyr, Lys, Asn) is not represented in any single option, though the question's format (single best answer) accommodates this."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `model_residue_identity_error`.

> The original frozen sequence uses1-based Y237, not leucine. C5/H3 annotate237 as proton donor by similarity. The model contradiction argument relies on a false residue identity.

**Remaining uncertainty:** This invalidates that stated argument only; the similarity-transferred active-site annotation is not direct validation of the exact residue function.

**Direct check of the original sequence:**

```json
{
  "indexing": "1-based",
  "length": 359,
  "residues": {
    "237": "Y"
  },
  "sha256": "00a67859bfb5799f648543ed75c5168c3c4cc678d78363e0f961ad4cc8caaf9d"
}
```

Evidence checked: [C5](#evidence-c5), [H3](#evidence-h3).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `P0DXW2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:52.717483+00:00.  

```json
"P0DXW2"
```

Source SHA-256: `49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:52.717483+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein G"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"value":"1.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Short chain dehydrogenase resG"}}}
```

Source SHA-256: `49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:52.717483+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000250","id":"O93868","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":237},"start":{"modifier":"EXACT","value":237}},"type":"Active site"}
```

Source SHA-256: `49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:52.717483+00:00.  

```json
{"description":"Lowers pKa of active site Tyr","evidences":[{"evidenceCode":"ECO:0000250","id":"O93868","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":241},"start":{"modifier":"EXACT","value":241}},"type":"Active site"}
```

Source SHA-256: `49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)  
**Locator:** `lines 60-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:57.835506+00:00.  

```text
FT   ACT_SITE        237
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000250|UniProtKB:O93868"
```

Source SHA-256: `4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)  
**Locator:** `lines 63-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:57.835506+00:00.  

```text
FT   ACT_SITE        241
FT                   /note="Lowers pKa of active site Tyr"
FT                   /evidence="ECO:0000250|UniProtKB:O93868"
```

Source SHA-256: `4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
