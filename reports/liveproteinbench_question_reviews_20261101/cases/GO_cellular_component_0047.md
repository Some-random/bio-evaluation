# GO_cellular_component_0047

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — cytosol

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASGARYAGKVVVVTGAARGIGAGIARAFVDSGAQVVICDKDERGGRALEQELRGAVFIRCDVTREEDVRALLSDTVHRFGRLDCVVNNAGSHPPLQPLEETTAQGFRELLELNLLGTYTLCKLAFPHLRRSRGNIINISTLVGAVGQLQGVPYAATKGAVTALTKALALDESQYGVRVNCISPGNIWTPLWQELAALAPDPRAAIREGAMAQPLGRMGQPAEVGAAAVFLASEASFCTGLELFVTGGAELGSGPENFFRSLGLCVVPEDVPPPTSRPRICSYK

[Multiple Choices]
A. cytosol
B. eukaryotic translation elongation factor 1 complex
C. plasmodesma
D. aggresome
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

> The exact sequence matches the rabbit UniProt entry, which annotates it to cytosol (GO:0005829) with ISS evidence. This supports the key as a database annotation, but ISS indicates inference by sequence similarity rather than direct experimental localization evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble oxidoreductase, including an N-terminal glycine-rich dinucleotide-binding region, and has no obvious transmembrane segment or organelle-targeting signal. That favors cytosol over a specific translation-factor complex, a plant plasmodesma, or an aggresome.


**Missing item-specific fact**

> The specific protein's cytosolic localization annotation is not supplied; the reviewer-only matched UniProt record provides it.


**Reason**

> Although the sequence cannot establish localization with certainty, its soluble-enzyme features and the nature of the alternatives provide a meaningful biological basis for favoring cytosol without relying on recognition of the exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options differ substantially in biological specificity, and the sequence supports a soluble enzyme rather than the particular complex, plant structure, or aggregation compartment.


### Important caveats

