# EC_number_0001

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 4.4.1.11

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNSMHPETLMVHGGMDGLTEAGVHVPAIDLSTTNPVNDVATGGDSYEWLATGHALKDGDSAVYQRLWQPGVARFETALAELEHADEAVAFATGMAAMTAALLAAVNAGTPHIVAVRPLYGGSDHLLETGLLGTTVTWAKEAEIASAIQDDTGLVIVETPANPSLDLVDLDSVVAAAGTVPVLVDNTFCTPVLQQPIRHGAALVLHSATKYLGGHGDAMGGIIATNSDWAMRLRQVRAITGALLHPMGAYLLHRGLRTLAVRMRAAQTTAGELAERLAAHPAITAVHYPGLNGQDPRGLLGRQMSGGGAMIALELAGGFDAARSFVEHCSLVVHAVSLGGADTLIQHPASLTHRPVAATAKPGDGLIRLSVGLEHVDDLEDDLIAALDASRAAA

[Multiple Choices]
A. 4.3.1.24
B. 4.2.1.70
C. 4.4.1.11
D. 2.7.13.3
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a UniProt entry annotated as L-methionine gamma-lyase, EC 4.4.1.11, with the corresponding catalytic reaction. The annotation is transferred by similarity from another UniProt entry (ECO:0000250), not direct experimental evidence for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying a related enzyme family, but that alone does not establish which specific reaction—and thus which complete EC number—the protein catalyzes.


**Missing item-specific fact**

> A protein-specific functional annotation or experimental determination distinguishing methionine gamma-lyase activity from related sulfur-amino-acid reactions.


**Reason**

> The input supplies only the sequence and choices. Selecting the reaction-specific EC number requires protein-specific functional knowledge; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only C matches the supported annotation. The source also lists EC 4.4.1.2 as an alternative name/activity, but that number is not among the choices.


### Important caveats

