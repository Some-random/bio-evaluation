# active_site_0110

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0110.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 308 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | Unusable review | Unusable review |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASTTNGVNGHKASQPQSLIQTLNNIGADSFSNDGERIQAVLAAYALVSRLETPWEFVARTCMGQPALGAALKVAKDLKLYDKWHELGDGEMTCEQLSELVSCDSALLFRILRHLAANHVLEETSIGVFKPTKLSISFTVPVFGEWINHLYDATTPCFFKMPEFLAQNGYKNPVDPNNGVFQAAKGWKGDMFDYYKSHPVEGASFDHVMGGVMANQAGWLEIFPHNKLLETADAQSPLVVDVGGNIGHDIERFRQEHPETASRLYLEDLPEVVKRSKCPDDVNKVGYDFFTPQPIKGARAYYMHGVLHDWSEEPARKILEMQKEAMKPGYSTLLIHDHIAPESLAHPHTTAYDLTMMVMVAGVERREAHWRALLKSAGYKLVRIWRSPLAVQGVIEAELDQ

[Multiple Choices]
A. Position 308 (Proton acceptor)
B. Position 318 (For beta-ketoacyl synthase activity)
C. Position 95 (Nucleophile)
D. Position 2688 (Proton acceptor; for dehydratase activity 2)
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

> The matched-sequence UniProt record annotates residue 308 as a proton acceptor, both in the current entry and in the archived entry. This is computational support from a PROSITE rule, not direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a pattern consistent with a SAM-dependent O-methyltransferase, including a glycine-rich region around residues 241–250. Transferable knowledge of this enzyme family makes an acidic catalytic base plausible; residue 308 is Asp in the sequence and is a credible proton acceptor. The beta-ketoacyl synthase alternative is inconsistent with that family-level inference, and position 2688 is beyond the 401-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family and sequence-pattern knowledge offer a meaningful basis for selecting A among these choices, though they do not independently prove the specific catalytic assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported by the sequence and the transferable enzyme-family inference.


### Important caveats

