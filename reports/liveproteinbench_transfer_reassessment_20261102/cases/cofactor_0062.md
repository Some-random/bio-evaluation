# cofactor_0062

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0062.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPEGDTVFHTAAALRAALEGKTLTRCDVRVPRYATVDLSGAVVDEVLSRGKHLFIRAGSASIHSHLKMEGAWRIGHTKVAPHRIRIVLETADTRAIGIDLGILEVLDRGTDMDAVAYLGPDLLGPDWEPRVAADNLAADPDRPLAQALLDQRVMAGVGNVYCNELCFVFGRLPTAPVGTLKDPLRVVQRARDMLWLNRSRWNRTTTGDTRNGRQLWVYGRAGEPCRRCGTLIQTDRGGERVTYWCPVCQTAS

[Multiple Choices]
A. Na(+)
B. Fe cation
C. Zn(2+)
D. Cu(2+)
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

> The sequence-matched UniProt annotation identifies Zn(2+) and reports one zinc ion per subunit; a cited crystal structure is also described as being in complex with Zn(2+). This supports choice C as the protein’s cofactor, though binding evidence alone does not prove zinc is strictly essential for catalytic turnover.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The input sequence has a C-terminal Cys-rich pattern consistent with a Cys4 zinc-binding site. Such zinc-binding motifs occur in bacterial Nei/endonuclease VIII-family DNA repair enzymes. That family-level pattern makes Zn(2+) a meaningful choice over Na(+), Fe, or Cu among the offered alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A conserved-family and sequence-motif inference provides a concrete basis for selecting zinc without needing this exact protein’s database record. It is a strong inference, although the motif alone does not establish that zinc is essential for catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Cys-rich zinc-binding motif and the supplied sequence-matched cofactor annotation both favor Zn(2+); no other offered ion is comparably supported.


### Important caveats

