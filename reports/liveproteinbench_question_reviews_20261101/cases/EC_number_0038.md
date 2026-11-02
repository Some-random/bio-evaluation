# EC_number_0038

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.4.1.259

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPPAARARYIANKADNQILSKKPPKRPGLNGNNKTKEATPAGKKKDKDAKKRNQPTSGGQEKGLPNPIMPSVQTAFKTFVSARLCSAIWAYIADCDETFNYWEPLHYIINGHGLQTWEYSPQFGLRSYTYLLLQGVPGYFYQKLFNPSPILIFYMVRCMLGFGCAVMERYMYKSICQEFGIHIGRLWLIFQLFSVGMFVSSTALLPSSFSMYFGCAALAAWWQQNYCFAIFLTAISALLGWPFAALIGIPLVLEMLLRQRDWKTFVQWTLISGATVAIPMIAIDTSYFGKLTFAPLNIVWYNVFTSHGPNIFGTEPLSYYIINGFLNFNIIWLLALQLPIMLVIDYLIVPAKSKSTLNFPHYISLAPLYLWLLVFFAQPHKEERFLFPIYPLISLCGAITVDVYQRIFFRMKSVVFKIKAGVHYLDHSMFIAILVMVTSTLLGLSRVFALYRNYHAPMDLMLELNQFKATPQYDPDVIYNVCIGKDWHRYPGSFFFPAKNFRLRFLKSEFRGMLPAYYDEGQNATKVVQPYFNDLNQENEHMYFDYDRCDFLVDFDEGKYTALEPNYSKRSKDWSVMKSLPFLIPEKSHKVLRAFYVPFLTDNHIQYGDFNLLKRKTKRNGR

[Multiple Choices]
A. 2.4.1.392
B. 4.2.1.70
C. 2.4.1.259
D. 2.3.1.319
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

> The exact sequence matches the Drosophila Alg9 record, which annotates EC 2.4.1.259 and describes the corresponding mannosyltransferase reaction. This support is transferred by similarity from Q9H6U8 (ECO:0000250), not evidence of direct experimental characterization of this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a multipass membrane glycosyltransferase, but that broad inference does not determine its precise glycan substrate, reaction, or complete EC number.


**Missing item-specific fact**

> Identifying this protein as Alg9 and knowing its specific annotated mannosyltransferase activities requires protein-specific functional annotation or experimental knowledge absent from the input.


**Reason**

> The exact EC distinction among the choices depends on the specific reaction catalyzed, which cannot be established from the sequence and choices by general biological reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the evidence supports C. The matched record also annotates EC 2.4.1.261 for a second reaction, but that number is not offered as an option.


### Important caveats

