# active_site_0085

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0085.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 60 (Cysteine sulfenic acid (-SOH) intermediate)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPLQPGDSFPANVVFSYIPPTGSLDLTVCGRPIEYNASEALAKGTSVLVAVPGAFTPTCQEKHVTGFIAKLDQLRQAGVDRVLFIASNDAFVMSAWGKANGIKDESILFLSDSDTAFSSSIGWANAGRTGRYAIVVKDGKVVYAAVDTVRGSTEKSGVDAVLTVLGNQGKL

[Multiple Choices]
A. Position 341 (For beta-ketoacyl synthase activity)
B. Position 959 (Proton acceptor; for dehydratase activity)
C. Position 60 (Cysteine sulfenic acid (-SOH) intermediate)
D. Position 151 (Proton acceptor)
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

> The sequence-matched UniProt record annotates residue 60 as the cysteine sulfenic acid intermediate of Peroxiredoxin AHP1. The annotation is transferred by similarity, not presented as direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 172-residue sequence contains a cysteine in the characteristic peroxiredoxin active-site region (the PxxxTxxC motif around position 60). Peroxiredoxins use a peroxidatic cysteine that forms a sulfenic acid intermediate, making choice C a credible family-based inference. Choices A and B give positions beyond the sequence length; choice D does not match this key peroxidatic-cysteine role.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the conserved peroxiredoxin motif and its shared catalytic mechanism meaningfully distinguishes C without needing the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence length rules out A and B, and the conserved peroxiredoxin cysteine motif supports C over D.


### Important caveats

