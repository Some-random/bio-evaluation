# pathway_0177

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0177.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSQPEFTRSIVGASFLLPVINGAMHIPPAVSATRVTLEDNQPRDAPILVLLFALSVLIDVMDKAADLPRQTRKTWLMTIVVFASPFVVLAVYGTMHCGLLALLRLLGVPLLAVVHAMPLIPVYSWKTGSISTVKLKYFLGPFKSLFGATCIGLMDVTAVVLYLRGTMLHPENASSAGHFRVLMYTITYDFLWESICDVRDIQEDEQNNITTLATAFGVRPTLIFLGGSTMMGDLSITLLGGGSAVLSVVRSTVFWGAFAALALHKPRSAVYPWGLATLFGLLPVWLASLGART

[Multiple Choices]
A. Metabolic intermediate biosynthesis
B. Secondary metabolite biosynthesis
C. peptidoglycan degradation. .
D. L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9. .
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

> The sequence-matched UniProt record assigns this protein to secondary metabolite biosynthesis, with a terpenoid-biosynthesis annotation linked to a publication and experimental evidence code. This supports choice B, though the cited study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic sequence suggests a multipass membrane protein, plausibly a membrane-associated prenyltransferase. That makes secondary-metabolite biosynthesis plausible, but prenyltransferases can serve different pathways, including primary metabolism; the sequence alone does not establish the relevant substrate or pathway.


**Missing item-specific fact**

> Whether this protein's prenyltransferase activity acts in a specialized secondary-metabolite pathway rather than primary metabolic-intermediate biosynthesis.


**Reason**

> The sequence provides a plausible enzyme-class clue but not a meaningful basis for reliably distinguishing the two broad pathway choices A and B. Resolving that distinction requires the protein's specific biological role or pathway context, which is absent from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The membrane-protein character can suggest a prenyltransferase, but does not specify whether its pathway is primary metabolism or secondary-metabolite biosynthesis.


### Important caveats

