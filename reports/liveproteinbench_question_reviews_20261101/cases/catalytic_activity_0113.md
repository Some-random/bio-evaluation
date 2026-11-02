# catalytic_activity_0113

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — an N(6)-methyladenosine in mRNA + 2-oxoglutarate + O2 = an adenosine in mRNA + formaldehyde + succinate + CO2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHLHYDLPYPKHDMTDEPVSFFTYPPDSDTKFIPKDPCVHKPLSIKQVMERKLHWITLGGQYDWTNRVYPGERPPEFPRDVAGLLETLFPETLAQAAIVNFYTPGDTMMMHRDVSEETDKGLVSLSMGCDALFMIAPNDVGKMSEEDRPGHGEKEHLLLRIRSGDAIYMTQEARYAWHGVPKVLKGTCPDYLEDWPAEDGKYEEWQGWMKNKRINLNVRQMRDC

[Multiple Choices]
A. a quinone + NADH + H(+) = a quinol + NAD(+)
B. an N(6)-methyladenosine in mRNA + 2-oxoglutarate + O2 = an adenosine in mRNA + formaldehyde + succinate + CO2
C. D-alanyl-D-alanine + H2O = 2 D-alanine
D. 4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)
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

> The matched sequence is annotated as an N6-methyladenosine RNA demethylase, with the listed reaction attributed to experimental evidence (ECO:0000269). This supports B, though the cited primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an HxD motif and a downstream histidine, consistent with the metal-binding motif of Fe(II)/2-oxoglutarate-dependent dioxygenases. Of the choices, B is the reaction using 2-oxoglutarate and O2; the others describe a reductase or hydrolytic reactions. This supports the reaction class, not by itself the enzyme’s exact m6A substrate specificity.


**Missing item-specific fact**

> The exact preference for m6A in mRNA is not established by those motifs alone; it is supported here by the external, sequence-matched annotation and cited study.


**Reason**

> The sequence and reaction choices provide a concrete family-level distinction favoring B, although external evidence is needed to establish the precise substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, B is the one consistent with a 2-oxoglutarate-dependent dioxygenase.


### Important caveats

