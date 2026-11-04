# GO_cellular_component_0054

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0054.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTQLPYLLDRRGGALAAPATAWGDMMLNRALFSVALLSSVGSAWVVLSYACIKELRSYRHQLILGLAISDLLMSLNFMFSAGWNVAGGDLALEESRTACSVNGFLTQVFVVQTDWWILVIAIATYIILGNFKTQSQFIQTHVWIPWVGPWVLSIIIAAICHGVLGYGYIGGWCWLTSDLMRLLINFIPRWLIVIAIALIYIRLYMIVRKARKWDIEGVSPDPGDDMADTSVILMSVGKKDRERQGSGVLVSRDVSVSFGRKGSTAPTFVTMVTTSGAGDSREAISSCSAREEGSRARTVNVNSSRSLSLGMRQPLNAAQLKRIAKKMMVYPVAYAIIWACPTAIRIYQGTTGSRAPLWITIVDKSCIVIQGLVDAVVYGLNERAWQGWRDHIRRIIYKNEGGRIIG

[Multiple Choices]
A. cell leading edge
B. plasma membrane
C. endoplasmic reticulum
D. cell surface
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched record reports cell-membrane localization with experimental evidence and notes ligand-induced relocalization to the vacuole (C5, H3). The record also assigns plasma membrane by computational annotation (C6, H4). The experimental cell-membrane localization supports the keyed plasma-membrane choice, while the vacuolar relocation is a condition-dependent caveat.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long hydrophobic segments consistent with a multi-pass membrane protein, and its overall architecture is GPCR-like. Transferable knowledge that GPCRs are generally cell-surface receptors makes plasma membrane a meaningful choice over ER or cell leading edge. The sequence alone does not establish exact trafficking or localization under every condition.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family/architecture-based inference from the supplied sequence meaningfully favors plasma membrane among the choices. This supports a probabilistic prediction without relying on the target's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Cell surface can describe proteins integrated into or attached to the plasma membrane, so it can overlap with plasma membrane for an integral receptor. Plasma membrane is the more direct compartment-level choice, but the alternatives do not make the two descriptions fully exclusive.


### Important caveats

