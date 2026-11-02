# GO_cellular_component_0108

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — host cell cytoplasm

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEDFVRQCFNPMIVELAEKAMKEYGEDPKIETNKFAAICTHLEVCFMYSDFHFIDERGESIIVESGDPNALLKHRFEIIEGRDRIMAWTVVNSICNTTGVEKPKFLPDLYDYKENRFIEIGVTRREVHIYYLEKANKIKSEKTHIHIFSFTGEEMATKADYTLDEESRARIKTRLFTIRQEMASRSLWDSFRQSERGEETIEEKFEITGTMRKLADQSLPPNFPSLENFRAYVDGFEPNGCIEGKLSQMSKEVNAKIEPFLRTTPRPLRLPDGPLCHQRSKFLLMDALKLSIEDPSHEGEGIPLYDAIKCMKTFFGWKEPNIVKPHEKGINPNYLMAWKQVLAELQDIENEEKIPRTKNMKRTSQLKWALGENMAPEKVDFDDCKDVGDLKQYDSDEPEPRSLASWVQNEFNKACELTDSSWIELDEIGEDVAPIEHIASMRRNYFTAEVSHCRATEYIMKGVYINTALLNASCAAMDDFQLIPMISKCRTKEGRRKTNLYGFIIKGRSHLRNDTDVVNFVSMEFSLTDPRLEPHKWEKYCVLEIGDMLLRTAIGQVSRPMFLYVRTNGTSKIKMKWGMEMRRCLLQSLQQIESMIEAESSVKEKDMTKEFFENKSETWPIGESPRGVEEGSIGKVCRTLLAKSVFNSLYASPQLEGFSAESRKLLLIVQALRDNLEPGTFDLGGLYEAIEECLINDPWVLLNASWFNSFLTHALK

[Multiple Choices]
A. egg coat
B. nematocyst
C. RQC complex
D. host cell cytoplasm
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches the influenza A virus polymerase acidic protein, and both current and archived UniProt records annotate it to the host cell cytoplasm. This is computational annotation (HAMAP/IEA), not direct experimental confirmation; the records also annotate host nucleus.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The viral-protein context makes egg coat, nematocyst, and the RQC complex poor fits, but the sequence alone does not establish host-cytoplasm localization over other compartments. Influenza polymerase localization depends on protein-specific biology, including its transport with PB1 into the nucleus.


**Missing item-specific fact**

> The identity and localization annotation of this exact influenza PA protein, including its host-cytoplasm annotation, are not supplied in the question.


**Reason**

> Choosing D requires a protein-specific localization fact or annotation; generic sequence features do not meaningfully distinguish cytoplasmic residence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only offered option supported by the cited annotation. However, the protein is also annotated to the host nucleus, which is not offered, so the wording asking for its primary location is not fully resolved by the choices.


### Important caveats

