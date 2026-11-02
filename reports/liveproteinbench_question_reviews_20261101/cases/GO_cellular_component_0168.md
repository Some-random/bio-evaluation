# GO_cellular_component_0168

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MALSTLWLVLMLWTSLFSDSQCSTLSQAELQELEQIHTWVVSRSFPCSVTCGLGLLTQELCPIGVTRNISTSSCKLRTISCLDSWQCGLKTQTATVGRRLVLDCLEEVMEAMGRFSFVVSWRFAFAIITTDDSLFTRYEALSLDKVVLDPLREEDSGTYRCDVLDTGKRRVKRMYKGVKVLSPKDLSLDFAQGLIHWEIPESRFANLTSSRKVYSSSTIRNIVIISVPLSFAIAVVIFIFLFCYSRRARRAAHLCQDNI

[Multiple Choices]
A. site of double-strand break
B. protein-DNA complex
C. matrilin complex
D. plasma membrane
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

> The exact sequence matches the zebrafish UniProt record, which annotates it to the cell membrane with a literature citation; GO treats “cell membrane” as an exact synonym of plasma membrane. The record also assigns plasma membrane through computational annotations. This supports D, though the excerpts do not independently establish the underlying experimental evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal sequence, a large intervening non-hydrophobic region, and a hydrophobic segment near the C-terminus followed by a basic tail. This is consistent with a single-pass type I membrane protein and makes a membrane location much more plausible than a DNA-damage site, protein-DNA complex, or matrilin complex.


**Missing item-specific fact**

> The sequence alone does not establish plasma membrane localization over other cellular membranes; the record’s specific cell-membrane localization is additional item-specific annotation evidence.


**Reason**

> The sequence and choices provide a meaningful basis to select D over the three biologically mismatched alternatives, although the precise plasma-membrane assignment is more specific than the targeting signals alone prove.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, plasma membrane is the only one consistent with the sequence’s membrane-protein features. The choices do not include other membrane compartments that could be harder to distinguish.


### Important caveats

