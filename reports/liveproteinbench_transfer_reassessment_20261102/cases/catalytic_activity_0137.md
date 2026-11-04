# catalytic_activity_0137

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0137.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — Endohydrolysis of (1-&gt;4)-beta-D-xylosidic linkages in xylans.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MITFSSLLVTFSAISTSLAIPGSILPKRSPMNFVLQRNESSLVRRATPNYEQDYTTGGDVIYTPSGSSFTVDWSTEDDFVVGLGWTTGSTNPINFSGTFGIGSGTALLSIYGWSENPLVEYYIVEDSASPPSFGTVKGSVTSDGSSYTIWENQRVNEPSIVGTATFNQYISVRSSPRKSGTVTVENHFQAWAALGMNLGTLNYQVLAVEGWGGEGAATQTVS

[Multiple Choices]
A. L-proline betaine + NADPH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NADP(+) + H2O
B. (2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl diphosphate
C. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
D. L-arginyl-[protein] + 2-oxoglutarate + O2 = (3R)-3-hydroxy-L-arginyl-[protein] + succinate + CO2
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The matched-sequence UniProt record assigns EC 3.2.1.8 and the same xylan-hydrolysis reaction as choice C. The cited evidence is a computational PROSITE-ProRule annotation, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the size and secreted-enzyme-like N-terminus of a fungal xylanase, along with sequence patterns consistent with a glycoside hydrolase. Transferable knowledge of fungal endo-xylanase families makes hydrolysis of xylan a credible inference. The other choices instead describe a small-molecule oxygenase, a farnesyl-diphosphate cyclization, or oxygen-dependent arginine hydroxylation, none of which fits this sequence as well.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition provides a meaningful basis for distinguishing C among the offered reactions, although the sequence alone does not establish the exact annotation with experimental certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct reaction classes, and the sequence supports a fungal xylanase-like enzyme rather than any of the other listed activities.


### Important caveats

- The reviewer-only evidence supports the key through a computational PROSITE-ProRule annotation; the excerpts do not establish direct experimental validation of this exact protein's catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the size and secreted-enzyme-like N-terminus of a fungal xylanase, along with sequence patterns consistent with a glycoside hydrolase. Transferable knowledge of fungal endo-xylanase families makes hydrolysis of xylan a credible inference. The other choices instead describe a small-molecule oxygenase, a farnesyl-diphosphate cyclization, or oxygen-dependent arginine hydroxylation, none of which fits this sequence as well.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition provides a meaningful basis for distinguishing C among the offered reactions, although the sequence alone does not establish the exact annotation with experimental certainty."
  },
  "case_id": "catalytic_activity_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record assigns EC 3.2.1.8 and the same xylan-hydrolysis reaction as choice C. The cited evidence is a computational PROSITE-ProRule annotation, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key through a computational PROSITE-ProRule annotation; the excerpts do not establish direct experimental validation of this exact protein's catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction classes, and the sequence supports a fungal xylanase-like enzyme rather than any of the other listed activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record assigns EC 3.2.1.8 and the same xylan-hydrolysis reaction as choice C. The cited evidence is a computational PROSITE-ProRule annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the size and secreted-enzyme-like N-terminus of a fungal xylanase, along with sequence patterns consistent with a glycoside hydrolase. Transferable knowledge of fungal endo-xylanase families makes hydrolysis of xylan a credible inference. The other choices instead describe a small-molecule oxygenase, a farnesyl-diphosphate cyclization, or oxygen-dependent arginine hydroxylation, none of which fits this sequence as well.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition provides a meaningful basis for distinguishing C among the offered reactions, although the sequence alone does not establish the exact annotation with experimental certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction classes, and the sequence supports a fungal xylanase-like enzyme rather than any of the other listed activities."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key through a computational PROSITE-ProRule annotation; the excerpts do not establish direct experimental validation of this exact protein's catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProtKB entry A0A384K474 (Swiss-Prot, reviewed) annotates this protein as EC 3.2.1.8 with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches the benchmark input exactly (222 aa, SHA-256 confirmed). The evidence code is ECO:0000255|PROSITE-ProRule:PRU01097, indicating a computational/prosite-based annotation rather than direct experimental kinetics, but the entry is in the curated Swiss-Prot section and the alternative name 'Endo-1,4-beta-xylanase EIX2' is consistent. The expected answer C exactly matches the database annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 222-amino-acid protein has a clear N-terminal hydrophobic signal peptide (MITFSSLLVTFSAISTSLAIPG), indicating a secreted enzyme. Among the four options: (A) P450 monooxygenases are typically 400–600 aa and require the heme-binding FxxGxxxCxG motif, which is absent; (B) terpene cyclases are typically 400–600 aa with DDXXD and NSE/DTE motifs, which are absent; (D) 2-oxoglutarate-dependent dioxygenases are typically 280–400+ aa with the HxD/E facial triad, which is not identifiable here. A 222 aa secreted protein lacking all of these motifs is far more consistent with a small fungal glycoside hydrolase such as a GH11 or GH12 xylanase (typically 180–250 aa, β-jelly-roll or β-sandwich fold, secreted by plant-pathogenic fungi). The sequence contains multiple GSG/GG/SG motifs and a compact fold consistent with small β-structure-rich glycosidases. By size, subcellular targeting, and absence of diagnostic motifs for the other three enzyme classes, option C is meaningfully distinguished.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use transferable knowledge about protein family size ranges, conserved catalytic motifs (P450 heme-binding, terpene cyclase DDXXD, Fe(II)/2-OG HxD/E triad), and the general principle that small secreted fungal proteins with β-rich folds and no cofactor-binding motifs are likely glycoside hydrolases. This eliminates A, B, and D and points to C without needing to recall the specific UniProt annotation for this exact sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The size and motif analysis cleanly eliminates A, B, and D. No other option is consistent with a 222 aa secreted protein lacking P450, terpene cyclase, or dioxygenase signatures.


