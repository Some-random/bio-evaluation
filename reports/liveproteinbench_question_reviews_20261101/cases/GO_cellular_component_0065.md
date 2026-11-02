# GO_cellular_component_0065

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — fungal-type cell wall

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVGKSTLLSVLASASVAFAACSLDSHCPEETPCCSQYGECGTGAYCLGGCDPRMSFSLESCVPEPVCESASYTFTSMDGITSNTKYLGDASKSNWVYSGSPVIYNDNVLLTMSANSVGTVMASSTYMWYGNVKAKFKTSRGQGVITAFILFSDVKDEIDYEFVGSELTTAQSNYYFQGITNYDNELNITLSDTYANYHEYEIDWTPDEITWLVDGQVGRTKKRADTWNATANQWNFPQTPARVQLSLWPGGLASNGAGTIAWAGGEIDWNSEDIQNNGYYYAAFESVDISCYNAKSAPGTNSGKSYYYNSVLGTNNTVIDSKNATILSSLLATGTNMTAGESAAASGSTAASTAATVPGLTGSGGGGVGDNHSDDGSSSSDSSSGSATSSSSGSSSTGSSGFSQGDGSTSTSKSSADSLVANQERVLKGSLFAGIVAVVAMMAL

[Multiple Choices]
A. fungal-type cell wall
B. monoatomic ion channel complex
C. primosome complex
D. virus tail, tube
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

> The sequence-matched UniProt record annotates fungal-type cell wall, but the cited GO assignments are computational (IEA:TreeGrafter historically and IEA:UniProtKB-ARBA currently), not direct experimental localization evidence. The record also assigns cell-membrane localization with a GPI anchor, which is compatible with a cell-surface protein and does not contradict cell-wall association.