- The sequence-matched record reports ligand-associated relocation to the vacuole, so localization may depend on stimulation state.
- The plasma-membrane GO assignment is computational; the cited cell-membrane localization has experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic segments consistent with a multi-pass membrane protein, and its overall architecture is GPCR-like. Transferable knowledge that GPCRs are generally cell-surface receptors makes plasma membrane a meaningful choice over ER or cell leading edge. The sequence alone does not establish exact trafficking or localization under every condition.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family/architecture-based inference from the supplied sequence meaningfully favors plasma membrane among the choices. This supports a probabilistic prediction without relying on the target's database record."
  },
  "case_id": "GO_cellular_component_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record reports cell-membrane localization with experimental evidence and notes ligand-induced relocalization to the vacuole (C5, H3). The record also assigns plasma membrane by computational annotation (C6, H4). The experimental cell-membrane localization supports the keyed plasma-membrane choice, while the vacuolar relocation is a condition-dependent caveat."
  },
  "important_caveats": [
    "The sequence-matched record reports ligand-associated relocation to the vacuole, so localization may depend on stimulation state.",
    "The plasma-membrane GO assignment is computational; the cited cell-membrane localization has experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Cell surface can describe proteins integrated into or attached to the plasma membrane, so it can overlap with plasma membrane for an integral receptor. Plasma membrane is the more direct compartment-level choice, but the alternatives do not make the two descriptions fully exclusive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record reports cell-membrane localization with experimental evidence and notes ligand-induced relocalization to the vacuole (C5, H3). The record also assigns plasma membrane by computational annotation (C6, H4). The experimental cell-membrane localization supports the keyed plasma-membrane choice, while the vacuolar relocation is a condition-dependent caveat.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic segments consistent with a multi-pass membrane protein, and its overall architecture is GPCR-like. Transferable knowledge that GPCRs are generally cell-surface receptors makes plasma membrane a meaningful choice over ER or cell leading edge. The sequence alone does not establish exact trafficking or localization under every condition.",
    "missing_item_specific_fact": "",
    "reason": "A family/architecture-based inference from the supplied sequence meaningfully favors plasma membrane among the choices. This supports a probabilistic prediction without relying on the target's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Cell surface can describe proteins integrated into or attached to the plasma membrane, so it can overlap with plasma membrane for an integral receptor. Plasma membrane is the more direct compartment-level choice, but the alternatives do not make the two descriptions fully exclusive."
  },
  "important_caveats": [
    "The sequence-matched record reports ligand-associated relocation to the vacuole, so localization may depend on stimulation state.",
    "The plasma-membrane GO assignment is computational; the cited cell-membrane localization has experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (G1X9E2, Ascaroside receptor GPR2) annotates the protein as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269|PubMed:38649409). The GO cross-reference assigns GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym per the ontology. The protein is a GPCR with multiple transmembrane helices, consistent with plasma membrane localization. The note about vacuolar relocalization upon ligand stimulation does not contradict the primary plasma membrane location.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches (~7 transmembrane helices) with conserved GPCR motifs (e.g., NxxQ in TM6, the DRY-like motif region 'RKARK', and the characteristic intracellular loop with phosphorylation sites). This identifies the protein as a G protein-coupled receptor. GPCRs are the textbook example of integral plasma membrane proteins. This distinguishes B (plasma membrane) from C (endoplasmic reticulum, where proteins are transiently processed but not resident) and from A (cell leading edge, a term specific to motile animal cells, irrelevant to a fungus). The distinction between B and D (cell surface) rests on the GO definitions: 'plasma membrane' (GO:0005886) is the membrane itself, while 'cell surface' (GO:0009986) refers to 'the external part of the cell wall and/or plasma membrane'—in fungi, this typically denotes cell wall-associated or GPI-anchored proteins on the exterior. A multi-pass integral membrane protein like a GPCR is embedded within the plasma membrane, not merely attached to the cell surface. Standard GO annotation practice assigns GPCRs to GO:0005886, not GO:0009986.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the GPCR family from sequence features (multiple TM helices, conserved motifs) and applying the well-established principle that GPCRs are integral plasma membrane proteins provides a concrete, transferable inference that meaningfully selects B over the other choices. The B-vs-D distinction follows from the GO term definitions and the standard practice of annotating multi-pass membrane receptors to 'plasma membrane' rather than 'cell surface.'


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B (plasma membrane) and D (cell surface) are both membrane-related, the GO definitions and standard annotation practice for multi-pass membrane proteins clearly favor 'plasma membrane.' The 'cell surface' term is defined as the external part of cell wall/plasma membrane and is typically reserved for cell wall-associated or peripherally attached proteins, not integral multi-pass receptors. A and C are clearly excluded by GPCR biology and fungal cell biology.


### Important caveats

- The UniProt GO annotation for plasma membrane carries IEA:UniProtKB-SubCell evidence code (automatically assigned from the 'Cell membrane' subcellular location comment), but the underlying subcellular location comment itself has experimental evidence (ECO:0000269|PubMed:38649409).
- The protein relocalizes to the vacuole upon ligand stimulation, but its primary/steady-state location is the plasma membrane.
- The distinction between 'plasma membrane' and 'cell surface' in fungi involves the cell wall; a GPCR in the plasma membrane is technically beneath the cell wall exterior, further supporting B over D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches (~7 transmembrane helices) with conserved GPCR motifs (e.g., NxxQ in TM6, the DRY-like motif region 'RKARK', and the characteristic intracellular loop with phosphorylation sites). This identifies the protein as a G protein-coupled receptor. GPCRs are the textbook example of integral plasma membrane proteins. This distinguishes B (plasma membrane) from C (endoplasmic reticulum, where proteins are transiently processed but not resident) and from A (cell leading edge, a term specific to motile animal cells, irrelevant to a fungus). The distinction between B and D (cell surface) rests on the GO definitions: 'plasma membrane' (GO:0005886) is the membrane itself, while 'cell surface' (GO:0009986) refers to 'the external part of the cell wall and/or plasma membrane'—in fungi, this typically denotes cell wall-associated or GPI-anchored proteins on the exterior. A multi-pass integral membrane protein like a GPCR is embedded within the plasma membrane, not merely attached to the cell surface. Standard GO annotation practice assigns GPCRs to GO:0005886, not GO:0009986.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the GPCR family from sequence features (multiple TM helices, conserved motifs) and applying the well-established principle that GPCRs are integral plasma membrane proteins provides a concrete, transferable inference that meaningfully selects B over the other choices. The B-vs-D distinction follows from the GO term definitions and the standard practice of annotating multi-pass membrane receptors to 'plasma membrane' rather than 'cell surface.'"
  },
  "case_id": "GO_cellular_component_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (G1X9E2, Ascaroside receptor GPR2) annotates the protein as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269|PubMed:38649409). The GO cross-reference assigns GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym per the ontology. The protein is a GPCR with multiple transmembrane helices, consistent with plasma membrane localization. The note about vacuolar relocalization upon ligand stimulation does not contradict the primary plasma membrane location."
  },
  "important_caveats": [
    "The UniProt GO annotation for plasma membrane carries IEA:UniProtKB-SubCell evidence code (automatically assigned from the 'Cell membrane' subcellular location comment), but the underlying subcellular location comment itself has experimental evidence (ECO:0000269|PubMed:38649409).",
    "The protein relocalizes to the vacuole upon ligand stimulation, but its primary/steady-state location is the plasma membrane.",
    "The distinction between 'plasma membrane' and 'cell surface' in fungi involves the cell wall; a GPCR in the plasma membrane is technically beneath the cell wall exterior, further supporting B over D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B (plasma membrane) and D (cell surface) are both membrane-related, the GO definitions and standard annotation practice for multi-pass membrane proteins clearly favor 'plasma membrane.' The 'cell surface' term is defined as the external part of cell wall/plasma membrane and is typically reserved for cell wall-associated or peripherally attached proteins, not integral multi-pass receptors. A and C are clearly excluded by GPCR biology and fungal cell biology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (G1X9E2, Ascaroside receptor GPR2) annotates the protein as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269|PubMed:38649409). The GO cross-reference assigns GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym per the ontology. The protein is a GPCR with multiple transmembrane helices, consistent with plasma membrane localization. The note about vacuolar relocalization upon ligand stimulation does not contradict the primary plasma membrane location.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches (~7 transmembrane helices) with conserved GPCR motifs (e.g., NxxQ in TM6, the DRY-like motif region 'RKARK', and the characteristic intracellular loop with phosphorylation sites). This identifies the protein as a G protein-coupled receptor. GPCRs are the textbook example of integral plasma membrane proteins. This distinguishes B (plasma membrane) from C (endoplasmic reticulum, where proteins are transiently processed but not resident) and from A (cell leading edge, a term specific to motile animal cells, irrelevant to a fungus). The distinction between B and D (cell surface) rests on the GO definitions: 'plasma membrane' (GO:0005886) is the membrane itself, while 'cell surface' (GO:0009986) refers to 'the external part of the cell wall and/or plasma membrane'—in fungi, this typically denotes cell wall-associated or GPI-anchored proteins on the exterior. A multi-pass integral membrane protein like a GPCR is embedded within the plasma membrane, not merely attached to the cell surface. Standard GO annotation practice assigns GPCRs to GO:0005886, not GO:0009986.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the GPCR family from sequence features (multiple TM helices, conserved motifs) and applying the well-established principle that GPCRs are integral plasma membrane proteins provides a concrete, transferable inference that meaningfully selects B over the other choices. The B-vs-D distinction follows from the GO term definitions and the standard practice of annotating multi-pass membrane receptors to 'plasma membrane' rather than 'cell surface.'"
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B (plasma membrane) and D (cell surface) are both membrane-related, the GO definitions and standard annotation practice for multi-pass membrane proteins clearly favor 'plasma membrane.' The 'cell surface' term is defined as the external part of cell wall/plasma membrane and is typically reserved for cell wall-associated or peripherally attached proteins, not integral multi-pass receptors. A and C are clearly excluded by GPCR biology and fungal cell biology."
  },
  "important_caveats": [
    "The UniProt GO annotation for plasma membrane carries IEA:UniProtKB-SubCell evidence code (automatically assigned from the 'Cell membrane' subcellular location comment), but the underlying subcellular location comment itself has experimental evidence (ECO:0000269|PubMed:38649409).",
    "The protein relocalizes to the vacuole upon ligand stimulation, but its primary/steady-state location is the plasma membrane.",
    "The distinction between 'plasma membrane' and 'cell surface' in fungi involves the cell wall; a GPCR in the plasma membrane is technically beneath the cell wall exterior, further supporting B over D."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 406,
  "benchmark_sequence_sha256": "4e764ad5fe8865d73836f34a410857326f248f960936c909cff720a56696f0f3",
  "current_entry_audit": {
    "entryVersion": 47,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 406,
  "current_source_sequence_sha256": "4e764ad5fe8865d73836f34a410857326f248f960936c909cff720a56696f0f3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 45,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G1X9E2",
  "selected_historical_entry_version": 45,
  "selected_historical_record_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "selected_historical_source_sequence_length": 406,
  "selected_historical_source_sequence_sha256": "4e764ad5fe8865d73836f34a410857326f248f960936c909cff720a56696f0f3",
  "selected_historical_version": {
    "accession": "G1X9E2",
    "database": "Swiss-Prot",
    "entryVersion": 45,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GPR2_ARTOA",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G1X9E2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":47,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Nematode-trapping fungus\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008784\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Orbiliomycetes\",\"Orbiliales\",\"Orbiliaceae\",\"Orbilia\",\"Orbilia oligospora\"],\"scientificName\":\"Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\",\"synonyms\":[\"Didymozoophaga oligospora\"],\"taxonId\":756982}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Ascaroside receptor GPR2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38649409\",\"source\":\"PubMed\"}],\"value\":\"Relocalizes to the vacuole following stimulation by ligand\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38649409\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Kuo C.Y.\",\"Tay R.J.\",\"Lin H.C.\",\"Juan S.C.\",\"Vidal-Diez de Ulzurrun G.\",\"Chang Y.C.\",\"Hoki J.\",\"Schroeder F.C.\",\"Hsueh Y.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38649409\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41564-024-01679-w\"}],\"citationType\":\"journal article\",\"firstPage\":\"1738\",\"id\":\"38649409\",\"journal\":\"Nat. Microbiol.\",\"lastPage\":\"1751\",\"publicationDate\":\"2024\",\"title\":\"The nematode-trapping fungus Arthrobotrys oligospora detects prey pheromones via G protein-coupled receptors.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38649409\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"TWF154\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH GPA2 AND GPR3\",\"SUBCELLULAR LOCATION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H1",
  "excerpt": "ID   GPR2_ARTOA              Reviewed;         406 AA.\nAC   G1X9E2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 45.\nDE   RecName: Full=Ascaroside receptor GPR2 {ECO:0000305};\nGN   Name=GPR2 {ECO:0000303|PubMed:38649409};\nGN   ORFNames=AOL_s00076g249 {ECO:0000312|EMBL:EGX50174.1};\nOS   Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\nOS   (Nematode-trapping fungus) (Didymozoophaga oligospora).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Orbiliomycetes;\nOC   Orbiliales; Orbiliaceae; Orbilia; Orbilia oligospora.\nOX   NCBI_TaxID=756982 {ECO:0000312|Proteomes:UP000008784};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH GPA2 AND GPR3, SUBCELLULAR LOCATION, INDUCTION,\nRP   AND DISRUPTION PHENOTYPE.\nRC   STRAIN=TWF154 {ECO:0000303|PubMed:38649409};\nRX   PubMed=38649409; DOI=10.1038/s41564-024-01679-w;\nRA   Kuo C.Y., Tay R.J., Lin H.C., Juan S.C., Vidal-Diez de Ulzurrun G.,\nRA   Chang Y.C., Hoki J., Schroeder F.C., Hsueh Y.P.;\nRT   \"The nematode-trapping fungus Arthrobotrys oligospora detects prey\nRT   pheromones via G protein-coupled receptors.\";\nRL   Nat. Microbiol. 9:1738-1751(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:38649409};\nCC       Multi-pass membrane protein {ECO:0000255}. Note=Relocalizes to the\nCC       vacuole following stimulation by ligand. {ECO:0000269|PubMed:38649409}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005783\nname: endoplasmic reticulum\nnamespace: cellular_component\ndef: \"The irregular network of unit membranes, visible only by electron microscopy, that occurs in the cytoplasm of many eukaryotic cells. The membranes form a complex meshwork of tubular channels, which are often expanded into slitlike cavities called cisternae. The ER takes two forms, rough (or granular), with ribosomes adhering to the outer surface, and smooth (with no ribosomes attached).\" [ISBN:0198506732]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"ER\" EXACT []\nxref: NIF_Subcellular:sao1036339110\nxref: Wikipedia:Endoplasmic_reticulum\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\nrelationship: part_of GO:0012505 ! endomembrane system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005783",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59450-59472",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60420-60454",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0009986\nname: cell surface\nnamespace: cellular_component\nalt_id: GO:0009928\nalt_id: GO:0009929\ndef: \"The external part of the cell wall and/or plasma membrane.\" [GOC:jl, GOC:mtg_sensu, GOC:sm]\ncomment: Note that this term is intended to annotate gene products that are attached (integrated or loosely bound) to the plasma membrane or cell wall.\nsubset: goslim_pir\nsynonym: \"cell associated\" EXACT []\nsynonym: \"cell bound\" EXACT []\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009986",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 101772-101784",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0031252\nname: cell leading edge\nnamespace: cellular_component\ndef: \"The area of a motile cell closest to the direction of movement.\" [GOC:pg]\nsubset: goslim_pir\nsynonym: \"front of cell\" EXACT []\nsynonym: \"leading edge of cell\" EXACT []\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031252",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 174523-174532",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 54. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
