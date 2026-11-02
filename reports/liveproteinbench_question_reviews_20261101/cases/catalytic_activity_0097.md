# catalytic_activity_0097

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKEIKIQNIIINEEKAPLVVPEIGINHNGSLELAKIMVDAAFSAGAKIIKHQTHIVEDEMSKAAKKVIPGNAKISIYEIMQKCALDYKDELALKEYTEKLGLVYLSTPFSRAGANRLEDMGVSAFKIGSGECNNYPLIKHIAAFKKPMIVSTGMNSIESIKPTVKILLDNEIPFVLMHTTNLYPTPHNLVRLNAMLELKKEFSCMVGLSDHTTDNLACLGAVALGACVLERHFTDSMDRSGPDIVCSMDTKALKELIMQSEQMAIMRGNNESKKAAKQEQVTIDFAFASVVSIKDIKKGEVLSMDNIWVKRPGLGGISAAEFENILGKKALRDIENDTQLSYEDFA

[Multiple Choices]
A. L-dopa + H(+) = dopamine + CO2
B. isopentadecanoyl-CoA + L-cysteate + H(+) = 3-oxocapnine + CO2 + CoA
C. (19E)-geissoschizine + NADPH + H(+) = (16R,19E)-isositsirikine + NADP(+)
D. N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate
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

> The supplied reviewer evidence identifies this exact sequence as a bacterial N-acetylneuraminate synthase and annotates the reaction in choice D. The annotation cites experimental evidence (ECO:0000269); the cited paper was not independently assessed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices alone provide no concrete, distinctive clue that identifies this enzyme's specific substrates and products. Recognizing the exact sequence or recalling its annotation would not constitute reasoning from the supplied input.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental identification of this sequence as N-acetylneuraminate synthase.


**Reason**

> Distinguishing D requires a protein-specific enzyme-function fact not given in the question. General sequence heuristics do not establish this precise reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation specifies choice D; no evidence supports another listed reaction for this protein.


### Important caveats

