# GO_cellular_component_0174

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — nucleus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELCGNVMTNSKYEMFRLKCLYCSIESELKDWELFIVHVKSAHYCEDEDVRINEIKEDTEELYSVVDAADPAIAYGPDEFFEVIENSNGVDQWMEADSKDIQYEEDATAWSAATNNSWEFGPGGSSLELPAGKEVTQMDESSQNHIPLNTDDDDVDCSDFFMSEDDLAPPRKPGRPPRRTRPGQVFKFKVSFIRSNPRVLHLIQAYKEHPCLWNPSDEHYQDEPARSMAYEAIMERMDRKANVLFTVEELKKTLEQLHVQYTLALETKQRGKLVGLAARYFAKCEFLSVAPVVTPRENEEDNDLTAIKLNFKEENLITTSFIETYANYPVLYNQALPDFGSIEIRADAFKRMAKEFQPVVKANETDVYIAVNKLRRWLYDAIRRLKSKELIQKCSKQEVQYLQMCSFLPAKGSESQVLYCDYCDKRFHGDYNLRVHIVKAHEVGDLPYLCSFCPRRFDRHVDMDRHKLRSHFERKLKCQYCEKSFAVDTDLKVHTLIHTGERPHVCDICGKTFRLKLLLDHHVNGVHLNIRPYSCNMCTKTFRKKFELANHIKGHLNIRDKKCEYCDATFYDHSSLSRHRRSHRSE

[Multiple Choices]
A. nucleus
B. membrane attack complex
C. transcription regulator complex
D. SCF ubiquitin ligase complex
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched historical UniProt record reports nucleus localization with experimental evidence, including binding to chromatin and distribution between chromatin and nucleoplasm.

