# active_site_0107

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0107.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 175 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTTASSDPLLQPFTLKHLVLKNRVMSTSHASRLTRDEFPQEVYQRYHEEKAKGGLALTMFGGSSNVSLDSPNTFQQINLSADAVVPHLRRFSDRIHTHGAALMCQITHLGRRGDAYTEPWLPMIAPSPVRETLHRAMPQAIHDADIKRVIRDFGLAAKRCRDGGLDGIETHAGGHLIGQFMDPTVNLRTDKYGGSTANRVRFAIEVHEEIRKQVGDDFVVGFRFALEDGCSFEEGLEMSRILQGTGLFDFFNVTFGRMDTKMALAVNSMPGMFVPSAPWLPKAAAFKRAVDLPVFHAAKIADLATARYAIREGLLDMVGMTRAHIAEPHLVKLVEAGKEDEARPCVGASFCRNFRATCIHNPATSRETYLTHDIPKAAQTKRVLIVGAGPAGLEAARICATRGHDVTVLEANSTAGGQLLLAATGSWRRDLIGIVDWRVSALERLSVDVRYNHYAELSDVLDHGADVVIIATGGLPNLDALPGAEHCKSVFDALTETPPREGSVIVYDGTGRHNAYLCAERYVDAGLDVSLALIDSMPAQETGGRGDDQVWMRNIARWDVPVRTNIELIEVTASSNGKRRAVFQHHLTNERVELEADHVVVERGMLAVEDLFEAARMYSANDGYTDLEAFATGKPQPGHEAEEGQFHLYRIGDASASRDIHTAIYDAYRLCLAL

[Multiple Choices]
A. Position 558 (For beta-ketoacyl synthase activity)
B. Position 166 (Proton donor)
C. Position 421 (Nucleophile)
D. Position 175 (Proton donor)
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

> The sequence-matched UniProt annotation assigns position 175 as the proton donor, and the archived annotation makes the same assignment. This supports choice D; the feature is a curated assertion citing a paper, not by itself a description of the underlying experiment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a flavin-dependent ene-reductase, for which family-level knowledge of conserved catalytic proton-transfer residues provides a basis for favoring the histidine at position 175. In the local sequence, position 175 is His, whereas position 166 is Asp; the family pattern makes the His a more meaningful proton-donor candidate than the alternative. This is a transferable inference, not an independent proof of the exact annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could use sequence-family recognition and conserved catalytic-residue patterns to distinguish D among these choices. The sequence alone may not establish the assignment with certainty, but the distinction does not require recalling this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although Asp can participate in proton transfer in some enzymes, the family-level inference and the matching curated assignment favor position 175 over position 166 in this question.


### Important caveats

