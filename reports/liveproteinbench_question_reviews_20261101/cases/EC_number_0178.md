# EC_number_0178

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.1.3.16

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGQTLSEPVVEKTSEKGEDDRLIYGVSAMQGWRISMEDAHTAELNLPPPDNDTKTHPDRLSFFGVFDGHGGDKVALFAGENIHNIVFKQESFKSGDYAQGLKDGFLATDRAILNDPKYEEEVSGCTACVTLIAGNKLYVANAGDSRSVLGIKGRAKPLSNDHKPQLETEKNRITAAGGFVDFGRVNGNLALSRAIGDFEFKKSAELSPENQIVTAFPDVEVHELTEEDEFLVIACDGIWDCQSSQAVVEFVRRGIAAKQDLDKICENMMDNCLASNSETGGVGCDNMTMVIIGFLHGKTKEEWYDEIAKRVANGDGPCAPPEYAEFRGPGVHHNYEDSDSGYDVDADSGGKFSLAGSRGRIIFLGDGTEVLTGSDDTEMFDNADEDKDLASQVPKSSGKTDAKEETEAKPAPEAESSKPADGSEKKQDEKTPEESKKD

[Multiple Choices]
A. 3.1.3.16
B. 3.1.3.2
C. 5.1.1.24
D. 3.2.1.20
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

> The sequence-matched UniProt entry assigns EC 3.1.3.16 to this protein and describes it as a PP2C homolog. The assignment is annotation-based: the catalytic activity is associated with a PROSITE ProRule, and the threonine reaction is transferred by similarity from another UniProt protein; these excerpts do not establish direct experimental measurement of this protein's activity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has motifs characteristic of metal-dependent PP2C phosphatases, including the DGHGG region, supporting a protein phosphatase 2C assignment (EC 3.1.3.16). That distinguishes A from the acid phosphatase, racemase, and beta-galactosidase alternatives.


**Missing item-specific fact**

> No additional protein-specific fact is needed to distinguish these listed choices from the sequence-family evidence; the exact substrate activity is not independently demonstrated by the supplied input.


**Reason**

> The choices represent distinct enzyme families, and the sequence provides meaningful PP2C-family evidence. This is more than recognizing the exact protein or relying on an absent database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, the PP2C-family sequence signature supports A; the other choices describe unrelated enzyme activities.


### Important caveats

