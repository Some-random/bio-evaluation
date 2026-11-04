# active_site_0027

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0027.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 153 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRYAVVTGVSSGIGKAICEKFLAKGLYVFGSVRKKEDAKYFEEKYPNTFHTLVFDTTDYPAVDKAVEEIHKVVGKKGLSVLVNNAGVAKYGPIQHVPIEELRQQYEVNVFASVYLTQKLLWLLGASKEAKWQGKVIQISSTAGVMTRPMLGPYSSSKHAVEAIYDALRRELMIYGVEVVLIEPGPIKTEIWGKAKSGGNPYKDTDYGEIFAQLDKAVDEIEKIGLPVEAVAGKAWEAFVAKKPKARYVVAPKKLMFKAAMYLIPDRMLDKIFYKDLKKLTQES

[Multiple Choices]
A. Position 31 (Proton donor)
B. Position 153 (Proton acceptor)
C. Position 405 (For beta-ketoacyl synthase 1 activity)
D. Position 184 (For beta-ketoacyl synthase activity)
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

> The sequence-matched UniProt record annotates position 153 as an active-site proton acceptor. The annotation is transferred by similarity from Q9BPW9, so it supports the key at the database-annotation level, but the supplied evidence does not establish direct experimental validation of this residue in this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a likely Rossmann-like dinucleotide-binding motif near its N-terminus and a YxxxK motif at residues 153–157, consistent with the catalytic Tyr/Lys motif of short-chain dehydrogenase/reductase enzymes. That transferable family pattern makes the tyrosine at position 153 a credible active-site choice. The alternatives are less plausible: position 31 is valine, position 184 is glycine, and position 405 is beyond the 283-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features meaningfully distinguish position 153 from the offered alternatives without needing the exact protein's database record. The specific proton-transfer assignment is less securely inferred from sequence alone than the catalytic-residue identification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered options, position 153 is the only one consistent with a plausible catalytic residue and the sequence length.


### Important caveats