- The source annotation is computationally inferred, rather than established by experimental evidence in the supplied excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a pattern consistent with a SAM-dependent O-methyltransferase, including a glycine-rich region around residues 241–250. Transferable knowledge of this enzyme family makes an acidic catalytic base plausible; residue 308 is Asp in the sequence and is a credible proton acceptor. The beta-ketoacyl synthase alternative is inconsistent with that family-level inference, and position 2688 is beyond the 401-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family and sequence-pattern knowledge offer a meaningful basis for selecting A among these choices, though they do not independently prove the specific catalytic assignment."
  },
  "case_id": "active_site_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates residue 308 as a proton acceptor, both in the current entry and in the archived entry. This is computational support from a PROSITE rule, not direct experimental confirmation."
  },
  "important_caveats": [
    "The source annotation is computationally inferred, rather than established by experimental evidence in the supplied excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence and the transferable enzyme-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates residue 308 as a proton acceptor, both in the current entry and in the archived entry. This is computational support from a PROSITE rule, not direct experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a pattern consistent with a SAM-dependent O-methyltransferase, including a glycine-rich region around residues 241–250. Transferable knowledge of this enzyme family makes an acidic catalytic base plausible; residue 308 is Asp in the sequence and is a credible proton acceptor. The beta-ketoacyl synthase alternative is inconsistent with that family-level inference, and position 2688 is beyond the 401-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family and sequence-pattern knowledge offer a meaningful basis for selecting A among these choices, though they do not independently prove the specific catalytic assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence and the transferable enzyme-family inference."
  },
  "important_caveats": [
    "The source annotation is computationally inferred, rather than established by experimental evidence in the supplied excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

No visible final review text was saved. Internal model reasoning is not a substitute for a visible review and is not published. The final-content extraction failed because the saved final content was not text.

**Saved parsed visible review:** `null`.

**Saved visible final text:** empty string (`""`).

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 401,
  "benchmark_sequence_sha256": "6cfc09707733a1f9780ef66f5d2b1f440e910de12814b5aee6608c39d7f1d918",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "951c9805e3f5495465fa2073e5dc93713a74fafc14f052798e02ea80ac79b432",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 401,
  "current_source_sequence_sha256": "6cfc09707733a1f9780ef66f5d2b1f440e910de12814b5aee6608c39d7f1d918",
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
  "requested_accession": "P9WEG4",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "ab50f7c37654fa60bf5b1d59b32a4688ea73cf2b9ee5ef208bcd560c1a433116",
  "selected_historical_source_sequence_length": 401,
  "selected_historical_source_sequence_sha256": "6cfc09707733a1f9780ef66f5d2b1f440e910de12814b5aee6608c39d7f1d918",
  "selected_historical_version": {
    "accession": "P9WEG4",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFME_ANNMO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEG4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:13.696495+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "951c9805e3f5495465fa2073e5dc93713a74fafc14f052798e02ea80ac79b432",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:13.696495+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "951c9805e3f5495465fa2073e5dc93713a74fafc14f052798e02ea80ac79b432",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Xylariomycetidae\",\"Xylariales\",\"Hypoxylaceae\",\"Annulohypoxylon\"],\"scientificName\":\"Annulohypoxylon moriforme\",\"synonyms\":[\"Hypoxylon moriforme\"],\"taxonId\":326622}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:13.696495+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "951c9805e3f5495465fa2073e5dc93713a74fafc14f052798e02ea80ac79b432",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"11'-O-desmethylfendlerol biosynthesis cluster protein E\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase mfmE\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:13.696495+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "951c9805e3f5495465fa2073e5dc93713a74fafc14f052798e02ea80ac79b432",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":308},\"start\":{\"modifier\":\"EXACT\",\"value\":308}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:30:13.696495+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "951c9805e3f5495465fa2073e5dc93713a74fafc14f052798e02ea80ac79b432",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O04385\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":244},\"start\":{\"modifier\":\"EXACT\",\"value\":243}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:30:13.696495+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "951c9805e3f5495465fa2073e5dc93713a74fafc14f052798e02ea80ac79b432",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":268},\"start\":{\"modifier\":\"EXACT\",\"value\":268}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:30:13.696495+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "951c9805e3f5495465fa2073e5dc93713a74fafc14f052798e02ea80ac79b432",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan D.\",\"Matsuda Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38404388\"},{\"database\":\"DOI\",\"id\":\"10.1039/d3sc06001b\"}],\"citationType\":\"journal article\",\"firstPage\":\"3011\",\"id\":\"38404388\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"3017\",\"publicationDate\":\"2024\",\"title\":\"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CBS 123579\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:13.696495+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "951c9805e3f5495465fa2073e5dc93713a74fafc14f052798e02ea80ac79b432",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG4?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   MFME_ANNMO              Reviewed;         401 AA.\nAC   P9WEG4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=O-methyltransferase mfmE {ECO:0000303|PubMed:38404388};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:38404388};\nDE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein E {ECO:0000303|PubMed:38404388};\nGN   Name=mfmE {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_462788;\nOS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.\nOX   NCBI_TaxID=326622;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:15.434880+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab50f7c37654fa60bf5b1d59b32a4688ea73cf2b9ee5ef208bcd560c1a433116",
  "url": "https://rest.uniprot.org/unisave/P9WEG4?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG4?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   STRAIN=CBS 123579;\nRX   PubMed=38404388; DOI=10.1039/d3sc06001b;\nRA   Yan D., Matsuda Y.;\nRT   \"Global genome mining-driven discovery of an unusual biosynthetic logic for\nRT   fungal polyketide-terpenoid hybrids.\";\nRL   Chem. Sci. 15:3011-3017(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:15.434880+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab50f7c37654fa60bf5b1d59b32a4688ea73cf2b9ee5ef208bcd560c1a433116",
  "url": "https://rest.uniprot.org/unisave/P9WEG4?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG4?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        308\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:15.434880+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab50f7c37654fa60bf5b1d59b32a4688ea73cf2b9ee5ef208bcd560c1a433116",
  "url": "https://rest.uniprot.org/unisave/P9WEG4?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG4?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         243..244\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O04385\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:15.434880+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab50f7c37654fa60bf5b1d59b32a4688ea73cf2b9ee5ef208bcd560c1a433116",
  "url": "https://rest.uniprot.org/unisave/P9WEG4?format=txt&versions=3"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG4?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         268\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:15.434880+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab50f7c37654fa60bf5b1d59b32a4688ea73cf2b9ee5ef208bcd560c1a433116",
  "url": "https://rest.uniprot.org/unisave/P9WEG4?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 110. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
