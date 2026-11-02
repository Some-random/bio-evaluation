# GO_cellular_component_0190

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — nucleoplasm

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSKRKLSKIDAAEESSKTDLQSRCPETKRSRISDKRAPSQGGLENEGVFEELLRTSGIILKVGEGQNEIAVDQTAFQKKLRVALEKHPSYPGVVNEFISGLESHIKDRSQFKNCLLPCTPARTEGSRTLVHSYCESLIKLLLGIKILQPAVVTLLLEKIPEFFFDVVGTFGTNFPRLIVNQFKWLDGLLDSQDLVKKLMQMLSVSPVPIQHDIITSLPEILEDSQQNEVARELSCLLKQGRRLTVPILDALSRLDLDAELLAEVRQSAMTIVPSVKLEDLPVVIKFILHNVKAADAVEVISDLRKSLDLSSCVLPLQLLGSQRKLKSQAQASSSMSQVTTSQNCVKLLFDVIKQAVRFQKDVSEAWIKAIENSTSVSDHKVLDLIVLLLIHSTNSKNRKQTEKVLRSKIRLGCMPEQLMQNAFQNHSMVIKDFFPSILSLAQTFLHSAHPAVVSFGSCMYKQAFAVFDSYCQQEVVCALVTHVCSGNETELDISLDVLTDLVILHPSLLLRYATFVKTILDSMQKLNPCQIRKLFYILSTLAFSQRQEGSYIQDDMHMVIRKWLSSSVPNHKQMGIIGAVTMMGSVALKRNEADGGLLERPELSIECDGQLSTLLDLVGFCCEQTPEVLALYYDELANLIEKQKGNLDLQLLDKFGKSLVEDFPNDFVVDLSPTVDGSFLFPVKSLYNLDEDETQGAIAINLLPLVSQSEPGRVADEMSNSRKRVVSPICLSPCFRLLRLYTGEQNNGSLEEIDALLGCPLYLTDLEVEGKLDSLSKQEREFLCSLLFYALNWFREVVNAFCQQQDAEMKGKVLTRLQNITELQNVLGKCLAATPGYVPPPATFDSEAPEGVPSINAGGPVRKKNGKKRKSDSSKACSAERTQADESSDGNQPDTELSELEKSATEKETGNPLAQLQSYRPYFRELDLEVFSVLHCGLLTKSILDTEMHTEASEVVQLGPAELCFLLDDMCWKLEHVLTPGSTRRVPFLKERGNKDVGFSHLCQRSPKEVAVCVVKLLKPLCNHMENMHNYFQTVIPNQGVVDESGLNIQEYQLMSSCYHQLLLAFRLLFAWSGFSQHENSNLLRSALQVLADRLKPGETEFLPLEELISESFQYLLNFQASIPSFQCAFILTQVLMAISEKPMTGWKREKMASLAKQFLCQSWMKPGGDREKGSHFNSALHTLLCVYLEHTDNILKAIEEISSVGVPELINSAKDGCSSTYPTLSRQTFPVFFRVMMAQLESSVKSIPAGKPSDSGEVQLEKLLKWNIAVRNFHILINLVKVFDSRPVLSICLKYGRLFVEAFLKLAMPLLDHSFKKHRDDVQSLLKTLQLSTRQLHHMCGHSKIHQDLGLTNHVPLLKKSLEQFVYRVKAMLAFNHCQEAFWVGVLKNRDLQGEEILSQASAAPEEDSAEGSEEDTADSAAEEPDGTDSDSGGAGR

[Multiple Choices]
A. mitochondrial outer membrane
B. cellular bud neck septin ring
C. cell surface
D. nucleoplasm
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

> The exact-matched chicken sequence is annotated to the nucleus, with a GO nucleoplasm annotation (TAS:Reactome). The UniProt subcellular-location annotation is transferred by similarity from human Q9BXW9, so this supports the key as database annotation rather than establishing direct experimental evidence for this chicken protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus contains a basic Lys/Arg-rich stretch consistent with a nuclear localization signal, while the sequence lacks an evident hydrophobic signal peptide or transmembrane segment. Among these choices, that favors a soluble nuclear location over membrane-associated or bud-neck options.


**Missing item-specific fact**

> The precise protein-specific GO annotation is not supplied, but an exact database entry is not necessary to distinguish the nuclear option from these alternatives using the sequence’s localization clues.