- The localization annotations are computationally assigned, not evidence of experimental measurement.
- The annotation supports host cytoplasm but does not establish that it is the protein's exclusive or primary location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The viral-protein context makes egg coat, nematocyst, and the RQC complex poor fits, but the sequence alone does not establish host-cytoplasm localization over other compartments. Influenza polymerase localization depends on protein-specific biology, including its transport with PB1 into the nucleus.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity and localization annotation of this exact influenza PA protein, including its host-cytoplasm annotation, are not supplied in the question.",
    "reason": "Choosing D requires a protein-specific localization fact or annotation; generic sequence features do not meaningfully distinguish cytoplasmic residence."
  },
  "case_id": "GO_cellular_component_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the influenza A virus polymerase acidic protein, and both current and archived UniProt records annotate it to the host cell cytoplasm. This is computational annotation (HAMAP/IEA), not direct experimental confirmation; the records also annotate host nucleus."
  },
  "important_caveats": [
    "The localization annotations are computationally assigned, not evidence of experimental measurement.",
    "The annotation supports host cytoplasm but does not establish that it is the protein's exclusive or primary location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered option supported by the cited annotation. However, the protein is also annotated to the host nucleus, which is not offered, so the wording asking for its primary location is not fully resolved by the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the influenza A virus polymerase acidic protein, and both current and archived UniProt records annotate it to the host cell cytoplasm. This is computational annotation (HAMAP/IEA), not direct experimental confirmation; the records also annotate host nucleus.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The viral-protein context makes egg coat, nematocyst, and the RQC complex poor fits, but the sequence alone does not establish host-cytoplasm localization over other compartments. Influenza polymerase localization depends on protein-specific biology, including its transport with PB1 into the nucleus.",
    "missing_item_specific_fact": "The identity and localization annotation of this exact influenza PA protein, including its host-cytoplasm annotation, are not supplied in the question.",
    "reason": "Choosing D requires a protein-specific localization fact or annotation; generic sequence features do not meaningfully distinguish cytoplasmic residence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered option supported by the cited annotation. However, the protein is also annotated to the host nucleus, which is not offered, so the wording asking for its primary location is not fully resolved by the choices."
  },
  "important_caveats": [
    "The localization annotations are computationally assigned, not evidence of experimental measurement.",
    "The annotation supports host cytoplasm but does not establish that it is the protein's exclusive or primary location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt C3W5S0 (Influenza A virus PA, Polymerase Acidic protein, 716 aa). UniProt annotates subcellular location as both 'Host cytoplasm' and 'Host nucleus' (HAMAP-Rule MF_04063, ECO:0000255), and the GO cross-reference GO:0030430 'host cell cytoplasm' (IEA:UniProtKB-SubCell) is present. The expected answer D is directly supported by the annotation. However, the protein is also annotated in host cell nucleus (GO:0042025), and the annotation evidence is purely computational (IEA/HAMAP-Rule), not experimental. Among the four provided options, D is the only one consistent with a viral polymerase protein; the other three (egg coat, nematocyst, RQC complex) are entirely irrelevant to influenza virus biology.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The three distractors are specific to entirely unrelated biological contexts: an egg coat (GO:0035805) is an extracellular matrix surrounding an ovum; a nematocyst (GO:0042151) is a stinging organelle in cnidarian cnidoblasts; the RQC complex (GO:1990112) is a ribosome-associated protein degradation complex. A 716-aa protein with polymerase-like sequence motifs (e.g., conserved acidic/charged regions, potential endonuclease motifs) cannot plausibly reside in any of these three compartments. By general biological reasoning about protein types and their expected localizations, all three distractors can be eliminated, leaving 'host cell cytoplasm' as the only compartment consistent with a viral protein that functions within a host cell. The positive identification does not require knowing the exact UniProt annotation.


**Missing item-specific fact**

> None that is strictly necessary to distinguish the choices. The very broad category 'host cell cytoplasm' vs. the three highly specific and biologically irrelevant alternatives can be resolved by general knowledge that viral proteins localize within host cells (cytoplasm and/or nucleus), not in cnidarian stinging organelles, oocyte extracellular matrices, or ribosome quality-control complexes.


**Reason**

> The distractors are so clearly inappropriate for a viral polymerase that general biological reasoning about protein function and compartment biology is sufficient to eliminate them. Recognizing the sequence as viral (large size, polymerase-like motifs, lack of eukaryotic targeting signals) and knowing that viral replication machinery operates in host cell compartments is general knowledge, not item-specific lookup. The question does not require identifying the exact accession or recalling a specific database entry to select the correct answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is annotated in both host cell cytoplasm and host cell nucleus, 'host cell nucleus' is not among the choices. The other three options (egg coat, nematocyst, RQC complex) are biologically incompatible with a viral polymerase. Only D is defensible.


### Important caveats

- The subcellular location annotation is purely computational (IEA:UniProtKB-SubCell, HAMAP-Rule MF_04063), not experimentally verified.
- The protein is annotated in both host cytoplasm and host nucleus; the question's choice set does not include 'host cell nucleus,' so the cytoplasm/nucleus distinction is not tested here.
- The extremely easy distractors (cnidarian organelle, oocyte extracellular matrix, ribosome quality-control complex) make the question trivially solvable by elimination, reducing its discriminative power for assessing GO-cellular-component prediction ability.
- The identity of the protein (Influenza A PA, C3W5S0) was inferred by the reviewer from dataset metadata and is not provided to the evaluated model; the model must work from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The three distractors are specific to entirely unrelated biological contexts: an egg coat (GO:0035805) is an extracellular matrix surrounding an ovum; a nematocyst (GO:0042151) is a stinging organelle in cnidarian cnidoblasts; the RQC complex (GO:1990112) is a ribosome-associated protein degradation complex. A 716-aa protein with polymerase-like sequence motifs (e.g., conserved acidic/charged regions, potential endonuclease motifs) cannot plausibly reside in any of these three compartments. By general biological reasoning about protein types and their expected localizations, all three distractors can be eliminated, leaving 'host cell cytoplasm' as the only compartment consistent with a viral protein that functions within a host cell. The positive identification does not require knowing the exact UniProt annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is strictly necessary to distinguish the choices. The very broad category 'host cell cytoplasm' vs. the three highly specific and biologically irrelevant alternatives can be resolved by general knowledge that viral proteins localize within host cells (cytoplasm and/or nucleus), not in cnidarian stinging organelles, oocyte extracellular matrices, or ribosome quality-control complexes.",
    "reason": "The distractors are so clearly inappropriate for a viral polymerase that general biological reasoning about protein function and compartment biology is sufficient to eliminate them. Recognizing the sequence as viral (large size, polymerase-like motifs, lack of eukaryotic targeting signals) and knowing that viral replication machinery operates in host cell compartments is general knowledge, not item-specific lookup. The question does not require identifying the exact accession or recalling a specific database entry to select the correct answer."
  },
  "case_id": "GO_cellular_component_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt C3W5S0 (Influenza A virus PA, Polymerase Acidic protein, 716 aa). UniProt annotates subcellular location as both 'Host cytoplasm' and 'Host nucleus' (HAMAP-Rule MF_04063, ECO:0000255), and the GO cross-reference GO:0030430 'host cell cytoplasm' (IEA:UniProtKB-SubCell) is present. The expected answer D is directly supported by the annotation. However, the protein is also annotated in host cell nucleus (GO:0042025), and the annotation evidence is purely computational (IEA/HAMAP-Rule), not experimental. Among the four provided options, D is the only one consistent with a viral polymerase protein; the other three (egg coat, nematocyst, RQC complex) are entirely irrelevant to influenza virus biology."
  },
  "important_caveats": [
    "The subcellular location annotation is purely computational (IEA:UniProtKB-SubCell, HAMAP-Rule MF_04063), not experimentally verified.",
    "The protein is annotated in both host cytoplasm and host nucleus; the question's choice set does not include 'host cell nucleus,' so the cytoplasm/nucleus distinction is not tested here.",
    "The extremely easy distractors (cnidarian organelle, oocyte extracellular matrix, ribosome quality-control complex) make the question trivially solvable by elimination, reducing its discriminative power for assessing GO-cellular-component prediction ability.",
    "The identity of the protein (Influenza A PA, C3W5S0) was inferred by the reviewer from dataset metadata and is not provided to the evaluated model; the model must work from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is annotated in both host cell cytoplasm and host cell nucleus, 'host cell nucleus' is not among the choices. The other three options (egg coat, nematocyst, RQC complex) are biologically incompatible with a viral polymerase. Only D is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt C3W5S0 (Influenza A virus PA, Polymerase Acidic protein, 716 aa). UniProt annotates subcellular location as both 'Host cytoplasm' and 'Host nucleus' (HAMAP-Rule MF_04063, ECO:0000255), and the GO cross-reference GO:0030430 'host cell cytoplasm' (IEA:UniProtKB-SubCell) is present. The expected answer D is directly supported by the annotation. However, the protein is also annotated in host cell nucleus (GO:0042025), and the annotation evidence is purely computational (IEA/HAMAP-Rule), not experimental. Among the four provided options, D is the only one consistent with a viral polymerase protein; the other three (egg coat, nematocyst, RQC complex) are entirely irrelevant to influenza virus biology.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The three distractors are specific to entirely unrelated biological contexts: an egg coat (GO:0035805) is an extracellular matrix surrounding an ovum; a nematocyst (GO:0042151) is a stinging organelle in cnidarian cnidoblasts; the RQC complex (GO:1990112) is a ribosome-associated protein degradation complex. A 716-aa protein with polymerase-like sequence motifs (e.g., conserved acidic/charged regions, potential endonuclease motifs) cannot plausibly reside in any of these three compartments. By general biological reasoning about protein types and their expected localizations, all three distractors can be eliminated, leaving 'host cell cytoplasm' as the only compartment consistent with a viral protein that functions within a host cell. The positive identification does not require knowing the exact UniProt annotation.",
    "missing_item_specific_fact": "None that is strictly necessary to distinguish the choices. The very broad category 'host cell cytoplasm' vs. the three highly specific and biologically irrelevant alternatives can be resolved by general knowledge that viral proteins localize within host cells (cytoplasm and/or nucleus), not in cnidarian stinging organelles, oocyte extracellular matrices, or ribosome quality-control complexes.",
    "reason": "The distractors are so clearly inappropriate for a viral polymerase that general biological reasoning about protein function and compartment biology is sufficient to eliminate them. Recognizing the sequence as viral (large size, polymerase-like motifs, lack of eukaryotic targeting signals) and knowing that viral replication machinery operates in host cell compartments is general knowledge, not item-specific lookup. The question does not require identifying the exact accession or recalling a specific database entry to select the correct answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is annotated in both host cell cytoplasm and host cell nucleus, 'host cell nucleus' is not among the choices. The other three options (egg coat, nematocyst, RQC complex) are biologically incompatible with a viral polymerase. Only D is defensible."
  },
  "important_caveats": [
    "The subcellular location annotation is purely computational (IEA:UniProtKB-SubCell, HAMAP-Rule MF_04063), not experimentally verified.",
    "The protein is annotated in both host cytoplasm and host nucleus; the question's choice set does not include 'host cell nucleus,' so the cytoplasm/nucleus distinction is not tested here.",
    "The extremely easy distractors (cnidarian organelle, oocyte extracellular matrix, ribosome quality-control complex) make the question trivially solvable by elimination, reducing its discriminative power for assessing GO-cellular-component prediction ability.",
    "The identity of the protein (Influenza A PA, C3W5S0) was inferred by the reviewer from dataset metadata and is not provided to the evaluated model; the model must work from the raw sequence alone."
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

**Accession:** `C3W5S0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 105. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C3W5S0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.548827+00:00.  

```json
"C3W5S0"
```

Source SHA-256: `41de97cb89c07354676a2d9a707a158e2cc4d809c3ea945287a37298998ef378`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C3W5S0.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.548827+00:00.  

```json
{"lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Polyploviricotina","Insthoviricetes","Articulavirales","Orthomyxoviridae","Alphainfluenzavirus","Alphainfluenzavirus influenzae","Influenza A virus"],"scientificName":"Influenza A virus (strain swl A/California/04/2009 H1N1)","taxonId":641501}
```

Source SHA-256: `41de97cb89c07354676a2d9a707a158e2cc4d809c3ea945287a37298998ef378`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C3W5S0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.548827+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_04063","source":"HAMAP-Rule"}],"value":"RNA-directed RNA polymerase subunit P2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_04063","source":"HAMAP-Rule"}],"value":"3.1.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_04063","source":"HAMAP-Rule"}],"value":"Polymerase acidic protein"}}}
```

