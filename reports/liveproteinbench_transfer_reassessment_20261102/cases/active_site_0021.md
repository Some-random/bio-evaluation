# active_site_0021

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0021.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 119 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFPKIFLTAATALLSAKSTFAQTYSSCNPLFTTGCPANTALGKSIDVDFTSGSVNSFDGSGDITYDSNGASFTVAKSGDAPTLSSIFYIMFGKVQITMKAAPGAGIVSTLVLQSDDLDEIDMEWLGADDTEVQTNYFGKGKVTDYNRGAFNPAANNQGEFITYTIEWTSEQVVWSVGSTVVRVLTPATADTDQYPQSPMQIKFGAWSGGDSSNAAGTISWARGPTDYSNGPFTMVVQSIDVSDYSTGTQYKYGDQSGDWTSIEAIGGSVNGNVPASASSIQTAGAAAVTSSSPTIPAGINNGNSATRTGYPWVAGTQTVSEVTWSTGPSIPSGWEISSEGKIVPVSASPINISRINPLLLCGPFTFFFFAAIRRWP

[Multiple Choices]
A. Position 119 (Nucleophile)
B. Position 118 (Nucleophile)
C. Position 959 (Proton acceptor; for dehydratase activity)
D. Position 95 (Nucleophile)
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

> The sequence-matched UniProt annotation identifies position 119 as the nucleophile, consistent with the key. The annotation is linked to a publication, though the excerpts do not independently establish the experimental basis.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the motif EIDME at positions 119–123, matching the characteristic catalytic motif of GH16-like glycoside hydrolases and transglycosylases. In this family, the first glutamate is the nucleophile and the later glutamate participates in acid/base catalysis. This distinguishes position 119 from adjacent position 118; position 959 is beyond the 376-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A conserved family-level catalytic motif provides a credible transferable basis for choosing A, without needing the exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A gives the motif's nucleophilic glutamate; the neighboring residue in B is not that catalytic residue, and C and D do not fit the sequence and motif.


### Important caveats

- The source annotation is publication-linked, but the supplied excerpts do not include the underlying experimental results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the motif EIDME at positions 119–123, matching the characteristic catalytic motif of GH16-like glycoside hydrolases and transglycosylases. In this family, the first glutamate is the nucleophile and the later glutamate participates in acid/base catalysis. This distinguishes position 119 from adjacent position 118; position 959 is beyond the 376-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A conserved family-level catalytic motif provides a credible transferable basis for choosing A, without needing the exact protein's database annotation."
  },
  "case_id": "active_site_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 119 as the nucleophile, consistent with the key. The annotation is linked to a publication, though the excerpts do not independently establish the experimental basis."
  },
  "important_caveats": [
    "The source annotation is publication-linked, but the supplied excerpts do not include the underlying experimental results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A gives the motif's nucleophilic glutamate; the neighboring residue in B is not that catalytic residue, and C and D do not fit the sequence and motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 119 as the nucleophile, consistent with the key. The annotation is linked to a publication, though the excerpts do not independently establish the experimental basis.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the motif EIDME at positions 119–123, matching the characteristic catalytic motif of GH16-like glycoside hydrolases and transglycosylases. In this family, the first glutamate is the nucleophile and the later glutamate participates in acid/base catalysis. This distinguishes position 119 from adjacent position 118; position 959 is beyond the 376-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "A conserved family-level catalytic motif provides a credible transferable basis for choosing A, without needing the exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A gives the motif's nucleophilic glutamate; the neighboring residue in B is not that catalytic residue, and C and D do not fit the sequence and motif."
  },
  "important_caveats": [
    "The source annotation is publication-linked, but the supplied excerpts do not include the underlying experimental results."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) explicitly records Position 119 as 'Nucleophile' active site with evidence code ECO:0000305|PubMed:33846308 (a 2021 Nature Communications paper on Botrytis cinerea Crh proteins). The sequence at position 119 is Glutamic acid (E), consistent with the GH18 chitinase/transglycosylase catalytic nucleophile. The expected answer A is directly confirmed by the database annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can apply transferable GH18 family knowledge to distinguish the options. (1) Position 959 is impossible for a 376-residue protein, eliminating C. (2) Position 95 is Glutamine (Q), which is not a recognized nucleophile in glycoside hydrolases, eliminating D. (3) Between positions 118 (Asp/D) and 119 (Glu/E): GH18 chitinases and transglycosylases characteristically use a Glutamic acid as the catalytic nucleophile (not Asp), a well-established family-level feature. The acidic cluster D(115)-D(116)-L(117)-D(118)-E(119) matches the conserved catalytic motif in GH18 enzymes where the Glu at the end of the acidic stretch performs nucleophilic attack on the anomeric carbon. The adjacent E(123) in the context D(121)-M(122)-E(123)-W(124) is consistent with the GH18 proton donor position. Thus, family-level knowledge that GH18 nucleophiles are Glu (not Asp) and the recognizable acidic-cluster-then-Glu motif meaningfully distinguishes position 119 (E) from position 118 (D).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinction between options A (119, E) and B (118, D) rests on the well-known GH18 family rule that the catalytic nucleophile is a Glutamic acid, not an Aspartic acid, and on the recognizable D-D-L-D-E catalytic motif pattern. This is transferable family-level knowledge, not a fact specific to this exact protein's database record. The elimination of C (position beyond sequence length) and D (Gln is not a glycosidase nucleophile) uses basic sequence arithmetic and general enzymology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly eliminable (position 959 exceeds sequence length; Gln is not a glycosidase nucleophile). The remaining choice between 118 (D) and 119 (E) is resolved by the GH18 Glu-nucleophile rule and the catalytic motif context, leaving only one defensible answer.


