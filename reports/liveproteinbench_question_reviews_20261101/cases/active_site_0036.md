# active_site_0036

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 327 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTIRGTLSELSRAADAFAHEVDEAGYGDYTFLPDNSPFDLSFLTSKGLEARGSLIAAAEKILRLAKGPQGCLASFADTKGIEMGTIQALTQLEVPDKVPLQGSITYEELAGVIRVAPELLQRLVRLAALAGFLIEDESGAVRHTAMSAVFLRDTAAGDTARFLFDVDMRAYSFFADSLRLDPSGQNIGDGPTALAFQHDSDDQGNRPTIWDILERNPIQRARFHSTMQALGSFPSHLLKHILVAHDWHSIGSLVDVGGSLGHASLVIAENFPEIRITVQDLPDVVERGRSSLPTVPHAERVSFQAHDLFQEQAIIADAYFLRQILHDWPDGDAERIVRCLIPAMRPGAKLLIMDIVVPEPGAISPYMEKYLRTYDVSMFSMFSAKERTVQQLRDLVERCSARLQFQGISCPPGSATSLLSWVYSAE

[Multiple Choices]
A. Position 2723 (Proton acceptor; for dehydratase activity 2)
B. Position 327 (Proton acceptor)
C. Position 180 (For beta-ketoacyl synthase activity)
D. Position 161 (Proton donor)
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

> The sequence matches the UniProt entry for O-methyltransferase FrzF, which annotates residue 327 as a proton acceptor. This supports choice B as a database annotation, but the site assignment is attributed to a PROSITE-ProRule computational annotation, not experimental evidence in the supplied record.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence length rules out position 2723, and the enzyme annotation identifies an O-methyltransferase rather than a beta-ketoacyl synthase. Those clues do not establish which specific residue is the proton acceptor.


**Missing item-specific fact**

> The residue-level assignment that position 327 is a proton acceptor, supplied here by a protein-specific PROSITE-ProRule annotation.


**Reason**

> General sequence reasoning may suggest enzyme-family features, but it does not reliably distinguish the catalytic role of residue 327 from the proposed role at position 161.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports B. The other options are not supported by the excerpts; in particular, position 2723 exceeds the sequence length. The excerpts do not establish that another listed residue is also catalytic.


### Important caveats