Citations as saved: [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic signal and C-terminal hydrophobic region are consistent with a secreted or surface-anchored protein, making a channel complex, primosome, or viral tail tube unlikely. Those signals alone do not establish that the protein resides in the fungal cell wall rather than at the membrane or another surface-associated location.


**Missing item-specific fact**

> The protein-specific identification/function and its cell-wall localization annotation or experimental evidence are absent from the input.


**Reason**

> Sequence features provide useful broad localization clues but do not independently establish the particular GO cellular-component assignment. The supporting database annotations are reviewer-only and cannot count as information available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, fungal-type cell wall is the only plausible surface-location option; the membrane annotation is not itself a listed choice.


### Important caveats

- The supporting fungal-cell-wall GO annotation is computational rather than experimental.
- The sequence-matched record also annotates cell-membrane localization with a GPI anchor; the evidence does not establish which location is primary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal and C-terminal hydrophobic region are consistent with a secreted or surface-anchored protein, making a channel complex, primosome, or viral tail tube unlikely. Those signals alone do not establish that the protein resides in the fungal cell wall rather than at the membrane or another surface-associated location.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification/function and its cell-wall localization annotation or experimental evidence are absent from the input.",
    "reason": "Sequence features provide useful broad localization clues but do not independently establish the particular GO cellular-component assignment. The supporting database annotations are reviewer-only and cannot count as information available to the evaluated model."
  },
  "case_id": "GO_cellular_component_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C6",
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates fungal-type cell wall, but the cited GO assignments are computational (IEA:TreeGrafter historically and IEA:UniProtKB-ARBA currently), not direct experimental localization evidence. The record also assigns cell-membrane localization with a GPI anchor, which is compatible with a cell-surface protein and does not contradict cell-wall association."
  },
  "important_caveats": [
    "The supporting fungal-cell-wall GO annotation is computational rather than experimental.",
    "The sequence-matched record also annotates cell-membrane localization with a GPI anchor; the evidence does not establish which location is primary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, fungal-type cell wall is the only plausible surface-location option; the membrane annotation is not itself a listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates fungal-type cell wall, but the cited GO assignments are computational (IEA:TreeGrafter historically and IEA:UniProtKB-ARBA currently), not direct experimental localization evidence. The record also assigns cell-membrane localization with a GPI anchor, which is compatible with a cell-surface protein and does not contradict cell-wall association.",
    "evidence_ids": ["H4", "C6", "H3", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal and C-terminal hydrophobic region are consistent with a secreted or surface-anchored protein, making a channel complex, primosome, or viral tail tube unlikely. Those signals alone do not establish that the protein resides in the fungal cell wall rather than at the membrane or another surface-associated location.",
    "missing_item_specific_fact": "The protein-specific identification/function and its cell-wall localization annotation or experimental evidence are absent from the input.",
    "reason": "Sequence features provide useful broad localization clues but do not independently establish the particular GO cellular-component assignment. The supporting database annotations are reviewer-only and cannot count as information available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, fungal-type cell wall is the only plausible surface-location option; the membrane annotation is not itself a listed choice."
  },
  "important_caveats": [
    "The supporting fungal-cell-wall GO annotation is computational rather than experimental.",
    "The sequence-matched record also annotates cell-membrane localization with a GPI anchor; the evidence does not establish which location is primary."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A384K116, Crh-like protein 3 / Chitinase crh3 / Chitin transglycosylase crh3 from Botrytis cinerea) carries GO:0009277 (fungal-type cell wall) as a cellular component annotation. The evidence code is IEA (TreeGrafter / UniProtKB-ARBA), i.e., computational inference rather than experimental localization. The primary subcellular location annotation is 'Cell membrane; Lipid-anchor, GPI-anchor' (ECO:0000255, similarity-based). However, the GO:0009277 definition explicitly states that fungal cell wall glycoproteins 'may be modified with N- or O-linked carbohydrates, or glycosylphosphatidylinositol (GPI) anchors,' directly encompassing GPI-anchored proteins. A chitin transglycosylase involved in cell wall remodeling, secreted via a signal peptide and tethered by a GPI anchor, is biologically consistent with the fungal-type cell wall compartment. The annotation is computationally derived but biologically well-grounded.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a classic N-terminal signal peptide (MVGKSTLLSVLASASVAFAACSLDSH: hydrophobic core preceded by a positively charged N-terminus) and ends with a C-terminal hydrophobic segment (SLVANQERVLKGSLFAGIVAVVAMMAL) consistent with a GPI-anchor signal. This architecture dictates a secreted, cell-surface-tethered protein. This immediately eliminates C (primosome complex: a nuclear DNA-replication complex, incompatible with a signal peptide) and D (virus tail tube: a viral structural protein, incompatible with eukaryotic secretion machinery). Option B (monoatomic ion channel complex) requires multiple transmembrane helices forming a pore; this protein has a cleavable signal peptide and a GPI anchor, not a channel-forming multi-TM topology. Among the four choices, only A (fungal-type cell wall) represents an extracellular/cell-surface compartment compatible with a GPI-anchored secreted enzyme. The GO definition of fungal-type cell wall explicitly includes GPI-anchored glycoproteins, reinforcing the fit.


**Missing item-specific fact**

> None strictly required. A knowledgeable model can reason from signal peptide + GPI anchor architecture to a cell-surface compartment and eliminate the three clearly incompatible alternatives without knowing the exact UniProt accession or chitinase domain identity.


**Reason**

> The sequence features (signal peptide, GPI anchor, absence of channel-forming TMs, absence of nuclear localization signals, absence of viral structural motifs) provide concrete, general biological grounds to select A by elimination and positive inference. No protein-specific experimental measurement or database lookup is strictly necessary, although recognizing the chitinase/transglycosylase domain family would strengthen the argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is also annotated to plasma membrane (GO:0005886, IEA:UniProtKB-SubCell), but 'plasma membrane' is not among the four choices. Among the provided options, A is the only cell-surface/extracellular compartment. B, C, and D are structurally and functionally incompatible with a GPI-anchored secreted protein. No ambiguity among the given choices.


### Important caveats

- The GO:0009277 annotation is IEA (computational, TreeGrafter/ARBA), not experimentally verified localization. The primary UniProt subcellular location comment states 'Cell membrane; GPI-anchor' (ECO:0000255, similarity-based).
- The PubMed reference (33846308) describes Crh1 as a 'cytoplasmic effector,' but the entry here is for Crh3; the functional role of Crh3 in cell wall remodeling is inferred by similarity to Crh1/Crh2.
- The model is not told the organism is a fungus; reasoning to 'fungal-type cell wall' requires recognizing that a GPI-anchored secreted protein in a eukaryote with a cell wall would localize there, or eliminating all other options.
- Sequence identity to UniProt A0A384K116 is confirmed (444 AA, SHA-256 match) in both current and historical (v26) snapshots.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a classic N-terminal signal peptide (MVGKSTLLSVLASASVAFAACSLDSH: hydrophobic core preceded by a positively charged N-terminus) and ends with a C-terminal hydrophobic segment (SLVANQERVLKGSLFAGIVAVVAMMAL) consistent with a GPI-anchor signal. This architecture dictates a secreted, cell-surface-tethered protein. This immediately eliminates C (primosome complex: a nuclear DNA-replication complex, incompatible with a signal peptide) and D (virus tail tube: a viral structural protein, incompatible with eukaryotic secretion machinery). Option B (monoatomic ion channel complex) requires multiple transmembrane helices forming a pore; this protein has a cleavable signal peptide and a GPI anchor, not a channel-forming multi-TM topology. Among the four choices, only A (fungal-type cell wall) represents an extracellular/cell-surface compartment compatible with a GPI-anchored secreted enzyme. The GO definition of fungal-type cell wall explicitly includes GPI-anchored glycoproteins, reinforcing the fit.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. A knowledgeable model can reason from signal peptide + GPI anchor architecture to a cell-surface compartment and eliminate the three clearly incompatible alternatives without knowing the exact UniProt accession or chitinase domain identity.",
    "reason": "The sequence features (signal peptide, GPI anchor, absence of channel-forming TMs, absence of nuclear localization signals, absence of viral structural motifs) provide concrete, general biological grounds to select A by elimination and positive inference. No protein-specific experimental measurement or database lookup is strictly necessary, although recognizing the chitinase/transglycosylase domain family would strengthen the argument."
  },
  "case_id": "GO_cellular_component_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "GO1",
      "H1",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384K116, Crh-like protein 3 / Chitinase crh3 / Chitin transglycosylase crh3 from Botrytis cinerea) carries GO:0009277 (fungal-type cell wall) as a cellular component annotation. The evidence code is IEA (TreeGrafter / UniProtKB-ARBA), i.e., computational inference rather than experimental localization. The primary subcellular location annotation is 'Cell membrane; Lipid-anchor, GPI-anchor' (ECO:0000255, similarity-based). However, the GO:0009277 definition explicitly states that fungal cell wall glycoproteins 'may be modified with N- or O-linked carbohydrates, or glycosylphosphatidylinositol (GPI) anchors,' directly encompassing GPI-anchored proteins. A chitin transglycosylase involved in cell wall remodeling, secreted via a signal peptide and tethered by a GPI anchor, is biologically consistent with the fungal-type cell wall compartment. The annotation is computationally derived but biologically well-grounded."
  },
  "important_caveats": [
    "The GO:0009277 annotation is IEA (computational, TreeGrafter/ARBA), not experimentally verified localization. The primary UniProt subcellular location comment states 'Cell membrane; GPI-anchor' (ECO:0000255, similarity-based).",
    "The PubMed reference (33846308) describes Crh1 as a 'cytoplasmic effector,' but the entry here is for Crh3; the functional role of Crh3 in cell wall remodeling is inferred by similarity to Crh1/Crh2.",
    "The model is not told the organism is a fungus; reasoning to 'fungal-type cell wall' requires recognizing that a GPI-anchored secreted protein in a eukaryote with a cell wall would localize there, or eliminating all other options.",
    "Sequence identity to UniProt A0A384K116 is confirmed (444 AA, SHA-256 match) in both current and historical (v26) snapshots."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is also annotated to plasma membrane (GO:0005886, IEA:UniProtKB-SubCell), but 'plasma membrane' is not among the four choices. Among the provided options, A is the only cell-surface/extracellular compartment. B, C, and D are structurally and functionally incompatible with a GPI-anchored secreted protein. No ambiguity among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384K116, Crh-like protein 3 / Chitinase crh3 / Chitin transglycosylase crh3 from Botrytis cinerea) carries GO:0009277 (fungal-type cell wall) as a cellular component annotation. The evidence code is IEA (TreeGrafter / UniProtKB-ARBA), i.e., computational inference rather than experimental localization. The primary subcellular location annotation is 'Cell membrane; Lipid-anchor, GPI-anchor' (ECO:0000255, similarity-based). However, the GO:0009277 definition explicitly states that fungal cell wall glycoproteins 'may be modified with N- or O-linked carbohydrates, or glycosylphosphatidylinositol (GPI) anchors,' directly encompassing GPI-anchored proteins. A chitin transglycosylase involved in cell wall remodeling, secreted via a signal peptide and tethered by a GPI anchor, is biologically consistent with the fungal-type cell wall compartment. The annotation is computationally derived but biologically well-grounded.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "GO1", "H1", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a classic N-terminal signal peptide (MVGKSTLLSVLASASVAFAACSLDSH: hydrophobic core preceded by a positively charged N-terminus) and ends with a C-terminal hydrophobic segment (SLVANQERVLKGSLFAGIVAVVAMMAL) consistent with a GPI-anchor signal. This architecture dictates a secreted, cell-surface-tethered protein. This immediately eliminates C (primosome complex: a nuclear DNA-replication complex, incompatible with a signal peptide) and D (virus tail tube: a viral structural protein, incompatible with eukaryotic secretion machinery). Option B (monoatomic ion channel complex) requires multiple transmembrane helices forming a pore; this protein has a cleavable signal peptide and a GPI anchor, not a channel-forming multi-TM topology. Among the four choices, only A (fungal-type cell wall) represents an extracellular/cell-surface compartment compatible with a GPI-anchored secreted enzyme. The GO definition of fungal-type cell wall explicitly includes GPI-anchored glycoproteins, reinforcing the fit.",
    "missing_item_specific_fact": "None strictly required. A knowledgeable model can reason from signal peptide + GPI anchor architecture to a cell-surface compartment and eliminate the three clearly incompatible alternatives without knowing the exact UniProt accession or chitinase domain identity.",
    "reason": "The sequence features (signal peptide, GPI anchor, absence of channel-forming TMs, absence of nuclear localization signals, absence of viral structural motifs) provide concrete, general biological grounds to select A by elimination and positive inference. No protein-specific experimental measurement or database lookup is strictly necessary, although recognizing the chitinase/transglycosylase domain family would strengthen the argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is also annotated to plasma membrane (GO:0005886, IEA:UniProtKB-SubCell), but 'plasma membrane' is not among the four choices. Among the provided options, A is the only cell-surface/extracellular compartment. B, C, and D are structurally and functionally incompatible with a GPI-anchored secreted protein. No ambiguity among the given choices."
  },
  "important_caveats": [
    "The GO:0009277 annotation is IEA (computational, TreeGrafter/ARBA), not experimentally verified localization. The primary UniProt subcellular location comment states 'Cell membrane; GPI-anchor' (ECO:0000255, similarity-based).",
    "The PubMed reference (33846308) describes Crh1 as a 'cytoplasmic effector,' but the entry here is for Crh3; the functional role of Crh3 in cell wall remodeling is inferred by similarity to Crh1/Crh2.",
    "The model is not told the organism is a fungus; reasoning to 'fungal-type cell wall' requires recognizing that a GPI-anchored secreted protein in a eukaryote with a cell wall would localize there, or eliminating all other options.",
    "Sequence identity to UniProt A0A384K116 is confirmed (444 AA, SHA-256 match) in both current and historical (v26) snapshots."
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

**Accession:** `A0A384K116` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"flag":"Precursor","includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"3.2.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"Chitinase crh3"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"2.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"Chitin transglycosylase crh3"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33846308","source":"PubMed"}],"value":"Crh-like protein 3"}}}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9902","value":"Lipid-anchor, GPI-anchor"}}]}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"database":"GO","id":"GO:0009277","properties":[{"key":"GoTerm","value":"C:fungal-type cell wall"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-ARBA"}]}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:01.844205+00:00.  

