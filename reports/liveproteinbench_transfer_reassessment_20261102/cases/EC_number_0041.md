# EC_number_0041

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0041.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 3.2.1.8

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
A. 3.2.1.105
B. 4.2.3.1
C. 1.14.13.238
D. 3.2.1.8
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

> The sequence-matched UniProt annotation assigns EC 3.2.1.8 and describes endohydrolysis of beta-xylosidic linkages in xylans. The EC assignment is supported by a PROSITE-ProRule computational annotation, rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a likely N-terminal secretion signal followed by a compact fungal glycoside-hydrolase-sized domain. Its sequence is consistent with the small fungal endo-xylanase family, whose transferable family-level association supports EC 3.2.1.8. This distinguishes the xylanase choice from the offered oxidoreductase and lyase choices, and more specifically than secretion or size alone would.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence provides a meaningful basis for selecting the xylanase EC without needing the target's database record. It is probabilistic, and the family assignment is not an experimental demonstration of catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based xylanase-family inference supports D among the offered choices; no other option is comparably supported by the sequence.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but its EC evidence is computational (PROSITE-ProRule), not direct experimental evidence in these excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a likely N-terminal secretion signal followed by a compact fungal glycoside-hydrolase-sized domain. Its sequence is consistent with the small fungal endo-xylanase family, whose transferable family-level association supports EC 3.2.1.8. This distinguishes the xylanase choice from the offered oxidoreductase and lyase choices, and more specifically than secretion or size alone would.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence provides a meaningful basis for selecting the xylanase EC without needing the target's database record. It is probabilistic, and the family assignment is not an experimental demonstration of catalytic activity."
  },
  "case_id": "EC_number_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 3.2.1.8 and describes endohydrolysis of beta-xylosidic linkages in xylans. The EC assignment is supported by a PROSITE-ProRule computational annotation, rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its EC evidence is computational (PROSITE-ProRule), not direct experimental evidence in these excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based xylanase-family inference supports D among the offered choices; no other option is comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 3.2.1.8 and describes endohydrolysis of beta-xylosidic linkages in xylans. The EC assignment is supported by a PROSITE-ProRule computational annotation, rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a likely N-terminal secretion signal followed by a compact fungal glycoside-hydrolase-sized domain. Its sequence is consistent with the small fungal endo-xylanase family, whose transferable family-level association supports EC 3.2.1.8. This distinguishes the xylanase choice from the offered oxidoreductase and lyase choices, and more specifically than secretion or size alone would.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence provides a meaningful basis for selecting the xylanase EC without needing the target's database record. It is probabilistic, and the family assignment is not an experimental demonstration of catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based xylanase-family inference supports D among the offered choices; no other option is comparably supported by the sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its EC evidence is computational (PROSITE-ProRule), not direct experimental evidence in these excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A384K474, EIX2_BOTFB) annotates EC 3.2.1.8 (endo-1,4-beta-xylanase) based on PROSITE-ProRule PRU01097 (ECO:0000255, computational family assignment). The protein is named 'Ethylene-inducing xylanase 2' and described as 'Endo-1,4-beta-xylanase EIX2.' The catalytic activity is stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The annotation is family-rule-based rather than direct experimental kinetics, but the protein name and PubMed reference (33205907) suggest functional characterization. The expected answer D (3.2.1.8) is consistent with the database annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features distinguish D from the alternatives. (1) Size: The protein is only 222 aa. Terpene synthases (EC 4.2.3.1) are typically 300-500+ aa with DDXXD motifs; cytochrome P450s (EC 1.14.13.238) are typically 400-600+ aa with the FxxGxxxCxG heme-binding motif. Neither motif is present, and the size is far too small, strongly disfavoring B and C. (2) Signal peptide: The N-terminal 'MITFSSLLVTFSAISTSLAIPGS' is a classic fungal signal peptide, consistent with a secreted hydrolase rather than an intracellular P450 or terpene cyclase. (3) GH11 vs GH10 (D vs A): The sequence contains the highly diagnostic GH11 xylanase motifs 'GSGT' (in 'GSGTALLSIYGW') and 'NPINFSGTFGIGSGT', which are hallmark conserved regions of the GH11 beta-jelly-roll fold. GH10 xylanases (EC 3.2.1.105) have a completely different (alpha/beta)5/7 barrel fold and lack these motifs. A knowledgeable model familiar with glycoside hydrolase families would recognize the GSGT and NPINFSGTFGIGSGT patterns as GH11-specific, distinguishing D from A. (4) The overall compact size (~222 aa mature) is consistent with GH11 xylanases (typically 150-250 aa) rather than GH10 (typically 350-500 aa).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of protein size, presence of a signal peptide, and the highly characteristic GH11 sequence motifs (GSGT, NPINFSGTFGIGSGT) provides a concrete, family-level inference that meaningfully distinguishes D (3.2.1.8, GH11) from A (3.2.1.105, GH10), B (terpene synthase), and C (P450). This relies on transferable knowledge of glycoside hydrolase family signatures, enzyme size ranges, and structural principles learned from many related proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The size constraint eliminates B and C decisively. The GH11-specific GSGT and NPINFSGTFGIGSGT motifs clearly distinguish D from A (GH10). No other option is defensible given the sequence features.


