# cofactor_0181

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0181.txt)

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
MEVNQKWNWDTKPILVKCGGFSSQLAKNVTEKVDGDPLWGSRFDATNPEAVIQTHLDFLRNGADIILTNTYQSSVEGFVKYLGVTRERGVELIQKSVQLAKQAKEQYLSEIGSEAESALPLIMGSIGPYGAYLHDGSEYTGNYADKMSKEELRAWHKTRIEICLAAGVDGLALETLPCLMEAEAVTELVLDNFPDAKFWVSLQCMDEKHMASGENFAEAALSLWRLVQSRKAENRLLGIGLNCVNPLFVTPLLSSLTKVAGSDRIPLVVYSNRGEIYDVEQGDWTGTGEEVVKFVPEWIQLGVRIVGGCCRVYPTDVLAIRKYVDGLNIKP

[Multiple Choices]
A. cob(II)alamin
B. Zn(2+)
C. NAD(+)
D. Ca(2+)
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

> The exact sequence matches the archived UniProt entry for betaine-homocysteine S-methyltransferase, whose cofactor is annotated as Zn(2+). The annotation is based on a PROSITE rule, so it supports the key but is computational rather than direct experimental evidence.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the betaine-homocysteine S-methyltransferase family, a zinc-dependent enzyme family. Transferable family knowledge, including conserved metal-binding features, meaningfully favors Zn(2+) over cob(II)alamin, NAD(+), or Ca(2+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the supplied sequence can distinguish the zinc option without knowing this exact protein's database record. This is a credible inference, though sequence-based family recognition does not itself establish experimental cofactor occupancy.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, Zn(2+) is the family-consistent cofactor; no other option is comparably supported.


### Important caveats

- The source annotation is attributed to a PROSITE rule, not direct experimental evidence.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the betaine-homocysteine S-methyltransferase family, a zinc-dependent enzyme family. Transferable family knowledge, including conserved metal-binding features, meaningfully favors Zn(2+) over cob(II)alamin, NAD(+), or Ca(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the supplied sequence can distinguish the zinc option without knowing this exact protein's database record. This is a credible inference, though sequence-based family recognition does not itself establish experimental cofactor occupancy."
  },
  "case_id": "cofactor_0181",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the archived UniProt entry for betaine-homocysteine S-methyltransferase, whose cofactor is annotated as Zn(2+). The annotation is based on a PROSITE rule, so it supports the key but is computational rather than direct experimental evidence."
  },
  "important_caveats": [
    "The source annotation is attributed to a PROSITE rule, not direct experimental evidence.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, Zn(2+) is the family-consistent cofactor; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0181",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the archived UniProt entry for betaine-homocysteine S-methyltransferase, whose cofactor is annotated as Zn(2+). The annotation is based on a PROSITE rule, so it supports the key but is computational rather than direct experimental evidence.",
    "evidence_ids": ["H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the betaine-homocysteine S-methyltransferase family, a zinc-dependent enzyme family. Transferable family knowledge, including conserved metal-binding features, meaningfully favors Zn(2+) over cob(II)alamin, NAD(+), or Ca(2+).",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the supplied sequence can distinguish the zinc option without knowing this exact protein's database record. This is a credible inference, though sequence-based family recognition does not itself establish experimental cofactor occupancy."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, Zn(2+) is the family-consistent cofactor; no other option is comparably supported."
  },
  "important_caveats": [
    "The source annotation is attributed to a PROSITE rule, not direct experimental evidence.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates Zn(2+) as the cofactor with evidence code ECO:0000255 (PROSITE-ProRule:PRU00333, the BHMT zinc-binding domain pattern). The EC number 2.1.1.5 (Betaine-homocysteine S-methyltransferase) is transferred by similarity to human BHMT (Q93088, ECO:0000250). BHMT is a well-characterized zinc metalloenzyme across multiple species (human, rat), confirmed by crystallographic structures showing zinc coordinated by conserved Cys/His residues. The annotation is computational/proteome-wide rather than experimentally derived for this exact Drosophila protein, but it is consistent with the established biochemistry of the BHMT family.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~331 aa) contains BHMT-family hallmarks: a Cys-rich N-terminal region ('VKCGGFSSQLA'), a conserved His in 'LHDGSEYTGNYADK', and a C-terminal 'CCRVY' motif — these match the PROSITE BHMT zinc-binding domain (PRU00333) pattern of conserved Cys/His residues that coordinate Zn(2+). From other BHMT homologs (human Q93088, rat, yeast), the family-level fact that BHMT is a zinc metalloenzyme is well established (crystallographically confirmed in human BHMT). For the distractors: BHMT is a methyltransferase (EC 2.1.1.5), not a dehydrogenase (rules out NAD+), not a B12-dependent enzyme like methionine synthase (rules out cob(II)alamin), and Ca(2+) is not a cofactor for any known methyltransferase in this class. Recognizing the BHMT fold and its zinc dependence from family knowledge meaningfully distinguishes B from A, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can identify BHMT-family sequence features (conserved Cys/His motifs, overall length, domain architecture) and apply the well-established family-level fact that BHMT enzymes are zinc metalloenzymes, as demonstrated in human and rat structures. The enzyme class (methyltransferase) independently eliminates NAD+, cob(II)alamin, and Ca(2+). This is a legitimate transfer from other proteins in the same family.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four cofactor options are mechanistically distinct (metal ion vs. nucleotide vs. vitamin-derived corrinoid). Once the enzyme is identified as a BHMT-family methyltransferase, only Zn(2+) is consistent with the known catalytic mechanism. The remaining three options correspond to entirely different enzyme classes and are not defensible alternatives.


### Important caveats

- The Zn(2+) annotation for this Drosophila BHMT is based on PROSITE pattern matching (ECO:0000255) and EC transfer from human BHMT (ECO:0000250), not direct experimental measurement on the Drosophila protein.
- The sequence was matched to UniProt Q9VJ31 (BHMT_DROME) by the reviewer; the evaluated model received only the raw sequence without accession or organism name.
- BHMT zinc dependence is well-supported across the family, but the specific zinc-binding residue positions in the Drosophila protein were not independently validated experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~331 aa) contains BHMT-family hallmarks: a Cys-rich N-terminal region ('VKCGGFSSQLA'), a conserved His in 'LHDGSEYTGNYADK', and a C-terminal 'CCRVY' motif — these match the PROSITE BHMT zinc-binding domain (PRU00333) pattern of conserved Cys/His residues that coordinate Zn(2+). From other BHMT homologs (human Q93088, rat, yeast), the family-level fact that BHMT is a zinc metalloenzyme is well established (crystallographically confirmed in human BHMT). For the distractors: BHMT is a methyltransferase (EC 2.1.1.5), not a dehydrogenase (rules out NAD+), not a B12-dependent enzyme like methionine synthase (rules out cob(II)alamin), and Ca(2+) is not a cofactor for any known methyltransferase in this class. Recognizing the BHMT fold and its zinc dependence from family knowledge meaningfully distinguishes B from A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can identify BHMT-family sequence features (conserved Cys/His motifs, overall length, domain architecture) and apply the well-established family-level fact that BHMT enzymes are zinc metalloenzymes, as demonstrated in human and rat structures. The enzyme class (methyltransferase) independently eliminates NAD+, cob(II)alamin, and Ca(2+). This is a legitimate transfer from other proteins in the same family."
  },
  "case_id": "cofactor_0181",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates Zn(2+) as the cofactor with evidence code ECO:0000255 (PROSITE-ProRule:PRU00333, the BHMT zinc-binding domain pattern). The EC number 2.1.1.5 (Betaine-homocysteine S-methyltransferase) is transferred by similarity to human BHMT (Q93088, ECO:0000250). BHMT is a well-characterized zinc metalloenzyme across multiple species (human, rat), confirmed by crystallographic structures showing zinc coordinated by conserved Cys/His residues. The annotation is computational/proteome-wide rather than experimentally derived for this exact Drosophila protein, but it is consistent with the established biochemistry of the BHMT family."
  },
  "important_caveats": [
    "The Zn(2+) annotation for this Drosophila BHMT is based on PROSITE pattern matching (ECO:0000255) and EC transfer from human BHMT (ECO:0000250), not direct experimental measurement on the Drosophila protein.",
    "The sequence was matched to UniProt Q9VJ31 (BHMT_DROME) by the reviewer; the evaluated model received only the raw sequence without accession or organism name.",
    "BHMT zinc dependence is well-supported across the family, but the specific zinc-binding residue positions in the Drosophila protein were not independently validated experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor options are mechanistically distinct (metal ion vs. nucleotide vs. vitamin-derived corrinoid). Once the enzyme is identified as a BHMT-family methyltransferase, only Zn(2+) is consistent with the known catalytic mechanism. The remaining three options correspond to entirely different enzyme classes and are not defensible alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0181",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates Zn(2+) as the cofactor with evidence code ECO:0000255 (PROSITE-ProRule:PRU00333, the BHMT zinc-binding domain pattern). The EC number 2.1.1.5 (Betaine-homocysteine S-methyltransferase) is transferred by similarity to human BHMT (Q93088, ECO:0000250). BHMT is a well-characterized zinc metalloenzyme across multiple species (human, rat), confirmed by crystallographic structures showing zinc coordinated by conserved Cys/His residues. The annotation is computational/proteome-wide rather than experimentally derived for this exact Drosophila protein, but it is consistent with the established biochemistry of the BHMT family.",
    "evidence_ids": ["C5", "H3", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~331 aa) contains BHMT-family hallmarks: a Cys-rich N-terminal region ('VKCGGFSSQLA'), a conserved His in 'LHDGSEYTGNYADK', and a C-terminal 'CCRVY' motif — these match the PROSITE BHMT zinc-binding domain (PRU00333) pattern of conserved Cys/His residues that coordinate Zn(2+). From other BHMT homologs (human Q93088, rat, yeast), the family-level fact that BHMT is a zinc metalloenzyme is well established (crystallographically confirmed in human BHMT). For the distractors: BHMT is a methyltransferase (EC 2.1.1.5), not a dehydrogenase (rules out NAD+), not a B12-dependent enzyme like methionine synthase (rules out cob(II)alamin), and Ca(2+) is not a cofactor for any known methyltransferase in this class. Recognizing the BHMT fold and its zinc dependence from family knowledge meaningfully distinguishes B from A, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "A model can identify BHMT-family sequence features (conserved Cys/His motifs, overall length, domain architecture) and apply the well-established family-level fact that BHMT enzymes are zinc metalloenzymes, as demonstrated in human and rat structures. The enzyme class (methyltransferase) independently eliminates NAD+, cob(II)alamin, and Ca(2+). This is a legitimate transfer from other proteins in the same family."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor options are mechanistically distinct (metal ion vs. nucleotide vs. vitamin-derived corrinoid). Once the enzyme is identified as a BHMT-family methyltransferase, only Zn(2+) is consistent with the known catalytic mechanism. The remaining three options correspond to entirely different enzyme classes and are not defensible alternatives."
  },
  "important_caveats": [
    "The Zn(2+) annotation for this Drosophila BHMT is based on PROSITE pattern matching (ECO:0000255) and EC transfer from human BHMT (ECO:0000250), not direct experimental measurement on the Drosophila protein.",
    "The sequence was matched to UniProt Q9VJ31 (BHMT_DROME) by the reviewer; the evaluated model received only the raw sequence without accession or organism name.",
    "BHMT zinc dependence is well-supported across the family, but the specific zinc-binding residue positions in the Drosophila protein were not independently validated experimentally."
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
  "benchmark_sequence_length": 331,
  "benchmark_sequence_sha256": "6bd107edc9e34f66f2c22eae9672febecece9154557d102db3fa92c074ab48db",
  "current_entry_audit": {
    "entryVersion": 181,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 331,
  "current_source_sequence_sha256": "6bd107edc9e34f66f2c22eae9672febecece9154557d102db3fa92c074ab48db",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 179,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VJ31",
  "selected_historical_entry_version": 179,
  "selected_historical_record_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "selected_historical_source_sequence_length": 331,
  "selected_historical_source_sequence_sha256": "6bd107edc9e34f66f2c22eae9672febecece9154557d102db3fa92c074ab48db",
  "selected_historical_version": {
    "accession": "Q9VJ31",
    "database": "Swiss-Prot",
    "entryVersion": 179,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BHMT_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VJ31\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":181,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q93088\",\"source\":\"UniProtKB\"}],\"value\":\"2.1.1.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0032727\",\"source\":\"FlyBase\"}],\"value\":\"Betaine-homocysteine S-methyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00333\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)

```json
{
  "entry_version": 179,
  "evidence_id": "H1",
  "excerpt": "ID   BHMT_DROME              Reviewed;         331 AA.\nAC   Q9VJ31;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 179.\nDE   RecName: Full=Betaine-homocysteine S-methyltransferase {ECO:0000312|FlyBase:FBgn0032727};\nDE            EC=2.1.1.5 {ECO:0000250|UniProtKB:Q93088};\nGN   Name=Bhmt {ECO:0000312|FlyBase:FBgn0032727};\nGN   ORFNames=CG10623 {ECO:0000312|FlyBase:FBgn0032727};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.773902+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "url": "https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)

```json
{
  "entry_version": 179,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Betaine-homocysteine S-methyltransferase {ECO:0000312|FlyBase:FBgn0032727};\nDE            EC=2.1.1.5 {ECO:0000250|UniProtKB:Q93088};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.773902+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "url": "https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)

```json
{
  "entry_version": 179,
  "evidence_id": "H3",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00333};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.773902+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "url": "https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 181. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
