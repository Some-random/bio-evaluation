# transmembrane_0084

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0084.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 18..38

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGASTFSQSFAEGYAAWALMLPALVGCALLIYRAFFAIRYPANLPLAGEPDGKRTFSWRTRWRYYIDCEALYKETYDNYTKHGKTVLLPGLGFRHDIVLPQSAMRDIMARPEKELSHADAVLELVQLKYSLGHEKYKADPWPCMLVKSDINSKLEAVCDGMNEELKYAFDKYVGCDTESWKEVDLLETIRMIIMAAASRFTVGFPLCRSEAYLRACWKVNDGIMMNGGLTGATPRLLRPIVGPLVTMKLRQSIEQVKKHVEPIYRQRVQALSQQNSAEKPASDETQDLFQQMLRYAQRERPGELHDLPSMCRRLCFANFAAVHQTTLLVTNMVLNIVSSDPQHNTISVLRDEVKDVIGPDSNAKWTKYKVAQMIKSDSVARETMRLYSNTNRGVFRKVLVEGIKTEDGIELPKGAYVSFLGRPLQCDPETFEDPFEYNPFRFSRIREQAPRDTKGRSSASHLSFVSTSPEHLPFGHGGHSCPGRFLVDFEVKMIVAYLLMNYDVEFPAEYKGQRPANRWMAEALMPPSGARIRIKRRS

[Multiple Choices]
A. 18..38; 321..343
B. 18..38
C. 9..29; 2201..2221; 2238..2258; 2267..2287; 2296..2316; 2352..2372; 2386..2406
D. 16..43
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

> The sequence-matched UniProt annotation identifies residues 18–38 as a helical transmembrane region, supporting B. Its evidence code indicates computational annotation, not direct experimental demonstration.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a prominent N-terminal hydrophobic stretch of about membrane-spanning length, a transferable hallmark of a transmembrane helix. B gives a plausible span; D includes the same stretch but extends into flanking residues, while A adds a second region and C proposes positions beyond this sequence's length.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The hydrophobic sequence pattern meaningfully distinguishes the N-terminal segment from the other proposed regions without needing an annotation for this exact protein. Exact helix boundaries can be uncertain, but B is the best-delimited offered span.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D overlaps the same hydrophobic helix, but extends appreciably beyond the best-delimited membrane-spanning segment; the sequence gives a reasonable basis to prefer B.


### Important caveats

