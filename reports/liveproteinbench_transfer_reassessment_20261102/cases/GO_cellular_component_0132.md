# GO_cellular_component_0132

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0132.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSDLAKTAQRRALRSSGSARPDEDVPAPNRRGNRLPRDERRGQLLVVASDVFVDRGYHAAGMDEIADRAGVSKPVLYQHFSSKLELYLAVLHRHVENLVSGVHQALSTTTDNRQRLHVAVQAFFDFIEHDSQGYRLIFENDFVTEPEVAAQVRVATESCIDAVFALISADSGLDPHRARMIAVGLVGMSVDCARYWLDADKPISKSDAVEGTVQFAWGGLSHVPLTRS

[Multiple Choices]
A. transcription regulator complex
B. plasma membrane
C. site of double-strand break
D. cell tip
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

> The sequence-matched UniProt record annotates this protein to the plasma membrane with GO evidence type HDA:MTBBASE. This supports the keyed choice as a database annotation, though it is not independent validation of the localization.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The basic N-terminal region and lack of an obvious transmembrane segment are more consistent with a soluble bacterial DNA-binding regulator than an integral membrane protein. That family-level inference makes a transcription-related choice more plausible than plasma membrane, but does not establish the protein’s actual membrane association.


**Missing item-specific fact**

> Evidence that this exact protein is associated with the plasma membrane, such as the protein-specific localization annotation or measurement.


**Reason**

> Transferable sequence and protein-family knowledge does not meaningfully favor B; it arguably favors a soluble transcription regulator instead. Selecting B therefore requires a fact specific to this protein that is absent from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence suggests a transcription regulator, but that alone does not establish membership in a transcription regulator complex. The other alternatives are not comparably supported by the original input.


### Important caveats

