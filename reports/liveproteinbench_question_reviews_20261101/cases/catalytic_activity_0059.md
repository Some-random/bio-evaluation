# catalytic_activity_0059

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKKILFITGTRADYSKIKSLMYRVQNSSEFELCIFATGMHLSKNFGYTVKELYKNGFKNIYEFINYDKYYQTDKALATTIDGFSRYVNELKPDLIVVHGDRIEPLAAAIVGALNNILVAHIEGGEISGTIDDSLRHAISKLAHIHLVNDEFAKKRLMQLGEDEKSIFIIGSPDLELLNDNKISLNEAKKYYDINYENYALLMFHPVTTEITSIKNQADNLVKALIQSNKNYIVIYPNNDLGFELILQSYEELKNNPRFKLFPSLRFEYFITLLKNADFIIGNSSCILKEALYLKTAGILVGSRQNGRLGNENTLKVNANSDEILKAINTIHKKQDLFSAKLEILDSSKLFFEYLQSGEFFKLSTQKVFKDIII

[Multiple Choices]
A. L-dopa + H(+) = dopamine + CO2
B. D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)
C. 2 5'-deoxyadenosin-5'-yl radical + 2 dAMP + A = 2 4'-phospho-dehydrooxetanocin + 2 5'-deoxyadenosine + AH2
D. UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)
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

> The supplied sequence exactly matches the UniProt sequence annotated as UDP-N-acetylglucosamine 2-epimerase. Its catalytic-activity annotation gives choice D and cites experimental evidence (ECO:0000269) from a 2024 paper. The archived entry available by the stated historical cutoff also records this reaction.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct reactions, but the sequence and prompt provide no biological context or recognizable, decisive feature that identifies this specific UDP-GlcNAc hydrolysis/epimerization reaction over the alternatives.


**Missing item-specific fact**

> The protein-specific catalytic-function annotation or experimental characterization linking this sequence to the UDP-N-acetylglucosamine reaction.


**Reason**

> Identifying the correct option requires knowing the function of this particular protein. The reviewer-only database and paper evidence supports the key, but that information was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options specify distinct reactions, and the sequence-matched annotation supports D; no competing option is supported by the supplied evidence.


### Important caveats