- The sequence match and historical record support that the annotation applies to this sequence, but the actual author source snapshot is unknown.
- The proton-acceptor assignment is computationally annotated; the supplied evidence does not independently verify it experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence length rules out position 2723, and the enzyme annotation identifies an O-methyltransferase rather than a beta-ketoacyl synthase. Those clues do not establish which specific residue is the proton acceptor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The residue-level assignment that position 327 is a proton acceptor, supplied here by a protein-specific PROSITE-ProRule annotation.",
    "reason": "General sequence reasoning may suggest enzyme-family features, but it does not reliably distinguish the catalytic role of residue 327 from the proposed role at position 161."
  },
  "case_id": "active_site_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for O-methyltransferase FrzF, which annotates residue 327 as a proton acceptor. This supports choice B as a database annotation, but the site assignment is attributed to a PROSITE-ProRule computational annotation, not experimental evidence in the supplied record."
  },
  "important_caveats": [
    "The sequence match and historical record support that the annotation applies to this sequence, but the actual author source snapshot is unknown.",
    "The proton-acceptor assignment is computationally annotated; the supplied evidence does not independently verify it experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B. The other options are not supported by the excerpts; in particular, position 2723 exceeds the sequence length. The excerpts do not establish that another listed residue is also catalytic."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for O-methyltransferase FrzF, which annotates residue 327 as a proton acceptor. This supports choice B as a database annotation, but the site assignment is attributed to a PROSITE-ProRule computational annotation, not experimental evidence in the supplied record.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence length rules out position 2723, and the enzyme annotation identifies an O-methyltransferase rather than a beta-ketoacyl synthase. Those clues do not establish which specific residue is the proton acceptor.",
    "missing_item_specific_fact": "The residue-level assignment that position 327 is a proton acceptor, supplied here by a protein-specific PROSITE-ProRule annotation.",
    "reason": "General sequence reasoning may suggest enzyme-family features, but it does not reliably distinguish the catalytic role of residue 327 from the proposed role at position 161."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B. The other options are not supported by the excerpts; in particular, position 2723 exceeds the sequence length. The excerpts do not establish that another listed residue is also catalytic."
  },
  "important_caveats": [
    "The sequence match and historical record support that the annotation applies to this sequence, but the actual author source snapshot is unknown.",
    "The proton-acceptor assignment is computationally annotated; the supplied evidence does not independently verify it experimentally."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A7T8J1Z8 (O-methyltransferase FrzF, 427 aa, sequence matched) explicitly annotates position 327 as an Active site with description 'Proton acceptor' (evidence_id C5, H3). The evidence code is ECO:0000255 (inferred by sequence analysis via PROSITE-ProRule PRU01020), making this a computational/pattern-based annotation rather than experimentally validated, but it is the authoritative database annotation for this entry. The protein is an O-methyltransferase (EC 2.1.1.-) that uses SAM (binding site at position 281, C6/H4), and a proton-accepting residue at the catalytic center is mechanistically consistent with methyltransferase chemistry (deprotonating the substrate hydroxyl to enable nucleophilic attack on SAM's methyl group). Position 327 in the provided 427-aa sequence corresponds to a histidine residue, which can serve as a general base in some methyltransferase subfamilies.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is an O-methyltransferase (identifiable from the SAM-binding motif 'VDVGGSLGH' and overall fold context). Methyltransferases require a proton acceptor (general base) at the catalytic center to deprotonate the substrate's hydroxyl/amino group, enabling nucleophilic attack on the methyl group of SAM. This eliminates option D ('Proton donor'), which describes the opposite mechanistic role. Option A (position 2723) is arithmetically impossible in a 427-residue protein. Option C references 'beta-ketoacyl synthase activity,' an entirely unrelated enzyme class (type I/II fatty acid synthase), irrelevant to an O-methyltransferase. By elimination of A (out of range), C (wrong enzyme class), and D (wrong catalytic role), option B is the only biologically coherent choice.


**Missing item-specific fact**

> The exact residue number 327 is a database annotation fact not derivable from first principles; however, it is determined by elimination since all other options are independently falsifiable by general biological reasoning.


**Reason**

> The functional descriptor 'Proton acceptor' is derivable from methyltransferase catalytic mechanism. The position 327 itself is a database fact, but since the three distractors are eliminable by arithmetic (A: 2723 > 427), enzyme-class knowledge (C: beta-ketoacyl synthase ≠ methyltransferase), and mechanistic reasoning (D: donor vs. acceptor), the correct answer is reachable without memorizing the specific annotation. The reasoning chain is concrete and does not require recognizing the exact sequence or recalling a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor is independently falsifiable: A is out of range for a 427-aa protein; C references a completely different enzyme class; D assigns the wrong mechanistic role (proton donor instead of acceptor). Only B survives elimination. No ambiguity remains.


### Important caveats

- The active-site annotation at position 327 carries evidence code ECO:0000255 (inferred by sequence analysis via PROSITE-ProRule PRU01020), meaning it is a computational/pattern-based prediction, not an experimentally determined catalytic residue. No mutagenesis or kinetic data specific to this residue in FrzF was found in the supplied evidence.
- The PROSITE-ProRule annotation is transferred by profile similarity; the actual catalytic mechanism of FrzF (position 327, a histidine) has not been independently validated in the cited primary literature (PubMed 33372776) beyond general pathway reconstitution.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and the UniProt entry, and the historical (v19) and current (v21) annotations both list ACT_SITE 327 as 'Proton acceptor.'
- The identity of the protein (accession A0A7T8J1Z8) was inferred mechanically by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is an O-methyltransferase (identifiable from the SAM-binding motif 'VDVGGSLGH' and overall fold context). Methyltransferases require a proton acceptor (general base) at the catalytic center to deprotonate the substrate's hydroxyl/amino group, enabling nucleophilic attack on the methyl group of SAM. This eliminates option D ('Proton donor'), which describes the opposite mechanistic role. Option A (position 2723) is arithmetically impossible in a 427-residue protein. Option C references 'beta-ketoacyl synthase activity,' an entirely unrelated enzyme class (type I/II fatty acid synthase), irrelevant to an O-methyltransferase. By elimination of A (out of range), C (wrong enzyme class), and D (wrong catalytic role), option B is the only biologically coherent choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact residue number 327 is a database annotation fact not derivable from first principles; however, it is determined by elimination since all other options are independently falsifiable by general biological reasoning.",
    "reason": "The functional descriptor 'Proton acceptor' is derivable from methyltransferase catalytic mechanism. The position 327 itself is a database fact, but since the three distractors are eliminable by arithmetic (A: 2723 > 427), enzyme-class knowledge (C: beta-ketoacyl synthase ≠ methyltransferase), and mechanistic reasoning (D: donor vs. acceptor), the correct answer is reachable without memorizing the specific annotation. The reasoning chain is concrete and does not require recognizing the exact sequence or recalling a database entry."
  },
  "case_id": "active_site_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A7T8J1Z8 (O-methyltransferase FrzF, 427 aa, sequence matched) explicitly annotates position 327 as an Active site with description 'Proton acceptor' (evidence_id C5, H3). The evidence code is ECO:0000255 (inferred by sequence analysis via PROSITE-ProRule PRU01020), making this a computational/pattern-based annotation rather than experimentally validated, but it is the authoritative database annotation for this entry. The protein is an O-methyltransferase (EC 2.1.1.-) that uses SAM (binding site at position 281, C6/H4), and a proton-accepting residue at the catalytic center is mechanistically consistent with methyltransferase chemistry (deprotonating the substrate hydroxyl to enable nucleophilic attack on SAM's methyl group). Position 327 in the provided 427-aa sequence corresponds to a histidine residue, which can serve as a general base in some methyltransferase subfamilies."
  },
  "important_caveats": [
    "The active-site annotation at position 327 carries evidence code ECO:0000255 (inferred by sequence analysis via PROSITE-ProRule PRU01020), meaning it is a computational/pattern-based prediction, not an experimentally determined catalytic residue. No mutagenesis or kinetic data specific to this residue in FrzF was found in the supplied evidence.",
    "The PROSITE-ProRule annotation is transferred by profile similarity; the actual catalytic mechanism of FrzF (position 327, a histidine) has not been independently validated in the cited primary literature (PubMed 33372776) beyond general pathway reconstitution.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and the UniProt entry, and the historical (v19) and current (v21) annotations both list ACT_SITE 327 as 'Proton acceptor.'",
    "The identity of the protein (accession A0A7T8J1Z8) was inferred mechanically by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor is independently falsifiable: A is out of range for a 427-aa protein; C references a completely different enzyme class; D assigns the wrong mechanistic role (proton donor instead of acceptor). Only B survives elimination. No ambiguity remains."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A7T8J1Z8 (O-methyltransferase FrzF, 427 aa, sequence matched) explicitly annotates position 327 as an Active site with description 'Proton acceptor' (evidence_id C5, H3). The evidence code is ECO:0000255 (inferred by sequence analysis via PROSITE-ProRule PRU01020), making this a computational/pattern-based annotation rather than experimentally validated, but it is the authoritative database annotation for this entry. The protein is an O-methyltransferase (EC 2.1.1.-) that uses SAM (binding site at position 281, C6/H4), and a proton-accepting residue at the catalytic center is mechanistically consistent with methyltransferase chemistry (deprotonating the substrate hydroxyl to enable nucleophilic attack on SAM's methyl group). Position 327 in the provided 427-aa sequence corresponds to a histidine residue, which can serve as a general base in some methyltransferase subfamilies.",
    "evidence_ids": ["C5", "H3", "C4", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is an O-methyltransferase (identifiable from the SAM-binding motif 'VDVGGSLGH' and overall fold context). Methyltransferases require a proton acceptor (general base) at the catalytic center to deprotonate the substrate's hydroxyl/amino group, enabling nucleophilic attack on the methyl group of SAM. This eliminates option D ('Proton donor'), which describes the opposite mechanistic role. Option A (position 2723) is arithmetically impossible in a 427-residue protein. Option C references 'beta-ketoacyl synthase activity,' an entirely unrelated enzyme class (type I/II fatty acid synthase), irrelevant to an O-methyltransferase. By elimination of A (out of range), C (wrong enzyme class), and D (wrong catalytic role), option B is the only biologically coherent choice.",
    "missing_item_specific_fact": "The exact residue number 327 is a database annotation fact not derivable from first principles; however, it is determined by elimination since all other options are independently falsifiable by general biological reasoning.",
    "reason": "The functional descriptor 'Proton acceptor' is derivable from methyltransferase catalytic mechanism. The position 327 itself is a database fact, but since the three distractors are eliminable by arithmetic (A: 2723 > 427), enzyme-class knowledge (C: beta-ketoacyl synthase ≠ methyltransferase), and mechanistic reasoning (D: donor vs. acceptor), the correct answer is reachable without memorizing the specific annotation. The reasoning chain is concrete and does not require recognizing the exact sequence or recalling a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor is independently falsifiable: A is out of range for a 427-aa protein; C references a completely different enzyme class; D assigns the wrong mechanistic role (proton donor instead of acceptor). Only B survives elimination. No ambiguity remains."
  },
  "important_caveats": [
    "The active-site annotation at position 327 carries evidence code ECO:0000255 (inferred by sequence analysis via PROSITE-ProRule PRU01020), meaning it is a computational/pattern-based prediction, not an experimentally determined catalytic residue. No mutagenesis or kinetic data specific to this residue in FrzF was found in the supplied evidence.",
    "The PROSITE-ProRule annotation is transferred by profile similarity; the actual catalytic mechanism of FrzF (position 327, a histidine) has not been independently validated in the cited primary literature (PubMed 33372776) beyond general pathway reconstitution.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and the UniProt entry, and the historical (v19) and current (v21) annotations both list ACT_SITE 327 as 'Proton acceptor.'",
    "The identity of the protein (accession A0A7T8J1Z8) was inferred mechanically by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone."
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

**Accession:** `A0A7T8J1Z8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
"A0A7T8J1Z8"
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis cluster protein F"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"O-methyltransferase FrzF"}}}
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01020","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":327},"start":{"modifier":"EXACT","value":327}},"type":"Active site"}
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01020","source":"PROSITE-ProRule"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:59789"}],"ligand":{"id":"ChEBI:CHEBI:59789","name":"S-adenosyl-L-methionine"},"location":{"end":{"modifier":"EXACT","value":281},"start":{"modifier":"EXACT","value":281}},"type":"Binding site"}
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)  
**Locator:** `lines 106-108`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:54.122159+00:00.  

```text
FT   ACT_SITE        327
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01020"
```

Source SHA-256: `b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)  
**Locator:** `lines 109-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:54.122159+00:00.  

```text
FT   BINDING         281
FT                   /ligand="S-adenosyl-L-methionine"
FT                   /ligand_id="ChEBI:CHEBI:59789"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01020"
```

Source SHA-256: `b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 36. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
