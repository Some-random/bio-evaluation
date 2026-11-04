# EC_number_0174

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0174.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 1.97.1.13

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MYAYNGKLLDVDLTREKVKEVELSEDVLKKFYGGRGLGTYILWKELGEKWEKVDPLGEENLLLILTGPLTGYYPGMKTSIVSKSPESNGVVGSVLSSELGLELKAAGYDGIIIRGKAKSPVYLFIHNDTVEIRDATKYWGMGGIELYKTLLKEVHEEIRKKEKLKGVPKEPAMIYIGKGGENKVRFAAIMTKLMHAAGYGGYGAVMGSKNLKAVIAKGSGPLPEVYDKEKMKVLLREFWKELFSMTTFREWGTGAGGYSVGHDRSSEPIRNWQEEYHDNEEISVVNFENRTWIKKYWADYGCPVNCMKISYLRYGPYKGSISDAPDYELQAYMGTNLGIFEPEKIVYLSYLVDELGLDGINTGNILGFAAELYQRGILTKEDLGFELNWGDEKAFAKLLHLIVEKEGIGKILAEGTYRAALKISEIKGIDVTKYAVHVKGIAVGAHGIRSELDYTKDISYAVSVQGGDHTSTAALPAKGYTGELVEAFYDSAVICNFVTKPGFEKIIEFGNALSGFNITPEQWLNEIGLRIIHLQRILLLLGGPDVYWDPRKDDDNPPRFYEPLPSGPVKGKAPNREDIKAKVKQYYEEIGYDEHGIPKEEVLEELGIGEAKREVKRIKKRLNL

[Multiple Choices]
A. 1.97.1.13
B. 1.97.1.14
C. 2.7.1.39
D. 1.16.1.10
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record assigns EC 1.97.1.13, and its catalytic-activity annotation cites experimental evidence from two publications. The annotated reaction is oxidation of an aliphatic sulfonate with ferredoxin, supporting the keyed EC number.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence and cysteine-rich features may support recognition as a tungsten/iron-sulfur oxidoreductase, making the kinase option and some unrelated oxidoreductases less plausible. But that broad family-level inference does not meaningfully distinguish the closely related EC 1.97.1.13 and 1.97.1.14 alternatives.


**Missing item-specific fact**

> The enzyme's specific substrate and reaction classification, needed to distinguish EC 1.97.1.13 from EC 1.97.1.14.


**Reason**

> The choices include closely related EC numbers for which general recognition of an oxidoreductase family is insufficient. The supplied sequence alone does not establish the substrate specificity that selects the keyed number; doing so would require target-specific functional evidence or an annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports the keyed EC number; no alternative is identified as equally defensible.


### Important caveats

