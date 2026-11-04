# GO_cellular_component_0172

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0172.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDTTMLQNAMQTDQAESKDLMNLAFFVRIIGLGVLPSVLVAVAKVNYPTWGKGLIQRAMTWGVSLVLLLVPIGLFSSQYASFFRVHKPVRFYINPITPIYSVGKLASIEYKKATAPTDTIYHAKDAVQTTKPSERKPRLVVFVVGETARADHVQFNGYGRETFPQLAKVDGLANFSQVTSCGTSTAYSVPCMFSYLGQDDYDVDTAKYQENVLDTLDRLGVGILWRDNNSDSKGVMDKLPATQYFDYKSATNNTICNTNPYNECRDVGMLVGLDDYVSANNGKDMLIMLHQMGNHGPAYFKRYDEQFAKFTPVCEGNELAKCEHQSLINAYDNALLATDDFIAKSIDWLKTHEANYDVAMLYVSDHGESLGENGVYLHGMPNAFAPKEQRAVPAFFWSNNTTFKPTASDTVLTHDAITPTLLKLFDVTAGKVKDRAAFIQ

[Multiple Choices]
A. rhoptry
B. plasma membrane
C. endomembrane system
D. vitelline envelope
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

> The sequence has several strongly hydrophobic N-terminal segments consistent with membrane-spanning helices. The matched UniProt record annotates the protein to the cell inner membrane and as a multipass membrane protein, and assigns the GO plasma membrane term. For a bacterial inner membrane, that GO term is appropriate. The location annotation is transferred/computational rather than direct experimental localization evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence’s multiple hydrophobic N-terminal segments support a membrane-anchored protein, while the long remainder is consistent with a membrane-associated enzyme domain. Transferable knowledge of bacterial membrane-protein families, including MCR-like phosphatidylethanolamine transferases, makes a cell membrane location a credible inference. Among the choices, plasma membrane is the fitting bacterial membrane option; rhoptry and vitelline envelope are specialized eukaryotic structures, and endomembrane system is not the typical location for a bacterial inner-membrane protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence architecture and transferable knowledge of membrane-protein families distinguish the membrane choice without requiring the target’s specific database annotation. The sequence alone does not prove the precise localization, so this is a biologically grounded inference rather than certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives do not present a comparably plausible competing location for a bacterial multipass membrane protein.


### Important caveats