**Reason**

> The sequence offers a defensible, though not conclusive, basis for nuclear localization. The choice of nucleoplasm is the best fit among the listed options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is comparably supported by the sequence’s apparent nuclear localization signals and lack of membrane-targeting features.


### Important caveats

- A basic sequence motif predicts nuclear targeting but does not by itself prove the precise subnuclear compartment.
- The supplied annotation’s subcellular-location evidence is transferred by similarity; the GO nucleoplasm annotation is TAS:Reactome, not presented here as direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus contains a basic Lys/Arg-rich stretch consistent with a nuclear localization signal, while the sequence lacks an evident hydrophobic signal peptide or transmembrane segment. Among these choices, that favors a soluble nuclear location over membrane-associated or bud-neck options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise protein-specific GO annotation is not supplied, but an exact database entry is not necessary to distinguish the nuclear option from these alternatives using the sequence’s localization clues.",
    "reason": "The sequence offers a defensible, though not conclusive, basis for nuclear localization. The choice of nucleoplasm is the best fit among the listed options."
  },
  "case_id": "GO_cellular_component_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-matched chicken sequence is annotated to the nucleus, with a GO nucleoplasm annotation (TAS:Reactome). The UniProt subcellular-location annotation is transferred by similarity from human Q9BXW9, so this supports the key as database annotation rather than establishing direct experimental evidence for this chicken protein."
  },
  "important_caveats": [
    "A basic sequence motif predicts nuclear targeting but does not by itself prove the precise subnuclear compartment.",
    "The supplied annotation’s subcellular-location evidence is transferred by similarity; the GO nucleoplasm annotation is TAS:Reactome, not presented here as direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence’s apparent nuclear localization signals and lack of membrane-targeting features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched chicken sequence is annotated to the nucleus, with a GO nucleoplasm annotation (TAS:Reactome). The UniProt subcellular-location annotation is transferred by similarity from human Q9BXW9, so this supports the key as database annotation rather than establishing direct experimental evidence for this chicken protein.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus contains a basic Lys/Arg-rich stretch consistent with a nuclear localization signal, while the sequence lacks an evident hydrophobic signal peptide or transmembrane segment. Among these choices, that favors a soluble nuclear location over membrane-associated or bud-neck options.",
    "missing_item_specific_fact": "The precise protein-specific GO annotation is not supplied, but an exact database entry is not necessary to distinguish the nuclear option from these alternatives using the sequence’s localization clues.",
    "reason": "The sequence offers a defensible, though not conclusive, basis for nuclear localization. The choice of nucleoplasm is the best fit among the listed options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence’s apparent nuclear localization signals and lack of membrane-targeting features."
  },
  "important_caveats": [
    "A basic sequence motif predicts nuclear targeting but does not by itself prove the precise subnuclear compartment.",
    "The supplied annotation’s subcellular-location evidence is transferred by similarity; the GO nucleoplasm annotation is TAS:Reactome, not presented here as direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q68Y81 (FANCD2_CHICK, Gallus gallus) carries GO:0005654 (C:nucleoplasm) with evidence code TAS:Reactome, and the subcellular location comment states 'Nucleus' with note 'Concentrates in nuclear foci during S phase and upon genotoxic stress' (ECO:0000250, transferred from human FANCD2 Q9BXW9). The sequence in the prompt matches the UniProt entry exactly (SHA-256 confirmed). The nucleoplasm annotation is directly recorded in the database entry.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence lacks any N-terminal mitochondrial targeting signal (no amphipathic helix with positively charged residues), eliminating option A. It lacks a septin-specific GTPase domain, eliminating option B. It lacks a signal peptide or transmembrane hydrophobic segments, eliminating option C. The protein is 1439 aa with multiple WD40 repeat motifs (repeated Trp-Asp dipeptides in beta-propeller-like context, e.g., 'WD' patterns visible throughout the C-terminal region), a domain architecture strongly associated with nuclear DNA-repair and cell-cycle proteins. The absence of any membrane anchor or secretion signal combined with the WD40-repeat architecture points toward a soluble nuclear compartment, making nucleoplasm the most defensible choice among the four options.


**Missing item-specific fact**

> None strictly required. A model could arrive at D by eliminating A, B, C through absence of their defining sequence features and recognizing WD40 repeats as hallmarks of nuclear repair machinery. However, confident identification of the specific WD40 architecture and its nuclear DNA-repair association benefits from prior knowledge of FANCD2 or similar large nuclear repair complexes.


**Reason**

> The three distractors (mitochondrial outer membrane, septin ring, cell surface) each require specific sequence features (mito targeting signal, septin GTPase domain, signal peptide/TM helices) that are clearly absent from this sequence. The remaining option, nucleoplasm, is consistent with the protein's large size, WD40-repeat architecture, and lack of any membrane-localization signal. This provides a concrete, sequence-grounded elimination pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C each demand specific sequence hallmarks (mito targeting signal, septin domain, signal peptide/TM domain) that are absent from the supplied sequence. D (nucleoplasm) is the only remaining option and is consistent with the protein's domain architecture. No genuine ambiguity exists among the four choices.


### Important caveats

- The UniProt subcellular location annotation uses ECO:0000250 (inferred by similarity from human FANCD2 Q9BXW9), meaning the nuclear localization was transferred from the human ortholog rather than experimentally verified in chicken specifically.
- The GO nucleoplasm annotation carries evidence code TAS:Reactome (curated pathway database), not direct experimental localization in this organism.
- The WD40 repeat identification from sequence alone is a heuristic; not all WD40 proteins are nuclear, though those involved in DNA repair (like FANCD2) are.
- The accession Q68Y81 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks any N-terminal mitochondrial targeting signal (no amphipathic helix with positively charged residues), eliminating option A. It lacks a septin-specific GTPase domain, eliminating option B. It lacks a signal peptide or transmembrane hydrophobic segments, eliminating option C. The protein is 1439 aa with multiple WD40 repeat motifs (repeated Trp-Asp dipeptides in beta-propeller-like context, e.g., 'WD' patterns visible throughout the C-terminal region), a domain architecture strongly associated with nuclear DNA-repair and cell-cycle proteins. The absence of any membrane anchor or secretion signal combined with the WD40-repeat architecture points toward a soluble nuclear compartment, making nucleoplasm the most defensible choice among the four options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. A model could arrive at D by eliminating A, B, C through absence of their defining sequence features and recognizing WD40 repeats as hallmarks of nuclear repair machinery. However, confident identification of the specific WD40 architecture and its nuclear DNA-repair association benefits from prior knowledge of FANCD2 or similar large nuclear repair complexes.",
    "reason": "The three distractors (mitochondrial outer membrane, septin ring, cell surface) each require specific sequence features (mito targeting signal, septin GTPase domain, signal peptide/TM helices) that are clearly absent from this sequence. The remaining option, nucleoplasm, is consistent with the protein's large size, WD40-repeat architecture, and lack of any membrane-localization signal. This provides a concrete, sequence-grounded elimination pathway."
  },
  "case_id": "GO_cellular_component_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt Q68Y81 (FANCD2_CHICK, Gallus gallus) carries GO:0005654 (C:nucleoplasm) with evidence code TAS:Reactome, and the subcellular location comment states 'Nucleus' with note 'Concentrates in nuclear foci during S phase and upon genotoxic stress' (ECO:0000250, transferred from human FANCD2 Q9BXW9). The sequence in the prompt matches the UniProt entry exactly (SHA-256 confirmed). The nucleoplasm annotation is directly recorded in the database entry."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses ECO:0000250 (inferred by similarity from human FANCD2 Q9BXW9), meaning the nuclear localization was transferred from the human ortholog rather than experimentally verified in chicken specifically.",
    "The GO nucleoplasm annotation carries evidence code TAS:Reactome (curated pathway database), not direct experimental localization in this organism.",
    "The WD40 repeat identification from sequence alone is a heuristic; not all WD40 proteins are nuclear, though those involved in DNA repair (like FANCD2) are.",
    "The accession Q68Y81 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C each demand specific sequence hallmarks (mito targeting signal, septin domain, signal peptide/TM domain) that are absent from the supplied sequence. D (nucleoplasm) is the only remaining option and is consistent with the protein's domain architecture. No genuine ambiguity exists among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q68Y81 (FANCD2_CHICK, Gallus gallus) carries GO:0005654 (C:nucleoplasm) with evidence code TAS:Reactome, and the subcellular location comment states 'Nucleus' with note 'Concentrates in nuclear foci during S phase and upon genotoxic stress' (ECO:0000250, transferred from human FANCD2 Q9BXW9). The sequence in the prompt matches the UniProt entry exactly (SHA-256 confirmed). The nucleoplasm annotation is directly recorded in the database entry.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence lacks any N-terminal mitochondrial targeting signal (no amphipathic helix with positively charged residues), eliminating option A. It lacks a septin-specific GTPase domain, eliminating option B. It lacks a signal peptide or transmembrane hydrophobic segments, eliminating option C. The protein is 1439 aa with multiple WD40 repeat motifs (repeated Trp-Asp dipeptides in beta-propeller-like context, e.g., 'WD' patterns visible throughout the C-terminal region), a domain architecture strongly associated with nuclear DNA-repair and cell-cycle proteins. The absence of any membrane anchor or secretion signal combined with the WD40-repeat architecture points toward a soluble nuclear compartment, making nucleoplasm the most defensible choice among the four options.",
    "missing_item_specific_fact": "None strictly required. A model could arrive at D by eliminating A, B, C through absence of their defining sequence features and recognizing WD40 repeats as hallmarks of nuclear repair machinery. However, confident identification of the specific WD40 architecture and its nuclear DNA-repair association benefits from prior knowledge of FANCD2 or similar large nuclear repair complexes.",
    "reason": "The three distractors (mitochondrial outer membrane, septin ring, cell surface) each require specific sequence features (mito targeting signal, septin GTPase domain, signal peptide/TM helices) that are clearly absent from this sequence. The remaining option, nucleoplasm, is consistent with the protein's large size, WD40-repeat architecture, and lack of any membrane-localization signal. This provides a concrete, sequence-grounded elimination pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C each demand specific sequence hallmarks (mito targeting signal, septin domain, signal peptide/TM domain) that are absent from the supplied sequence. D (nucleoplasm) is the only remaining option and is consistent with the protein's domain architecture. No genuine ambiguity exists among the four choices."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses ECO:0000250 (inferred by similarity from human FANCD2 Q9BXW9), meaning the nuclear localization was transferred from the human ortholog rather than experimentally verified in chicken specifically.",
    "The GO nucleoplasm annotation carries evidence code TAS:Reactome (curated pathway database), not direct experimental localization in this organism.",
    "The WD40 repeat identification from sequence alone is a heuristic; not all WD40 proteins are nuclear, though those involved in DNA repair (like FANCD2) are.",
    "The accession Q68Y81 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
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

