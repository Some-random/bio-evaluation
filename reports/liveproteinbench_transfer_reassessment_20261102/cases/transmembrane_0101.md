# transmembrane_0101

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0101.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 29..49; 153..173; 200..220; 399..419; 443..463; 479..499; 526..546; 569..586; 590..610; 635..665; 674..694

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVMSENSNISYCQAVANRTSFFTTAYNGIPETLILNTIFWVLLILLFTVLRHQAGDFGRLALVNSNGSKKRWTEIFYSRAASVVDPQPSTSTQVSPRPSTTSQGVPDSTPLSPIQPEEGLFGWIRVTLKLRKETILLHTGPDAVHYLSFQQHLMAVMALVTIVSLVIILPVNFLNGPKENPYDVNAFGRTTMANLSPDSPWLWVHTIITILYIPLVVLIMRRASGRNAFKKAATRTIMISNISSSDRNKTVVRNYMQELFPDVTIENVSIAYNISRLYVRNAEFERVHEARLYCEHHRNRDTLMVKPEMCSCKKENAYEYYQREERKLSGDVARLRASTMNEPLDIAFITVSTVQEAQNIVTHFTPGTYRQWHLVFAPSPDDLFWENLNVNKSHWYLKFFCVNAVLFLVLFFLSTPAMVVSLLNSRPWVKETEGKISPLVADFLPTLMLWTLSALMPVIVAISDKWMRHYTRSKQNYSIMTKCFGYLLMMIMILPSLGLTSAQALLEWGFLNQTDRWQCIFLPDRGSFYVNYIITAAFIGTALELLRFPELIVYIWSLLKAKSKAETPYIRKAILIEFPFGTHYAWTTLVFTIAIVYSVACPLIMPFAMIYICLKHFVDRHNLYFAYGPSNMISRKGGKIHSTAVTMTKFSVVILVLVMAMICFFRGDNGMARFLLLIISLAITLTLFTFMSPIKRCAATRRPSIVEIAGPAPIYVPDVLKDNGIRTSSVRPSAAAFGGYGSDSVSEYDSSQYSVNSVEA

[Multiple Choices]
A. 29..49; 153..173; 200..220; 399..419; 443..463; 479..499; 526..546; 569..586; 590..610; 635..665; 674..694
B. 20..40; 84..104; 119..139; 180..200; 210..230; 273..293; 304..324; 381..401
C. 29..49; 153..173; 399..419; 443..463; 479..499; 526..546; 569..586; 590..610; 635..665; 674..694
D. 29..49; 153..173; 200..220; 399..419; 443..463; 479..499; 526..546; 569..586; 585..608; 635..665; 674..694
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

> The sequence matches the annotated protein sequence, and the supplied UniProt annotations identify the listed segments in A as transmembrane helices. These annotations carry evidence code ECO:0000255, indicating computational evidence rather than direct experimental confirmation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated long, strongly hydrophobic stretches characteristic of membrane-spanning alpha-helices, separated by more polar or charged regions. This multipass pattern supports the set of helices in A: for example, the hydrophobic stretch around 200–220 distinguishes A from C, while the hydrophobic region around 590–610 follows a short polar interruption near 587–589, distinguishing A from D's overlapping alternative. B's proposed intervals also do not align well with this pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices differ in whether their intervals match recognizable hydrophobic transmembrane segments in the provided sequence. Family-specific annotation or exact target identity is not needed to meaningfully favor A, though sequence-based prediction does not guarantee exact experimental boundaries.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives differ at intervals where the sequence's hydrophobicity pattern favors the intervals in A; no other choice is comparably defensible from the supplied sequence.


### Important caveats

