# catalytic_activity_0103

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSVKKAGVLGATGSVGQRFILLLSKHPEFEIHALGASSRSAGKKYKDAASWKQTETLPETEQDIVVQECKPEGNFLECDVVFSGLDADVAGDIEKSFVEAGLAVVSNAKNYRREKDVPLVVPIVNPEHIDVVENKVKQAVSKGGKKPGFIICISNCSTAGLVAPLKPLVEKFGPIDALTTTTLQAISGAGFSPGVSGMDILDNIVPYISGEEDKLEWETKKILGGVNAEGTEFVPIPESEMKVSAQCNRVPVIDGHTECISLRFANRPAPSVEDVKQCLREYECAASKLGCHSAPKQTIHVLDQPDRPQPRLDRDRDSGYGVSVGRIREDSLLDFKMVVLSHNTIIGAAGAGILIAEILKAKNII

[Multiple Choices]
A. a phosphate monoester + H2O = an alcohol + phosphate
B. daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)
C. L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)
D. (2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)
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

> The sequence exactly matches the annotated Candida albicans aspartate-semialdehyde dehydrogenase. The UniProt catalytic-activity annotation gives the reaction in choice C and cites ECO:0000269 evidence linked to publications. This supports the key, while the evidence excerpt does not independently establish the details of those experiments.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with an NADP-dependent enzyme, which could help disfavor choices involving a phosphatase or an ATP-driven transporter. But that broad inference does not establish the specific substrate and product in choice C.


**Missing item-specific fact**

> The protein-specific identity or functional annotation as aspartate-semialdehyde dehydrogenase, or equivalent experimental knowledge of its substrate and reaction, is absent from the input.


**Reason**

> Distinguishing the precise reaction requires linking this sequence to its specific enzyme function; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotated catalytic activity matches choice C; the other choices describe different reaction types or substrates.


### Important caveats