Citations as saved: [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has basic regions and multiple Cys/His-rich motifs consistent with nuclear localization and DNA-binding zinc-finger domains. Along with its likely DNA-binding character, this favors the nucleus over a membrane attack complex or SCF ligase complex; the sequence does not establish membership in a transcription regulator complex.


**Missing item-specific fact**

> No protein-specific annotation is necessary to favor the nucleus, though direct localization evidence would be needed to establish the particular protein's actual localization experimentally.


**Reason**

> The sequence provides a meaningful biological basis for favoring nuclear localization, while the choices representing distinct complexes require evidence of complex membership not supplied by sequence motifs alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The nuclear DNA-binding features favor A. The protein might participate in a transcription-regulatory complex, but that membership is not established by the supplied sequence.


### Important caveats

- The experimental localization evidence is reviewer-only and was not provided to the evaluated model.
- The historical sequence-matched record supports the key; the exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has basic regions and multiple Cys/His-rich motifs consistent with nuclear localization and DNA-binding zinc-finger domains. Along with its likely DNA-binding character, this favors the nucleus over a membrane attack complex or SCF ligase complex; the sequence does not establish membership in a transcription regulator complex.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is necessary to favor the nucleus, though direct localization evidence would be needed to establish the particular protein's actual localization experimentally.",
    "reason": "The sequence provides a meaningful biological basis for favoring nuclear localization, while the choices representing distinct complexes require evidence of complex membership not supplied by sequence motifs alone."
  },
  "case_id": "GO_cellular_component_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record reports nucleus localization with experimental evidence, including binding to chromatin and distribution between chromatin and nucleoplasm."
  },
  "important_caveats": [
    "The experimental localization evidence is reviewer-only and was not provided to the evaluated model.",
    "The historical sequence-matched record supports the key; the exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The nuclear DNA-binding features favor A. The protein might participate in a transcription-regulatory complex, but that membership is not established by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record reports nucleus localization with experimental evidence, including binding to chromatin and distribution between chromatin and nucleoplasm.",
    "evidence_ids": ["H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has basic regions and multiple Cys/His-rich motifs consistent with nuclear localization and DNA-binding zinc-finger domains. Along with its likely DNA-binding character, this favors the nucleus over a membrane attack complex or SCF ligase complex; the sequence does not establish membership in a transcription regulator complex.",
    "missing_item_specific_fact": "No protein-specific annotation is necessary to favor the nucleus, though direct localization evidence would be needed to establish the particular protein's actual localization experimentally.",
    "reason": "The sequence provides a meaningful biological basis for favoring nuclear localization, while the choices representing distinct complexes require evidence of complex membership not supplied by sequence motifs alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The nuclear DNA-binding features favor A. The protein might participate in a transcription-regulatory complex, but that membership is not established by the supplied sequence."
  },
  "important_caveats": [
    "The experimental localization evidence is reviewer-only and was not provided to the evaluated model.",
    "The historical sequence-matched record supports the key; the exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q1LZ24, Mzfp1/Clifford) is experimentally confirmed to localize to the nucleus (GO:0005634, EXP evidence from PubMed:38769058), as well as chromosome and nucleoplasm. The subcellular location comment states it binds euchromatin and heterochromatin bands on polytene chromosomes and is distributed between chromatin and nucleoplasm. 'Nucleus' is the correct broad cellular compartment. The other options are clearly incompatible: membrane attack complex (complement system), SCF ubiquitin ligase complex (requires F-box/cullin/RING architecture absent here), and transcription regulator complex (the protein is an architectural/chromatin protein, not annotated as a transcription regulator complex component).

Citations as saved: [C5](#evidence-c5), [C9](#evidence-c9), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO4](#evidence-go4), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region contains multiple tandem C2H2 zinc finger motifs (recurring C-x(2,4)-C-x(12)-H-x(3,5)-H patterns, e.g., 'CSKQEVQYLQMCSFLPAKGSESQVLYCDYCDKRFHGDYNLRVHIVKAHEVGDLPYLCSFCPRRFDRHVDMDRHKLRSHFERKLKCQYCEKSFAVDTDLKVHTLIHTGERPHVCDICGKTFRLKLLLDHHVNGVHLNIRPYSCNMCTKTFRKKFELANHIKGHLNIRDKKCEYCDATFYDHSSLSRHRRSHRSE'). C2H2 zinc finger proteins are overwhelmingly nuclear DNA-binding proteins. The sequence lacks mitochondrial targeting peptides, signal peptides, and transmembrane helices, ruling out secretory/membrane/mitochondrial compartments. Option B (membrane attack complex) requires complement C6-C9 subunits with entirely different architecture. Option D (SCF complex) requires F-box, cullin, and RING domains absent here. The A vs C distinction is defensible: while the protein affects gene expression, it is an architectural/chromatin protein (interacting with CP190), not a canonical component of a 'transcription regulator complex' as defined in GO.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The tandem C2H2 zinc finger array is a well-known, general biological indicator of nuclear localization. The absence of other targeting signals and the domain architecture (zinc fingers + MADF-like domain, no F-box/cullin/RING) allow elimination of B and D by general knowledge. The A vs C distinction relies on the biological principle that architectural chromatin proteins reside in the nucleus but are not necessarily components of a 'transcription regulator complex.' This is a reasonable inference from domain composition and general biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A protein with multiple zinc fingers that binds chromatin and affects gene expression could be argued to reside in a 'transcription regulator complex' (option C) rather than merely the 'nucleus' (option A). The GO definition of 'transcription regulator complex' is broad ('associating with DNA by direct binding... and regulating transcription'). However, the protein is specifically an architectural/insulator protein rather than a classic transcription factor complex component, and 'nucleus' is the experimentally confirmed primary compartment. The ambiguity is minor since B and D are clearly eliminable, and the broader 'nucleus' is the safer, more defensible answer for a chromatin-associated protein.


### Important caveats

- The protein was only annotated in UniProt/Swiss-Prot starting 2025-02-05 (entry Q1LZ24, first public date). The key experimental paper (PubMed:38769058) was published in 2024. The benchmark's author source snapshot is unknown; if constructed before 2025, this protein may not have had a Swiss-Prot entry at the time.
- The nuclear localization evidence (ECO:0000269) is experimental (immunofluorescence on polytene chromosomes), not merely computational inference.
- The distinction between 'nucleus' and 'transcription regulator complex' depends on whether an architectural/insulator protein qualifies as part of a 'transcription regulator complex'—a judgment that could go either way depending on interpretation.
- The reviewer-only accession identification was inferred from dataset metadata absent from the model input; the model must reason from sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains multiple tandem C2H2 zinc finger motifs (recurring C-x(2,4)-C-x(12)-H-x(3,5)-H patterns, e.g., 'CSKQEVQYLQMCSFLPAKGSESQVLYCDYCDKRFHGDYNLRVHIVKAHEVGDLPYLCSFCPRRFDRHVDMDRHKLRSHFERKLKCQYCEKSFAVDTDLKVHTLIHTGERPHVCDICGKTFRLKLLLDHHVNGVHLNIRPYSCNMCTKTFRKKFELANHIKGHLNIRDKKCEYCDATFYDHSSLSRHRRSHRSE'). C2H2 zinc finger proteins are overwhelmingly nuclear DNA-binding proteins. The sequence lacks mitochondrial targeting peptides, signal peptides, and transmembrane helices, ruling out secretory/membrane/mitochondrial compartments. Option B (membrane attack complex) requires complement C6-C9 subunits with entirely different architecture. Option D (SCF complex) requires F-box, cullin, and RING domains absent here. The A vs C distinction is defensible: while the protein affects gene expression, it is an architectural/chromatin protein (interacting with CP190), not a canonical component of a 'transcription regulator complex' as defined in GO.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The tandem C2H2 zinc finger array is a well-known, general biological indicator of nuclear localization. The absence of other targeting signals and the domain architecture (zinc fingers + MADF-like domain, no F-box/cullin/RING) allow elimination of B and D by general knowledge. The A vs C distinction relies on the biological principle that architectural chromatin proteins reside in the nucleus but are not necessarily components of a 'transcription regulator complex.' This is a reasonable inference from domain composition and general biology."
  },
  "case_id": "GO_cellular_component_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C9",
      "C6",
      "C7",
      "C8",
      "GO1",
      "GO2",
      "GO4",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The protein (Q1LZ24, Mzfp1/Clifford) is experimentally confirmed to localize to the nucleus (GO:0005634, EXP evidence from PubMed:38769058), as well as chromosome and nucleoplasm. The subcellular location comment states it binds euchromatin and heterochromatin bands on polytene chromosomes and is distributed between chromatin and nucleoplasm. 'Nucleus' is the correct broad cellular compartment. The other options are clearly incompatible: membrane attack complex (complement system), SCF ubiquitin ligase complex (requires F-box/cullin/RING architecture absent here), and transcription regulator complex (the protein is an architectural/chromatin protein, not annotated as a transcription regulator complex component)."
  },
  "important_caveats": [
    "The protein was only annotated in UniProt/Swiss-Prot starting 2025-02-05 (entry Q1LZ24, first public date). The key experimental paper (PubMed:38769058) was published in 2024. The benchmark's author source snapshot is unknown; if constructed before 2025, this protein may not have had a Swiss-Prot entry at the time.",
    "The nuclear localization evidence (ECO:0000269) is experimental (immunofluorescence on polytene chromosomes), not merely computational inference.",
    "The distinction between 'nucleus' and 'transcription regulator complex' depends on whether an architectural/insulator protein qualifies as part of a 'transcription regulator complex'—a judgment that could go either way depending on interpretation.",
    "The reviewer-only accession identification was inferred from dataset metadata absent from the model input; the model must reason from sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A protein with multiple zinc fingers that binds chromatin and affects gene expression could be argued to reside in a 'transcription regulator complex' (option C) rather than merely the 'nucleus' (option A). The GO definition of 'transcription regulator complex' is broad ('associating with DNA by direct binding... and regulating transcription'). However, the protein is specifically an architectural/insulator protein rather than a classic transcription factor complex component, and 'nucleus' is the experimentally confirmed primary compartment. The ambiguity is minor since B and D are clearly eliminable, and the broader 'nucleus' is the safer, more defensible answer for a chromatin-associated protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q1LZ24, Mzfp1/Clifford) is experimentally confirmed to localize to the nucleus (GO:0005634, EXP evidence from PubMed:38769058), as well as chromosome and nucleoplasm. The subcellular location comment states it binds euchromatin and heterochromatin bands on polytene chromosomes and is distributed between chromatin and nucleoplasm. 'Nucleus' is the correct broad cellular compartment. The other options are clearly incompatible: membrane attack complex (complement system), SCF ubiquitin ligase complex (requires F-box/cullin/RING architecture absent here), and transcription regulator complex (the protein is an architectural/chromatin protein, not annotated as a transcription regulator complex component).",
    "evidence_ids": ["C5", "C9", "C6", "C7", "C8", "GO1", "GO2", "GO4", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region contains multiple tandem C2H2 zinc finger motifs (recurring C-x(2,4)-C-x(12)-H-x(3,5)-H patterns, e.g., 'CSKQEVQYLQMCSFLPAKGSESQVLYCDYCDKRFHGDYNLRVHIVKAHEVGDLPYLCSFCPRRFDRHVDMDRHKLRSHFERKLKCQYCEKSFAVDTDLKVHTLIHTGERPHVCDICGKTFRLKLLLDHHVNGVHLNIRPYSCNMCTKTFRKKFELANHIKGHLNIRDKKCEYCDATFYDHSSLSRHRRSHRSE'). C2H2 zinc finger proteins are overwhelmingly nuclear DNA-binding proteins. The sequence lacks mitochondrial targeting peptides, signal peptides, and transmembrane helices, ruling out secretory/membrane/mitochondrial compartments. Option B (membrane attack complex) requires complement C6-C9 subunits with entirely different architecture. Option D (SCF complex) requires F-box, cullin, and RING domains absent here. The A vs C distinction is defensible: while the protein affects gene expression, it is an architectural/chromatin protein (interacting with CP190), not a canonical component of a 'transcription regulator complex' as defined in GO.",
    "missing_item_specific_fact": "",
    "reason": "The tandem C2H2 zinc finger array is a well-known, general biological indicator of nuclear localization. The absence of other targeting signals and the domain architecture (zinc fingers + MADF-like domain, no F-box/cullin/RING) allow elimination of B and D by general knowledge. The A vs C distinction relies on the biological principle that architectural chromatin proteins reside in the nucleus but are not necessarily components of a 'transcription regulator complex.' This is a reasonable inference from domain composition and general biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A protein with multiple zinc fingers that binds chromatin and affects gene expression could be argued to reside in a 'transcription regulator complex' (option C) rather than merely the 'nucleus' (option A). The GO definition of 'transcription regulator complex' is broad ('associating with DNA by direct binding... and regulating transcription'). However, the protein is specifically an architectural/insulator protein rather than a classic transcription factor complex component, and 'nucleus' is the experimentally confirmed primary compartment. The ambiguity is minor since B and D are clearly eliminable, and the broader 'nucleus' is the safer, more defensible answer for a chromatin-associated protein."
  },
  "important_caveats": [
    "The protein was only annotated in UniProt/Swiss-Prot starting 2025-02-05 (entry Q1LZ24, first public date). The key experimental paper (PubMed:38769058) was published in 2024. The benchmark's author source snapshot is unknown; if constructed before 2025, this protein may not have had a Swiss-Prot entry at the time.",
    "The nuclear localization evidence (ECO:0000269) is experimental (immunofluorescence on polytene chromosomes), not merely computational inference.",
    "The distinction between 'nucleus' and 'transcription regulator complex' depends on whether an architectural/insulator protein qualifies as part of a 'transcription regulator complex'—a judgment that could go either way depending on interpretation.",
    "The reviewer-only accession identification was inferred from dataset metadata absent from the model input; the model must reason from sequence features alone."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q1LZ24` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 158. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1LZ24.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:34.051385+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38769058","source":"PubMed"}],"value":"Binds to specific bands on both euchromatin and heterochromatin regions of polytene chromosomes (PubMed:38769058). Roughly equally distributed between chromatin and the nucleoplasm (PubMed:38769058)"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38769058","source":"PubMed"}],"id":"SL-0191","value":"Nucleus"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38769058","source":"PubMed"}],"id":"SL-0468","value":"Chromosome"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38769058","source":"PubMed"}],"id":"SL-0190","value":"Nucleus, nucleoplasm"}}]}
```

Source SHA-256: `8417b17d1f69bf26667dccab8593df3ec34ac8b6f5097f7e9ffaa3346b7f81bb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1LZ24.json)  
**Locator:** `/uniProtKBCrossReferences/33`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:34.051385+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"38769058","source":"PubMed"}],"id":"GO:0000785","properties":[{"key":"GoTerm","value":"C:chromatin"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `8417b17d1f69bf26667dccab8593df3ec34ac8b6f5097f7e9ffaa3346b7f81bb`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1LZ24.json)  
**Locator:** `/uniProtKBCrossReferences/34`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:34.051385+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"38769058","source":"PubMed"}],"id":"GO:0005694","properties":[{"key":"GoTerm","value":"C:chromosome"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `8417b17d1f69bf26667dccab8593df3ec34ac8b6f5097f7e9ffaa3346b7f81bb`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1LZ24.json)  
**Locator:** `/uniProtKBCrossReferences/35`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:34.051385+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"38769058","source":"PubMed"}],"id":"GO:0005654","properties":[{"key":"GoTerm","value":"C:nucleoplasm"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `8417b17d1f69bf26667dccab8593df3ec34ac8b6f5097f7e9ffaa3346b7f81bb`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1LZ24.json)  
**Locator:** `/uniProtKBCrossReferences/36`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:34.051385+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"38769058","source":"PubMed"}],"id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `8417b17d1f69bf26667dccab8593df3ec34ac8b6f5097f7e9ffaa3346b7f81bb`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1LZ24?format=txt&versions=158)  
**Locator:** `lines 107-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 158 / 1.  
**Retrieved:** 2026-11-02T04:30:39.255146+00:00.  

```text
RN   [6] {ECO:0000305}
RP   FUNCTION, INTERACTION WITH CP190, SUBCELLULAR LOCATION, MADF AND ZN-FINGER
RP   DOMAINS, AND DISRUPTION PHENOTYPE.
RX   PubMed=38769058; DOI=10.1093/nar/gkae393;
RA   Sokolov V., Kyrchanova O., Klimenko N., Fedotova A., Ibragimov A.,
RA   Maksimenko O., Georgiev P.;
RT   "New Drosophila promoter-associated architectural protein Mzfp1 interacts
RT   with CP190 and is required for housekeeping gene expression and insulator
RT   activity.";
RL   Nucleic Acids Res. 52:6886-6905(2024).
```

Source SHA-256: `2553ad9043073efec2b54ab52177b462c29a5f79fa3e5578f31c32329850e8d6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1LZ24?format=txt&versions=158)  
**Locator:** `lines 138-143`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 158 / 1.  
**Retrieved:** 2026-11-02T04:30:39.255146+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:38769058}. Chromosome
CC       {ECO:0000269|PubMed:38769058}. Nucleus, nucleoplasm
CC       {ECO:0000269|PubMed:38769058}. Note=Binds to specific bands on both
CC       euchromatin and heterochromatin regions of polytene chromosomes
CC       (PubMed:38769058). Roughly equally distributed between chromatin and
CC       the nucleoplasm (PubMed:38769058). {ECO:0000269|PubMed:38769058}.
```

Source SHA-256: `2553ad9043073efec2b54ab52177b462c29a5f79fa3e5578f31c32329850e8d6`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 57517-57530`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005579
name: membrane attack complex
namespace: cellular_component
def: "A protein complex produced by sequentially activated components of the complement cascade inserted into a target cell membrane and forming a pore leading to cell lysis via ion and water flow." [GOC:add, ISBN:0198547684, ISBN:068340007X, ISBN:0781735149]
synonym: "MAC" EXACT []
synonym: "membrane attack complex protein alphaM chain" NARROW []
synonym: "membrane attack complex protein beta2 chain" NARROW []
synonym: "TCC" EXACT []
synonym: "terminal complement complex" EXACT []
xref: Wikipedia:Complement_membrane_attack_complex
is_a: GO:0046930 ! pore complex
is_a: GO:0098797 ! plasma membrane protein complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58002-58025`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005634
name: nucleus
namespace: cellular_component
def: "A membrane-bounded organelle of eukaryotic cells in which chromosomes are housed and replicated. In most cells, the nucleus contains all of the cell's chromosomes except the organellar chromosomes, and is the site of RNA synthesis and processing. In some species, or in specialized cell types, RNA metabolism or DNA replication may be absent." [GOC:curators]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_yeast
synonym: "cell nucleus" EXACT []
synonym: "horsetail nucleus" NARROW [GOC:al, GOC:mah, GOC:vw, PMID:15030757]
xref: NIF_Subcellular:sao1702920020
xref: Wikipedia:Cell_nucleus
is_a: GO:0043231 ! intracellular membrane-bounded organelle

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58346-58358`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005667
name: transcription regulator complex
namespace: cellular_component
alt_id: GO:0044797
alt_id: GO:0044798
def: "A protein complex that is capable of associating with DNA by direct binding, or via other DNA-binding proteins or complexes, and regulating transcription." [GOC:jl]
subset: goslim_pir
synonym: "cytoplasmic transcription factor complex" RELATED []
synonym: "nuclear transcription factor complex" RELATED []
synonym: "transcription factor complex" RELATED []
is_a: GO:0032991 ! protein-containing complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 144478-144492`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0019005
name: SCF ubiquitin ligase complex
namespace: cellular_component
def: "A ubiquitin ligase complex in which a cullin from the Cul1 subfamily and a RING domain protein form the catalytic core; substrate specificity is conferred by a Skp1 adaptor and an F-box protein. SCF complexes are involved in targeting proteins for degradation by the proteasome. The best characterized complexes are those from yeast and mammals (with core subunits named Cdc53/Cul1, Rbx1/Hrt1/Roc1)." [PMID:15571813, PMID:15688063]
synonym: "CDL1 complex" EXACT []
synonym: "CRL1 complex" EXACT []
synonym: "Cul1-RING ubiquitin ligase complex" EXACT []
synonym: "cullin-RING ligase 1" EXACT []
synonym: "SCF complex" EXACT []
synonym: "SCF complex substrate recognition subunit" NARROW []
synonym: "Skp1/Cul1/F-box protein complex" EXACT []
xref: Wikipedia:SCF_complex
is_a: GO:0031461 ! cullin-RING ubiquitin ligase complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 174. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
