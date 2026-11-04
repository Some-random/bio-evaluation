# GO_biological_process_0010

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0010.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — killing of cells of another organism

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQVTSLLILVCFIAAFQVFSRASSPVNCKWDSYGPWSECNGCTKTQTRRRSVAVYGQYGGYPCEGSAFETQSCKPERGCPTEEGCGDRFRCFSGQCISKSLVCNGDPDCEEDGADEDKCENVANPSCNIDKPPPNIELTGYGYNVVTGQGKKRVINTKSFGGQCRKVFSGDGKDFYRLSGNILSYTFQVKVDNDFNYEFYNSSWSYIKHTSTEQNTFYSWKGLFSHSRNTYGHGSAKEEIDTKMKSYKLLVVQNTVEVAQFTNNNPEFLQVAEPFWKELSHLPTLYDYSAYRRLIDQYGTHYLQSGSLGGEYRVLFYVDSGSAKETGFQSDQDNACSSADFQFLFTSSADQRCMKQLETEKSTSGNKGRLLRGKPLVRGGDSGFVADLSFLDLDNPAGNKQRYSSWAGSVTRLPQVIKEKLAPLYELVKEVPCASVKRLYLKRAIEEYFDEFDPCHCRPCQNGGLAIVVETQCQCLCKPYTFGSACEQGVLVGDQAGGVDGGWNCWSSWSPCVQGKRTRSRECNNPPPRDDGKSCLGETTESKQCEDQDLEKLRLLEPHCFHSSLAPKEFCLSPPALKDGFVQGEGTMVPVGQSVVYACDEGYSLIGDPVARCGEDLQWLVGEMHCQKLACVLPGEMNGMQSHPQKPFYMVGEKVTLSCVGGMSLEGPSTLLCGSSLKWSPELKDAKCVQKATSTPPPAAPACQPWEKLQNSKCICKMPYECGSSLDVCARDESRNKILSLTICKMHVVHCHKRNYTLVGKESCTLPSPAEKVCGACPIWSKCDAQNGKCICREASECQTAGYRICVEVNGKEETMSECEAGILRCRGQSISITAIKPCAEEAAQ

[Multiple Choices]
A. positive regulation of leukocyte adhesion to vascular endothelial cell
B. killing of cells of another organism
C. negative regulation of neuron projection development
D. DNA recombination
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

> The sequence-matched record identifies the protein as complement component C7 and describes its role in the membrane attack complex, which forms pores and lyses target cells. The record also annotates the keyed process, though that GO annotation is computationally inferred rather than direct experimental evidence for this mouse protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The secreted, cysteine-rich sequence and its C-terminal membrane-attack-complex-perforin (MACPF) family region are consistent with a complement terminal-pathway protein. Transferable knowledge of this family predicts membrane pore formation and lysis of target cells, meaningfully favoring B over leukocyte adhesion regulation, neuron projection development, or DNA recombination.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence features supports the keyed process without needing the exact protein's recorded annotation. The inference is biologically credible, although sequence alone may not establish the precise GO term with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered alternatives, killing of cells of another organism is the clear match to the predicted MAC-mediated lysis function.


### Important caveats