- The supplied source annotation is similarity-transferred; it does not establish direct experimental measurement of the sulfenic acid intermediate in this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 172-residue sequence contains a cysteine in the characteristic peroxiredoxin active-site region (the PxxxTxxC motif around position 60). Peroxiredoxins use a peroxidatic cysteine that forms a sulfenic acid intermediate, making choice C a credible family-based inference. Choices A and B give positions beyond the sequence length; choice D does not match this key peroxidatic-cysteine role.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the conserved peroxiredoxin motif and its shared catalytic mechanism meaningfully distinguishes C without needing the exact protein's database record."
  },
  "case_id": "active_site_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 60 as the cysteine sulfenic acid intermediate of Peroxiredoxin AHP1. The annotation is transferred by similarity, not presented as direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The supplied source annotation is similarity-transferred; it does not establish direct experimental measurement of the sulfenic acid intermediate in this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence length rules out A and B, and the conserved peroxiredoxin cysteine motif supports C over D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 60 as the cysteine sulfenic acid intermediate of Peroxiredoxin AHP1. The annotation is transferred by similarity, not presented as direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 172-residue sequence contains a cysteine in the characteristic peroxiredoxin active-site region (the PxxxTxxC motif around position 60). Peroxiredoxins use a peroxidatic cysteine that forms a sulfenic acid intermediate, making choice C a credible family-based inference. Choices A and B give positions beyond the sequence length; choice D does not match this key peroxidatic-cysteine role.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the conserved peroxiredoxin motif and its shared catalytic mechanism meaningfully distinguishes C without needing the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence length rules out A and B, and the conserved peroxiredoxin cysteine motif supports C over D."
  },
  "important_caveats": [
    "The supplied source annotation is similarity-transferred; it does not establish direct experimental measurement of the sulfenic acid intermediate in this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G0S1P8 (Peroxiredoxin AHP1, 172 aa) annotates position 60 as 'Cysteine sulfenic acid (-SOH) intermediate' (Active site). Position 60 in the supplied sequence is indeed Cysteine (verified: ...PGAFTPTC(60)QEKH...). The annotation is by similarity (ECO:0000250 from P38013, yeast Tsa1), but the peroxiredoxin catalytic mechanism involving a peroxidatic cysteine forming a sulfenic acid intermediate is well-established experimentally across the family. The sequence contains the characteristic PxxC peroxiredoxin motif around positions 58-60 (P-T-C), consistent with the annotation.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent transferable arguments distinguish C: (1) The protein is only 172 amino acids long, so options A (position 341) and B (position 959) are physically impossible and can be eliminated immediately. (2) The sequence region 'VLVAVPGAFTPTC(60)QEKH' contains the PxxC motif (P-T-C at positions 58-60) that is the hallmark active-site signature of the peroxiredoxin family (EC 1.11.1.24). This motif is conserved across hundreds of peroxiredoxin homologs (Tsa1, AhpC, Prx1-6, etc.) and is a well-known family-level sequence feature. (3) The peroxiredoxin mechanism universally involves a peroxidatic cysteine that is oxidized to a sulfenic acid (-SOH) intermediate upon peroxide reduction—this is the defining catalytic step taught in biochemistry. Option C's description ('Cysteine sulfenic acid (-SOH) intermediate') exactly matches this mechanism. Option D ('Proton acceptor' at position 151, which is Arginine) does not correspond to any known peroxiredoxin catalytic mechanism.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A and B by noting the sequence is 172 aa (positions 341 and 959 are out of range). It can then recognize the peroxiredoxin PxxC motif in the sequence context 'PGAFTPTC' and recall that peroxiredoxins catalyze peroxide reduction via a catalytic Cys→-SOH mechanism. This family-level knowledge, learned from numerous peroxiredoxin homologs, directly identifies position 60 (Cys) with the sulfenic acid intermediate description in option C, while option D's 'proton acceptor' mechanism is inconsistent with peroxiredoxin chemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are impossible (positions exceed the 172-aa sequence length). Option D describes a 'proton acceptor' mechanism at an arginine, which is inconsistent with peroxiredoxin catalytic chemistry. Only option C matches both the sequence feature (Cys at position 60 in a PxxC context) and the well-established peroxiredoxin mechanism.


### Important caveats

- The UniProt annotation for position 60 is by similarity (ECO:0000250 from P38013/yeast Tsa1), not direct experimental evidence on this specific protein. However, the peroxiredoxin catalytic mechanism is experimentally validated across the family.
- The peroxiredoxin PxxC motif here reads P-T-C-Q rather than the canonical PxxCP; this is a known variant within the peroxiredoxin superfamily and does not undermine the assignment.
- Options A and B appear to be drawn from a completely different protein (possibly a fatty acid synthase subunit given 'beta-ketoacyl synthase' and 'dehydratase' annotations), serving as easy distractors.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent transferable arguments distinguish C: (1) The protein is only 172 amino acids long, so options A (position 341) and B (position 959) are physically impossible and can be eliminated immediately. (2) The sequence region 'VLVAVPGAFTPTC(60)QEKH' contains the PxxC motif (P-T-C at positions 58-60) that is the hallmark active-site signature of the peroxiredoxin family (EC 1.11.1.24). This motif is conserved across hundreds of peroxiredoxin homologs (Tsa1, AhpC, Prx1-6, etc.) and is a well-known family-level sequence feature. (3) The peroxiredoxin mechanism universally involves a peroxidatic cysteine that is oxidized to a sulfenic acid (-SOH) intermediate upon peroxide reduction—this is the defining catalytic step taught in biochemistry. Option C's description ('Cysteine sulfenic acid (-SOH) intermediate') exactly matches this mechanism. Option D ('Proton acceptor' at position 151, which is Arginine) does not correspond to any known peroxiredoxin catalytic mechanism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A and B by noting the sequence is 172 aa (positions 341 and 959 are out of range). It can then recognize the peroxiredoxin PxxC motif in the sequence context 'PGAFTPTC' and recall that peroxiredoxins catalyze peroxide reduction via a catalytic Cys→-SOH mechanism. This family-level knowledge, learned from numerous peroxiredoxin homologs, directly identifies position 60 (Cys) with the sulfenic acid intermediate description in option C, while option D's 'proton acceptor' mechanism is inconsistent with peroxiredoxin chemistry."
  },
  "case_id": "active_site_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G0S1P8 (Peroxiredoxin AHP1, 172 aa) annotates position 60 as 'Cysteine sulfenic acid (-SOH) intermediate' (Active site). Position 60 in the supplied sequence is indeed Cysteine (verified: ...PGAFTPTC(60)QEKH...). The annotation is by similarity (ECO:0000250 from P38013, yeast Tsa1), but the peroxiredoxin catalytic mechanism involving a peroxidatic cysteine forming a sulfenic acid intermediate is well-established experimentally across the family. The sequence contains the characteristic PxxC peroxiredoxin motif around positions 58-60 (P-T-C), consistent with the annotation."
  },
  "important_caveats": [
    "The UniProt annotation for position 60 is by similarity (ECO:0000250 from P38013/yeast Tsa1), not direct experimental evidence on this specific protein. However, the peroxiredoxin catalytic mechanism is experimentally validated across the family.",
    "The peroxiredoxin PxxC motif here reads P-T-C-Q rather than the canonical PxxCP; this is a known variant within the peroxiredoxin superfamily and does not undermine the assignment.",
    "Options A and B appear to be drawn from a completely different protein (possibly a fatty acid synthase subunit given 'beta-ketoacyl synthase' and 'dehydratase' annotations), serving as easy distractors."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are impossible (positions exceed the 172-aa sequence length). Option D describes a 'proton acceptor' mechanism at an arginine, which is inconsistent with peroxiredoxin catalytic chemistry. Only option C matches both the sequence feature (Cys at position 60 in a PxxC context) and the well-established peroxiredoxin mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G0S1P8 (Peroxiredoxin AHP1, 172 aa) annotates position 60 as 'Cysteine sulfenic acid (-SOH) intermediate' (Active site). Position 60 in the supplied sequence is indeed Cysteine (verified: ...PGAFTPTC(60)QEKH...). The annotation is by similarity (ECO:0000250 from P38013, yeast Tsa1), but the peroxiredoxin catalytic mechanism involving a peroxidatic cysteine forming a sulfenic acid intermediate is well-established experimentally across the family. The sequence contains the characteristic PxxC peroxiredoxin motif around positions 58-60 (P-T-C), consistent with the annotation.",
    "evidence_ids": ["C5", "H2", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent transferable arguments distinguish C: (1) The protein is only 172 amino acids long, so options A (position 341) and B (position 959) are physically impossible and can be eliminated immediately. (2) The sequence region 'VLVAVPGAFTPTC(60)QEKH' contains the PxxC motif (P-T-C at positions 58-60) that is the hallmark active-site signature of the peroxiredoxin family (EC 1.11.1.24). This motif is conserved across hundreds of peroxiredoxin homologs (Tsa1, AhpC, Prx1-6, etc.) and is a well-known family-level sequence feature. (3) The peroxiredoxin mechanism universally involves a peroxidatic cysteine that is oxidized to a sulfenic acid (-SOH) intermediate upon peroxide reduction—this is the defining catalytic step taught in biochemistry. Option C's description ('Cysteine sulfenic acid (-SOH) intermediate') exactly matches this mechanism. Option D ('Proton acceptor' at position 151, which is Arginine) does not correspond to any known peroxiredoxin catalytic mechanism.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A and B by noting the sequence is 172 aa (positions 341 and 959 are out of range). It can then recognize the peroxiredoxin PxxC motif in the sequence context 'PGAFTPTC' and recall that peroxiredoxins catalyze peroxide reduction via a catalytic Cys→-SOH mechanism. This family-level knowledge, learned from numerous peroxiredoxin homologs, directly identifies position 60 (Cys) with the sulfenic acid intermediate description in option C, while option D's 'proton acceptor' mechanism is inconsistent with peroxiredoxin chemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are impossible (positions exceed the 172-aa sequence length). Option D describes a 'proton acceptor' mechanism at an arginine, which is inconsistent with peroxiredoxin catalytic chemistry. Only option C matches both the sequence feature (Cys at position 60 in a PxxC context) and the well-established peroxiredoxin mechanism."
  },
  "important_caveats": [
    "The UniProt annotation for position 60 is by similarity (ECO:0000250 from P38013/yeast Tsa1), not direct experimental evidence on this specific protein. However, the peroxiredoxin catalytic mechanism is experimentally validated across the family.",
    "The peroxiredoxin PxxC motif here reads P-T-C-Q rather than the canonical PxxCP; this is a known variant within the peroxiredoxin superfamily and does not undermine the assignment.",
    "Options A and B appear to be drawn from a completely different protein (possibly a fatty acid synthase subunit given 'beta-ketoacyl synthase' and 'dehydratase' annotations), serving as easy distractors."
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
  "benchmark_sequence_length": 172,
  "benchmark_sequence_sha256": "192d7107c7c1fff1917cea3fb330c144082964f8d6c33e949126d604354b924b",
  "current_entry_audit": {
    "entryVersion": 56,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-10-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 172,
  "current_source_sequence_sha256": "192d7107c7c1fff1917cea3fb330c144082964f8d6c33e949126d604354b924b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 54,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G0S1P8",
  "selected_historical_entry_version": 54,
  "selected_historical_record_sha256": "ad6b8e635a2d1310f20d35c06db92e8909dc4cbae80b5fef229cdcd3da0ecf4f",
  "selected_historical_source_sequence_length": 172,
  "selected_historical_source_sequence_sha256": "192d7107c7c1fff1917cea3fb330c144082964f8d6c33e949126d604354b924b",
  "selected_historical_version": {
    "accession": "G0S1P8",
    "database": "Swiss-Prot",
    "entryVersion": 54,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AHP1_CHATD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0S1P8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G0S1P8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:23.003674+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f",
  "url": "https://rest.uniprot.org/uniprotkb/G0S1P8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0S1P8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":56,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-10-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:23.003674+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f",
  "url": "https://rest.uniprot.org/uniprotkb/G0S1P8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0S1P8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Chaetomium thermophilum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Thermochaetoides\"],\"scientificName\":\"Thermochaetoides thermophila (strain DSM 1495 / CBS 144.50 / DAOM 24625 / IMI 039719)\",\"taxonId\":759272}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:23.003674+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f",
  "url": "https://rest.uniprot.org/uniprotkb/G0S1P8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0S1P8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Alkyl hydroperoxide reductase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P38013\",\"source\":\"UniProtKB\"}],\"value\":\"1.11.1.24\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Peroxiredoxin AHP1\"},\"shortNames\":[{\"value\":\"Prx\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:23.003674+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f",
  "url": "https://rest.uniprot.org/uniprotkb/G0S1P8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0S1P8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cysteine sulfenic acid (-SOH) intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P38013\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":60},\"start\":{\"modifier\":\"EXACT\",\"value\":60}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:28:23.003674+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f",
  "url": "https://rest.uniprot.org/uniprotkb/G0S1P8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0S1P8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H1",
  "excerpt": "ID   AHP1_CHATD              Reviewed;         172 AA.\nAC   G0S1P8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-OCT-2011, sequence version 1.\nDT   28-JAN-2026, entry version 54.\nDE   RecName: Full=Peroxiredoxin AHP1 {ECO:0000305};\nDE            Short=Prx;\nDE            EC=1.11.1.24 {ECO:0000250|UniProtKB:P38013};\nDE   AltName: Full=Alkyl hydroperoxide reductase;\nGN   Name=AHP1; ORFNames=CTHT_0014370;\nOS   Chaetomium thermophilum (strain DSM 1495 / CBS 144.50 / IMI 039719)\nOS   (Thermochaetoides thermophila).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Thermochaetoides.\nOX   NCBI_TaxID=759272;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:28.092103+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ad6b8e635a2d1310f20d35c06db92e8909dc4cbae80b5fef229cdcd3da0ecf4f",
  "url": "https://rest.uniprot.org/unisave/G0S1P8?format=txt&versions=54"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0S1P8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H2",
  "excerpt": "FT   ACT_SITE        60\nFT                   /note=\"Cysteine sulfenic acid (-SOH) intermediate\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P38013\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:28.092103+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ad6b8e635a2d1310f20d35c06db92e8909dc4cbae80b5fef229cdcd3da0ecf4f",
  "url": "https://rest.uniprot.org/unisave/G0S1P8?format=txt&versions=54"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
