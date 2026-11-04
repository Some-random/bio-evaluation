# transmembrane_0038

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0038.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 7..27

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDSPTLLLFIFASIFYFITFQIVKLGFNVVMTSKKTKRRRLPLPPGPKPLPIIGNVLELGPKPHRSFANLAKVHGPLMSLRLGSVTTIIVSSSDVAKEMFLKNDQPLSSNRTIPNSVTAGDHHLLTMSWLPVSPKWRSFRKITTFHLLSPQRLDSCCSLRQAKVQQLFEYVLECSRTGQTVDIGKAAFTTSLNLLSKLFFSLELAHHRSSKSQEFKDLIWDIMEDIGKPNYADYFPCLKYFDPCGIRRRLANSFEKLIEVFQGIIRQRLSLSSGSDTHNDVLDVLLQLYKQKELSMDEINHLLVDIFDAGTDTTSSTFEWAMAELIKSPKTMEKAQAEIKLVLGKESHIQESDIPKLPYLRAIIKETLRLHPPTVFLLPRKAETDVELYGYTVPKNAQILVNLWALGRDPKVWENPDVFLPERFLTCDIDVKGRDFGLLPFGAGRRICPGMNLAYRMLTLMLATLLQSFDWKLPNELNPRNLDMDEKFGIALQKTKPLEIIPVCKD

[Multiple Choices]
A. 7..27; 278..300
B. 4..23
C. 7..27
D. 93..113; 163..183; 382..402; 425..445; 764..784
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

> The sequence-matched UniProt annotation identifies residues 7–27 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational annotation, not direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Residues near the N-terminus form a conspicuously hydrophobic stretch consistent with a membrane-spanning helix. Such N-terminal membrane anchors are also characteristic of many microsomal cytochrome P450s. Of the choices, C captures that stretch without adding a distant internal region as A does; D includes positions beyond the 506-residue sequence. C starts at the hydrophobic run, whereas B begins with Pro-Thr before it and omits its hydrophobic C-terminal extension.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The membrane-helix inference follows from the supplied sequence and transferable membrane-protein knowledge, rather than requiring the exact protein's database record. The precise helix boundaries are less certain than the presence of the N-terminal hydrophobic region.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both intervals overlap the prominent N-terminal hydrophobic stretch and could describe a membrane-spanning segment; their boundaries differ, and the sequence alone does not make the exact endpoints decisive.


### Important caveats