**Accession:** `Q68Y81` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 83. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q68Y81.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:33.185561+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BXW9","source":"UniProtKB"}],"value":"Concentrates in nuclear foci during S phase and upon genotoxic stress"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BXW9","source":"UniProtKB"}],"id":"SL-0191","value":"Nucleus"}}]}
```

Source SHA-256: `ff3ce4e6f36dcd0d11c43ebcae1b8c25b23f684dfaa6fc884279d884121ad6e4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q68Y81.json)  
**Locator:** `/uniProtKBCrossReferences/25`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:33.185561+00:00.  

```json
{"database":"GO","id":"GO:0005654","properties":[{"key":"GoTerm","value":"C:nucleoplasm"},{"key":"GoEvidenceType","value":"TAS:Reactome"}]}
```

Source SHA-256: `ff3ce4e6f36dcd0d11c43ebcae1b8c25b23f684dfaa6fc884279d884121ad6e4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q68Y81?format=txt&versions=83)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-02T04:31:35.768181+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000250|UniProtKB:Q9BXW9}.
CC       Note=Concentrates in nuclear foci during S phase and upon genotoxic
CC       stress. {ECO:0000250|UniProtKB:Q9BXW9}.
```

Source SHA-256: `759f64b5ffb3efb084b28033deae86d52a50d5f5cbf316fa2b017e6aed4cc5ae`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q68Y81?format=txt&versions=83)  
**Locator:** `lines 128-128`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-02T04:31:35.768181+00:00.  

```text
DR   GO; GO:0005654; C:nucleoplasm; TAS:Reactome.
```

Source SHA-256: `759f64b5ffb3efb084b28033deae86d52a50d5f5cbf316fa2b017e6aed4cc5ae`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 190. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