- The active-site annotation is similarity-based rather than direct experimental evidence for this exact protein.
- The exact proton-acceptor role is more specific than what the sequence motif alone establishes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a likely Rossmann-like dinucleotide-binding motif near its N-terminus and a YxxxK motif at residues 153–157, consistent with the catalytic Tyr/Lys motif of short-chain dehydrogenase/reductase enzymes. That transferable family pattern makes the tyrosine at position 153 a credible active-site choice. The alternatives are less plausible: position 31 is valine, position 184 is glycine, and position 405 is beyond the 283-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features meaningfully distinguish position 153 from the offered alternatives without needing the exact protein's database record. The specific proton-transfer assignment is less securely inferred from sequence alone than the catalytic-residue identification."
  },
  "case_id": "active_site_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 153 as an active-site proton acceptor. The annotation is transferred by similarity from Q9BPW9, so it supports the key at the database-annotation level, but the supplied evidence does not establish direct experimental validation of this residue in this protein."
  },
  "important_caveats": [
    "The active-site annotation is similarity-based rather than direct experimental evidence for this exact protein.",
    "The exact proton-acceptor role is more specific than what the sequence motif alone establishes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, position 153 is the only one consistent with a plausible catalytic residue and the sequence length."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 153 as an active-site proton acceptor. The annotation is transferred by similarity from Q9BPW9, so it supports the key at the database-annotation level, but the supplied evidence does not establish direct experimental validation of this residue in this protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a likely Rossmann-like dinucleotide-binding motif near its N-terminus and a YxxxK motif at residues 153–157, consistent with the catalytic Tyr/Lys motif of short-chain dehydrogenase/reductase enzymes. That transferable family pattern makes the tyrosine at position 153 a credible active-site choice. The alternatives are less plausible: position 31 is valine, position 184 is glycine, and position 405 is beyond the 283-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features meaningfully distinguish position 153 from the offered alternatives without needing the exact protein's database record. The specific proton-transfer assignment is less securely inferred from sequence alone than the catalytic-residue identification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, position 153 is the only one consistent with a plausible catalytic residue and the sequence length."
  },
  "important_caveats": [
    "The active-site annotation is similarity-based rather than direct experimental evidence for this exact protein.",
    "The exact proton-acceptor role is more specific than what the sequence motif alone establishes."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H3) lists position 153 as 'Proton acceptor' active site. The sequence confirms position 153 is Tyrosine, followed by SSSK (positions 154-157), forming the canonical YSSSK catalytic motif of short-chain dehydrogenase/reductases (SDRs). The protein is annotated as an NADPH-dependent reductase (EC 1.1.1.-), consistent with SDR family membership. The annotation evidence code is ECO:0000250 (inferred by similarity from Q9BPW9, another SDR), meaning the assignment is by family transfer rather than direct experimental mutagenesis of this specific protein. However, the YSSSK motif is present verbatim in the sequence, and the protein's reductase function is experimentally supported (PubMed 35414181, ECO:0000269). The annotation is consistent with the sequence and family context.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The YSSSK motif at positions 153-157 is the single most recognizable catalytic signature in the SDR (short-chain dehydrogenase/reductase) superfamily, found in hundreds of characterized enzymes (e.g., alcohol dehydrogenases, 3-hydroxyacyl-CoA dehydrogenases, carbonyl reductases). In this motif, the tyrosine serves as the catalytic proton acceptor/donor, while the serine and lysine complete the catalytic triad. A model trained on general enzymology would recognize YSSSK as the SDR catalytic tetrad. Additionally: (1) Option C references position 405, which exceeds the 283-residue protein length, making it physically impossible. (2) Options C and D reference 'beta-ketoacyl synthase' activity, which belongs to an entirely different enzyme family (FabB/FabF) with a Cys-His-His catalytic mechanism, not a YSSSK motif. (3) Position 31 is a serine (S) in a 'SVRKK' context, which does not match any known catalytic motif for this enzyme class. The transferable knowledge of the SDR YSSSK motif, combined with the impossibility of position 405 and the irrelevance of beta-ketoacyl synthase references, meaningfully distinguishes option B from all alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The YSSSK motif is a universally recognized SDR catalytic signature. Recognizing it requires only family-level pattern knowledge learned from many other SDR enzymes, not memorization of this specific protein's annotation. The other options are eliminable by simple arithmetic (position 405 > 283) and by recognizing that beta-ketoacyl synthase is a different enzyme family with different catalytic residues.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is physically impossible (position 405 exceeds the 283-residue sequence). Options C and D reference beta-ketoacyl synthase, a mechanistically unrelated enzyme family. Option A (position 31, serine in SVRKK) does not match any known SDR catalytic pattern. Only option B (position 153, Y in the YSSSK motif) is consistent with SDR catalytic chemistry.


### Important caveats

