# EC_number_0101

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.2.1.11

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
A. 1.2.1.101
B. 1.2.1.11
C. 2.1.1.394
D. 1.5.1.38
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

> The supplied sequence exactly matches the UniProt sequence identified as Candida albicans aspartate-semialdehyde dehydrogenase. Its EC 1.2.1.11 annotation is linked to catalytic-activity evidence cited to published studies, supporting choice B for this protein.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could support a protein-family inference with suitable analysis, but the input provides no organism, functional annotation, or reaction data. General sequence reasoning alone does not establish this specific enzyme's complete EC number.


**Missing item-specific fact**

> The protein-specific functional identification as aspartate-semialdehyde dehydrogenase and its experimentally supported catalytic reaction, which maps to EC 1.2.1.11.


**Reason**

> Distinguishing the correct EC requires recognizing or identifying this particular protein's function from external annotation, homology analysis, or experimental knowledge. The reviewer-only sequence-matched annotation supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports EC 1.2.1.11 for the sequence-matched protein; no competing listed choice is supported.


### Important caveats

- The annotation is for the exact matching Candida albicans sequence and cites experimental evidence codes, but the primary studies were not independently reviewed here.
- The evidence establishes support for the author's key; it does not show that the model could derive the EC number from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could support a protein-family inference with suitable analysis, but the input provides no organism, functional annotation, or reaction data. General sequence reasoning alone does not establish this specific enzyme's complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification as aspartate-semialdehyde dehydrogenase and its experimentally supported catalytic reaction, which maps to EC 1.2.1.11.",
    "reason": "Distinguishing the correct EC requires recognizing or identifying this particular protein's function from external annotation, homology analysis, or experimental knowledge. The reviewer-only sequence-matched annotation supports the key but was not supplied to the evaluated model."
  },
  "case_id": "EC_number_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence identified as Candida albicans aspartate-semialdehyde dehydrogenase. Its EC 1.2.1.11 annotation is linked to catalytic-activity evidence cited to published studies, supporting choice B for this protein."
  },
  "important_caveats": [
    "The annotation is for the exact matching Candida albicans sequence and cites experimental evidence codes, but the primary studies were not independently reviewed here.",
    "The evidence establishes support for the author's key; it does not show that the model could derive the EC number from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports EC 1.2.1.11 for the sequence-matched protein; no competing listed choice is supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence identified as Candida albicans aspartate-semialdehyde dehydrogenase. Its EC 1.2.1.11 annotation is linked to catalytic-activity evidence cited to published studies, supporting choice B for this protein.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could support a protein-family inference with suitable analysis, but the input provides no organism, functional annotation, or reaction data. General sequence reasoning alone does not establish this specific enzyme's complete EC number.",
    "missing_item_specific_fact": "The protein-specific functional identification as aspartate-semialdehyde dehydrogenase and its experimentally supported catalytic reaction, which maps to EC 1.2.1.11.",
    "reason": "Distinguishing the correct EC requires recognizing or identifying this particular protein's function from external annotation, homology analysis, or experimental knowledge. The reviewer-only sequence-matched annotation supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports EC 1.2.1.11 for the sequence-matched protein; no competing listed choice is supported."
  },
  "important_caveats": [
    "The annotation is for the exact matching Candida albicans sequence and cites experimental evidence codes, but the primary studies were not independently reviewed here.",
    "The evidence establishes support for the author's key; it does not show that the model could derive the EC number from the sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5ALM0 (sequence matched exactly, 365 aa) annotates this protein as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, backed by experimental evidence (ECO:0000269) from four independent publications including X-ray crystallography (PDB 3HSK, 2.2 Å in complex with NADP+), enzyme activity assays, and inhibitor studies. The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP(+) → 4-phospho-L-aspartate + NADPH + H(+)) is experimentally confirmed. Both current (v147) and historical (v145) UniProt records agree.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C10](#evidence-c10), [H1](#evidence-h1), [H2](#evidence-h2), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Rossmann-fold nucleotide-binding motif (GVLGATGSVGQRF, GxGxxG pattern) indicating an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). Critically, the 'NCSTAG' motif containing the catalytic cysteine is a well-characterized active-site signature specific to the aspartate-semialdehyde dehydrogenase (ASADH) family (EC 1.2.1.11), distinguishing it from other aldehyde dehydrogenases. EC 2.1.1.394 (methyltransferase) is eliminated by the oxidoreductase architecture; EC 1.5.1.38 (CH-NH oxidoreductase) is eliminated by the aldehyde-dehydrogenase catalytic Cys. EC 1.2.1.101 (methylmalonate-semialdehyde dehydrogenase, acylating) uses CoA rather than phosphate and lacks the 'NCSTAG' catalytic motif, allowing elimination by family-specific motif recognition.


**Missing item-specific fact**

> None critical. Recognition of the 'NCSTAG' catalytic motif as specific to aspartate-semialdehyde dehydrogenase is established enzymology knowledge (appears in structural and mechanistic literature on amino acid biosynthesis), not an item-specific database annotation.


**Reason**

> A model with general enzymology knowledge can trace: Rossmann fold → EC 1.x; aldehyde dehydrogenase Cys motif → EC 1.2.1.x; 'NCSTAG' specificity → EC 1.2.1.11. The distractors span different EC classes/subclasses (2.1.1.394 is a transferase; 1.5.1.38 acts on CH-NH), making them eliminable by class-level reasoning. The remaining distinction between 1.2.1.11 and 1.2.1.101 rests on the well-known 'NCSTAG' family signature rather than a single-protein database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The 'NCSTAG' catalytic motif, the Rossmann fold, the ~365-aa length, and the NADP-binding context collectively point to EC 1.2.1.11. The other three options belong to different EC classes or subclasses and lack the diagnostic semialdehyde dehydrogenase active-site architecture. No alternative option is defensible given the sequence features.


### Important caveats

- The EC 1.2.1.11 annotation is supported by direct experimental evidence (ECO:0000269) including X-ray crystallography and multiple biochemical assays, not merely computational transfer.
- The 'NCSTAG' motif recognition is a family-level enzymology signature; a model unfamiliar with ASADH active-site architecture might struggle to distinguish 1.2.1.11 from 1.2.1.101 without database lookup, though the broader class/subclass elimination of C and D is straightforward.
- The sequence is from Candida albicans (fungal ASADH); the reviewer evidence confirms the sequence matches Q5ALM0 exactly (SHA-256 match, 365 aa).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold nucleotide-binding motif (GVLGATGSVGQRF, GxGxxG pattern) indicating an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). Critically, the 'NCSTAG' motif containing the catalytic cysteine is a well-characterized active-site signature specific to the aspartate-semialdehyde dehydrogenase (ASADH) family (EC 1.2.1.11), distinguishing it from other aldehyde dehydrogenases. EC 2.1.1.394 (methyltransferase) is eliminated by the oxidoreductase architecture; EC 1.5.1.38 (CH-NH oxidoreductase) is eliminated by the aldehyde-dehydrogenase catalytic Cys. EC 1.2.1.101 (methylmalonate-semialdehyde dehydrogenase, acylating) uses CoA rather than phosphate and lacks the 'NCSTAG' catalytic motif, allowing elimination by family-specific motif recognition.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of the 'NCSTAG' catalytic motif as specific to aspartate-semialdehyde dehydrogenase is established enzymology knowledge (appears in structural and mechanistic literature on amino acid biosynthesis), not an item-specific database annotation.",
    "reason": "A model with general enzymology knowledge can trace: Rossmann fold → EC 1.x; aldehyde dehydrogenase Cys motif → EC 1.2.1.x; 'NCSTAG' specificity → EC 1.2.1.11. The distractors span different EC classes/subclasses (2.1.1.394 is a transferase; 1.5.1.38 acts on CH-NH), making them eliminable by class-level reasoning. The remaining distinction between 1.2.1.11 and 1.2.1.101 rests on the well-known 'NCSTAG' family signature rather than a single-protein database lookup."
  },
  "case_id": "EC_number_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C10",
      "H1",
      "H2",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5ALM0 (sequence matched exactly, 365 aa) annotates this protein as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, backed by experimental evidence (ECO:0000269) from four independent publications including X-ray crystallography (PDB 3HSK, 2.2 Å in complex with NADP+), enzyme activity assays, and inhibitor studies. The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP(+) → 4-phospho-L-aspartate + NADPH + H(+)) is experimentally confirmed. Both current (v147) and historical (v145) UniProt records agree."
  },
  "important_caveats": [
    "The EC 1.2.1.11 annotation is supported by direct experimental evidence (ECO:0000269) including X-ray crystallography and multiple biochemical assays, not merely computational transfer.",
    "The 'NCSTAG' motif recognition is a family-level enzymology signature; a model unfamiliar with ASADH active-site architecture might struggle to distinguish 1.2.1.11 from 1.2.1.101 without database lookup, though the broader class/subclass elimination of C and D is straightforward.",
    "The sequence is from Candida albicans (fungal ASADH); the reviewer evidence confirms the sequence matches Q5ALM0 exactly (SHA-256 match, 365 aa)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 'NCSTAG' catalytic motif, the Rossmann fold, the ~365-aa length, and the NADP-binding context collectively point to EC 1.2.1.11. The other three options belong to different EC classes or subclasses and lack the diagnostic semialdehyde dehydrogenase active-site architecture. No alternative option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5ALM0 (sequence matched exactly, 365 aa) annotates this protein as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, backed by experimental evidence (ECO:0000269) from four independent publications including X-ray crystallography (PDB 3HSK, 2.2 Å in complex with NADP+), enzyme activity assays, and inhibitor studies. The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP(+) → 4-phospho-L-aspartate + NADPH + H(+)) is experimentally confirmed. Both current (v147) and historical (v145) UniProt records agree.",
    "evidence_ids": ["C4", "C5", "C10", "H1", "H2", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold nucleotide-binding motif (GVLGATGSVGQRF, GxGxxG pattern) indicating an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). Critically, the 'NCSTAG' motif containing the catalytic cysteine is a well-characterized active-site signature specific to the aspartate-semialdehyde dehydrogenase (ASADH) family (EC 1.2.1.11), distinguishing it from other aldehyde dehydrogenases. EC 2.1.1.394 (methyltransferase) is eliminated by the oxidoreductase architecture; EC 1.5.1.38 (CH-NH oxidoreductase) is eliminated by the aldehyde-dehydrogenase catalytic Cys. EC 1.2.1.101 (methylmalonate-semialdehyde dehydrogenase, acylating) uses CoA rather than phosphate and lacks the 'NCSTAG' catalytic motif, allowing elimination by family-specific motif recognition.",
    "missing_item_specific_fact": "None critical. Recognition of the 'NCSTAG' catalytic motif as specific to aspartate-semialdehyde dehydrogenase is established enzymology knowledge (appears in structural and mechanistic literature on amino acid biosynthesis), not an item-specific database annotation.",
    "reason": "A model with general enzymology knowledge can trace: Rossmann fold → EC 1.x; aldehyde dehydrogenase Cys motif → EC 1.2.1.x; 'NCSTAG' specificity → EC 1.2.1.11. The distractors span different EC classes/subclasses (2.1.1.394 is a transferase; 1.5.1.38 acts on CH-NH), making them eliminable by class-level reasoning. The remaining distinction between 1.2.1.11 and 1.2.1.101 rests on the well-known 'NCSTAG' family signature rather than a single-protein database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 'NCSTAG' catalytic motif, the Rossmann fold, the ~365-aa length, and the NADP-binding context collectively point to EC 1.2.1.11. The other three options belong to different EC classes or subclasses and lack the diagnostic semialdehyde dehydrogenase active-site architecture. No alternative option is defensible given the sequence features."
  },
  "important_caveats": [
    "The EC 1.2.1.11 annotation is supported by direct experimental evidence (ECO:0000269) including X-ray crystallography and multiple biochemical assays, not merely computational transfer.",
    "The 'NCSTAG' motif recognition is a family-level enzymology signature; a model unfamiliar with ASADH active-site architecture might struggle to distinguish 1.2.1.11 from 1.2.1.101 without database lookup, though the broader class/subclass elimination of C and D is straightforward.",
    "The sequence is from Candida albicans (fungal ASADH); the reviewer evidence confirms the sequence matches Q5ALM0 exactly (SHA-256 match, 365 aa)."
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

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"commonName":"Yeast","evidences":[{"evidenceCode":"ECO:0000312","id":"UP000000559","source":"Proteomes"}],"lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Saccharomycotina","Pichiomycetes","Debaryomycetaceae","Candida/Lodderomyces clade","Candida"],"scientificName":"Candida albicans (strain SC5314 / ATCC MYA-2876)","taxonId":237561}
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

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/references/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"citation":{"authors":["Arachea B.T.","Liu X.","Pavlovsky A.G.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"20124701"},{"database":"DOI","id":"10.1107/s0907444909052834"}],"citationType":"journal article","firstPage":"205","id":"20124701","journal":"Acta Crystallogr. D","lastPage":"212","publicationDate":"2010","title":"Expansion of the aspartate beta-semialdehyde dehydrogenase family: the first structure of a fungal ortholog.","volume":"66"},"evidences":[{"evidenceCode":"ECO:0007744","id":"3HSK","source":"PDB"}],"referenceNumber":8,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH NADP(+)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT"]}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
ID   DHAS_CANAL              Reviewed;         365 AA.
AC   Q5ALM0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   26-APR-2005, sequence version 1.
DT   18-JUN-2025, entry version 145.
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};
DE   AltName: Full=CaASADH {ECO:0000303|PubMed:17419877};
GN   Name=HOM2 {ECO:0000303|PubMed:17419877};
GN   OrderedLocusNames=CAALFM_C202370CA {ECO:0000312|EMBL:AOW27277.1},
GN   orf19.9132 {ECO:0000312|CGD:CAL0000179646};
OS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;
OC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.
OX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 101. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
