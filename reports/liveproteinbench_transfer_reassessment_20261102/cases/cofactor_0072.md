# cofactor_0072

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0072.txt)

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
MATKRKVIITCAPTGAIHTPSMSPYLPVTPQQIGDAALAAAKEGAAIIHLHARDPDDGHPTQDPAVFQEFLPRIKAECDAVINLTTGGSPHMTVAERLKPAHHFQPEVASLNMGSMNFGLYPMLERFKELKYDWERKHLENSRDLVFKNTFADIEYILTSCGANGTRFEFECYDISHLYNLAHFVDRGLAKPPFFVQSVFGLLGGIGAHPEDLAHMRRTADRLFGKDYVWSILGAGRNQIPLASIGVAQGSNARVGLEDSLWIEPGKLAESSAAQVRKIRQVIEGLSLDIATPAEAREMLQLKGAANTNF

[Multiple Choices]
A. [4Fe-4S] cluster
B. Zn(2+)
C. pyridoxal 5'-phosphate
D. FMN
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

> The sequence-matched UniProt record annotates Zn(2+) as a cofactor. That annotation is transferred by similarity from a related UniProt entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a plausible metal-binding pattern, including H-L-H-A-R-D (an HxHxD-like motif), alongside additional histidines and acidic residues. Such His/Asp-rich motifs are characteristic of some zinc-dependent metalloenzyme families. This favors Zn over the offered Fe-S, PLP, and FMN choices, although the sequence pattern alone is not conclusive.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable sequence-based inference meaningfully favors Zn among these alternatives; it does not require knowing the exact protein's database annotation. The inference is probabilistic rather than proof of cofactor occupancy or catalytic requirement.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported by the sequence features.


### Important caveats

- The supplied database cofactor annotation is similarity-based, not identified here as a direct measurement on this exact protein.
- Histidine- and acidic-residue patterns can suggest metal binding but do not independently establish zinc binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a plausible metal-binding pattern, including H-L-H-A-R-D (an HxHxD-like motif), alongside additional histidines and acidic residues. Such His/Asp-rich motifs are characteristic of some zinc-dependent metalloenzyme families. This favors Zn over the offered Fe-S, PLP, and FMN choices, although the sequence pattern alone is not conclusive.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-based inference meaningfully favors Zn among these alternatives; it does not require knowing the exact protein's database annotation. The inference is probabilistic rather than proof of cofactor occupancy or catalytic requirement."
  },
  "case_id": "cofactor_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Zn(2+) as a cofactor. That annotation is transferred by similarity from a related UniProt entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied database cofactor annotation is similarity-based, not identified here as a direct measurement on this exact protein.",
    "Histidine- and acidic-residue patterns can suggest metal binding but do not independently establish zinc binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Zn(2+) as a cofactor. That annotation is transferred by similarity from a related UniProt entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a plausible metal-binding pattern, including H-L-H-A-R-D (an HxHxD-like motif), alongside additional histidines and acidic residues. Such His/Asp-rich motifs are characteristic of some zinc-dependent metalloenzyme families. This favors Zn over the offered Fe-S, PLP, and FMN choices, although the sequence pattern alone is not conclusive.",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-based inference meaningfully favors Zn among these alternatives; it does not require knowing the exact protein's database annotation. The inference is probabilistic rather than proof of cofactor occupancy or catalytic requirement."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence features."
  },
  "important_caveats": [
    "The supplied database cofactor annotation is similarity-based, not identified here as a direct measurement on this exact protein.",
    "Histidine- and acidic-residue patterns can suggest metal binding but do not independently establish zinc binding."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5/H4) explicitly lists Zn(2+) as the cofactor for this entry (B1G5Y9, 3,5-dioxohexanoate:acetyl-CoA acetone transferase, EC 2.3.1.319). The evidence code is ECO:0000250 (inferred by similarity from B0VHH0), so the cofactor assignment is computational transfer rather than direct experimental measurement on this exact protein. However, the enzyme's function and biophysical properties were experimentally characterized (PubMed 24240508, Bastard et al. 2014), and the Zn(2+) annotation is consistent with the characterized enzyme family. The sequence matches the benchmark input exactly.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains clusters of His, Cys, and Asp residues (e.g., 'CAPTGAIHT', 'HLHARD', 'HARDPDDGHPTQ', 'SCGANGTRFEFECYDISHLYNLAHFVDRG') consistent with Zn(2+) coordination geometry. Critically, the sequence lacks: (1) a Rossmann-fold GxGxxG motif or other FMN-binding signatures, making FMN unlikely; (2) the characteristic lysine-in-context and conserved motifs of PLP-dependent enzymes (aminotransferases, amino acid decarboxylases), making PLP unlikely; (3) the canonical CxxCxxC...C four-cysteine spacing required for &#91;4Fe-4S&#93; cluster ligation. The enzyme is a CoA-transferase/cleavage enzyme (not an oxidoreductase), which further disfavors FMN. Recognition of the 'CAPTGAIHT' motif and overall ~310-aa fold as belonging to the acetoacetate decarboxylase/acetone carboxylase superfamily—a family well-known from other members (e.g., acetoacetate decarboxylase from Clostridium) to require Zn(2+)—provides additional family-level transferable support. Together, the positive metal-coordinating residue pattern and the systematic absence of motifs for the three distractors meaningfully distinguish Zn(2+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate FMN (no oxidoreductase context, no Rossmann fold), PLP (no aminotransferase/decarboxylase context, no PLP-binding lysine motif), and &#91;4Fe-4S&#93; (no 4-Cys cluster spacing) by the absence of their signature sequence features, while the His/Cys/Asp clusters and family-level resemblance to Zn-dependent CoA-transferase/decarboxylase enzymes positively support Zn(2+). This is legitimate transfer from other proteins in the same family and general cofactor-binding principles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors each require specific structural motifs (Rossmann fold for FMN, PLP-binding lysine context, 4-Cys cluster for &#91;4Fe-4S&#93;) that are absent from the sequence. Zn(2+) is the only option consistent with both the positive features (His/Cys/Asp clusters) and the enzyme class (transferase/cleavage enzyme). No other option is meaningfully supported.