- The supporting source annotations are computationally evidenced and should not be described as experimental measurements.
- Reviewer-only source identity and annotations were not available as original inputs and were not used as the basis for the answerability inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated long, strongly hydrophobic stretches characteristic of membrane-spanning alpha-helices, separated by more polar or charged regions. This multipass pattern supports the set of helices in A: for example, the hydrophobic stretch around 200–220 distinguishes A from C, while the hydrophobic region around 590–610 follows a short polar interruption near 587–589, distinguishing A from D's overlapping alternative. B's proposed intervals also do not align well with this pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices differ in whether their intervals match recognizable hydrophobic transmembrane segments in the provided sequence. Family-specific annotation or exact target identity is not needed to meaningfully favor A, though sequence-based prediction does not guarantee exact experimental boundaries."
  },
  "case_id": "transmembrane_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24",
      "C26"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein sequence, and the supplied UniProt annotations identify the listed segments in A as transmembrane helices. These annotations carry evidence code ECO:0000255, indicating computational evidence rather than direct experimental confirmation."
  },
  "important_caveats": [
    "The supporting source annotations are computationally evidenced and should not be described as experimental measurements.",
    "Reviewer-only source identity and annotations were not available as original inputs and were not used as the basis for the answerability inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ at intervals where the sequence's hydrophobicity pattern favors the intervals in A; no other choice is comparably defensible from the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein sequence, and the supplied UniProt annotations identify the listed segments in A as transmembrane helices. These annotations carry evidence code ECO:0000255, indicating computational evidence rather than direct experimental confirmation.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated long, strongly hydrophobic stretches characteristic of membrane-spanning alpha-helices, separated by more polar or charged regions. This multipass pattern supports the set of helices in A: for example, the hydrophobic stretch around 200–220 distinguishes A from C, while the hydrophobic region around 590–610 follows a short polar interruption near 587–589, distinguishing A from D's overlapping alternative. B's proposed intervals also do not align well with this pattern.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices differ in whether their intervals match recognizable hydrophobic transmembrane segments in the provided sequence. Family-specific annotation or exact target identity is not needed to meaningfully favor A, though sequence-based prediction does not guarantee exact experimental boundaries."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ at intervals where the sequence's hydrophobicity pattern favors the intervals in A; no other choice is comparably defensible from the supplied sequence."
  },
  "important_caveats": [
    "The supporting source annotations are computationally evidenced and should not be described as experimental measurements.",
    "Reviewer-only source identity and annotations were not available as original inputs and were not used as the basis for the answerability inference."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q6NP91 (Drosophila Tmem63) lists exactly 11 transmembrane helical segments at positions 29-49, 153-173, 200-220, 399-419, 443-463, 479-499, 526-546, 569-586, 590-610, 635-665, and 674-694, matching option A precisely. All annotations carry evidence code ECO:0000255 (similarity-based computational inference), not experimental determination.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H19](#evidence-h19), [H21](#evidence-h21), [H23](#evidence-h23), [H25](#evidence-h25).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can apply hydrophobicity analysis (e.g., Kyte-Doolittle sliding window) to the 760-residue sequence to identify approximately 11 hydrophobic stretches of ~20 residues each. This eliminates option B, whose proposed segments (20-40, 84-104, 119-139, etc.) do not correspond to the major hydrophobic stretches in the sequence. The segment at 200-220 contains a clearly hydrophobic region (WVHTIITILYIPLVVLIM) that a hydrophobicity scan would flag as a TM helix, eliminating option C which omits it. Option D lists TM8 as 585-608, which overlaps TM7 (569-586) by residues 585-586; two transmembrane helices cannot physically overlap in the membrane, providing a structural constraint to reject D. The correct non-overlapping topology with a 3-residue extracellular loop (587-589) between TM7 and TM8 is consistent with option A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinction among options relies on standard transmembrane prediction principles: hydrophobicity analysis to locate TM segments, and the structural principle that TM helices cannot overlap. The 200-220 segment is identifiable by its hydrophobic character from the sequence itself. The overlap in option D (585-608 overlapping 569-586) is a structural impossibility that any model understanding membrane topology can use to eliminate that choice. Option B's positions are inconsistent with the sequence's hydrophobic profile. These are transferable principles of membrane protein biology, not facts specific to this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is eliminated by hydrophobicity analysis. Option C is eliminated because the 200-220 hydrophobic stretch is clearly present. Option D is eliminated by the structural impossibility of overlapping TM helices (585-586 overlap). Only option A satisfies all constraints simultaneously.


### Important caveats

- All UniProt TM annotations for this entry use evidence code ECO:0000255 (similarity-based), meaning they are computational predictions rather than experimentally determined boundaries.
- The boundary precision required to distinguish 590-610 from 585-608 is at the limit of typical TM predictor accuracy (±5 residues), but the overlap argument for D provides a principled structural exclusion independent of boundary precision.
- The 3-residue extracellular loop (587-589) between TM7 and TM8 is unusually short; a model might question this topology, but the non-overlap constraint still favors A over D.
- The protein is a mechanosensitive cation channel (TMEM63 family) with 11 TM segments, consistent with the TMEM63/TMC family topology known from related proteins.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can apply hydrophobicity analysis (e.g., Kyte-Doolittle sliding window) to the 760-residue sequence to identify approximately 11 hydrophobic stretches of ~20 residues each. This eliminates option B, whose proposed segments (20-40, 84-104, 119-139, etc.) do not correspond to the major hydrophobic stretches in the sequence. The segment at 200-220 contains a clearly hydrophobic region (WVHTIITILYIPLVVLIM) that a hydrophobicity scan would flag as a TM helix, eliminating option C which omits it. Option D lists TM8 as 585-608, which overlaps TM7 (569-586) by residues 585-586; two transmembrane helices cannot physically overlap in the membrane, providing a structural constraint to reject D. The correct non-overlapping topology with a 3-residue extracellular loop (587-589) between TM7 and TM8 is consistent with option A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinction among options relies on standard transmembrane prediction principles: hydrophobicity analysis to locate TM segments, and the structural principle that TM helices cannot overlap. The 200-220 segment is identifiable by its hydrophobic character from the sequence itself. The overlap in option D (585-608 overlapping 569-586) is a structural impossibility that any model understanding membrane topology can use to eliminate that choice. Option B's positions are inconsistent with the sequence's hydrophobic profile. These are transferable principles of membrane protein biology, not facts specific to this exact protein's database record."
  },
  "case_id": "transmembrane_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24",
      "C26",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17",
      "H19",
      "H21",
      "H23",
      "H25"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q6NP91 (Drosophila Tmem63) lists exactly 11 transmembrane helical segments at positions 29-49, 153-173, 200-220, 399-419, 443-463, 479-499, 526-546, 569-586, 590-610, 635-665, and 674-694, matching option A precisely. All annotations carry evidence code ECO:0000255 (similarity-based computational inference), not experimental determination."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry use evidence code ECO:0000255 (similarity-based), meaning they are computational predictions rather than experimentally determined boundaries.",
    "The boundary precision required to distinguish 590-610 from 585-608 is at the limit of typical TM predictor accuracy (±5 residues), but the overlap argument for D provides a principled structural exclusion independent of boundary precision.",
    "The 3-residue extracellular loop (587-589) between TM7 and TM8 is unusually short; a model might question this topology, but the non-overlap constraint still favors A over D.",
    "The protein is a mechanosensitive cation channel (TMEM63 family) with 11 TM segments, consistent with the TMEM63/TMC family topology known from related proteins."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is eliminated by hydrophobicity analysis. Option C is eliminated because the 200-220 hydrophobic stretch is clearly present. Option D is eliminated by the structural impossibility of overlapping TM helices (585-586 overlap). Only option A satisfies all constraints simultaneously."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q6NP91 (Drosophila Tmem63) lists exactly 11 transmembrane helical segments at positions 29-49, 153-173, 200-220, 399-419, 443-463, 479-499, 526-546, 569-586, 590-610, 635-665, and 674-694, matching option A precisely. All annotations carry evidence code ECO:0000255 (similarity-based computational inference), not experimental determination.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26", "H5", "H7", "H9", "H11", "H13", "H15", "H17", "H19", "H21", "H23", "H25"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can apply hydrophobicity analysis (e.g., Kyte-Doolittle sliding window) to the 760-residue sequence to identify approximately 11 hydrophobic stretches of ~20 residues each. This eliminates option B, whose proposed segments (20-40, 84-104, 119-139, etc.) do not correspond to the major hydrophobic stretches in the sequence. The segment at 200-220 contains a clearly hydrophobic region (WVHTIITILYIPLVVLIM) that a hydrophobicity scan would flag as a TM helix, eliminating option C which omits it. Option D lists TM8 as 585-608, which overlaps TM7 (569-586) by residues 585-586; two transmembrane helices cannot physically overlap in the membrane, providing a structural constraint to reject D. The correct non-overlapping topology with a 3-residue extracellular loop (587-589) between TM7 and TM8 is consistent with option A.",
    "missing_item_specific_fact": "",
    "reason": "The distinction among options relies on standard transmembrane prediction principles: hydrophobicity analysis to locate TM segments, and the structural principle that TM helices cannot overlap. The 200-220 segment is identifiable by its hydrophobic character from the sequence itself. The overlap in option D (585-608 overlapping 569-586) is a structural impossibility that any model understanding membrane topology can use to eliminate that choice. Option B's positions are inconsistent with the sequence's hydrophobic profile. These are transferable principles of membrane protein biology, not facts specific to this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is eliminated by hydrophobicity analysis. Option C is eliminated because the 200-220 hydrophobic stretch is clearly present. Option D is eliminated by the structural impossibility of overlapping TM helices (585-586 overlap). Only option A satisfies all constraints simultaneously."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry use evidence code ECO:0000255 (similarity-based), meaning they are computational predictions rather than experimentally determined boundaries.",
    "The boundary precision required to distinguish 590-610 from 585-608 is at the limit of typical TM predictor accuracy (±5 residues), but the overlap argument for D provides a principled structural exclusion independent of boundary precision.",
    "The 3-residue extracellular loop (587-589) between TM7 and TM8 is unusually short; a model might question this topology, but the non-overlap constraint still favors A over D.",
    "The protein is a mechanosensitive cation channel (TMEM63 family) with 11 TM segments, consistent with the TMEM63/TMC family topology known from related proteins."
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
  "benchmark_sequence_length": 760,
  "benchmark_sequence_sha256": "9076bde0b51e3b259052a8e628ac3042e27980689b45147e79e2d424167c3189",
  "current_entry_audit": {
    "entryVersion": 148,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 760,
  "current_source_sequence_sha256": "9076bde0b51e3b259052a8e628ac3042e27980689b45147e79e2d424167c3189",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 147,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q6NP91",
  "selected_historical_entry_version": 147,
  "selected_historical_record_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "selected_historical_source_sequence_length": 760,
  "selected_historical_source_sequence_sha256": "9076bde0b51e3b259052a8e628ac3042e27980689b45147e79e2d424167c3189",
  "selected_historical_version": {
    "accession": "Q6NP91",
    "database": "Swiss-Prot",
    "entryVersion": 147,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "TM63_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q6NP91\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":148,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Transmembrane protein 63\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38388853\",\"source\":\"PubMed\"}],\"value\":\"DmTMEM63\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Mechanosensitive cation channel Tmem63\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":28},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical; Name=TM0\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":49},\"start\":{\"modifier\":\"EXACT\",\"value\":29}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":152},\"start\":{\"modifier\":\"EXACT\",\"value\":50}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical; Name=TM1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":173},\"start\":{\"modifier\":\"EXACT\",\"value\":153}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":199},\"start\":{\"modifier\":\"EXACT\",\"value\":174}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical; Name=TM2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":220},\"start\":{\"modifier\":\"EXACT\",\"value\":200}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":398},\"start\":{\"modifier\":\"EXACT\",\"value\":221}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical; Name=TM3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":419},\"start\":{\"modifier\":\"EXACT\",\"value\":399}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":442},\"start\":{\"modifier\":\"EXACT\",\"value\":420}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical; Name=TM4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":463},\"start\":{\"modifier\":\"EXACT\",\"value\":443}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":478},\"start\":{\"modifier\":\"EXACT\",\"value\":464}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical; Name=TM5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":499},\"start\":{\"modifier\":\"EXACT\",\"value\":479}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":525},\"start\":{\"modifier\":\"EXACT\",\"value\":500}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical; Name=TM6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":546},\"start\":{\"modifier\":\"EXACT\",\"value\":526}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":568},\"start\":{\"modifier\":\"EXACT\",\"value\":547}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"Helical; Name=TM7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":586},\"start\":{\"modifier\":\"EXACT\",\"value\":569}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":589},\"start\":{\"modifier\":\"EXACT\",\"value\":587}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"Helical; Name=TM8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":610},\"start\":{\"modifier\":\"EXACT\",\"value\":590}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":634},\"start\":{\"modifier\":\"EXACT\",\"value\":611}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"Helical; Name=TM9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":665},\"start\":{\"modifier\":\"EXACT\",\"value\":635}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":673},\"start\":{\"modifier\":\"EXACT\",\"value\":666}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"description\":\"Helical; Name=TM10\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":694},\"start\":{\"modifier\":\"EXACT\",\"value\":674}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/22",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C27",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":760},\"start\":{\"modifier\":\"EXACT\",\"value\":695}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/23",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6NP91.json)