- The UniProt functional and catalytic annotations are similarity-transferred rather than direct experimental evidence for the supplied protein.
- The sequence match and historical record support that this annotation applied to the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying a related enzyme family, but that alone does not establish which specific reaction—and thus which complete EC number—the protein catalyzes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific functional annotation or experimental determination distinguishing methionine gamma-lyase activity from related sulfur-amino-acid reactions.",
    "reason": "The input supplies only the sequence and choices. Selecting the reaction-specific EC number requires protein-specific functional knowledge; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from supplied context."
  },
  "case_id": "EC_number_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as L-methionine gamma-lyase, EC 4.4.1.11, with the corresponding catalytic reaction. The annotation is transferred by similarity from another UniProt entry (ECO:0000250), not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The UniProt functional and catalytic annotations are similarity-transferred rather than direct experimental evidence for the supplied protein.",
    "The sequence match and historical record support that this annotation applied to the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only C matches the supported annotation. The source also lists EC 4.4.1.2 as an alternative name/activity, but that number is not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as L-methionine gamma-lyase, EC 4.4.1.11, with the corresponding catalytic reaction. The annotation is transferred by similarity from another UniProt entry (ECO:0000250), not direct experimental evidence for this sequence.",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying a related enzyme family, but that alone does not establish which specific reaction—and thus which complete EC number—the protein catalyzes.",
    "missing_item_specific_fact": "A protein-specific functional annotation or experimental determination distinguishing methionine gamma-lyase activity from related sulfur-amino-acid reactions.",
    "reason": "The input supplies only the sequence and choices. Selecting the reaction-specific EC number requires protein-specific functional knowledge; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only C matches the supported annotation. The source also lists EC 4.4.1.2 as an alternative name/activity, but that number is not among the choices."
  },
  "important_caveats": [
    "The UniProt functional and catalytic annotations are similarity-transferred rather than direct experimental evidence for the supplied protein.",
    "The sequence match and historical record support that this annotation applied to the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A1H1YBL2 (MEGL_BRESA, Brevibacterium sandarakinum) annotates this 393-aa protein with EC 4.4.1.11 (L-methionine gamma-lyase) as the recommended name. The sequence matches exactly (SHA256 confirmed). However, the annotation evidence code is ECO:0000250 (inferred by similarity from A0A2H1K3G9), meaning this is a computational transfer rather than direct experimental verification. The entry also lists EC 4.4.1.2 (homocysteine desulfhydrase) as an alternative name, indicating the enzyme may have dual substrate specificity. The annotation supports 4.4.1.11 as the primary EC assignment, but it is a database inference, not experimental proof.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains conserved motifs characteristic of the Cys/Met metabolism PLP-dependent lyase family (~393 aa, PLP-binding lysine motif, characteristic fold). This family catalyzes C-S bond cleavage (EC class 4.4, sulfur-lyases). This reasoning eliminates D (EC 2.7.13.3, a transferase — completely different EC class), B (EC 4.2.1.70, a carbon-oxygen lyase/hydroxynitrile lyase with a different fold and substrate chemistry), and A (EC 4.3.1.24, a carbon-nitrogen lyase — different bond cleaved). Only C (4.4.1.11) falls in the correct EC subclass (4.4, carbon-sulfur lyases) for a Cys/Met metabolism PLP-dependent lyase.


**Missing item-specific fact**

> The precise 4-digit assignment (4.4.1.11 vs 4.4.1.2) depends on substrate specificity data (methionine vs homocysteine preference), which is an experimental measurement not derivable from sequence alone. The UniProt annotation itself assigns both EC numbers to this protein via similarity inference. However, since 4.4.1.2 is not among the answer choices, this ambiguity does not affect selection among the given options.


**Reason**

> Elimination of three options in different EC classes (2, 4.2, 4.3) is achievable through general knowledge of enzyme classification and recognition of the Cys/Met metabolism PLP-dependent lyase family. The only remaining option (C, 4.4.1.11) is in the correct subclass. The 4-digit precision is somewhat aided by the absence of other 4.4.1.x distractors, but the family-level identification and EC class elimination constitute a meaningful biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC main classes (2, 4.2, 4.3, 4.4). Only C falls in the carbon-sulfur lyase subclass (4.4) appropriate for the Cys/Met metabolism PLP-dependent lyase family. While the protein also has EC 4.4.1.2 activity per annotation, that number is not offered as a choice, so no ambiguity exists among the provided options.


### Important caveats

- The UniProt annotation for EC 4.4.1.11 is based on similarity inference (ECO:0000250 from A0A2H1K3G9), not direct experimental characterization of this Brevibacterium protein.
- The same UniProt entry lists EC 4.4.1.2 (homocysteine desulfhydrase) as an alternative name, indicating the enzyme may act on both methionine and homocysteine. The distinction between 4.4.1.11 and 4.4.1.2 is a substrate-specificity judgment not resolvable from sequence.
- The source snapshot used by the question author is unknown; the current UniProt entry (version 34) and the archived version 32 both carry the same EC annotation, but the original dataset construction date is unconfirmed.
- Recognition of the Cys/Met metabolism PLP-dependent lyase family from a raw 393-aa sequence without database tools requires substantial prior knowledge of conserved motifs; this is general biological knowledge but not trivially obvious to all practitioners.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains conserved motifs characteristic of the Cys/Met metabolism PLP-dependent lyase family (~393 aa, PLP-binding lysine motif, characteristic fold). This family catalyzes C-S bond cleavage (EC class 4.4, sulfur-lyases). This reasoning eliminates D (EC 2.7.13.3, a transferase — completely different EC class), B (EC 4.2.1.70, a carbon-oxygen lyase/hydroxynitrile lyase with a different fold and substrate chemistry), and A (EC 4.3.1.24, a carbon-nitrogen lyase — different bond cleaved). Only C (4.4.1.11) falls in the correct EC subclass (4.4, carbon-sulfur lyases) for a Cys/Met metabolism PLP-dependent lyase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise 4-digit assignment (4.4.1.11 vs 4.4.1.2) depends on substrate specificity data (methionine vs homocysteine preference), which is an experimental measurement not derivable from sequence alone. The UniProt annotation itself assigns both EC numbers to this protein via similarity inference. However, since 4.4.1.2 is not among the answer choices, this ambiguity does not affect selection among the given options.",
    "reason": "Elimination of three options in different EC classes (2, 4.2, 4.3) is achievable through general knowledge of enzyme classification and recognition of the Cys/Met metabolism PLP-dependent lyase family. The only remaining option (C, 4.4.1.11) is in the correct subclass. The 4-digit precision is somewhat aided by the absence of other 4.4.1.x distractors, but the family-level identification and EC class elimination constitute a meaningful biological argument."
  },
  "case_id": "EC_number_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A1H1YBL2 (MEGL_BRESA, Brevibacterium sandarakinum) annotates this 393-aa protein with EC 4.4.1.11 (L-methionine gamma-lyase) as the recommended name. The sequence matches exactly (SHA256 confirmed). However, the annotation evidence code is ECO:0000250 (inferred by similarity from A0A2H1K3G9), meaning this is a computational transfer rather than direct experimental verification. The entry also lists EC 4.4.1.2 (homocysteine desulfhydrase) as an alternative name, indicating the enzyme may have dual substrate specificity. The annotation supports 4.4.1.11 as the primary EC assignment, but it is a database inference, not experimental proof."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.4.1.11 is based on similarity inference (ECO:0000250 from A0A2H1K3G9), not direct experimental characterization of this Brevibacterium protein.",
    "The same UniProt entry lists EC 4.4.1.2 (homocysteine desulfhydrase) as an alternative name, indicating the enzyme may act on both methionine and homocysteine. The distinction between 4.4.1.11 and 4.4.1.2 is a substrate-specificity judgment not resolvable from sequence.",
    "The source snapshot used by the question author is unknown; the current UniProt entry (version 34) and the archived version 32 both carry the same EC annotation, but the original dataset construction date is unconfirmed.",
    "Recognition of the Cys/Met metabolism PLP-dependent lyase family from a raw 393-aa sequence without database tools requires substantial prior knowledge of conserved motifs; this is general biological knowledge but not trivially obvious to all practitioners."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC main classes (2, 4.2, 4.3, 4.4). Only C falls in the carbon-sulfur lyase subclass (4.4) appropriate for the Cys/Met metabolism PLP-dependent lyase family. While the protein also has EC 4.4.1.2 activity per annotation, that number is not offered as a choice, so no ambiguity exists among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A1H1YBL2 (MEGL_BRESA, Brevibacterium sandarakinum) annotates this 393-aa protein with EC 4.4.1.11 (L-methionine gamma-lyase) as the recommended name. The sequence matches exactly (SHA256 confirmed). However, the annotation evidence code is ECO:0000250 (inferred by similarity from A0A2H1K3G9), meaning this is a computational transfer rather than direct experimental verification. The entry also lists EC 4.4.1.2 (homocysteine desulfhydrase) as an alternative name, indicating the enzyme may have dual substrate specificity. The annotation supports 4.4.1.11 as the primary EC assignment, but it is a database inference, not experimental proof.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains conserved motifs characteristic of the Cys/Met metabolism PLP-dependent lyase family (~393 aa, PLP-binding lysine motif, characteristic fold). This family catalyzes C-S bond cleavage (EC class 4.4, sulfur-lyases). This reasoning eliminates D (EC 2.7.13.3, a transferase — completely different EC class), B (EC 4.2.1.70, a carbon-oxygen lyase/hydroxynitrile lyase with a different fold and substrate chemistry), and A (EC 4.3.1.24, a carbon-nitrogen lyase — different bond cleaved). Only C (4.4.1.11) falls in the correct EC subclass (4.4, carbon-sulfur lyases) for a Cys/Met metabolism PLP-dependent lyase.",
    "missing_item_specific_fact": "The precise 4-digit assignment (4.4.1.11 vs 4.4.1.2) depends on substrate specificity data (methionine vs homocysteine preference), which is an experimental measurement not derivable from sequence alone. The UniProt annotation itself assigns both EC numbers to this protein via similarity inference. However, since 4.4.1.2 is not among the answer choices, this ambiguity does not affect selection among the given options.",
    "reason": "Elimination of three options in different EC classes (2, 4.2, 4.3) is achievable through general knowledge of enzyme classification and recognition of the Cys/Met metabolism PLP-dependent lyase family. The only remaining option (C, 4.4.1.11) is in the correct subclass. The 4-digit precision is somewhat aided by the absence of other 4.4.1.x distractors, but the family-level identification and EC class elimination constitute a meaningful biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC main classes (2, 4.2, 4.3, 4.4). Only C falls in the carbon-sulfur lyase subclass (4.4) appropriate for the Cys/Met metabolism PLP-dependent lyase family. While the protein also has EC 4.4.1.2 activity per annotation, that number is not offered as a choice, so no ambiguity exists among the provided options."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.4.1.11 is based on similarity inference (ECO:0000250 from A0A2H1K3G9), not direct experimental characterization of this Brevibacterium protein.",
    "The same UniProt entry lists EC 4.4.1.2 (homocysteine desulfhydrase) as an alternative name, indicating the enzyme may act on both methionine and homocysteine. The distinction between 4.4.1.11 and 4.4.1.2 is a substrate-specificity judgment not resolvable from sequence.",
    "The source snapshot used by the question author is unknown; the current UniProt entry (version 34) and the archived version 32 both carry the same EC annotation, but the original dataset construction date is unconfirmed.",
    "Recognition of the Cys/Met metabolism PLP-dependent lyase family from a raw 393-aa sequence without database tools requires substantial prior knowledge of conserved motifs; this is general biological knowledge but not trivially obvious to all practitioners."
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

