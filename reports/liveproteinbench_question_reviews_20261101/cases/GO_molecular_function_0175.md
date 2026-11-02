# GO_molecular_function_0175

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — nucleoside transmembrane transporter activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLKGGTAAPAPMAPPRKWYDMTSAEFYVYVVAFMCGISIMMPINAVFSAPSYMLEYYLYATKDPFLVPKMTNFWTNVMTYYNLISMVTSLVVEPLTLLKSFRKIPMLVRLLGGLSVLIIEIIVLMVVPARGTTEAGAVATMCIAGFIGGLGTSIFESTVYGMFGAFPPSFTSIMMGGVGISGVLTSLIQIIVKAALPDTYEGVKKQSYIYYSLDVGIQAATFIALIMMRFNSFAQLHFGDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLAERELSEEESGDSRAVEAAGEAPTSNEILRATSVFSVLRSVKWMFVACGFNFLITLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRFSSAFRITWPRRYNQRWIIVAASFARVIFVPLLLLHSYHYIPSEAYGYVMQVVFGLSSGYIASMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRETY

[Multiple Choices]
A. DNA-binding transcription activator activity
B. nucleoside transmembrane transporter activity
C. RNA polymerase II transcription regulatory region sequence-specific DNA binding
D. cardiolipin synthase (CMP-forming)
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

