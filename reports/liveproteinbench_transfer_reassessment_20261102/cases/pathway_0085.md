# pathway_0085

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0085.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Amino-acid degradation

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
A. terpenoid biosynthesis.
B. L-leucine degradation
C. Amino-acid degradation
D. L-methionine biosynthesis via de novo pathway
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates the protein as methylglutaconyl-CoA hydratase and places it in amino-acid degradation, specifically L-leucine degradation. This supports the keyed broad pathway, though the annotation is not by itself proof of experimental validation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The arginine-rich N-terminus is consistent with a mitochondrial targeting segment, and family-level recognition of the enzyme sequence as a CoA-processing hydratase would point toward methylglutaconyl-CoA hydratase. Knowledge transferable from that enzyme family connects it to leucine catabolism, distinguishing B/C from terpenoid biosynthesis and de novo methionine biosynthesis. This supports the pathway choice without needing this exact protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level enzyme and pathway inference is available from the sequence and general knowledge of related enzymes. It does not uniquely choose between the broad amino-acid-degradation label and its more specific leucine-degradation label.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> L-leucine degradation is a form of amino-acid degradation, and the supplied annotation assigns both labels. The choices therefore overlap rather than distinguish a unique pathway.


### Important caveats

- The sequence match and pathway assignment come from reviewer-only database evidence, not the original input; they support the key but are not credited as information available to the model.
- The database evidence cites a publication but uses an ECO:0000305 pathway assertion; this should not be mistaken for independently reviewed direct experimental proof.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The arginine-rich N-terminus is consistent with a mitochondrial targeting segment, and family-level recognition of the enzyme sequence as a CoA-processing hydratase would point toward methylglutaconyl-CoA hydratase. Knowledge transferable from that enzyme family connects it to leucine catabolism, distinguishing B/C from terpenoid biosynthesis and de novo methionine biosynthesis. This supports the pathway choice without needing this exact protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level enzyme and pathway inference is available from the sequence and general knowledge of related enzymes. It does not uniquely choose between the broad amino-acid-degradation label and its more specific leucine-degradation label."
  },
  "case_id": "pathway_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as methylglutaconyl-CoA hydratase and places it in amino-acid degradation, specifically L-leucine degradation. This supports the keyed broad pathway, though the annotation is not by itself proof of experimental validation."
  },
  "important_caveats": [
    "The sequence match and pathway assignment come from reviewer-only database evidence, not the original input; they support the key but are not credited as information available to the model.",
    "The database evidence cites a publication but uses an ECO:0000305 pathway assertion; this should not be mistaken for independently reviewed direct experimental proof."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "L-leucine degradation is a form of amino-acid degradation, and the supplied annotation assigns both labels. The choices therefore overlap rather than distinguish a unique pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as methylglutaconyl-CoA hydratase and places it in amino-acid degradation, specifically L-leucine degradation. This supports the keyed broad pathway, though the annotation is not by itself proof of experimental validation.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The arginine-rich N-terminus is consistent with a mitochondrial targeting segment, and family-level recognition of the enzyme sequence as a CoA-processing hydratase would point toward methylglutaconyl-CoA hydratase. Knowledge transferable from that enzyme family connects it to leucine catabolism, distinguishing B/C from terpenoid biosynthesis and de novo methionine biosynthesis. This supports the pathway choice without needing this exact protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "A family-level enzyme and pathway inference is available from the sequence and general knowledge of related enzymes. It does not uniquely choose between the broad amino-acid-degradation label and its more specific leucine-degradation label."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "L-leucine degradation is a form of amino-acid degradation, and the supplied annotation assigns both labels. The choices therefore overlap rather than distinguish a unique pathway."
  },
  "important_caveats": [
    "The sequence match and pathway assignment come from reviewer-only database evidence, not the original input; they support the key but are not credited as information available to the model.",
    "The database evidence cites a publication but uses an ECO:0000305 pathway assertion; this should not be mistaken for independently reviewed direct experimental proof."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) explicitly states the pathway as 'Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3.' Choice C ('Amino-acid degradation') is the top-level pathway name in this hierarchical annotation and is directly supported. However, Choice B ('L-leucine degradation') is the immediately nested sub-pathway and is equally stated in the same annotation line.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmarks of the crotonase superfamily of hydratases/dehydratases (α/β-fold, conserved catalytic residues in the 'GGLE…' and 'GAGG' motifs near positions ~140-180), plus an N-terminal mitochondrial targeting peptide. A model familiar with the crotonase superfamily can recognize methylglutaconyl-CoA hydratase (AUH) homologs, which catalyze the hydration of 3-methylglutaconyl-CoA to HMG-CoA specifically within leucine catabolism. This immediately eliminates terpenoid biosynthesis (A: the mevalonate pathway uses cytosolic HMG-CoA synthase, not a mitochondrial crotonase-type hydratase acting on 3-methylglutaconyl-CoA) and methionine biosynthesis (D: mechanistically unrelated). The protein is clearly in amino-acid/leucine degradation. The remaining B-vs-C distinction is a granularity issue within the same pathway hierarchy rather than a need for a protein-specific fact.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use crotonase-superfamily sequence motifs, mitochondrial targeting, and the specific substrate logic (3-methylglutaconyl-CoA → HMG-CoA is the leucine-degradation step, not the mevalonate-pathway step) to confidently place the protein in amino-acid/leucine degradation and eliminate A and D. The B-vs-C choice is a pathway-granularity convention, not a lookup of a unique fact about this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The UniProt annotation reads 'Amino-acid degradation; L-leucine degradation; …' as a single hierarchical pathway string. Choice C is the top-level pathway and Choice B is the nested sub-pathway; both are explicitly present in the same annotation. The task asks for 'the primary metabolic or signaling pathway,' which could reasonably be interpreted as either the top-level category (C) or the specific named pathway (B). Without a stated convention that 'primary' means the top-level UniProt pathway name, both answers are defensible.


