# GO_biological_process_0163

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0163.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **D** — symbiont-mediated suppression of host innate immune response

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIEIFKDTGATHDLVYHSKINTFVWDVEFDIVLSDSKELNKCYFVKCFNPYRINGKCDFAVSSIDIFSEGKRLLIENEFNFKITKAVHVATSKDVTEIVLHLSERISSPFPIVKEVVYLD

[Multiple Choices]
A. neuron projection maintenance
B. DNA damage checkpoint signaling
C. extracellular matrix organization
D. symbiont-mediated suppression of host innate immune response
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry reports experimentally supported inhibition of the host DSR2 defense system, which supports the host-innate-immune-suppression process in choice D. The GO cross-reference itself is IEA, so the GO annotation is computationally assigned, but it is consistent with the reported function.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> That this particular protein is a phage protein that counteracts the host DSR2 defense system.


**Reason**

> The input provides only a short amino-acid sequence, with no organism, family annotation, or recognizable diagnostic feature that meaningfully identifies a role in host immune suppression rather than the other offered processes. Sequence length and apparent solubility alone are too nonspecific to distinguish choice D by transferable biological knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence-matched functional evidence supports choice D; no other offered process is comparably supported.


### Important caveats

- The functional evidence supports the expected process, while the GO term cross-reference is marked IEA rather than as a direct experimental GO annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular protein is a phage protein that counteracts the host DSR2 defense system.",
    "reason": "The input provides only a short amino-acid sequence, with no organism, family annotation, or recognizable diagnostic feature that meaningfully identifies a role in host immune suppression rather than the other offered processes. Sequence length and apparent solubility alone are too nonspecific to distinguish choice D by transferable biological knowledge."
  },
  "case_id": "GO_biological_process_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry reports experimentally supported inhibition of the host DSR2 defense system, which supports the host-innate-immune-suppression process in choice D. The GO cross-reference itself is IEA, so the GO annotation is computationally assigned, but it is consistent with the reported function."
  },
  "important_caveats": [
    "The functional evidence supports the expected process, while the GO term cross-reference is marked IEA rather than as a direct experimental GO annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence-matched functional evidence supports choice D; no other offered process is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry reports experimentally supported inhibition of the host DSR2 defense system, which supports the host-innate-immune-suppression process in choice D. The GO cross-reference itself is IEA, so the GO annotation is computationally assigned, but it is consistent with the reported function.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "That this particular protein is a phage protein that counteracts the host DSR2 defense system.",
    "reason": "The input provides only a short amino-acid sequence, with no organism, family annotation, or recognizable diagnostic feature that meaningfully identifies a role in host immune suppression rather than the other offered processes. Sequence length and apparent solubility alone are too nonspecific to distinguish choice D by transferable biological knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence-matched functional evidence supports choice D; no other offered process is comparably supported."
  },
  "important_caveats": [
    "The functional evidence supports the expected process, while the GO term cross-reference is marked IEA rather than as a direct experimental GO annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms the protein is DSR anti-defense 1 (DSAD1, O64191) from Bacillus phage SPbeta. Multiple experimental studies (ECO:0000269, PubMed:36192536, 38538592, 38555355, 38729958, 39039073) demonstrate it counteracts the host DSR2 anti-phage defense system by inhibiting DSR2 NADase activity. The GO annotation GO:0052170 (symbiont-mediated suppression of host innate immune response) is assigned via IEA:UniProtKB-KW, but the underlying experimental evidence supports the biological role: a phage (symbiont) protein suppressing the bacterial (host) innate immune defense. The GO term definition matches: 'a symbiont inhibits or disrupts the normal execution of the innate immune response of the host organism.'

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [GO3](#evidence-go3), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 120-aa sequence lacks any eukaryotic-specific features: no signal peptide, no transmembrane domains, no kinase/DNA-binding/SH2/SH3 domains, no extracellular matrix motifs (e.g., EGF, fibronectin, laminin repeats), and no neuron-specific structural elements. Options A (neuron projection maintenance), B (DNA damage checkpoint signaling), and C (extracellular matrix organization) are all processes carried out by eukaryotic cells requiring large multi-domain proteins or complex signaling machineries. A knowledgeable model can eliminate A (requires neuronal cell biology context), C (requires ECM structural proteins typically >300 aa with domain repeats), and B (checkpoint signaling involves kinases, adaptors, and DNA-binding proteins absent here). Option D (symbiont-mediated suppression of host innate immune response) is the only GO term routinely assigned to small pathogen/viral effector proteins that interfere with host defense systems. The small size, absence of catalytic or structural domains, and lack of eukaryotic context features are consistent with a compact effector protein. This elimination-based reasoning uses transferable knowledge about the typical protein architectures associated with each biological process category.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can meaningfully distinguish D from A, B, and C by recognizing that the three distractors describe processes requiring eukaryotic cellular machinery and large multi-domain proteins, while the 120-aa sequence with no eukaryotic features is only compatible with the small pathogen effector category described by D. This is legitimate transferable knowledge about protein-size and architecture requirements for different biological processes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe eukaryotic processes requiring cellular contexts (neurons, checkpoint machinery, ECM assembly) and typically large multi-domain proteins, which are clearly incompatible with a 120-aa protein lacking eukaryotic features. Option D is the only viable choice. No ambiguity among the offered alternatives.


### Important caveats

- The GO annotation for this protein is IEA (Inferred from Electronic Annotation) via UniProtKB keyword, not a direct experimental GO assignment. However, the underlying experimental evidence (ECO:0000269) strongly supports the biological role.
- The positive identification of D relies primarily on elimination of the three eukaryotic-specific options rather than on a recognizable phage-effector motif in the sequence itself.
- The DSR2 anti-defense system was characterized in 2022-2024; a model trained on earlier literature might not recognize this specific mechanism, but the elimination logic for A, B, C remains valid regardless.
- The reviewer-only evidence identifies the protein as O64191 from Bacillus phage SPbeta, but this organism/accession information was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 120-aa sequence lacks any eukaryotic-specific features: no signal peptide, no transmembrane domains, no kinase/DNA-binding/SH2/SH3 domains, no extracellular matrix motifs (e.g., EGF, fibronectin, laminin repeats), and no neuron-specific structural elements. Options A (neuron projection maintenance), B (DNA damage checkpoint signaling), and C (extracellular matrix organization) are all processes carried out by eukaryotic cells requiring large multi-domain proteins or complex signaling machineries. A knowledgeable model can eliminate A (requires neuronal cell biology context), C (requires ECM structural proteins typically >300 aa with domain repeats), and B (checkpoint signaling involves kinases, adaptors, and DNA-binding proteins absent here). Option D (symbiont-mediated suppression of host innate immune response) is the only GO term routinely assigned to small pathogen/viral effector proteins that interfere with host defense systems. The small size, absence of catalytic or structural domains, and lack of eukaryotic context features are consistent with a compact effector protein. This elimination-based reasoning uses transferable knowledge about the typical protein architectures associated with each biological process category.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can meaningfully distinguish D from A, B, and C by recognizing that the three distractors describe processes requiring eukaryotic cellular machinery and large multi-domain proteins, while the 120-aa sequence with no eukaryotic features is only compatible with the small pathogen effector category described by D. This is legitimate transferable knowledge about protein-size and architecture requirements for different biological processes."
  },
  "case_id": "GO_biological_process_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "GO3",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is DSR anti-defense 1 (DSAD1, O64191) from Bacillus phage SPbeta. Multiple experimental studies (ECO:0000269, PubMed:36192536, 38538592, 38555355, 38729958, 39039073) demonstrate it counteracts the host DSR2 anti-phage defense system by inhibiting DSR2 NADase activity. The GO annotation GO:0052170 (symbiont-mediated suppression of host innate immune response) is assigned via IEA:UniProtKB-KW, but the underlying experimental evidence supports the biological role: a phage (symbiont) protein suppressing the bacterial (host) innate immune defense. The GO term definition matches: 'a symbiont inhibits or disrupts the normal execution of the innate immune response of the host organism.'"
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA (Inferred from Electronic Annotation) via UniProtKB keyword, not a direct experimental GO assignment. However, the underlying experimental evidence (ECO:0000269) strongly supports the biological role.",
    "The positive identification of D relies primarily on elimination of the three eukaryotic-specific options rather than on a recognizable phage-effector motif in the sequence itself.",
    "The DSR2 anti-defense system was characterized in 2022-2024; a model trained on earlier literature might not recognize this specific mechanism, but the elimination logic for A, B, C remains valid regardless.",
    "The reviewer-only evidence identifies the protein as O64191 from Bacillus phage SPbeta, but this organism/accession information was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe eukaryotic processes requiring cellular contexts (neurons, checkpoint machinery, ECM assembly) and typically large multi-domain proteins, which are clearly incompatible with a 120-aa protein lacking eukaryotic features. Option D is the only viable choice. No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is DSR anti-defense 1 (DSAD1, O64191) from Bacillus phage SPbeta. Multiple experimental studies (ECO:0000269, PubMed:36192536, 38538592, 38555355, 38729958, 39039073) demonstrate it counteracts the host DSR2 anti-phage defense system by inhibiting DSR2 NADase activity. The GO annotation GO:0052170 (symbiont-mediated suppression of host innate immune response) is assigned via IEA:UniProtKB-KW, but the underlying experimental evidence supports the biological role: a phage (symbiont) protein suppressing the bacterial (host) innate immune defense. The GO term definition matches: 'a symbiont inhibits or disrupts the normal execution of the innate immune response of the host organism.'",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "GO3", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 120-aa sequence lacks any eukaryotic-specific features: no signal peptide, no transmembrane domains, no kinase/DNA-binding/SH2/SH3 domains, no extracellular matrix motifs (e.g., EGF, fibronectin, laminin repeats), and no neuron-specific structural elements. Options A (neuron projection maintenance), B (DNA damage checkpoint signaling), and C (extracellular matrix organization) are all processes carried out by eukaryotic cells requiring large multi-domain proteins or complex signaling machineries. A knowledgeable model can eliminate A (requires neuronal cell biology context), C (requires ECM structural proteins typically >300 aa with domain repeats), and B (checkpoint signaling involves kinases, adaptors, and DNA-binding proteins absent here). Option D (symbiont-mediated suppression of host innate immune response) is the only GO term routinely assigned to small pathogen/viral effector proteins that interfere with host defense systems. The small size, absence of catalytic or structural domains, and lack of eukaryotic context features are consistent with a compact effector protein. This elimination-based reasoning uses transferable knowledge about the typical protein architectures associated with each biological process category.",
    "missing_item_specific_fact": "",
    "reason": "A model can meaningfully distinguish D from A, B, and C by recognizing that the three distractors describe processes requiring eukaryotic cellular machinery and large multi-domain proteins, while the 120-aa sequence with no eukaryotic features is only compatible with the small pathogen effector category described by D. This is legitimate transferable knowledge about protein-size and architecture requirements for different biological processes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe eukaryotic processes requiring cellular contexts (neurons, checkpoint machinery, ECM assembly) and typically large multi-domain proteins, which are clearly incompatible with a 120-aa protein lacking eukaryotic features. Option D is the only viable choice. No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA (Inferred from Electronic Annotation) via UniProtKB keyword, not a direct experimental GO assignment. However, the underlying experimental evidence (ECO:0000269) strongly supports the biological role.",
    "The positive identification of D relies primarily on elimination of the three eukaryotic-specific options rather than on a recognizable phage-effector motif in the sequence itself.",
    "The DSR2 anti-defense system was characterized in 2022-2024; a model trained on earlier literature might not recognize this specific mechanism, but the elimination logic for A, B, C remains valid regardless.",
    "The reviewer-only evidence identifies the protein as O64191 from Bacillus phage SPbeta, but this organism/accession information was not available to the evaluated model."
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
  "benchmark_sequence_length": 120,
  "benchmark_sequence_sha256": "40678122002b46dfbc860b820c9d19a101b8f3e72b16161ed2b4519ed6c26fcd",
  "current_entry_audit": {
    "entryVersion": 56,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "1998-08-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 120,
  "current_source_sequence_sha256": "40678122002b46dfbc860b820c9d19a101b8f3e72b16161ed2b4519ed6c26fcd",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O64191",
  "selected_historical_entry_version": 55,
  "selected_historical_record_sha256": "a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11",
  "selected_historical_source_sequence_length": 120,
  "selected_historical_source_sequence_sha256": "40678122002b46dfbc860b820c9d19a101b8f3e72b16161ed2b4519ed6c26fcd",
  "selected_historical_version": {
    "accession": "O64191",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DSAD1_BPSPB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O64191\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":56,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"1998-08-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacillus phage SPBc2\",\"lineage\":[\"Viruses\",\"Duplodnaviria\",\"Heunggongvirae\",\"Uroviricota\",\"Caudoviricetes\",\"Caudoviricetes incertae sedis\",\"Spbetavirus\",\"Spbetavirus SPbeta\"],\"scientificName\":\"Bacillus phage SPbeta\",\"synonyms\":[\"Bacteriophage SP-beta\"],\"taxonId\":2932878}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36192536\",\"source\":\"PubMed\"}],\"value\":\"DSR anti-defense 1\"},\"shortNames\":[{\"value\":\"DSAD1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36192536\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38538592\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38555355\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38729958\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39039073\",\"source\":\"PubMed\"}],\"value\":\"Counteracts the defense-associated sirtuin 2 (DSR2) defense system of the host (PubMed:36192536, PubMed:38538592, PubMed:38555355, PubMed:38729958, PubMed:39039073). Inhibits the NADase activity of host DSR2 by competing with the tail tube protein that normally activates DSR2 (PubMed:38538592, PubMed:39039073)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0052170\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:symbiont-mediated suppression of host innate immune response\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/36",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Garb J.\",\"Lopatina A.\",\"Bernheim A.\",\"Zaremba M.\",\"Siksnys V.\",\"Melamed S.\",\"Leavitt A.\",\"Millman A.\",\"Amitai G.\",\"Sorek R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36192536\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41564-022-01207-8\"}],\"citationType\":\"journal article\",\"firstPage\":\"1849\",\"id\":\"36192536\",\"journal\":\"Nat. Microbiol.\",\"lastPage\":\"1856\",\"publicationDate\":\"2022\",\"title\":\"Multiple phage resistance systems inhibit infection via SIR2-dependent NAD+ depletion.\",\"volume\":\"7\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang R.\",\"Xu Q.\",\"Wu Z.\",\"Li J.\",\"Guo H.\",\"Liao T.\",\"Shi Y.\",\"Yuan L.\",\"Gao H.\",\"Yang R.\",\"Shi Z.\",\"Li F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39039073\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-50410-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"6185\",\"id\":\"39039073\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"6185\",\"publicationDate\":\"2024\",\"title\":\"The structural basis of the activation and inhibition of DSR2 NADase by phage proteins.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y3M\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y3W\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y3Y\",\"source\":\"PDB\"}],\"referenceNumber\":3,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.25 ANGSTROMS) IN COMPLEX WITH BACILLUS SUBTILIS DSR2\",\"INTERACTION WITH BACILLUS SUBTILIS DSR2\",\"MUTAGENESIS OF HIS-17; LYS-19; ASN-21 AND PHE-59\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang J.T.\",\"Liu X.Y.\",\"Li Z.\",\"Wei X.Y.\",\"Song X.Y.\",\"Cui N.\",\"Zhong J.\",\"Li H.\",\"Jia N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38555355\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-47177-9\"}],\"citationType\":\"journal article\",\"firstPage\":\"2797\",\"id\":\"38555355\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2797\",\"publicationDate\":\"2024\",\"title\":\"Structural basis for phage-mediated activation and repression of bacterial DSR2 anti-phage defense system.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYD\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYF\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (2.56 ANGSTROMS) IN COMPLEX WITH BACILLUS SUBTILIS DSR2\",\"STRUCTURE BY ELECTRON MICROSCOPY (2.85 ANGSTROMS) IN COMPLEX WITH BACILLUS SUBTILIS DSR2 AND NAD\",\"INTERACTION WITH BACILLUS SUBTILIS DSR2\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Huang J.\",\"Zhu K.\",\"Gao Y.\",\"Ye F.\",\"Li Z.\",\"Ge Y.\",\"Liu S.\",\"Yang J.\",\"Gao A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38729958\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-48291-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"3954\",\"id\":\"38729958\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"3954\",\"publicationDate\":\"2024\",\"title\":\"Molecular basis of bacterial DSR2 anti-phage defense and viral immune evasion.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WKT\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R\"}],\"referenceNumber\":5,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.86 ANGSTROMS) IN COMPLEX WITH BACILLUS SUBTILIS DSR2\",\"INTERACTION WITH BACILLUS SUBTILIS DSR2\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin H.\",\"Li X.\",\"Wang X.\",\"Zhang C.\",\"Gao J.\",\"Yu G.\",\"He Q.\",\"Yang J.\",\"Liu X.\",\"Wei Y.\",\"Li Z.\",\"Zhang H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38538592\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-47030-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"2692\",\"id\":\"38538592\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2692\",\"publicationDate\":\"2024\",\"title\":\"Insights into the modulation of bacterial NADase activity by phage proteins.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8W56\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WKN\",\"source\":\"PDB\"}],\"referenceNumber\":6,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS) IN COMPLEX WITH BACILLUS SUBTILIS DSR2\",\"FUNCTION\",\"INTERACTION WITH BACILLUS SUBTILIS DSR2\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:29:15.584566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d",
  "url": "https://rest.uniprot.org/uniprotkb/O64191.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O64191?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H1",
  "excerpt": "ID   DSAD1_BPSPB             Reviewed;         120 AA.\nAC   O64191;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-AUG-1998, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=DSR anti-defense 1 {ECO:0000303|PubMed:36192536};\nDE            Short=DSAD1;\nGN   Name=yotI;\nOS   Bacillus phage SPbeta (Bacillus phage SPBc2) (Bacteriophage SP-beta).\nOC   Viruses; Duplodnaviria; Heunggongvirae; Uroviricota; Caudoviricetes;\nOC   Spbetavirus; Spbetavirus SPbeta.\nOX   NCBI_TaxID=2932878;\nOH   NCBI_TaxID=1408; Bacillus pumilus (Bacillus mesentericus).\nOH   NCBI_TaxID=1423; Bacillus subtilis.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:17.658870+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11",
  "url": "https://rest.uniprot.org/unisave/O64191?format=txt&versions=55"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O64191?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=36192536; DOI=10.1038/s41564-022-01207-8;\nRA   Garb J., Lopatina A., Bernheim A., Zaremba M., Siksnys V., Melamed S.,\nRA   Leavitt A., Millman A., Amitai G., Sorek R.;\nRT   \"Multiple phage resistance systems inhibit infection via SIR2-dependent\nRT   NAD+ depletion.\";\nRL   Nat. Microbiol. 7:1849-1856(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:17.658870+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11",
  "url": "https://rest.uniprot.org/unisave/O64191?format=txt&versions=55"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O64191?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:8Y3M, ECO:0007744|PDB:8Y3W, ECO:0007744|PDB:8Y3Y}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.25 ANGSTROMS) IN COMPLEX WITH BACILLUS\nRP   SUBTILIS DSR2, INTERACTION WITH BACILLUS SUBTILIS DSR2, MUTAGENESIS OF\nRP   HIS-17; LYS-19; ASN-21 AND PHE-59, AND FUNCTION.\nRX   PubMed=39039073; DOI=10.1038/s41467-024-50410-0;\nRA   Wang R., Xu Q., Wu Z., Li J., Guo H., Liao T., Shi Y., Yuan L., Gao H.,\nRA   Yang R., Shi Z., Li F.;\nRT   \"The structural basis of the activation and inhibition of DSR2 NADase by\nRT   phage proteins.\";\nRL   Nat. Commun. 15:6185-6185(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:17.658870+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11",
  "url": "https://rest.uniprot.org/unisave/O64191?format=txt&versions=55"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O64191?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:8WYD, ECO:0007744|PDB:8WYE, ECO:0007744|PDB:8WYF}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (2.56 ANGSTROMS) IN COMPLEX WITH BACILLUS\nRP   SUBTILIS DSR2, STRUCTURE BY ELECTRON MICROSCOPY (2.85 ANGSTROMS) IN COMPLEX\nRP   WITH BACILLUS SUBTILIS DSR2 AND NAD, INTERACTION WITH BACILLUS SUBTILIS\nRP   DSR2, AND FUNCTION.\nRX   PubMed=38555355; DOI=10.1038/s41467-024-47177-9;\nRA   Zhang J.T., Liu X.Y., Li Z., Wei X.Y., Song X.Y., Cui N., Zhong J., Li H.,\nRA   Jia N.;\nRT   \"Structural basis for phage-mediated activation and repression of bacterial\nRT   DSR2 anti-phage defense system.\";\nRL   Nat. Commun. 15:2797-2797(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:17.658870+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11",
  "url": "https://rest.uniprot.org/unisave/O64191?format=txt&versions=55"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O64191?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H5",
  "excerpt": "RN   [5] {ECO:0007744|PDB:8WKT}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.86 ANGSTROMS) IN COMPLEX WITH BACILLUS\nRP   SUBTILIS DSR2, INTERACTION WITH BACILLUS SUBTILIS DSR2, AND FUNCTION.\nRC   STRAIN=29R;\nRX   PubMed=38729958; DOI=10.1038/s41467-024-48291-4;\nRA   Huang J., Zhu K., Gao Y., Ye F., Li Z., Ge Y., Liu S., Yang J., Gao A.;\nRT   \"Molecular basis of bacterial DSR2 anti-phage defense and viral immune\nRT   evasion.\";\nRL   Nat. Commun. 15:3954-3954(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:17.658870+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11",
  "url": "https://rest.uniprot.org/unisave/O64191?format=txt&versions=55"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O64191?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H6",
  "excerpt": "RN   [6] {ECO:0007744|PDB:8W56, ECO:0007744|PDB:8WKN}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS) IN COMPLEX WITH BACILLUS\nRP   SUBTILIS DSR2, FUNCTION, AND INTERACTION WITH BACILLUS SUBTILIS DSR2.\nRX   PubMed=38538592; DOI=10.1038/s41467-024-47030-z;\nRA   Yin H., Li X., Wang X., Zhang C., Gao J., Yu G., He Q., Yang J., Liu X.,\nRA   Wei Y., Li Z., Zhang H.;\nRT   \"Insights into the modulation of bacterial NADase activity by phage\nRT   proteins.\";\nRL   Nat. Commun. 15:2692-2692(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:17.658870+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11",
  "url": "https://rest.uniprot.org/unisave/O64191?format=txt&versions=55"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O64191?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H7",
  "excerpt": "CC   -!- FUNCTION: Counteracts the defense-associated sirtuin 2 (DSR2) defense\nCC       system of the host (PubMed:36192536, PubMed:38538592, PubMed:38555355,\nCC       PubMed:38729958, PubMed:39039073). Inhibits the NADase activity of host\nCC       DSR2 by competing with the tail tube protein that normally activates\nCC       DSR2 (PubMed:38538592, PubMed:39039073). {ECO:0000269|PubMed:36192536,\nCC       ECO:0000269|PubMed:38538592, ECO:0000269|PubMed:38555355,\nCC       ECO:0000269|PubMed:38729958, ECO:0000269|PubMed:39039073}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:17.658870+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11",
  "url": "https://rest.uniprot.org/unisave/O64191?format=txt&versions=55"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O64191?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0052170; P:symbiont-mediated suppression of host innate immune response; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:17.658870+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11",
  "url": "https://rest.uniprot.org/unisave/O64191?format=txt&versions=55"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000077\nname: DNA damage checkpoint signaling\nnamespace: biological_process\nalt_id: GO:0072422\ndef: \"A signal transduction process that contributes to a DNA damage checkpoint.\" [GOC:mah]\nsynonym: \"DNA damage checkpoint\" EXACT []\nsynonym: \"DNA damage response, signal transduction resulting in cell cycle arrest\" NARROW []\nsynonym: \"signal transduction involved in DNA damage checkpoint\" EXACT []\nxref: Wikipedia:DNA_damage_checkpoint\nxref: Wikipedia:Postreplication_checkpoint\nis_a: GO:0031570 ! DNA integrity checkpoint signaling\nis_a: GO:0042770 ! signal transduction in response to DNA damage\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000077",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 717-730",
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
  "excerpt": "[Term]\nid: GO:0030198\nname: extracellular matrix organization\nnamespace: biological_process\ndef: \"A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of an extracellular matrix.\" [GOC:mah]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsynonym: \"extracellular matrix organisation\" EXACT []\nsynonym: \"extracellular matrix organization and biogenesis\" RELATED [GOC:mah]\nxref: Reactome:R-HSA-1474244 \"Extracellular matrix organization\"\nis_a: GO:0043062 ! extracellular structure organization\nis_a: GO:0045229 ! external encapsulating structure organization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030198",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 163837-163850",
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
  "excerpt": "[Term]\nid: GO:0052170\nname: symbiont-mediated suppression of host innate immune response\nnamespace: biological_process\nalt_id: GO:0052309\ndef: \"A process in which a symbiont inhibits or disrupts the normal execution of the innate immune response of the host organism, the host's first line of defense against infection. The host is defined as the larger of the organisms involved in a symbiotic interaction.\" [GOC:mtg_pamgo_17jul06]\nsynonym: \"down regulation by symbiont of host innate immunity\" EXACT []\nsynonym: \"down-regulation by symbiont of host innate immunity\" EXACT []\nsynonym: \"downregulation by symbiont of host innate immunity\" EXACT []\nsynonym: \"inhibition by symbiont of host innate immunity\" NARROW []\nsynonym: \"negative regulation by symbiont of host innate immune response\" EXACT []\nsynonym: \"negative regulation by symbiont of host innate immunity\" EXACT [GOC:pg]\nsynonym: \"negative regulation of host innate immune response\" EXACT []\nsynonym: \"negative regulation of innate immune response in other organism\" BROAD []\nsynonym: \"suppression by symbiont of host innate immune response\" EXACT []\nsynonym: \"suppression of host innate immune response\" EXACT []\nxref: Reactome:R-HSA-9637687 \"Suppression of phagosomal maturation\"\nis_a: GO:0052167 ! symbiont-mediated perturbation of host innate immune response\nis_a: GO:0052562 ! symbiont-mediated suppression of host immune response\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0052170",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 334843-334862",
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
  "excerpt": "[Term]\nid: GO:1990535\nname: neuron projection maintenance\nnamespace: biological_process\ndef: \"The organization process that preserves a neuron projection in a stable functional or structural state. A neuron projection is a prolongation or process extending from a nerve cell, e.g. an axon or dendrite.\" [GOC:kmv, PMID:25359212]\nsynonym: \"axon homeostasis\" RELATED []\nsynonym: \"axon maintenance\" RELATED []\nsynonym: \"neurite maintenance\" NARROW []\nsynonym: \"neuron process maintenance\" EXACT []\nsynonym: \"neuron protrusion maintenance\" EXACT []\nsynonym: \"neuronal cell projection maintenance\" EXACT []\nis_a: GO:0106027 ! neuron projection organization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990535",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 552917-552929",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 163. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
