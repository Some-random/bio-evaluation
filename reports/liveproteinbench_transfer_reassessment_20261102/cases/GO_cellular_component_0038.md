# GO_cellular_component_0038

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0038.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — transcription regulator complex

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSGHLQAARPYGSPTSMHASLHMPEPNMGPSGMAFPSMAPELYAPPQPLRAPDATSQPAPKAYACSTCGKGFARRSDLARHERIHTGVRPHVCEYPNCGKQFIQRSALTVHQRVHTGEKPHMCERCGKPFSDSSSLARHRRIHSGKRPYKCPYADCQKTFTRRTTLTRHQNHHTGTVEDAARATAEVLARNSVARSASARPTRSEGDQISNHGSPLSTPSPAQRTMSMSPSAELAAANGMQHQYNGNSSLPAHMRTDLHSSSPAATTSSGFSSNVRPTSHPNAYGAAPPPTTLEPSIEGSQGPGSAVGSPHMSSVGWASPSHVASPAHSNSGGNSSYVYPDPDSSYPTNAAAQGQMFYSAAMGLQRPGSAEPGAQSAYKPRQNELWAA

[Multiple Choices]
A. RNA polymerase II transcription regulator complex
B. transcription regulator complex
C. axon
D. protein-DNA complex
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

> The sequence-matched record annotates the protein to transcription regulator complex, matching B. This is computational evidence (IEA:TreeGrafter), not direct experimental evidence that the protein physically occupies such a complex.