```text
ID   CRH3_BOTFB              Reviewed;         444 AA.
AC   A0A384K116;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   07-NOV-2018, sequence version 1.
DT   28-JAN-2026, entry version 26.
DE   RecName: Full=Crh-like protein 3 {ECO:0000303|PubMed:33846308};
DE   Includes:
DE     RecName: Full=Chitinase crh3 {ECO:0000250|UniProtKB:Q8J0P4};
DE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};
DE   Includes:
DE     RecName: Full=Chitin transglycosylase crh3 {ECO:0000250|UniProtKB:Q8J0P4};
DE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};
DE   Flags: Precursor;
GN   Name=crh3 {ECO:0000303|PubMed:33846308}; ORFNames=BCIN_13g03640;
OS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis
OS   cinerea).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;
OC   Helotiales; Sclerotiniaceae; Botrytis.
OX   NCBI_TaxID=332648;
```

Source SHA-256: `68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)  
**Locator:** `lines 79-80`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:01.844205+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000255}; Lipid-anchor, GPI-
CC       anchor {ECO:0000255}.
```

Source SHA-256: `68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)  
**Locator:** `lines 97-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:01.844205+00:00.  

```text
DR   GO; GO:0009277; C:fungal-type cell wall; IEA:TreeGrafter.
```

Source SHA-256: `68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)  
**Locator:** `lines 98-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:01.844205+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 94765-94774`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009277
name: fungal-type cell wall
namespace: cellular_component
def: "A rigid yet dynamic structure surrounding the plasma membrane that affords protection from stresses and contributes to cell morphogenesis, consisting of extensively cross-linked glycoproteins and carbohydrates. The glycoproteins may be modified with N- or O-linked carbohydrates, or glycosylphosphatidylinositol (GPI) anchors; the polysaccharides are primarily branched glucans, including beta-linked and alpha-linked glucans, and may also include chitin and other carbohydrate polymers, but not cellulose or pectin. Enzymes involved in cell wall biosynthesis are also found in the cell wall. Note that some forms of fungi develop a capsule outside of the cell wall under certain circumstances; this is considered a separate structure." [GOC:mcc, GOC:mtg_sensu, ISBN:3540601864, PMID:11283274, PMID:16927300, PMID:3319422, PMID:36266346]
synonym: "beta-glucan-containing cell wall" RELATED []
synonym: "chitin- and beta-glucan-containing cell wall" NARROW []
synonym: "chitin-containing cell wall" RELATED []
is_a: GO:0005618 ! cell wall

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 65. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
