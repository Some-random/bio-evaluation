# active_site_0003

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0003.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 118 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVAFSSLFLGASIAATALAAPGELPGMHLNKRQTYTQSATGTHDGYYFSFWTDGGPNVRYTNEAGGQYSVTWSGNGNWVGGKGWNPGAARTINYTGTYQPNGNSYLAVYGWTRNPLVEYYVVENFGTYDPSTGAQRLGSINVDGSTYNVYRTRRTNAPSIEGTRSFDQYWSVRVNKRVGGSVDMNAHFNAWRQAGLTLGTHDYQIVATEGYFSSGSARINVGGGSTGGGNNGGGNNGGNPGGNPGGNPGGNPGGNCSPRWGQCGGQGWNGPTCCESGTTCRQQNQWYSQCL

[Multiple Choices]
A. Position 2153 (For beta-ketoacyl synthase 2 activity)
B. Position 161 (Lowers pKa of active site Tyr)
C. Position 118 (Nucleophile)
D. Position 209 (Proton donor)
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

> The sequence-matched UniProt record annotates position 118 as the nucleophile, consistent with choice C. This is a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts. The same record also annotates position 209 as a proton donor, so C is supported but is not uniquely correct under the question wording.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a fungal GH11 xylanase. GH11 xylanases use a conserved pair of catalytic glutamates in a retaining mechanism: one acts as the nucleophile and the other as the proton donor. Family-level knowledge can therefore support the catalytic roles represented by choices C and D, rather than requiring recall of this exact protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable GH11 family knowledge gives a meaningful basis for identifying catalytic residues among the options. It does not, however, make C uniquely correct because D also describes a catalytic active-site residue.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The question asks for residues that constitute the catalytic center, and both the nucleophile at position 118 and proton donor at position 209 are annotated as active-site residues. Thus both choices are defensible as written.


### Important caveats

- The reviewer-only sequence-matched annotations support both catalytic roles but are based on a PROSITE-ProRule computational annotation.
- The source identity and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a fungal GH11 xylanase. GH11 xylanases use a conserved pair of catalytic glutamates in a retaining mechanism: one acts as the nucleophile and the other as the proton donor. Family-level knowledge can therefore support the catalytic roles represented by choices C and D, rather than requiring recall of this exact protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable GH11 family knowledge gives a meaningful basis for identifying catalytic residues among the options. It does not, however, make C uniquely correct because D also describes a catalytic active-site residue."
  },
  "case_id": "active_site_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 118 as the nucleophile, consistent with choice C. This is a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts. The same record also annotates position 209 as a proton donor, so C is supported but is not uniquely correct under the question wording."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched annotations support both catalytic roles but are based on a PROSITE-ProRule computational annotation.",
    "The source identity and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The question asks for residues that constitute the catalytic center, and both the nucleophile at position 118 and proton donor at position 209 are annotated as active-site residues. Thus both choices are defensible as written."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 118 as the nucleophile, consistent with choice C. This is a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts. The same record also annotates position 209 as a proton donor, so C is supported but is not uniquely correct under the question wording.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a fungal GH11 xylanase. GH11 xylanases use a conserved pair of catalytic glutamates in a retaining mechanism: one acts as the nucleophile and the other as the proton donor. Family-level knowledge can therefore support the catalytic roles represented by choices C and D, rather than requiring recall of this exact protein's record.",
    "missing_item_specific_fact": "",
    "reason": "Transferable GH11 family knowledge gives a meaningful basis for identifying catalytic residues among the options. It does not, however, make C uniquely correct because D also describes a catalytic active-site residue."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The question asks for residues that constitute the catalytic center, and both the nucleophile at position 118 and proton donor at position 209 are annotated as active-site residues. Thus both choices are defensible as written."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched annotations support both catalytic roles but are based on a PROSITE-ProRule computational annotation.",
    "The source identity and annotations were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A0B5JC15 (Endo-1,4-beta-xylanase 11B, EC 3.2.1.8) explicitly annotates position 118 as 'Nucleophile' (Active site feature, evidence ECO:0000255|PROSITE-ProRule:PRU01097). Position 118 in the supplied 291-residue sequence is indeed Y (Tyrosine), consistent with a Tyr-nucleophile variant of GH11 xylanases. The annotation is computational (PROSITE-ProRule pattern matching), not experimentally validated, but it is the recorded annotation for this entry and the sequence matches.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark GH11 xylanase motifs (e.g., 'WTDGGPNVRY' near the N-terminus, 'PLVEYY' in the nucleophile region, 'ATEG' in the proton donor region), allowing family identification. In retaining glycosidases, the nucleophile is conventionally the primary catalytic residue—it forms the covalent glycosyl-enzyme intermediate—whereas the proton donor (acid/base) assists proton transfer. The question asks for 'the enzyme's catalytic center,' and the nucleophile is the single most defining residue of that center. Position 118 falls squarely in the GH11 nucleophile region (the conserved 'PLVE' motif, here 'PLVEYY'), while position 209 falls in the proton donor region ('ATEG'). A model familiar with GH11 catalytic architecture can recognize the nucleophile region and select C over D. Additionally, option A (position 2153 in a 291-residue protein, unrelated beta-ketoacyl synthase) and B (secondary pKa-lowering role) are clearly non-catalytic-center roles.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The protein can be identified as GH11 xylanase from conserved sequence motifs. The nucleophile vs. proton donor distinction is standard glycosidase biochemistry learned from many GH families. The nucleophile region in GH11 ('PLVE' motif) is well-characterized across homologs, and position 118 lies within it. Choosing the nucleophile as 'the' catalytic center residue over the proton donor is a defensible, transferable inference from glycosidase mechanism knowledge. Some uncertainty remains about whether the nucleophile is E(117) or Y(118) in this variant, but the options only offer 118, and the PROSITE-ProRule mapping places it there.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both position 118 (nucleophile) and position 209 (proton donor) are annotated active site residues in the UniProt entry. The question asks for 'the enzyme's catalytic center,' which in strict biochemical terms includes both residues. However, the nucleophile is conventionally emphasized as THE key catalytic residue in glycosidases (it performs the nucleophilic attack forming the covalent intermediate), making C the stronger single answer. D is not wrong as an active site residue but is secondary in catalytic importance.


