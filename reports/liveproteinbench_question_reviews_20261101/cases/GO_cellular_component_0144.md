# GO_cellular_component_0144

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — other organism cell membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQLKKQLIVIFFTYFIVVNESEAFFGALFKLATKIIPSLFRKRKGREVMMKRDLEQLFDPYQRNLELDRLLKQLPNY

[Multiple Choices]
A. matrilin complex
B. other organism cell membrane
C. external side of plasma membrane
D. phosphopantothenoylcysteine decarboxylase complex
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

> The sequence-matched historical UniProt entry assigns GO:0044218, “other organism cell membrane,” to this protein. This is a keyword-based database annotation, not direct experimental proof of that specific GO term; the entry separately describes the protein as secreted and its location as the target cell membrane.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with secretion, and the basic short sequence is compatible with a secreted antimicrobial peptide. That may suggest interaction with microbial membranes, but it does not establish the protein’s specific target or distinguish a foreign cell membrane from the external side of a plasma membrane.


**Missing item-specific fact**

> The protein-specific fact that this scorpion peptide is secreted and associates with a target organism’s cell membrane, as reflected in the database annotation.


**Reason**

> The supplied sequence supports a broad secretion or membrane-interaction hypothesis, but selecting the specific cellular-component term requires protein-specific functional or annotation information absent from the prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The target-cell-membrane annotation supports B. If the peptide is attached to the extracellular-facing surface of that target’s plasma membrane, C may also describe its location; the prompt does not specify whether the intended term is the foreign membrane as a whole or its external-facing side.


### Important caveats

