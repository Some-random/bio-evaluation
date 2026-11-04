# active_site_0054

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0054.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 156 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEPSKMEVKIISSETIKPSSPTPSHLRKYTLSLLDQKYTPIVVPAILFYERPQGVAPLDMDRLRTCLSQTLTAFYPLAGRAESRDVIICNDEGIPFVEAHVDCELSSVVKSLSSLGSDLRSFYPPRDGLLEGGIQFAIQMNVFSCGGFAFAWYCTHNVTDGTSTANFFRYWTALYAQRSEYAVQDLMDFNSVVTAFPPVPPRVPQEEKPVTTELKPEKQEGQEKEEKKKSSFNFSFQSHIVARSFLIKSKAVAELKAKSVSEEVPYPSRFEAVSAFLWKSIVSSSTTEGKTMINMPVNLRPRVDPPLPLDSVGNIFENALVQSEKKAELHEFVARIRGSISKMKDFATEYQGEKREEAKDAHWKRFIKAVIECKGKDAYVISPWYKSSGFTDIDFGFGTPIRVVPMDDVVNHNQRNTIMLMEFVDSDGDGFEAWMFLEEECIKFLESNPEFLAFASPNF

[Multiple Choices]
A. Position 256 (Proton acceptor)
B. Position 118 (Nucleophile)
C. Position 156 (Proton acceptor)
D. Position 182 (For beta-ketoacyl synthase activity)
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

> The matched-sequence UniProt annotation identifies position 156 as a proton acceptor. This is a similarity-based annotation, not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the BAHD-acyltransferase-like HXXXD motif, including the histidine around position 156. In this enzyme family, the conserved histidine acts as a catalytic general base/proton acceptor, making choice C meaningfully distinguishable from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level motif and catalytic mechanism provide a credible inference from the original sequence; the answer need not depend on recalling this protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered alternatives, the conserved catalytic histidine motif supports position 156 and no other option is comparably supported.


### Important caveats

