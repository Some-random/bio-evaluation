# GO_biological_process_0003

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — alkaloid metabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAATDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNDMGCFTYPLVPGFETVGTATEVGSKVTKVKVGDKVAVGIMVGSCGKCDECVNDRECYCPEVITSYGRIDHDGTPTYGGFSSETVANEKFVFCFPEKLPMAAGAPLLNAGVSVYSAMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSTSKKGEAINDLGADAFLVSTDAEQMQAGSGTLDGILDTVPVVHPIEALLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVVSTIGGSTKETQEMLDFAAEHDITASVEIIPMDYVNTAMERIEKGDVRYRFVIDIGNTLTPPES

[Multiple Choices]
A. positive regulation of bone mineralization
B. alkaloid metabolic process
C. venom-mediated fibrinolysis
D. cellular response to topologically incorrect protein
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the annotated 363-aa protein. Its UniProt function and pathway annotations describe an enzyme in ajmaline-type alkaloid biosynthesis, supported by cited experimental evidence, which fits alkaloid metabolic process. The GO annotation itself is computationally assigned, but the functional evidence supports the process.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme, but generic sequence features do not identify its particular substrate or its role in alkaloid biosynthesis rather than another process.


**Missing item-specific fact**

> The protein-specific functional identification: this enzyme catalyzes a reaction in ajmaline-type monoterpenoid indole alkaloid biosynthesis.


**Reason**

> Distinguishing B requires information about the identity or experimentally characterized function of this specific protein that is not supplied by the sequence and choices alone. Remembering or retrieving its annotation would be lookup, not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supported alkaloid-biosynthesis role directly fits B; the other options describe processes unsupported by the evidence.


### Important caveats

