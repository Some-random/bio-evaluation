# active_site_0025

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0025.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 121 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQFNSLVLLAGATILSPFVQAQTWTTCNPLNETCPNDPALGTNHTFVFNTSSTVTDYYNITAGSLTYGDDGAEFTIAKQGQSPTIQSKFYIFFGQVSVIMKAATGVGIVSSIVLESDDLDEIDWEFIGGNDTHAETNYFGKGNTTSYDRAIWYPTPSDPTANFHNYTVDWTAERVQWWIDDSLVRTLAYADAVDGKNFPQTPMTVRLGIWSGGDPKGNSQGTIEWAGGETDFTKVPFTMYVKSAAVQDYSTGSEYEWTDKTGDWTSIKVISGNSTVAETITKNETPTLSLGEKWDNLPKTTKLAVYCGGGAAVAALVSAFLFTFLRQRRNGRLEREAYNQLIEKQQQDAYKDQMELHNKGIGGFDNNSYATQGDDALGGWGSNQGTGYVGPSGSASAMASGSPMVQAGQHGPMSPTMVMRNGEMSPHSAEFPQPQQPMFGGSANGGSYMKM

[Multiple Choices]
A. Position 8 (Nucleophile)
B. Position 121 (Nucleophile)
C. Position 255 (Proton acceptor)
D. Position 1211 (Proton donor; for dehydratase activity)
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

> The sequence-matched UniProt annotation identifies position 121 as the nucleophile, supporting choice B. Its evidence cites a publication; this is curator-annotated evidence, not an independently reviewed primary-paper result here.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an E-X-D-X-E motif at positions 121–125. This is a conserved catalytic motif in GH16 glycoside hydrolase-family enzymes, with the first glutamate serving as the nucleophile. That pattern supports position 121; position 8 lies in the hydrophobic N-terminal signal region, and position 1211 is beyond the 451-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level motif knowledge provides a credible way to distinguish B from the offered alternatives without knowing this protein’s recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The conserved catalytic motif supports the keyed residue and the other options do not offer a comparably plausible nucleophile.


### Important caveats

