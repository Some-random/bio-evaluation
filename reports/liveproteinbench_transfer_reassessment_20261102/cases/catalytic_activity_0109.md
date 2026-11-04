# catalytic_activity_0109

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0109.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — Hydrolysis of terminal, non-reducing (1-&gt;4)-linked alpha-D-glucose residues with release of alpha-D-glucose.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKTFAPLLATLLLAGFGSALQWWEHGNFYQVYPRSFKDSDGNGIGDLDGVTEKLQYLKDVGMDGIWLSPIFASPMADFGYDISDFYNIQGEYGDLAAFERLSAKCKELGLRLILDFVPNHTSNQHEYFKKSVQKEDPYTNYYVWHPGVTNEDGTKSPPSNWISVFRGSAWEWNEDRQEYYLHQFLKEQPDLNYRDPALVEEMKNVLKFWLNKGVSGFRIDAVPYLFESVEVENRYVDEPLSRATDDAENPAYLIHNQTMDQPETYDMIYQWRAVLDEFTAKDNQTRIMMTEGYTSIPNVMKFFGEGEQNGAQIPFNFQMISNLRKTSTAADFARYANLWLDNLPAGRRSNWVLGNHDNNRIGSRLGEAKIDLYNIALQTLPDIAVTYYGEEIGMVDQPIPFNETVDPAGLRAGPDDYTLYSRDPARTPMQWNSDKNAGFSSADKTWLPVATNYKQLNVKAQDAAQKSHLKLFKRLTTYRKRQILTHGDLDLRTTDSNLVLYKRKVDKVGYVVVVLNFSDEPQSLAAIKQQFPGADDRLQVVASSKLVTIKDNKWINVADTELPGESAIVLQKLWGPNPVVVYEA

