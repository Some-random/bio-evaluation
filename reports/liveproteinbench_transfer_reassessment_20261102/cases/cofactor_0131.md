# cofactor_0131

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0131.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | uncertain |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTQPCIISVAITGSLPRKRDNPAVPITVSEQVESTQAAFEAGATLVHLHVRNDDETPSSEPDRFARVLEGIRKHAPGIITQVSTGGRSGAGRERGGMLSLRPDMASLATGSVNFPTRVYDNPPDLVDWLAAEMKAYAIKPEIEAFDLSMIFQAVAMQQAGKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGGHCRTGLEDNVRLDKQTLAPSNAALVSQVAALCEEYGRPVATVAQARALLGLPSMEIDGRSPW

[Multiple Choices]
A. NAD(+)
B. Zn(2+)
C. Co(2+)
D. cob(II)alamin
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

> The sequence-matched UniProt entry annotates Zn(2+) as a cofactor, and the historical entry carries the same annotation. This supports the key, but the cofactor evidence is transferred from a homolog rather than direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: uncertain

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence has no clear NAD-binding or cobalamin-binding signature, and its His/Cys residues could be consistent with metal binding. Those general features do not distinguish Zn(2+) from Co(2+). A family-level inference might resolve that distinction, but the supplied sequence and choices do not establish one.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The sequence-level clues described above are compatible with a metal cofactor but do not identify which of these two metal ions is used.


### Important caveats

