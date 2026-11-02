# active_site_0015

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 385 (Glycyl thioester intermediate)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNLTLDHTTLHRAAKYFMDSGKAASHEAAMNLLQQFGLTIYVGEEIRSSAAHQIALLTIVNVTRRTLLGGVEVIGLPDCDSLTALAPNTGLKEAVMALGGTPVAVARPEWPTALIGSVEDYSNKDTAWRVTWEGWRAGAAPLMIGDRLSEDNSMALAPALAAAVCAGEVFSHYAGDHPMAGRRTAGLSLWQPGADWLDVDESEPELAFLPSNLWIIGLGNLGQAFAWLLALMPYETPQELQLVLQDYDRIAPSNDSTSLLSYKHDTNKMKARVVADWLDKRGFTTFIEERRFGPWTKRHADEPGVALCGVDNALARSALDQAGFPLIVEAGLGGGPQAFRSLGIHTFPSSRTAAEIWAKQVALADTSTEDMPAYQALKKSGIDACGLTQLASRTVGVPFVGLIAACLAMSELLRRLHGGKAFEFIAGSTATLQDIEFGTLHAPPYAHGYTRAMPMGWPTAP

[Multiple Choices]
A. Position 661 (For beta-ketoacyl synthase activity)
B. Position 385 (Glycyl thioester intermediate)
C. Position 10 (Proton donor)
D. Position 700 (For beta-ketoacyl synthase activity)
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

> The exact sequence matches UniProt entry A0A1I1P074, which annotates position 385 as the active site for a glycyl thioester intermediate. The annotation cites a paper that includes mutagenesis of Cys-385. This supports choice B, though the primary experimental results were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and options reveal that positions 661 and 700 exceed the 461-residue sequence, and position 10 is leucine, making those distractors implausible. But this does not establish which in-range residue is the active site or that it forms a glycyl thioester intermediate.


**Missing item-specific fact**

> That Cys-385 of this particular protein is annotated as the active site involved in a glycyl thioester intermediate.


**Reason**

> The keyed role is a protein-specific functional fact not established by the supplied sequence alone. The supporting annotation and cited mutagenesis evidence are reviewer-only, not information supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the only plausible listed option: the other positions are out of range or identify leucine as a proton donor. Those eliminations do not independently demonstrate the active-site role.


### Important caveats