- The source evidence is reviewer-only and was not part of the original model input.
- The sequence matches the cited UniProt entry, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence and cysteine-rich features may support recognition as a tungsten/iron-sulfur oxidoreductase, making the kinase option and some unrelated oxidoreductases less plausible. But that broad family-level inference does not meaningfully distinguish the closely related EC 1.97.1.13 and 1.97.1.14 alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's specific substrate and reaction classification, needed to distinguish EC 1.97.1.13 from EC 1.97.1.14.",
    "reason": "The choices include closely related EC numbers for which general recognition of an oxidoreductase family is insufficient. The supplied sequence alone does not establish the substrate specificity that selects the keyed number; doing so would require target-specific functional evidence or an annotation."
  },
  "case_id": "EC_number_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.97.1.13, and its catalytic-activity annotation cites experimental evidence from two publications. The annotated reaction is oxidation of an aliphatic sulfonate with ferredoxin, supporting the keyed EC number."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and was not part of the original model input.",
    "The sequence matches the cited UniProt entry, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the keyed EC number; no alternative is identified as equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.97.1.13, and its catalytic-activity annotation cites experimental evidence from two publications. The annotated reaction is oxidation of an aliphatic sulfonate with ferredoxin, supporting the keyed EC number.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence and cysteine-rich features may support recognition as a tungsten/iron-sulfur oxidoreductase, making the kinase option and some unrelated oxidoreductases less plausible. But that broad family-level inference does not meaningfully distinguish the closely related EC 1.97.1.13 and 1.97.1.14 alternatives.",
    "missing_item_specific_fact": "The enzyme's specific substrate and reaction classification, needed to distinguish EC 1.97.1.13 from EC 1.97.1.14.",
    "reason": "The choices include closely related EC numbers for which general recognition of an oxidoreductase family is insufficient. The supplied sequence alone does not establish the substrate specificity that selects the keyed number; doing so would require target-specific functional evidence or an annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the keyed EC number; no alternative is identified as equally defensible."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and was not part of the original model input.",
    "The sequence matches the cited UniProt entry, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry E7FHH1 (ASOR_PYRFU, Pyrococcus furiosus) carries EC 1.97.1.13 with experimental evidence codes (ECO:0000269) from PubMed:16199576 and PubMed:36269456. The catalytic reaction (aliphatic sulfonate + 4 oxidized ferredoxin + 2 H2O → 4 reduced ferredoxin + carboxylate + sulfite + 6H+) is supported by X-ray crystallography (PDB 6X1O, 6X6U) and biochemical characterization. The benchmark sequence SHA256 matches the source entry exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C11](#evidence-c11), [C12](#evidence-c12), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can eliminate C (2.7.1.39, a kinase/transferase) and D (1.16.1.10, an Fe(II) oxidoreductase) using family-level knowledge: the GADHT motif and overall fold identify this as a tungsten-containing oxidoreductase (WOR/AOR family) that uses ferredoxin as electron acceptor (EC 1.97.x.x), not a transferase or an iron-donor enzyme. However, distinguishing A (1.97.1.13, aliphatic sulfonate oxidoreductase) from B (1.97.1.14) requires knowing the specific experimental substrate-specificity data for THIS protein. The GADHT motif and W/Mo cofactor binding residues are shared across the entire WOR family and do not encode which particular substrate (sulfonate vs. the substrate of 1.97.1.14) is acted upon. The 1.97.1.13 assignment was made in 2022 based on novel experimental characterization (PubMed:36269456) showing sulfonate desulfonation; prior to that, this protein was annotated as a generic aldehyde oxidoreductase. No sequence motif or family-level inference distinguishes the sulfonate desulfonase activity from other 1.97.1.x reactions.


**Missing item-specific fact**

> The experimental demonstration (PubMed:36269456, 2022) that this specific protein catalyzes aliphatic sulfonate desulfonation (rather than the reaction assigned to EC 1.97.1.14), including the identification of active-site residues conferring sulfonate specificity, which is not derivable from sequence-level family motifs alone.


**Reason**

> While family-level knowledge eliminates options C and D, the critical A-vs-B distinction (1.97.1.13 vs 1.97.1.14) requires the specific experimental characterization of this protein's substrate specificity published in 2022. The shared GADHT/WOR-family motifs do not encode the precise 4th-digit EC assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the experimental data for 1.97.1.13 is known, only A is correct. C and D are clearly wrong by EC class. B (1.97.1.14) would only be defensible if one knew it applied to a different reaction/protein.


### Important caveats