- The UniProt record and sequence match support the author key, but the annotation’s cited experimental study was not independently validated here.
- The family-level sequence argument does not alone prove m6A demethylation specifically.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an HxD motif and a downstream histidine, consistent with the metal-binding motif of Fe(II)/2-oxoglutarate-dependent dioxygenases. Of the choices, B is the reaction using 2-oxoglutarate and O2; the others describe a reductase or hydrolytic reactions. This supports the reaction class, not by itself the enzyme’s exact m6A substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact preference for m6A in mRNA is not established by those motifs alone; it is supported here by the external, sequence-matched annotation and cited study.",
    "reason": "The sequence and reaction choices provide a concrete family-level distinction favoring B, although external evidence is needed to establish the precise substrate specificity."
  },
  "case_id": "catalytic_activity_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as an N6-methyladenosine RNA demethylase, with the listed reaction attributed to experimental evidence (ECO:0000269). This supports B, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt record and sequence match support the author key, but the annotation’s cited experimental study was not independently validated here.",
    "The family-level sequence argument does not alone prove m6A demethylation specifically."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B is the one consistent with a 2-oxoglutarate-dependent dioxygenase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as an N6-methyladenosine RNA demethylase, with the listed reaction attributed to experimental evidence (ECO:0000269). This supports B, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an HxD motif and a downstream histidine, consistent with the metal-binding motif of Fe(II)/2-oxoglutarate-dependent dioxygenases. Of the choices, B is the reaction using 2-oxoglutarate and O2; the others describe a reductase or hydrolytic reactions. This supports the reaction class, not by itself the enzyme’s exact m6A substrate specificity.",
    "missing_item_specific_fact": "The exact preference for m6A in mRNA is not established by those motifs alone; it is supported here by the external, sequence-matched annotation and cited study.",
    "reason": "The sequence and reaction choices provide a concrete family-level distinction favoring B, although external evidence is needed to establish the precise substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B is the one consistent with a 2-oxoglutarate-dependent dioxygenase."
  },
  "important_caveats": [
    "The UniProt record and sequence match support the author key, but the annotation’s cited experimental study was not independently validated here.",
    "The family-level sequence argument does not alone prove m6A demethylation specifically."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A9P4XUZ4 (Cryphonectria parasitica ALKBH, 224 aa, SHA256 confirmed). The UniProt entry carries the recommended name 'N6-methyladenosine RNA demethylase ALKBH' with EC 1.14.11.53 and the exact catalytic reaction stated in choice B. The annotation is backed by experimental evidence (ECO:0000269, PubMed 39611846, MBio 2025), not merely computational transfer. Both the current (v14) and historical (v12) entries confirm the same reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the HxD/E…H…H triad characteristic of the Fe(II)/2-oxoglutarate-dependent dioxygenase superfamily (approx. H-I-T-L-G-G-Q-Y-D at ~res 52-60, then H-G-E-K-E-H and A-W-H-G toward the C-terminus). This triad is the hallmark of the ALKBH/AlkB family and related 2OG dioxygenases. Among the four choices, only B involves 2-oxoglutarate + O₂ as co-substrates, the defining chemistry of this enzyme class. The other options describe an NADH-dependent oxidoreductase (A), a peptidase (C), and a hydrolase (D)—none of which involve 2OG or O₂. A biologist recognizing the 2OG-dioxygenase signature can therefore eliminate A, C, and D on mechanistic grounds. The additional observation that the protein is short (~224 aa, consistent with a compact ALKBH core rather than a large JmjC-domain histone demethylase) and the ALKBH-family association with nucleic-acid demethylation further support the m6A-in-mRNA substrate in B.


**Missing item-specific fact**

> Precise discrimination between ALKBH-family members acting on DNA vs. RNA vs. other 2OG-dioxygenase substrates would require item-specific annotation or experimental data; however, the four choices are mechanistically distinct enough that class-level identification suffices.


**Reason**

> The HxD/E…H…H triad is a well-known, teachable signature of the 2OG dioxygenase superfamily. Matching it to the sole 2OG-dependent option among four mechanistically distinct enzyme classes constitutes a concrete, general biological argument rather than a pure lookup of this particular protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent clearly different enzyme classes (NADH oxidoreductase, 2OG dioxygenase, peptidase, hydrolase). Once the 2OG-dioxygenase triad is recognized, only B is mechanistically compatible. No other option involves 2-oxoglutarate or O₂.


### Important caveats

- The experimental evidence (PubMed 39611846, MBio 2025) establishing m6A demethylase activity was published after the sequence was deposited (2023); the annotation was added in 2025. A model trained on earlier data might not have this annotation.
- The HxD/E…H…H spacing in this particular sequence is somewhat degenerate compared to the canonical E. coli AlkB triad, so motif recognition requires familiarity with the broader ALKBH family rather than a textbook-perfect pattern.
- The reviewer-only UniProt accession was inferred from dataset metadata and was not available to the evaluated model; the model must rely solely on the raw 224-aa sequence and general knowledge.
- The specific m6A-in-mRNA substrate (as opposed to m6A in DNA, m1A, or other ALKBH targets) is not trivially deducible from sequence alone, but the four-choice format makes this distinction unnecessary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the HxD/E…H…H triad characteristic of the Fe(II)/2-oxoglutarate-dependent dioxygenase superfamily (approx. H-I-T-L-G-G-Q-Y-D at ~res 52-60, then H-G-E-K-E-H and A-W-H-G toward the C-terminus). This triad is the hallmark of the ALKBH/AlkB family and related 2OG dioxygenases. Among the four choices, only B involves 2-oxoglutarate + O₂ as co-substrates, the defining chemistry of this enzyme class. The other options describe an NADH-dependent oxidoreductase (A), a peptidase (C), and a hydrolase (D)—none of which involve 2OG or O₂. A biologist recognizing the 2OG-dioxygenase signature can therefore eliminate A, C, and D on mechanistic grounds. The additional observation that the protein is short (~224 aa, consistent with a compact ALKBH core rather than a large JmjC-domain histone demethylase) and the ALKBH-family association with nucleic-acid demethylation further support the m6A-in-mRNA substrate in B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise discrimination between ALKBH-family members acting on DNA vs. RNA vs. other 2OG-dioxygenase substrates would require item-specific annotation or experimental data; however, the four choices are mechanistically distinct enough that class-level identification suffices.",
    "reason": "The HxD/E…H…H triad is a well-known, teachable signature of the 2OG dioxygenase superfamily. Matching it to the sole 2OG-dependent option among four mechanistically distinct enzyme classes constitutes a concrete, general biological argument rather than a pure lookup of this particular protein's database entry."
  },
  "case_id": "catalytic_activity_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A9P4XUZ4 (Cryphonectria parasitica ALKBH, 224 aa, SHA256 confirmed). The UniProt entry carries the recommended name 'N6-methyladenosine RNA demethylase ALKBH' with EC 1.14.11.53 and the exact catalytic reaction stated in choice B. The annotation is backed by experimental evidence (ECO:0000269, PubMed 39611846, MBio 2025), not merely computational transfer. Both the current (v14) and historical (v12) entries confirm the same reaction."
  },
  "important_caveats": [
    "The experimental evidence (PubMed 39611846, MBio 2025) establishing m6A demethylase activity was published after the sequence was deposited (2023); the annotation was added in 2025. A model trained on earlier data might not have this annotation.",
    "The HxD/E…H…H spacing in this particular sequence is somewhat degenerate compared to the canonical E. coli AlkB triad, so motif recognition requires familiarity with the broader ALKBH family rather than a textbook-perfect pattern.",
    "The reviewer-only UniProt accession was inferred from dataset metadata and was not available to the evaluated model; the model must rely solely on the raw 224-aa sequence and general knowledge.",
    "The specific m6A-in-mRNA substrate (as opposed to m6A in DNA, m1A, or other ALKBH targets) is not trivially deducible from sequence alone, but the four-choice format makes this distinction unnecessary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly different enzyme classes (NADH oxidoreductase, 2OG dioxygenase, peptidase, hydrolase). Once the 2OG-dioxygenase triad is recognized, only B is mechanistically compatible. No other option involves 2-oxoglutarate or O₂."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A9P4XUZ4 (Cryphonectria parasitica ALKBH, 224 aa, SHA256 confirmed). The UniProt entry carries the recommended name 'N6-methyladenosine RNA demethylase ALKBH' with EC 1.14.11.53 and the exact catalytic reaction stated in choice B. The annotation is backed by experimental evidence (ECO:0000269, PubMed 39611846, MBio 2025), not merely computational transfer. Both the current (v14) and historical (v12) entries confirm the same reaction.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the HxD/E…H…H triad characteristic of the Fe(II)/2-oxoglutarate-dependent dioxygenase superfamily (approx. H-I-T-L-G-G-Q-Y-D at ~res 52-60, then H-G-E-K-E-H and A-W-H-G toward the C-terminus). This triad is the hallmark of the ALKBH/AlkB family and related 2OG dioxygenases. Among the four choices, only B involves 2-oxoglutarate + O₂ as co-substrates, the defining chemistry of this enzyme class. The other options describe an NADH-dependent oxidoreductase (A), a peptidase (C), and a hydrolase (D)—none of which involve 2OG or O₂. A biologist recognizing the 2OG-dioxygenase signature can therefore eliminate A, C, and D on mechanistic grounds. The additional observation that the protein is short (~224 aa, consistent with a compact ALKBH core rather than a large JmjC-domain histone demethylase) and the ALKBH-family association with nucleic-acid demethylation further support the m6A-in-mRNA substrate in B.",
    "missing_item_specific_fact": "Precise discrimination between ALKBH-family members acting on DNA vs. RNA vs. other 2OG-dioxygenase substrates would require item-specific annotation or experimental data; however, the four choices are mechanistically distinct enough that class-level identification suffices.",
    "reason": "The HxD/E…H…H triad is a well-known, teachable signature of the 2OG dioxygenase superfamily. Matching it to the sole 2OG-dependent option among four mechanistically distinct enzyme classes constitutes a concrete, general biological argument rather than a pure lookup of this particular protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly different enzyme classes (NADH oxidoreductase, 2OG dioxygenase, peptidase, hydrolase). Once the 2OG-dioxygenase triad is recognized, only B is mechanistically compatible. No other option involves 2-oxoglutarate or O₂."
  },
  "important_caveats": [
    "The experimental evidence (PubMed 39611846, MBio 2025) establishing m6A demethylase activity was published after the sequence was deposited (2023); the annotation was added in 2025. A model trained on earlier data might not have this annotation.",
    "The HxD/E…H…H spacing in this particular sequence is somewhat degenerate compared to the canonical E. coli AlkB triad, so motif recognition requires familiarity with the broader ALKBH family rather than a textbook-perfect pattern.",
    "The reviewer-only UniProt accession was inferred from dataset metadata and was not available to the evaluated model; the model must rely solely on the raw 224-aa sequence and general knowledge.",
    "The specific m6A-in-mRNA substrate (as opposed to m6A in DNA, m1A, or other ALKBH targets) is not trivially deducible from sequence alone, but the four-choice format makes this distinction unnecessary."
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

**Accession:** `A0A9P4XUZ4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XUZ4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:15.906572+00:00.  

```json
"A0A9P4XUZ4"
```

Source SHA-256: `b3840b9b219920ebd5a30838fec1826145f43e3ca1900e4a6d56abfcb06d5673`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XUZ4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:15.906572+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39611846","source":"PubMed"}],"value":"M6A eraser ALKBH"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Nucleic acid dioxygenase ALKBH"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"value":"1.14.11.53"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39611846","source":"PubMed"}],"value":"N6-methyladenosine RNA demethylase ALKBH"}}}
```

Source SHA-256: `b3840b9b219920ebd5a30838fec1826145f43e3ca1900e4a6d56abfcb06d5673`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XUZ4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:15.906572+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:49521"}}],"reaction":{"ecNumber":"1.14.11.53","evidences":[{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"name":"an N(6)-methyladenosine in mRNA + 2-oxoglutarate + O2 = an adenosine in mRNA + formaldehyde + succinate + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:49520"},{"database":"Rhea","id":"RHEA-COMP:12414"},{"database":"Rhea","id":"RHEA-COMP:12417"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:16810"},{"database":"ChEBI","id":"CHEBI:16842"},{"database":"ChEBI","id":"CHEBI:30031"},{"database":"ChEBI","id":"CHEBI:74411"},{"database":"ChEBI","id":"CHEBI:74449"}]}}
```

Source SHA-256: `b3840b9b219920ebd5a30838fec1826145f43e3ca1900e4a6d56abfcb06d5673`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XUZ4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:15.906572+00:00.  

```json
{"citation":{"authors":["Zhao L.","Wei X.","Chen F.","Chen B.","Li R."],"citationCrossReferences":[{"database":"PubMed","id":"39611846"},{"database":"DOI","id":"10.1128/mbio.01844-24"}],"citationType":"journal article","firstPage":"e0184424","id":"39611846","journal":"MBio","lastPage":"e0184424","publicationDate":"2025","title":"m6A demethylase CpALKBH regulates CpZap1 mRNA stability to modulate the development and virulence of chestnut blight fungus.","volume":"16"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `b3840b9b219920ebd5a30838fec1826145f43e3ca1900e4a6d56abfcb06d5673`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XUZ4?format=txt&versions=12)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:18.356161+00:00.  

```text
ID   ALKBH_CRYP1             Reviewed;         224 AA.
AC   A0A9P4XUZ4;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-SEP-2023, sequence version 1.
DT   28-JAN-2026, entry version 12.
DE   RecName: Full=N6-methyladenosine RNA demethylase ALKBH {ECO:0000303|PubMed:39611846};
DE            EC=1.14.11.53 {ECO:0000269|PubMed:39611846};
DE   AltName: Full=M6A eraser ALKBH {ECO:0000303|PubMed:39611846};
DE   AltName: Full=Nucleic acid dioxygenase ALKBH {ECO:0000305};
GN   Name=ALKBH {ECO:0000303|PubMed:39611846}; ORFNames=M406DRAFT_358091;
OS   Cryphonectria parasitica (strain ATCC 38755 / EP155).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Diaporthales; Cryphonectriaceae;
OC   Cryphonectria-Endothia species complex; Cryphonectria.
OX   NCBI_TaxID=660469;
```

Source SHA-256: `68a824b89237d7c3caedd6985cd8467f9aab542d3e48e598d57dea889bd51057`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XUZ4?format=txt&versions=12)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:18.356161+00:00.  

