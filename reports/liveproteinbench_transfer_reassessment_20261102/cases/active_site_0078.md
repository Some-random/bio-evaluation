# active_site_0078

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0078.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 67 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDGKVQVLDFIKINPAGNITILIDNFDIYDKNIPKLSEEIMKETNLYAEQVGFIKEKHLQMMGGEFCGNASRSFASLLAFRDKDFSEQKNYSITCSGESEVLDVDVRTDGAKNKFLAKIKMPKFISLEEISIDEYKLGLVRFSGISHFIFNIKENKETSFENIIDLVKKYLSNEDYSAFGIMFFDKDNLSMKPYVYVKELESGIYENSCASGTTALGYYLKKYKNLDRAKVVQPNGWLEYIIENDEMYIDGPVEIVAEGKVYI

[Multiple Choices]
A. Position 64 (Nucleophile (Probable))
B. Position 67 (Proton acceptor)
C. Position 8 (Nucleophile)
D. Position 143 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies residue 67 as the proton acceptor. This supports choice B, though the annotation is transferred by similarity rather than direct experimental evidence for this exact residue in this protein.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has cysteine at position 67, while the other choices nominate leucine at 8, glycine at 64, or serine at 143. A cysteine-dependent racemase-like active site is a plausible family-level inference from the sequence and transferable knowledge of amino-acid racemases; that makes position 67 substantially more credible as a catalytic acid/base residue than the alternatives. This supports B probabilistically, though the exact proton-acceptor role is not established from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A sequence-based catalytic-residue and family inference meaningfully distinguishes B among these choices; the exact target's database annotation is not necessary to make that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered positions, only position 67 is a plausible catalytic cysteine; the other listed residues do not provide an equally defensible alternative.


### Important caveats