```json
{
  "evidence_id": "C28",
  "excerpt": "{\"citation\":{\"authors\":[\"Li K.\",\"Guo Y.\",\"Wang Y.\",\"Zhu R.\",\"Chen W.\",\"Cheng T.\",\"Zhang X.\",\"Jia Y.\",\"Liu T.\",\"Zhang W.\",\"Jan L.Y.\",\"Jan Y.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38388853\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41556-024-01353-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"393\",\"id\":\"38388853\",\"journal\":\"Nat. Cell Biol.\",\"lastPage\":\"403\",\"publicationDate\":\"2024\",\"title\":\"Drosophila TMEM63 and mouse TMEM63A are lysosomal mechanosensory ion channels.\",\"volume\":\"26\"},\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:31:44.009321+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e32e7a44bd1e381c63270566272501cc8fa1b07bcb82b91922729646dc1da734",
  "url": "https://rest.uniprot.org/uniprotkb/Q6NP91.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H1",
  "excerpt": "ID   TM63_DROME              Reviewed;         760 AA.\nAC   Q6NP91;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 147.\nDE   RecName: Full=Mechanosensitive cation channel Tmem63 {ECO:0000305};\nDE   AltName: Full=Transmembrane protein 63 {ECO:0000305};\nDE            Short=DmTMEM63 {ECO:0000303|PubMed:38388853};\nGN   Name=Tmem63 {ECO:0000303|PubMed:33657409, ECO:0000312|FlyBase:FBgn0033259};\nGN   ORFNames=CG11210 {ECO:0000312|FlyBase:FBgn0033259};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H2",
  "excerpt": "RN   [5]\nRP   FUNCTION, TISSUE SPECIFICITY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=33657409; DOI=10.1016/j.cub.2021.02.007;\nRA   Li Q., Montell C.;\nRT   \"Mechanism for food texture preference based on grittiness.\";\nRL   Curr. Biol. 31:1850-1861(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H3",
  "excerpt": "RN   [7]\nRP   FUNCTION, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=38388853; DOI=10.1038/s41556-024-01353-7;\nRA   Li K., Guo Y., Wang Y., Zhu R., Chen W., Cheng T., Zhang X., Jia Y.,\nRA   Liu T., Zhang W., Jan L.Y., Jan Y.N.;\nRT   \"Drosophila TMEM63 and mouse TMEM63A are lysosomal mechanosensory ion\nRT   channels.\";\nRL   Nat. Cell Biol. 26:393-403(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        1..28\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 192-194",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        29..49\nFT                   /note=\"Helical; Name=TM0\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 195-197",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H6",
  "excerpt": "FT   TOPO_DOM        50..152\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 198-200",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        153..173\nFT                   /note=\"Helical; Name=TM1\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 201-203",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H8",
  "excerpt": "FT   TOPO_DOM        174..199\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 204-206",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        200..220\nFT                   /note=\"Helical; Name=TM2\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 207-209",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H10",
  "excerpt": "FT   TOPO_DOM        221..398\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 210-212",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        399..419\nFT                   /note=\"Helical; Name=TM3\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 213-215",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H12",
  "excerpt": "FT   TOPO_DOM        420..442\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 216-218",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        443..463\nFT                   /note=\"Helical; Name=TM4\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 219-221",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H14",
  "excerpt": "FT   TOPO_DOM        464..478\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 222-224",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H15",
  "excerpt": "FT   TRANSMEM        479..499\nFT                   /note=\"Helical; Name=TM5\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 225-227",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H16",
  "excerpt": "FT   TOPO_DOM        500..525\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 228-230",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H17",
  "excerpt": "FT   TRANSMEM        526..546\nFT                   /note=\"Helical; Name=TM6\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 231-233",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H18",
  "excerpt": "FT   TOPO_DOM        547..568\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 234-236",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H19",
  "excerpt": "FT   TRANSMEM        569..586\nFT                   /note=\"Helical; Name=TM7\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 237-239",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H20",
  "excerpt": "FT   TOPO_DOM        587..589\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 240-242",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H21",
  "excerpt": "FT   TRANSMEM        590..610\nFT                   /note=\"Helical; Name=TM8\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 243-245",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H22",
  "excerpt": "FT   TOPO_DOM        611..634\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 246-248",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H23",
  "excerpt": "FT   TRANSMEM        635..665\nFT                   /note=\"Helical; Name=TM9\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 249-251",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H24",
  "excerpt": "FT   TOPO_DOM        666..673\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 252-254",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H25",
  "excerpt": "FT   TRANSMEM        674..694\nFT                   /note=\"Helical; Name=TM10\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 255-257",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H26",
  "excerpt": "FT   TOPO_DOM        695..760\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.465310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 258-260",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "90e6f99e49624c57df9aa440e9ed4ff3cd0ca857729e891a296f80e977458c87",
  "url": "https://rest.uniprot.org/unisave/Q6NP91?format=txt&versions=147"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 101. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