Source SHA-256: `41de97cb89c07354676a2d9a707a158e2cc4d809c3ea945287a37298998ef378`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C3W5S0.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.548827+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_04063","source":"HAMAP-Rule"}],"value":"PB1 and PA are transported in the host nucleus as a complex"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_04063","source":"HAMAP-Rule"}],"id":"SL-0381","value":"Host cytoplasm"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_04063","source":"HAMAP-Rule"}],"id":"SL-0414","value":"Host nucleus"}}]}
```

Source SHA-256: `41de97cb89c07354676a2d9a707a158e2cc4d809c3ea945287a37298998ef378`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C3W5S0.json)  
**Locator:** `/uniProtKBCrossReferences/211`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.548827+00:00.  

```json
{"database":"GO","id":"GO:0030430","properties":[{"key":"GoTerm","value":"C:host cell cytoplasm"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `41de97cb89c07354676a2d9a707a158e2cc4d809c3ea945287a37298998ef378`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C3W5S0.json)  
**Locator:** `/uniProtKBCrossReferences/212`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.548827+00:00.  

```json
{"database":"GO","id":"GO:0042025","properties":[{"key":"GoTerm","value":"C:host cell nucleus"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `41de97cb89c07354676a2d9a707a158e2cc4d809c3ea945287a37298998ef378`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C3W5S0?format=txt&versions=105)  
**Locator:** `lines 189-192`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:27:30.499324+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Host cytoplasm {ECO:0000255|HAMAP-Rule:MF_04063}.
CC       Host nucleus {ECO:0000255|HAMAP-Rule:MF_04063}. Note=PB1 and PA are
CC       transported in the host nucleus as a complex. {ECO:0000255|HAMAP-
CC       Rule:MF_04063}.
```

Source SHA-256: `dd6527288091b8021cdd92a9500cb06cf91332794d3ed14c1592693b57498db5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C3W5S0?format=txt&versions=105)  
**Locator:** `lines 400-400`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:27:30.499324+00:00.  

```text
DR   GO; GO:0030430; C:host cell cytoplasm; IEA:UniProtKB-SubCell.
```

Source SHA-256: `dd6527288091b8021cdd92a9500cb06cf91332794d3ed14c1592693b57498db5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C3W5S0?format=txt&versions=105)  
**Locator:** `lines 401-401`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:27:30.499324+00:00.  

```text
DR   GO; GO:0042025; C:host cell nucleus; IEA:UniProtKB-SubCell.
```

Source SHA-256: `dd6527288091b8021cdd92a9500cb06cf91332794d3ed14c1592693b57498db5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
