# EC_number_0156

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 7.6.2.2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNTQPTRAIETSGLVKVYNGTRAVDGLDLDVPAGLVYGILGPNGAGKSTTIRMLATLLRPDGGTARVFGHDVTSEPDTVRRRISVTGQYASVDEGLTGTENLVMMGRLQGYSWARARERAAELIDGFGLGDARDRLLKTYSGGMRRRLDIAASIVVTPDLLFLDEPTTGLDPRSRNQVWDIVRALVDAGTTVLLTTQYLDEADQLADRIAVIDHGRVIAEGTTGELKSSLGSNVLRLRLHDAQSRAEAERLLSAELGVTIHRDSDPTALSARIDDPRQGMRALAELSRTQLEVRSFSLGQSSLDEVFLALTGHPADDRSTEEAAEEEKVA

[Multiple Choices]
A. 6.3.5.1
B. 7.6.2.2
C. 2.3.1.319
D. 4.3.1.12
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

> The exact sequence matches UniProt entry P0DXG8, which assigns EC 7.6.2.2 and annotates ATP-dependent daunorubicin export. This supports choice B, although the cited evidence is a curated annotation rather than, by itself, proof of a direct enzyme assay.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's P-loop/Walker A motif is consistent with an ATP-binding protein and favors a transporter ATPase over the listed ligase, transferase, and lyase choices. It does not establish the particular transported substrate or exact EC subclass.


**Missing item-specific fact**

> The protein-specific association with daunorubicin efflux, needed to support the exact EC 7.6.2.2 assignment, is absent from the question.


**Reason**

> Sequence motifs provide a broad functional clue, but the complete EC number depends on the protein's specific transport function, which requires an external annotation or other item-specific evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports B; the supplied sequence alone does not establish the exact EC number, but the other choices are not equally supported.


### Important caveats

- The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.
- The EC annotation cites curator-evaluated evidence and a paper on daunorubicin efflux; the excerpts do not independently establish a direct catalytic assay.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's P-loop/Walker A motif is consistent with an ATP-binding protein and favors a transporter ATPase over the listed ligase, transferase, and lyase choices. It does not establish the particular transported substrate or exact EC subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific association with daunorubicin efflux, needed to support the exact EC 7.6.2.2 assignment, is absent from the question.",
    "reason": "Sequence motifs provide a broad functional clue, but the complete EC number depends on the protein's specific transport function, which requires an external annotation or other item-specific evidence."
  },
  "case_id": "EC_number_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry P0DXG8, which assigns EC 7.6.2.2 and annotates ATP-dependent daunorubicin export. This supports choice B, although the cited evidence is a curated annotation rather than, by itself, proof of a direct enzyme assay."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.",
    "The EC annotation cites curator-evaluated evidence and a paper on daunorubicin efflux; the excerpts do not independently establish a direct catalytic assay."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports B; the supplied sequence alone does not establish the exact EC number, but the other choices are not equally supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry P0DXG8, which assigns EC 7.6.2.2 and annotates ATP-dependent daunorubicin export. This supports choice B, although the cited evidence is a curated annotation rather than, by itself, proof of a direct enzyme assay.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's P-loop/Walker A motif is consistent with an ATP-binding protein and favors a transporter ATPase over the listed ligase, transferase, and lyase choices. It does not establish the particular transported substrate or exact EC subclass.",
    "missing_item_specific_fact": "The protein-specific association with daunorubicin efflux, needed to support the exact EC 7.6.2.2 assignment, is absent from the question.",
    "reason": "Sequence motifs provide a broad functional clue, but the complete EC number depends on the protein's specific transport function, which requires an external annotation or other item-specific evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports B; the supplied sequence alone does not establish the exact EC number, but the other choices are not equally supported."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.",
    "The EC annotation cites curator-evaluated evidence and a paper on daunorubicin efflux; the excerpts do not independently establish a direct catalytic assay."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXG8 (sequence SHA256 match confirmed, 330 AA) annotates this protein as 'Daunorubicin resistance ATP-binding protein DrrA1' with EC 7.6.2.2, supported by experimental evidence (ECO:0000305, PubMed:39375957, 2024). The catalytic reaction is documented: daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+). The historical entry (v4, Swiss-Prot) and current entry (v6) both confirm EC 7.6.2.2.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Walker A (P-loop) motif 'GILGPNGAGKST' and an ABC transporter signature region 'IHRDSDPTALSARIDDPR', which together unambiguously identify this protein as an ABC-type ATP-binding translocase (EC 7.x.x.x). Among the four options, only B (EC 7.6.2.2) belongs to the translocase class (EC 7). Option A (EC 6.3.5.1) is a ligase (glutamine synthetase), option C (EC 2.3.1.319) is a transferase (acyltransferase), and option D (EC 4.3.1.12) is a lyase (argininosuccinate lyase). None of these enzyme classes contain ABC transporter architecture. Therefore, recognizing the ABC motifs and mapping them to the correct EC top-level class (translocases) is sufficient to select B from the given choices.


