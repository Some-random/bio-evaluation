# GO_biological_process_0047

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0047.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **A** — microtubule cytoskeleton organization

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MESGPRVEPGPGAPAAVLARIPQEPRPSPEGDPSPPPPPTPMSALVPDTPPDTPPAMKNASTPQQLPLEPVSPTGQVSPQPAPPPDECPSSEAKSRGPTPTATGPRDAKPSQRSSQPSPTAVPASDSPSAKQDVKKAGERHKLAKERREERAKYLAAKKAVWLEKEEKAKALREKQLQERRRRLEEQRLKAEQRRAALEERQRQKLEKNKERYEAAIQRSVKKTWAEIRQQRWSWAGALHHNSPGRKTSGSRCSVSAVNLPKHVDSIINKRLSKSSATLWNSPSRNRSLQLSAWESSIVDRLMTPTLSFLARSRSAVTLPRNGRDQGRGSGPGRRPTRARAGASLAPGPHPDRTHPSAAVPVCPRSASASPLTPCSAPRSAHRCTPSGERPERRKPGAGGSPALVRRRLEATPVQKKEKKDKERENEKEKSALARERNLKKRQSLPASIRPRISTGAELSTKSKARPTSPSTTWHRPASPCPSPGPGHTLPPKPPSPRGTTASPKGRIRRKEEAKESPSPSGPEDKNHSKSRTAEEKEPAAPASPAPSPVPSPTPAQPQKEQSSTQIPPDTAVPAVPTVPTFPTAPPTAAPSVTPSKPMAGTTDREEATRLLAEKRRQAREQREREEQERKLQAERDKRMREEQLAREAEARAEREAEARRREEQEAREKAQAEQEEQERLQKQKEEAEARSREEAERQRLEREKHFQKEEQERQERRKRLEEIMKRTRKSEAAETKKQDGKETMANNSGPDPVKAVETRPSGLQKDSMQKEELAPQEPQWSLPSKEMPGSLVNGLQPLPAHQENGFPAKGTAGDKSLGRAAEGLLPFAEADAFLKKAVVQPPQVTEVL

[Multiple Choices]
A. microtubule cytoskeleton organization
B. positive regulation of signal transduction
C. protein-containing complex disassembly
D. regulation of root development
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

> The sequence-matched historical UniProt record assigns microtubule cytoskeleton organization (GO:0000226) with ISS evidence, and describes the protein as microtubule-stabilizing. The function annotation is transferred by similarity, not direct experimental evidence for this protein.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has extensive low-complexity regions and long, highly charged coiled-coil-like segments, an architecture compatible with cytoskeletal adaptor proteins. Transferable knowledge of MAP7-family proteins links this kind of architecture to microtubule association and stabilization, making microtubule cytoskeleton organization a meaningful choice over signal-transduction regulation, complex disassembly, or root development. This is a probabilistic family-level inference, not proof from sequence architecture alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference can distinguish the offered alternatives without recalling this exact protein's annotation. The sequence architecture is not uniquely diagnostic, but the choices permit a meaningful inference toward microtubule organization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence-based cytoskeletal inference.


### Important caveats

