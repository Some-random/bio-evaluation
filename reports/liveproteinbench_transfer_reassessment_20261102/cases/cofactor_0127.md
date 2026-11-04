# cofactor_0127

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0127.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — heme

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGASTFSQSFAEGYAAWALMLPALVGCALLIYRAFFAIRYPANLPLAGEPDGKRTFSWRTRWRYYIDCEALYKETYDNYTKHGKTVLLPGLGFRHDIVLPQSAMRDIMARPEKELSHADAVLELVQLKYSLGHEKYKADPWPCMLVKSDINSKLEAVCDGMNEELKYAFDKYVGCDTESWKEVDLLETIRMIIMAAASRFTVGFPLCRSEAYLRACWKVNDGIMMNGGLTGATPRLLRPIVGPLVTMKLRQSIEQVKKHVEPIYRQRVQALSQQNSAEKPASDETQDLFQQMLRYAQRERPGELHDLPSMCRRLCFANFAAVHQTTLLVTNMVLNIVSSDPQHNTISVLRDEVKDVIGPDSNAKWTKYKVAQMIKSDSVARETMRLYSNTNRGVFRKVLVEGIKTEDGIELPKGAYVSFLGRPLQCDPETFEDPFEYNPFRFSRIREQAPRDTKGRSSASHLSFVSTSPEHLPFGHGGHSCPGRFLVDFEVKMIVAYLLMNYDVEFPAEYKGQRPANRWMAEALMPPSGARIRIKRRS

[Multiple Choices]
A. Mn(2+)
B. cob(II)alamin
C. heme b
D. heme
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

> The sequence is consistent with a cytochrome P450, whose catalytic cofactor is heme. The matched UniProt record annotates heme, but its evidence is transferred by similarity rather than direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable P450 heme-binding cysteine motif (approximately F-G-H-G-G-H-S-C-P-G), supporting a heme-dependent P450 and distinguishing the heme choices from Mn(2+) and cob(II)alamin.


**Missing item-specific fact**

> To select the keyed generic term over the also-applicable, more specific heme b option, one needs the benchmark's exact cofactor-label convention or this protein's annotation wording.


**Reason**

> Transferable P450 knowledge supports heme, but does not uniquely distinguish C from D: heme b is a form of heme, and both options fit the inferred cofactor. The target record's generic heme annotation matches the key, but that target-specific wording was not in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Heme b is a specific form of heme, so both the specific option and the broader heme option are defensible for a P450.


### Important caveats