### Important caveats

- The EC 3.2.1.8 annotation in UniProt is based on PROSITE-ProRule PRU01097 (ECO:0000255), a computational family assignment, not direct experimental kinetic measurement. The protein name 'Ethylene-inducing xylanase' and a PubMed reference suggest functional studies, but the EC assignment itself is rule-based.
- The protein is annotated as a precursor; the mature enzyme after signal peptide cleavage would be shorter (~190 aa), still consistent with GH11 xylanase size.
- The distinction between GH11 (D) and GH10 (A) relies on recognizing family-specific motifs; a model unfamiliar with GH family signatures might struggle, though the size difference (GH11 ~200 aa vs GH10 ~400+ aa) provides an additional clue.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features distinguish D from the alternatives. (1) Size: The protein is only 222 aa. Terpene synthases (EC 4.2.3.1) are typically 300-500+ aa with DDXXD motifs; cytochrome P450s (EC 1.14.13.238) are typically 400-600+ aa with the FxxGxxxCxG heme-binding motif. Neither motif is present, and the size is far too small, strongly disfavoring B and C. (2) Signal peptide: The N-terminal 'MITFSSLLVTFSAISTSLAIPGS' is a classic fungal signal peptide, consistent with a secreted hydrolase rather than an intracellular P450 or terpene cyclase. (3) GH11 vs GH10 (D vs A): The sequence contains the highly diagnostic GH11 xylanase motifs 'GSGT' (in 'GSGTALLSIYGW') and 'NPINFSGTFGIGSGT', which are hallmark conserved regions of the GH11 beta-jelly-roll fold. GH10 xylanases (EC 3.2.1.105) have a completely different (alpha/beta)5/7 barrel fold and lack these motifs. A knowledgeable model familiar with glycoside hydrolase families would recognize the GSGT and NPINFSGTFGIGSGT patterns as GH11-specific, distinguishing D from A. (4) The overall compact size (~222 aa mature) is consistent with GH11 xylanases (typically 150-250 aa) rather than GH10 (typically 350-500 aa).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of protein size, presence of a signal peptide, and the highly characteristic GH11 sequence motifs (GSGT, NPINFSGTFGIGSGT) provides a concrete, family-level inference that meaningfully distinguishes D (3.2.1.8, GH11) from A (3.2.1.105, GH10), B (terpene synthase), and C (P450). This relies on transferable knowledge of glycoside hydrolase family signatures, enzyme size ranges, and structural principles learned from many related proteins."
  },
  "case_id": "EC_number_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384K474, EIX2_BOTFB) annotates EC 3.2.1.8 (endo-1,4-beta-xylanase) based on PROSITE-ProRule PRU01097 (ECO:0000255, computational family assignment). The protein is named 'Ethylene-inducing xylanase 2' and described as 'Endo-1,4-beta-xylanase EIX2.' The catalytic activity is stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The annotation is family-rule-based rather than direct experimental kinetics, but the protein name and PubMed reference (33205907) suggest functional characterization. The expected answer D (3.2.1.8) is consistent with the database annotation."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation in UniProt is based on PROSITE-ProRule PRU01097 (ECO:0000255), a computational family assignment, not direct experimental kinetic measurement. The protein name 'Ethylene-inducing xylanase' and a PubMed reference suggest functional studies, but the EC assignment itself is rule-based.",
    "The protein is annotated as a precursor; the mature enzyme after signal peptide cleavage would be shorter (~190 aa), still consistent with GH11 xylanase size.",
    "The distinction between GH11 (D) and GH10 (A) relies on recognizing family-specific motifs; a model unfamiliar with GH family signatures might struggle, though the size difference (GH11 ~200 aa vs GH10 ~400+ aa) provides an additional clue."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size constraint eliminates B and C decisively. The GH11-specific GSGT and NPINFSGTFGIGSGT motifs clearly distinguish D from A (GH10). No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384K474, EIX2_BOTFB) annotates EC 3.2.1.8 (endo-1,4-beta-xylanase) based on PROSITE-ProRule PRU01097 (ECO:0000255, computational family assignment). The protein is named 'Ethylene-inducing xylanase 2' and described as 'Endo-1,4-beta-xylanase EIX2.' The catalytic activity is stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The annotation is family-rule-based rather than direct experimental kinetics, but the protein name and PubMed reference (33205907) suggest functional characterization. The expected answer D (3.2.1.8) is consistent with the database annotation.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features distinguish D from the alternatives. (1) Size: The protein is only 222 aa. Terpene synthases (EC 4.2.3.1) are typically 300-500+ aa with DDXXD motifs; cytochrome P450s (EC 1.14.13.238) are typically 400-600+ aa with the FxxGxxxCxG heme-binding motif. Neither motif is present, and the size is far too small, strongly disfavoring B and C. (2) Signal peptide: The N-terminal 'MITFSSLLVTFSAISTSLAIPGS' is a classic fungal signal peptide, consistent with a secreted hydrolase rather than an intracellular P450 or terpene cyclase. (3) GH11 vs GH10 (D vs A): The sequence contains the highly diagnostic GH11 xylanase motifs 'GSGT' (in 'GSGTALLSIYGW') and 'NPINFSGTFGIGSGT', which are hallmark conserved regions of the GH11 beta-jelly-roll fold. GH10 xylanases (EC 3.2.1.105) have a completely different (alpha/beta)5/7 barrel fold and lack these motifs. A knowledgeable model familiar with glycoside hydrolase families would recognize the GSGT and NPINFSGTFGIGSGT patterns as GH11-specific, distinguishing D from A. (4) The overall compact size (~222 aa mature) is consistent with GH11 xylanases (typically 150-250 aa) rather than GH10 (typically 350-500 aa).",
    "missing_item_specific_fact": "",
    "reason": "The combination of protein size, presence of a signal peptide, and the highly characteristic GH11 sequence motifs (GSGT, NPINFSGTFGIGSGT) provides a concrete, family-level inference that meaningfully distinguishes D (3.2.1.8, GH11) from A (3.2.1.105, GH10), B (terpene synthase), and C (P450). This relies on transferable knowledge of glycoside hydrolase family signatures, enzyme size ranges, and structural principles learned from many related proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size constraint eliminates B and C decisively. The GH11-specific GSGT and NPINFSGTFGIGSGT motifs clearly distinguish D from A (GH10). No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation in UniProt is based on PROSITE-ProRule PRU01097 (ECO:0000255), a computational family assignment, not direct experimental kinetic measurement. The protein name 'Ethylene-inducing xylanase' and a PubMed reference suggest functional studies, but the EC assignment itself is rule-based.",
    "The protein is annotated as a precursor; the mature enzyme after signal peptide cleavage would be shorter (~190 aa), still consistent with GH11 xylanase size.",
    "The distinction between GH11 (D) and GH10 (A) relies on recognizing family-specific motifs; a model unfamiliar with GH family signatures might struggle, though the size difference (GH11 ~200 aa vs GH10 ~400+ aa) provides an additional clue."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 41. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