- The supplied functional annotation is based on similarity evidence, and the GO assignment is ISS; neither establishes direct experimental validation for this exact protein.
- The organism and protein identity in the reviewer-only source were not original model inputs and are not used as the basis for answerability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has extensive low-complexity regions and long, highly charged coiled-coil-like segments, an architecture compatible with cytoskeletal adaptor proteins. Transferable knowledge of MAP7-family proteins links this kind of architecture to microtubule association and stabilization, making microtubule cytoskeleton organization a meaningful choice over signal-transduction regulation, complex disassembly, or root development. This is a probabilistic family-level inference, not proof from sequence architecture alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference can distinguish the offered alternatives without recalling this exact protein's annotation. The sequence architecture is not uniquely diagnostic, but the choices permit a meaningful inference toward microtubule organization."
  },
  "case_id": "GO_biological_process_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns microtubule cytoskeleton organization (GO:0000226) with ISS evidence, and describes the protein as microtubule-stabilizing. The function annotation is transferred by similarity, not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The supplied functional annotation is based on similarity evidence, and the GO assignment is ISS; neither establishes direct experimental validation for this exact protein.",
    "The organism and protein identity in the reviewer-only source were not original model inputs and are not used as the basis for answerability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-based cytoskeletal inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns microtubule cytoskeleton organization (GO:0000226) with ISS evidence, and describes the protein as microtubule-stabilizing. The function annotation is transferred by similarity, not direct experimental evidence for this protein.",
    "evidence_ids": ["H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has extensive low-complexity regions and long, highly charged coiled-coil-like segments, an architecture compatible with cytoskeletal adaptor proteins. Transferable knowledge of MAP7-family proteins links this kind of architecture to microtubule association and stabilization, making microtubule cytoskeleton organization a meaningful choice over signal-transduction regulation, complex disassembly, or root development. This is a probabilistic family-level inference, not proof from sequence architecture alone.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference can distinguish the offered alternatives without recalling this exact protein's annotation. The sequence architecture is not uniquely diagnostic, but the choices permit a meaningful inference toward microtubule organization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-based cytoskeletal inference."
  },
  "important_caveats": [
    "The supplied functional annotation is based on similarity evidence, and the GO assignment is ISS; neither establishes direct experimental validation for this exact protein.",
    "The organism and protein identity in the reviewer-only source were not original model inputs and are not used as the basis for answerability."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A8I5ZM56, MAP7 domain-containing protein 1, Rattus norvegicus) annotates this protein as a 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' (C5/H2) and assigns GO:0000226 (microtubule cytoskeleton organization) with evidence code ISS:UniProtKB (C6/H3). The sequence matches exactly (849 AA, SHA256 confirmed). The GO annotation is inferred by similarity (ISS), not direct experiment on this exact protein, but the functional description and family assignment are consistent and directly support option A.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 849-aa sequence displays hallmark features of microtubule-associated protein (MAP) family members: (1) extensive coiled-coil regions with heptad-like alternating charged residues (e.g., 'AKERREERAKYLAAKKAVWLEKEEKAKALREKQLQERRRRLEEQRLKAEQRRAALEERQRQKLEKNKERYEAAIQRSVKKTWAEIRQQRW' and 'EATRLLAEKRRQAREQREREEQERKLQAERDKRMREEQLAREAEARAEREAEARRREEQEAREKAQAEQEEQERLQKQKEEAEARSREEAERQRLEREKHFQKEEQERQERRKRLEEIMKRTRKSEAAETKK'), (2) multiple proline-rich segments ('PSPPPPPTPMSALVPDTPPDTPPAMKNASTPQQLPLEPVSPTGQVSPQPAPPP'), and (3) serine/threonine-rich stretches. These compositional and structural motifs are well-established signatures of the MAP superfamily (MAP1, MAP2, MAP4, MAP7, tau), all of which are characterized by long coiled-coil and proline-rich regions and function in microtubule stabilization and cytoskeleton organization. Option D (regulation of root development) is trivially eliminated as a plant-specific GO term in a clearly mammalian sequence. Option B (positive regulation of signal transduction) would typically require enzymatic domains (kinase, GTPase, SH2/SH3) absent here. Option C (protein-containing complex disassembly) implies protease or chaperone activity not suggested by the sequence. The MAP-family sequence signature thus meaningfully distinguishes A from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the coiled-coil/proline-rich/serine-rich composition as characteristic of the MAP family, which is broadly associated with microtubule cytoskeleton organization. This family-level inference, combined with elimination of the plant-specific option D and the lack of enzymatic domains for B and C, provides a credible transferable basis for selecting A without needing the exact database record for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D is eliminated as a plant-specific term. Option B lacks supporting structural features (no enzymatic or adaptor domains). Option C lacks protease/chaperone features. Option A is the only choice consistent with the MAP-family sequence signature. No ambiguity among the offered choices.


### Important caveats