- The supplied annotation supports C but is computational, not experimental evidence.
- The original sequence provides strong evidence for a hydrophobic N-terminal helix, but exact transmembrane boundaries can vary by prediction method.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Residues near the N-terminus form a conspicuously hydrophobic stretch consistent with a membrane-spanning helix. Such N-terminal membrane anchors are also characteristic of many microsomal cytochrome P450s. Of the choices, C captures that stretch without adding a distant internal region as A does; D includes positions beyond the 506-residue sequence. C starts at the hydrophobic run, whereas B begins with Pro-Thr before it and omits its hydrophobic C-terminal extension.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The membrane-helix inference follows from the supplied sequence and transferable membrane-protein knowledge, rather than requiring the exact protein's database record. The precise helix boundaries are less certain than the presence of the N-terminal hydrophobic region."
  },
  "case_id": "transmembrane_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 7–27 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational annotation, not direct experimental confirmation."
  },
  "important_caveats": [
    "The supplied annotation supports C but is computational, not experimental evidence.",
    "The original sequence provides strong evidence for a hydrophobic N-terminal helix, but exact transmembrane boundaries can vary by prediction method."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both intervals overlap the prominent N-terminal hydrophobic stretch and could describe a membrane-spanning segment; their boundaries differ, and the sequence alone does not make the exact endpoints decisive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 7–27 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational annotation, not direct experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Residues near the N-terminus form a conspicuously hydrophobic stretch consistent with a membrane-spanning helix. Such N-terminal membrane anchors are also characteristic of many microsomal cytochrome P450s. Of the choices, C captures that stretch without adding a distant internal region as A does; D includes positions beyond the 506-residue sequence. C starts at the hydrophobic run, whereas B begins with Pro-Thr before it and omits its hydrophobic C-terminal extension.",
    "missing_item_specific_fact": "",
    "reason": "The membrane-helix inference follows from the supplied sequence and transferable membrane-protein knowledge, rather than requiring the exact protein's database record. The precise helix boundaries are less certain than the presence of the N-terminal hydrophobic region."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both intervals overlap the prominent N-terminal hydrophobic stretch and could describe a membrane-spanning segment; their boundaries differ, and the sequence alone does not make the exact endpoints decisive."
  },
  "important_caveats": [
    "The supplied annotation supports C but is computational, not experimental evidence.",
    "The original sequence provides strong evidence for a hydrophobic N-terminal helix, but exact transmembrane boundaries can vary by prediction method."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5/H3) records a single Transmembrane helix at 7..27 with evidence code ECO:0000255 (by similarity, i.e., computational transfer). The sequence at positions 7-27 (LLFIFASIFYFITFQIVKLGF) is predominantly hydrophobic and consistent with a single N-terminal TM anchor helix typical of cytochrome P450 enzymes. The annotation is computational rather than experimental, but the sequence itself supports a hydrophobic helix in this region, and the P450 family biology (single N-terminal TM helix anchoring to ER membrane) is consistent with this annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical P450 heme-binding motif FGAGRRICPG (~position 385-395), identifying it as a cytochrome P450. From family knowledge of P450 enzymes (transferable across hundreds of characterized P450s), these proteins possess exactly ONE N-terminal transmembrane helix that anchors them to the ER membrane; they do not have multiple TM segments in their catalytic domain. This eliminates option A (two TM regions) and option D (five TM regions, including position 764..784 which exceeds the 506-residue protein length). Between B (4..23) and C (7..27): position 4 is a proline (P), a well-known helix breaker that is atypical at the start of a TM helix, whereas position 7 begins with LLFIF — a clean hydrophobic stretch. The N-terminal residues MDSPTL (positions 1-6) contain charged/polar residues (D, S, P) consistent with a short cytoplasmic tail preceding the TM helix, supporting a helix start at position 7 rather than 4. This reasoning uses P450 family biology and general helix-structure principles learned from many other P450s.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the P450 heme-binding motif from the sequence can apply well-established family-level knowledge (single N-terminal TM helix) to eliminate multi-TM options, then use hydrophobicity and helix-breaking residue analysis to distinguish B from C. No fact specific to this exact protein beyond what is derivable from the sequence and P450 family biology is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D is eliminated by exceeding protein length. Option A is eliminated by P450 single-TM-helix biology. Option B is disfavored by the proline at position 4 (helix breaker) and inclusion of polar N-terminal residues in the helix. Option C is the most consistent with both sequence hydrophobicity and P450 family architecture.


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), meaning it is a computational transfer rather than experimental determination (e.g., no crystal structure or mutagenesis confirms the exact boundaries).
- The exact boundaries of TM helices are inherently approximate (±2-3 residues); the distinction between 4..23 and 7..27 relies on the helix-breaking proline and hydrophobicity gradient, which is a reasonable but not absolute discriminator.
- Option D contains a position (764..784) beyond the 506-residue protein length, making it trivially eliminable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif FGAGRRICPG (~position 385-395), identifying it as a cytochrome P450. From family knowledge of P450 enzymes (transferable across hundreds of characterized P450s), these proteins possess exactly ONE N-terminal transmembrane helix that anchors them to the ER membrane; they do not have multiple TM segments in their catalytic domain. This eliminates option A (two TM regions) and option D (five TM regions, including position 764..784 which exceeds the 506-residue protein length). Between B (4..23) and C (7..27): position 4 is a proline (P), a well-known helix breaker that is atypical at the start of a TM helix, whereas position 7 begins with LLFIF — a clean hydrophobic stretch. The N-terminal residues MDSPTL (positions 1-6) contain charged/polar residues (D, S, P) consistent with a short cytoplasmic tail preceding the TM helix, supporting a helix start at position 7 rather than 4. This reasoning uses P450 family biology and general helix-structure principles learned from many other P450s.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the P450 heme-binding motif from the sequence can apply well-established family-level knowledge (single N-terminal TM helix) to eliminate multi-TM options, then use hydrophobicity and helix-breaking residue analysis to distinguish B from C. No fact specific to this exact protein beyond what is derivable from the sequence and P450 family biology is needed."
  },
  "case_id": "transmembrane_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) records a single Transmembrane helix at 7..27 with evidence code ECO:0000255 (by similarity, i.e., computational transfer). The sequence at positions 7-27 (LLFIFASIFYFITFQIVKLGF) is predominantly hydrophobic and consistent with a single N-terminal TM anchor helix typical of cytochrome P450 enzymes. The annotation is computational rather than experimental, but the sequence itself supports a hydrophobic helix in this region, and the P450 family biology (single N-terminal TM helix anchoring to ER membrane) is consistent with this annotation."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), meaning it is a computational transfer rather than experimental determination (e.g., no crystal structure or mutagenesis confirms the exact boundaries).",
    "The exact boundaries of TM helices are inherently approximate (±2-3 residues); the distinction between 4..23 and 7..27 relies on the helix-breaking proline and hydrophobicity gradient, which is a reasonable but not absolute discriminator.",
    "Option D contains a position (764..784) beyond the 506-residue protein length, making it trivially eliminable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated by exceeding protein length. Option A is eliminated by P450 single-TM-helix biology. Option B is disfavored by the proline at position 4 (helix breaker) and inclusion of polar N-terminal residues in the helix. Option C is the most consistent with both sequence hydrophobicity and P450 family architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) records a single Transmembrane helix at 7..27 with evidence code ECO:0000255 (by similarity, i.e., computational transfer). The sequence at positions 7-27 (LLFIFASIFYFITFQIVKLGF) is predominantly hydrophobic and consistent with a single N-terminal TM anchor helix typical of cytochrome P450 enzymes. The annotation is computational rather than experimental, but the sequence itself supports a hydrophobic helix in this region, and the P450 family biology (single N-terminal TM helix anchoring to ER membrane) is consistent with this annotation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif FGAGRRICPG (~position 385-395), identifying it as a cytochrome P450. From family knowledge of P450 enzymes (transferable across hundreds of characterized P450s), these proteins possess exactly ONE N-terminal transmembrane helix that anchors them to the ER membrane; they do not have multiple TM segments in their catalytic domain. This eliminates option A (two TM regions) and option D (five TM regions, including position 764..784 which exceeds the 506-residue protein length). Between B (4..23) and C (7..27): position 4 is a proline (P), a well-known helix breaker that is atypical at the start of a TM helix, whereas position 7 begins with LLFIF — a clean hydrophobic stretch. The N-terminal residues MDSPTL (positions 1-6) contain charged/polar residues (D, S, P) consistent with a short cytoplasmic tail preceding the TM helix, supporting a helix start at position 7 rather than 4. This reasoning uses P450 family biology and general helix-structure principles learned from many other P450s.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the P450 heme-binding motif from the sequence can apply well-established family-level knowledge (single N-terminal TM helix) to eliminate multi-TM options, then use hydrophobicity and helix-breaking residue analysis to distinguish B from C. No fact specific to this exact protein beyond what is derivable from the sequence and P450 family biology is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated by exceeding protein length. Option A is eliminated by P450 single-TM-helix biology. Option B is disfavored by the proline at position 4 (helix breaker) and inclusion of polar N-terminal residues in the helix. Option C is the most consistent with both sequence hydrophobicity and P450 family architecture."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), meaning it is a computational transfer rather than experimental determination (e.g., no crystal structure or mutagenesis confirms the exact boundaries).",
    "The exact boundaries of TM helices are inherently approximate (±2-3 residues); the distinction between 4..23 and 7..27 relies on the helix-breaking proline and hydrophobicity gradient, which is a reasonable but not absolute discriminator.",
    "Option D contains a position (764..784) beyond the 506-residue protein length, making it trivially eliminable."
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
  "benchmark_sequence_length": 506,
  "benchmark_sequence_sha256": "cc59859fc141ed1a466ff7c8d0c595373164b54bfb54ba133c45fead91ba46c7",
  "current_entry_audit": {
    "entryVersion": 9,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-01-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "fa54283daa1d3049bcd1c62998404cfdbbdb36a1e0cef69f3e36d5f2c79ba7fe",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 506,
  "current_source_sequence_sha256": "cc59859fc141ed1a466ff7c8d0c595373164b54bfb54ba133c45fead91ba46c7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 8,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AA51VJB7",
  "selected_historical_entry_version": 8,
  "selected_historical_record_sha256": "2e43e41f0efa99bebb67f207b56375da2d0ad85b786f876cbbc5552e4beb3e4c",
  "selected_historical_source_sequence_length": 506,
  "selected_historical_source_sequence_sha256": "cc59859fc141ed1a466ff7c8d0c595373164b54bfb54ba133c45fead91ba46c7",
  "selected_historical_version": {
    "accession": "A0AA51VJB7",
    "database": "Swiss-Prot",
    "entryVersion": 8,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C7694_LOPWI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AA51VJB7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:22.946105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fa54283daa1d3049bcd1c62998404cfdbbdb36a1e0cef69f3e36d5f2c79ba7fe",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":9,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:22.946105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fa54283daa1d3049bcd1c62998404cfdbbdb36a1e0cef69f3e36d5f2c79ba7fe",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Peyote\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Cactineae\",\"Cactaceae\",\"Cactoideae\",\"Cacteae\",\"Lophophora\"],\"scientificName\":\"Lophophora williamsii\",\"synonyms\":[\"Echinocactus williamsii\"],\"taxonId\":130138}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:22.946105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fa54283daa1d3049bcd1c62998404cfdbbdb36a1e0cef69f3e36d5f2c79ba7fe",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase 76AD-1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"LwCYP76AD-1\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q94IP1\",\"source\":\"UniProtKB\"}],\"value\":\"1.14.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase 76AD94\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"LwCYP76AD94\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:22.946105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fa54283daa1d3049bcd1c62998404cfdbbdb36a1e0cef69f3e36d5f2c79ba7fe",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":27},\"start\":{\"modifier\":\"EXACT\",\"value\":7}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:26:22.946105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fa54283daa1d3049bcd1c62998404cfdbbdb36a1e0cef69f3e36d5f2c79ba7fe",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Watkins J.L.\",\"Li Q.\",\"Yeaman S.\",\"Facchini P.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37675639\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.16447\"}],\"citationType\":\"journal article\",\"firstPage\":\"635\",\"id\":\"37675639\",\"journal\":\"Plant J.\",\"lastPage\":\"649\",\"publicationDate\":\"2023\",\"title\":\"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora williamsii).\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WMX25291.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Jourdaniana\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:22.946105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fa54283daa1d3049bcd1c62998404cfdbbdb36a1e0cef69f3e36d5f2c79ba7fe",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VJB7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VJB7?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H1",
  "excerpt": "ID   C7694_LOPWI             Reviewed;         506 AA.\nAC   A0AA51VJB7;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2024, sequence version 1.\nDT   28-JAN-2026, entry version 8.\nDE   RecName: Full=Cytochrome P450 monooxygenase 76AD94 {ECO:0000303|PubMed:37675639};\nDE            Short=LwCYP76AD94 {ECO:0000303|PubMed:37675639};\nDE            EC=1.14.-.- {ECO:0000250|UniProtKB:Q94IP1};\nDE   AltName: Full=Cytochrome P450 monooxygenase 76AD-1 {ECO:0000303|PubMed:37675639};\nDE            Short=LwCYP76AD-1 {ECO:0000303|PubMed:37675639};\nGN   Name=CYP76AD94 {ECO:0000303|PubMed:37675639};\nGN   Synonyms=CYP76AD-1 {ECO:0000303|PubMed:37675639};\nOS   Lophophora williamsii (Peyote) (Echinocactus williamsii).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Cactineae; Cactaceae; Cactoideae; Cacteae; Lophophora.\nOX   NCBI_TaxID=130138;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.030705+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2e43e41f0efa99bebb67f207b56375da2d0ad85b786f876cbbc5552e4beb3e4c",
  "url": "https://rest.uniprot.org/unisave/A0AA51VJB7?format=txt&versions=8"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VJB7?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WMX25291.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   TISSUE SPECIFICITY.\nRC   STRAIN=cv. Jourdaniana;\nRX   PubMed=37675639; DOI=10.1111/tpj.16447;\nRA   Watkins J.L., Li Q., Yeaman S., Facchini P.J.;\nRT   \"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora\nRT   williamsii).\";\nRL   Plant J. 116:635-649(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.030705+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2e43e41f0efa99bebb67f207b56375da2d0ad85b786f876cbbc5552e4beb3e4c",
  "url": "https://rest.uniprot.org/unisave/A0AA51VJB7?format=txt&versions=8"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VJB7?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        7..27\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.030705+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2e43e41f0efa99bebb67f207b56375da2d0ad85b786f876cbbc5552e4beb3e4c",
  "url": "https://rest.uniprot.org/unisave/A0AA51VJB7?format=txt&versions=8"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