- The source annotation is transferred by similarity and does not establish direct experimental validation for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the BAHD-acyltransferase-like HXXXD motif, including the histidine around position 156. In this enzyme family, the conserved histidine acts as a catalytic general base/proton acceptor, making choice C meaningfully distinguishable from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level motif and catalytic mechanism provide a credible inference from the original sequence; the answer need not depend on recalling this protein's database entry."
  },
  "case_id": "active_site_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies position 156 as a proton acceptor. This is a similarity-based annotation, not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The source annotation is transferred by similarity and does not establish direct experimental validation for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, the conserved catalytic histidine motif supports position 156 and no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies position 156 as a proton acceptor. This is a similarity-based annotation, not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the BAHD-acyltransferase-like HXXXD motif, including the histidine around position 156. In this enzyme family, the conserved histidine acts as a catalytic general base/proton acceptor, making choice C meaningfully distinguishable from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A family-level motif and catalytic mechanism provide a credible inference from the original sequence; the answer need not depend on recalling this protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, the conserved catalytic histidine motif supports position 156 and no other option is comparably supported."
  },
  "important_caveats": [
    "The source annotation is transferred by similarity and does not establish direct experimental validation for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0AAW1LG41, BAHD acyltransferase 1 from Saponaria officinalis) annotates position 156 as 'Proton acceptor' (evidence C5, H3). The residue at position 156 in the supplied sequence is H (Histidine), embedded in the context W-Y-C-T-H-N-V-T-D-G (positions 152-161), which matches the conserved HxxxDG catalytic motif characteristic of the BAHD acyltransferase superfamily. The annotation evidence code is ECO:0000250 (similarity, transferred from Q70PR7), so it is a computational inference from a homolog rather than direct experimental determination on this exact protein, but the HxxDG motif's role as a general base/proton acceptor is well-established across the BAHD family. The answer is consistent with the annotation and with the family mechanism.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains a recognizable HxxxDG motif at positions 156-161 (H-N-V-T-D-G), which is the hallmark catalytic motif of the BAHD acyltransferase superfamily. In BAHD enzymes, the conserved histidine in this motif acts as a general base (proton acceptor) that deprotonates the substrate hydroxyl to generate the nucleophile. A model with knowledge of the BAHD family can scan the sequence for the H...DG pattern, identify H(156) as the catalytic histidine, and assign it the proton-acceptor role. The distractors are mechanistically inconsistent: position 256 is K (lysine, not a proton acceptor in BAHD catalysis), position 118 is D (aspartate, not a nucleophile in this enzyme class—the substrate hydroxyl is the nucleophile), and position 182 is A (alanine, catalytically inert, and 'beta-ketoacyl synthase activity' refers to a completely different enzyme class). Thus, family-level motif recognition plus established BAHD mechanism meaningfully distinguishes choice C from all alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HxxDG/HxxxDG motif is a widely recognized family-level signature of BAHD acyltransferases. Its identification from the raw sequence and the assignment of the histidine as proton acceptor rely on transferable knowledge of the BAHD superfamily, not on a unique annotation of this exact protein. The four options are mechanistically distinct (K, D-as-nucleophile, H-as-proton-acceptor, A-for-unrelated-enzyme-class), so the family motif alone is sufficient to select C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices involve different residue types (K, D, H, A) and different mechanistic roles (proton acceptor, nucleophile, proton acceptor, beta-ketoacyl synthase activity). Only H(156) in the HxxxDG context matches the established BAHD catalytic mechanism. The other options are mechanistically incompatible with BAHD acyltransferase chemistry. No genuine ambiguity exists among the offered alternatives.


### Important caveats

- The UniProt annotation for position 156 carries evidence code ECO:0000250 (similarity), meaning the proton-acceptor assignment is inferred by homology from Q70PR7 rather than directly demonstrated on this exact protein. The HxxDG motif's role is well-supported across the BAHD family, but the specific annotation for this sequence is a computational transfer.
- The motif spacing here is HxxxDG (three residues between H and D) rather than the canonical HxxDG (two residues). This is a recognized variant within the BAHD superfamily and does not alter the catalytic role of the histidine.
- Position 394 is also annotated as 'Proton acceptor' in the UniProt entry (C6, H4) with the same similarity evidence. Position 394 is D (aspartate), which is unusual for a proton-acceptor label and may reflect an annotation-transfer artifact. This second site is not offered as a choice, so it does not create ambiguity for this question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains a recognizable HxxxDG motif at positions 156-161 (H-N-V-T-D-G), which is the hallmark catalytic motif of the BAHD acyltransferase superfamily. In BAHD enzymes, the conserved histidine in this motif acts as a general base (proton acceptor) that deprotonates the substrate hydroxyl to generate the nucleophile. A model with knowledge of the BAHD family can scan the sequence for the H...DG pattern, identify H(156) as the catalytic histidine, and assign it the proton-acceptor role. The distractors are mechanistically inconsistent: position 256 is K (lysine, not a proton acceptor in BAHD catalysis), position 118 is D (aspartate, not a nucleophile in this enzyme class—the substrate hydroxyl is the nucleophile), and position 182 is A (alanine, catalytically inert, and 'beta-ketoacyl synthase activity' refers to a completely different enzyme class). Thus, family-level motif recognition plus established BAHD mechanism meaningfully distinguishes choice C from all alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HxxDG/HxxxDG motif is a widely recognized family-level signature of BAHD acyltransferases. Its identification from the raw sequence and the assignment of the histidine as proton acceptor rely on transferable knowledge of the BAHD superfamily, not on a unique annotation of this exact protein. The four options are mechanistically distinct (K, D-as-nucleophile, H-as-proton-acceptor, A-for-unrelated-enzyme-class), so the family motif alone is sufficient to select C."
  },
  "case_id": "active_site_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0AAW1LG41, BAHD acyltransferase 1 from Saponaria officinalis) annotates position 156 as 'Proton acceptor' (evidence C5, H3). The residue at position 156 in the supplied sequence is H (Histidine), embedded in the context W-Y-C-T-H-N-V-T-D-G (positions 152-161), which matches the conserved HxxxDG catalytic motif characteristic of the BAHD acyltransferase superfamily. The annotation evidence code is ECO:0000250 (similarity, transferred from Q70PR7), so it is a computational inference from a homolog rather than direct experimental determination on this exact protein, but the HxxDG motif's role as a general base/proton acceptor is well-established across the BAHD family. The answer is consistent with the annotation and with the family mechanism."
  },
  "important_caveats": [
    "The UniProt annotation for position 156 carries evidence code ECO:0000250 (similarity), meaning the proton-acceptor assignment is inferred by homology from Q70PR7 rather than directly demonstrated on this exact protein. The HxxDG motif's role is well-supported across the BAHD family, but the specific annotation for this sequence is a computational transfer.",
    "The motif spacing here is HxxxDG (three residues between H and D) rather than the canonical HxxDG (two residues). This is a recognized variant within the BAHD superfamily and does not alter the catalytic role of the histidine.",
    "Position 394 is also annotated as 'Proton acceptor' in the UniProt entry (C6, H4) with the same similarity evidence. Position 394 is D (aspartate), which is unusual for a proton-acceptor label and may reflect an annotation-transfer artifact. This second site is not offered as a choice, so it does not create ambiguity for this question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices involve different residue types (K, D, H, A) and different mechanistic roles (proton acceptor, nucleophile, proton acceptor, beta-ketoacyl synthase activity). Only H(156) in the HxxxDG context matches the established BAHD catalytic mechanism. The other options are mechanistically incompatible with BAHD acyltransferase chemistry. No genuine ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0AAW1LG41, BAHD acyltransferase 1 from Saponaria officinalis) annotates position 156 as 'Proton acceptor' (evidence C5, H3). The residue at position 156 in the supplied sequence is H (Histidine), embedded in the context W-Y-C-T-H-N-V-T-D-G (positions 152-161), which matches the conserved HxxxDG catalytic motif characteristic of the BAHD acyltransferase superfamily. The annotation evidence code is ECO:0000250 (similarity, transferred from Q70PR7), so it is a computational inference from a homolog rather than direct experimental determination on this exact protein, but the HxxDG motif's role as a general base/proton acceptor is well-established across the BAHD family. The answer is consistent with the annotation and with the family mechanism.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence contains a recognizable HxxxDG motif at positions 156-161 (H-N-V-T-D-G), which is the hallmark catalytic motif of the BAHD acyltransferase superfamily. In BAHD enzymes, the conserved histidine in this motif acts as a general base (proton acceptor) that deprotonates the substrate hydroxyl to generate the nucleophile. A model with knowledge of the BAHD family can scan the sequence for the H...DG pattern, identify H(156) as the catalytic histidine, and assign it the proton-acceptor role. The distractors are mechanistically inconsistent: position 256 is K (lysine, not a proton acceptor in BAHD catalysis), position 118 is D (aspartate, not a nucleophile in this enzyme class—the substrate hydroxyl is the nucleophile), and position 182 is A (alanine, catalytically inert, and 'beta-ketoacyl synthase activity' refers to a completely different enzyme class). Thus, family-level motif recognition plus established BAHD mechanism meaningfully distinguishes choice C from all alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The HxxDG/HxxxDG motif is a widely recognized family-level signature of BAHD acyltransferases. Its identification from the raw sequence and the assignment of the histidine as proton acceptor rely on transferable knowledge of the BAHD superfamily, not on a unique annotation of this exact protein. The four options are mechanistically distinct (K, D-as-nucleophile, H-as-proton-acceptor, A-for-unrelated-enzyme-class), so the family motif alone is sufficient to select C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices involve different residue types (K, D, H, A) and different mechanistic roles (proton acceptor, nucleophile, proton acceptor, beta-ketoacyl synthase activity). Only H(156) in the HxxxDG context matches the established BAHD catalytic mechanism. The other options are mechanistically incompatible with BAHD acyltransferase chemistry. No genuine ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The UniProt annotation for position 156 carries evidence code ECO:0000250 (similarity), meaning the proton-acceptor assignment is inferred by homology from Q70PR7 rather than directly demonstrated on this exact protein. The HxxDG motif's role is well-supported across the BAHD family, but the specific annotation for this sequence is a computational transfer.",
    "The motif spacing here is HxxxDG (three residues between H and D) rather than the canonical HxxDG (two residues). This is a recognized variant within the BAHD superfamily and does not alter the catalytic role of the histidine.",
    "Position 394 is also annotated as 'Proton acceptor' in the UniProt entry (C6, H4) with the same similarity evidence. Position 394 is D (aspartate), which is unusual for a proton-acceptor label and may reflect an annotation-transfer artifact. This second site is not offered as a choice, so it does not create ambiguity for this question."
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
  "benchmark_sequence_length": 459,
  "benchmark_sequence_sha256": "26ed0fa20fc132fc6d2a47c811d0cd8d71f191da088736328b12b747d0946563",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 459,
  "current_source_sequence_sha256": "26ed0fa20fc132fc6d2a47c811d0cd8d71f191da088736328b12b747d0946563",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAW1LG41",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "selected_historical_source_sequence_length": 459,
  "selected_historical_source_sequence_sha256": "26ed0fa20fc132fc6d2a47c811d0cd8d71f191da088736328b12b747d0946563",
  "selected_historical_version": {
    "accession": "A0AAW1LG41",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BAHD1_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1LG41\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"BAHD acyltransferase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoBAHD1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q70PR7\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":156},\"start\":{\"modifier\":\"EXACT\",\"value\":156}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q70PR7\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":394},\"start\":{\"modifier\":\"EXACT\",\"value\":394}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48159.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   BAHD1_SAPOF             Reviewed;         459 AA.\nAC   A0AAW1LG41;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=BAHD acyltransferase 1 {ECO:0000303|PubMed:39043959};\nDE            Short=SoBAHD1 {ECO:0000303|PubMed:39043959};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:39043959};\nGN   Name=BAHD1 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11017477m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_04G021000 {ECO:0000312|EMBL:KAK9732775.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:42.902980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "url": "https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48159.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:42.902980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "url": "https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        156\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q70PR7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:42.902980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "url": "https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        394\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q70PR7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:42.902980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "url": "https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 54. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
