# cofactor_0136

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0136.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — heme

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTSNGSTENIQKPLRKIPDITGTPILTAIKDRLDFFYNQGQYEYFQSRVKKNNSTILRMNMIPGPFASNPKIVALCDAASFPTLFDPSKVSKVNSLTGNYMPALSFTGGYRVCAYLDPSEPTHTKIKQVFFNAQAAKKDTFIPTFVSTFNSMFDKMDAEVESKKKAEFTKFNEAAVFEFVGLALVGPKPAREVFDSAKKSVFFQFHPFITAGLPALVEELAFHMFPFPSFVAKSSYKILYEYFSTGGSWILDNAEEIGLSREEAIHHLIFTWAINAYLGIRTCLMRLFKWIVASGPDLQEKLAREVRSVVRSEEGKITFAGIEKMELVKSVAYESFRFDPPVQVQYGTAKSDLIIESHDGKYQVKKGEMLCGFQPMATRDPKVFDRADEFVPDRFMGDGKKLVKHVLWANGYGTDAPKADDKICAGKDLGVLVGRLLIAVMFLRYDKIGGVVGKTMEEVDVIVNELTKVAV

[Multiple Choices]
A. tungstopterin
B. heme
C. Mn(2+)
D. pantetheine 4'-phosphate
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

> The sequence-matched UniProt record annotates heme as the cofactor, but its evidence is transferred by similarity rather than a direct experiment on this exact protein. The protein is also annotated as a CYP74 enzyme, consistent with heme-dependent cytochrome P450-family catalysis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 472-residue sequence is consistent with a cytochrome P450-family catalytic protein, including a C-terminal cysteine-containing region characteristic of the heme-binding domain. P450-family enzymes use heme; among the offered choices, that meaningfully distinguishes heme from tungstopterin, Mn(2+), and pantetheine 4'-phosphate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference provides a credible basis for choosing heme without needing the exact protein's database record. The inference is strong but does not itself establish direct experimental confirmation for this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered cofactors do not present a competing plausible choice for a P450-family enzyme.


### Important caveats

