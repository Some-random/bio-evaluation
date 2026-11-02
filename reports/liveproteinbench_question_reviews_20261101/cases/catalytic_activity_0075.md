# catalytic_activity_0075

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTVKVKFPKDIREYARKEKVKDSLIKLTETALAEAISKFHRRMIVLQGDTLNKAKLAGILAGGAARILSEYIPEMLERKLRDTEQIEVLYATDALGEDTYGRKRFEEFRKHFSLLAPTAELTSVTFKHSRDILGRTFDILVIDLSYDYSPNDLGRIIETVRGGGLIFVLTNPFEKWKDMWTGFHKSLVTPPYTIEDVKKRFNRRLIRKFTEHKGIYIVNTDRMSIERKPGKYRSQATLPEREKVEIPKNIRFPRELYELCLTRGQVEVLKTLEELIEKEGMVVLTADRGRGKSVSIGIASVGLAVSSKKKRFRIVVTAPEPENVQSLMKFAKKSLEVLGYKTKVITDNGLIKEVYAKGIGIRYYPPTKGYRQRAELYIVDEAAGIHVPILHRYLEKERVVFSSTIHGYEGAGRGFSVKFLKKAKEKREYKEVHLSTPIRYAEGDPIEKWLFDVLLLDAEPVELTEEDYELIRKMEVYLEEPDLDDWFENDREDLRHFVGIYVLAHYRNRPSDVALLADAPHHEARVLRLKNGKIVTAIQIAKEGGIPKAVIDKMAKGYKPPGNIIPDMMVKHHYAKEFARLKGYRVVRIATHPDAMDMGLGSKALELLIKEAEEKGLDWVGSGFGASPELIRFWVRNGFAVVHLSPTRNPVSGEYTAIVIKPISEKAKEIVKKANEEFRIRLTEWLGDTHRDLEPEIARWLFESPFGEAVNYPIYLTKTQKRRLEMFIKRILTYDTVVDAVKPLVKLYFLDGWMRPYLDERQIMLLIHRVLQAHDWKETAKLLNRTEMYTMVELRDIVRGLWYYYKHLIKDEEGEK

[Multiple Choices]
A. cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)
B. 5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O
C. L-aspartate + ATP = 4-phospho-L-aspartate + ADP
D. uridine(out) = uridine(in)
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

> The supplied sequence exactly matches the 816-aa UniProt entry annotated as TmcA, a tRNA(Met) cytidine acetyltransferase, and that entry lists the reaction in choice A. The exact reaction annotation is computationally assigned by a HAMAP rule; separate cited evidence supports acetylation of cytidine in RNA more generally, but does not by itself establish the precise elongator-tRNA(Met) substrate.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme activities, but the sequence and prompt provide no context that meaningfully identifies this protein's specific substrate and reaction among them.


**Missing item-specific fact**

> The protein-specific identification as TmcA and its annotated catalytic reaction; recognizing the sequence or recalling its database entry would be lookup or memorization.


**Reason**

> A precise tRNA modification reaction cannot be inferred from the sequence alone by a general biological argument supplied in the question. The reviewer-only annotation supports the key but was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed reactions are chemically and functionally distinct, and the supplied evidence supports choice A for the matched protein.


### Important caveats

