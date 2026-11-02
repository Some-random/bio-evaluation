# EC_number_0061

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.7.7.43

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVIAVIPARSGSKGIKNKNLVLLNNQPLIYYTIKAALNSKCISKVLVSSDSEEILSYAKSQNVDILKRPIELAQDDTTSDKVLLHALEFYKDYEDVIFLQPTSPLRTNIHIDEAFKIYKNSDANALISVTECDNKILKAFICDNKGDLKGICDDEYPFMPRQKLPKTYMSNGAIYILSIKDFLNKPSFLQSKTKYFLMNKISSLDIDNLEDLKQVENIQKMKGCVVWISGLAGAGKTTISSGLYKKLKEKYNNSVLLDGDELRKIFKHTGYTREERLESAKKISSLCSFLAKNDIIVICATISLFEEIYLLNRNTIENYFEVFVDCPMEELILRDQKGLYSGALKGEIKDVVGVDIKYAKPNAHYIIDNSSKTDLEKKINNLYNEVELFFNKER

[Multiple Choices]
A. 2.7.7.88
B. 2.7.7.43
C. 2.7.8.43
D. 4.2.1.9
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

> The supplied sequence exactly matches the UniProt entry for this protein. That entry assigns EC 2.7.7.43 and links the assignment to experimental evidence (ECO:0000269) describing the relevant CTP-dependent N-acylneuraminate reaction. This supports B, while the source snapshot does not establish what information the question's author used.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest an enzyme that binds nucleotide substrates, but the supplied sequence and choices do not establish the specific substrate and reaction needed to distinguish the exact EC number.


**Missing item-specific fact**

> The protein's experimentally established catalytic reaction and substrate specificity—N-acylneuraminate plus CTP yielding CMP-N-acylneuraminate and diphosphate—are absent from the input.


**Reason**

> The key is supported by sequence-matched, experimentally linked annotation, but that evidence is reviewer-only. Choosing the exact EC requires item-specific functional knowledge, not merely general sequence reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-only input does not justify an exact EC assignment, but the reviewer evidence supports a single answer for this protein.


### Important caveats