### Important caveats

- The UniProt annotation for EC 3.2.1.8 is based on PROSITE-ProRule (ECO:0000255), a computational/pattern-based assignment, not direct experimental enzyme kinetics. The PubMed reference (33205907) describes EIX2 as an ethylene-inducing xylanase involved in plant perception, supporting the xylanase activity contextually.
- The reviewer-only evidence confirms the protein is from Botrytis cinerea (a plant-pathogenic fungus), but the evaluated model would not have this organism information from the original input alone.
- The model does not need to distinguish GH11 from GH12 specifically; the question only requires selecting among four very different enzyme classes, and the size/motif argument suffices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 222-amino-acid protein has a clear N-terminal hydrophobic signal peptide (MITFSSLLVTFSAISTSLAIPG), indicating a secreted enzyme. Among the four options: (A) P450 monooxygenases are typically 400–600 aa and require the heme-binding FxxGxxxCxG motif, which is absent; (B) terpene cyclases are typically 400–600 aa with DDXXD and NSE/DTE motifs, which are absent; (D) 2-oxoglutarate-dependent dioxygenases are typically 280–400+ aa with the HxD/E facial triad, which is not identifiable here. A 222 aa secreted protein lacking all of these motifs is far more consistent with a small fungal glycoside hydrolase such as a GH11 or GH12 xylanase (typically 180–250 aa, β-jelly-roll or β-sandwich fold, secreted by plant-pathogenic fungi). The sequence contains multiple GSG/GG/SG motifs and a compact fold consistent with small β-structure-rich glycosidases. By size, subcellular targeting, and absence of diagnostic motifs for the other three enzyme classes, option C is meaningfully distinguished.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use transferable knowledge about protein family size ranges, conserved catalytic motifs (P450 heme-binding, terpene cyclase DDXXD, Fe(II)/2-OG HxD/E triad), and the general principle that small secreted fungal proteins with β-rich folds and no cofactor-binding motifs are likely glycoside hydrolases. This eliminates A, B, and D and points to C without needing to recall the specific UniProt annotation for this exact sequence."
  },
  "case_id": "catalytic_activity_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProtKB entry A0A384K474 (Swiss-Prot, reviewed) annotates this protein as EC 3.2.1.8 with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches the benchmark input exactly (222 aa, SHA-256 confirmed). The evidence code is ECO:0000255|PROSITE-ProRule:PRU01097, indicating a computational/prosite-based annotation rather than direct experimental kinetics, but the entry is in the curated Swiss-Prot section and the alternative name 'Endo-1,4-beta-xylanase EIX2' is consistent. The expected answer C exactly matches the database annotation."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.2.1.8 is based on PROSITE-ProRule (ECO:0000255), a computational/pattern-based assignment, not direct experimental enzyme kinetics. The PubMed reference (33205907) describes EIX2 as an ethylene-inducing xylanase involved in plant perception, supporting the xylanase activity contextually.",
    "The reviewer-only evidence confirms the protein is from Botrytis cinerea (a plant-pathogenic fungus), but the evaluated model would not have this organism information from the original input alone.",
    "The model does not need to distinguish GH11 from GH12 specifically; the question only requires selecting among four very different enzyme classes, and the size/motif argument suffices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size and motif analysis cleanly eliminates A, B, and D. No other option is consistent with a 222 aa secreted protein lacking P450, terpene cyclase, or dioxygenase signatures."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProtKB entry A0A384K474 (Swiss-Prot, reviewed) annotates this protein as EC 3.2.1.8 with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches the benchmark input exactly (222 aa, SHA-256 confirmed). The evidence code is ECO:0000255|PROSITE-ProRule:PRU01097, indicating a computational/prosite-based annotation rather than direct experimental kinetics, but the entry is in the curated Swiss-Prot section and the alternative name 'Endo-1,4-beta-xylanase EIX2' is consistent. The expected answer C exactly matches the database annotation.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 222-amino-acid protein has a clear N-terminal hydrophobic signal peptide (MITFSSLLVTFSAISTSLAIPG), indicating a secreted enzyme. Among the four options: (A) P450 monooxygenases are typically 400–600 aa and require the heme-binding FxxGxxxCxG motif, which is absent; (B) terpene cyclases are typically 400–600 aa with DDXXD and NSE/DTE motifs, which are absent; (D) 2-oxoglutarate-dependent dioxygenases are typically 280–400+ aa with the HxD/E facial triad, which is not identifiable here. A 222 aa secreted protein lacking all of these motifs is far more consistent with a small fungal glycoside hydrolase such as a GH11 or GH12 xylanase (typically 180–250 aa, β-jelly-roll or β-sandwich fold, secreted by plant-pathogenic fungi). The sequence contains multiple GSG/GG/SG motifs and a compact fold consistent with small β-structure-rich glycosidases. By size, subcellular targeting, and absence of diagnostic motifs for the other three enzyme classes, option C is meaningfully distinguished.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use transferable knowledge about protein family size ranges, conserved catalytic motifs (P450 heme-binding, terpene cyclase DDXXD, Fe(II)/2-OG HxD/E triad), and the general principle that small secreted fungal proteins with β-rich folds and no cofactor-binding motifs are likely glycoside hydrolases. This eliminates A, B, and D and points to C without needing to recall the specific UniProt annotation for this exact sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size and motif analysis cleanly eliminates A, B, and D. No other option is consistent with a 222 aa secreted protein lacking P450, terpene cyclase, or dioxygenase signatures."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.2.1.8 is based on PROSITE-ProRule (ECO:0000255), a computational/pattern-based assignment, not direct experimental enzyme kinetics. The PubMed reference (33205907) describes EIX2 as an ethylene-inducing xylanase involved in plant perception, supporting the xylanase activity contextually.",
    "The reviewer-only evidence confirms the protein is from Botrytis cinerea (a plant-pathogenic fungus), but the evaluated model would not have this organism information from the original input alone.",
    "The model does not need to distinguish GH11 from GH12 specifically; the question only requires selecting among four very different enzyme classes, and the size/motif argument suffices."
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
  "benchmark_sequence_length": 222,
  "benchmark_sequence_sha256": "2265146ae5d59cb592dd036988cd6b2763b6251bd85f07a031b262ea02925786",
  "current_entry_audit": {
    "entryVersion": 27,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 222,
  "current_source_sequence_sha256": "2265146ae5d59cb592dd036988cd6b2763b6251bd85f07a031b262ea02925786",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 25,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384K474",
  "selected_historical_entry_version": 25,
  "selected_historical_record_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "selected_historical_source_sequence_length": 222,
  "selected_historical_source_sequence_sha256": "2265146ae5d59cb592dd036988cd6b2763b6251bd85f07a031b262ea02925786",
  "selected_historical_version": {
    "accession": "A0A384K474",
    "database": "Swiss-Prot",
    "entryVersion": 25,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX2_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384K474\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":27,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX2\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX21\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H1",
  "excerpt": "ID   EIX2_BOTFB              Reviewed;         222 AA.\nAC   A0A384K474;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 25.\nDE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX21 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX2 {ECO:0000303|PubMed:33205907}; ORFNames=BCIN_15g01600;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX21 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 137. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