- The UniProt function and pathway entries cite experimental evidence; the GO:0009820 annotation is marked IEA, so the GO annotation itself is computational rather than direct experimental evidence.
- The reviewer-only sequence match and annotations establish support for auditing but were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but generic sequence features do not identify its particular substrate or its role in alkaloid biosynthesis rather than another process.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification: this enzyme catalyzes a reaction in ajmaline-type monoterpenoid indole alkaloid biosynthesis.",
    "reason": "Distinguishing B requires information about the identity or experimentally characterized function of this specific protein that is not supplied by the sequence and choices alone. Remembering or retrieving its annotation would be lookup, not sequence-based reasoning."
  },
  "case_id": "GO_biological_process_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 363-aa protein. Its UniProt function and pathway annotations describe an enzyme in ajmaline-type alkaloid biosynthesis, supported by cited experimental evidence, which fits alkaloid metabolic process. The GO annotation itself is computationally assigned, but the functional evidence supports the process."
  },
  "important_caveats": [
    "The UniProt function and pathway entries cite experimental evidence; the GO:0009820 annotation is marked IEA, so the GO annotation itself is computational rather than direct experimental evidence.",
    "The reviewer-only sequence match and annotations establish support for auditing but were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported alkaloid-biosynthesis role directly fits B; the other options describe processes unsupported by the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 363-aa protein. Its UniProt function and pathway annotations describe an enzyme in ajmaline-type alkaloid biosynthesis, supported by cited experimental evidence, which fits alkaloid metabolic process. The GO annotation itself is computationally assigned, but the functional evidence supports the process.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but generic sequence features do not identify its particular substrate or its role in alkaloid biosynthesis rather than another process.",
    "missing_item_specific_fact": "The protein-specific functional identification: this enzyme catalyzes a reaction in ajmaline-type monoterpenoid indole alkaloid biosynthesis.",
    "reason": "Distinguishing B requires information about the identity or experimentally characterized function of this specific protein that is not supplied by the sequence and choices alone. Remembering or retrieving its annotation would be lookup, not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported alkaloid-biosynthesis role directly fits B; the other options describe processes unsupported by the evidence."
  },
  "important_caveats": [
    "The UniProt function and pathway entries cite experimental evidence; the GO:0009820 annotation is marked IEA, so the GO annotation itself is computational rather than direct experimental evidence.",
    "The reviewer-only sequence match and annotations establish support for auditing but were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0U3S9Q3 (1,2-Dihydrovomilenine reductase, RsDHVR) is experimentally characterized (ECO:0000269, PubMed:12391554, 26715562, 38212296) as an alcohol dehydrogenase in the ajmaline-type monoterpenoid indole alkaloid biosynthesis pathway. The pathway is explicitly annotated as 'Alkaloid biosynthesis; ajmaline biosynthesis.' The GO term GO:0009820 (alkaloid metabolic process) is assigned (IEA:UniProtKB-ARBA), and the underlying pathway evidence is experimental. The GO definition of GO:0009820 ('chemical reactions and pathways involving alkaloids') directly encompasses ajmaline biosynthesis. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Rossmann-fold-like NAD(P)-binding motif (GGLGGLGHLAVKF region) and overall architecture consistent with a short-chain alcohol dehydrogenase/reductase (SDR) or medium-chain dehydrogenase. This enzyme class is catalytic/metabolic. Among the four options: (A) positive regulation of bone mineralization involves transcription factors, matrix proteins, and signaling cascades in animals—not dehydrogenases; (C) venom-mediated fibrinolysis requires proteolytic activity (serine/metalloproteases), incompatible with a dehydrogenase fold; (D) cellular response to topologically incorrect protein involves chaperones, ERAD components, and ubiquitin ligases—not dehydrogenases. Only (B) alkaloid metabolic process is a metabolic/biosynthetic pathway that routinely employs dehydrogenases and reductases as catalytic steps. Thus, identifying the enzyme class eliminates A, C, and D by biochemical incompatibility.


**Missing item-specific fact**

> None strictly required among the four choices. The specific substrate identity (vomilenine/ajmaline pathway) would require database lookup, but is not needed to select B over A, C, or D given the enzyme-class argument.


**Reason**

> A model recognizing the dehydrogenase/reductase fold can reason that options A (animal signaling/regulation), C (protease-dependent), and D (chaperone/quality-control) are biochemically incompatible with a catalytic oxidoreductase, leaving B as the only metabolically consistent choice. This is general biological reasoning, not item-specific memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors are biochemically incompatible with a dehydrogenase/reductase enzyme class. No alternative among the choices is defensible for this protein type.


### Important caveats

- The GO annotation for this entry is IEA (inferred from electronic annotation via UniProtKB-ARBA), but the underlying pathway annotation is backed by experimental evidence (ECO:0000269 from three PubMed references).
- The protein is from Rauvolfia serpentina (a plant); recognizing plant origin from sequence alone is difficult, but the enzyme-class argument does not depend on species identification.
- The specific identification of 'alkaloid' vs. other metabolic pathways (e.g., terpenoid, amino acid) would require substrate knowledge, but this distinction is irrelevant among the four provided choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold-like NAD(P)-binding motif (GGLGGLGHLAVKF region) and overall architecture consistent with a short-chain alcohol dehydrogenase/reductase (SDR) or medium-chain dehydrogenase. This enzyme class is catalytic/metabolic. Among the four options: (A) positive regulation of bone mineralization involves transcription factors, matrix proteins, and signaling cascades in animals—not dehydrogenases; (C) venom-mediated fibrinolysis requires proteolytic activity (serine/metalloproteases), incompatible with a dehydrogenase fold; (D) cellular response to topologically incorrect protein involves chaperones, ERAD components, and ubiquitin ligases—not dehydrogenases. Only (B) alkaloid metabolic process is a metabolic/biosynthetic pathway that routinely employs dehydrogenases and reductases as catalytic steps. Thus, identifying the enzyme class eliminates A, C, and D by biochemical incompatibility.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required among the four choices. The specific substrate identity (vomilenine/ajmaline pathway) would require database lookup, but is not needed to select B over A, C, or D given the enzyme-class argument.",
    "reason": "A model recognizing the dehydrogenase/reductase fold can reason that options A (animal signaling/regulation), C (protease-dependent), and D (chaperone/quality-control) are biochemically incompatible with a catalytic oxidoreductase, leaving B as the only metabolically consistent choice. This is general biological reasoning, not item-specific memorization."
  },
  "case_id": "GO_biological_process_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H5",
      "H6",
      "H7",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U3S9Q3 (1,2-Dihydrovomilenine reductase, RsDHVR) is experimentally characterized (ECO:0000269, PubMed:12391554, 26715562, 38212296) as an alcohol dehydrogenase in the ajmaline-type monoterpenoid indole alkaloid biosynthesis pathway. The pathway is explicitly annotated as 'Alkaloid biosynthesis; ajmaline biosynthesis.' The GO term GO:0009820 (alkaloid metabolic process) is assigned (IEA:UniProtKB-ARBA), and the underlying pathway evidence is experimental. The GO definition of GO:0009820 ('chemical reactions and pathways involving alkaloids') directly encompasses ajmaline biosynthesis. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The GO annotation for this entry is IEA (inferred from electronic annotation via UniProtKB-ARBA), but the underlying pathway annotation is backed by experimental evidence (ECO:0000269 from three PubMed references).",
    "The protein is from Rauvolfia serpentina (a plant); recognizing plant origin from sequence alone is difficult, but the enzyme-class argument does not depend on species identification.",
    "The specific identification of 'alkaloid' vs. other metabolic pathways (e.g., terpenoid, amino acid) would require substrate knowledge, but this distinction is irrelevant among the four provided choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are biochemically incompatible with a dehydrogenase/reductase enzyme class. No alternative among the choices is defensible for this protein type."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U3S9Q3 (1,2-Dihydrovomilenine reductase, RsDHVR) is experimentally characterized (ECO:0000269, PubMed:12391554, 26715562, 38212296) as an alcohol dehydrogenase in the ajmaline-type monoterpenoid indole alkaloid biosynthesis pathway. The pathway is explicitly annotated as 'Alkaloid biosynthesis; ajmaline biosynthesis.' The GO term GO:0009820 (alkaloid metabolic process) is assigned (IEA:UniProtKB-ARBA), and the underlying pathway evidence is experimental. The GO definition of GO:0009820 ('chemical reactions and pathways involving alkaloids') directly encompasses ajmaline biosynthesis. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H5", "H6", "H7", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold-like NAD(P)-binding motif (GGLGGLGHLAVKF region) and overall architecture consistent with a short-chain alcohol dehydrogenase/reductase (SDR) or medium-chain dehydrogenase. This enzyme class is catalytic/metabolic. Among the four options: (A) positive regulation of bone mineralization involves transcription factors, matrix proteins, and signaling cascades in animals—not dehydrogenases; (C) venom-mediated fibrinolysis requires proteolytic activity (serine/metalloproteases), incompatible with a dehydrogenase fold; (D) cellular response to topologically incorrect protein involves chaperones, ERAD components, and ubiquitin ligases—not dehydrogenases. Only (B) alkaloid metabolic process is a metabolic/biosynthetic pathway that routinely employs dehydrogenases and reductases as catalytic steps. Thus, identifying the enzyme class eliminates A, C, and D by biochemical incompatibility.",
    "missing_item_specific_fact": "None strictly required among the four choices. The specific substrate identity (vomilenine/ajmaline pathway) would require database lookup, but is not needed to select B over A, C, or D given the enzyme-class argument.",
    "reason": "A model recognizing the dehydrogenase/reductase fold can reason that options A (animal signaling/regulation), C (protease-dependent), and D (chaperone/quality-control) are biochemically incompatible with a catalytic oxidoreductase, leaving B as the only metabolically consistent choice. This is general biological reasoning, not item-specific memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are biochemically incompatible with a dehydrogenase/reductase enzyme class. No alternative among the choices is defensible for this protein type."
  },
  "important_caveats": [
    "The GO annotation for this entry is IEA (inferred from electronic annotation via UniProtKB-ARBA), but the underlying pathway annotation is backed by experimental evidence (ECO:0000269 from three PubMed references).",
    "The protein is from Rauvolfia serpentina (a plant); recognizing plant origin from sequence alone is difficult, but the enzyme-class argument does not depend on species identification.",
    "The specific identification of 'alkaloid' vs. other metabolic pathways (e.g., terpenoid, amino acid) would require substrate knowledge, but this distinction is irrelevant among the four provided choices."
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

**Accession:** `A0A0U3S9Q3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
"A0A0U3S9Q3"
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Protein RR4"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsRR4"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Vomilenine reductase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsVR2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"12391554","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.3.1.73"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"1,2-Dihydrovomilenine reductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsDHVR"}]}}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"12391554","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alcohol dehydrogenase involved in the biosynthesis of ajmaline-type monoterpenoid indole alkaloids (MIAs) natural products, important plant-derived pharmaceuticals used in the therapy of heart disorders (PubMed:26715562, PubMed:38212296). Catalyzes the conversion of 1,2-dihydrovomilenine to 17-O-acetylnorajmaline, an intermediate chemical in the biosynthesis of ajmaline (PubMed:12391554, PubMed:26715562, PubMed:38212296). Also able, with a lower efficiency, to convert vomilenine into 19,20-dihydrovomilenine (PubMed:26715562, PubMed:38212296)"}]}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"12391554","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"database":"GO","id":"GO:0009820","properties":[{"key":"GoTerm","value":"P:alkaloid metabolic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-ARBA"}]}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)  
**Locator:** `lines 47-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:20.990872+00:00.  

```text
CC   -!- FUNCTION: Alcohol dehydrogenase involved in the biosynthesis of
CC       ajmaline-type monoterpenoid indole alkaloids (MIAs) natural products,
CC       important plant-derived pharmaceuticals used in the therapy of heart
CC       disorders (PubMed:26715562, PubMed:38212296). Catalyzes the conversion
CC       of 1,2-dihydrovomilenine to 17-O-acetylnorajmaline, an intermediate
CC       chemical in the biosynthesis of ajmaline (PubMed:12391554,
CC       PubMed:26715562, PubMed:38212296). Also able, with a lower efficiency,
CC       to convert vomilenine into 19,20-dihydrovomilenine (PubMed:26715562,
CC       PubMed:38212296). {ECO:0000269|PubMed:12391554,
CC       ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:20.990872+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:26715562,
CC       ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)  
**Locator:** `lines 130-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:20.990872+00:00.  

```text
DR   GO; GO:0009820; P:alkaloid metabolic process; IEA:UniProtKB-KW.
```

Source SHA-256: `d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 99940-99948`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009820
name: alkaloid metabolic process
namespace: biological_process
def: "The chemical reactions and pathways involving alkaloids, nitrogen containing natural products which are not otherwise classified as peptides, nonprotein amino acids, amines, cyanogenic glycosides, glucosinolates, cofactors, phytohormones or primary metabolites (such as purine or pyrimidine bases)." [GOC:lr, ISBN:0122146743]
subset: goslim_chembl
synonym: "alkaloid metabolism" EXACT []
is_a: GO:0008152 ! metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