- The database record links the reaction to experimental evidence from a cited paper, but the paper was not independently retrieved or validated here.
- The author’s exact source snapshot is unknown; the archived sequence-matched entry supports the reaction annotation by the stated historical cutoff.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct reactions, but the sequence and prompt provide no biological context or recognizable, decisive feature that identifies this specific UDP-GlcNAc hydrolysis/epimerization reaction over the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic-function annotation or experimental characterization linking this sequence to the UDP-N-acetylglucosamine reaction.",
    "reason": "Identifying the correct option requires knowing the function of this particular protein. The reviewer-only database and paper evidence supports the key, but that information was not supplied to the evaluated model."
  },
  "case_id": "catalytic_activity_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as UDP-N-acetylglucosamine 2-epimerase. Its catalytic-activity annotation gives choice D and cites experimental evidence (ECO:0000269) from a 2024 paper. The archived entry available by the stated historical cutoff also records this reaction."
  },
  "important_caveats": [
    "The database record links the reaction to experimental evidence from a cited paper, but the paper was not independently retrieved or validated here.",
    "The author’s exact source snapshot is unknown; the archived sequence-matched entry supports the reaction annotation by the stated historical cutoff."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options specify distinct reactions, and the sequence-matched annotation supports D; no competing option is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as UDP-N-acetylglucosamine 2-epimerase. Its catalytic-activity annotation gives choice D and cites experimental evidence (ECO:0000269) from a 2024 paper. The archived entry available by the stated historical cutoff also records this reaction.",
    "evidence_ids": ["C1", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct reactions, but the sequence and prompt provide no biological context or recognizable, decisive feature that identifies this specific UDP-GlcNAc hydrolysis/epimerization reaction over the alternatives.",
    "missing_item_specific_fact": "The protein-specific catalytic-function annotation or experimental characterization linking this sequence to the UDP-N-acetylglucosamine reaction.",
    "reason": "Identifying the correct option requires knowing the function of this particular protein. The reviewer-only database and paper evidence supports the key, but that information was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options specify distinct reactions, and the sequence-matched annotation supports D; no competing option is supported by the supplied evidence."
  },
  "important_caveats": [
    "The database record links the reaction to experimental evidence from a cited paper, but the paper was not independently retrieved or validated here.",
    "The author’s exact source snapshot is unknown; the archived sequence-matched entry supports the reaction annotation by the stated historical cutoff."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The benchmark sequence (373 aa, SHA256 matched) corresponds exactly to UniProt P0DY05 (UAEPH_CAMJ8) from Campylobacter jejuni strain 81116. The UniProt entry annotates this protein as 'UDP-N-acetylglucosamine 2-epimerase' (EC 3.2.1.183, 'Hydrolyzing UDP-GlcNAc 2-epimerase') with the catalytic reaction 'UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)' (Rhea:RHEA:30683), supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024 Biochemistry). Choice D matches this reaction verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could partially eliminate distractors from sequence: absence of a PLP-binding lysine in a conserved aromatic-decarboxylase context weakens Choice A; absence of a radical SAM CX3CX2C motif weakens Choice C. However, positively identifying the hydrolyzing UDP-GlcNAc 2-epimerase (EC 3.2.1.183) and distinguishing it from an N-acetyltransferase (Choice B) requires recognizing a specific, relatively obscure enzyme family fold or recalling the 2024 experimental characterization. No widely-taught sequence motif in the provided sequence unambiguously points to this rare hydrolyzing epimerase reaction.


**Missing item-specific fact**

> The specific family assignment (UDP-GlcNAc 2-epimerase / hydrolyzing variant, EC 3.2.1.183) and the 2024 experimental demonstration (PubMed:38382015) that this Campylobacter protein catalyzes the hydrolyzing epimerization of UDP-GlcNAc to aldehydo-GlcNAc. This is a recently characterized, specialized reaction not inferable from generic sequence features without prior knowledge of this enzyme family.


**Reason**

> The question requires identifying a recently characterized (2024/2025) and relatively obscure enzyme activity from a 373-aa sequence lacking broadly recognizable catalytic motifs. While negative reasoning can eliminate A (no PLP motif) and C (no radical SAM motif), the positive identification of D over B depends on knowing the specific protein family or its experimental annotation rather than on generalizable sequence-to-function inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent mechanistically distinct enzyme classes (PLP decarboxylase, acyltransferase, radical SAM enzyme, glycosidase/epimerase). Only D matches the annotated activity. No other option is defensible for this protein given the experimental evidence.


### Important caveats

- The UniProt entry was first public on 2025-06-18 and the key experimental paper (PubMed:38382015) was published in 2024; the annotation may postdate the benchmark construction window, though the sequence itself is stable (sequence version 1 unchanged).
- The evidence code ECO:0000269 (inferred from direct assay) indicates experimental characterization, not mere computational prediction.
- The 'hydrolyzing' qualifier distinguishes EC 3.2.1.183 from the more common non-hydrolyzing UDP-GlcNAc 2-epimerase (EC 5.1.3.14); this distinction is itself a specialized biochemical point.
- Reviewer-only evidence was used to confirm the key; the evaluated model received only the raw sequence and four reaction choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could partially eliminate distractors from sequence: absence of a PLP-binding lysine in a conserved aromatic-decarboxylase context weakens Choice A; absence of a radical SAM CX3CX2C motif weakens Choice C. However, positively identifying the hydrolyzing UDP-GlcNAc 2-epimerase (EC 3.2.1.183) and distinguishing it from an N-acetyltransferase (Choice B) requires recognizing a specific, relatively obscure enzyme family fold or recalling the 2024 experimental characterization. No widely-taught sequence motif in the provided sequence unambiguously points to this rare hydrolyzing epimerase reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific family assignment (UDP-GlcNAc 2-epimerase / hydrolyzing variant, EC 3.2.1.183) and the 2024 experimental demonstration (PubMed:38382015) that this Campylobacter protein catalyzes the hydrolyzing epimerization of UDP-GlcNAc to aldehydo-GlcNAc. This is a recently characterized, specialized reaction not inferable from generic sequence features without prior knowledge of this enzyme family.",
    "reason": "The question requires identifying a recently characterized (2024/2025) and relatively obscure enzyme activity from a 373-aa sequence lacking broadly recognizable catalytic motifs. While negative reasoning can eliminate A (no PLP motif) and C (no radical SAM motif), the positive identification of D over B depends on knowing the specific protein family or its experimental annotation rather than on generalizable sequence-to-function inference."
  },
  "case_id": "catalytic_activity_0059",
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
    "reason": "The benchmark sequence (373 aa, SHA256 matched) corresponds exactly to UniProt P0DY05 (UAEPH_CAMJ8) from Campylobacter jejuni strain 81116. The UniProt entry annotates this protein as 'UDP-N-acetylglucosamine 2-epimerase' (EC 3.2.1.183, 'Hydrolyzing UDP-GlcNAc 2-epimerase') with the catalytic reaction 'UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)' (Rhea:RHEA:30683), supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024 Biochemistry). Choice D matches this reaction verbatim."
  },
  "important_caveats": [
    "The UniProt entry was first public on 2025-06-18 and the key experimental paper (PubMed:38382015) was published in 2024; the annotation may postdate the benchmark construction window, though the sequence itself is stable (sequence version 1 unchanged).",
    "The evidence code ECO:0000269 (inferred from direct assay) indicates experimental characterization, not mere computational prediction.",
    "The 'hydrolyzing' qualifier distinguishes EC 3.2.1.183 from the more common non-hydrolyzing UDP-GlcNAc 2-epimerase (EC 5.1.3.14); this distinction is itself a specialized biochemical point.",
    "Reviewer-only evidence was used to confirm the key; the evaluated model received only the raw sequence and four reaction choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes (PLP decarboxylase, acyltransferase, radical SAM enzyme, glycosidase/epimerase). Only D matches the annotated activity. No other option is defensible for this protein given the experimental evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The benchmark sequence (373 aa, SHA256 matched) corresponds exactly to UniProt P0DY05 (UAEPH_CAMJ8) from Campylobacter jejuni strain 81116. The UniProt entry annotates this protein as 'UDP-N-acetylglucosamine 2-epimerase' (EC 3.2.1.183, 'Hydrolyzing UDP-GlcNAc 2-epimerase') with the catalytic reaction 'UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)' (Rhea:RHEA:30683), supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024 Biochemistry). Choice D matches this reaction verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could partially eliminate distractors from sequence: absence of a PLP-binding lysine in a conserved aromatic-decarboxylase context weakens Choice A; absence of a radical SAM CX3CX2C motif weakens Choice C. However, positively identifying the hydrolyzing UDP-GlcNAc 2-epimerase (EC 3.2.1.183) and distinguishing it from an N-acetyltransferase (Choice B) requires recognizing a specific, relatively obscure enzyme family fold or recalling the 2024 experimental characterization. No widely-taught sequence motif in the provided sequence unambiguously points to this rare hydrolyzing epimerase reaction.",
    "missing_item_specific_fact": "The specific family assignment (UDP-GlcNAc 2-epimerase / hydrolyzing variant, EC 3.2.1.183) and the 2024 experimental demonstration (PubMed:38382015) that this Campylobacter protein catalyzes the hydrolyzing epimerization of UDP-GlcNAc to aldehydo-GlcNAc. This is a recently characterized, specialized reaction not inferable from generic sequence features without prior knowledge of this enzyme family.",
    "reason": "The question requires identifying a recently characterized (2024/2025) and relatively obscure enzyme activity from a 373-aa sequence lacking broadly recognizable catalytic motifs. While negative reasoning can eliminate A (no PLP motif) and C (no radical SAM motif), the positive identification of D over B depends on knowing the specific protein family or its experimental annotation rather than on generalizable sequence-to-function inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes (PLP decarboxylase, acyltransferase, radical SAM enzyme, glycosidase/epimerase). Only D matches the annotated activity. No other option is defensible for this protein given the experimental evidence."
  },
  "important_caveats": [
    "The UniProt entry was first public on 2025-06-18 and the key experimental paper (PubMed:38382015) was published in 2024; the annotation may postdate the benchmark construction window, though the sequence itself is stable (sequence version 1 unchanged).",
    "The evidence code ECO:0000269 (inferred from direct assay) indicates experimental characterization, not mere computational prediction.",
    "The 'hydrolyzing' qualifier distinguishes EC 3.2.1.183 from the more common non-hydrolyzing UDP-GlcNAc 2-epimerase (EC 5.1.3.14); this distinction is itself a specialized biochemical point.",
    "Reviewer-only evidence was used to confirm the key; the evaluated model received only the raw sequence and four reaction choices."
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

**Accession:** `P0DY05` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
"P0DY05"
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"Hydrolyzing UDP-GlcNAc 2-epimerase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"3.2.1.183"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetylglucosamine 2-epimerase"}}}
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:30684"}}],"reaction":{"ecNumber":"3.2.1.183","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:30683"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17122"},{"database":"ChEBI","id":"CHEBI:57705"},{"database":"ChEBI","id":"CHEBI:58223"}]}}
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"81116 / NCTC 11828"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:04.730217+00:00.  

```text
ID   UAEPH_CAMJ8             Reviewed;         373 AA.
AC   P0DY05;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};
DE            EC=3.2.1.183 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=Hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};
GN   Name=HS6.10 {ECO:0000303|PubMed:38382015};
GN   OrderedLocusNames=C8J_1338 {ECO:0000312|EMBL:ABV52936.1};
OS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC
OS   11828).
OC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;
OC   Campylobacterales; Campylobacteraceae; Campylobacter.
OX   NCBI_TaxID=407148;
```

Source SHA-256: `5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:04.730217+00:00.  

```text
DE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};
DE            EC=3.2.1.183 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=Hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};
```

Source SHA-256: `5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:04.730217+00:00.  

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

Source SHA-256: `5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)  
**Locator:** `lines 40-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:04.730217+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-
CC         mannosamine + UDP + H(+); Xref=Rhea:RHEA:30683, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17122, ChEBI:CHEBI:57705,
CC         ChEBI:CHEBI:58223; EC=3.2.1.183;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:30684;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 59. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
