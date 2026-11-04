# GO_cellular_component_0045

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0045.txt)

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
MNTQPTRAIETSGLVKVYNGTRAVDGLDLDVPAGLVYGILGPNGAGKSTTIRMLATLLRPDGGTARVFGHDVTSEPDTVRRRISVTGQYASVDEGLTGTENLVMMGRLQGYSWARARERAAELIDGFGLGDARDRLLKTYSGGMRRRLDIAASIVVTPDLLFLDEPTTGLDPRSRNQVWDIVRALVDAGTTVLLTTQYLDEADQLADRIAVIDHGRVIAEGTTGELKSSLGSNVLRLRLHDAQSRAEAERLLSAELGVTIHRDSDPTALSARIDDPRQGMRALAELSRTQLEVRSFSLGQSSLDEVFLALTGHPADDRSTEEAAEEEKVA

[Multiple Choices]
A. membrane
B. phosphopantothenoylcysteine decarboxylase complex
C. plasma membrane
D. axon
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

> The sequence-matched UniProt record annotates the protein to the cell membrane as a peripheral membrane protein on the cytoplasmic side, and assigns plasma membrane by computational evidence. This supports C, though the localization is transferred/inferred rather than shown here by direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a P-loop nucleotide-binding motif (GPNGAGKST) and a soluble ATPase-like architecture, consistent with an ATP-binding component of a transporter rather than a membrane-spanning protein itself. Transferable knowledge of bacterial transporter ATPases supports association with the cell membrane, which corresponds to plasma membrane in the offered GO choices; axon and the phosphopantothenoylcysteine decarboxylase complex are poor fits.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features and the usual association of transporter ATPase components with the cell membrane provide a meaningful, though not certain, basis for choosing C without knowing this protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A is a broader location that includes C: the GO plasma membrane term is a child of membrane. Thus both describe the inferred location, although C is the more specific choice.


### Important caveats