### Important caveats

- The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from B0VHH0), meaning it is a computational transfer rather than a direct experimental measurement on this exact protein sequence.
- The experimental paper (Bastard et al. 2014) characterized function and biophysical properties of the enzyme family, providing indirect experimental support for Zn(2+) dependence in the family context.
- The reviewer identified the protein via accession B1G5Y9 from dataset metadata not provided to the evaluated model; the model must rely solely on sequence features and general knowledge.
- The 'CAPTGAIHT' motif recognition as a family signature depends on the model having learned this pattern from homologous proteins; if the family is obscure, the positive identification of Zn(2+) may rely more heavily on elimination of the other three options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains clusters of His, Cys, and Asp residues (e.g., 'CAPTGAIHT', 'HLHARD', 'HARDPDDGHPTQ', 'SCGANGTRFEFECYDISHLYNLAHFVDRG') consistent with Zn(2+) coordination geometry. Critically, the sequence lacks: (1) a Rossmann-fold GxGxxG motif or other FMN-binding signatures, making FMN unlikely; (2) the characteristic lysine-in-context and conserved motifs of PLP-dependent enzymes (aminotransferases, amino acid decarboxylases), making PLP unlikely; (3) the canonical CxxCxxC...C four-cysteine spacing required for [4Fe-4S] cluster ligation. The enzyme is a CoA-transferase/cleavage enzyme (not an oxidoreductase), which further disfavors FMN. Recognition of the 'CAPTGAIHT' motif and overall ~310-aa fold as belonging to the acetoacetate decarboxylase/acetone carboxylase superfamily—a family well-known from other members (e.g., acetoacetate decarboxylase from Clostridium) to require Zn(2+)—provides additional family-level transferable support. Together, the positive metal-coordinating residue pattern and the systematic absence of motifs for the three distractors meaningfully distinguish Zn(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate FMN (no oxidoreductase context, no Rossmann fold), PLP (no aminotransferase/decarboxylase context, no PLP-binding lysine motif), and [4Fe-4S] (no 4-Cys cluster spacing) by the absence of their signature sequence features, while the His/Cys/Asp clusters and family-level resemblance to Zn-dependent CoA-transferase/decarboxylase enzymes positively support Zn(2+). This is legitimate transfer from other proteins in the same family and general cofactor-binding principles."
  },
  "case_id": "cofactor_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H4) explicitly lists Zn(2+) as the cofactor for this entry (B1G5Y9, 3,5-dioxohexanoate:acetyl-CoA acetone transferase, EC 2.3.1.319). The evidence code is ECO:0000250 (inferred by similarity from B0VHH0), so the cofactor assignment is computational transfer rather than direct experimental measurement on this exact protein. However, the enzyme's function and biophysical properties were experimentally characterized (PubMed 24240508, Bastard et al. 2014), and the Zn(2+) annotation is consistent with the characterized enzyme family. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from B0VHH0), meaning it is a computational transfer rather than a direct experimental measurement on this exact protein sequence.",
    "The experimental paper (Bastard et al. 2014) characterized function and biophysical properties of the enzyme family, providing indirect experimental support for Zn(2+) dependence in the family context.",
    "The reviewer identified the protein via accession B1G5Y9 from dataset metadata not provided to the evaluated model; the model must rely solely on sequence features and general knowledge.",
    "The 'CAPTGAIHT' motif recognition as a family signature depends on the model having learned this pattern from homologous proteins; if the family is obscure, the positive identification of Zn(2+) may rely more heavily on elimination of the other three options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors each require specific structural motifs (Rossmann fold for FMN, PLP-binding lysine context, 4-Cys cluster for [4Fe-4S]) that are absent from the sequence. Zn(2+) is the only option consistent with both the positive features (His/Cys/Asp clusters) and the enzyme class (transferase/cleavage enzyme). No other option is meaningfully supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H4) explicitly lists Zn(2+) as the cofactor for this entry (B1G5Y9, 3,5-dioxohexanoate:acetyl-CoA acetone transferase, EC 2.3.1.319). The evidence code is ECO:0000250 (inferred by similarity from B0VHH0), so the cofactor assignment is computational transfer rather than direct experimental measurement on this exact protein. However, the enzyme's function and biophysical properties were experimentally characterized (PubMed 24240508, Bastard et al. 2014), and the Zn(2+) annotation is consistent with the characterized enzyme family. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C5", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains clusters of His, Cys, and Asp residues (e.g., 'CAPTGAIHT', 'HLHARD', 'HARDPDDGHPTQ', 'SCGANGTRFEFECYDISHLYNLAHFVDRG') consistent with Zn(2+) coordination geometry. Critically, the sequence lacks: (1) a Rossmann-fold GxGxxG motif or other FMN-binding signatures, making FMN unlikely; (2) the characteristic lysine-in-context and conserved motifs of PLP-dependent enzymes (aminotransferases, amino acid decarboxylases), making PLP unlikely; (3) the canonical CxxCxxC...C four-cysteine spacing required for [4Fe-4S] cluster ligation. The enzyme is a CoA-transferase/cleavage enzyme (not an oxidoreductase), which further disfavors FMN. Recognition of the 'CAPTGAIHT' motif and overall ~310-aa fold as belonging to the acetoacetate decarboxylase/acetone carboxylase superfamily—a family well-known from other members (e.g., acetoacetate decarboxylase from Clostridium) to require Zn(2+)—provides additional family-level transferable support. Together, the positive metal-coordinating residue pattern and the systematic absence of motifs for the three distractors meaningfully distinguish Zn(2+).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate FMN (no oxidoreductase context, no Rossmann fold), PLP (no aminotransferase/decarboxylase context, no PLP-binding lysine motif), and [4Fe-4S] (no 4-Cys cluster spacing) by the absence of their signature sequence features, while the His/Cys/Asp clusters and family-level resemblance to Zn-dependent CoA-transferase/decarboxylase enzymes positively support Zn(2+). This is legitimate transfer from other proteins in the same family and general cofactor-binding principles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors each require specific structural motifs (Rossmann fold for FMN, PLP-binding lysine context, 4-Cys cluster for [4Fe-4S]) that are absent from the sequence. Zn(2+) is the only option consistent with both the positive features (His/Cys/Asp clusters) and the enzyme class (transferase/cleavage enzyme). No other option is meaningfully supported."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from B0VHH0), meaning it is a computational transfer rather than a direct experimental measurement on this exact protein sequence.",
    "The experimental paper (Bastard et al. 2014) characterized function and biophysical properties of the enzyme family, providing indirect experimental support for Zn(2+) dependence in the family context.",
    "The reviewer identified the protein via accession B1G5Y9 from dataset metadata not provided to the evaluated model; the model must rely solely on sequence features and general knowledge.",
    "The 'CAPTGAIHT' motif recognition as a family signature depends on the model having learned this pattern from homologous proteins; if the family is obscure, the positive identification of Zn(2+) may rely more heavily on elimination of the other three options."
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
  "benchmark_sequence_length": 310,
  "benchmark_sequence_sha256": "669119f3660e25802e4d9d5d3abdcf25e9feb3666a00e1d4a9a294493841e494",
  "current_entry_audit": {
    "entryVersion": 44,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-04-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 310,
  "current_source_sequence_sha256": "669119f3660e25802e4d9d5d3abdcf25e9feb3666a00e1d4a9a294493841e494",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 43,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B1G5Y9",
  "selected_historical_entry_version": 43,
  "selected_historical_record_sha256": "d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94",
  "selected_historical_source_sequence_length": 310,
  "selected_historical_source_sequence_sha256": "669119f3660e25802e4d9d5d3abdcf25e9feb3666a00e1d4a9a294493841e494",
  "selected_historical_version": {
    "accession": "B1G5Y9",
    "database": "Swiss-Prot",
    "entryVersion": 43,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "DOHCE_PARG4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B1G5Y9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":44,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-04-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Burkholderiaceae\",\"Paraburkholderia\"],\"scientificName\":\"Paraburkholderia graminis (strain ATCC 700544 / DSM 17151 / LMG 18924 / NCIMB 13744 / C4D1M)\",\"taxonId\":396598}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"3,5-dioxohexanoate cleavage enzyme\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"value\":\"BKACE_274\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.319\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"3,5-dioxohexanoate:acetyl-CoA acetone transferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"B0VHH0\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bastard K.\",\"Smith A.A.\",\"Vergne-Vaxelaire C.\",\"Perret A.\",\"Zaparucha A.\",\"De Melo-Minardi R.\",\"Mariage A.\",\"Boutard M.\",\"Debard A.\",\"Lechaplais C.\",\"Pelle C.\",\"Pellouin V.\",\"Perchat N.\",\"Petit J.L.\",\"Kreimeyer A.\",\"Medigue C.\",\"Weissenbach J.\",\"Artiguenave F.\",\"De Berardinis V.\",\"Vallenet D.\",\"Salanoubat M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24240508\"},{\"database\":\"DOI\",\"id\":\"10.1038/nchembio.1387\"}],\"citationType\":\"journal article\",\"firstPage\":\"42\",\"id\":\"24240508\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"49\",\"publicationDate\":\"2014\",\"title\":\"Revealing the hidden functional diversity of an enzyme family.\",\"volume\":\"10\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H1",
  "excerpt": "ID   DOHCE_PARG4             Reviewed;         310 AA.\nAC   B1G5Y9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-APR-2008, sequence version 1.\nDT   28-JAN-2026, entry version 43.\nDE   RecName: Full=3,5-dioxohexanoate:acetyl-CoA acetone transferase {ECO:0000305};\nDE            EC=2.3.1.319 {ECO:0000269|PubMed:24240508};\nDE   AltName: Full=3,5-dioxohexanoate cleavage enzyme {ECO:0000305};\nDE   AltName: Full=BKACE_274 {ECO:0000303|PubMed:24240508};\nGN   Name=kce_3 {ECO:0000312|EMBL:CAB3715113.1};\nGN   ORFNames=BgramDRAFT_4880 {ECO:0000312|EMBL:EDT08458.1},\nGN   R8871_04389 {ECO:0000312|EMBL:CAB3715113.1};\nOS   Paraburkholderia graminis (strain ATCC 700544 / DSM 17151 / LMG 18924 /\nOS   NCIMB 13744 / C4D1M).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Burkholderiaceae; Paraburkholderia.\nOX   NCBI_TaxID=396598;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.999580+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94",
  "url": "https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=3,5-dioxohexanoate:acetyl-CoA acetone transferase {ECO:0000305};\nDE            EC=2.3.1.319 {ECO:0000269|PubMed:24240508};\nDE   AltName: Full=3,5-dioxohexanoate cleavage enzyme {ECO:0000305};\nDE   AltName: Full=BKACE_274 {ECO:0000303|PubMed:24240508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.999580+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94",
  "url": "https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=24240508; DOI=10.1038/nchembio.1387;\nRA   Bastard K., Smith A.A., Vergne-Vaxelaire C., Perret A., Zaparucha A.,\nRA   De Melo-Minardi R., Mariage A., Boutard M., Debard A., Lechaplais C.,\nRA   Pelle C., Pellouin V., Perchat N., Petit J.L., Kreimeyer A., Medigue C.,\nRA   Weissenbach J., Artiguenave F., De Berardinis V., Vallenet D.,\nRA   Salanoubat M.;\nRT   \"Revealing the hidden functional diversity of an enzyme family.\";\nRL   Nat. Chem. Biol. 10:42-49(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.999580+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94",
  "url": "https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:B0VHH0};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.999580+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94",
  "url": "https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 72. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
