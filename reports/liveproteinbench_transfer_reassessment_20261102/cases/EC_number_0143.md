# EC_number_0143

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0143.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 1.14.15.9

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTNELSNAAGASQQGPAASSFSADTPPRTTAGGDVLVLLLIDVAPAARLWGYGRFVAGTTPALGEPGARFAKQLGTGYEGGFGLRPSATRQGLFVLFEDEAAADAFIGRSELVQTYRRNARELCIVKARPYSARGSWDGQKLRVGSPAPVDGPVAALTRASIRPSQAHRFWPNAGPSQDSLERAAGCRLAVGLGEAPFLRQATFSVWDSVAAMDAYARTGAHQRAIVASRDFFSESMFVRFVPLSIEGVWKGRRYG

[Multiple Choices]
A. 1.14.14.126
B. 1.1.1.17
C. 1.14.15.9
D. 1.14.18.1
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

> The sequence matches the UniProt sequence, and the matched entry assigns EC 1.14.15.9 to a catalytic reaction with experimental evidence (ECO:0000269, PubMed:19136077). This supports the keyed EC number for the supplied protein.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model could recognize the compact bacterial sequence as belonging to the CrtA-like carotenoid oxygenase/ketolase family from transferable sequence-family patterns. That family-level association points to carotenoid monooxygenation, making C a meaningful fit among the choices; the alcohol dehydrogenase option is a different reaction class, and the other oxygenase choices describe different enzyme activities.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The precise EC assignment is supported by the source record, but a transferable family-recognition argument can meaningfully distinguish C without relying on that record. Sequence-based family recognition does not guarantee the complete EC number, so the inference is probabilistic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported for a CrtA-like carotenoid oxygenase.


### Important caveats