- The source explicitly supports zinc binding/cofactor status, but the excerpts do not independently demonstrate that removing zinc abolishes catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The input sequence has a C-terminal Cys-rich pattern consistent with a Cys4 zinc-binding site. Such zinc-binding motifs occur in bacterial Nei/endonuclease VIII-family DNA repair enzymes. That family-level pattern makes Zn(2+) a meaningful choice over Na(+), Fe, or Cu among the offered alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A conserved-family and sequence-motif inference provides a concrete basis for selecting zinc without needing this exact protein’s database record. It is a strong inference, although the motif alone does not establish that zinc is essential for catalytic activity."
  },
  "case_id": "cofactor_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies Zn(2+) and reports one zinc ion per subunit; a cited crystal structure is also described as being in complex with Zn(2+). This supports choice C as the protein’s cofactor, though binding evidence alone does not prove zinc is strictly essential for catalytic turnover."
  },
  "important_caveats": [
    "The source explicitly supports zinc binding/cofactor status, but the excerpts do not independently demonstrate that removing zinc abolishes catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Cys-rich zinc-binding motif and the supplied sequence-matched cofactor annotation both favor Zn(2+); no other offered ion is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies Zn(2+) and reports one zinc ion per subunit; a cited crystal structure is also described as being in complex with Zn(2+). This supports choice C as the protein’s cofactor, though binding evidence alone does not prove zinc is strictly essential for catalytic turnover.",
    "evidence_ids": ["C5", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The input sequence has a C-terminal Cys-rich pattern consistent with a Cys4 zinc-binding site. Such zinc-binding motifs occur in bacterial Nei/endonuclease VIII-family DNA repair enzymes. That family-level pattern makes Zn(2+) a meaningful choice over Na(+), Fe, or Cu among the offered alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A conserved-family and sequence-motif inference provides a concrete basis for selecting zinc without needing this exact protein’s database record. It is a strong inference, although the motif alone does not establish that zinc is essential for catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Cys-rich zinc-binding motif and the supplied sequence-matched cofactor annotation both favor Zn(2+); no other offered ion is comparably supported."
  },
  "important_caveats": [
    "The source explicitly supports zinc binding/cofactor status, but the excerpts do not independently demonstrate that removing zinc abolishes catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0QT90 (END8B_MYCS2) explicitly annotates Zn(2+) as the cofactor with 'Binds 1 zinc ion per subunit,' supported by both PROSITE-ProRule computational evidence (PRU00391) and experimental evidence from PubMed:39012146 (X-ray crystallography at 1.45 Å in complex with Zn(2+), PDB:8TJG). The sequence matches the benchmark exactly (252 AA, SHA-256 confirmed). The protein is DNA-(apurinic or apyrimidinic site) lyase Nei2, an Endonuclease 8 family member.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region contains the motif 'CPVCQTAS' (Cys-Pro-Val-Cys), a classic zinc-coordination pattern found in many Zn-dependent enzymes. Additionally, the Endonuclease VIII (Nei) family of DNA repair enzymes is a well-characterized family known to require Zn(2+), in contrast to the related Endonuclease III (Nth) family which uses &#91;4Fe-4S&#93; clusters. The sequence lacks the canonical Fe-S cluster motif (Cys-X2-Cys-X45-Cys-X29-Cys) characteristic of Nth-family enzymes, arguing against Fe. Na(+) and Cu(2+) are not typical cofactors for DNA glycosylase/AP lyase enzymes. A model recognizing the Cys-rich zinc-binding pattern and the general architecture of DNA repair enzymes could meaningfully favor Zn(2+) over the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of the Endonuclease VIII family (Zn-dependent) versus Endonuclease III family (Fe-S-dependent), combined with the visible C-terminal CPVC zinc-binding motif and absence of Fe-S cluster motifs, provides a credible basis for selecting Zn(2+) over Fe, Na, and Cu without needing to recall this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Zn(2+) is the only well-supported cofactor for this enzyme class. Fe could theoretically be considered if one confused Nth and Nei families, but the sequence lacks Fe-S cluster motifs. Na(+) and Cu(2+) are implausible for DNA glycosylase/AP lyases.


### Important caveats

- The PROSITE-ProRule evidence (ECO:0000255) is computational/pattern-based, while PubMed:39012146 provides experimental X-ray crystallographic confirmation of Zn(2+) binding.
- The protein was only formally named and reviewed in 2025-2026; the family-level knowledge (Endonuclease VIII = Zn-dependent) predates this specific entry's annotation.
- The C-terminal CPVC motif is suggestive but not uniquely diagnostic of zinc; the family-level inference strengthens the argument.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains the motif 'CPVCQTAS' (Cys-Pro-Val-Cys), a classic zinc-coordination pattern found in many Zn-dependent enzymes. Additionally, the Endonuclease VIII (Nei) family of DNA repair enzymes is a well-characterized family known to require Zn(2+), in contrast to the related Endonuclease III (Nth) family which uses [4Fe-4S] clusters. The sequence lacks the canonical Fe-S cluster motif (Cys-X2-Cys-X45-Cys-X29-Cys) characteristic of Nth-family enzymes, arguing against Fe. Na(+) and Cu(2+) are not typical cofactors for DNA glycosylase/AP lyase enzymes. A model recognizing the Cys-rich zinc-binding pattern and the general architecture of DNA repair enzymes could meaningfully favor Zn(2+) over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of the Endonuclease VIII family (Zn-dependent) versus Endonuclease III family (Fe-S-dependent), combined with the visible C-terminal CPVC zinc-binding motif and absence of Fe-S cluster motifs, provides a credible basis for selecting Zn(2+) over Fe, Na, and Cu without needing to recall this specific protein's database annotation."
  },
  "case_id": "cofactor_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0QT90 (END8B_MYCS2) explicitly annotates Zn(2+) as the cofactor with 'Binds 1 zinc ion per subunit,' supported by both PROSITE-ProRule computational evidence (PRU00391) and experimental evidence from PubMed:39012146 (X-ray crystallography at 1.45 Å in complex with Zn(2+), PDB:8TJG). The sequence matches the benchmark exactly (252 AA, SHA-256 confirmed). The protein is DNA-(apurinic or apyrimidinic site) lyase Nei2, an Endonuclease 8 family member."
  },
  "important_caveats": [
    "The PROSITE-ProRule evidence (ECO:0000255) is computational/pattern-based, while PubMed:39012146 provides experimental X-ray crystallographic confirmation of Zn(2+) binding.",
    "The protein was only formally named and reviewed in 2025-2026; the family-level knowledge (Endonuclease VIII = Zn-dependent) predates this specific entry's annotation.",
    "The C-terminal CPVC motif is suggestive but not uniquely diagnostic of zinc; the family-level inference strengthens the argument."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Zn(2+) is the only well-supported cofactor for this enzyme class. Fe could theoretically be considered if one confused Nth and Nei families, but the sequence lacks Fe-S cluster motifs. Na(+) and Cu(2+) are implausible for DNA glycosylase/AP lyases."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0QT90 (END8B_MYCS2) explicitly annotates Zn(2+) as the cofactor with 'Binds 1 zinc ion per subunit,' supported by both PROSITE-ProRule computational evidence (PRU00391) and experimental evidence from PubMed:39012146 (X-ray crystallography at 1.45 Å in complex with Zn(2+), PDB:8TJG). The sequence matches the benchmark exactly (252 AA, SHA-256 confirmed). The protein is DNA-(apurinic or apyrimidinic site) lyase Nei2, an Endonuclease 8 family member.",
    "evidence_ids": ["C5", "C7", "H5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region contains the motif 'CPVCQTAS' (Cys-Pro-Val-Cys), a classic zinc-coordination pattern found in many Zn-dependent enzymes. Additionally, the Endonuclease VIII (Nei) family of DNA repair enzymes is a well-characterized family known to require Zn(2+), in contrast to the related Endonuclease III (Nth) family which uses [4Fe-4S] clusters. The sequence lacks the canonical Fe-S cluster motif (Cys-X2-Cys-X45-Cys-X29-Cys) characteristic of Nth-family enzymes, arguing against Fe. Na(+) and Cu(2+) are not typical cofactors for DNA glycosylase/AP lyase enzymes. A model recognizing the Cys-rich zinc-binding pattern and the general architecture of DNA repair enzymes could meaningfully favor Zn(2+) over the other three options.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of the Endonuclease VIII family (Zn-dependent) versus Endonuclease III family (Fe-S-dependent), combined with the visible C-terminal CPVC zinc-binding motif and absence of Fe-S cluster motifs, provides a credible basis for selecting Zn(2+) over Fe, Na, and Cu without needing to recall this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Zn(2+) is the only well-supported cofactor for this enzyme class. Fe could theoretically be considered if one confused Nth and Nei families, but the sequence lacks Fe-S cluster motifs. Na(+) and Cu(2+) are implausible for DNA glycosylase/AP lyases."
  },
  "important_caveats": [
    "The PROSITE-ProRule evidence (ECO:0000255) is computational/pattern-based, while PubMed:39012146 provides experimental X-ray crystallographic confirmation of Zn(2+) binding.",
    "The protein was only formally named and reviewed in 2025-2026; the family-level knowledge (Endonuclease VIII = Zn-dependent) predates this specific entry's annotation.",
    "The C-terminal CPVC motif is suggestive but not uniquely diagnostic of zinc; the family-level inference strengthens the argument."
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
  "benchmark_sequence_length": 252,
  "benchmark_sequence_sha256": "3219f396f539d267333a763309b8cbd0a0d2cd246ccaaaf6d27d6db63a93ffaa",
  "current_entry_audit": {
    "entryVersion": 142,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-01-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 252,
  "current_source_sequence_sha256": "3219f396f539d267333a763309b8cbd0a0d2cd246ccaaaf6d27d6db63a93ffaa",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 140,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0QT90",
  "selected_historical_entry_version": 140,
  "selected_historical_record_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "selected_historical_source_sequence_length": 252,
  "selected_historical_source_sequence_sha256": "3219f396f539d267333a763309b8cbd0a0d2cd246ccaaaf6d27d6db63a93ffaa",
  "selected_historical_version": {
    "accession": "A0QT90",
    "database": "Swiss-Prot",
    "entryVersion": 140,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "END8B_MYCS2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0QT90\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":142,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-01-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mycobacterium smegmatis\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Mycobacteriales\",\"Mycobacteriaceae\",\"Mycolicibacterium\"],\"scientificName\":\"Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155)\",\"taxonId\":246196}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WNC1\",\"source\":\"UniProtKB\"}],\"value\":\"Endonuclease 8 2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00392\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39012146\",\"source\":\"PubMed\"}],\"value\":\"3.2.2.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00392\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36610794\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39012146\",\"source\":\"PubMed\"}],\"value\":\"4.2.99.18\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36610794\",\"source\":\"PubMed\"}],\"value\":\"DNA-(apurinic or apyrimidinic site) lyase Nei2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36610794\",\"source\":\"PubMed\"}],\"value\":\"AP lyase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00391\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39012146\",\"source\":\"PubMed\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00391\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39012146\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 zinc ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Warren G.M.\",\"Ejaz A.\",\"Fay A.\",\"Glickman M.S.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36610794\"},{\"database\":\"DOI\",\"id\":\"10.1093/nar/gkac1222\"}],\"citationType\":\"journal article\",\"firstPage\":\"218\",\"id\":\"36610794\",\"journal\":\"Nucleic Acids Res.\",\"lastPage\":\"235\",\"publicationDate\":\"2023\",\"title\":\"Mycobacterial helicase Lhr abets resistance to DNA crosslinking agents mitomycin C and cisplatin.\",\"volume\":\"51\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700084 / mc(2)155\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PROBABLE ACTIVE SITE\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Warren G.M.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39012146\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.01248-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0124824\",\"id\":\"39012146\",\"journal\":\"MBio\",\"lastPage\":\"e0124824\",\"publicationDate\":\"2024\",\"title\":\"Structure and in vivo psoralen DNA crosslink repair activity of mycobacterial Nei2.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8TJG\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700084 / mc(2)155\"}],\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.45 ANGSTROMS) IN COMPLEX WITH ZN(2+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PROBABLE ACTIVE SITE\",\"COFACTOR\",\"SUBUNIT\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF PRO-2; GLU-3 AND LYS-51\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H1",
  "excerpt": "ID   END8B_MYCS2             Reviewed;         252 AA.\nAC   A0QT90; I7G4T3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-JAN-2007, sequence version 1.\nDT   28-JAN-2026, entry version 140.\nDE   RecName: Full=DNA-(apurinic or apyrimidinic site) lyase Nei2 {ECO:0000303|PubMed:36610794};\nDE            Short=AP lyase {ECO:0000303|PubMed:36610794};\nDE            EC=3.2.2.- {ECO:0000255|PROSITE-ProRule:PRU00392, ECO:0000269|PubMed:39012146};\nDE            EC=4.2.99.18 {ECO:0000255|PROSITE-ProRule:PRU00392, ECO:0000269|PubMed:36610794, ECO:0000269|PubMed:39012146};\nDE   AltName: Full=Endonuclease 8 2 {ECO:0000250|UniProtKB:P9WNC1};\nGN   Name=nei2 {ECO:0000303|PubMed:36610794};\nGN   OrderedLocusNames=MSMEG_1756 {ECO:0000312|EMBL:ABK74586.1};\nOS   Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155) (Mycobacterium\nOS   smegmatis).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales;\nOC   Mycobacteriaceae; Mycolicibacterium.\nOX   NCBI_TaxID=246196;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=DNA-(apurinic or apyrimidinic site) lyase Nei2 {ECO:0000303|PubMed:36610794};\nDE            Short=AP lyase {ECO:0000303|PubMed:36610794};\nDE            EC=3.2.2.- {ECO:0000255|PROSITE-ProRule:PRU00392, ECO:0000269|PubMed:39012146};\nDE            EC=4.2.99.18 {ECO:0000255|PROSITE-ProRule:PRU00392, ECO:0000269|PubMed:36610794, ECO:0000269|PubMed:39012146};\nDE   AltName: Full=Endonuclease 8 2 {ECO:0000250|UniProtKB:P9WNC1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, PROBABLE ACTIVE SITE, AND SUBUNIT.\nRC   STRAIN=ATCC 700084 / mc(2)155;\nRX   PubMed=36610794; DOI=10.1093/nar/gkac1222;\nRA   Warren G.M., Ejaz A., Fay A., Glickman M.S., Shuman S.;\nRT   \"Mycobacterial helicase Lhr abets resistance to DNA crosslinking agents\nRT   mitomycin C and cisplatin.\";\nRL   Nucleic Acids Res. 51:218-235(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H4",
  "excerpt": "RN   [5] {ECO:0007744|PDB:8TJG}\nRP   X-RAY CRYSTALLOGRAPHY (1.45 ANGSTROMS) IN COMPLEX WITH ZN(2+), FUNCTION,\nRP   CATALYTIC ACTIVITY, PROBABLE ACTIVE SITE, COFACTOR, SUBUNIT, DISRUPTION\nRP   PHENOTYPE, AND MUTAGENESIS OF PRO-2; GLU-3 AND LYS-51.\nRC   STRAIN=ATCC 700084 / mc(2)155;\nRX   PubMed=39012146; DOI=10.1128/mbio.01248-24;\nRA   Warren G.M., Shuman S.;\nRT   \"Structure and in vivo psoralen DNA crosslink repair activity of\nRT   mycobacterial Nei2.\";\nRL   MBio 15:e0124824-e0124824(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00391,\nCC         ECO:0000269|PubMed:39012146};\nCC       Note=Binds 1 zinc ion per subunit. {ECO:0000255|PROSITE-\nCC       ProRule:PRU00391, ECO:0000269|PubMed:39012146};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 62. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
