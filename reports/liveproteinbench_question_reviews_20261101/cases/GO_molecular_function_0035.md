# GO_molecular_function_0035

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — endo-1,4-beta-xylanase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFSSLFVAACAAVTAFALPSELEKRAITTSQQGTSNGYFYSFWTNGGGSVSYNNGASGEYSVSWSNCGSFTSGKGWATGSSRNINFSGSFKPSGNAYLAVYGWTTSPLVEYYIMENYGDYNPGRSMTFKGTVTSDGSVYDIYTHQQVNQPSISGTATFEQYWSIRRTKRSSGTVTTANHFKAWASHGMYLGSHNYQIVSTEGYQSSGSSDITVS

[Multiple Choices]
A. double-stranded DNA endonuclease activity
B. iron-sulfur cluster binding
C. phosphorelay sensor kinase activity
D. endo-1,4-beta-xylanase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches a UniProt entry annotated as an endo-1,4-beta-xylanase. The catalytic-activity assignment and GO term are based on a PROSITE-ProRule/EC inference; the function text also cites similarity to another protein. The cited 2025 paper supports a biological role as a PAMP, but the excerpts do not establish that the xylan-hydrolysis activity itself was experimentally measured for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted fungal protein, and the sequence is unlike an obvious kinase, iron-sulfur protein, or DNA nuclease. That can make D plausible, but does not establish the precise xylanase activity.


**Missing item-specific fact**

> The protein-specific identification or annotation linking this exact sequence to endo-1,4-beta-xylanase activity is absent from the question.


**Reason**

> Selecting D over the distractors at the specific molecular-function level requires the sequence-specific functional annotation or equivalent experimental knowledge, not merely general sequence reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices name distinct activities, and the matched protein annotation supports D; no alternative listed activity is comparably supported by the evidence.


### Important caveats

