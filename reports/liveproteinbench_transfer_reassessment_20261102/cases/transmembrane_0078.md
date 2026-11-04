# transmembrane_0078

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0078.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 3..23

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDKISIIPIVGVALSLAIILQLGRTYWRLRHIPGPFPACITNFQRVGWVKTKRAHLILQDMHKKYGEVVRIGPNMVSFSNPEVIPTVYPARSGFPKGDFYVTLRPYTRGGGALHAVFNTTEEDLHKQIKSPIAPMFTPANTPSFEGLVDEVLTCIHEKLDENFIANSEIFNLGQWLQYFAFDVMGTMTFSKRYGFLDTGKDVGRMLGTIVDFMRDAAPMTQIPWLDWALRKNRIGDSIQRLFGKTASLGILGFVGKAIKERQELLSKGDFKVSDEKSGRKDFLTRFIELQQNDPKIPPWAPTAWTFSNVIAGSDSVGSLMRTTMFNLLVYPHTLEKLHDELRSAGVSRPYPKWSEIRNLLYLDACVQEGARMHPPFALPFERVVPAGGITILGYYLPGGTVVGGSPYVVNRHRETFGRDAEFWRPERWLESDEGHKRKLEQGVLTFGAGRRVCLGKHVGILEIKKLISFLVLNYDIRVVNPEKFELENSWFFFQRGLYATIRKRPDAVAVKNQQV

[Multiple Choices]
A. 3..23; 635..655
B. 5..27
C. 3..18
D. 3..23
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates a helical transmembrane region at 3..23. This is computational annotation (ECO:0000255), not direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Residues 3..23 form a long, strongly hydrophobic stretch, consistent with a membrane-spanning alpha helix. This favors D over C, which truncates the stretch, and B, which extends into the more polar and charged sequence after it. A also includes coordinates beyond this 515-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself contains a recognizable hydrophobic transmembrane segment, so transferable knowledge of membrane-spanning helices meaningfully distinguishes the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, 3..23 best captures the hydrophobic segment; the alternatives either truncate it, extend it into non-hydrophobic residues, or include out-of-range coordinates.


### Important caveats

