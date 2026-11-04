# GO_cellular_component_0032

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0032.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDGYAVRAEAMEKRYGEKRALDGFDLAVGEGTVHGLLGPNGAGKTTAVRILSTLVRLDGGRATVAGLDVARQPREVRARIGLTGQYAAVDEVLTGRQNLEMFGRLFHLGGRRARLRATELLEQFDLTDAGDRGVGKYSGGMRRRLDLAASMILAPAVLFLDEPTTGLDPRSRGEVWESVRALVAGGTTVLLTTQYLEEADKLASRITVIDQGRAIADDTPDGLKNLVGGDRIEVVVAERAEIPRVVKVVARVADGEPEADETESRVHAPVTDRVTALTEVARTLQDEGVRVEDIGLRRPSLDDVFLRLTGHRTENTEAKEAA

[Multiple Choices]
A. food vacuole
B. ATP-binding cassette (ABC) transporter complex
C. plasma membrane
D. replisome
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates the protein to the cell membrane and to GO:0005886, plasma membrane. This supports C as a database annotation, although the location is transferred by similarity rather than established here by direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a P-loop ATP-binding motif (GPNGAGKTT) and lacks an obvious long transmembrane segment, which is consistent with a soluble ATPase subunit associating with a membrane transporter. Transferable knowledge of transporter ATPases therefore favors a membrane-associated location over a food vacuole or replisome. It also makes the ABC transporter complex option plausible, so the inference does not uniquely separate B from C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence and topology reasoning gives a meaningful basis for choosing membrane-associated options over A and D. It does not establish whether the intended primary component is the membrane location or the transporter complex.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> An ATPase subunit associated with a membrane transporter can be described as residing at the plasma membrane and as belonging to an ABC transporter complex. The question does not specify whether it seeks physical locale or complex membership.


### Important caveats