- The source’s EC assignment is linked to experimental evidence, but the primary study was not independently reviewed here.
- The family-level inference supports the choice among these alternatives; it is not an independent experimental confirmation of every substrate or reaction detail.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize the compact bacterial sequence as belonging to the CrtA-like carotenoid oxygenase/ketolase family from transferable sequence-family patterns. That family-level association points to carotenoid monooxygenation, making C a meaningful fit among the choices; the alcohol dehydrogenase option is a different reaction class, and the other oxygenase choices describe different enzyme activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The precise EC assignment is supported by the source record, but a transferable family-recognition argument can meaningfully distinguish C without relying on that record. Sequence-based family recognition does not guarantee the complete EC number, so the inference is probabilistic."
  },
  "case_id": "EC_number_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt sequence, and the matched entry assigns EC 1.14.15.9 to a catalytic reaction with experimental evidence (ECO:0000269, PubMed:19136077). This supports the keyed EC number for the supplied protein."
  },
  "important_caveats": [
    "The source’s EC assignment is linked to experimental evidence, but the primary study was not independently reviewed here.",
    "The family-level inference supports the choice among these alternatives; it is not an independent experimental confirmation of every substrate or reaction detail."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported for a CrtA-like carotenoid oxygenase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt sequence, and the matched entry assigns EC 1.14.15.9 to a catalytic reaction with experimental evidence (ECO:0000269, PubMed:19136077). This supports the keyed EC number for the supplied protein.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could recognize the compact bacterial sequence as belonging to the CrtA-like carotenoid oxygenase/ketolase family from transferable sequence-family patterns. That family-level association points to carotenoid monooxygenation, making C a meaningful fit among the choices; the alcohol dehydrogenase option is a different reaction class, and the other oxygenase choices describe different enzyme activities.",
    "missing_item_specific_fact": "",
    "reason": "The precise EC assignment is supported by the source record, but a transferable family-recognition argument can meaningfully distinguish C without relying on that record. Sequence-based family recognition does not guarantee the complete EC number, so the inference is probabilistic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported for a CrtA-like carotenoid oxygenase."
  },
  "important_caveats": [
    "The source’s EC assignment is linked to experimental evidence, but the primary study was not independently reviewed here.",
    "The family-level inference supports the choice among these alternatives; it is not an independent experimental confirmation of every substrate or reaction detail."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q83YH3 (CRTA_RUBGE) assigns EC 1.14.15.9 with evidence code ECO:0000269 (experimental evidence) from PubMed:19136077 (Gerjets et al. 2009, Biochim. Biophys. Acta). Multiple catalytic activity reactions are explicitly listed under EC 1.14.15.9, including spheroidene → spheroiden-2-one and spirilloxanthin → 2-oxospirilloxanthin, all supported by experimental characterization of the expressed protein. The sequence matches exactly (SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C18](#evidence-c18), [H2](#evidence-h2), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options represent structurally and mechanistically distinct enzyme classes with well-known diagnostic sequence features: (A) EC 1.14.14.126 is a P450 monooxygenase requiring the highly conserved heme-binding motif FxxGxxxCxG (a conserved Cys ligating heme iron) — this motif is absent from the sequence; (B) EC 1.1.1.17 is an alcohol dehydrogenase requiring a Rossmann-fold NAD-binding motif (GxxGxxG) and is typically 350–400 aa — the 256-aa sequence lacks this fold and is too short; (D) EC 1.14.18.1 is a laccase (multicopper oxidase) requiring multiple copper-binding motifs (HxH, HCH, HxxH) and is typically 500–700 aa — these motifs and the required size are absent. By elimination, the remaining option (C, EC 1.14.15.9) belongs to the carotenoid monooxygenase/2-ketolase family (CrtA/CrtF/CrtZ/CrtY/CrtW), which are ~200–300 aa ferritin-like diiron proteins that use reduced ferredoxin as electron donor. The 256-aa length, hydrophobic character, and presence of multiple His and Glu residues consistent with diiron coordination in the ferritin-like fold are positive features matching this family. Since only one 1.14.15.- option is offered, the model need not distinguish among sub-EC numbers within that class.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of options A, B, and D relies on the well-established absence of their defining structural motifs (P450 heme-binding Cys, Rossmann fold, multicopper oxidase copper ligands), which is standard transferable knowledge. The positive identification as a carotenoid hydroxylase/monooxygenase (EC 1.14.15.-) uses family-level recognition of size, hydrophobicity, and diiron-coordination residue patterns shared across CrtA/CrtF/CrtZ homologs. This constitutes legitimate family-level inference rather than lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct EC subclasses (1.14.14.-, 1.1.1.-, 1.14.15.-, 1.14.18.-) with mutually exclusive structural requirements. The sequence clearly lacks P450, ADH, and laccase signatures while being consistent with the carotenoid hydroxylase family, leaving only one defensible choice.


### Important caveats

- The specific fourth-digit assignment (1.14.15.9 vs. other 1.14.15.- enzymes) would require substrate-level knowledge, but this is moot here since only one 1.14.15.- option is offered.
- The CRD/carotenoid hydroxylase family is less universally recognizable by a single short motif compared to P450s, so the positive identification of C relies partly on elimination rather than a single diagnostic motif.
- The experimental evidence (ECO:0000269) for EC 1.14.15.9 comes from in vitro characterization of the expressed protein (Gerjets et al. 2009), not from the original genome sequence annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options represent structurally and mechanistically distinct enzyme classes with well-known diagnostic sequence features: (A) EC 1.14.14.126 is a P450 monooxygenase requiring the highly conserved heme-binding motif FxxGxxxCxG (a conserved Cys ligating heme iron) — this motif is absent from the sequence; (B) EC 1.1.1.17 is an alcohol dehydrogenase requiring a Rossmann-fold NAD-binding motif (GxxGxxG) and is typically 350–400 aa — the 256-aa sequence lacks this fold and is too short; (D) EC 1.14.18.1 is a laccase (multicopper oxidase) requiring multiple copper-binding motifs (HxH, HCH, HxxH) and is typically 500–700 aa — these motifs and the required size are absent. By elimination, the remaining option (C, EC 1.14.15.9) belongs to the carotenoid monooxygenase/2-ketolase family (CrtA/CrtF/CrtZ/CrtY/CrtW), which are ~200–300 aa ferritin-like diiron proteins that use reduced ferredoxin as electron donor. The 256-aa length, hydrophobic character, and presence of multiple His and Glu residues consistent with diiron coordination in the ferritin-like fold are positive features matching this family. Since only one 1.14.15.- option is offered, the model need not distinguish among sub-EC numbers within that class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of options A, B, and D relies on the well-established absence of their defining structural motifs (P450 heme-binding Cys, Rossmann fold, multicopper oxidase copper ligands), which is standard transferable knowledge. The positive identification as a carotenoid hydroxylase/monooxygenase (EC 1.14.15.-) uses family-level recognition of size, hydrophobicity, and diiron-coordination residue patterns shared across CrtA/CrtF/CrtZ homologs. This constitutes legitimate family-level inference rather than lookup of this specific protein's annotation."
  },
  "case_id": "EC_number_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C18",
      "H2",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q83YH3 (CRTA_RUBGE) assigns EC 1.14.15.9 with evidence code ECO:0000269 (experimental evidence) from PubMed:19136077 (Gerjets et al. 2009, Biochim. Biophys. Acta). Multiple catalytic activity reactions are explicitly listed under EC 1.14.15.9, including spheroidene → spheroiden-2-one and spirilloxanthin → 2-oxospirilloxanthin, all supported by experimental characterization of the expressed protein. The sequence matches exactly (SHA256 confirmed)."
  },
  "important_caveats": [
    "The specific fourth-digit assignment (1.14.15.9 vs. other 1.14.15.- enzymes) would require substrate-level knowledge, but this is moot here since only one 1.14.15.- option is offered.",
    "The CRD/carotenoid hydroxylase family is less universally recognizable by a single short motif compared to P450s, so the positive identification of C relies partly on elimination rather than a single diagnostic motif.",
    "The experimental evidence (ECO:0000269) for EC 1.14.15.9 comes from in vitro characterization of the expressed protein (Gerjets et al. 2009), not from the original genome sequence annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct EC subclasses (1.14.14.-, 1.1.1.-, 1.14.15.-, 1.14.18.-) with mutually exclusive structural requirements. The sequence clearly lacks P450, ADH, and laccase signatures while being consistent with the carotenoid hydroxylase family, leaving only one defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q83YH3 (CRTA_RUBGE) assigns EC 1.14.15.9 with evidence code ECO:0000269 (experimental evidence) from PubMed:19136077 (Gerjets et al. 2009, Biochim. Biophys. Acta). Multiple catalytic activity reactions are explicitly listed under EC 1.14.15.9, including spheroidene → spheroiden-2-one and spirilloxanthin → 2-oxospirilloxanthin, all supported by experimental characterization of the expressed protein. The sequence matches exactly (SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C18", "H2", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options represent structurally and mechanistically distinct enzyme classes with well-known diagnostic sequence features: (A) EC 1.14.14.126 is a P450 monooxygenase requiring the highly conserved heme-binding motif FxxGxxxCxG (a conserved Cys ligating heme iron) — this motif is absent from the sequence; (B) EC 1.1.1.17 is an alcohol dehydrogenase requiring a Rossmann-fold NAD-binding motif (GxxGxxG) and is typically 350–400 aa — the 256-aa sequence lacks this fold and is too short; (D) EC 1.14.18.1 is a laccase (multicopper oxidase) requiring multiple copper-binding motifs (HxH, HCH, HxxH) and is typically 500–700 aa — these motifs and the required size are absent. By elimination, the remaining option (C, EC 1.14.15.9) belongs to the carotenoid monooxygenase/2-ketolase family (CrtA/CrtF/CrtZ/CrtY/CrtW), which are ~200–300 aa ferritin-like diiron proteins that use reduced ferredoxin as electron donor. The 256-aa length, hydrophobic character, and presence of multiple His and Glu residues consistent with diiron coordination in the ferritin-like fold are positive features matching this family. Since only one 1.14.15.- option is offered, the model need not distinguish among sub-EC numbers within that class.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of options A, B, and D relies on the well-established absence of their defining structural motifs (P450 heme-binding Cys, Rossmann fold, multicopper oxidase copper ligands), which is standard transferable knowledge. The positive identification as a carotenoid hydroxylase/monooxygenase (EC 1.14.15.-) uses family-level recognition of size, hydrophobicity, and diiron-coordination residue patterns shared across CrtA/CrtF/CrtZ homologs. This constitutes legitimate family-level inference rather than lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct EC subclasses (1.14.14.-, 1.1.1.-, 1.14.15.-, 1.14.18.-) with mutually exclusive structural requirements. The sequence clearly lacks P450, ADH, and laccase signatures while being consistent with the carotenoid hydroxylase family, leaving only one defensible choice."
  },
  "important_caveats": [
    "The specific fourth-digit assignment (1.14.15.9 vs. other 1.14.15.- enzymes) would require substrate-level knowledge, but this is moot here since only one 1.14.15.- option is offered.",
    "The CRD/carotenoid hydroxylase family is less universally recognizable by a single short motif compared to P450s, so the positive identification of C relies partly on elimination rather than a single diagnostic motif.",
    "The experimental evidence (ECO:0000269) for EC 1.14.15.9 comes from in vitro characterization of the expressed protein (Gerjets et al. 2009), not from the original genome sequence annotation."
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
  "benchmark_sequence_length": 256,
  "benchmark_sequence_sha256": "a65db65812f53b7088d2d99b943e650ad4c0d7b76ec0cdde3b3dcfcb5bf162d5",
  "current_entry_audit": {
    "entryVersion": 42,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 256,
  "current_source_sequence_sha256": "a65db65812f53b7088d2d99b943e650ad4c0d7b76ec0cdde3b3dcfcb5bf162d5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 41,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q83YH3",
  "selected_historical_entry_version": 41,
  "selected_historical_record_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "selected_historical_source_sequence_length": 256,
  "selected_historical_source_sequence_sha256": "a65db65812f53b7088d2d99b943e650ad4c0d7b76ec0cdde3b3dcfcb5bf162d5",
  "selected_historical_version": {
    "accession": "Q83YH3",
    "database": "Swiss-Prot",
    "entryVersion": 41,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "CRTA_RUBGE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q83YH3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":42,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rhodocyclus gelatinosus\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Sphaerotilaceae\",\"Rubrivivax\"],\"scientificName\":\"Rubrivivax gelatinosus\",\"synonyms\":[\"Rhodopseudomonas gelatinosa\"],\"taxonId\":28068}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"value\":\"Acyclic carotenoid 2-ketolase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Spheroidene/spirilloxanthin monooxygenase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"value\":\"1.14.15.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"12664193\",\"source\":\"PubMed\"}],\"value\":\"Spheroidene monooxygenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:33028\"}}],\"reaction\":{\"ecNumber\":\"1.14.15.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"spheroidene + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = spheroiden-2-one + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:33027\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35330\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:62480\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:33040\"}}],\"reaction\":{\"ecNumber\":\"1.14.15.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"spirilloxanthin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = 2-oxospirilloxanthin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:33039\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35328\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64792\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:33036\"}}],\"reaction\":{\"ecNumber\":\"1.14.15.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"2-oxospirilloxanthin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = 2,2'-dioxospirilloxanthin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:33035\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64792\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64793\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49329\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"spheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2-hydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49328\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35330\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91221\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49333\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"2-hydroxyspheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49332\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91221\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91223\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49337\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"2,2-dihydroxyspheroidene = spheroiden-2-one + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49336\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:62480\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91223\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49341\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"spirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2-hydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49340\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35328\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91227\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/7",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49345\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"2-hydroxyspirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49344\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91227\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91228\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/8",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49349\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"2,2-dihydroxyspirilloxanthin = 2-oxospirilloxanthin + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49348\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64792\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91228\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/9",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49353\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2'-hydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49352\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64792\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91229\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/10",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49357\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"2'-hydroxy-2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2',2'-dihydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49356\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91229\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91230\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/11",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49361\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"name\":\"2',2'-dihydroxy-2-oxospirilloxanthin = 2,2'-dioxospirilloxanthin + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49360\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64793\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91230\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/12",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Pinta V.\",\"Ouchane S.\",\"Picaud M.\",\"Takaichi S.\",\"Astier C.\",\"Reiss-Husson F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12664193\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00203-003-0538-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"354\",\"id\":\"12664193\",\"journal\":\"Arch. Microbiol.\",\"lastPage\":\"362\",\"publicationDate\":\"2003\",\"title\":\"Characterization of unusual hydroxy- and ketocarotenoids in Rubrivivax gelatinosus: involvement of enzyme CrtF or CrtA.\",\"volume\":\"179\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"S1\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"citation\":{\"authors\":[\"Gerjets T.\",\"Steiger S.\",\"Sandmann G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19136077\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbalip.2008.12.006\"}],\"citationType\":\"journal article\",\"firstPage\":\"125\",\"id\":\"19136077\",\"journal\":\"Biochim. Biophys. Acta\",\"lastPage\":\"131\",\"publicationDate\":\"2009\",\"title\":\"Catalytic properties of the expressed acyclic carotenoid 2-ketolases from Rhodobacter capsulatus and Rubrivivax gelatinosus.\",\"volume\":\"1791\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"S1\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H1",
  "excerpt": "ID   CRTA_RUBGE              Reviewed;         256 AA.\nAC   Q83YH3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2003, sequence version 1.\nDT   28-JAN-2026, entry version 41.\nDE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:12664193};\nDE            EC=1.14.15.9 {ECO:0000269|PubMed:19136077};\nDE   AltName: Full=Acyclic carotenoid 2-ketolase {ECO:0000303|PubMed:19136077};\nDE   AltName: Full=Spheroidene/spirilloxanthin monooxygenase {ECO:0000305};\nGN   Name=crtA {ECO:0000303|PubMed:8999844};\nOS   Rubrivivax gelatinosus (Rhodocyclus gelatinosus) (Rhodopseudomonas\nOS   gelatinosa).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Sphaerotilaceae; Rubrivivax.\nOX   NCBI_TaxID=28068;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:12664193};\nDE            EC=1.14.15.9 {ECO:0000269|PubMed:19136077};\nDE   AltName: Full=Acyclic carotenoid 2-ketolase {ECO:0000303|PubMed:19136077};\nDE   AltName: Full=Spheroidene/spirilloxanthin monooxygenase {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAO93123.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=S1;\nRX   PubMed=8999844; DOI=10.1074/jbc.272.3.1670;\nRA   Ouchane S., Picaud M., Vernotte C., Reiss-Husson F., Astier C.;\nRT   \"Pleiotropic effects of puf interposon mutagenesis on carotenoid\nRT   biosynthesis in Rubrivivax gelatinosus. A new gene organization in purple\nRT   bacteria.\";\nRL   J. Biol. Chem. 272:1670-1676(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=S1;\nRX   PubMed=12664193; DOI=10.1007/s00203-003-0538-3;\nRA   Pinta V., Ouchane S., Picaud M., Takaichi S., Astier C., Reiss-Husson F.;\nRT   \"Characterization of unusual hydroxy- and ketocarotenoids in Rubrivivax\nRT   gelatinosus: involvement of enzyme CrtF or CrtA.\";\nRL   Arch. Microbiol. 179:354-362(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H5",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=S1;\nRX   PubMed=19136077; DOI=10.1016/j.bbalip.2008.12.006;\nRA   Gerjets T., Steiger S., Sandmann G.;\nRT   \"Catalytic properties of the expressed acyclic carotenoid 2-ketolases from\nRT   Rhodobacter capsulatus and Rubrivivax gelatinosus.\";\nRL   Biochim. Biophys. Acta 1791:125-131(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=spheroidene + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+)\nCC         = spheroiden-2-one + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O;\nCC         Xref=Rhea:RHEA:33027, Rhea:RHEA-COMP:10000, Rhea:RHEA-COMP:10001,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:33737, ChEBI:CHEBI:33738, ChEBI:CHEBI:35330,\nCC         ChEBI:CHEBI:62480; EC=1.14.15.9;\nCC         Evidence={ECO:0000269|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33028;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=spirilloxanthin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4\nCC         H(+) = 2-oxospirilloxanthin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3\nCC         H2O; Xref=Rhea:RHEA:33039, Rhea:RHEA-COMP:10000, Rhea:RHEA-\nCC         COMP:10001, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:33737, ChEBI:CHEBI:33738, ChEBI:CHEBI:35328,\nCC         ChEBI:CHEBI:64792; EC=1.14.15.9;\nCC         Evidence={ECO:0000269|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33040;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2-oxospirilloxanthin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2\nCC         + 4 H(+) = 2,2'-dioxospirilloxanthin + 4 oxidized [2Fe-2S]-\nCC         [ferredoxin] + 3 H2O; Xref=Rhea:RHEA:33035, Rhea:RHEA-COMP:10000,\nCC         Rhea:RHEA-COMP:10001, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:33737, ChEBI:CHEBI:33738,\nCC         ChEBI:CHEBI:64792, ChEBI:CHEBI:64793; EC=1.14.15.9;\nCC         Evidence={ECO:0000269|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33036;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=spheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) =\nCC         2-hydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O;\nCC         Xref=Rhea:RHEA:49328, Rhea:RHEA-COMP:10000, Rhea:RHEA-COMP:10001,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:33737, ChEBI:CHEBI:33738, ChEBI:CHEBI:35330,\nCC         ChEBI:CHEBI:91221; Evidence={ECO:0000305|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49329;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H10",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2-hydroxyspheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 +\nCC         2 H(+) = 2,2-dihydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin]\nCC         + H2O; Xref=Rhea:RHEA:49332, Rhea:RHEA-COMP:10000, Rhea:RHEA-\nCC         COMP:10001, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:33737, ChEBI:CHEBI:33738, ChEBI:CHEBI:91221,\nCC         ChEBI:CHEBI:91223; Evidence={ECO:0000305|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49333;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H11",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2,2-dihydroxyspheroidene = spheroiden-2-one + H2O;\nCC         Xref=Rhea:RHEA:49336, ChEBI:CHEBI:15377, ChEBI:CHEBI:62480,\nCC         ChEBI:CHEBI:91223; Evidence={ECO:0000305|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49337;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H12",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=spirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2\nCC         H(+) = 2-hydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] +\nCC         H2O; Xref=Rhea:RHEA:49340, Rhea:RHEA-COMP:10000, Rhea:RHEA-\nCC         COMP:10001, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:33737, ChEBI:CHEBI:33738, ChEBI:CHEBI:35328,\nCC         ChEBI:CHEBI:91227; Evidence={ECO:0000305|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49341;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H13",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2-hydroxyspirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] +\nCC         O2 + 2 H(+) = 2,2-dihydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-\nCC         [ferredoxin] + H2O; Xref=Rhea:RHEA:49344, Rhea:RHEA-COMP:10000,\nCC         Rhea:RHEA-COMP:10001, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:33737, ChEBI:CHEBI:33738,\nCC         ChEBI:CHEBI:91227, ChEBI:CHEBI:91228;\nCC         Evidence={ECO:0000305|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49345;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H14",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2,2-dihydroxyspirilloxanthin = 2-oxospirilloxanthin + H2O;\nCC         Xref=Rhea:RHEA:49348, ChEBI:CHEBI:15377, ChEBI:CHEBI:64792,\nCC         ChEBI:CHEBI:91228; Evidence={ECO:0000305|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49349;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-125",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H15",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 +\nCC         2 H(+) = 2'-hydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-\nCC         [ferredoxin] + H2O; Xref=Rhea:RHEA:49352, Rhea:RHEA-COMP:10000,\nCC         Rhea:RHEA-COMP:10001, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:33737, ChEBI:CHEBI:33738,\nCC         ChEBI:CHEBI:64792, ChEBI:CHEBI:91229;\nCC         Evidence={ECO:0000305|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49353;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H16",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2'-hydroxy-2-oxospirilloxanthin + 2 reduced [2Fe-2S]-\nCC         [ferredoxin] + O2 + 2 H(+) = 2',2'-dihydroxy-2-oxospirilloxanthin + 2\nCC         oxidized [2Fe-2S]-[ferredoxin] + H2O; Xref=Rhea:RHEA:49356,\nCC         Rhea:RHEA-COMP:10000, Rhea:RHEA-COMP:10001, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:33737,\nCC         ChEBI:CHEBI:33738, ChEBI:CHEBI:91229, ChEBI:CHEBI:91230;\nCC         Evidence={ECO:0000305|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49357;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-145",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H17",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2',2'-dihydroxy-2-oxospirilloxanthin = 2,2'-\nCC         dioxospirilloxanthin + H2O; Xref=Rhea:RHEA:49360, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:64793, ChEBI:CHEBI:91230;\nCC         Evidence={ECO:0000305|PubMed:19136077};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49361;\nCC         Evidence={ECO:0000305|PubMed:19136077};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 146-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 143. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