- The supporting UniProt annotation is linked to a publication and mutagenesis of Cys-385, but the primary paper was not independently assessed.
- The sequence match establishes applicability of the annotation to the supplied sequence; the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and options reveal that positions 661 and 700 exceed the 461-residue sequence, and position 10 is leucine, making those distractors implausible. But this does not establish which in-range residue is the active site or that it forms a glycyl thioester intermediate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That Cys-385 of this particular protein is annotated as the active site involved in a glycyl thioester intermediate.",
    "reason": "The keyed role is a protein-specific functional fact not established by the supplied sequence alone. The supporting annotation and cited mutagenesis evidence are reviewer-only, not information supplied to the evaluated model."
  },
  "case_id": "active_site_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry A0A1I1P074, which annotates position 385 as the active site for a glycyl thioester intermediate. The annotation cites a paper that includes mutagenesis of Cys-385. This supports choice B, though the primary experimental results were not independently reviewed here."
  },
  "important_caveats": [
    "The supporting UniProt annotation is linked to a publication and mutagenesis of Cys-385, but the primary paper was not independently assessed.",
    "The sequence match establishes applicability of the annotation to the supplied sequence; the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only plausible listed option: the other positions are out of range or identify leucine as a proton donor. Those eliminations do not independently demonstrate the active-site role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry A0A1I1P074, which annotates position 385 as the active site for a glycyl thioester intermediate. The annotation cites a paper that includes mutagenesis of Cys-385. This supports choice B, though the primary experimental results were not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and options reveal that positions 661 and 700 exceed the 461-residue sequence, and position 10 is leucine, making those distractors implausible. But this does not establish which in-range residue is the active site or that it forms a glycyl thioester intermediate.",
    "missing_item_specific_fact": "That Cys-385 of this particular protein is annotated as the active site involved in a glycyl thioester intermediate.",
    "reason": "The keyed role is a protein-specific functional fact not established by the supplied sequence alone. The supporting annotation and cited mutagenesis evidence are reviewer-only, not information supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only plausible listed option: the other positions are out of range or identify leucine as a proton donor. Those eliminations do not independently demonstrate the active-site role."
  },
  "important_caveats": [
    "The supporting UniProt annotation is linked to a publication and mutagenesis of Cys-385, but the primary paper was not independently assessed.",
    "The sequence match establishes applicability of the annotation to the supplied sequence; the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A1I1P074 (Bacterial E1-like protein BilD, EC 6.2.1.-) annotates an Active site at position 385 described as 'Glycyl thioester intermediate' (evidence ECO:0000305, PubMed:39020165). The cited reference (Hoer et al., Nature 631:850-856, 2024) reports 'FUNCTION, PROBABLE ACTIVE SITE, AND MUTAGENESIS OF CYS-385,' providing experimental support via mutagenesis. The sequence SHA-256 matches exactly (461 AA). This is consistent with E1 enzyme biochemistry where a catalytic cysteine forms a thioester intermediate with ubiquitin/ubiquitin-like proteins. Options A (position 661) and D (position 700) are beyond the 461-residue protein length, making them impossible.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General E1 enzyme biochemistry states that E1 (ubiquitin-activating) enzymes use a catalytic cysteine to form a thioester intermediate with the C-terminus of ubiquitin/ubiquitin-like proteins. This mechanistic knowledge eliminates option C ('Proton donor'), which is inconsistent with E1 catalysis. Options A and D are trivially eliminable because positions 661 and 700 exceed the 461-residue protein length. However, positively identifying this specific protein as E1-like from the raw sequence (to invoke E1 mechanism) and pinpointing the exact catalytic cysteine at position 385 require protein-specific annotation knowledge or domain-recognition tooling not derivable from general reasoning alone.


**Missing item-specific fact**

> The specific identity of this protein as a bacterial E1-like protein (BilD) and the exact position of its catalytic cysteine (385) are protein-specific facts. While the mechanistic description in option B is consistent with E1 biochemistry, confirming that this particular sequence is an E1-like enzyme and that Cys-385 is its catalytic residue requires database annotation or structural/biochemical characterization of this specific protein.


**Reason**

> The trivial elimination of out-of-range positions (A, D) and the mechanistic inconsistency of 'proton donor' with E1 catalysis (C) provide some reasoning grounds. However, the positive identification of B requires recognizing this specific protein as E1-like from the raw sequence and knowing that position 385 harbors the catalytic cysteine—both of which are item-specific facts not derivable from general biological reasoning applied to the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D reference positions (661, 700) that exceed the 461-residue protein length, making them physically impossible. Option C ('Proton donor') is mechanistically inconsistent with E1 enzyme catalysis. Only option B provides both a valid position within the protein and a mechanistically correct description for an E1-like enzyme. No ambiguity among defensible choices.


### Important caveats

- Options A and D are trivially eliminable by noting positions 661 and 700 exceed the 461-residue sequence length, reducing effective difficulty.
- The UniProt annotation evidence code ECO:0000305 indicates curator inference from the PubMed reference, but the underlying reference includes mutagenesis of Cys-385 (experimental support).
- The protein was only integrated into Swiss-Prot in April 2025; the author's source snapshot timing is unknown but the sequence has been unchanged since 2017.
- The reviewer-only evidence was absent from the evaluated model's input; the model must work from the raw sequence and options alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General E1 enzyme biochemistry states that E1 (ubiquitin-activating) enzymes use a catalytic cysteine to form a thioester intermediate with the C-terminus of ubiquitin/ubiquitin-like proteins. This mechanistic knowledge eliminates option C ('Proton donor'), which is inconsistent with E1 catalysis. Options A and D are trivially eliminable because positions 661 and 700 exceed the 461-residue protein length. However, positively identifying this specific protein as E1-like from the raw sequence (to invoke E1 mechanism) and pinpointing the exact catalytic cysteine at position 385 require protein-specific annotation knowledge or domain-recognition tooling not derivable from general reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as a bacterial E1-like protein (BilD) and the exact position of its catalytic cysteine (385) are protein-specific facts. While the mechanistic description in option B is consistent with E1 biochemistry, confirming that this particular sequence is an E1-like enzyme and that Cys-385 is its catalytic residue requires database annotation or structural/biochemical characterization of this specific protein.",
    "reason": "The trivial elimination of out-of-range positions (A, D) and the mechanistic inconsistency of 'proton donor' with E1 catalysis (C) provide some reasoning grounds. However, the positive identification of B requires recognizing this specific protein as E1-like from the raw sequence and knowing that position 385 harbors the catalytic cysteine—both of which are item-specific facts not derivable from general biological reasoning applied to the sequence alone."
  },
  "case_id": "active_site_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A1I1P074 (Bacterial E1-like protein BilD, EC 6.2.1.-) annotates an Active site at position 385 described as 'Glycyl thioester intermediate' (evidence ECO:0000305, PubMed:39020165). The cited reference (Hoer et al., Nature 631:850-856, 2024) reports 'FUNCTION, PROBABLE ACTIVE SITE, AND MUTAGENESIS OF CYS-385,' providing experimental support via mutagenesis. The sequence SHA-256 matches exactly (461 AA). This is consistent with E1 enzyme biochemistry where a catalytic cysteine forms a thioester intermediate with ubiquitin/ubiquitin-like proteins. Options A (position 661) and D (position 700) are beyond the 461-residue protein length, making them impossible."
  },
  "important_caveats": [
    "Options A and D are trivially eliminable by noting positions 661 and 700 exceed the 461-residue sequence length, reducing effective difficulty.",
    "The UniProt annotation evidence code ECO:0000305 indicates curator inference from the PubMed reference, but the underlying reference includes mutagenesis of Cys-385 (experimental support).",
    "The protein was only integrated into Swiss-Prot in April 2025; the author's source snapshot timing is unknown but the sequence has been unchanged since 2017.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must work from the raw sequence and options alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D reference positions (661, 700) that exceed the 461-residue protein length, making them physically impossible. Option C ('Proton donor') is mechanistically inconsistent with E1 enzyme catalysis. Only option B provides both a valid position within the protein and a mechanistically correct description for an E1-like enzyme. No ambiguity among defensible choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A1I1P074 (Bacterial E1-like protein BilD, EC 6.2.1.-) annotates an Active site at position 385 described as 'Glycyl thioester intermediate' (evidence ECO:0000305, PubMed:39020165). The cited reference (Hoer et al., Nature 631:850-856, 2024) reports 'FUNCTION, PROBABLE ACTIVE SITE, AND MUTAGENESIS OF CYS-385,' providing experimental support via mutagenesis. The sequence SHA-256 matches exactly (461 AA). This is consistent with E1 enzyme biochemistry where a catalytic cysteine forms a thioester intermediate with ubiquitin/ubiquitin-like proteins. Options A (position 661) and D (position 700) are beyond the 461-residue protein length, making them impossible.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General E1 enzyme biochemistry states that E1 (ubiquitin-activating) enzymes use a catalytic cysteine to form a thioester intermediate with the C-terminus of ubiquitin/ubiquitin-like proteins. This mechanistic knowledge eliminates option C ('Proton donor'), which is inconsistent with E1 catalysis. Options A and D are trivially eliminable because positions 661 and 700 exceed the 461-residue protein length. However, positively identifying this specific protein as E1-like from the raw sequence (to invoke E1 mechanism) and pinpointing the exact catalytic cysteine at position 385 require protein-specific annotation knowledge or domain-recognition tooling not derivable from general reasoning alone.",
    "missing_item_specific_fact": "The specific identity of this protein as a bacterial E1-like protein (BilD) and the exact position of its catalytic cysteine (385) are protein-specific facts. While the mechanistic description in option B is consistent with E1 biochemistry, confirming that this particular sequence is an E1-like enzyme and that Cys-385 is its catalytic residue requires database annotation or structural/biochemical characterization of this specific protein.",
    "reason": "The trivial elimination of out-of-range positions (A, D) and the mechanistic inconsistency of 'proton donor' with E1 catalysis (C) provide some reasoning grounds. However, the positive identification of B requires recognizing this specific protein as E1-like from the raw sequence and knowing that position 385 harbors the catalytic cysteine—both of which are item-specific facts not derivable from general biological reasoning applied to the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D reference positions (661, 700) that exceed the 461-residue protein length, making them physically impossible. Option C ('Proton donor') is mechanistically inconsistent with E1 enzyme catalysis. Only option B provides both a valid position within the protein and a mechanistically correct description for an E1-like enzyme. No ambiguity among defensible choices."
  },
  "important_caveats": [
    "Options A and D are trivially eliminable by noting positions 661 and 700 exceed the 461-residue sequence length, reducing effective difficulty.",
    "The UniProt annotation evidence code ECO:0000305 indicates curator inference from the PubMed reference, but the underlying reference includes mutagenesis of Cys-385 (experimental support).",
    "The protein was only integrated into Swiss-Prot in April 2025; the author's source snapshot timing is unknown but the sequence has been unchanged since 2017.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must work from the raw sequence and options alone."
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

**Accession:** `A0A1I1P074` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1P074.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:37.902008+00:00.  

```json
"A0A1I1P074"
```

Source SHA-256: `85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1P074.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:37.902008+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"E1 ubiquitin-conjugating enzyme BilD"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39020165","source":"PubMed"}],"value":"6.2.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39020165","source":"PubMed"}],"value":"Bacterial E1-like protein BilD"}}}
```

Source SHA-256: `85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1P074.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:37.902008+00:00.  

```json
{"description":"Glycyl thioester intermediate","evidences":[{"evidenceCode":"ECO:0000305","id":"39020165","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":385},"start":{"modifier":"EXACT","value":385}},"type":"Active site"}
```

Source SHA-256: `85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1P074.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:37.902008+00:00.  

```json
{"citation":{"authors":["Hoer J.","Wolf S.G.","Sorek R."],"citationCrossReferences":[{"database":"PubMed","id":"39020165"},{"database":"DOI","id":"10.1038/s41586-024-07616-5"}],"citationType":"journal article","firstPage":"850","id":"39020165","journal":"Nature","lastPage":"856","publicationDate":"2024","title":"Bacteria conjugate ubiquitin-like proteins to interfere with phage assembly.","volume":"631"},"referenceNumber":2,"referencePositions":["FUNCTION","PROBABLE ACTIVE SITE","MUTAGENESIS OF CYS-385"]}
```

Source SHA-256: `85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1P074?format=txt&versions=13)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:24:41.131133+00:00.  

```text
ID   BILD_COLS4              Reviewed;         461 AA.
AC   A0A1I1P074;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   22-NOV-2017, sequence version 1.
DT   28-JAN-2026, entry version 13.
DE   RecName: Full=Bacterial E1-like protein BilD {ECO:0000303|PubMed:39020165};
DE            EC=6.2.1.- {ECO:0000305|PubMed:39020165};
DE   AltName: Full=E1 ubiquitin-conjugating enzyme BilD;
GN   Name=bilD {ECO:0000303|PubMed:39020165};
GN   ORFNames=SAMN04515619_11955 {ECO:0000312|EMBL:SFD01128.1};
OS   Collimonas sp. (strain OK412).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;
OC   Burkholderiales; Oxalobacteraceae; Collimonas.
OX   NCBI_TaxID=1801619;
```

Source SHA-256: `a37af1ad780f0f67b0b403cc351978c7e209c2d02ee53894ad0fc5e2c09bea6a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1P074?format=txt&versions=13)  
**Locator:** `lines 20-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:24:41.131133+00:00.  

```text
RN   [2]
RP   FUNCTION, PROBABLE ACTIVE SITE, AND MUTAGENESIS OF CYS-385.
RX   PubMed=39020165; DOI=10.1038/s41586-024-07616-5;
RA   Hoer J., Wolf S.G., Sorek R.;
RT   "Bacteria conjugate ubiquitin-like proteins to interfere with phage
RT   assembly.";
RL   Nature 631:850-856(2024).
```

Source SHA-256: `a37af1ad780f0f67b0b403cc351978c7e209c2d02ee53894ad0fc5e2c09bea6a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1P074?format=txt&versions=13)  
**Locator:** `lines 73-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:24:41.131133+00:00.  

```text
FT   ACT_SITE        385
FT                   /note="Glycyl thioester intermediate"
FT                   /evidence="ECO:0000305|PubMed:39020165"
```

Source SHA-256: `a37af1ad780f0f67b0b403cc351978c7e209c2d02ee53894ad0fc5e2c09bea6a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 15. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