### Important caveats

- The author's key C is supported by the annotation but is not uniquely determined over B, which is the more specific sub-pathway explicitly named in the same annotation line.
- The pathway evidence (ECO:0000305) is a manual assertion based on PubMed:32431008, indicating experimental/contextual annotation rather than pure sequence inference.
- The mitochondrial targeting sequence and crotonase-superfamily motifs are visible in the raw sequence and constitute legitimate transferable features for pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmarks of the crotonase superfamily of hydratases/dehydratases (α/β-fold, conserved catalytic residues in the 'GGLE…' and 'GAGG' motifs near positions ~140-180), plus an N-terminal mitochondrial targeting peptide. A model familiar with the crotonase superfamily can recognize methylglutaconyl-CoA hydratase (AUH) homologs, which catalyze the hydration of 3-methylglutaconyl-CoA to HMG-CoA specifically within leucine catabolism. This immediately eliminates terpenoid biosynthesis (A: the mevalonate pathway uses cytosolic HMG-CoA synthase, not a mitochondrial crotonase-type hydratase acting on 3-methylglutaconyl-CoA) and methionine biosynthesis (D: mechanistically unrelated). The protein is clearly in amino-acid/leucine degradation. The remaining B-vs-C distinction is a granularity issue within the same pathway hierarchy rather than a need for a protein-specific fact.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use crotonase-superfamily sequence motifs, mitochondrial targeting, and the specific substrate logic (3-methylglutaconyl-CoA → HMG-CoA is the leucine-degradation step, not the mevalonate-pathway step) to confidently place the protein in amino-acid/leucine degradation and eliminate A and D. The B-vs-C choice is a pathway-granularity convention, not a lookup of a unique fact about this protein."
  },
  "case_id": "pathway_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly states the pathway as 'Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3.' Choice C ('Amino-acid degradation') is the top-level pathway name in this hierarchical annotation and is directly supported. However, Choice B ('L-leucine degradation') is the immediately nested sub-pathway and is equally stated in the same annotation line."
  },
  "important_caveats": [
    "The author's key C is supported by the annotation but is not uniquely determined over B, which is the more specific sub-pathway explicitly named in the same annotation line.",
    "The pathway evidence (ECO:0000305) is a manual assertion based on PubMed:32431008, indicating experimental/contextual annotation rather than pure sequence inference.",
    "The mitochondrial targeting sequence and crotonase-superfamily motifs are visible in the raw sequence and constitute legitimate transferable features for pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The UniProt annotation reads 'Amino-acid degradation; L-leucine degradation; …' as a single hierarchical pathway string. Choice C is the top-level pathway and Choice B is the nested sub-pathway; both are explicitly present in the same annotation. The task asks for 'the primary metabolic or signaling pathway,' which could reasonably be interpreted as either the top-level category (C) or the specific named pathway (B). Without a stated convention that 'primary' means the top-level UniProt pathway name, both answers are defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly states the pathway as 'Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3.' Choice C ('Amino-acid degradation') is the top-level pathway name in this hierarchical annotation and is directly supported. However, Choice B ('L-leucine degradation') is the immediately nested sub-pathway and is equally stated in the same annotation line.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmarks of the crotonase superfamily of hydratases/dehydratases (α/β-fold, conserved catalytic residues in the 'GGLE…' and 'GAGG' motifs near positions ~140-180), plus an N-terminal mitochondrial targeting peptide. A model familiar with the crotonase superfamily can recognize methylglutaconyl-CoA hydratase (AUH) homologs, which catalyze the hydration of 3-methylglutaconyl-CoA to HMG-CoA specifically within leucine catabolism. This immediately eliminates terpenoid biosynthesis (A: the mevalonate pathway uses cytosolic HMG-CoA synthase, not a mitochondrial crotonase-type hydratase acting on 3-methylglutaconyl-CoA) and methionine biosynthesis (D: mechanistically unrelated). The protein is clearly in amino-acid/leucine degradation. The remaining B-vs-C distinction is a granularity issue within the same pathway hierarchy rather than a need for a protein-specific fact.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use crotonase-superfamily sequence motifs, mitochondrial targeting, and the specific substrate logic (3-methylglutaconyl-CoA → HMG-CoA is the leucine-degradation step, not the mevalonate-pathway step) to confidently place the protein in amino-acid/leucine degradation and eliminate A and D. The B-vs-C choice is a pathway-granularity convention, not a lookup of a unique fact about this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The UniProt annotation reads 'Amino-acid degradation; L-leucine degradation; …' as a single hierarchical pathway string. Choice C is the top-level pathway and Choice B is the nested sub-pathway; both are explicitly present in the same annotation. The task asks for 'the primary metabolic or signaling pathway,' which could reasonably be interpreted as either the top-level category (C) or the specific named pathway (B). Without a stated convention that 'primary' means the top-level UniProt pathway name, both answers are defensible."
  },
  "important_caveats": [
    "The author's key C is supported by the annotation but is not uniquely determined over B, which is the more specific sub-pathway explicitly named in the same annotation line.",
    "The pathway evidence (ECO:0000305) is a manual assertion based on PubMed:32431008, indicating experimental/contextual annotation rather than pure sequence inference.",
    "The mitochondrial targeting sequence and crotonase-superfamily motifs are visible in the raw sequence and constitute legitimate transferable features for pathway assignment."
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-\nCC       3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3.\nCC       {ECO:0000305|PubMed:32431008}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
