# cofactor_0032

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0032.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — heme

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNDFVFSDIPDILKPMASVEFDDPLTKATGDVLNWTLWLIRNFPALSNIIMRLPSSLVSIVTSSFEGANQMFQVTTSTHNLYSASLPTHATKQIISKLVEHEKTHIGPKNKDCVVQRLLNAHRDSESKISIPTPDATVRSEAIGFTLAGTADPPNILALGTFMAARDPEMQEGLYKELRAVWPDLRSPVPSYNLLHQLPLLRGVVKESIRFTHGVATGPARLVGAGGARIGGYNVPAKASLAVVAAPSYFVHMDETVFSEPEKFEPRRWADNDYSKSLVAFSRGRRMCPAEQFHVEPYETTSVPRSEERG

[Multiple Choices]
A. heme
B. Mg(2+)
C. Cu(2+)
D. Co(2+)
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

> The sequence-matched UniProt record identifies the protein as a cytochrome P450 monooxygenase and annotates heme as its cofactor. The cofactor annotation is transferred by similarity rather than presented as a direct experimental measurement, but it is consistent with the established heme-thiolate chemistry of cytochrome P450 enzymes.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can recognize or infer a cytochrome P450-like enzyme from transferable sequence-family features. Cytochrome P450 monooxygenases use heme as their catalytic cofactor, distinguishing heme from the offered Mg(2+), Cu(2+), and Co(2+) choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer follows from family-level knowledge about P450 enzymes and their conserved heme-dependent catalytic mechanism; it does not require recalling this exact protein's database entry. The reviewer-only annotation corroborates the inference but is not needed to make it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Heme is the meaningful choice for a cytochrome P450 enzyme among these alternatives.


### Important caveats