**Accession:** `A0A1H1YBL2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:35.559742+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A2H1K3G9","source":"UniProtKB"}],"value":"4.4.1.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A2H1K3G9","source":"UniProtKB"}],"value":"Homocysteine desulfhydrase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A2H1K3G9","source":"UniProtKB"}],"value":"4.4.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A2H1K3G9","source":"UniProtKB"}],"value":"L-methionine gamma-lyase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A2H1K3G9","source":"UniProtKB"}],"value":"MGL"}]}}
```

Source SHA-256: `8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:35.559742+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A2H1K3G9","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23801"}}],"reaction":{"ecNumber":"4.4.1.11","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A2H1K3G9","source":"UniProtKB"}],"name":"L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23800"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:16007"},{"database":"ChEBI","id":"CHEBI:16763"},{"database":"ChEBI","id":"CHEBI:28938"},{"database":"ChEBI","id":"CHEBI:57844"}]}}
```

Source SHA-256: `8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:37.341815+00:00.  

```text
ID   MEGL_BRESA              Reviewed;         393 AA.
AC   A0A1H1YBL2;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JAN-2017, sequence version 1.
DT   28-JAN-2026, entry version 32.
DE   RecName: Full=L-methionine gamma-lyase {ECO:0000250|UniProtKB:A0A2H1K3G9};
DE            Short=MGL {ECO:0000250|UniProtKB:A0A2H1K3G9};
DE            EC=4.4.1.11 {ECO:0000250|UniProtKB:A0A2H1K3G9};
DE   AltName: Full=Homocysteine desulfhydrase {ECO:0000250|UniProtKB:A0A2H1K3G9};
DE            EC=4.4.1.2 {ECO:0000250|UniProtKB:A0A2H1K3G9};
GN   ORFNames=SAMN04489751_4033 {ECO:0000312|EMBL:SDT18406.1};
OS   Brevibacterium sandarakinum.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales;
OC   Brevibacteriaceae; Brevibacterium.
OX   NCBI_TaxID=629680;
```

Source SHA-256: `5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:37.341815+00:00.  

```text
DE   RecName: Full=L-methionine gamma-lyase {ECO:0000250|UniProtKB:A0A2H1K3G9};
DE            Short=MGL {ECO:0000250|UniProtKB:A0A2H1K3G9};
DE            EC=4.4.1.11 {ECO:0000250|UniProtKB:A0A2H1K3G9};
DE   AltName: Full=Homocysteine desulfhydrase {ECO:0000250|UniProtKB:A0A2H1K3G9};
DE            EC=4.4.1.2 {ECO:0000250|UniProtKB:A0A2H1K3G9};
```

Source SHA-256: `5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32)  
**Locator:** `lines 25-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:37.341815+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+);
CC         Xref=Rhea:RHEA:23800, ChEBI:CHEBI:15377, ChEBI:CHEBI:16007,
CC         ChEBI:CHEBI:16763, ChEBI:CHEBI:28938, ChEBI:CHEBI:57844; EC=4.4.1.11;
CC         Evidence={ECO:0000250|UniProtKB:A0A2H1K3G9};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23801;
CC         Evidence={ECO:0000250|UniProtKB:A0A2H1K3G9};
```

Source SHA-256: `5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
