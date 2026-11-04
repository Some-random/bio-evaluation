# GO_biological_process_0136

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0136.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **D** — vitelline membrane formation involved in chorion-containing eggshell formation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMMHSRNRSWTLTLLALGVVLATSAEDLPRSNRIAVPGEPLYYLMADAGPVVTPNEALKRTNRSLLKWWDDLFPRNNNNCCNNNNNNLLYPTAPLLPAPAVPNNCNGLQLQDLDPFKQMKLFKKLPELFPTASPCGQCGGGCGQNNYVAPAPQSPSYGGDGYGVLPNGGYIKPDTEYNGPGDGDAGYVAPAAPAYEAPAPPAPAYEAPAPPAPAYEAPAPAAPAYEAPAPAAPAYEAPTTDYSAPAPPAPAYEPPASSYTQGYSQPAQPSYVGAPPAQIVYQPIIYLSTPLASKSSTSQVEYDDQKYVTPTAPPPPPPPAPVYEAPSQNCYQPAAPPAPNYATPSCQTPIRLSLIDQPYRVAPELFEEYNYRLALASQNIL

[Multiple Choices]
A. monoatomic cation transport
B. DNA replication
C. gamete generation
D. vitelline membrane formation involved in chorion-containing eggshell formation
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

> The supplied sequence matches the protein described in the archived source record. That record reports an experimentally supported role in vitelline membrane biogenesis, and its GO annotation assigns the process in option D. This directly supports the keyed answer.

