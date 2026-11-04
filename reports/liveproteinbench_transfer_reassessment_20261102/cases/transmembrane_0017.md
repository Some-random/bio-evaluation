# transmembrane_0017

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0017.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 305..325

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
A. 305..325; 704..727
B. 301..328
C. 305..325
D. 483..503
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

> The exact-match UniProt record annotates residues 305–325 as a helical transmembrane region. This is computational annotation (ECO:0000255), not evidence of experimental validation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Residues 305–325 are a strongly hydrophobic stretch (AVYCGGGAAVAALVSAFLFTF), consistent with a membrane-spanning helix. The neighboring residues included by B contain more polar or charged flanks, making C the better match for the crossing region. The other choices include positions beyond the 451-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence-based knowledge of transmembrane helices gives a meaningful basis for choosing C over the offered alternatives, although sequence inspection alone cannot establish exact membrane boundaries with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B overlaps the hydrophobic core but includes flanking residues less consistent with the crossing segment; C is the better-supported boundary choice among the offered options.


### Important caveats

- The supplied evidence supports a database annotation for this matched sequence, but the annotation is computational rather than experimental.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Residues 305–325 are a strongly hydrophobic stretch (AVYCGGGAAVAALVSAFLFTF), consistent with a membrane-spanning helix. The neighboring residues included by B contain more polar or charged flanks, making C the better match for the crossing region. The other choices include positions beyond the 451-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-based knowledge of transmembrane helices gives a meaningful basis for choosing C over the offered alternatives, although sequence inspection alone cannot establish exact membrane boundaries with certainty."
  },
  "case_id": "transmembrane_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-match UniProt record annotates residues 305–325 as a helical transmembrane region. This is computational annotation (ECO:0000255), not evidence of experimental validation."
  },
  "important_caveats": [
    "The supplied evidence supports a database annotation for this matched sequence, but the annotation is computational rather than experimental."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B overlaps the hydrophobic core but includes flanking residues less consistent with the crossing segment; C is the better-supported boundary choice among the offered options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-match UniProt record annotates residues 305–325 as a helical transmembrane region. This is computational annotation (ECO:0000255), not evidence of experimental validation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Residues 305–325 are a strongly hydrophobic stretch (AVYCGGGAAVAALVSAFLFTF), consistent with a membrane-spanning helix. The neighboring residues included by B contain more polar or charged flanks, making C the better match for the crossing region. The other choices include positions beyond the 451-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-based knowledge of transmembrane helices gives a meaningful basis for choosing C over the offered alternatives, although sequence inspection alone cannot establish exact membrane boundaries with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B overlaps the hydrophobic core but includes flanking residues less consistent with the crossing segment; C is the better-supported boundary choice among the offered options."
  },
  "important_caveats": [
    "The supplied evidence supports a database annotation for this matched sequence, but the annotation is computational rather than experimental."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A384K4T0 annotates a transmembrane helix at positions 305..325 (evidence code ECO:0000255, rule-based computational prediction). The sequence segment at 305-325 (VYCGGGAAVAALVSAFLFTF) is the hydrophobic core of a C-terminal TM anchor region. Choices A and D reference positions (704-727, 483-503) that exceed the 451-residue protein length, making them impossible. Choice B (301-328) includes charged residues K (pos 302) and R (pos 327) incompatible with TM helix criteria. The annotation supports C as the correct boundary.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can eliminate choices A and D by noting the protein is 451 residues long, making positions 483-503 and 704-727 out of range. Between B (301..328) and C (305..325), standard transmembrane helix criteria exclude charged residues from the hydrophobic core. Position 302 is lysine (K, positively charged) and position 327 is arginine (R, positively charged), both clearly incompatible with a TM helix segment. Choice B therefore includes charged boundary residues that violate the hydrophobic requirement of a ~20-residue TM alpha-helix. Choice C (305-325) captures the hydrophobic core (V, A, V, A, A, L, V, A, F, L, F, F) without charged residues. This is a well-established, transferable principle of membrane protein biology applicable to any TM prediction task.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The discrimination relies on (1) checking protein length against offered coordinates (eliminates A, D) and (2) applying the universal rule that TM helices exclude charged residues from their hydrophobic core (eliminates B in favor of C). Both are standard, transferable knowledge about transmembrane protein architecture, not specific to this protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A and D are eliminated by out-of-range positions. Choice B is eliminated by inclusion of charged residues (K, R) incompatible with TM helix criteria. Choice C is the only option consistent with both the protein length and hydrophobic TM helix requirements. No genuine ambiguity remains among the offered alternatives.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (rule-based/computational), not experimental data. Exact TM boundaries can vary between prediction algorithms.
- The segment 305-325 contains some polar residues (Y, C, G, S, T) that make it a borderline TM helix, but it is still the best hydrophobic stretch available and consistent with the known C-terminal TM anchor architecture of Crh-family chitin transglycosylases.
- The reviewer-only evidence confirms the annotation matches the supplied sequence (451 AA, SHA256 match), but the model was not given the protein identity or UniProt accession.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate choices A and D by noting the protein is 451 residues long, making positions 483-503 and 704-727 out of range. Between B (301..328) and C (305..325), standard transmembrane helix criteria exclude charged residues from the hydrophobic core. Position 302 is lysine (K, positively charged) and position 327 is arginine (R, positively charged), both clearly incompatible with a TM helix segment. Choice B therefore includes charged boundary residues that violate the hydrophobic requirement of a ~20-residue TM alpha-helix. Choice C (305-325) captures the hydrophobic core (V, A, V, A, A, L, V, A, F, L, F, F) without charged residues. This is a well-established, transferable principle of membrane protein biology applicable to any TM prediction task.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The discrimination relies on (1) checking protein length against offered coordinates (eliminates A, D) and (2) applying the universal rule that TM helices exclude charged residues from their hydrophobic core (eliminates B in favor of C). Both are standard, transferable knowledge about transmembrane protein architecture, not specific to this protein's database entry."
  },
  "case_id": "transmembrane_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A384K4T0 annotates a transmembrane helix at positions 305..325 (evidence code ECO:0000255, rule-based computational prediction). The sequence segment at 305-325 (VYCGGGAAVAALVSAFLFTF) is the hydrophobic core of a C-terminal TM anchor region. Choices A and D reference positions (704-727, 483-503) that exceed the 451-residue protein length, making them impossible. Choice B (301-328) includes charged residues K (pos 302) and R (pos 327) incompatible with TM helix criteria. The annotation supports C as the correct boundary."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (rule-based/computational), not experimental data. Exact TM boundaries can vary between prediction algorithms.",
    "The segment 305-325 contains some polar residues (Y, C, G, S, T) that make it a borderline TM helix, but it is still the best hydrophobic stretch available and consistent with the known C-terminal TM anchor architecture of Crh-family chitin transglycosylases.",
    "The reviewer-only evidence confirms the annotation matches the supplied sequence (451 AA, SHA256 match), but the model was not given the protein identity or UniProt accession."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and D are eliminated by out-of-range positions. Choice B is eliminated by inclusion of charged residues (K, R) incompatible with TM helix criteria. Choice C is the only option consistent with both the protein length and hydrophobic TM helix requirements. No genuine ambiguity remains among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A384K4T0 annotates a transmembrane helix at positions 305..325 (evidence code ECO:0000255, rule-based computational prediction). The sequence segment at 305-325 (VYCGGGAAVAALVSAFLFTF) is the hydrophobic core of a C-terminal TM anchor region. Choices A and D reference positions (704-727, 483-503) that exceed the 451-residue protein length, making them impossible. Choice B (301-328) includes charged residues K (pos 302) and R (pos 327) incompatible with TM helix criteria. The annotation supports C as the correct boundary.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can eliminate choices A and D by noting the protein is 451 residues long, making positions 483-503 and 704-727 out of range. Between B (301..328) and C (305..325), standard transmembrane helix criteria exclude charged residues from the hydrophobic core. Position 302 is lysine (K, positively charged) and position 327 is arginine (R, positively charged), both clearly incompatible with a TM helix segment. Choice B therefore includes charged boundary residues that violate the hydrophobic requirement of a ~20-residue TM alpha-helix. Choice C (305-325) captures the hydrophobic core (V, A, V, A, A, L, V, A, F, L, F, F) without charged residues. This is a well-established, transferable principle of membrane protein biology applicable to any TM prediction task.",
    "missing_item_specific_fact": "",
    "reason": "The discrimination relies on (1) checking protein length against offered coordinates (eliminates A, D) and (2) applying the universal rule that TM helices exclude charged residues from their hydrophobic core (eliminates B in favor of C). Both are standard, transferable knowledge about transmembrane protein architecture, not specific to this protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and D are eliminated by out-of-range positions. Choice B is eliminated by inclusion of charged residues (K, R) incompatible with TM helix criteria. Choice C is the only option consistent with both the protein length and hydrophobic TM helix requirements. No genuine ambiguity remains among the offered alternatives."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (rule-based/computational), not experimental data. Exact TM boundaries can vary between prediction algorithms.",
    "The segment 305-325 contains some polar residues (Y, C, G, S, T) that make it a borderline TM helix, but it is still the best hydrophobic stretch available and consistent with the known C-terminal TM anchor architecture of Crh-family chitin transglycosylases.",
    "The reviewer-only evidence confirms the annotation matches the supplied sequence (451 AA, SHA256 match), but the model was not given the protein identity or UniProt accession."
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
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":325},\"start\":{\"modifier\":\"EXACT\",\"value\":305}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
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
  "excerpt": "FT   TRANSMEM        305..325\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:27.918229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f",
  "url": "https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
