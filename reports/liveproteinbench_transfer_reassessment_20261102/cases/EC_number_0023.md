# EC_number_0023

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0023.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSFTTLLTAVATAVSAVTASPLEALKRGIQPGTGVHDGYFYSFWTDGRGYVDFNNGPRGSYRVSWSNVNNWVGGKGWNPGPPRRIAYNGTWNNWNVNSYLALYGWTTNPLVEYYIVEAYGSYNPSSGAARLGTIEDDGGVYDIYRTRRINQPSIIGTASFDQYWSVRRQKRVGGTIDTGKHFDEWRRQGNLQLGAWNYMIMATEGYQSSGSAEIEVRSLD

[Multiple Choices]
A. 3.2.1.18
B. 3.2.1.8
C. 4.2.1.121
D. 2.7.11.11
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

> The sequence-matched UniProt record assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans, citing experimental evidence (ECO:0000269). The historical record also carries this assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a short N-terminal signal-peptide-like region followed by a compact, roughly 200-residue fungal glycoside-hydrolase domain. Its length and sequence pattern are characteristic of secreted GH11 xylanases, which are endo-1,4-beta-xylanases (EC 3.2.1.8). That family-level inference distinguishes B from the unrelated sialidase-like, lyase, and kinase alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices include the characteristic EC activity of the inferred enzyme family, so transferable family knowledge gives a meaningful basis to select B without needing this exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe substantially different enzyme activities, and the sequence supports the xylanase choice.


### Important caveats