### Important caveats

- Recognizing this sequence as a GH18 chitinase/transglycosylase from raw sequence alone (without BLAST or database lookup) is non-trivial; the family assignment relies on the acidic-cluster motif and overall composition, which a model may or may not reliably extract.
- The UniProt active-site annotation carries evidence code ECO:0000305 linked to PubMed:33846308, indicating experimental support from the cited Nature Communications paper, not mere computational transfer.
- The proton donor annotation at position 123 (also E) is consistent with GH18 mechanism and further supports the catalytic assignment at 119, but this corroboration is reviewer-visible only.
- The sequence length in the user input appears to be 374-376 residues depending on counting; the reviewer confirms 376 AA with exact sequence match.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can apply transferable GH18 family knowledge to distinguish the options. (1) Position 959 is impossible for a 376-residue protein, eliminating C. (2) Position 95 is Glutamine (Q), which is not a recognized nucleophile in glycoside hydrolases, eliminating D. (3) Between positions 118 (Asp/D) and 119 (Glu/E): GH18 chitinases and transglycosylases characteristically use a Glutamic acid as the catalytic nucleophile (not Asp), a well-established family-level feature. The acidic cluster D(115)-D(116)-L(117)-D(118)-E(119) matches the conserved catalytic motif in GH18 enzymes where the Glu at the end of the acidic stretch performs nucleophilic attack on the anomeric carbon. The adjacent E(123) in the context D(121)-M(122)-E(123)-W(124) is consistent with the GH18 proton donor position. Thus, family-level knowledge that GH18 nucleophiles are Glu (not Asp) and the recognizable acidic-cluster-then-Glu motif meaningfully distinguishes position 119 (E) from position 118 (D).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinction between options A (119, E) and B (118, D) rests on the well-known GH18 family rule that the catalytic nucleophile is a Glutamic acid, not an Aspartic acid, and on the recognizable D-D-L-D-E catalytic motif pattern. This is transferable family-level knowledge, not a fact specific to this exact protein's database record. The elimination of C (position beyond sequence length) and D (Gln is not a glycosidase nucleophile) uses basic sequence arithmetic and general enzymology."
  },
  "case_id": "active_site_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly records Position 119 as 'Nucleophile' active site with evidence code ECO:0000305|PubMed:33846308 (a 2021 Nature Communications paper on Botrytis cinerea Crh proteins). The sequence at position 119 is Glutamic acid (E), consistent with the GH18 chitinase/transglycosylase catalytic nucleophile. The expected answer A is directly confirmed by the database annotation."
  },
  "important_caveats": [
    "Recognizing this sequence as a GH18 chitinase/transglycosylase from raw sequence alone (without BLAST or database lookup) is non-trivial; the family assignment relies on the acidic-cluster motif and overall composition, which a model may or may not reliably extract.",
    "The UniProt active-site annotation carries evidence code ECO:0000305 linked to PubMed:33846308, indicating experimental support from the cited Nature Communications paper, not mere computational transfer.",
    "The proton donor annotation at position 123 (also E) is consistent with GH18 mechanism and further supports the catalytic assignment at 119, but this corroboration is reviewer-visible only.",
    "The sequence length in the user input appears to be 374-376 residues depending on counting; the reviewer confirms 376 AA with exact sequence match."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminable (position 959 exceeds sequence length; Gln is not a glycosidase nucleophile). The remaining choice between 118 (D) and 119 (E) is resolved by the GH18 Glu-nucleophile rule and the catalytic motif context, leaving only one defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly records Position 119 as 'Nucleophile' active site with evidence code ECO:0000305|PubMed:33846308 (a 2021 Nature Communications paper on Botrytis cinerea Crh proteins). The sequence at position 119 is Glutamic acid (E), consistent with the GH18 chitinase/transglycosylase catalytic nucleophile. The expected answer A is directly confirmed by the database annotation.",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can apply transferable GH18 family knowledge to distinguish the options. (1) Position 959 is impossible for a 376-residue protein, eliminating C. (2) Position 95 is Glutamine (Q), which is not a recognized nucleophile in glycoside hydrolases, eliminating D. (3) Between positions 118 (Asp/D) and 119 (Glu/E): GH18 chitinases and transglycosylases characteristically use a Glutamic acid as the catalytic nucleophile (not Asp), a well-established family-level feature. The acidic cluster D(115)-D(116)-L(117)-D(118)-E(119) matches the conserved catalytic motif in GH18 enzymes where the Glu at the end of the acidic stretch performs nucleophilic attack on the anomeric carbon. The adjacent E(123) in the context D(121)-M(122)-E(123)-W(124) is consistent with the GH18 proton donor position. Thus, family-level knowledge that GH18 nucleophiles are Glu (not Asp) and the recognizable acidic-cluster-then-Glu motif meaningfully distinguishes position 119 (E) from position 118 (D).",
    "missing_item_specific_fact": "",
    "reason": "The distinction between options A (119, E) and B (118, D) rests on the well-known GH18 family rule that the catalytic nucleophile is a Glutamic acid, not an Aspartic acid, and on the recognizable D-D-L-D-E catalytic motif pattern. This is transferable family-level knowledge, not a fact specific to this exact protein's database record. The elimination of C (position beyond sequence length) and D (Gln is not a glycosidase nucleophile) uses basic sequence arithmetic and general enzymology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminable (position 959 exceeds sequence length; Gln is not a glycosidase nucleophile). The remaining choice between 118 (D) and 119 (E) is resolved by the GH18 Glu-nucleophile rule and the catalytic motif context, leaving only one defensible answer."
  },
  "important_caveats": [
    "Recognizing this sequence as a GH18 chitinase/transglycosylase from raw sequence alone (without BLAST or database lookup) is non-trivial; the family assignment relies on the acidic-cluster motif and overall composition, which a model may or may not reliably extract.",
    "The UniProt active-site annotation carries evidence code ECO:0000305 linked to PubMed:33846308, indicating experimental support from the cited Nature Communications paper, not mere computational transfer.",
    "The proton donor annotation at position 123 (also E) is consistent with GH18 mechanism and further supports the catalytic assignment at 119, but this corroboration is reviewer-visible only.",
    "The sequence length in the user input appears to be 374-376 residues depending on counting; the reviewer confirms 376 AA with exact sequence match."
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
  "benchmark_sequence_length": 376,
  "benchmark_sequence_sha256": "93c30927e9f4a2529afa60c60aafd3d9da23bd8a18c0bce7ba4f794ddcbc6138",
  "current_entry_audit": {
    "entryVersion": 25,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 376,
  "current_source_sequence_sha256": "93c30927e9f4a2529afa60c60aafd3d9da23bd8a18c0bce7ba4f794ddcbc6138",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 23,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384JN58",
  "selected_historical_entry_version": 23,
  "selected_historical_record_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "selected_historical_source_sequence_length": 376,
  "selected_historical_source_sequence_sha256": "93c30927e9f4a2529afa60c60aafd3d9da23bd8a18c0bce7ba4f794ddcbc6138",
  "selected_historical_version": {
    "accession": "A0A384JN58",
    "database": "Swiss-Prot",
    "entryVersion": 23,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH4_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384JN58\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":25,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitinase crh4\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitin transglycosylase crh4\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 4\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":119},\"start\":{\"modifier\":\"EXACT\",\"value\":119}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":123},\"start\":{\"modifier\":\"EXACT\",\"value\":123}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":123},\"start\":{\"modifier\":\"EXACT\",\"value\":123}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":202},\"start\":{\"modifier\":\"EXACT\",\"value\":202}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":206},\"start\":{\"modifier\":\"EXACT\",\"value\":206}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":217},\"start\":{\"modifier\":\"EXACT\",\"value\":217}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Bi K.\",\"Scalschi L.\",\"Jaiswal N.\",\"Mengiste T.\",\"Fried R.\",\"Sanz A.B.\",\"Arroyo J.\",\"Zhu W.\",\"Masrati G.\",\"Sharon A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33846308\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-021-22436-1\"}],\"citationType\":\"journal article\",\"firstPage\":\"2166\",\"id\":\"33846308\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2166\",\"publicationDate\":\"2021\",\"title\":\"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.\",\"volume\":\"12\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H1",
  "excerpt": "ID   CRH4_BOTFB              Reviewed;         376 AA.\nAC   A0A384JN58;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 23.\nDE   RecName: Full=Crh-like protein 4 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh4 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh4 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\nGN   Name=crh4 {ECO:0000303|PubMed:33846308}; ORFNames=BCIN_07g04870;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;\nRA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,\nRA   Arroyo J., Zhu W., Masrati G., Sharon A.;\nRT   \"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector\nRT   triggering plant cell death and defense response.\";\nRL   Nat. Commun. 12:2166-2166(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        119\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000305|PubMed:33846308\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        123\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000305|PubMed:33846308\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         123\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 134-137",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         202\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 138-141",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         206\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-145",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         217\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 146-149",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