- The current and historical source records match the supplied sequence.
- The GO annotation for B is computationally assigned by UniProtKB-KW; the source’s target-cell-membrane location statement is not itself a GO annotation for B.
- The source also reports an experimentally supported secreted location, which is not one of the options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with secretion, and the basic short sequence is compatible with a secreted antimicrobial peptide. That may suggest interaction with microbial membranes, but it does not establish the protein’s specific target or distinguish a foreign cell membrane from the external side of a plasma membrane.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this scorpion peptide is secreted and associates with a target organism’s cell membrane, as reflected in the database annotation.",
    "reason": "The supplied sequence supports a broad secretion or membrane-interaction hypothesis, but selecting the specific cellular-component term requires protein-specific functional or annotation information absent from the prompt."
  },
  "case_id": "GO_cellular_component_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry assigns GO:0044218, “other organism cell membrane,” to this protein. This is a keyword-based database annotation, not direct experimental proof of that specific GO term; the entry separately describes the protein as secreted and its location as the target cell membrane."
  },
  "important_caveats": [
    "The current and historical source records match the supplied sequence.",
    "The GO annotation for B is computationally assigned by UniProtKB-KW; the source’s target-cell-membrane location statement is not itself a GO annotation for B.",
    "The source also reports an experimentally supported secreted location, which is not one of the options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The target-cell-membrane annotation supports B. If the peptide is attached to the extracellular-facing surface of that target’s plasma membrane, C may also describe its location; the prompt does not specify whether the intended term is the foreign membrane as a whole or its external-facing side."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry assigns GO:0044218, “other organism cell membrane,” to this protein. This is a keyword-based database annotation, not direct experimental proof of that specific GO term; the entry separately describes the protein as secreted and its location as the target cell membrane.",
    "evidence_ids": ["H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with secretion, and the basic short sequence is compatible with a secreted antimicrobial peptide. That may suggest interaction with microbial membranes, but it does not establish the protein’s specific target or distinguish a foreign cell membrane from the external side of a plasma membrane.",
    "missing_item_specific_fact": "The protein-specific fact that this scorpion peptide is secreted and associates with a target organism’s cell membrane, as reflected in the database annotation.",
    "reason": "The supplied sequence supports a broad secretion or membrane-interaction hypothesis, but selecting the specific cellular-component term requires protein-specific functional or annotation information absent from the prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The target-cell-membrane annotation supports B. If the peptide is attached to the extracellular-facing surface of that target’s plasma membrane, C may also describe its location; the prompt does not specify whether the intended term is the foreign membrane as a whole or its external-facing side."
  },
  "important_caveats": [
    "The current and historical source records match the supplied sequence.",
    "The GO annotation for B is computationally assigned by UniProtKB-KW; the source’s target-cell-membrane location statement is not itself a GO annotation for B.",
    "The source also reports an experimentally supported secreted location, which is not one of the options."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A059U8Y9) annotates GO:0044218 (other organism cell membrane) via IEA:UniProtKB-KW, derived from the subcellular location comment 'Target cell membrane' (ECO:0000305, curator inference). The protein is antimicrobial peptide megicin-18 from scorpion venom, experimentally shown (PubMed:29896190) to target Gram-positive bacterial membranes. The GO:0044218 annotation is electronic/inferred rather than directly experimental, but the underlying biology (AMP targeting foreign bacterial membranes) is well-supported by the bioassay data in the cited paper. The annotation is present in both current (C6 context, H6) and historical (entry version 9) records.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H3](#evidence-h3), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 77-aa sequence exhibits a hydrophobic N-terminal signal peptide (MQLKKQLIVIFFTYFIVVNESEAFFGALFKLATKIIPSLF...) followed by a short cationic amphipathic mature region (RKRKGREVMMKRDLEQLFDPYQRNLELDRLLKQLPNY), characteristic of a secreted antimicrobial peptide. General biological knowledge establishes that AMPs exert their function by targeting bacterial cell membranes. GO:0044218 'other organism cell membrane' is defined as the cell membrane of a secondary organism with which the first organism interacts, which precisely describes the bacterial target membrane of an AMP. Option C (external side of plasma membrane, GO:0009897) refers to the host cell's own membrane external leaflet, not a foreign organism's membrane, and is therefore distinguishable. Options A (cartilage matrilin complex) and D (CoA biosynthesis enzyme complex) are categorically incompatible with a small cationic venom peptide.


**Missing item-specific fact**

> None strictly required; the reasoning chain (signal peptide → secreted AMP → bacterial membrane target → 'other organism cell membrane') is accessible through general biological knowledge and GO term definitions.


**Reason**

> A knowledgeable model can eliminate A and D as functionally irrelevant, distinguish C (host's own membrane) from B (foreign organism's membrane) based on the biological role of antimicrobial peptides targeting bacterial membranes, and select B. The sequence features (small size, cationic amphipathic mature region, signal peptide) provide concrete grounds for identifying this as an AMP without memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B and C both involve membranes, the GO definitions clearly distinguish them: GO:0044218 refers to a foreign organism's membrane (the bacterial target), while GO:0009897 refers to the external leaflet of the protein-producing organism's own plasma membrane. An antimicrobial peptide does not reside on its host's external membrane surface; it is secreted and acts on bacterial membranes. A and D are categorically incompatible with the protein's identity.


### Important caveats

- The GO:0044218 annotation is IEA (inferred from electronic annotation via keyword mapping), not direct experimental evidence. The experimental evidence (ECO:0000269) supports 'Secreted' and 'extracellular region' (GO:0005576). The 'Target cell membrane' annotation is ECO:0000305 (curator inference).
- The sequence in the question is the full 77-aa precursor; the mature antimicrobial peptide corresponds to residues 24-41 per the reference. The signal peptide and propeptide are present in the supplied sequence.
- The GO term name 'other organism cell membrane' is somewhat non-intuitive; a model unfamiliar with this specific GO term nomenclature might struggle even with correct biological reasoning.
- The primary GO annotation in the current entry is GO:0005576 (extracellular region, EXP), which is not among the options. The question forces selection among four choices, none of which is the most directly experimentally supported annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 77-aa sequence exhibits a hydrophobic N-terminal signal peptide (MQLKKQLIVIFFTYFIVVNESEAFFGALFKLATKIIPSLF...) followed by a short cationic amphipathic mature region (RKRKGREVMMKRDLEQLFDPYQRNLELDRLLKQLPNY), characteristic of a secreted antimicrobial peptide. General biological knowledge establishes that AMPs exert their function by targeting bacterial cell membranes. GO:0044218 'other organism cell membrane' is defined as the cell membrane of a secondary organism with which the first organism interacts, which precisely describes the bacterial target membrane of an AMP. Option C (external side of plasma membrane, GO:0009897) refers to the host cell's own membrane external leaflet, not a foreign organism's membrane, and is therefore distinguishable. Options A (cartilage matrilin complex) and D (CoA biosynthesis enzyme complex) are categorically incompatible with a small cationic venom peptide.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; the reasoning chain (signal peptide → secreted AMP → bacterial membrane target → 'other organism cell membrane') is accessible through general biological knowledge and GO term definitions.",
    "reason": "A knowledgeable model can eliminate A and D as functionally irrelevant, distinguish C (host's own membrane) from B (foreign organism's membrane) based on the biological role of antimicrobial peptides targeting bacterial membranes, and select B. The sequence features (small size, cationic amphipathic mature region, signal peptide) provide concrete grounds for identifying this as an AMP without memorizing the specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "H6",
      "H3",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A059U8Y9) annotates GO:0044218 (other organism cell membrane) via IEA:UniProtKB-KW, derived from the subcellular location comment 'Target cell membrane' (ECO:0000305, curator inference). The protein is antimicrobial peptide megicin-18 from scorpion venom, experimentally shown (PubMed:29896190) to target Gram-positive bacterial membranes. The GO:0044218 annotation is electronic/inferred rather than directly experimental, but the underlying biology (AMP targeting foreign bacterial membranes) is well-supported by the bioassay data in the cited paper. The annotation is present in both current (C6 context, H6) and historical (entry version 9) records."
  },
  "important_caveats": [
    "The GO:0044218 annotation is IEA (inferred from electronic annotation via keyword mapping), not direct experimental evidence. The experimental evidence (ECO:0000269) supports 'Secreted' and 'extracellular region' (GO:0005576). The 'Target cell membrane' annotation is ECO:0000305 (curator inference).",
    "The sequence in the question is the full 77-aa precursor; the mature antimicrobial peptide corresponds to residues 24-41 per the reference. The signal peptide and propeptide are present in the supplied sequence.",
    "The GO term name 'other organism cell membrane' is somewhat non-intuitive; a model unfamiliar with this specific GO term nomenclature might struggle even with correct biological reasoning.",
    "The primary GO annotation in the current entry is GO:0005576 (extracellular region, EXP), which is not among the options. The question forces selection among four choices, none of which is the most directly experimentally supported annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and C both involve membranes, the GO definitions clearly distinguish them: GO:0044218 refers to a foreign organism's membrane (the bacterial target), while GO:0009897 refers to the external leaflet of the protein-producing organism's own plasma membrane. An antimicrobial peptide does not reside on its host's external membrane surface; it is secreted and acts on bacterial membranes. A and D are categorically incompatible with the protein's identity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A059U8Y9) annotates GO:0044218 (other organism cell membrane) via IEA:UniProtKB-KW, derived from the subcellular location comment 'Target cell membrane' (ECO:0000305, curator inference). The protein is antimicrobial peptide megicin-18 from scorpion venom, experimentally shown (PubMed:29896190) to target Gram-positive bacterial membranes. The GO:0044218 annotation is electronic/inferred rather than directly experimental, but the underlying biology (AMP targeting foreign bacterial membranes) is well-supported by the bioassay data in the cited paper. The annotation is present in both current (C6 context, H6) and historical (entry version 9) records.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "H6", "H3", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 77-aa sequence exhibits a hydrophobic N-terminal signal peptide (MQLKKQLIVIFFTYFIVVNESEAFFGALFKLATKIIPSLF...) followed by a short cationic amphipathic mature region (RKRKGREVMMKRDLEQLFDPYQRNLELDRLLKQLPNY), characteristic of a secreted antimicrobial peptide. General biological knowledge establishes that AMPs exert their function by targeting bacterial cell membranes. GO:0044218 'other organism cell membrane' is defined as the cell membrane of a secondary organism with which the first organism interacts, which precisely describes the bacterial target membrane of an AMP. Option C (external side of plasma membrane, GO:0009897) refers to the host cell's own membrane external leaflet, not a foreign organism's membrane, and is therefore distinguishable. Options A (cartilage matrilin complex) and D (CoA biosynthesis enzyme complex) are categorically incompatible with a small cationic venom peptide.",
    "missing_item_specific_fact": "None strictly required; the reasoning chain (signal peptide → secreted AMP → bacterial membrane target → 'other organism cell membrane') is accessible through general biological knowledge and GO term definitions.",
    "reason": "A knowledgeable model can eliminate A and D as functionally irrelevant, distinguish C (host's own membrane) from B (foreign organism's membrane) based on the biological role of antimicrobial peptides targeting bacterial membranes, and select B. The sequence features (small size, cationic amphipathic mature region, signal peptide) provide concrete grounds for identifying this as an AMP without memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and C both involve membranes, the GO definitions clearly distinguish them: GO:0044218 refers to a foreign organism's membrane (the bacterial target), while GO:0009897 refers to the external leaflet of the protein-producing organism's own plasma membrane. An antimicrobial peptide does not reside on its host's external membrane surface; it is secreted and acts on bacterial membranes. A and D are categorically incompatible with the protein's identity."
  },
  "important_caveats": [
    "The GO:0044218 annotation is IEA (inferred from electronic annotation via keyword mapping), not direct experimental evidence. The experimental evidence (ECO:0000269) supports 'Secreted' and 'extracellular region' (GO:0005576). The 'Target cell membrane' annotation is ECO:0000305 (curator inference).",
    "The sequence in the question is the full 77-aa precursor; the mature antimicrobial peptide corresponds to residues 24-41 per the reference. The signal peptide and propeptide are present in the supplied sequence.",
    "The GO term name 'other organism cell membrane' is somewhat non-intuitive; a model unfamiliar with this specific GO term nomenclature might struggle even with correct biological reasoning.",
    "The primary GO annotation in the current entry is GO:0005576 (extracellular region, EXP), which is not among the options. The question forces selection among four choices, none of which is the most directly experimentally supported annotation."
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

**Accession:** `A0A059U8Y9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 9. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.328913+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"29896190","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0451","value":"Target cell membrane"}}]}
```

Source SHA-256: `0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json)  
**Locator:** `/uniProtKBCrossReferences/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.328913+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"29896190","source":"PubMed"}],"id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9)  
**Locator:** `lines 22-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 1.  
**Retrieved:** 2026-11-01T06:27:15.104172+00:00.  

```text
RN   [2]
RP   FUNCTION, BIOASSAY, SYNTHESIS OF 24-41, AND CIRCULAR DICHROISM ANALYSIS.
RC   TISSUE=Venom;
RX   PubMed=29896190; DOI=10.3389/fmicb.2018.01159;
RA   Liu G., Yang F., Li F., Li Z., Lang Y., Shen B., Wu Y., Li W.,
RA   Harrison P.L., Strong P.N., Xie Y., Miller K., Cao Z.;
RT   "Therapeutic potential of a scorpion venom-derived antimicrobial peptide
RT   and its homologs against antibiotic-resistant Gram-positive bacteria.";
RL   Front. Microbiol. 9:1159-1159(2018).
```

Source SHA-256: `c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9)  
**Locator:** `lines 44-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 1.  
**Retrieved:** 2026-11-01T06:27:15.104172+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000269|PubMed:29896190}. Target
CC       cell membrane {ECO:0000305}.
```

Source SHA-256: `c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9)  
**Locator:** `lines 60-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 1.  
**Retrieved:** 2026-11-01T06:27:15.104172+00:00.  

```text
DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.
```

Source SHA-256: `c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9)  
**Locator:** `lines 61-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 1.  
**Retrieved:** 2026-11-01T06:27:15.104172+00:00.  

```text
DR   GO; GO:0044218; C:other organism cell membrane; IEA:UniProtKB-KW.
```

Source SHA-256: `c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 255298-255307`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0044218
name: other organism cell membrane
namespace: cellular_component
alt_id: GO:0044279
def: "The cell membrane of a secondary organism with which the first organism is interacting." [GOC:jl]
synonym: "foreign membrane" RELATED []
synonym: "other organism membrane" BROAD []
is_a: GO:0044217 ! other organism part

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 144. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