- The cited active-site annotation is transferred from another UniProt entry, not shown here to be experimentally validated on this exact protein.
- The sequence supports a plausible family-level inference, but does not by itself prove the precise catalytic role assigned to residue 67.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has cysteine at position 67, while the other choices nominate leucine at 8, glycine at 64, or serine at 143. A cysteine-dependent racemase-like active site is a plausible family-level inference from the sequence and transferable knowledge of amino-acid racemases; that makes position 67 substantially more credible as a catalytic acid/base residue than the alternatives. This supports B probabilistically, though the exact proton-acceptor role is not established from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A sequence-based catalytic-residue and family inference meaningfully distinguishes B among these choices; the exact target's database annotation is not necessary to make that distinction."
  },
  "case_id": "active_site_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 67 as the proton acceptor. This supports choice B, though the annotation is transferred by similarity rather than direct experimental evidence for this exact residue in this protein."
  },
  "important_caveats": [
    "The cited active-site annotation is transferred from another UniProt entry, not shown here to be experimentally validated on this exact protein.",
    "The sequence supports a plausible family-level inference, but does not by itself prove the precise catalytic role assigned to residue 67."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered positions, only position 67 is a plausible catalytic cysteine; the other listed residues do not provide an equally defensible alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 67 as the proton acceptor. This supports choice B, though the annotation is transferred by similarity rather than direct experimental evidence for this exact residue in this protein.",
    "evidence_ids": ["H3", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has cysteine at position 67, while the other choices nominate leucine at 8, glycine at 64, or serine at 143. A cysteine-dependent racemase-like active site is a plausible family-level inference from the sequence and transferable knowledge of amino-acid racemases; that makes position 67 substantially more credible as a catalytic acid/base residue than the alternatives. This supports B probabilistically, though the exact proton-acceptor role is not established from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "A sequence-based catalytic-residue and family inference meaningfully distinguishes B among these choices; the exact target's database annotation is not necessary to make that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered positions, only position 67 is a plausible catalytic cysteine; the other listed residues do not provide an equally defensible alternative."
  },
  "important_caveats": [
    "The cited active-site annotation is transferred from another UniProt entry, not shown here to be experimentally validated on this exact protein.",
    "The sequence supports a plausible family-level inference, but does not by itself prove the precise catalytic role assigned to residue 67."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry D5RFM4 annotates position 67 (Cys) as 'Proton acceptor' active site (evidence ECO:0000250, transferred from Q8RI81) and position 209 (Cys) as 'Proton donor'. The 2024 experimental paper (PubMed 39424140) characterized this histidine racemase. The author's expected answer B (Position 67, Proton acceptor) matches the UniProt active-site annotation. The annotation is by similarity rather than direct experimental determination on this exact protein, but it is the recorded and supported assignment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [C4](#evidence-c4), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Cofactor-independent amino acid racemases (a well-characterized enzyme family) use two cysteine residues as their catalytic dyad: one Cys abstracts the α-proton (proton acceptor) and the other returns it from the opposite face (proton donor). This is established from homologs such as ornithine racemase, lysine racemase, and related enzymes. Examining the sequence, Cys67 and Cys209 are the two cysteines in positions consistent with a catalytic pair. Among the four options: A (Position 64, Gly, 'Nucleophile') is chemically impossible—glycine has no side chain capable of nucleophilic catalysis. C (Position 8, Leu, 'Nucleophile') is likewise impossible—leucine is a hydrophobic, inert side chain. D (Position 143, Ser, 'Proton donor') is unlikely for this enzyme class, as amino acid racemases use Cys, not Ser, as the proton donor. Only B (Position 67, Cys, 'Proton acceptor') identifies a residue that is both chemically capable of the stated role and consistent with the known two-Cys catalytic mechanism of cofactor-independent amino acid racemases. A model with general knowledge of thiol-based catalysis and amino acid racemase mechanisms can eliminate A, C, and D and select B without needing the specific UniProt record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The four options differ in both residue identity and assigned catalytic role. Three options (A: Gly as nucleophile, C: Leu as nucleophile, D: Ser as proton donor in a racemase) are eliminated by basic chemical reasoning and family-level knowledge of cofactor-independent amino acid racemases using two Cys residues. Option B uniquely pairs a Cys residue with the proton-acceptor role, consistent with the well-known two-Cys catalytic dyad. This is a concrete, transferable inference from enzyme-family knowledge and residue chemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option B identifies a chemically plausible catalytic residue (Cys) with a role consistent with amino acid racemase mechanism. The other three options assign catalytic roles to residues (Gly, Leu, Ser) that are either chemically incapable of the stated function or inconsistent with the enzyme family's known mechanism.


### Important caveats

- The UniProt active-site annotation at position 67 is by similarity (ECO:0000250 to Q8RI81), not direct experimental mutagenesis on this exact protein, though a 2024 paper (PubMed 39424140) characterized the enzyme experimentally.
- The specific assignment of Cys67 as proton acceptor versus proton donor (vs. Cys209) depends on 3D structural context; however, since option D uses Ser143 rather than Cys209, the answer is uniquely determined among the offered choices without resolving this subtlety.
- The model is not told the enzyme identity (histidine racemase) from the original input; the reasoning relies on recognizing catalytic-residue chemistry and general amino acid racemase mechanisms from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Cofactor-independent amino acid racemases (a well-characterized enzyme family) use two cysteine residues as their catalytic dyad: one Cys abstracts the α-proton (proton acceptor) and the other returns it from the opposite face (proton donor). This is established from homologs such as ornithine racemase, lysine racemase, and related enzymes. Examining the sequence, Cys67 and Cys209 are the two cysteines in positions consistent with a catalytic pair. Among the four options: A (Position 64, Gly, 'Nucleophile') is chemically impossible—glycine has no side chain capable of nucleophilic catalysis. C (Position 8, Leu, 'Nucleophile') is likewise impossible—leucine is a hydrophobic, inert side chain. D (Position 143, Ser, 'Proton donor') is unlikely for this enzyme class, as amino acid racemases use Cys, not Ser, as the proton donor. Only B (Position 67, Cys, 'Proton acceptor') identifies a residue that is both chemically capable of the stated role and consistent with the known two-Cys catalytic mechanism of cofactor-independent amino acid racemases. A model with general knowledge of thiol-based catalysis and amino acid racemase mechanisms can eliminate A, C, and D and select B without needing the specific UniProt record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The four options differ in both residue identity and assigned catalytic role. Three options (A: Gly as nucleophile, C: Leu as nucleophile, D: Ser as proton donor in a racemase) are eliminated by basic chemical reasoning and family-level knowledge of cofactor-independent amino acid racemases using two Cys residues. Option B uniquely pairs a Cys residue with the proton-acceptor role, consistent with the well-known two-Cys catalytic dyad. This is a concrete, transferable inference from enzyme-family knowledge and residue chemistry."
  },
  "case_id": "active_site_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4",
      "C4",
      "C7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry D5RFM4 annotates position 67 (Cys) as 'Proton acceptor' active site (evidence ECO:0000250, transferred from Q8RI81) and position 209 (Cys) as 'Proton donor'. The 2024 experimental paper (PubMed 39424140) characterized this histidine racemase. The author's expected answer B (Position 67, Proton acceptor) matches the UniProt active-site annotation. The annotation is by similarity rather than direct experimental determination on this exact protein, but it is the recorded and supported assignment."
  },
  "important_caveats": [
    "The UniProt active-site annotation at position 67 is by similarity (ECO:0000250 to Q8RI81), not direct experimental mutagenesis on this exact protein, though a 2024 paper (PubMed 39424140) characterized the enzyme experimentally.",
    "The specific assignment of Cys67 as proton acceptor versus proton donor (vs. Cys209) depends on 3D structural context; however, since option D uses Ser143 rather than Cys209, the answer is uniquely determined among the offered choices without resolving this subtlety.",
    "The model is not told the enzyme identity (histidine racemase) from the original input; the reasoning relies on recognizing catalytic-residue chemistry and general amino acid racemase mechanisms from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B identifies a chemically plausible catalytic residue (Cys) with a role consistent with amino acid racemase mechanism. The other three options assign catalytic roles to residues (Gly, Leu, Ser) that are either chemically incapable of the stated function or inconsistent with the enzyme family's known mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry D5RFM4 annotates position 67 (Cys) as 'Proton acceptor' active site (evidence ECO:0000250, transferred from Q8RI81) and position 209 (Cys) as 'Proton donor'. The 2024 experimental paper (PubMed 39424140) characterized this histidine racemase. The author's expected answer B (Position 67, Proton acceptor) matches the UniProt active-site annotation. The annotation is by similarity rather than direct experimental determination on this exact protein, but it is the recorded and supported assignment.",
    "evidence_ids": ["C5", "H3", "C6", "H4", "C4", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Cofactor-independent amino acid racemases (a well-characterized enzyme family) use two cysteine residues as their catalytic dyad: one Cys abstracts the α-proton (proton acceptor) and the other returns it from the opposite face (proton donor). This is established from homologs such as ornithine racemase, lysine racemase, and related enzymes. Examining the sequence, Cys67 and Cys209 are the two cysteines in positions consistent with a catalytic pair. Among the four options: A (Position 64, Gly, 'Nucleophile') is chemically impossible—glycine has no side chain capable of nucleophilic catalysis. C (Position 8, Leu, 'Nucleophile') is likewise impossible—leucine is a hydrophobic, inert side chain. D (Position 143, Ser, 'Proton donor') is unlikely for this enzyme class, as amino acid racemases use Cys, not Ser, as the proton donor. Only B (Position 67, Cys, 'Proton acceptor') identifies a residue that is both chemically capable of the stated role and consistent with the known two-Cys catalytic mechanism of cofactor-independent amino acid racemases. A model with general knowledge of thiol-based catalysis and amino acid racemase mechanisms can eliminate A, C, and D and select B without needing the specific UniProt record.",
    "missing_item_specific_fact": "",
    "reason": "The four options differ in both residue identity and assigned catalytic role. Three options (A: Gly as nucleophile, C: Leu as nucleophile, D: Ser as proton donor in a racemase) are eliminated by basic chemical reasoning and family-level knowledge of cofactor-independent amino acid racemases using two Cys residues. Option B uniquely pairs a Cys residue with the proton-acceptor role, consistent with the well-known two-Cys catalytic dyad. This is a concrete, transferable inference from enzyme-family knowledge and residue chemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B identifies a chemically plausible catalytic residue (Cys) with a role consistent with amino acid racemase mechanism. The other three options assign catalytic roles to residues (Gly, Leu, Ser) that are either chemically incapable of the stated function or inconsistent with the enzyme family's known mechanism."
  },
  "important_caveats": [
    "The UniProt active-site annotation at position 67 is by similarity (ECO:0000250 to Q8RI81), not direct experimental mutagenesis on this exact protein, though a 2024 paper (PubMed 39424140) characterized the enzyme experimentally.",
    "The specific assignment of Cys67 as proton acceptor versus proton donor (vs. Cys209) depends on 3D structural context; however, since option D uses Ser143 rather than Cys209, the answer is uniquely determined among the offered choices without resolving this subtlety.",
    "The model is not told the enzyme identity (histidine racemase) from the original input; the reasoning relies on recognizing catalytic-residue chemistry and general amino acid racemase mechanisms from the sequence alone."
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
  "benchmark_sequence_length": 263,
  "benchmark_sequence_sha256": "c3c062f84cb504706da4f93fc7c25a17790dd9bc3a42419a61e2a9462719a5f8",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-07-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 263,
  "current_source_sequence_sha256": "c3c062f84cb504706da4f93fc7c25a17790dd9bc3a42419a61e2a9462719a5f8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D5RFM4",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc",
  "selected_historical_source_sequence_length": 263,
  "selected_historical_source_sequence_sha256": "c3c062f84cb504706da4f93fc7c25a17790dd9bc3a42419a61e2a9462719a5f8",
  "selected_historical_version": {
    "accession": "D5RFM4",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HISR_FUSN2",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D5RFM4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-07-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Fusobacteriati\",\"Fusobacteriota\",\"Fusobacteriia\",\"Fusobacteriales\",\"Fusobacteriaceae\",\"Fusobacterium\"],\"scientificName\":\"Fusobacterium nucleatum subsp. nucleatum (strain ATCC 23726 / VPI 4351)\",\"taxonId\":525283}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"value\":\"5.1.1.24\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"value\":\"Histidine racemase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8RI81\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":67},\"start\":{\"modifier\":\"EXACT\",\"value\":67}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8RI81\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":209},\"start\":{\"modifier\":\"EXACT\",\"value\":209}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Lamer T.\",\"Chen P.\",\"Venter M.J.\",\"van Belkum M.J.\",\"Wijewardane A.\",\"Wu C.\",\"Lemieux M.J.\",\"Vederas J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39424140\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107896\"}],\"citationType\":\"journal article\",\"firstPage\":\"107896\",\"id\":\"39424140\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107896\",\"publicationDate\":\"2024\",\"title\":\"Discovery, characterization, and structure of a cofactor-independent histidine racemase from the oral pathogen Fusobacterium nucleatum.\",\"volume\":\"300\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 23726 / VPI 4351\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   HISR_FUSN2              Reviewed;         263 AA.\nAC   D5RFM4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-JUL-2010, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};\nDE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};\nGN   Name=hisR {ECO:0000303|PubMed:39424140};\nGN   ORFNames=HMPREF0397_2009 {ECO:0000312|EMBL:EFG94488.1};\nOS   Fusobacterium nucleatum subsp. nucleatum (strain ATCC 23726 / VPI 4351).\nOC   Bacteria; Fusobacteriati; Fusobacteriota; Fusobacteriia; Fusobacteriales;\nOC   Fusobacteriaceae; Fusobacterium.\nOX   NCBI_TaxID=525283;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:51.450216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc",
  "url": "https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 23726 / VPI 4351;\nRX   PubMed=39424140; DOI=10.1016/j.jbc.2024.107896;\nRA   Lamer T., Chen P., Venter M.J., van Belkum M.J., Wijewardane A., Wu C.,\nRA   Lemieux M.J., Vederas J.C.;\nRT   \"Discovery, characterization, and structure of a cofactor-independent\nRT   histidine racemase from the oral pathogen Fusobacterium nucleatum.\";\nRL   J. Biol. Chem. 300:107896-107896(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:51.450216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc",
  "url": "https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        67\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8RI81\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:51.450216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc",
  "url": "https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        209\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8RI81\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:51.450216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc",
  "url": "https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
