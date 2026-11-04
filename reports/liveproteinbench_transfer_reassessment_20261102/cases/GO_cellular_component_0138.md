# GO_cellular_component_0138

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0138.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — cytosolic large ribosomal subunit

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAFHKLVKNSAYYSRFQTKFKRRRQGKTDYYARKRLITQAKNKYNAPKYRLVVRFTNRDIITQMVTSEINGDKIFAAAYSHELRAYGINHGLTNWAAAYATGLLLARRVLAKLGLDKTFTGVEEPNGEYTLTEAAETEDGERRPFKAILDVGLARTSTGARVFGVMKGASDGGIFIPHSENRFPGYDIETEELDTEVLKKYIYGGHVAEYMETLADDDEERYKSQFVKYIEDDVEADSLEELYAEAHKQIRADPFRKYVSDAPKKSKEEWKAESLKYKKAKLSREERKARVEAKIKQLLAEQDE

[Multiple Choices]
A. perikaryon
B. nuclear pore nuclear basket
C. extracellular space
D. cytosolic large ribosomal subunit
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

> The sequence-matched record identifies the protein as large ribosomal subunit protein uL18 / 60S ribosomal protein L5 and annotates it to the cytosolic large ribosomal subunit. The GO annotation is computational (IEA:TreeGrafter), while the cited structural study concerns nascent 5S ribonucleoprotein assembly; the record also places the protein in the cytoplasm. Together these support D, though the GO annotation itself is not direct experimental localization evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly basic, Lys/Arg-rich region and a globular conserved core, consistent with an RNA-binding ribosomal protein. Transferable knowledge of eukaryotic RPL5/uL18 homologs links this protein family to 5S RNP and large-subunit assembly. That makes the cytosolic large ribosomal subunit a meaningful choice over the neuronal perikaryon, nuclear pore basket, or extracellular space.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the known role of RPL5/uL18 provide a concrete basis for choosing D from these alternatives; this does not require recalling the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives distinguish a specific large-ribosomal-subunit component from unrelated locations, and the sequence/family inference favors D.


### Important caveats