- The supplied annotation evidence is computational or transferred, not direct experimental localization evidence.
- The sequence supports a transporter-associated ATPase inference but does not alone prove its exact cellular localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a P-loop nucleotide-binding motif (GPNGAGKST) and a soluble ATPase-like architecture, consistent with an ATP-binding component of a transporter rather than a membrane-spanning protein itself. Transferable knowledge of bacterial transporter ATPases supports association with the cell membrane, which corresponds to plasma membrane in the offered GO choices; axon and the phosphopantothenoylcysteine decarboxylase complex are poor fits.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features and the usual association of transporter ATPase components with the cell membrane provide a meaningful, though not certain, basis for choosing C without knowing this protein's recorded annotation."
  },
  "case_id": "GO_cellular_component_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the cell membrane as a peripheral membrane protein on the cytoplasmic side, and assigns plasma membrane by computational evidence. This supports C, though the localization is transferred/inferred rather than shown here by direct experimental evidence."
  },
  "important_caveats": [
    "The supplied annotation evidence is computational or transferred, not direct experimental localization evidence.",
    "The sequence supports a transporter-associated ATPase inference but does not alone prove its exact cellular localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A is a broader location that includes C: the GO plasma membrane term is a child of membrane. Thus both describe the inferred location, although C is the more specific choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the cell membrane as a peripheral membrane protein on the cytoplasmic side, and assigns plasma membrane by computational evidence. This supports C, though the localization is transferred/inferred rather than shown here by direct experimental evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a P-loop nucleotide-binding motif (GPNGAGKST) and a soluble ATPase-like architecture, consistent with an ATP-binding component of a transporter rather than a membrane-spanning protein itself. Transferable knowledge of bacterial transporter ATPases supports association with the cell membrane, which corresponds to plasma membrane in the offered GO choices; axon and the phosphopantothenoylcysteine decarboxylase complex are poor fits.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features and the usual association of transporter ATPase components with the cell membrane provide a meaningful, though not certain, basis for choosing C without knowing this protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A is a broader location that includes C: the GO plasma membrane term is a child of membrane. Thus both describe the inferred location, although C is the more specific choice."
  },
  "important_caveats": [
    "The supplied annotation evidence is computational or transferred, not direct experimental localization evidence.",
    "The sequence supports a transporter-associated ATPase inference but does not alone prove its exact cellular localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5/H3) records 'Cell membrane; Peripheral membrane protein; Cytoplasmic side' with ISS evidence from P32010. The GO cross-reference (C6/H4) explicitly assigns GO:0005886 'C:plasma membrane'. The GO ontology (GO1) confirms 'cell membrane' is an EXACT synonym of 'plasma membrane' and 'bacterial inner membrane' is a NARROW synonym. Thus the database annotation directly supports the expected answer C. The evidence code is ISS (similarity-based, not experimental), but the annotation is present and consistent.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Walker A motif (GPNGAGKST, residues ~35-43) and an ABC signature-like region (LLFLDEPTT), identifying this as an ABC transporter nucleotide-binding domain (NBD). ABC NBDs are well-characterized as cytoplasmic domains that dock onto membrane-embedded transmembrane domains. The sequence lacks eukaryotic signal peptides, mitochondrial targeting sequences, or nuclear localization signals, and its composition is consistent with a bacterial protein. In bacteria, the only membrane compartment for ABC transporter association is the plasma membrane (inner membrane). The GO ontology confirms 'plasma membrane' (GO:0005886) has 'cell membrane' as EXACT synonym and 'bacterial inner membrane' as NARROW synonym. Option B (phosphopantothenoylcysteine decarboxylase complex) is a CoA-biosynthesis enzyme complex with no relation to ABC transporters. Option D (axon) is a eukaryotic neuronal structure irrelevant to a bacterium. Between A (membrane, GO:0016020) and C (plasma membrane, GO:0005886): the question asks for the 'primary' location, and GO annotation practice assigns the most specific applicable term. For a bacterial ABC NBD, the specific membrane is the plasma membrane. A knowledgeable model can recognize the ABC NBD family from motifs, recall that bacterial ABC transporters are plasma-membrane-associated, and select the more specific term C over the general parent term A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence motifs (Walker A, ABC signature) are directly readable and identify the protein family. Family-level knowledge of ABC transporter NBDs and their membrane association in bacteria, combined with the 'primary' qualifier favoring the most specific GO term, provides a concrete transferable inference distinguishing C from A, B, and D without needing the exact database record for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> GO:0005886 (plasma membrane) is_a GO:0016020 (membrane), so a protein at the plasma membrane is also at a membrane. Strictly, both A and C are true statements about the location. However, the question asks for the 'primary' cellular component, and GO convention assigns the most specific term. The distinction is one of specificity rather than correctness, making A a less precise but not factually incorrect choice. In a well-constructed benchmark, the 'primary' qualifier should resolve this toward C.


### Important caveats

- The GO annotation for this protein is ISS (Inferred from Sequence Similarity to P32010), not experimental evidence. The subcellular location is transferred by similarity, not directly measured.
- The protein is from Streptomyces coeruleorubidus (a bacterium). The GO term 'plasma membrane' encompasses 'cell membrane' (EXACT synonym) and 'bacterial inner membrane' (NARROW synonym), so the terminology is appropriate for bacteria.
- Option A (membrane, GO:0016020) is the parent of C (plasma membrane, GO:0005886). Both are technically true locations, but 'primary' in the question prompt favors the more specific annotation.
- The identity of the protein as DrrA1 and its association with daunorubicin efflux is reviewer-only information not available to the evaluated model; the model must rely on sequence motifs and family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Walker A motif (GPNGAGKST, residues ~35-43) and an ABC signature-like region (LLFLDEPTT), identifying this as an ABC transporter nucleotide-binding domain (NBD). ABC NBDs are well-characterized as cytoplasmic domains that dock onto membrane-embedded transmembrane domains. The sequence lacks eukaryotic signal peptides, mitochondrial targeting sequences, or nuclear localization signals, and its composition is consistent with a bacterial protein. In bacteria, the only membrane compartment for ABC transporter association is the plasma membrane (inner membrane). The GO ontology confirms 'plasma membrane' (GO:0005886) has 'cell membrane' as EXACT synonym and 'bacterial inner membrane' as NARROW synonym. Option B (phosphopantothenoylcysteine decarboxylase complex) is a CoA-biosynthesis enzyme complex with no relation to ABC transporters. Option D (axon) is a eukaryotic neuronal structure irrelevant to a bacterium. Between A (membrane, GO:0016020) and C (plasma membrane, GO:0005886): the question asks for the 'primary' location, and GO annotation practice assigns the most specific applicable term. For a bacterial ABC NBD, the specific membrane is the plasma membrane. A knowledgeable model can recognize the ABC NBD family from motifs, recall that bacterial ABC transporters are plasma-membrane-associated, and select the more specific term C over the general parent term A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence motifs (Walker A, ABC signature) are directly readable and identify the protein family. Family-level knowledge of ABC transporter NBDs and their membrane association in bacteria, combined with the 'primary' qualifier favoring the most specific GO term, provides a concrete transferable inference distinguishing C from A, B, and D without needing the exact database record for this protein."
  },
  "case_id": "GO_cellular_component_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H3) records 'Cell membrane; Peripheral membrane protein; Cytoplasmic side' with ISS evidence from P32010. The GO cross-reference (C6/H4) explicitly assigns GO:0005886 'C:plasma membrane'. The GO ontology (GO1) confirms 'cell membrane' is an EXACT synonym of 'plasma membrane' and 'bacterial inner membrane' is a NARROW synonym. Thus the database annotation directly supports the expected answer C. The evidence code is ISS (similarity-based, not experimental), but the annotation is present and consistent."
  },
  "important_caveats": [
    "The GO annotation for this protein is ISS (Inferred from Sequence Similarity to P32010), not experimental evidence. The subcellular location is transferred by similarity, not directly measured.",
    "The protein is from Streptomyces coeruleorubidus (a bacterium). The GO term 'plasma membrane' encompasses 'cell membrane' (EXACT synonym) and 'bacterial inner membrane' (NARROW synonym), so the terminology is appropriate for bacteria.",
    "Option A (membrane, GO:0016020) is the parent of C (plasma membrane, GO:0005886). Both are technically true locations, but 'primary' in the question prompt favors the more specific annotation.",
    "The identity of the protein as DrrA1 and its association with daunorubicin efflux is reviewer-only information not available to the evaluated model; the model must rely on sequence motifs and family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "GO:0005886 (plasma membrane) is_a GO:0016020 (membrane), so a protein at the plasma membrane is also at a membrane. Strictly, both A and C are true statements about the location. However, the question asks for the 'primary' cellular component, and GO convention assigns the most specific term. The distinction is one of specificity rather than correctness, making A a less precise but not factually incorrect choice. In a well-constructed benchmark, the 'primary' qualifier should resolve this toward C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H3) records 'Cell membrane; Peripheral membrane protein; Cytoplasmic side' with ISS evidence from P32010. The GO cross-reference (C6/H4) explicitly assigns GO:0005886 'C:plasma membrane'. The GO ontology (GO1) confirms 'cell membrane' is an EXACT synonym of 'plasma membrane' and 'bacterial inner membrane' is a NARROW synonym. Thus the database annotation directly supports the expected answer C. The evidence code is ISS (similarity-based, not experimental), but the annotation is present and consistent.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Walker A motif (GPNGAGKST, residues ~35-43) and an ABC signature-like region (LLFLDEPTT), identifying this as an ABC transporter nucleotide-binding domain (NBD). ABC NBDs are well-characterized as cytoplasmic domains that dock onto membrane-embedded transmembrane domains. The sequence lacks eukaryotic signal peptides, mitochondrial targeting sequences, or nuclear localization signals, and its composition is consistent with a bacterial protein. In bacteria, the only membrane compartment for ABC transporter association is the plasma membrane (inner membrane). The GO ontology confirms 'plasma membrane' (GO:0005886) has 'cell membrane' as EXACT synonym and 'bacterial inner membrane' as NARROW synonym. Option B (phosphopantothenoylcysteine decarboxylase complex) is a CoA-biosynthesis enzyme complex with no relation to ABC transporters. Option D (axon) is a eukaryotic neuronal structure irrelevant to a bacterium. Between A (membrane, GO:0016020) and C (plasma membrane, GO:0005886): the question asks for the 'primary' location, and GO annotation practice assigns the most specific applicable term. For a bacterial ABC NBD, the specific membrane is the plasma membrane. A knowledgeable model can recognize the ABC NBD family from motifs, recall that bacterial ABC transporters are plasma-membrane-associated, and select the more specific term C over the general parent term A.",
    "missing_item_specific_fact": "",
    "reason": "The sequence motifs (Walker A, ABC signature) are directly readable and identify the protein family. Family-level knowledge of ABC transporter NBDs and their membrane association in bacteria, combined with the 'primary' qualifier favoring the most specific GO term, provides a concrete transferable inference distinguishing C from A, B, and D without needing the exact database record for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "GO:0005886 (plasma membrane) is_a GO:0016020 (membrane), so a protein at the plasma membrane is also at a membrane. Strictly, both A and C are true statements about the location. However, the question asks for the 'primary' cellular component, and GO convention assigns the most specific term. The distinction is one of specificity rather than correctness, making A a less precise but not factually incorrect choice. In a well-constructed benchmark, the 'primary' qualifier should resolve this toward C."
  },
  "important_caveats": [
    "The GO annotation for this protein is ISS (Inferred from Sequence Similarity to P32010), not experimental evidence. The subcellular location is transferred by similarity, not directly measured.",
    "The protein is from Streptomyces coeruleorubidus (a bacterium). The GO term 'plasma membrane' encompasses 'cell membrane' (EXACT synonym) and 'bacterial inner membrane' (NARROW synonym), so the terminology is appropriate for bacteria.",
    "Option A (membrane, GO:0016020) is the parent of C (plasma membrane, GO:0005886). Both are technically true locations, but 'primary' in the question prompt favors the more specific annotation.",
    "The identity of the protein as DrrA1 and its association with daunorubicin efflux is reviewer-only information not available to the evaluated model; the model must rely on sequence motifs and family knowledge."
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
  "benchmark_sequence_length": 330,
  "benchmark_sequence_sha256": "ad2ea907ea45035c9658ce71d6525af775e5e2cb247a1245bff85cb9dce29966",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 330,
  "current_source_sequence_sha256": "ad2ea907ea45035c9658ce71d6525af775e5e2cb247a1245bff85cb9dce29966",
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
  "requested_accession": "P0DXG8",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111",
  "selected_historical_source_sequence_length": 330,
  "selected_historical_source_sequence_sha256": "ad2ea907ea45035c9658ce71d6525af775e5e2cb247a1245bff85cb9dce29966",
  "selected_historical_version": {
    "accession": "P0DXG8",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRA1_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXG8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"value\":\"7.6.2.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ATP-binding protein DrrA1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32010\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"orientation\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32010\",\"source\":\"UniProtKB\"}],\"id\":\"SL-9910\",\"value\":\"Cytoplasmic side\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32010\",\"source\":\"UniProtKB\"}],\"id\":\"SL-9903\",\"value\":\"Peripheral membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Dong J.\",\"Ning J.\",\"Tian Y.\",\"Li H.\",\"Chen H.\",\"Guan W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39375957\"},{\"database\":\"DOI\",\"id\":\"10.1111/1751-7915.70023\"}],\"citationType\":\"journal article\",\"firstPage\":\"e70023\",\"id\":\"39375957\",\"journal\":\"Microb. Biotechnol.\",\"lastPage\":\"e70023\",\"publicationDate\":\"2024\",\"title\":\"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.\",\"volume\":\"17\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION IN DAUNORUBICIN EFFLUX\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRA1_STRC4             Reviewed;         330 AA.\nAC   P0DXG8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA1 {ECO:0000305};\nDE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};\nGN   Name=drrA1 {ECO:0000303|PubMed:39375957};\nGN   Synonyms=drrA {ECO:0000312|EMBL:WOT33550.1};\nGN   ORFNames=R5U08_05025 {ECO:0000312|EMBL:WOT33550.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:29.046585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111",
  "url": "https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:29.046585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111",
  "url": "https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P32010};\nCC       Peripheral membrane protein {ECO:0000250|UniProtKB:P32010}; Cytoplasmic\nCC       side {ECO:0000250|UniProtKB:P32010}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:29.046585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111",
  "url": "https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:29.046585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111",
  "url": "https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4"
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
  "excerpt": "[Term]\nid: GO:0016020\nname: membrane\nnamespace: cellular_component\nalt_id: GO:0016021\nalt_id: GO:0098589\nalt_id: GO:0098805\ndef: \"A lipid bilayer along with all the proteins and protein complexes embedded in it and attached to it.\" [GOC:dos, GOC:mah, ISBN:0815316194]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_yeast\nsynonym: \"integral component of membrane\" NARROW []\nsynonym: \"integral to membrane\" NARROW []\nsynonym: \"membrane region\" NARROW []\nsynonym: \"region of membrane\" NARROW []\nsynonym: \"transmembrane\" RELATED [GOC:mah]\nsynonym: \"whole membrane\" NARROW []\nxref: Wikipedia:Biological_membrane\nxref: Wikipedia:Transmembrane_protein\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016020",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 122626-122650",
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
  "excerpt": "[Term]\nid: GO:0030424\nname: axon\nnamespace: cellular_component\ndef: \"The long process of a neuron that conducts nerve impulses, usually away from the cell body to the terminals and varicosities, which are sites of storage and release of neurotransmitter.\" [GOC:nln, ISBN:0198506732]\nxref: NIF_Subcellular:sao1770195789\nxref: Wikipedia:Axon\nis_a: GO:0043005 ! neuron projection\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030424",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 166061-166069",
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
  "excerpt": "[Term]\nid: GO:0071513\nname: phosphopantothenoylcysteine decarboxylase complex\nnamespace: cellular_component\ndef: \"A protein complex that catalyzes decarboxylation of 4'-phosphopantothenoylcysteine to yield 4'-phosphopantetheine; this is the third step in the biosynthesis of Coenzyme A. The complex is homotrimeric in many eukaryotes, but is a heterotrimer in Saccharomyces.\" [GOC:jh, PMID:19915539]\ncomment: See also the molecular function term 'acetolactate synthase activity ; GO:0003984'.\nis_a: GO:1902494 ! catalytic complex\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0071513",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 377848-377856",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
