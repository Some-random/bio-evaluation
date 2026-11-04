# active_site_0064

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0064.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 64 (Nucleophile (Probable))

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTEELTTVRDACARTLENTARTLHLGASGTEFVAAFRAMTDHWGAARPHDLPLSDVSPDGSPVEYAVDLGGLAPALQFAMEPLTAGVPARDPLAARAIMPLLAGRYGADATRWSALADRLLPDDAHGPHVSMYGAEVRAGAPIRFKAWFYLNVTGPDGAFNLLYSALERMGTTHLWPVVQAHVHRAGEDVPFLLSLDLSDDPAARVKVYFRHFAADVEEVAAVLKAYPGFEPGEVRAFCKVMMGGRRRFSDQPAVTCVSLLDAQTFDRTAATLYVPLWTYAEHDGEVRQRVHRTLAAWPEALYRYDSVLAGIAHRGLDAGTGIHNYISWQPGRTRPRMKVYLSPEMHDVTPPPLGVSQQHHLSGQTTARGRTE

[Multiple Choices]
A. Position 213 (Proton acceptor)
B. Position 64 (Nucleophile (Probable))
C. Position 931 (Proton acceptor)
D. Position 268 (Proton acceptor)
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

> The matching UniProt entry annotates position 64 as a probable nucleophile, citing a publication, and the archived record carries the same annotation. This supports the keyed choice, though the qualifier “probable” means it is not presented as definitive experimental proof.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable solver could recognize the sequence as consistent with an aromatic prenyltransferase family and use transferable family knowledge that a conserved catalytic residue can participate directly in prenylation. Position 64 is a tyrosine in this sequence, making the offered probable-nucleophile assignment plausible; position 931 is outside the 373-residue sequence. This is a family-based, probabilistic inference, not proof that this exact residue has the annotated role.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level sequence and catalytic-residue pattern offers a meaningful basis for preferring B among these choices without needing to recall this protein’s database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports position 64 as the probable nucleophile. No other offered option is comparably supported as the catalytic residue; position 931 is beyond the sequence length.


### Important caveats

