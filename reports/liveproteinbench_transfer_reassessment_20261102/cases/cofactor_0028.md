# cofactor_0028

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0028.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVKPTKSNIGVYTNPAHDLWVAEAEPSLEQVQTGEKLAPGEVTVAVKSTGICGSDVHFWHAGCIGPMIVEDDHILGHESAGVVVAVHENVKSLKVGDRVAIEPNIICGECEPCLTGRYNGCDSVLFRSTPPVPGLLRRYVNHPAMWCHKIGDMSYENGSLLEPLSVALAGVQRAEVRLGDPILVCGAGPIGLVTLACVKAAGAEPIIITDIDEGRLAFAKEFCPSVRTHKVDFKHTPEDFAKAITELGGGVEPAIALECTGVESSIAGAIQTVKFGGKVFVIGVGKNEIKIPFMRLSTREVDLQFQYRYANTWPRAIRLLQGGVINLEKLVTHRFKIEDALEAFKTAADPKTGAIKVQIQSFEEGESR

[Multiple Choices]
A. Mg(2+)
B. Ca(2+)
C. Zn(2+)
D. Mo-bis(molybdopterin guanine dinucleotide)
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

> The exact sequence matches a UniProt entry annotated with Zn(2+) as its cofactor. The annotation is transferred by similarity from Q7SI09 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a roughly 370-residue NAD-dependent polyol/alcohol dehydrogenase, with conserved histidine/cysteine-rich regions characteristic of zinc-dependent members of this enzyme family. That family-level pattern makes Zn a meaningful choice over Mg, Ca, or a molybdopterin cofactor, even without identifying the exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable dehydrogenase-family knowledge and the sequence’s metal-binding features provide a credible basis for choosing Zn among these alternatives. The exact protein’s annotation is not necessary for that inference, though it offers corroboration.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered choices distinguish zinc-dependent dehydrogenases from the other listed cofactor types; no alternative is comparably supported.


### Important caveats

