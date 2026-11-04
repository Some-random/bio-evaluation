# cofactor_0185

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0185.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSLSLNEYLRYGRQLIVPEFGLQGQISLKNSRVLVVGAGGLGCPALQYLVGAGFGTVGIVDHDTVDISNLHRQILHTSETVEMLKCESAKLQLAKLNPLVQINTHPVALSPDNSFGIFEQYDIILDCTDTPATRYLINDTAVLLGLTVISGSGLKTEGQLSILNFNNTGPCYRCFYPTPPPPSSVTACSDGGVLGPVIGIMGVMMALEAIKVVSGYYLREDVEFQPFLSLYSGYGPLQSLRTFKMRRRSPKCRVCNAGTREITRHVIETELDYAVWCGKMDYNVLEKDERVSVEQLSAQRAPYLVDVRAKEQYSIVHLPNSINIPLNALKHMDTLDVPKETMIYVICRFGNDSQLAVKHLKSIGYENCVDVIGGLTQWSRQIDPNFPIY

[Multiple Choices]
A. FAD
B. Zn(2+)
C. Fe(2+)
D. pyridoxal 5'-phosphate
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates one Zn(2+) ion per subunit, based on a HAMAP computational rule. This supports the keyed answer, though the cited annotation is computational rather than direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a cysteine-rich region, including a Cys-X2-Cys motif and additional nearby cysteines, which is a plausible metal-binding feature. Transferable knowledge of sulfurtransferase/UBA4-like proteins supports zinc as a meaningful choice among these options; the sequence does not present comparably diagnostic FAD- or PLP-binding features.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level and sequence-feature inference provides a credible basis for choosing Zn(2+) over the listed alternatives. It is probabilistic and does not independently establish the exact binding stoichiometry or experimental requirement.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied annotation supports Zn(2+), and no other offered option is comparably supported.


### Important caveats

