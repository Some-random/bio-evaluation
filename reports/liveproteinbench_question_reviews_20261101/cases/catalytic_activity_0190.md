# catalytic_activity_0190

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAAVTRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRALEQELSGTVFIPGDVTQERDLQTLVSETLSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEVNLLGTYTLIKLALPHLRKSRGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRHGVRVNCISPGNIWTPLWEELAASTSDPRATILEGTLAQPLGRMGQPAEVAAAAVFLASEATFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH

[Multiple Choices]
A. a 3-O-beta-D-glucosyl-beta-D-glucuronoside + phosphate = a beta-D-glucuronoside + alpha-D-glucose 1-phosphate
B. (2R,3R,5S)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)
C. demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine
D. L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence exactly matches the mouse UniProt entry annotated with reaction D. However, the catalytic-activity annotation is transferred by similarity from Q9BPX1 (ECO:0000250), not evidence here of a direct experiment on this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich motif is consistent with an NAD-binding dehydrogenase, which favors D over the glycosidase and methyltransferase choices. It does not establish L-fucose as the substrate.


**Missing item-specific fact**

> The protein's substrate specificity—particularly its annotated or experimentally established activity on L-fucose—is not supplied.


**Reason**

> Sequence features can suggest a dehydrogenase family, but assigning the precise L-fucose-to-lactone reaction depends on protein-specific functional information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reaction types, and D is the one consistent with the likely NAD-dependent dehydrogenase class; the uncertainty is the exact substrate specificity, not an equally supported alternative.


### Important caveats