- The exact substrate-specific reaction annotation is supported by computational HAMAP evidence; the cited publication evidence in the supplied excerpts concerns cytidine acetylation in RNA more broadly.
- The source identity and exact sequence match are established by reviewer-only evidence, not by information provided in the original question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the sequence and prompt provide no context that meaningfully identifies this protein's specific substrate and reaction among them.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as TmcA and its annotated catalytic reaction; recognizing the sequence or recalling its database entry would be lookup or memorization.",
    "reason": "A precise tRNA modification reaction cannot be inferred from the sequence alone by a general biological argument supplied in the question. The reviewer-only annotation supports the key but was not available to the evaluated model."
  },
  "case_id": "catalytic_activity_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 816-aa UniProt entry annotated as TmcA, a tRNA(Met) cytidine acetyltransferase, and that entry lists the reaction in choice A. The exact reaction annotation is computationally assigned by a HAMAP rule; separate cited evidence supports acetylation of cytidine in RNA more generally, but does not by itself establish the precise elongator-tRNA(Met) substrate."
  },
  "important_caveats": [
    "The exact substrate-specific reaction annotation is supported by computational HAMAP evidence; the cited publication evidence in the supplied excerpts concerns cytidine acetylation in RNA more broadly.",
    "The source identity and exact sequence match are established by reviewer-only evidence, not by information provided in the original question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions are chemically and functionally distinct, and the supplied evidence supports choice A for the matched protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 816-aa UniProt entry annotated as TmcA, a tRNA(Met) cytidine acetyltransferase, and that entry lists the reaction in choice A. The exact reaction annotation is computationally assigned by a HAMAP rule; separate cited evidence supports acetylation of cytidine in RNA more generally, but does not by itself establish the precise elongator-tRNA(Met) substrate.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the sequence and prompt provide no context that meaningfully identifies this protein's specific substrate and reaction among them.",
    "missing_item_specific_fact": "The protein-specific identification as TmcA and its annotated catalytic reaction; recognizing the sequence or recalling its database entry would be lookup or memorization.",
    "reason": "A precise tRNA modification reaction cannot be inferred from the sequence alone by a general biological argument supplied in the question. The reviewer-only annotation supports the key but was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions are chemically and functionally distinct, and the supplied evidence supports choice A for the matched protein."
  },
  "important_caveats": [
    "The exact substrate-specific reaction annotation is supported by computational HAMAP evidence; the cited publication evidence in the supplied excerpts concerns cytidine acetylation in RNA more broadly.",
    "The source identity and exact sequence match are established by reviewer-only evidence, not by information provided in the original question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 816-aa sequence matches UniProt Q8U3G4 (TMCA_PYRFU) exactly (SHA256 confirmed). UniProt annotates this entry as 'tRNA(Met) cytidine acetyltransferase TmcA' (EC 2.3.1.193) with the catalytic reaction identical to Choice A. The primary annotation evidence is HAMAP-Rule (ECO:0000255, computational/curatorial), supplemented by experimental evidence from PubMed:32555463 (Sas-Chen et al., Nature 2020) supporting RNA acetylation activity broadly. The specific tRNA(Met) cytidine(34) acetylation is the canonical annotated function.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could argue that the 816-aa multi-domain architecture, the presence of P-loop/Walker A-like nucleotide-binding motifs (e.g., 'GDTLNKAKLAGILAGG'), and potential acetyl-CoA-binding regions might suggest an acetyltransferase that also binds ATP—a combination unusual among acetyltransferases and characteristic of the TmcA/NAT10 family. However, recognizing these motifs as specifically indicating a tRNA(Met) cytidine acetyltransferase (rather than a protein acetyltransferase, a histone acetyltransferase, or another RNA modification enzyme) requires knowledge of the specific domain architecture of the TmcA/NAT10 family. The GNAT fold or acetyltransferase-like motifs are shared across many unrelated acetyltransferases.


**Missing item-specific fact**

> The specific identification of this protein as a tRNA(Met) cytidine acetyltransferase (TmcA) rather than another acetyltransferase requires recognizing the particular combination of domains (acetyltransferase + nucleotide-binding + tRNA-binding) that defines the TmcA/NAT10 family, or knowing the database annotation for this specific archaeal protein. The ATP-dependence combined with acetyl-CoA usage is a family-specific trait not trivially deducible from sequence motifs alone.


**Reason**

> While the distractors B (purine biosynthesis phosphatase), C (aspartate kinase), and D (uridine transporter) are from entirely different enzyme classes and could potentially be excluded by noting the multi-domain size and lack of obvious transmembrane topology, positively identifying the enzyme as specifically a tRNA(Met) cytidine acetyltransferase from the sequence alone requires either recognizing the TmcA/NAT10 domain architecture or recalling the database annotation. General biological knowledge about acetyltransferase folds is insufficient to distinguish tRNA acetylation from protein or small-molecule acetylation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent entirely different enzyme classes (acetyltransferase, phosphatase, kinase, transporter). If the solver correctly identifies the enzyme as an acetyltransferase using both acetyl-CoA and ATP, Choice A is uniquely determined. The distractors are not plausible alternatives for a multi-domain 816-aa protein lacking obvious transmembrane segments. No ambiguity exists among the options once the enzyme class is identified.


### Important caveats

- The primary annotation evidence is HAMAP-Rule (ECO:0000255), a computational/curatorial inference based on sequence similarity, not direct experimental validation of this specific archaeal protein's tRNA(Met) specificity.
- The PubMed:32555463 experimental evidence (Sas-Chen et al., Nature 2020) demonstrates RNA acetylation activity broadly but was performed in human cells; direct experimental demonstration of tRNA(Met) cytidine(34) specificity in P. furiosus TmcA is not explicitly provided in the evidence excerpts.
- The sequence is from a hyperthermophilic archaeon; functional characterization of archaeal TmcA homologs may differ from eukaryotic NAT10/TmcA.
- The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the model sees only the raw sequence and choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could argue that the 816-aa multi-domain architecture, the presence of P-loop/Walker A-like nucleotide-binding motifs (e.g., 'GDTLNKAKLAGILAGG'), and potential acetyl-CoA-binding regions might suggest an acetyltransferase that also binds ATP—a combination unusual among acetyltransferases and characteristic of the TmcA/NAT10 family. However, recognizing these motifs as specifically indicating a tRNA(Met) cytidine acetyltransferase (rather than a protein acetyltransferase, a histone acetyltransferase, or another RNA modification enzyme) requires knowledge of the specific domain architecture of the TmcA/NAT10 family. The GNAT fold or acetyltransferase-like motifs are shared across many unrelated acetyltransferases.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this protein as a tRNA(Met) cytidine acetyltransferase (TmcA) rather than another acetyltransferase requires recognizing the particular combination of domains (acetyltransferase + nucleotide-binding + tRNA-binding) that defines the TmcA/NAT10 family, or knowing the database annotation for this specific archaeal protein. The ATP-dependence combined with acetyl-CoA usage is a family-specific trait not trivially deducible from sequence motifs alone.",
    "reason": "While the distractors B (purine biosynthesis phosphatase), C (aspartate kinase), and D (uridine transporter) are from entirely different enzyme classes and could potentially be excluded by noting the multi-domain size and lack of obvious transmembrane topology, positively identifying the enzyme as specifically a tRNA(Met) cytidine acetyltransferase from the sequence alone requires either recognizing the TmcA/NAT10 domain architecture or recalling the database annotation. General biological knowledge about acetyltransferase folds is insufficient to distinguish tRNA acetylation from protein or small-molecule acetylation."
  },
  "case_id": "catalytic_activity_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied 816-aa sequence matches UniProt Q8U3G4 (TMCA_PYRFU) exactly (SHA256 confirmed). UniProt annotates this entry as 'tRNA(Met) cytidine acetyltransferase TmcA' (EC 2.3.1.193) with the catalytic reaction identical to Choice A. The primary annotation evidence is HAMAP-Rule (ECO:0000255, computational/curatorial), supplemented by experimental evidence from PubMed:32555463 (Sas-Chen et al., Nature 2020) supporting RNA acetylation activity broadly. The specific tRNA(Met) cytidine(34) acetylation is the canonical annotated function."
  },
  "important_caveats": [
    "The primary annotation evidence is HAMAP-Rule (ECO:0000255), a computational/curatorial inference based on sequence similarity, not direct experimental validation of this specific archaeal protein's tRNA(Met) specificity.",
    "The PubMed:32555463 experimental evidence (Sas-Chen et al., Nature 2020) demonstrates RNA acetylation activity broadly but was performed in human cells; direct experimental demonstration of tRNA(Met) cytidine(34) specificity in P. furiosus TmcA is not explicitly provided in the evidence excerpts.",
    "The sequence is from a hyperthermophilic archaeon; functional characterization of archaeal TmcA homologs may differ from eukaryotic NAT10/TmcA.",
    "The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the model sees only the raw sequence and choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent entirely different enzyme classes (acetyltransferase, phosphatase, kinase, transporter). If the solver correctly identifies the enzyme as an acetyltransferase using both acetyl-CoA and ATP, Choice A is uniquely determined. The distractors are not plausible alternatives for a multi-domain 816-aa protein lacking obvious transmembrane segments. No ambiguity exists among the options once the enzyme class is identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 816-aa sequence matches UniProt Q8U3G4 (TMCA_PYRFU) exactly (SHA256 confirmed). UniProt annotates this entry as 'tRNA(Met) cytidine acetyltransferase TmcA' (EC 2.3.1.193) with the catalytic reaction identical to Choice A. The primary annotation evidence is HAMAP-Rule (ECO:0000255, computational/curatorial), supplemented by experimental evidence from PubMed:32555463 (Sas-Chen et al., Nature 2020) supporting RNA acetylation activity broadly. The specific tRNA(Met) cytidine(34) acetylation is the canonical annotated function.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could argue that the 816-aa multi-domain architecture, the presence of P-loop/Walker A-like nucleotide-binding motifs (e.g., 'GDTLNKAKLAGILAGG'), and potential acetyl-CoA-binding regions might suggest an acetyltransferase that also binds ATP—a combination unusual among acetyltransferases and characteristic of the TmcA/NAT10 family. However, recognizing these motifs as specifically indicating a tRNA(Met) cytidine acetyltransferase (rather than a protein acetyltransferase, a histone acetyltransferase, or another RNA modification enzyme) requires knowledge of the specific domain architecture of the TmcA/NAT10 family. The GNAT fold or acetyltransferase-like motifs are shared across many unrelated acetyltransferases.",
    "missing_item_specific_fact": "The specific identification of this protein as a tRNA(Met) cytidine acetyltransferase (TmcA) rather than another acetyltransferase requires recognizing the particular combination of domains (acetyltransferase + nucleotide-binding + tRNA-binding) that defines the TmcA/NAT10 family, or knowing the database annotation for this specific archaeal protein. The ATP-dependence combined with acetyl-CoA usage is a family-specific trait not trivially deducible from sequence motifs alone.",
    "reason": "While the distractors B (purine biosynthesis phosphatase), C (aspartate kinase), and D (uridine transporter) are from entirely different enzyme classes and could potentially be excluded by noting the multi-domain size and lack of obvious transmembrane topology, positively identifying the enzyme as specifically a tRNA(Met) cytidine acetyltransferase from the sequence alone requires either recognizing the TmcA/NAT10 domain architecture or recalling the database annotation. General biological knowledge about acetyltransferase folds is insufficient to distinguish tRNA acetylation from protein or small-molecule acetylation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent entirely different enzyme classes (acetyltransferase, phosphatase, kinase, transporter). If the solver correctly identifies the enzyme as an acetyltransferase using both acetyl-CoA and ATP, Choice A is uniquely determined. The distractors are not plausible alternatives for a multi-domain 816-aa protein lacking obvious transmembrane segments. No ambiguity exists among the options once the enzyme class is identified."
  },
  "important_caveats": [
    "The primary annotation evidence is HAMAP-Rule (ECO:0000255), a computational/curatorial inference based on sequence similarity, not direct experimental validation of this specific archaeal protein's tRNA(Met) specificity.",
    "The PubMed:32555463 experimental evidence (Sas-Chen et al., Nature 2020) demonstrates RNA acetylation activity broadly but was performed in human cells; direct experimental demonstration of tRNA(Met) cytidine(34) specificity in P. furiosus TmcA is not explicitly provided in the evidence excerpts.",
    "The sequence is from a hyperthermophilic archaeon; functional characterization of archaeal TmcA homologs may differ from eukaryotic NAT10/TmcA.",
    "The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the model sees only the raw sequence and choices."
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

**Accession:** `Q8U3G4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 122. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:29.260789+00:00.  

```json
"Q8U3G4"
```

Source SHA-256: `0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:29.260789+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"value":"2.3.1.193"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"value":"tRNA(Met) cytidine acetyltransferase TmcA"}}}
```

Source SHA-256: `0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:29.260789+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.193","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"name":"cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:43788"},{"database":"Rhea","id":"RHEA-COMP:10693"},{"database":"Rhea","id":"RHEA-COMP:10694"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:29.260789+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"name":"a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in RNA + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:82211"},{"database":"Rhea","id":"RHEA-COMP:15704"},{"database":"Rhea","id":"RHEA-COMP:19834"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:36.397993+00:00.  

```text
ID   TMCA_PYRFU              Reviewed;         816 AA.
AC   Q8U3G4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-2002, sequence version 1.
DT   28-JAN-2026, entry version 122.
DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};
DE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886};
GN   Name=tmcA {ECO:0000255|HAMAP-Rule:MF_01886};
GN   OrderedLocusNames=PF0504 {ECO:0000312|EMBL:AAL80628.1};
OS   Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1).
OC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;
OC   Thermococcaceae; Pyrococcus.
OX   NCBI_TaxID=186497;
```

Source SHA-256: `71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:36.397993+00:00.  

```text
DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};
DE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886};
```

Source SHA-256: `71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)  
**Locator:** `lines 23-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:36.397993+00:00.  

```text
RN   [2]
RP   FUNCTION.
RC   STRAIN=COM1;
RX   PubMed=32555463; DOI=10.1038/s41586-020-2418-2;
RA   Sas-Chen A., Thomas J.M., Matzov D., Taoka M., Nance K.D., Nir R.,
RA   Bryson K.M., Shachar R., Liman G.L.S., Burkhart B.W., Gamage S.T., Nobe Y.,
RA   Briney C.A., Levy M.J., Fuchs R.T., Robb G.B., Hartmann J., Sharma S.,
RA   Lin Q., Florens L., Washburn M.P., Isobe T., Santangelo T.J.,
RA   Shalev-Benami M., Meier J.L., Schwartz S.;
RT   "Dynamic RNA acetylation revealed by quantitative cross-evolutionary
RT   mapping.";
RL   Nature 583:638-643(2020).
```

Source SHA-256: `71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:36.397993+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O =
CC         N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate +
CC         CoA + H(+); Xref=Rhea:RHEA:43788, Rhea:RHEA-COMP:10693, Rhea:RHEA-
CC         COMP:10694, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         EC=2.3.1.193; Evidence={ECO:0000255|HAMAP-Rule:MF_01886};
```

Source SHA-256: `71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 75. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