- The pathway annotation is reviewer-only evidence and was not part of the original input.
- The source annotation supports the key but does not by itself establish that the pathway can be identified from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic sequence suggests a multipass membrane protein, plausibly a membrane-associated prenyltransferase. That makes secondary-metabolite biosynthesis plausible, but prenyltransferases can serve different pathways, including primary metabolism; the sequence alone does not establish the relevant substrate or pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this protein's prenyltransferase activity acts in a specialized secondary-metabolite pathway rather than primary metabolic-intermediate biosynthesis.",
    "reason": "The sequence provides a plausible enzyme-class clue but not a meaningful basis for reliably distinguishing the two broad pathway choices A and B. Resolving that distinction requires the protein's specific biological role or pathway context, which is absent from the original input."
  },
  "case_id": "pathway_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein to secondary metabolite biosynthesis, with a terpenoid-biosynthesis annotation linked to a publication and experimental evidence code. This supports choice B, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The pathway annotation is reviewer-only evidence and was not part of the original input.",
    "The source annotation supports the key but does not by itself establish that the pathway can be identified from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The membrane-protein character can suggest a prenyltransferase, but does not specify whether its pathway is primary metabolism or secondary-metabolite biosynthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein to secondary metabolite biosynthesis, with a terpenoid-biosynthesis annotation linked to a publication and experimental evidence code. This supports choice B, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic sequence suggests a multipass membrane protein, plausibly a membrane-associated prenyltransferase. That makes secondary-metabolite biosynthesis plausible, but prenyltransferases can serve different pathways, including primary metabolism; the sequence alone does not establish the relevant substrate or pathway.",
    "missing_item_specific_fact": "Whether this protein's prenyltransferase activity acts in a specialized secondary-metabolite pathway rather than primary metabolic-intermediate biosynthesis.",
    "reason": "The sequence provides a plausible enzyme-class clue but not a meaningful basis for reliably distinguishing the two broad pathway choices A and B. Resolving that distinction requires the protein's specific biological role or pathway context, which is absent from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The membrane-protein character can suggest a prenyltransferase, but does not specify whether its pathway is primary metabolism or secondary-metabolite biosynthesis."
  },
  "important_caveats": [
    "The pathway annotation is reviewer-only evidence and was not part of the original input.",
    "The source annotation supports the key but does not by itself establish that the pathway can be identified from sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (evidence C5, H3) explicitly states PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with evidence code ECO:0000269 (direct assay) from PubMed:39310987. The protein is annotated as Prenyltransferase vviA (EC 2.5.1.-), a membrane-bound enzyme catalyzing prenylation in Sporulositol A biosynthesis. This experimental annotation directly supports choice B.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 293-aa sequence displays approximately 5-6 long hydrophobic stretches (e.g., residues ~10-30, ~50-80, ~95-120, ~140-170, ~195-220, ~240-270) consistent with a multi-pass membrane protein. Membrane-bound prenyltransferases (UbiA-family and related fungal prenyltransferases) are a well-characterized family whose defining topology is multiple transmembrane helices. In fungi, these membrane-bound prenyltransferases catalyze prenylation of terpenoid scaffolds and are universally classified under secondary metabolite biosynthesis (terpenoid biosynthesis), not primary metabolic intermediate biosynthesis. Against distractor C (peptidoglycan degradation): peptidoglycan-degrading enzymes (lysozymes, amidases, transglycosylases) are soluble or periplasmic with entirely different folds and lack multi-TM architecture. Against distractor D (histidine biosynthesis step 4/9): histidine biosynthesis enzymes (e.g., HisA, HisF) are soluble cytoplasmic TIM-barrel proteins with no transmembrane segments. Against distractor A (metabolic intermediate biosynthesis): this term in pathway databases (MetaCyc, UniProt) refers to primary metabolism intermediates (amino acids, nucleotides, cofactors); prenylation of terpenoid scaffolds is specifically categorized under secondary metabolism. Thus the multi-TM membrane topology plus fungal context points to secondary metabolite biosynthesis via the well-known membrane-bound prenyltransferase family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-transmembrane topology is directly observable from the hydrophobic stretches in the supplied sequence. Knowledge that membrane-bound prenyltransferases in fungi belong to secondary metabolite (terpenoid) biosynthesis is a well-established family-level pattern transferable from other fungal prenyltransferases. The distractors C and D are eliminated by topology mismatch (soluble enzymes), and A is eliminated by the standard pathway classification of prenylation reactions as secondary metabolism rather than primary metabolic intermediate biosynthesis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While A (metabolic intermediate biosynthesis) and B (secondary metabolite biosynthesis) could superficially seem similar, the standard pathway classification places prenyltransferase-mediated terpenoid modifications firmly under secondary metabolite biosynthesis. The multi-TM membrane architecture eliminates C and D unambiguously. No genuine ambiguity remains among the offered choices.


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269) from a 2024 Org. Lett. paper, confirming the pathway assignment is not merely computational.
- The term 'metabolic intermediate biosynthesis' (option A) is broad and could in principle encompass some prenylation steps, but in standard pathway ontology it refers to primary metabolism, making B the clearly correct classification for a terpenoid prenyltransferase.
- The protein is from a lichen-forming fungus (Viridothelium virens); fungal secondary metabolite biosynthesis is well-established as a major category of membrane-bound enzyme function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 293-aa sequence displays approximately 5-6 long hydrophobic stretches (e.g., residues ~10-30, ~50-80, ~95-120, ~140-170, ~195-220, ~240-270) consistent with a multi-pass membrane protein. Membrane-bound prenyltransferases (UbiA-family and related fungal prenyltransferases) are a well-characterized family whose defining topology is multiple transmembrane helices. In fungi, these membrane-bound prenyltransferases catalyze prenylation of terpenoid scaffolds and are universally classified under secondary metabolite biosynthesis (terpenoid biosynthesis), not primary metabolic intermediate biosynthesis. Against distractor C (peptidoglycan degradation): peptidoglycan-degrading enzymes (lysozymes, amidases, transglycosylases) are soluble or periplasmic with entirely different folds and lack multi-TM architecture. Against distractor D (histidine biosynthesis step 4/9): histidine biosynthesis enzymes (e.g., HisA, HisF) are soluble cytoplasmic TIM-barrel proteins with no transmembrane segments. Against distractor A (metabolic intermediate biosynthesis): this term in pathway databases (MetaCyc, UniProt) refers to primary metabolism intermediates (amino acids, nucleotides, cofactors); prenylation of terpenoid scaffolds is specifically categorized under secondary metabolism. Thus the multi-TM membrane topology plus fungal context points to secondary metabolite biosynthesis via the well-known membrane-bound prenyltransferase family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-transmembrane topology is directly observable from the hydrophobic stretches in the supplied sequence. Knowledge that membrane-bound prenyltransferases in fungi belong to secondary metabolite (terpenoid) biosynthesis is a well-established family-level pattern transferable from other fungal prenyltransferases. The distractors C and D are eliminated by topology mismatch (soluble enzymes), and A is eliminated by the standard pathway classification of prenylation reactions as secondary metabolism rather than primary metabolic intermediate biosynthesis."
  },
  "case_id": "pathway_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5, H3) explicitly states PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with evidence code ECO:0000269 (direct assay) from PubMed:39310987. The protein is annotated as Prenyltransferase vviA (EC 2.5.1.-), a membrane-bound enzyme catalyzing prenylation in Sporulositol A biosynthesis. This experimental annotation directly supports choice B."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2024 Org. Lett. paper, confirming the pathway assignment is not merely computational.",
    "The term 'metabolic intermediate biosynthesis' (option A) is broad and could in principle encompass some prenylation steps, but in standard pathway ontology it refers to primary metabolism, making B the clearly correct classification for a terpenoid prenyltransferase.",
    "The protein is from a lichen-forming fungus (Viridothelium virens); fungal secondary metabolite biosynthesis is well-established as a major category of membrane-bound enzyme function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A (metabolic intermediate biosynthesis) and B (secondary metabolite biosynthesis) could superficially seem similar, the standard pathway classification places prenyltransferase-mediated terpenoid modifications firmly under secondary metabolite biosynthesis. The multi-TM membrane architecture eliminates C and D unambiguously. No genuine ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5, H3) explicitly states PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with evidence code ECO:0000269 (direct assay) from PubMed:39310987. The protein is annotated as Prenyltransferase vviA (EC 2.5.1.-), a membrane-bound enzyme catalyzing prenylation in Sporulositol A biosynthesis. This experimental annotation directly supports choice B.",
    "evidence_ids": ["C5", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 293-aa sequence displays approximately 5-6 long hydrophobic stretches (e.g., residues ~10-30, ~50-80, ~95-120, ~140-170, ~195-220, ~240-270) consistent with a multi-pass membrane protein. Membrane-bound prenyltransferases (UbiA-family and related fungal prenyltransferases) are a well-characterized family whose defining topology is multiple transmembrane helices. In fungi, these membrane-bound prenyltransferases catalyze prenylation of terpenoid scaffolds and are universally classified under secondary metabolite biosynthesis (terpenoid biosynthesis), not primary metabolic intermediate biosynthesis. Against distractor C (peptidoglycan degradation): peptidoglycan-degrading enzymes (lysozymes, amidases, transglycosylases) are soluble or periplasmic with entirely different folds and lack multi-TM architecture. Against distractor D (histidine biosynthesis step 4/9): histidine biosynthesis enzymes (e.g., HisA, HisF) are soluble cytoplasmic TIM-barrel proteins with no transmembrane segments. Against distractor A (metabolic intermediate biosynthesis): this term in pathway databases (MetaCyc, UniProt) refers to primary metabolism intermediates (amino acids, nucleotides, cofactors); prenylation of terpenoid scaffolds is specifically categorized under secondary metabolism. Thus the multi-TM membrane topology plus fungal context points to secondary metabolite biosynthesis via the well-known membrane-bound prenyltransferase family.",
    "missing_item_specific_fact": "",
    "reason": "The multi-transmembrane topology is directly observable from the hydrophobic stretches in the supplied sequence. Knowledge that membrane-bound prenyltransferases in fungi belong to secondary metabolite (terpenoid) biosynthesis is a well-established family-level pattern transferable from other fungal prenyltransferases. The distractors C and D are eliminated by topology mismatch (soluble enzymes), and A is eliminated by the standard pathway classification of prenylation reactions as secondary metabolism rather than primary metabolic intermediate biosynthesis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A (metabolic intermediate biosynthesis) and B (secondary metabolite biosynthesis) could superficially seem similar, the standard pathway classification places prenyltransferase-mediated terpenoid modifications firmly under secondary metabolite biosynthesis. The multi-TM membrane architecture eliminates C and D unambiguously. No genuine ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2024 Org. Lett. paper, confirming the pathway assignment is not merely computational.",
    "The term 'metabolic intermediate biosynthesis' (option A) is broad and could in principle encompass some prenylation steps, but in standard pathway ontology it refers to primary metabolism, making B the clearly correct classification for a terpenoid prenyltransferase.",
    "The protein is from a lichen-forming fungus (Viridothelium virens); fungal secondary metabolite biosynthesis is well-established as a major category of membrane-bound enzyme function."
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
  "benchmark_sequence_length": 293,
  "benchmark_sequence_sha256": "897fc4df843bf85f1cdd0a1f4daa86fcaba8dd7ff09001216f7df7ed7a613ef7",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2020-06-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 293,
  "current_source_sequence_sha256": "897fc4df843bf85f1cdd0a1f4daa86fcaba8dd7ff09001216f7df7ed7a613ef7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A6A6H402",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "selected_historical_source_sequence_length": 293,
  "selected_historical_source_sequence_sha256": "897fc4df843bf85f1cdd0a1f4daa86fcaba8dd7ff09001216f7df7ed7a613ef7",
  "selected_historical_version": {
    "accession": "A0A6A6H402",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "VVIA_VIRVR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A6A6H402\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2020-06-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Speckled blister lichen\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetes incertae sedis\",\"Trypetheliales\",\"Trypetheliaceae\",\"Viridothelium\"],\"scientificName\":\"Viridothelium virens\",\"synonyms\":[\"Trypethelium virens\"],\"taxonId\":1048519}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"Sporulositol A biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"Prenyltransferase vviA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Tang Y.J.\",\"Zou Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39310987\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.orglett.4c03154\"}],\"citationType\":\"journal article\",\"firstPage\":\"8366\",\"id\":\"39310987\",\"journal\":\"Org. Lett.\",\"lastPage\":\"8370\",\"publicationDate\":\"2024\",\"title\":\"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.\",\"volume\":\"26\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"PATHWAY\",\"MUTAGENESIS OF LEU-17; ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND THR-277\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   VVIA_VIRVR              Reviewed;         293 AA.\nAC   A0A6A6H402;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-JUN-2020, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Prenyltransferase vviA {ECO:0000303|PubMed:39310987};\nDE            EC=2.5.1.- {ECO:0000269|PubMed:39310987};\nDE   AltName: Full=Sporulositol A biosynthesis cluster protein A {ECO:0000303|PubMed:39310987};\nGN   Name=vviA {ECO:0000303|PubMed:39310987}; ORFNames=EV356DRAFT_253807;\nOS   Viridothelium virens (Speckled blister lichen) (Trypethelium virens).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetes incertae sedis; Trypetheliales; Trypetheliaceae;\nOC   Viridothelium.\nOX   NCBI_TaxID=1048519;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, PATHWAY, AND MUTAGENESIS OF LEU-17;\nRP   ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND\nRP   THR-277.\nRX   PubMed=39310987; DOI=10.1021/acs.orglett.4c03154;\nRA   Tang Y.J., Zou Y.;\nRT   \"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.\";\nRL   Org. Lett. 26:8366-8370(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:39310987}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 177. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
