# cofactor_0138

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0138.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — heme

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQTVTLSIFRFNEFEKRLWVLGQMTANKLGMHYLPKAKFWKMFGSGTGQGFTPKPNWHVWSILAVWPDEETARREVAESPIYQRWTKMADESYTVLLQPTSAWGKWDGKEPFEPVKPASDVRPIAALTRATVKFWKAERFWAREPAISHMIGRNKDVVFKIGVGEVPFVQQVTFSIWPDARSMEEFARGAGGPHGEAIKAVRAENWFKEELYARFQILGTIGKWEGKDPVGEALTARPSEAPKPAPAPAAAQPAPAAEAPKPAPAPVAEKPALAVEMPKPAEPPKPVVEAPKPASAPVASKPMPQGGKPNFKGKPGKGGRKENA

[Multiple Choices]
A. heme
B. Fe cation
C. tungstopterin
D. pyridoxal 5'-phosphate
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

> A historical UniProt entry matching the supplied sequence annotates heme as the cofactor, with experimental evidence and a note that each subunit binds one heme.

Citations as saved: [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A credible sequence-family inference is that this is a bacterial carotenoid-modifying monooxygenase; family-level knowledge of such oxygenases makes heme a plausible cofactor. That favors A over PLP or tungstopterin, and distinguishes heme from a non-heme iron cation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence can support a transferable family-level inference that meaningfully favors heme among these choices, though sequence-only prediction is less conclusive than direct cofactor evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence specifies heme; although heme contains iron, the choices distinguish heme from a non-heme Fe cation.


### Important caveats

- The family-level inference is probabilistic; the experimental cofactor annotation is reviewer-only evidence, not an input to the original question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A credible sequence-family inference is that this is a bacterial carotenoid-modifying monooxygenase; family-level knowledge of such oxygenases makes heme a plausible cofactor. That favors A over PLP or tungstopterin, and distinguishes heme from a non-heme iron cation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence can support a transferable family-level inference that meaningfully favors heme among these choices, though sequence-only prediction is less conclusive than direct cofactor evidence."
  },
  "case_id": "cofactor_0138",
  "expected_answer_check": {
    "evidence_ids": [
      "H5"
    ],
    "judgment": "supported",
    "reason": "A historical UniProt entry matching the supplied sequence annotates heme as the cofactor, with experimental evidence and a note that each subunit binds one heme."
  },
  "important_caveats": [
    "The family-level inference is probabilistic; the experimental cofactor annotation is reviewer-only evidence, not an input to the original question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence specifies heme; although heme contains iron, the choices distinguish heme from a non-heme Fe cation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0138",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "A historical UniProt entry matching the supplied sequence annotates heme as the cofactor, with experimental evidence and a note that each subunit binds one heme.",
    "evidence_ids": ["H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A credible sequence-family inference is that this is a bacterial carotenoid-modifying monooxygenase; family-level knowledge of such oxygenases makes heme a plausible cofactor. That favors A over PLP or tungstopterin, and distinguishes heme from a non-heme iron cation.",
    "missing_item_specific_fact": "",
    "reason": "The sequence can support a transferable family-level inference that meaningfully favors heme among these choices, though sequence-only prediction is less conclusive than direct cofactor evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence specifies heme; although heme contains iron, the choices distinguish heme from a non-heme Fe cation."
  },
  "important_caveats": [
    "The family-level inference is probabilistic; the experimental cofactor annotation is reviewer-only evidence, not an input to the original question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q3J189 (Spheroidene monooxygenase, CrtA, EC 1.14.15.9) annotates heme as the cofactor with experimental evidence (ECO:0000269, PubMed:20851979), stating 'Binds 1 heme per subunit.' The benchmark sequence matches the source sequence (SHA-256 confirmed). The author's expected answer of heme (A) is directly supported by experimental data.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains features consistent with a carotenoid-modifying monooxygenase: glycine-rich loops ('GSGTGQGFTPKPNWHVWSILAVWPDEE') and conserved histidine residues ('HPGEAIKAVRAENWFKEELYARFQILGTIGKWEGKDP') that are hallmarks of heme-coordinating sites in the CrtA/spheroidene monooxygenase family. Transferable family-level knowledge from well-characterized CrtA homologs (e.g., from Rhodobacter capsulatus, Pantoea agglomerans, Xanthobacter autotrophicus) establishes that spheroidene/carotenoid monooxygenases require heme (iron protoporphyrin IX) as a prosthetic group for oxygen-activation chemistry, not a free Fe²⁺/Fe³⁺ ion. Tungstopterin (C) is restricted to anaerobic oxidoreductases (e.g., aldehyde oxidoreductases, formate dehydrogenases) and is implausible for an aerobic carotenoid pathway enzyme. Pyridoxal 5'-phosphate (D) is specific to amino-acid metabolism (transaminases, decarboxylases) and is irrelevant to carotenoid oxidation. The heme-vs-Fe-cation distinction is addressable because monooxygenase catalysis requires the porphyrin scaffold to position and activate O₂; a bare Fe ion cannot perform this chemistry. The glycine-rich motif and histidine spacing in the sequence are consistent with the heme-binding architecture seen across the CrtA family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C and D by recognizing the enzyme class (carotenoid monooxygenase) from sequence features and pathway context, then distinguish heme from free Fe cation using family-level knowledge of CrtA proteins and the mechanistic requirement for a porphyrin-based cofactor in monooxygenase chemistry. The sequence's histidine-containing motifs and glycine-rich loops provide additional sequence-level support for heme coordination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (tungstopterin) and D (PLP) are clearly incompatible with a carotenoid monooxygenase. Option B (Fe cation) is mechanistically insufficient for monooxygenase O₂ activation and is inconsistent with the heme-binding histidine residues and glycine-rich motifs present in the sequence. Only option A (heme) is defensible.


### Important caveats

- The heme annotation is experimentally supported (PubMed:20851979), not merely inferred by homology.
- The EC number assignment (1.14.15.9) carries evidence code ECO:0000250 (similarity to P17055), but the cofactor annotation itself is experimental (ECO:0000269).
- Recognizing the protein as CrtA from the sequence alone requires familiarity with the carotenoid biosynthesis pathway; however, this is transferable family-level knowledge, not a lookup of this exact protein's record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features consistent with a carotenoid-modifying monooxygenase: glycine-rich loops ('GSGTGQGFTPKPNWHVWSILAVWPDEE') and conserved histidine residues ('HPGEAIKAVRAENWFKEELYARFQILGTIGKWEGKDP') that are hallmarks of heme-coordinating sites in the CrtA/spheroidene monooxygenase family. Transferable family-level knowledge from well-characterized CrtA homologs (e.g., from Rhodobacter capsulatus, Pantoea agglomerans, Xanthobacter autotrophicus) establishes that spheroidene/carotenoid monooxygenases require heme (iron protoporphyrin IX) as a prosthetic group for oxygen-activation chemistry, not a free Fe²⁺/Fe³⁺ ion. Tungstopterin (C) is restricted to anaerobic oxidoreductases (e.g., aldehyde oxidoreductases, formate dehydrogenases) and is implausible for an aerobic carotenoid pathway enzyme. Pyridoxal 5'-phosphate (D) is specific to amino-acid metabolism (transaminases, decarboxylases) and is irrelevant to carotenoid oxidation. The heme-vs-Fe-cation distinction is addressable because monooxygenase catalysis requires the porphyrin scaffold to position and activate O₂; a bare Fe ion cannot perform this chemistry. The glycine-rich motif and histidine spacing in the sequence are consistent with the heme-binding architecture seen across the CrtA family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D by recognizing the enzyme class (carotenoid monooxygenase) from sequence features and pathway context, then distinguish heme from free Fe cation using family-level knowledge of CrtA proteins and the mechanistic requirement for a porphyrin-based cofactor in monooxygenase chemistry. The sequence's histidine-containing motifs and glycine-rich loops provide additional sequence-level support for heme coordination."
  },
  "case_id": "cofactor_0138",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q3J189 (Spheroidene monooxygenase, CrtA, EC 1.14.15.9) annotates heme as the cofactor with experimental evidence (ECO:0000269, PubMed:20851979), stating 'Binds 1 heme per subunit.' The benchmark sequence matches the source sequence (SHA-256 confirmed). The author's expected answer of heme (A) is directly supported by experimental data."
  },
  "important_caveats": [
    "The heme annotation is experimentally supported (PubMed:20851979), not merely inferred by homology.",
    "The EC number assignment (1.14.15.9) carries evidence code ECO:0000250 (similarity to P17055), but the cofactor annotation itself is experimental (ECO:0000269).",
    "Recognizing the protein as CrtA from the sequence alone requires familiarity with the carotenoid biosynthesis pathway; however, this is transferable family-level knowledge, not a lookup of this exact protein's record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (tungstopterin) and D (PLP) are clearly incompatible with a carotenoid monooxygenase. Option B (Fe cation) is mechanistically insufficient for monooxygenase O₂ activation and is inconsistent with the heme-binding histidine residues and glycine-rich motifs present in the sequence. Only option A (heme) is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0138",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q3J189 (Spheroidene monooxygenase, CrtA, EC 1.14.15.9) annotates heme as the cofactor with experimental evidence (ECO:0000269, PubMed:20851979), stating 'Binds 1 heme per subunit.' The benchmark sequence matches the source sequence (SHA-256 confirmed). The author's expected answer of heme (A) is directly supported by experimental data.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains features consistent with a carotenoid-modifying monooxygenase: glycine-rich loops ('GSGTGQGFTPKPNWHVWSILAVWPDEE') and conserved histidine residues ('HPGEAIKAVRAENWFKEELYARFQILGTIGKWEGKDP') that are hallmarks of heme-coordinating sites in the CrtA/spheroidene monooxygenase family. Transferable family-level knowledge from well-characterized CrtA homologs (e.g., from Rhodobacter capsulatus, Pantoea agglomerans, Xanthobacter autotrophicus) establishes that spheroidene/carotenoid monooxygenases require heme (iron protoporphyrin IX) as a prosthetic group for oxygen-activation chemistry, not a free Fe²⁺/Fe³⁺ ion. Tungstopterin (C) is restricted to anaerobic oxidoreductases (e.g., aldehyde oxidoreductases, formate dehydrogenases) and is implausible for an aerobic carotenoid pathway enzyme. Pyridoxal 5'-phosphate (D) is specific to amino-acid metabolism (transaminases, decarboxylases) and is irrelevant to carotenoid oxidation. The heme-vs-Fe-cation distinction is addressable because monooxygenase catalysis requires the porphyrin scaffold to position and activate O₂; a bare Fe ion cannot perform this chemistry. The glycine-rich motif and histidine spacing in the sequence are consistent with the heme-binding architecture seen across the CrtA family.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D by recognizing the enzyme class (carotenoid monooxygenase) from sequence features and pathway context, then distinguish heme from free Fe cation using family-level knowledge of CrtA proteins and the mechanistic requirement for a porphyrin-based cofactor in monooxygenase chemistry. The sequence's histidine-containing motifs and glycine-rich loops provide additional sequence-level support for heme coordination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (tungstopterin) and D (PLP) are clearly incompatible with a carotenoid monooxygenase. Option B (Fe cation) is mechanistically insufficient for monooxygenase O₂ activation and is inconsistent with the heme-binding histidine residues and glycine-rich motifs present in the sequence. Only option A (heme) is defensible."
  },
  "important_caveats": [
    "The heme annotation is experimentally supported (PubMed:20851979), not merely inferred by homology.",
    "The EC number assignment (1.14.15.9) carries evidence code ECO:0000250 (similarity to P17055), but the cofactor annotation itself is experimental (ECO:0000269).",
    "Recognizing the protein as CrtA from the sequence alone requires familiarity with the carotenoid biosynthesis pathway; however, this is transferable family-level knowledge, not a lookup of this exact protein's record."
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
  "benchmark_sequence_length": 324,
  "benchmark_sequence_sha256": "729a48d70d6bbe461cee74d78aec69eadd0836a65bfc944cb3241dac87281b34",
  "current_entry_audit": {
    "entryVersion": 76,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-11-08",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 324,
  "current_source_sequence_sha256": "729a48d70d6bbe461cee74d78aec69eadd0836a65bfc944cb3241dac87281b34",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 74,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q3J189",
  "selected_historical_entry_version": 74,
  "selected_historical_record_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "selected_historical_source_sequence_length": 324,
  "selected_historical_source_sequence_sha256": "729a48d70d6bbe461cee74d78aec69eadd0836a65bfc944cb3241dac87281b34",
  "selected_historical_version": {
    "accession": "Q3J189",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRTA_CERS4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q3J189\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":76,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-11-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rhodobacter sphaeroides\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Alphaproteobacteria\",\"Rhodobacterales\",\"Paracoccaceae\",\"Cereibacter\"],\"scientificName\":\"Cereibacter sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 / NBRC 12203 / NCIMB 8253 / ATH 2.4.1.)\",\"taxonId\":272943}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"value\":\"1.14.15.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20851979\",\"source\":\"PubMed\"}],\"value\":\"Spheroidene monooxygenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20851979\",\"source\":\"PubMed\"}],\"name\":\"heme\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20851979\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 heme per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lee P.C.\",\"Holtzapple E.\",\"Schmidt-Dannert C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20851979\"},{\"database\":\"DOI\",\"id\":\"10.1128/aem.01606-10\"}],\"citationType\":\"journal article\",\"firstPage\":\"7328\",\"id\":\"20851979\",\"journal\":\"Appl. Environ. Microbiol.\",\"lastPage\":\"7331\",\"publicationDate\":\"2010\",\"title\":\"Novel activity of Rhodobacter sphaeroides spheroidene monooxygenase CrtA expressed in Escherichia coli.\",\"volume\":\"76\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H1",
  "excerpt": "ID   CRTA_CERS4              Reviewed;         324 AA.\nAC   Q3J189; Q54790;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-NOV-2005, sequence version 1.\nDT   28-JAN-2026, entry version 74.\nDE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:20851979};\nDE            EC=1.14.15.9 {ECO:0000250|UniProtKB:P17055};\nGN   Name=crtA {ECO:0000303|PubMed:7721699};\nGN   OrderedLocusNames=RHOS4_18770 {ECO:0000305};\nGN   ORFNames=RSP_0272 {ECO:0000312|EMBL:ABA79445.1};\nOS   Cereibacter sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG\nOS   31486 / LMG 2827 / NBRC 12203 / NCIMB 8253 / ATH 2.4.1.) (Rhodobacter\nOS   sphaeroides).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;\nOC   Rhodobacterales; Paracoccaceae; Cereibacter.\nOX   NCBI_TaxID=272943;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:20851979};\nDE            EC=1.14.15.9 {ECO:0000250|UniProtKB:P17055};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAB38738.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 / NBRC 12203\nRC   / NCIMB 8253 / ATH 2.4.1.;\nRX   PubMed=7721699; DOI=10.1128/jb.177.8.2064-2073.1995;\nRA   Lang H.P., Cogdell R.J., Takaichi S., Hunter C.N.;\nRT   \"Complete DNA sequence, specific Tn5 insertion map, and gene assignment of\nRT   the carotenoid biosynthesis pathway of Rhodobacter sphaeroides.\";\nRL   J. Bacteriol. 177:2064-2073(1995).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, COFACTOR, SUBSTRATE SPECIFICITY, AND BIOTECHNOLOGY.\nRX   PubMed=20851979; DOI=10.1128/aem.01606-10;\nRA   Lee P.C., Holtzapple E., Schmidt-Dannert C.;\nRT   \"Novel activity of Rhodobacter sphaeroides spheroidene monooxygenase CrtA\nRT   expressed in Escherichia coli.\";\nRL   Appl. Environ. Microbiol. 76:7328-7331(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=heme; Xref=ChEBI:CHEBI:30413;\nCC         Evidence={ECO:0000269|PubMed:20851979};\nCC       Note=Binds 1 heme per subunit. {ECO:0000269|PubMed:20851979};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 138. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
