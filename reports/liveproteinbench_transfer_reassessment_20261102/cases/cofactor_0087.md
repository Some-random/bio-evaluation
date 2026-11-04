# cofactor_0087

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0087.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — heme

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSASGKEKPLKDVPGSYGVPVVGALKDRLDFYWFQGEVEFYKSRMEKNQSTVFRVNFPPGPPGFPEGHGIVLLDQVSYSVLLDNAKVDKRDTLIGSYMPDLAFTGGYRTLPYLDTAEEKHTTYKSLMFEILHESAQRFGPELSSAFDRTAQEWEAKIAKDGSVESLSTAGNMVIQFLYKTITHQDPMATMGDDPHSVYMAWTGVQFAGIAYTNLPHITEELLMHSFQLPFFPIKKKYEQIVEFFRSAGSGLLDLAVTKYGLDREEALHNLVFSFGINTRLGLLKMFPPILFFIARAGAEFQARLKQEIRGRMKKREDAASIQALGDLKLVKATVLEVFRLMPSIFVAFGRARQDLEVESHDARYKIKKGELLGTHQYFVMRDPVVFKDPHSFVPDRFMGSEGAALLPHIVWSNGRETDSPTPTNKQCPGKNQAELIAVQFIAEMFLRYDSWEVTQESSVSATKLDVHLCKLVKRS

[Multiple Choices]
A. Cu(2+)
B. Co(2+)
C. FAD
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

> The annotation for the sequence-matched protein assigns heme, with evidence transferred from a related UniProtKB protein (ECO:0000250), rather than direct experimental evidence on this exact protein. That assignment is consistent with the catalytic heme requirement of cytochrome P450 enzymes.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a cytochrome P450-family enzyme, including a C-terminal cysteine-containing region characteristic of the heme-binding part of that family. Transferable knowledge of P450 enzymes links their catalytic activity to heme, distinguishing heme from Cu(2+), Co(2+), and FAD among the options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition from sequence features and the shared P450 catalytic mechanism provide a meaningful inference without needing the exact protein's database record. This supports a probabilistic family-level prediction, not independent confirmation of heme binding in this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives distinguish heme from unrelated common cofactors, and the P450-family inference supports heme.


### Important caveats