- The mouse protein's database function annotation is transferred from a homolog, and the keyed GO annotation is listed as IEA; these are not direct experimental demonstrations for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The secreted, cysteine-rich sequence and its C-terminal membrane-attack-complex-perforin (MACPF) family region are consistent with a complement terminal-pathway protein. Transferable knowledge of this family predicts membrane pore formation and lysis of target cells, meaningfully favoring B over leukocyte adhesion regulation, neuron projection development, or DNA recombination.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features supports the keyed process without needing the exact protein's recorded annotation. The inference is biologically credible, although sequence alone may not establish the precise GO term with certainty."
  },
  "case_id": "GO_biological_process_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as complement component C7 and describes its role in the membrane attack complex, which forms pores and lyses target cells. The record also annotates the keyed process, though that GO annotation is computationally inferred rather than direct experimental evidence for this mouse protein."
  },
  "important_caveats": [
    "The mouse protein's database function annotation is transferred from a homolog, and the keyed GO annotation is listed as IEA; these are not direct experimental demonstrations for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, killing of cells of another organism is the clear match to the predicted MAC-mediated lysis function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as complement component C7 and describes its role in the membrane attack complex, which forms pores and lyses target cells. The record also annotates the keyed process, though that GO annotation is computationally inferred rather than direct experimental evidence for this mouse protein.",
    "evidence_ids": ["C4", "C5", "C8", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The secreted, cysteine-rich sequence and its C-terminal membrane-attack-complex-perforin (MACPF) family region are consistent with a complement terminal-pathway protein. Transferable knowledge of this family predicts membrane pore formation and lysis of target cells, meaningfully favoring B over leukocyte adhesion regulation, neuron projection development, or DNA recombination.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features supports the keyed process without needing the exact protein's recorded annotation. The inference is biologically credible, although sequence alone may not establish the precise GO term with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, killing of cells of another organism is the clear match to the predicted MAC-mediated lysis function."
  },
  "important_caveats": [
    "The mouse protein's database function annotation is transferred from a homolog, and the keyed GO annotation is listed as IEA; these are not direct experimental demonstrations for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms the protein is Complement component C7, a component of the membrane attack complex (MAC). Its annotated function is to serve as a membrane anchor in the MAC, which 'inserts into a target cell membrane and forms a pore, leading to target cell membrane rupture and cell lysis' (C5, H2). The GO term GO:0031640 'killing of cells of another organism' is directly assigned to this entry (C8, H6), and the GO term definition (GO3) states it covers 'the induction of death in one cell by another cell.' The MAC-mediated lysis of pathogenic cells is a textbook example of this GO term. The expected answer B is scientifically supported.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a hallmark architecture of terminal complement pathway proteins: (1) an N-terminal signal peptide indicating secretion; (2) multiple complement control protein (CCP/SCR) modules recognizable by their conserved Cys-X2-4-Cys spacing patterns (e.g., 'CHCRPCQNGG', 'CICKMPYECGSSLDVCARDESRNKILSLTICKMHVVHCHKRNYTLVGKESCTLPSPAEKVCGACPIWSKCDAQNGKCICREASECQTAGYRICVEVNGKEETMSECEAGILRCRGQSISITAIKPCAEEAAQ'); and (3) a large MACPF (membrane attack complex/perforin) domain, identifiable by the characteristic β-sheet-forming motifs in the central region. The MACPF domain is a well-characterized pore-forming module shared across perforins and complement C6/C7/C8/C9 proteins. Transferable knowledge from the perforin family and other MAC proteins establishes that MACPF-domain proteins function by inserting into target membranes and forming lytic pores, i.e., directly killing cells of another organism. Among the four options: (A) leukocyte adhesion to endothelium involves selectins, integrins, and ICAMs—not MACPF proteins; (C) neuron projection regulation involves semaphorins, ephrins, and guidance cues—no neuronal motifs here; (D) DNA recombination requires recombinase/transposase folds—absent here. Only (B) 'killing of cells of another organism' matches the pore-forming, membrane-lytic function encoded by the MACPF domain architecture.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The MACPF domain and complement domain architecture are recognizable from homologs (perforins, C6, C8, C9) and represent a well-known pore-forming module whose biological role—direct lysis of foreign cells—maps unambiguously to GO:0031640. A model with general knowledge of the complement system and MACPF domain family can distinguish B from the adhesion, neuronal, and DNA-recombination alternatives without needing the exact C7 annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span entirely different biological processes (adhesion regulation, cell killing, neuronal development, DNA recombination). The MACPF/complement domain architecture uniquely points to pore-forming cytotoxicity (B). While complement fragments (C3a, C5a) can indirectly promote inflammation, the MAC proteins' primary and defining role is direct target-cell lysis, not leukocyte adhesion regulation. No other option is defensible given the domain architecture.


### Important caveats

- The model is not told the protein is C7 or that it is from mouse; recognition must come from sequence features and family knowledge.
- The MACPF domain identification relies on pattern recognition of the β-barrel pore-forming fold motifs, which a well-trained model can infer from homologs like perforin and other complement proteins.
- The GO term 'killing of cells of another organism' is an ISO/IEA annotation transferred from human C7 (P10643); the mouse-specific experimental evidence for this exact entry is computational transfer, though the MAC function is extensively experimentally validated across species.
- The historical entry (v111, released 2026-01-28) matches the benchmark sequence exactly (SHA-256 confirmed).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a hallmark architecture of terminal complement pathway proteins: (1) an N-terminal signal peptide indicating secretion; (2) multiple complement control protein (CCP/SCR) modules recognizable by their conserved Cys-X2-4-Cys spacing patterns (e.g., 'CHCRPCQNGG', 'CICKMPYECGSSLDVCARDESRNKILSLTICKMHVVHCHKRNYTLVGKESCTLPSPAEKVCGACPIWSKCDAQNGKCICREASECQTAGYRICVEVNGKEETMSECEAGILRCRGQSISITAIKPCAEEAAQ'); and (3) a large MACPF (membrane attack complex/perforin) domain, identifiable by the characteristic β-sheet-forming motifs in the central region. The MACPF domain is a well-characterized pore-forming module shared across perforins and complement C6/C7/C8/C9 proteins. Transferable knowledge from the perforin family and other MAC proteins establishes that MACPF-domain proteins function by inserting into target membranes and forming lytic pores, i.e., directly killing cells of another organism. Among the four options: (A) leukocyte adhesion to endothelium involves selectins, integrins, and ICAMs—not MACPF proteins; (C) neuron projection regulation involves semaphorins, ephrins, and guidance cues—no neuronal motifs here; (D) DNA recombination requires recombinase/transposase folds—absent here. Only (B) 'killing of cells of another organism' matches the pore-forming, membrane-lytic function encoded by the MACPF domain architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The MACPF domain and complement domain architecture are recognizable from homologs (perforins, C6, C8, C9) and represent a well-known pore-forming module whose biological role—direct lysis of foreign cells—maps unambiguously to GO:0031640. A model with general knowledge of the complement system and MACPF domain family can distinguish B from the adhesion, neuronal, and DNA-recombination alternatives without needing the exact C7 annotation."
  },
  "case_id": "GO_biological_process_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H2",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is Complement component C7, a component of the membrane attack complex (MAC). Its annotated function is to serve as a membrane anchor in the MAC, which 'inserts into a target cell membrane and forms a pore, leading to target cell membrane rupture and cell lysis' (C5, H2). The GO term GO:0031640 'killing of cells of another organism' is directly assigned to this entry (C8, H6), and the GO term definition (GO3) states it covers 'the induction of death in one cell by another cell.' The MAC-mediated lysis of pathogenic cells is a textbook example of this GO term. The expected answer B is scientifically supported."
  },
  "important_caveats": [
    "The model is not told the protein is C7 or that it is from mouse; recognition must come from sequence features and family knowledge.",
    "The MACPF domain identification relies on pattern recognition of the β-barrel pore-forming fold motifs, which a well-trained model can infer from homologs like perforin and other complement proteins.",
    "The GO term 'killing of cells of another organism' is an ISO/IEA annotation transferred from human C7 (P10643); the mouse-specific experimental evidence for this exact entry is computational transfer, though the MAC function is extensively experimentally validated across species.",
    "The historical entry (v111, released 2026-01-28) matches the benchmark sequence exactly (SHA-256 confirmed)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different biological processes (adhesion regulation, cell killing, neuronal development, DNA recombination). The MACPF/complement domain architecture uniquely points to pore-forming cytotoxicity (B). While complement fragments (C3a, C5a) can indirectly promote inflammation, the MAC proteins' primary and defining role is direct target-cell lysis, not leukocyte adhesion regulation. No other option is defensible given the domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is Complement component C7, a component of the membrane attack complex (MAC). Its annotated function is to serve as a membrane anchor in the MAC, which 'inserts into a target cell membrane and forms a pore, leading to target cell membrane rupture and cell lysis' (C5, H2). The GO term GO:0031640 'killing of cells of another organism' is directly assigned to this entry (C8, H6), and the GO term definition (GO3) states it covers 'the induction of death in one cell by another cell.' The MAC-mediated lysis of pathogenic cells is a textbook example of this GO term. The expected answer B is scientifically supported.",
    "evidence_ids": ["C5", "C8", "H2", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a hallmark architecture of terminal complement pathway proteins: (1) an N-terminal signal peptide indicating secretion; (2) multiple complement control protein (CCP/SCR) modules recognizable by their conserved Cys-X2-4-Cys spacing patterns (e.g., 'CHCRPCQNGG', 'CICKMPYECGSSLDVCARDESRNKILSLTICKMHVVHCHKRNYTLVGKESCTLPSPAEKVCGACPIWSKCDAQNGKCICREASECQTAGYRICVEVNGKEETMSECEAGILRCRGQSISITAIKPCAEEAAQ'); and (3) a large MACPF (membrane attack complex/perforin) domain, identifiable by the characteristic β-sheet-forming motifs in the central region. The MACPF domain is a well-characterized pore-forming module shared across perforins and complement C6/C7/C8/C9 proteins. Transferable knowledge from the perforin family and other MAC proteins establishes that MACPF-domain proteins function by inserting into target membranes and forming lytic pores, i.e., directly killing cells of another organism. Among the four options: (A) leukocyte adhesion to endothelium involves selectins, integrins, and ICAMs—not MACPF proteins; (C) neuron projection regulation involves semaphorins, ephrins, and guidance cues—no neuronal motifs here; (D) DNA recombination requires recombinase/transposase folds—absent here. Only (B) 'killing of cells of another organism' matches the pore-forming, membrane-lytic function encoded by the MACPF domain architecture.",
    "missing_item_specific_fact": "",
    "reason": "The MACPF domain and complement domain architecture are recognizable from homologs (perforins, C6, C8, C9) and represent a well-known pore-forming module whose biological role—direct lysis of foreign cells—maps unambiguously to GO:0031640. A model with general knowledge of the complement system and MACPF domain family can distinguish B from the adhesion, neuronal, and DNA-recombination alternatives without needing the exact C7 annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different biological processes (adhesion regulation, cell killing, neuronal development, DNA recombination). The MACPF/complement domain architecture uniquely points to pore-forming cytotoxicity (B). While complement fragments (C3a, C5a) can indirectly promote inflammation, the MAC proteins' primary and defining role is direct target-cell lysis, not leukocyte adhesion regulation. No other option is defensible given the domain architecture."
  },
  "important_caveats": [
    "The model is not told the protein is C7 or that it is from mouse; recognition must come from sequence features and family knowledge.",
    "The MACPF domain identification relies on pattern recognition of the β-barrel pore-forming fold motifs, which a well-trained model can infer from homologs like perforin and other complement proteins.",
    "The GO term 'killing of cells of another organism' is an ISO/IEA annotation transferred from human C7 (P10643); the mouse-specific experimental evidence for this exact entry is computational transfer, though the MAC function is extensively experimentally validated across species.",
    "The historical entry (v111, released 2026-01-28) matches the benchmark sequence exactly (SHA-256 confirmed)."
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
  "benchmark_sequence_length": 845,
  "benchmark_sequence_sha256": "dc93fe1d2b11f0267bd1960d07d9ec9a56f008cb367ad7597552e5252fb454ce",
  "current_entry_audit": {
    "entryVersion": 113,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-10-03",
    "sequenceVersion": 2
  },
  "current_record_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 845,
  "current_source_sequence_sha256": "dc93fe1d2b11f0267bd1960d07d9ec9a56f008cb367ad7597552e5252fb454ce",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 111,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D3YXF5",
  "selected_historical_entry_version": 111,
  "selected_historical_record_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "selected_historical_source_sequence_length": 845,
  "selected_historical_source_sequence_sha256": "dc93fe1d2b11f0267bd1960d07d9ec9a56f008cb367ad7597552e5252fb454ce",
  "selected_historical_version": {
    "accession": "D3YXF5",
    "database": "Swiss-Prot",
    "entryVersion": 111,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CO7_MOUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D3YXF5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":113,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-10-03\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mouse\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Mus\",\"Mus\"],\"scientificName\":\"Mus musculus\",\"taxonId\":10090}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Complement component C7\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10643\",\"source\":\"UniProtKB\"}],\"value\":\"Component of the membrane attack complex (MAC), a multiprotein complex activated by the complement cascade, which inserts into a target cell membrane and forms a pore, leading to target cell membrane rupture and cell lysis. The MAC is initiated by proteolytic cleavage of C5 into complement C5b in response to the classical, alternative, lectin and GZMK complement pathways. The complement pathways consist in a cascade of proteins that leads to phagocytosis and breakdown of pathogens and signaling that strengthens the adaptive immune system. C7 serves as a membrane anchor. During MAC assembly, associates with C5b and C6 to form the C5b-7 complex, a key lipophilic precursor of the MAC complex, which associates with the outer leaflet and reduces the energy for membrane bending\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0006956\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:complement activation\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/43",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0160257\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:complement activation, GZMK pathway\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/44",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031640\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:killing of cells of another organism\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/45",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30552328\",\"source\":\"PubMed\"}],\"id\":\"GO:0050778\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:positive regulation of immune response\"},{\"key\":\"GoEvidenceType\",\"value\":\"NAS:ComplexPortal\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/46",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H1",
  "excerpt": "ID   CO7_MOUSE               Reviewed;         845 AA.\nAC   D3YXF5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-OCT-2012, sequence version 2.\nDT   28-JAN-2026, entry version 111.\nDE   RecName: Full=Complement component C7 {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=C7 {ECO:0000312|MGI:MGI:88235};\nOS   Mus musculus (Mouse).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Mus; Mus.\nOX   NCBI_TaxID=10090;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H2",
  "excerpt": "CC   -!- FUNCTION: Component of the membrane attack complex (MAC), a\nCC       multiprotein complex activated by the complement cascade, which inserts\nCC       into a target cell membrane and forms a pore, leading to target cell\nCC       membrane rupture and cell lysis. The MAC is initiated by proteolytic\nCC       cleavage of C5 into complement C5b in response to the classical,\nCC       alternative, lectin and GZMK complement pathways. The complement\nCC       pathways consist in a cascade of proteins that leads to phagocytosis\nCC       and breakdown of pathogens and signaling that strengthens the adaptive\nCC       immune system. C7 serves as a membrane anchor. During MAC assembly,\nCC       associates with C5b and C6 to form the C5b-7 complex, a key lipophilic\nCC       precursor of the MAC complex, which associates with the outer leaflet\nCC       and reduces the energy for membrane bending.\nCC       {ECO:0000250|UniProtKB:P10643}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0006956; P:complement activation; ISO:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0006958; P:complement activation, classical pathway; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0160257; P:complement activation, GZMK pathway; ISS:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0031640; P:killing of cells of another organism; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0050778; P:positive regulation of immune response; NAS:ComplexPortal.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006310\nname: DNA recombination\nnamespace: biological_process\ndef: \"Any process in which a new genotype is formed by reassortment of genes resulting in gene combinations different from those that were present in the parents. In eukaryotes genetic recombination can occur by chromosome assortment, intrachromosomal recombination, or nonreciprocal interchromosomal recombination. Interchromosomal recombination occurs by crossing over. In bacteria it may occur by genetic transformation, conjugation, transduction, or F-duction.\" [ISBN:0198506732]\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_pombe\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nis_a: GO:0006259 ! DNA metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006310",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 65050-65062",
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
  "excerpt": "[Term]\nid: GO:0010977\nname: negative regulation of neuron projection development\nnamespace: biological_process\ndef: \"Any process that decreases the rate, frequency or extent of neuron projection development. Neuron projection development is the process whose specific outcome is the progression of a neuron projection over time, from its formation to the mature structure. A neuron projection is any process extending from a neural cell, such as axons or dendrites (collectively called neurites).\" [GOC:dph, GOC:tb]\nsynonym: \"growth cone collapse\" RELATED [GOC:pr]\nsynonym: \"negative regulation of neurite biosynthesis\" NARROW [GOC:mah]\nsynonym: \"negative regulation of neurite development\" NARROW [GOC:mah]\nsynonym: \"negative regulation of neurite formation\" NARROW [GOC:mah]\nsynonym: \"negative regulation of neurite growth\" NARROW [GOC:mah]\nis_a: GO:0010975 ! regulation of neuron projection development\nis_a: GO:0031345 ! negative regulation of cell projection organization\nrelationship: negatively_regulates GO:0031175 ! neuron projection development\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0010977",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 110813-110826",
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
  "excerpt": "[Term]\nid: GO:0031640\nname: killing of cells of another organism\nnamespace: biological_process\nalt_id: GO:0001908\nalt_id: GO:0051852\ndef: \"Any process in an organism that results in the killing of cells of another organism, including in some cases the death of the other organism. Killing here refers to the induction of death in one cell by another cell, not cell-autonomous death due to internal or other environmental conditions.\" [GOC:add]\nsubset: goslim_pir\nsynonym: \"killing of cells of other organism\" EXACT []\nis_a: GO:0001906 ! cell killing\nis_a: GO:0141061 ! disruption of cell in another organism\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031640",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 178549-178560",
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
  "excerpt": "[Term]\nid: GO:1904996\nname: positive regulation of leukocyte adhesion to vascular endothelial cell\nnamespace: biological_process\ndef: \"Any process that activates or increases the frequency, rate or extent of leukocyte adhesion to vascular endothelial cell.\" [GO_REF:0000058, GOC:bc, GOC:BHF, GOC:BHF_miRNA, GOC:TermGenie, PMID:23897866]\nsynonym: \"activation of leukocyte adhesion to vascular endothelial cell\" NARROW [GOC:TermGenie]\nsynonym: \"up regulation of leukocyte adhesion to vascular endothelial cell\" EXACT [GOC:TermGenie]\nsynonym: \"up-regulation of leukocyte adhesion to vascular endothelial cell\" EXACT [GOC:TermGenie]\nsynonym: \"upregulation of leukocyte adhesion to vascular endothelial cell\" EXACT [GOC:TermGenie]\nis_a: GO:1903039 ! positive regulation of leukocyte cell-cell adhesion\nis_a: GO:1904994 ! regulation of leukocyte adhesion to vascular endothelial cell\nrelationship: positively_regulates GO:0061756 ! leukocyte adhesion to vascular endothelial cell\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1904996",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 532532-532544",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