- The supplied evidence supports the annotation through similarity transfer; it does not establish that heme binding or catalytic activity was experimentally measured for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can recognize or infer a cytochrome P450-like enzyme from transferable sequence-family features. Cytochrome P450 monooxygenases use heme as their catalytic cofactor, distinguishing heme from the offered Mg(2+), Cu(2+), and Co(2+) choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer follows from family-level knowledge about P450 enzymes and their conserved heme-dependent catalytic mechanism; it does not require recalling this exact protein's database entry. The reviewer-only annotation corroborates the inference but is not needed to make it."
  },
  "case_id": "cofactor_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as a cytochrome P450 monooxygenase and annotates heme as its cofactor. The cofactor annotation is transferred by similarity rather than presented as a direct experimental measurement, but it is consistent with the established heme-thiolate chemistry of cytochrome P450 enzymes."
  },
  "important_caveats": [
    "The supplied evidence supports the annotation through similarity transfer; it does not establish that heme binding or catalytic activity was experimentally measured for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Heme is the meaningful choice for a cytochrome P450 enzyme among these alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as a cytochrome P450 monooxygenase and annotates heme as its cofactor. The cofactor annotation is transferred by similarity rather than presented as a direct experimental measurement, but it is consistent with the established heme-thiolate chemistry of cytochrome P450 enzymes.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can recognize or infer a cytochrome P450-like enzyme from transferable sequence-family features. Cytochrome P450 monooxygenases use heme as their catalytic cofactor, distinguishing heme from the offered Mg(2+), Cu(2+), and Co(2+) choices.",
    "missing_item_specific_fact": "",
    "reason": "The answer follows from family-level knowledge about P450 enzymes and their conserved heme-dependent catalytic mechanism; it does not require recalling this exact protein's database entry. The reviewer-only annotation corroborates the inference but is not needed to make it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Heme is the meaningful choice for a cytochrome P450 enzyme among these alternatives."
  },
  "important_caveats": [
    "The supplied evidence supports the annotation through similarity transfer; it does not establish that heme binding or catalytic activity was experimentally measured for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation identifies this protein as 'Cytochrome P450 monooxygenase ppzG' and explicitly lists heme (CHEBI:30413) as the cofactor. The evidence code is ECO:0000250 (inferred by similarity to P04798, a well-characterized P450), which is a computational transfer. However, this transfer is exceptionally well-grounded because heme is the universal, defining prosthetic group of ALL cytochrome P450 enzymes — it is the iron-containing porphyrin that performs the oxygen activation chemistry. The annotation is therefore strongly supported by the defining biochemistry of the P450 superfamily.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable cytochrome P450 signature motifs: (1) the heme-binding motif FxxGxxxC is present near the C-terminus as 'FSRGRRMC' (F-S-R-G-R-R-M-C), where the conserved Cys coordinates the heme iron; (2) the FGAG/GAGG substrate-access motif appears as 'GAGGARIGG'; (3) the overall domain architecture (N-terminal hydrophobic segment, core P450 fold, C-terminal heme-binding region) is consistent with a fungal P450. A knowledgeable model recognizing these features would apply the universal rule of the P450 superfamily: every cytochrome P450 enzyme uses heme (an iron-protoporphyrin IX) as its obligate prosthetic group for catalyzing monooxygenation. None of the distractors (Mg²⁺, Cu²⁺, Co²⁺) are cofactors of any P450 enzyme — Mg²⁺ is typical of kinases/polymerases, Cu²⁺ of multicopper oxidases/SODs, Co²⁺ of adenosylcobalamin-dependent enzymes. The family-level inference from P450 sequence signatures to heme is textbook biochemistry and does not require knowledge of this specific protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of P450 family sequence motifs (FxxGxxxC heme-ligating Cys, FGAG motif, overall fold architecture) combined with the universally known fact that all cytochrome P450 enzymes require heme provides a concrete, transferable inference that cleanly distinguishes heme from the metal-ion distractors. No protein-specific annotation or measurement is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The P450 superfamily is universally and unambiguously defined by its heme prosthetic group. None of the alternative choices (Mg²⁺, Cu²⁺, Co²⁺) correspond to any known P450 cofactor. The sequence features clearly indicate a P450, leaving no legitimate ambiguity among the options.


### Important caveats

- The UniProt cofactor annotation uses evidence code ECO:0000250 (similarity-based transfer from P04798), not direct experimental measurement on this specific protein. However, this transfer is essentially equivalent to experimental certainty because heme is the invariant defining cofactor of the entire P450 superfamily.
- The protein is 310 amino acids, which is shorter than typical P450s (400-550 AA), suggesting it may be a truncated or atypical fungal P450, but the core catalytic domain and heme-binding motifs are intact.
- The reviewer-only source evidence (accession, organism, protein name) was not available to the evaluated model; the reasoning above relies solely on sequence motif recognition and general P450 family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable cytochrome P450 signature motifs: (1) the heme-binding motif FxxGxxxC is present near the C-terminus as 'FSRGRRMC' (F-S-R-G-R-R-M-C), where the conserved Cys coordinates the heme iron; (2) the FGAG/GAGG substrate-access motif appears as 'GAGGARIGG'; (3) the overall domain architecture (N-terminal hydrophobic segment, core P450 fold, C-terminal heme-binding region) is consistent with a fungal P450. A knowledgeable model recognizing these features would apply the universal rule of the P450 superfamily: every cytochrome P450 enzyme uses heme (an iron-protoporphyrin IX) as its obligate prosthetic group for catalyzing monooxygenation. None of the distractors (Mg²⁺, Cu²⁺, Co²⁺) are cofactors of any P450 enzyme — Mg²⁺ is typical of kinases/polymerases, Cu²⁺ of multicopper oxidases/SODs, Co²⁺ of adenosylcobalamin-dependent enzymes. The family-level inference from P450 sequence signatures to heme is textbook biochemistry and does not require knowledge of this specific protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of P450 family sequence motifs (FxxGxxxC heme-ligating Cys, FGAG motif, overall fold architecture) combined with the universally known fact that all cytochrome P450 enzymes require heme provides a concrete, transferable inference that cleanly distinguishes heme from the metal-ion distractors. No protein-specific annotation or measurement is needed."
  },
  "case_id": "cofactor_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation identifies this protein as 'Cytochrome P450 monooxygenase ppzG' and explicitly lists heme (CHEBI:30413) as the cofactor. The evidence code is ECO:0000250 (inferred by similarity to P04798, a well-characterized P450), which is a computational transfer. However, this transfer is exceptionally well-grounded because heme is the universal, defining prosthetic group of ALL cytochrome P450 enzymes — it is the iron-containing porphyrin that performs the oxygen activation chemistry. The annotation is therefore strongly supported by the defining biochemistry of the P450 superfamily."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000250 (similarity-based transfer from P04798), not direct experimental measurement on this specific protein. However, this transfer is essentially equivalent to experimental certainty because heme is the invariant defining cofactor of the entire P450 superfamily.",
    "The protein is 310 amino acids, which is shorter than typical P450s (400-550 AA), suggesting it may be a truncated or atypical fungal P450, but the core catalytic domain and heme-binding motifs are intact.",
    "The reviewer-only source evidence (accession, organism, protein name) was not available to the evaluated model; the reasoning above relies solely on sequence motif recognition and general P450 family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The P450 superfamily is universally and unambiguously defined by its heme prosthetic group. None of the alternative choices (Mg²⁺, Cu²⁺, Co²⁺) correspond to any known P450 cofactor. The sequence features clearly indicate a P450, leaving no legitimate ambiguity among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation identifies this protein as 'Cytochrome P450 monooxygenase ppzG' and explicitly lists heme (CHEBI:30413) as the cofactor. The evidence code is ECO:0000250 (inferred by similarity to P04798, a well-characterized P450), which is a computational transfer. However, this transfer is exceptionally well-grounded because heme is the universal, defining prosthetic group of ALL cytochrome P450 enzymes — it is the iron-containing porphyrin that performs the oxygen activation chemistry. The annotation is therefore strongly supported by the defining biochemistry of the P450 superfamily.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable cytochrome P450 signature motifs: (1) the heme-binding motif FxxGxxxC is present near the C-terminus as 'FSRGRRMC' (F-S-R-G-R-R-M-C), where the conserved Cys coordinates the heme iron; (2) the FGAG/GAGG substrate-access motif appears as 'GAGGARIGG'; (3) the overall domain architecture (N-terminal hydrophobic segment, core P450 fold, C-terminal heme-binding region) is consistent with a fungal P450. A knowledgeable model recognizing these features would apply the universal rule of the P450 superfamily: every cytochrome P450 enzyme uses heme (an iron-protoporphyrin IX) as its obligate prosthetic group for catalyzing monooxygenation. None of the distractors (Mg²⁺, Cu²⁺, Co²⁺) are cofactors of any P450 enzyme — Mg²⁺ is typical of kinases/polymerases, Cu²⁺ of multicopper oxidases/SODs, Co²⁺ of adenosylcobalamin-dependent enzymes. The family-level inference from P450 sequence signatures to heme is textbook biochemistry and does not require knowledge of this specific protein's record.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of P450 family sequence motifs (FxxGxxxC heme-ligating Cys, FGAG motif, overall fold architecture) combined with the universally known fact that all cytochrome P450 enzymes require heme provides a concrete, transferable inference that cleanly distinguishes heme from the metal-ion distractors. No protein-specific annotation or measurement is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The P450 superfamily is universally and unambiguously defined by its heme prosthetic group. None of the alternative choices (Mg²⁺, Cu²⁺, Co²⁺) correspond to any known P450 cofactor. The sequence features clearly indicate a P450, leaving no legitimate ambiguity among the options."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000250 (similarity-based transfer from P04798), not direct experimental measurement on this specific protein. However, this transfer is essentially equivalent to experimental certainty because heme is the invariant defining cofactor of the entire P450 superfamily.",
    "The protein is 310 amino acids, which is shorter than typical P450s (400-550 AA), suggesting it may be a truncated or atypical fungal P450, but the core catalytic domain and heme-binding motifs are intact.",
    "The reviewer-only source evidence (accession, organism, protein name) was not available to the evaluated model; the reasoning above relies solely on sequence motif recognition and general P450 family knowledge."
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
  "benchmark_sequence_length": 310,
  "benchmark_sequence_sha256": "f43c07841a6175c125bba9ab5474c67719d466b07295c69b50449f964246f483",
  "current_entry_audit": {
    "entryVersion": 24,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9c7ce8707b3aae4d0d2f246c70997c160f3bd908218c3af7dd5563094728f4d3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 310,
  "current_source_sequence_sha256": "f43c07841a6175c125bba9ab5474c67719d466b07295c69b50449f964246f483",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 23,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A455ZM03",
  "selected_historical_entry_version": 23,
  "selected_historical_record_sha256": "c85f65dda2bcec72e8a4991649c1744c4a28fefbb47fb8a716a368c7f84e8a6b",
  "selected_historical_source_sequence_length": 310,
  "selected_historical_source_sequence_sha256": "f43c07841a6175c125bba9ab5474c67719d466b07295c69b50449f964246f483",
  "selected_historical_version": {
    "accession": "A0A455ZM03",
    "database": "Swiss-Prot",
    "entryVersion": 23,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PPZG_METMF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZM03.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A455ZM03\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:17.796999+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c7ce8707b3aae4d0d2f246c70997c160f3bd908218c3af7dd5563094728f4d3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZM03.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZM03.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":24,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:17.796999+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c7ce8707b3aae4d0d2f246c70997c160f3bd908218c3af7dd5563094728f4d3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZM03.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZM03.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"DAC76723.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:17.796999+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c7ce8707b3aae4d0d2f246c70997c160f3bd908218c3af7dd5563094728f4d3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZM03.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZM03.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein G\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase ppzG\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:17.796999+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c7ce8707b3aae4d0d2f246c70997c160f3bd908218c3af7dd5563094728f4d3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZM03.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZM03.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P04798\",\"source\":\"UniProtKB\"}],\"name\":\"heme\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:17.796999+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c7ce8707b3aae4d0d2f246c70997c160f3bd908218c3af7dd5563094728f4d3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZM03.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZM03.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:17.796999+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c7ce8707b3aae4d0d2f246c70997c160f3bd908218c3af7dd5563094728f4d3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZM03.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZM03?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H1",
  "excerpt": "ID   PPZG_METMF              Reviewed;         310 AA.\nAC   A0A455ZM03;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 23.\nDE   RecName: Full=Cytochrome P450 monooxygenase ppzG {ECO:0000303|PubMed:30452111};\nDE            EC=1.-.-.- {ECO:0000305|PubMed:30452111};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein G {ECO:0000303|PubMed:30452111};\nGN   Name=ppzG;\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143 {ECO:0000312|EMBL:DAC76723.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:20.024616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c85f65dda2bcec72e8a4991649c1744c4a28fefbb47fb8a716a368c7f84e8a6b",
  "url": "https://rest.uniprot.org/unisave/A0A455ZM03?format=txt&versions=23"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZM03?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cytochrome P450 monooxygenase ppzG {ECO:0000303|PubMed:30452111};\nDE            EC=1.-.-.- {ECO:0000305|PubMed:30452111};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein G {ECO:0000303|PubMed:30452111};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:20.024616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c85f65dda2bcec72e8a4991649c1744c4a28fefbb47fb8a716a368c7f84e8a6b",
  "url": "https://rest.uniprot.org/unisave/A0A455ZM03?format=txt&versions=23"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZM03?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:20.024616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c85f65dda2bcec72e8a4991649c1744c4a28fefbb47fb8a716a368c7f84e8a6b",
  "url": "https://rest.uniprot.org/unisave/A0A455ZM03?format=txt&versions=23"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZM03?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=heme; Xref=ChEBI:CHEBI:30413;\nCC         Evidence={ECO:0000250|UniProtKB:P04798};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:20.024616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c85f65dda2bcec72e8a4991649c1744c4a28fefbb47fb8a716a368c7f84e8a6b",
  "url": "https://rest.uniprot.org/unisave/A0A455ZM03?format=txt&versions=23"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