- The supplied source supports C through database annotations based on similarity; it is not direct experimental localization evidence.
- The sequence-based family inference is probabilistic, and the original input does not resolve the B-versus-C distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a P-loop ATP-binding motif (GPNGAGKTT) and lacks an obvious long transmembrane segment, which is consistent with a soluble ATPase subunit associating with a membrane transporter. Transferable knowledge of transporter ATPases therefore favors a membrane-associated location over a food vacuole or replisome. It also makes the ABC transporter complex option plausible, so the inference does not uniquely separate B from C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and topology reasoning gives a meaningful basis for choosing membrane-associated options over A and D. It does not establish whether the intended primary component is the membrane location or the transporter complex."
  },
  "case_id": "GO_cellular_component_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the cell membrane and to GO:0005886, plasma membrane. This supports C as a database annotation, although the location is transferred by similarity rather than established here by direct experimental evidence."
  },
  "important_caveats": [
    "The supplied source supports C through database annotations based on similarity; it is not direct experimental localization evidence.",
    "The sequence-based family inference is probabilistic, and the original input does not resolve the B-versus-C distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "An ATPase subunit associated with a membrane transporter can be described as residing at the plasma membrane and as belonging to an ABC transporter complex. The question does not specify whether it seeks physical locale or complex membership."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the cell membrane and to GO:0005886, plasma membrane. This supports C as a database annotation, although the location is transferred by similarity rather than established here by direct experimental evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a P-loop ATP-binding motif (GPNGAGKTT) and lacks an obvious long transmembrane segment, which is consistent with a soluble ATPase subunit associating with a membrane transporter. Transferable knowledge of transporter ATPases therefore favors a membrane-associated location over a food vacuole or replisome. It also makes the ABC transporter complex option plausible, so the inference does not uniquely separate B from C.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and topology reasoning gives a meaningful basis for choosing membrane-associated options over A and D. It does not establish whether the intended primary component is the membrane location or the transporter complex."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "An ATPase subunit associated with a membrane transporter can be described as residing at the plasma membrane and as belonging to an ABC transporter complex. The question does not specify whether it seeks physical locale or complex membership."
  },
  "important_caveats": [
    "The supplied source supports C through database annotations based on similarity; it is not direct experimental localization evidence.",
    "The sequence-based family inference is probabilistic, and the original input does not resolve the B-versus-C distinction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (P0DXU5, DrrA2 from Streptomyces coeruleorubidus) assigns GO:0005886 (plasma membrane) as the cellular component (evidence C6, H4). The subcellular location is annotated as 'Cell membrane; Peripheral membrane protein; Cytoplasmic side' (evidence C5, H3). GO:0005886 has 'plasma membrane' as its name and 'cell membrane' as an EXACT synonym (evidence GO1). The sequence matches the UniProt entry exactly.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an unmistakable ABC transporter nucleotide-binding domain (NBD) signature: the Walker A motif 'GEGTVHGLLGPNGAGKTT' (P-loop) and the ABC signature motif region 'DEPTTGLDPRSRG'. This immediately eliminates A (food vacuole, a parasite-specific organelle irrelevant to bacteria) and D (replisome, DNA replication machinery). Between B (ABC transporter complex) and C (plasma membrane): the question asks for the 'primary Cellular Component where a protein is located.' Transferable knowledge about ABC transporter architecture indicates that the NBD is a soluble/peripheral ATPase domain that associates with the cytoplasmic face of the membrane—it is not itself a transmembrane protein. GO:0043190 (ABC transporter complex) describes the assembled multi-subunit complex including transmembrane permease domains encoded by separate proteins, whereas the physical location of the NBD subunit is the plasma membrane (cytoplasmic side). A knowledgeable model can reason: Walker A → ABC NBD → peripheral membrane protein → located at plasma membrane (C), rather than being 'the complex' itself (B).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Walker A motif and ABC signature are highly recognizable sequence features transferable across the ABC superfamily. The architectural principle that NBDs are peripheral membrane proteins at the plasma membrane is well-established across bacterial ABC exporters. The distinction between 'location' (plasma membrane) and 'complex membership' (ABC transporter complex) is a legitimate biological reasoning step, though B is a somewhat defensible distractor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> GO:0043190 (ABC transporter complex) is in the cellular_component namespace and the protein is unambiguously an ABC transporter NBD. A model could argue the protein's 'cellular component' is the ABC transporter complex it belongs to. However, the question phrasing 'where a protein is located' favors a physical location (plasma membrane) over a complex name, and the NBD is a peripheral membrane protein rather than a transmembrane component of the full complex. The distinction is subtle but the question wording and the peripheral-membrane nature of NBDs favor C.


### Important caveats

- The GO annotation for this protein is ISS (Inferred from Sequence Similarity) to P32010, not direct experimental evidence for this exact protein.
- The GO:0005886 annotation uses IEA:UniProtKB-SubCell in the historical record and ISS:UniProtKB in the current record, indicating computational transfer rather than direct measurement.
- Option B (ABC transporter complex) is a legitimate cellular_component GO term and the protein is genuinely part of such a complex, making B a non-trivial distractor.
- The organism (Streptomyces coeruleorubidus) is not stated in the original user input; the bacterial context must be inferred from sequence composition or general knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an unmistakable ABC transporter nucleotide-binding domain (NBD) signature: the Walker A motif 'GEGTVHGLLGPNGAGKTT' (P-loop) and the ABC signature motif region 'DEPTTGLDPRSRG'. This immediately eliminates A (food vacuole, a parasite-specific organelle irrelevant to bacteria) and D (replisome, DNA replication machinery). Between B (ABC transporter complex) and C (plasma membrane): the question asks for the 'primary Cellular Component where a protein is located.' Transferable knowledge about ABC transporter architecture indicates that the NBD is a soluble/peripheral ATPase domain that associates with the cytoplasmic face of the membrane—it is not itself a transmembrane protein. GO:0043190 (ABC transporter complex) describes the assembled multi-subunit complex including transmembrane permease domains encoded by separate proteins, whereas the physical location of the NBD subunit is the plasma membrane (cytoplasmic side). A knowledgeable model can reason: Walker A → ABC NBD → peripheral membrane protein → located at plasma membrane (C), rather than being 'the complex' itself (B).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Walker A motif and ABC signature are highly recognizable sequence features transferable across the ABC superfamily. The architectural principle that NBDs are peripheral membrane proteins at the plasma membrane is well-established across bacterial ABC exporters. The distinction between 'location' (plasma membrane) and 'complex membership' (ABC transporter complex) is a legitimate biological reasoning step, though B is a somewhat defensible distractor."
  },
  "case_id": "GO_cellular_component_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (P0DXU5, DrrA2 from Streptomyces coeruleorubidus) assigns GO:0005886 (plasma membrane) as the cellular component (evidence C6, H4). The subcellular location is annotated as 'Cell membrane; Peripheral membrane protein; Cytoplasmic side' (evidence C5, H3). GO:0005886 has 'plasma membrane' as its name and 'cell membrane' as an EXACT synonym (evidence GO1). The sequence matches the UniProt entry exactly."
  },
  "important_caveats": [
    "The GO annotation for this protein is ISS (Inferred from Sequence Similarity) to P32010, not direct experimental evidence for this exact protein.",
    "The GO:0005886 annotation uses IEA:UniProtKB-SubCell in the historical record and ISS:UniProtKB in the current record, indicating computational transfer rather than direct measurement.",
    "Option B (ABC transporter complex) is a legitimate cellular_component GO term and the protein is genuinely part of such a complex, making B a non-trivial distractor.",
    "The organism (Streptomyces coeruleorubidus) is not stated in the original user input; the bacterial context must be inferred from sequence composition or general knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "GO:0043190 (ABC transporter complex) is in the cellular_component namespace and the protein is unambiguously an ABC transporter NBD. A model could argue the protein's 'cellular component' is the ABC transporter complex it belongs to. However, the question phrasing 'where a protein is located' favors a physical location (plasma membrane) over a complex name, and the NBD is a peripheral membrane protein rather than a transmembrane component of the full complex. The distinction is subtle but the question wording and the peripheral-membrane nature of NBDs favor C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (P0DXU5, DrrA2 from Streptomyces coeruleorubidus) assigns GO:0005886 (plasma membrane) as the cellular component (evidence C6, H4). The subcellular location is annotated as 'Cell membrane; Peripheral membrane protein; Cytoplasmic side' (evidence C5, H3). GO:0005886 has 'plasma membrane' as its name and 'cell membrane' as an EXACT synonym (evidence GO1). The sequence matches the UniProt entry exactly.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an unmistakable ABC transporter nucleotide-binding domain (NBD) signature: the Walker A motif 'GEGTVHGLLGPNGAGKTT' (P-loop) and the ABC signature motif region 'DEPTTGLDPRSRG'. This immediately eliminates A (food vacuole, a parasite-specific organelle irrelevant to bacteria) and D (replisome, DNA replication machinery). Between B (ABC transporter complex) and C (plasma membrane): the question asks for the 'primary Cellular Component where a protein is located.' Transferable knowledge about ABC transporter architecture indicates that the NBD is a soluble/peripheral ATPase domain that associates with the cytoplasmic face of the membrane—it is not itself a transmembrane protein. GO:0043190 (ABC transporter complex) describes the assembled multi-subunit complex including transmembrane permease domains encoded by separate proteins, whereas the physical location of the NBD subunit is the plasma membrane (cytoplasmic side). A knowledgeable model can reason: Walker A → ABC NBD → peripheral membrane protein → located at plasma membrane (C), rather than being 'the complex' itself (B).",
    "missing_item_specific_fact": "",
    "reason": "The Walker A motif and ABC signature are highly recognizable sequence features transferable across the ABC superfamily. The architectural principle that NBDs are peripheral membrane proteins at the plasma membrane is well-established across bacterial ABC exporters. The distinction between 'location' (plasma membrane) and 'complex membership' (ABC transporter complex) is a legitimate biological reasoning step, though B is a somewhat defensible distractor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "GO:0043190 (ABC transporter complex) is in the cellular_component namespace and the protein is unambiguously an ABC transporter NBD. A model could argue the protein's 'cellular component' is the ABC transporter complex it belongs to. However, the question phrasing 'where a protein is located' favors a physical location (plasma membrane) over a complex name, and the NBD is a peripheral membrane protein rather than a transmembrane component of the full complex. The distinction is subtle but the question wording and the peripheral-membrane nature of NBDs favor C."
  },
  "important_caveats": [
    "The GO annotation for this protein is ISS (Inferred from Sequence Similarity) to P32010, not direct experimental evidence for this exact protein.",
    "The GO:0005886 annotation uses IEA:UniProtKB-SubCell in the historical record and ISS:UniProtKB in the current record, indicating computational transfer rather than direct measurement.",
    "Option B (ABC transporter complex) is a legitimate cellular_component GO term and the protein is genuinely part of such a complex, making B a non-trivial distractor.",
    "The organism (Streptomyces coeruleorubidus) is not stated in the original user input; the bacterial context must be inferred from sequence composition or general knowledge."
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
  "benchmark_sequence_length": 322,
  "benchmark_sequence_sha256": "2ca962384eab52f63840ebe294f20a563ed32fb8966a77e2f1c8c7c091f6e9f3",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 322,
  "current_source_sequence_sha256": "2ca962384eab52f63840ebe294f20a563ed32fb8966a77e2f1c8c7c091f6e9f3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXU5",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425",
  "selected_historical_source_sequence_length": 322,
  "selected_historical_source_sequence_sha256": "2ca962384eab52f63840ebe294f20a563ed32fb8966a77e2f1c8c7c091f6e9f3",
  "selected_historical_version": {
    "accession": "P0DXU5",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRA2_STRC4",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"value\":\"7.6.2.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ATP-binding protein DrrA2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32010\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"orientation\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32010\",\"source\":\"UniProtKB\"}],\"id\":\"SL-9910\",\"value\":\"Cytoplasmic side\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32010\",\"source\":\"UniProtKB\"}],\"id\":\"SL-9903\",\"value\":\"Peripheral membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Dong J.\",\"Ning J.\",\"Tian Y.\",\"Li H.\",\"Chen H.\",\"Guan W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39375957\"},{\"database\":\"DOI\",\"id\":\"10.1111/1751-7915.70023\"}],\"citationType\":\"journal article\",\"firstPage\":\"e70023\",\"id\":\"39375957\",\"journal\":\"Microb. Biotechnol.\",\"lastPage\":\"e70023\",\"publicationDate\":\"2024\",\"title\":\"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.\",\"volume\":\"17\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION IN DAUNORUBICIN EFFLUX\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRA2_STRC4             Reviewed;         322 AA.\nAC   P0DXU5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA2 {ECO:0000305};\nDE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};\nGN   Name=drrA2 {ECO:0000303|PubMed:39375957};\nGN   ORFNames=R5U08_15995 {ECO:0000312|EMBL:WOT35541.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.836268+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425",
  "url": "https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.836268+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425",
  "url": "https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P32010};\nCC       Peripheral membrane protein {ECO:0000250|UniProtKB:P32010}; Cytoplasmic\nCC       side {ECO:0000250|UniProtKB:P32010}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.836268+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425",
  "url": "https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.836268+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425",
  "url": "https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60420-60454",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0020020\nname: food vacuole\nnamespace: cellular_component\nalt_id: GO:0005772\ndef: \"Vacuole within a parasite used for digestion of the host cell cytoplasm. An example of this component is found in the Apicomplexa.\" [GOC:mb]\nsynonym: \"digestive vacuole\" EXACT []\nis_a: GO:0032010 ! phagolysosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020020",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155270-155278",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0030894\nname: replisome\nnamespace: cellular_component\ndef: \"A multi-component enzymatic machine at the replication fork which mediates DNA replication. Includes DNA primase, one or more DNA polymerases, DNA helicases, and other proteins.\" [GOC:mah, GOC:vw]\nsubset: goslim_pir\nsynonym: \"DNA synthesome complex\" RELATED [CORUM:1001]\nsynonym: \"RC complex\" RELATED [CORUM:309, PMID:12006500]\nsynonym: \"replication-competent complex\" RELATED [CORUM:309, PMID:12006500]\nxref: Wikipedia:Replisome\nis_a: GO:0032993 ! protein-DNA complex\nrelationship: part_of GO:0005657 ! replication fork\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030894",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 171246-171258",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0043190\nname: ATP-binding cassette (ABC) transporter complex\nnamespace: cellular_component\nalt_id: GO:0043191\nalt_id: GO:0043192\ndef: \"A complex for the transport of metabolites into and out of the cell, typically comprised of four domains; two membrane-associated domains and two ATP-binding domains at the intracellular face of the membrane, that form a central pore through the plasma membrane. Each of the four core domains may be encoded as a separate polypeptide or the domains can be fused in any one of a number of ways into multidomain polypeptides. In Bacteria and Archaebacteria, ABC transporters also include substrate binding proteins to bind substrate external to the cytoplasm and deliver it to the transporter.\" [GOC:jl, GOC:mtg_sensu, PMID:11421269, PMID:15111107]\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"ABC-type efflux permease complex\" NARROW []\nsynonym: \"ABC-type efflux porter complex\" NARROW []\nsynonym: \"ABC-type uptake permease complex\" NARROW []\nsynonym: \"mating pheromone exporter\" NARROW []\nis_a: GO:0098533 ! ATPase dependent transmembrane transport complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043190",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 244782-244797",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
