# cofactor_0184

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0184.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — pyridoxal 5&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI

[Multiple Choices]
A. Mn(2+)
B. pyridoxal 5'-phosphate
C. Na(+)
D. FMN
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact-sequence-matched UniProt record annotates pyridoxal 5'-phosphate as the cofactor, with experimental evidence cited; a crystal-structure reference also reports the protein in complex with PLP. This supports choice B.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the cystathionine gamma-synthase family of PLP-dependent enzymes. Family recognition and the conserved PLP-enzyme active-site architecture provide a transferable basis for choosing PLP over Mn2+, Na+, or FMN.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference meaningfully distinguishes PLP among these alternatives without requiring the exact protein's database annotation. The inference is strong but is not itself experimental confirmation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> PLP is the clearly supported choice among the offered cofactors.


### Important caveats

- The reviewer-only evidence supports the key but was not available as original input.
- The sequence-based family inference is probabilistic; direct cofactor evidence comes from the matched source record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the cystathionine gamma-synthase family of PLP-dependent enzymes. Family recognition and the conserved PLP-enzyme active-site architecture provide a transferable basis for choosing PLP over Mn2+, Na+, or FMN.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully distinguishes PLP among these alternatives without requiring the exact protein's database annotation. The inference is strong but is not itself experimental confirmation."
  },
  "case_id": "cofactor_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record annotates pyridoxal 5'-phosphate as the cofactor, with experimental evidence cited; a crystal-structure reference also reports the protein in complex with PLP. This supports choice B."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available as original input.",
    "The sequence-based family inference is probabilistic; direct cofactor evidence comes from the matched source record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "PLP is the clearly supported choice among the offered cofactors."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record annotates pyridoxal 5'-phosphate as the cofactor, with experimental evidence cited; a crystal-structure reference also reports the protein in complex with PLP. This supports choice B.",
    "evidence_ids": ["C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the cystathionine gamma-synthase family of PLP-dependent enzymes. Family recognition and the conserved PLP-enzyme active-site architecture provide a transferable basis for choosing PLP over Mn2+, Na+, or FMN.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully distinguishes PLP among these alternatives without requiring the exact protein's database annotation. The inference is strong but is not itself experimental confirmation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "PLP is the clearly supported choice among the offered cofactors."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available as original input.",
    "The sequence-based family inference is probabilistic; direct cofactor evidence comes from the matched source record."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (Q9ZPL5, Cystathionine gamma-synthase 1, chloroplastic, EC 2.5.1.160) explicitly lists pyridoxal 5'-phosphate as the cofactor, supported by experimental evidence (ECO:0000269) from two crystallographic studies (PubMed:10438597 and PubMed:11518531) showing X-ray structures in complex with PLP at Lys-356. The evidence is experimental (X-ray crystallography), not merely computational inference.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the motif 'GADLVLHSATKFLGG' which includes the conserved 'HSATK' pattern characteristic of fold-type I PLP-dependent enzymes, where the lysine in the 'T-K' context forms the internal aldimine (Schiff base) with PLP. This is a well-known signature across the PLP-dependent enzyme superfamily (transaminases, decarboxylases, racemases, and trans-sulfuration enzymes). Furthermore, family-level knowledge from other proteins strongly supports PLP: enzymes in the Cys/Met trans-sulfuration pathway (cystathionine beta-synthase, cystathionine gamma-synthase, O-acetylhomoserine sulfhydrylase) are universally PLP-dependent across all organisms studied. The ~540-residue length and domain architecture are consistent with fold-type I PLP enzymes. The distractors can be eliminated: FMN-binding proteins show Rossmann-fold 'GxGxxG' motifs (absent here); Mn(2+) sites typically cluster His/Asp/Glu residues in specific geometries (not matching); Na(+) is not a recognized catalytic cofactor for amino acid metabolism enzymes. The PLP-binding lysine motif and the amino acid metabolism context together meaningfully distinguish choice B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the PLP-binding lysine motif (HSATK) and apply well-established family-level knowledge that trans-sulfuration pathway enzymes and amino acid metabolism enzymes broadly require PLP. The absence of Rossmann-fold motifs rules out FMN, and the absence of typical metal-binding clusters rules out Mn(2+). Na(+) as a catalytic cofactor is implausible for this enzyme class. This constitutes legitimate transferable knowledge from the PLP-dependent enzyme superfamily and amino acid biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PLP-binding motif and family-level biochemistry clearly favor PLP over the other three options. FMN requires a distinct Rossmann-fold architecture not present; Mn(2+) requires specific metal-coordinating residue clusters not matching; Na(+) is not a recognized cofactor for this enzyme class. No alternative option is defensible.


### Important caveats

- The reviewer evidence confirms the protein is Cystathionine gamma-synthase from Nicotiana tabacum, but this identity was not given to the evaluated model. The reasoning relies on recognizing the PLP-binding motif and applying family-level knowledge about amino acid metabolism enzymes.
- The PLP-binding lysine in the crystal structure is annotated at position 356 (Lys-356), which corresponds to the K in the 'HSATK' motif visible in the sequence.
- The evidence is experimental (X-ray crystallography at 2.90 and 3.10 Å resolution), providing high confidence in the cofactor assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the motif 'GADLVLHSATKFLGG' which includes the conserved 'HSATK' pattern characteristic of fold-type I PLP-dependent enzymes, where the lysine in the 'T-K' context forms the internal aldimine (Schiff base) with PLP. This is a well-known signature across the PLP-dependent enzyme superfamily (transaminases, decarboxylases, racemases, and trans-sulfuration enzymes). Furthermore, family-level knowledge from other proteins strongly supports PLP: enzymes in the Cys/Met trans-sulfuration pathway (cystathionine beta-synthase, cystathionine gamma-synthase, O-acetylhomoserine sulfhydrylase) are universally PLP-dependent across all organisms studied. The ~540-residue length and domain architecture are consistent with fold-type I PLP enzymes. The distractors can be eliminated: FMN-binding proteins show Rossmann-fold 'GxGxxG' motifs (absent here); Mn(2+) sites typically cluster His/Asp/Glu residues in specific geometries (not matching); Na(+) is not a recognized catalytic cofactor for amino acid metabolism enzymes. The PLP-binding lysine motif and the amino acid metabolism context together meaningfully distinguish choice B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PLP-binding lysine motif (HSATK) and apply well-established family-level knowledge that trans-sulfuration pathway enzymes and amino acid metabolism enzymes broadly require PLP. The absence of Rossmann-fold motifs rules out FMN, and the absence of typical metal-binding clusters rules out Mn(2+). Na(+) as a catalytic cofactor is implausible for this enzyme class. This constitutes legitimate transferable knowledge from the PLP-dependent enzyme superfamily and amino acid biochemistry."
  },
  "case_id": "cofactor_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (Q9ZPL5, Cystathionine gamma-synthase 1, chloroplastic, EC 2.5.1.160) explicitly lists pyridoxal 5'-phosphate as the cofactor, supported by experimental evidence (ECO:0000269) from two crystallographic studies (PubMed:10438597 and PubMed:11518531) showing X-ray structures in complex with PLP at Lys-356. The evidence is experimental (X-ray crystallography), not merely computational inference."
  },
  "important_caveats": [
    "The reviewer evidence confirms the protein is Cystathionine gamma-synthase from Nicotiana tabacum, but this identity was not given to the evaluated model. The reasoning relies on recognizing the PLP-binding motif and applying family-level knowledge about amino acid metabolism enzymes.",
    "The PLP-binding lysine in the crystal structure is annotated at position 356 (Lys-356), which corresponds to the K in the 'HSATK' motif visible in the sequence.",
    "The evidence is experimental (X-ray crystallography at 2.90 and 3.10 Å resolution), providing high confidence in the cofactor assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PLP-binding motif and family-level biochemistry clearly favor PLP over the other three options. FMN requires a distinct Rossmann-fold architecture not present; Mn(2+) requires specific metal-coordinating residue clusters not matching; Na(+) is not a recognized cofactor for this enzyme class. No alternative option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (Q9ZPL5, Cystathionine gamma-synthase 1, chloroplastic, EC 2.5.1.160) explicitly lists pyridoxal 5'-phosphate as the cofactor, supported by experimental evidence (ECO:0000269) from two crystallographic studies (PubMed:10438597 and PubMed:11518531) showing X-ray structures in complex with PLP at Lys-356. The evidence is experimental (X-ray crystallography), not merely computational inference.",
    "evidence_ids": ["C5", "C7", "C8", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the motif 'GADLVLHSATKFLGG' which includes the conserved 'HSATK' pattern characteristic of fold-type I PLP-dependent enzymes, where the lysine in the 'T-K' context forms the internal aldimine (Schiff base) with PLP. This is a well-known signature across the PLP-dependent enzyme superfamily (transaminases, decarboxylases, racemases, and trans-sulfuration enzymes). Furthermore, family-level knowledge from other proteins strongly supports PLP: enzymes in the Cys/Met trans-sulfuration pathway (cystathionine beta-synthase, cystathionine gamma-synthase, O-acetylhomoserine sulfhydrylase) are universally PLP-dependent across all organisms studied. The ~540-residue length and domain architecture are consistent with fold-type I PLP enzymes. The distractors can be eliminated: FMN-binding proteins show Rossmann-fold 'GxGxxG' motifs (absent here); Mn(2+) sites typically cluster His/Asp/Glu residues in specific geometries (not matching); Na(+) is not a recognized catalytic cofactor for amino acid metabolism enzymes. The PLP-binding lysine motif and the amino acid metabolism context together meaningfully distinguish choice B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PLP-binding lysine motif (HSATK) and apply well-established family-level knowledge that trans-sulfuration pathway enzymes and amino acid metabolism enzymes broadly require PLP. The absence of Rossmann-fold motifs rules out FMN, and the absence of typical metal-binding clusters rules out Mn(2+). Na(+) as a catalytic cofactor is implausible for this enzyme class. This constitutes legitimate transferable knowledge from the PLP-dependent enzyme superfamily and amino acid biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PLP-binding motif and family-level biochemistry clearly favor PLP over the other three options. FMN requires a distinct Rossmann-fold architecture not present; Mn(2+) requires specific metal-coordinating residue clusters not matching; Na(+) is not a recognized cofactor for this enzyme class. No alternative option is defensible."
  },
  "important_caveats": [
    "The reviewer evidence confirms the protein is Cystathionine gamma-synthase from Nicotiana tabacum, but this identity was not given to the evaluated model. The reasoning relies on recognizing the PLP-binding motif and applying family-level knowledge about amino acid metabolism enzymes.",
    "The PLP-binding lysine in the crystal structure is annotated at position 356 (Lys-356), which corresponds to the K in the 'HSATK' motif visible in the sequence.",
    "The evidence is experimental (X-ray crystallography at 2.90 and 3.10 Å resolution), providing high confidence in the cofactor assignment."
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
  "benchmark_sequence_length": 540,
  "benchmark_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "current_entry_audit": {
    "entryVersion": 112,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 2
  },
  "current_record_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 540,
  "current_source_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 110,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9ZPL5",
  "selected_historical_entry_version": 110,
  "selected_historical_record_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "selected_historical_source_sequence_length": 540,
  "selected_historical_source_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "selected_historical_version": {
    "accession": "Q9ZPL5",
    "database": "Swiss-Prot",
    "entryVersion": 110,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CGS1_TOBAC",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9ZPL5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":112,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common tobacco\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Solanales\",\"Solanaceae\",\"Nicotianoideae\",\"Nicotianeae\",\"Nicotiana\"],\"scientificName\":\"Nicotiana tabacum\",\"taxonId\":4097}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10595588\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.160\"}],\"fullName\":{\"value\":\"Cystathionine gamma-synthase 1, chloroplastic\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:597326\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10438597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11518531\",\"source\":\"PubMed\"}],\"name\":\"pyridoxal 5'-phosphate\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10438597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11518531\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 pyridoxal 5'-phosphate per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Clausen T.\",\"Wahl M.C.\",\"Messerschmidt A.\",\"Huber R.\",\"Fuhrmann J.C.\",\"Laber B.\",\"Streber W.\",\"Steegborn C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10595588\"},{\"database\":\"DOI\",\"id\":\"10.1515/bc.1999.157\"}],\"citationType\":\"journal article\",\"firstPage\":\"1237\",\"id\":\"10595588\",\"journal\":\"Biol. Chem.\",\"lastPage\":\"1242\",\"publicationDate\":\"1999\",\"title\":\"Cloning, purification and characterisation of cystathionine gamma-synthase from Nicotiana tabacum.\",\"volume\":\"380\"},\"referenceNumber\":3,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] OF 97-540\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Steegborn C.\",\"Messerschmidt A.\",\"Laber B.\",\"Streber W.\",\"Huber R.\",\"Clausen T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10438597\"},{\"database\":\"DOI\",\"id\":\"10.1006/jmbi.1999.2935\"}],\"citationType\":\"journal article\",\"firstPage\":\"983\",\"id\":\"10438597\",\"journal\":\"J. Mol. Biol.\",\"lastPage\":\"996\",\"publicationDate\":\"1999\",\"title\":\"The crystal structure of cystathionine gamma-synthase from Nicotiana tabacum reveals its substrate and reaction specificity.\",\"volume\":\"290\"},\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.90 ANGSTROMS) IN COMPLEX WITH PYRIDOXAL PHOSPHATE AT LYS-356\",\"COFACTOR\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Steegborn C.\",\"Laber B.\",\"Messerschmidt A.\",\"Huber R.\",\"Clausen T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11518531\"},{\"database\":\"DOI\",\"id\":\"10.1006/jmbi.2001.4880\"}],\"citationType\":\"journal article\",\"firstPage\":\"789\",\"id\":\"11518531\",\"journal\":\"J. Mol. Biol.\",\"lastPage\":\"801\",\"publicationDate\":\"2001\",\"title\":\"Crystal structures of cystathionine gamma-synthase inhibitor complexes rationalize the increased affinity of a novel inhibitor.\",\"volume\":\"311\"},\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (3.10 ANGSTROMS) IN COMPLEX WITH PYRIDOXAL PHOSPHATE AT LYS-356\",\"COFACTOR\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H1",
  "excerpt": "ID   CGS1_TOBAC              Reviewed;         540 AA.\nAC   Q9ZPL5; W8SGH6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 2.\nDT   28-JAN-2026, entry version 110.\nDE   RecName: Full=Cystathionine gamma-synthase 1, chloroplastic;\nDE            EC=2.5.1.160 {ECO:0000269|PubMed:10595588};\nDE   Flags: Precursor;\nGN   Name=CGS1 {ECO:0000305}; ORFNames=LOC107822634;\nOS   Nicotiana tabacum (Common tobacco).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Solanales; Solanaceae; Nicotianoideae; Nicotianeae;\nOC   Nicotiana.\nOX   NCBI_TaxID=4097;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cystathionine gamma-synthase 1, chloroplastic;\nDE            EC=2.5.1.160 {ECO:0000269|PubMed:10595588};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   NUCLEOTIDE SEQUENCE [MRNA] OF 97-540, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.\nRX   PubMed=10595588; DOI=10.1515/bc.1999.157;\nRA   Clausen T., Wahl M.C., Messerschmidt A., Huber R., Fuhrmann J.C., Laber B.,\nRA   Streber W., Steegborn C.;\nRT   \"Cloning, purification and characterisation of cystathionine gamma-synthase\nRT   from Nicotiana tabacum.\";\nRL   Biol. Chem. 380:1237-1242(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H4",
  "excerpt": "RN   [4]\nRP   X-RAY CRYSTALLOGRAPHY (2.90 ANGSTROMS) IN COMPLEX WITH PYRIDOXAL PHOSPHATE\nRP   AT LYS-356, COFACTOR, AND SUBUNIT.\nRX   PubMed=10438597; DOI=10.1006/jmbi.1999.2935;\nRA   Steegborn C., Messerschmidt A., Laber B., Streber W., Huber R., Clausen T.;\nRT   \"The crystal structure of cystathionine gamma-synthase from Nicotiana\nRT   tabacum reveals its substrate and reaction specificity.\";\nRL   J. Mol. Biol. 290:983-996(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H5",
  "excerpt": "RN   [5]\nRP   X-RAY CRYSTALLOGRAPHY (3.10 ANGSTROMS) IN COMPLEX WITH PYRIDOXAL PHOSPHATE\nRP   AT LYS-356, COFACTOR, AND SUBUNIT.\nRX   PubMed=11518531; DOI=10.1006/jmbi.2001.4880;\nRA   Steegborn C., Laber B., Messerschmidt A., Huber R., Clausen T.;\nRT   \"Crystal structures of cystathionine gamma-synthase inhibitor complexes\nRT   rationalize the increased affinity of a novel inhibitor.\";\nRL   J. Mol. Biol. 311:789-801(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;\nCC         Evidence={ECO:0000269|PubMed:10438597, ECO:0000269|PubMed:11518531};\nCC       Note=Binds 1 pyridoxal 5'-phosphate per subunit.\nCC       {ECO:0000269|PubMed:10438597, ECO:0000269|PubMed:11518531};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