- The active-site annotation uses evidence code ECO:0000250 (inferred by similarity from Q9BPW9), not direct experimental mutagenesis of this specific protein. However, the YSSSK motif is unambiguously present in the sequence.
- The protein's reductase function is experimentally supported (ECO:0000269, PubMed 35414181), confirming it is an SDR-type enzyme where the YSSSK motif is the expected catalytic center.
- Option C's reference to 'position 405' in a 283-residue protein is a clear error/distractor that aids elimination.
- The annotation is from a Swiss-Prot entry first released in January 2026; the historical record at the pinned cutoff confirms the same annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The YSSSK motif at positions 153-157 is the single most recognizable catalytic signature in the SDR (short-chain dehydrogenase/reductase) superfamily, found in hundreds of characterized enzymes (e.g., alcohol dehydrogenases, 3-hydroxyacyl-CoA dehydrogenases, carbonyl reductases). In this motif, the tyrosine serves as the catalytic proton acceptor/donor, while the serine and lysine complete the catalytic triad. A model trained on general enzymology would recognize YSSSK as the SDR catalytic tetrad. Additionally: (1) Option C references position 405, which exceeds the 283-residue protein length, making it physically impossible. (2) Options C and D reference 'beta-ketoacyl synthase' activity, which belongs to an entirely different enzyme family (FabB/FabF) with a Cys-His-His catalytic mechanism, not a YSSSK motif. (3) Position 31 is a serine (S) in a 'SVRKK' context, which does not match any known catalytic motif for this enzyme class. The transferable knowledge of the SDR YSSSK motif, combined with the impossibility of position 405 and the irrelevance of beta-ketoacyl synthase references, meaningfully distinguishes option B from all alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The YSSSK motif is a universally recognized SDR catalytic signature. Recognizing it requires only family-level pattern knowledge learned from many other SDR enzymes, not memorization of this specific protein's annotation. The other options are eliminable by simple arithmetic (position 405 > 283) and by recognizing that beta-ketoacyl synthase is a different enzyme family with different catalytic residues."
  },
  "case_id": "active_site_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) lists position 153 as 'Proton acceptor' active site. The sequence confirms position 153 is Tyrosine, followed by SSSK (positions 154-157), forming the canonical YSSSK catalytic motif of short-chain dehydrogenase/reductases (SDRs). The protein is annotated as an NADPH-dependent reductase (EC 1.1.1.-), consistent with SDR family membership. The annotation evidence code is ECO:0000250 (inferred by similarity from Q9BPW9, another SDR), meaning the assignment is by family transfer rather than direct experimental mutagenesis of this specific protein. However, the YSSSK motif is present verbatim in the sequence, and the protein's reductase function is experimentally supported (PubMed 35414181, ECO:0000269). The annotation is consistent with the sequence and family context."
  },
  "important_caveats": [
    "The active-site annotation uses evidence code ECO:0000250 (inferred by similarity from Q9BPW9), not direct experimental mutagenesis of this specific protein. However, the YSSSK motif is unambiguously present in the sequence.",
    "The protein's reductase function is experimentally supported (ECO:0000269, PubMed 35414181), confirming it is an SDR-type enzyme where the YSSSK motif is the expected catalytic center.",
    "Option C's reference to 'position 405' in a 283-residue protein is a clear error/distractor that aids elimination.",
    "The annotation is from a Swiss-Prot entry first released in January 2026; the historical record at the pinned cutoff confirms the same annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is physically impossible (position 405 exceeds the 283-residue sequence). Options C and D reference beta-ketoacyl synthase, a mechanistically unrelated enzyme family. Option A (position 31, serine in SVRKK) does not match any known SDR catalytic pattern. Only option B (position 153, Y in the YSSSK motif) is consistent with SDR catalytic chemistry."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) lists position 153 as 'Proton acceptor' active site. The sequence confirms position 153 is Tyrosine, followed by SSSK (positions 154-157), forming the canonical YSSSK catalytic motif of short-chain dehydrogenase/reductases (SDRs). The protein is annotated as an NADPH-dependent reductase (EC 1.1.1.-), consistent with SDR family membership. The annotation evidence code is ECO:0000250 (inferred by similarity from Q9BPW9, another SDR), meaning the assignment is by family transfer rather than direct experimental mutagenesis of this specific protein. However, the YSSSK motif is present verbatim in the sequence, and the protein's reductase function is experimentally supported (PubMed 35414181, ECO:0000269). The annotation is consistent with the sequence and family context.",
    "evidence_ids": ["C5", "C4", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The YSSSK motif at positions 153-157 is the single most recognizable catalytic signature in the SDR (short-chain dehydrogenase/reductase) superfamily, found in hundreds of characterized enzymes (e.g., alcohol dehydrogenases, 3-hydroxyacyl-CoA dehydrogenases, carbonyl reductases). In this motif, the tyrosine serves as the catalytic proton acceptor/donor, while the serine and lysine complete the catalytic triad. A model trained on general enzymology would recognize YSSSK as the SDR catalytic tetrad. Additionally: (1) Option C references position 405, which exceeds the 283-residue protein length, making it physically impossible. (2) Options C and D reference 'beta-ketoacyl synthase' activity, which belongs to an entirely different enzyme family (FabB/FabF) with a Cys-His-His catalytic mechanism, not a YSSSK motif. (3) Position 31 is a serine (S) in a 'SVRKK' context, which does not match any known catalytic motif for this enzyme class. The transferable knowledge of the SDR YSSSK motif, combined with the impossibility of position 405 and the irrelevance of beta-ketoacyl synthase references, meaningfully distinguishes option B from all alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The YSSSK motif is a universally recognized SDR catalytic signature. Recognizing it requires only family-level pattern knowledge learned from many other SDR enzymes, not memorization of this specific protein's annotation. The other options are eliminable by simple arithmetic (position 405 > 283) and by recognizing that beta-ketoacyl synthase is a different enzyme family with different catalytic residues."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is physically impossible (position 405 exceeds the 283-residue sequence). Options C and D reference beta-ketoacyl synthase, a mechanistically unrelated enzyme family. Option A (position 31, serine in SVRKK) does not match any known SDR catalytic pattern. Only option B (position 153, Y in the YSSSK motif) is consistent with SDR catalytic chemistry."
  },
  "important_caveats": [
    "The active-site annotation uses evidence code ECO:0000250 (inferred by similarity from Q9BPW9), not direct experimental mutagenesis of this specific protein. However, the YSSSK motif is unambiguously present in the sequence.",
    "The protein's reductase function is experimentally supported (ECO:0000269, PubMed 35414181), confirming it is an SDR-type enzyme where the YSSSK motif is the expected catalytic center.",
    "Option C's reference to 'position 405' in a 283-residue protein is a clear error/distractor that aids elimination.",
    "The annotation is from a Swiss-Prot entry first released in January 2026; the historical record at the pinned cutoff confirms the same annotation."
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
  "benchmark_sequence_length": 283,
  "benchmark_sequence_sha256": "c34636190c93b708ede11afe25d8f3e950d83ee164fe4651dffd58c7eb032d36",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-04-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 283,
  "current_source_sequence_sha256": "c34636190c93b708ede11afe25d8f3e950d83ee164fe4651dffd58c7eb032d36",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 16,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A3R5XUE6",
  "selected_historical_entry_version": 16,
  "selected_historical_record_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "selected_historical_source_sequence_length": 283,
  "selected_historical_source_sequence_sha256": "c34636190c93b708ede11afe25d8f3e950d83ee164fe4651dffd58c7eb032d36",
  "selected_historical_version": {
    "accession": "A0A3R5XUE6",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CAPC_ORNRH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A3R5XUE6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-04-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Bacteroidota\",\"Flavobacteriia\",\"Flavobacteriales\",\"Weeksellaceae\",\"Ornithobacterium\"],\"scientificName\":\"Ornithobacterium rhinotracheale\",\"taxonId\":28251}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"NADPH-dependent 3-dehydrocapnine reductase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPW9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":153},\"start\":{\"modifier\":\"EXACT\",\"value\":153}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu Y.\",\"Wei Y.\",\"Teh T.M.\",\"Liu D.\",\"Zhou Y.\",\"Zhao S.\",\"Ang E.L.\",\"Zhao H.\",\"Zhang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35414181\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.2c00102\"}],\"citationType\":\"journal article\",\"firstPage\":\"2861\",\"id\":\"35414181\",\"journal\":\"Biochemistry\",\"lastPage\":\"2869\",\"publicationDate\":\"2022\",\"title\":\"Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine.\",\"volume\":\"61\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H1",
  "excerpt": "ID   CAPC_ORNRH              Reviewed;         283 AA.\nAC   A0A3R5XUE6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-APR-2019, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=NADPH-dependent 3-dehydrocapnine reductase {ECO:0000303|PubMed:35414181};\nDE            EC=1.1.1.- {ECO:0000269|PubMed:35414181};\nGN   Name=capC {ECO:0000303|PubMed:35414181};\nGN   ORFNames=EQP59_04780 {ECO:0000312|EMBL:QAR30703.1};\nOS   Ornithobacterium rhinotracheale.\nOC   Bacteria; Pseudomonadati; Bacteroidota; Flavobacteriia; Flavobacteriales;\nOC   Weeksellaceae; Ornithobacterium.\nOX   NCBI_TaxID=28251;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:30.826829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "url": "https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=35414181; DOI=10.1021/acs.biochem.2c00102;\nRA   Liu Y., Wei Y., Teh T.M., Liu D., Zhou Y., Zhao S., Ang E.L., Zhao H.,\nRA   Zhang Y.;\nRT   \"Identification and Characterization of the Biosynthetic Pathway of the\nRT   Sulfonolipid Capnine.\";\nRL   Biochemistry 61:2861-2869(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:30.826829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "url": "https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        153\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPW9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:30.826829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "url": "https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
