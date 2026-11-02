# GO_cellular_component_0173

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — egg chorion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMMHSRNRSWTLTLLALGVVLATSAEDLPRSNRIAVPGEPLYYLMADAGPVVTPNEALKRTNRSLLKWWDDLFPRNNNNCCNNNNNNLLYPTAPLLPAPAVPNNCNGLQLQDLDPFKQMKLFKKLPELFPTASPCGQCGGGCGQNNYVAPAPQSPSYGGDGYGVLPNGGYIKPDTEYNGPGDGDAGYVAPAAPAYEAPAPPAPAYEAPAPPAPAYEAPAPAAPAYEAPAPAAPAYEAPTTDYSAPAPPAPAYEPPASSYTQGYSQPAQPSYVGAPPAQIVYQPIIYLSTPLASKSSTSQVEYDDQKYVTPTAPPPPPPPAPVYEAPSQNCYQPAAPPAPNYATPSCQTPIRLSLIDQPYRVAPELFEEYNYRLALASQNIL

[Multiple Choices]
A. ATAC complex
B. food vacuole
C. caveola
D. egg chorion
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

> The exact sequence matches the Drosophila protein palisade entry. Its egg-chorion GO annotation is supported by IDA:FlyBase evidence, and the cited experimental subcellular-location annotation says it is secreted into the perivitelline space and incorporated into the vitelline membrane.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus has a hydrophobic signal-peptide-like segment, while the rest of the sequence lacks an evident membrane-spanning segment, favoring a secreted protein over an intracellular ATAC subunit, a food-vacuole protein, or a caveolar membrane protein. Among the choices, egg chorion is the plausible extracellular destination.


**Missing item-specific fact**

> Sequence features alone do not establish the specific egg-associated destination; the protein-specific evidence that it is palisade and is incorporated into the vitelline membrane is absent from the question.


**Reason**

> The secretion signal and the contrast among the choices provide a concrete comparative biological basis for selecting D, although the precise egg-structure localization is not independently encoded by a general secretion signal.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports secretion, and D is the only listed extracellular structure; the other choices imply intracellular complexes or membrane-associated localization.


### Important caveats

- The reviewer-only sequence-matched annotation supports D but was not available to the evaluated model.
- The experimental location description specifies incorporation into the vitelline membrane; the egg-chorion assignment is a GO annotation for that protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus has a hydrophobic signal-peptide-like segment, while the rest of the sequence lacks an evident membrane-spanning segment, favoring a secreted protein over an intracellular ATAC subunit, a food-vacuole protein, or a caveolar membrane protein. Among the choices, egg chorion is the plausible extracellular destination.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Sequence features alone do not establish the specific egg-associated destination; the protein-specific evidence that it is palisade and is incorporated into the vitelline membrane is absent from the question.",
    "reason": "The secretion signal and the contrast among the choices provide a concrete comparative biological basis for selecting D, although the precise egg-structure localization is not independently encoded by a general secretion signal."
  },
  "case_id": "GO_cellular_component_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila protein palisade entry. Its egg-chorion GO annotation is supported by IDA:FlyBase evidence, and the cited experimental subcellular-location annotation says it is secreted into the perivitelline space and incorporated into the vitelline membrane."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched annotation supports D but was not available to the evaluated model.",
    "The experimental location description specifies incorporation into the vitelline membrane; the egg-chorion assignment is a GO annotation for that protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports secretion, and D is the only listed extracellular structure; the other choices imply intracellular complexes or membrane-associated localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila protein palisade entry. Its egg-chorion GO annotation is supported by IDA:FlyBase evidence, and the cited experimental subcellular-location annotation says it is secreted into the perivitelline space and incorporated into the vitelline membrane.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a hydrophobic signal-peptide-like segment, while the rest of the sequence lacks an evident membrane-spanning segment, favoring a secreted protein over an intracellular ATAC subunit, a food-vacuole protein, or a caveolar membrane protein. Among the choices, egg chorion is the plausible extracellular destination.",
    "missing_item_specific_fact": "Sequence features alone do not establish the specific egg-associated destination; the protein-specific evidence that it is palisade and is incorporated into the vitelline membrane is absent from the question.",
    "reason": "The secretion signal and the contrast among the choices provide a concrete comparative biological basis for selecting D, although the precise egg-structure localization is not independently encoded by a general secretion signal."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports secretion, and D is the only listed extracellular structure; the other choices imply intracellular complexes or membrane-associated localization."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched annotation supports D but was not available to the evaluated model.",
    "The experimental location description specifies incorporation into the vitelline membrane; the egg-chorion assignment is a GO annotation for that protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9VMK3 (Protein palisade, Drosophila melanogaster) carries GO:0042600 'egg chorion' with IDA:FlyBase evidence (evidence C6/H4), indicating direct experimental annotation. The subcellular location comment (C5/H3) states the protein is 'Secreted into the perivitelline space by follicle cells and becomes incorporated into the vitelline membrane,' and GO:0060388 'vitelline envelope' (IDA:FlyBase, C8/H6) further corroborates the egg-shell association. The sequence matches the benchmark input exactly (SHA256 confirmed).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'MMMHSRNRSWTLTLLALGVVLATSAEDLPRSNRIAVPGEPLYYLMADAGPVVTPNEALKRTNRSLLKWWDDLFPRNNNNCCNNNNNNLLYPTAPLLPAPAVPNNCNGLQLQDLDPFKQMKLFKKLPELFPTASPCGQCGGGCGQNNY' contains a clear hydrophobic signal peptide (residues ~1-19), indicating the protein enters the secretory pathway and is exported from the cell. Among the four options: (A) ATAC complex is a nuclear chromatin-remodeling complex — incompatible with a secreted protein; (B) food vacuole is an intracellular digestive compartment specific to parasites (Apicomplexa per GO definition) — incompatible with a secreted extracellular protein; (C) caveola is a plasma-membrane invagination — incompatible with a fully secreted protein. Only (D) egg chorion is an extracellular structure, consistent with a signal-peptide-bearing secreted protein. The proline-rich repetitive motifs (PAPAYEAPAPPAPAYEAP…) and cysteine clusters are also characteristic of structural extracellular-matrix proteins found in insect egg shells.