- The active-site annotation is explicitly qualified as probable.
- The reviewer-only source supports applicability to the supplied sequence, but that source identity and annotation were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable solver could recognize the sequence as consistent with an aromatic prenyltransferase family and use transferable family knowledge that a conserved catalytic residue can participate directly in prenylation. Position 64 is a tyrosine in this sequence, making the offered probable-nucleophile assignment plausible; position 931 is outside the 373-residue sequence. This is a family-based, probabilistic inference, not proof that this exact residue has the annotated role.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level sequence and catalytic-residue pattern offers a meaningful basis for preferring B among these choices without needing to recall this protein’s database record."
  },
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The matching UniProt entry annotates position 64 as a probable nucleophile, citing a publication, and the archived record carries the same annotation. This supports the keyed choice, though the qualifier “probable” means it is not presented as definitive experimental proof."
  },
  "important_caveats": [
    "The active-site annotation is explicitly qualified as probable.",
    "The reviewer-only source supports applicability to the supplied sequence, but that source identity and annotation were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports position 64 as the probable nucleophile. No other offered option is comparably supported as the catalytic residue; position 931 is beyond the sequence length."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matching UniProt entry annotates position 64 as a probable nucleophile, citing a publication, and the archived record carries the same annotation. This supports the keyed choice, though the qualifier “probable” means it is not presented as definitive experimental proof.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable solver could recognize the sequence as consistent with an aromatic prenyltransferase family and use transferable family knowledge that a conserved catalytic residue can participate directly in prenylation. Position 64 is a tyrosine in this sequence, making the offered probable-nucleophile assignment plausible; position 931 is outside the 373-residue sequence. This is a family-based, probabilistic inference, not proof that this exact residue has the annotated role.",
    "missing_item_specific_fact": "",
    "reason": "The family-level sequence and catalytic-residue pattern offers a meaningful basis for preferring B among these choices without needing to recall this protein’s database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports position 64 as the probable nucleophile. No other offered option is comparably supported as the catalytic residue; position 931 is beyond the sequence length."
  },
  "important_caveats": [
    "The active-site annotation is explicitly qualified as probable.",
    "The reviewer-only source supports applicability to the supplied sequence, but that source identity and annotation were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates position 64 (Glu) as 'Nucleophile (Probable)' active site (evidence ECO:0000303|PubMed:31251043, Roose & Christianson 2019, supported by X-ray crystallography PDB 6OS3/6OS5/6OS6). The sequence at position 64 is E (Glutamate), consistent with the annotation. The 'Probable' qualifier indicates structural inference rather than direct experimental proof of nucleophilic attack, but the annotation is well-supported by the primary literature.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C23](#evidence-c23), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent lines of reasoning from the original inputs and general biochemistry eliminate options A, C, and D: (1) The protein is 373 amino acids long, so position 931 (Option C) is physically impossible. (2) Position 213 is Phenylalanine (F), which has no ionizable side chain and cannot function as a proton acceptor. (3) Position 268 is Arginine (R), whose guanidinium group is positively charged and acts as a proton donor, not acceptor. Only position 64 is Glutamate (E), whose carboxylate side chain is a well-known nucleophile in enzyme catalysis. Additionally, glutamate residues are established catalytic participants in the DMATS (dimethylallyltryptophan synthase) prenyltransferase family, where they can attack DMAPP or activate the substrate nitrogen. The protein sequence itself reveals a prenyltransferase-like architecture (tryptophan-binding motifs, DMAPP-binding residues), supporting the family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate three of four options using the protein length (373 aa eliminates position 931), amino acid chemistry (Phe cannot accept a proton; Arg is a proton donor not acceptor), and the known catalytic role of glutamate in prenyltransferase families. The remaining option B (Glu64 as nucleophile) is the only chemically and structurally plausible choice without needing to recall this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option survives basic chemical and physical constraints: position 931 exceeds protein length, Phe cannot be a proton acceptor, and Arg is not a proton acceptor. Glu as a nucleophile is the sole chemically coherent answer.


### Important caveats

- The 'Probable' qualifier on the nucleophile annotation indicates structural inference from crystallography rather than direct experimental demonstration of covalent intermediate formation.
- The evidence code ECO:0000303 indicates the annotation derives from the primary literature (Roose & Christianson 2019) rather than direct mutagenesis or kinetics proving nucleophilic role.
- Position 213 (F) is near annotated L-tryptophan binding residues (211, 326) but is not itself the catalytic center.
- The protein length constraint (373 aa) making option C impossible is the strongest single discriminator available from the raw input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent lines of reasoning from the original inputs and general biochemistry eliminate options A, C, and D: (1) The protein is 373 amino acids long, so position 931 (Option C) is physically impossible. (2) Position 213 is Phenylalanine (F), which has no ionizable side chain and cannot function as a proton acceptor. (3) Position 268 is Arginine (R), whose guanidinium group is positively charged and acts as a proton donor, not acceptor. Only position 64 is Glutamate (E), whose carboxylate side chain is a well-known nucleophile in enzyme catalysis. Additionally, glutamate residues are established catalytic participants in the DMATS (dimethylallyltryptophan synthase) prenyltransferase family, where they can attack DMAPP or activate the substrate nitrogen. The protein sequence itself reveals a prenyltransferase-like architecture (tryptophan-binding motifs, DMAPP-binding residues), supporting the family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate three of four options using the protein length (373 aa eliminates position 931), amino acid chemistry (Phe cannot accept a proton; Arg is a proton donor not acceptor), and the known catalytic role of glutamate in prenyltransferase families. The remaining option B (Glu64 as nucleophile) is the only chemically and structurally plausible choice without needing to recall this specific protein's database annotation."
  },
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C23",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates position 64 (Glu) as 'Nucleophile (Probable)' active site (evidence ECO:0000303|PubMed:31251043, Roose & Christianson 2019, supported by X-ray crystallography PDB 6OS3/6OS5/6OS6). The sequence at position 64 is E (Glutamate), consistent with the annotation. The 'Probable' qualifier indicates structural inference rather than direct experimental proof of nucleophilic attack, but the annotation is well-supported by the primary literature."
  },
  "important_caveats": [
    "The 'Probable' qualifier on the nucleophile annotation indicates structural inference from crystallography rather than direct experimental demonstration of covalent intermediate formation.",
    "The evidence code ECO:0000303 indicates the annotation derives from the primary literature (Roose & Christianson 2019) rather than direct mutagenesis or kinetics proving nucleophilic role.",
    "Position 213 (F) is near annotated L-tryptophan binding residues (211, 326) but is not itself the catalytic center.",
    "The protein length constraint (373 aa) making option C impossible is the strongest single discriminator available from the raw input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option survives basic chemical and physical constraints: position 931 exceeds protein length, Phe cannot be a proton acceptor, and Arg is not a proton acceptor. Glu as a nucleophile is the sole chemically coherent answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates position 64 (Glu) as 'Nucleophile (Probable)' active site (evidence ECO:0000303|PubMed:31251043, Roose & Christianson 2019, supported by X-ray crystallography PDB 6OS3/6OS5/6OS6). The sequence at position 64 is E (Glutamate), consistent with the annotation. The 'Probable' qualifier indicates structural inference rather than direct experimental proof of nucleophilic attack, but the annotation is well-supported by the primary literature.",
    "evidence_ids": ["C5", "H6", "C23", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent lines of reasoning from the original inputs and general biochemistry eliminate options A, C, and D: (1) The protein is 373 amino acids long, so position 931 (Option C) is physically impossible. (2) Position 213 is Phenylalanine (F), which has no ionizable side chain and cannot function as a proton acceptor. (3) Position 268 is Arginine (R), whose guanidinium group is positively charged and acts as a proton donor, not acceptor. Only position 64 is Glutamate (E), whose carboxylate side chain is a well-known nucleophile in enzyme catalysis. Additionally, glutamate residues are established catalytic participants in the DMATS (dimethylallyltryptophan synthase) prenyltransferase family, where they can attack DMAPP or activate the substrate nitrogen. The protein sequence itself reveals a prenyltransferase-like architecture (tryptophan-binding motifs, DMAPP-binding residues), supporting the family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate three of four options using the protein length (373 aa eliminates position 931), amino acid chemistry (Phe cannot accept a proton; Arg is a proton donor not acceptor), and the known catalytic role of glutamate in prenyltransferase families. The remaining option B (Glu64 as nucleophile) is the only chemically and structurally plausible choice without needing to recall this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option survives basic chemical and physical constraints: position 931 exceeds protein length, Phe cannot be a proton acceptor, and Arg is not a proton acceptor. Glu as a nucleophile is the sole chemically coherent answer."
  },
  "important_caveats": [
    "The 'Probable' qualifier on the nucleophile annotation indicates structural inference from crystallography rather than direct experimental demonstration of covalent intermediate formation.",
    "The evidence code ECO:0000303 indicates the annotation derives from the primary literature (Roose & Christianson 2019) rather than direct mutagenesis or kinetics proving nucleophilic role.",
    "Position 213 (F) is near annotated L-tryptophan binding residues (211, 326) but is not itself the catalytic center.",
    "The protein length constraint (373 aa) making option C impossible is the strongest single discriminator available from the raw input."
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
  "benchmark_sequence_length": 373,
  "benchmark_sequence_sha256": "c6494f8ce6bfbaecdb19e4e2579661bdd6cbc9b83eb2bcdd2c51a5dbc1b7af98",
  "current_entry_audit": {
    "entryVersion": 69,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-12-04",
    "sequenceVersion": 1
  },
  "current_record_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 373,
  "current_source_sequence_sha256": "c6494f8ce6bfbaecdb19e4e2579661bdd6cbc9b83eb2bcdd2c51a5dbc1b7af98",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A8M6W6",
  "selected_historical_entry_version": 67,
  "selected_historical_record_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "selected_historical_source_sequence_length": 373,
  "selected_historical_source_sequence_sha256": "c6494f8ce6bfbaecdb19e4e2579661bdd6cbc9b83eb2bcdd2c51a5dbc1b7af98",
  "selected_historical_version": {
    "accession": "A8M6W6",
    "database": "Swiss-Prot",
    "entryVersion": 67,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CYMD_SALAI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A8M6W6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":69,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-12-04\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Micromonosporales\",\"Micromonosporaceae\",\"Salinispora\"],\"scientificName\":\"Salinispora arenicola (strain CNS-205)\",\"taxonId\":391037}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20055491\",\"source\":\"PubMed\"}],\"value\":\"Cyclomarin/cyclomarazine N-prenyltransferase\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18331040\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20055491\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22935004\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"18331040\",\"source\":\"PubMed\"}],\"value\":\"Tryptophan N-prenyltransferase\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22935004\",\"source\":\"PubMed\"}],\"value\":\"Dimethylallyltryptophan synthase CymD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile (Probable)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"31251043\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":64},\"start\":{\"modifier\":\"EXACT\",\"value\":64}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57912\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57912\",\"name\":\"L-tryptophan\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":55},\"start\":{\"modifier\":\"EXACT\",\"value\":55}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57912\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57912\",\"name\":\"L-tryptophan\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":56},\"start\":{\"modifier\":\"EXACT\",\"value\":56}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57912\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57912\",\"name\":\"L-tryptophan\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":64},\"start\":{\"modifier\":\"EXACT\",\"value\":64}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":77},\"start\":{\"modifier\":\"EXACT\",\"value\":77}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":146},\"start\":{\"modifier\":\"EXACT\",\"value\":146}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":148},\"start\":{\"modifier\":\"EXACT\",\"value\":148}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":205},\"start\":{\"modifier\":\"EXACT\",\"value\":205}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":207},\"start\":{\"modifier\":\"EXACT\",\"value\":207}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57912\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57912\",\"name\":\"L-tryptophan\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":211},\"start\":{\"modifier\":\"EXACT\",\"value\":211}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":274},\"start\":{\"modifier\":\"EXACT\",\"value\":274}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57912\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57912\",\"name\":\"L-tryptophan\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":326},\"start\":{\"modifier\":\"EXACT\",\"value\":326}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":337},\"start\":{\"modifier\":\"EXACT\",\"value\":337}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":339},\"start\":{\"modifier\":\"EXACT\",\"value\":339}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":341},\"start\":{\"modifier\":\"EXACT\",\"value\":341}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"citation\":{\"authors\":[\"Schultz A.W.\",\"Oh D.C.\",\"Carney J.R.\",\"Williamson R.T.\",\"Udwary D.W.\",\"Jensen P.R.\",\"Gould S.J.\",\"Fenical W.\",\"Moore B.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18331040\"},{\"database\":\"DOI\",\"id\":\"10.1021/ja711188x\"}],\"citationType\":\"journal article\",\"firstPage\":\"4507\",\"id\":\"18331040\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"4516\",\"publicationDate\":\"2008\",\"title\":\"Biosynthesis and structures of cyclomarins and cyclomarazines, prenylated cyclic peptides of marine actinobacterial origin.\",\"volume\":\"130\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"citation\":{\"authors\":[\"Schultz A.W.\",\"Lewis C.A.\",\"Luzung M.R.\",\"Baran P.S.\",\"Moore B.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20055491\"},{\"database\":\"DOI\",\"id\":\"10.1021/np9006876\"}],\"citationType\":\"journal article\",\"firstPage\":\"373\",\"id\":\"20055491\",\"journal\":\"J. Nat. Prod.\",\"lastPage\":\"377\",\"publicationDate\":\"2010\",\"title\":\"Functional characterization of the cyclomarin/cyclomarazine prenyltransferase CymD directs the biosynthesis of unnatural cyclic peptides.\",\"volume\":\"73\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"citation\":{\"authors\":[\"Qian Q.\",\"Schultz A.W.\",\"Moore B.S.\",\"Tanner M.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22935004\"},{\"database\":\"DOI\",\"id\":\"10.1021/bi3009054\"}],\"citationType\":\"journal article\",\"firstPage\":\"7733\",\"id\":\"22935004\",\"journal\":\"Biochemistry\",\"lastPage\":\"7739\",\"publicationDate\":\"2012\",\"title\":\"Mechanistic studies on CymD: a tryptophan reverse N-prenyltransferase.\",\"volume\":\"51\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"citation\":{\"authors\":[\"Roose B.W.\",\"Christianson D.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31251043\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.9b00399\"}],\"citationType\":\"journal article\",\"firstPage\":\"3232\",\"id\":\"31251043\",\"journal\":\"Biochemistry\",\"lastPage\":\"3242\",\"publicationDate\":\"2019\",\"title\":\"Structural Basis of Tryptophan Reverse N-Prenylation Catalyzed by CymD.\",\"volume\":\"58\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS3\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.33 ANGSTROMS) OF 2-373 IN APO FORM AND IN COMPLEXES WITH L-TRYPTOPHAN AND DIMETHYLALLYL S-THIOLODIPHOSPHATE\",\"FUNCTION\",\"ACTIVE SITE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H1",
  "excerpt": "ID   CYMD_SALAI              Reviewed;         373 AA.\nAC   A8M6W6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   04-DEC-2007, sequence version 1.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Dimethylallyltryptophan synthase CymD {ECO:0000303|PubMed:22935004};\nDE   AltName: Full=Cyclomarin/cyclomarazine N-prenyltransferase {ECO:0000303|PubMed:20055491};\nDE   AltName: Full=Tryptophan N-prenyltransferase {ECO:0000305|PubMed:18331040};\nDE            EC=2.5.1.- {ECO:0000269|PubMed:18331040, ECO:0000269|PubMed:20055491, ECO:0000269|PubMed:22935004};\nGN   Name=cymD {ECO:0000303|PubMed:18331040};\nGN   OrderedLocusNames=Sare_4565 {ECO:0000312|EMBL:ABW00334.1};\nOS   Salinispora arenicola (strain CNS-205).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micromonosporales;\nOC   Micromonosporaceae; Salinispora.\nOX   NCBI_TaxID=391037;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=18331040; DOI=10.1021/ja711188x;\nRA   Schultz A.W., Oh D.C., Carney J.R., Williamson R.T., Udwary D.W.,\nRA   Jensen P.R., Gould S.J., Fenical W., Moore B.S.;\nRT   \"Biosynthesis and structures of cyclomarins and cyclomarazines, prenylated\nRT   cyclic peptides of marine actinobacterial origin.\";\nRL   J. Am. Chem. Soc. 130:4507-4516(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=20055491; DOI=10.1021/np9006876;\nRA   Schultz A.W., Lewis C.A., Luzung M.R., Baran P.S., Moore B.S.;\nRT   \"Functional characterization of the cyclomarin/cyclomarazine\nRT   prenyltransferase CymD directs the biosynthesis of unnatural cyclic\nRT   peptides.\";\nRL   J. Nat. Prod. 73:373-377(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=22935004; DOI=10.1021/bi3009054;\nRA   Qian Q., Schultz A.W., Moore B.S., Tanner M.E.;\nRT   \"Mechanistic studies on CymD: a tryptophan reverse N-prenyltransferase.\";\nRL   Biochemistry 51:7733-7739(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H5",
  "excerpt": "RN   [5] {ECO:0007744|PDB:6OS3, ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6}\nRP   X-RAY CRYSTALLOGRAPHY (1.33 ANGSTROMS) OF 2-373 IN APO FORM AND IN\nRP   COMPLEXES WITH L-TRYPTOPHAN AND DIMETHYLALLYL S-THIOLODIPHOSPHATE,\nRP   FUNCTION, AND ACTIVE SITE.\nRX   PubMed=31251043; DOI=10.1021/acs.biochem.9b00399;\nRA   Roose B.W., Christianson D.W.;\nRT   \"Structural Basis of Tryptophan Reverse N-Prenylation Catalyzed by CymD.\";\nRL   Biochemistry 58:3232-3242(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H6",
  "excerpt": "FT   ACT_SITE        64\nFT                   /note=\"Nucleophile (Probable)\"\nFT                   /evidence=\"ECO:0000303|PubMed:31251043\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         55\nFT                   /ligand=\"L-tryptophan\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57912\"\nFT                   /evidence=\"ECO:0000269|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 133-137",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         56\nFT                   /ligand=\"L-tryptophan\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57912\"\nFT                   /evidence=\"ECO:0000269|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 138-142",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         64\nFT                   /ligand=\"L-tryptophan\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57912\"\nFT                   /evidence=\"ECO:0000269|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 143-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         77\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         146\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-157",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         148\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 158-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         205\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         207\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 168-172",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H15",
  "excerpt": "FT   BINDING         211\nFT                   /ligand=\"L-tryptophan\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57912\"\nFT                   /evidence=\"ECO:0000269|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 173-177",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H16",
  "excerpt": "FT   BINDING         274\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 178-182",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H17",
  "excerpt": "FT   BINDING         326\nFT                   /ligand=\"L-tryptophan\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57912\"\nFT                   /evidence=\"ECO:0000269|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 183-187",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H18",
  "excerpt": "FT   BINDING         337\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 188-192",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H19",
  "excerpt": "FT   BINDING         339\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 193-197",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H20",
  "excerpt": "FT   BINDING         341\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 198-202",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