- The cited experimental evidence is recorded in UniProt, but the primary publication was not independently reviewed here.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest an enzyme that binds nucleotide substrates, but the supplied sequence and choices do not establish the specific substrate and reaction needed to distinguish the exact EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally established catalytic reaction and substrate specificity—N-acylneuraminate plus CTP yielding CMP-N-acylneuraminate and diphosphate—are absent from the input.",
    "reason": "The key is supported by sequence-matched, experimentally linked annotation, but that evidence is reviewer-only. Choosing the exact EC requires item-specific functional knowledge, not merely general sequence reasoning."
  },
  "case_id": "EC_number_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein. That entry assigns EC 2.7.7.43 and links the assignment to experimental evidence (ECO:0000269) describing the relevant CTP-dependent N-acylneuraminate reaction. This supports B, while the source snapshot does not establish what information the question's author used."
  },
  "important_caveats": [
    "The cited experimental evidence is recorded in UniProt, but the primary publication was not independently reviewed here.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-only input does not justify an exact EC assignment, but the reviewer evidence supports a single answer for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein. That entry assigns EC 2.7.7.43 and links the assignment to experimental evidence (ECO:0000269) describing the relevant CTP-dependent N-acylneuraminate reaction. This supports B, while the source snapshot does not establish what information the question's author used.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest an enzyme that binds nucleotide substrates, but the supplied sequence and choices do not establish the specific substrate and reaction needed to distinguish the exact EC number.",
    "missing_item_specific_fact": "The protein's experimentally established catalytic reaction and substrate specificity—N-acylneuraminate plus CTP yielding CMP-N-acylneuraminate and diphosphate—are absent from the input.",
    "reason": "The key is supported by sequence-matched, experimentally linked annotation, but that evidence is reviewer-only. Choosing the exact EC requires item-specific functional knowledge, not merely general sequence reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-only input does not justify an exact EC assignment, but the reviewer evidence supports a single answer for this protein."
  },
  "important_caveats": [
    "The cited experimental evidence is recorded in UniProt, but the primary publication was not independently reviewed here.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DY07 (sequence matched, 394 aa) annotates this protein as N-acylneuraminate cytidylyltransferase with EC 2.7.7.43, supported by experimental evidence (ECO:0000269, PubMed 38382015, Ghosh & Raushel 2024). The catalytic activity (N-acylneuraminate + CTP → CMP-N-acyl-beta-neuraminate + diphosphate) confirms the EC assignment. The historical archived entry (version 2, released 2026-01-28) carries the same EC annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical P-loop/Walker A motif (GAGKTT at positions ~196-201) diagnostic of nucleotidyltransferases (EC 2.7.7.x), which eliminates option D (EC 4.2.1.9, a hydro-lyase) and option C (EC 2.7.8.43, a transferase of a different subclass). Additionally, the sequence contains the well-known 'NSS' motif (in the stretch DNSSKTDLEK, ~positions 290-298), a hallmark of the CMP-sialic acid synthase family involved in sialic acid biosynthesis. This motif is characteristic of N-acylneuraminate cytidylyltransferase (EC 2.7.7.43) and is not found in unrelated nucleotidyltransferases. The combination of P-loop (nucleotidyltransferase class) and NSS motif (sialic acid pathway specificity) provides a concrete biological argument favoring B over A (EC 2.7.7.88, an unrelated nucleotidyltransferase).


**Missing item-specific fact**

> None critical. The NSS motif is a recognized family-diagnostic signature in glycobiology, and the P-loop is standard enzyme-mechanism knowledge. Distinguishing 2.7.7.43 from 2.7.7.88 relies on recognizing that 2.7.7.88 is not a sialic acid pathway enzyme, which follows from the absence of the NSS motif and unrelated substrate specificity.


**Reason**

> The sequence provides two independently informative motifs: the GAGKTT P-loop constrains the EC class to 2.7.7.x (nucleotidyltransferases), and the NSS motif specifically identifies the CMP-sialic acid synthase family, pointing to EC 2.7.7.43. These are general biochemical knowledge elements (nucleotide-binding motifs and sialic acid pathway signatures) rather than a single item-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three distinct EC classes (2.7.7, 2.7.8, 4.2.1), making the class-level distinction clear from the P-loop. Within 2.7.7, the NSS motif provides a specific family-level discriminator. No option is equally defensible given the sequence evidence.


### Important caveats

- The NSS motif identification, while well-established in glycobiology, represents moderately specialized knowledge; a model unfamiliar with sialic acid biosynthesis motifs might struggle to distinguish A from B.
- The UniProt entry was first published 2025-06-18 with the EC annotation added via PubMed 38382015 (2024). The historical archived version (entry v2, Jan 2026) already carries the EC 2.7.7.43 annotation, so the key was available before the 2026-05-07 cutoff.
- EC 2.7.7.88 is a valid but obscure nucleotidyltransferase entry; its obscurity makes it a relatively easy distractor once the sialic acid pathway is recognized.
- All reviewer evidence is annotation-derived; the underlying experimental validation rests on the Ghosh & Raushel 2024 Biochemistry paper, which was not independently retrieved here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical P-loop/Walker A motif (GAGKTT at positions ~196-201) diagnostic of nucleotidyltransferases (EC 2.7.7.x), which eliminates option D (EC 4.2.1.9, a hydro-lyase) and option C (EC 2.7.8.43, a transferase of a different subclass). Additionally, the sequence contains the well-known 'NSS' motif (in the stretch DNSSKTDLEK, ~positions 290-298), a hallmark of the CMP-sialic acid synthase family involved in sialic acid biosynthesis. This motif is characteristic of N-acylneuraminate cytidylyltransferase (EC 2.7.7.43) and is not found in unrelated nucleotidyltransferases. The combination of P-loop (nucleotidyltransferase class) and NSS motif (sialic acid pathway specificity) provides a concrete biological argument favoring B over A (EC 2.7.7.88, an unrelated nucleotidyltransferase).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The NSS motif is a recognized family-diagnostic signature in glycobiology, and the P-loop is standard enzyme-mechanism knowledge. Distinguishing 2.7.7.43 from 2.7.7.88 relies on recognizing that 2.7.7.88 is not a sialic acid pathway enzyme, which follows from the absence of the NSS motif and unrelated substrate specificity.",
    "reason": "The sequence provides two independently informative motifs: the GAGKTT P-loop constrains the EC class to 2.7.7.x (nucleotidyltransferases), and the NSS motif specifically identifies the CMP-sialic acid synthase family, pointing to EC 2.7.7.43. These are general biochemical knowledge elements (nucleotide-binding motifs and sialic acid pathway signatures) rather than a single item-specific database lookup."
  },
  "case_id": "EC_number_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DY07 (sequence matched, 394 aa) annotates this protein as N-acylneuraminate cytidylyltransferase with EC 2.7.7.43, supported by experimental evidence (ECO:0000269, PubMed 38382015, Ghosh & Raushel 2024). The catalytic activity (N-acylneuraminate + CTP → CMP-N-acyl-beta-neuraminate + diphosphate) confirms the EC assignment. The historical archived entry (version 2, released 2026-01-28) carries the same EC annotation."
  },
  "important_caveats": [
    "The NSS motif identification, while well-established in glycobiology, represents moderately specialized knowledge; a model unfamiliar with sialic acid biosynthesis motifs might struggle to distinguish A from B.",
    "The UniProt entry was first published 2025-06-18 with the EC annotation added via PubMed 38382015 (2024). The historical archived version (entry v2, Jan 2026) already carries the EC 2.7.7.43 annotation, so the key was available before the 2026-05-07 cutoff.",
    "EC 2.7.7.88 is a valid but obscure nucleotidyltransferase entry; its obscurity makes it a relatively easy distractor once the sialic acid pathway is recognized.",
    "All reviewer evidence is annotation-derived; the underlying experimental validation rests on the Ghosh & Raushel 2024 Biochemistry paper, which was not independently retrieved here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three distinct EC classes (2.7.7, 2.7.8, 4.2.1), making the class-level distinction clear from the P-loop. Within 2.7.7, the NSS motif provides a specific family-level discriminator. No option is equally defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DY07 (sequence matched, 394 aa) annotates this protein as N-acylneuraminate cytidylyltransferase with EC 2.7.7.43, supported by experimental evidence (ECO:0000269, PubMed 38382015, Ghosh & Raushel 2024). The catalytic activity (N-acylneuraminate + CTP → CMP-N-acyl-beta-neuraminate + diphosphate) confirms the EC assignment. The historical archived entry (version 2, released 2026-01-28) carries the same EC annotation.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical P-loop/Walker A motif (GAGKTT at positions ~196-201) diagnostic of nucleotidyltransferases (EC 2.7.7.x), which eliminates option D (EC 4.2.1.9, a hydro-lyase) and option C (EC 2.7.8.43, a transferase of a different subclass). Additionally, the sequence contains the well-known 'NSS' motif (in the stretch DNSSKTDLEK, ~positions 290-298), a hallmark of the CMP-sialic acid synthase family involved in sialic acid biosynthesis. This motif is characteristic of N-acylneuraminate cytidylyltransferase (EC 2.7.7.43) and is not found in unrelated nucleotidyltransferases. The combination of P-loop (nucleotidyltransferase class) and NSS motif (sialic acid pathway specificity) provides a concrete biological argument favoring B over A (EC 2.7.7.88, an unrelated nucleotidyltransferase).",
    "missing_item_specific_fact": "None critical. The NSS motif is a recognized family-diagnostic signature in glycobiology, and the P-loop is standard enzyme-mechanism knowledge. Distinguishing 2.7.7.43 from 2.7.7.88 relies on recognizing that 2.7.7.88 is not a sialic acid pathway enzyme, which follows from the absence of the NSS motif and unrelated substrate specificity.",
    "reason": "The sequence provides two independently informative motifs: the GAGKTT P-loop constrains the EC class to 2.7.7.x (nucleotidyltransferases), and the NSS motif specifically identifies the CMP-sialic acid synthase family, pointing to EC 2.7.7.43. These are general biochemical knowledge elements (nucleotide-binding motifs and sialic acid pathway signatures) rather than a single item-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three distinct EC classes (2.7.7, 2.7.8, 4.2.1), making the class-level distinction clear from the P-loop. Within 2.7.7, the NSS motif provides a specific family-level discriminator. No option is equally defensible given the sequence evidence."
  },
  "important_caveats": [
    "The NSS motif identification, while well-established in glycobiology, represents moderately specialized knowledge; a model unfamiliar with sialic acid biosynthesis motifs might struggle to distinguish A from B.",
    "The UniProt entry was first published 2025-06-18 with the EC annotation added via PubMed 38382015 (2024). The historical archived version (entry v2, Jan 2026) already carries the EC 2.7.7.43 annotation, so the key was available before the 2026-05-07 cutoff.",
    "EC 2.7.7.88 is a valid but obscure nucleotidyltransferase entry; its obscurity makes it a relatively easy distractor once the sialic acid pathway is recognized.",
    "All reviewer evidence is annotation-derived; the underlying experimental validation rests on the Ghosh & Raushel 2024 Biochemistry paper, which was not independently retrieved here."
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

**Accession:** `P0DY07` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
"P0DY07"
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"CMP-N-acetylneuraminate synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"CMP-Neu5Ac synthase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"2.7.7.43"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"N-acylneuraminate cytidylyltransferase"}}}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:11345"}}],"reaction":{"ecNumber":"2.7.7.43","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:11344"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:37563"},{"database":"ChEBI","id":"CHEBI:60073"},{"database":"ChEBI","id":"CHEBI:68671"}]}}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"81116 / NCTC 11828"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.379520+00:00.  

```text
DE   RecName: Full=N-acylneuraminate cytidylyltransferase {ECO:0000305};
DE            EC=2.7.7.43 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=CMP-N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};
DE            Short=CMP-Neu5Ac synthase {ECO:0000303|PubMed:38382015};
```

Source SHA-256: `4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)  
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.379520+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate +
CC         diphosphate; Xref=Rhea:RHEA:11344, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:37563, ChEBI:CHEBI:60073, ChEBI:CHEBI:68671; EC=2.7.7.43;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:11345;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 61. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