- The HDA:MTBBASE annotation supports the key but does not, by itself, establish how the protein associates with the membrane.
- The author’s source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The basic N-terminal region and lack of an obvious transmembrane segment are more consistent with a soluble bacterial DNA-binding regulator than an integral membrane protein. That family-level inference makes a transcription-related choice more plausible than plasma membrane, but does not establish the protein’s actual membrane association.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Evidence that this exact protein is associated with the plasma membrane, such as the protein-specific localization annotation or measurement.",
    "reason": "Transferable sequence and protein-family knowledge does not meaningfully favor B; it arguably favors a soluble transcription regulator instead. Selecting B therefore requires a fact specific to this protein that is absent from the original input."
  },
  "case_id": "GO_cellular_component_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein to the plasma membrane with GO evidence type HDA:MTBBASE. This supports the keyed choice as a database annotation, though it is not independent validation of the localization."
  },
  "important_caveats": [
    "The HDA:MTBBASE annotation supports the key but does not, by itself, establish how the protein associates with the membrane.",
    "The author’s source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence suggests a transcription regulator, but that alone does not establish membership in a transcription regulator complex. The other alternatives are not comparably supported by the original input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein to the plasma membrane with GO evidence type HDA:MTBBASE. This supports the keyed choice as a database annotation, though it is not independent validation of the localization.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The basic N-terminal region and lack of an obvious transmembrane segment are more consistent with a soluble bacterial DNA-binding regulator than an integral membrane protein. That family-level inference makes a transcription-related choice more plausible than plasma membrane, but does not establish the protein’s actual membrane association.",
    "missing_item_specific_fact": "Evidence that this exact protein is associated with the plasma membrane, such as the protein-specific localization annotation or measurement.",
    "reason": "Transferable sequence and protein-family knowledge does not meaningfully favor B; it arguably favors a soluble transcription regulator instead. Selecting B therefore requires a fact specific to this protein that is absent from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence suggests a transcription regulator, but that alone does not establish membership in a transcription regulator complex. The other alternatives are not comparably supported by the original input."
  },
  "important_caveats": [
    "The HDA:MTBBASE annotation supports the key but does not, by itself, establish how the protein associates with the membrane.",
    "The author’s source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for O05858 (FasR, HTH-type transcriptional activator) records GO:0005886 (plasma membrane) with evidence code HDA:MTBBASE (evidence C5, H3). This database annotation directly matches the expected answer B. However, the evidence quality is low: HDA from MTBBASE is a high-throughput database annotation, not direct experimental localization. The protein's annotated function (HTH-type transcriptional activator, DNA-binding, fatty acid synthesis regulator per C4, C6, H1, H2) is biologically inconsistent with plasma membrane localization in a bacterium. The annotation is present but its biological validity is questionable.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model analyzing this 228-aa sequence would observe: (1) an N-terminal region rich in basic residues (R, K) consistent with a DNA-binding domain; (2) patterns suggestive of a helix-turn-helix (HTH) motif; (3) absence of any long hydrophobic stretches typical of transmembrane helices; (4) no signal peptide or lipid-anchoring motifs. Transferable knowledge about HTH-type transcription factors (e.g., LacI, TetR, MarR families) places them in the cytoplasm/nucleoid, not the membrane. The protein is explicitly a transcriptional activator that binds DNA to regulate fatty acid biosynthesis genes. This reasoning strongly favors option A (transcription regulator complex) and disfavors B (plasma membrane). There is no generalizable biological principle that would lead a model to predict plasma membrane for an HTH transcription factor lacking transmembrane segments.


**Missing item-specific fact**

> The specific MTBBASE database annotation (HDA:MTBBASE) assigning GO:0005886 (plasma membrane) to this exact protein (O05858/FasR), which contradicts the protein's sequence features and annotated DNA-binding transcriptional activator function. Without knowing this particular database record, biological reasoning points to option A, not B.


**Reason**

> The expected answer (B, plasma membrane) contradicts what sequence-based reasoning and transferable knowledge about HTH transcription factors would predict (A, transcription regulator complex). The only basis for selecting B is the specific HDA:MTBBASE annotation in this protein's database entry. No family-level inference, structural principle, or analogy from other proteins supports membrane localization for an HTH DNA-binding transcriptional activator lacking transmembrane domains.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Option A (transcription regulator complex) is strongly supported by the protein's sequence features (HTH motifs, basic residues, no TM domains) and its annotated function as a DNA-binding transcriptional activator. Option B (plasma membrane) is supported only by a low-confidence HDA:MTBBASE database annotation. Both options could be defended depending on whether one trusts the database annotation or the biological reasoning from sequence, creating genuine ambiguity in which answer a model should select.


### Important caveats

- The HDA:MTBBASE evidence code indicates a high-throughput database annotation, not direct experimental subcellular localization. This is the weakest form of GO evidence.
- The protein is annotated as an HTH-type transcriptional activator with DNA-BINDING activity (C4, C6, H1, H2), which is fundamentally inconsistent with plasma membrane localization in a bacterium.
- The MTBBASE annotation may represent an error or a non-standard interpretation (e.g., membrane proximity during fatty acid synthesis regulation), but no experimental evidence for membrane association is provided in the supplied excerpts.
- The expected answer contradicts what legitimate biological reasoning from sequence and protein family knowledge would produce, making this question problematic for assessing model reasoning ability.
- The identity of the protein (O05858, Mycobacterium tuberculosis) was inferred from reviewer-only metadata and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model analyzing this 228-aa sequence would observe: (1) an N-terminal region rich in basic residues (R, K) consistent with a DNA-binding domain; (2) patterns suggestive of a helix-turn-helix (HTH) motif; (3) absence of any long hydrophobic stretches typical of transmembrane helices; (4) no signal peptide or lipid-anchoring motifs. Transferable knowledge about HTH-type transcription factors (e.g., LacI, TetR, MarR families) places them in the cytoplasm/nucleoid, not the membrane. The protein is explicitly a transcriptional activator that binds DNA to regulate fatty acid biosynthesis genes. This reasoning strongly favors option A (transcription regulator complex) and disfavors B (plasma membrane). There is no generalizable biological principle that would lead a model to predict plasma membrane for an HTH transcription factor lacking transmembrane segments.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific MTBBASE database annotation (HDA:MTBBASE) assigning GO:0005886 (plasma membrane) to this exact protein (O05858/FasR), which contradicts the protein's sequence features and annotated DNA-binding transcriptional activator function. Without knowing this particular database record, biological reasoning points to option A, not B.",
    "reason": "The expected answer (B, plasma membrane) contradicts what sequence-based reasoning and transferable knowledge about HTH transcription factors would predict (A, transcription regulator complex). The only basis for selecting B is the specific HDA:MTBBASE annotation in this protein's database entry. No family-level inference, structural principle, or analogy from other proteins supports membrane localization for an HTH DNA-binding transcriptional activator lacking transmembrane domains."
  },
  "case_id": "GO_cellular_component_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for O05858 (FasR, HTH-type transcriptional activator) records GO:0005886 (plasma membrane) with evidence code HDA:MTBBASE (evidence C5, H3). This database annotation directly matches the expected answer B. However, the evidence quality is low: HDA from MTBBASE is a high-throughput database annotation, not direct experimental localization. The protein's annotated function (HTH-type transcriptional activator, DNA-binding, fatty acid synthesis regulator per C4, C6, H1, H2) is biologically inconsistent with plasma membrane localization in a bacterium. The annotation is present but its biological validity is questionable."
  },
  "important_caveats": [
    "The HDA:MTBBASE evidence code indicates a high-throughput database annotation, not direct experimental subcellular localization. This is the weakest form of GO evidence.",
    "The protein is annotated as an HTH-type transcriptional activator with DNA-BINDING activity (C4, C6, H1, H2), which is fundamentally inconsistent with plasma membrane localization in a bacterium.",
    "The MTBBASE annotation may represent an error or a non-standard interpretation (e.g., membrane proximity during fatty acid synthesis regulation), but no experimental evidence for membrane association is provided in the supplied excerpts.",
    "The expected answer contradicts what legitimate biological reasoning from sequence and protein family knowledge would produce, making this question problematic for assessing model reasoning ability.",
    "The identity of the protein (O05858, Mycobacterium tuberculosis) was inferred from reviewer-only metadata and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Option A (transcription regulator complex) is strongly supported by the protein's sequence features (HTH motifs, basic residues, no TM domains) and its annotated function as a DNA-binding transcriptional activator. Option B (plasma membrane) is supported only by a low-confidence HDA:MTBBASE database annotation. Both options could be defended depending on whether one trusts the database annotation or the biological reasoning from sequence, creating genuine ambiguity in which answer a model should select."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for O05858 (FasR, HTH-type transcriptional activator) records GO:0005886 (plasma membrane) with evidence code HDA:MTBBASE (evidence C5, H3). This database annotation directly matches the expected answer B. However, the evidence quality is low: HDA from MTBBASE is a high-throughput database annotation, not direct experimental localization. The protein's annotated function (HTH-type transcriptional activator, DNA-binding, fatty acid synthesis regulator per C4, C6, H1, H2) is biologically inconsistent with plasma membrane localization in a bacterium. The annotation is present but its biological validity is questionable.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable model analyzing this 228-aa sequence would observe: (1) an N-terminal region rich in basic residues (R, K) consistent with a DNA-binding domain; (2) patterns suggestive of a helix-turn-helix (HTH) motif; (3) absence of any long hydrophobic stretches typical of transmembrane helices; (4) no signal peptide or lipid-anchoring motifs. Transferable knowledge about HTH-type transcription factors (e.g., LacI, TetR, MarR families) places them in the cytoplasm/nucleoid, not the membrane. The protein is explicitly a transcriptional activator that binds DNA to regulate fatty acid biosynthesis genes. This reasoning strongly favors option A (transcription regulator complex) and disfavors B (plasma membrane). There is no generalizable biological principle that would lead a model to predict plasma membrane for an HTH transcription factor lacking transmembrane segments.",
    "missing_item_specific_fact": "The specific MTBBASE database annotation (HDA:MTBBASE) assigning GO:0005886 (plasma membrane) to this exact protein (O05858/FasR), which contradicts the protein's sequence features and annotated DNA-binding transcriptional activator function. Without knowing this particular database record, biological reasoning points to option A, not B.",
    "reason": "The expected answer (B, plasma membrane) contradicts what sequence-based reasoning and transferable knowledge about HTH transcription factors would predict (A, transcription regulator complex). The only basis for selecting B is the specific HDA:MTBBASE annotation in this protein's database entry. No family-level inference, structural principle, or analogy from other proteins supports membrane localization for an HTH DNA-binding transcriptional activator lacking transmembrane domains."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Option A (transcription regulator complex) is strongly supported by the protein's sequence features (HTH motifs, basic residues, no TM domains) and its annotated function as a DNA-binding transcriptional activator. Option B (plasma membrane) is supported only by a low-confidence HDA:MTBBASE database annotation. Both options could be defended depending on whether one trusts the database annotation or the biological reasoning from sequence, creating genuine ambiguity in which answer a model should select."
  },
  "important_caveats": [
    "The HDA:MTBBASE evidence code indicates a high-throughput database annotation, not direct experimental subcellular localization. This is the weakest form of GO evidence.",
    "The protein is annotated as an HTH-type transcriptional activator with DNA-BINDING activity (C4, C6, H1, H2), which is fundamentally inconsistent with plasma membrane localization in a bacterium.",
    "The MTBBASE annotation may represent an error or a non-standard interpretation (e.g., membrane proximity during fatty acid synthesis regulation), but no experimental evidence for membrane association is provided in the supplied excerpts.",
    "The expected answer contradicts what legitimate biological reasoning from sequence and protein family knowledge would produce, making this question problematic for assessing model reasoning ability.",
    "The identity of the protein (O05858, Mycobacterium tuberculosis) was inferred from reviewer-only metadata and was not available to the evaluated model."
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
  "benchmark_sequence_length": 228,
  "benchmark_sequence_sha256": "1621eedefff3630c8192cd5b4fcfd4879e875f8fbc8942b921307bce32788e81",
  "current_entry_audit": {
    "entryVersion": 172,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1997-07-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 228,
  "current_source_sequence_sha256": "1621eedefff3630c8192cd5b4fcfd4879e875f8fbc8942b921307bce32788e81",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 170,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O05858",
  "selected_historical_entry_version": 170,
  "selected_historical_record_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "selected_historical_source_sequence_length": 228,
  "selected_historical_source_sequence_sha256": "1621eedefff3630c8192cd5b4fcfd4879e875f8fbc8942b921307bce32788e81",
  "selected_historical_version": {
    "accession": "O05858",
    "database": "Swiss-Prot",
    "entryVersion": 170,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FASR_MYCTU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O05858\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":172,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1997-07-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Mycobacteriales\",\"Mycobacteriaceae\",\"Mycobacterium\",\"Mycobacterium tuberculosis complex\"],\"scientificName\":\"Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv)\",\"taxonId\":83332}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23721164\",\"source\":\"PubMed\"}],\"value\":\"Fatty acid synthesis regulator\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"HTH-type transcriptional activator FasR\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0007005\",\"id\":\"14532352\",\"source\":\"PubMed\"}],\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"HDA:MTBBASE\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/26",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Mondino S.\",\"Gago G.\",\"Gramajo H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23721164\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.12282\"}],\"citationType\":\"journal article\",\"firstPage\":\"372\",\"id\":\"23721164\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"387\",\"publicationDate\":\"2013\",\"title\":\"Transcriptional regulation of fatty acid biosynthesis in mycobacteria.\",\"volume\":\"89\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"H37Rv\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DNA-BINDING\",\"ACTIVITY REGULATION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H1",
  "excerpt": "ID   FASR_MYCTU              Reviewed;         228 AA.\nAC   O05858; F2GK79; I6Y2X8; Q7D5X8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUL-1997, sequence version 1.\nDT   28-JAN-2026, entry version 170.\nDE   RecName: Full=HTH-type transcriptional activator FasR {ECO:0000305};\nDE   AltName: Full=Fatty acid synthesis regulator {ECO:0000303|PubMed:23721164};\nGN   Name=fasR {ECO:0000303|PubMed:23721164};\nGN   OrderedLocusNames=Rv3208 {ECO:0000312|EMBL:CCP46023.1};\nOS   Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales;\nOC   Mycobacteriaceae; Mycobacterium; Mycobacterium tuberculosis complex.\nOX   NCBI_TaxID=83332;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:12.681576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "url": "https://rest.uniprot.org/unisave/O05858?format=txt&versions=170"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   FUNCTION, DNA-BINDING, ACTIVITY REGULATION, AND SUBUNIT.\nRC   STRAIN=H37Rv;\nRX   PubMed=23721164; DOI=10.1111/mmi.12282;\nRA   Mondino S., Gago G., Gramajo H.;\nRT   \"Transcriptional regulation of fatty acid biosynthesis in mycobacteria.\";\nRL   Mol. Microbiol. 89:372-387(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:12.681576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "url": "https://rest.uniprot.org/unisave/O05858?format=txt&versions=170"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; HDA:MTBBASE.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:12.681576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-136",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "url": "https://rest.uniprot.org/unisave/O05858?format=txt&versions=170"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005667\nname: transcription regulator complex\nnamespace: cellular_component\nalt_id: GO:0044797\nalt_id: GO:0044798\ndef: \"A protein complex that is capable of associating with DNA by direct binding, or via other DNA-binding proteins or complexes, and regulating transcription.\" [GOC:jl]\nsubset: goslim_pir\nsynonym: \"cytoplasmic transcription factor complex\" RELATED []\nsynonym: \"nuclear transcription factor complex\" RELATED []\nsynonym: \"transcription factor complex\" RELATED []\nis_a: GO:0032991 ! protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005667",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58346-58358",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0035861\nname: site of double-strand break\nnamespace: cellular_component\ndef: \"A region of a chromosome at which a DNA double-strand break has occurred. DNA damage signaling and repair proteins accumulate at the lesion to respond to the damage and repair the DNA to form a continuous DNA helix.\" [GOC:bf, GOC:mah, GOC:vw, PMID:20096808, PMID:21035408]\nsynonym: \"DNA damage foci\" RELATED [GOC:vw]\nsynonym: \"DNA damage focus\" RELATED [GOC:mah, PMID:20096808, PMID:21035408]\nsynonym: \"ionizing radiation-induced foci\" RELATED [PMID:20096808, PMID:21035408]\nsynonym: \"IRIF\" RELATED [PMID:20096808, PMID:21035408]\nsynonym: \"site of DSB\" EXACT [PMID:21035408]\nis_a: GO:0090734 ! site of DNA damage\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0035861",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 221963-221974",
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
  "excerpt": "[Term]\nid: GO:0051286\nname: cell tip\nnamespace: cellular_component\ndef: \"The region at the end of the longest axis of a cylindrical or elongated cell.\" [GOC:ai, GOC:mah]\ncomment: Note that this term differs from 'cell pole ; GO:0060187' in that it is applicable to the thin ends of elongated cells, such as the ends of axons or dendrites.\nsynonym: \"cell end\" EXACT [GOC:mah]\nis_a: GO:0060187 ! cell pole\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051286",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 325114-325122",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 132. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