- The reviewer evidence matches the supplied sequence, but the exact source snapshot used by the author is unknown.
- The active-site annotation cites a publication and has evidence code ECO:0000305; the supplied evidence does not independently establish the experimental basis for the assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a flavin-dependent ene-reductase, for which family-level knowledge of conserved catalytic proton-transfer residues provides a basis for favoring the histidine at position 175. In the local sequence, position 175 is His, whereas position 166 is Asp; the family pattern makes the His a more meaningful proton-donor candidate than the alternative. This is a transferable inference, not an independent proof of the exact annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use sequence-family recognition and conserved catalytic-residue patterns to distinguish D among these choices. The sequence alone may not establish the assignment with certainty, but the distinction does not require recalling this exact protein's database record."
  },
  "case_id": "active_site_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 175 as the proton donor, and the archived annotation makes the same assignment. This supports choice D; the feature is a curated assertion citing a paper, not by itself a description of the underlying experiment."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the exact source snapshot used by the author is unknown.",
    "The active-site annotation cites a publication and has evidence code ECO:0000305; the supplied evidence does not independently establish the experimental basis for the assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although Asp can participate in proton transfer in some enzymes, the family-level inference and the matching curated assignment favor position 175 over position 166 in this question."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 175 as the proton donor, and the archived annotation makes the same assignment. This supports choice D; the feature is a curated assertion citing a paper, not by itself a description of the underlying experiment.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a flavin-dependent ene-reductase, for which family-level knowledge of conserved catalytic proton-transfer residues provides a basis for favoring the histidine at position 175. In the local sequence, position 175 is His, whereas position 166 is Asp; the family pattern makes the His a more meaningful proton-donor candidate than the alternative. This is a transferable inference, not an independent proof of the exact annotation.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use sequence-family recognition and conserved catalytic-residue patterns to distinguish D among these choices. The sequence alone may not establish the assignment with certainty, but the distinction does not require recalling this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although Asp can participate in proton transfer in some enzymes, the family-level inference and the matching curated assignment favor position 175 over position 166 in this question."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the exact source snapshot used by the author is unknown.",
    "The active-site annotation cites a publication and has evidence code ECO:0000305; the supplied evidence does not independently establish the experimental basis for the assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXY1 explicitly annotates position 175 as 'Active site' with description 'Proton donor' (evidence code ECO:0000305, based on PubMed:39867842, the 2025 Blue-Lahom et al. paper on the 2-ER subfamily of OYEs). The sequence at position 175 is indeed Histidine (H), consistent with a proton donor role. The annotation is a curator inference from the cited publication.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains FMN-binding motifs (GGLD at ~162-165, and other conserved OYE-family features) identifying this as an Old Yellow Enzyme (OYE) family member. Option A (position 558, 'beta-ketoacyl synthase activity') is eliminated because beta-ketoacyl synthase (FabH) is an entirely different enzyme family with no FMN cofactor; this protein clearly is not FabH. Option C (position 421, 'Nucleophile') is eliminated because position 421 is Leucine (L), which has no nucleophilic side chain. Between B (Asp166, proton donor) and D (His175, proton donor): position 166 (D) falls within or immediately adjacent to the GGLD motif, which in the OYE family (e.g., OYE1/P42593) is a well-established FMN-binding motif, not a catalytic proton-donor site. Position 175 (H) is downstream of this motif in a region more consistent with a catalytic residue. Histidine is the most common proton donor/acceptor in enzyme catalysis (serine proteases, many oxidoreductases), making it a far more plausible proton donor than an Asp embedded in a cofactor-binding motif. Thus, family-level knowledge of OYE FMN-binding motifs plus general enzymology of His as a proton shuttle meaningfully distinguishes D from B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the protein as OYE-family from sequence motifs, eliminate A (wrong enzyme class) and C (Leucine cannot be nucleophile), and prefer D over B using the well-known fact that GGLD is an FMN-binding motif (not a catalytic site) and that His is a canonical proton donor. The argument does not require knowing this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are clearly eliminable (wrong enzyme family; non-nucleophilic residue). Between B and D, the GGLD-motif argument and His-vs-Asp proton-donor plausibility favor D. While the classical OYE1 proton donor is Tyr (not His), the 2-ER subfamily differs, and among the four offered choices, D is the most defensible by transferable reasoning.


### Important caveats