### Important caveats

- The active site annotation is computational (ECO:0000255, PROSITE-ProRule PRU01097), not experimentally determined. No mutagenesis or structural data in the evidence confirms Tyr118 as the nucleophile.
- Position 118 is Tyr, which is atypical for GH11 (most GH11 xylanases use Glu as nucleophile). This Tyr-nucleophile variant is annotated by pattern matching and may warrant experimental confirmation.
- Both C and D are valid active site residues per the annotation; the question's phrasing 'the catalytic center' could arguably encompass both, but the single-answer format forces selection of the most critical residue (nucleophile).
- Option A (position 2153) is trivially wrong for a 291-residue protein and references an unrelated enzyme class.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark GH11 xylanase motifs (e.g., 'WTDGGPNVRY' near the N-terminus, 'PLVEYY' in the nucleophile region, 'ATEG' in the proton donor region), allowing family identification. In retaining glycosidases, the nucleophile is conventionally the primary catalytic residue—it forms the covalent glycosyl-enzyme intermediate—whereas the proton donor (acid/base) assists proton transfer. The question asks for 'the enzyme's catalytic center,' and the nucleophile is the single most defining residue of that center. Position 118 falls squarely in the GH11 nucleophile region (the conserved 'PLVE' motif, here 'PLVEYY'), while position 209 falls in the proton donor region ('ATEG'). A model familiar with GH11 catalytic architecture can recognize the nucleophile region and select C over D. Additionally, option A (position 2153 in a 291-residue protein, unrelated beta-ketoacyl synthase) and B (secondary pKa-lowering role) are clearly non-catalytic-center roles.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The protein can be identified as GH11 xylanase from conserved sequence motifs. The nucleophile vs. proton donor distinction is standard glycosidase biochemistry learned from many GH families. The nucleophile region in GH11 ('PLVE' motif) is well-characterized across homologs, and position 118 lies within it. Choosing the nucleophile as 'the' catalytic center residue over the proton donor is a defensible, transferable inference from glycosidase mechanism knowledge. Some uncertainty remains about whether the nucleophile is E(117) or Y(118) in this variant, but the options only offer 118, and the PROSITE-ProRule mapping places it there."
  },
  "case_id": "active_site_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A0B5JC15 (Endo-1,4-beta-xylanase 11B, EC 3.2.1.8) explicitly annotates position 118 as 'Nucleophile' (Active site feature, evidence ECO:0000255|PROSITE-ProRule:PRU01097). Position 118 in the supplied 291-residue sequence is indeed Y (Tyrosine), consistent with a Tyr-nucleophile variant of GH11 xylanases. The annotation is computational (PROSITE-ProRule pattern matching), not experimentally validated, but it is the recorded annotation for this entry and the sequence matches."
  },
  "important_caveats": [
    "The active site annotation is computational (ECO:0000255, PROSITE-ProRule PRU01097), not experimentally determined. No mutagenesis or structural data in the evidence confirms Tyr118 as the nucleophile.",
    "Position 118 is Tyr, which is atypical for GH11 (most GH11 xylanases use Glu as nucleophile). This Tyr-nucleophile variant is annotated by pattern matching and may warrant experimental confirmation.",
    "Both C and D are valid active site residues per the annotation; the question's phrasing 'the catalytic center' could arguably encompass both, but the single-answer format forces selection of the most critical residue (nucleophile).",
    "Option A (position 2153) is trivially wrong for a 291-residue protein and references an unrelated enzyme class."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both position 118 (nucleophile) and position 209 (proton donor) are annotated active site residues in the UniProt entry. The question asks for 'the enzyme's catalytic center,' which in strict biochemical terms includes both residues. However, the nucleophile is conventionally emphasized as THE key catalytic residue in glycosidases (it performs the nucleophilic attack forming the covalent intermediate), making C the stronger single answer. D is not wrong as an active site residue but is secondary in catalytic importance."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"active_site_0003","expected_answer_check":{"judgment":"supported","reason":"The UniProt annotation for A0A0B5JC15 (Endo-1,4-beta-xylanase 11B, EC 3.2.1.8) explicitly annotates position 118 as 'Nucleophile' (Active site feature, evidence ECO:0000255|PROSITE-ProRule:PRU01097). Position 118 in the supplied 291-residue sequence is indeed Y (Tyrosine), consistent with a Tyr-nucleophile variant of GH11 xylanases. The annotation is computational (PROSITE-ProRule pattern matching), not experimentally validated, but it is the recorded annotation for this entry and the sequence matches.","evidence_ids":["C5","H4"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The sequence contains hallmark GH11 xylanase motifs (e.g., 'WTDGGPNVRY' near the N-terminus, 'PLVEYY' in the nucleophile region, 'ATEG' in the proton donor region), allowing family identification. In retaining glycosidases, the nucleophile is conventionally the primary catalytic residue—it forms the covalent glycosyl-enzyme intermediate—whereas the proton donor (acid/base) assists proton transfer. The question asks for 'the enzyme's catalytic center,' and the nucleophile is the single most defining residue of that center. Position 118 falls squarely in the GH11 nucleophile region (the conserved 'PLVE' motif, here 'PLVEYY'), while position 209 falls in the proton donor region ('ATEG'). A model familiar with GH11 catalytic architecture can recognize the nucleophile region and select C over D. Additionally, option A (position 2153 in a 291-residue protein, unrelated beta-ketoacyl synthase) and B (secondary pKa-lowering role) are clearly non-catalytic-center roles.","missing_item_specific_fact":"","reason":"The protein can be identified as GH11 xylanase from conserved sequence motifs. The nucleophile vs. proton donor distinction is standard glycosidase biochemistry learned from many GH families. The nucleophile region in GH11 ('PLVE' motif) is well-characterized across homologs, and position 118 lies within it. Choosing the nucleophile as 'the' catalytic center residue over the proton donor is a defensible, transferable inference from glycosidase mechanism knowledge. Some uncertainty remains about whether the nucleophile is E(117) or Y(118) in this variant, but the options only offer 118, and the PROSITE-ProRule mapping places it there."},"question_ambiguity":{"multiple_defensible_options":["C","D"],"reason":"Both position 118 (nucleophile) and position 209 (proton donor) are annotated active site residues in the UniProt entry. The question asks for 'the enzyme's catalytic center,' which in strict biochemical terms includes both residues. However, the nucleophile is conventionally emphasized as THE key catalytic residue in glycosidases (it performs the nucleophilic attack forming the covalent intermediate), making C the stronger single answer. D is not wrong as an active site residue but is secondary in catalytic importance."},"important_caveats":["The active site annotation is computational (ECO:0000255, PROSITE-ProRule PRU01097), not experimentally determined. No mutagenesis or structural data in the evidence confirms Tyr118 as the nucleophile.","Position 118 is Tyr, which is atypical for GH11 (most GH11 xylanases use Glu as nucleophile). This Tyr-nucleophile variant is annotated by pattern matching and may warrant experimental confirmation.","Both C and D are valid active site residues per the annotation; the question's phrasing 'the catalytic center' could arguably encompass both, but the single-answer format forces selection of the most critical residue (nucleophile).","Option A (position 2153) is trivially wrong for a 291-residue protein and references an unrelated enzyme class."]}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 291,
  "benchmark_sequence_sha256": "cd3a3423a03c858541b956741c23114bb67ae727771dfd47823e3d5c8afd1852",
  "current_entry_audit": {
    "entryVersion": 35,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-04-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 291,
  "current_source_sequence_sha256": "cd3a3423a03c858541b956741c23114bb67ae727771dfd47823e3d5c8afd1852",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 34,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0B5JC15",
  "selected_historical_entry_version": 34,
  "selected_historical_record_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "selected_historical_source_sequence_length": 291,
  "selected_historical_source_sequence_sha256": "cd3a3423a03c858541b956741c23114bb67ae727771dfd47823e3d5c8afd1852",
  "selected_historical_version": {
    "accession": "A0A0B5JC15",
    "database": "Swiss-Prot",
    "entryVersion": 34,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "XY11B_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0B5JC15\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":35,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-04-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase 11B\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25629035\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25629035\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase 11B\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25629035\",\"source\":\"PubMed\"}],\"value\":\"Xylanase 11B\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":118},\"start\":{\"modifier\":\"EXACT\",\"value\":118}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":209},\"start\":{\"modifier\":\"EXACT\",\"value\":209}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Shi P.\",\"Du Y.\",\"Yang H.\",\"Huang H.\",\"Zhang X.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25629035\"},{\"database\":\"DOI\",\"id\":\"10.1155/2015/149504\"}],\"citationType\":\"journal article\",\"firstPage\":\"149504\",\"id\":\"25629035\",\"journal\":\"Biomed. Res. Int.\",\"lastPage\":\"149504\",\"publicationDate\":\"2015\",\"title\":\"Molecular characterization of a new alkaline-tolerant xylanase from Humicola insolens Y1.\",\"volume\":\"2015\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"DOMAIN\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:36.597840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a238daea93370d4280f04bdd206eb25eb6338af729fb5ec529e171df677d32d5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0B5JC15.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)

