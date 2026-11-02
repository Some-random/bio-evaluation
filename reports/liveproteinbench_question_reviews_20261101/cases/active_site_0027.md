# active_site_0027

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 153 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRYAVVTGVSSGIGKAICEKFLAKGLYVFGSVRKKEDAKYFEEKYPNTFHTLVFDTTDYPAVDKAVEEIHKVVGKKGLSVLVNNAGVAKYGPIQHVPIEELRQQYEVNVFASVYLTQKLLWLLGASKEAKWQGKVIQISSTAGVMTRPMLGPYSSSKHAVEAIYDALRRELMIYGVEVVLIEPGPIKTEIWGKAKSGGNPYKDTDYGEIFAQLDKAVDEIEKIGLPVEAVAGKAWEAFVAKKPKARYVVAPKKLMFKAAMYLIPDRMLDKIFYKDLKKLTQES

[Multiple Choices]
A. Position 31 (Proton donor)
B. Position 153 (Proton acceptor)
C. Position 405 (For beta-ketoacyl synthase 1 activity)
D. Position 184 (For beta-ketoacyl synthase activity)
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

### Expected-answer support: supported

> The exact-match UniProt record annotates position 153 as a proton acceptor, supporting choice B. This is a similarity-based annotation, not direct experimental confirmation in the supplied evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence length rules out position 405, and the enzyme annotation identifies a reductase rather than a beta-ketoacyl synthase. But the sequence and choices do not establish whether position 31 is a proton donor or position 153 is a proton acceptor.


**Missing item-specific fact**

> The protein-specific catalytic-site mapping that identifies residue 153 as the proton acceptor; the reviewer evidence traces this to a similarity-based UniProt annotation.


**Reason**

> Choosing B over A requires the specific site annotation or equivalent protein-specific functional evidence, which is not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports B; it does not establish another listed choice as a catalytic-site annotation for this sequence.


### Important caveats