- The family-level sequence inference supports the choice probabilistically; the reviewer-only record provides the sequence-matched, experimentally supported annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a short N-terminal signal-peptide-like region followed by a compact, roughly 200-residue fungal glycoside-hydrolase domain. Its length and sequence pattern are characteristic of secreted GH11 xylanases, which are endo-1,4-beta-xylanases (EC 3.2.1.8). That family-level inference distinguishes B from the unrelated sialidase-like, lyase, and kinase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices include the characteristic EC activity of the inferred enzyme family, so transferable family knowledge gives a meaningful basis to select B without needing this exact protein's recorded annotation."
  },
  "case_id": "EC_number_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans, citing experimental evidence (ECO:0000269). The historical record also carries this assignment."
  },
  "important_caveats": [
    "The family-level sequence inference supports the choice probabilistically; the reviewer-only record provides the sequence-matched, experimentally supported annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe substantially different enzyme activities, and the sequence supports the xylanase choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans, citing experimental evidence (ECO:0000269). The historical record also carries this assignment.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a short N-terminal signal-peptide-like region followed by a compact, roughly 200-residue fungal glycoside-hydrolase domain. Its length and sequence pattern are characteristic of secreted GH11 xylanases, which are endo-1,4-beta-xylanases (EC 3.2.1.8). That family-level inference distinguishes B from the unrelated sialidase-like, lyase, and kinase alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices include the characteristic EC activity of the inferred enzyme family, so transferable family knowledge gives a meaningful basis to select B without needing this exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe substantially different enzyme activities, and the sequence supports the xylanase choice."
  },
  "important_caveats": [
    "The family-level sequence inference supports the choice probabilistically; the reviewer-only record provides the sequence-matched, experimentally supported annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry V9TS54 (XY11A_HUMIN) is annotated as Endo-1,4-beta-xylanase 11A with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed 24262572). The sequence matches exactly (221 aa, SHA256 confirmed). The catalytic activity is described as endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans, consistent with EC 3.2.1.8.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmark features of Glycoside Hydrolase family 11 (GH11) xylanases: (1) small mature size (~190 aa after signal peptide cleavage), consistent with the ~200 aa GH11 fold; (2) multiple conserved 'WNNW' tryptophan motifs (visible at positions forming 'WNNWVGGKGWNPGPPRRIAYNGTWNNWNVNSYLALYGWTTNPLVEYYIVEAYGSYNPSSG'), which create the characteristic beta-jellyroll xylan-binding groove; (3) an aromatic-rich surface (multiple W, Y, F residues) typical of carbohydrate-binding sites; (4) the conserved 'GKHFDEWRRQ' region containing the catalytic glutamate. These features are well-established transferable knowledge from the GH11 family. Among the choices: EC 3.2.1.8 (xylanase, GH11) matches perfectly; EC 3.2.1.18 (arabinofuranosidase, GH43/51/54/62/93) has a completely different fold and lacks WNNW motifs; EC 4.2.1.121 (lyase) involves elimination chemistry incompatible with a glycoside hydrolase fold; EC 2.7.11.11 (kinase) requires a phosphotransferase fold with ATP-binding motifs absent here. The WNNW motif pattern alone is a strong GH11 diagnostic that distinguishes B from all other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the GH11 xylanase family from the conserved WNNW tryptophan motifs, small protein size, and aromatic-rich binding surface. These are well-characterized family-level features learned from many GH11 xylanases across organisms. The distractors represent completely different enzyme classes (lyase, kinase) or a different GH family (arabinofuranosidase) with incompatible folds and motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different EC top-level classes (3=hydrolase, 4=lyase, 2=transferase), making elimination of C and D straightforward from the sequence's hydrolase-like architecture. Within EC 3.2.1.x, the GH11-specific WNNW motifs clearly distinguish xylanase (B) from arabinofuranosidase (A).


### Important caveats

- The evidence code ECO:0000269 indicates experimental determination of catalytic activity, strengthening the annotation.
- The protein is a precursor (signal peptide present); the mature enzyme is ~190 aa, consistent with typical GH11 xylanase size.
- The WNNW motif recognition is a well-established family-level diagnostic used across many GH11 members and does not require memorizing this specific protein's record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmark features of Glycoside Hydrolase family 11 (GH11) xylanases: (1) small mature size (~190 aa after signal peptide cleavage), consistent with the ~200 aa GH11 fold; (2) multiple conserved 'WNNW' tryptophan motifs (visible at positions forming 'WNNWVGGKGWNPGPPRRIAYNGTWNNWNVNSYLALYGWTTNPLVEYYIVEAYGSYNPSSG'), which create the characteristic beta-jellyroll xylan-binding groove; (3) an aromatic-rich surface (multiple W, Y, F residues) typical of carbohydrate-binding sites; (4) the conserved 'GKHFDEWRRQ' region containing the catalytic glutamate. These features are well-established transferable knowledge from the GH11 family. Among the choices: EC 3.2.1.8 (xylanase, GH11) matches perfectly; EC 3.2.1.18 (arabinofuranosidase, GH43/51/54/62/93) has a completely different fold and lacks WNNW motifs; EC 4.2.1.121 (lyase) involves elimination chemistry incompatible with a glycoside hydrolase fold; EC 2.7.11.11 (kinase) requires a phosphotransferase fold with ATP-binding motifs absent here. The WNNW motif pattern alone is a strong GH11 diagnostic that distinguishes B from all other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the GH11 xylanase family from the conserved WNNW tryptophan motifs, small protein size, and aromatic-rich binding surface. These are well-characterized family-level features learned from many GH11 xylanases across organisms. The distractors represent completely different enzyme classes (lyase, kinase) or a different GH family (arabinofuranosidase) with incompatible folds and motifs."
  },
  "case_id": "EC_number_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry V9TS54 (XY11A_HUMIN) is annotated as Endo-1,4-beta-xylanase 11A with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed 24262572). The sequence matches exactly (221 aa, SHA256 confirmed). The catalytic activity is described as endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans, consistent with EC 3.2.1.8."
  },
  "important_caveats": [
    "The evidence code ECO:0000269 indicates experimental determination of catalytic activity, strengthening the annotation.",
    "The protein is a precursor (signal peptide present); the mature enzyme is ~190 aa, consistent with typical GH11 xylanase size.",
    "The WNNW motif recognition is a well-established family-level diagnostic used across many GH11 members and does not require memorizing this specific protein's record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC top-level classes (3=hydrolase, 4=lyase, 2=transferase), making elimination of C and D straightforward from the sequence's hydrolase-like architecture. Within EC 3.2.1.x, the GH11-specific WNNW motifs clearly distinguish xylanase (B) from arabinofuranosidase (A)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry V9TS54 (XY11A_HUMIN) is annotated as Endo-1,4-beta-xylanase 11A with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed 24262572). The sequence matches exactly (221 aa, SHA256 confirmed). The catalytic activity is described as endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans, consistent with EC 3.2.1.8.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmark features of Glycoside Hydrolase family 11 (GH11) xylanases: (1) small mature size (~190 aa after signal peptide cleavage), consistent with the ~200 aa GH11 fold; (2) multiple conserved 'WNNW' tryptophan motifs (visible at positions forming 'WNNWVGGKGWNPGPPRRIAYNGTWNNWNVNSYLALYGWTTNPLVEYYIVEAYGSYNPSSG'), which create the characteristic beta-jellyroll xylan-binding groove; (3) an aromatic-rich surface (multiple W, Y, F residues) typical of carbohydrate-binding sites; (4) the conserved 'GKHFDEWRRQ' region containing the catalytic glutamate. These features are well-established transferable knowledge from the GH11 family. Among the choices: EC 3.2.1.8 (xylanase, GH11) matches perfectly; EC 3.2.1.18 (arabinofuranosidase, GH43/51/54/62/93) has a completely different fold and lacks WNNW motifs; EC 4.2.1.121 (lyase) involves elimination chemistry incompatible with a glycoside hydrolase fold; EC 2.7.11.11 (kinase) requires a phosphotransferase fold with ATP-binding motifs absent here. The WNNW motif pattern alone is a strong GH11 diagnostic that distinguishes B from all other options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the GH11 xylanase family from the conserved WNNW tryptophan motifs, small protein size, and aromatic-rich binding surface. These are well-characterized family-level features learned from many GH11 xylanases across organisms. The distractors represent completely different enzyme classes (lyase, kinase) or a different GH family (arabinofuranosidase) with incompatible folds and motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC top-level classes (3=hydrolase, 4=lyase, 2=transferase), making elimination of C and D straightforward from the sequence's hydrolase-like architecture. Within EC 3.2.1.x, the GH11-specific WNNW motifs clearly distinguish xylanase (B) from arabinofuranosidase (A)."
  },
  "important_caveats": [
    "The evidence code ECO:0000269 indicates experimental determination of catalytic activity, strengthening the annotation.",
    "The protein is a precursor (signal peptide present); the mature enzyme is ~190 aa, consistent with typical GH11 xylanase size.",
    "The WNNW motif recognition is a well-established family-level diagnostic used across many GH11 members and does not require memorizing this specific protein's record."
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
  "benchmark_sequence_length": 221,
  "benchmark_sequence_sha256": "6e283cc779810dd9174f1b61924b8c74d0bd81ae7161f1184006352195efc500",
  "current_entry_audit": {
    "entryVersion": 41,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 221,
  "current_source_sequence_sha256": "6e283cc779810dd9174f1b61924b8c74d0bd81ae7161f1184006352195efc500",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 39,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "V9TS54",
  "selected_historical_entry_version": 39,
  "selected_historical_record_sha256": "a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34",
  "selected_historical_source_sequence_length": 221,
  "selected_historical_source_sequence_sha256": "6e283cc779810dd9174f1b61924b8c74d0bd81ae7161f1184006352195efc500",
  "selected_historical_version": {
    "accession": "V9TS54",
    "database": "Swiss-Prot",
    "entryVersion": 39,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XY11A_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"V9TS54\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":41,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase 11A\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase 11A\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Xylanase 11A\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.\",\"Shi P.\",\"Huang H.\",\"Luo H.\",\"Wang Y.\",\"Zhang W.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24262572\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.foodchem.2013.10.062\"}],\"citationType\":\"journal article\",\"firstPage\":\"381\",\"id\":\"24262572\",\"journal\":\"Food Chem.\",\"lastPage\":\"387\",\"publicationDate\":\"2014\",\"title\":\"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and one GH11 xylanase from Humicola insolens and their synergy in the degradation of xylan.\",\"volume\":\"148\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:30.137210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e",
  "url": "https://rest.uniprot.org/uniprotkb/V9TS54.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H1",
  "excerpt": "ID   XY11A_HUMIN             Reviewed;         221 AA.\nAC   V9TS54;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   18-JUN-2025, entry version 39.\nDE   RecName: Full=Endo-1,4-beta-xylanase 11A {ECO:0000303|PubMed:24262572};\nDE            Short=Xylanase 11A {ECO:0000303|PubMed:24262572};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:24262572};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase 11A {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=Xyn11A {ECO:0000303|PubMed:24262572};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:53.416982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34",
  "url": "https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Endo-1,4-beta-xylanase 11A {ECO:0000303|PubMed:24262572};\nDE            Short=Xylanase 11A {ECO:0000303|PubMed:24262572};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:24262572};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase 11A {ECO:0000305};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:53.416982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34",
  "url": "https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=24262572; DOI=10.1016/j.foodchem.2013.10.062;\nRA   Yang X., Shi P., Huang H., Luo H., Wang Y., Zhang W., Yao B.;\nRT   \"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and\nRT   one GH11 xylanase from Humicola insolens and their synergy in the\nRT   degradation of xylan.\";\nRL   Food Chem. 148:381-387(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:53.416982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34",
  "url": "https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:24262572};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:53.416982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34",
  "url": "https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