- The cited UniProt cell-membrane annotation and GO plasma-membrane annotations are distinct forms of evidence; the GO assignment is computational, and the cited annotation excerpt is not itself a report of a direct localization assay.
- A membrane-targeting sequence does not by itself guarantee plasma-membrane rather than another membrane localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal sequence, a large intervening non-hydrophobic region, and a hydrophobic segment near the C-terminus followed by a basic tail. This is consistent with a single-pass type I membrane protein and makes a membrane location much more plausible than a DNA-damage site, protein-DNA complex, or matrilin complex.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish plasma membrane localization over other cellular membranes; the record’s specific cell-membrane localization is additional item-specific annotation evidence.",
    "reason": "The sequence and choices provide a meaningful basis to select D over the three biologically mismatched alternatives, although the precise plasma-membrane assignment is more specific than the targeting signals alone prove."
  },
  "case_id": "GO_cellular_component_0168",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the zebrafish UniProt record, which annotates it to the cell membrane with a literature citation; GO treats “cell membrane” as an exact synonym of plasma membrane. The record also assigns plasma membrane through computational annotations. This supports D, though the excerpts do not independently establish the underlying experimental evidence."
  },
  "important_caveats": [
    "The cited UniProt cell-membrane annotation and GO plasma-membrane annotations are distinct forms of evidence; the GO assignment is computational, and the cited annotation excerpt is not itself a report of a direct localization assay.",
    "A membrane-targeting sequence does not by itself guarantee plasma-membrane rather than another membrane localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, plasma membrane is the only one consistent with the sequence’s membrane-protein features. The choices do not include other membrane compartments that could be harder to distinguish."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0168",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the zebrafish UniProt record, which annotates it to the cell membrane with a literature citation; GO treats “cell membrane” as an exact synonym of plasma membrane. The record also assigns plasma membrane through computational annotations. This supports D, though the excerpts do not independently establish the underlying experimental evidence.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal sequence, a large intervening non-hydrophobic region, and a hydrophobic segment near the C-terminus followed by a basic tail. This is consistent with a single-pass type I membrane protein and makes a membrane location much more plausible than a DNA-damage site, protein-DNA complex, or matrilin complex.",
    "missing_item_specific_fact": "The sequence alone does not establish plasma membrane localization over other cellular membranes; the record’s specific cell-membrane localization is additional item-specific annotation evidence.",
    "reason": "The sequence and choices provide a meaningful basis to select D over the three biologically mismatched alternatives, although the precise plasma-membrane assignment is more specific than the targeting signals alone prove."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, plasma membrane is the only one consistent with the sequence’s membrane-protein features. The choices do not include other membrane compartments that could be harder to distinguish."
  },
  "important_caveats": [
    "The cited UniProt cell-membrane annotation and GO plasma-membrane annotations are distinct forms of evidence; the GO assignment is computational, and the cited annotation excerpt is not itself a report of a direct localization assay.",
    "A membrane-targeting sequence does not by itself guarantee plasma-membrane rather than another membrane localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B8JI67 (Transmembrane protein 81, zebrafish) annotates the subcellular location as 'Cell membrane' with evidence code ECO:0000305 linked to PubMed:39423812 (a 2024 Cell paper on a conserved fertilization complex), and specifies 'Single-pass type I membrane protein' topology (ECO:0000255, computational). The GO cross-reference assigns GO:0005886 (plasma membrane) via IBA:GO_Central. The GO term GO:0005886 lists 'cell membrane' as an EXACT synonym. The sequence matches the benchmark input (259 aa, SHA256 confirmed). The expected answer D (plasma membrane) is directly supported by both the UniProt annotation and the GO assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmarks of a single-pass type I membrane protein: (1) an N-terminal hydrophobic stretch (MALSTLWLVLMLWTSLF) consistent with a cleavable signal peptide directing entry into the secretory pathway; (2) a large hydrophilic extracellular domain; (3) a highly hydrophobic stretch near the C-terminus (SFAIAVVIFIFLFC) consistent with a single transmembrane helix; and (4) a short basic cytoplasmic tail (RRARRAAHLCQDNI) following the TM segment. This signal→extracellular→TM→cytoplasmic topology is the defining architecture of a plasma-membrane-anchored type I protein. None of the distractors fit: a 'site of double-strand break' protein requires nuclear localization signals and DNA-damage-response domains; a 'protein-DNA complex' component requires DNA-binding motifs (zinc fingers, HTH, etc.); a 'matrilin complex' member requires EGF-like and cartilage matrix protein (CMP) domains characteristic of the matrilin family. The absence of any such features and the clear membrane-protein topology allow a knowledgeable biologist to select D without knowing the specific protein identity.


**Missing item-specific fact**

> None critical. Identifying the exact boundaries of the TM helix and confirming 'single-pass type I' topology with certainty benefits from prediction tools (e.g., TMHMM) or the UniProt annotation, but the gross sequence features are sufficient to distinguish D from the three clearly incompatible distractors.


**Reason**

> The sequence contains identifiable signal peptide and transmembrane-domain-like hydrophobic regions that, combined with the short basic C-terminal tail, form a recognizable type-I membrane protein topology. The three distractors (DSB site, protein-DNA complex, matrilin complex) each demand specific domain architectures (NLS + DDR motifs, DNA-binding domains, EGF/CMP domains) that are entirely absent from this sequence. General knowledge of protein targeting and GO term definitions is sufficient to eliminate them.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mutually exclusive and well-separated. Only plasma membrane is compatible with a signal-peptide-plus-TM-domain topology. The other three options require fundamentally different protein architectures (nuclear/DNA-binding or ECM-domain-containing) that are clearly absent. No ambiguity exists among the choices.


### Important caveats

- The UniProt subcellular-location annotation (ECO:0000305) is linked to a 2024 Cell paper (PubMed:39423812) on a fertilization complex, indicating experimental context (sperm surface localization), while the topology assignment (single-pass type I) is computational (ECO:0000255). The GO annotation uses IBA (Inferred by Biological Aspect), a computational transfer, not direct experimental GO curation.
- The protein is annotated as a 'Precursor' (signal peptide present), so the mature protein lacks the N-terminal signal sequence. This does not change the plasma-membrane assignment but is relevant to topology interpretation.
- The reviewer-only accession (B8JI67) and all annotations were absent from the evaluated model's input; the model must reason from the raw sequence and choices alone.
- The GO term GO:0005886 'plasma membrane' has 'cell membrane' as an EXACT synonym, matching the UniProt 'Cell membrane' annotation, so there is no terminology mismatch between the option text and the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmarks of a single-pass type I membrane protein: (1) an N-terminal hydrophobic stretch (MALSTLWLVLMLWTSLF) consistent with a cleavable signal peptide directing entry into the secretory pathway; (2) a large hydrophilic extracellular domain; (3) a highly hydrophobic stretch near the C-terminus (SFAIAVVIFIFLFC) consistent with a single transmembrane helix; and (4) a short basic cytoplasmic tail (RRARRAAHLCQDNI) following the TM segment. This signal→extracellular→TM→cytoplasmic topology is the defining architecture of a plasma-membrane-anchored type I protein. None of the distractors fit: a 'site of double-strand break' protein requires nuclear localization signals and DNA-damage-response domains; a 'protein-DNA complex' component requires DNA-binding motifs (zinc fingers, HTH, etc.); a 'matrilin complex' member requires EGF-like and cartilage matrix protein (CMP) domains characteristic of the matrilin family. The absence of any such features and the clear membrane-protein topology allow a knowledgeable biologist to select D without knowing the specific protein identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Identifying the exact boundaries of the TM helix and confirming 'single-pass type I' topology with certainty benefits from prediction tools (e.g., TMHMM) or the UniProt annotation, but the gross sequence features are sufficient to distinguish D from the three clearly incompatible distractors.",
    "reason": "The sequence contains identifiable signal peptide and transmembrane-domain-like hydrophobic regions that, combined with the short basic C-terminal tail, form a recognizable type-I membrane protein topology. The three distractors (DSB site, protein-DNA complex, matrilin complex) each demand specific domain architectures (NLS + DDR motifs, DNA-binding domains, EGF/CMP domains) that are entirely absent from this sequence. General knowledge of protein targeting and GO term definitions is sufficient to eliminate them."
  },
  "case_id": "GO_cellular_component_0168",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B8JI67 (Transmembrane protein 81, zebrafish) annotates the subcellular location as 'Cell membrane' with evidence code ECO:0000305 linked to PubMed:39423812 (a 2024 Cell paper on a conserved fertilization complex), and specifies 'Single-pass type I membrane protein' topology (ECO:0000255, computational). The GO cross-reference assigns GO:0005886 (plasma membrane) via IBA:GO_Central. The GO term GO:0005886 lists 'cell membrane' as an EXACT synonym. The sequence matches the benchmark input (259 aa, SHA256 confirmed). The expected answer D (plasma membrane) is directly supported by both the UniProt annotation and the GO assignment."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation (ECO:0000305) is linked to a 2024 Cell paper (PubMed:39423812) on a fertilization complex, indicating experimental context (sperm surface localization), while the topology assignment (single-pass type I) is computational (ECO:0000255). The GO annotation uses IBA (Inferred by Biological Aspect), a computational transfer, not direct experimental GO curation.",
    "The protein is annotated as a 'Precursor' (signal peptide present), so the mature protein lacks the N-terminal signal sequence. This does not change the plasma-membrane assignment but is relevant to topology interpretation.",
    "The reviewer-only accession (B8JI67) and all annotations were absent from the evaluated model's input; the model must reason from the raw sequence and choices alone.",
    "The GO term GO:0005886 'plasma membrane' has 'cell membrane' as an EXACT synonym, matching the UniProt 'Cell membrane' annotation, so there is no terminology mismatch between the option text and the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive and well-separated. Only plasma membrane is compatible with a signal-peptide-plus-TM-domain topology. The other three options require fundamentally different protein architectures (nuclear/DNA-binding or ECM-domain-containing) that are clearly absent. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0168",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B8JI67 (Transmembrane protein 81, zebrafish) annotates the subcellular location as 'Cell membrane' with evidence code ECO:0000305 linked to PubMed:39423812 (a 2024 Cell paper on a conserved fertilization complex), and specifies 'Single-pass type I membrane protein' topology (ECO:0000255, computational). The GO cross-reference assigns GO:0005886 (plasma membrane) via IBA:GO_Central. The GO term GO:0005886 lists 'cell membrane' as an EXACT synonym. The sequence matches the benchmark input (259 aa, SHA256 confirmed). The expected answer D (plasma membrane) is directly supported by both the UniProt annotation and the GO assignment.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmarks of a single-pass type I membrane protein: (1) an N-terminal hydrophobic stretch (MALSTLWLVLMLWTSLF) consistent with a cleavable signal peptide directing entry into the secretory pathway; (2) a large hydrophilic extracellular domain; (3) a highly hydrophobic stretch near the C-terminus (SFAIAVVIFIFLFC) consistent with a single transmembrane helix; and (4) a short basic cytoplasmic tail (RRARRAAHLCQDNI) following the TM segment. This signal→extracellular→TM→cytoplasmic topology is the defining architecture of a plasma-membrane-anchored type I protein. None of the distractors fit: a 'site of double-strand break' protein requires nuclear localization signals and DNA-damage-response domains; a 'protein-DNA complex' component requires DNA-binding motifs (zinc fingers, HTH, etc.); a 'matrilin complex' member requires EGF-like and cartilage matrix protein (CMP) domains characteristic of the matrilin family. The absence of any such features and the clear membrane-protein topology allow a knowledgeable biologist to select D without knowing the specific protein identity.",
    "missing_item_specific_fact": "None critical. Identifying the exact boundaries of the TM helix and confirming 'single-pass type I' topology with certainty benefits from prediction tools (e.g., TMHMM) or the UniProt annotation, but the gross sequence features are sufficient to distinguish D from the three clearly incompatible distractors.",
    "reason": "The sequence contains identifiable signal peptide and transmembrane-domain-like hydrophobic regions that, combined with the short basic C-terminal tail, form a recognizable type-I membrane protein topology. The three distractors (DSB site, protein-DNA complex, matrilin complex) each demand specific domain architectures (NLS + DDR motifs, DNA-binding domains, EGF/CMP domains) that are entirely absent from this sequence. General knowledge of protein targeting and GO term definitions is sufficient to eliminate them."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive and well-separated. Only plasma membrane is compatible with a signal-peptide-plus-TM-domain topology. The other three options require fundamentally different protein architectures (nuclear/DNA-binding or ECM-domain-containing) that are clearly absent. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation (ECO:0000305) is linked to a 2024 Cell paper (PubMed:39423812) on a fertilization complex, indicating experimental context (sperm surface localization), while the topology assignment (single-pass type I) is computational (ECO:0000255). The GO annotation uses IBA (Inferred by Biological Aspect), a computational transfer, not direct experimental GO curation.",
    "The protein is annotated as a 'Precursor' (signal peptide present), so the mature protein lacks the N-terminal signal sequence. This does not change the plasma-membrane assignment but is relevant to topology interpretation.",
    "The reviewer-only accession (B8JI67) and all annotations were absent from the evaluated model's input; the model must reason from the raw sequence and choices alone.",
    "The GO term GO:0005886 'plasma membrane' has 'cell membrane' as an EXACT synonym, matching the UniProt 'Cell membrane' annotation, so there is no terminology mismatch between the option text and the annotation."
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