- The supplied location and GO annotations are computationally or similarity supported; the excerpts do not establish direct experimental localization.
- The identity and organism information in the reviewer-only source evidence were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s multiple hydrophobic N-terminal segments support a membrane-anchored protein, while the long remainder is consistent with a membrane-associated enzyme domain. Transferable knowledge of bacterial membrane-protein families, including MCR-like phosphatidylethanolamine transferases, makes a cell membrane location a credible inference. Among the choices, plasma membrane is the fitting bacterial membrane option; rhoptry and vitelline envelope are specialized eukaryotic structures, and endomembrane system is not the typical location for a bacterial inner-membrane protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture and transferable knowledge of membrane-protein families distinguish the membrane choice without requiring the target’s specific database annotation. The sequence alone does not prove the precise localization, so this is a biologically grounded inference rather than certainty."
  },
  "case_id": "GO_cellular_component_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence has several strongly hydrophobic N-terminal segments consistent with membrane-spanning helices. The matched UniProt record annotates the protein to the cell inner membrane and as a multipass membrane protein, and assigns the GO plasma membrane term. For a bacterial inner membrane, that GO term is appropriate. The location annotation is transferred/computational rather than direct experimental localization evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The supplied location and GO annotations are computationally or similarity supported; the excerpts do not establish direct experimental localization.",
    "The identity and organism information in the reviewer-only source evidence were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives do not present a comparably plausible competing location for a bacterial multipass membrane protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence has several strongly hydrophobic N-terminal segments consistent with membrane-spanning helices. The matched UniProt record annotates the protein to the cell inner membrane and as a multipass membrane protein, and assigns the GO plasma membrane term. For a bacterial inner membrane, that GO term is appropriate. The location annotation is transferred/computational rather than direct experimental localization evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence’s multiple hydrophobic N-terminal segments support a membrane-anchored protein, while the long remainder is consistent with a membrane-associated enzyme domain. Transferable knowledge of bacterial membrane-protein families, including MCR-like phosphatidylethanolamine transferases, makes a cell membrane location a credible inference. Among the choices, plasma membrane is the fitting bacterial membrane option; rhoptry and vitelline envelope are specialized eukaryotic structures, and endomembrane system is not the typical location for a bacterial inner-membrane protein.",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture and transferable knowledge of membrane-protein families distinguish the membrane choice without requiring the target’s specific database annotation. The sequence alone does not prove the precise localization, so this is a biologically grounded inference rather than certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives do not present a comparably plausible competing location for a bacterial multipass membrane protein."
  },
  "important_caveats": [
    "The supplied location and GO annotations are computationally or similarity supported; the excerpts do not establish direct experimental localization.",
    "The identity and organism information in the reviewer-only source evidence were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A1C3NEV1, MCR-2) annotates the protein as 'Cell inner membrane' with 'Multi-pass membrane protein' topology (evidence ECO:0000250, transferred from MCR-1 A0A0R6L508). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The GO term definition explicitly includes 'bacterial inner membrane' as a NARROW synonym and 'cytoplasmic membrane' as an EXACT synonym, confirming that for bacteria, 'plasma membrane' in GO encompasses the inner membrane. A crystal structure (PDB 6A7W, residues 215-538) provides structural context for the catalytic domain but the membrane localization annotation is computational transfer rather than direct experimental evidence. The expected answer B is consistent with the database annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long hydrophobic stretches (e.g., residues ~10-30, ~130-160, ~170-200, ~210-240) characteristic of multi-pass transmembrane proteins, strongly indicating membrane localization. Among the four choices: (A) Rhoptry is a highly specialized secretory organelle unique to apicomplexan parasites (Toxoplasma, Plasmodium) requiring specific rhoptry protein families—no sequence similarity to those families is present. (D) Vitelline envelope is an animal egg-coat glycoprotein structure—completely inapplicable to a bacterial membrane enzyme. (C) Endomembrane system refers to the eukaryotic ER/Golgi/vesicle/nuclear-envelope network; bacteria lack this system entirely, and even in eukaryotes, a multi-pass membrane protein would be annotated as plasma membrane rather than the broad endomembrane system. (B) Plasma membrane is the universal membrane compartment for bacteria (GO:0005886 explicitly includes 'bacterial inner membrane' as a synonym) and is the natural annotation for a multi-pass membrane protein. A knowledgeable model can eliminate A, C, D as eukaryotic-specific structures incompatible with the observed multi-pass membrane topology and bacterial protein context, leaving B as the only viable answer.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-pass transmembrane topology visible in the sequence, combined with general knowledge that rhoptry (apicomplexan-specific), vitelline envelope (animal egg-specific), and endomembrane system (eukaryotic-specific) are incompatible with a bacterial multi-pass membrane protein, provides a concrete and credible inference pathway to answer B without needing to look up this specific protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (rhoptry, vitelline envelope, endomembrane system) are all eukaryotic-specific structures that are categorically incompatible with a bacterial multi-pass membrane protein. The sequence's hydrophobic topology unambiguously indicates membrane localization, and plasma membrane is the only membrane compartment among the choices applicable to bacteria. No genuine ambiguity exists.


### Important caveats

- The subcellular location annotation (ECO:0000250) is transferred from MCR-1 (A0A0R6L508) by similarity, not directly experimentally determined for MCR-2. However, the crystal structure of the catalytic domain and the clear multi-pass topology support membrane association.
- The organism identity (E. coli) is not provided in the original input to the model; the model must infer bacterial context from sequence features and the inapplicability of eukaryotic-specific options.
- The GO term 'plasma membrane' (GO:0005886) for bacteria refers to the inner/cytoplasmic membrane, not the outer membrane of Gram-negative bacteria.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches (e.g., residues ~10-30, ~130-160, ~170-200, ~210-240) characteristic of multi-pass transmembrane proteins, strongly indicating membrane localization. Among the four choices: (A) Rhoptry is a highly specialized secretory organelle unique to apicomplexan parasites (Toxoplasma, Plasmodium) requiring specific rhoptry protein families—no sequence similarity to those families is present. (D) Vitelline envelope is an animal egg-coat glycoprotein structure—completely inapplicable to a bacterial membrane enzyme. (C) Endomembrane system refers to the eukaryotic ER/Golgi/vesicle/nuclear-envelope network; bacteria lack this system entirely, and even in eukaryotes, a multi-pass membrane protein would be annotated as plasma membrane rather than the broad endomembrane system. (B) Plasma membrane is the universal membrane compartment for bacteria (GO:0005886 explicitly includes 'bacterial inner membrane' as a synonym) and is the natural annotation for a multi-pass membrane protein. A knowledgeable model can eliminate A, C, D as eukaryotic-specific structures incompatible with the observed multi-pass membrane topology and bacterial protein context, leaving B as the only viable answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass transmembrane topology visible in the sequence, combined with general knowledge that rhoptry (apicomplexan-specific), vitelline envelope (animal egg-specific), and endomembrane system (eukaryotic-specific) are incompatible with a bacterial multi-pass membrane protein, provides a concrete and credible inference pathway to answer B without needing to look up this specific protein's database record."
  },
  "case_id": "GO_cellular_component_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A1C3NEV1, MCR-2) annotates the protein as 'Cell inner membrane' with 'Multi-pass membrane protein' topology (evidence ECO:0000250, transferred from MCR-1 A0A0R6L508). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The GO term definition explicitly includes 'bacterial inner membrane' as a NARROW synonym and 'cytoplasmic membrane' as an EXACT synonym, confirming that for bacteria, 'plasma membrane' in GO encompasses the inner membrane. A crystal structure (PDB 6A7W, residues 215-538) provides structural context for the catalytic domain but the membrane localization annotation is computational transfer rather than direct experimental evidence. The expected answer B is consistent with the database annotation."
  },
  "important_caveats": [
    "The subcellular location annotation (ECO:0000250) is transferred from MCR-1 (A0A0R6L508) by similarity, not directly experimentally determined for MCR-2. However, the crystal structure of the catalytic domain and the clear multi-pass topology support membrane association.",
    "The organism identity (E. coli) is not provided in the original input to the model; the model must infer bacterial context from sequence features and the inapplicability of eukaryotic-specific options.",
    "The GO term 'plasma membrane' (GO:0005886) for bacteria refers to the inner/cytoplasmic membrane, not the outer membrane of Gram-negative bacteria."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (rhoptry, vitelline envelope, endomembrane system) are all eukaryotic-specific structures that are categorically incompatible with a bacterial multi-pass membrane protein. The sequence's hydrophobic topology unambiguously indicates membrane localization, and plasma membrane is the only membrane compartment among the choices applicable to bacteria. No genuine ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A1C3NEV1, MCR-2) annotates the protein as 'Cell inner membrane' with 'Multi-pass membrane protein' topology (evidence ECO:0000250, transferred from MCR-1 A0A0R6L508). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The GO term definition explicitly includes 'bacterial inner membrane' as a NARROW synonym and 'cytoplasmic membrane' as an EXACT synonym, confirming that for bacteria, 'plasma membrane' in GO encompasses the inner membrane. A crystal structure (PDB 6A7W, residues 215-538) provides structural context for the catalytic domain but the membrane localization annotation is computational transfer rather than direct experimental evidence. The expected answer B is consistent with the database annotation.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches (e.g., residues ~10-30, ~130-160, ~170-200, ~210-240) characteristic of multi-pass transmembrane proteins, strongly indicating membrane localization. Among the four choices: (A) Rhoptry is a highly specialized secretory organelle unique to apicomplexan parasites (Toxoplasma, Plasmodium) requiring specific rhoptry protein families—no sequence similarity to those families is present. (D) Vitelline envelope is an animal egg-coat glycoprotein structure—completely inapplicable to a bacterial membrane enzyme. (C) Endomembrane system refers to the eukaryotic ER/Golgi/vesicle/nuclear-envelope network; bacteria lack this system entirely, and even in eukaryotes, a multi-pass membrane protein would be annotated as plasma membrane rather than the broad endomembrane system. (B) Plasma membrane is the universal membrane compartment for bacteria (GO:0005886 explicitly includes 'bacterial inner membrane' as a synonym) and is the natural annotation for a multi-pass membrane protein. A knowledgeable model can eliminate A, C, D as eukaryotic-specific structures incompatible with the observed multi-pass membrane topology and bacterial protein context, leaving B as the only viable answer.",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass transmembrane topology visible in the sequence, combined with general knowledge that rhoptry (apicomplexan-specific), vitelline envelope (animal egg-specific), and endomembrane system (eukaryotic-specific) are incompatible with a bacterial multi-pass membrane protein, provides a concrete and credible inference pathway to answer B without needing to look up this specific protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (rhoptry, vitelline envelope, endomembrane system) are all eukaryotic-specific structures that are categorically incompatible with a bacterial multi-pass membrane protein. The sequence's hydrophobic topology unambiguously indicates membrane localization, and plasma membrane is the only membrane compartment among the choices applicable to bacteria. No genuine ambiguity exists."
  },
  "important_caveats": [
    "The subcellular location annotation (ECO:0000250) is transferred from MCR-1 (A0A0R6L508) by similarity, not directly experimentally determined for MCR-2. However, the crystal structure of the catalytic domain and the clear multi-pass topology support membrane association.",
    "The organism identity (E. coli) is not provided in the original input to the model; the model must infer bacterial context from sequence features and the inapplicability of eukaryotic-specific options.",
    "The GO term 'plasma membrane' (GO:0005886) for bacteria refers to the inner/cytoplasmic membrane, not the outer membrane of Gram-negative bacteria."
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
  "benchmark_sequence_length": 538,
  "benchmark_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 538,
  "current_source_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1C3NEV1",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "selected_historical_source_sequence_length": 538,
  "selected_historical_source_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "selected_historical_version": {
    "accession": "A0A1C3NEV1",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MCR2_ECOLX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1C3NEV1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"SBV31106.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Escherichia\"],\"scientificName\":\"Escherichia coli\",\"taxonId\":562}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0R6L508\",\"source\":\"UniProtKB\"}],\"value\":\"Polymyxin resistance protein MCR-2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30194678\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.43\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30194678\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.1\",\"source\":\"Reference\"}],\"value\":\"Phosphatidylethanolamine transferase Mcr-2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0R6L508\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0037\",\"value\":\"Cell inner membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang X.\",\"Lu Q.\",\"Qi J.\",\"Chai Y.\",\"Wang Y.\",\"Gao G.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30194678\"},{\"database\":\"DOI\",\"id\":\"10.1007/s11427-018-9363-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"1432\",\"id\":\"30194678\",\"journal\":\"Sci. China Life Sci.\",\"lastPage\":\"1436\",\"publicationDate\":\"2018\",\"title\":\"Structural and functional insights into MCR-2 mediated colistin resistance.\",\"volume\":\"61\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6A7W\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WHI04997.1\",\"source\":\"EMBL\"}],\"type\":\"PLASMID\",\"value\":\"unnamed5\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+)\",\"DISULFIDE BONDS\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF PHE-91; TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283; LYS-331 AND HIS-476\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   MCR2_ECOLX              Reviewed;         538 AA.\nAC   A0A1C3NEV1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2016, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Phosphatidylethanolamine transferase Mcr-2 {ECO:0000303|PubMed:30194678, ECO:0000303|Ref.1};\nDE            EC=2.7.8.43 {ECO:0000305|PubMed:30194678};\nDE   AltName: Full=Polymyxin resistance protein MCR-2 {ECO:0000250|UniProtKB:A0A0R6L508};\nGN   Name=mcr2 {ECO:0000305}; Synonyms=mcr-2 {ECO:0000312|EMBL:SBV31106.1};\nGN   ORFNames=QDW62_28200 {ECO:0000312|EMBL:WHI04997.1};\nOS   Escherichia coli.\nOG   Plasmid pKP37-BE {ECO:0000312|EMBL:SBV31106.1}, and\nOG   Plasmid unnamed5 {ECO:0000312|EMBL:WHI04997.1}.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Escherichia.\nOX   NCBI_TaxID=562 {ECO:0000312|EMBL:SBV31106.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6A7W}\nRP   X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+),\nRP   DISULFIDE BONDS, FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF PHE-91;\nRP   TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283;\nRP   LYS-331 AND HIS-476.\nRC   PLASMID=unnamed5 {ECO:0000312|EMBL:WHI04997.1};\nRX   PubMed=30194678; DOI=10.1007/s11427-018-9363-4;\nRA   Wang X., Lu Q., Qi J., Chai Y., Wang Y., Gao G.F.;\nRT   \"Structural and functional insights into MCR-2 mediated colistin\nRT   resistance.\";\nRL   Sci. China Life Sci. 61:1432-1436(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane\nCC       {ECO:0000250|UniProtKB:A0A0R6L508}; Multi-pass membrane protein\nCC       {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
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
  "excerpt": "[Term]\nid: GO:0012505\nname: endomembrane system\nnamespace: cellular_component\ndef: \"A collection of membranous structures involved in transport within the cell. The main components of the endomembrane system are endoplasmic reticulum, Golgi bodies, vesicles, cell membrane and nuclear envelope. Members of the endomembrane system pass materials through each other or though the use of vesicles.\" [GOC:lh]\nsubset: goslim_candida\nsubset: goslim_flybase_ribbon\nsubset: goslim_yeast\nxref: Wikipedia:Endomembrane_system\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0012505",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 111059-111069",
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
  "excerpt": "[Term]\nid: GO:0020008\nname: rhoptry\nnamespace: cellular_component\ndef: \"A large, club-shaped secretory organelle that forms part of the apical complex of an apicomplexan parasite, and consists of a bulbous body and a narrow electron-dense neck that extends through the conoid at the apical tip of the parasite. The rhoptry necks serve as ducts through which the contents of the rhoptries are secreted after attachment to the host has been completed and at the commencement of invasion. Rhoptry proteins function in the biogenesis and host organellar association of the parasitophorous vacuole.\" [ISBN:0521664470, PMID:11801218, PMID:16002398]\nsynonym: \"paired organelles\" RELATED []\nsynonym: \"toxoneme\" RELATED []\nxref: Wikipedia:Rhoptry\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0020007 ! apical complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020008",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155180-155190",
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
  "excerpt": "[Term]\nid: GO:0060388\nname: vitelline envelope\nnamespace: cellular_component\ndef: \"A glycoprotein-based structure that lies outside the plasma membrane and surrounds the egg before fertilization.\" [GOC:dph, ISBN:0878932437]\nsynonym: \"fertilization membrane\" RELATED []\nis_a: GO:0035805 ! egg coat\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0060388",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 347268-347275",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 172. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
