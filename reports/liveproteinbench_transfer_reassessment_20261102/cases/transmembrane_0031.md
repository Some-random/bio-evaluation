# transmembrane_0031

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0031.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 6..26

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MYYRETMLAFVPYLAVFVACYGLVYYRRKRQRLPLPPGPPQLPLVGNLYQIPEMNPWRTYREWHQKYGPIITVKSGLTNTIILGSHKAARDLLDKRNRNYGSRPHFILIGDFIYGGNQTSLLPTGQRWRIHRRILSAFGNVRTSQRYRILYDAESKRLLREILHGGDFFEPFHHYFVRILFALTYGKRVTGSHDPEARDVIEIVDVVLKEASRSSVPEAFPILNSLPGALAPWKRRAQLLFEQHSRLFDNHMNAALANKPWNFCKQALRLKASSEVDRVELNFILGSITEATHSGSMVLGVFIMANILHPDAVRWVQEEIDRVIGPDRLPSFDDMAKLPYLNAYLLEVMRWRPITPGGMPHASFQDDEYMGYHIPKGTTVVANHWSMDFDESVFTDPYEFRPQRWIEDPNLPSIAFGFGTRICPGRHIAESSIFIVAARLLWSFNFDYAYEDGKRQEIDSWNMTQGLDSGPMPFKASFKIRSPKHQEVMDRECGVSDLDIDAILDKIGADFL

[Multiple Choices]
A. 5..27
B. 6..26; 439..463
C. 6..26
D. 9..30
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

> The matched-sequence UniProt annotation places a helical transmembrane region at 6..26. Its evidence code indicates computational annotation, not direct experimental confirmation; the sequence itself also has a strongly hydrophobic N-terminal stretch in this region.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Residues around 7..26 are rich in hydrophobic amino acids, fitting a membrane-spanning alpha helix, with charged residues flanking the stretch. This strongly favors the N-terminal region in C over the distant region added in B; A includes charged residues at both ends, and D extends farther into the basic C-terminal flank. The pattern supports C as the best choice without requiring knowledge of this protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The characteristic hydrophobic segment and its flanking charges provide a transferable sequence-based basis for distinguishing the offered regions. Exact helix boundaries are less certain than the identification of the segment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> C is the better-supported boundary, but A extends it by only one residue at each end. Those extra charged residues could be interpreted as boundary/interfacial residues, so the sequence alone does not make the precise endpoints unequivocal.


### Important caveats

