# GO_cellular_component_0041

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — extracellular region

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTQLVVLIVALVFMQLFAQSEAFWSTIWNAAKSLIGKRGLRNLDDLDQFDDSFEPELSEADLKYLEDLLR

[Multiple Choices]
A. food vacuole
B. membrane attack complex
C. extracellular region
D. peroxisomal membrane
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

> The sequence-matched UniProt record describes a secreted antimicrobial peptide and annotates it to the extracellular region. This supports choice C, while noting that the record also lists target cell membrane.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The strongly hydrophobic N-terminus is consistent with a secretory signal peptide, supporting secretion to the extracellular space. The remaining choices describe a parasite digestive vacuole, a complement complex, or a peroxisomal membrane, none of which fits that signal or the short secreted-peptide context.


**Missing item-specific fact**

> No protein-specific annotation is required to distinguish the extracellular choice from these alternatives, though the exact localization and activity would require protein-specific evidence.


**Reason**

> The sequence offers a biologically meaningful secretion signal that distinguishes the extracellular option from the listed intracellular compartments and complement complex.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The record also reports target-cell-membrane localization, but that is not an option; the extracellular-region choice is supported by the secreted status.


### Important caveats

- The GO extracellular-region annotation is IEA:UniProtKB-SubCell, whereas the UniProt subcellular-location statement cites a publication; these are annotation evidence, not independently reviewed experimental results here.
- The sequence is an exact match to the reviewer-identified UniProt record, but that accession and record were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic N-terminus is consistent with a secretory signal peptide, supporting secretion to the extracellular space. The remaining choices describe a parasite digestive vacuole, a complement complex, or a peroxisomal membrane, none of which fits that signal or the short secreted-peptide context.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is required to distinguish the extracellular choice from these alternatives, though the exact localization and activity would require protein-specific evidence.",
    "reason": "The sequence offers a biologically meaningful secretion signal that distinguishes the extracellular option from the listed intracellular compartments and complement complex."
  },
  "case_id": "GO_cellular_component_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes a secreted antimicrobial peptide and annotates it to the extracellular region. This supports choice C, while noting that the record also lists target cell membrane."
  },
  "important_caveats": [
    "The GO extracellular-region annotation is IEA:UniProtKB-SubCell, whereas the UniProt subcellular-location statement cites a publication; these are annotation evidence, not independently reviewed experimental results here.",
    "The sequence is an exact match to the reviewer-identified UniProt record, but that accession and record were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also reports target-cell-membrane localization, but that is not an option; the extracellular-region choice is supported by the secreted status."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes a secreted antimicrobial peptide and annotates it to the extracellular region. This supports choice C, while noting that the record also lists target cell membrane.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The strongly hydrophobic N-terminus is consistent with a secretory signal peptide, supporting secretion to the extracellular space. The remaining choices describe a parasite digestive vacuole, a complement complex, or a peroxisomal membrane, none of which fits that signal or the short secreted-peptide context.",
    "missing_item_specific_fact": "No protein-specific annotation is required to distinguish the extracellular choice from these alternatives, though the exact localization and activity would require protein-specific evidence.",
    "reason": "The sequence offers a biologically meaningful secretion signal that distinguishes the extracellular option from the listed intracellular compartments and complement complex."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also reports target-cell-membrane localization, but that is not an option; the extracellular-region choice is supported by the secreted status."
  },
  "important_caveats": [
    "The GO extracellular-region annotation is IEA:UniProtKB-SubCell, whereas the UniProt subcellular-location statement cites a publication; these are annotation evidence, not independently reviewed experimental results here.",
    "The sequence is an exact match to the reviewer-identified UniProt record, but that accession and record were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DRH4 (sequence matched exactly) annotates the subcellular location as 'Secreted' and 'Target cell membrane' (ECO:0000305, traceable author statement from PubMed:25659089, tissue = venom gland). The GO cross-reference maps to GO:0005576 (extracellular region) via IEA:UniProtKB-SubCell. The protein is a 71-aa scorpion antimicrobial peptide precursor (VpCT2) with a clear N-terminal signal peptide, consistent with secretion into the extracellular space. The sequence match is confirmed across both current and historical (entry v3) snapshots.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region MKTQLVVLIVALVFMQLFAQ exhibits the canonical architecture of a secretory signal peptide: positively charged residues (M, K) followed by a hydrophobic core (VLIVALVFMQLFAQ) and a cleavage-site region. General biology dictates that proteins bearing a functional signal peptide are routed through the secretory pathway and released extracellularly. The small mature peptide (~36 aa, amphipathic, cationic) is consistent with a secreted antimicrobial peptide. The distractors can be eliminated by general knowledge: (B) membrane attack complex is a vertebrate complement C5b-9 pore complex, incompatible with a single small arthropod peptide; (A) food vacuole is a parasite (Apicomplexa)-specific digestive compartment, irrelevant to a scorpion protein; (D) peroxisomal membrane requires a C-terminal PTS1 (SKL-type) or N-terminal PTS2 targeting signal, neither of which is present (C-terminus is LEDLLR, no SKL motif; no PTS2 tripeptide at N-terminus).


**Missing item-specific fact**

> None strictly required. Identifying the protein as a scorpion venom-gland antimicrobial peptide would strengthen confidence but is not necessary; the signal peptide and absence of alternative targeting signals suffice for a defensible extracellular call.


**Reason**

> The sequence itself provides a concrete, general-biology argument (signal peptide → secretion → extracellular) that distinguishes C from the other three options without needing to recall a specific database annotation. The distractors are eliminated by well-known compartment-specific constraints (vertebrate-only MAC, parasite-only food vacuole, peroxisomal targeting signals absent).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C (extracellular region) is consistent with the presence of a signal peptide and the absence of peroxisomal, parasitic, or complement-complex features. The other three options are biologically incompatible with the sequence and organism context. No ambiguity among choices.


### Important caveats

- The GO annotation for extracellular region carries IEA evidence (inferred from electronic annotation via UniProtKB-SubCell), not direct experimental localization. The underlying subcellular-location comment uses ECO:0000305 (traceable author statement), based on tissue-of-origin (venom gland) rather than in-situ localization experiments.
- The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence matches the current and historical (v3) records.
- The protein is annotated as a precursor; the mature antimicrobial peptide (residues 24-36 per reference &#91;2&#93;) is the functional secreted form, but the full precursor still localizes extracellularly after signal-peptide cleavage and secretion.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning-supported judgment rests on what the model could infer from the raw sequence and general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region MKTQLVVLIVALVFMQLFAQ exhibits the canonical architecture of a secretory signal peptide: positively charged residues (M, K) followed by a hydrophobic core (VLIVALVFMQLFAQ) and a cleavage-site region. General biology dictates that proteins bearing a functional signal peptide are routed through the secretory pathway and released extracellularly. The small mature peptide (~36 aa, amphipathic, cationic) is consistent with a secreted antimicrobial peptide. The distractors can be eliminated by general knowledge: (B) membrane attack complex is a vertebrate complement C5b-9 pore complex, incompatible with a single small arthropod peptide; (A) food vacuole is a parasite (Apicomplexa)-specific digestive compartment, irrelevant to a scorpion protein; (D) peroxisomal membrane requires a C-terminal PTS1 (SKL-type) or N-terminal PTS2 targeting signal, neither of which is present (C-terminus is LEDLLR, no SKL motif; no PTS2 tripeptide at N-terminus).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Identifying the protein as a scorpion venom-gland antimicrobial peptide would strengthen confidence but is not necessary; the signal peptide and absence of alternative targeting signals suffice for a defensible extracellular call.",
    "reason": "The sequence itself provides a concrete, general-biology argument (signal peptide → secretion → extracellular) that distinguishes C from the other three options without needing to recall a specific database annotation. The distractors are eliminated by well-known compartment-specific constraints (vertebrate-only MAC, parasite-only food vacuole, peroxisomal targeting signals absent)."
  },
  "case_id": "GO_cellular_component_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DRH4 (sequence matched exactly) annotates the subcellular location as 'Secreted' and 'Target cell membrane' (ECO:0000305, traceable author statement from PubMed:25659089, tissue = venom gland). The GO cross-reference maps to GO:0005576 (extracellular region) via IEA:UniProtKB-SubCell. The protein is a 71-aa scorpion antimicrobial peptide precursor (VpCT2) with a clear N-terminal signal peptide, consistent with secretion into the extracellular space. The sequence match is confirmed across both current and historical (entry v3) snapshots."
  },
  "important_caveats": [
    "The GO annotation for extracellular region carries IEA evidence (inferred from electronic annotation via UniProtKB-SubCell), not direct experimental localization. The underlying subcellular-location comment uses ECO:0000305 (traceable author statement), based on tissue-of-origin (venom gland) rather than in-situ localization experiments.",
    "The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence matches the current and historical (v3) records.",
    "The protein is annotated as a precursor; the mature antimicrobial peptide (residues 24-36 per reference [2]) is the functional secreted form, but the full precursor still localizes extracellularly after signal-peptide cleavage and secretion.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning-supported judgment rests on what the model could infer from the raw sequence and general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C (extracellular region) is consistent with the presence of a signal peptide and the absence of peroxisomal, parasitic, or complement-complex features. The other three options are biologically incompatible with the sequence and organism context. No ambiguity among choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DRH4 (sequence matched exactly) annotates the subcellular location as 'Secreted' and 'Target cell membrane' (ECO:0000305, traceable author statement from PubMed:25659089, tissue = venom gland). The GO cross-reference maps to GO:0005576 (extracellular region) via IEA:UniProtKB-SubCell. The protein is a 71-aa scorpion antimicrobial peptide precursor (VpCT2) with a clear N-terminal signal peptide, consistent with secretion into the extracellular space. The sequence match is confirmed across both current and historical (entry v3) snapshots.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region MKTQLVVLIVALVFMQLFAQ exhibits the canonical architecture of a secretory signal peptide: positively charged residues (M, K) followed by a hydrophobic core (VLIVALVFMQLFAQ) and a cleavage-site region. General biology dictates that proteins bearing a functional signal peptide are routed through the secretory pathway and released extracellularly. The small mature peptide (~36 aa, amphipathic, cationic) is consistent with a secreted antimicrobial peptide. The distractors can be eliminated by general knowledge: (B) membrane attack complex is a vertebrate complement C5b-9 pore complex, incompatible with a single small arthropod peptide; (A) food vacuole is a parasite (Apicomplexa)-specific digestive compartment, irrelevant to a scorpion protein; (D) peroxisomal membrane requires a C-terminal PTS1 (SKL-type) or N-terminal PTS2 targeting signal, neither of which is present (C-terminus is LEDLLR, no SKL motif; no PTS2 tripeptide at N-terminus).",
    "missing_item_specific_fact": "None strictly required. Identifying the protein as a scorpion venom-gland antimicrobial peptide would strengthen confidence but is not necessary; the signal peptide and absence of alternative targeting signals suffice for a defensible extracellular call.",
    "reason": "The sequence itself provides a concrete, general-biology argument (signal peptide → secretion → extracellular) that distinguishes C from the other three options without needing to recall a specific database annotation. The distractors are eliminated by well-known compartment-specific constraints (vertebrate-only MAC, parasite-only food vacuole, peroxisomal targeting signals absent)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C (extracellular region) is consistent with the presence of a signal peptide and the absence of peroxisomal, parasitic, or complement-complex features. The other three options are biologically incompatible with the sequence and organism context. No ambiguity among choices."
  },
  "important_caveats": [
    "The GO annotation for extracellular region carries IEA evidence (inferred from electronic annotation via UniProtKB-SubCell), not direct experimental localization. The underlying subcellular-location comment uses ECO:0000305 (traceable author statement), based on tissue-of-origin (venom gland) rather than in-situ localization experiments.",
    "The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence matches the current and historical (v3) records.",
    "The protein is annotated as a precursor; the mature antimicrobial peptide (residues 24-36 per reference [2]) is the functional secreted form, but the full precursor still localizes extracellularly after signal-peptide cleavage and secretion.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning-supported judgment rests on what the model could infer from the raw sequence and general biology."
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

**Accession:** `P0DRH4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:21.921175+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33862164","source":"PubMed"}],"value":"Antimicrobial peptide VpCT2"}}}
```

Source SHA-256: `107625498df1d10deda5ccda413543ed93c64ecded2c9366c6fb6d1072538ab9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:21.921175+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"25659089","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"25659089","source":"PubMed"}],"id":"SL-0451","value":"Target cell membrane"}}]}
```

Source SHA-256: `107625498df1d10deda5ccda413543ed93c64ecded2c9366c6fb6d1072538ab9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH4.json)  
**Locator:** `/uniProtKBCrossReferences/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:21.921175+00:00.  

```json
{"database":"GO","id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `107625498df1d10deda5ccda413543ed93c64ecded2c9366c6fb6d1072538ab9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:21.921175+00:00.  

```json
{"citation":{"authors":["Quintero-Hernandez V.","Ramirez-Carreto S.","Romero-Gutierrez M.T.","Valdez-Velazquez L.L.","Becerril B.","Possani L.D.","Ortiz E."],"citationCrossReferences":[{"database":"PubMed","id":"25659089"},{"database":"DOI","id":"10.1371/journal.pone.0117188"}],"citationType":"journal article","firstPage":"E0117188","id":"25659089","journal":"PLoS ONE","lastPage":"E0117188","publicationDate":"2015","title":"Transcriptome analysis of scorpion species belonging to the Vaejovis genus.","volume":"10"},"referenceComments":[{"type":"TISSUE","value":"Venom gland"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","PROBABLE AMIDATION AT ILE-36"]}
```

Source SHA-256: `107625498df1d10deda5ccda413543ed93c64ecded2c9366c6fb6d1072538ab9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DRH4?format=txt&versions=3)  
**Locator:** `lines 35-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:24.024520+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:25659089}. Target
CC       cell membrane {ECO:0000305|PubMed:25659089}.
```

Source SHA-256: `35d9a3fd31155ce2f4024cfed4859ad0021a35ba4a613cd2a8c60d568d3bd9eb`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DRH4?format=txt&versions=3)  
**Locator:** `lines 55-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:24.024520+00:00.  

```text
DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.
```

Source SHA-256: `35d9a3fd31155ce2f4024cfed4859ad0021a35ba4a613cd2a8c60d568d3bd9eb`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 57481-57505`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005576
name: extracellular region
namespace: cellular_component
def: "The space external to the outermost structure of a cell. For cells without external protective or external encapsulating structures this refers to space outside of the plasma membrane. This term covers the host cell environment outside an intracellular parasite." [GOC:curators]
comment: Note that this term is intended to annotate gene products that are not attached to the cell surface. For gene products at the cell surface, consider annotating to external side of plasma membrane ; GO:0009897.
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "extracellular" EXACT []
xref: Wikipedia:Extracellular
is_a: GO:0110165 ! cellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 41. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
