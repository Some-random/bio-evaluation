# cofactor_0129

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0129.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDMNTFPASTYCESIVRFLDAIEYHDDNLTHEERVEGLRHVHSKTAQYFTEPLPRSILKGVAPRRIAAVTRTISHFIVYCWSKLPREAQVDVSIYLSIINVLDDEISSEPSTQMTSFWSDLIQGKQPKHPFWVLFNSHLPRLLRHYGSFCAFNIMRCTFDYFEGCWIEQHNFQGYPGADCYPSFLRRLNCLGGAVAGTIFPAAKFDEQKLFAQMSCVMAQIDGPVALMNDLFSFYKEYDQDEANLVSNWCTVDGITMDQALTRLTDDTIHACVRILDILKDKDPDMLATIRGFIHGYATWHICDFRYRLREIYDREDLQESGARFREYFDKAIDVGWVDVEEWTCQVQGFEVEGPAPSGSEVQAYQANAFGFSVDTQRHHNIDYVGSSILGLFEWATRYLRGKLPLGNA

[Multiple Choices]
A. Mg(2+)
B. tungstopterin
C. [4Fe-4S] cluster
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

> The sequence-matched entry identifies the protein as a terpene cyclase and annotates Mg(2+) as its cofactor. The cofactor annotation is transferred by similarity rather than shown here as a direct experiment on this exact protein, so the evidence supports the key without establishing direct measurement.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model could recognize the sequence as consistent with a terpene cyclase. Class I terpene cyclases generally use divalent metal ions, commonly Mg2+, to support diphosphate-substrate catalysis; this makes Mg2+ a meaningful choice over tungsten-pterin, &#91;4Fe-4S&#93;, or cob(II)alamin, which are associated with different enzyme families and mechanisms.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level catalytic pattern provides a credible basis for distinguishing the offered options without knowing this exact protein's database annotation. The sequence-only family assignment may be uncertain, and the supplied evidence indicates that the exact cofactor annotation is transferred rather than direct experimental confirmation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the terpene-cyclase inference, Mg(2+) is the clearly best-supported option among those offered.


### Important caveats