- The supporting cofactor annotation is rule-based computational evidence, not evidence here of a direct experimental measurement.
- The reviewer-only source record is sequence-matched; its target-specific annotations are not used as original-input evidence for the answerability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine-rich region, including a Cys-X2-Cys motif and additional nearby cysteines, which is a plausible metal-binding feature. Transferable knowledge of sulfurtransferase/UBA4-like proteins supports zinc as a meaningful choice among these options; the sequence does not present comparably diagnostic FAD- or PLP-binding features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level and sequence-feature inference provides a credible basis for choosing Zn(2+) over the listed alternatives. It is probabilistic and does not independently establish the exact binding stoichiometry or experimental requirement."
  },
  "case_id": "cofactor_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates one Zn(2+) ion per subunit, based on a HAMAP computational rule. This supports the keyed answer, though the cited annotation is computational rather than direct experimental evidence."
  },
  "important_caveats": [
    "The supporting cofactor annotation is rule-based computational evidence, not evidence here of a direct experimental measurement.",
    "The reviewer-only source record is sequence-matched; its target-specific annotations are not used as original-input evidence for the answerability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation supports Zn(2+), and no other offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates one Zn(2+) ion per subunit, based on a HAMAP computational rule. This supports the keyed answer, though the cited annotation is computational rather than direct experimental evidence.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a cysteine-rich region, including a Cys-X2-Cys motif and additional nearby cysteines, which is a plausible metal-binding feature. Transferable knowledge of sulfurtransferase/UBA4-like proteins supports zinc as a meaningful choice among these options; the sequence does not present comparably diagnostic FAD- or PLP-binding features.",
    "missing_item_specific_fact": "",
    "reason": "A family-level and sequence-feature inference provides a credible basis for choosing Zn(2+) over the listed alternatives. It is probabilistic and does not independently establish the exact binding stoichiometry or experimental requirement."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation supports Zn(2+), and no other offered option is comparably supported."
  },
  "important_caveats": [
    "The supporting cofactor annotation is rule-based computational evidence, not evidence here of a direct experimental measurement.",
    "The reviewer-only source record is sequence-matched; its target-specific annotations are not used as original-input evidence for the answerability judgment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (W1QET1, UBA4_OGAPD) annotates Zn(2+) as a cofactor ('Binds 1 zinc ion per subunit') based on HAMAP-Rule MF_03049 (ECO:0000255). This is a computational/proteome-level annotation rather than direct experimental evidence, but it is the recorded annotation for this entry and is not contradicted by any other data. The protein is an adenylyltransferase and sulfurtransferase (EC 2.7.7.80, EC 2.8.1.11) involved in molybdopterin biosynthesis, and the Zn(2+) annotation is consistent with Cys-rich motifs visible in the sequence (e.g., 'CRVCN').

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein contains two recognizable functional domains: (1) an N-terminal Rossmann-fold adenylyltransferase domain (GAGGLGCPALQ motif, GxGxxG pattern) that binds ATP for adenylyltransferase activity, and (2) a C-terminal rhodanese-like sulfurtransferase domain (recognizable by the conserved Cys-rich catalytic region 'CRVCNAGTREITRHVIETELDYAVWCGKMDYNVLE' and the overall fold topology). This dual-domain architecture is characteristic of the UBA4/MoeB-type adenylyltransferase-sulfurtransferase family. A knowledgeable model can reason: (a) The Rossmann fold here binds ATP for adenylyltransferase activity, not FAD for redox chemistry; the presence of a rhodanese-like sulfurtransferase domain strongly argues this is NOT a flavoprotein, ruling out FAD (A). (b) No PLP-binding lysine in the characteristic active-site context is present, ruling out pyridoxal 5'-phosphate (D). (c) No heme-binding, iron-sulfur cluster, or His-rich iron-binding motifs are present, ruling out Fe(2+) (C). (d) The Cys-rich regions (CRVCN with two cysteines in proximity, plus additional Cys residues in the sulfurtransferase domain) are consistent with zinc coordination, which is a well-documented structural cofactor in sulfurtransferase and related enzymes. The combination of a sulfurtransferase domain with Cys-rich motifs and the absence of features for FAD, PLP, or iron makes Zn(2+) the most defensible choice among the four options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of protein domain architecture (Rossmann fold for adenylyltransferase vs. flavoprotein, rhodanese-like sulfurtransferase domains) and the cofactor preferences of these enzyme families can meaningfully eliminate FAD, PLP, and Fe(2+) and arrive at Zn(2+). The argument relies on recognizing the dual-domain architecture and the typical cofactor biology of sulfurtransferases, which is transferable knowledge from other proteins in these families. The prominent GxGxxG Rossmann motif is a strong distractor toward FAD, but the rhodanese domain and overall enzymatic context (adenylyltransferase + sulfurtransferase, not oxidoreductase) provide the discriminating logic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the GxGxxG Rossmann fold motif is a strong visual distractor toward FAD, the presence of the rhodanese-like sulfurtransferase domain and the absence of flavoprotein-specific features (isoalloxazine-binding residues, FAD-specific secondary structure motifs) allow a careful analyst to rule out FAD. The remaining three options (Zn2+, Fe2+, PLP) are distinguishable by the absence of iron-binding motifs and PLP-binding motifs, leaving Zn2+ as the only option consistent with the Cys-rich sulfurtransferase context. No two options are equally defensible under careful analysis.


### Important caveats

- The Zn(2+) annotation is based on a HAMAP computational rule (ECO:0000255), not direct experimental binding data. The zinc may be structural rather than catalytic.
- The GAGGLG Rossmann fold motif is a very strong distractor toward FAD; a model that pattern-matches this motif without considering the full domain architecture could reasonably (but incorrectly) choose FAD.
- The sequence is from Ogataea parapolymorpha (a yeast), but organism identity was not provided to the model and is not needed for the domain-level reasoning.
- The zinc-binding motif (CRVCN) is suggestive but not a canonical, unambiguous zinc-binding signature; the argument for Zn(2+) relies partly on the family-level context of sulfurtransferases rather than a single decisive sequence motif.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein contains two recognizable functional domains: (1) an N-terminal Rossmann-fold adenylyltransferase domain (GAGGLGCPALQ motif, GxGxxG pattern) that binds ATP for adenylyltransferase activity, and (2) a C-terminal rhodanese-like sulfurtransferase domain (recognizable by the conserved Cys-rich catalytic region 'CRVCNAGTREITRHVIETELDYAVWCGKMDYNVLE' and the overall fold topology). This dual-domain architecture is characteristic of the UBA4/MoeB-type adenylyltransferase-sulfurtransferase family. A knowledgeable model can reason: (a) The Rossmann fold here binds ATP for adenylyltransferase activity, not FAD for redox chemistry; the presence of a rhodanese-like sulfurtransferase domain strongly argues this is NOT a flavoprotein, ruling out FAD (A). (b) No PLP-binding lysine in the characteristic active-site context is present, ruling out pyridoxal 5'-phosphate (D). (c) No heme-binding, iron-sulfur cluster, or His-rich iron-binding motifs are present, ruling out Fe(2+) (C). (d) The Cys-rich regions (CRVCN with two cysteines in proximity, plus additional Cys residues in the sulfurtransferase domain) are consistent with zinc coordination, which is a well-documented structural cofactor in sulfurtransferase and related enzymes. The combination of a sulfurtransferase domain with Cys-rich motifs and the absence of features for FAD, PLP, or iron makes Zn(2+) the most defensible choice among the four options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of protein domain architecture (Rossmann fold for adenylyltransferase vs. flavoprotein, rhodanese-like sulfurtransferase domains) and the cofactor preferences of these enzyme families can meaningfully eliminate FAD, PLP, and Fe(2+) and arrive at Zn(2+). The argument relies on recognizing the dual-domain architecture and the typical cofactor biology of sulfurtransferases, which is transferable knowledge from other proteins in these families. The prominent GxGxxG Rossmann motif is a strong distractor toward FAD, but the rhodanese domain and overall enzymatic context (adenylyltransferase + sulfurtransferase, not oxidoreductase) provide the discriminating logic."
  },
  "case_id": "cofactor_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (W1QET1, UBA4_OGAPD) annotates Zn(2+) as a cofactor ('Binds 1 zinc ion per subunit') based on HAMAP-Rule MF_03049 (ECO:0000255). This is a computational/proteome-level annotation rather than direct experimental evidence, but it is the recorded annotation for this entry and is not contradicted by any other data. The protein is an adenylyltransferase and sulfurtransferase (EC 2.7.7.80, EC 2.8.1.11) involved in molybdopterin biosynthesis, and the Zn(2+) annotation is consistent with Cys-rich motifs visible in the sequence (e.g., 'CRVCN')."
  },
  "important_caveats": [
    "The Zn(2+) annotation is based on a HAMAP computational rule (ECO:0000255), not direct experimental binding data. The zinc may be structural rather than catalytic.",
    "The GAGGLG Rossmann fold motif is a very strong distractor toward FAD; a model that pattern-matches this motif without considering the full domain architecture could reasonably (but incorrectly) choose FAD.",
    "The sequence is from Ogataea parapolymorpha (a yeast), but organism identity was not provided to the model and is not needed for the domain-level reasoning.",
    "The zinc-binding motif (CRVCN) is suggestive but not a canonical, unambiguous zinc-binding signature; the argument for Zn(2+) relies partly on the family-level context of sulfurtransferases rather than a single decisive sequence motif."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the GxGxxG Rossmann fold motif is a strong visual distractor toward FAD, the presence of the rhodanese-like sulfurtransferase domain and the absence of flavoprotein-specific features (isoalloxazine-binding residues, FAD-specific secondary structure motifs) allow a careful analyst to rule out FAD. The remaining three options (Zn2+, Fe2+, PLP) are distinguishable by the absence of iron-binding motifs and PLP-binding motifs, leaving Zn2+ as the only option consistent with the Cys-rich sulfurtransferase context. No two options are equally defensible under careful analysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (W1QET1, UBA4_OGAPD) annotates Zn(2+) as a cofactor ('Binds 1 zinc ion per subunit') based on HAMAP-Rule MF_03049 (ECO:0000255). This is a computational/proteome-level annotation rather than direct experimental evidence, but it is the recorded annotation for this entry and is not contradicted by any other data. The protein is an adenylyltransferase and sulfurtransferase (EC 2.7.7.80, EC 2.8.1.11) involved in molybdopterin biosynthesis, and the Zn(2+) annotation is consistent with Cys-rich motifs visible in the sequence (e.g., 'CRVCN').",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein contains two recognizable functional domains: (1) an N-terminal Rossmann-fold adenylyltransferase domain (GAGGLGCPALQ motif, GxGxxG pattern) that binds ATP for adenylyltransferase activity, and (2) a C-terminal rhodanese-like sulfurtransferase domain (recognizable by the conserved Cys-rich catalytic region 'CRVCNAGTREITRHVIETELDYAVWCGKMDYNVLE' and the overall fold topology). This dual-domain architecture is characteristic of the UBA4/MoeB-type adenylyltransferase-sulfurtransferase family. A knowledgeable model can reason: (a) The Rossmann fold here binds ATP for adenylyltransferase activity, not FAD for redox chemistry; the presence of a rhodanese-like sulfurtransferase domain strongly argues this is NOT a flavoprotein, ruling out FAD (A). (b) No PLP-binding lysine in the characteristic active-site context is present, ruling out pyridoxal 5'-phosphate (D). (c) No heme-binding, iron-sulfur cluster, or His-rich iron-binding motifs are present, ruling out Fe(2+) (C). (d) The Cys-rich regions (CRVCN with two cysteines in proximity, plus additional Cys residues in the sulfurtransferase domain) are consistent with zinc coordination, which is a well-documented structural cofactor in sulfurtransferase and related enzymes. The combination of a sulfurtransferase domain with Cys-rich motifs and the absence of features for FAD, PLP, or iron makes Zn(2+) the most defensible choice among the four options.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of protein domain architecture (Rossmann fold for adenylyltransferase vs. flavoprotein, rhodanese-like sulfurtransferase domains) and the cofactor preferences of these enzyme families can meaningfully eliminate FAD, PLP, and Fe(2+) and arrive at Zn(2+). The argument relies on recognizing the dual-domain architecture and the typical cofactor biology of sulfurtransferases, which is transferable knowledge from other proteins in these families. The prominent GxGxxG Rossmann motif is a strong distractor toward FAD, but the rhodanese domain and overall enzymatic context (adenylyltransferase + sulfurtransferase, not oxidoreductase) provide the discriminating logic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the GxGxxG Rossmann fold motif is a strong visual distractor toward FAD, the presence of the rhodanese-like sulfurtransferase domain and the absence of flavoprotein-specific features (isoalloxazine-binding residues, FAD-specific secondary structure motifs) allow a careful analyst to rule out FAD. The remaining three options (Zn2+, Fe2+, PLP) are distinguishable by the absence of iron-binding motifs and PLP-binding motifs, leaving Zn2+ as the only option consistent with the Cys-rich sulfurtransferase context. No two options are equally defensible under careful analysis."
  },
  "important_caveats": [
    "The Zn(2+) annotation is based on a HAMAP computational rule (ECO:0000255), not direct experimental binding data. The zinc may be structural rather than catalytic.",
    "The GAGGLG Rossmann fold motif is a very strong distractor toward FAD; a model that pattern-matches this motif without considering the full domain architecture could reasonably (but incorrectly) choose FAD.",
    "The sequence is from Ogataea parapolymorpha (a yeast), but organism identity was not provided to the model and is not needed for the domain-level reasoning.",
    "The zinc-binding motif (CRVCN) is suggestive but not a canonical, unambiguous zinc-binding signature; the argument for Zn(2+) relies partly on the family-level context of sulfurtransferases rather than a single decisive sequence motif."
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
  "benchmark_sequence_length": 389,
  "benchmark_sequence_sha256": "a901665ea3dc44218892e98264561a93d82231546cdf75b9015b7ec0eb86f63a",
  "current_entry_audit": {
    "entryVersion": 69,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 389,
  "current_source_sequence_sha256": "a901665ea3dc44218892e98264561a93d82231546cdf75b9015b7ec0eb86f63a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "W1QET1",
  "selected_historical_entry_version": 67,
  "selected_historical_record_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "selected_historical_source_sequence_length": 389,
  "selected_historical_source_sequence_sha256": "a901665ea3dc44218892e98264561a93d82231546cdf75b9015b7ec0eb86f63a",
  "selected_historical_version": {
    "accession": "W1QET1",
    "database": "Swiss-Prot",
    "entryVersion": 67,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UBA4_OGAPD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"W1QET1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":69,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008673\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Pichiales\",\"Pichiaceae\",\"Ogataea\"],\"scientificName\":\"Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL Y-7560 / DL-1)\",\"synonyms\":[\"Hansenula polymorpha\"],\"taxonId\":871575}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Ubiquitin-like protein activator 4\"}}],\"includes\":[{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Adenylyltransferase UBA4\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Sulfur carrier protein MOCS2A adenylyltransferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O95396\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.7.80\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Molybdopterin-synthase adenylyltransferase\"}}},{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Sulfur carrier protein MOCS2A sulfurtransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Sulfurtransferase UBA4\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O95396\",\"source\":\"UniProtKB\"}],\"value\":\"2.8.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Molybdopterin-synthase sulfurtransferase\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Adenylyltransferase and sulfurtransferase uba4\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Binds 1 zinc ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H1",
  "excerpt": "ID   UBA4_OGAPD              Reviewed;         389 AA.\nAC   W1QET1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Adenylyltransferase and sulfurtransferase uba4 {ECO:0000305};\nDE   AltName: Full=Ubiquitin-like protein activator 4 {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=Molybdopterin-synthase adenylyltransferase {ECO:0000305};\nDE              EC=2.7.7.80 {ECO:0000250|UniProtKB:O95396};\nDE     AltName: Full=Adenylyltransferase UBA4 {ECO:0000305};\nDE     AltName: Full=Sulfur carrier protein MOCS2A adenylyltransferase {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=Molybdopterin-synthase sulfurtransferase {ECO:0000305};\nDE              EC=2.8.1.11 {ECO:0000250|UniProtKB:O95396};\nDE     AltName: Full=Sulfur carrier protein MOCS2A sulfurtransferase {ECO:0000305};\nDE     AltName: Full=Sulfurtransferase UBA4 {ECO:0000305};\nGN   Name=UBA4 {ECO:0000305}; Synonyms=CNX4 {ECO:0000303|PubMed:33617956};\nGN   ORFNames=HPODL_00948 {ECO:0000312|EMBL:ESX00063.1};\nOS   Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL\nOS   Y-7560 / DL-1) (Yeast) (Hansenula polymorpha).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Pichiales; Pichiaceae; Ogataea.\nOX   NCBI_TaxID=871575 {ECO:0000312|Proteomes:UP000008673};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Adenylyltransferase and sulfurtransferase uba4 {ECO:0000305};\nDE   AltName: Full=Ubiquitin-like protein activator 4 {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=Molybdopterin-synthase adenylyltransferase {ECO:0000305};\nDE              EC=2.7.7.80 {ECO:0000250|UniProtKB:O95396};\nDE     AltName: Full=Adenylyltransferase UBA4 {ECO:0000305};\nDE     AltName: Full=Sulfur carrier protein MOCS2A adenylyltransferase {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=Molybdopterin-synthase sulfurtransferase {ECO:0000305};\nDE              EC=2.8.1.11 {ECO:0000250|UniProtKB:O95396};\nDE     AltName: Full=Sulfur carrier protein MOCS2A sulfurtransferase {ECO:0000305};\nDE     AltName: Full=Sulfurtransferase UBA4 {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND PATHWAY.\nRX   PubMed=33617956; DOI=10.1016/j.ymben.2021.02.004;\nRA   Perli T., van der Vorm D.N.A., Wassink M., van den Broek M., Pronk J.T.,\nRA   Daran J.M.;\nRT   \"Engineering heterologous molybdenum-cofactor-biosynthesis and nitrate-\nRT   assimilation pathways enables nitrate utilization by Saccharomyces\nRT   cerevisiae.\";\nRL   Metab. Eng. 65:11-29(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000255|HAMAP-Rule:MF_03049};\nCC       Note=Binds 1 zinc ion per subunit. {ECO:0000255|HAMAP-Rule:MF_03049};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 185. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