**Missing item-specific fact**

> None strictly required; the elimination logic (signal peptide → secreted → extracellular → only extracellular option) relies on general cell biology. Positive identification of 'egg chorion' specifically (vs. any other extracellular structure) benefits from knowledge of insect chorion/vitelline protein composition but is not strictly necessary given the four options.


**Reason**

> A model with general knowledge of signal peptides, secretion, and the cellular nature of each GO term can eliminate A (nuclear), B (intracellular parasite organelle), and C (membrane) to arrive at D (extracellular). The proline/glycine/cysteine-rich secreted-protein architecture further supports an extracellular structural role consistent with chorion.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct cellular localizations (nuclear complex, parasite intracellular organelle, plasma-membrane structure, extracellular structure). A secreted protein with a signal peptide is unambiguously incompatible with the first three, leaving egg chorion as the only viable option.


### Important caveats

- The GO annotation 'egg chorion' (GO:0042600) has IDA:FlyBase evidence, meaning it was assigned by direct assay in FlyBase, not purely by sequence similarity. The vitelline membrane and chorion are closely related but distinct egg-shell layers; the protein is more precisely described as a vitelline membrane component, but FlyBase also annotates it to egg chorion.
- The organism (Drosophila melanogaster) is not explicitly stated in the model input; recognition of the organism relies on sequence features or prior knowledge. However, the elimination logic does not strictly require knowing the organism — a secreted protein cannot reside in a nuclear complex, a parasite-specific food vacuole, or a membrane invagination.
- The reviewer-only evidence confirms sequence identity (SHA256 match) and that the GO:0042600 annotation predates the benchmark cutoff (entry version 166, first released 2026-01-28).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MMMHSRNRSWTLTLLALGVVLATSAEDLPRSNRIAVPGEPLYYLMADAGPVVTPNEALKRTNRSLLKWWDDLFPRNNNNCCNNNNNNLLYPTAPLLPAPAVPNNCNGLQLQDLDPFKQMKLFKKLPELFPTASPCGQCGGGCGQNNY' contains a clear hydrophobic signal peptide (residues ~1-19), indicating the protein enters the secretory pathway and is exported from the cell. Among the four options: (A) ATAC complex is a nuclear chromatin-remodeling complex — incompatible with a secreted protein; (B) food vacuole is an intracellular digestive compartment specific to parasites (Apicomplexa per GO definition) — incompatible with a secreted extracellular protein; (C) caveola is a plasma-membrane invagination — incompatible with a fully secreted protein. Only (D) egg chorion is an extracellular structure, consistent with a signal-peptide-bearing secreted protein. The proline-rich repetitive motifs (PAPAYEAPAPPAPAYEAP…) and cysteine clusters are also characteristic of structural extracellular-matrix proteins found in insect egg shells.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; the elimination logic (signal peptide → secreted → extracellular → only extracellular option) relies on general cell biology. Positive identification of 'egg chorion' specifically (vs. any other extracellular structure) benefits from knowledge of insect chorion/vitelline protein composition but is not strictly necessary given the four options.",
    "reason": "A model with general knowledge of signal peptides, secretion, and the cellular nature of each GO term can eliminate A (nuclear), B (intracellular parasite organelle), and C (membrane) to arrive at D (extracellular). The proline/glycine/cysteine-rich secreted-protein architecture further supports an extracellular structural role consistent with chorion."
  },
  "case_id": "GO_cellular_component_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9VMK3 (Protein palisade, Drosophila melanogaster) carries GO:0042600 'egg chorion' with IDA:FlyBase evidence (evidence C6/H4), indicating direct experimental annotation. The subcellular location comment (C5/H3) states the protein is 'Secreted into the perivitelline space by follicle cells and becomes incorporated into the vitelline membrane,' and GO:0060388 'vitelline envelope' (IDA:FlyBase, C8/H6) further corroborates the egg-shell association. The sequence matches the benchmark input exactly (SHA256 confirmed)."
  },
  "important_caveats": [
    "The GO annotation 'egg chorion' (GO:0042600) has IDA:FlyBase evidence, meaning it was assigned by direct assay in FlyBase, not purely by sequence similarity. The vitelline membrane and chorion are closely related but distinct egg-shell layers; the protein is more precisely described as a vitelline membrane component, but FlyBase also annotates it to egg chorion.",
    "The organism (Drosophila melanogaster) is not explicitly stated in the model input; recognition of the organism relies on sequence features or prior knowledge. However, the elimination logic does not strictly require knowing the organism — a secreted protein cannot reside in a nuclear complex, a parasite-specific food vacuole, or a membrane invagination.",
    "The reviewer-only evidence confirms sequence identity (SHA256 match) and that the GO:0042600 annotation predates the benchmark cutoff (entry version 166, first released 2026-01-28)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct cellular localizations (nuclear complex, parasite intracellular organelle, plasma-membrane structure, extracellular structure). A secreted protein with a signal peptide is unambiguously incompatible with the first three, leaving egg chorion as the only viable option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9VMK3 (Protein palisade, Drosophila melanogaster) carries GO:0042600 'egg chorion' with IDA:FlyBase evidence (evidence C6/H4), indicating direct experimental annotation. The subcellular location comment (C5/H3) states the protein is 'Secreted into the perivitelline space by follicle cells and becomes incorporated into the vitelline membrane,' and GO:0060388 'vitelline envelope' (IDA:FlyBase, C8/H6) further corroborates the egg-shell association. The sequence matches the benchmark input exactly (SHA256 confirmed).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'MMMHSRNRSWTLTLLALGVVLATSAEDLPRSNRIAVPGEPLYYLMADAGPVVTPNEALKRTNRSLLKWWDDLFPRNNNNCCNNNNNNLLYPTAPLLPAPAVPNNCNGLQLQDLDPFKQMKLFKKLPELFPTASPCGQCGGGCGQNNY' contains a clear hydrophobic signal peptide (residues ~1-19), indicating the protein enters the secretory pathway and is exported from the cell. Among the four options: (A) ATAC complex is a nuclear chromatin-remodeling complex — incompatible with a secreted protein; (B) food vacuole is an intracellular digestive compartment specific to parasites (Apicomplexa per GO definition) — incompatible with a secreted extracellular protein; (C) caveola is a plasma-membrane invagination — incompatible with a fully secreted protein. Only (D) egg chorion is an extracellular structure, consistent with a signal-peptide-bearing secreted protein. The proline-rich repetitive motifs (PAPAYEAPAPPAPAYEAP…) and cysteine clusters are also characteristic of structural extracellular-matrix proteins found in insect egg shells.",
    "missing_item_specific_fact": "None strictly required; the elimination logic (signal peptide → secreted → extracellular → only extracellular option) relies on general cell biology. Positive identification of 'egg chorion' specifically (vs. any other extracellular structure) benefits from knowledge of insect chorion/vitelline protein composition but is not strictly necessary given the four options.",
    "reason": "A model with general knowledge of signal peptides, secretion, and the cellular nature of each GO term can eliminate A (nuclear), B (intracellular parasite organelle), and C (membrane) to arrive at D (extracellular). The proline/glycine/cysteine-rich secreted-protein architecture further supports an extracellular structural role consistent with chorion."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct cellular localizations (nuclear complex, parasite intracellular organelle, plasma-membrane structure, extracellular structure). A secreted protein with a signal peptide is unambiguously incompatible with the first three, leaving egg chorion as the only viable option."
  },
  "important_caveats": [
    "The GO annotation 'egg chorion' (GO:0042600) has IDA:FlyBase evidence, meaning it was assigned by direct assay in FlyBase, not purely by sequence similarity. The vitelline membrane and chorion are closely related but distinct egg-shell layers; the protein is more precisely described as a vitelline membrane component, but FlyBase also annotates it to egg chorion.",
    "The organism (Drosophila melanogaster) is not explicitly stated in the model input; recognition of the organism relies on sequence features or prior knowledge. However, the elimination logic does not strictly require knowing the organism — a secreted protein cannot reside in a nuclear complex, a parasite-specific food vacuole, or a membrane invagination.",
    "The reviewer-only evidence confirms sequence identity (SHA256 match) and that the GO:0042600 annotation predates the benchmark cutoff (entry version 166, first released 2026-01-28)."
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

**Accession:** `Q9VMK3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 166. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:28.895931+00:00.  

```json
"Q9VMK3"
```

Source SHA-256: `e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:28.895931+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18514182","source":"PubMed"},{"evidenceCode":"ECO:0000312","id":"FBgn0086265","source":"FlyBase"}],"value":"Protein palisade"}}}
```

Source SHA-256: `e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:28.895931+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18514182","source":"PubMed"}],"value":"Secreted into the perivitelline space by follicle cells and becomes incorporated into the vitelline membrane"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"18514182","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"18514182","source":"PubMed"}],"id":"SL-0111","value":"Secreted, extracellular space, extracellular matrix"}}]}
```

Source SHA-256: `e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)  
**Locator:** `/uniProtKBCrossReferences/30`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:28.895931+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"16515779","source":"PubMed"}],"id":"GO:0042600","properties":[{"key":"GoTerm","value":"C:egg chorion"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)  
**Locator:** `/uniProtKBCrossReferences/32`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:28.895931+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"18514182","source":"PubMed"}],"id":"GO:0060388","properties":[{"key":"GoTerm","value":"C:vitelline envelope"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166)  
**Locator:** `lines 90-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 166 / 2.  
**Retrieved:** 2026-11-02T04:33:31.077925+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000269|PubMed:18514182}. Secreted,
CC       extracellular space, extracellular matrix
CC       {ECO:0000269|PubMed:18514182}. Note=Secreted into the perivitelline
CC       space by follicle cells and becomes incorporated into the vitelline
CC       membrane. {ECO:0000269|PubMed:18514182}.
```

Source SHA-256: `e29e678a73bb740d92e70bafa920eafb90e0bfe6e683dd2672c8a1a7d8834a98`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166)  
**Locator:** `lines 152-152`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 166 / 2.  
**Retrieved:** 2026-11-02T04:33:31.077925+00:00.  

```text
DR   GO; GO:0042600; C:egg chorion; IDA:FlyBase.
```

Source SHA-256: `e29e678a73bb740d92e70bafa920eafb90e0bfe6e683dd2672c8a1a7d8834a98`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166)  
**Locator:** `lines 154-154`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 166 / 2.  
**Retrieved:** 2026-11-02T04:33:31.077925+00:00.  

```text
DR   GO; GO:0060388; C:vitelline envelope; IDA:FlyBase.
```

Source SHA-256: `e29e678a73bb740d92e70bafa920eafb90e0bfe6e683dd2672c8a1a7d8834a98`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 173. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