- The database cofactor annotation is homology-based, not direct experimental confirmation for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "cannot_determine",
    "missing_item_specific_fact": "",
    "reason": "The sequence has no clear NAD-binding or cobalamin-binding signature, and its His/Cys residues could be consistent with metal binding. Those general features do not distinguish Zn(2+) from Co(2+). A family-level inference might resolve that distinction, but the supplied sequence and choices do not establish one."
  },
  "case_id": "cofactor_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates Zn(2+) as a cofactor, and the historical entry carries the same annotation. This supports the key, but the cofactor evidence is transferred from a homolog rather than direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The database cofactor annotation is homology-based, not direct experimental confirmation for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The sequence-level clues described above are compatible with a metal cofactor but do not identify which of these two metal ions is used."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates Zn(2+) as a cofactor, and the historical entry carries the same annotation. This supports the key, but the cofactor evidence is transferred from a homolog rather than direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "cannot_determine",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "",
    "reason": "The sequence has no clear NAD-binding or cobalamin-binding signature, and its His/Cys residues could be consistent with metal binding. Those general features do not distinguish Zn(2+) from Co(2+). A family-level inference might resolve that distinction, but the supplied sequence and choices do not establish one."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The sequence-level clues described above are compatible with a metal cofactor but do not identify which of these two metal ions is used."
  },
  "important_caveats": [
    "The database cofactor annotation is homology-based, not direct experimental confirmation for this sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q0KAA1 annotates Zn(2+) as the cofactor (evidence_id C5/H4), matching the author's key B. However, the evidence code is ECO:0000250 (inferred by similarity from UniProtKB:B0VHH0), making this a computational/similarity-based annotation rather than direct experimental measurement for this specific protein. The 2014 Nature Chemical Biology paper (PubMed:24240508) established function and catalytic activity but the Zn annotation itself is transferred by similarity. The annotation is consistent with the well-established thiolase superfamily cofactor requirement.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence displays hallmarks of the thiolase superfamily: a catalytic cysteine motif (GHCRTG region), glycine-rich loops, and the overall length (~284 aa) consistent with a thiolase-like fold. The EC number 2.3.1.318 places this enzyme in the transferase (acyltransferase) class. Transferable knowledge provides a strong discrimination chain: (1) NAD(+) is the canonical cofactor for oxidoreductases (EC 1.x.x.x), not transferases, immediately making option A implausible; (2) cob(II)alamin (vitamin B12) is restricted to radical rearrangement enzymes such as methylmalonyl-CoA mutase and diol dehydratase, not acetyltransferases, ruling out D; (3) Co(2+) is found in a narrow set of isomerases and mutases, not in the thiolase family, making C unlikely; (4) The thiolase superfamily (acetyl-CoA acetyltransferase, 3-ketoacyl-CoA thiolase, and related Claisen-type enzymes) is well-established as Zn(2+)-dependent, with the Zn ion stabilizing the enolate intermediate during the condensation/cleavage mechanism. This family-level association between thiolases and Zn(2+) is a broadly learned pattern across dozens of characterized members.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can leverage EC-class logic (transferase vs. oxidoreductase cofactors) and the well-documented Zn(2+) dependence of the thiolase superfamily to eliminate NAD(+), Co(2+), and cob(II)alamin, converging on Zn(2+). The sequence motifs (catalytic Cys, thiolase-like architecture) provide additional family-level cues. No fact specific to this exact protein's experimental measurement is strictly needed to make the distinction among the four offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The EC transferase classification and thiolase-family association with Zn(2+) provide a clear discrimination. NAD(+) and cob(II)alamin are cofactors for entirely different enzyme classes. Co(2+) is not a recognized thiolase cofactor. No two options are genuinely ambiguous given the sequence and family context.


### Important caveats

- The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from B0VHH0), not direct experimental validation for this specific protein. The 2014 paper established catalytic activity and biophysical properties but the Zn assignment is transferred.
- The protein was characterized in 2014 (Nat. Chem. Biol.) as a 'hidden functional diversity' member of the thiolase superfamily, so its exact Zn coordination geometry has not been crystallographically confirmed for this specific enzyme.
- The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning must rely on sequence features and family-level knowledge alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence displays hallmarks of the thiolase superfamily: a catalytic cysteine motif (GHCRTG region), glycine-rich loops, and the overall length (~284 aa) consistent with a thiolase-like fold. The EC number 2.3.1.318 places this enzyme in the transferase (acyltransferase) class. Transferable knowledge provides a strong discrimination chain: (1) NAD(+) is the canonical cofactor for oxidoreductases (EC 1.x.x.x), not transferases, immediately making option A implausible; (2) cob(II)alamin (vitamin B12) is restricted to radical rearrangement enzymes such as methylmalonyl-CoA mutase and diol dehydratase, not acetyltransferases, ruling out D; (3) Co(2+) is found in a narrow set of isomerases and mutases, not in the thiolase family, making C unlikely; (4) The thiolase superfamily (acetyl-CoA acetyltransferase, 3-ketoacyl-CoA thiolase, and related Claisen-type enzymes) is well-established as Zn(2+)-dependent, with the Zn ion stabilizing the enolate intermediate during the condensation/cleavage mechanism. This family-level association between thiolases and Zn(2+) is a broadly learned pattern across dozens of characterized members.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can leverage EC-class logic (transferase vs. oxidoreductase cofactors) and the well-documented Zn(2+) dependence of the thiolase superfamily to eliminate NAD(+), Co(2+), and cob(II)alamin, converging on Zn(2+). The sequence motifs (catalytic Cys, thiolase-like architecture) provide additional family-level cues. No fact specific to this exact protein's experimental measurement is strictly needed to make the distinction among the four offered choices."
  },
  "case_id": "cofactor_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q0KAA1 annotates Zn(2+) as the cofactor (evidence_id C5/H4), matching the author's key B. However, the evidence code is ECO:0000250 (inferred by similarity from UniProtKB:B0VHH0), making this a computational/similarity-based annotation rather than direct experimental measurement for this specific protein. The 2014 Nature Chemical Biology paper (PubMed:24240508) established function and catalytic activity but the Zn annotation itself is transferred by similarity. The annotation is consistent with the well-established thiolase superfamily cofactor requirement."
  },
  "important_caveats": [
    "The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from B0VHH0), not direct experimental validation for this specific protein. The 2014 paper established catalytic activity and biophysical properties but the Zn assignment is transferred.",
    "The protein was characterized in 2014 (Nat. Chem. Biol.) as a 'hidden functional diversity' member of the thiolase superfamily, so its exact Zn coordination geometry has not been crystallographically confirmed for this specific enzyme.",
    "The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning must rely on sequence features and family-level knowledge alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC transferase classification and thiolase-family association with Zn(2+) provide a clear discrimination. NAD(+) and cob(II)alamin are cofactors for entirely different enzyme classes. Co(2+) is not a recognized thiolase cofactor. No two options are genuinely ambiguous given the sequence and family context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q0KAA1 annotates Zn(2+) as the cofactor (evidence_id C5/H4), matching the author's key B. However, the evidence code is ECO:0000250 (inferred by similarity from UniProtKB:B0VHH0), making this a computational/similarity-based annotation rather than direct experimental measurement for this specific protein. The 2014 Nature Chemical Biology paper (PubMed:24240508) established function and catalytic activity but the Zn annotation itself is transferred by similarity. The annotation is consistent with the well-established thiolase superfamily cofactor requirement.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence displays hallmarks of the thiolase superfamily: a catalytic cysteine motif (GHCRTG region), glycine-rich loops, and the overall length (~284 aa) consistent with a thiolase-like fold. The EC number 2.3.1.318 places this enzyme in the transferase (acyltransferase) class. Transferable knowledge provides a strong discrimination chain: (1) NAD(+) is the canonical cofactor for oxidoreductases (EC 1.x.x.x), not transferases, immediately making option A implausible; (2) cob(II)alamin (vitamin B12) is restricted to radical rearrangement enzymes such as methylmalonyl-CoA mutase and diol dehydratase, not acetyltransferases, ruling out D; (3) Co(2+) is found in a narrow set of isomerases and mutases, not in the thiolase family, making C unlikely; (4) The thiolase superfamily (acetyl-CoA acetyltransferase, 3-ketoacyl-CoA thiolase, and related Claisen-type enzymes) is well-established as Zn(2+)-dependent, with the Zn ion stabilizing the enolate intermediate during the condensation/cleavage mechanism. This family-level association between thiolases and Zn(2+) is a broadly learned pattern across dozens of characterized members.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can leverage EC-class logic (transferase vs. oxidoreductase cofactors) and the well-documented Zn(2+) dependence of the thiolase superfamily to eliminate NAD(+), Co(2+), and cob(II)alamin, converging on Zn(2+). The sequence motifs (catalytic Cys, thiolase-like architecture) provide additional family-level cues. No fact specific to this exact protein's experimental measurement is strictly needed to make the distinction among the four offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC transferase classification and thiolase-family association with Zn(2+) provide a clear discrimination. NAD(+) and cob(II)alamin are cofactors for entirely different enzyme classes. Co(2+) is not a recognized thiolase cofactor. No two options are genuinely ambiguous given the sequence and family context."
  },
  "important_caveats": [
    "The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from B0VHH0), not direct experimental validation for this specific protein. The 2014 paper established catalytic activity and biophysical properties but the Zn assignment is transferred.",
    "The protein was characterized in 2014 (Nat. Chem. Biol.) as a 'hidden functional diversity' member of the thiolase superfamily, so its exact Zn coordination geometry has not been crystallographically confirmed for this specific enzyme.",
    "The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning must rely on sequence features and family-level knowledge alone."
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
  "benchmark_sequence_length": 284,
  "benchmark_sequence_sha256": "578ee40d19a4187b96bbd813dd5b2ad6c5cd4952c2e58954fc66e0445da2dd06",
  "current_entry_audit": {
    "entryVersion": 89,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 284,
  "current_source_sequence_sha256": "578ee40d19a4187b96bbd813dd5b2ad6c5cd4952c2e58954fc66e0445da2dd06",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 87,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0KAA1",
  "selected_historical_entry_version": 87,
  "selected_historical_record_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "selected_historical_source_sequence_length": 284,
  "selected_historical_source_sequence_sha256": "578ee40d19a4187b96bbd813dd5b2ad6c5cd4952c2e58954fc66e0445da2dd06",
  "selected_historical_version": {
    "accession": "Q0KAA1",
    "database": "Swiss-Prot",
    "entryVersion": 87,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "3OXCE_CUPNH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0KAA1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":89,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ralstonia eutropha\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Burkholderiaceae\",\"Cupriavidus\"],\"scientificName\":\"Cupriavidus necator (strain ATCC 17699 / DSM 428 / KCTC 22496 / NCIMB 10442 / H16 / Stanier 337)\",\"taxonId\":381666}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"3-oxoadipate cleavage enzyme\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"value\":\"BKACE_378\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.318\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"3-oxoadipate:acetyl-CoA acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"B0VHH0\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bastard K.\",\"Smith A.A.\",\"Vergne-Vaxelaire C.\",\"Perret A.\",\"Zaparucha A.\",\"De Melo-Minardi R.\",\"Mariage A.\",\"Boutard M.\",\"Debard A.\",\"Lechaplais C.\",\"Pelle C.\",\"Pellouin V.\",\"Perchat N.\",\"Petit J.L.\",\"Kreimeyer A.\",\"Medigue C.\",\"Weissenbach J.\",\"Artiguenave F.\",\"De Berardinis V.\",\"Vallenet D.\",\"Salanoubat M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24240508\"},{\"database\":\"DOI\",\"id\":\"10.1038/nchembio.1387\"}],\"citationType\":\"journal article\",\"firstPage\":\"42\",\"id\":\"24240508\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"49\",\"publicationDate\":\"2014\",\"title\":\"Revealing the hidden functional diversity of an enzyme family.\",\"volume\":\"10\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H1",
  "excerpt": "ID   3OXCE_CUPNH             Reviewed;         284 AA.\nAC   Q0KAA1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 87.\nDE   RecName: Full=3-oxoadipate:acetyl-CoA acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.318 {ECO:0000269|PubMed:24240508};\nDE   AltName: Full=3-oxoadipate cleavage enzyme {ECO:0000305};\nDE   AltName: Full=BKACE_378 {ECO:0000303|PubMed:24240508};\nGN   OrderedLocusNames=H16_A1969 {ECO:0000312|EMBL:CAJ93070.1};\nGN   ORFNames=E6A55_10065 {ECO:0000312|EMBL:QCC00902.1};\nOS   Cupriavidus necator (strain ATCC 17699 / DSM 428 / KCTC 22496 / NCIMB 10442\nOS   / H16 / Stanier 337) (Ralstonia eutropha).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Burkholderiaceae; Cupriavidus.\nOX   NCBI_TaxID=381666;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=3-oxoadipate:acetyl-CoA acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.318 {ECO:0000269|PubMed:24240508};\nDE   AltName: Full=3-oxoadipate cleavage enzyme {ECO:0000305};\nDE   AltName: Full=BKACE_378 {ECO:0000303|PubMed:24240508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=24240508; DOI=10.1038/nchembio.1387;\nRA   Bastard K., Smith A.A., Vergne-Vaxelaire C., Perret A., Zaparucha A.,\nRA   De Melo-Minardi R., Mariage A., Boutard M., Debard A., Lechaplais C.,\nRA   Pelle C., Pellouin V., Perchat N., Petit J.L., Kreimeyer A., Medigue C.,\nRA   Weissenbach J., Artiguenave F., De Berardinis V., Vallenet D.,\nRA   Salanoubat M.;\nRT   \"Revealing the hidden functional diversity of an enzyme family.\";\nRL   Nat. Chem. Biol. 10:42-49(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:B0VHH0};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