- The protein was originally characterized as WOR5 (tungsten-containing aldehyde oxidoreductase) in 2005; the sulfonate desulfonase EC assignment came only in 2022. Models trained on earlier data might have a different annotation.
- The existence and exact definition of EC 1.97.1.14 could not be independently verified from the supplied evidence; if it is a non-existent or fabricated EC number, option B would be trivially eliminable, making the question more answerable.
- The GADHT motif confirms WOR-family membership but is shared with AOR, FOR, POR, and other family members, so it cannot resolve the 4th-digit EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can eliminate C (2.7.1.39, a kinase/transferase) and D (1.16.1.10, an Fe(II) oxidoreductase) using family-level knowledge: the GADHT motif and overall fold identify this as a tungsten-containing oxidoreductase (WOR/AOR family) that uses ferredoxin as electron acceptor (EC 1.97.x.x), not a transferase or an iron-donor enzyme. However, distinguishing A (1.97.1.13, aliphatic sulfonate oxidoreductase) from B (1.97.1.14) requires knowing the specific experimental substrate-specificity data for THIS protein. The GADHT motif and W/Mo cofactor binding residues are shared across the entire WOR family and do not encode which particular substrate (sulfonate vs. the substrate of 1.97.1.14) is acted upon. The 1.97.1.13 assignment was made in 2022 based on novel experimental characterization (PubMed:36269456) showing sulfonate desulfonation; prior to that, this protein was annotated as a generic aldehyde oxidoreductase. No sequence motif or family-level inference distinguishes the sulfonate desulfonase activity from other 1.97.1.x reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental demonstration (PubMed:36269456, 2022) that this specific protein catalyzes aliphatic sulfonate desulfonation (rather than the reaction assigned to EC 1.97.1.14), including the identification of active-site residues conferring sulfonate specificity, which is not derivable from sequence-level family motifs alone.",
    "reason": "While family-level knowledge eliminates options C and D, the critical A-vs-B distinction (1.97.1.13 vs 1.97.1.14) requires the specific experimental characterization of this protein's substrate specificity published in 2022. The shared GADHT/WOR-family motifs do not encode the precise 4th-digit EC assignment."
  },
  "case_id": "EC_number_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C11",
      "C12",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry E7FHH1 (ASOR_PYRFU, Pyrococcus furiosus) carries EC 1.97.1.13 with experimental evidence codes (ECO:0000269) from PubMed:16199576 and PubMed:36269456. The catalytic reaction (aliphatic sulfonate + 4 oxidized ferredoxin + 2 H2O → 4 reduced ferredoxin + carboxylate + sulfite + 6H+) is supported by X-ray crystallography (PDB 6X1O, 6X6U) and biochemical characterization. The benchmark sequence SHA256 matches the source entry exactly."
  },
  "important_caveats": [
    "The protein was originally characterized as WOR5 (tungsten-containing aldehyde oxidoreductase) in 2005; the sulfonate desulfonase EC assignment came only in 2022. Models trained on earlier data might have a different annotation.",
    "The existence and exact definition of EC 1.97.1.14 could not be independently verified from the supplied evidence; if it is a non-existent or fabricated EC number, option B would be trivially eliminable, making the question more answerable.",
    "The GADHT motif confirms WOR-family membership but is shared with AOR, FOR, POR, and other family members, so it cannot resolve the 4th-digit EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the experimental data for 1.97.1.13 is known, only A is correct. C and D are clearly wrong by EC class. B (1.97.1.14) would only be defensible if one knew it applied to a different reaction/protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"EC_number_0174","expected_answer_check":{"judgment":"supported","reason":"UniProtKB entry E7FHH1 (ASOR_PYRFU, Pyrococcus furiosus) carries EC 1.97.1.13 with experimental evidence codes (ECO:0000269) from PubMed:16199576 and PubMed:36269456. The catalytic reaction (aliphatic sulfonate + 4 oxidized ferredoxin + 2 H2O → 4 reduced ferredoxin + carboxylate + sulfite + 6H+) is supported by X-ray crystallography (PDB 6X1O, 6X6U) and biochemical characterization. The benchmark sequence SHA256 matches the source entry exactly.","evidence_ids":["C4","C5","C11","C12","H2","H5"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"A model can eliminate C (2.7.1.39, a kinase/transferase) and D (1.16.1.10, an Fe(II) oxidoreductase) using family-level knowledge: the GADHT motif and overall fold identify this as a tungsten-containing oxidoreductase (WOR/AOR family) that uses ferredoxin as electron acceptor (EC 1.97.x.x), not a transferase or an iron-donor enzyme. However, distinguishing A (1.97.1.13, aliphatic sulfonate oxidoreductase) from B (1.97.1.14) requires knowing the specific experimental substrate-specificity data for THIS protein. The GADHT motif and W/Mo cofactor binding residues are shared across the entire WOR family and do not encode which particular substrate (sulfonate vs. the substrate of 1.97.1.14) is acted upon. The 1.97.1.13 assignment was made in 2022 based on novel experimental characterization (PubMed:36269456) showing sulfonate desulfonation; prior to that, this protein was annotated as a generic aldehyde oxidoreductase. No sequence motif or family-level inference distinguishes the sulfonate desulfonase activity from other 1.97.1.x reactions.","missing_item_specific_fact":"The experimental demonstration (PubMed:36269456, 2022) that this specific protein catalyzes aliphatic sulfonate desulfonation (rather than the reaction assigned to EC 1.97.1.14), including the identification of active-site residues conferring sulfonate specificity, which is not derivable from sequence-level family motifs alone.","reason":"While family-level knowledge eliminates options C and D, the critical A-vs-B distinction (1.97.1.13 vs 1.97.1.14) requires the specific experimental characterization of this protein's substrate specificity published in 2022. The shared GADHT/WOR-family motifs do not encode the precise 4th-digit EC assignment."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"Once the experimental data for 1.97.1.13 is known, only A is correct. C and D are clearly wrong by EC class. B (1.97.1.14) would only be defensible if one knew it applied to a different reaction/protein."},"important_caveats":["The protein was originally characterized as WOR5 (tungsten-containing aldehyde oxidoreductase) in 2005; the sulfonate desulfonase EC assignment came only in 2022. Models trained on earlier data might have a different annotation.","The existence and exact definition of EC 1.97.1.14 could not be independently verified from the supplied evidence; if it is a non-existent or fabricated EC number, option B would be trivially eliminable, making the question more answerable.","The GADHT motif confirms WOR-family membership but is shared with AOR, FOR, POR, and other family members, so it cannot resolve the 4th-digit EC assignment."]}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 624,
  "benchmark_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "current_entry_audit": {
    "entryVersion": 61,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 624,
  "current_source_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E7FHH1",
  "selected_historical_entry_version": 59,
  "selected_historical_record_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "selected_historical_source_sequence_length": 624,
  "selected_historical_source_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "selected_historical_version": {
    "accession": "E7FHH1",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASOR_PYRFU",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E7FHH1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":61,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Pyrococcus\"],\"scientificName\":\"Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1)\",\"taxonId\":186497}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"Aliphatic sulfonate ferredoxin oxidoreductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"ASOR\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"Tungsten-containing aldehyde oxidoreductase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"WOR5\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5 large subunit\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5-L\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"1.97.1.13\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aliphatic sulfonate oxidoreductase, WOR-like subunit\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.97.1.13\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80643\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29067\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231625\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"an aliphatic sulfonate + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + an aldehyde + sulfite + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80647\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17478\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231625\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"2 oxidized [4Fe-4S]-[ferredoxin] + an aldehyde + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80651\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17478\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29067\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80087\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57305\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:507393\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"2 oxidized [4Fe-4S]-[ferredoxin] + taurine + H2O = aminoacetaldehyde + 2 reduced [4Fe-4S]-[ferredoxin] + sulfite + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80635\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58213\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:507393\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"aminoacetaldehyde + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + glycine + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80639\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57305\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58213\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Bevers L.E.\",\"Bol E.\",\"Hagedoorn P.L.\",\"Hagen W.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16199576\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.187.20.7056-7061.2005\"}],\"citationType\":\"journal article\",\"firstPage\":\"7056\",\"id\":\"16199576\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"7061\",\"publicationDate\":\"2005\",\"title\":\"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus furiosus with a broad substrate specificity.\",\"volume\":\"187\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 43587 / DSM 3638 / JCM 8422 / Vc1\"}],\"referenceNumber\":3,\"referencePositions\":[\"PROTEIN SEQUENCE OF 1-21\",\"FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Mathew L.G.\",\"Haja D.K.\",\"Pritchett C.\",\"McCormick W.\",\"Zeineddine R.\",\"Fontenot L.S.\",\"Rivera M.E.\",\"Glushka J.\",\"Adams M.W.W.\",\"Lanzilotta W.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36269456\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00775-022-01965-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"747\",\"id\":\"36269456\",\"journal\":\"J. Biol. Inorg. Chem.\",\"lastPage\":\"758\",\"publicationDate\":\"2022\",\"title\":\"An unprecedented function for a tungsten-containing oxidoreductase.\",\"volume\":\"27\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X1O\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X6U\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"COM1\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR (4FE-4S) CLUSTER AND TUNGSTOPTERIN\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H1",
  "excerpt": "ID   ASOR_PYRFU              Reviewed;         624 AA.\nAC   E7FHH1; A0A5C0XQU4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};\nDE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nDE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};\nDE            Short=ASOR {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-L {ECO:0000303|PubMed:36269456};\nGN   Name=wor5 {ECO:0000303|PubMed:16199576};\nGN   OrderedLocusNames=PF1480 {ECO:0000312|EMBL:AAL81604.1};\nGN   ORFNames=PFDSM3638_07420 {ECO:0000312|EMBL:QEK79109.1};\nOS   Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Pyrococcus.\nOX   NCBI_TaxID=186497;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};\nDE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nDE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};\nDE            Short=ASOR {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-L {ECO:0000303|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   PROTEIN SEQUENCE OF 1-21, FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE, COFACTOR,\nRP   AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=ATCC 43587 / DSM 3638 / JCM 8422 / Vc1;\nRX   PubMed=16199576; DOI=10.1128/jb.187.20.7056-7061.2005;\nRA   Bevers L.E., Bol E., Hagedoorn P.L., Hagen W.R.;\nRT   \"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus\nRT   furiosus with a broad substrate specificity.\";\nRL   J. Bacteriol. 187:7056-7061(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6X1O, ECO:0007744|PDB:6X6U}\nRP   X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR\nRP   (4FE-4S) CLUSTER AND TUNGSTOPTERIN, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND SUBCELLULAR LOCATION.\nRC   STRAIN=COM1;\nRX   PubMed=36269456; DOI=10.1007/s00775-022-01965-0;\nRA   Mathew L.G., Haja D.K., Pritchett C., McCormick W., Zeineddine R.,\nRA   Fontenot L.S., Rivera M.E., Glushka J., Adams M.W.W., Lanzilotta W.N.;\nRT   \"An unprecedented function for a tungsten-containing oxidoreductase.\";\nRL   J. Biol. Inorg. Chem. 27:747-758(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2\nCC         H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6\nCC         H(+); Xref=Rhea:RHEA:80643, Rhea:RHEA-COMP:18797, Rhea:RHEA-\nCC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:29067, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723,\nCC         ChEBI:CHEBI:231625; EC=1.97.1.13;\nCC         Evidence={ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an aliphatic sulfonate + 2 oxidized [4Fe-4S]-[ferredoxin] +\nCC         H2O = 2 reduced [4Fe-4S]-[ferredoxin] + an aldehyde + sulfite + 3\nCC         H(+); Xref=Rhea:RHEA:80647, Rhea:RHEA-COMP:18797, Rhea:RHEA-\nCC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:17478, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723,\nCC         ChEBI:CHEBI:231625; Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 oxidized [4Fe-4S]-[ferredoxin] + an aldehyde + H2O = 2\nCC         reduced [4Fe-4S]-[ferredoxin] + a carboxylate + 3 H(+);\nCC         Xref=Rhea:RHEA:80651, Rhea:RHEA-COMP:18797, Rhea:RHEA-COMP:18798,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17478,\nCC         ChEBI:CHEBI:29067, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723;\nCC         Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced\nCC         [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+);\nCC         Xref=Rhea:RHEA:80087, Rhea:RHEA-COMP:18797, Rhea:RHEA-COMP:18798,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:33722, ChEBI:CHEBI:33723, ChEBI:CHEBI:57305,\nCC         ChEBI:CHEBI:507393; Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 oxidized [4Fe-4S]-[ferredoxin] + taurine + H2O =\nCC         aminoacetaldehyde + 2 reduced [4Fe-4S]-[ferredoxin] + sulfite + 3\nCC         H(+); Xref=Rhea:RHEA:80635, Rhea:RHEA-COMP:18797, Rhea:RHEA-\nCC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:33722, ChEBI:CHEBI:33723, ChEBI:CHEBI:58213,\nCC         ChEBI:CHEBI:507393; Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H10",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=aminoacetaldehyde + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2\nCC         reduced [4Fe-4S]-[ferredoxin] + glycine + 3 H(+);\nCC         Xref=Rhea:RHEA:80639, Rhea:RHEA-COMP:18797, Rhea:RHEA-COMP:18798,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:33722,\nCC         ChEBI:CHEBI:33723, ChEBI:CHEBI:57305, ChEBI:CHEBI:58213;\nCC         Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 174. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