- The supplied GO annotation is computationally inferred, not direct experimental localization evidence.
- The current ontology uses GO:0022625 for this term; an older term with the same label is obsolete, and the exact ontology snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly basic, Lys/Arg-rich region and a globular conserved core, consistent with an RNA-binding ribosomal protein. Transferable knowledge of eukaryotic RPL5/uL18 homologs links this protein family to 5S RNP and large-subunit assembly. That makes the cytosolic large ribosomal subunit a meaningful choice over the neuronal perikaryon, nuclear pore basket, or extracellular space.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known role of RPL5/uL18 provide a concrete basis for choosing D from these alternatives; this does not require recalling the exact protein's database record."
  },
  "case_id": "GO_cellular_component_0138",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as large ribosomal subunit protein uL18 / 60S ribosomal protein L5 and annotates it to the cytosolic large ribosomal subunit. The GO annotation is computational (IEA:TreeGrafter), while the cited structural study concerns nascent 5S ribonucleoprotein assembly; the record also places the protein in the cytoplasm. Together these support D, though the GO annotation itself is not direct experimental localization evidence."
  },
  "important_caveats": [
    "The supplied GO annotation is computationally inferred, not direct experimental localization evidence.",
    "The current ontology uses GO:0022625 for this term; an older term with the same label is obsolete, and the exact ontology snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives distinguish a specific large-ribosomal-subunit component from unrelated locations, and the sequence/family inference favors D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0138",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as large ribosomal subunit protein uL18 / 60S ribosomal protein L5 and annotates it to the cytosolic large ribosomal subunit. The GO annotation is computational (IEA:TreeGrafter), while the cited structural study concerns nascent 5S ribonucleoprotein assembly; the record also places the protein in the cytoplasm. Together these support D, though the GO annotation itself is not direct experimental localization evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly basic, Lys/Arg-rich region and a globular conserved core, consistent with an RNA-binding ribosomal protein. Transferable knowledge of eukaryotic RPL5/uL18 homologs links this protein family to 5S RNP and large-subunit assembly. That makes the cytosolic large ribosomal subunit a meaningful choice over the neuronal perikaryon, nuclear pore basket, or extracellular space.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known role of RPL5/uL18 provide a concrete basis for choosing D from these alternatives; this does not require recalling the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives distinguish a specific large-ribosomal-subunit component from unrelated locations, and the sequence/family inference favors D."
  },
  "important_caveats": [
    "The supplied GO annotation is computationally inferred, not direct experimental localization evidence.",
    "The current ontology uses GO:0022625 for this term; an older term with the same label is obsolete, and the exact ontology snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (G0SEG2) names this protein 'Large ribosomal subunit protein uL18' / '60S ribosomal protein L5'. GO:0022625 (cytosolic large ribosomal subunit) is annotated with IEA:TreeGrafter, and the subcellular location is listed as 'Cytoplasm' (ECO:0000305|PubMed:37291423). A PDB structure (7OZS) confirms the protein in complex with RPL11, RRS1, RPF2, SYO1 and 5S RNA as part of the 60S subunit. The GO evidence code is computational (IEA), but the protein identity as a 60S ribosomal subunit component is corroborated by structural and literature evidence, supporting choice D.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~304 aa) shows hallmark features of ribosomal proteins: enrichment in basic residues (multiple K/R clusters such as 'KFKRRRQGK', 'KAKL', 'KKAKLSREERKARVEAKIKQ'), absence of any signal peptide or transmembrane segment (rules out C: extracellular space), absence of long coiled-coil or filamentous domains characteristic of nuclear basket components like Tpr/Mlp1-2 (rules out B: nuclear pore nuclear basket), and no neuronal-specific features (rules out A: perikaryon, which is restricted to neuronal cell bodies). The sequence contains motifs highly conserved in the uL18/L5 fold across all domains of life (e.g., 'RLVVRFTNRDIITQMVTSEINGDKIFAAAYSHELRAYGINHGLTNWAAAYATGLLLARR', 'GVMKGASDGGIFIPHSENRFPGYDIETEELDTEVLKKYIYGGHVAEYMETLADDDEERYKSQFVKYIEDDVEADSLEELYAEAHKQIRADPFRKYVSDAPKKSKEEWKAESLKYKKAKLSREERKARVEAKIKQLLAEQDE'), which is one of the most conserved ribosomal protein folds. A model trained on protein sequences across many organisms would recognize the L5/uL18 signature and infer cytosolic large ribosomal subunit localization, since ribosomal proteins lack targeting signals and function in the cytoplasm.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The ribosomal protein L5/uL18 fold is among the most universally conserved protein structures, found in bacteria, archaea, and eukaryotes. Recognition of this fold and the general principle that ribosomal proteins are cytoplasmic, lack targeting signals, and are rich in basic residues provides a concrete transferable inference that meaningfully distinguishes D from A, B, and C without requiring a lookup of this exact entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent clearly distinct compartments. The sequence features (basic residue enrichment, no signal peptide, no coiled-coil basket domains, no neuronal markers) unambiguously favor a ribosomal protein assignment over the other three choices.


### Important caveats

- The GO:0022625 annotation carries an IEA:TreeGrafter evidence code (computational transfer), though the protein name and PDB structural data independently confirm 60S subunit membership.
- The UniProt subcellular location field states 'Cytoplasm' rather than the more specific 'cytosolic large ribosomal subunit'; the GO term is the more precise annotation.
- The organism is Chaetomium thermophilum (a fungus); the L5/uL18 fold is conserved across eukaryotes, so family-level inference applies regardless of species.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~304 aa) shows hallmark features of ribosomal proteins: enrichment in basic residues (multiple K/R clusters such as 'KFKRRRQGK', 'KAKL', 'KKAKLSREERKARVEAKIKQ'), absence of any signal peptide or transmembrane segment (rules out C: extracellular space), absence of long coiled-coil or filamentous domains characteristic of nuclear basket components like Tpr/Mlp1-2 (rules out B: nuclear pore nuclear basket), and no neuronal-specific features (rules out A: perikaryon, which is restricted to neuronal cell bodies). The sequence contains motifs highly conserved in the uL18/L5 fold across all domains of life (e.g., 'RLVVRFTNRDIITQMVTSEINGDKIFAAAYSHELRAYGINHGLTNWAAAYATGLLLARR', 'GVMKGASDGGIFIPHSENRFPGYDIETEELDTEVLKKYIYGGHVAEYMETLADDDEERYKSQFVKYIEDDVEADSLEELYAEAHKQIRADPFRKYVSDAPKKSKEEWKAESLKYKKAKLSREERKARVEAKIKQLLAEQDE'), which is one of the most conserved ribosomal protein folds. A model trained on protein sequences across many organisms would recognize the L5/uL18 signature and infer cytosolic large ribosomal subunit localization, since ribosomal proteins lack targeting signals and function in the cytoplasm.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The ribosomal protein L5/uL18 fold is among the most universally conserved protein structures, found in bacteria, archaea, and eukaryotes. Recognition of this fold and the general principle that ribosomal proteins are cytoplasmic, lack targeting signals, and are rich in basic residues provides a concrete transferable inference that meaningfully distinguishes D from A, B, and C without requiring a lookup of this exact entry's annotation."
  },
  "case_id": "GO_cellular_component_0138",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (G0SEG2) names this protein 'Large ribosomal subunit protein uL18' / '60S ribosomal protein L5'. GO:0022625 (cytosolic large ribosomal subunit) is annotated with IEA:TreeGrafter, and the subcellular location is listed as 'Cytoplasm' (ECO:0000305|PubMed:37291423). A PDB structure (7OZS) confirms the protein in complex with RPL11, RRS1, RPF2, SYO1 and 5S RNA as part of the 60S subunit. The GO evidence code is computational (IEA), but the protein identity as a 60S ribosomal subunit component is corroborated by structural and literature evidence, supporting choice D."
  },
  "important_caveats": [
    "The GO:0022625 annotation carries an IEA:TreeGrafter evidence code (computational transfer), though the protein name and PDB structural data independently confirm 60S subunit membership.",
    "The UniProt subcellular location field states 'Cytoplasm' rather than the more specific 'cytosolic large ribosomal subunit'; the GO term is the more precise annotation.",
    "The organism is Chaetomium thermophilum (a fungus); the L5/uL18 fold is conserved across eukaryotes, so family-level inference applies regardless of species."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct compartments. The sequence features (basic residue enrichment, no signal peptide, no coiled-coil basket domains, no neuronal markers) unambiguously favor a ribosomal protein assignment over the other three choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0138",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (G0SEG2) names this protein 'Large ribosomal subunit protein uL18' / '60S ribosomal protein L5'. GO:0022625 (cytosolic large ribosomal subunit) is annotated with IEA:TreeGrafter, and the subcellular location is listed as 'Cytoplasm' (ECO:0000305|PubMed:37291423). A PDB structure (7OZS) confirms the protein in complex with RPL11, RRS1, RPF2, SYO1 and 5S RNA as part of the 60S subunit. The GO evidence code is computational (IEA), but the protein identity as a 60S ribosomal subunit component is corroborated by structural and literature evidence, supporting choice D.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~304 aa) shows hallmark features of ribosomal proteins: enrichment in basic residues (multiple K/R clusters such as 'KFKRRRQGK', 'KAKL', 'KKAKLSREERKARVEAKIKQ'), absence of any signal peptide or transmembrane segment (rules out C: extracellular space), absence of long coiled-coil or filamentous domains characteristic of nuclear basket components like Tpr/Mlp1-2 (rules out B: nuclear pore nuclear basket), and no neuronal-specific features (rules out A: perikaryon, which is restricted to neuronal cell bodies). The sequence contains motifs highly conserved in the uL18/L5 fold across all domains of life (e.g., 'RLVVRFTNRDIITQMVTSEINGDKIFAAAYSHELRAYGINHGLTNWAAAYATGLLLARR', 'GVMKGASDGGIFIPHSENRFPGYDIETEELDTEVLKKYIYGGHVAEYMETLADDDEERYKSQFVKYIEDDVEADSLEELYAEAHKQIRADPFRKYVSDAPKKSKEEWKAESLKYKKAKLSREERKARVEAKIKQLLAEQDE'), which is one of the most conserved ribosomal protein folds. A model trained on protein sequences across many organisms would recognize the L5/uL18 signature and infer cytosolic large ribosomal subunit localization, since ribosomal proteins lack targeting signals and function in the cytoplasm.",
    "missing_item_specific_fact": "",
    "reason": "The ribosomal protein L5/uL18 fold is among the most universally conserved protein structures, found in bacteria, archaea, and eukaryotes. Recognition of this fold and the general principle that ribosomal proteins are cytoplasmic, lack targeting signals, and are rich in basic residues provides a concrete transferable inference that meaningfully distinguishes D from A, B, and C without requiring a lookup of this exact entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct compartments. The sequence features (basic residue enrichment, no signal peptide, no coiled-coil basket domains, no neuronal markers) unambiguously favor a ribosomal protein assignment over the other three choices."
  },
  "important_caveats": [
    "The GO:0022625 annotation carries an IEA:TreeGrafter evidence code (computational transfer), though the protein name and PDB structural data independently confirm 60S subunit membership.",
    "The UniProt subcellular location field states 'Cytoplasm' rather than the more specific 'cytosolic large ribosomal subunit'; the GO term is the more precise annotation.",
    "The organism is Chaetomium thermophilum (a fungus); the L5/uL18 fold is conserved across eukaryotes, so family-level inference applies regardless of species."
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
  "benchmark_sequence_length": 304,
  "benchmark_sequence_sha256": "5e850aa2a567f0ef5f34a40fa5df7ed6666298024bf5e4a4184e8725ce2b1ae0",
  "current_entry_audit": {
    "entryVersion": 58,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-10-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 304,
  "current_source_sequence_sha256": "5e850aa2a567f0ef5f34a40fa5df7ed6666298024bf5e4a4184e8725ce2b1ae0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 56,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G0SEG2",
  "selected_historical_entry_version": 56,
  "selected_historical_record_sha256": "de21ed9c5893dab95459cc199cc0c02ce4d43bb6a09f9dad35281a744e77edb9",
  "selected_historical_source_sequence_length": 304,
  "selected_historical_source_sequence_sha256": "5e850aa2a567f0ef5f34a40fa5df7ed6666298024bf5e4a4184e8725ce2b1ae0",
  "selected_historical_version": {
    "accession": "G0SEG2",
    "database": "Swiss-Prot",
    "entryVersion": 56,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RL5_CHATD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G0SEG2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:25.225490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023",
  "url": "https://rest.uniprot.org/uniprotkb/G0SEG2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":58,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-10-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:25.225490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023",
  "url": "https://rest.uniprot.org/uniprotkb/G0SEG2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Chaetomium thermophilum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Thermochaetoides\"],\"scientificName\":\"Thermochaetoides thermophila (strain DSM 1495 / CBS 144.50 / DAOM 24625 / IMI 039719)\",\"taxonId\":759272}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:25.225490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023",
  "url": "https://rest.uniprot.org/uniprotkb/G0SEG2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"37291423\",\"source\":\"PubMed\"}],\"value\":\"60S ribosomal protein L5\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"37291423\",\"source\":\"PubMed\"}],\"value\":\"ctRPL5\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"37291423\",\"source\":\"PubMed\"}],\"value\":\"Large ribosomal subunit protein uL18\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:25.225490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023",
  "url": "https://rest.uniprot.org/uniprotkb/G0SEG2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"37291423\",\"source\":\"PubMed\"}],\"id\":\"SL-0086\",\"value\":\"Cytoplasm\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:25.225490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023",
  "url": "https://rest.uniprot.org/uniprotkb/G0SEG2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0022625\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosolic large ribosomal subunit\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/74",
  "retrieved_utc": "2026-11-02T04:28:25.225490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023",
  "url": "https://rest.uniprot.org/uniprotkb/G0SEG2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Castillo Duque de Estrada N.M.\",\"Thoms M.\",\"Flemming D.\",\"Hammaren H.M.\",\"Buschauer R.\",\"Ameismeier M.\",\"Bassler J.\",\"Beck M.\",\"Beckmann R.\",\"Hurt E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37291423\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41594-023-01006-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"1119\",\"id\":\"37291423\",\"journal\":\"Nat. Struct. Mol. Biol.\",\"lastPage\":\"1131\",\"publicationDate\":\"2023\",\"title\":\"Structure of nascent 5S RNPs at the crossroad between ribosome assembly and MDM2-p53 pathways.\",\"volume\":\"30\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7OZS\",\"source\":\"PDB\"}],\"referenceNumber\":8,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.50 ANGSTROMS) IN COMPLEX WITH RPL11; RRS1; RPF2; SYO1 AND 5S RNA\",\"FUNCTION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:28:25.225490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023",
  "url": "https://rest.uniprot.org/uniprotkb/G0SEG2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H1",
  "excerpt": "ID   RL5_CHATD               Reviewed;         304 AA.\nAC   G0SEG2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-OCT-2011, sequence version 1.\nDT   28-JAN-2026, entry version 56.\nDE   RecName: Full=Large ribosomal subunit protein uL18 {ECO:0000305|PubMed:37291423};\nDE   AltName: Full=60S ribosomal protein L5 {ECO:0000305|PubMed:37291423};\nDE            Short=ctRPL5 {ECO:0000305|PubMed:37291423};\nGN   ORFNames=HT_0063640 {ECO:0000312|EMBL:EGS18339.1};\nOS   Chaetomium thermophilum (strain DSM 1495 / CBS 144.50 / IMI 039719)\nOS   (Thermochaetoides thermophila).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Thermochaetoides.\nOX   NCBI_TaxID=759272;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:28.823797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de21ed9c5893dab95459cc199cc0c02ce4d43bb6a09f9dad35281a744e77edb9",
  "url": "https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H2",
  "excerpt": "RN   [8] {ECO:0007744|PDB:7OZS}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.50 ANGSTROMS) IN COMPLEX WITH RPL11;\nRP   RRS1; RPF2; SYO1 AND 5S RNA, FUNCTION, AND SUBUNIT.\nRX   PubMed=37291423; DOI=10.1038/s41594-023-01006-7;\nRA   Castillo Duque de Estrada N.M., Thoms M., Flemming D., Hammaren H.M.,\nRA   Buschauer R., Ameismeier M., Bassler J., Beck M., Beckmann R., Hurt E.;\nRT   \"Structure of nascent 5S RNPs at the crossroad between ribosome assembly\nRT   and MDM2-p53 pathways.\";\nRL   Nat. Struct. Mol. Biol. 30:1119-1131(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:28.823797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de21ed9c5893dab95459cc199cc0c02ce4d43bb6a09f9dad35281a744e77edb9",
  "url": "https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:37291423}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:28.823797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de21ed9c5893dab95459cc199cc0c02ce4d43bb6a09f9dad35281a744e77edb9",
  "url": "https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0022625; C:cytosolic large ribosomal subunit; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:28.823797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 173-173",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de21ed9c5893dab95459cc199cc0c02ce4d43bb6a09f9dad35281a744e77edb9",
  "url": "https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000180\nname: obsolete cytosolic large ribosomal subunit\nnamespace: cellular_component\ndef: \"OBSOLETE. (Was not defined before being made obsolete).\" [GOC:ai]\ncomment: This term was made obsolete because more specific children exist.\nsynonym: \"cytosolic large ribosomal subunit\" EXACT []\nis_obsolete: true\nconsider: GO:0022625\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000180",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1791-1800",
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
  "excerpt": "[Term]\nid: GO:0022625\nname: cytosolic large ribosomal subunit\nnamespace: cellular_component\nalt_id: GO:0005842\nalt_id: GO:0009282\nalt_id: GO:0030498\nalt_id: GO:0030872\ndef: \"The large subunit of a ribosome located in the cytosol.\" [GOC:mtg_sensu]\nsynonym: \"50S ribosomal subunit\" NARROW []\nsynonym: \"60S ribosomal subunit\" NARROW []\nsynonym: \"eukaryotic ribosomal LSU\" NARROW []\nsynonym: \"prokaryotic large ribosomal subunit\" NARROW []\nis_a: GO:0015934 ! large ribosomal subunit\nrelationship: part_of GO:0022626 ! cytosolic ribosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0022625",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 160556-160571",
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
  "excerpt": "[Term]\nid: GO:0043204\nname: perikaryon\nnamespace: cellular_component\ndef: \"The portion of the cell soma (neuronal cell body) that excludes the nucleus.\" [GOC:jl]\nsynonym: \"cell soma cytoplasm\" RELATED []\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0043025 ! neuronal cell body\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043204",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 244903-244911",
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
  "excerpt": "[Term]\nid: GO:0044615\nname: nuclear pore nuclear basket\nnamespace: cellular_component\ndef: \"A filamentous, cage-like assembly on the nuclear face of the nuclear pore complex (NPC). In S. cerevisiae, Mlp1p and Mlp2p are two major components of the NPC nuclear basket. In vertebrates, Tpr is a major component.\" [GOC:dgf, PMID:18046406, PMID:19524430, PMID:20947011, PMID:22419078]\nis_a: GO:0140513 ! nuclear protein-containing complex\nrelationship: part_of GO:0005643 ! nuclear pore\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044615",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 258897-258904",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 138. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