- The sequence-to-accession match and annotation evidence are reviewer-only, not information supplied to the evaluated model.
- The UniProt annotation cites experimental evidence codes, but the cited primary studies were not independently assessed here.
- The annotation gives a physiological direction of right-to-left; choice C states the same reaction in the opposite direction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with an NADP-dependent enzyme, which could help disfavor choices involving a phosphatase or an ATP-driven transporter. But that broad inference does not establish the specific substrate and product in choice C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation as aspartate-semialdehyde dehydrogenase, or equivalent experimental knowledge of its substrate and reaction, is absent from the input.",
    "reason": "Distinguishing the precise reaction requires linking this sequence to its specific enzyme function; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from supplied evidence."
  },
  "case_id": "catalytic_activity_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the annotated Candida albicans aspartate-semialdehyde dehydrogenase. The UniProt catalytic-activity annotation gives the reaction in choice C and cites ECO:0000269 evidence linked to publications. This supports the key, while the evidence excerpt does not independently establish the details of those experiments."
  },
  "important_caveats": [
    "The sequence-to-accession match and annotation evidence are reviewer-only, not information supplied to the evaluated model.",
    "The UniProt annotation cites experimental evidence codes, but the cited primary studies were not independently assessed here.",
    "The annotation gives a physiological direction of right-to-left; choice C states the same reaction in the opposite direction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated catalytic activity matches choice C; the other choices describe different reaction types or substrates."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the annotated Candida albicans aspartate-semialdehyde dehydrogenase. The UniProt catalytic-activity annotation gives the reaction in choice C and cites ECO:0000269 evidence linked to publications. This supports the key, while the evidence excerpt does not independently establish the details of those experiments.",
    "evidence_ids": ["C1", "C4", "C5", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with an NADP-dependent enzyme, which could help disfavor choices involving a phosphatase or an ATP-driven transporter. But that broad inference does not establish the specific substrate and product in choice C.",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation as aspartate-semialdehyde dehydrogenase, or equivalent experimental knowledge of its substrate and reaction, is absent from the input.",
    "reason": "Distinguishing the precise reaction requires linking this sequence to its specific enzyme function; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated catalytic activity matches choice C; the other choices describe different reaction types or substrates."
  },
  "important_caveats": [
    "The sequence-to-accession match and annotation evidence are reviewer-only, not information supplied to the evaluated model.",
    "The UniProt annotation cites experimental evidence codes, but the cited primary studies were not independently assessed here.",
    "The annotation gives a physiological direction of right-to-left; choice C states the same reaction in the opposite direction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5ALM0 (sequence matched, 365 AA) explicitly annotates this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)', which matches Choice C verbatim. The annotation is backed by experimental evidence (ECO:0000269) from four independent publications and a crystal structure (PDB 3HSK in complex with NADP+). The historical archived entry (version 145) confirms the same annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H8](#evidence-h8), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GVLGATGSVG at positions ~6-15), which is diagnostic of a nucleotide-dependent oxidoreductase and effectively eliminates Choice A (phosphatase, no NAD cofactor) and Choice B (ABC transporter, different fold entirely). More specifically, the catalytic-cysteine context 'VPVIDGHTECISL' contains the 'GHTC' signature motif characteristic of the aspartate-semialdehyde dehydrogenase (ASADH) family, where the active-site cysteine attacks the aldehyde substrate to form a thiohemiacetal intermediate. This motif, combined with the NADP (not NAD) preference implied by the Rossmann fold context, points specifically to EC 1.2.1.11 (Choice C). Choice D (vomilenine dehydrogenase) is a plant monoterpene-indole-alkaloid biosynthesis enzyme; the fungal origin of the sequence and the ASADH-specific catalytic motif argue against it.


**Missing item-specific fact**

> Precise recognition of the 'GHTEC' catalytic motif as ASADH-family-specific requires specialized enzyme-family knowledge beyond generic Rossmann-fold recognition, though this motif is well-documented in biochemistry literature.


**Reason**

> The sequence provides two layers of identifiable signal: (1) the Rossmann fold narrows the answer to NAD(P)-dependent dehydrogenases (eliminating A and B), and (2) the 'GHTC' catalytic-cysteine context is a recognized ASADH family signature that distinguishes C from other dehydrogenases like D. A model with solid enzyme-family knowledge can construct this argument. The distinction from D is further supported by biological plausibility (vomilenine is a plant alkaloid intermediate; this is a fungal protein).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A and B are clearly eliminable by the Rossmann fold (not a phosphatase or transporter). Choice D is a plant-specific alkaloid biosynthesis enzyme with a different catalytic architecture and biological context. Only Choice C matches both the NADP-dependent dehydrogenase fold and the ASADH-specific catalytic cysteine motif. No other choice is genuinely defensible.


### Important caveats

- The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269, four publications, crystal structure PDB 3HSK), not merely computational or by similarity.
- The identity of the protein (Q5ALM0, Candida albicans ASADH) was inferred from dataset metadata and is reviewer-only; the evaluated model sees only the raw sequence.
- Distinguishing C from D relies on recognizing the 'GHTC' catalytic motif and the biological implausibility of a fungal enzyme performing a plant-specific alkaloid reaction; a model lacking enzyme-family knowledge may struggle with this specific discrimination.
- The physiological direction is noted as right-to-left (reductive direction, i.e., 4-phospho-L-aspartate → L-aspartate 4-semialdehyde), but the question lists the oxidative direction as written in the Rhea reaction, which is the standard EC notation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GVLGATGSVG at positions ~6-15), which is diagnostic of a nucleotide-dependent oxidoreductase and effectively eliminates Choice A (phosphatase, no NAD cofactor) and Choice B (ABC transporter, different fold entirely). More specifically, the catalytic-cysteine context 'VPVIDGHTECISL' contains the 'GHTC' signature motif characteristic of the aspartate-semialdehyde dehydrogenase (ASADH) family, where the active-site cysteine attacks the aldehyde substrate to form a thiohemiacetal intermediate. This motif, combined with the NADP (not NAD) preference implied by the Rossmann fold context, points specifically to EC 1.2.1.11 (Choice C). Choice D (vomilenine dehydrogenase) is a plant monoterpene-indole-alkaloid biosynthesis enzyme; the fungal origin of the sequence and the ASADH-specific catalytic motif argue against it.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of the 'GHTEC' catalytic motif as ASADH-family-specific requires specialized enzyme-family knowledge beyond generic Rossmann-fold recognition, though this motif is well-documented in biochemistry literature.",
    "reason": "The sequence provides two layers of identifiable signal: (1) the Rossmann fold narrows the answer to NAD(P)-dependent dehydrogenases (eliminating A and B), and (2) the 'GHTC' catalytic-cysteine context is a recognized ASADH family signature that distinguishes C from other dehydrogenases like D. A model with solid enzyme-family knowledge can construct this argument. The distinction from D is further supported by biological plausibility (vomilenine is a plant alkaloid intermediate; this is a fungal protein)."
  },
  "case_id": "catalytic_activity_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H8",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5ALM0 (sequence matched, 365 AA) explicitly annotates this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)', which matches Choice C verbatim. The annotation is backed by experimental evidence (ECO:0000269) from four independent publications and a crystal structure (PDB 3HSK in complex with NADP+). The historical archived entry (version 145) confirms the same annotation."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269, four publications, crystal structure PDB 3HSK), not merely computational or by similarity.",
    "The identity of the protein (Q5ALM0, Candida albicans ASADH) was inferred from dataset metadata and is reviewer-only; the evaluated model sees only the raw sequence.",
    "Distinguishing C from D relies on recognizing the 'GHTC' catalytic motif and the biological implausibility of a fungal enzyme performing a plant-specific alkaloid reaction; a model lacking enzyme-family knowledge may struggle with this specific discrimination.",
    "The physiological direction is noted as right-to-left (reductive direction, i.e., 4-phospho-L-aspartate → L-aspartate 4-semialdehyde), but the question lists the oxidative direction as written in the Rhea reaction, which is the standard EC notation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and B are clearly eliminable by the Rossmann fold (not a phosphatase or transporter). Choice D is a plant-specific alkaloid biosynthesis enzyme with a different catalytic architecture and biological context. Only Choice C matches both the NADP-dependent dehydrogenase fold and the ASADH-specific catalytic cysteine motif. No other choice is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5ALM0 (sequence matched, 365 AA) explicitly annotates this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)', which matches Choice C verbatim. The annotation is backed by experimental evidence (ECO:0000269) from four independent publications and a crystal structure (PDB 3HSK in complex with NADP+). The historical archived entry (version 145) confirms the same annotation.",
    "evidence_ids": ["C4", "C5", "H2", "H8", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GVLGATGSVG at positions ~6-15), which is diagnostic of a nucleotide-dependent oxidoreductase and effectively eliminates Choice A (phosphatase, no NAD cofactor) and Choice B (ABC transporter, different fold entirely). More specifically, the catalytic-cysteine context 'VPVIDGHTECISL' contains the 'GHTC' signature motif characteristic of the aspartate-semialdehyde dehydrogenase (ASADH) family, where the active-site cysteine attacks the aldehyde substrate to form a thiohemiacetal intermediate. This motif, combined with the NADP (not NAD) preference implied by the Rossmann fold context, points specifically to EC 1.2.1.11 (Choice C). Choice D (vomilenine dehydrogenase) is a plant monoterpene-indole-alkaloid biosynthesis enzyme; the fungal origin of the sequence and the ASADH-specific catalytic motif argue against it.",
    "missing_item_specific_fact": "Precise recognition of the 'GHTEC' catalytic motif as ASADH-family-specific requires specialized enzyme-family knowledge beyond generic Rossmann-fold recognition, though this motif is well-documented in biochemistry literature.",
    "reason": "The sequence provides two layers of identifiable signal: (1) the Rossmann fold narrows the answer to NAD(P)-dependent dehydrogenases (eliminating A and B), and (2) the 'GHTC' catalytic-cysteine context is a recognized ASADH family signature that distinguishes C from other dehydrogenases like D. A model with solid enzyme-family knowledge can construct this argument. The distinction from D is further supported by biological plausibility (vomilenine is a plant alkaloid intermediate; this is a fungal protein)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and B are clearly eliminable by the Rossmann fold (not a phosphatase or transporter). Choice D is a plant-specific alkaloid biosynthesis enzyme with a different catalytic architecture and biological context. Only Choice C matches both the NADP-dependent dehydrogenase fold and the ASADH-specific catalytic cysteine motif. No other choice is genuinely defensible."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269, four publications, crystal structure PDB 3HSK), not merely computational or by similarity.",
    "The identity of the protein (Q5ALM0, Candida albicans ASADH) was inferred from dataset metadata and is reviewer-only; the evaluated model sees only the raw sequence.",
    "Distinguishing C from D relies on recognizing the 'GHTC' catalytic motif and the biological implausibility of a fungal enzyme performing a plant-specific alkaloid reaction; a model lacking enzyme-family knowledge may struggle with this specific discrimination.",
    "The physiological direction is noted as right-to-left (reductive direction, i.e., 4-phospho-L-aspartate → L-aspartate 4-semialdehyde), but the question lists the oxidative direction as written in the Rhea reaction, which is the standard EC notation."
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

**Accession:** `Q5ALM0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 145. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
"Q5ALM0"
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17419877","source":"PubMed"}],"value":"CaASADH"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20124701","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32383780","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"34469014","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"20124701","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32383780","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"34469014","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24286"}}],"reaction":{"ecNumber":"1.2.1.11","evidences":[{"evidenceCode":"ECO:0000269","id":"20124701","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32383780","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"34469014","source":"PubMed"}],"name":"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24284"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:537519"}]}}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};
DE   AltName: Full=CaASADH {ECO:0000303|PubMed:17419877};
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 75-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
RN   [8] {ECO:0007744|PDB:3HSK}
RP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH NADP(+), FUNCTION,
RP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.
RX   PubMed=20124701; DOI=10.1107/s0907444909052834;
RA   Arachea B.T., Liu X., Pavlovsky A.G., Viola R.E.;
RT   "Expansion of the aspartate beta-semialdehyde dehydrogenase family: the
RT   first structure of a fungal ortholog.";
RL   Acta Crystallogr. D 66:205-212(2010).
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 92-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-
CC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;
CC         Evidence={ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391,
CC         ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;
CC         Evidence={ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391,
CC         ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 103. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
