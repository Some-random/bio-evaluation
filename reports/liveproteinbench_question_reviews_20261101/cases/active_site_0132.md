# active_site_0132

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 67 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDRKVQVLDFIKINPAGNITILIDNFDIYDKNIPKLSEEIMKETNLYAEQVGFIKDSHLQMMGGEFCGNASRAFASLLAFRDKDFSKQKNYNITCSGESKVLDVDVRNDGAKNKFLAKIKMPKFLSLEEINVDEYKLGLVRFSGINHFIFNIKENKETSFENIIDLVKKYLSNEEYSAFGIMFFDSDNLSMKPYVYVKEVGSGVYENSCASGTTALGYYLKKCKNLDRAKIVQPNGWLEYIIENDEMYIDGPVEIIAEGKIYIGK

[Multiple Choices]
A. Position 2428 (For thioesterase activity)
B. Position 67 (Proton acceptor)
C. Position 241 (Lowers pKa of active site Tyr)
D. Position 38 (Nucleophile)
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

> The exact sequence matches a UniProt entry annotating position 67 as the proton acceptor; the archived entry available by the historical cutoff carries the same annotation. This supports the key as a database annotation, though the cited evidence code is curator inference and the excerpts do not independently establish the experimental result.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a cysteine at position 67, which is compatible with a catalytic role, but the sequence and choices alone do not establish that this residue is the proton acceptor rather than another active-site residue.


**Missing item-specific fact**

> The protein-specific assignment of residue 67 as the proton acceptor, provided by the histidine-racemase annotation and its cited study.


**Reason**

> Identifying the exact catalytic role requires protein-specific functional or structural information not supplied with the sequence; recognizing the sequence or recalling its annotation would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only matched-sequence annotation supports B. Option A gives a position beyond the 265-residue sequence; the other options are not supported by the supplied input.


### Important caveats