- The supplied source annotation is transferred by similarity, not direct experimental evidence for this exact protein.
- Reviewer-only protein identity and annotation were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a cytochrome P450-family enzyme, including a C-terminal cysteine-containing region characteristic of the heme-binding part of that family. Transferable knowledge of P450 enzymes links their catalytic activity to heme, distinguishing heme from Cu(2+), Co(2+), and FAD among the options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition from sequence features and the shared P450 catalytic mechanism provide a meaningful inference without needing the exact protein's database record. This supports a probabilistic family-level prediction, not independent confirmation of heme binding in this particular protein."
  },
  "case_id": "cofactor_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The annotation for the sequence-matched protein assigns heme, with evidence transferred from a related UniProtKB protein (ECO:0000250), rather than direct experimental evidence on this exact protein. That assignment is consistent with the catalytic heme requirement of cytochrome P450 enzymes."
  },
  "important_caveats": [
    "The supplied source annotation is transferred by similarity, not direct experimental evidence for this exact protein.",
    "Reviewer-only protein identity and annotation were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives distinguish heme from unrelated common cofactors, and the P450-family inference supports heme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The annotation for the sequence-matched protein assigns heme, with evidence transferred from a related UniProtKB protein (ECO:0000250), rather than direct experimental evidence on this exact protein. That assignment is consistent with the catalytic heme requirement of cytochrome P450 enzymes.",
    "evidence_ids": ["H4", "C5", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a cytochrome P450-family enzyme, including a C-terminal cysteine-containing region characteristic of the heme-binding part of that family. Transferable knowledge of P450 enzymes links their catalytic activity to heme, distinguishing heme from Cu(2+), Co(2+), and FAD among the options.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition from sequence features and the shared P450 catalytic mechanism provide a meaningful inference without needing the exact protein's database record. This supports a probabilistic family-level prediction, not independent confirmation of heme binding in this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives distinguish heme from unrelated common cofactors, and the P450-family inference supports heme."
  },
  "important_caveats": [
    "The supplied source annotation is transferred by similarity, not direct experimental evidence for this exact protein.",
    "Reviewer-only protein identity and annotation were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly lists heme (CHEBI:30413) as the cofactor for this protein (D8S724, Divinyl ether synthase CYP74M1). The evidence code is ECO:0000250 (inferred from similarity to Q96242), which is a transferred annotation rather than direct experimental measurement for this exact protein. However, the protein belongs to the cytochrome P450 superfamily (CYP74M1), and the universal requirement of heme as the prosthetic group in all CYP450 enzymes is well-established biochemistry. The PubMed reference (26776054) confirms the enzymatic function as a divinyl ether synthase (EC 4.2.1.183), a CYP74-family member. The answer 'heme' is scientifically correct.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple well-known cytochrome P450 signature motifs: (1) the I-helix region 'FAGIAYTNLPHITEELLMHSF' with its characteristic FxxG pattern; (2) the heme-binding region beginning 'FGRARQDLE' which is the start of the canonical FxxGxxxCxG heme-ligating motif (slightly diverged in CYP74 family but still recognizable); (3) the overall ~475-residue length and domain architecture consistent with a microsomal CYP450; (4) the 'ExxR' pattern in the K-helix region. These are highly conserved family-level features across the entire CYP450 superfamily (thousands of characterized members). Once a model recognizes the protein as a cytochrome P450 from these motifs, the cofactor assignment is unambiguous: ALL cytochrome P450 enzymes use heme (iron-protoporphyrin IX) as their prosthetic group to activate molecular oxygen. Cu2+, Co2+, and FAD are not cofactors of any CYP450 enzyme. This is a universal family-level biochemical fact, not a protein-specific measurement.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The CYP450 superfamily is one of the most extensively characterized enzyme families in biology. The heme-binding motifs (FxxGxxxCxG, I-helix FAGIAYTNLPHITEELLMHSF pattern) are textbook-level conserved features. A knowledgeable model recognizing these motifs can confidently assign this as a CYP450 and conclude heme is the cofactor. The reasoning relies on family-level transfer (all CYP450s use heme) rather than a protein-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the protein is identified as a cytochrome P450 (which the sequence motifs clearly support), heme is the only possible cofactor. Cu2+, Co2+, and FAD are not cofactors of any known CYP450 enzyme. There is no genuine ambiguity among the offered choices for a CYP450.


### Important caveats

- The UniProt cofactor annotation uses evidence code ECO:0000250 (inferred from similarity to Q96242), meaning it is a transferred annotation rather than a direct experimental measurement on this exact protein. However, the universal heme requirement of CYP450s makes this a well-established family-level fact.
- The CYP74 family heme-binding motif is slightly diverged from the canonical FxxGxxxCxG (the exact Cys spacing differs), but the overall CYP450 architecture is still clearly recognizable from the I-helix and other conserved features.
- The reviewer-only source identified this as D8S724 (CYP74M1 from Selaginella moellendorffii), but the sequence itself contains sufficient CYP450 family signatures for identification without needing the accession number.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple well-known cytochrome P450 signature motifs: (1) the I-helix region 'FAGIAYTNLPHITEELLMHSF' with its characteristic FxxG pattern; (2) the heme-binding region beginning 'FGRARQDLE' which is the start of the canonical FxxGxxxCxG heme-ligating motif (slightly diverged in CYP74 family but still recognizable); (3) the overall ~475-residue length and domain architecture consistent with a microsomal CYP450; (4) the 'ExxR' pattern in the K-helix region. These are highly conserved family-level features across the entire CYP450 superfamily (thousands of characterized members). Once a model recognizes the protein as a cytochrome P450 from these motifs, the cofactor assignment is unambiguous: ALL cytochrome P450 enzymes use heme (iron-protoporphyrin IX) as their prosthetic group to activate molecular oxygen. Cu2+, Co2+, and FAD are not cofactors of any CYP450 enzyme. This is a universal family-level biochemical fact, not a protein-specific measurement.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The CYP450 superfamily is one of the most extensively characterized enzyme families in biology. The heme-binding motifs (FxxGxxxCxG, I-helix FAGIAYTNLPHITEELLMHSF pattern) are textbook-level conserved features. A knowledgeable model recognizing these motifs can confidently assign this as a CYP450 and conclude heme is the cofactor. The reasoning relies on family-level transfer (all CYP450s use heme) rather than a protein-specific database lookup."
  },
  "case_id": "cofactor_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists heme (CHEBI:30413) as the cofactor for this protein (D8S724, Divinyl ether synthase CYP74M1). The evidence code is ECO:0000250 (inferred from similarity to Q96242), which is a transferred annotation rather than direct experimental measurement for this exact protein. However, the protein belongs to the cytochrome P450 superfamily (CYP74M1), and the universal requirement of heme as the prosthetic group in all CYP450 enzymes is well-established biochemistry. The PubMed reference (26776054) confirms the enzymatic function as a divinyl ether synthase (EC 4.2.1.183), a CYP74-family member. The answer 'heme' is scientifically correct."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000250 (inferred from similarity to Q96242), meaning it is a transferred annotation rather than a direct experimental measurement on this exact protein. However, the universal heme requirement of CYP450s makes this a well-established family-level fact.",
    "The CYP74 family heme-binding motif is slightly diverged from the canonical FxxGxxxCxG (the exact Cys spacing differs), but the overall CYP450 architecture is still clearly recognizable from the I-helix and other conserved features.",
    "The reviewer-only source identified this as D8S724 (CYP74M1 from Selaginella moellendorffii), but the sequence itself contains sufficient CYP450 family signatures for identification without needing the accession number."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is identified as a cytochrome P450 (which the sequence motifs clearly support), heme is the only possible cofactor. Cu2+, Co2+, and FAD are not cofactors of any known CYP450 enzyme. There is no genuine ambiguity among the offered choices for a CYP450."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists heme (CHEBI:30413) as the cofactor for this protein (D8S724, Divinyl ether synthase CYP74M1). The evidence code is ECO:0000250 (inferred from similarity to Q96242), which is a transferred annotation rather than direct experimental measurement for this exact protein. However, the protein belongs to the cytochrome P450 superfamily (CYP74M1), and the universal requirement of heme as the prosthetic group in all CYP450 enzymes is well-established biochemistry. The PubMed reference (26776054) confirms the enzymatic function as a divinyl ether synthase (EC 4.2.1.183), a CYP74-family member. The answer 'heme' is scientifically correct.",
    "evidence_ids": ["C5", "C4", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple well-known cytochrome P450 signature motifs: (1) the I-helix region 'FAGIAYTNLPHITEELLMHSF' with its characteristic FxxG pattern; (2) the heme-binding region beginning 'FGRARQDLE' which is the start of the canonical FxxGxxxCxG heme-ligating motif (slightly diverged in CYP74 family but still recognizable); (3) the overall ~475-residue length and domain architecture consistent with a microsomal CYP450; (4) the 'ExxR' pattern in the K-helix region. These are highly conserved family-level features across the entire CYP450 superfamily (thousands of characterized members). Once a model recognizes the protein as a cytochrome P450 from these motifs, the cofactor assignment is unambiguous: ALL cytochrome P450 enzymes use heme (iron-protoporphyrin IX) as their prosthetic group to activate molecular oxygen. Cu2+, Co2+, and FAD are not cofactors of any CYP450 enzyme. This is a universal family-level biochemical fact, not a protein-specific measurement.",
    "missing_item_specific_fact": "",
    "reason": "The CYP450 superfamily is one of the most extensively characterized enzyme families in biology. The heme-binding motifs (FxxGxxxCxG, I-helix FAGIAYTNLPHITEELLMHSF pattern) are textbook-level conserved features. A knowledgeable model recognizing these motifs can confidently assign this as a CYP450 and conclude heme is the cofactor. The reasoning relies on family-level transfer (all CYP450s use heme) rather than a protein-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is identified as a cytochrome P450 (which the sequence motifs clearly support), heme is the only possible cofactor. Cu2+, Co2+, and FAD are not cofactors of any known CYP450 enzyme. There is no genuine ambiguity among the offered choices for a CYP450."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000250 (inferred from similarity to Q96242), meaning it is a transferred annotation rather than a direct experimental measurement on this exact protein. However, the universal heme requirement of CYP450s makes this a well-established family-level fact.",
    "The CYP74 family heme-binding motif is slightly diverged from the canonical FxxGxxxCxG (the exact Cys spacing differs), but the overall CYP450 architecture is still clearly recognizable from the I-helix and other conserved features.",
    "The reviewer-only source identified this as D8S724 (CYP74M1 from Selaginella moellendorffii), but the sequence itself contains sufficient CYP450 family signatures for identification without needing the accession number."
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
  "benchmark_sequence_length": 475,
  "benchmark_sequence_sha256": "9f49b14cb8368a9ffc643a4692f62ffc62551e339d784cdad52577751ca0370f",
  "current_entry_audit": {
    "entryVersion": 66,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-10-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 475,
  "current_source_sequence_sha256": "9f49b14cb8368a9ffc643a4692f62ffc62551e339d784cdad52577751ca0370f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 64,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D8S724",
  "selected_historical_entry_version": 64,
  "selected_historical_record_sha256": "1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c",
  "selected_historical_source_sequence_length": 475,
  "selected_historical_source_sequence_sha256": "9f49b14cb8368a9ffc643a4692f62ffc62551e339d784cdad52577751ca0370f",
  "selected_historical_version": {
    "accession": "D8S724",
    "database": "Swiss-Prot",
    "entryVersion": 64,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C74M1_SELML",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D8S724\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:52.483973+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059",
  "url": "https://rest.uniprot.org/uniprotkb/D8S724.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":66,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-10-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:52.483973+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059",
  "url": "https://rest.uniprot.org/uniprotkb/D8S724.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Gemmiferous spikemoss\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Lycopodiopsida\",\"Selaginellales\",\"Selaginellaceae\",\"Selaginelloideae\",\"Selaginella\"],\"scientificName\":\"Selaginella moellendorffii\",\"synonyms\":[\"Kungiselaginella moellendorffii\"],\"taxonId\":88036}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:52.483973+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059",
  "url": "https://rest.uniprot.org/uniprotkb/D8S724.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.183\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"Etheroleic acid synthase CYP74M1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"Divinyl ether synthase CYP74M1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:52.483973+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059",
  "url": "https://rest.uniprot.org/uniprotkb/D8S724.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q96242\",\"source\":\"UniProtKB\"}],\"name\":\"heme\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:27:52.483973+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059",
  "url": "https://rest.uniprot.org/uniprotkb/D8S724.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Gorina S.S.\",\"Toporkova Y.Y.\",\"Mukhtarova L.S.\",\"Smirnova E.O.\",\"Chechetkin I.R.\",\"Khairutdinov B.I.\",\"Gogolev Y.V.\",\"Grechkin A.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26776054\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbalip.2016.01.001\"}],\"citationType\":\"journal article\",\"firstPage\":\"301\",\"id\":\"26776054\",\"journal\":\"Biochim. Biophys. Acta\",\"lastPage\":\"309\",\"publicationDate\":\"2016\",\"title\":\"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular cloning and identification of divinyl ether synthases CYP74M1 and CYP74M3.\",\"volume\":\"1861\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:52.483973+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059",
  "url": "https://rest.uniprot.org/uniprotkb/D8S724.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H1",
  "excerpt": "ID   C74M1_SELML             Reviewed;         475 AA.\nAC   D8S724;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-OCT-2010, sequence version 1.\nDT   28-JAN-2026, entry version 64.\nDE   RecName: Full=Divinyl ether synthase CYP74M1 {ECO:0000303|PubMed:26776054};\nDE   AltName: Full=Etheroleic acid synthase CYP74M1 {ECO:0000305|PubMed:26776054};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};\nGN   Name=CYP74M1 {ECO:0000303|PubMed:26776054};\nGN   Synonyms=DES1 {ECO:0000303|PubMed:26776054};\nGN   ORFNames=SELMODRAFT_177485 {ECO:0000312|EMBL:EFJ19674.1};\nOS   Selaginella moellendorffii (Spikemoss).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Lycopodiopsida; Selaginellales; Selaginellaceae; Selaginella.\nOX   NCBI_TaxID=88036;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:54.936001+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c",
  "url": "https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Divinyl ether synthase CYP74M1 {ECO:0000303|PubMed:26776054};\nDE   AltName: Full=Etheroleic acid synthase CYP74M1 {ECO:0000305|PubMed:26776054};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:54.936001+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c",
  "url": "https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRX   PubMed=26776054; DOI=10.1016/j.bbalip.2016.01.001;\nRA   Gorina S.S., Toporkova Y.Y., Mukhtarova L.S., Smirnova E.O.,\nRA   Chechetkin I.R., Khairutdinov B.I., Gogolev Y.V., Grechkin A.N.;\nRT   \"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular\nRT   cloning and identification of divinyl ether synthases CYP74M1 and\nRT   CYP74M3.\";\nRL   Biochim. Biophys. Acta 1861:301-309(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:54.936001+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c",
  "url": "https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=heme; Xref=ChEBI:CHEBI:30413;\nCC         Evidence={ECO:0000250|UniProtKB:Q96242};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:54.936001+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c",
  "url": "https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