- The UniProt annotation for position 175 uses evidence code ECO:0000305 (inferred by curator) based on a 2025 publication, not direct experimental mutagenesis evidence. The paper describes it as a 'probable active site.'
- In classical OYE1 (P42593), the proton donor is Tyr196, not His. The identification of His as the proton donor is specific to the 2-ER subfamily characterized in the 2025 paper. A model relying solely on classical OYE1 knowledge might expect a Tyr rather than a His, but among the four offered options, no Tyr is listed as a proton donor, so the reasoning still favors D.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt P0DXY1, validating that the annotation applies to this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains FMN-binding motifs (GGLD at ~162-165, and other conserved OYE-family features) identifying this as an Old Yellow Enzyme (OYE) family member. Option A (position 558, 'beta-ketoacyl synthase activity') is eliminated because beta-ketoacyl synthase (FabH) is an entirely different enzyme family with no FMN cofactor; this protein clearly is not FabH. Option C (position 421, 'Nucleophile') is eliminated because position 421 is Leucine (L), which has no nucleophilic side chain. Between B (Asp166, proton donor) and D (His175, proton donor): position 166 (D) falls within or immediately adjacent to the GGLD motif, which in the OYE family (e.g., OYE1/P42593) is a well-established FMN-binding motif, not a catalytic proton-donor site. Position 175 (H) is downstream of this motif in a region more consistent with a catalytic residue. Histidine is the most common proton donor/acceptor in enzyme catalysis (serine proteases, many oxidoreductases), making it a far more plausible proton donor than an Asp embedded in a cofactor-binding motif. Thus, family-level knowledge of OYE FMN-binding motifs plus general enzymology of His as a proton shuttle meaningfully distinguishes D from B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the protein as OYE-family from sequence motifs, eliminate A (wrong enzyme class) and C (Leucine cannot be nucleophile), and prefer D over B using the well-known fact that GGLD is an FMN-binding motif (not a catalytic site) and that His is a canonical proton donor. The argument does not require knowing this exact protein's database annotation."
  },
  "case_id": "active_site_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXY1 explicitly annotates position 175 as 'Active site' with description 'Proton donor' (evidence code ECO:0000305, based on PubMed:39867842, the 2025 Blue-Lahom et al. paper on the 2-ER subfamily of OYEs). The sequence at position 175 is indeed Histidine (H), consistent with a proton donor role. The annotation is a curator inference from the cited publication."
  },
  "important_caveats": [
    "The UniProt annotation for position 175 uses evidence code ECO:0000305 (inferred by curator) based on a 2025 publication, not direct experimental mutagenesis evidence. The paper describes it as a 'probable active site.'",
    "In classical OYE1 (P42593), the proton donor is Tyr196, not His. The identification of His as the proton donor is specific to the 2-ER subfamily characterized in the 2025 paper. A model relying solely on classical OYE1 knowledge might expect a Tyr rather than a His, but among the four offered options, no Tyr is listed as a proton donor, so the reasoning still favors D.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt P0DXY1, validating that the annotation applies to this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly eliminable (wrong enzyme family; non-nucleophilic residue). Between B and D, the GGLD-motif argument and His-vs-Asp proton-donor plausibility favor D. While the classical OYE1 proton donor is Tyr (not His), the 2-ER subfamily differs, and among the four offered choices, D is the most defensible by transferable reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXY1 explicitly annotates position 175 as 'Active site' with description 'Proton donor' (evidence code ECO:0000305, based on PubMed:39867842, the 2025 Blue-Lahom et al. paper on the 2-ER subfamily of OYEs). The sequence at position 175 is indeed Histidine (H), consistent with a proton donor role. The annotation is a curator inference from the cited publication.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains FMN-binding motifs (GGLD at ~162-165, and other conserved OYE-family features) identifying this as an Old Yellow Enzyme (OYE) family member. Option A (position 558, 'beta-ketoacyl synthase activity') is eliminated because beta-ketoacyl synthase (FabH) is an entirely different enzyme family with no FMN cofactor; this protein clearly is not FabH. Option C (position 421, 'Nucleophile') is eliminated because position 421 is Leucine (L), which has no nucleophilic side chain. Between B (Asp166, proton donor) and D (His175, proton donor): position 166 (D) falls within or immediately adjacent to the GGLD motif, which in the OYE family (e.g., OYE1/P42593) is a well-established FMN-binding motif, not a catalytic proton-donor site. Position 175 (H) is downstream of this motif in a region more consistent with a catalytic residue. Histidine is the most common proton donor/acceptor in enzyme catalysis (serine proteases, many oxidoreductases), making it a far more plausible proton donor than an Asp embedded in a cofactor-binding motif. Thus, family-level knowledge of OYE FMN-binding motifs plus general enzymology of His as a proton shuttle meaningfully distinguishes D from B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the protein as OYE-family from sequence motifs, eliminate A (wrong enzyme class) and C (Leucine cannot be nucleophile), and prefer D over B using the well-known fact that GGLD is an FMN-binding motif (not a catalytic site) and that His is a canonical proton donor. The argument does not require knowing this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly eliminable (wrong enzyme family; non-nucleophilic residue). Between B and D, the GGLD-motif argument and His-vs-Asp proton-donor plausibility favor D. While the classical OYE1 proton donor is Tyr (not His), the 2-ER subfamily differs, and among the four offered choices, D is the most defensible by transferable reasoning."
  },
  "important_caveats": [
    "The UniProt annotation for position 175 uses evidence code ECO:0000305 (inferred by curator) based on a 2025 publication, not direct experimental mutagenesis evidence. The paper describes it as a 'probable active site.'",
    "In classical OYE1 (P42593), the proton donor is Tyr196, not His. The identification of His as the proton donor is specific to the 2-ER subfamily characterized in the 2025 paper. A model relying solely on classical OYE1 knowledge might expect a Tyr rather than a His, but among the four offered options, no Tyr is listed as a proton donor, so the reasoning still favors D.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt P0DXY1, validating that the annotation applies to this exact sequence."
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
  "benchmark_sequence_length": 674,
  "benchmark_sequence_sha256": "d0a9daceb358a7ab215246a52585cb052774e4be4676ac0c90d1d7ce1289a52e",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 674,
  "current_source_sequence_sha256": "d0a9daceb358a7ab215246a52585cb052774e4be4676ac0c90d1d7ce1289a52e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXY1",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "selected_historical_source_sequence_length": 674,
  "selected_historical_source_sequence_sha256": "d0a9daceb358a7ab215246a52585cb052774e4be4676ac0c90d1d7ce1289a52e",
  "selected_historical_version": {
    "accession": "P0DXY1",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OYE_CABCO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXY1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Burkholderia cordobensis\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Burkholderiaceae\",\"Caballeronia\"],\"scientificName\":\"Caballeronia cordobensis\",\"taxonId\":1353886}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"value\":\"Old yellow enzyme\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"value\":\"OYE\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"value\":\"1.14.13.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"value\":\"1.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Multifunctional alkene reductase/demethylase OYE\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":175},\"start\":{\"modifier\":\"EXACT\",\"value\":175}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P42593\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":62},\"start\":{\"modifier\":\"EXACT\",\"value\":62}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P42593\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":105},\"start\":{\"modifier\":\"EXACT\",\"value\":105}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P42593\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":223},\"start\":{\"modifier\":\"EXACT\",\"value\":223}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P42593\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":299},\"start\":{\"modifier\":\"EXACT\",\"value\":299}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:49883\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:49883\",\"name\":\"[4Fe-4S] cluster\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":345},\"start\":{\"modifier\":\"EXACT\",\"value\":345}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:49883\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:49883\",\"name\":\"[4Fe-4S] cluster\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":351},\"start\":{\"modifier\":\"EXACT\",\"value\":351}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:49883\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:49883\",\"name\":\"[4Fe-4S] cluster\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":358},\"start\":{\"modifier\":\"EXACT\",\"value\":358}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P42593\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57692\",\"name\":\"FAD\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":391},\"start\":{\"modifier\":\"EXACT\",\"value\":391}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P42593\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57692\",\"name\":\"FAD\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":418},\"start\":{\"modifier\":\"EXACT\",\"value\":418}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P42593\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57692\",\"name\":\"FAD\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":428},\"start\":{\"modifier\":\"EXACT\",\"value\":428}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Blue-Lahom T.C.\",\"Jones S.K.\",\"Davis K.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39867842\"},{\"database\":\"DOI\",\"id\":\"10.1039/d4cb00289j\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"39867842\",\"journal\":\"RSC Chem. Biol.\",\"lastPage\":\"0\",\"publicationDate\":\"2025\",\"title\":\"Bioinformatic and biochemical analysis uncovers novel activity in the 2-ER subfamily of OYEs.\",\"volume\":\"0\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"RPE67\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PROBABLE ACTIVE SITE\",\"COFACTORS\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   OYE_CABCO               Reviewed;         674 AA.\nAC   P0DXY1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Multifunctional alkene reductase/demethylase OYE {ECO:0000305};\nDE            EC=1.14.13.- {ECO:0000269|PubMed:39867842};\nDE            EC=1.3.1.- {ECO:0000269|PubMed:39867842};\nDE   AltName: Full=Old yellow enzyme {ECO:0000303|PubMed:39867842};\nDE            Short=OYE {ECO:0000303|PubMed:39867842};\nGN   ORFNames=BRPE67_CCDS01850;\nOS   Caballeronia cordobensis (Burkholderia cordobensis).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Burkholderiaceae; Caballeronia.\nOX   NCBI_TaxID=1353886;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PROBABLE ACTIVE SITE, COFACTORS, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=RPE67;\nRX   PubMed=39867842; DOI=10.1039/d4cb00289j;\nRA   Blue-Lahom T.C., Jones S.K., Davis K.M.;\nRT   \"Bioinformatic and biochemical analysis uncovers novel activity in the 2-ER\nRT   subfamily of OYEs.\";\nRL   RSC Chem. Biol. 0:0-0(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        175\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000305|PubMed:39867842\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         62\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P42593\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         105\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P42593\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         223\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P42593\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         299\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P42593\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         345\nFT                   /ligand=\"[4Fe-4S] cluster\"\nFT                   /ligand_id=\"ChEBI:CHEBI:49883\"\nFT                   /evidence=\"ECO:0000305|PubMed:39867842\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         351\nFT                   /ligand=\"[4Fe-4S] cluster\"\nFT                   /ligand_id=\"ChEBI:CHEBI:49883\"\nFT                   /evidence=\"ECO:0000305|PubMed:39867842\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 132-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         358\nFT                   /ligand=\"[4Fe-4S] cluster\"\nFT                   /ligand_id=\"ChEBI:CHEBI:49883\"\nFT                   /evidence=\"ECO:0000305|PubMed:39867842\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         391\nFT                   /ligand=\"FAD\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57692\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P42593\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 140-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         418\nFT                   /ligand=\"FAD\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57692\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P42593\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         428\nFT                   /ligand=\"FAD\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57692\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P42593\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-151",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