- The reviewer-only accession and database evidence were not provided to the evaluated model.
- The author’s exact annotation snapshot is unknown, although a historical entry with the matching sequence was retrieved.
- The evidence supports the key through database annotation and computational inference; the excerpts do not independently verify xylan hydrolysis experimentally for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal protein, and the sequence is unlike an obvious kinase, iron-sulfur protein, or DNA nuclease. That can make D plausible, but does not establish the precise xylanase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification or annotation linking this exact sequence to endo-1,4-beta-xylanase activity is absent from the question.",
    "reason": "Selecting D over the distractors at the specific molecular-function level requires the sequence-specific functional annotation or equivalent experimental knowledge, not merely general sequence reasoning."
  },
  "case_id": "GO_molecular_function_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated as an endo-1,4-beta-xylanase. The catalytic-activity assignment and GO term are based on a PROSITE-ProRule/EC inference; the function text also cites similarity to another protein. The cited 2025 paper supports a biological role as a PAMP, but the excerpts do not establish that the xylan-hydrolysis activity itself was experimentally measured for this sequence."
  },
  "important_caveats": [
    "The reviewer-only accession and database evidence were not provided to the evaluated model.",
    "The author’s exact annotation snapshot is unknown, although a historical entry with the matching sequence was retrieved.",
    "The evidence supports the key through database annotation and computational inference; the excerpts do not independently verify xylan hydrolysis experimentally for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices name distinct activities, and the matched protein annotation supports D; no alternative listed activity is comparably supported by the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated as an endo-1,4-beta-xylanase. The catalytic-activity assignment and GO term are based on a PROSITE-ProRule/EC inference; the function text also cites similarity to another protein. The cited 2025 paper supports a biological role as a PAMP, but the excerpts do not establish that the xylan-hydrolysis activity itself was experimentally measured for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal protein, and the sequence is unlike an obvious kinase, iron-sulfur protein, or DNA nuclease. That can make D plausible, but does not establish the precise xylanase activity.",
    "missing_item_specific_fact": "The protein-specific identification or annotation linking this exact sequence to endo-1,4-beta-xylanase activity is absent from the question.",
    "reason": "Selecting D over the distractors at the specific molecular-function level requires the sequence-specific functional annotation or equivalent experimental knowledge, not merely general sequence reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices name distinct activities, and the matched protein annotation supports D; no alternative listed activity is comparably supported by the evidence."
  },
  "important_caveats": [
    "The reviewer-only accession and database evidence were not provided to the evaluated model.",
    "The author’s exact annotation snapshot is unknown, although a historical entry with the matching sequence was retrieved.",
    "The evidence supports the key through database annotation and computational inference; the excerpts do not independently verify xylan hydrolysis experimentally for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt Swiss-Prot entry K9GHZ3 (sequence SHA256 matched) annotates this protein as Ethylene-inducing xylanase (EIX) with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The EC assignment is supported by PROSITE-ProRule motif analysis (ECO:0000255), and the functional annotation is further supported by experimental evidence from PubMed:39718348 (ECO:0000269) demonstrating xylanase activity and PAMP function. The GO annotation itself is IEA:UniProtKB-EC (inferred from EC), but the underlying EC assignment and functional characterization are well-supported.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a clear N-terminal signal peptide (hydrophobic stretch MVSFSSLFVAACAAVTAFALPSE), indicating a secreted protein. At ~216 AA, it is far too small for a two-component sensor kinase (option C, which requires HATPase and HisKA domains, typically >500 AA transmembrane proteins). It lacks cysteine-rich Fe-S cluster motifs (option B requires CxxCP or similar Cys clusters; this protein has only one Cys). It lacks any DNA-binding domain or nuclease catalytic motifs (option A). The remaining profile—small, secreted, heavily O-glycosylated (Ser/Thr/Asn-rich), fungal origin—is consistent with a small secreted glycoside hydrolase such as a xylanase. Among the four options, only D is compatible with these structural and topological features.


**Missing item-specific fact**

> Positive identification as specifically a xylanase (rather than another small secreted fungal hydrolase such as a glucanase or protease) would require recognizing specific catalytic residues or fold motifs (e.g., GH11/GH10 conserved Glu pairs) that are not trivially identifiable from the raw sequence alone. However, among the four provided choices, elimination of A, B, C is sufficient to select D.


**Reason**

> The three distractors (A, B, C) are incompatible with the protein's size, subcellular topology (secreted vs. membrane/cytosolic), and domain architecture. A general biology reasoning approach can eliminate them. Option D is the only remaining choice consistent with a small secreted fungal enzyme. While the positive identification as a xylanase specifically (vs. another glycoside hydrolase) would benefit from motif-level recognition, the elimination argument among these four choices is biologically sound.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are clearly incompatible with the protein's size, secretion signal, and lack of relevant domains. Only D is consistent with the observed sequence features. No ambiguity among the four choices.


### Important caveats

- The GO annotation (GO:0031176) carries evidence code IEA:UniProtKB-EC, meaning it is inferred from the EC number rather than directly annotated. The EC number itself is assigned via PROSITE-ProRule (computational motif match, ECO:0000255), though the broader function is experimentally supported by PubMed:39718348.
- The sequence does not display easily recognizable GH11 or GH10 xylanase catalytic motifs at first glance; positive family assignment from sequence alone would require more detailed structural motif analysis or database comparison.
- The protein is a precursor (216 AA including signal peptide); the mature enzyme is shorter, which is typical for secreted xylanases.
- The reviewer evidence confirms sequence match (SHA256 identical) between the benchmark input and the UniProt entry K9GHZ3.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (hydrophobic stretch MVSFSSLFVAACAAVTAFALPSE), indicating a secreted protein. At ~216 AA, it is far too small for a two-component sensor kinase (option C, which requires HATPase and HisKA domains, typically >500 AA transmembrane proteins). It lacks cysteine-rich Fe-S cluster motifs (option B requires CxxCP or similar Cys clusters; this protein has only one Cys). It lacks any DNA-binding domain or nuclease catalytic motifs (option A). The remaining profile—small, secreted, heavily O-glycosylated (Ser/Thr/Asn-rich), fungal origin—is consistent with a small secreted glycoside hydrolase such as a xylanase. Among the four options, only D is compatible with these structural and topological features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification as specifically a xylanase (rather than another small secreted fungal hydrolase such as a glucanase or protease) would require recognizing specific catalytic residues or fold motifs (e.g., GH11/GH10 conserved Glu pairs) that are not trivially identifiable from the raw sequence alone. However, among the four provided choices, elimination of A, B, C is sufficient to select D.",
    "reason": "The three distractors (A, B, C) are incompatible with the protein's size, subcellular topology (secreted vs. membrane/cytosolic), and domain architecture. A general biology reasoning approach can eliminate them. Option D is the only remaining choice consistent with a small secreted fungal enzyme. While the positive identification as a xylanase specifically (vs. another glycoside hydrolase) would benefit from motif-level recognition, the elimination argument among these four choices is biologically sound."
  },
  "case_id": "GO_molecular_function_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt Swiss-Prot entry K9GHZ3 (sequence SHA256 matched) annotates this protein as Ethylene-inducing xylanase (EIX) with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The EC assignment is supported by PROSITE-ProRule motif analysis (ECO:0000255), and the functional annotation is further supported by experimental evidence from PubMed:39718348 (ECO:0000269) demonstrating xylanase activity and PAMP function. The GO annotation itself is IEA:UniProtKB-EC (inferred from EC), but the underlying EC assignment and functional characterization are well-supported."
  },
  "important_caveats": [
    "The GO annotation (GO:0031176) carries evidence code IEA:UniProtKB-EC, meaning it is inferred from the EC number rather than directly annotated. The EC number itself is assigned via PROSITE-ProRule (computational motif match, ECO:0000255), though the broader function is experimentally supported by PubMed:39718348.",
    "The sequence does not display easily recognizable GH11 or GH10 xylanase catalytic motifs at first glance; positive family assignment from sequence alone would require more detailed structural motif analysis or database comparison.",
    "The protein is a precursor (216 AA including signal peptide); the mature enzyme is shorter, which is typical for secreted xylanases.",
    "The reviewer evidence confirms sequence match (SHA256 identical) between the benchmark input and the UniProt entry K9GHZ3."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with the protein's size, secretion signal, and lack of relevant domains. Only D is consistent with the observed sequence features. No ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt Swiss-Prot entry K9GHZ3 (sequence SHA256 matched) annotates this protein as Ethylene-inducing xylanase (EIX) with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The EC assignment is supported by PROSITE-ProRule motif analysis (ECO:0000255), and the functional annotation is further supported by experimental evidence from PubMed:39718348 (ECO:0000269) demonstrating xylanase activity and PAMP function. The GO annotation itself is IEA:UniProtKB-EC (inferred from EC), but the underlying EC assignment and functional characterization are well-supported.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H3", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (hydrophobic stretch MVSFSSLFVAACAAVTAFALPSE), indicating a secreted protein. At ~216 AA, it is far too small for a two-component sensor kinase (option C, which requires HATPase and HisKA domains, typically >500 AA transmembrane proteins). It lacks cysteine-rich Fe-S cluster motifs (option B requires CxxCP or similar Cys clusters; this protein has only one Cys). It lacks any DNA-binding domain or nuclease catalytic motifs (option A). The remaining profile—small, secreted, heavily O-glycosylated (Ser/Thr/Asn-rich), fungal origin—is consistent with a small secreted glycoside hydrolase such as a xylanase. Among the four options, only D is compatible with these structural and topological features.",
    "missing_item_specific_fact": "Positive identification as specifically a xylanase (rather than another small secreted fungal hydrolase such as a glucanase or protease) would require recognizing specific catalytic residues or fold motifs (e.g., GH11/GH10 conserved Glu pairs) that are not trivially identifiable from the raw sequence alone. However, among the four provided choices, elimination of A, B, C is sufficient to select D.",
    "reason": "The three distractors (A, B, C) are incompatible with the protein's size, subcellular topology (secreted vs. membrane/cytosolic), and domain architecture. A general biology reasoning approach can eliminate them. Option D is the only remaining choice consistent with a small secreted fungal enzyme. While the positive identification as a xylanase specifically (vs. another glycoside hydrolase) would benefit from motif-level recognition, the elimination argument among these four choices is biologically sound."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with the protein's size, secretion signal, and lack of relevant domains. Only D is consistent with the observed sequence features. No ambiguity among the four choices."
  },
  "important_caveats": [
    "The GO annotation (GO:0031176) carries evidence code IEA:UniProtKB-EC, meaning it is inferred from the EC number rather than directly annotated. The EC number itself is assigned via PROSITE-ProRule (computational motif match, ECO:0000255), though the broader function is experimentally supported by PubMed:39718348.",
    "The sequence does not display easily recognizable GH11 or GH10 xylanase catalytic motifs at first glance; positive family assignment from sequence alone would require more detailed structural motif analysis or database comparison.",
    "The protein is a precursor (216 AA including signal peptide); the mature enzyme is shorter, which is typical for secreted xylanases.",
    "The reviewer evidence confirms sequence match (SHA256 identical) between the benchmark input and the UniProt entry K9GHZ3."
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

**Accession:** `K9GHZ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
"K9GHZ3"
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"Ethylene-inducing xylanase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"EIX"}]}}
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"B3VSG7","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"39718348","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (By similarity). Acts as a pathogen-associated molecular pattern (PAMP) that can trigger plant cell death (PubMed:39718348). Triggers a series of immune responses in citrus fruit and enhanced the resistance of citrus and other fruit against fungal pathogens (PubMed:39718348)"}]}
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
{"database":"GO","id":"GO:0031176","properties":[{"key":"GoTerm","value":"F:endo-1,4-beta-xylanase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-EC"}]}
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:29:01.625551+00:00.  

```text
ID   EIX_PEND1               Reviewed;         216 AA.
AC   K9GHZ3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   06-FEB-2013, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:39718348};
DE            Short=EIX {ECO:0000303|PubMed:39718348};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:39718348};
DE   Flags: Precursor;
GN   Name=EIX {ECO:0000303|PubMed:39718348}; ORFNames=PDIP_02920;
OS   Penicillium digitatum (strain Pd1 / CECT 20795) (Green mold).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=1170230;
```

Source SHA-256: `c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)  
**Locator:** `lines 32-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:29:01.625551+00:00.  

```text
CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a
CC       major structural heterogeneous polysaccharide found in plant biomass
CC       representing the second most abundant polysaccharide in the biosphere,
CC       after cellulose (By similarity). Acts as a pathogen-associated
CC       molecular pattern (PAMP) that can trigger plant cell death
CC       (PubMed:39718348). Triggers a series of immune responses in citrus
CC       fruit and enhanced the resistance of citrus and other fruit against
CC       fungal pathogens (PubMed:39718348). {ECO:0000250|UniProtKB:B3VSG7,
CC       ECO:0000269|PubMed:39718348}.
```

Source SHA-256: `c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)  
**Locator:** `lines 41-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:29:01.625551+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};
```

Source SHA-256: `c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)  
**Locator:** `lines 65-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:29:01.625551+00:00.  

```text
DR   GO; GO:0031176; F:endo-1,4-beta-xylanase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 173997-174018`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031176
name: endo-1,4-beta-xylanase activity
namespace: molecular_function
def: "Catalysis of the endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans." [EC:3.2.1.8]
synonym: "1,4-beta-D-xylan xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "1,4-beta-xylan xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "beta-1,4-xylan xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "beta-1,4-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "beta-D-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "beta-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "endo-(1,4)-beta-xylanase(1,4)-beta-xylan 4-xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "endo-(1->4)-beta-xylanase(1->4)-beta-xylan 4-xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "endo-1,4-beta-D-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "endo-1,4-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "endo-beta-1,4-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "xylanase" BROAD [EC:3.2.1.8]
xref: EC:3.2.1.8
xref: MetaCyc:3.2.1.8-RXN
is_a: GO:0097599 ! xylanase activity
property_value: skos:exactMatch EC:3.2.1.8

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 35. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
