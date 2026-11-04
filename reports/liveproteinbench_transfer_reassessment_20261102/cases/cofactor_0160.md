# cofactor_0160

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0160.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKSKILCNLFKGKSCICLYTNCLNENNVNKCYYNLVRNYSDHVKDHFNKPRNVGSFDKNEKNIGTSIVGKASCGDVIKLQLKIENDVIKDARFMAFGCGSAIASSSYATELIKGKTIDEALKIKNNDIASHLSLPPVKIHCSLLAEDAIKHAIKNYREKVLT

[Multiple Choices]
A. Zn(2+)
B. pantetheine 4'-phosphate
C. [4Fe-4S] cluster
D. NAD(+)
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

> The sequence-matched UniProt record annotates a &#91;4Fe-4S&#93; cluster as the cofactor, citing evidence code ECO:0000269. The archived record also contains this cofactor annotation. This supports the key, though the excerpts do not independently present the underlying experimental results.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short, cysteine-rich sequence is compatible with the conserved IscU iron-sulfur-cluster scaffold family: cysteine ligands are characteristic of its cluster-binding role. Transferable knowledge of this family makes an iron-sulfur cluster a meaningful choice over Zn(2+), pantetheine 4'-phosphate, or NAD(+); among the offered options, that points to &#91;4Fe-4S&#93;.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and alternatives provides a credible basis for the keyed choice; knowing this exact protein's database annotation is not necessary to distinguish these options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level cluster-scaffold inference distinguishes the iron-sulfur choice from the offered alternatives.


### Important caveats