Citations as saved: [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains C2H2-type zinc-finger motifs, a transferable feature of many DNA-binding transcription factors; its low-complexity regions are also compatible with transcription-regulatory proteins. That makes a transcription regulator complex a meaningful choice over an axon or a protein-DNA complex. In the GO definition, protein-DNA complex refers to a complex containing DNA as a member, not merely a transcription factor that binds DNA. The sequence does not establish the narrower RNA polymerase II association in A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features support a transcription-regulator interpretation without needing the exact target annotation. They do not, however, establish the more specific RNA polymerase II complex option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A is a narrower kind of transcription regulator complex and therefore is compatible with the broader B category. The sequence supports transcription-factor character but does not resolve whether its complex is specifically associated with RNA polymerase II; the prompt also does not state a rule for choosing the broad category over its narrower subtype.


### Important caveats

- The supplied choices do not include nucleus, despite the prompt describing prediction of a primary cellular location.
- The exact B annotation is computationally inferred; the cited experimental subcellular-location evidence supports nuclear localization, not complex membership.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains C2H2-type zinc-finger motifs, a transferable feature of many DNA-binding transcription factors; its low-complexity regions are also compatible with transcription-regulatory proteins. That makes a transcription regulator complex a meaningful choice over an axon or a protein-DNA complex. In the GO definition, protein-DNA complex refers to a complex containing DNA as a member, not merely a transcription factor that binds DNA. The sequence does not establish the narrower RNA polymerase II association in A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features support a transcription-regulator interpretation without needing the exact target annotation. They do not, however, establish the more specific RNA polymerase II complex option."
  },
  "case_id": "GO_cellular_component_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates the protein to transcription regulator complex, matching B. This is computational evidence (IEA:TreeGrafter), not direct experimental evidence that the protein physically occupies such a complex."
  },
  "important_caveats": [
    "The supplied choices do not include nucleus, despite the prompt describing prediction of a primary cellular location.",
    "The exact B annotation is computationally inferred; the cited experimental subcellular-location evidence supports nuclear localization, not complex membership."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A is a narrower kind of transcription regulator complex and therefore is compatible with the broader B category. The sequence supports transcription-factor character but does not resolve whether its complex is specifically associated with RNA polymerase II; the prompt also does not state a rule for choosing the broad category over its narrower subtype."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates the protein to transcription regulator complex, matching B. This is computational evidence (IEA:TreeGrafter), not direct experimental evidence that the protein physically occupies such a complex.",
    "evidence_ids": ["C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains C2H2-type zinc-finger motifs, a transferable feature of many DNA-binding transcription factors; its low-complexity regions are also compatible with transcription-regulatory proteins. That makes a transcription regulator complex a meaningful choice over an axon or a protein-DNA complex. In the GO definition, protein-DNA complex refers to a complex containing DNA as a member, not merely a transcription factor that binds DNA. The sequence does not establish the narrower RNA polymerase II association in A.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features support a transcription-regulator interpretation without needing the exact target annotation. They do not, however, establish the more specific RNA polymerase II complex option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A is a narrower kind of transcription regulator complex and therefore is compatible with the broader B category. The sequence supports transcription-factor character but does not resolve whether its complex is specifically associated with RNA polymerase II; the prompt also does not state a rule for choosing the broad category over its narrower subtype."
  },
  "important_caveats": [
    "The supplied choices do not include nucleus, despite the prompt describing prediction of a primary cellular location.",
    "The exact B annotation is computationally inferred; the cited experimental subcellular-location evidence supports nuclear localization, not complex membership."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The annotation GO:0005667 (transcription regulator complex) is present in the UniProt entry (evidence C8/H6), though via IEA:TreeGrafter (computational transfer). The protein is named 'C2H2-type transcription factor ZAP1' (C4/H1) and the sequence clearly contains four C2H2 zinc finger motifs. The experimental evidence (C5/H3, C7/H5) supports 'Nucleus' as the subcellular location, which is not among the options. Among the offered choices, 'transcription regulator complex' is the annotated and biologically appropriate term for a DNA-binding transcription factor. The answer is supported as a database annotation, albeit computational rather than experimental.

Citations as saved: [C8](#evidence-c8), [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains four tandem C2H2 zinc finger motifs (CGK...H...H pattern repeated), identifying it as a zinc finger transcription factor. This immediately eliminates C (axon), which is a neuronal structure irrelevant to fungal zinc finger proteins, and D (protein-DNA complex), which the GO ontology explicitly excludes for transcription factor complexes (GO3 note: 'Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here'). Between A and B: 'RNA polymerase II transcription regulator complex' (GO:0090575) refers to a specific, characterized multi-protein complex acting at Pol II regulatory regions, while 'transcription regulator complex' (GO:0005667) is the broader parent term appropriate for a DNA-binding transcription factor whose specific polymerase-associated complex assembly has not been experimentally defined. Transferable knowledge of GO annotation conventions indicates that the broader term is the default when the specific RNA Pol II complex membership is not established. Additionally, a single zinc finger protein functioning through direct DNA binding is more naturally described as part of a general transcription regulatory assembly rather than a dedicated 'RNA Pol II transcription regulator complex.'


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The C2H2 zinc finger pattern identifies the protein as a transcription factor, eliminating C and D through well-known biology and GO annotation conventions. The distinction between A and B relies on transferable knowledge of GO term specificity: the broader term is the appropriate annotation when specific polymerase-complex membership is not experimentally characterized, which is the typical default for transferred annotations of individual zinc finger proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> GO:0090575 (option A) is_a GO:0005667 (option B), so if A is true, B is also true by hierarchy. In fungi, all protein-coding genes are transcribed by RNA Pol II, so a fungal transcription factor could arguably be classified under the more specific term A. A knowledgeable model could reasonably argue for either the broader (B) or more specific (A) term depending on whether it prioritizes annotation conservatism or the biological fact that fungal transcription is exclusively Pol II-mediated. The distinction is subtle and both choices have biological justification.


### Important caveats

- The annotation supporting B is IEA:TreeGrafter (computational similarity transfer), not experimental evidence.
- The experimental evidence (ECO:0000269) supports 'Nucleus' as the subcellular location, which is not among the offered options.
- The GO hierarchy means A and B are not mutually exclusive; the question of 'primary' location is ambiguous when one term is a parent of the other.
- The protein is from Cryphonectria parasitica (a fungus), but this organism identity is not derivable from the sequence alone without database lookup; however, the C2H2 zinc finger family is broadly conserved and the reasoning does not depend on knowing the organism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains four tandem C2H2 zinc finger motifs (CGK...H...H pattern repeated), identifying it as a zinc finger transcription factor. This immediately eliminates C (axon), which is a neuronal structure irrelevant to fungal zinc finger proteins, and D (protein-DNA complex), which the GO ontology explicitly excludes for transcription factor complexes (GO3 note: 'Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here'). Between A and B: 'RNA polymerase II transcription regulator complex' (GO:0090575) refers to a specific, characterized multi-protein complex acting at Pol II regulatory regions, while 'transcription regulator complex' (GO:0005667) is the broader parent term appropriate for a DNA-binding transcription factor whose specific polymerase-associated complex assembly has not been experimentally defined. Transferable knowledge of GO annotation conventions indicates that the broader term is the default when the specific RNA Pol II complex membership is not established. Additionally, a single zinc finger protein functioning through direct DNA binding is more naturally described as part of a general transcription regulatory assembly rather than a dedicated 'RNA Pol II transcription regulator complex.'",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The C2H2 zinc finger pattern identifies the protein as a transcription factor, eliminating C and D through well-known biology and GO annotation conventions. The distinction between A and B relies on transferable knowledge of GO term specificity: the broader term is the appropriate annotation when specific polymerase-complex membership is not experimentally characterized, which is the typical default for transferred annotations of individual zinc finger proteins."
  },
  "case_id": "GO_cellular_component_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "C4",
      "C5",
      "H6",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The annotation GO:0005667 (transcription regulator complex) is present in the UniProt entry (evidence C8/H6), though via IEA:TreeGrafter (computational transfer). The protein is named 'C2H2-type transcription factor ZAP1' (C4/H1) and the sequence clearly contains four C2H2 zinc finger motifs. The experimental evidence (C5/H3, C7/H5) supports 'Nucleus' as the subcellular location, which is not among the options. Among the offered choices, 'transcription regulator complex' is the annotated and biologically appropriate term for a DNA-binding transcription factor. The answer is supported as a database annotation, albeit computational rather than experimental."
  },
  "important_caveats": [
    "The annotation supporting B is IEA:TreeGrafter (computational similarity transfer), not experimental evidence.",
    "The experimental evidence (ECO:0000269) supports 'Nucleus' as the subcellular location, which is not among the offered options.",
    "The GO hierarchy means A and B are not mutually exclusive; the question of 'primary' location is ambiguous when one term is a parent of the other.",
    "The protein is from Cryphonectria parasitica (a fungus), but this organism identity is not derivable from the sequence alone without database lookup; however, the C2H2 zinc finger family is broadly conserved and the reasoning does not depend on knowing the organism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "GO:0090575 (option A) is_a GO:0005667 (option B), so if A is true, B is also true by hierarchy. In fungi, all protein-coding genes are transcribed by RNA Pol II, so a fungal transcription factor could arguably be classified under the more specific term A. A knowledgeable model could reasonably argue for either the broader (B) or more specific (A) term depending on whether it prioritizes annotation conservatism or the biological fact that fungal transcription is exclusively Pol II-mediated. The distinction is subtle and both choices have biological justification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The annotation GO:0005667 (transcription regulator complex) is present in the UniProt entry (evidence C8/H6), though via IEA:TreeGrafter (computational transfer). The protein is named 'C2H2-type transcription factor ZAP1' (C4/H1) and the sequence clearly contains four C2H2 zinc finger motifs. The experimental evidence (C5/H3, C7/H5) supports 'Nucleus' as the subcellular location, which is not among the options. Among the offered choices, 'transcription regulator complex' is the annotated and biologically appropriate term for a DNA-binding transcription factor. The answer is supported as a database annotation, albeit computational rather than experimental.",
    "evidence_ids": ["C8", "C4", "C5", "H6", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains four tandem C2H2 zinc finger motifs (CGK...H...H pattern repeated), identifying it as a zinc finger transcription factor. This immediately eliminates C (axon), which is a neuronal structure irrelevant to fungal zinc finger proteins, and D (protein-DNA complex), which the GO ontology explicitly excludes for transcription factor complexes (GO3 note: 'Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here'). Between A and B: 'RNA polymerase II transcription regulator complex' (GO:0090575) refers to a specific, characterized multi-protein complex acting at Pol II regulatory regions, while 'transcription regulator complex' (GO:0005667) is the broader parent term appropriate for a DNA-binding transcription factor whose specific polymerase-associated complex assembly has not been experimentally defined. Transferable knowledge of GO annotation conventions indicates that the broader term is the default when the specific RNA Pol II complex membership is not established. Additionally, a single zinc finger protein functioning through direct DNA binding is more naturally described as part of a general transcription regulatory assembly rather than a dedicated 'RNA Pol II transcription regulator complex.'",
    "missing_item_specific_fact": "",
    "reason": "The C2H2 zinc finger pattern identifies the protein as a transcription factor, eliminating C and D through well-known biology and GO annotation conventions. The distinction between A and B relies on transferable knowledge of GO term specificity: the broader term is the appropriate annotation when specific polymerase-complex membership is not experimentally characterized, which is the typical default for transferred annotations of individual zinc finger proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "GO:0090575 (option A) is_a GO:0005667 (option B), so if A is true, B is also true by hierarchy. In fungi, all protein-coding genes are transcribed by RNA Pol II, so a fungal transcription factor could arguably be classified under the more specific term A. A knowledgeable model could reasonably argue for either the broader (B) or more specific (A) term depending on whether it prioritizes annotation conservatism or the biological fact that fungal transcription is exclusively Pol II-mediated. The distinction is subtle and both choices have biological justification."
  },
  "important_caveats": [
    "The annotation supporting B is IEA:TreeGrafter (computational similarity transfer), not experimental evidence.",
    "The experimental evidence (ECO:0000269) supports 'Nucleus' as the subcellular location, which is not among the offered options.",
    "The GO hierarchy means A and B are not mutually exclusive; the question of 'primary' location is ambiguous when one term is a parent of the other.",
    "The protein is from Cryphonectria parasitica (a fungus), but this organism identity is not derivable from the sequence alone without database lookup; however, the C2H2 zinc finger family is broadly conserved and the reasoning does not depend on knowing the organism."
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
  "benchmark_sequence_length": 388,
  "benchmark_sequence_sha256": "4bcf4b06c81e67c28e273b2697c49580d95ca989162e84b86e6d6f4cc541ab9f",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-09-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 388,
  "current_source_sequence_sha256": "4bcf4b06c81e67c28e273b2697c49580d95ca989162e84b86e6d6f4cc541ab9f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 11,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9P4XV22",
  "selected_historical_entry_version": 11,
  "selected_historical_record_sha256": "ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803",
  "selected_historical_source_sequence_length": 388,
  "selected_historical_source_sequence_sha256": "4bcf4b06c81e67c28e273b2697c49580d95ca989162e84b86e6d6f4cc541ab9f",
  "selected_historical_version": {
    "accession": "A0A9P4XV22",
    "database": "Swiss-Prot",
    "entryVersion": 11,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ZAP1_CRYP1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9P4XV22\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:16.008633+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-09-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:16.008633+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Diaporthales\",\"Cryphonectriaceae\",\"Cryphonectria-Endothia species complex\",\"Cryphonectria\"],\"scientificName\":\"Cryphonectria parasitica (strain ATCC 38755 / EP155)\",\"taxonId\":660469}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:16.008633+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39611846\",\"source\":\"PubMed\"}],\"value\":\"C2H2-type transcription factor ZAP1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:16.008633+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39611846\",\"source\":\"PubMed\"}],\"id\":\"SL-0191\",\"value\":\"Nucleus\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:16.008633+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0000785\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:chromatin\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:26:16.008633+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39611846\",\"source\":\"PubMed\"}],\"id\":\"GO:0005634\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleus\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-02T04:26:16.008633+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005667\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:transcription regulator complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-02T04:26:16.008633+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhao L.\",\"Wei X.\",\"Chen F.\",\"Chen B.\",\"Li R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39611846\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.01844-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0184424\",\"id\":\"39611846\",\"journal\":\"MBio\",\"lastPage\":\"e0184424\",\"publicationDate\":\"2025\",\"title\":\"m6A demethylase CpALKBH regulates CpZap1 mRNA stability to modulate the development and virulence of chestnut blight fungus.\",\"volume\":\"16\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:16.008633+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H1",
  "excerpt": "ID   ZAP1_CRYP1              Reviewed;         388 AA.\nAC   A0A9P4XV22;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-SEP-2023, sequence version 1.\nDT   28-JAN-2026, entry version 11.\nDE   RecName: Full=C2H2-type transcription factor ZAP1 {ECO:0000303|PubMed:39611846};\nGN   Name=ZAP1 {ECO:0000303|PubMed:39611846}; ORFNames=M406DRAFT_281560;\nOS   Cryphonectria parasitica (strain ATCC 38755 / EP155).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Diaporthales; Cryphonectriaceae;\nOC   Cryphonectria-Endothia species complex; Cryphonectria.\nOX   NCBI_TaxID=660469;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:18.672095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803",
  "url": "https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, SUBCELLULAR LOCATION, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39611846; DOI=10.1128/mbio.01844-24;\nRA   Zhao L., Wei X., Chen F., Chen B., Li R.;\nRT   \"m6A demethylase CpALKBH regulates CpZap1 mRNA stability to modulate the\nRT   development and virulence of chestnut blight fungus.\";\nRL   MBio 16:e0184424-e0184424(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:18.672095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803",
  "url": "https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:39611846}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:18.672095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803",
  "url": "https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0000785; C:chromatin; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:18.672095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803",
  "url": "https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005634; C:nucleus; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:18.672095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803",
  "url": "https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005667; C:transcription regulator complex; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:18.672095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803",
  "url": "https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11"
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0032993\nname: protein-DNA complex\nnamespace: cellular_component\ndef: \"A macromolecular complex containing both protein and DNA molecules.\" [GOC:mah]\ncomment: Note that this term is intended to classify complexes that have DNA as one of the members of the complex, that is, the complex does not exist if DNA is not present. Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here.\nsubset: goslim_pir\nsynonym: \"DNA-protein complex\" EXACT [GOC:mah]\nis_a: GO:0032991 ! protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032993",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 192695-192704",
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
  "excerpt": "[Term]\nid: GO:0090575\nname: RNA polymerase II transcription regulator complex\nnamespace: cellular_component\ndef: \"A transcription factor complex that acts at a regulatory region of a gene transcribed by RNA polymerase II.\" [GOC:tb]\nsynonym: \"RNA polymerase II transcription factor complex\" NARROW []\nis_a: GO:0005667 ! transcription regulator complex\nis_a: GO:0140513 ! nuclear protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0090575",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 400139-400147",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