- The evidence supports D as a database annotation for the sequence, but the cited evidence is transferred by similarity and does not independently establish direct experimental validation for this mouse protein.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich motif is consistent with an NAD-binding dehydrogenase, which favors D over the glycosidase and methyltransferase choices. It does not establish L-fucose as the substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's substrate specificity—particularly its annotated or experimentally established activity on L-fucose—is not supplied.",
    "reason": "Sequence features can suggest a dehydrogenase family, but assigning the precise L-fucose-to-lactone reaction depends on protein-specific functional information."
  },
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the mouse UniProt entry annotated with reaction D. However, the catalytic-activity annotation is transferred by similarity from Q9BPX1 (ECO:0000250), not evidence here of a direct experiment on this protein."
  },
  "important_caveats": [
    "The evidence supports D as a database annotation for the sequence, but the cited evidence is transferred by similarity and does not independently establish direct experimental validation for this mouse protein.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction types, and D is the one consistent with the likely NAD-dependent dehydrogenase class; the uncertainty is the exact substrate specificity, not an equally supported alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the mouse UniProt entry annotated with reaction D. However, the catalytic-activity annotation is transferred by similarity from Q9BPX1 (ECO:0000250), not evidence here of a direct experiment on this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich motif is consistent with an NAD-binding dehydrogenase, which favors D over the glycosidase and methyltransferase choices. It does not establish L-fucose as the substrate.",
    "missing_item_specific_fact": "The protein's substrate specificity—particularly its annotated or experimentally established activity on L-fucose—is not supplied.",
    "reason": "Sequence features can suggest a dehydrogenase family, but assigning the precise L-fucose-to-lactone reaction depends on protein-specific functional information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction types, and D is the one consistent with the likely NAD-dependent dehydrogenase class; the uncertainty is the exact substrate specificity, not an equally supported alternative."
  },
  "important_caveats": [
    "The evidence supports D as a database annotation for the sequence, but the cited evidence is transferred by similarity and does not independently establish direct experimental validation for this mouse protein.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt E9Q3D4 (sequence SHA256 match confirmed) is annotated as L-fucose dehydrogenase (EC 1.1.1.122) with the exact catalytic reaction 'L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)' listed as the primary reaction (C5, H3). The evidence code is ECO:0000250 (inferred by similarity from human ortholog Q9BPX1), making this a transferred annotation rather than direct experimental evidence for the mouse protein, but it is the authoritative database annotation for this exact sequence. The entry also lists D-arabinose and L-galactose as alternative substrates (C6, C7), but L-fucose is the recommended/primary reaction. The expected answer matches the annotation exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark short-chain dehydrogenase/reductase (SDR) family architecture: an N-terminal Rossmann-fold NAD-binding motif (VVVVTGGSRGIGAAIVRAF, containing the GxGxxG pattern GSRGIGAA) and a C-terminal catalytic tetrad region (YGRK near the C-terminus, consistent with the Tyr-x-x-x-Lys pair). SDRs catalyze simple NAD(P)+-dependent oxidation of alcohols/aldehydes/ketones. Among the four choices, only option D (L-fucose + NAD+ → L-fucono-1,5-lactone + NADH + H+) represents a simple NAD-dependent dehydrogenase reaction consistent with SDR mechanism. Option A is a phosphorylase reaction (no NAD, different fold), option B is a radical SAM carbapenam synthase reaction (requires radical chemistry and SAM, incompatible with SDR fold), and option C is an O-methyltransferase reaction (SAM-dependent, no NAD). The SDR family identification from sequence features eliminates three of four options without needing to memorize the specific UniProt entry.


**Missing item-specific fact**

> None critical. The specific substrate identity (L-fucose vs. D-arabinose or L-galactose, which are also listed in the UniProt entry) would require item-specific knowledge, but those alternatives are not among the answer choices, so the SDR-family reasoning suffices to select D uniquely.


**Reason**

> A knowledgeable reader can identify the SDR family from the Rossmann-fold and catalytic-tetrad motifs, then eliminate the phosphorylase, radical SAM, and methyltransferase options as mechanistically incompatible with SDR architecture. This leaves D as the only viable answer through general enzymology reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry lists three substrates (L-fucose, D-arabinose, L-galactose) for this enzyme, only L-fucose appears among the answer choices. The other three options represent entirely different enzyme classes (phosphorylase, radical SAM synthase, methyltransferase) that are mechanistically incompatible with the SDR fold evident in the sequence. No ambiguity exists among the provided choices.


### Important caveats

- The UniProt annotation carries evidence code ECO:0000250 (inferred by similarity from human Q9BPX1), meaning the L-fucose dehydrogenase assignment for the mouse protein is a computational transfer, not a direct experimental measurement on this exact protein.
- The entry is relatively new (first public date 2025-04-09); the author's source snapshot is unknown, so the annotation available at benchmark construction time may have differed.
- The protein also has the alternative name 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its SDR-family membership and potential broader substrate range, but this does not conflict with the L-fucose dehydrogenase annotation.
- The sequence is 273 aa, consistent with a monomeric SDR; no cofactor-binding anomalies or truncations are apparent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark short-chain dehydrogenase/reductase (SDR) family architecture: an N-terminal Rossmann-fold NAD-binding motif (VVVVTGGSRGIGAAIVRAF, containing the GxGxxG pattern GSRGIGAA) and a C-terminal catalytic tetrad region (YGRK near the C-terminus, consistent with the Tyr-x-x-x-Lys pair). SDRs catalyze simple NAD(P)+-dependent oxidation of alcohols/aldehydes/ketones. Among the four choices, only option D (L-fucose + NAD+ → L-fucono-1,5-lactone + NADH + H+) represents a simple NAD-dependent dehydrogenase reaction consistent with SDR mechanism. Option A is a phosphorylase reaction (no NAD, different fold), option B is a radical SAM carbapenam synthase reaction (requires radical chemistry and SAM, incompatible with SDR fold), and option C is an O-methyltransferase reaction (SAM-dependent, no NAD). The SDR family identification from sequence features eliminates three of four options without needing to memorize the specific UniProt entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific substrate identity (L-fucose vs. D-arabinose or L-galactose, which are also listed in the UniProt entry) would require item-specific knowledge, but those alternatives are not among the answer choices, so the SDR-family reasoning suffices to select D uniquely.",
    "reason": "A knowledgeable reader can identify the SDR family from the Rossmann-fold and catalytic-tetrad motifs, then eliminate the phosphorylase, radical SAM, and methyltransferase options as mechanistically incompatible with SDR architecture. This leaves D as the only viable answer through general enzymology reasoning."
  },
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt E9Q3D4 (sequence SHA256 match confirmed) is annotated as L-fucose dehydrogenase (EC 1.1.1.122) with the exact catalytic reaction 'L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)' listed as the primary reaction (C5, H3). The evidence code is ECO:0000250 (inferred by similarity from human ortholog Q9BPX1), making this a transferred annotation rather than direct experimental evidence for the mouse protein, but it is the authoritative database annotation for this exact sequence. The entry also lists D-arabinose and L-galactose as alternative substrates (C6, C7), but L-fucose is the recommended/primary reaction. The expected answer matches the annotation exactly."
  },
  "important_caveats": [
    "The UniProt annotation carries evidence code ECO:0000250 (inferred by similarity from human Q9BPX1), meaning the L-fucose dehydrogenase assignment for the mouse protein is a computational transfer, not a direct experimental measurement on this exact protein.",
    "The entry is relatively new (first public date 2025-04-09); the author's source snapshot is unknown, so the annotation available at benchmark construction time may have differed.",
    "The protein also has the alternative name 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its SDR-family membership and potential broader substrate range, but this does not conflict with the L-fucose dehydrogenase annotation.",
    "The sequence is 273 aa, consistent with a monomeric SDR; no cofactor-binding anomalies or truncations are apparent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry lists three substrates (L-fucose, D-arabinose, L-galactose) for this enzyme, only L-fucose appears among the answer choices. The other three options represent entirely different enzyme classes (phosphorylase, radical SAM synthase, methyltransferase) that are mechanistically incompatible with the SDR fold evident in the sequence. No ambiguity exists among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt E9Q3D4 (sequence SHA256 match confirmed) is annotated as L-fucose dehydrogenase (EC 1.1.1.122) with the exact catalytic reaction 'L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)' listed as the primary reaction (C5, H3). The evidence code is ECO:0000250 (inferred by similarity from human ortholog Q9BPX1), making this a transferred annotation rather than direct experimental evidence for the mouse protein, but it is the authoritative database annotation for this exact sequence. The entry also lists D-arabinose and L-galactose as alternative substrates (C6, C7), but L-fucose is the recommended/primary reaction. The expected answer matches the annotation exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark short-chain dehydrogenase/reductase (SDR) family architecture: an N-terminal Rossmann-fold NAD-binding motif (VVVVTGGSRGIGAAIVRAF, containing the GxGxxG pattern GSRGIGAA) and a C-terminal catalytic tetrad region (YGRK near the C-terminus, consistent with the Tyr-x-x-x-Lys pair). SDRs catalyze simple NAD(P)+-dependent oxidation of alcohols/aldehydes/ketones. Among the four choices, only option D (L-fucose + NAD+ → L-fucono-1,5-lactone + NADH + H+) represents a simple NAD-dependent dehydrogenase reaction consistent with SDR mechanism. Option A is a phosphorylase reaction (no NAD, different fold), option B is a radical SAM carbapenam synthase reaction (requires radical chemistry and SAM, incompatible with SDR fold), and option C is an O-methyltransferase reaction (SAM-dependent, no NAD). The SDR family identification from sequence features eliminates three of four options without needing to memorize the specific UniProt entry.",
    "missing_item_specific_fact": "None critical. The specific substrate identity (L-fucose vs. D-arabinose or L-galactose, which are also listed in the UniProt entry) would require item-specific knowledge, but those alternatives are not among the answer choices, so the SDR-family reasoning suffices to select D uniquely.",
    "reason": "A knowledgeable reader can identify the SDR family from the Rossmann-fold and catalytic-tetrad motifs, then eliminate the phosphorylase, radical SAM, and methyltransferase options as mechanistically incompatible with SDR architecture. This leaves D as the only viable answer through general enzymology reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry lists three substrates (L-fucose, D-arabinose, L-galactose) for this enzyme, only L-fucose appears among the answer choices. The other three options represent entirely different enzyme classes (phosphorylase, radical SAM synthase, methyltransferase) that are mechanistically incompatible with the SDR fold evident in the sequence. No ambiguity exists among the provided choices."
  },
  "important_caveats": [
    "The UniProt annotation carries evidence code ECO:0000250 (inferred by similarity from human Q9BPX1), meaning the L-fucose dehydrogenase assignment for the mouse protein is a computational transfer, not a direct experimental measurement on this exact protein.",
    "The entry is relatively new (first public date 2025-04-09); the author's source snapshot is unknown, so the annotation available at benchmark construction time may have differed.",
    "The protein also has the alternative name 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its SDR-family membership and potential broader substrate range, but this does not conflict with the L-fucose dehydrogenase annotation.",
    "The sequence is 273 aa, consistent with a monomeric SDR; no cofactor-binding anomalies or truncations are apparent."
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

**Accession:** `E9Q3D4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 95. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
"E9Q3D4"
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Hydroxysteroid 17-beta dehydrogenase 14"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"value":"1.1.1.122"}],"fullName":{"value":"L-fucose dehydrogenase"}}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81516"}}],"reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"name":"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81515"},{"database":"ChEBI","id":"CHEBI:2181"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:81457"}]}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"name":"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81519"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:46994"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:194242"}]}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"name":"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81523"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:37619"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:182410"}]}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:17.926007+00:00.  

```text
DE   RecName: Full=L-fucose dehydrogenase;
DE            EC=1.1.1.122 {ECO:0000250|UniProtKB:Q9BPX1};
DE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;
```

Source SHA-256: `e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:17.926007+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);
CC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;
CC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;
CC         Evidence={ECO:0000250|UniProtKB:Q9BPX1};
```

Source SHA-256: `e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 190. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