- The active-site evidence is annotated by similarity (ECO:0000250), not shown here to be an experimental determination for this protein.
- The matched UniProt sequence identifies the protein as NADPH-dependent 3-dehydrocapnine reductase; the source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence length rules out position 405, and the enzyme annotation identifies a reductase rather than a beta-ketoacyl synthase. But the sequence and choices do not establish whether position 31 is a proton donor or position 153 is a proton acceptor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic-site mapping that identifies residue 153 as the proton acceptor; the reviewer evidence traces this to a similarity-based UniProt annotation.",
    "reason": "Choosing B over A requires the specific site annotation or equivalent protein-specific functional evidence, which is not supplied in the question."
  },
  "case_id": "active_site_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-match UniProt record annotates position 153 as a proton acceptor, supporting choice B. This is a similarity-based annotation, not direct experimental confirmation in the supplied evidence."
  },
  "important_caveats": [
    "The active-site evidence is annotated by similarity (ECO:0000250), not shown here to be an experimental determination for this protein.",
    "The matched UniProt sequence identifies the protein as NADPH-dependent 3-dehydrocapnine reductase; the source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B; it does not establish another listed choice as a catalytic-site annotation for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-match UniProt record annotates position 153 as a proton acceptor, supporting choice B. This is a similarity-based annotation, not direct experimental confirmation in the supplied evidence.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence length rules out position 405, and the enzyme annotation identifies a reductase rather than a beta-ketoacyl synthase. But the sequence and choices do not establish whether position 31 is a proton donor or position 153 is a proton acceptor.",
    "missing_item_specific_fact": "The protein-specific catalytic-site mapping that identifies residue 153 as the proton acceptor; the reviewer evidence traces this to a similarity-based UniProt annotation.",
    "reason": "Choosing B over A requires the specific site annotation or equivalent protein-specific functional evidence, which is not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B; it does not establish another listed choice as a catalytic-site annotation for this sequence."
  },
  "important_caveats": [
    "The active-site evidence is annotated by similarity (ECO:0000250), not shown here to be an experimental determination for this protein.",
    "The matched UniProt sequence identifies the protein as NADPH-dependent 3-dehydrocapnine reductase; the source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A3R5XUE6 (CAPC_ORNRH, NADPH-dependent 3-dehydrocapnine reductase, 283 aa) explicitly annotates position 153 as 'Proton acceptor' (Active site). The evidence code is ECO:0000250 (similarity to Q9BPW9), so this is a computational inference by homology rather than direct experimental measurement. However, the annotation is mechanistically consistent: the sequence contains the SDR-family Rossmann-fold motif TGxxxGxG (VSSGIGK at ~positions 7-13) and the catalytic tetrad pattern Tyr-X-X-X-Lys (Y153-S154-S155-S156-K157), which is the well-established SDR catalytic arrangement where the tyrosine serves as proton acceptor/donor. The sequence matches the benchmark input exactly (SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two hallmarks of the short-chain dehydrogenase/reductase (SDR) superfamily: (1) the N-terminal Rossmann-fold NAD(P)H-binding motif TGxxxGxG (visible as VSSGIGK at positions ~7-13), and (2) the canonical SDR catalytic tetrad Ser-Tyr-Lys-Asn with the diagnostic Tyr-X-X-X-Lys spacing (Y153-S154-S155-S156-K157). In SDR enzymes, the catalytic tyrosine acts as the proton acceptor during substrate oxidation and the lysine as the proton donor. A model familiar with SDR biochemistry can locate Y153 by scanning the C-terminal region for the Y-X-X-X-K pattern following the Rossmann motif. Additionally, the distractors are eliminable by general knowledge: option C cites position 405 in a 283-residue protein (impossible); option D invokes 'beta-ketoacyl synthase activity,' an entirely different enzyme class (FAS II condensing enzymes use an active-site Cys, not a Tyr); option A assigns 'proton donor' to Ser31, which contradicts the SDR mechanism where the proton donor is the catalytic Lys, not an N-terminal Ser.


**Missing item-specific fact**

> None strictly required. The SDR catalytic tetrad geometry and the Tyr-as-proton-acceptor role are general enzymology. The exact residue number 153 is derivable from the sequence by locating the Y-X-X-X-K motif after the Rossmann fold. However, a model without SDR-family knowledge would struggle to distinguish B from A on residue-role grounds alone.


**Reason**

> The answer can be reached through general SDR biochemistry: recognizing the TGxxxGxG motif, identifying the Y-X-X-X-K catalytic tetrad, and applying the well-known SDR mechanism (Tyr = proton acceptor, Lys = proton donor). The three distractors are eliminated by elementary checks (position out of range, wrong enzyme class, wrong residue-role assignment). This constitutes a concrete biological argument from the supplied sequence and choices, not a protein-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is physically impossible (position 405 exceeds the 283-residue length). Option D names a completely unrelated enzyme class (beta-ketoacyl synthase). Option A misassigns both the residue identity (Ser at 31) and the mechanistic role (proton donor belongs to Lys in SDR enzymes). Only option B is consistent with the SDR catalytic mechanism and the sequence features. No ambiguity among the options.


### Important caveats

- The UniProt active-site annotation at position 153 carries evidence code ECO:0000250 (similarity to Q9BPW9), meaning it is a computational inference by homology, not a direct experimental determination on this specific protein. The SDR catalytic mechanism is, however, experimentally established in many family members.
- The protein is annotated as EC 1.1.1.- (non-specific NADPH-dependent dehydrogenase/reductase); the exact substrate (3-dehydrocapnine) was characterized in PubMed:35414181, but the active-site residue assignment relies on family-level inference.
- The UniProt accession and annotation were reviewer-only; the evaluated model saw only the raw 283-aa sequence and the four options.
- Position numbering follows the canonical UniProt entry (sequence version 1, 283 aa), matching the benchmark input exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two hallmarks of the short-chain dehydrogenase/reductase (SDR) superfamily: (1) the N-terminal Rossmann-fold NAD(P)H-binding motif TGxxxGxG (visible as VSSGIGK at positions ~7-13), and (2) the canonical SDR catalytic tetrad Ser-Tyr-Lys-Asn with the diagnostic Tyr-X-X-X-Lys spacing (Y153-S154-S155-S156-K157). In SDR enzymes, the catalytic tyrosine acts as the proton acceptor during substrate oxidation and the lysine as the proton donor. A model familiar with SDR biochemistry can locate Y153 by scanning the C-terminal region for the Y-X-X-X-K pattern following the Rossmann motif. Additionally, the distractors are eliminable by general knowledge: option C cites position 405 in a 283-residue protein (impossible); option D invokes 'beta-ketoacyl synthase activity,' an entirely different enzyme class (FAS II condensing enzymes use an active-site Cys, not a Tyr); option A assigns 'proton donor' to Ser31, which contradicts the SDR mechanism where the proton donor is the catalytic Lys, not an N-terminal Ser.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The SDR catalytic tetrad geometry and the Tyr-as-proton-acceptor role are general enzymology. The exact residue number 153 is derivable from the sequence by locating the Y-X-X-X-K motif after the Rossmann fold. However, a model without SDR-family knowledge would struggle to distinguish B from A on residue-role grounds alone.",
    "reason": "The answer can be reached through general SDR biochemistry: recognizing the TGxxxGxG motif, identifying the Y-X-X-X-K catalytic tetrad, and applying the well-known SDR mechanism (Tyr = proton acceptor, Lys = proton donor). The three distractors are eliminated by elementary checks (position out of range, wrong enzyme class, wrong residue-role assignment). This constitutes a concrete biological argument from the supplied sequence and choices, not a protein-specific lookup."
  },
  "case_id": "active_site_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A3R5XUE6 (CAPC_ORNRH, NADPH-dependent 3-dehydrocapnine reductase, 283 aa) explicitly annotates position 153 as 'Proton acceptor' (Active site). The evidence code is ECO:0000250 (similarity to Q9BPW9), so this is a computational inference by homology rather than direct experimental measurement. However, the annotation is mechanistically consistent: the sequence contains the SDR-family Rossmann-fold motif TGxxxGxG (VSSGIGK at ~positions 7-13) and the catalytic tetrad pattern Tyr-X-X-X-Lys (Y153-S154-S155-S156-K157), which is the well-established SDR catalytic arrangement where the tyrosine serves as proton acceptor/donor. The sequence matches the benchmark input exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt active-site annotation at position 153 carries evidence code ECO:0000250 (similarity to Q9BPW9), meaning it is a computational inference by homology, not a direct experimental determination on this specific protein. The SDR catalytic mechanism is, however, experimentally established in many family members.",
    "The protein is annotated as EC 1.1.1.- (non-specific NADPH-dependent dehydrogenase/reductase); the exact substrate (3-dehydrocapnine) was characterized in PubMed:35414181, but the active-site residue assignment relies on family-level inference.",
    "The UniProt accession and annotation were reviewer-only; the evaluated model saw only the raw 283-aa sequence and the four options.",
    "Position numbering follows the canonical UniProt entry (sequence version 1, 283 aa), matching the benchmark input exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is physically impossible (position 405 exceeds the 283-residue length). Option D names a completely unrelated enzyme class (beta-ketoacyl synthase). Option A misassigns both the residue identity (Ser at 31) and the mechanistic role (proton donor belongs to Lys in SDR enzymes). Only option B is consistent with the SDR catalytic mechanism and the sequence features. No ambiguity among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A3R5XUE6 (CAPC_ORNRH, NADPH-dependent 3-dehydrocapnine reductase, 283 aa) explicitly annotates position 153 as 'Proton acceptor' (Active site). The evidence code is ECO:0000250 (similarity to Q9BPW9), so this is a computational inference by homology rather than direct experimental measurement. However, the annotation is mechanistically consistent: the sequence contains the SDR-family Rossmann-fold motif TGxxxGxG (VSSGIGK at ~positions 7-13) and the catalytic tetrad pattern Tyr-X-X-X-Lys (Y153-S154-S155-S156-K157), which is the well-established SDR catalytic arrangement where the tyrosine serves as proton acceptor/donor. The sequence matches the benchmark input exactly (SHA-256 confirmed).",
    "evidence_ids": ["C5", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two hallmarks of the short-chain dehydrogenase/reductase (SDR) superfamily: (1) the N-terminal Rossmann-fold NAD(P)H-binding motif TGxxxGxG (visible as VSSGIGK at positions ~7-13), and (2) the canonical SDR catalytic tetrad Ser-Tyr-Lys-Asn with the diagnostic Tyr-X-X-X-Lys spacing (Y153-S154-S155-S156-K157). In SDR enzymes, the catalytic tyrosine acts as the proton acceptor during substrate oxidation and the lysine as the proton donor. A model familiar with SDR biochemistry can locate Y153 by scanning the C-terminal region for the Y-X-X-X-K pattern following the Rossmann motif. Additionally, the distractors are eliminable by general knowledge: option C cites position 405 in a 283-residue protein (impossible); option D invokes 'beta-ketoacyl synthase activity,' an entirely different enzyme class (FAS II condensing enzymes use an active-site Cys, not a Tyr); option A assigns 'proton donor' to Ser31, which contradicts the SDR mechanism where the proton donor is the catalytic Lys, not an N-terminal Ser.",
    "missing_item_specific_fact": "None strictly required. The SDR catalytic tetrad geometry and the Tyr-as-proton-acceptor role are general enzymology. The exact residue number 153 is derivable from the sequence by locating the Y-X-X-X-K motif after the Rossmann fold. However, a model without SDR-family knowledge would struggle to distinguish B from A on residue-role grounds alone.",
    "reason": "The answer can be reached through general SDR biochemistry: recognizing the TGxxxGxG motif, identifying the Y-X-X-X-K catalytic tetrad, and applying the well-known SDR mechanism (Tyr = proton acceptor, Lys = proton donor). The three distractors are eliminated by elementary checks (position out of range, wrong enzyme class, wrong residue-role assignment). This constitutes a concrete biological argument from the supplied sequence and choices, not a protein-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is physically impossible (position 405 exceeds the 283-residue length). Option D names a completely unrelated enzyme class (beta-ketoacyl synthase). Option A misassigns both the residue identity (Ser at 31) and the mechanistic role (proton donor belongs to Lys in SDR enzymes). Only option B is consistent with the SDR catalytic mechanism and the sequence features. No ambiguity among the options."
  },
  "important_caveats": [
    "The UniProt active-site annotation at position 153 carries evidence code ECO:0000250 (similarity to Q9BPW9), meaning it is a computational inference by homology, not a direct experimental determination on this specific protein. The SDR catalytic mechanism is, however, experimentally established in many family members.",
    "The protein is annotated as EC 1.1.1.- (non-specific NADPH-dependent dehydrogenase/reductase); the exact substrate (3-dehydrocapnine) was characterized in PubMed:35414181, but the active-site residue assignment relies on family-level inference.",
    "The UniProt accession and annotation were reviewer-only; the evaluated model saw only the raw 283-aa sequence and the four options.",
    "Position numbering follows the canonical UniProt entry (sequence version 1, 283 aa), matching the benchmark input exactly."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A3R5XUE6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 16. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.269818+00:00.  

```json
"A0A3R5XUE6"
```

Source SHA-256: `eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.269818+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35414181","source":"PubMed"}],"value":"1.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35414181","source":"PubMed"}],"value":"NADPH-dependent 3-dehydrocapnine reductase"}}}
```

Source SHA-256: `eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.269818+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPW9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":153},"start":{"modifier":"EXACT","value":153}},"type":"Active site"}
```

Source SHA-256: `eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.269818+00:00.  

```json
{"citation":{"authors":["Liu Y.","Wei Y.","Teh T.M.","Liu D.","Zhou Y.","Zhao S.","Ang E.L.","Zhao H.","Zhang Y."],"citationCrossReferences":[{"database":"PubMed","id":"35414181"},{"database":"DOI","id":"10.1021/acs.biochem.2c00102"}],"citationType":"journal article","firstPage":"2861","id":"35414181","journal":"Biochemistry","lastPage":"2869","publicationDate":"2022","title":"Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine.","volume":"61"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)  
**Locator:** `lines 72-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:30.826829+00:00.  

```text
FT   ACT_SITE        153
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000250|UniProtKB:Q9BPW9"
```

Source SHA-256: `6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
