# GO_molecular_function_0136

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0136.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — hydrolase activity, hydrolyzing O-glycosyl compounds

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFPKIFLTAATALLSAKSTFAQTYSSCNPLFTTGCPANTALGKSIDVDFTSGSVNSFDGSGDITYDSNGASFTVAKSGDAPTLSSIFYIMFGKVQITMKAAPGAGIVSTLVLQSDDLDEIDMEWLGADDTEVQTNYFGKGKVTDYNRGAFNPAANNQGEFITYTIEWTSEQVVWSVGSTVVRVLTPATADTDQYPQSPMQIKFGAWSGGDSSNAAGTISWARGPTDYSNGPFTMVVQSIDVSDYSTGTQYKYGDQSGDWTSIEAIGGSVNGNVPASASSIQTAGAAAVTSSSPTIPAGINNGNSATRTGYPWVAGTQTVSEVTWSTGPSIPSGWEISSEGKIVPVSASPINISRINPLLLCGPFTFFFFAAIRRWP

[Multiple Choices]
A. carbohydrate derivative binding
B. mechanosensitive monoatomic cation channel activity
C. hydrolase activity, hydrolyzing O-glycosyl compounds
D. ankyrin repeat binding
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The matched-sequence annotation describes chitinase activity and hydrolysis of chitin linkages; chitinase activity is a descendant of the broader GO term in choice C. The functional annotation includes both similarity-based evidence and a cited publication, while the specific catalytic-activity annotation is transferred by similarity.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal secretion signal, a long enzyme-like domain with a cluster of conserved acidic residues consistent with a glycoside hydrolase, and a hydrophobic C-terminal segment compatible with cell-wall association. Transferable knowledge of secreted fungal carbohydrate-active enzymes makes hydrolysis of glycosidic bonds a meaningful inference for C. The sequence is unlike a multipass mechanosensitive channel or a protein dominated by ankyrin repeats; the enzyme-like features also favor catalysis over generic carbohydrate-derivative binding.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level enzyme inference and sequence features meaningfully distinguish C from the offered alternatives without needing the exact protein's database record. The precise substrate and coupled transglycosylase activity are not established from sequence alone, but are not needed to choose the broad hydrolase option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C is the only offered option that describes the likely catalytic activity; the other choices describe unrelated binding or channel functions.


### Important caveats