- The cited cofactor annotation is computationally transferred from a related UniProt entry, not established here as a direct experimental measurement of this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a roughly 370-residue NAD-dependent polyol/alcohol dehydrogenase, with conserved histidine/cysteine-rich regions characteristic of zinc-dependent members of this enzyme family. That family-level pattern makes Zn a meaningful choice over Mg, Ca, or a molybdopterin cofactor, even without identifying the exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable dehydrogenase-family knowledge and the sequence’s metal-binding features provide a credible basis for choosing Zn among these alternatives. The exact protein’s annotation is not necessary for that inference, though it offers corroboration."
  },
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with Zn(2+) as its cofactor. The annotation is transferred by similarity from Q7SI09 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The cited cofactor annotation is computationally transferred from a related UniProt entry, not established here as a direct experimental measurement of this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices distinguish zinc-dependent dehydrogenases from the other listed cofactor types; no alternative is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with Zn(2+) as its cofactor. The annotation is transferred by similarity from Q7SI09 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a roughly 370-residue NAD-dependent polyol/alcohol dehydrogenase, with conserved histidine/cysteine-rich regions characteristic of zinc-dependent members of this enzyme family. That family-level pattern makes Zn a meaningful choice over Mg, Ca, or a molybdopterin cofactor, even without identifying the exact protein.",
    "missing_item_specific_fact": "",
    "reason": "Transferable dehydrogenase-family knowledge and the sequence’s metal-binding features provide a credible basis for choosing Zn among these alternatives. The exact protein’s annotation is not necessary for that inference, though it offers corroboration."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices distinguish zinc-dependent dehydrogenases from the other listed cofactor types; no alternative is comparably supported."
  },
  "important_caveats": [
    "The cited cofactor annotation is computationally transferred from a related UniProt entry, not established here as a direct experimental measurement of this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates Zn(2+) as the cofactor for this L-arabinitol 4-dehydrogenase (EC 1.1.1.12), with evidence code ECO:0000250 (inferred by similarity from Q7SI09). While the annotation is computational rather than directly experimental, it is well-supported by the protein's membership in the medium-chain dehydrogenase/reductase (MDR) family, which universally uses a catalytic Zn(2+) ion coordinated by conserved Cys and His residues. The sequence contains the hallmark zinc-binding motifs 'ICGSDVHFWHAGC' (Cys-X-X-X-X-X-His-X-X-X-Cys) and 'CGAGPIGLVTLAC', consistent with the canonical MDR zinc site. The Zn(2+) assignment is therefore consistent with both the annotation and the visible sequence features.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two highly diagnostic motifs for the medium-chain dehydrogenase/reductase (MDR) family: (1) 'ICGSDVHFWHAGC' with the Cys-X-X-X-X-X-His-X-X-X-Cys pattern, which is the canonical zinc-coordination motif in MDR enzymes (analogous to Cys46/His67/Cys174 in horse liver alcohol dehydrogenase), and (2) 'CGAGPIGLVTLAC', the second Cys-rich zinc-ligand region. Additionally, the Rossmann-fold-like segment 'GGGVEPAIALECTGVESSIAGAIQTVKFGGKVFVIGVGKNEIKIPFMRLSTREV' indicates NAD(P)-dependent dehydrogenase activity. A knowledgeable model can recognize these Cys-His-Cys motifs as the zinc-binding site of the MDR family, which universally requires a catalytic Zn(2+). This directly eliminates Mg(2+) (found in kinases, polymerases, ATPases), Ca(2+) (found in EF-hand proteins, some proteases), and Mo-bis(molybdopterin guanine dinucleotide) (found in molybdoenzymes with entirely different folds and Moco-binding motifs absent here). The inference relies on well-established family-level sequence signatures shared across hundreds of MDR dehydrogenases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The zinc-binding Cys-His-Cys motif in the MDR family is a widely taught, transferable sequence feature. Recognizing 'ICGSDVHFWHAGC' and 'CGAGPIGLVTLAC' as zinc-coordination motifs in a dehydrogenase context is a legitimate family-level inference from other proteins, not a lookup of this specific entry's annotation. The four options are well-separated by family context: none of the distractors (Mg2+, Ca2+, Mo-bis-MGD) are associated with MDR dehydrogenases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Cys-His-Cys zinc-binding motif and the Rossmann-fold NAD-binding region uniquely identify this as an MDR-family dehydrogenase, which uses Zn(2+) as its catalytic cofactor. The other three options correspond to entirely different enzyme classes and structural folds not suggested by any feature in the sequence.


### Important caveats

- The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from Q7SI09), meaning it is a computational transfer rather than a direct experimental measurement on this exact protein.
- The organism identity (Aureobasidium melanogenum) and specific protein name (L-arabinitol 4-dehydrogenase) were not provided to the evaluated model; the reasoning must rely on sequence motifs alone.
- The Mo-bis(molybdopterin guanine dinucleotide) distractor is particularly easy to eliminate because molybdoenzymes have a completely different fold and Moco-binding motifs absent from this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two highly diagnostic motifs for the medium-chain dehydrogenase/reductase (MDR) family: (1) 'ICGSDVHFWHAGC' with the Cys-X-X-X-X-X-His-X-X-X-Cys pattern, which is the canonical zinc-coordination motif in MDR enzymes (analogous to Cys46/His67/Cys174 in horse liver alcohol dehydrogenase), and (2) 'CGAGPIGLVTLAC', the second Cys-rich zinc-ligand region. Additionally, the Rossmann-fold-like segment 'GGGVEPAIALECTGVESSIAGAIQTVKFGGKVFVIGVGKNEIKIPFMRLSTREV' indicates NAD(P)-dependent dehydrogenase activity. A knowledgeable model can recognize these Cys-His-Cys motifs as the zinc-binding site of the MDR family, which universally requires a catalytic Zn(2+). This directly eliminates Mg(2+) (found in kinases, polymerases, ATPases), Ca(2+) (found in EF-hand proteins, some proteases), and Mo-bis(molybdopterin guanine dinucleotide) (found in molybdoenzymes with entirely different folds and Moco-binding motifs absent here). The inference relies on well-established family-level sequence signatures shared across hundreds of MDR dehydrogenases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The zinc-binding Cys-His-Cys motif in the MDR family is a widely taught, transferable sequence feature. Recognizing 'ICGSDVHFWHAGC' and 'CGAGPIGLVTLAC' as zinc-coordination motifs in a dehydrogenase context is a legitimate family-level inference from other proteins, not a lookup of this specific entry's annotation. The four options are well-separated by family context: none of the distractors (Mg2+, Ca2+, Mo-bis-MGD) are associated with MDR dehydrogenases."
  },
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates Zn(2+) as the cofactor for this L-arabinitol 4-dehydrogenase (EC 1.1.1.12), with evidence code ECO:0000250 (inferred by similarity from Q7SI09). While the annotation is computational rather than directly experimental, it is well-supported by the protein's membership in the medium-chain dehydrogenase/reductase (MDR) family, which universally uses a catalytic Zn(2+) ion coordinated by conserved Cys and His residues. The sequence contains the hallmark zinc-binding motifs 'ICGSDVHFWHAGC' (Cys-X-X-X-X-X-His-X-X-X-Cys) and 'CGAGPIGLVTLAC', consistent with the canonical MDR zinc site. The Zn(2+) assignment is therefore consistent with both the annotation and the visible sequence features."
  },
  "important_caveats": [
    "The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from Q7SI09), meaning it is a computational transfer rather than a direct experimental measurement on this exact protein.",
    "The organism identity (Aureobasidium melanogenum) and specific protein name (L-arabinitol 4-dehydrogenase) were not provided to the evaluated model; the reasoning must rely on sequence motifs alone.",
    "The Mo-bis(molybdopterin guanine dinucleotide) distractor is particularly easy to eliminate because molybdoenzymes have a completely different fold and Moco-binding motifs absent from this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Cys-His-Cys zinc-binding motif and the Rossmann-fold NAD-binding region uniquely identify this as an MDR-family dehydrogenase, which uses Zn(2+) as its catalytic cofactor. The other three options correspond to entirely different enzyme classes and structural folds not suggested by any feature in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates Zn(2+) as the cofactor for this L-arabinitol 4-dehydrogenase (EC 1.1.1.12), with evidence code ECO:0000250 (inferred by similarity from Q7SI09). While the annotation is computational rather than directly experimental, it is well-supported by the protein's membership in the medium-chain dehydrogenase/reductase (MDR) family, which universally uses a catalytic Zn(2+) ion coordinated by conserved Cys and His residues. The sequence contains the hallmark zinc-binding motifs 'ICGSDVHFWHAGC' (Cys-X-X-X-X-X-His-X-X-X-Cys) and 'CGAGPIGLVTLAC', consistent with the canonical MDR zinc site. The Zn(2+) assignment is therefore consistent with both the annotation and the visible sequence features.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two highly diagnostic motifs for the medium-chain dehydrogenase/reductase (MDR) family: (1) 'ICGSDVHFWHAGC' with the Cys-X-X-X-X-X-His-X-X-X-Cys pattern, which is the canonical zinc-coordination motif in MDR enzymes (analogous to Cys46/His67/Cys174 in horse liver alcohol dehydrogenase), and (2) 'CGAGPIGLVTLAC', the second Cys-rich zinc-ligand region. Additionally, the Rossmann-fold-like segment 'GGGVEPAIALECTGVESSIAGAIQTVKFGGKVFVIGVGKNEIKIPFMRLSTREV' indicates NAD(P)-dependent dehydrogenase activity. A knowledgeable model can recognize these Cys-His-Cys motifs as the zinc-binding site of the MDR family, which universally requires a catalytic Zn(2+). This directly eliminates Mg(2+) (found in kinases, polymerases, ATPases), Ca(2+) (found in EF-hand proteins, some proteases), and Mo-bis(molybdopterin guanine dinucleotide) (found in molybdoenzymes with entirely different folds and Moco-binding motifs absent here). The inference relies on well-established family-level sequence signatures shared across hundreds of MDR dehydrogenases.",
    "missing_item_specific_fact": "",
    "reason": "The zinc-binding Cys-His-Cys motif in the MDR family is a widely taught, transferable sequence feature. Recognizing 'ICGSDVHFWHAGC' and 'CGAGPIGLVTLAC' as zinc-coordination motifs in a dehydrogenase context is a legitimate family-level inference from other proteins, not a lookup of this specific entry's annotation. The four options are well-separated by family context: none of the distractors (Mg2+, Ca2+, Mo-bis-MGD) are associated with MDR dehydrogenases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Cys-His-Cys zinc-binding motif and the Rossmann-fold NAD-binding region uniquely identify this as an MDR-family dehydrogenase, which uses Zn(2+) as its catalytic cofactor. The other three options correspond to entirely different enzyme classes and structural folds not suggested by any feature in the sequence."
  },
  "important_caveats": [
    "The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (inferred by similarity from Q7SI09), meaning it is a computational transfer rather than a direct experimental measurement on this exact protein.",
    "The organism identity (Aureobasidium melanogenum) and specific protein name (L-arabinitol 4-dehydrogenase) were not provided to the evaluated model; the reasoning must rely on sequence motifs alone.",
    "The Mo-bis(molybdopterin guanine dinucleotide) distractor is particularly easy to eliminate because molybdoenzymes have a completely different fold and Moco-binding motifs absent from this sequence."
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
  "benchmark_sequence_length": 368,
  "benchmark_sequence_sha256": "b6243c25f76bd5341c3276e5e72351d95b636da19da05dae2fa407490c6e3c1c",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-12-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 368,
  "current_source_sequence_sha256": "b6243c25f76bd5341c3276e5e72351d95b636da19da05dae2fa407490c6e3c1c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 21,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A385XI11",
  "selected_historical_entry_version": 21,
  "selected_historical_record_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "selected_historical_source_sequence_length": 368,
  "selected_historical_source_sequence_sha256": "b6243c25f76bd5341c3276e5e72351d95b636da19da05dae2fa407490c6e3c1c",
  "selected_historical_version": {
    "accession": "A0A385XI11",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "LAD_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A385XI11\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-12-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7SI09\",\"source\":\"UniProtKB\"}],\"value\":\"1.1.1.12\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"L-arabinitol 4-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"ArDH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7SI09\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H1",
  "excerpt": "ID   LAD_AURME               Reviewed;         368 AA.\nAC   A0A385XI11;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-DEC-2018, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=L-arabinitol 4-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=ArDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.12 {ECO:0000250|UniProtKB:Q7SI09};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=L-arabinitol 4-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=ArDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.12 {ECO:0000250|UniProtKB:Q7SI09};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:Q7SI09};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
