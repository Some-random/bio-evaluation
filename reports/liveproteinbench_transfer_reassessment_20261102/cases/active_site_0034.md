# active_site_0034

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0034.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 143 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNPPPSLLDKAAIVTGGSRGIGAAIAIELARRGAHVLITYNTASHKAQLVAEEIQKLGRKATVVQASSTDREGPNRIVQAAVSQYGRIDIIVNNAGMADDCLLQDLTHEFWDRIMDVNLRLPAFLVQAALQHLGPAPRIVNISSLAARAGYNATSVYAASKAALEGMTRAWATELGHRYNVTVNCVNPGPVDTDIMAVDENTDAEVVAYWNAKVKETPAAPRVGTPGDIAQIVAFLCEEGSRWCTGSVVNANGGLVTV

[Multiple Choices]
A. Position 357 (For beta-ketoacyl synthase activity)
B. Position 1008 (Proton acceptor; for dehydratase activity 1)
C. Position 143 (Proton donor)
D. Position 27 (Proton acceptor)
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

> The sequence-matched UniProt annotation identifies position 143 as a proton donor. This is a similarity-based annotation, not direct experimental verification in the supplied evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 258-residue sequence has an N-terminal TGxxGxG-like motif characteristic of the cofactor-binding region of short-chain dehydrogenase/reductases, and contains Ser at position 143 alongside a TyrxxxLys motif consistent with the conserved SDR catalytic machinery. Position 27 is Ile, while positions 357 and 1008 are outside the sequence. Transferable SDR family knowledge therefore gives a meaningful basis for choosing C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features distinguish the offered option without needing to recall this exact protein's database record. The inference is credible, though it does not independently prove the precise catalytic role experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, only C gives an in-range position with a plausible catalytic residue and role.


### Important caveats

