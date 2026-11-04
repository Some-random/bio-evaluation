# cofactor_0176

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0176.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Mn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSKTDFSHDLLRFSDEVKEALHSGKPVVALESTVIAHGLPYPENVATARKIEAAVRAEGAIPATIGIENGRFLIGMSDADLERFGSTRGIPKASSRDIPVILAQGGMGATTVASSLVAADLAGIPFFASAGIGGVHRGAERSMDISADLIQFTRSRVAVVCAGAKSILDLGLTLEYLETQCVPIISYQSDDFPAFYCRSSGFHSPHRLDDATVIARSIDMHWKLGNQSSVLITHPIHEEDAIGTDEVESIIREAAVQAEHEGIRGPGATPYLMRAVAKATEGKTVKANMSVLISTAALAGKLACAHIDYLRQQNQA

[Multiple Choices]
A. pyridoxal 5'-phosphate
B. cob(II)alamin
C. heme
D. Mn(2+)
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

> The exact-sequence-matched UniProt annotation assigns Mn(2+) as the cofactor, citing a HAMAP family rule that predicts one Mn(2+) ion per subunit. This supports the key as a computational family-based annotation, not as direct experimental evidence in the supplied material.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model could recognize the sequence as belonging to the bacterial pseudouridine-5'-phosphate glycosidase family and transfer the family-level association with Mn(2+). That distinguishes D from PLP, cob(II)alamin, and heme, which require different enzyme-family features or cofactor-binding architectures. This is a probabilistic sequence-family inference, not proof of metal binding from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinction can be made through transferable family knowledge applied to sequence similarity and architecture, without needing the accession or recorded annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence and the family-level inference support Mn(2+); no other offered option is comparably supported.


### Important caveats