[Multiple Choices]
A. N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
B. AH2 + 2 S-adenosyl-L-methionine = 2 5'-deoxyadenosin-5'-yl radical + 2 L-methionine + A + 2 H(+)
C. Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.
D. beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)
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

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1300)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein the reaction in option C and cites experimental evidence codes for that catalytic activity. This supports the key, though the cited primary studies were not independently reviewed here.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a hydrophobic signal-peptide-like segment, consistent with a secreted enzyme, and the long sequence is compatible with a eukaryotic glycoside hydrolase. Family-level knowledge of secreted alpha-glucosidases makes cleavage of alpha-glucose linkages (C) a credible inference. The alternatives instead describe a small-molecule methyltransferase, a radical-SAM reaction, or ATP-dependent NAD synthesis, none of which fits that sequence/context nearly as well.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-family patterns meaningfully distinguish the glycoside-hydrolysis option from the three chemically and biologically different alternatives, even without establishing the exact substrate specificity from first principles.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions describe distinct enzyme activities, and the sequence/context supports option C over the others."
  },
  "important_caveats": [
    "The signal-peptide and family interpretation is an inference from the supplied sequence, not direct experimental evidence shown to the model.",
    "The database annotation cites experimental evidence, but the primary papers were not independently validated in this review."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B0XAA1 (sequence matched) annotates this protein as Salivary alpha-glucosidase with EC 3.2.1.20 and the catalytic activity 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' This annotation is backed by experimental evidence (ECO:0000269) from two independent PubMed studies (25746591 and 38428508). The expected answer C matches the annotated reaction exactly.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a clear hydrophobic signal peptide (MKTFAPLLATLLLAGFGSALQWWEHG), indicating a secreted protein. This immediately disfavors options B (radical SAM enzymes are intracellular and require a CX3CX2C motif, which is absent) and D (NAD synthase/NMN adenylyltransferase is intracellular). The total length of 584 residues is far too long for option A (COMT is ~271 aa, cytoplasmic, no signal peptide). The remaining option C (alpha-glucosidase, GH31 family) is consistent with: (1) a secreted insect salivary enzyme, (2) the ~500-600 aa length typical of GH31 catalytic domains, (3) the absence of motifs diagnostic of the other three families. Family-level knowledge that insect salivary alpha-glucosidases (GH31) are secreted proteins of this approximate size provides a credible transferable inference to select C among the four offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal peptide (visible in the N-terminal hydrophobic stretch), the 584-aa length, the absence of a radical SAM CX3CX2C motif, and general knowledge that COMT is ~271 aa and cytoplasmic collectively eliminate A, B, and D. GH31 alpha-glucosidases in insects are well-known secreted salivary enzymes of this size, making C the only viable option through family-level reasoning without needing the exact database annotation for this specific protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent very different enzyme classes (methyltransferase, radical SAM, glycosidase, nucleotidyltransferase). The signal peptide, length, and absence of family-specific motifs for A, B, and D leave C as the uniquely consistent choice. No two options are simultaneously defensible.


### Important caveats

- The signal peptide recognition is based on the hydrophobic N-terminal stretch; while highly suggestive, formal signal peptide prediction tools would confirm this.
- The argument relies on the four offered choices being the only alternatives; in a broader search, other secreted 584-aa enzymes could exist, but the question constrains the answer space to these four.
- The UniProt annotation is experimentally supported (ECO:0000269) from two independent studies, strengthening confidence in the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a clear hydrophobic signal peptide (MKTFAPLLATLLLAGFGSALQWWEHG), indicating a secreted protein. This immediately disfavors options B (radical SAM enzymes are intracellular and require a CX3CX2C motif, which is absent) and D (NAD synthase/NMN adenylyltransferase is intracellular). The total length of 584 residues is far too long for option A (COMT is ~271 aa, cytoplasmic, no signal peptide). The remaining option C (alpha-glucosidase, GH31 family) is consistent with: (1) a secreted insect salivary enzyme, (2) the ~500-600 aa length typical of GH31 catalytic domains, (3) the absence of motifs diagnostic of the other three families. Family-level knowledge that insect salivary alpha-glucosidases (GH31) are secreted proteins of this approximate size provides a credible transferable inference to select C among the four offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide (visible in the N-terminal hydrophobic stretch), the 584-aa length, the absence of a radical SAM CX3CX2C motif, and general knowledge that COMT is ~271 aa and cytoplasmic collectively eliminate A, B, and D. GH31 alpha-glucosidases in insects are well-known secreted salivary enzymes of this size, making C the only viable option through family-level reasoning without needing the exact database annotation for this specific protein."
  },
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B0XAA1 (sequence matched) annotates this protein as Salivary alpha-glucosidase with EC 3.2.1.20 and the catalytic activity 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' This annotation is backed by experimental evidence (ECO:0000269) from two independent PubMed studies (25746591 and 38428508). The expected answer C matches the annotated reaction exactly."
  },
  "important_caveats": [
    "The signal peptide recognition is based on the hydrophobic N-terminal stretch; while highly suggestive, formal signal peptide prediction tools would confirm this.",
    "The argument relies on the four offered choices being the only alternatives; in a broader search, other secreted 584-aa enzymes could exist, but the question constrains the answer space to these four.",
    "The UniProt annotation is experimentally supported (ECO:0000269) from two independent studies, strengthening confidence in the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes (methyltransferase, radical SAM, glycosidase, nucleotidyltransferase). The signal peptide, length, and absence of family-specific motifs for A, B, and D leave C as the uniquely consistent choice. No two options are simultaneously defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B0XAA1 (sequence matched) annotates this protein as Salivary alpha-glucosidase with EC 3.2.1.20 and the catalytic activity 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' This annotation is backed by experimental evidence (ECO:0000269) from two independent PubMed studies (25746591 and 38428508). The expected answer C matches the annotated reaction exactly.",
    "evidence_ids": ["C5", "C4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a clear hydrophobic signal peptide (MKTFAPLLATLLLAGFGSALQWWEHG), indicating a secreted protein. This immediately disfavors options B (radical SAM enzymes are intracellular and require a CX3CX2C motif, which is absent) and D (NAD synthase/NMN adenylyltransferase is intracellular). The total length of 584 residues is far too long for option A (COMT is ~271 aa, cytoplasmic, no signal peptide). The remaining option C (alpha-glucosidase, GH31 family) is consistent with: (1) a secreted insect salivary enzyme, (2) the ~500-600 aa length typical of GH31 catalytic domains, (3) the absence of motifs diagnostic of the other three families. Family-level knowledge that insect salivary alpha-glucosidases (GH31) are secreted proteins of this approximate size provides a credible transferable inference to select C among the four offered choices.",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide (visible in the N-terminal hydrophobic stretch), the 584-aa length, the absence of a radical SAM CX3CX2C motif, and general knowledge that COMT is ~271 aa and cytoplasmic collectively eliminate A, B, and D. GH31 alpha-glucosidases in insects are well-known secreted salivary enzymes of this size, making C the only viable option through family-level reasoning without needing the exact database annotation for this specific protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes (methyltransferase, radical SAM, glycosidase, nucleotidyltransferase). The signal peptide, length, and absence of family-specific motifs for A, B, and D leave C as the uniquely consistent choice. No two options are simultaneously defensible."
  },
  "important_caveats": [
    "The signal peptide recognition is based on the hydrophobic N-terminal stretch; while highly suggestive, formal signal peptide prediction tools would confirm this.",
    "The argument relies on the four offered choices being the only alternatives; in a broader search, other secreted 584-aa enzymes could exist, but the question constrains the answer space to these four.",
    "The UniProt annotation is experimentally supported (ECO:0000269) from two independent studies, strengthening confidence in the key."
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
  "benchmark_sequence_length": 584,
  "benchmark_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "current_entry_audit": {
    "entryVersion": 94,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-04-08",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 584,
  "current_source_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 92,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B0XAA1",
  "selected_historical_entry_version": 92,
  "selected_historical_record_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "selected_historical_source_sequence_length": 584,
  "selected_historical_source_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "selected_historical_version": {
    "accession": "B0XAA1",
    "database": "Swiss-Prot",
    "entryVersion": 92,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MALT_CULQU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B0XAA1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":94,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-04-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Southern house mosquito\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Nematocera\",\"Culicoidea\",\"Culicidae\",\"Culicinae\",\"Culicini\",\"Culex\",\"Culex\"],\"scientificName\":\"Culex quinquefasciatus\",\"synonyms\":[\"Culex pungens\"],\"taxonId\":7176}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"value\":\"CQMalI\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.20\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"Salivary alpha-glucosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"CxGluc\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.20\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Suthangkornkul R.\",\"Sirichaiyakul P.\",\"Sungvornyothin S.\",\"Thepouyporn A.\",\"Svasti J.\",\"Arthan D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25746591\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.pep.2015.02.018\"}],\"citationType\":\"journal article\",\"firstPage\":\"145\",\"id\":\"25746591\",\"journal\":\"Protein Expr. Purif.\",\"lastPage\":\"150\",\"publicationDate\":\"2015\",\"title\":\"Functional expression and molecular characterization of Culex quinquefasciatus salivary alpha-glucosidase (MalI).\",\"volume\":\"110\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"GLYCOSYLATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Williams A.E.\",\"Gittis A.G.\",\"Botello K.\",\"Cruz P.\",\"Martin-Martin I.\",\"Valenzuela Leon P.C.\",\"Sumner B.\",\"Bonilla B.\",\"Calvo E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38428508\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ibmb.2024.104097\"}],\"citationType\":\"journal article\",\"firstPage\":\"104097\",\"id\":\"38428508\",\"journal\":\"Insect Biochem. Mol. Biol.\",\"lastPage\":\"104097\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.\",\"volume\":\"167\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H1",
  "excerpt": "ID   MALT_CULQU              Reviewed;         584 AA.\nAC   B0XAA1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-APR-2008, sequence version 1.\nDT   28-JAN-2026, entry version 92.\nDE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=CxGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\nDE   AltName: Full=CQMalI {ECO:0000303|PubMed:25746591};\nDE   Flags: Precursor;\nGN   Name=MAL1 {ECO:0000303|PubMed:25746591};\nGN   ORFNames=CpipJ_CPIJ016362 {ECO:0000312|EMBL:EDS43598.1};\nOS   Culex quinquefasciatus (Southern house mosquito) (Culex pungens).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;\nOC   Culicinae; Culicini; Culex; Culex.\nOX   NCBI_TaxID=7176;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=CxGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\nDE   AltName: Full=CQMalI {ECO:0000303|PubMed:25746591};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND GLYCOSYLATION.\nRX   PubMed=25746591; DOI=10.1016/j.pep.2015.02.018;\nRA   Suthangkornkul R., Sirichaiyakul P., Sungvornyothin S., Thepouyporn A.,\nRA   Svasti J., Arthan D.;\nRT   \"Functional expression and molecular characterization of Culex\nRT   quinquefasciatus salivary alpha-glucosidase (MalI).\";\nRL   Protein Expr. Purif. 110:145-150(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H4",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR\nRP   LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=38428508; DOI=10.1016/j.ibmb.2024.104097;\nRA   Williams A.E., Gittis A.G., Botello K., Cruz P., Martin-Martin I.,\nRA   Valenzuela Leon P.C., Sumner B., Bonilla B., Calvo E.;\nRT   \"Structural and functional comparisons of salivary alpha-glucosidases from\nRT   the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex\nRT   quinquefasciatus.\";\nRL   Insect Biochem. Mol. Biol. 167:104097-104097(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-\nCC         glucose residues with release of alpha-D-glucose.; EC=3.2.1.20;\nCC         Evidence={ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