- The supporting annotation is inferred by similarity to another protein rather than shown here to be experimentally measured for this sequence.
- A separate annotation also assigns proton-donor activity to position 144, but that position is not an offered choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 258-residue sequence has an N-terminal TGxxGxG-like motif characteristic of the cofactor-binding region of short-chain dehydrogenase/reductases, and contains Ser at position 143 alongside a TyrxxxLys motif consistent with the conserved SDR catalytic machinery. Position 27 is Ile, while positions 357 and 1008 are outside the sequence. Transferable SDR family knowledge therefore gives a meaningful basis for choosing C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features distinguish the offered option without needing to recall this exact protein's database record. The inference is credible, though it does not independently prove the precise catalytic role experimentally."
  },
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 143 as a proton donor. This is a similarity-based annotation, not direct experimental verification in the supplied evidence."
  },
  "important_caveats": [
    "The supporting annotation is inferred by similarity to another protein rather than shown here to be experimentally measured for this sequence.",
    "A separate annotation also assigns proton-donor activity to position 144, but that position is not an offered choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only C gives an in-range position with a plausible catalytic residue and role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 143 as a proton donor. This is a similarity-based annotation, not direct experimental verification in the supplied evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 258-residue sequence has an N-terminal TGxxGxG-like motif characteristic of the cofactor-binding region of short-chain dehydrogenase/reductases, and contains Ser at position 143 alongside a TyrxxxLys motif consistent with the conserved SDR catalytic machinery. Position 27 is Ile, while positions 357 and 1008 are outside the sequence. Transferable SDR family knowledge therefore gives a meaningful basis for choosing C.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features distinguish the offered option without needing to recall this exact protein's database record. The inference is credible, though it does not independently prove the precise catalytic role experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only C gives an in-range position with a plausible catalytic residue and role."
  },
  "important_caveats": [
    "The supporting annotation is inferred by similarity to another protein rather than shown here to be experimentally measured for this sequence.",
    "A separate annotation also assigns proton-donor activity to position 144, but that position is not an offered choice."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (evidence C5/H3) explicitly lists Position 143 as 'Proton donor' active site. The evidence code ECO:0000250 indicates this is inferred by similarity to O93868 (another SDR), not direct experimental evidence for this exact protein. However, the annotation is consistent with the well-established SDR catalytic tetrad (S-S-Y-K) and the sequence context (Ser at 143, Ser at 144, Tyr at 157, Lys at 161). The answer is supported by the database annotation, albeit as a computational/similarity-based assignment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [C7](#evidence-c7), [H5](#evidence-h5), [C8](#evidence-c8), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A (position 357) and B (position 1008) are immediately eliminated because the protein is only 258 residues long—these positions do not exist. Between C (position 143, Proton donor) and D (position 27, Proton acceptor): Position 27 in the sequence is Isoleucine (I), which has no ionizable side chain and cannot function as a proton acceptor in enzyme catalysis. Position 143 is Serine (S), a canonical catalytic residue. Furthermore, the N-terminal region contains the SDR-family Rossmann-fold motif TGxxxGG (TGSRGIG at positions 16-22), identifying this as a short-chain dehydrogenase/reductase. SDR enzymes universally employ a catalytic tetrad (Ser-Tyr-Lys) located in the C-terminal half of the protein. The Ser at 143, Tyr at 157, and Lys at 161 match this conserved SDR catalytic architecture. A model recognizing the SDR family from the TGxxxGG motif and knowing the conserved catalytic tetrad positions would confidently select C over D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of A and B relies on protein length (trivially derivable from the input). The elimination of D relies on recognizing that Isoleucine cannot be a proton acceptor—a basic biochemistry fact. The positive identification of C relies on recognizing the SDR family signature (TGxxxGG Rossmann motif) and the conserved S-Y-K catalytic tetrad, which are well-known transferable features across the SDR superfamily. No target-specific memorization is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are impossible (positions exceed protein length). Option D is biochemically nonsensical (Isoleucine cannot be a proton acceptor). Only C is consistent with both the sequence and SDR family catalytic architecture.


### Important caveats

- The UniProt annotation for position 143 carries evidence code ECO:0000250 (inferred by similarity to O93868), not direct experimental evidence for this specific protein. The annotation is a computational transfer within the SDR family.
- Options A and B appear to be distractors drawn from an entirely different protein (possibly a fatty acid synthase or dehydratase with >1000 residues), making them trivially eliminable.
- The SDR catalytic tetrad assignment (S143/S144-Y157-K161) is a family-level inference; individual SDR members may show variation in which Ser of the pair acts as the primary proton donor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A (position 357) and B (position 1008) are immediately eliminated because the protein is only 258 residues long—these positions do not exist. Between C (position 143, Proton donor) and D (position 27, Proton acceptor): Position 27 in the sequence is Isoleucine (I), which has no ionizable side chain and cannot function as a proton acceptor in enzyme catalysis. Position 143 is Serine (S), a canonical catalytic residue. Furthermore, the N-terminal region contains the SDR-family Rossmann-fold motif TGxxxGG (TGSRGIG at positions 16-22), identifying this as a short-chain dehydrogenase/reductase. SDR enzymes universally employ a catalytic tetrad (Ser-Tyr-Lys) located in the C-terminal half of the protein. The Ser at 143, Tyr at 157, and Lys at 161 match this conserved SDR catalytic architecture. A model recognizing the SDR family from the TGxxxGG motif and knowing the conserved catalytic tetrad positions would confidently select C over D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A and B relies on protein length (trivially derivable from the input). The elimination of D relies on recognizing that Isoleucine cannot be a proton acceptor—a basic biochemistry fact. The positive identification of C relies on recognizing the SDR family signature (TGxxxGG Rossmann motif) and the conserved S-Y-K catalytic tetrad, which are well-known transferable features across the SDR superfamily. No target-specific memorization is needed."
  },
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4",
      "C7",
      "H5",
      "C8",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5/H3) explicitly lists Position 143 as 'Proton donor' active site. The evidence code ECO:0000250 indicates this is inferred by similarity to O93868 (another SDR), not direct experimental evidence for this exact protein. However, the annotation is consistent with the well-established SDR catalytic tetrad (S-S-Y-K) and the sequence context (Ser at 143, Ser at 144, Tyr at 157, Lys at 161). The answer is supported by the database annotation, albeit as a computational/similarity-based assignment."
  },
  "important_caveats": [
    "The UniProt annotation for position 143 carries evidence code ECO:0000250 (inferred by similarity to O93868), not direct experimental evidence for this specific protein. The annotation is a computational transfer within the SDR family.",
    "Options A and B appear to be distractors drawn from an entirely different protein (possibly a fatty acid synthase or dehydratase with >1000 residues), making them trivially eliminable.",
    "The SDR catalytic tetrad assignment (S143/S144-Y157-K161) is a family-level inference; individual SDR members may show variation in which Ser of the pair acts as the primary proton donor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are impossible (positions exceed protein length). Option D is biochemically nonsensical (Isoleucine cannot be a proton acceptor). Only C is consistent with both the sequence and SDR family catalytic architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5/H3) explicitly lists Position 143 as 'Proton donor' active site. The evidence code ECO:0000250 indicates this is inferred by similarity to O93868 (another SDR), not direct experimental evidence for this exact protein. However, the annotation is consistent with the well-established SDR catalytic tetrad (S-S-Y-K) and the sequence context (Ser at 143, Ser at 144, Tyr at 157, Lys at 161). The answer is supported by the database annotation, albeit as a computational/similarity-based assignment.",
    "evidence_ids": ["C5", "H3", "C6", "H4", "C7", "H5", "C8", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A (position 357) and B (position 1008) are immediately eliminated because the protein is only 258 residues long—these positions do not exist. Between C (position 143, Proton donor) and D (position 27, Proton acceptor): Position 27 in the sequence is Isoleucine (I), which has no ionizable side chain and cannot function as a proton acceptor in enzyme catalysis. Position 143 is Serine (S), a canonical catalytic residue. Furthermore, the N-terminal region contains the SDR-family Rossmann-fold motif TGxxxGG (TGSRGIG at positions 16-22), identifying this as a short-chain dehydrogenase/reductase. SDR enzymes universally employ a catalytic tetrad (Ser-Tyr-Lys) located in the C-terminal half of the protein. The Ser at 143, Tyr at 157, and Lys at 161 match this conserved SDR catalytic architecture. A model recognizing the SDR family from the TGxxxGG motif and knowing the conserved catalytic tetrad positions would confidently select C over D.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A and B relies on protein length (trivially derivable from the input). The elimination of D relies on recognizing that Isoleucine cannot be a proton acceptor—a basic biochemistry fact. The positive identification of C relies on recognizing the SDR family signature (TGxxxGG Rossmann motif) and the conserved S-Y-K catalytic tetrad, which are well-known transferable features across the SDR superfamily. No target-specific memorization is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are impossible (positions exceed protein length). Option D is biochemically nonsensical (Isoleucine cannot be a proton acceptor). Only C is consistent with both the sequence and SDR family catalytic architecture."
  },
  "important_caveats": [
    "The UniProt annotation for position 143 carries evidence code ECO:0000250 (inferred by similarity to O93868), not direct experimental evidence for this specific protein. The annotation is a computational transfer within the SDR family.",
    "Options A and B appear to be distractors drawn from an entirely different protein (possibly a fatty acid synthase or dehydratase with >1000 residues), making them trivially eliminable.",
    "The SDR catalytic tetrad assignment (S143/S144-Y157-K161) is a family-level inference; individual SDR members may show variation in which Ser of the pair acts as the primary proton donor."
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
  "benchmark_sequence_length": 258,
  "benchmark_sequence_sha256": "900848c2f83044ac5f5a81d57e8b7d27cd6bc66d8b0cdb266bed700cbb1522de",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 258,
  "current_source_sequence_sha256": "900848c2f83044ac5f5a81d57e8b7d27cd6bc66d8b0cdb266bed700cbb1522de",
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
  "requested_accession": "A0A7T8F1N2",
  "selected_historical_entry_version": 16,
  "selected_historical_record_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "selected_historical_source_sequence_length": 258,
  "selected_historical_source_sequence_sha256": "900848c2f83044ac5f5a81d57e8b7d27cd6bc66d8b0cdb266bed700cbb1522de",
  "selected_historical_version": {
    "accession": "A0A7T8F1N2",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZI_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1N2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis clusters protein I\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Short-chain dehydrogenase/reductase FrzI\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":143},\"start\":{\"modifier\":\"EXACT\",\"value\":143}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":144},\"start\":{\"modifier\":\"EXACT\",\"value\":144}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10001\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":157},\"start\":{\"modifier\":\"EXACT\",\"value\":157}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Lowers pKa of active site Tyr\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":161},\"start\":{\"modifier\":\"EXACT\",\"value\":161}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":21},\"start\":{\"modifier\":\"EXACT\",\"value\":21}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":41},\"start\":{\"modifier\":\"EXACT\",\"value\":41}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":94},\"start\":{\"modifier\":\"EXACT\",\"value\":94}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":157},\"start\":{\"modifier\":\"EXACT\",\"value\":157}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":161},\"start\":{\"modifier\":\"EXACT\",\"value\":161}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":191},\"start\":{\"modifier\":\"EXACT\",\"value\":191}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":193}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H1",
  "excerpt": "ID   FRZI_CLASX              Reviewed;         258 AA.\nAC   A0A7T8F1N2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=Short-chain dehydrogenase/reductase FrzI {ECO:0000303|PubMed:33372776};\nDE            EC=1.1.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis clusters protein I {ECO:0000303|PubMed:33372776};\nGN   Name=FrzI {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        143\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        144\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        157\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU10001\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H6",
  "excerpt": "FT   ACT_SITE        161\nFT                   /note=\"Lowers pKa of active site Tyr\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         21\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         41\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         94\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         157\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         161\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         191\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         193\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