Citations as saved: [H3](#evidence-h3), [H5](#evidence-h5), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal signal-peptide-like region and low-complexity, cysteine-containing sequence are consistent with a secreted extracellular protein, which makes an eggshell-related role plausible and makes ion transport or DNA replication unlikely. But these features do not specifically identify vitelline-membrane formation over other extracellular or reproductive roles.


**Missing item-specific fact**

> The protein-specific functional finding that it contributes to vitelline membrane biogenesis and cross-linking, rather than merely being a secreted protein with an extracellular-matrix-like sequence.


**Reason**

> Transferable sequence features narrow the likely functional class, but do not meaningfully establish the specific vitelline/chorion process needed to select D over the broader gamete-generation option C. The decisive functional fact is specific to this protein and is absent from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Gamete generation is a broad reproductive category related to egg formation, but D is the more specific process directly supported for this protein.


### Important caveats

- The support judgment relies on reviewer-only evidence, not information supplied to the evaluated model.
- The available source evidence identifies D as the direct process; it does not make every broader reproductive category an equally appropriate primary answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal signal-peptide-like region and low-complexity, cysteine-containing sequence are consistent with a secreted extracellular protein, which makes an eggshell-related role plausible and makes ion transport or DNA replication unlikely. But these features do not specifically identify vitelline-membrane formation over other extracellular or reproductive roles.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional finding that it contributes to vitelline membrane biogenesis and cross-linking, rather than merely being a secreted protein with an extracellular-matrix-like sequence.",
    "reason": "Transferable sequence features narrow the likely functional class, but do not meaningfully establish the specific vitelline/chorion process needed to select D over the broader gamete-generation option C. The decisive functional fact is specific to this protein and is absent from the original input."
  },
  "case_id": "GO_biological_process_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H5",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the protein described in the archived source record. That record reports an experimentally supported role in vitelline membrane biogenesis, and its GO annotation assigns the process in option D. This directly supports the keyed answer."
  },
  "important_caveats": [
    "The support judgment relies on reviewer-only evidence, not information supplied to the evaluated model.",
    "The available source evidence identifies D as the direct process; it does not make every broader reproductive category an equally appropriate primary answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Gamete generation is a broad reproductive category related to egg formation, but D is the more specific process directly supported for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the protein described in the archived source record. That record reports an experimentally supported role in vitelline membrane biogenesis, and its GO annotation assigns the process in option D. This directly supports the keyed answer.",
    "evidence_ids": ["H3", "H5", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal signal-peptide-like region and low-complexity, cysteine-containing sequence are consistent with a secreted extracellular protein, which makes an eggshell-related role plausible and makes ion transport or DNA replication unlikely. But these features do not specifically identify vitelline-membrane formation over other extracellular or reproductive roles.",
    "missing_item_specific_fact": "The protein-specific functional finding that it contributes to vitelline membrane biogenesis and cross-linking, rather than merely being a secreted protein with an extracellular-matrix-like sequence.",
    "reason": "Transferable sequence features narrow the likely functional class, but do not meaningfully establish the specific vitelline/chorion process needed to select D over the broader gamete-generation option C. The decisive functional fact is specific to this protein and is absent from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Gamete generation is a broad reproductive category related to egg formation, but D is the more specific process directly supported for this protein."
  },
  "important_caveats": [
    "The support judgment relies on reviewer-only evidence, not information supplied to the evaluated model.",
    "The available source evidence identifies D as the direct process; it does not make every broader reproductive category an equally appropriate primary answer."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VMK3 (Protein palisade, Drosophila melanogaster) carries GO:0007305 'vitelline membrane formation involved in chorion-containing eggshell formation' with evidence code IMP:FlyBase (ECO:0000315, mutant phenotype evidence from PubMed:18514182). The FUNCTION comment explicitly states the protein is a minor component of the vitelline membrane involved in its biogenesis during late oogenesis and required for disulfide and non-disulfide cross-linking of vitelline membrane components. The sequence matches the benchmark input exactly (SHA256 confirmed).

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a clear N-terminal signal peptide (MMMHSRNRSWTLTLLALGVVLATSAEDLPRSNRIAV...), indicating a secreted protein. It contains multiple cysteine clusters (CC, CGQCGGGCGQ, CYQPAAPPAPNYATPSCQTPIRLSLIDQPYRVAPELFEEYNYRLALASQNIL) consistent with extensive disulfide cross-linking. The highly repetitive Gly/Ala/Pro/Tyr regions (APAPPAPAYEAPAPPAPAYE...) are hallmarks of structural assembly proteins in insect eggshells. These combined features—secreted, cysteine-rich for cross-linking, repetitive structural motifs—are well-known signatures of Drosophila and other insect vitelline membrane/chorion assembly proteins (a family-level pattern shared across many characterized egg-coat proteins). This distinguishes D from A (no ion-channel transmembrane topology or conserved ion-binding motifs), from B (no nuclear localization, no helicase/polymerase/DNA-binding domains), and from C (gamete generation is an extremely broad parent term encompassing all aspects of gamete production; the specific cysteine-cross-linking and secreted-assembly architecture points to a structural eggshell-assembly role rather than general gametogenesis machinery such as meiotic or germline-differentiation proteins).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use family-level knowledge of insect eggshell/vitelline membrane proteins (secreted, cysteine-rich, repetitive structural motifs undergoing cross-linking) to recognize the sequence as an egg-coat assembly protein, selecting the specific term D over the very broad parent term C and the clearly unrelated A and B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although GO:0007305 (D) is a descendant of GO:0007276 (C) in the ontology, the question asks for the 'primary biological process' and 'overall biological objective to which the protein contributes.' For a protein whose direct molecular role is vitelline membrane assembly and cross-linking, the most specific and appropriate BP term is D. C is so broad (encompassing all gamete production) that it would not be considered the 'primary' process for a structural eggshell component. The sequence features specifically indicate egg-coat assembly rather than general gametogenesis.


### Important caveats

- The evidence code IMP (Inferred by Mutant Phenotype) indicates experimental genetic evidence from a 2008 developmental biology study (PubMed:18514182), not mere computational annotation.
- The protein is annotated as a 'minor' component of the vitelline membrane, so its role is contributory rather than primary structural.
- The repetitive AP/AY regions could superficially resemble other secreted structural proteins, but the combination with cysteine-rich cross-linking motifs and the overall Drosophila eggshell protein architecture supports the vitelline membrane assignment.
- The GO path shows D is part_of oogenesis which is part_of gamete generation, so a model selecting C would not be strictly 'wrong' in a hierarchy sense, but the question's phrasing ('primary biological process') favors the most specific applicable term.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (MMMHSRNRSWTLTLLALGVVLATSAEDLPRSNRIAV...), indicating a secreted protein. It contains multiple cysteine clusters (CC, CGQCGGGCGQ, CYQPAAPPAPNYATPSCQTPIRLSLIDQPYRVAPELFEEYNYRLALASQNIL) consistent with extensive disulfide cross-linking. The highly repetitive Gly/Ala/Pro/Tyr regions (APAPPAPAYEAPAPPAPAYE...) are hallmarks of structural assembly proteins in insect eggshells. These combined features—secreted, cysteine-rich for cross-linking, repetitive structural motifs—are well-known signatures of Drosophila and other insect vitelline membrane/chorion assembly proteins (a family-level pattern shared across many characterized egg-coat proteins). This distinguishes D from A (no ion-channel transmembrane topology or conserved ion-binding motifs), from B (no nuclear localization, no helicase/polymerase/DNA-binding domains), and from C (gamete generation is an extremely broad parent term encompassing all aspects of gamete production; the specific cysteine-cross-linking and secreted-assembly architecture points to a structural eggshell-assembly role rather than general gametogenesis machinery such as meiotic or germline-differentiation proteins).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use family-level knowledge of insect eggshell/vitelline membrane proteins (secreted, cysteine-rich, repetitive structural motifs undergoing cross-linking) to recognize the sequence as an egg-coat assembly protein, selecting the specific term D over the very broad parent term C and the clearly unrelated A and B."
  },
  "case_id": "GO_biological_process_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VMK3 (Protein palisade, Drosophila melanogaster) carries GO:0007305 'vitelline membrane formation involved in chorion-containing eggshell formation' with evidence code IMP:FlyBase (ECO:0000315, mutant phenotype evidence from PubMed:18514182). The FUNCTION comment explicitly states the protein is a minor component of the vitelline membrane involved in its biogenesis during late oogenesis and required for disulfide and non-disulfide cross-linking of vitelline membrane components. The sequence matches the benchmark input exactly (SHA256 confirmed)."
  },
  "important_caveats": [
    "The evidence code IMP (Inferred by Mutant Phenotype) indicates experimental genetic evidence from a 2008 developmental biology study (PubMed:18514182), not mere computational annotation.",
    "The protein is annotated as a 'minor' component of the vitelline membrane, so its role is contributory rather than primary structural.",
    "The repetitive AP/AY regions could superficially resemble other secreted structural proteins, but the combination with cysteine-rich cross-linking motifs and the overall Drosophila eggshell protein architecture supports the vitelline membrane assignment.",
    "The GO path shows D is part_of oogenesis which is part_of gamete generation, so a model selecting C would not be strictly 'wrong' in a hierarchy sense, but the question's phrasing ('primary biological process') favors the most specific applicable term."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although GO:0007305 (D) is a descendant of GO:0007276 (C) in the ontology, the question asks for the 'primary biological process' and 'overall biological objective to which the protein contributes.' For a protein whose direct molecular role is vitelline membrane assembly and cross-linking, the most specific and appropriate BP term is D. C is so broad (encompassing all gamete production) that it would not be considered the 'primary' process for a structural eggshell component. The sequence features specifically indicate egg-coat assembly rather than general gametogenesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VMK3 (Protein palisade, Drosophila melanogaster) carries GO:0007305 'vitelline membrane formation involved in chorion-containing eggshell formation' with evidence code IMP:FlyBase (ECO:0000315, mutant phenotype evidence from PubMed:18514182). The FUNCTION comment explicitly states the protein is a minor component of the vitelline membrane involved in its biogenesis during late oogenesis and required for disulfide and non-disulfide cross-linking of vitelline membrane components. The sequence matches the benchmark input exactly (SHA256 confirmed).",
    "evidence_ids": ["C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (MMMHSRNRSWTLTLLALGVVLATSAEDLPRSNRIAV...), indicating a secreted protein. It contains multiple cysteine clusters (CC, CGQCGGGCGQ, CYQPAAPPAPNYATPSCQTPIRLSLIDQPYRVAPELFEEYNYRLALASQNIL) consistent with extensive disulfide cross-linking. The highly repetitive Gly/Ala/Pro/Tyr regions (APAPPAPAYEAPAPPAPAYE...) are hallmarks of structural assembly proteins in insect eggshells. These combined features—secreted, cysteine-rich for cross-linking, repetitive structural motifs—are well-known signatures of Drosophila and other insect vitelline membrane/chorion assembly proteins (a family-level pattern shared across many characterized egg-coat proteins). This distinguishes D from A (no ion-channel transmembrane topology or conserved ion-binding motifs), from B (no nuclear localization, no helicase/polymerase/DNA-binding domains), and from C (gamete generation is an extremely broad parent term encompassing all aspects of gamete production; the specific cysteine-cross-linking and secreted-assembly architecture points to a structural eggshell-assembly role rather than general gametogenesis machinery such as meiotic or germline-differentiation proteins).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use family-level knowledge of insect eggshell/vitelline membrane proteins (secreted, cysteine-rich, repetitive structural motifs undergoing cross-linking) to recognize the sequence as an egg-coat assembly protein, selecting the specific term D over the very broad parent term C and the clearly unrelated A and B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although GO:0007305 (D) is a descendant of GO:0007276 (C) in the ontology, the question asks for the 'primary biological process' and 'overall biological objective to which the protein contributes.' For a protein whose direct molecular role is vitelline membrane assembly and cross-linking, the most specific and appropriate BP term is D. C is so broad (encompassing all gamete production) that it would not be considered the 'primary' process for a structural eggshell component. The sequence features specifically indicate egg-coat assembly rather than general gametogenesis."
  },
  "important_caveats": [
    "The evidence code IMP (Inferred by Mutant Phenotype) indicates experimental genetic evidence from a 2008 developmental biology study (PubMed:18514182), not mere computational annotation.",
    "The protein is annotated as a 'minor' component of the vitelline membrane, so its role is contributory rather than primary structural.",
    "The repetitive AP/AY regions could superficially resemble other secreted structural proteins, but the combination with cysteine-rich cross-linking motifs and the overall Drosophila eggshell protein architecture supports the vitelline membrane assignment.",
    "The GO path shows D is part_of oogenesis which is part_of gamete generation, so a model selecting C would not be strictly 'wrong' in a hierarchy sense, but the question's phrasing ('primary biological process') favors the most specific applicable term."
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
  "benchmark_sequence_length": 381,
  "benchmark_sequence_sha256": "8caed05ef2c2b8523afadcf0ad8106baaafc542e1c8c9b20d56f60f4b3c4c6a8",
  "current_entry_audit": {
    "entryVersion": 168,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 381,
  "current_source_sequence_sha256": "8caed05ef2c2b8523afadcf0ad8106baaafc542e1c8c9b20d56f60f4b3c4c6a8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 166,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VMK3",
  "selected_historical_entry_version": 166,
  "selected_historical_record_sha256": "e29e678a73bb740d92e70bafa920eafb90e0bfe6e683dd2672c8a1a7d8834a98",
  "selected_historical_source_sequence_length": 381,
  "selected_historical_source_sequence_sha256": "8caed05ef2c2b8523afadcf0ad8106baaafc542e1c8c9b20d56f60f4b3c4c6a8",
  "selected_historical_version": {
    "accession": "Q9VMK3",
    "database": "Swiss-Prot",
    "entryVersion": 166,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "VTU5_DROME",
    "sequenceVersion": 2
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VMK3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:28.895931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VMK3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":168,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:28.895931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VMK3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:28.895931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VMK3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18514182\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0086265\",\"source\":\"FlyBase\"}],\"value\":\"Protein palisade\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:28.895931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VMK3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18514182\",\"source\":\"PubMed\"}],\"value\":\"Minor protein component of the vitelline membrane (PubMed:18514182). Involved in vitelline membrane biogenesis during late stages of oogenesis (PubMed:18514182). Required for efficient disulfide and non-disulfide cross-linking of several vitelline membrane components (PubMed:18514182)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:33:28.895931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VMK3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000315\",\"id\":\"18514182\",\"source\":\"PubMed\"}],\"id\":\"GO:0032529\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:follicle cell microvillus organization\"},{\"key\":\"GoEvidenceType\",\"value\":\"IMP:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/33",
  "retrieved_utc": "2026-11-02T04:33:28.895931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VMK3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000315\",\"id\":\"18514182\",\"source\":\"PubMed\"}],\"id\":\"GO:0007305\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:vitelline membrane formation involved in chorion-containing eggshell formation\"},{\"key\":\"GoEvidenceType\",\"value\":\"IMP:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/34",
  "retrieved_utc": "2026-11-02T04:33:28.895931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VMK3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VMK3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Elalayli M.\",\"Hall J.D.\",\"Fakhouri M.\",\"Neiswender H.\",\"Ellison T.T.\",\"Han Z.\",\"Roon P.\",\"LeMosy E.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18514182\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ydbio.2008.04.035\"}],\"citationType\":\"journal article\",\"firstPage\":\"359\",\"id\":\"18514182\",\"journal\":\"Dev. Biol.\",\"lastPage\":\"369\",\"publicationDate\":\"2008\",\"title\":\"Palisade is required in the Drosophila ovary for assembly and function of the protective vitelline membrane.\",\"volume\":\"319\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DEVELOPMENTAL STAGE\",\"CROSS-LINKING\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:28.895931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1129d33a731f9c47e5ca28a66a290894bdb1049cb685a2c60663450523fe78a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VMK3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166)

```json
{
  "entry_version": 166,
  "evidence_id": "H1",
  "excerpt": "ID   VTU5_DROME              Reviewed;         381 AA.\nAC   Q9VMK3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 2.\nDT   28-JAN-2026, entry version 166.\nDE   RecName: Full=Protein palisade {ECO:0000303|PubMed:18514182, ECO:0000312|FlyBase:FBgn0086265};\nDE   Flags: Precursor;\nGN   Name=psd {ECO:0000303|PubMed:18514182, ECO:0000312|FlyBase:FBgn0086265};\nGN   Synonyms=TU-1 {ECO:0000312|FlyBase:FBgn0086265};\nGN   ORFNames=CG9050 {ECO:0000312|FlyBase:FBgn0086265};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:31.077925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e29e678a73bb740d92e70bafa920eafb90e0bfe6e683dd2672c8a1a7d8834a98",
  "url": "https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166)

```json
{
  "entry_version": 166,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, TISSUE SPECIFICITY, DEVELOPMENTAL STAGE,\nRP   CROSS-LINKING, AND DISRUPTION PHENOTYPE.\nRX   PubMed=18514182; DOI=10.1016/j.ydbio.2008.04.035;\nRA   Elalayli M., Hall J.D., Fakhouri M., Neiswender H., Ellison T.T., Han Z.,\nRA   Roon P., LeMosy E.K.;\nRT   \"Palisade is required in the Drosophila ovary for assembly and function of\nRT   the protective vitelline membrane.\";\nRL   Dev. Biol. 319:359-369(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:31.077925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e29e678a73bb740d92e70bafa920eafb90e0bfe6e683dd2672c8a1a7d8834a98",
  "url": "https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166)

```json
{
  "entry_version": 166,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Minor protein component of the vitelline membrane\nCC       (PubMed:18514182). Involved in vitelline membrane biogenesis during\nCC       late stages of oogenesis (PubMed:18514182). Required for efficient\nCC       disulfide and non-disulfide cross-linking of several vitelline membrane\nCC       components (PubMed:18514182). {ECO:0000269|PubMed:18514182}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:31.077925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e29e678a73bb740d92e70bafa920eafb90e0bfe6e683dd2672c8a1a7d8834a98",
  "url": "https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166)

```json
{
  "entry_version": 166,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0032529; P:follicle cell microvillus organization; IMP:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:31.077925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 155-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e29e678a73bb740d92e70bafa920eafb90e0bfe6e683dd2672c8a1a7d8834a98",
  "url": "https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166)

```json
{
  "entry_version": 166,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0007305; P:vitelline membrane formation involved in chorion-containing eggshell formation; IMP:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:31.077925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 156-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e29e678a73bb740d92e70bafa920eafb90e0bfe6e683dd2672c8a1a7d8834a98",
  "url": "https://rest.uniprot.org/unisave/Q9VMK3?format=txt&versions=166"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006260\nname: DNA replication\nnamespace: biological_process\nalt_id: GO:0055133\ndef: \"The cellular metabolic process in which a cell duplicates one or more molecules of DNA. DNA replication begins when specific sequences, known as origins of replication, are recognized and bound by the origin recognition complex, and ends when the original DNA molecule has been completely duplicated and the copies topologically separated. The unit of replication usually corresponds to the genome of the cell, an organelle, or a virus. The template for replication can either be an existing DNA molecule or RNA.\" [GOC:mah]\ncomment: DNA biosynthesis is only part of this process. See also the biological process terms 'DNA-dependent DNA replication ; GO:0006261' and 'RNA-dependent DNA replication ; GO:0006278'.\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_pir\nsubset: goslim_pombe\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nxref: Reactome:R-HSA-176187 \"Activation of ATR in response to replication stress\"\nxref: Reactome:R-HSA-69239 \"Synthesis of DNA\"\nxref: Wikipedia:DNA_replication\nis_a: GO:0006259 ! DNA metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006260",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 64550-64568",
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
  "excerpt": "[Term]\nid: GO:0006812\nname: monoatomic cation transport\nnamespace: biological_process\nalt_id: GO:0006819\nalt_id: GO:0015674\nalt_id: GO:0072512\ndef: \"The directed movement of a monoatomic cation, into, out of or within a cell, or between cells, by means of some agent such as a transporter or pore. Monatomic cations (also called simple cations) are positively charged ions consisting of exactly one atom.\" [GOC:ai]\nsynonym: \"cation transport\" BROAD []\nsynonym: \"di-, tri-valent inorganic cation transport\" NARROW [GOC:mah]\nsynonym: \"trivalent inorganic cation transport\" NARROW []\nis_a: GO:0006811 ! monoatomic ion transport\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006812",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 70615-70627",
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
  "excerpt": "[Term]\nid: GO:0007276\nname: gamete generation\nnamespace: biological_process\nalt_id: GO:0009552\ndef: \"The generation and maintenance of gametes in a multicellular organism. A gamete is a haploid reproductive cell.\" [GOC:ems, GOC:mtg_sensu]\nsynonym: \"gametogenesis\" RELATED []\nis_a: GO:0048609 ! multicellular organismal reproductive process\nrelationship: part_of GO:0019953 ! sexual reproduction\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007276",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 75115-75124",
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
  "excerpt": "[Term]\nid: GO:0007281\nname: germ cell development\nnamespace: biological_process\ndef: \"The process whose specific outcome is the progression of an immature germ cell over time, from its formation to the mature structure (gamete). A germ cell is any reproductive cell in a multicellular organism.\" [GOC:curators]\nsynonym: \"gametogenesis\" NARROW []\nsynonym: \"germ-cell development\" EXACT []\nsynonym: \"primordial germ cell development\" NARROW []\nxref: Reactome:R-HSA-9827857 \"Specification of primordial germ cells\"\nis_a: GO:0003006 ! developmental process involved in reproduction\nis_a: GO:0022412 ! cellular process involved in reproduction in multicellular organism\nis_a: GO:0048468 ! cell development\nrelationship: part_of GO:0007276 ! gamete generation\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007281",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 75162-75175",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0007305\nname: vitelline membrane formation involved in chorion-containing eggshell formation\nnamespace: biological_process\ndef: \"Construction of the vitelline membrane portion of a chorion-containing eggshell. An example of this is found in Drosophila melanogaster.\" [GOC:mah, GOC:mtg_sensu]\nsynonym: \"vitelline membrane formation in chorion-containing eggshell\" EXACT [GOC:dph, GOC:tb]\nis_a: GO:0030704 ! vitelline membrane formation\nrelationship: part_of GO:0007304 ! chorion-containing eggshell formation\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007305",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 75393-75401",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "excerpt": "[Term]\nid: GO:0030704\nname: vitelline membrane formation\nnamespace: biological_process\ndef: \"Construction of the vitelline membrane portion of the egg shell, a rigid structure required to maintain the shape of the egg.\" [ISBN:0879694238]\nis_a: GO:0003006 ! developmental process involved in reproduction\nis_a: GO:0010927 ! cellular component assembly involved in morphogenesis\nis_a: GO:0035803 ! egg coat formation\nis_a: GO:0085029 ! extracellular matrix assembly\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030704",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 168689-168698",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO7

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO7",
  "excerpt": "[Term]\nid: GO:0035803\nname: egg coat formation\nnamespace: biological_process\ndef: \"Construction of an egg coat, a specialized extracellular matrix that surrounds the ovum of animals. The egg coat provides structural support and can play an essential role in oogenesis, fertilization and early development.\" [GOC:bf, GOC:sart, GOC:yaf, PMID:16944418, PMID:17163408]\nsynonym: \"VE formation\" NARROW [PMID:16944418, PMID:17163408]\nsynonym: \"vitelline envelope formation\" NARROW [PMID:16944418]\nsynonym: \"zona pellucida assembly\" NARROW [GOC:yaf, PMID:18420282]\nsynonym: \"ZP assembly\" NARROW [PMID:18420282]\nis_a: GO:0022412 ! cellular process involved in reproduction in multicellular organism\nrelationship: part_of GO:0048477 ! oogenesis\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0035803",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 221399-221410",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO8

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO8",
  "excerpt": "[Term]\nid: GO:0048477\nname: oogenesis\nnamespace: biological_process\nalt_id: GO:0009993\nalt_id: GO:0048157\ndef: \"The complete process of formation and maturation of an ovum or female gamete from a primordial female germ cell. Examples of this process are found in Mus musculus and Drosophila melanogaster.\" [GOC:kmv, GOC:mtg_sensu, GOC:pr]\nsynonym: \"ovum development\" EXACT systematic_synonym []\nxref: Wikipedia:Oogenesis\nis_a: GO:0007281 ! germ cell development\nis_a: GO:0007292 ! female gamete generation\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0048477",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 303571-303582",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