- The sequence supports a glycoside-hydrolase-like function more readily than it establishes the exact substrate or all activities of the protein.
- Some reviewer-only annotations are transferred by similarity rather than direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal secretion signal, a long enzyme-like domain with a cluster of conserved acidic residues consistent with a glycoside hydrolase, and a hydrophobic C-terminal segment compatible with cell-wall association. Transferable knowledge of secreted fungal carbohydrate-active enzymes makes hydrolysis of glycosidic bonds a meaningful inference for C. The sequence is unlike a multipass mechanosensitive channel or a protein dominated by ankyrin repeats; the enzyme-like features also favor catalysis over generic carbohydrate-derivative binding.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level enzyme inference and sequence features meaningfully distinguish C from the offered alternatives without needing the exact protein's database record. The precise substrate and coupled transglycosylase activity are not established from sequence alone, but are not needed to choose the broad hydrolase option."
  },
  "case_id": "GO_molecular_function_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "GO1",
      "GO2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence annotation describes chitinase activity and hydrolysis of chitin linkages; chitinase activity is a descendant of the broader GO term in choice C. The functional annotation includes both similarity-based evidence and a cited publication, while the specific catalytic-activity annotation is transferred by similarity."
  },
  "important_caveats": [
    "The sequence supports a glycoside-hydrolase-like function more readily than it establishes the exact substrate or all activities of the protein.",
    "Some reviewer-only annotations are transferred by similarity rather than direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is the only offered option that describes the likely catalytic activity; the other choices describe unrelated binding or channel functions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence annotation describes chitinase activity and hydrolysis of chitin linkages; chitinase activity is a descendant of the broader GO term in choice C. The functional annotation includes both similarity-based evidence and a cited publication, while the specific catalytic-activity annotation is transferred by similarity.",
    "evidence_ids": ["C5", "C6", "C7", "GO1", "GO2", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal secretion signal, a long enzyme-like domain with a cluster of conserved acidic residues consistent with a glycoside hydrolase, and a hydrophobic C-terminal segment compatible with cell-wall association. Transferable knowledge of secreted fungal carbohydrate-active enzymes makes hydrolysis of glycosidic bonds a meaningful inference for C. The sequence is unlike a multipass mechanosensitive channel or a protein dominated by ankyrin repeats; the enzyme-like features also favor catalysis over generic carbohydrate-derivative binding.",
    "missing_item_specific_fact": "",
    "reason": "The family-level enzyme inference and sequence features meaningfully distinguish C from the offered alternatives without needing the exact protein's database record. The precise substrate and coupled transglycosylase activity are not established from sequence alone, but are not needed to choose the broad hydrolase option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is the only offered option that describes the likely catalytic activity; the other choices describe unrelated binding or channel functions."
  },
  "important_caveats": [
    "The sequence supports a glycoside-hydrolase-like function more readily than it establishes the exact substrate or all activities of the protein.",
    "Some reviewer-only annotations are transferred by similarity rather than direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is annotated with EC 3.2.1.14 (endochitinase activity, GO:0008843). The GO hierarchy confirms GO:0008843 is_a GO:0004568 (chitinase activity) is_a GO:0004553 (hydrolase activity, hydrolyzing O-glycosyl compounds). The catalytic reaction (hydrolysis of N-acetyl-beta-D-glucosaminide (1→4)-beta-linkages) involves cleavage of O-glycosidic bonds, which falls under the definition of GO:0004553 ('Catalysis of the hydrolysis of any O-glycosyl bond'). The annotation evidence is primarily by similarity (ECO:0000250) to Q8J0P4, with experimental support (ECO:0000269, PubMed:33846308) for the dual chitinase/transglycosylase function. While the most specific annotation is endochitinase activity, GO:0004553 is a valid ancestor term and the best match among the four offered options.

Citations as saved: [C6](#evidence-c6), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO3](#evidence-go3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits features recognizable as a GH18 (glycoside hydrolase family 18) chitinase-like domain common in fungal secreted proteins: (1) an N-terminal signal peptide (hydrophobic 'MFPKIFLTAATALLSAKST' region) indicating secretion; (2) a catalytic domain rich in beta-strand character with recognizable GH18 catalytic motifs including the DXXDXDXE-type motif region ('DIDMEWLGADDTEVQT'); (3) a C-terminal hydrophobic region ('PLLLCGPFTFFFFAAIRRWP') consistent with a GPI anchor or membrane-tethering segment seen in fungal Crh/chitinase proteins. This architecture is a well-known family signature in fungal glycoside hydrolases. Against the distractors: (B) mechanosensitive cation channels require multi-pass transmembrane topology (e.g., PIEZO-like trimeric architecture) absent here; (D) ankyrin repeat binding requires tandem ~33-aa helix-loop-helix modules (LxxLLGGA pattern) not present; (A) carbohydrate derivative binding is a passive binding function, whereas the sequence clearly encodes a catalytic domain with conserved catalytic residues, making hydrolase activity the primary function. The family-level inference from GH18 chitinases in fungi (a well-characterized protein family) meaningfully distinguishes C from the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the GH18 chitinase-like domain architecture, the signal peptide, the catalytic motifs, and the overall secreted-enzyme topology from transferable knowledge of fungal glycoside hydrolase families. These features positively support C (hydrolase activity) and exclude B (no channel topology), D (no ankyrin repeats), and A (catalytic rather than merely binding function). The inference is probabilistic but well-grounded in family-level knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While option A (carbohydrate derivative binding) could superficially apply since chitinases do bind carbohydrates, the primary molecular function of a chitinase is catalytic hydrolysis, not binding. The GO hierarchy places endochitinase activity under hydrolase activity, not under binding. The sequence clearly encodes catalytic machinery (conserved catalytic residues, TIM-barrel-like fold), making C unambiguously the best primary function among the four choices.


### Important caveats

- The primary UniProt annotation is by similarity (ECO:0000250) to Q8J0P4 for the chitinase/transglycosylase activities, with one experimental reference (PubMed:33846308) supporting the dual function.
- The protein also has transglycosylase (glycosyltransferase) activity (EC 2.4.-.-), but this is not among the offered options.
- The GO:0004553 term is an ancestor of the most specific annotation (GO:0008843 endochitinase activity); the question asks for the best match among the four choices, not the most specific GO term.
- The GH18 domain recognition from sequence alone is probabilistic; without structural confirmation, family assignment relies on motif similarity and overall composition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits features recognizable as a GH18 (glycoside hydrolase family 18) chitinase-like domain common in fungal secreted proteins: (1) an N-terminal signal peptide (hydrophobic 'MFPKIFLTAATALLSAKST' region) indicating secretion; (2) a catalytic domain rich in beta-strand character with recognizable GH18 catalytic motifs including the DXXDXDXE-type motif region ('DIDMEWLGADDTEVQT'); (3) a C-terminal hydrophobic region ('PLLLCGPFTFFFFAAIRRWP') consistent with a GPI anchor or membrane-tethering segment seen in fungal Crh/chitinase proteins. This architecture is a well-known family signature in fungal glycoside hydrolases. Against the distractors: (B) mechanosensitive cation channels require multi-pass transmembrane topology (e.g., PIEZO-like trimeric architecture) absent here; (D) ankyrin repeat binding requires tandem ~33-aa helix-loop-helix modules (LxxLLGGA pattern) not present; (A) carbohydrate derivative binding is a passive binding function, whereas the sequence clearly encodes a catalytic domain with conserved catalytic residues, making hydrolase activity the primary function. The family-level inference from GH18 chitinases in fungi (a well-characterized protein family) meaningfully distinguishes C from the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the GH18 chitinase-like domain architecture, the signal peptide, the catalytic motifs, and the overall secreted-enzyme topology from transferable knowledge of fungal glycoside hydrolase families. These features positively support C (hydrolase activity) and exclude B (no channel topology), D (no ankyrin repeats), and A (catalytic rather than merely binding function). The inference is probabilistic but well-grounded in family-level knowledge."
  },
  "case_id": "GO_molecular_function_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "GO1",
      "GO2",
      "GO3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The protein is annotated with EC 3.2.1.14 (endochitinase activity, GO:0008843). The GO hierarchy confirms GO:0008843 is_a GO:0004568 (chitinase activity) is_a GO:0004553 (hydrolase activity, hydrolyzing O-glycosyl compounds). The catalytic reaction (hydrolysis of N-acetyl-beta-D-glucosaminide (1→4)-beta-linkages) involves cleavage of O-glycosidic bonds, which falls under the definition of GO:0004553 ('Catalysis of the hydrolysis of any O-glycosyl bond'). The annotation evidence is primarily by similarity (ECO:0000250) to Q8J0P4, with experimental support (ECO:0000269, PubMed:33846308) for the dual chitinase/transglycosylase function. While the most specific annotation is endochitinase activity, GO:0004553 is a valid ancestor term and the best match among the four offered options."
  },
  "important_caveats": [
    "The primary UniProt annotation is by similarity (ECO:0000250) to Q8J0P4 for the chitinase/transglycosylase activities, with one experimental reference (PubMed:33846308) supporting the dual function.",
    "The protein also has transglycosylase (glycosyltransferase) activity (EC 2.4.-.-), but this is not among the offered options.",
    "The GO:0004553 term is an ancestor of the most specific annotation (GO:0008843 endochitinase activity); the question asks for the best match among the four choices, not the most specific GO term.",
    "The GH18 domain recognition from sequence alone is probabilistic; without structural confirmation, family assignment relies on motif similarity and overall composition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option A (carbohydrate derivative binding) could superficially apply since chitinases do bind carbohydrates, the primary molecular function of a chitinase is catalytic hydrolysis, not binding. The GO hierarchy places endochitinase activity under hydrolase activity, not under binding. The sequence clearly encodes catalytic machinery (conserved catalytic residues, TIM-barrel-like fold), making C unambiguously the best primary function among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is annotated with EC 3.2.1.14 (endochitinase activity, GO:0008843). The GO hierarchy confirms GO:0008843 is_a GO:0004568 (chitinase activity) is_a GO:0004553 (hydrolase activity, hydrolyzing O-glycosyl compounds). The catalytic reaction (hydrolysis of N-acetyl-beta-D-glucosaminide (1→4)-beta-linkages) involves cleavage of O-glycosidic bonds, which falls under the definition of GO:0004553 ('Catalysis of the hydrolysis of any O-glycosyl bond'). The annotation evidence is primarily by similarity (ECO:0000250) to Q8J0P4, with experimental support (ECO:0000269, PubMed:33846308) for the dual chitinase/transglycosylase function. While the most specific annotation is endochitinase activity, GO:0004553 is a valid ancestor term and the best match among the four offered options.",
    "evidence_ids": ["C6", "GO1", "GO2", "GO3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits features recognizable as a GH18 (glycoside hydrolase family 18) chitinase-like domain common in fungal secreted proteins: (1) an N-terminal signal peptide (hydrophobic 'MFPKIFLTAATALLSAKST' region) indicating secretion; (2) a catalytic domain rich in beta-strand character with recognizable GH18 catalytic motifs including the DXXDXDXE-type motif region ('DIDMEWLGADDTEVQT'); (3) a C-terminal hydrophobic region ('PLLLCGPFTFFFFAAIRRWP') consistent with a GPI anchor or membrane-tethering segment seen in fungal Crh/chitinase proteins. This architecture is a well-known family signature in fungal glycoside hydrolases. Against the distractors: (B) mechanosensitive cation channels require multi-pass transmembrane topology (e.g., PIEZO-like trimeric architecture) absent here; (D) ankyrin repeat binding requires tandem ~33-aa helix-loop-helix modules (LxxLLGGA pattern) not present; (A) carbohydrate derivative binding is a passive binding function, whereas the sequence clearly encodes a catalytic domain with conserved catalytic residues, making hydrolase activity the primary function. The family-level inference from GH18 chitinases in fungi (a well-characterized protein family) meaningfully distinguishes C from the other options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the GH18 chitinase-like domain architecture, the signal peptide, the catalytic motifs, and the overall secreted-enzyme topology from transferable knowledge of fungal glycoside hydrolase families. These features positively support C (hydrolase activity) and exclude B (no channel topology), D (no ankyrin repeats), and A (catalytic rather than merely binding function). The inference is probabilistic but well-grounded in family-level knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option A (carbohydrate derivative binding) could superficially apply since chitinases do bind carbohydrates, the primary molecular function of a chitinase is catalytic hydrolysis, not binding. The GO hierarchy places endochitinase activity under hydrolase activity, not under binding. The sequence clearly encodes catalytic machinery (conserved catalytic residues, TIM-barrel-like fold), making C unambiguously the best primary function among the four choices."
  },
  "important_caveats": [
    "The primary UniProt annotation is by similarity (ECO:0000250) to Q8J0P4 for the chitinase/transglycosylase activities, with one experimental reference (PubMed:33846308) supporting the dual function.",
    "The protein also has transglycosylase (glycosyltransferase) activity (EC 2.4.-.-), but this is not among the offered options.",
    "The GO:0004553 term is an ancestor of the most specific annotation (GO:0008843 endochitinase activity); the question asks for the best match among the four choices, not the most specific GO term.",
    "The GH18 domain recognition from sequence alone is probabilistic; without structural confirmation, family assignment relies on motif similarity and overall composition."
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
  "benchmark_sequence_length": 376,
  "benchmark_sequence_sha256": "93c30927e9f4a2529afa60c60aafd3d9da23bd8a18c0bce7ba4f794ddcbc6138",
  "current_entry_audit": {
    "entryVersion": 25,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 376,
  "current_source_sequence_sha256": "93c30927e9f4a2529afa60c60aafd3d9da23bd8a18c0bce7ba4f794ddcbc6138",
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
  "requested_accession": "A0A384JN58",
  "selected_historical_entry_version": 23,
  "selected_historical_record_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "selected_historical_source_sequence_length": 376,
  "selected_historical_source_sequence_sha256": "93c30927e9f4a2529afa60c60aafd3d9da23bd8a18c0bce7ba4f794ddcbc6138",
  "selected_historical_version": {
    "accession": "A0A384JN58",
    "database": "Swiss-Prot",
    "entryVersion": 23,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH4_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384JN58\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":25,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitinase crh4\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitin transglycosylase crh4\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 4\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Dual chitinase/transglycosylase that plays a role in cell wall architecture (PubMed:33846308). Chitinase and transglycosylase activities are coupled (By similarity). Required for the polysaccharide cross-linking at the septa and the cell wall (By similarity). More specifically, transfers chitin to 1,6-beta-glucan in the cell wall (By similarity)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"name\":\"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0008843\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:endochitinase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0016757\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:glycosyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Bi K.\",\"Scalschi L.\",\"Jaiswal N.\",\"Mengiste T.\",\"Fried R.\",\"Sanz A.B.\",\"Arroyo J.\",\"Zhu W.\",\"Masrati G.\",\"Sharon A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33846308\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-021-22436-1\"}],\"citationType\":\"journal article\",\"firstPage\":\"2166\",\"id\":\"33846308\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2166\",\"publicationDate\":\"2021\",\"title\":\"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.\",\"volume\":\"12\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H1",
  "excerpt": "ID   CRH4_BOTFB              Reviewed;         376 AA.\nAC   A0A384JN58;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 23.\nDE   RecName: Full=Crh-like protein 4 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh4 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh4 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\nGN   Name=crh4 {ECO:0000303|PubMed:33846308}; ORFNames=BCIN_07g04870;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;\nRA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,\nRA   Arroyo J., Zhu W., Masrati G., Sharon A.;\nRT   \"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector\nRT   triggering plant cell death and defense response.\";\nRL   Nat. Commun. 12:2166-2166(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Dual chitinase/transglycosylase that plays a role in cell\nCC       wall architecture (PubMed:33846308). Chitinase and transglycosylase\nCC       activities are coupled (By similarity). Required for the polysaccharide\nCC       cross-linking at the septa and the cell wall (By similarity). More\nCC       specifically, transfers chitin to 1,6-beta-glucan in the cell wall (By\nCC       similarity). {ECO:0000250|UniProtKB:Q8J0P4,\nCC       ECO:0000269|PubMed:33846308}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide\nCC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;\nCC         Evidence={ECO:0000250|UniProtKB:Q8J0P4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0008843; F:endochitinase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0016757; F:glycosyltransferase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004553\nname: hydrolase activity, hydrolyzing O-glycosyl compounds\nnamespace: molecular_function\nalt_id: GO:0016800\ndef: \"Catalysis of the hydrolysis of any O-glycosyl bond.\" [GOC:mah]\nsynonym: \"O-glucosyl hydrolase activity\" EXACT []\nxref: EC:3.2.1.-\nxref: Reactome:R-HSA-5694563 \"ABHD10 hydrolyses MPAG\"\nxref: Reactome:R-HSA-6786652 \"CHIT1 hydrolyses CHIT to 3xADGP\"\nxref: Reactome:R-HSA-9661820 \"Bacterial GUSB hydrolyses BDG to BIL\"\nis_a: GO:0016798 ! hydrolase activity, acting on glycosyl bonds\nproperty_value: skos:exactMatch EC:3.2.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004553",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 44250-44263",
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
  "excerpt": "[Term]\nid: GO:0004568\nname: chitinase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of (1->4)-beta linkages of N-acetyl-D-glucosamine (GlcNAc) polymers of chitin and chitodextrins.\" [GOC:bf, GOC:kah, GOC:pde, PMID:11468293]\nxref: Reactome:R-HSA-6786421 \"CHIA hydrolyses chitin\"\nis_a: GO:0004553 ! hydrolase activity, hydrolyzing O-glycosyl compounds\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004568",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 44534-44541",
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
  "excerpt": "[Term]\nid: GO:0008843\nname: endochitinase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of nonterminal (1->4)-beta linkages of N-acetyl-D-glucosamine (GlcNAc) polymers of chitin and chitodextrins. Typically, endochitinases cleave randomly within the chitin chain.\" [EC:3.2.1.14, GOC:bf, GOC:kah, GOC:pde, PMID:11468293]\nsynonym: \"1,4-beta-poly-N-acetylglucosaminidase\" EXACT [EC:3.2.1.14]\nsynonym: \"chitinase\" EXACT [EC:3.2.1.14]\nsynonym: \"chitodextrinase\" EXACT [EC:3.2.1.14]\nsynonym: \"poly-beta-glucosaminidase\" EXACT [EC:3.2.1.14]\nxref: EC:3.2.1.14\nxref: MetaCyc:3.2.1.14-RXN\nis_a: GO:0004568 ! chitinase activity\nproperty_value: skos:exactMatch EC:3.2.1.14\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008843",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 88913-88926",
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
  "excerpt": "[Term]\nid: GO:0071532\nname: ankyrin repeat binding\nnamespace: molecular_function\ndef: \"Binding to an ankyrin repeat of a protein. Ankyrin repeats are tandemly repeated modules of about 33 amino acids; each repeat folds into a helix-loop-helix structure with a beta-hairpin/loop region projecting out from the helices at a 90-degree angle, and repeats stack to form an L-shaped structure.\" [GOC:mah, InterPro:IPR002110]\nsynonym: \"ANK repeat binding\" EXACT [GOC:amm]\nis_a: GO:0019904 ! protein domain specific binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0071532",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 378039-378046",
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
  "excerpt": "[Term]\nid: GO:0097367\nname: carbohydrate derivative binding\nnamespace: molecular_function\ndef: \"Binding to a carbohydrate derivative.\" [GOC:pr]\nsubset: goslim_agr\nsubset: goslim_mouse\nis_a: GO:0005488 ! binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0097367",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 404743-404751",
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
  "excerpt": "[Term]\nid: GO:0140135\nname: mechanosensitive monoatomic cation channel activity\nnamespace: molecular_function\ndef: \"Enables the transmembrane transfer of a monoatomic cation by a channel that opens in response to a mechanical stress.\" [GOC:ha, PMID:22343900]\nsynonym: \"mechanically-gated cation channel activity\" EXACT []\nsynonym: \"mechanosensitive cation channel activity\" BROAD []\nxref: Reactome:R-HSA-9659380 \"Mechanoelectrical transduction (MET) channel transports cations from the extracellular region into the cytosol of stereocilia of inner hair cell\"\nxref: Reactome:R-HSA-9663363 \"Mechanoelectrical transduction (MET) channel transports cations into the cytosol of stereocilia of cochlear outer hair cell\"\nxref: Reactome:R-HSA-9855089 \"PIEZO1 trimer passively transports cations across the plasma membrane according to their electrochemical gradients\"\nis_a: GO:0005261 ! monoatomic cation channel activity\nis_a: GO:0008381 ! mechanosensitive monoatomic ion channel activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140135",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 437568-437580",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