- The cofactor annotation cites similarity-based evidence, not direct experimental evidence for this exact sequence.
- The family-level inference is probabilistic; the original input provides only a sequence and choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as consistent with a terpene cyclase. Class I terpene cyclases generally use divalent metal ions, commonly Mg2+, to support diphosphate-substrate catalysis; this makes Mg2+ a meaningful choice over tungsten-pterin, [4Fe-4S], or cob(II)alamin, which are associated with different enzyme families and mechanisms.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level catalytic pattern provides a credible basis for distinguishing the offered options without knowing this exact protein's database annotation. The sequence-only family assignment may be uncertain, and the supplied evidence indicates that the exact cofactor annotation is transferred rather than direct experimental confirmation."
  },
  "case_id": "cofactor_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched entry identifies the protein as a terpene cyclase and annotates Mg(2+) as its cofactor. The cofactor annotation is transferred by similarity rather than shown here as a direct experiment on this exact protein, so the evidence supports the key without establishing direct measurement."
  },
  "important_caveats": [
    "The cofactor annotation cites similarity-based evidence, not direct experimental evidence for this exact sequence.",
    "The family-level inference is probabilistic; the original input provides only a sequence and choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the terpene-cyclase inference, Mg(2+) is the clearly best-supported option among those offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched entry identifies the protein as a terpene cyclase and annotates Mg(2+) as its cofactor. The cofactor annotation is transferred by similarity rather than shown here as a direct experiment on this exact protein, so the evidence supports the key without establishing direct measurement.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as consistent with a terpene cyclase. Class I terpene cyclases generally use divalent metal ions, commonly Mg2+, to support diphosphate-substrate catalysis; this makes Mg2+ a meaningful choice over tungsten-pterin, [4Fe-4S], or cob(II)alamin, which are associated with different enzyme families and mechanisms.",
    "missing_item_specific_fact": "",
    "reason": "The family-level catalytic pattern provides a credible basis for distinguishing the offered options without knowing this exact protein's database annotation. The sequence-only family assignment may be uncertain, and the supplied evidence indicates that the exact cofactor annotation is transferred rather than direct experimental confirmation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the terpene-cyclase inference, Mg(2+) is the clearly best-supported option among those offered."
  },
  "important_caveats": [
    "The cofactor annotation cites similarity-based evidence, not direct experimental evidence for this exact sequence.",
    "The family-level inference is probabilistic; the original input provides only a sequence and choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q0CPG8 (sequence matched, 409 aa) annotates Mg(2+) as the cofactor (evidence IDs C5, H4). The evidence code is ECO:0000250 (inferred by similarity to P13513), meaning the cofactor assignment is transferred computationally rather than experimentally demonstrated for this exact protein. However, the protein is annotated as a terpene cyclase (astA, EC 4.2.3.-) with function/catalytic activity supported by PubMed:29995859 (Nature 2018). Mg(2+) is the universally accepted divalent-metal cofactor for terpene cyclases, making the annotation well-supported at the family level even though the per-protein evidence is similarity-based.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~409 aa) contains aspartate-rich regions characteristic of the DDxxD motif (e.g., 'DDEISSEPST' and 'DDEANLVSNWCTVDGITMDQ'), which is the hallmark active-site signature of terpene cyclases. This motif coordinates Mg(2+) ions that are essential for ionizing the diphosphate group of the substrate (e.g., farnesyl diphosphate) to initiate cyclization. Recognizing the DDxxD motif and the overall single-domain terpene-cyclase architecture is standard family-level knowledge. None of the distractor cofactors are associated with terpene cyclases: tungstopterin occurs in anaerobic tungsten-containing oxidoreductases, &#91;4Fe-4S&#93; clusters in radical SAM enzymes and dehydratases (requiring CxxC motifs absent here), and cob(II)alamin in B12-dependent isomerases/methyltransferases (requiring B12-binding domains absent here). The DDxxD motif and the absence of any motifs for the other three cofactors meaningfully and uniquely point to Mg(2+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with standard knowledge of terpene cyclase family features (DDxxD motif, ~400 aa single-domain architecture, aspartate-rich active site) can confidently assign Mg(2+) and exclude the three distractors without knowing this specific protein's database record. The inference relies on well-established family-level biochemistry, not on memorizing Q0CPG8's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four cofactor options correspond to entirely different enzyme classes. The DDxxD motif and terpene-cyclase architecture unambiguously select Mg(2+); the other three cofactors have no plausible connection to a terpene cyclase.


### Important caveats

- The Mg(2+) cofactor annotation in UniProt carries evidence code ECO:0000250 (similarity to P13513), not direct experimental evidence for astA itself. The family-level assignment is nonetheless well-established.
- Some terpene cyclases can substitute Mn(2+) for Mg(2+), but Mn(2+) is not among the offered choices, so this does not create ambiguity here.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) and Swiss-Prot reviewed status, but the evaluated model had no access to the UniProt entry or organism identity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~409 aa) contains aspartate-rich regions characteristic of the DDxxD motif (e.g., 'DDEISSEPST' and 'DDEANLVSNWCTVDGITMDQ'), which is the hallmark active-site signature of terpene cyclases. This motif coordinates Mg(2+) ions that are essential for ionizing the diphosphate group of the substrate (e.g., farnesyl diphosphate) to initiate cyclization. Recognizing the DDxxD motif and the overall single-domain terpene-cyclase architecture is standard family-level knowledge. None of the distractor cofactors are associated with terpene cyclases: tungstopterin occurs in anaerobic tungsten-containing oxidoreductases, [4Fe-4S] clusters in radical SAM enzymes and dehydratases (requiring CxxC motifs absent here), and cob(II)alamin in B12-dependent isomerases/methyltransferases (requiring B12-binding domains absent here). The DDxxD motif and the absence of any motifs for the other three cofactors meaningfully and uniquely point to Mg(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with standard knowledge of terpene cyclase family features (DDxxD motif, ~400 aa single-domain architecture, aspartate-rich active site) can confidently assign Mg(2+) and exclude the three distractors without knowing this specific protein's database record. The inference relies on well-established family-level biochemistry, not on memorizing Q0CPG8's annotation."
  },
  "case_id": "cofactor_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG8 (sequence matched, 409 aa) annotates Mg(2+) as the cofactor (evidence IDs C5, H4). The evidence code is ECO:0000250 (inferred by similarity to P13513), meaning the cofactor assignment is transferred computationally rather than experimentally demonstrated for this exact protein. However, the protein is annotated as a terpene cyclase (astA, EC 4.2.3.-) with function/catalytic activity supported by PubMed:29995859 (Nature 2018). Mg(2+) is the universally accepted divalent-metal cofactor for terpene cyclases, making the annotation well-supported at the family level even though the per-protein evidence is similarity-based."
  },
  "important_caveats": [
    "The Mg(2+) cofactor annotation in UniProt carries evidence code ECO:0000250 (similarity to P13513), not direct experimental evidence for astA itself. The family-level assignment is nonetheless well-established.",
    "Some terpene cyclases can substitute Mn(2+) for Mg(2+), but Mn(2+) is not among the offered choices, so this does not create ambiguity here.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) and Swiss-Prot reviewed status, but the evaluated model had no access to the UniProt entry or organism identity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor options correspond to entirely different enzyme classes. The DDxxD motif and terpene-cyclase architecture unambiguously select Mg(2+); the other three cofactors have no plausible connection to a terpene cyclase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG8 (sequence matched, 409 aa) annotates Mg(2+) as the cofactor (evidence IDs C5, H4). The evidence code is ECO:0000250 (inferred by similarity to P13513), meaning the cofactor assignment is transferred computationally rather than experimentally demonstrated for this exact protein. However, the protein is annotated as a terpene cyclase (astA, EC 4.2.3.-) with function/catalytic activity supported by PubMed:29995859 (Nature 2018). Mg(2+) is the universally accepted divalent-metal cofactor for terpene cyclases, making the annotation well-supported at the family level even though the per-protein evidence is similarity-based.",
    "evidence_ids": ["C5", "H4", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~409 aa) contains aspartate-rich regions characteristic of the DDxxD motif (e.g., 'DDEISSEPST' and 'DDEANLVSNWCTVDGITMDQ'), which is the hallmark active-site signature of terpene cyclases. This motif coordinates Mg(2+) ions that are essential for ionizing the diphosphate group of the substrate (e.g., farnesyl diphosphate) to initiate cyclization. Recognizing the DDxxD motif and the overall single-domain terpene-cyclase architecture is standard family-level knowledge. None of the distractor cofactors are associated with terpene cyclases: tungstopterin occurs in anaerobic tungsten-containing oxidoreductases, [4Fe-4S] clusters in radical SAM enzymes and dehydratases (requiring CxxC motifs absent here), and cob(II)alamin in B12-dependent isomerases/methyltransferases (requiring B12-binding domains absent here). The DDxxD motif and the absence of any motifs for the other three cofactors meaningfully and uniquely point to Mg(2+).",
    "missing_item_specific_fact": "",
    "reason": "A model with standard knowledge of terpene cyclase family features (DDxxD motif, ~400 aa single-domain architecture, aspartate-rich active site) can confidently assign Mg(2+) and exclude the three distractors without knowing this specific protein's database record. The inference relies on well-established family-level biochemistry, not on memorizing Q0CPG8's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor options correspond to entirely different enzyme classes. The DDxxD motif and terpene-cyclase architecture unambiguously select Mg(2+); the other three cofactors have no plausible connection to a terpene cyclase."
  },
  "important_caveats": [
    "The Mg(2+) cofactor annotation in UniProt carries evidence code ECO:0000250 (similarity to P13513), not direct experimental evidence for astA itself. The family-level assignment is nonetheless well-established.",
    "Some terpene cyclases can substitute Mn(2+) for Mg(2+), but Mn(2+) is not among the offered choices, so this does not create ambiguity here.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) and Swiss-Prot reviewed status, but the evaluated model had no access to the UniProt entry or organism identity."
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
  "benchmark_sequence_length": 409,
  "benchmark_sequence_sha256": "a8bdca14275904fa582aa8697339e5415804e0c32861786fd957a494391b298d",
  "current_entry_audit": {
    "entryVersion": 74,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 409,
  "current_source_sequence_sha256": "a8bdca14275904fa582aa8697339e5415804e0c32861786fd957a494391b298d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 72,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0CPG8",
  "selected_historical_entry_version": 72,
  "selected_historical_record_sha256": "8040263c1b9046b4a755612b8a302a40f1e3a3fb5933ba220c4cdc45d26bb7b4",
  "selected_historical_source_sequence_length": 409,
  "selected_historical_source_sequence_sha256": "a8bdca14275904fa582aa8697339e5415804e0c32861786fd957a494391b298d",
  "selected_historical_version": {
    "accession": "Q0CPG8",
    "database": "Swiss-Prot",
    "entryVersion": 72,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTA_ASPTN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0CPG8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":74,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Terpene cyclase astA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P13513\",\"source\":\"UniProtKB\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:25.406247+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6e167e30a30f78b9ccfda1c5f52911fe9fcc757c95015df5d729c7d3a30f26f8",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H1",
  "excerpt": "ID   ASTA_ASPTN              Reviewed;         409 AA.\nAC   Q0CPG8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 72.\nDE   RecName: Full=Terpene cyclase astA {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.3.- {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein A {ECO:0000303|PubMed:29995859};\nGN   Name=astA {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04416;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:31.349868+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8040263c1b9046b4a755612b8a302a40f1e3a3fb5933ba220c4cdc45d26bb7b4",
  "url": "https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Terpene cyclase astA {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.3.- {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein A {ECO:0000303|PubMed:29995859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:31.349868+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8040263c1b9046b4a755612b8a302a40f1e3a3fb5933ba220c4cdc45d26bb7b4",
  "url": "https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:31.349868+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8040263c1b9046b4a755612b8a302a40f1e3a3fb5933ba220c4cdc45d26bb7b4",
  "url": "https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000250|UniProtKB:P13513};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:31.349868+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8040263c1b9046b4a755612b8a302a40f1e3a3fb5933ba220c4cdc45d26bb7b4",
  "url": "https://rest.uniprot.org/unisave/Q0CPG8?format=txt&versions=72"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