- The evidence supports the database cofactor annotation, but the excerpts do not show the underlying experimental measurements.
- IscU is an iron-sulfur cluster assembly scaffold rather than a typical catalytic enzyme; its cluster-binding state may depend on context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short, cysteine-rich sequence is compatible with the conserved IscU iron-sulfur-cluster scaffold family: cysteine ligands are characteristic of its cluster-binding role. Transferable knowledge of this family makes an iron-sulfur cluster a meaningful choice over Zn(2+), pantetheine 4'-phosphate, or NAD(+); among the offered options, that points to [4Fe-4S].",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and alternatives provides a credible basis for the keyed choice; knowing this exact protein's database annotation is not necessary to distinguish these options."
  },
  "case_id": "cofactor_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a [4Fe-4S] cluster as the cofactor, citing evidence code ECO:0000269. The archived record also contains this cofactor annotation. This supports the key, though the excerpts do not independently present the underlying experimental results."
  },
  "important_caveats": [
    "The evidence supports the database cofactor annotation, but the excerpts do not show the underlying experimental measurements.",
    "IscU is an iron-sulfur cluster assembly scaffold rather than a typical catalytic enzyme; its cluster-binding state may depend on context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level cluster-scaffold inference distinguishes the iron-sulfur choice from the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a [4Fe-4S] cluster as the cofactor, citing evidence code ECO:0000269. The archived record also contains this cofactor annotation. This supports the key, though the excerpts do not independently present the underlying experimental results.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short, cysteine-rich sequence is compatible with the conserved IscU iron-sulfur-cluster scaffold family: cysteine ligands are characteristic of its cluster-binding role. Transferable knowledge of this family makes an iron-sulfur cluster a meaningful choice over Zn(2+), pantetheine 4'-phosphate, or NAD(+); among the offered options, that points to [4Fe-4S].",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and alternatives provides a credible basis for the keyed choice; knowing this exact protein's database annotation is not necessary to distinguish these options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level cluster-scaffold inference distinguishes the iron-sulfur choice from the offered alternatives."
  },
  "important_caveats": [
    "The evidence supports the database cofactor annotation, but the excerpts do not show the underlying experimental measurements.",
    "IscU is an iron-sulfur cluster assembly scaffold rather than a typical catalytic enzyme; its cluster-binding state may depend on context."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IKT4 (ISCU_PLAF7, Iron-sulfur cluster assembly protein IscU from Plasmodium falciparum) explicitly annotates &#91;4Fe-4S&#93; cluster as the cofactor with experimental evidence (ECO:0000269, PubMed:34032321). The sequence matches the benchmark input exactly. The 2021 Molecular Microbiology paper by Sadik et al. provides experimental support for the &#91;4Fe-4S&#93; cluster cofactor assignment.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a dense cysteine cluster (C7, C14, C16, C20, C28) with spacings characteristic of &#91;Fe-S&#93; cluster coordination (CxxC, Cx4C, Cx8C motifs), which is the hallmark of iron-sulfur cluster scaffold proteins like IscU. Additional cysteines at C84, C96, and C146 are consistent with the multi-cysteine ligation pattern seen in IscU-family proteins (e.g., E. coli IscU uses C63, C104, C137). Against the alternatives: (1) NAD+ binding requires a Rossmann-fold GxGxxG motif, which is absent from this sequence; (2) pantetheine 4'-phosphate is carried by acyl carrier proteins/fatty acid synthases with conserved GxDSL serine motifs, not present here; (3) Zn(2+) coordination typically involves C2H2, C4, or C2HC motifs with histidines, but this sequence lacks histidines in the cysteine-rich region and the irregular, densely packed cysteine spacing is more consistent with &#91;Fe-S&#93; cluster ligation than zinc finger geometry. The small protein size (~162 aa) with a cysteine-rich N-terminal scaffold domain and a structured C-terminal domain matches the conserved architecture of IscU-family Fe-S scaffold proteins across bacteria and eukaryotes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the &#91;4Fe-4S&#93; cluster from the cysteine-rich N-terminal domain pattern (CxxC and related motifs), the absence of Rossmann-fold motifs (ruling out NAD+), the absence of ACP/CoA-transferase motifs (ruling out pantetheine 4'-phosphate), and the absence of histidines in the cysteine cluster (making Zn less likely than Fe-S). Family-level knowledge of IscU/Fe-S scaffold proteins provides a concrete, transferable basis for selecting C over the other options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cysteine-rich N-terminal motif strongly and specifically points to &#91;Fe-S&#93; cluster coordination. The alternatives (NAD+, pantetheine 4'-phosphate, Zn2+) each require distinct sequence features (Rossmann fold, ACP serine motif, Cys/His zinc-binding geometry) that are absent. No other option is meaningfully defensible.


### Important caveats

- The protein is from Plasmodium falciparum, an unusual organism for Fe-S biology; the IscU scaffold here has some atypical features noted in the 2021 paper, but the &#91;4Fe-4S&#93; cofactor assignment is experimentally supported.
- The cysteine spacing in this Plasmodium IscU differs somewhat from the canonical E. coli IscU pattern, but the overall cysteine-rich scaffold architecture remains recognizable.
- The evidence code ECO:0000269 indicates direct experimental evidence for the cofactor assignment, not mere computational inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a dense cysteine cluster (C7, C14, C16, C20, C28) with spacings characteristic of [Fe-S] cluster coordination (CxxC, Cx4C, Cx8C motifs), which is the hallmark of iron-sulfur cluster scaffold proteins like IscU. Additional cysteines at C84, C96, and C146 are consistent with the multi-cysteine ligation pattern seen in IscU-family proteins (e.g., E. coli IscU uses C63, C104, C137). Against the alternatives: (1) NAD+ binding requires a Rossmann-fold GxGxxG motif, which is absent from this sequence; (2) pantetheine 4'-phosphate is carried by acyl carrier proteins/fatty acid synthases with conserved GxDSL serine motifs, not present here; (3) Zn(2+) coordination typically involves C2H2, C4, or C2HC motifs with histidines, but this sequence lacks histidines in the cysteine-rich region and the irregular, densely packed cysteine spacing is more consistent with [Fe-S] cluster ligation than zinc finger geometry. The small protein size (~162 aa) with a cysteine-rich N-terminal scaffold domain and a structured C-terminal domain matches the conserved architecture of IscU-family Fe-S scaffold proteins across bacteria and eukaryotes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the [4Fe-4S] cluster from the cysteine-rich N-terminal domain pattern (CxxC and related motifs), the absence of Rossmann-fold motifs (ruling out NAD+), the absence of ACP/CoA-transferase motifs (ruling out pantetheine 4'-phosphate), and the absence of histidines in the cysteine cluster (making Zn less likely than Fe-S). Family-level knowledge of IscU/Fe-S scaffold proteins provides a concrete, transferable basis for selecting C over the other options."
  },
  "case_id": "cofactor_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IKT4 (ISCU_PLAF7, Iron-sulfur cluster assembly protein IscU from Plasmodium falciparum) explicitly annotates [4Fe-4S] cluster as the cofactor with experimental evidence (ECO:0000269, PubMed:34032321). The sequence matches the benchmark input exactly. The 2021 Molecular Microbiology paper by Sadik et al. provides experimental support for the [4Fe-4S] cluster cofactor assignment."
  },
  "important_caveats": [
    "The protein is from Plasmodium falciparum, an unusual organism for Fe-S biology; the IscU scaffold here has some atypical features noted in the 2021 paper, but the [4Fe-4S] cofactor assignment is experimentally supported.",
    "The cysteine spacing in this Plasmodium IscU differs somewhat from the canonical E. coli IscU pattern, but the overall cysteine-rich scaffold architecture remains recognizable.",
    "The evidence code ECO:0000269 indicates direct experimental evidence for the cofactor assignment, not mere computational inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cysteine-rich N-terminal motif strongly and specifically points to [Fe-S] cluster coordination. The alternatives (NAD+, pantetheine 4'-phosphate, Zn2+) each require distinct sequence features (Rossmann fold, ACP serine motif, Cys/His zinc-binding geometry) that are absent. No other option is meaningfully defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IKT4 (ISCU_PLAF7, Iron-sulfur cluster assembly protein IscU from Plasmodium falciparum) explicitly annotates [4Fe-4S] cluster as the cofactor with experimental evidence (ECO:0000269, PubMed:34032321). The sequence matches the benchmark input exactly. The 2021 Molecular Microbiology paper by Sadik et al. provides experimental support for the [4Fe-4S] cluster cofactor assignment.",
    "evidence_ids": ["C5", "C6", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a dense cysteine cluster (C7, C14, C16, C20, C28) with spacings characteristic of [Fe-S] cluster coordination (CxxC, Cx4C, Cx8C motifs), which is the hallmark of iron-sulfur cluster scaffold proteins like IscU. Additional cysteines at C84, C96, and C146 are consistent with the multi-cysteine ligation pattern seen in IscU-family proteins (e.g., E. coli IscU uses C63, C104, C137). Against the alternatives: (1) NAD+ binding requires a Rossmann-fold GxGxxG motif, which is absent from this sequence; (2) pantetheine 4'-phosphate is carried by acyl carrier proteins/fatty acid synthases with conserved GxDSL serine motifs, not present here; (3) Zn(2+) coordination typically involves C2H2, C4, or C2HC motifs with histidines, but this sequence lacks histidines in the cysteine-rich region and the irregular, densely packed cysteine spacing is more consistent with [Fe-S] cluster ligation than zinc finger geometry. The small protein size (~162 aa) with a cysteine-rich N-terminal scaffold domain and a structured C-terminal domain matches the conserved architecture of IscU-family Fe-S scaffold proteins across bacteria and eukaryotes.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the [4Fe-4S] cluster from the cysteine-rich N-terminal domain pattern (CxxC and related motifs), the absence of Rossmann-fold motifs (ruling out NAD+), the absence of ACP/CoA-transferase motifs (ruling out pantetheine 4'-phosphate), and the absence of histidines in the cysteine cluster (making Zn less likely than Fe-S). Family-level knowledge of IscU/Fe-S scaffold proteins provides a concrete, transferable basis for selecting C over the other options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cysteine-rich N-terminal motif strongly and specifically points to [Fe-S] cluster coordination. The alternatives (NAD+, pantetheine 4'-phosphate, Zn2+) each require distinct sequence features (Rossmann fold, ACP serine motif, Cys/His zinc-binding geometry) that are absent. No other option is meaningfully defensible."
  },
  "important_caveats": [
    "The protein is from Plasmodium falciparum, an unusual organism for Fe-S biology; the IscU scaffold here has some atypical features noted in the 2021 paper, but the [4Fe-4S] cofactor assignment is experimentally supported.",
    "The cysteine spacing in this Plasmodium IscU differs somewhat from the canonical E. coli IscU pattern, but the overall cysteine-rich scaffold architecture remains recognizable.",
    "The evidence code ECO:0000269 indicates direct experimental evidence for the cofactor assignment, not mere computational inference."
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
  "benchmark_sequence_length": 162,
  "benchmark_sequence_sha256": "8e140c4dbd21b2ba798ee3b637384532a5902af39272bee7a18981ab9ceabe88",
  "current_entry_audit": {
    "entryVersion": 125,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 162,
  "current_source_sequence_sha256": "8e140c4dbd21b2ba798ee3b637384532a5902af39272bee7a18981ab9ceabe88",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 123,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IKT4",
  "selected_historical_entry_version": 123,
  "selected_historical_record_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "selected_historical_source_sequence_length": 162,
  "selected_historical_source_sequence_sha256": "8e140c4dbd21b2ba798ee3b637384532a5902af39272bee7a18981ab9ceabe88",
  "selected_historical_version": {
    "accession": "Q8IKT4",
    "database": "Swiss-Prot",
    "entryVersion": 123,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ISCU_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IKT4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":125,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Iron-sulfur cluster assembly protein IscU\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"PfIscU\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:49883\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"name\":\"[4Fe-4S] cluster\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Sadik M.\",\"Afsar M.\",\"Ramachandran R.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34032321\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.14735\"}],\"citationType\":\"journal article\",\"firstPage\":\"606\",\"id\":\"34032321\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"623\",\"publicationDate\":\"2021\",\"title\":\"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"COFACTOR\",\"SUBUNIT\",\"INTERACTION WITH ISCS\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H1",
  "excerpt": "ID   ISCU_PLAF7              Reviewed;         162 AA.\nAC   Q8IKT4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 123.\nDE   RecName: Full=Iron-sulfur cluster assembly protein IscU {ECO:0000305};\nDE            Short=PfIscU {ECO:0000303|PubMed:34032321};\nGN   Name=IscU {ECO:0000305};\nGN   ORFNames=PF3D7_1454500 {ECO:0000312|EMBL:CZU00240.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Iron-sulfur cluster assembly protein IscU {ECO:0000305};\nDE            Short=PfIscU {ECO:0000303|PubMed:34032321};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, COFACTOR, SUBUNIT, INTERACTION WITH ISCS, AND SUBCELLULAR\nRP   LOCATION.\nRX   PubMed=34032321; DOI=10.1111/mmi.14735;\nRA   Sadik M., Afsar M., Ramachandran R., Habib S.;\nRT   \"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the\nRT   Plasmodium falciparum mitochondrion.\";\nRL   Mol. Microbiol. 116:606-623(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;\nCC         Evidence={ECO:0000269|PubMed:34032321};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 160. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