- The supporting EC annotations are similarity-based transfers, not direct experimental evidence for the supplied Drosophila protein.
- The exact author data snapshot is unknown, though the matched historical record available by the stated cutoff includes EC 2.4.1.259.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a multipass membrane glycosyltransferase, but that broad inference does not determine its precise glycan substrate, reaction, or complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this protein as Alg9 and knowing its specific annotated mannosyltransferase activities requires protein-specific functional annotation or experimental knowledge absent from the input.",
    "reason": "The exact EC distinction among the choices depends on the specific reaction catalyzed, which cannot be established from the sequence and choices by general biological reasoning alone."
  },
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila Alg9 record, which annotates EC 2.4.1.259 and describes the corresponding mannosyltransferase reaction. This support is transferred by similarity from Q9H6U8 (ECO:0000250), not evidence of direct experimental characterization of this exact protein."
  },
  "important_caveats": [
    "The supporting EC annotations are similarity-based transfers, not direct experimental evidence for the supplied Drosophila protein.",
    "The exact author data snapshot is unknown, though the matched historical record available by the stated cutoff includes EC 2.4.1.259."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the evidence supports C. The matched record also annotates EC 2.4.1.261 for a second reaction, but that number is not offered as an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila Alg9 record, which annotates EC 2.4.1.259 and describes the corresponding mannosyltransferase reaction. This support is transferred by similarity from Q9H6U8 (ECO:0000250), not evidence of direct experimental characterization of this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a multipass membrane glycosyltransferase, but that broad inference does not determine its precise glycan substrate, reaction, or complete EC number.",
    "missing_item_specific_fact": "Identifying this protein as Alg9 and knowing its specific annotated mannosyltransferase activities requires protein-specific functional annotation or experimental knowledge absent from the input.",
    "reason": "The exact EC distinction among the choices depends on the specific reaction catalyzed, which cannot be established from the sequence and choices by general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the evidence supports C. The matched record also annotates EC 2.4.1.261 for a second reaction, but that number is not offered as an option."
  },
  "important_caveats": [
    "The supporting EC annotations are similarity-based transfers, not direct experimental evidence for the supplied Drosophila protein.",
    "The exact author data snapshot is unknown, though the matched historical record available by the stated cutoff includes EC 2.4.1.259."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9VBV8 (ALG9_DROME, Drosophila melanogaster Alpha-1,2-mannosyltransferase Alg9) exactly (623 AA, SHA256 confirmed). The UniProt entry assigns EC 2.4.1.259 (and also EC 2.4.1.261) with evidence code ECO:0000250 (inferred by similarity from human Q9H6U8). Among the four choices, only 2.4.1.259 (option C) appears in the annotation. The other options (2.4.1.392, 4.2.1.70, 2.3.1.319) are unrelated EC numbers. The annotation is computational (transferred by similarity), not direct experimental evidence for the Drosophila protein, but it is the official database assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could note the protein is a polytopic membrane protein with multiple hydrophobic segments consistent with an ER-resident enzyme, and might infer it belongs to the transferase class (EC 2) rather than lyase (EC 4), eliminating option B. However, distinguishing EC 2.4.1.259 (alpha-1,2-mannosyltransferase Alg9, GT47 family) from EC 2.4.1.392 (another glycosyltransferase) and EC 2.3.1.319 (acyltransferase) requires knowing the specific protein family, its role in the dolichol-linked N-glycan biosynthesis pathway (adding the 6th mannose to Man5GlcNAc2-PP-dolichol), and the exact EC assignment. No general sequence motif or biochemical reasoning from the raw 623-aa sequence alone reliably distinguishes these four specific EC numbers.


**Missing item-specific fact**

> The specific identity of this sequence as Alg9 (Drosophila ortholog of human DPAGT1-pathway mannosyltransferase) and the knowledge that Alg9 catalyzes the alpha-1,2-mannosyl transfer step designated EC 2.4.1.259 (as opposed to other glycosyltransferase EC numbers in the choices). This is a protein-specific database annotation.


**Reason**

> While the transferase vs. lyase distinction (eliminating B) is somewhat accessible, the precise 4-digit EC assignment among three transferase options (A, C, D) requires recognizing this as Alg9 and recalling its specific EC number. This is fundamentally a sequence-to-annotation lookup task, not a reasoning task from general biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry annotates both EC 2.4.1.259 and EC 2.4.1.261, only 2.4.1.259 appears among the four choices. None of the distractors match any annotation for this protein. Thus, among the given options, only C is defensible.


### Important caveats

- The EC assignment carries evidence code ECO:0000250 (inferred by similarity from human Q9H6U8), not direct experimental characterization of the Drosophila protein.
- The protein is annotated with a second EC number (2.4.1.261) for a later step in the same pathway; the question asks for 'the' EC number (singular), which is slightly imprecise, but this does not affect answer selection since 2.4.1.261 is not a choice.
- The UniProt entry was first public in 2025-06-18 (Swiss-Prot reviewed status); the benchmark's author source snapshot is unknown but the sequence has been unchanged since 2000.
- The accession identity was inferred by the reviewer from dataset metadata, not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could note the protein is a polytopic membrane protein with multiple hydrophobic segments consistent with an ER-resident enzyme, and might infer it belongs to the transferase class (EC 2) rather than lyase (EC 4), eliminating option B. However, distinguishing EC 2.4.1.259 (alpha-1,2-mannosyltransferase Alg9, GT47 family) from EC 2.4.1.392 (another glycosyltransferase) and EC 2.3.1.319 (acyltransferase) requires knowing the specific protein family, its role in the dolichol-linked N-glycan biosynthesis pathway (adding the 6th mannose to Man5GlcNAc2-PP-dolichol), and the exact EC assignment. No general sequence motif or biochemical reasoning from the raw 623-aa sequence alone reliably distinguishes these four specific EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this sequence as Alg9 (Drosophila ortholog of human DPAGT1-pathway mannosyltransferase) and the knowledge that Alg9 catalyzes the alpha-1,2-mannosyl transfer step designated EC 2.4.1.259 (as opposed to other glycosyltransferase EC numbers in the choices). This is a protein-specific database annotation.",
    "reason": "While the transferase vs. lyase distinction (eliminating B) is somewhat accessible, the precise 4-digit EC assignment among three transferase options (A, C, D) requires recognizing this as Alg9 and recalling its specific EC number. This is fundamentally a sequence-to-annotation lookup task, not a reasoning task from general biochemistry."
  },
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VBV8 (ALG9_DROME, Drosophila melanogaster Alpha-1,2-mannosyltransferase Alg9) exactly (623 AA, SHA256 confirmed). The UniProt entry assigns EC 2.4.1.259 (and also EC 2.4.1.261) with evidence code ECO:0000250 (inferred by similarity from human Q9H6U8). Among the four choices, only 2.4.1.259 (option C) appears in the annotation. The other options (2.4.1.392, 4.2.1.70, 2.3.1.319) are unrelated EC numbers. The annotation is computational (transferred by similarity), not direct experimental evidence for the Drosophila protein, but it is the official database assignment."
  },
  "important_caveats": [
    "The EC assignment carries evidence code ECO:0000250 (inferred by similarity from human Q9H6U8), not direct experimental characterization of the Drosophila protein.",
    "The protein is annotated with a second EC number (2.4.1.261) for a later step in the same pathway; the question asks for 'the' EC number (singular), which is slightly imprecise, but this does not affect answer selection since 2.4.1.261 is not a choice.",
    "The UniProt entry was first public in 2025-06-18 (Swiss-Prot reviewed status); the benchmark's author source snapshot is unknown but the sequence has been unchanged since 2000.",
    "The accession identity was inferred by the reviewer from dataset metadata, not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry annotates both EC 2.4.1.259 and EC 2.4.1.261, only 2.4.1.259 appears among the four choices. None of the distractors match any annotation for this protein. Thus, among the given options, only C is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VBV8 (ALG9_DROME, Drosophila melanogaster Alpha-1,2-mannosyltransferase Alg9) exactly (623 AA, SHA256 confirmed). The UniProt entry assigns EC 2.4.1.259 (and also EC 2.4.1.261) with evidence code ECO:0000250 (inferred by similarity from human Q9H6U8). Among the four choices, only 2.4.1.259 (option C) appears in the annotation. The other options (2.4.1.392, 4.2.1.70, 2.3.1.319) are unrelated EC numbers. The annotation is computational (transferred by similarity), not direct experimental evidence for the Drosophila protein, but it is the official database assignment.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could note the protein is a polytopic membrane protein with multiple hydrophobic segments consistent with an ER-resident enzyme, and might infer it belongs to the transferase class (EC 2) rather than lyase (EC 4), eliminating option B. However, distinguishing EC 2.4.1.259 (alpha-1,2-mannosyltransferase Alg9, GT47 family) from EC 2.4.1.392 (another glycosyltransferase) and EC 2.3.1.319 (acyltransferase) requires knowing the specific protein family, its role in the dolichol-linked N-glycan biosynthesis pathway (adding the 6th mannose to Man5GlcNAc2-PP-dolichol), and the exact EC assignment. No general sequence motif or biochemical reasoning from the raw 623-aa sequence alone reliably distinguishes these four specific EC numbers.",
    "missing_item_specific_fact": "The specific identity of this sequence as Alg9 (Drosophila ortholog of human DPAGT1-pathway mannosyltransferase) and the knowledge that Alg9 catalyzes the alpha-1,2-mannosyl transfer step designated EC 2.4.1.259 (as opposed to other glycosyltransferase EC numbers in the choices). This is a protein-specific database annotation.",
    "reason": "While the transferase vs. lyase distinction (eliminating B) is somewhat accessible, the precise 4-digit EC assignment among three transferase options (A, C, D) requires recognizing this as Alg9 and recalling its specific EC number. This is fundamentally a sequence-to-annotation lookup task, not a reasoning task from general biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry annotates both EC 2.4.1.259 and EC 2.4.1.261, only 2.4.1.259 appears among the four choices. None of the distractors match any annotation for this protein. Thus, among the given options, only C is defensible."
  },
  "important_caveats": [
    "The EC assignment carries evidence code ECO:0000250 (inferred by similarity from human Q9H6U8), not direct experimental characterization of the Drosophila protein.",
    "The protein is annotated with a second EC number (2.4.1.261) for a later step in the same pathway; the question asks for 'the' EC number (singular), which is slightly imprecise, but this does not affect answer selection since 2.4.1.261 is not a choice.",
    "The UniProt entry was first public in 2025-06-18 (Swiss-Prot reviewed status); the benchmark's author source snapshot is unknown but the sequence has been unchanged since 2000.",
    "The accession identity was inferred by the reviewer from dataset metadata, not provided to the evaluated model."
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

**Accession:** `Q9VBV8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 174. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
"Q9VBV8"
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9H6U8","source":"UniProtKB"}],"value":"2.4.1.259"},{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9H6U8","source":"UniProtKB"}],"value":"2.4.1.261"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0039293","source":"FlyBase"}],"value":"Alpha-1,2-mannosyltransferase Alg9"}}}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.4.1.259","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9H6U8","source":"UniProtKB"}],"name":"an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:29531"},{"database":"Rhea","id":"RHEA-COMP:19498"},{"database":"Rhea","id":"RHEA-COMP:19501"},{"database":"Rhea","id":"RHEA-COMP:19517"},{"database":"Rhea","id":"RHEA-COMP:19518"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57683"},{"database":"ChEBI","id":"CHEBI:58211"},{"database":"ChEBI","id":"CHEBI:132516"},{"database":"ChEBI","id":"CHEBI:132517"}]}}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
ID   ALG9_DROME              Reviewed;         623 AA.
AC   Q9VBV8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 174.
DE   RecName: Full=Alpha-1,2-mannosyltransferase Alg9 {ECO:0000312|FlyBase:FBgn0039293};
DE            EC=2.4.1.259 {ECO:0000250|UniProtKB:Q9H6U8};
DE            EC=2.4.1.261 {ECO:0000250|UniProtKB:Q9H6U8};
DE   AltName: Full=Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};
DE   AltName: Full=Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};
GN   Name=Alg9 {ECO:0000312|FlyBase:FBgn0039293};
GN   ORFNames=CG11851 {ECO:0000312|FlyBase:FBgn0039293};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
DE   RecName: Full=Alpha-1,2-mannosyltransferase Alg9 {ECO:0000312|FlyBase:FBgn0039293};
DE            EC=2.4.1.259 {ECO:0000250|UniProtKB:Q9H6U8};
DE            EC=2.4.1.261 {ECO:0000250|UniProtKB:Q9H6U8};
DE   AltName: Full=Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};
DE   AltName: Full=Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 104-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-
CC         [alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-
CC         GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a
CC         di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-
CC         Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-
CC         alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-
CC         GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a
CC         di-trans,poly-cis-dolichyl phosphate + H(+); Xref=Rhea:RHEA:29531,
CC         Rhea:RHEA-COMP:19498, Rhea:RHEA-COMP:19501, Rhea:RHEA-COMP:19517,
CC         Rhea:RHEA-COMP:19518, ChEBI:CHEBI:15378, ChEBI:CHEBI:57683,
CC         ChEBI:CHEBI:58211, ChEBI:CHEBI:132516, ChEBI:CHEBI:132517;
CC         EC=2.4.1.259; Evidence={ECO:0000250|UniProtKB:Q9H6U8};
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