- Reviewer-only annotation evidence matches the supplied sequence but was not available to the evaluated model.
- The cited EC assignment is computationally inferred or transferred by similarity in the supplied evidence, not shown here to be experimentally validated for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has motifs characteristic of metal-dependent PP2C phosphatases, including the DGHGG region, supporting a protein phosphatase 2C assignment (EC 3.1.3.16). That distinguishes A from the acid phosphatase, racemase, and beta-galactosidase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No additional protein-specific fact is needed to distinguish these listed choices from the sequence-family evidence; the exact substrate activity is not independently demonstrated by the supplied input.",
    "reason": "The choices represent distinct enzyme families, and the sequence provides meaningful PP2C-family evidence. This is more than recognizing the exact protein or relying on an absent database lookup."
  },
  "case_id": "EC_number_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.1.3.16 to this protein and describes it as a PP2C homolog. The assignment is annotation-based: the catalytic activity is associated with a PROSITE ProRule, and the threonine reaction is transferred by similarity from another UniProt protein; these excerpts do not establish direct experimental measurement of this protein's activity."
  },
  "important_caveats": [
    "Reviewer-only annotation evidence matches the supplied sequence but was not available to the evaluated model.",
    "The cited EC assignment is computationally inferred or transferred by similarity in the supplied evidence, not shown here to be experimentally validated for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the PP2C-family sequence signature supports A; the other choices describe unrelated enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.1.3.16 to this protein and describes it as a PP2C homolog. The assignment is annotation-based: the catalytic activity is associated with a PROSITE ProRule, and the threonine reaction is transferred by similarity from another UniProt protein; these excerpts do not establish direct experimental measurement of this protein's activity.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has motifs characteristic of metal-dependent PP2C phosphatases, including the DGHGG region, supporting a protein phosphatase 2C assignment (EC 3.1.3.16). That distinguishes A from the acid phosphatase, racemase, and beta-galactosidase alternatives.",
    "missing_item_specific_fact": "No additional protein-specific fact is needed to distinguish these listed choices from the sequence-family evidence; the exact substrate activity is not independently demonstrated by the supplied input.",
    "reason": "The choices represent distinct enzyme families, and the sequence provides meaningful PP2C-family evidence. This is more than recognizing the exact protein or relying on an absent database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the PP2C-family sequence signature supports A; the other choices describe unrelated enzyme activities."
  },
  "important_caveats": [
    "Reviewer-only annotation evidence matches the supplied sequence but was not available to the evaluated model.",
    "The cited EC assignment is computationally inferred or transferred by similarity in the supplied evidence, not shown here to be experimentally validated for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G0RT93 (PP2C2_HYPJQ) is annotated with EC 3.1.3.16 as 'Protein phosphatase 2C homolog 2.' The annotation is consistent across current (C4, C5, C6) and archived (H1-H5) records. However, the evidence codes are ECO:0000250 (similarity to P39966, yeast PP2C) and ECO:0000255 (PROSITE-ProRule PRU01082), indicating computational inference by homology/pattern rather than direct experimental characterization of this specific T. reesei protein. The entry was integrated into Swiss-Prot in Feb 2025. The annotation is database-supported but not independently experimentally verified for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable PP2C-family catalytic motifs: conserved 'GDG' and 'Dx' patterns (e.g., 'IIFLGDGTEVLTGSDD', 'VFDGHGGDK'), a metal-binding architecture typical of PPP-family metallophosphoesterases, and a ~438-aa length consistent with PP2C domains. PP2C enzymes are Ser/Thr-specific protein phosphatases classified as EC 3.1.3.16. Acid phosphatases (EC 3.1.3.2) use a distinct nucleophilic mechanism (His/Cys nucleophile) and lack the PP2C DxSxG/GDG metal-coordination signature. The other two options (5.1.1.24 isomerase; 3.2.1.20 glycosidase) are excluded by mechanism class. A knowledgeable reader can use PP2C motif recognition to eliminate B and assign the correct EC class.


**Missing item-specific fact**

> None strictly required; PP2C family identification from sequence motifs is general biochemical knowledge. However, precise EC-number assignment (3.1.3.16 vs. other phosphatase sub-numbers) relies on knowing the IUBMB classification convention that maps PP2C to 3.1.3.16.


**Reason**

> Distractors C and D are excluded by enzyme class (isomerase vs. hydrolase; glycosidase vs. phosphatase). Distinguishing A from B requires recognizing PP2C-specific sequence motifs (GDG, DxSxG, metal-binding Asp clusters) and knowing that PP2C-type Ser/Thr phosphatases are classified as EC 3.1.3.16 rather than the acid-phosphatase class 3.1.3.2. This is achievable through general enzymology knowledge and sequence pattern recognition without needing to look up this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (5.1.1.24, amino-acid racemase) and D (3.2.1.20, alpha-glucosidase) are clearly incompatible with a phosphatase sequence. Option B (3.1.3.2, acid phosphatase) is the only plausible competitor, but the PP2C motif signature in the sequence distinguishes it. No genuine ambiguity among the four choices.


### Important caveats

- The EC annotation for G0RT93 rests on similarity to yeast P39966 (ECO:0000250) and PROSITE-ProRule pattern matching (ECO:0000255), not on direct enzymatic assay of this T. reesei protein. The 'homolog' designation in the name reflects this.
- The UniProt entry was only integrated into Swiss-Prot in February 2025; the author's source snapshot date is unknown and may predate Swiss-Prot integration.
- The 2004 reference (PubMed:15480788) describes ptc2 in the context of the unfolded protein response pathway and reports 'FUNCTION' but the excerpt does not specify whether phosphatase activity was directly measured for this protein or inferred from homology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable PP2C-family catalytic motifs: conserved 'GDG' and 'Dx' patterns (e.g., 'IIFLGDGTEVLTGSDD', 'VFDGHGGDK'), a metal-binding architecture typical of PPP-family metallophosphoesterases, and a ~438-aa length consistent with PP2C domains. PP2C enzymes are Ser/Thr-specific protein phosphatases classified as EC 3.1.3.16. Acid phosphatases (EC 3.1.3.2) use a distinct nucleophilic mechanism (His/Cys nucleophile) and lack the PP2C DxSxG/GDG metal-coordination signature. The other two options (5.1.1.24 isomerase; 3.2.1.20 glycosidase) are excluded by mechanism class. A knowledgeable reader can use PP2C motif recognition to eliminate B and assign the correct EC class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; PP2C family identification from sequence motifs is general biochemical knowledge. However, precise EC-number assignment (3.1.3.16 vs. other phosphatase sub-numbers) relies on knowing the IUBMB classification convention that maps PP2C to 3.1.3.16.",
    "reason": "Distractors C and D are excluded by enzyme class (isomerase vs. hydrolase; glycosidase vs. phosphatase). Distinguishing A from B requires recognizing PP2C-specific sequence motifs (GDG, DxSxG, metal-binding Asp clusters) and knowing that PP2C-type Ser/Thr phosphatases are classified as EC 3.1.3.16 rather than the acid-phosphatase class 3.1.3.2. This is achievable through general enzymology knowledge and sequence pattern recognition without needing to look up this specific protein's database entry."
  },
  "case_id": "EC_number_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G0RT93 (PP2C2_HYPJQ) is annotated with EC 3.1.3.16 as 'Protein phosphatase 2C homolog 2.' The annotation is consistent across current (C4, C5, C6) and archived (H1-H5) records. However, the evidence codes are ECO:0000250 (similarity to P39966, yeast PP2C) and ECO:0000255 (PROSITE-ProRule PRU01082), indicating computational inference by homology/pattern rather than direct experimental characterization of this specific T. reesei protein. The entry was integrated into Swiss-Prot in Feb 2025. The annotation is database-supported but not independently experimentally verified for this exact protein."
  },
  "important_caveats": [
    "The EC annotation for G0RT93 rests on similarity to yeast P39966 (ECO:0000250) and PROSITE-ProRule pattern matching (ECO:0000255), not on direct enzymatic assay of this T. reesei protein. The 'homolog' designation in the name reflects this.",
    "The UniProt entry was only integrated into Swiss-Prot in February 2025; the author's source snapshot date is unknown and may predate Swiss-Prot integration.",
    "The 2004 reference (PubMed:15480788) describes ptc2 in the context of the unfolded protein response pathway and reports 'FUNCTION' but the excerpt does not specify whether phosphatase activity was directly measured for this protein or inferred from homology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (5.1.1.24, amino-acid racemase) and D (3.2.1.20, alpha-glucosidase) are clearly incompatible with a phosphatase sequence. Option B (3.1.3.2, acid phosphatase) is the only plausible competitor, but the PP2C motif signature in the sequence distinguishes it. No genuine ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G0RT93 (PP2C2_HYPJQ) is annotated with EC 3.1.3.16 as 'Protein phosphatase 2C homolog 2.' The annotation is consistent across current (C4, C5, C6) and archived (H1-H5) records. However, the evidence codes are ECO:0000250 (similarity to P39966, yeast PP2C) and ECO:0000255 (PROSITE-ProRule PRU01082), indicating computational inference by homology/pattern rather than direct experimental characterization of this specific T. reesei protein. The entry was integrated into Swiss-Prot in Feb 2025. The annotation is database-supported but not independently experimentally verified for this exact protein.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable PP2C-family catalytic motifs: conserved 'GDG' and 'Dx' patterns (e.g., 'IIFLGDGTEVLTGSDD', 'VFDGHGGDK'), a metal-binding architecture typical of PPP-family metallophosphoesterases, and a ~438-aa length consistent with PP2C domains. PP2C enzymes are Ser/Thr-specific protein phosphatases classified as EC 3.1.3.16. Acid phosphatases (EC 3.1.3.2) use a distinct nucleophilic mechanism (His/Cys nucleophile) and lack the PP2C DxSxG/GDG metal-coordination signature. The other two options (5.1.1.24 isomerase; 3.2.1.20 glycosidase) are excluded by mechanism class. A knowledgeable reader can use PP2C motif recognition to eliminate B and assign the correct EC class.",
    "missing_item_specific_fact": "None strictly required; PP2C family identification from sequence motifs is general biochemical knowledge. However, precise EC-number assignment (3.1.3.16 vs. other phosphatase sub-numbers) relies on knowing the IUBMB classification convention that maps PP2C to 3.1.3.16.",
    "reason": "Distractors C and D are excluded by enzyme class (isomerase vs. hydrolase; glycosidase vs. phosphatase). Distinguishing A from B requires recognizing PP2C-specific sequence motifs (GDG, DxSxG, metal-binding Asp clusters) and knowing that PP2C-type Ser/Thr phosphatases are classified as EC 3.1.3.16 rather than the acid-phosphatase class 3.1.3.2. This is achievable through general enzymology knowledge and sequence pattern recognition without needing to look up this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (5.1.1.24, amino-acid racemase) and D (3.2.1.20, alpha-glucosidase) are clearly incompatible with a phosphatase sequence. Option B (3.1.3.2, acid phosphatase) is the only plausible competitor, but the PP2C motif signature in the sequence distinguishes it. No genuine ambiguity among the four choices."
  },
  "important_caveats": [
    "The EC annotation for G0RT93 rests on similarity to yeast P39966 (ECO:0000250) and PROSITE-ProRule pattern matching (ECO:0000255), not on direct enzymatic assay of this T. reesei protein. The 'homolog' designation in the name reflects this.",
    "The UniProt entry was only integrated into Swiss-Prot in February 2025; the author's source snapshot date is unknown and may predate Swiss-Prot integration.",
    "The 2004 reference (PubMed:15480788) describes ptc2 in the context of the unfolded protein response pathway and reports 'FUNCTION' but the excerpt does not specify whether phosphatase activity was directly measured for this protein or inferred from homology."
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

**Accession:** `G0RT93` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 60. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.800559+00:00.  

```json
"G0RT93"
```

Source SHA-256: `b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.800559+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Protein phosphatase 2C homolog 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PP2C-2"}]}}
```

Source SHA-256: `b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.800559+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01082","source":"PROSITE-ProRule"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.800559+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:47005"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"name":"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:47004"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:61977"}]}}
```

Source SHA-256: `b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-02T04:28:22.841847+00:00.  

```text
ID   PP2C2_HYPJQ             Reviewed;         438 AA.
AC   G0RT93; Q7Z8F2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-OCT-2011, sequence version 1.
DT   28-JAN-2026, entry version 60.
DE   RecName: Full=Protein phosphatase 2C homolog 2 {ECO:0000305};
DE            Short=PP2C-2 {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000250|UniProtKB:P39966};
GN   Name=PTC2 {ECO:0000303|PubMed:15480788};
GN   ORFNames=TRIREDRAFT_81164 {ECO:0000312|EMBL:EGR45524.1};
OS   Hypocrea jecorina (strain QM6a) (Trichoderma reesei).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Trichoderma.
OX   NCBI_TaxID=431241 {ECO:0000312|Proteomes:UP000008984};
```

Source SHA-256: `83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-02T04:28:22.841847+00:00.  

```text
DE   RecName: Full=Protein phosphatase 2C homolog 2 {ECO:0000305};
DE            Short=PP2C-2 {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000250|UniProtKB:P39966};
```

Source SHA-256: `83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-02T04:28:22.841847+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16; Evidence={ECO:0000255|PROSITE-
CC         ProRule:PRU01082};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000305};
```

Source SHA-256: `83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)  
**Locator:** `lines 50-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-02T04:28:22.841847+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:61977; EC=3.1.3.16;
CC         Evidence={ECO:0000250|UniProtKB:P39966};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;
CC         Evidence={ECO:0000250|UniProtKB:P39966};
```

Source SHA-256: `83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 178. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
