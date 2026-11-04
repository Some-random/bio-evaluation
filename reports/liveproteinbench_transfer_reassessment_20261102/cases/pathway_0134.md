# pathway_0134

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0134.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGFAPLLVFSLFVFAGTTKGFICSFDSIYQLGDSFSDTGNLIRQPPDGPTFCSAHFPYGETFPGMPTGRCSDGRLIIDFIATALNLPLLNPYLQQNVSFRHGVNFAVGGATALDLSFLAARGVQVYDVHSPLSTQLKWFRTYLGSICSSPKECSNKLKNALFILGNIGNNDVNYAFPNRSIEEIRAYLPFITEAVANATREIIRLGGTRVIVPGMFPLGCLARNLYFFPDGDKDDLGCLSSLNDLSIYFNSLIQQALASLRIEFPQAVIIYADYYNAWGFLFRNGPALGFNSTTMLKCCCGIGGPYNYDPDRECASQGVPVCSNPTEYIQWDGTHFTQAAYRRVAEYIIPDIIKELKCSYSSIQHLTEGREALHINERE

[Multiple Choices]
A. Alkaloid biosynthesis
B. NAD(+) biosynthesis
C. iron-sulfur cluster biosynthesis. .
D. L-valine from pyruvate: step 3/4. .
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

> The sequence-matched UniProt annotation assigns this protein to alkaloid biosynthesis, specifically ajmaline biosynthesis, with evidence attributed to a publication. This supports choice A, though the annotation is not an independent review of the underlying experiment.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The pronounced N-terminal hydrophobic stretch is consistent with a secretory-pathway signal peptide. That makes the listed intracellular primary-metabolism pathways—NAD(+) synthesis, iron-sulfur cluster assembly, and valine synthesis—less plausible than a specialized plant-metabolite pathway among these choices. This is a probabilistic distinction, not a unique pathway signature.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable localization-based inference meaningfully favors A over the offered alternatives without relying on the exact protein's recorded annotation. The sequence alone does not establish alkaloid biosynthesis, so the inference is limited rather than definitive.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative is comparably supported by the sequence features and choices, although the pathway cannot be identified with certainty from the signal peptide alone.


### Important caveats