**Missing item-specific fact**

> The precise 4-digit assignment (7.6.2.2 specifically for daunorubicin efflux rather than other ABC-type translocases like 7.6.2.1) would require knowing the substrate specificity. However, since only one EC 7 option is presented, this does not impede answer selection from the given choices.


**Reason**

> The Walker A motif and ABC signature are well-known sequence features that any model with general enzymology knowledge can identify. These features place the protein in EC 7 (translocases), and only option B falls in that class. The reasoning is concrete and does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (B, EC 7.6.2.2) is an ABC translocase. The other three options belong to entirely different enzyme classes (ligase, transferase, lyase) that are incompatible with the ABC transporter motifs present in the sequence. No ambiguity exists among the choices.


### Important caveats

- The EC annotation carries evidence code ECO:0000305 (inferred by curator from literature), based on a 2024 paper (PubMed:39375957). The entry was first public on 2025-02-05, so this is a relatively recent annotation.
- The identity of the protein (P0DXG8, DrrA1) was inferred by the reviewer from dataset metadata, not from the model input. However, the reasoning argument (ABC motifs → EC 7 class) does not depend on knowing the accession.
- The organism (Streptomyces coeruleorubidus) is an anthracycline producer, consistent with daunorubicin efflux function, but this taxonomic context was not provided to the model.
- While the top-level class (EC 7) is clearly identifiable from motifs, the exact 4-digit number depends on substrate specificity determined experimentally. This does not affect answerability given the single EC 7 option.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Walker A (P-loop) motif 'GILGPNGAGKST' and an ABC transporter signature region 'IHRDSDPTALSARIDDPR', which together unambiguously identify this protein as an ABC-type ATP-binding translocase (EC 7.x.x.x). Among the four options, only B (EC 7.6.2.2) belongs to the translocase class (EC 7). Option A (EC 6.3.5.1) is a ligase (glutamine synthetase), option C (EC 2.3.1.319) is a transferase (acyltransferase), and option D (EC 4.3.1.12) is a lyase (argininosuccinate lyase). None of these enzyme classes contain ABC transporter architecture. Therefore, recognizing the ABC motifs and mapping them to the correct EC top-level class (translocases) is sufficient to select B from the given choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise 4-digit assignment (7.6.2.2 specifically for daunorubicin efflux rather than other ABC-type translocases like 7.6.2.1) would require knowing the substrate specificity. However, since only one EC 7 option is presented, this does not impede answer selection from the given choices.",
    "reason": "The Walker A motif and ABC signature are well-known sequence features that any model with general enzymology knowledge can identify. These features place the protein in EC 7 (translocases), and only option B falls in that class. The reasoning is concrete and does not require memorizing this specific protein's database entry."
  },
  "case_id": "EC_number_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXG8 (sequence SHA256 match confirmed, 330 AA) annotates this protein as 'Daunorubicin resistance ATP-binding protein DrrA1' with EC 7.6.2.2, supported by experimental evidence (ECO:0000305, PubMed:39375957, 2024). The catalytic reaction is documented: daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+). The historical entry (v4, Swiss-Prot) and current entry (v6) both confirm EC 7.6.2.2."
  },
  "important_caveats": [
    "The EC annotation carries evidence code ECO:0000305 (inferred by curator from literature), based on a 2024 paper (PubMed:39375957). The entry was first public on 2025-02-05, so this is a relatively recent annotation.",
    "The identity of the protein (P0DXG8, DrrA1) was inferred by the reviewer from dataset metadata, not from the model input. However, the reasoning argument (ABC motifs → EC 7 class) does not depend on knowing the accession.",
    "The organism (Streptomyces coeruleorubidus) is an anthracycline producer, consistent with daunorubicin efflux function, but this taxonomic context was not provided to the model.",
    "While the top-level class (EC 7) is clearly identifiable from motifs, the exact 4-digit number depends on substrate specificity determined experimentally. This does not affect answerability given the single EC 7 option."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (B, EC 7.6.2.2) is an ABC translocase. The other three options belong to entirely different enzyme classes (ligase, transferase, lyase) that are incompatible with the ABC transporter motifs present in the sequence. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXG8 (sequence SHA256 match confirmed, 330 AA) annotates this protein as 'Daunorubicin resistance ATP-binding protein DrrA1' with EC 7.6.2.2, supported by experimental evidence (ECO:0000305, PubMed:39375957, 2024). The catalytic reaction is documented: daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+). The historical entry (v4, Swiss-Prot) and current entry (v6) both confirm EC 7.6.2.2.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Walker A (P-loop) motif 'GILGPNGAGKST' and an ABC transporter signature region 'IHRDSDPTALSARIDDPR', which together unambiguously identify this protein as an ABC-type ATP-binding translocase (EC 7.x.x.x). Among the four options, only B (EC 7.6.2.2) belongs to the translocase class (EC 7). Option A (EC 6.3.5.1) is a ligase (glutamine synthetase), option C (EC 2.3.1.319) is a transferase (acyltransferase), and option D (EC 4.3.1.12) is a lyase (argininosuccinate lyase). None of these enzyme classes contain ABC transporter architecture. Therefore, recognizing the ABC motifs and mapping them to the correct EC top-level class (translocases) is sufficient to select B from the given choices.",
    "missing_item_specific_fact": "The precise 4-digit assignment (7.6.2.2 specifically for daunorubicin efflux rather than other ABC-type translocases like 7.6.2.1) would require knowing the substrate specificity. However, since only one EC 7 option is presented, this does not impede answer selection from the given choices.",
    "reason": "The Walker A motif and ABC signature are well-known sequence features that any model with general enzymology knowledge can identify. These features place the protein in EC 7 (translocases), and only option B falls in that class. The reasoning is concrete and does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (B, EC 7.6.2.2) is an ABC translocase. The other three options belong to entirely different enzyme classes (ligase, transferase, lyase) that are incompatible with the ABC transporter motifs present in the sequence. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The EC annotation carries evidence code ECO:0000305 (inferred by curator from literature), based on a 2024 paper (PubMed:39375957). The entry was first public on 2025-02-05, so this is a relatively recent annotation.",
    "The identity of the protein (P0DXG8, DrrA1) was inferred by the reviewer from dataset metadata, not from the model input. However, the reasoning argument (ABC motifs → EC 7 class) does not depend on knowing the accession.",
    "The organism (Streptomyces coeruleorubidus) is an anthracycline producer, consistent with daunorubicin efflux function, but this taxonomic context was not provided to the model.",
    "While the top-level class (EC 7) is clearly identifiable from motifs, the exact 4-digit number depends on substrate specificity determined experimentally. This does not affect answerability given the single EC 7 option."
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