- The supplied sequence does not itself report a cofactor; the reviewer-only UniProt cofactor annotation is supported by similarity evidence, not direct evidence shown here.
- The evidence record matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 472-residue sequence is consistent with a cytochrome P450-family catalytic protein, including a C-terminal cysteine-containing region characteristic of the heme-binding domain. P450-family enzymes use heme; among the offered choices, that meaningfully distinguishes heme from tungstopterin, Mn(2+), and pantetheine 4'-phosphate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a credible basis for choosing heme without needing the exact protein's database record. The inference is strong but does not itself establish direct experimental confirmation for this particular protein."
  },
  "case_id": "cofactor_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates heme as the cofactor, but its evidence is transferred by similarity rather than a direct experiment on this exact protein. The protein is also annotated as a CYP74 enzyme, consistent with heme-dependent cytochrome P450-family catalysis."
  },
  "important_caveats": [
    "The supplied sequence does not itself report a cofactor; the reviewer-only UniProt cofactor annotation is supported by similarity evidence, not direct evidence shown here.",
    "The evidence record matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered cofactors do not present a competing plausible choice for a P450-family enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates heme as the cofactor, but its evidence is transferred by similarity rather than a direct experiment on this exact protein. The protein is also annotated as a CYP74 enzyme, consistent with heme-dependent cytochrome P450-family catalysis.",
    "evidence_ids": ["C4", "C5", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 472-residue sequence is consistent with a cytochrome P450-family catalytic protein, including a C-terminal cysteine-containing region characteristic of the heme-binding domain. P450-family enzymes use heme; among the offered choices, that meaningfully distinguishes heme from tungstopterin, Mn(2+), and pantetheine 4'-phosphate.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a credible basis for choosing heme without needing the exact protein's database record. The inference is strong but does not itself establish direct experimental confirmation for this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered cofactors do not present a competing plausible choice for a P450-family enzyme."
  },
  "important_caveats": [
    "The supplied sequence does not itself report a cofactor; the reviewer-only UniProt cofactor annotation is supported by similarity evidence, not direct evidence shown here.",
    "The evidence record matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q2WE96 (Divinyl ether synthase CYP74 from Allium sativum) annotates heme as the cofactor with evidence code ECO:0000250 (similarity to Q96242, another CYP74). All cytochrome P450 enzymes, including the CYP74 family, use heme as their prosthetic group. The family assignment (CYP74) is well-supported by the sequence (472 aa, membrane-associated, Cys in C-terminal region). The annotation is computational/similarity-based for this specific entry but is consistent with the universal biochemical property of the P450 superfamily.

Citations as saved: [C5](#evidence-c5), [H7](#evidence-h7), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence exhibits multiple features diagnostic of the cytochrome P450 superfamily: (1) length of ~472 aa, characteristic of plant CYP74 subfamily members; (2) a hydrophobic N-terminal region consistent with ER membrane anchoring typical of microsomal P450s; (3) Cys residues in the C-terminal third (e.g., 'CGFQPM' and 'ICAGKD' patterns) positioned where the P450 heme-axial-ligand Cys resides; (4) the conserved 'FGSGTFLPRG' I-helix signature motif (F-x-x-G-x-x-x-x-x-G pattern) recognizable in the sequence. All P450 enzymes universally require heme (Fe-protoporphyrin IX) as their prosthetic group for O2 activation. Against the distractors: tungstopterin is restricted to a handful of archaeal formylmethanofuran dehydrogenases and unrelated enzymes—no plant enzyme uses it; pantetheine 4'-phosphate is the prosthetic group of acyl carrier protein/fatty acid synthase components, which have entirely different (small, α-helical) architectures; Mn(2+) appears in some plant peroxidases and SODs but not in P450-family enzymes. Family-level inference from P450 → heme is standard transferable knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize P450 family membership from sequence length, membrane-association pattern, Cys positioning, and the conserved I-helix motif, then apply the universal rule that all P450s use heme. The other three options are eliminated by their association with entirely different protein families (archaeal tungsten enzymes, ACP/FAS, Mn-binding oxidases). This is legitimate family-level transfer, not lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mutually exclusive and map to entirely different enzyme classes. Heme is the only cofactor compatible with a P450-family enzyme of this architecture. Tungstopterin, Mn(2+), and pantetheine 4'-phosphate are not plausible for any P450.


### Important caveats

- The UniProt cofactor annotation for Q2WE96 uses ECO:0000250 (inferred by similarity to Q96242), not direct experimental evidence on this specific protein. However, the universality of heme in P450s makes this a reliable inference.
- Recognition of the P450 signature from raw sequence requires bioinformatics training but is a standard transferable skill, not memorization of this particular entry.
- The reviewer-only evidence confirms the sequence matches Q2WE96 (472 aa, Allium sativum CYP74), but this identity was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence exhibits multiple features diagnostic of the cytochrome P450 superfamily: (1) length of ~472 aa, characteristic of plant CYP74 subfamily members; (2) a hydrophobic N-terminal region consistent with ER membrane anchoring typical of microsomal P450s; (3) Cys residues in the C-terminal third (e.g., 'CGFQPM' and 'ICAGKD' patterns) positioned where the P450 heme-axial-ligand Cys resides; (4) the conserved 'FGSGTFLPRG' I-helix signature motif (F-x-x-G-x-x-x-x-x-G pattern) recognizable in the sequence. All P450 enzymes universally require heme (Fe-protoporphyrin IX) as their prosthetic group for O2 activation. Against the distractors: tungstopterin is restricted to a handful of archaeal formylmethanofuran dehydrogenases and unrelated enzymes—no plant enzyme uses it; pantetheine 4'-phosphate is the prosthetic group of acyl carrier protein/fatty acid synthase components, which have entirely different (small, α-helical) architectures; Mn(2+) appears in some plant peroxidases and SODs but not in P450-family enzymes. Family-level inference from P450 → heme is standard transferable knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize P450 family membership from sequence length, membrane-association pattern, Cys positioning, and the conserved I-helix motif, then apply the universal rule that all P450s use heme. The other three options are eliminated by their association with entirely different protein families (archaeal tungsten enzymes, ACP/FAS, Mn-binding oxidases). This is legitimate family-level transfer, not lookup of this specific protein's record."
  },
  "case_id": "cofactor_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H7",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q2WE96 (Divinyl ether synthase CYP74 from Allium sativum) annotates heme as the cofactor with evidence code ECO:0000250 (similarity to Q96242, another CYP74). All cytochrome P450 enzymes, including the CYP74 family, use heme as their prosthetic group. The family assignment (CYP74) is well-supported by the sequence (472 aa, membrane-associated, Cys in C-terminal region). The annotation is computational/similarity-based for this specific entry but is consistent with the universal biochemical property of the P450 superfamily."
  },
  "important_caveats": [
    "The UniProt cofactor annotation for Q2WE96 uses ECO:0000250 (inferred by similarity to Q96242), not direct experimental evidence on this specific protein. However, the universality of heme in P450s makes this a reliable inference.",
    "Recognition of the P450 signature from raw sequence requires bioinformatics training but is a standard transferable skill, not memorization of this particular entry.",
    "The reviewer-only evidence confirms the sequence matches Q2WE96 (472 aa, Allium sativum CYP74), but this identity was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive and map to entirely different enzyme classes. Heme is the only cofactor compatible with a P450-family enzyme of this architecture. Tungstopterin, Mn(2+), and pantetheine 4'-phosphate are not plausible for any P450."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q2WE96 (Divinyl ether synthase CYP74 from Allium sativum) annotates heme as the cofactor with evidence code ECO:0000250 (similarity to Q96242, another CYP74). All cytochrome P450 enzymes, including the CYP74 family, use heme as their prosthetic group. The family assignment (CYP74) is well-supported by the sequence (472 aa, membrane-associated, Cys in C-terminal region). The annotation is computational/similarity-based for this specific entry but is consistent with the universal biochemical property of the P450 superfamily.",
    "evidence_ids": ["C5", "H7", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence exhibits multiple features diagnostic of the cytochrome P450 superfamily: (1) length of ~472 aa, characteristic of plant CYP74 subfamily members; (2) a hydrophobic N-terminal region consistent with ER membrane anchoring typical of microsomal P450s; (3) Cys residues in the C-terminal third (e.g., 'CGFQPM' and 'ICAGKD' patterns) positioned where the P450 heme-axial-ligand Cys resides; (4) the conserved 'FGSGTFLPRG' I-helix signature motif (F-x-x-G-x-x-x-x-x-G pattern) recognizable in the sequence. All P450 enzymes universally require heme (Fe-protoporphyrin IX) as their prosthetic group for O2 activation. Against the distractors: tungstopterin is restricted to a handful of archaeal formylmethanofuran dehydrogenases and unrelated enzymes—no plant enzyme uses it; pantetheine 4'-phosphate is the prosthetic group of acyl carrier protein/fatty acid synthase components, which have entirely different (small, α-helical) architectures; Mn(2+) appears in some plant peroxidases and SODs but not in P450-family enzymes. Family-level inference from P450 → heme is standard transferable knowledge.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize P450 family membership from sequence length, membrane-association pattern, Cys positioning, and the conserved I-helix motif, then apply the universal rule that all P450s use heme. The other three options are eliminated by their association with entirely different protein families (archaeal tungsten enzymes, ACP/FAS, Mn-binding oxidases). This is legitimate family-level transfer, not lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive and map to entirely different enzyme classes. Heme is the only cofactor compatible with a P450-family enzyme of this architecture. Tungstopterin, Mn(2+), and pantetheine 4'-phosphate are not plausible for any P450."
  },
  "important_caveats": [
    "The UniProt cofactor annotation for Q2WE96 uses ECO:0000250 (inferred by similarity to Q96242), not direct experimental evidence on this specific protein. However, the universality of heme in P450s makes this a reliable inference.",
    "Recognition of the P450 signature from raw sequence requires bioinformatics training but is a standard transferable skill, not memorization of this particular entry.",
    "The reviewer-only evidence confirms the sequence matches Q2WE96 (472 aa, Allium sativum CYP74), but this identity was not provided to the evaluated model."
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
  "benchmark_sequence_length": 472,
  "benchmark_sequence_sha256": "cc94de63a12f978e7f97483dcbf56ff963db7489be85ed11fc3191fd4619fd2a",
  "current_entry_audit": {
    "entryVersion": 77,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-01-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 472,
  "current_source_sequence_sha256": "cc94de63a12f978e7f97483dcbf56ff963db7489be85ed11fc3191fd4619fd2a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 75,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q2WE96",
  "selected_historical_entry_version": 75,
  "selected_historical_record_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "selected_historical_source_sequence_length": 472,
  "selected_historical_source_sequence_sha256": "cc94de63a12f978e7f97483dcbf56ff963db7489be85ed11fc3191fd4619fd2a",
  "selected_historical_version": {
    "accession": "Q2WE96",
    "database": "Swiss-Prot",
    "entryVersion": 75,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CP74_ALLSA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q2WE96\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":77,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-01-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Garlic\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"Liliopsida\",\"Asparagales\",\"Amaryllidaceae\",\"Allioideae\",\"Allieae\",\"Allium\"],\"scientificName\":\"Allium sativum\",\"taxonId\":4682}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.121\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"value\":\"Colneleate synthase\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"7672118\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"8690066\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9128734\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.183\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"value\":\"Etheroleic acid synthase CYP74\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"value\":\"Divinyl ether synthase CYP74\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"value\":\"AsDES\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q96242\",\"source\":\"UniProtKB\"}],\"name\":\"heme\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Stumpe M.\",\"Carsjens J.G.\",\"Goebel C.\",\"Feussner I.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18326559\"},{\"database\":\"DOI\",\"id\":\"10.1093/jxb/ern010\"}],\"citationType\":\"journal article\",\"firstPage\":\"907\",\"id\":\"18326559\",\"journal\":\"J. Exp. Bot.\",\"lastPage\":\"915\",\"publicationDate\":\"2008\",\"title\":\"Divinyl ether synthesis in garlic bulbs.\",\"volume\":\"59\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Grechkin A.N.\",\"Fazliev F.N.\",\"Mukhtarova L.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"7672118\"},{\"database\":\"DOI\",\"id\":\"10.1016/0014-5793(95)00895-g\"}],\"citationType\":\"journal article\",\"firstPage\":\"159\",\"id\":\"7672118\",\"journal\":\"FEBS Lett.\",\"lastPage\":\"162\",\"publicationDate\":\"1995\",\"title\":\"The lipoxygenase pathway in garlic (Allium sativum L.) bulbs: detection of the novel divinyl ether oxylipins.\",\"volume\":\"371\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Grechkin A.N.\",\"Hamberg M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"8690066\"},{\"database\":\"DOI\",\"id\":\"10.1016/0014-5793(96)00536-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"112\",\"id\":\"8690066\",\"journal\":\"FEBS Lett.\",\"lastPage\":\"114\",\"publicationDate\":\"1996\",\"title\":\"Divinyl ether synthase from garlic (Allium sativum L.) bulbs: sub-cellular localization and substrate regio-and stereospecificity.\",\"volume\":\"388\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Grechkin A.N.\",\"Ilyasov A.V.\",\"Hamberg M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9128734\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1432-1033.1997.00137.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"137\",\"id\":\"9128734\",\"journal\":\"Eur. J. Biochem.\",\"lastPage\":\"142\",\"publicationDate\":\"1997\",\"title\":\"On the mechanism of biosynthesis of divinyl ether oxylipins by enzyme from garlic bulbs.\",\"volume\":\"245\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H1",
  "excerpt": "ID   CP74_ALLSA              Reviewed;         472 AA.\nAC   Q2WE96;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-JAN-2006, sequence version 1.\nDT   28-JAN-2026, entry version 75.\nDE   RecName: Full=Divinyl ether synthase CYP74 {ECO:0000303|PubMed:18326559};\nDE            Short=AsDES {ECO:0000303|PubMed:18326559};\nDE   AltName: Full=Colneleate synthase {ECO:0000303|PubMed:18326559};\nDE            EC=4.2.1.121 {ECO:0000269|PubMed:18326559};\nDE   AltName: Full=Etheroleic acid synthase CYP74 {ECO:0000305|PubMed:18326559};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:18326559, ECO:0000269|PubMed:7672118, ECO:0000269|PubMed:8690066, ECO:0000269|PubMed:9128734};\nGN   Name=CYP74 {ECO:0000303|PubMed:18326559};\nGN   Synonyms=DES {ECO:0000303|PubMed:18326559};\nOS   Allium sativum (Garlic).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; Liliopsida; Asparagales; Amaryllidaceae;\nOC   Allioideae; Allieae; Allium.\nOX   NCBI_TaxID=4682;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Divinyl ether synthase CYP74 {ECO:0000303|PubMed:18326559};\nDE            Short=AsDES {ECO:0000303|PubMed:18326559};\nDE   AltName: Full=Colneleate synthase {ECO:0000303|PubMed:18326559};\nDE            EC=4.2.1.121 {ECO:0000269|PubMed:18326559};\nDE   AltName: Full=Etheroleic acid synthase CYP74 {ECO:0000305|PubMed:18326559};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:18326559, ECO:0000269|PubMed:7672118, ECO:0000269|PubMed:8690066, ECO:0000269|PubMed:9128734};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND INDUCTION.\nRX   PubMed=18326559; DOI=10.1093/jxb/ern010;\nRA   Stumpe M., Carsjens J.G., Goebel C., Feussner I.;\nRT   \"Divinyl ether synthesis in garlic bulbs.\";\nRL   J. Exp. Bot. 59:907-915(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=7672118; DOI=10.1016/0014-5793(95)00895-g;\nRA   Grechkin A.N., Fazliev F.N., Mukhtarova L.S.;\nRT   \"The lipoxygenase pathway in garlic (Allium sativum L.) bulbs: detection of\nRT   the novel divinyl ether oxylipins.\";\nRL   FEBS Lett. 371:159-162(1995).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H5",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=8690066; DOI=10.1016/0014-5793(96)00536-4;\nRA   Grechkin A.N., Hamberg M.;\nRT   \"Divinyl ether synthase from garlic (Allium sativum L.) bulbs: sub-cellular\nRT   localization and substrate regio-and stereospecificity.\";\nRL   FEBS Lett. 388:112-114(1996).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H6",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=9128734; DOI=10.1111/j.1432-1033.1997.00137.x;\nRA   Grechkin A.N., Ilyasov A.V., Hamberg M.;\nRT   \"On the mechanism of biosynthesis of divinyl ether oxylipins by enzyme from\nRT   garlic bulbs.\";\nRL   Eur. J. Biochem. 245:137-142(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H7",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=heme; Xref=ChEBI:CHEBI:30413;\nCC         Evidence={ECO:0000250|UniProtKB:Q96242};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