```json
{
  "entry_version": 34,
  "evidence_id": "H1",
  "excerpt": "ID   XY11B_HUMIN             Reviewed;         291 AA.\nAC   A0A0B5JC15;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-APR-2015, sequence version 1.\nDT   28-JAN-2026, entry version 34.\nDE   RecName: Full=Endo-1,4-beta-xylanase 11B {ECO:0000303|PubMed:25629035};\nDE            Short=Xylanase 11B {ECO:0000303|PubMed:25629035};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:25629035};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase 11B {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=Xyn11B {ECO:0000303|PubMed:25629035};\nGN   Synonyms=Xyl2 {ECO:0000303|PubMed:8190078};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:16.201745+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "url": "https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)

```json
{
  "entry_version": 34,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   DOMAIN, AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=25629035; DOI=10.1155/2015/149504;\nRA   Shi P., Du Y., Yang H., Huang H., Zhang X., Wang Y., Yao B.;\nRT   \"Molecular characterization of a new alkaline-tolerant xylanase from\nRT   Humicola insolens Y1.\";\nRL   Biomed. Res. Int. 2015:149504-149504(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:16.201745+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "url": "https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)

```json
{
  "entry_version": 34,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   IDENTIFICATION.\nRX   PubMed=8190078; DOI=10.1007/bf00301060;\nRA   Dalboege H., Hansen H.P.H.;\nRT   \"A novel method for efficient expression cloning of fungal enzyme genes.\";\nRL   Mol. Gen. Genet. 243:253-260(1994).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:16.201745+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "url": "https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)

```json
{
  "entry_version": 34,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        118\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:16.201745+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "url": "https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34)

```json
{
  "entry_version": 34,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        209\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:16.201745+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee9bc3bc973cf545f5a28e6f916095cb6d6bebc19423799079b62f9b5d645663",
  "url": "https://rest.uniprot.org/unisave/A0A0B5JC15?format=txt&versions=34"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