**Accession:** `P0DXG8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.942110+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"value":"7.6.2.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Daunorubicin resistance ATP-binding protein DrrA1"}}}
```

Source SHA-256: `0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.942110+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:33148"}}],"reaction":{"ecNumber":"7.6.2.2","evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"name":"daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:33147"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:64677"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.942110+00:00.  

```json
{"citation":{"authors":["Dong J.","Ning J.","Tian Y.","Li H.","Chen H.","Guan W."],"citationCrossReferences":[{"database":"PubMed","id":"39375957"},{"database":"DOI","id":"10.1111/1751-7915.70023"}],"citationType":"journal article","firstPage":"e70023","id":"39375957","journal":"Microb. Biotechnol.","lastPage":"e70023","publicationDate":"2024","title":"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.","volume":"17"},"referenceNumber":2,"referencePositions":["FUNCTION IN DAUNORUBICIN EFFLUX","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:29.046585+00:00.  

```text
ID   DRRA1_STRC4             Reviewed;         330 AA.
AC   P0DXG8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA1 {ECO:0000305};
DE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};
GN   Name=drrA1 {ECO:0000303|PubMed:39375957};
GN   Synonyms=drrA {ECO:0000312|EMBL:WOT33550.1};
GN   ORFNames=R5U08_05025 {ECO:0000312|EMBL:WOT33550.1};
OS   Streptomyces coeruleorubidus.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=116188;
```

Source SHA-256: `f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:29.046585+00:00.  

```text
DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA1 {ECO:0000305};
DE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};
```

Source SHA-256: `f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)  
**Locator:** `lines 32-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:29.046585+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP +
CC         phosphate + H(+); Xref=Rhea:RHEA:33147, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:30616, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:64677, ChEBI:CHEBI:456216; EC=7.6.2.2;
CC         Evidence={ECO:0000305|PubMed:39375957};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33148;
CC         Evidence={ECO:0000305|PubMed:39375957};
```

Source SHA-256: `f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 156. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
