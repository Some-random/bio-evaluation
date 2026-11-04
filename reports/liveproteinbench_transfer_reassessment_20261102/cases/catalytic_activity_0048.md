# catalytic_activity_0048

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0048.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSGHIRVLELNRPKARNAISRALLASLREEVHSIARQYDAQTGEEIPTPSWNKRFGGIAGDSEKGPTRALVLASAVESSFCAGADLKERRGFTQEETNEFLANLRSTFAALDALPIPTISAISSRALGGGLELALCTHFRVLTSNAIVSLPETRLGIIPGAGGTHRLPRLIGLGRARDMIVTGRAVSGAEAYFLGLADRLVEVLPPDEQEAADTTDKDAALLSAAREAALTEAVRLASQICEGGPIGIRAALQAVQAPSQETENKMYERVIGTEDRNEALKAFAEKRKPVFKGR

[Multiple Choices]
A. N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2 CO2
B. Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.
C. (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O
D. cytidine(in) = cytidine(out)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation assigns this protein EC 4.2.1.18 and gives the reaction in choice C. The annotation cites PubMed but uses evidence code ECO:0000305, so this supports the key as an annotation, not as independently verified direct experimental evidence here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 349-residue sequence is a soluble enzyme-like protein without the multiple long hydrophobic segments expected of a cytidine transporter (D). Its compact size and sequence pattern are compatible with a crotonase-family CoA hydratase, which supports the HMG-CoA dehydration in C. The sequence also lacks the characteristic metal-binding HxD/E…H pattern expected for a 2-oxoglutarate-dependent demethylase (A); the glucosidase option (B) is a different, typically larger enzyme class with recognizable glycoside-hydrolase features.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and enzyme-family knowledge provides a meaningful basis for distinguishing C from the substantially different enzyme and transporter alternatives. This is a family-level inference, not a claim that the reaction is proven from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed reactions describe distinct protein functions; no other option is comparably supported by the sequence.


### Important caveats

- The supporting database annotation is evidence for the expected answer, but its cited evidence code does not establish direct experimental validation in the supplied excerpts.
- The reaction is reversible; choice C gives the annotated dehydration direction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 349-residue sequence is a soluble enzyme-like protein without the multiple long hydrophobic segments expected of a cytidine transporter (D). Its compact size and sequence pattern are compatible with a crotonase-family CoA hydratase, which supports the HMG-CoA dehydration in C. The sequence also lacks the characteristic metal-binding HxD/E…H pattern expected for a 2-oxoglutarate-dependent demethylase (A); the glucosidase option (B) is a different, typically larger enzyme class with recognizable glycoside-hydrolase features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-family knowledge provides a meaningful basis for distinguishing C from the substantially different enzyme and transporter alternatives. This is a family-level inference, not a claim that the reaction is proven from sequence alone."
  },
  "case_id": "catalytic_activity_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein EC 4.2.1.18 and gives the reaction in choice C. The annotation cites PubMed but uses evidence code ECO:0000305, so this supports the key as an annotation, not as independently verified direct experimental evidence here."
  },
  "important_caveats": [
    "The supporting database annotation is evidence for the expected answer, but its cited evidence code does not establish direct experimental validation in the supplied excerpts.",
    "The reaction is reversible; choice C gives the annotated dehydration direction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions describe distinct protein functions; no other option is comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein EC 4.2.1.18 and gives the reaction in choice C. The annotation cites PubMed but uses evidence code ECO:0000305, so this supports the key as an annotation, not as independently verified direct experimental evidence here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 349-residue sequence is a soluble enzyme-like protein without the multiple long hydrophobic segments expected of a cytidine transporter (D). Its compact size and sequence pattern are compatible with a crotonase-family CoA hydratase, which supports the HMG-CoA dehydration in C. The sequence also lacks the characteristic metal-binding HxD/E…H pattern expected for a 2-oxoglutarate-dependent demethylase (A); the glucosidase option (B) is a different, typically larger enzyme class with recognizable glycoside-hydrolase features.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-family knowledge provides a meaningful basis for distinguishing C from the substantially different enzyme and transporter alternatives. This is a family-level inference, not a claim that the reaction is proven from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions describe distinct protein functions; no other option is comparably supported by the sequence."
  },
  "important_caveats": [
    "The supporting database annotation is evidence for the expected answer, but its cited evidence code does not establish direct experimental validation in the supplied excerpts.",
    "The reaction is reversible; choice C gives the annotated dehydration direction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G4N954 (AUH1_PYRO7) is annotated as 'Methylglutaconyl-CoA hydratase 1, mitochondrial' with EC 4.2.1.18, and the recorded catalytic activity matches choice C exactly: (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O. The sequence in the question matches the UniProt entry exactly (SHA256 confirmed). The evidence code is ECO:0000305 (inferred by similarity), indicating the annotation was transferred from characterized homologs rather than demonstrated experimentally for this exact protein, but the annotation is well-supported by the family assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'GAGGTH' motif (visible at ~position 200: 'PGAGGTHRLPRLIG'), a well-known signature of the crotonase superfamily, which includes methylglutaconyl-CoA hydratase (AUH), enoyl-CoA hydratase, and related enzymes. The N-terminal region ('MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSG') is rich in S, R, A, L with very few acidic residues, consistent with a mitochondrial targeting peptide—matching the mitochondrial localization of AUH. Among the four choices, only C belongs to the crotonase superfamily. Choice A (JmjC histone demethylase) requires a JmjC domain with conserved His/Asp/Glu metal-binding residues, which are absent. Choice B (α-glucosidase) requires glycosidase motifs (e.g., DXE, NPNY) and a different fold entirely. Choice D (nucleoside transporter) requires multiple transmembrane helices, which are absent from this soluble mitochondrial protein. Thus, recognizing the crotonase superfamily GAGGTH motif and the mitochondrial targeting signal, combined with elimination of the other three structurally incompatible choices, provides a concrete transferable inference favoring C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the crotonase superfamily via the GAGGTH motif and the mitochondrial targeting peptide, then eliminate the three structurally incompatible alternatives (JmjC demethylase, glycosidase, membrane transporter). This is family-level pattern recognition transferable from other crotonase superfamily members, not a lookup of this protein's specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices belong to entirely different structural and functional classes (JmjC demethylase, glycosidase, crotonase superfamily hydratase, membrane transporter). The crotonase superfamily signature and mitochondrial targeting signal clearly point to C, while the other three lack any supporting sequence features.


### Important caveats

- The UniProt annotation for this protein carries evidence code ECO:0000305 (inferred by similarity), meaning the catalytic activity was assigned by homology to characterized AUH enzymes rather than by direct experimentation on this specific Pyricularia protein.
- The crotonase superfamily is large and includes many enzymes; however, among the four offered choices, only C belongs to this superfamily, so family-level recognition is sufficient to select the correct answer.
- The GAGGTH motif is a strong but not absolutely exclusive crotonase superfamily indicator; nonetheless, combined with the mitochondrial targeting signal and elimination of the other three structurally incompatible options, the inference is robust.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'GAGGTH' motif (visible at ~position 200: 'PGAGGTHRLPRLIG'), a well-known signature of the crotonase superfamily, which includes methylglutaconyl-CoA hydratase (AUH), enoyl-CoA hydratase, and related enzymes. The N-terminal region ('MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSG') is rich in S, R, A, L with very few acidic residues, consistent with a mitochondrial targeting peptide—matching the mitochondrial localization of AUH. Among the four choices, only C belongs to the crotonase superfamily. Choice A (JmjC histone demethylase) requires a JmjC domain with conserved His/Asp/Glu metal-binding residues, which are absent. Choice B (α-glucosidase) requires glycosidase motifs (e.g., DXE, NPNY) and a different fold entirely. Choice D (nucleoside transporter) requires multiple transmembrane helices, which are absent from this soluble mitochondrial protein. Thus, recognizing the crotonase superfamily GAGGTH motif and the mitochondrial targeting signal, combined with elimination of the other three structurally incompatible choices, provides a concrete transferable inference favoring C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the crotonase superfamily via the GAGGTH motif and the mitochondrial targeting peptide, then eliminate the three structurally incompatible alternatives (JmjC demethylase, glycosidase, membrane transporter). This is family-level pattern recognition transferable from other crotonase superfamily members, not a lookup of this protein's specific database entry."
  },
  "case_id": "catalytic_activity_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4N954 (AUH1_PYRO7) is annotated as 'Methylglutaconyl-CoA hydratase 1, mitochondrial' with EC 4.2.1.18, and the recorded catalytic activity matches choice C exactly: (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O. The sequence in the question matches the UniProt entry exactly (SHA256 confirmed). The evidence code is ECO:0000305 (inferred by similarity), indicating the annotation was transferred from characterized homologs rather than demonstrated experimentally for this exact protein, but the annotation is well-supported by the family assignment."
  },
  "important_caveats": [
    "The UniProt annotation for this protein carries evidence code ECO:0000305 (inferred by similarity), meaning the catalytic activity was assigned by homology to characterized AUH enzymes rather than by direct experimentation on this specific Pyricularia protein.",
    "The crotonase superfamily is large and includes many enzymes; however, among the four offered choices, only C belongs to this superfamily, so family-level recognition is sufficient to select the correct answer.",
    "The GAGGTH motif is a strong but not absolutely exclusive crotonase superfamily indicator; nonetheless, combined with the mitochondrial targeting signal and elimination of the other three structurally incompatible options, the inference is robust."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices belong to entirely different structural and functional classes (JmjC demethylase, glycosidase, crotonase superfamily hydratase, membrane transporter). The crotonase superfamily signature and mitochondrial targeting signal clearly point to C, while the other three lack any supporting sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G4N954 (AUH1_PYRO7) is annotated as 'Methylglutaconyl-CoA hydratase 1, mitochondrial' with EC 4.2.1.18, and the recorded catalytic activity matches choice C exactly: (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O. The sequence in the question matches the UniProt entry exactly (SHA256 confirmed). The evidence code is ECO:0000305 (inferred by similarity), indicating the annotation was transferred from characterized homologs rather than demonstrated experimentally for this exact protein, but the annotation is well-supported by the family assignment.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'GAGGTH' motif (visible at ~position 200: 'PGAGGTHRLPRLIG'), a well-known signature of the crotonase superfamily, which includes methylglutaconyl-CoA hydratase (AUH), enoyl-CoA hydratase, and related enzymes. The N-terminal region ('MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSG') is rich in S, R, A, L with very few acidic residues, consistent with a mitochondrial targeting peptide—matching the mitochondrial localization of AUH. Among the four choices, only C belongs to the crotonase superfamily. Choice A (JmjC histone demethylase) requires a JmjC domain with conserved His/Asp/Glu metal-binding residues, which are absent. Choice B (α-glucosidase) requires glycosidase motifs (e.g., DXE, NPNY) and a different fold entirely. Choice D (nucleoside transporter) requires multiple transmembrane helices, which are absent from this soluble mitochondrial protein. Thus, recognizing the crotonase superfamily GAGGTH motif and the mitochondrial targeting signal, combined with elimination of the other three structurally incompatible choices, provides a concrete transferable inference favoring C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the crotonase superfamily via the GAGGTH motif and the mitochondrial targeting peptide, then eliminate the three structurally incompatible alternatives (JmjC demethylase, glycosidase, membrane transporter). This is family-level pattern recognition transferable from other crotonase superfamily members, not a lookup of this protein's specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices belong to entirely different structural and functional classes (JmjC demethylase, glycosidase, crotonase superfamily hydratase, membrane transporter). The crotonase superfamily signature and mitochondrial targeting signal clearly point to C, while the other three lack any supporting sequence features."
  },
  "important_caveats": [
    "The UniProt annotation for this protein carries evidence code ECO:0000305 (inferred by similarity), meaning the catalytic activity was assigned by homology to characterized AUH enzymes rather than by direct experimentation on this specific Pyricularia protein.",
    "The crotonase superfamily is large and includes many enzymes; however, among the four offered choices, only C belongs to this superfamily, so family-level recognition is sufficient to select the correct answer.",
    "The GAGGTH motif is a strong but not absolutely exclusive crotonase superfamily indicator; nonetheless, combined with the mitochondrial targeting signal and elimination of the other three structurally incompatible options, the inference is robust."
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
  "benchmark_sequence_length": 349,
  "benchmark_sequence_sha256": "5e891c748ec2835aa75f719bfdb800087960d21c8e74e2457645a7ad7fbe7243",
  "current_entry_audit": {
    "entryVersion": 56,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-12-14",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 349,
  "current_source_sequence_sha256": "5e891c748ec2835aa75f719bfdb800087960d21c8e74e2457645a7ad7fbe7243",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 54,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G4N954",
  "selected_historical_entry_version": 54,
  "selected_historical_record_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "selected_historical_source_sequence_length": 349,
  "selected_historical_source_sequence_sha256": "5e891c748ec2835aa75f719bfdb800087960d21c8e74e2457645a7ad7fbe7243",
  "selected_historical_version": {
    "accession": "G4N954",
    "database": "Swiss-Prot",
    "entryVersion": 54,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AUH1_PYRO7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G4N954\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":56,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice blast fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Magnaporthales\",\"Pyriculariaceae\",\"Pyricularia\"],\"scientificName\":\"Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958)\",\"synonyms\":[\"Magnaporthe oryzae\"],\"taxonId\":242507}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.18\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"value\":\"Methylglutaconyl-CoA hydratase 1, mitochondrial\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"4.2.1.18\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"name\":\"(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:21536\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43074\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57346\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Xiao Y.\",\"Liu L.\",\"Zhang T.\",\"Zhou R.\",\"Ren Y.\",\"Li X.\",\"Shu H.\",\"Ye W.\",\"Zheng X.\",\"Zhang Z.\",\"Zhang H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32431008\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.15088\"}],\"citationType\":\"journal article\",\"firstPage\":\"774\",\"id\":\"32431008\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"790\",\"publicationDate\":\"2021\",\"title\":\"Transcription factor MoMsn2 targets the putative 3-methylglutaconyl-CoA hydratase-encoding gene MoAUH1 to govern infectious growth via mitochondrial fusion/fission balance in Magnaporthe oryzae.\",\"volume\":\"23\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H1",
  "excerpt": "ID   AUH1_PYRO7              Reviewed;         349 AA.\nAC   G4N954;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2011, sequence version 1.\nDT   28-JAN-2026, entry version 54.\nDE   RecName: Full=Methylglutaconyl-CoA hydratase 1, mitochondrial {ECO:0000303|PubMed:32431008};\nDE            EC=4.2.1.18 {ECO:0000305|PubMed:32431008};\nDE   Flags: Precursor;\nGN   Name=AUH1 {ECO:0000303|PubMed:32431008}; ORFNames=MGG_03335;\nOS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast\nOS   fungus) (Magnaporthe oryzae).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.\nOX   NCBI_TaxID=242507;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Methylglutaconyl-CoA hydratase 1, mitochondrial {ECO:0000303|PubMed:32431008};\nDE            EC=4.2.1.18 {ECO:0000305|PubMed:32431008};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=32431008; DOI=10.1111/1462-2920.15088;\nRA   Xiao Y., Liu L., Zhang T., Zhou R., Ren Y., Li X., Shu H., Ye W., Zheng X.,\nRA   Zhang Z., Zhang H.;\nRT   \"Transcription factor MoMsn2 targets the putative 3-methylglutaconyl-CoA\nRT   hydratase-encoding gene MoAUH1 to govern infectious growth via\nRT   mitochondrial fusion/fission balance in Magnaporthe oryzae.\";\nRL   Environ. Microbiol. 23:774-790(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-\nCC         glutaconyl-CoA + H2O; Xref=Rhea:RHEA:21536, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:43074, ChEBI:CHEBI:57346; EC=4.2.1.18;\nCC         Evidence={ECO:0000305|PubMed:32431008};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 48. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