- The supporting database feature is computationally annotated; the supplied evidence does not establish experimental confirmation of membrane insertion or exact boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Residues 3..23 form a long, strongly hydrophobic stretch, consistent with a membrane-spanning alpha helix. This favors D over C, which truncates the stretch, and B, which extends into the more polar and charged sequence after it. A also includes coordinates beyond this 515-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself contains a recognizable hydrophobic transmembrane segment, so transferable knowledge of membrane-spanning helices meaningfully distinguishes the offered choices."
  },
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a helical transmembrane region at 3..23. This is computational annotation (ECO:0000255), not direct experimental evidence."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated; the supplied evidence does not establish experimental confirmation of membrane insertion or exact boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, 3..23 best captures the hydrophobic segment; the alternatives either truncate it, extend it into non-hydrophobic residues, or include out-of-range coordinates."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a helical transmembrane region at 3..23. This is computational annotation (ECO:0000255), not direct experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Residues 3..23 form a long, strongly hydrophobic stretch, consistent with a membrane-spanning alpha helix. This favors D over C, which truncates the stretch, and B, which extends into the more polar and charged sequence after it. A also includes coordinates beyond this 515-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself contains a recognizable hydrophobic transmembrane segment, so transferable knowledge of membrane-spanning helices meaningfully distinguishes the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, 3..23 best captures the hydrophobic segment; the alternatives either truncate it, extend it into non-hydrophobic residues, or include out-of-range coordinates."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated; the supplied evidence does not establish experimental confirmation of membrane insertion or exact boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence code ECO:0000255, inferred by similarity) records a transmembrane helix at positions 3..23. The segment KISIIPIVGVALSLAIILQLG (21 residues) is predominantly hydrophobic with boundary residues (K at 3, G at 23), consistent with a TM alpha-helix of appropriate length. The annotation is computational/inferred rather than experimentally verified, but it directly supports the expected answer.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable principles distinguish D from the other choices. (1) Option A is trivially eliminated because positions 635-655 exceed the 515-residue protein length. (2) A TM alpha-helix requires approximately 19-21 residues to span the ~30 Å hydrophobic core of the lipid bilayer; option C (3..18) provides only 16 residues, which is below the minimum helix length for membrane crossing. (3) Option B (5..27) extends into positions 24-27 (R, T, Y, W), which include a charged Arg and aromatic Trp/Tyr residues that are characteristic of the membrane-water interface, not the hydrophobic core. (4) Option D (3..23) yields a 21-residue segment that is predominantly hydrophobic (I, I, I, P, I, V, V, A, L, L, A, I, I, L, L) with boundary residues (K, S, Q, G) at the edges, matching the expected length and composition of a TM helix. This reasoning relies on general TM helix biophysics learned from many membrane proteins, not on memorizing this specific entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The discrimination among options relies on well-established general principles: TM helix length (~19-21 residues), hydrophobic composition, boundary residue patterns (charged/aromatic at interfaces), and simple arithmetic (option A exceeds protein length). No fact specific to this exact protein beyond reading the sequence is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is eliminated by length; option C is too short for a TM helix; option B includes clearly non-TM residues (Arg, Tyr, Trp). Only D satisfies both the length requirement and the hydrophobic composition criterion for a TM alpha-helix.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational rather than experimentally determined.
- The segment 3-23 is not a 'textbook' pure-hydrophobic TM helix; it contains several polar residues (K, S, S, Q, G), which is common in real TM helices but makes purely hydrophobicity-based prediction less crisp.
- The protein is a fungal cytochrome P450 monooxygenase (mfmA from Annulohypoxylon moriforme), a family in which N-terminal TM anchoring to the ER membrane is a well-known feature, further supporting the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable principles distinguish D from the other choices. (1) Option A is trivially eliminated because positions 635-655 exceed the 515-residue protein length. (2) A TM alpha-helix requires approximately 19-21 residues to span the ~30 Å hydrophobic core of the lipid bilayer; option C (3..18) provides only 16 residues, which is below the minimum helix length for membrane crossing. (3) Option B (5..27) extends into positions 24-27 (R, T, Y, W), which include a charged Arg and aromatic Trp/Tyr residues that are characteristic of the membrane-water interface, not the hydrophobic core. (4) Option D (3..23) yields a 21-residue segment that is predominantly hydrophobic (I, I, I, P, I, V, V, A, L, L, A, I, I, L, L) with boundary residues (K, S, Q, G) at the edges, matching the expected length and composition of a TM helix. This reasoning relies on general TM helix biophysics learned from many membrane proteins, not on memorizing this specific entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The discrimination among options relies on well-established general principles: TM helix length (~19-21 residues), hydrophobic composition, boundary residue patterns (charged/aromatic at interfaces), and simple arithmetic (option A exceeds protein length). No fact specific to this exact protein beyond reading the sequence is needed."
  },
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, inferred by similarity) records a transmembrane helix at positions 3..23. The segment KISIIPIVGVALSLAIILQLG (21 residues) is predominantly hydrophobic with boundary residues (K at 3, G at 23), consistent with a TM alpha-helix of appropriate length. The annotation is computational/inferred rather than experimentally verified, but it directly supports the expected answer."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational rather than experimentally determined.",
    "The segment 3-23 is not a 'textbook' pure-hydrophobic TM helix; it contains several polar residues (K, S, S, Q, G), which is common in real TM helices but makes purely hydrophobicity-based prediction less crisp.",
    "The protein is a fungal cytochrome P450 monooxygenase (mfmA from Annulohypoxylon moriforme), a family in which N-terminal TM anchoring to the ER membrane is a well-known feature, further supporting the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by length; option C is too short for a TM helix; option B includes clearly non-TM residues (Arg, Tyr, Trp). Only D satisfies both the length requirement and the hydrophobic composition criterion for a TM alpha-helix."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, inferred by similarity) records a transmembrane helix at positions 3..23. The segment KISIIPIVGVALSLAIILQLG (21 residues) is predominantly hydrophobic with boundary residues (K at 3, G at 23), consistent with a TM alpha-helix of appropriate length. The annotation is computational/inferred rather than experimentally verified, but it directly supports the expected answer.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable principles distinguish D from the other choices. (1) Option A is trivially eliminated because positions 635-655 exceed the 515-residue protein length. (2) A TM alpha-helix requires approximately 19-21 residues to span the ~30 Å hydrophobic core of the lipid bilayer; option C (3..18) provides only 16 residues, which is below the minimum helix length for membrane crossing. (3) Option B (5..27) extends into positions 24-27 (R, T, Y, W), which include a charged Arg and aromatic Trp/Tyr residues that are characteristic of the membrane-water interface, not the hydrophobic core. (4) Option D (3..23) yields a 21-residue segment that is predominantly hydrophobic (I, I, I, P, I, V, V, A, L, L, A, I, I, L, L) with boundary residues (K, S, Q, G) at the edges, matching the expected length and composition of a TM helix. This reasoning relies on general TM helix biophysics learned from many membrane proteins, not on memorizing this specific entry.",
    "missing_item_specific_fact": "",
    "reason": "The discrimination among options relies on well-established general principles: TM helix length (~19-21 residues), hydrophobic composition, boundary residue patterns (charged/aromatic at interfaces), and simple arithmetic (option A exceeds protein length). No fact specific to this exact protein beyond reading the sequence is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by length; option C is too short for a TM helix; option B includes clearly non-TM residues (Arg, Tyr, Trp). Only D satisfies both the length requirement and the hydrophobic composition criterion for a TM alpha-helix."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational rather than experimentally determined.",
    "The segment 3-23 is not a 'textbook' pure-hydrophobic TM helix; it contains several polar residues (K, S, S, Q, G), which is common in real TM helices but makes purely hydrophobicity-based prediction less crisp.",
    "The protein is a fungal cytochrome P450 monooxygenase (mfmA from Annulohypoxylon moriforme), a family in which N-terminal TM anchoring to the ER membrane is a well-known feature, further supporting the annotation."
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
  "benchmark_sequence_length": 515,
  "benchmark_sequence_sha256": "b148dd6535a2478e2a065541559f956e45ac653fa2dceff0ebdbeae21e9d5591",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 515,
  "current_source_sequence_sha256": "b148dd6535a2478e2a065541559f956e45ac653fa2dceff0ebdbeae21e9d5591",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P9WEG0",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "selected_historical_source_sequence_length": 515,
  "selected_historical_source_sequence_sha256": "b148dd6535a2478e2a065541559f956e45ac653fa2dceff0ebdbeae21e9d5591",
  "selected_historical_version": {
    "accession": "P9WEG0",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFMA_ANNMO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEG0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Xylariomycetidae\",\"Xylariales\",\"Hypoxylaceae\",\"Annulohypoxylon\"],\"scientificName\":\"Annulohypoxylon moriforme\",\"synonyms\":[\"Hypoxylon moriforme\"],\"taxonId\":326622}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"11'-O-desmethylfendlerol biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase mfmA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":23},\"start\":{\"modifier\":\"EXACT\",\"value\":3}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan D.\",\"Matsuda Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38404388\"},{\"database\":\"DOI\",\"id\":\"10.1039/d3sc06001b\"}],\"citationType\":\"journal article\",\"firstPage\":\"3011\",\"id\":\"38404388\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"3017\",\"publicationDate\":\"2024\",\"title\":\"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CBS 123579\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   MFMA_ANNMO              Reviewed;         515 AA.\nAC   P9WEG0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Cytochrome P450 monooxygenase mfmA {ECO:0000303|PubMed:38404388};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:38404388};\nDE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein A {ECO:0000303|PubMed:38404388};\nGN   Name=mfmA {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_29954;\nOS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.\nOX   NCBI_TaxID=326622;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:18.350529+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "url": "https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   STRAIN=CBS 123579;\nRX   PubMed=38404388; DOI=10.1039/d3sc06001b;\nRA   Yan D., Matsuda Y.;\nRT   \"Global genome mining-driven discovery of an unusual biosynthetic logic for\nRT   fungal polyketide-terpenoid hybrids.\";\nRL   Chem. Sci. 15:3011-3017(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:18.350529+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "url": "https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        3..23\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:18.350529+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "url": "https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