- The supplied evidence supports the keyed boundaries through a computational annotation; it does not establish them experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Residues around 7..26 are rich in hydrophobic amino acids, fitting a membrane-spanning alpha helix, with charged residues flanking the stretch. This strongly favors the N-terminal region in C over the distant region added in B; A includes charged residues at both ends, and D extends farther into the basic C-terminal flank. The pattern supports C as the best choice without requiring knowledge of this protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The characteristic hydrophobic segment and its flanking charges provide a transferable sequence-based basis for distinguishing the offered regions. Exact helix boundaries are less certain than the identification of the segment."
  },
  "case_id": "transmembrane_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation places a helical transmembrane region at 6..26. Its evidence code indicates computational annotation, not direct experimental confirmation; the sequence itself also has a strongly hydrophobic N-terminal stretch in this region."
  },
  "important_caveats": [
    "The supplied evidence supports the keyed boundaries through a computational annotation; it does not establish them experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "C is the better-supported boundary, but A extends it by only one residue at each end. Those extra charged residues could be interpreted as boundary/interfacial residues, so the sequence alone does not make the precise endpoints unequivocal."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation places a helical transmembrane region at 6..26. Its evidence code indicates computational annotation, not direct experimental confirmation; the sequence itself also has a strongly hydrophobic N-terminal stretch in this region.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Residues around 7..26 are rich in hydrophobic amino acids, fitting a membrane-spanning alpha helix, with charged residues flanking the stretch. This strongly favors the N-terminal region in C over the distant region added in B; A includes charged residues at both ends, and D extends farther into the basic C-terminal flank. The pattern supports C as the best choice without requiring knowledge of this protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "The characteristic hydrophobic segment and its flanking charges provide a transferable sequence-based basis for distinguishing the offered regions. Exact helix boundaries are less certain than the identification of the segment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "C is the better-supported boundary, but A extends it by only one residue at each end. Those extra charged residues could be interpreted as boundary/interfacial residues, so the sequence alone does not make the precise endpoints unequivocal."
  },
  "important_caveats": [
    "The supplied evidence supports the keyed boundaries through a computational annotation; it does not establish them experimentally."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7T8F1L2 annotates a transmembrane helix at positions 6..26 (evidence C5, H3) with evidence code ECO:0000255 (by similarity, i.e., computational/proba). The sequence at positions 6-26 (TMLAFVPYLAVFVACYGLVYY) is a hydrophobic stretch with Y at both ends serving as classic aromatic interface residues. This is consistent with the annotation and with the general biophysics of single-pass TM helices in P450 enzymes. The annotation is computational rather than experimentally validated, but the sequence characteristics strongly corroborate it.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> General principles of transmembrane helix structure clearly distinguish the choices. (1) TM helices require a hydrophobic core of ~18-25 residues with no charged residues inside the bilayer. Position 5 is E (charged) and positions 27-30 are R,R,K,R (charged), so choices A (5..27, includes E5 and R27) and D (9..30, includes R27-R30) violate this principle. (2) The region 439-463 (RLW SFNFDYAYEDGKRQEIDSWNM) is heavily charged/polar (R,D,K,R,Q,E,D,S,N) and is clearly not a TM segment, eliminating B. (3) Choice C (6..26) places T (small polar, common at TM interfaces) at the N-terminal boundary and Y (aromatic, classic 'aromatic belt' interface residue) at the C-terminal boundary, with a hydrophobic core (MLAFVPYLAVFVACYGLVY) in between. This matches the textbook definition of a single-pass TM helix. Additionally, P450 monooxygenases typically have a single N-terminal TM anchor, making a second TM region (as in B) biologically implausible for this enzyme class.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer can be determined by applying well-known biophysical rules about TM helix composition (hydrophobic core, aromatic/polar interface residues, exclusion of charged residues) and the typical single-TM-anchor architecture of cytochrome P450 enzymes. No fact specific to this exact protein's annotation is needed; the sequence itself and general TM biology suffice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The charged residues at positions 5 (E) and 27-30 (RRKR) unambiguously exclude choices A and D. The hydrophilic character of region 439-463 unambiguously excludes B. Choice C is the only option consistent with TM helix biophysics.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (by similarity), meaning the TM assignment is computational rather than experimentally determined, though the sequence characteristics strongly support it.
- TM helix boundaries can sometimes be ambiguous by 1-2 residues in practice, but the charged residues flanking positions 6-26 make the boundaries here particularly clear.
- The reviewer-only evidence confirms the sequence matches the UniProt entry (512 aa, SHA256 match), but the accession and organism identity were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General principles of transmembrane helix structure clearly distinguish the choices. (1) TM helices require a hydrophobic core of ~18-25 residues with no charged residues inside the bilayer. Position 5 is E (charged) and positions 27-30 are R,R,K,R (charged), so choices A (5..27, includes E5 and R27) and D (9..30, includes R27-R30) violate this principle. (2) The region 439-463 (RLW SFNFDYAYEDGKRQEIDSWNM) is heavily charged/polar (R,D,K,R,Q,E,D,S,N) and is clearly not a TM segment, eliminating B. (3) Choice C (6..26) places T (small polar, common at TM interfaces) at the N-terminal boundary and Y (aromatic, classic 'aromatic belt' interface residue) at the C-terminal boundary, with a hydrophobic core (MLAFVPYLAVFVACYGLVY) in between. This matches the textbook definition of a single-pass TM helix. Additionally, P450 monooxygenases typically have a single N-terminal TM anchor, making a second TM region (as in B) biologically implausible for this enzyme class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer can be determined by applying well-known biophysical rules about TM helix composition (hydrophobic core, aromatic/polar interface residues, exclusion of charged residues) and the typical single-TM-anchor architecture of cytochrome P450 enzymes. No fact specific to this exact protein's annotation is needed; the sequence itself and general TM biology suffice."
  },
  "case_id": "transmembrane_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1L2 annotates a transmembrane helix at positions 6..26 (evidence C5, H3) with evidence code ECO:0000255 (by similarity, i.e., computational/proba). The sequence at positions 6-26 (TMLAFVPYLAVFVACYGLVYY) is a hydrophobic stretch with Y at both ends serving as classic aromatic interface residues. This is consistent with the annotation and with the general biophysics of single-pass TM helices in P450 enzymes. The annotation is computational rather than experimentally validated, but the sequence characteristics strongly corroborate it."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (by similarity), meaning the TM assignment is computational rather than experimentally determined, though the sequence characteristics strongly support it.",
    "TM helix boundaries can sometimes be ambiguous by 1-2 residues in practice, but the charged residues flanking positions 6-26 make the boundaries here particularly clear.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry (512 aa, SHA256 match), but the accession and organism identity were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The charged residues at positions 5 (E) and 27-30 (RRKR) unambiguously exclude choices A and D. The hydrophilic character of region 439-463 unambiguously excludes B. Choice C is the only option consistent with TM helix biophysics."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1L2 annotates a transmembrane helix at positions 6..26 (evidence C5, H3) with evidence code ECO:0000255 (by similarity, i.e., computational/proba). The sequence at positions 6-26 (TMLAFVPYLAVFVACYGLVYY) is a hydrophobic stretch with Y at both ends serving as classic aromatic interface residues. This is consistent with the annotation and with the general biophysics of single-pass TM helices in P450 enzymes. The annotation is computational rather than experimentally validated, but the sequence characteristics strongly corroborate it.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "General principles of transmembrane helix structure clearly distinguish the choices. (1) TM helices require a hydrophobic core of ~18-25 residues with no charged residues inside the bilayer. Position 5 is E (charged) and positions 27-30 are R,R,K,R (charged), so choices A (5..27, includes E5 and R27) and D (9..30, includes R27-R30) violate this principle. (2) The region 439-463 (RLW SFNFDYAYEDGKRQEIDSWNM) is heavily charged/polar (R,D,K,R,Q,E,D,S,N) and is clearly not a TM segment, eliminating B. (3) Choice C (6..26) places T (small polar, common at TM interfaces) at the N-terminal boundary and Y (aromatic, classic 'aromatic belt' interface residue) at the C-terminal boundary, with a hydrophobic core (MLAFVPYLAVFVACYGLVY) in between. This matches the textbook definition of a single-pass TM helix. Additionally, P450 monooxygenases typically have a single N-terminal TM anchor, making a second TM region (as in B) biologically implausible for this enzyme class.",
    "missing_item_specific_fact": "",
    "reason": "The answer can be determined by applying well-known biophysical rules about TM helix composition (hydrophobic core, aromatic/polar interface residues, exclusion of charged residues) and the typical single-TM-anchor architecture of cytochrome P450 enzymes. No fact specific to this exact protein's annotation is needed; the sequence itself and general TM biology suffice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The charged residues at positions 5 (E) and 27-30 (RRKR) unambiguously exclude choices A and D. The hydrophilic character of region 439-463 unambiguously excludes B. Choice C is the only option consistent with TM helix biophysics."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (by similarity), meaning the TM assignment is computational rather than experimentally determined, though the sequence characteristics strongly support it.",
    "TM helix boundaries can sometimes be ambiguous by 1-2 residues in practice, but the charged residues flanking positions 6-26 make the boundaries here particularly clear.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry (512 aa, SHA256 match), but the accession and organism identity were not provided to the evaluated model."
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
  "benchmark_sequence_length": 512,
  "benchmark_sequence_sha256": "02f6775f75a6bde5b1b4a75830d1b42077d392027632296a27a40235aff1c6f1",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 512,
  "current_source_sequence_sha256": "02f6775f75a6bde5b1b4a75830d1b42077d392027632296a27a40235aff1c6f1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 17,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8F1L2",
  "selected_historical_entry_version": 17,
  "selected_historical_record_sha256": "f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c",
  "selected_historical_source_sequence_length": 512,
  "selected_historical_source_sequence_sha256": "02f6775f75a6bde5b1b4a75830d1b42077d392027632296a27a40235aff1c6f1",
  "selected_historical_version": {
    "accession": "A0A7T8F1L2",
    "database": "Swiss-Prot",
    "entryVersion": 17,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZL_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1L2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein L\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase FrzL\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":26},\"start\":{\"modifier\":\"EXACT\",\"value\":6}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H1",
  "excerpt": "ID   FRZL_CLASX              Reviewed;         512 AA.\nAC   A0A7T8F1L2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 17.\nDE   RecName: Full=Cytochrome P450 monooxygenase FrzL {ECO:0000303|PubMed:33372776};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein L {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.520828+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], AND FUNCTION.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.520828+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 13-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        6..26\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.520828+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 31. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