- The cited cofactor evidence is computational and family-rule-based; it does not establish direct experimental measurement of Mn(2+) binding for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as belonging to the bacterial pseudouridine-5'-phosphate glycosidase family and transfer the family-level association with Mn(2+). That distinguishes D from PLP, cob(II)alamin, and heme, which require different enzyme-family features or cofactor-binding architectures. This is a probabilistic sequence-family inference, not proof of metal binding from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinction can be made through transferable family knowledge applied to sequence similarity and architecture, without needing the accession or recorded annotation for this exact protein."
  },
  "case_id": "cofactor_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt annotation assigns Mn(2+) as the cofactor, citing a HAMAP family rule that predicts one Mn(2+) ion per subunit. This supports the key as a computational family-based annotation, not as direct experimental evidence in the supplied material."
  },
  "important_caveats": [
    "The cited cofactor evidence is computational and family-rule-based; it does not establish direct experimental measurement of Mn(2+) binding for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence and the family-level inference support Mn(2+); no other offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt annotation assigns Mn(2+) as the cofactor, citing a HAMAP family rule that predicts one Mn(2+) ion per subunit. This supports the key as a computational family-based annotation, not as direct experimental evidence in the supplied material.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as belonging to the bacterial pseudouridine-5'-phosphate glycosidase family and transfer the family-level association with Mn(2+). That distinguishes D from PLP, cob(II)alamin, and heme, which require different enzyme-family features or cofactor-binding architectures. This is a probabilistic sequence-family inference, not proof of metal binding from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "The distinction can be made through transferable family knowledge applied to sequence similarity and architecture, without needing the accession or recorded annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence and the family-level inference support Mn(2+); no other offered option is comparably supported."
  },
  "important_caveats": [
    "The cited cofactor evidence is computational and family-rule-based; it does not establish direct experimental measurement of Mn(2+) binding for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for Q9L393 (Pseudouridine-5'-phosphate glycosidase, EC 4.2.1.70) annotates Mn(2+) as the cofactor (1 ion per subunit), based on HAMAP-Rule MF_01876 (evidence code ECO:0000255, computational inference). The key matches the recorded annotation. Note that the evidence is computational (HAMAP rule), not experimentally validated.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence can be assessed by elimination of the three other cofactor classes using well-established binding-motif knowledge transferable from other proteins: (1) PLP-dependent enzymes (aminotransferases, decarboxylases) require a conserved catalytic Lys in a specific structural context to form a Schiff base; no such motif is apparent here. (2) Cobalamin (B12)-dependent enzymes possess a characteristic B12-binding domain with conserved motifs (e.g., the DXHXXG Rossmann-like fold or the B12-binding subdomain with specific His/Cys axial ligands); none are present. (3) Heme-binding proteins typically feature Cys-His or His-His axial ligand pairs in defined spacing (e.g., the CXXCH motif of cytochromes or the proximal/distal His pair of peroxidases); no such pattern is evident. (4) The sequence contains multiple potential divalent-metal-coordinating residues—Asp (e.g., 'DADLER', 'QSDDFPAFYCRSSGFHSPHRLDD', 'IHEEDAIGTDEVES'), Glu ('LETQ', 'DEVES'), Cys ('VCAG', 'CVPIISYQSDDFPAFYCRSSGFHSPHRLDD', 'LACAHIDYLRQQNQA'), and His ('HSPHRLDD', 'HIDYLRQQNQA')—consistent with a Mn(2+)-coordinating site. The absence of the hallmark motifs for A, B, and C, combined with the presence of a plausible metal-coordination cluster, meaningfully distinguishes D from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination argument relies on the well-known structural motifs required for PLP, B12, and heme binding, which are absent from the sequence, and on the presence of multiple acidic/Cys/His residues that are consistent with divalent metal coordination. This is a transferable inference from general biochemistry and protein-family knowledge, not a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (PLP, B12, heme) each require highly specific and well-characterized binding motifs that are clearly absent from the sequence. Mn(2+) is the only option consistent with the observed residue composition and the absence of the other cofactors' signature motifs. No other option is defensible.


### Important caveats

- The UniProt Mn(2+) annotation is based on a HAMAP computational rule (ECO:0000255), not direct experimental measurement. The cofactor assignment is inferred by pattern/similarity matching.
- The metal-coordinating residue pattern (multiple Asp, Glu, Cys, His) is suggestive but not uniquely diagnostic of Mn(2+) over other divalent metals (e.g., Zn2+, Mg2+); however, those alternatives are not offered as choices, so the discrimination among the four given options is still clear.
- The sequence lacks the N-terminal signal peptide or other features that might hint at the enzyme's specific function, making the identification of this particular glycosidase from sequence alone challenging, but the cofactor elimination logic does not require identifying the exact enzyme.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence can be assessed by elimination of the three other cofactor classes using well-established binding-motif knowledge transferable from other proteins: (1) PLP-dependent enzymes (aminotransferases, decarboxylases) require a conserved catalytic Lys in a specific structural context to form a Schiff base; no such motif is apparent here. (2) Cobalamin (B12)-dependent enzymes possess a characteristic B12-binding domain with conserved motifs (e.g., the DXHXXG Rossmann-like fold or the B12-binding subdomain with specific His/Cys axial ligands); none are present. (3) Heme-binding proteins typically feature Cys-His or His-His axial ligand pairs in defined spacing (e.g., the CXXCH motif of cytochromes or the proximal/distal His pair of peroxidases); no such pattern is evident. (4) The sequence contains multiple potential divalent-metal-coordinating residues—Asp (e.g., 'DADLER', 'QSDDFPAFYCRSSGFHSPHRLDD', 'IHEEDAIGTDEVES'), Glu ('LETQ', 'DEVES'), Cys ('VCAG', 'CVPIISYQSDDFPAFYCRSSGFHSPHRLDD', 'LACAHIDYLRQQNQA'), and His ('HSPHRLDD', 'HIDYLRQQNQA')—consistent with a Mn(2+)-coordinating site. The absence of the hallmark motifs for A, B, and C, combined with the presence of a plausible metal-coordination cluster, meaningfully distinguishes D from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination argument relies on the well-known structural motifs required for PLP, B12, and heme binding, which are absent from the sequence, and on the presence of multiple acidic/Cys/His residues that are consistent with divalent metal coordination. This is a transferable inference from general biochemistry and protein-family knowledge, not a lookup of this specific protein's record."
  },
  "case_id": "cofactor_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for Q9L393 (Pseudouridine-5'-phosphate glycosidase, EC 4.2.1.70) annotates Mn(2+) as the cofactor (1 ion per subunit), based on HAMAP-Rule MF_01876 (evidence code ECO:0000255, computational inference). The key matches the recorded annotation. Note that the evidence is computational (HAMAP rule), not experimentally validated."
  },
  "important_caveats": [
    "The UniProt Mn(2+) annotation is based on a HAMAP computational rule (ECO:0000255), not direct experimental measurement. The cofactor assignment is inferred by pattern/similarity matching.",
    "The metal-coordinating residue pattern (multiple Asp, Glu, Cys, His) is suggestive but not uniquely diagnostic of Mn(2+) over other divalent metals (e.g., Zn2+, Mg2+); however, those alternatives are not offered as choices, so the discrimination among the four given options is still clear.",
    "The sequence lacks the N-terminal signal peptide or other features that might hint at the enzyme's specific function, making the identification of this particular glycosidase from sequence alone challenging, but the cofactor elimination logic does not require identifying the exact enzyme."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (PLP, B12, heme) each require highly specific and well-characterized binding motifs that are clearly absent from the sequence. Mn(2+) is the only option consistent with the observed residue composition and the absence of the other cofactors' signature motifs. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for Q9L393 (Pseudouridine-5'-phosphate glycosidase, EC 4.2.1.70) annotates Mn(2+) as the cofactor (1 ion per subunit), based on HAMAP-Rule MF_01876 (evidence code ECO:0000255, computational inference). The key matches the recorded annotation. Note that the evidence is computational (HAMAP rule), not experimentally validated.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence can be assessed by elimination of the three other cofactor classes using well-established binding-motif knowledge transferable from other proteins: (1) PLP-dependent enzymes (aminotransferases, decarboxylases) require a conserved catalytic Lys in a specific structural context to form a Schiff base; no such motif is apparent here. (2) Cobalamin (B12)-dependent enzymes possess a characteristic B12-binding domain with conserved motifs (e.g., the DXHXXG Rossmann-like fold or the B12-binding subdomain with specific His/Cys axial ligands); none are present. (3) Heme-binding proteins typically feature Cys-His or His-His axial ligand pairs in defined spacing (e.g., the CXXCH motif of cytochromes or the proximal/distal His pair of peroxidases); no such pattern is evident. (4) The sequence contains multiple potential divalent-metal-coordinating residues—Asp (e.g., 'DADLER', 'QSDDFPAFYCRSSGFHSPHRLDD', 'IHEEDAIGTDEVES'), Glu ('LETQ', 'DEVES'), Cys ('VCAG', 'CVPIISYQSDDFPAFYCRSSGFHSPHRLDD', 'LACAHIDYLRQQNQA'), and His ('HSPHRLDD', 'HIDYLRQQNQA')—consistent with a Mn(2+)-coordinating site. The absence of the hallmark motifs for A, B, and C, combined with the presence of a plausible metal-coordination cluster, meaningfully distinguishes D from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "The elimination argument relies on the well-known structural motifs required for PLP, B12, and heme binding, which are absent from the sequence, and on the presence of multiple acidic/Cys/His residues that are consistent with divalent metal coordination. This is a transferable inference from general biochemistry and protein-family knowledge, not a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (PLP, B12, heme) each require highly specific and well-characterized binding motifs that are clearly absent from the sequence. Mn(2+) is the only option consistent with the observed residue composition and the absence of the other cofactors' signature motifs. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt Mn(2+) annotation is based on a HAMAP computational rule (ECO:0000255), not direct experimental measurement. The cofactor assignment is inferred by pattern/similarity matching.",
    "The metal-coordinating residue pattern (multiple Asp, Glu, Cys, His) is suggestive but not uniquely diagnostic of Mn(2+) over other divalent metals (e.g., Zn2+, Mg2+); however, those alternatives are not offered as choices, so the discrimination among the four given options is still clear.",
    "The sequence lacks the N-terminal signal peptide or other features that might hint at the enzyme's specific function, making the identification of this particular glycosidase from sequence alone challenging, but the cofactor elimination logic does not require identifying the exact enzyme."
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
  "benchmark_sequence_length": 316,
  "benchmark_sequence_sha256": "79ec54a1b9a163f1fff48088a706f31d4fafb5f1834f53349d86da2f5110f685",
  "current_entry_audit": {
    "entryVersion": 68,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 316,
  "current_source_sequence_sha256": "79ec54a1b9a163f1fff48088a706f31d4fafb5f1834f53349d86da2f5110f685",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9L393",
  "selected_historical_entry_version": 67,
  "selected_historical_record_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "selected_historical_source_sequence_length": 316,
  "selected_historical_source_sequence_sha256": "79ec54a1b9a163f1fff48088a706f31d4fafb5f1834f53349d86da2f5110f685",
  "selected_historical_version": {
    "accession": "Q9L393",
    "database": "Swiss-Prot",
    "entryVersion": 67,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PSUG_DICD3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9L393\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":68,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Erwinia chrysanthemi (strain 3937)\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Pectobacteriaceae\",\"Dickeya\"],\"scientificName\":\"Dickeya dadantii (strain 3937)\",\"taxonId\":198628}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"value\":\"4.2.1.70\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Pseudouridine-5'-phosphate glycosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"value\":\"PsiMP glycosidase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"name\":\"Mn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Binds 1 Mn(2+) ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H1",
  "excerpt": "ID   PSUG_DICD3              Reviewed;         316 AA.\nAC   Q9L393; E0SMH8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Pseudouridine-5'-phosphate glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};\nDE            Short=PsiMP glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};\nDE            EC=4.2.1.70 {ECO:0000255|HAMAP-Rule:MF_01876};\nGN   Name=indA {ECO:0000303|PubMed:11790734};\nGN   Synonyms=psuG {ECO:0000255|HAMAP-Rule:MF_01876};\nGN   OrderedLocusNames=Dda3937_00974 {ECO:0000312|EMBL:ADN00617.1};\nOS   Dickeya dadantii (strain 3937) (Erwinia chrysanthemi (strain 3937)).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Pectobacteriaceae; Dickeya.\nOX   NCBI_TaxID=198628;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Pseudouridine-5'-phosphate glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};\nDE            Short=PsiMP glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};\nDE            EC=4.2.1.70 {ECO:0000255|HAMAP-Rule:MF_01876};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAB87988.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, INDUCTION, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=3937;\nRX   PubMed=11790734; DOI=10.1128/jb.184.3.654-665.2002;\nRA   Reverchon S., Rouanet C., Expert D., Nasser W.;\nRT   \"Characterization of indigoidine biosynthetic genes in Erwinia chrysanthemi\nRT   and role of this blue pigment in pathogenicity.\";\nRL   J. Bacteriol. 184:654-665(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;\nCC         Evidence={ECO:0000255|HAMAP-Rule:MF_01876};\nCC       Note=Binds 1 Mn(2+) ion per subunit. {ECO:0000255|HAMAP-Rule:MF_01876};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 176. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