- The supporting GO annotation uses ISS evidence and should not be described as direct experimental localization.
- The sequence match is exact in the cited current and historical UniProt records; the author's actual source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble oxidoreductase, including an N-terminal glycine-rich dinucleotide-binding region, and has no obvious transmembrane segment or organelle-targeting signal. That favors cytosol over a specific translation-factor complex, a plant plasmodesma, or an aggresome.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific protein's cytosolic localization annotation is not supplied; the reviewer-only matched UniProt record provides it.",
    "reason": "Although the sequence cannot establish localization with certainty, its soluble-enzyme features and the nature of the alternatives provide a meaningful biological basis for favoring cytosol without relying on recognition of the exact protein."
  },
  "case_id": "GO_cellular_component_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the rabbit UniProt entry, which annotates it to cytosol (GO:0005829) with ISS evidence. This supports the key as a database annotation, but ISS indicates inference by sequence similarity rather than direct experimental localization evidence."
  },
  "important_caveats": [
    "The supporting GO annotation uses ISS evidence and should not be described as direct experimental localization.",
    "The sequence match is exact in the cited current and historical UniProt records; the author's actual source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options differ substantially in biological specificity, and the sequence supports a soluble enzyme rather than the particular complex, plant structure, or aggregation compartment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the rabbit UniProt entry, which annotates it to cytosol (GO:0005829) with ISS evidence. This supports the key as a database annotation, but ISS indicates inference by sequence similarity rather than direct experimental localization evidence.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble oxidoreductase, including an N-terminal glycine-rich dinucleotide-binding region, and has no obvious transmembrane segment or organelle-targeting signal. That favors cytosol over a specific translation-factor complex, a plant plasmodesma, or an aggresome.",
    "missing_item_specific_fact": "The specific protein's cytosolic localization annotation is not supplied; the reviewer-only matched UniProt record provides it.",
    "reason": "Although the sequence cannot establish localization with certainty, its soluble-enzyme features and the nature of the alternatives provide a meaningful biological basis for favoring cytosol without relying on recognition of the exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options differ substantially in biological specificity, and the sequence supports a soluble enzyme rather than the particular complex, plant structure, or aggregation compartment."
  },
  "important_caveats": [
    "The supporting GO annotation uses ISS evidence and should not be described as direct experimental localization.",
    "The sequence match is exact in the cited current and historical UniProt records; the author's actual source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAT9JA24 (L-fucose dehydrogenase / HSD17B14, rabbit) carries GO:0005829 (cytosol) with evidence code ISS:UniProtKB (Inferred from Sequence or Structural Similarity). This computational annotation matches the expected answer. However, the evidence is purely inferential (ISS), not experimental. The N-terminal sequence (MASGARYAGKVVVVTGAARGIGAGIARAFVDSGAQVVICDKDERGGRALEQELRGAVFIRCDVTREEDVRALLSDTVHRFGRLDCVVNNAGSHPPLQPLEETTAQGFRELLELNLLGTYTLCKLAFPHLRRSRGNIINISTLVGAVGQLQGVPYAATKGAVTALTKALALDESQYGVRVNCISPGNIWTPLWQELAALAPDPRAAIREGAMAQPLGRMGQPAEVGAAAVFLASEASFCTGLELFVTGGAELGSGPENFFRSLGLCVVPEDVPPPTSRPRICSYK) contains features suggestive of a mitochondrial targeting presequence (N-terminal Ser/Thr/Arg-rich, acidic-residue-poor region), and HSD17B14 is widely reported in the literature as a mitochondrial SDR enzyme. The 2024 Witecka et al. paper is cited for identification, function, catalytic activity, and biophysical properties but not for subcellular localization. Thus the annotation is a database-level inference that may not reflect the true compartment, but it does match the expected answer.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is a 284-aa mammalian (rabbit) short-chain dehydrogenase/reductase (SDR) enzyme (L-fucose dehydrogenase, EC 1.1.1.122). Option B (eukaryotic translation elongation factor 1 complex) is a multi-subunit nucleotide-exchange complex for tRNA delivery to the ribosome — the sequence bears no resemblance to eEF1A/B/D/G subunits and is a dehydrogenase, not a GTPase or translation factor. Option C (plasmodesma) is a plant-specific cytoplasmic channel; the organism is a rabbit (Oryctolagus cuniculus), making this impossible. Option D (aggresome) is a dynein-dependent pathological inclusion body formed from aggregated proteins — a normal, properly folding enzyme is not constitutively an aggresome component. By straightforward elimination of three clearly incompatible options, A (cytosol) is the only remaining plausible compartment for a soluble mammalian enzyme.


**Missing item-specific fact**

> The true subcellular localization of HSD17B14 (mitochondrial vs. cytosolic) is not determinable from the sequence alone without a mitochondrial targeting prediction tool or experimental data. The N-terminal MTS-like features could mislead a model toward 'mitochondrion,' which is not offered. The ISS annotation's correctness is an item-specific database fact.


**Reason**

> The elimination of B, C, and D relies on general biological knowledge (organism is not a plant; the protein is a dehydrogenase, not a translation factor; aggresomes are pathological structures). This is a valid reasoning path that does not require memorizing a specific database entry. However, the positive selection of 'cytosol' over 'mitochondrion' (the likely true compartment) is not achievable by reasoning from the sequence alone; it defaults to cytosol only because mitochondrion is absent from the options. The question is answerable by elimination but the 'correct' answer may not reflect the true biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are unambiguously incompatible with a rabbit SDR-family dehydrogenase (wrong protein class, wrong kingdom, wrong biological context respectively). Only A remains as a plausible compartment. No genuine ambiguity exists among the four choices, even though the true localization may be mitochondrial (not offered).


### Important caveats

- The GO annotation for cytosol carries ISS (Inferred from Sequence or Structural Similarity) evidence, not experimental evidence. It is a computational inference that may be incorrect.
- HSD17B14 is widely reported as a mitochondrial enzyme in the literature, and the N-terminal sequence contains features consistent with a mitochondrial targeting presequence. The 'cytosol' annotation may be a database error propagated by similarity-based inference.
- The true correct answer (mitochondrion) is not among the choices, making 'cytosol' the 'least wrong' option rather than a biologically accurate one.
- The 2024 Witecka et al. paper (PMID:38944119) is cited for function and catalytic activity but not for subcellular localization, so no experimental localization evidence is present in the reviewer sources.
- The sequence identity is confirmed (SHA-256 match) between the benchmark input and UniProt A0AAT9JA24, sequence version 2.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a 284-aa mammalian (rabbit) short-chain dehydrogenase/reductase (SDR) enzyme (L-fucose dehydrogenase, EC 1.1.1.122). Option B (eukaryotic translation elongation factor 1 complex) is a multi-subunit nucleotide-exchange complex for tRNA delivery to the ribosome — the sequence bears no resemblance to eEF1A/B/D/G subunits and is a dehydrogenase, not a GTPase or translation factor. Option C (plasmodesma) is a plant-specific cytoplasmic channel; the organism is a rabbit (Oryctolagus cuniculus), making this impossible. Option D (aggresome) is a dynein-dependent pathological inclusion body formed from aggregated proteins — a normal, properly folding enzyme is not constitutively an aggresome component. By straightforward elimination of three clearly incompatible options, A (cytosol) is the only remaining plausible compartment for a soluble mammalian enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The true subcellular localization of HSD17B14 (mitochondrial vs. cytosolic) is not determinable from the sequence alone without a mitochondrial targeting prediction tool or experimental data. The N-terminal MTS-like features could mislead a model toward 'mitochondrion,' which is not offered. The ISS annotation's correctness is an item-specific database fact.",
    "reason": "The elimination of B, C, and D relies on general biological knowledge (organism is not a plant; the protein is a dehydrogenase, not a translation factor; aggresomes are pathological structures). This is a valid reasoning path that does not require memorizing a specific database entry. However, the positive selection of 'cytosol' over 'mitochondrion' (the likely true compartment) is not achievable by reasoning from the sequence alone; it defaults to cytosol only because mitochondrion is absent from the options. The question is answerable by elimination but the 'correct' answer may not reflect the true biology."
  },
  "case_id": "GO_cellular_component_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAT9JA24 (L-fucose dehydrogenase / HSD17B14, rabbit) carries GO:0005829 (cytosol) with evidence code ISS:UniProtKB (Inferred from Sequence or Structural Similarity). This computational annotation matches the expected answer. However, the evidence is purely inferential (ISS), not experimental. The N-terminal sequence (MASGARYAGKVVVVTGAARGIGAGIARAFVDSGAQVVICDKDERGGRALEQELRGAVFIRCDVTREEDVRALLSDTVHRFGRLDCVVNNAGSHPPLQPLEETTAQGFRELLELNLLGTYTLCKLAFPHLRRSRGNIINISTLVGAVGQLQGVPYAATKGAVTALTKALALDESQYGVRVNCISPGNIWTPLWQELAALAPDPRAAIREGAMAQPLGRMGQPAEVGAAAVFLASEASFCTGLELFVTGGAELGSGPENFFRSLGLCVVPEDVPPPTSRPRICSYK) contains features suggestive of a mitochondrial targeting presequence (N-terminal Ser/Thr/Arg-rich, acidic-residue-poor region), and HSD17B14 is widely reported in the literature as a mitochondrial SDR enzyme. The 2024 Witecka et al. paper is cited for identification, function, catalytic activity, and biophysical properties but not for subcellular localization. Thus the annotation is a database-level inference that may not reflect the true compartment, but it does match the expected answer."
  },
  "important_caveats": [
    "The GO annotation for cytosol carries ISS (Inferred from Sequence or Structural Similarity) evidence, not experimental evidence. It is a computational inference that may be incorrect.",
    "HSD17B14 is widely reported as a mitochondrial enzyme in the literature, and the N-terminal sequence contains features consistent with a mitochondrial targeting presequence. The 'cytosol' annotation may be a database error propagated by similarity-based inference.",
    "The true correct answer (mitochondrion) is not among the choices, making 'cytosol' the 'least wrong' option rather than a biologically accurate one.",
    "The 2024 Witecka et al. paper (PMID:38944119) is cited for function and catalytic activity but not for subcellular localization, so no experimental localization evidence is present in the reviewer sources.",
    "The sequence identity is confirmed (SHA-256 match) between the benchmark input and UniProt A0AAT9JA24, sequence version 2."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are unambiguously incompatible with a rabbit SDR-family dehydrogenase (wrong protein class, wrong kingdom, wrong biological context respectively). Only A remains as a plausible compartment. No genuine ambiguity exists among the four choices, even though the true localization may be mitochondrial (not offered)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAT9JA24 (L-fucose dehydrogenase / HSD17B14, rabbit) carries GO:0005829 (cytosol) with evidence code ISS:UniProtKB (Inferred from Sequence or Structural Similarity). This computational annotation matches the expected answer. However, the evidence is purely inferential (ISS), not experimental. The N-terminal sequence (MASGARYAGKVVVVTGAARGIGAGIARAFVDSGAQVVICDKDERGGRALEQELRGAVFIRCDVTREEDVRALLSDTVHRFGRLDCVVNNAGSHPPLQPLEETTAQGFRELLELNLLGTYTLCKLAFPHLRRSRGNIINISTLVGAVGQLQGVPYAATKGAVTALTKALALDESQYGVRVNCISPGNIWTPLWQELAALAPDPRAAIREGAMAQPLGRMGQPAEVGAAAVFLASEASFCTGLELFVTGGAELGSGPENFFRSLGLCVVPEDVPPPTSRPRICSYK) contains features suggestive of a mitochondrial targeting presequence (N-terminal Ser/Thr/Arg-rich, acidic-residue-poor region), and HSD17B14 is widely reported in the literature as a mitochondrial SDR enzyme. The 2024 Witecka et al. paper is cited for identification, function, catalytic activity, and biophysical properties but not for subcellular localization. Thus the annotation is a database-level inference that may not reflect the true compartment, but it does match the expected answer.",
    "evidence_ids": ["C5", "H3", "C4", "C6", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is a 284-aa mammalian (rabbit) short-chain dehydrogenase/reductase (SDR) enzyme (L-fucose dehydrogenase, EC 1.1.1.122). Option B (eukaryotic translation elongation factor 1 complex) is a multi-subunit nucleotide-exchange complex for tRNA delivery to the ribosome — the sequence bears no resemblance to eEF1A/B/D/G subunits and is a dehydrogenase, not a GTPase or translation factor. Option C (plasmodesma) is a plant-specific cytoplasmic channel; the organism is a rabbit (Oryctolagus cuniculus), making this impossible. Option D (aggresome) is a dynein-dependent pathological inclusion body formed from aggregated proteins — a normal, properly folding enzyme is not constitutively an aggresome component. By straightforward elimination of three clearly incompatible options, A (cytosol) is the only remaining plausible compartment for a soluble mammalian enzyme.",
    "missing_item_specific_fact": "The true subcellular localization of HSD17B14 (mitochondrial vs. cytosolic) is not determinable from the sequence alone without a mitochondrial targeting prediction tool or experimental data. The N-terminal MTS-like features could mislead a model toward 'mitochondrion,' which is not offered. The ISS annotation's correctness is an item-specific database fact.",
    "reason": "The elimination of B, C, and D relies on general biological knowledge (organism is not a plant; the protein is a dehydrogenase, not a translation factor; aggresomes are pathological structures). This is a valid reasoning path that does not require memorizing a specific database entry. However, the positive selection of 'cytosol' over 'mitochondrion' (the likely true compartment) is not achievable by reasoning from the sequence alone; it defaults to cytosol only because mitochondrion is absent from the options. The question is answerable by elimination but the 'correct' answer may not reflect the true biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are unambiguously incompatible with a rabbit SDR-family dehydrogenase (wrong protein class, wrong kingdom, wrong biological context respectively). Only A remains as a plausible compartment. No genuine ambiguity exists among the four choices, even though the true localization may be mitochondrial (not offered)."
  },
  "important_caveats": [
    "The GO annotation for cytosol carries ISS (Inferred from Sequence or Structural Similarity) evidence, not experimental evidence. It is a computational inference that may be incorrect.",
    "HSD17B14 is widely reported as a mitochondrial enzyme in the literature, and the N-terminal sequence contains features consistent with a mitochondrial targeting presequence. The 'cytosol' annotation may be a database error propagated by similarity-based inference.",
    "The true correct answer (mitochondrion) is not among the choices, making 'cytosol' the 'least wrong' option rather than a biologically accurate one.",
    "The 2024 Witecka et al. paper (PMID:38944119) is cited for function and catalytic activity but not for subcellular localization, so no experimental localization evidence is present in the reviewer sources.",
    "The sequence identity is confirmed (SHA-256 match) between the benchmark input and UniProt A0AAT9JA24, sequence version 2."
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

**Accession:** `A0AAT9JA24` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
"A0AAT9JA24"
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Hydroxysteroid 17-beta dehydrogenase 14"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"value":"1.1.1.122"}],"fullName":{"value":"L-fucose dehydrogenase"}}}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"database":"GO","id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"citation":{"authors":["Witecka A.","Kazak V.","Kwiatkowski S.","Kiersztan A.","Jagielski A.K.","Kozminski W.","Augustyniak R.","Drozak J."],"citationCrossReferences":[{"database":"PubMed","id":"38944119"},{"database":"DOI","id":"10.1016/j.jbc.2024.107501"}],"citationType":"journal article","firstPage":"107501","id":"38944119","journal":"J. Biol. Chem.","lastPage":"107501","publicationDate":"2024","title":"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway.","volume":"300"},"referenceNumber":2,"referencePositions":["IDENTIFICATION","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF TYR-154"]}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 35-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
RN   [2]
RP   IDENTIFICATION, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL
RP   PROPERTIES, AND MUTAGENESIS OF TYR-154.
RX   PubMed=38944119; DOI=10.1016/j.jbc.2024.107501;
RA   Witecka A., Kazak V., Kwiatkowski S., Kiersztan A., Jagielski A.K.,
RA   Kozminski W., Augustyniak R., Drozak J.;
RT   "Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose
RT   dehydrogenase, the initial enzyme of the L-fucose degradation pathway.";
RL   J. Biol. Chem. 300:107501-107501(2024).
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 102-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; ISS:UniProtKB.
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 47. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