- The source cofactor annotation is similarity-transferred, not direct experimental evidence for the supplied protein.
- The sequence matches the cited record, but that record and its annotation were reviewer-only evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable P450 heme-binding cysteine motif (approximately F-G-H-G-G-H-S-C-P-G), supporting a heme-dependent P450 and distinguishing the heme choices from Mn(2+) and cob(II)alamin.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "To select the keyed generic term over the also-applicable, more specific heme b option, one needs the benchmark's exact cofactor-label convention or this protein's annotation wording.",
    "reason": "Transferable P450 knowledge supports heme, but does not uniquely distinguish C from D: heme b is a form of heme, and both options fit the inferred cofactor. The target record's generic heme annotation matches the key, but that target-specific wording was not in the original input."
  },
  "case_id": "cofactor_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence is consistent with a cytochrome P450, whose catalytic cofactor is heme. The matched UniProt record annotates heme, but its evidence is transferred by similarity rather than direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The source cofactor annotation is similarity-transferred, not direct experimental evidence for the supplied protein.",
    "The sequence matches the cited record, but that record and its annotation were reviewer-only evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Heme b is a specific form of heme, so both the specific option and the broader heme option are defensible for a P450."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence is consistent with a cytochrome P450, whose catalytic cofactor is heme. The matched UniProt record annotates heme, but its evidence is transferred by similarity rather than direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable P450 heme-binding cysteine motif (approximately F-G-H-G-G-H-S-C-P-G), supporting a heme-dependent P450 and distinguishing the heme choices from Mn(2+) and cob(II)alamin.",
    "missing_item_specific_fact": "To select the keyed generic term over the also-applicable, more specific heme b option, one needs the benchmark's exact cofactor-label convention or this protein's annotation wording.",
    "reason": "Transferable P450 knowledge supports heme, but does not uniquely distinguish C from D: heme b is a form of heme, and both options fit the inferred cofactor. The target record's generic heme annotation matches the key, but that target-specific wording was not in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Heme b is a specific form of heme, so both the specific option and the broader heme option are defensible for a P450."
  },
  "important_caveats": [
    "The source cofactor annotation is similarity-transferred, not direct experimental evidence for the supplied protein.",
    "The sequence matches the cited record, but that record and its annotation were reviewer-only evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly lists the cofactor as 'heme' with cross-reference ChEBI:CHEBI:30413, which is the general 'heme' term (not the more specific 'heme b'). The evidence code is ECO:0000250 (similarity transfer from P04798, a characterized P450), consistent with the protein being a cytochrome P450 monooxygenase (astC). The expected answer D ('heme') matches the database annotation exactly.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark P450 heme-binding motif 'FGHGGHSCPGRF' (FxxGxxxCxG pattern with the Cys coordinating heme iron), plus an N-terminal hydrophobic membrane-anchor region typical of microsomal P450s. Recognizing this as a cytochrome P450 is straightforward transferable family knowledge. The database convention across hundreds of P450 entries annotates the cofactor as 'heme' (ChEBI:30413), not 'heme b'. The term 'heme b' is more commonly reserved for electron-transport-chain cytochromes (cyt b, c1). A model trained on protein annotations would associate P450 → 'heme' as a learned pattern, distinguishing D from C. Mn(2+) (A) is associated with oxidoreductases like arginase or SOD; cob(II)alamin (B) with methyltransferases/isomerases — neither matches P450 family knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P450 family identification from the conserved heme-binding motif is transferable sequence-level knowledge. The convention of annotating P450 cofactor as 'heme' rather than 'heme b' is a pattern learned across the P450 superfamily in databases. This meaningfully distinguishes D from A, B, and C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C"
]
```

> Biochemically, the heme in P450s is protoporphyrin IX with iron, which is technically 'heme b' (ChEBI:16038). A rigorous biochemist could argue C is the more precise answer. However, the overwhelming database convention for P450 cofactor annotation uses the general term 'heme' (ChEBI:30413), and 'heme b' is more commonly used in the context of respiratory chain cytochromes. This makes C a secondary but defensible choice, while D aligns with standard annotation practice.


### Important caveats

- The cofactor annotation uses evidence code ECO:0000250 (similarity transfer from P04798), not direct experimental evidence for this specific protein.
- The distinction between 'heme' (ChEBI:30413) and 'heme b' (ChEBI:16038) is subtle; both describe iron-protoporphyrin, with 'heme b' being the specific chemical species in P450s.
- The protein is annotated as Cytochrome P450 monooxygenase astC from Aspergillus terreus, but this organism/protein name was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark P450 heme-binding motif 'FGHGGHSCPGRF' (FxxGxxxCxG pattern with the Cys coordinating heme iron), plus an N-terminal hydrophobic membrane-anchor region typical of microsomal P450s. Recognizing this as a cytochrome P450 is straightforward transferable family knowledge. The database convention across hundreds of P450 entries annotates the cofactor as 'heme' (ChEBI:30413), not 'heme b'. The term 'heme b' is more commonly reserved for electron-transport-chain cytochromes (cyt b, c1). A model trained on protein annotations would associate P450 → 'heme' as a learned pattern, distinguishing D from C. Mn(2+) (A) is associated with oxidoreductases like arginase or SOD; cob(II)alamin (B) with methyltransferases/isomerases — neither matches P450 family knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P450 family identification from the conserved heme-binding motif is transferable sequence-level knowledge. The convention of annotating P450 cofactor as 'heme' rather than 'heme b' is a pattern learned across the P450 superfamily in databases. This meaningfully distinguishes D from A, B, and C."
  },
  "case_id": "cofactor_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists the cofactor as 'heme' with cross-reference ChEBI:CHEBI:30413, which is the general 'heme' term (not the more specific 'heme b'). The evidence code is ECO:0000250 (similarity transfer from P04798, a characterized P450), consistent with the protein being a cytochrome P450 monooxygenase (astC). The expected answer D ('heme') matches the database annotation exactly."
  },
  "important_caveats": [
    "The cofactor annotation uses evidence code ECO:0000250 (similarity transfer from P04798), not direct experimental evidence for this specific protein.",
    "The distinction between 'heme' (ChEBI:30413) and 'heme b' (ChEBI:16038) is subtle; both describe iron-protoporphyrin, with 'heme b' being the specific chemical species in P450s.",
    "The protein is annotated as Cytochrome P450 monooxygenase astC from Aspergillus terreus, but this organism/protein name was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C"
    ],
    "reason": "Biochemically, the heme in P450s is protoporphyrin IX with iron, which is technically 'heme b' (ChEBI:16038). A rigorous biochemist could argue C is the more precise answer. However, the overwhelming database convention for P450 cofactor annotation uses the general term 'heme' (ChEBI:30413), and 'heme b' is more commonly used in the context of respiratory chain cytochromes. This makes C a secondary but defensible choice, while D aligns with standard annotation practice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists the cofactor as 'heme' with cross-reference ChEBI:CHEBI:30413, which is the general 'heme' term (not the more specific 'heme b'). The evidence code is ECO:0000250 (similarity transfer from P04798, a characterized P450), consistent with the protein being a cytochrome P450 monooxygenase (astC). The expected answer D ('heme') matches the database annotation exactly.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark P450 heme-binding motif 'FGHGGHSCPGRF' (FxxGxxxCxG pattern with the Cys coordinating heme iron), plus an N-terminal hydrophobic membrane-anchor region typical of microsomal P450s. Recognizing this as a cytochrome P450 is straightforward transferable family knowledge. The database convention across hundreds of P450 entries annotates the cofactor as 'heme' (ChEBI:30413), not 'heme b'. The term 'heme b' is more commonly reserved for electron-transport-chain cytochromes (cyt b, c1). A model trained on protein annotations would associate P450 → 'heme' as a learned pattern, distinguishing D from C. Mn(2+) (A) is associated with oxidoreductases like arginase or SOD; cob(II)alamin (B) with methyltransferases/isomerases — neither matches P450 family knowledge.",
    "missing_item_specific_fact": "",
    "reason": "The P450 family identification from the conserved heme-binding motif is transferable sequence-level knowledge. The convention of annotating P450 cofactor as 'heme' rather than 'heme b' is a pattern learned across the P450 superfamily in databases. This meaningfully distinguishes D from A, B, and C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C"],
    "reason": "Biochemically, the heme in P450s is protoporphyrin IX with iron, which is technically 'heme b' (ChEBI:16038). A rigorous biochemist could argue C is the more precise answer. However, the overwhelming database convention for P450 cofactor annotation uses the general term 'heme' (ChEBI:30413), and 'heme b' is more commonly used in the context of respiratory chain cytochromes. This makes C a secondary but defensible choice, while D aligns with standard annotation practice."
  },
  "important_caveats": [
    "The cofactor annotation uses evidence code ECO:0000250 (similarity transfer from P04798), not direct experimental evidence for this specific protein.",
    "The distinction between 'heme' (ChEBI:30413) and 'heme b' (ChEBI:16038) is subtle; both describe iron-protoporphyrin, with 'heme b' being the specific chemical species in P450s.",
    "The protein is annotated as Cytochrome P450 monooxygenase astC from Aspergillus terreus, but this organism/protein name was not provided to the evaluated model."
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
  "benchmark_sequence_length": 538,
  "benchmark_sequence_sha256": "d64a1263e1e31530d1873b74b304f62355010d457a8b6d79b78a7154c76862f3",
  "current_entry_audit": {
    "entryVersion": 98,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 538,
  "current_source_sequence_sha256": "d64a1263e1e31530d1873b74b304f62355010d457a8b6d79b78a7154c76862f3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 96,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0CPG6",
  "selected_historical_entry_version": 96,
  "selected_historical_record_sha256": "482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd",
  "selected_historical_source_sequence_length": 538,
  "selected_historical_source_sequence_sha256": "d64a1263e1e31530d1873b74b304f62355010d457a8b6d79b78a7154c76862f3",
  "selected_historical_version": {
    "accession": "Q0CPG6",
    "database": "Swiss-Prot",
    "entryVersion": 96,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTC_ASPTN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0CPG6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":98,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein C\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase astC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P04798\",\"source\":\"UniProtKB\"}],\"name\":\"heme\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:22.231293+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H1",
  "excerpt": "ID   ASTC_ASPTN              Reviewed;         538 AA.\nAC   Q0CPG6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 96.\nDE   RecName: Full=Cytochrome P450 monooxygenase astC {ECO:0000303|PubMed:29995859};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein C {ECO:0000303|PubMed:29995859};\nGN   Name=astC {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04418;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:24.324806+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd",
  "url": "https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cytochrome P450 monooxygenase astC {ECO:0000303|PubMed:29995859};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein C {ECO:0000303|PubMed:29995859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:24.324806+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd",
  "url": "https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:24.324806+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd",
  "url": "https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=heme; Xref=ChEBI:CHEBI:30413;\nCC         Evidence={ECO:0000250|UniProtKB:P04798};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:24.324806+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd",
  "url": "https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 127. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