- UniProt labels the active-site assignment with ECO:0000305, indicating curator inference; the excerpts cite a relevant study but do not reproduce its direct experimental findings.
- The exact author source snapshot is unknown, although the annotation appears in the archived entry available by the stated historical cutoff.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a cysteine at position 67, which is compatible with a catalytic role, but the sequence and choices alone do not establish that this residue is the proton acceptor rather than another active-site residue.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of residue 67 as the proton acceptor, provided by the histidine-racemase annotation and its cited study.",
    "reason": "Identifying the exact catalytic role requires protein-specific functional or structural information not supplied with the sequence; recognizing the sequence or recalling its annotation would be lookup or memorization."
  },
  "case_id": "active_site_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating position 67 as the proton acceptor; the archived entry available by the historical cutoff carries the same annotation. This supports the key as a database annotation, though the cited evidence code is curator inference and the excerpts do not independently establish the experimental result."
  },
  "important_caveats": [
    "UniProt labels the active-site assignment with ECO:0000305, indicating curator inference; the excerpts cite a relevant study but do not reproduce its direct experimental findings.",
    "The exact author source snapshot is unknown, although the annotation appears in the archived entry available by the stated historical cutoff."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports B. Option A gives a position beyond the 265-residue sequence; the other options are not supported by the supplied input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating position 67 as the proton acceptor; the archived entry available by the historical cutoff carries the same annotation. This supports the key as a database annotation, though the cited evidence code is curator inference and the excerpts do not independently establish the experimental result.",
    "evidence_ids": ["C5", "H3", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a cysteine at position 67, which is compatible with a catalytic role, but the sequence and choices alone do not establish that this residue is the proton acceptor rather than another active-site residue.",
    "missing_item_specific_fact": "The protein-specific assignment of residue 67 as the proton acceptor, provided by the histidine-racemase annotation and its cited study.",
    "reason": "Identifying the exact catalytic role requires protein-specific functional or structural information not supplied with the sequence; recognizing the sequence or recalling its annotation would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports B. Option A gives a position beyond the 265-residue sequence; the other options are not supported by the supplied input."
  },
  "important_caveats": [
    "UniProt labels the active-site assignment with ECO:0000305, indicating curator inference; the excerpts cite a relevant study but do not reproduce its direct experimental findings.",
    "The exact author source snapshot is unknown, although the annotation appears in the archived entry available by the stated historical cutoff."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8RI81 (Histidine racemase, EC 5.1.1.24, Fusobacterium nucleatum) explicitly annotates position 67 as 'Proton acceptor' (Active site, ECO:0000305|PubMed:39424140). The supporting publication (Lamer et al., JBC 2024, PMID 39424140) includes X-ray crystallography of C67S and C209S mutants and mutagenesis data confirming Cys-67 as the proton acceptor. The benchmark sequence (265 aa, SHA256 matched) corresponds exactly to this entry. Position 67 in the supplied sequence is indeed Cys (C), consistent with the annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Mechanistic reasoning can partially narrow choices: racemases (EC 5.1.x.x) operate by proton abstraction and return, making 'Proton acceptor' (B) mechanistically consistent while 'Nucleophile' (D) and 'Lowers pKa of active site Tyr' (C) describe mechanisms of serine hydrolases and tyrosine-dependent enzymes respectively. Option A is trivially eliminated because position 2428 exceeds the 265-aa sequence length. However, identifying this specific 265-aa sequence as a cofactor-independent histidine racemase and pinpointing Cys-67 (rather than Cys-209 or another residue) as the proton acceptor requires knowledge of this protein's specific annotation and the 2024 crystallographic/mutagenesis study.


**Missing item-specific fact**

> The protein's identity as histidine racemase (EC 5.1.1.24) and the experimental determination that Cys-67 (not Cys-209 or other positions) is the proton acceptor active site, established by X-ray crystallography of C67S/C209S mutants (PDB 9CR1, 9CR6) and site-directed mutagenesis (PMID 39424140).


**Reason**

> While general mechanistic knowledge (racemases use proton transfer, not nucleophilic attack or tyrosine pKa modulation) helps prefer B over C and D, the specific assignment of position 67 as the proton acceptor for this particular protein requires item-specific experimental annotation. The sequence alone does not contain a recognizable motif that unambiguously identifies Cys-67 as the catalytic residue without database or literature lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is eliminated by sequence length (265 aa vs. position 2428). Options C and D describe mechanistic roles (Tyr pKa modulation, nucleophile) inconsistent with racemase chemistry. Only B provides a mechanistic description (proton acceptor) that matches the known catalytic mechanism of EC 5.1.1.24 racemases. No other option is defensible.


### Important caveats

- The UniProt annotation for position 67 uses evidence code ECO:0000305 (inferred from reference), supported by the 2024 JBC publication with crystallographic and mutagenesis data (ECO:0007744 from PDB 9CR1/9CR6). This is experimental evidence, not purely computational.
- The protein also has a second annotated active site at position 209 (Proton donor), which is not offered as an option.
- The sequence was first released in 2002 but the active-site annotation was only added in 2025 (entry first public date 2025-04-09), meaning the active-site information is relatively recent.
- The reviewer identified the accession Q8RI81 from dataset image-path metadata; this identifier was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Mechanistic reasoning can partially narrow choices: racemases (EC 5.1.x.x) operate by proton abstraction and return, making 'Proton acceptor' (B) mechanistically consistent while 'Nucleophile' (D) and 'Lowers pKa of active site Tyr' (C) describe mechanisms of serine hydrolases and tyrosine-dependent enzymes respectively. Option A is trivially eliminated because position 2428 exceeds the 265-aa sequence length. However, identifying this specific 265-aa sequence as a cofactor-independent histidine racemase and pinpointing Cys-67 (rather than Cys-209 or another residue) as the proton acceptor requires knowledge of this protein's specific annotation and the 2024 crystallographic/mutagenesis study.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as histidine racemase (EC 5.1.1.24) and the experimental determination that Cys-67 (not Cys-209 or other positions) is the proton acceptor active site, established by X-ray crystallography of C67S/C209S mutants (PDB 9CR1, 9CR6) and site-directed mutagenesis (PMID 39424140).",
    "reason": "While general mechanistic knowledge (racemases use proton transfer, not nucleophilic attack or tyrosine pKa modulation) helps prefer B over C and D, the specific assignment of position 67 as the proton acceptor for this particular protein requires item-specific experimental annotation. The sequence alone does not contain a recognizable motif that unambiguously identifies Cys-67 as the catalytic residue without database or literature lookup."
  },
  "case_id": "active_site_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8RI81 (Histidine racemase, EC 5.1.1.24, Fusobacterium nucleatum) explicitly annotates position 67 as 'Proton acceptor' (Active site, ECO:0000305|PubMed:39424140). The supporting publication (Lamer et al., JBC 2024, PMID 39424140) includes X-ray crystallography of C67S and C209S mutants and mutagenesis data confirming Cys-67 as the proton acceptor. The benchmark sequence (265 aa, SHA256 matched) corresponds exactly to this entry. Position 67 in the supplied sequence is indeed Cys (C), consistent with the annotation."
  },
  "important_caveats": [
    "The UniProt annotation for position 67 uses evidence code ECO:0000305 (inferred from reference), supported by the 2024 JBC publication with crystallographic and mutagenesis data (ECO:0007744 from PDB 9CR1/9CR6). This is experimental evidence, not purely computational.",
    "The protein also has a second annotated active site at position 209 (Proton donor), which is not offered as an option.",
    "The sequence was first released in 2002 but the active-site annotation was only added in 2025 (entry first public date 2025-04-09), meaning the active-site information is relatively recent.",
    "The reviewer identified the accession Q8RI81 from dataset image-path metadata; this identifier was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by sequence length (265 aa vs. position 2428). Options C and D describe mechanistic roles (Tyr pKa modulation, nucleophile) inconsistent with racemase chemistry. Only B provides a mechanistic description (proton acceptor) that matches the known catalytic mechanism of EC 5.1.1.24 racemases. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8RI81 (Histidine racemase, EC 5.1.1.24, Fusobacterium nucleatum) explicitly annotates position 67 as 'Proton acceptor' (Active site, ECO:0000305|PubMed:39424140). The supporting publication (Lamer et al., JBC 2024, PMID 39424140) includes X-ray crystallography of C67S and C209S mutants and mutagenesis data confirming Cys-67 as the proton acceptor. The benchmark sequence (265 aa, SHA256 matched) corresponds exactly to this entry. Position 67 in the supplied sequence is indeed Cys (C), consistent with the annotation.",
    "evidence_ids": ["C5", "C6", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Mechanistic reasoning can partially narrow choices: racemases (EC 5.1.x.x) operate by proton abstraction and return, making 'Proton acceptor' (B) mechanistically consistent while 'Nucleophile' (D) and 'Lowers pKa of active site Tyr' (C) describe mechanisms of serine hydrolases and tyrosine-dependent enzymes respectively. Option A is trivially eliminated because position 2428 exceeds the 265-aa sequence length. However, identifying this specific 265-aa sequence as a cofactor-independent histidine racemase and pinpointing Cys-67 (rather than Cys-209 or another residue) as the proton acceptor requires knowledge of this protein's specific annotation and the 2024 crystallographic/mutagenesis study.",
    "missing_item_specific_fact": "The protein's identity as histidine racemase (EC 5.1.1.24) and the experimental determination that Cys-67 (not Cys-209 or other positions) is the proton acceptor active site, established by X-ray crystallography of C67S/C209S mutants (PDB 9CR1, 9CR6) and site-directed mutagenesis (PMID 39424140).",
    "reason": "While general mechanistic knowledge (racemases use proton transfer, not nucleophilic attack or tyrosine pKa modulation) helps prefer B over C and D, the specific assignment of position 67 as the proton acceptor for this particular protein requires item-specific experimental annotation. The sequence alone does not contain a recognizable motif that unambiguously identifies Cys-67 as the catalytic residue without database or literature lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by sequence length (265 aa vs. position 2428). Options C and D describe mechanistic roles (Tyr pKa modulation, nucleophile) inconsistent with racemase chemistry. Only B provides a mechanistic description (proton acceptor) that matches the known catalytic mechanism of EC 5.1.1.24 racemases. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt annotation for position 67 uses evidence code ECO:0000305 (inferred from reference), supported by the 2024 JBC publication with crystallographic and mutagenesis data (ECO:0007744 from PDB 9CR1/9CR6). This is experimental evidence, not purely computational.",
    "The protein also has a second annotated active site at position 209 (Proton donor), which is not offered as an option.",
    "The sequence was first released in 2002 but the active-site annotation was only added in 2025 (entry first public date 2025-04-09), meaning the active-site information is relatively recent.",
    "The reviewer identified the accession Q8RI81 from dataset image-path metadata; this identifier was not provided to the evaluated model."
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

**Accession:** `Q8RI81` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 79. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.407556+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000305","id":"39424140","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":67},"start":{"modifier":"EXACT","value":67}},"type":"Active site"}
```

Source SHA-256: `0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.407556+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000305","id":"39424140","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":209},"start":{"modifier":"EXACT","value":209}},"type":"Active site"}
```

Source SHA-256: `0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.407556+00:00.  

```json
{"citation":{"authors":["Lamer T.","Chen P.","Venter M.J.","van Belkum M.J.","Wijewardane A.","Wu C.","Lemieux M.J.","Vederas J.C."],"citationCrossReferences":[{"database":"PubMed","id":"39424140"},{"database":"DOI","id":"10.1016/j.jbc.2024.107896"}],"citationType":"journal article","firstPage":"107896","id":"39424140","journal":"J. Biol. Chem.","lastPage":"107896","publicationDate":"2024","title":"Discovery, characterization, and structure of a cofactor-independent histidine racemase from the oral pathogen Fusobacterium nucleatum.","volume":"300"},"evidences":[{"evidenceCode":"ECO:0007744","id":"9CR1","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9CR6","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","ACTIVE SITE","MUTAGENESIS OF CYS-67 AND CYS-209"]}
```

Source SHA-256: `0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
ID   HISR_FUSNN              Reviewed;         265 AA.
AC   Q8RI81;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-2002, sequence version 1.
DT   28-JAN-2026, entry version 79.
DE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};
DE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};
GN   Name=hisR {ECO:0000303|PubMed:39424140};
GN   OrderedLocusNames=FN1732 {ECO:0000312|EMBL:AAL93847.1};
OS   Fusobacterium nucleatum subsp. nucleatum (strain ATCC 25586 / DSM 15643 /
OS   BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355).
OC   Bacteria; Fusobacteriati; Fusobacteriota; Fusobacteriia; Fusobacteriales;
OC   Fusobacteriaceae; Fusobacterium.
OX   NCBI_TaxID=190304;
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 36-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
RN   [3] {ECO:0007744|PDB:9CR1, ECO:0007744|PDB:9CR6}
RP   X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209,
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF CYS-67 AND CYS-209.
RC   STRAIN=ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC
RC   2640 / LMG 13131 / VPI 4355;
RX   PubMed=39424140; DOI=10.1016/j.jbc.2024.107896;
RA   Lamer T., Chen P., Venter M.J., van Belkum M.J., Wijewardane A., Wu C.,
RA   Lemieux M.J., Vederas J.C.;
RT   "Discovery, characterization, and structure of a cofactor-independent
RT   histidine racemase from the oral pathogen Fusobacterium nucleatum.";
RL   J. Biol. Chem. 300:107896-107896(2024).
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 114-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
FT   ACT_SITE        67
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000305|PubMed:39424140"
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 117-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
FT   ACT_SITE        209
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000305|PubMed:39424140"
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 132. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