> The supplied sequence exactly matches the reviewed Crithidia fasciculata nucleoside transporter entry. That entry reports experimentally supported nucleoside transport, including adenosine transport, and assigns the matching GO term. This supports B for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C11](#evidence-c11), [H5](#evidence-h5), [H11](#evidence-h11).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments suggest a multipass membrane protein and make the transcription-related choices poor fits, but that feature alone does not establish nucleoside transport over another membrane-protein function such as cardiolipin synthesis.


**Missing item-specific fact**

> The protein's specific family identity or experimentally established substrate/function is needed to distinguish nucleoside transport from the other membrane-associated option.


**Reason**

> The reviewer evidence supports B, but the model input supplies only the sequence and choices. Generic topology is not sufficiently specific to establish the transported substrate or reliably exclude the membrane-enzyme distractor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-specific annotation and experimental evidence support B; no other listed option is supported by the supplied reviewer evidence.


### Important caveats

- The experimental annotation and accession match are reviewer-only evidence, not information supplied to the evaluated model.
- The sequence's multipass topology supports a membrane-protein inference but does not by itself prove nucleoside specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments suggest a multipass membrane protein and make the transcription-related choices poor fits, but that feature alone does not establish nucleoside transport over another membrane-protein function such as cardiolipin synthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific family identity or experimentally established substrate/function is needed to distinguish nucleoside transport from the other membrane-associated option.",
    "reason": "The reviewer evidence supports B, but the model input supplies only the sequence and choices. Generic topology is not sufficiently specific to establish the transported substrate or reliably exclude the membrane-enzyme distractor."
  },
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C11",
      "H5",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Crithidia fasciculata nucleoside transporter entry. That entry reports experimentally supported nucleoside transport, including adenosine transport, and assigns the matching GO term. This supports B for this sequence."
  },
  "important_caveats": [
    "The experimental annotation and accession match are reviewer-only evidence, not information supplied to the evaluated model.",
    "The sequence's multipass topology supports a membrane-protein inference but does not by itself prove nucleoside specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-specific annotation and experimental evidence support B; no other listed option is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Crithidia fasciculata nucleoside transporter entry. That entry reports experimentally supported nucleoside transport, including adenosine transport, and assigns the matching GO term. This supports B for this sequence.",
    "evidence_ids": ["C1", "C5", "C6", "C11", "H5", "H11"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments suggest a multipass membrane protein and make the transcription-related choices poor fits, but that feature alone does not establish nucleoside transport over another membrane-protein function such as cardiolipin synthesis.",
    "missing_item_specific_fact": "The protein's specific family identity or experimentally established substrate/function is needed to distinguish nucleoside transport from the other membrane-associated option.",
    "reason": "The reviewer evidence supports B, but the model input supplies only the sequence and choices. Generic topology is not sufficiently specific to establish the transported substrate or reliably exclude the membrane-enzyme distractor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-specific annotation and experimental evidence support B; no other listed option is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The experimental annotation and accession match are reviewer-only evidence, not information supplied to the evaluated model.",
    "The sequence's multipass topology supports a membrane-protein inference but does not by itself prove nucleoside specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9GTP5 (NT1_CRIFA) is experimentally characterized (ECO:0000269, direct assay) as 'Nucleoside transporter 1' (CfNT1) from Crithidia fasciculata. The FUNCTION comment states it is a 'nucleoside transporter with broad substrate specificity' transporting adenosine, hypoxanthine, inosine, uridine, and cytidine across membranes. Multiple catalytic activity entries (adenosine(in)=adenosine(out), etc.) confirm transmembrane nucleoside transport. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (497 AA, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The provided 497-residue sequence contains approximately 11-12 hydrophobic segments consistent with multi-pass transmembrane domains, characteristic of membrane transporters (e.g., the equilibrative nucleoside transporter family). Options A (DNA-binding transcription activator) and C (RNA Pol II regulatory region DNA binding) describe soluble nuclear transcription-factor functions requiring DNA-binding domains (zinc fingers, helix-turn-helix, etc.) and nuclear localization signals—features entirely absent from this sequence. Option D (cardiolipin synthase, CMP-forming) is a transferase enzyme, typically a single-pass or peripheral membrane protein with specific catalytic motifs, not a multi-pass integral membrane protein. Only option B (nucleoside transmembrane transporter activity) is consistent with the observed multi-pass transmembrane architecture, making it the sole viable choice through general protein-architecture reasoning.


**Missing item-specific fact**

> None critical. While recognizing the specific ENT-family nucleoside transporter signature (vs. other transporter families) would require specialized knowledge, the question's option set contains only one transporter function, so the multi-pass TM architecture alone suffices to eliminate A, C, and D.


**Reason**

> The transmembrane topology of the sequence provides a concrete, general biological argument: a protein with ~11 TM helices cannot be a DNA-binding transcription factor or a soluble transferase enzyme. This eliminates three of four options without needing to identify the exact protein family. The remaining option B is the only transmembrane transporter function listed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different protein classes (transcription factor, membrane transporter, DNA-binding regulatory protein, transferase enzyme). The multi-pass transmembrane architecture of the sequence unambiguously points to a transporter, and only one option (B) describes a transmembrane transporter activity. No other option is defensible given the sequence architecture.


### Important caveats

- The GO annotation GO:0005337 carries evidence code IEA:InterPro (computational transfer), but the underlying function is experimentally validated via ECO:0000269 (direct assay) from three independent studies (PubMed:15694482, 20037157, 24120444).
- The protein is from Crithidia fasciculata, a trypanosomatid parasite; nucleoside transporters are well-studied in this organism due to their inability to synthesize purines de novo.
- Option D (cardiolipin synthase CMP-forming) has no matching GO term in the supplied ontology candidates, but this does not affect the reasoning since the sequence architecture already excludes it.
- The identity of the protein (Q9GTP5) was inferred from reviewer-only metadata absent from the model input; however, the sequence-architecture reasoning does not depend on this identification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The provided 497-residue sequence contains approximately 11-12 hydrophobic segments consistent with multi-pass transmembrane domains, characteristic of membrane transporters (e.g., the equilibrative nucleoside transporter family). Options A (DNA-binding transcription activator) and C (RNA Pol II regulatory region DNA binding) describe soluble nuclear transcription-factor functions requiring DNA-binding domains (zinc fingers, helix-turn-helix, etc.) and nuclear localization signals—features entirely absent from this sequence. Option D (cardiolipin synthase, CMP-forming) is a transferase enzyme, typically a single-pass or peripheral membrane protein with specific catalytic motifs, not a multi-pass integral membrane protein. Only option B (nucleoside transmembrane transporter activity) is consistent with the observed multi-pass transmembrane architecture, making it the sole viable choice through general protein-architecture reasoning.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While recognizing the specific ENT-family nucleoside transporter signature (vs. other transporter families) would require specialized knowledge, the question's option set contains only one transporter function, so the multi-pass TM architecture alone suffices to eliminate A, C, and D.",
    "reason": "The transmembrane topology of the sequence provides a concrete, general biological argument: a protein with ~11 TM helices cannot be a DNA-binding transcription factor or a soluble transferase enzyme. This eliminates three of four options without needing to identify the exact protein family. The remaining option B is the only transmembrane transporter function listed."
  },
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9GTP5 (NT1_CRIFA) is experimentally characterized (ECO:0000269, direct assay) as 'Nucleoside transporter 1' (CfNT1) from Crithidia fasciculata. The FUNCTION comment states it is a 'nucleoside transporter with broad substrate specificity' transporting adenosine, hypoxanthine, inosine, uridine, and cytidine across membranes. Multiple catalytic activity entries (adenosine(in)=adenosine(out), etc.) confirm transmembrane nucleoside transport. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (497 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The GO annotation GO:0005337 carries evidence code IEA:InterPro (computational transfer), but the underlying function is experimentally validated via ECO:0000269 (direct assay) from three independent studies (PubMed:15694482, 20037157, 24120444).",
    "The protein is from Crithidia fasciculata, a trypanosomatid parasite; nucleoside transporters are well-studied in this organism due to their inability to synthesize purines de novo.",
    "Option D (cardiolipin synthase CMP-forming) has no matching GO term in the supplied ontology candidates, but this does not affect the reasoning since the sequence architecture already excludes it.",
    "The identity of the protein (Q9GTP5) was inferred from reviewer-only metadata absent from the model input; however, the sequence-architecture reasoning does not depend on this identification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different protein classes (transcription factor, membrane transporter, DNA-binding regulatory protein, transferase enzyme). The multi-pass transmembrane architecture of the sequence unambiguously points to a transporter, and only one option (B) describes a transmembrane transporter activity. No other option is defensible given the sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9GTP5 (NT1_CRIFA) is experimentally characterized (ECO:0000269, direct assay) as 'Nucleoside transporter 1' (CfNT1) from Crithidia fasciculata. The FUNCTION comment states it is a 'nucleoside transporter with broad substrate specificity' transporting adenosine, hypoxanthine, inosine, uridine, and cytidine across membranes. Multiple catalytic activity entries (adenosine(in)=adenosine(out), etc.) confirm transmembrane nucleoside transport. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (497 AA, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The provided 497-residue sequence contains approximately 11-12 hydrophobic segments consistent with multi-pass transmembrane domains, characteristic of membrane transporters (e.g., the equilibrative nucleoside transporter family). Options A (DNA-binding transcription activator) and C (RNA Pol II regulatory region DNA binding) describe soluble nuclear transcription-factor functions requiring DNA-binding domains (zinc fingers, helix-turn-helix, etc.) and nuclear localization signals—features entirely absent from this sequence. Option D (cardiolipin synthase, CMP-forming) is a transferase enzyme, typically a single-pass or peripheral membrane protein with specific catalytic motifs, not a multi-pass integral membrane protein. Only option B (nucleoside transmembrane transporter activity) is consistent with the observed multi-pass transmembrane architecture, making it the sole viable choice through general protein-architecture reasoning.",
    "missing_item_specific_fact": "None critical. While recognizing the specific ENT-family nucleoside transporter signature (vs. other transporter families) would require specialized knowledge, the question's option set contains only one transporter function, so the multi-pass TM architecture alone suffices to eliminate A, C, and D.",
    "reason": "The transmembrane topology of the sequence provides a concrete, general biological argument: a protein with ~11 TM helices cannot be a DNA-binding transcription factor or a soluble transferase enzyme. This eliminates three of four options without needing to identify the exact protein family. The remaining option B is the only transmembrane transporter function listed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different protein classes (transcription factor, membrane transporter, DNA-binding regulatory protein, transferase enzyme). The multi-pass transmembrane architecture of the sequence unambiguously points to a transporter, and only one option (B) describes a transmembrane transporter activity. No other option is defensible given the sequence architecture."
  },
  "important_caveats": [
    "The GO annotation GO:0005337 carries evidence code IEA:InterPro (computational transfer), but the underlying function is experimentally validated via ECO:0000269 (direct assay) from three independent studies (PubMed:15694482, 20037157, 24120444).",
    "The protein is from Crithidia fasciculata, a trypanosomatid parasite; nucleoside transporters are well-studied in this organism due to their inability to synthesize purines de novo.",
    "Option D (cardiolipin synthase CMP-forming) has no matching GO term in the supplied ontology candidates, but this does not affect the reasoning since the sequence architecture already excludes it.",
    "The identity of the protein (Q9GTP5) was inferred from reviewer-only metadata absent from the model input; however, the sequence-architecture reasoning does not depend on this identification."
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

**Accession:** `Q9GTP5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 57. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
"Q9GTP5"
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"15694482","source":"PubMed"}],"value":"Nucleoside transporter 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"15694482","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"20037157","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"24120444","source":"PubMed"}],"value":"CfNT1"}]}}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"15694482","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"20037157","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24120444","source":"PubMed"}],"value":"Nucleoside transporter with broad substrate specificity (PubMed:15694482). Transports adenosine with high affinity (PubMed:15694482, PubMed:20037157, PubMed:24120444). Can also transport hypoxanthine, inosine, uridine and cytidine (PubMed:15694482)"}]}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"15694482","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"20037157","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24120444","source":"PubMed"}],"name":"adenosine(in) = adenosine(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:75343"},{"database":"ChEBI","id":"CHEBI:16335"}]}}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"15694482","source":"PubMed"}],"name":"hypoxanthine(out) = hypoxanthine(in)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:71515"},{"database":"ChEBI","id":"CHEBI:17368"}]}}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"15694482","source":"PubMed"}],"name":"inosine(in) = inosine(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:75375"},{"database":"ChEBI","id":"CHEBI:17596"}]}}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"15694482","source":"PubMed"}],"name":"uridine(out) = uridine(in)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:71519"},{"database":"ChEBI","id":"CHEBI:16704"}]}}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"15694482","source":"PubMed"}],"name":"cytidine(in) = cytidine(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:75367"},{"database":"ChEBI","id":"CHEBI:17562"}]}}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"database":"GO","id":"GO:0005337","properties":[{"key":"GoTerm","value":"F:nucleoside transmembrane transporter activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"citation":{"authors":["Liu W.","Arendt C.S.","Gessford S.K.","Ntaba D.","Carter N.S.","Ullman B."],"citationCrossReferences":[{"database":"PubMed","id":"15694482"},{"database":"DOI","id":"10.1016/j.molbiopara.2004.11.018"}],"citationType":"journal article","firstPage":"1","id":"15694482","journal":"Mol. Biochem. Parasitol.","lastPage":"12","publicationDate":"2005","title":"Identification and characterization of purine nucleoside transporters from Crithidia fasciculata.","volume":"140"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","TRANSPORTER ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","INDUCTION BY PUFINE STARVATION"]}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"citation":{"authors":["Arendt C.S.","Ullman B."],"citationCrossReferences":[{"database":"PubMed","id":"20037157"},{"database":"DOI","id":"10.1074/jbc.m109.074351"}],"citationType":"journal article","firstPage":"6024","id":"20037157","journal":"J. Biol. Chem.","lastPage":"6035","publicationDate":"2010","title":"Role of transmembrane domain 4 in ligand permeation by Crithidia fasciculata equilibrative nucleoside transporter 2 (CfNT2).","volume":"285"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","TRANSPORTER ACTIVITY","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"citation":{"authors":["Arendt C.S."],"citationCrossReferences":[{"database":"PubMed","id":"24120444"},{"database":"DOI","id":"10.1016/j.molbiopara.2013.09.007"}],"citationType":"journal article","firstPage":"75","id":"24120444","journal":"Mol. Biochem. Parasitol.","lastPage":"79","publicationDate":"2013","title":"Crithidia fasciculata adenosine transporter 1 (CfAT1), a novel high-affinity equilibrative nucleoside transporter specific for adenosine.","volume":"191"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","TRANSPORTER ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF THR-153"]}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 41-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
CC   -!- FUNCTION: Nucleoside transporter with broad substrate specificity
CC       (PubMed:15694482). Transports adenosine with high affinity
CC       (PubMed:15694482, PubMed:20037157, PubMed:24120444). Can also transport
CC       hypoxanthine, inosine, uridine and cytidine (PubMed:15694482).
CC       {ECO:0000269|PubMed:15694482, ECO:0000269|PubMed:20037157,
CC       ECO:0000269|PubMed:24120444}.
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 47-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=adenosine(in) = adenosine(out); Xref=Rhea:RHEA:75343,
CC         ChEBI:CHEBI:16335; Evidence={ECO:0000269|PubMed:15694482,
CC         ECO:0000269|PubMed:20037157, ECO:0000269|PubMed:24120444};
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 51-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=hypoxanthine(out) = hypoxanthine(in); Xref=Rhea:RHEA:71515,
CC         ChEBI:CHEBI:17368; Evidence={ECO:0000269|PubMed:15694482};
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 54-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=inosine(in) = inosine(out); Xref=Rhea:RHEA:75375,
CC         ChEBI:CHEBI:17596; Evidence={ECO:0000269|PubMed:15694482};
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 57-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=uridine(out) = uridine(in); Xref=Rhea:RHEA:71519,
CC         ChEBI:CHEBI:16704; Evidence={ECO:0000269|PubMed:15694482};
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 60-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=cytidine(in) = cytidine(out); Xref=Rhea:RHEA:75367,
CC         ChEBI:CHEBI:17562; Evidence={ECO:0000269|PubMed:15694482};
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 86-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
DR   GO; GO:0005337; F:nucleoside transmembrane transporter activity; IEA:InterPro.
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 55843-55864`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005337
name: nucleoside transmembrane transporter activity
namespace: molecular_function
def: "Enables the transfer of a nucleoside, a nucleobase linked to either beta-D-ribofuranose (ribonucleoside) or 2-deoxy-beta-D-ribofuranose, (a deoxyribonucleotide) from one side of a membrane to the other." [GOC:ai]
synonym: "intracellular nucleoside transmembrane transporter activity" NARROW []
xref: Reactome:R-HSA-109527 "Equilibrative transport (import) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 2"
xref: Reactome:R-HSA-109529 "Equilibrative transport (export) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 2"
xref: Reactome:R-HSA-109534 "Equilibrative transport (export) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 1"
xref: Reactome:R-HSA-109536 "Equilibrative transport (import) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 1"
xref: Reactome:R-HSA-5628807 "Defective SLC29A3 does not transport nucleosides from lysosomal lumen to cytosol"
xref: Reactome:R-HSA-727740 "Equilibrative transport (import) of adenosine and biogenic amines by solute carrier family 29 (nucleoside transporters), member 4"
xref: Reactome:R-HSA-727749 "SLC29A3 transports nucleosides from lysosomal lumen to cytosol"
xref: Reactome:R-HSA-727767 "SLC29A3 transports nucleosides from cytosol to lysosomal lumen"
xref: Reactome:R-HSA-727768 "Equilibrative transport (export) of adenosine and biogenic amines by solute carrier family 29 (nucleoside transporters), member 4"
xref: Reactome:R-HSA-9751024 "SLC29A1,2 transport 6MP from extracellular region to cytosol"
xref: Reactome:R-HSA-9754929 "SLC29A3 transports RBV,RBV-TP from cytosol to mitochondrial matrix"
xref: Reactome:R-HSA-9755015 "SLC29A1 transports RBV from extracellular region to cytosol"
xref: Reactome:R-HSA-9755035 "SLC29A1 transports RBV from cytosol to extracellular region"
is_a: GO:0015932 ! nucleobase-containing compound transmembrane transporter activity
is_a: GO:1901505 ! carbohydrate derivative transmembrane transporter activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 175. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