```text
DE   RecName: Full=N6-methyladenosine RNA demethylase ALKBH {ECO:0000303|PubMed:39611846};
DE            EC=1.14.11.53 {ECO:0000269|PubMed:39611846};
DE   AltName: Full=M6A eraser ALKBH {ECO:0000303|PubMed:39611846};
DE   AltName: Full=Nucleic acid dioxygenase ALKBH {ECO:0000305};
```

Source SHA-256: `68a824b89237d7c3caedd6985cd8467f9aab542d3e48e598d57dea889bd51057`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XUZ4?format=txt&versions=12)  
**Locator:** `lines 27-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:18.356161+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.
RX   PubMed=39611846; DOI=10.1128/mbio.01844-24;
RA   Zhao L., Wei X., Chen F., Chen B., Li R.;
RT   "m6A demethylase CpALKBH regulates CpZap1 mRNA stability to modulate the
RT   development and virulence of chestnut blight fungus.";
RL   MBio 16:e0184424-e0184424(2025).
```

Source SHA-256: `68a824b89237d7c3caedd6985cd8467f9aab542d3e48e598d57dea889bd51057`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XUZ4?format=txt&versions=12)  
**Locator:** `lines 45-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:18.356161+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an N(6)-methyladenosine in mRNA + 2-oxoglutarate + O2 = an
CC         adenosine in mRNA + formaldehyde + succinate + CO2;
CC         Xref=Rhea:RHEA:49520, Rhea:RHEA-COMP:12414, Rhea:RHEA-COMP:12417,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:16526, ChEBI:CHEBI:16810,
CC         ChEBI:CHEBI:16842, ChEBI:CHEBI:30031, ChEBI:CHEBI:74411,
CC         ChEBI:CHEBI:74449; EC=1.14.11.53;
CC         Evidence={ECO:0000269|PubMed:39611846};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49521;
CC         Evidence={ECO:0000269|PubMed:39611846};
```

Source SHA-256: `68a824b89237d7c3caedd6985cd8467f9aab542d3e48e598d57dea889bd51057`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 113. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