- A signal peptide indicates likely entry into the secretory pathway but is not specific to alkaloid biosynthesis.
- The source annotation cites experimental evidence, but the cited study was not independently evaluated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The pronounced N-terminal hydrophobic stretch is consistent with a secretory-pathway signal peptide. That makes the listed intracellular primary-metabolism pathways—NAD(+) synthesis, iron-sulfur cluster assembly, and valine synthesis—less plausible than a specialized plant-metabolite pathway among these choices. This is a probabilistic distinction, not a unique pathway signature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable localization-based inference meaningfully favors A over the offered alternatives without relying on the exact protein's recorded annotation. The sequence alone does not establish alkaloid biosynthesis, so the inference is limited rather than definitive."
  },
  "case_id": "pathway_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein to alkaloid biosynthesis, specifically ajmaline biosynthesis, with evidence attributed to a publication. This supports choice A, though the annotation is not an independent review of the underlying experiment."
  },
  "important_caveats": [
    "A signal peptide indicates likely entry into the secretory pathway but is not specific to alkaloid biosynthesis.",
    "The source annotation cites experimental evidence, but the cited study was not independently evaluated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence features and choices, although the pathway cannot be identified with certainty from the signal peptide alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein to alkaloid biosynthesis, specifically ajmaline biosynthesis, with evidence attributed to a publication. This supports choice A, though the annotation is not an independent review of the underlying experiment.",
    "evidence_ids": ["H3", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The pronounced N-terminal hydrophobic stretch is consistent with a secretory-pathway signal peptide. That makes the listed intracellular primary-metabolism pathways—NAD(+) synthesis, iron-sulfur cluster assembly, and valine synthesis—less plausible than a specialized plant-metabolite pathway among these choices. This is a probabilistic distinction, not a unique pathway signature.",
    "missing_item_specific_fact": "",
    "reason": "A transferable localization-based inference meaningfully favors A over the offered alternatives without relying on the exact protein's recorded annotation. The sequence alone does not establish alkaloid biosynthesis, so the inference is limited rather than definitive."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence features and choices, although the pathway cannot be identified with certainty from the signal peptide alone."
  },
  "important_caveats": [
    "A signal peptide indicates likely entry into the secretory pathway but is not specific to alkaloid biosynthesis.",
    "The source annotation cites experimental evidence, but the cited study was not independently evaluated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ4 (Acetylajmalan esterase 1, EC 3.1.1.80) from Rauvolfia serpentina is explicitly annotated with the pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' (evidence C5, H3), supported by experimental evidence (ECO:0000269, PubMed:38212296). Ajmaline is a monoterpene indole alkaloid, so 'Alkaloid biosynthesis' (Choice A) is the correct pathway annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical GDS(S/T)G nucleophilic elbow motif ('GDSFSDTGN' near the N-terminus), identifying this as a serine hydrolase/esterase (α/β-hydrolase fold). Using transferable knowledge of enzyme mechanisms in each pathway: (B) NAD+ biosynthesis relies on phosphoribosyltransferases and synthetases, not serine esterases; (C) iron-sulfur cluster biosynthesis involves PLP-dependent cysteine desulfurases (NifS) and scaffold proteins (Isu), not esterases; (D) L-valine biosynthesis steps 3/4 involve dihydroxy-acid dehydratase (Fe-S enzyme) and branched-chain aminotransferase (PLP enzyme), neither of which is a serine esterase. Alkaloid biosynthesis (A) is a broad plant pathway encompassing many enzyme classes including esterases (e.g., deacetylation steps in monoterpene indole alkaloid biosynthesis). Thus, the serine hydrolase identity is mechanistically incompatible with the key enzymes of B, C, and D, while fully consistent with A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GDS(S/T)G serine hydrolase motif is a recognizable sequence feature. Knowledge of the enzyme types characterizing each pathway (transferable from biochemistry of related proteins) allows elimination of B, C, and D because their defining enzymes are not serine esterases. Alkaloid biosynthesis, being a broad category in plant secondary metabolism, encompasses esterases. This is a defensible probabilistic inference, not requiring recall of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (B, C, D) each specify very particular enzyme mechanisms (phosphoribosyltransferase, PLP-dependent desulfurase, Fe-S dehydratase/aminotransferase) that are mechanistically incompatible with a serine esterase. Only A (alkaloid biosynthesis) is a broad pathway category that includes esterase-type enzymes. No other option is defensible given the sequence motif.


### Important caveats

- The GDS(S/T)G motif is extremely common across hundreds of enzyme families; the inference relies on elimination of incompatible pathways rather than positive identification of alkaloid biosynthesis from the sequence alone.
- Knowing the source organism (Rauvolfia serpentina, a plant famous for indole alkaloids) would strengthen the inference, but this information was not provided in the model input.
- The entry was first published in June 2025 with annotation updates through 2026; the author's source snapshot is unknown but the sequence matches exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical GDS(S/T)G nucleophilic elbow motif ('GDSFSDTGN' near the N-terminus), identifying this as a serine hydrolase/esterase (α/β-hydrolase fold). Using transferable knowledge of enzyme mechanisms in each pathway: (B) NAD+ biosynthesis relies on phosphoribosyltransferases and synthetases, not serine esterases; (C) iron-sulfur cluster biosynthesis involves PLP-dependent cysteine desulfurases (NifS) and scaffold proteins (Isu), not esterases; (D) L-valine biosynthesis steps 3/4 involve dihydroxy-acid dehydratase (Fe-S enzyme) and branched-chain aminotransferase (PLP enzyme), neither of which is a serine esterase. Alkaloid biosynthesis (A) is a broad plant pathway encompassing many enzyme classes including esterases (e.g., deacetylation steps in monoterpene indole alkaloid biosynthesis). Thus, the serine hydrolase identity is mechanistically incompatible with the key enzymes of B, C, and D, while fully consistent with A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GDS(S/T)G serine hydrolase motif is a recognizable sequence feature. Knowledge of the enzyme types characterizing each pathway (transferable from biochemistry of related proteins) allows elimination of B, C, and D because their defining enzymes are not serine esterases. Alkaloid biosynthesis, being a broad category in plant secondary metabolism, encompasses esterases. This is a defensible probabilistic inference, not requiring recall of this specific protein's database entry."
  },
  "case_id": "pathway_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ4 (Acetylajmalan esterase 1, EC 3.1.1.80) from Rauvolfia serpentina is explicitly annotated with the pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' (evidence C5, H3), supported by experimental evidence (ECO:0000269, PubMed:38212296). Ajmaline is a monoterpene indole alkaloid, so 'Alkaloid biosynthesis' (Choice A) is the correct pathway annotation."
  },
  "important_caveats": [
    "The GDS(S/T)G motif is extremely common across hundreds of enzyme families; the inference relies on elimination of incompatible pathways rather than positive identification of alkaloid biosynthesis from the sequence alone.",
    "Knowing the source organism (Rauvolfia serpentina, a plant famous for indole alkaloids) would strengthen the inference, but this information was not provided in the model input.",
    "The entry was first published in June 2025 with annotation updates through 2026; the author's source snapshot is unknown but the sequence matches exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (B, C, D) each specify very particular enzyme mechanisms (phosphoribosyltransferase, PLP-dependent desulfurase, Fe-S dehydratase/aminotransferase) that are mechanistically incompatible with a serine esterase. Only A (alkaloid biosynthesis) is a broad pathway category that includes esterase-type enzymes. No other option is defensible given the sequence motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ4 (Acetylajmalan esterase 1, EC 3.1.1.80) from Rauvolfia serpentina is explicitly annotated with the pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' (evidence C5, H3), supported by experimental evidence (ECO:0000269, PubMed:38212296). Ajmaline is a monoterpene indole alkaloid, so 'Alkaloid biosynthesis' (Choice A) is the correct pathway annotation.",
    "evidence_ids": ["C5", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical GDS(S/T)G nucleophilic elbow motif ('GDSFSDTGN' near the N-terminus), identifying this as a serine hydrolase/esterase (α/β-hydrolase fold). Using transferable knowledge of enzyme mechanisms in each pathway: (B) NAD+ biosynthesis relies on phosphoribosyltransferases and synthetases, not serine esterases; (C) iron-sulfur cluster biosynthesis involves PLP-dependent cysteine desulfurases (NifS) and scaffold proteins (Isu), not esterases; (D) L-valine biosynthesis steps 3/4 involve dihydroxy-acid dehydratase (Fe-S enzyme) and branched-chain aminotransferase (PLP enzyme), neither of which is a serine esterase. Alkaloid biosynthesis (A) is a broad plant pathway encompassing many enzyme classes including esterases (e.g., deacetylation steps in monoterpene indole alkaloid biosynthesis). Thus, the serine hydrolase identity is mechanistically incompatible with the key enzymes of B, C, and D, while fully consistent with A.",
    "missing_item_specific_fact": "",
    "reason": "The GDS(S/T)G serine hydrolase motif is a recognizable sequence feature. Knowledge of the enzyme types characterizing each pathway (transferable from biochemistry of related proteins) allows elimination of B, C, and D because their defining enzymes are not serine esterases. Alkaloid biosynthesis, being a broad category in plant secondary metabolism, encompasses esterases. This is a defensible probabilistic inference, not requiring recall of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (B, C, D) each specify very particular enzyme mechanisms (phosphoribosyltransferase, PLP-dependent desulfurase, Fe-S dehydratase/aminotransferase) that are mechanistically incompatible with a serine esterase. Only A (alkaloid biosynthesis) is a broad pathway category that includes esterase-type enzymes. No other option is defensible given the sequence motif."
  },
  "important_caveats": [
    "The GDS(S/T)G motif is extremely common across hundreds of enzyme families; the inference relies on elimination of incompatible pathways rather than positive identification of alkaloid biosynthesis from the sequence alone.",
    "Knowing the source organism (Rauvolfia serpentina, a plant famous for indole alkaloids) would strengthen the inference, but this information was not provided in the model input.",
    "The entry was first published in June 2025 with annotation updates through 2026; the author's source snapshot is unknown but the sequence matches exactly."
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
  "benchmark_sequence_length": 379,
  "benchmark_sequence_sha256": "65d919ebd4646b3b1ec9c5e4e65248a0a9278098c4edeb33747ee0fa238c53ed",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 379,
  "current_source_sequence_sha256": "65d919ebd4646b3b1ec9c5e4e65248a0a9278098c4edeb33747ee0fa238c53ed",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXJ4",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069",
  "selected_historical_source_sequence_length": 379,
  "selected_historical_source_sequence_sha256": "65d919ebd4646b3b1ec9c5e4e65248a0a9278098c4edeb33747ee0fa238c53ed",
  "selected_historical_version": {
    "accession": "P0DXJ4",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AAE1_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"3.1.1.80\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Acetylajmalan esterase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsAAE1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis; ajmaline biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   AAE1_RAUSE              Reviewed;         379 AA.\nAC   P0DXJ4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Acetylajmalan esterase 1 {ECO:0000303|PubMed:38212296};\nDE            Short=RsAAE1 {ECO:0000303|PubMed:38212296};\nDE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};\nDE   Flags: Precursor;\nGN   Name=AAE1 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:19.289362+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069",
  "url": "https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE\nRP   SPECIFICITY, AND BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:19.289362+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069",
  "url": "https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.\nCC       {ECO:0000269|PubMed:38212296}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:19.289362+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069",
  "url": "https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