- The supporting database annotation is computational rather than direct experimental evidence.
- Transmembrane boundaries can vary somewhat among prediction methods.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a prominent N-terminal hydrophobic stretch of about membrane-spanning length, a transferable hallmark of a transmembrane helix. B gives a plausible span; D includes the same stretch but extends into flanking residues, while A adds a second region and C proposes positions beyond this sequence's length.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobic sequence pattern meaningfully distinguishes the N-terminal segment from the other proposed regions without needing an annotation for this exact protein. Exact helix boundaries can be uncertain, but B is the best-delimited offered span."
  },
  "case_id": "transmembrane_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 18–38 as a helical transmembrane region, supporting B. Its evidence code indicates computational annotation, not direct experimental demonstration."
  },
  "important_caveats": [
    "The supporting database annotation is computational rather than direct experimental evidence.",
    "Transmembrane boundaries can vary somewhat among prediction methods."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D overlaps the same hydrophobic helix, but extends appreciably beyond the best-delimited membrane-spanning segment; the sequence gives a reasonable basis to prefer B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 18–38 as a helical transmembrane region, supporting B. Its evidence code indicates computational annotation, not direct experimental demonstration.",
    "evidence_ids": ["H3", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a prominent N-terminal hydrophobic stretch of about membrane-spanning length, a transferable hallmark of a transmembrane helix. B gives a plausible span; D includes the same stretch but extends into flanking residues, while A adds a second region and C proposes positions beyond this sequence's length.",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobic sequence pattern meaningfully distinguishes the N-terminal segment from the other proposed regions without needing an annotation for this exact protein. Exact helix boundaries can be uncertain, but B is the best-delimited offered span."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D overlaps the same hydrophobic helix, but extends appreciably beyond the best-delimited membrane-spanning segment; the sequence gives a reasonable basis to prefer B."
  },
  "important_caveats": [
    "The supporting database annotation is computational rather than direct experimental evidence.",
    "Transmembrane boundaries can vary somewhat among prediction methods."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) records a single transmembrane helix at positions 18..38 with evidence code ECO:0000255 (inferred from electronic annotation, i.e., computational prediction). The sequence at positions 18-38 (ALMLPALVGCALLIYRAFFAI) is predominantly hydrophobic and consistent with a single-pass TM anchor, typical of microsomal cytochrome P450 enzymes. The key matches the sole annotated TM region. The annotation is computational rather than experimentally validated, but it is the recorded annotation and is consistent with the sequence composition.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option C is trivially eliminated because it references positions 2201-2406 in a 538-residue protein. Option A adds a second TM region at 321..343 (AVHQTTLLVTNMVLNIVSSDPQH), which contains numerous polar and charged residues (H, Q, T, N, S, D, P, Q, H) inconsistent with a transmembrane helix; a model applying hydrophobicity and TM composition rules learned from many proteins would reject this. Option D extends the helix to 16..43, adding C-terminal residues 39-43 (RYRAP): two arginines (charged), a tyrosine (polar aromatic), a proline (helix-breaking), and an asparagine (polar) — all incompatible with a TM helix per well-established composition rules (TM helices are overwhelmingly hydrophobic, avoid Pro, and exclude buried charges). The N-terminal extension (16-17 = AW) is more ambiguous, but the C-terminal extension decisively eliminates D. Option B (18..38) is the only region that is consistently hydrophobic and helix-compatible. This reasoning relies on transferable knowledge of TM helix composition learned across many membrane proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can distinguish the four options using hydrophobicity analysis and TM helix composition principles (avoidance of charged residues, proline, and polar residues within the bilayer core) that are generalizable across membrane proteins. The C-terminal boundary of D is clearly incompatible with TM, the second region in A is not convincingly TM, and C is impossible given protein length. No fact specific to this exact protein's experimental characterization is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The C-terminal extension in D (RYRAP) is clearly incompatible with TM helix composition, eliminating D. The second region in A (321-343) is too polar/charged for TM, eliminating A. C is impossible (positions exceed protein length). B is the only option fully consistent with TM helix properties. The N-terminal boundary (16 vs 18) is minor and does not create genuine ambiguity since D is already eliminated by its C-terminal extension.


### Important caveats

- The TM annotation is computational (ECO:0000255, inferred from electronic annotation), not experimentally validated. The exact boundaries could shift by a few residues depending on the prediction algorithm used.
- The protein is a cytochrome P450 monooxygenase (astC), and single-pass N-terminal TM anchors are common in microsomal P450s, which is consistent with the annotation but does not constitute experimental proof for this specific protein.
- The N-terminal boundary (16 vs 18) is somewhat ambiguous since residues A(16) and W(17) are compatible with TM, but this does not affect the final answer because D is eliminated by its clearly non-TM C-terminal extension.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C is trivially eliminated because it references positions 2201-2406 in a 538-residue protein. Option A adds a second TM region at 321..343 (AVHQTTLLVTNMVLNIVSSDPQH), which contains numerous polar and charged residues (H, Q, T, N, S, D, P, Q, H) inconsistent with a transmembrane helix; a model applying hydrophobicity and TM composition rules learned from many proteins would reject this. Option D extends the helix to 16..43, adding C-terminal residues 39-43 (RYRAP): two arginines (charged), a tyrosine (polar aromatic), a proline (helix-breaking), and an asparagine (polar) — all incompatible with a TM helix per well-established composition rules (TM helices are overwhelmingly hydrophobic, avoid Pro, and exclude buried charges). The N-terminal extension (16-17 = AW) is more ambiguous, but the C-terminal extension decisively eliminates D. Option B (18..38) is the only region that is consistently hydrophobic and helix-compatible. This reasoning relies on transferable knowledge of TM helix composition learned across many membrane proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can distinguish the four options using hydrophobicity analysis and TM helix composition principles (avoidance of charged residues, proline, and polar residues within the bilayer core) that are generalizable across membrane proteins. The C-terminal boundary of D is clearly incompatible with TM, the second region in A is not convincingly TM, and C is impossible given protein length. No fact specific to this exact protein's experimental characterization is needed."
  },
  "case_id": "transmembrane_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) records a single transmembrane helix at positions 18..38 with evidence code ECO:0000255 (inferred from electronic annotation, i.e., computational prediction). The sequence at positions 18-38 (ALMLPALVGCALLIYRAFFAI) is predominantly hydrophobic and consistent with a single-pass TM anchor, typical of microsomal cytochrome P450 enzymes. The key matches the sole annotated TM region. The annotation is computational rather than experimentally validated, but it is the recorded annotation and is consistent with the sequence composition."
  },
  "important_caveats": [
    "The TM annotation is computational (ECO:0000255, inferred from electronic annotation), not experimentally validated. The exact boundaries could shift by a few residues depending on the prediction algorithm used.",
    "The protein is a cytochrome P450 monooxygenase (astC), and single-pass N-terminal TM anchors are common in microsomal P450s, which is consistent with the annotation but does not constitute experimental proof for this specific protein.",
    "The N-terminal boundary (16 vs 18) is somewhat ambiguous since residues A(16) and W(17) are compatible with TM, but this does not affect the final answer because D is eliminated by its clearly non-TM C-terminal extension."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The C-terminal extension in D (RYRAP) is clearly incompatible with TM helix composition, eliminating D. The second region in A (321-343) is too polar/charged for TM, eliminating A. C is impossible (positions exceed protein length). B is the only option fully consistent with TM helix properties. The N-terminal boundary (16 vs 18) is minor and does not create genuine ambiguity since D is already eliminated by its C-terminal extension."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) records a single transmembrane helix at positions 18..38 with evidence code ECO:0000255 (inferred from electronic annotation, i.e., computational prediction). The sequence at positions 18-38 (ALMLPALVGCALLIYRAFFAI) is predominantly hydrophobic and consistent with a single-pass TM anchor, typical of microsomal cytochrome P450 enzymes. The key matches the sole annotated TM region. The annotation is computational rather than experimentally validated, but it is the recorded annotation and is consistent with the sequence composition.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option C is trivially eliminated because it references positions 2201-2406 in a 538-residue protein. Option A adds a second TM region at 321..343 (AVHQTTLLVTNMVLNIVSSDPQH), which contains numerous polar and charged residues (H, Q, T, N, S, D, P, Q, H) inconsistent with a transmembrane helix; a model applying hydrophobicity and TM composition rules learned from many proteins would reject this. Option D extends the helix to 16..43, adding C-terminal residues 39-43 (RYRAP): two arginines (charged), a tyrosine (polar aromatic), a proline (helix-breaking), and an asparagine (polar) — all incompatible with a TM helix per well-established composition rules (TM helices are overwhelmingly hydrophobic, avoid Pro, and exclude buried charges). The N-terminal extension (16-17 = AW) is more ambiguous, but the C-terminal extension decisively eliminates D. Option B (18..38) is the only region that is consistently hydrophobic and helix-compatible. This reasoning relies on transferable knowledge of TM helix composition learned across many membrane proteins.",
    "missing_item_specific_fact": "",
    "reason": "A model can distinguish the four options using hydrophobicity analysis and TM helix composition principles (avoidance of charged residues, proline, and polar residues within the bilayer core) that are generalizable across membrane proteins. The C-terminal boundary of D is clearly incompatible with TM, the second region in A is not convincingly TM, and C is impossible given protein length. No fact specific to this exact protein's experimental characterization is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The C-terminal extension in D (RYRAP) is clearly incompatible with TM helix composition, eliminating D. The second region in A (321-343) is too polar/charged for TM, eliminating A. C is impossible (positions exceed protein length). B is the only option fully consistent with TM helix properties. The N-terminal boundary (16 vs 18) is minor and does not create genuine ambiguity since D is already eliminated by its C-terminal extension."
  },
  "important_caveats": [
    "The TM annotation is computational (ECO:0000255, inferred from electronic annotation), not experimentally validated. The exact boundaries could shift by a few residues depending on the prediction algorithm used.",
    "The protein is a cytochrome P450 monooxygenase (astC), and single-pass N-terminal TM anchors are common in microsomal P450s, which is consistent with the annotation but does not constitute experimental proof for this specific protein.",
    "The N-terminal boundary (16 vs 18) is somewhat ambiguous since residues A(16) and W(17) are compatible with TM, but this does not affect the final answer because D is eliminated by its clearly non-TM C-terminal extension."
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
  "benchmark_sequence_length": 538,
  "benchmark_sequence_sha256": "d64a1263e1e31530d1873b74b304f62355010d457a8b6d79b78a7154c76862f3",
  "current_entry_audit": {
    "entryVersion": 98,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 538,
  "current_source_sequence_sha256": "d64a1263e1e31530d1873b74b304f62355010d457a8b6d79b78a7154c76862f3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 96,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0CPG6",
  "selected_historical_entry_version": 96,
  "selected_historical_record_sha256": "482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd",
  "selected_historical_source_sequence_length": 538,
  "selected_historical_source_sequence_sha256": "d64a1263e1e31530d1873b74b304f62355010d457a8b6d79b78a7154c76862f3",
  "selected_historical_version": {
    "accession": "Q0CPG6",
    "database": "Swiss-Prot",
    "entryVersion": 96,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTC_ASPTN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0CPG6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":98,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein C\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase astC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":38},\"start\":{\"modifier\":\"EXACT\",\"value\":18}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H1",
  "excerpt": "ID   ASTC_ASPTN              Reviewed;         538 AA.\nAC   Q0CPG6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 96.\nDE   RecName: Full=Cytochrome P450 monooxygenase astC {ECO:0000303|PubMed:29995859};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein C {ECO:0000303|PubMed:29995859};\nGN   Name=astC {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04418;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:24.324806+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd",
  "url": "https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:24.324806+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd",
  "url": "https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        18..38\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:24.324806+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd",
  "url": "https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