- The GO annotation for this protein carries evidence code ISS (Inferred from Sequence or Structural Similarity), meaning it is transferred by homology rather than directly experimentally validated on this exact rat protein.
- The MAP7 domain family is less widely studied than MAP1/2/4/tau; a model unfamiliar with the specific MAP7 subfamily might rely more heavily on the general coiled-coil/proline-rich signature shared with other MAPs.
- The reviewer-only evidence confirms the protein identity (MAP7D1, rat) but this was not available to the evaluated model; the reasoning above relies solely on sequence features and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 849-aa sequence displays hallmark features of microtubule-associated protein (MAP) family members: (1) extensive coiled-coil regions with heptad-like alternating charged residues (e.g., 'AKERREERAKYLAAKKAVWLEKEEKAKALREKQLQERRRRLEEQRLKAEQRRAALEERQRQKLEKNKERYEAAIQRSVKKTWAEIRQQRW' and 'EATRLLAEKRRQAREQREREEQERKLQAERDKRMREEQLAREAEARAEREAEARRREEQEAREKAQAEQEEQERLQKQKEEAEARSREEAERQRLEREKHFQKEEQERQERRKRLEEIMKRTRKSEAAETKK'), (2) multiple proline-rich segments ('PSPPPPPTPMSALVPDTPPDTPPAMKNASTPQQLPLEPVSPTGQVSPQPAPPP'), and (3) serine/threonine-rich stretches. These compositional and structural motifs are well-established signatures of the MAP superfamily (MAP1, MAP2, MAP4, MAP7, tau), all of which are characterized by long coiled-coil and proline-rich regions and function in microtubule stabilization and cytoskeleton organization. Option D (regulation of root development) is trivially eliminated as a plant-specific GO term in a clearly mammalian sequence. Option B (positive regulation of signal transduction) would typically require enzymatic domains (kinase, GTPase, SH2/SH3) absent here. Option C (protein-containing complex disassembly) implies protease or chaperone activity not suggested by the sequence. The MAP-family sequence signature thus meaningfully distinguishes A from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the coiled-coil/proline-rich/serine-rich composition as characteristic of the MAP family, which is broadly associated with microtubule cytoskeleton organization. This family-level inference, combined with elimination of the plant-specific option D and the lack of enzymatic domains for B and C, provides a credible transferable basis for selecting A without needing the exact database record for this protein."
  },
  "case_id": "GO_biological_process_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A8I5ZM56, MAP7 domain-containing protein 1, Rattus norvegicus) annotates this protein as a 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' (C5/H2) and assigns GO:0000226 (microtubule cytoskeleton organization) with evidence code ISS:UniProtKB (C6/H3). The sequence matches exactly (849 AA, SHA256 confirmed). The GO annotation is inferred by similarity (ISS), not direct experiment on this exact protein, but the functional description and family assignment are consistent and directly support option A."
  },
  "important_caveats": [
    "The GO annotation for this protein carries evidence code ISS (Inferred from Sequence or Structural Similarity), meaning it is transferred by homology rather than directly experimentally validated on this exact rat protein.",
    "The MAP7 domain family is less widely studied than MAP1/2/4/tau; a model unfamiliar with the specific MAP7 subfamily might rely more heavily on the general coiled-coil/proline-rich signature shared with other MAPs.",
    "The reviewer-only evidence confirms the protein identity (MAP7D1, rat) but this was not available to the evaluated model; the reasoning above relies solely on sequence features and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated as a plant-specific term. Option B lacks supporting structural features (no enzymatic or adaptor domains). Option C lacks protease/chaperone features. Option A is the only choice consistent with the MAP-family sequence signature. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A8I5ZM56, MAP7 domain-containing protein 1, Rattus norvegicus) annotates this protein as a 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' (C5/H2) and assigns GO:0000226 (microtubule cytoskeleton organization) with evidence code ISS:UniProtKB (C6/H3). The sequence matches exactly (849 AA, SHA256 confirmed). The GO annotation is inferred by similarity (ISS), not direct experiment on this exact protein, but the functional description and family assignment are consistent and directly support option A.",
    "evidence_ids": ["C5", "C6", "H2", "H3", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 849-aa sequence displays hallmark features of microtubule-associated protein (MAP) family members: (1) extensive coiled-coil regions with heptad-like alternating charged residues (e.g., 'AKERREERAKYLAAKKAVWLEKEEKAKALREKQLQERRRRLEEQRLKAEQRRAALEERQRQKLEKNKERYEAAIQRSVKKTWAEIRQQRW' and 'EATRLLAEKRRQAREQREREEQERKLQAERDKRMREEQLAREAEARAEREAEARRREEQEAREKAQAEQEEQERLQKQKEEAEARSREEAERQRLEREKHFQKEEQERQERRKRLEEIMKRTRKSEAAETKK'), (2) multiple proline-rich segments ('PSPPPPPTPMSALVPDTPPDTPPAMKNASTPQQLPLEPVSPTGQVSPQPAPPP'), and (3) serine/threonine-rich stretches. These compositional and structural motifs are well-established signatures of the MAP superfamily (MAP1, MAP2, MAP4, MAP7, tau), all of which are characterized by long coiled-coil and proline-rich regions and function in microtubule stabilization and cytoskeleton organization. Option D (regulation of root development) is trivially eliminated as a plant-specific GO term in a clearly mammalian sequence. Option B (positive regulation of signal transduction) would typically require enzymatic domains (kinase, GTPase, SH2/SH3) absent here. Option C (protein-containing complex disassembly) implies protease or chaperone activity not suggested by the sequence. The MAP-family sequence signature thus meaningfully distinguishes A from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the coiled-coil/proline-rich/serine-rich composition as characteristic of the MAP family, which is broadly associated with microtubule cytoskeleton organization. This family-level inference, combined with elimination of the plant-specific option D and the lack of enzymatic domains for B and C, provides a credible transferable basis for selecting A without needing the exact database record for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated as a plant-specific term. Option B lacks supporting structural features (no enzymatic or adaptor domains). Option C lacks protease/chaperone features. Option A is the only choice consistent with the MAP-family sequence signature. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The GO annotation for this protein carries evidence code ISS (Inferred from Sequence or Structural Similarity), meaning it is transferred by homology rather than directly experimentally validated on this exact rat protein.",
    "The MAP7 domain family is less widely studied than MAP1/2/4/tau; a model unfamiliar with the specific MAP7 subfamily might rely more heavily on the general coiled-coil/proline-rich signature shared with other MAPs.",
    "The reviewer-only evidence confirms the protein identity (MAP7D1, rat) but this was not available to the evaluated model; the reasoning above relies solely on sequence features and family-level knowledge."
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
  "benchmark_sequence_length": 849,
  "benchmark_sequence_sha256": "e40be7cea874b3cdc5cdcf1568de90f16d0cc0c2bc5e968f33da781f9868a87f",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-05-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1ebde045dc5cd2279bede8623441f3126cf1702b9f410da8cdc64ae95a8cdfc5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 849,
  "current_source_sequence_sha256": "e40be7cea874b3cdc5cdcf1568de90f16d0cc0c2bc5e968f33da781f9868a87f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A8I5ZM56",
  "selected_historical_entry_version": 18,
  "selected_historical_record_sha256": "ee69cffcb1959a398f57c781fc9212a6b8142d932b2370924cde96c6cc19a50b",
  "selected_historical_source_sequence_length": 849,
  "selected_historical_source_sequence_sha256": "e40be7cea874b3cdc5cdcf1568de90f16d0cc0c2bc5e968f33da781f9868a87f",
  "selected_historical_version": {
    "accession": "A0A8I5ZM56",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MA7D1_RAT",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A8I5ZM56\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:57.465249+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ebde045dc5cd2279bede8623441f3126cf1702b9f410da8cdc64ae95a8cdfc5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-05-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:57.465249+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ebde045dc5cd2279bede8623441f3126cf1702b9f410da8cdc64ae95a8cdfc5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rat\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:57.465249+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ebde045dc5cd2279bede8623441f3126cf1702b9f410da8cdc64ae95a8cdfc5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"value\":\"MAP7 domain-containing protein 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:57.465249+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ebde045dc5cd2279bede8623441f3126cf1702b9f410da8cdc64ae95a8cdfc5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A2AJI0\",\"source\":\"UniProtKB\"}],\"value\":\"Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth. Facilitate microtubule stabilization through the maintenance of acetylated stable microtubules\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:25:57.465249+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ebde045dc5cd2279bede8623441f3126cf1702b9f410da8cdc64ae95a8cdfc5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0000226\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:microtubule cytoskeleton organization\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/26",
  "retrieved_utc": "2026-11-02T04:25:57.465249+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ebde045dc5cd2279bede8623441f3126cf1702b9f410da8cdc64ae95a8cdfc5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I5ZM56?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H1",
  "excerpt": "ID   MA7D1_RAT               Reviewed;         849 AA.\nAC   A0A8I5ZM56; A0A8I5Y1Q7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-MAY-2022, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=MAP7 domain-containing protein 1;\nGN   Name=Map7d1; Synonyms=Mtap7d1;\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:59.955320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee69cffcb1959a398f57c781fc9212a6b8142d932b2370924cde96c6cc19a50b",
  "url": "https://rest.uniprot.org/unisave/A0A8I5ZM56?format=txt&versions=18"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I5ZM56?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H2",
  "excerpt": "CC   -!- FUNCTION: Microtubule-stabilizing protein involved in the control of\nCC       cell motility and neurite outgrowth. Facilitate microtubule\nCC       stabilization through the maintenance of acetylated stable\nCC       microtubules. {ECO:0000250|UniProtKB:A2AJI0}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:59.955320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee69cffcb1959a398f57c781fc9212a6b8142d932b2370924cde96c6cc19a50b",
  "url": "https://rest.uniprot.org/unisave/A0A8I5ZM56?format=txt&versions=18"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I5ZM56?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0000226; P:microtubule cytoskeleton organization; ISS:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:59.955320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee69cffcb1959a398f57c781fc9212a6b8142d932b2370924cde96c6cc19a50b",
  "url": "https://rest.uniprot.org/unisave/A0A8I5ZM56?format=txt&versions=18"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000226\nname: microtubule cytoskeleton organization\nnamespace: biological_process\ndef: \"A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of cytoskeletal structures comprising microtubules and their associated proteins.\" [GOC:mah]\nsubset: goslim_pombe\nsynonym: \"microtubule cytoskeleton organisation\" EXACT [GOC:mah]\nsynonym: \"microtubule cytoskeleton organization and biogenesis\" RELATED [GOC:mah]\nis_a: GO:0007010 ! cytoskeleton organization\nis_a: GO:0007017 ! microtubule-based process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000226",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 2328-2338",
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
  "excerpt": "[Term]\nid: GO:0009967\nname: positive regulation of signal transduction\nnamespace: biological_process\nalt_id: GO:0035468\ndef: \"Any process that activates or increases the frequency, rate or extent of signal transduction.\" [GOC:sm]\nsynonym: \"activation of signal transduction\" NARROW []\nsynonym: \"positive regulation of signaling pathway\" RELATED []\nsynonym: \"positive regulation of signalling pathway\" RELATED [GOC:mah]\nsynonym: \"stimulation of signal transduction\" NARROW []\nsynonym: \"up regulation of signal transduction\" EXACT []\nsynonym: \"up-regulation of signal transduction\" EXACT []\nsynonym: \"upregulation of signal transduction\" EXACT []\nis_a: GO:0009966 ! regulation of signal transduction\nis_a: GO:0010647 ! positive regulation of cell communication\nis_a: GO:0023056 ! positive regulation of signaling\nis_a: GO:0048584 ! positive regulation of response to stimulus\nrelationship: positively_regulates GO:0007165 ! signal transduction\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009967",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 101522-101540",
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
  "excerpt": "[Term]\nid: GO:0032984\nname: protein-containing complex disassembly\nnamespace: biological_process\nalt_id: GO:0034623\nalt_id: GO:0043241\nalt_id: GO:0043624\ndef: \"The disaggregation of a protein-containing macromolecular complex into its constituent components.\" [GOC:mah]\nsynonym: \"cellular macromolecule complex disassembly\" RELATED []\nsynonym: \"cellular protein complex disassembly\" RELATED []\nsynonym: \"macromolecule complex disassembly\" RELATED []\nsynonym: \"protein complex disassembly\" EXACT []\nis_a: GO:0022411 ! cellular component disassembly\nis_a: GO:0043933 ! protein-containing complex organization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032984",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 192597-192611",
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
  "excerpt": "[Term]\nid: GO:2000280\nname: regulation of root development\nnamespace: biological_process\ndef: \"Any process that modulates the frequency, rate or extent of root development.\" [GOC:obol]\nis_a: GO:0050793 ! regulation of developmental process\nrelationship: regulates GO:0048364 ! root development\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:2000280",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 559758-559765",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 47. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