- The reviewer-only annotation is sequence-matched, but its cited evidence is not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an E-X-D-X-E motif at positions 121–125. This is a conserved catalytic motif in GH16 glycoside hydrolase-family enzymes, with the first glutamate serving as the nucleophile. That pattern supports position 121; position 8 lies in the hydrophobic N-terminal signal region, and position 1211 is beyond the 451-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level motif knowledge provides a credible way to distinguish B from the offered alternatives without knowing this protein’s recorded annotation."
  },
  "case_id": "active_site_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 121 as the nucleophile, supporting choice B. Its evidence cites a publication; this is curator-annotated evidence, not an independently reviewed primary-paper result here."
  },
  "important_caveats": [
    "The reviewer-only annotation is sequence-matched, but its cited evidence is not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved catalytic motif supports the keyed residue and the other options do not offer a comparably plausible nucleophile."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 121 as the nucleophile, supporting choice B. Its evidence cites a publication; this is curator-annotated evidence, not an independently reviewed primary-paper result here.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an E-X-D-X-E motif at positions 121–125. This is a conserved catalytic motif in GH16 glycoside hydrolase-family enzymes, with the first glutamate serving as the nucleophile. That pattern supports position 121; position 8 lies in the hydrophobic N-terminal signal region, and position 1211 is beyond the 451-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level motif knowledge provides a credible way to distinguish B from the offered alternatives without knowing this protein’s recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved catalytic motif supports the keyed residue and the other options do not offer a comparably plausible nucleophile."
  },
  "important_caveats": [
    "The reviewer-only annotation is sequence-matched, but its cited evidence is not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (evidence ECO:0000305, from experimental study PubMed:33846308) explicitly annotates position 121 as 'Nucleophile' (Active site). Position 121 in the supplied 451-residue sequence is E (Glutamic acid), a chemically plausible nucleophilic residue. The companion annotation at position 125 (E) as 'Proton donor' is consistent with a DXE/DXXDXDXE-type catalytic arrangement in a glycoside hydrolase/transglycosylase. The evidence applies directly to the supplied sequence (sequence SHA-256 matches).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can eliminate three of four options using general reasoning and family-level transfer. (1) Option D (position 1211) is impossible because the sequence is only 451 residues long. (2) Option A (position 8) falls within the N-terminal signal peptide (MQFNSLVLLA…), and position 8 is L (Leucine), which is not a catalytic residue. (3) Option C (position 255, Proton acceptor) is Y (Tyrosine), which is not a typical proton acceptor in glycosidases. For option B, the sequence around positions 117–125 reads DDLD-E-IDW-E, which is recognizable as a variant of the DXXDXDXE catalytic motif characteristic of GH18 glycoside hydrolases/chitinases. In this motif family, the terminal Glu is the proton donor and an earlier Glu/Asp can serve as the nucleophile (or participate in substrate-assisted catalysis). A model trained on GH18 and related transglycosylase families would identify E121 as the nucleophilic glutamate within this motif, distinguishing B from the remaining option C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH18 DXXDXDXE motif is well-established family-level knowledge learned from many chitinases and transglycosylases. Recognizing this motif in the supplied sequence, combined with elimination of position-8 (signal-peptide Leu), position-1211 (out of range), and position-255 (Tyr, not a proton acceptor), provides a concrete transferable inference that meaningfully distinguishes option B from the alternatives without requiring recall of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (Leu in signal peptide), C (Tyr as proton acceptor, inconsistent with the actual E125 proton donor), and D (position beyond sequence length) are all clearly eliminated. Only B is consistent with both the sequence chemistry and the GH18-family motif context.


### Important caveats

- The nucleophile annotation at E121 is supported by experimental evidence (ECO:0000305) from the 2021 Nat. Commun. paper on Crh1/Crh2 transglycosylase activity, not merely by computational transfer.
- In canonical GH18 chitinases the nucleophile is the substrate's C2-acetamido group (substrate-assisted catalysis); the identification of E121 as a protein-level nucleophile reflects a mechanistic feature specific to this transglycosylase subclass, which a model would need family-level knowledge of Crh-type enzymes or related transglycosylases to appreciate.
- The reviewer-only evidence confirms the UniProt accession and annotation but was not available to the evaluated model; the answerability judgment relies on what a model could infer from the sequence and general knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate three of four options using general reasoning and family-level transfer. (1) Option D (position 1211) is impossible because the sequence is only 451 residues long. (2) Option A (position 8) falls within the N-terminal signal peptide (MQFNSLVLLA…), and position 8 is L (Leucine), which is not a catalytic residue. (3) Option C (position 255, Proton acceptor) is Y (Tyrosine), which is not a typical proton acceptor in glycosidases. For option B, the sequence around positions 117–125 reads DDLD-E-IDW-E, which is recognizable as a variant of the DXXDXDXE catalytic motif characteristic of GH18 glycoside hydrolases/chitinases. In this motif family, the terminal Glu is the proton donor and an earlier Glu/Asp can serve as the nucleophile (or participate in substrate-assisted catalysis). A model trained on GH18 and related transglycosylase families would identify E121 as the nucleophilic glutamate within this motif, distinguishing B from the remaining option C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH18 DXXDXDXE motif is well-established family-level knowledge learned from many chitinases and transglycosylases. Recognizing this motif in the supplied sequence, combined with elimination of position-8 (signal-peptide Leu), position-1211 (out of range), and position-255 (Tyr, not a proton acceptor), provides a concrete transferable inference that meaningfully distinguishes option B from the alternatives without requiring recall of this specific protein's database annotation."
  },
  "case_id": "active_site_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (evidence ECO:0000305, from experimental study PubMed:33846308) explicitly annotates position 121 as 'Nucleophile' (Active site). Position 121 in the supplied 451-residue sequence is E (Glutamic acid), a chemically plausible nucleophilic residue. The companion annotation at position 125 (E) as 'Proton donor' is consistent with a DXE/DXXDXDXE-type catalytic arrangement in a glycoside hydrolase/transglycosylase. The evidence applies directly to the supplied sequence (sequence SHA-256 matches)."
  },
  "important_caveats": [
    "The nucleophile annotation at E121 is supported by experimental evidence (ECO:0000305) from the 2021 Nat. Commun. paper on Crh1/Crh2 transglycosylase activity, not merely by computational transfer.",
    "In canonical GH18 chitinases the nucleophile is the substrate's C2-acetamido group (substrate-assisted catalysis); the identification of E121 as a protein-level nucleophile reflects a mechanistic feature specific to this transglycosylase subclass, which a model would need family-level knowledge of Crh-type enzymes or related transglycosylases to appreciate.",
    "The reviewer-only evidence confirms the UniProt accession and annotation but was not available to the evaluated model; the answerability judgment relies on what a model could infer from the sequence and general knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (Leu in signal peptide), C (Tyr as proton acceptor, inconsistent with the actual E125 proton donor), and D (position beyond sequence length) are all clearly eliminated. Only B is consistent with both the sequence chemistry and the GH18-family motif context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (evidence ECO:0000305, from experimental study PubMed:33846308) explicitly annotates position 121 as 'Nucleophile' (Active site). Position 121 in the supplied 451-residue sequence is E (Glutamic acid), a chemically plausible nucleophilic residue. The companion annotation at position 125 (E) as 'Proton donor' is consistent with a DXE/DXXDXDXE-type catalytic arrangement in a glycoside hydrolase/transglycosylase. The evidence applies directly to the supplied sequence (sequence SHA-256 matches).",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can eliminate three of four options using general reasoning and family-level transfer. (1) Option D (position 1211) is impossible because the sequence is only 451 residues long. (2) Option A (position 8) falls within the N-terminal signal peptide (MQFNSLVLLA…), and position 8 is L (Leucine), which is not a catalytic residue. (3) Option C (position 255, Proton acceptor) is Y (Tyrosine), which is not a typical proton acceptor in glycosidases. For option B, the sequence around positions 117–125 reads DDLD-E-IDW-E, which is recognizable as a variant of the DXXDXDXE catalytic motif characteristic of GH18 glycoside hydrolases/chitinases. In this motif family, the terminal Glu is the proton donor and an earlier Glu/Asp can serve as the nucleophile (or participate in substrate-assisted catalysis). A model trained on GH18 and related transglycosylase families would identify E121 as the nucleophilic glutamate within this motif, distinguishing B from the remaining option C.",
    "missing_item_specific_fact": "",
    "reason": "The GH18 DXXDXDXE motif is well-established family-level knowledge learned from many chitinases and transglycosylases. Recognizing this motif in the supplied sequence, combined with elimination of position-8 (signal-peptide Leu), position-1211 (out of range), and position-255 (Tyr, not a proton acceptor), provides a concrete transferable inference that meaningfully distinguishes option B from the alternatives without requiring recall of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (Leu in signal peptide), C (Tyr as proton acceptor, inconsistent with the actual E125 proton donor), and D (position beyond sequence length) are all clearly eliminated. Only B is consistent with both the sequence chemistry and the GH18-family motif context."
  },
  "important_caveats": [
    "The nucleophile annotation at E121 is supported by experimental evidence (ECO:0000305) from the 2021 Nat. Commun. paper on Crh1/Crh2 transglycosylase activity, not merely by computational transfer.",
    "In canonical GH18 chitinases the nucleophile is the substrate's C2-acetamido group (substrate-assisted catalysis); the identification of E121 as a protein-level nucleophile reflects a mechanistic feature specific to this transglycosylase subclass, which a model would need family-level knowledge of Crh-type enzymes or related transglycosylases to appreciate.",
    "The reviewer-only evidence confirms the UniProt accession and annotation but was not available to the evaluated model; the answerability judgment relies on what a model could infer from the sequence and general knowledge."
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
  "benchmark_sequence_length": 451,
  "benchmark_sequence_sha256": "b2c7f26714823706db7d5e7c3de974df2078007c1948a7f982df6ba305ede9bd",
  "current_entry_audit": {
    "entryVersion": 29,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 451,
  "current_source_sequence_sha256": "b2c7f26714823706db7d5e7c3de974df2078007c1948a7f982df6ba305ede9bd",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 27,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384K4T0",
  "selected_historical_entry_version": 27,
  "selected_historical_record_sha256": "864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f",
  "selected_historical_source_sequence_length": 451,
  "selected_historical_source_sequence_sha256": "b2c7f26714823706db7d5e7c3de974df2078007c1948a7f982df6ba305ede9bd",
  "selected_historical_version": {
    "accession": "A0A384K4T0",
    "database": "Swiss-Prot",
    "entryVersion": 27,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH2_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384K4T0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":29,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitinase crh2\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitin transglycosylase crh2\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":121},\"start\":{\"modifier\":\"EXACT\",\"value\":121}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":125},\"start\":{\"modifier\":\"EXACT\",\"value\":125}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":125},\"start\":{\"modifier\":\"EXACT\",\"value\":125}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":206},\"start\":{\"modifier\":\"EXACT\",\"value\":206}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":210},\"start\":{\"modifier\":\"EXACT\",\"value\":210}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":222},\"start\":{\"modifier\":\"EXACT\",\"value\":222}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Bi K.\",\"Scalschi L.\",\"Jaiswal N.\",\"Mengiste T.\",\"Fried R.\",\"Sanz A.B.\",\"Arroyo J.\",\"Zhu W.\",\"Masrati G.\",\"Sharon A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33846308\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-021-22436-1\"}],\"citationType\":\"journal article\",\"firstPage\":\"2166\",\"id\":\"33846308\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2166\",\"publicationDate\":\"2021\",\"title\":\"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.\",\"volume\":\"12\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"INTERACTION WITH CRH1 AND CRH3\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:24:45.289455+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K4T0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H1",
  "excerpt": "ID   CRH2_BOTFB              Reviewed;         451 AA.\nAC   A0A384K4T0;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 27.\nDE   RecName: Full=Crh-like protein 2 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh2 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh2 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\nGN   Name=crh2 {ECO:0000303|PubMed:33846308}; ORFNames=BCIN_15g03070;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:27.918229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f",
  "url": "https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, SUBUNIT, AND INTERACTION WITH CRH1 AND CRH3.\nRX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;\nRA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,\nRA   Arroyo J., Zhu W., Masrati G., Sharon A.;\nRT   \"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector\nRT   triggering plant cell death and defense response.\";\nRL   Nat. Commun. 12:2166-2166(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:27.918229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f",
  "url": "https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        121\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000305|PubMed:33846308\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:27.918229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 135-137",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f",
  "url": "https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        125\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000305|PubMed:33846308\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:27.918229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 138-140",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f",
  "url": "https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         125\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:27.918229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 141-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f",
  "url": "https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         206\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:27.918229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-148",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f",
  "url": "https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         210\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:27.918229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 149-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f",
  "url": "https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         222\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:27.918229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f",
  "url": "https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