**Accession:** `B8JI67` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 92. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8JI67.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.144269+00:00.  

```json
"B8JI67"
```

Source SHA-256: `f3f8005091c0912014ebf7b5bc0c98ba1bc6db24e53c5e397e47069aca9c868a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8JI67.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.144269+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"value":"Transmembrane protein 81"}}}
```

Source SHA-256: `f3f8005091c0912014ebf7b5bc0c98ba1bc6db24e53c5e397e47069aca9c868a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8JI67.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.144269+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"39423812","source":"PubMed"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9905","value":"Single-pass type I membrane protein"}}]}
```

Source SHA-256: `f3f8005091c0912014ebf7b5bc0c98ba1bc6db24e53c5e397e47069aca9c868a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8JI67.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.144269+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `f3f8005091c0912014ebf7b5bc0c98ba1bc6db24e53c5e397e47069aca9c868a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8JI67?format=txt&versions=92)  
**Locator:** `lines 70-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-01T06:27:55.829977+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:39423812};
CC       Single-pass type I membrane protein {ECO:0000255}.
```

Source SHA-256: `9a37db43c6aecf1d426aa96f8d8451400e467b3d3dd8984eb6e99dc85bc8509d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8JI67?format=txt&versions=92)  
**Locator:** `lines 99-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-01T06:27:55.829977+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `9a37db43c6aecf1d426aa96f8d8451400e467b3d3dd8984eb6e99dc85bc8509d`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 168. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