- Reviewer-only evidence was not available to the evaluated model.
- The historical UniProt record matches the sequence and cites experimental evidence, but the author's exact source snapshot is unknown and the primary paper was not independently validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices alone provide no concrete, distinctive clue that identifies this enzyme's specific substrates and products. Recognizing the exact sequence or recalling its annotation would not constitute reasoning from the supplied input.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of this sequence as N-acetylneuraminate synthase.",
    "reason": "Distinguishing D requires a protein-specific enzyme-function fact not given in the question. General sequence heuristics do not establish this precise reaction."
  },
  "case_id": "catalytic_activity_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied reviewer evidence identifies this exact sequence as a bacterial N-acetylneuraminate synthase and annotates the reaction in choice D. The annotation cites experimental evidence (ECO:0000269); the cited paper was not independently assessed here."
  },
  "important_caveats": [
    "Reviewer-only evidence was not available to the evaluated model.",
    "The historical UniProt record matches the sequence and cites experimental evidence, but the author's exact source snapshot is unknown and the primary paper was not independently validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation specifies choice D; no evidence supports another listed reaction for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied reviewer evidence identifies this exact sequence as a bacterial N-acetylneuraminate synthase and annotates the reaction in choice D. The annotation cites experimental evidence (ECO:0000269); the cited paper was not independently assessed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices alone provide no concrete, distinctive clue that identifies this enzyme's specific substrates and products. Recognizing the exact sequence or recalling its annotation would not constitute reasoning from the supplied input.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of this sequence as N-acetylneuraminate synthase.",
    "reason": "Distinguishing D requires a protein-specific enzyme-function fact not given in the question. General sequence heuristics do not establish this precise reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation specifies choice D; no evidence supports another listed reaction for this protein."
  },
  "important_caveats": [
    "Reviewer-only evidence was not available to the evaluated model.",
    "The historical UniProt record matches the sequence and cites experimental evidence, but the author's exact source snapshot is unknown and the primary paper was not independently validated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 346-aa sequence matches UniProt P0DY06 (NEUAS_CAMJ8) exactly (SHA256 confirmed). The entry is annotated as N-acetylneuraminate synthase (EC 2.5.1.56) with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic activity comment states verbatim: 'N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate,' which is identical to option D.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains motifs loosely consistent with the sialic acid synthase (Neu5Ac synthase) TIM-barrel family (e.g., the 'GSGECNNY' region), and knowledge that sialic acid biosynthesis proceeds via ManNAc + PEP condensation is general biochemistry. However, no single unambiguous catalytic motif in the sequence uniquely identifies this enzyme as Neu5Ac synthase rather than another transferase or synthase without recognizing the specific family assignment.


**Missing item-specific fact**

> Recognition that this particular 346-aa sequence belongs to the Neu5Ac synthase family (EC 2.5.1.56) rather than another enzyme class. The sequence does not contain a universally recognizable catalytic signature (like the KXXK motif of PLP enzymes) that would allow pure first-principles reasoning to the exact reaction. The identification relies on matching the sequence to a known enzyme family annotation.


**Reason**

> While general knowledge of sialic acid biosynthesis (ManNAc + PEP → Neu5Ac + Pi) is well-established biochemistry, the primary step is identifying the enzyme family from the raw sequence. This identification is essentially a database-annotation lookup (matching to the sialic acid synthase family) rather than a deduction from obvious catalytic motifs. The distractors (PLP decarboxylase, terpene reductase, exotic CoA reaction) are eliminable by general reasoning, but confirming D as the correct answer requires knowing this sequence is specifically a Neu5Ac synthase.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the enzyme is identified as a sialic acid synthase family member, option D is the only biochemically sensible reaction. Options A (PLP-dependent aromatic decarboxylase), B (exotic CoA/cysteate condensation), and C (terpene indole alkaloid NADPH-dependent reductase) correspond to entirely different enzyme classes and cofactor requirements inconsistent with the sequence's fold and motifs. The distractors are sufficiently distinct that no genuine ambiguity remains among the four choices.


### Important caveats

- The UniProt entry P0DY06 was first released in June 2025 with annotation updated through 2026; the author's data-construction date is unknown, so the annotation may not have existed at benchmark creation time.
- The experimental evidence (PubMed:38382015, Ghosh & Raushel 2024) confirms the catalytic activity in vitro for the Campylobacter jejuni enzyme, but the reaction is also the canonical step in sialic acid biosynthesis known from eukaryotic systems.
- The reviewer-only accession was inferred from dataset metadata, not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs loosely consistent with the sialic acid synthase (Neu5Ac synthase) TIM-barrel family (e.g., the 'GSGECNNY' region), and knowledge that sialic acid biosynthesis proceeds via ManNAc + PEP condensation is general biochemistry. However, no single unambiguous catalytic motif in the sequence uniquely identifies this enzyme as Neu5Ac synthase rather than another transferase or synthase without recognizing the specific family assignment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this particular 346-aa sequence belongs to the Neu5Ac synthase family (EC 2.5.1.56) rather than another enzyme class. The sequence does not contain a universally recognizable catalytic signature (like the KXXK motif of PLP enzymes) that would allow pure first-principles reasoning to the exact reaction. The identification relies on matching the sequence to a known enzyme family annotation.",
    "reason": "While general knowledge of sialic acid biosynthesis (ManNAc + PEP → Neu5Ac + Pi) is well-established biochemistry, the primary step is identifying the enzyme family from the raw sequence. This identification is essentially a database-annotation lookup (matching to the sialic acid synthase family) rather than a deduction from obvious catalytic motifs. The distractors (PLP decarboxylase, terpene reductase, exotic CoA reaction) are eliminable by general reasoning, but confirming D as the correct answer requires knowing this sequence is specifically a Neu5Ac synthase."
  },
  "case_id": "catalytic_activity_0097",
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
    "reason": "The supplied 346-aa sequence matches UniProt P0DY06 (NEUAS_CAMJ8) exactly (SHA256 confirmed). The entry is annotated as N-acetylneuraminate synthase (EC 2.5.1.56) with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic activity comment states verbatim: 'N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate,' which is identical to option D."
  },
  "important_caveats": [
    "The UniProt entry P0DY06 was first released in June 2025 with annotation updated through 2026; the author's data-construction date is unknown, so the annotation may not have existed at benchmark creation time.",
    "The experimental evidence (PubMed:38382015, Ghosh & Raushel 2024) confirms the catalytic activity in vitro for the Campylobacter jejuni enzyme, but the reaction is also the canonical step in sialic acid biosynthesis known from eukaryotic systems.",
    "The reviewer-only accession was inferred from dataset metadata, not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the enzyme is identified as a sialic acid synthase family member, option D is the only biochemically sensible reaction. Options A (PLP-dependent aromatic decarboxylase), B (exotic CoA/cysteate condensation), and C (terpene indole alkaloid NADPH-dependent reductase) correspond to entirely different enzyme classes and cofactor requirements inconsistent with the sequence's fold and motifs. The distractors are sufficiently distinct that no genuine ambiguity remains among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 346-aa sequence matches UniProt P0DY06 (NEUAS_CAMJ8) exactly (SHA256 confirmed). The entry is annotated as N-acetylneuraminate synthase (EC 2.5.1.56) with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic activity comment states verbatim: 'N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate,' which is identical to option D.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains motifs loosely consistent with the sialic acid synthase (Neu5Ac synthase) TIM-barrel family (e.g., the 'GSGECNNY' region), and knowledge that sialic acid biosynthesis proceeds via ManNAc + PEP condensation is general biochemistry. However, no single unambiguous catalytic motif in the sequence uniquely identifies this enzyme as Neu5Ac synthase rather than another transferase or synthase without recognizing the specific family assignment.",
    "missing_item_specific_fact": "Recognition that this particular 346-aa sequence belongs to the Neu5Ac synthase family (EC 2.5.1.56) rather than another enzyme class. The sequence does not contain a universally recognizable catalytic signature (like the KXXK motif of PLP enzymes) that would allow pure first-principles reasoning to the exact reaction. The identification relies on matching the sequence to a known enzyme family annotation.",
    "reason": "While general knowledge of sialic acid biosynthesis (ManNAc + PEP → Neu5Ac + Pi) is well-established biochemistry, the primary step is identifying the enzyme family from the raw sequence. This identification is essentially a database-annotation lookup (matching to the sialic acid synthase family) rather than a deduction from obvious catalytic motifs. The distractors (PLP decarboxylase, terpene reductase, exotic CoA reaction) are eliminable by general reasoning, but confirming D as the correct answer requires knowing this sequence is specifically a Neu5Ac synthase."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the enzyme is identified as a sialic acid synthase family member, option D is the only biochemically sensible reaction. Options A (PLP-dependent aromatic decarboxylase), B (exotic CoA/cysteate condensation), and C (terpene indole alkaloid NADPH-dependent reductase) correspond to entirely different enzyme classes and cofactor requirements inconsistent with the sequence's fold and motifs. The distractors are sufficiently distinct that no genuine ambiguity remains among the four choices."
  },
  "important_caveats": [
    "The UniProt entry P0DY06 was first released in June 2025 with annotation updated through 2026; the author's data-construction date is unknown, so the annotation may not have existed at benchmark creation time.",
    "The experimental evidence (PubMed:38382015, Ghosh & Raushel 2024) confirms the catalytic activity in vitro for the Campylobacter jejuni enzyme, but the reaction is also the canonical step in sialic acid biosynthesis known from eukaryotic systems.",
    "The reviewer-only accession was inferred from dataset metadata, not provided to the evaluated model."
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

**Accession:** `P0DY06` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
"P0DY06"
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"2.5.1.56"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"N-acetylneuraminate synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"Neu5Ac synthase"}]}}
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:19274"}}],"reaction":{"ecNumber":"2.5.1.56","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19273"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:35418"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:58702"},{"database":"ChEBI","id":"CHEBI:63153"}]}}
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"81116 / NCTC 11828"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

```text
ID   NEUAS_CAMJ8             Reviewed;         346 AA.
AC   P0DY06;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};
DE            Short=Neu5Ac synthase {ECO:0000303|PubMed:38382015};
DE            EC=2.5.1.56 {ECO:0000269|PubMed:38382015};
GN   Name=HS6.11 {ECO:0000303|PubMed:38382015};
GN   OrderedLocusNames=C8J_1339 {ECO:0000312|EMBL:ABV52937.1};
OS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC
OS   11828).
OC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;
OC   Campylobacterales; Campylobacteraceae; Campylobacter.
OX   NCBI_TaxID=407148;
```

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

```text
DE   RecName: Full=N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};
DE            Short=Neu5Ac synthase {ECO:0000303|PubMed:38382015};
DE            EC=2.5.1.56 {ECO:0000269|PubMed:38382015};
```

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.
RC   STRAIN=81116 / NCTC 11828;
RX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;
RA   Ghosh M.K., Raushel F.M.;
RT   "Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-
RT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter
RT   jejuni.";
RL   Biochemistry 63:688-698(2024).
```

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 39-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-
CC         acetylneuraminate + phosphate; Xref=Rhea:RHEA:19273,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:35418, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:58702, ChEBI:CHEBI:63153; EC=2.5.1.56;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19274;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
