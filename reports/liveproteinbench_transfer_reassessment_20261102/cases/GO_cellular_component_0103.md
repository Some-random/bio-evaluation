# GO_cellular_component_0103

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0103.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — cell outer membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAVFPLSAKHRKYALRALAVSIILVSAAYIASTEGTERVRPQRVEQKLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGSAREVQFFTDEDGERNLVALEKKGGIWRRSASDADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLLYDSLYFHGQQVAAGDILAAEVVKGGTTHQAFYYRSDKEGGGGGNYYDEDGRVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAQGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. host cell
B. centrosome
C. cell outer membrane
D. aggresome
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

> The sequence-matched UniProt annotation places the mature protein probably at the cell outer membrane, by similarity; the corresponding GO annotation is also recorded. This supports C, though it is not direct experimental localization evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a positively charged N-terminus followed by a strongly hydrophobic stretch, consistent with a bacterial export signal. Its globular enzyme-like sequence is consistent with an exported peptidoglycan-active metallopeptidase rather than a eukaryotic centrosome or aggresome protein. Among the offered choices, the bacterial cell outer membrane is the meaningful envelope-location candidate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence features and transferable knowledge of bacterial export and cell-envelope enzymes give a credible basis for choosing C over these alternatives. A signal peptide alone does not prove outer-membrane association, so the inference is probabilistic rather than definitive.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The signal peptide does not specify the precise envelope compartment, but none of the other choices is comparably plausible given the sequence and choices.


### Important caveats

- The supplied source describes outer-membrane association as probable and by similarity; the GO annotation is computationally transferred, not direct localization evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a positively charged N-terminus followed by a strongly hydrophobic stretch, consistent with a bacterial export signal. Its globular enzyme-like sequence is consistent with an exported peptidoglycan-active metallopeptidase rather than a eukaryotic centrosome or aggresome protein. Among the offered choices, the bacterial cell outer membrane is the meaningful envelope-location candidate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and transferable knowledge of bacterial export and cell-envelope enzymes give a credible basis for choosing C over these alternatives. A signal peptide alone does not prove outer-membrane association, so the inference is probabilistic rather than definitive."
  },
  "case_id": "GO_cellular_component_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places the mature protein probably at the cell outer membrane, by similarity; the corresponding GO annotation is also recorded. This supports C, though it is not direct experimental localization evidence."
  },
  "important_caveats": [
    "The supplied source describes outer-membrane association as probable and by similarity; the GO annotation is computationally transferred, not direct localization evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide does not specify the precise envelope compartment, but none of the other choices is comparably plausible given the sequence and choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places the mature protein probably at the cell outer membrane, by similarity; the corresponding GO annotation is also recorded. This supports C, though it is not direct experimental localization evidence.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a positively charged N-terminus followed by a strongly hydrophobic stretch, consistent with a bacterial export signal. Its globular enzyme-like sequence is consistent with an exported peptidoglycan-active metallopeptidase rather than a eukaryotic centrosome or aggresome protein. Among the offered choices, the bacterial cell outer membrane is the meaningful envelope-location candidate.",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and transferable knowledge of bacterial export and cell-envelope enzymes give a credible basis for choosing C over these alternatives. A signal peptide alone does not prove outer-membrane association, so the inference is probabilistic rather than definitive."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide does not specify the precise envelope compartment, but none of the other choices is comparably plausible given the sequence and choices."
  },
  "important_caveats": [
    "The supplied source describes outer-membrane association as probable and by similarity; the GO annotation is computationally transferred, not direct localization evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (Q5F676, MPG_NEIG1) explicitly assigns GO:0009279 (cell outer membrane) with ISS evidence (by similarity to E0N688). The protein is named 'Outer membrane protein' (OMP) and described as a DD-carboxypeptidase/endopeptidase Mpg (M23B family metallopeptidase). The annotation note states: 'There is a signal or a transmembrane region in the N-terminus of the pre-protein (Probable). Mature protein is probably associated with the cell outer membrane (By similarity).' The evidence code is ECO:0000250 (inferred from sequence/structural similarity) rather than direct experimental localization, but the annotation is consistent with the protein's known function as a peptidoglycan-active metalloprotease in a Gram-negative bacterium. The sequence matches the benchmark exactly (430 AA, SHA256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C4](#evidence-c4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable biological facts allow a knowledgeable model to distinguish C from the alternatives: (1) The protein is bacterial (the sequence has no eukaryotic targeting motifs, and the overall composition is consistent with a bacterial proteome). Centrosome (B) and aggresome (D) are strictly eukaryotic structures (centrosomes require centrioles; aggresomes require dynein/microtubule transport), so both are immediately eliminable for a bacterial protein. (2) The N-terminus 'MAVFPLSAKHRKYALRALAVSIILVSAAYIASTEGT' contains a classic hydrophobic signal peptide (core: ALAVSIILVSAAYIAST), which in Gram-negative bacteria directs proteins through the Sec/Tat pathway to the outer membrane. (3) 'Host cell' (GO:0043657) refers to the host organism's cellular component (e.g., a human cell's membrane), not the bacterium's own envelope. Since the protein carries its own bacterial signal peptide and is a peptidoglycan-active enzyme (M23 peptidase family motifs visible: 'GGDGS', zinc-binding His residues), it belongs to the bacterium's own outer membrane, not the host cell. (4) M23-family peptidases are well-characterized as cell-wall/outer-membrane-associated enzymes in bacteria (e.g., LytM, SleB, autolysins), providing family-level transferable knowledge that supports outer membrane localization.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer is reachable through standard biological reasoning: recognizing bacterial vs. eukaryotic cellular structures eliminates B and D; recognizing the N-terminal signal peptide and the Gram-negative bacterial context (implied by the sequence composition and absence of eukaryotic motifs) points to outer membrane targeting; and the M23 peptidase family association with peptidoglycan/outer membrane provides additional family-level support. No fact specific to this exact protein's database record is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (centrosome) and D (aggresome) are unambiguously eukaryotic structures incompatible with a bacterial protein. Option A (host cell) refers to the host organism's cellular component per GO definition, which does not match a protein with its own bacterial signal peptide. Option C is the only coherent choice for a Gram-negative bacterial outer membrane protein. No genuine ambiguity exists among the offered alternatives.


### Important caveats

- The UniProt annotation for this protein's subcellular location is based on similarity (ISS/ECO:0000250) to E0N688, not direct experimental localization of Q5F676 itself.
- The organism identity (Neisseria gonorrhoeae) is not explicitly stated in the model's input; it must be inferred from sequence features or recognized from the sequence. However, the bacterial nature and Gram-negative cell envelope architecture can be inferred from the signal peptide and overall sequence composition.
- The GO term 'host cell' (GO:0043657) could theoretically apply if the protein were secreted into and localized within a host cell during infection, but the annotation and protein function (peptidoglycan-active enzyme) clearly place it in the bacterium's own outer membrane.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable biological facts allow a knowledgeable model to distinguish C from the alternatives: (1) The protein is bacterial (the sequence has no eukaryotic targeting motifs, and the overall composition is consistent with a bacterial proteome). Centrosome (B) and aggresome (D) are strictly eukaryotic structures (centrosomes require centrioles; aggresomes require dynein/microtubule transport), so both are immediately eliminable for a bacterial protein. (2) The N-terminus 'MAVFPLSAKHRKYALRALAVSIILVSAAYIASTEGT' contains a classic hydrophobic signal peptide (core: ALAVSIILVSAAYIAST), which in Gram-negative bacteria directs proteins through the Sec/Tat pathway to the outer membrane. (3) 'Host cell' (GO:0043657) refers to the host organism's cellular component (e.g., a human cell's membrane), not the bacterium's own envelope. Since the protein carries its own bacterial signal peptide and is a peptidoglycan-active enzyme (M23 peptidase family motifs visible: 'GGDGS', zinc-binding His residues), it belongs to the bacterium's own outer membrane, not the host cell. (4) M23-family peptidases are well-characterized as cell-wall/outer-membrane-associated enzymes in bacteria (e.g., LytM, SleB, autolysins), providing family-level transferable knowledge that supports outer membrane localization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer is reachable through standard biological reasoning: recognizing bacterial vs. eukaryotic cellular structures eliminates B and D; recognizing the N-terminal signal peptide and the Gram-negative bacterial context (implied by the sequence composition and absence of eukaryotic motifs) points to outer membrane targeting; and the M23 peptidase family association with peptidoglycan/outer membrane provides additional family-level support. No fact specific to this exact protein's database record is required."
  },
  "case_id": "GO_cellular_component_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (Q5F676, MPG_NEIG1) explicitly assigns GO:0009279 (cell outer membrane) with ISS evidence (by similarity to E0N688). The protein is named 'Outer membrane protein' (OMP) and described as a DD-carboxypeptidase/endopeptidase Mpg (M23B family metallopeptidase). The annotation note states: 'There is a signal or a transmembrane region in the N-terminus of the pre-protein (Probable). Mature protein is probably associated with the cell outer membrane (By similarity).' The evidence code is ECO:0000250 (inferred from sequence/structural similarity) rather than direct experimental localization, but the annotation is consistent with the protein's known function as a peptidoglycan-active metalloprotease in a Gram-negative bacterium. The sequence matches the benchmark exactly (430 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation for this protein's subcellular location is based on similarity (ISS/ECO:0000250) to E0N688, not direct experimental localization of Q5F676 itself.",
    "The organism identity (Neisseria gonorrhoeae) is not explicitly stated in the model's input; it must be inferred from sequence features or recognized from the sequence. However, the bacterial nature and Gram-negative cell envelope architecture can be inferred from the signal peptide and overall sequence composition.",
    "The GO term 'host cell' (GO:0043657) could theoretically apply if the protein were secreted into and localized within a host cell during infection, but the annotation and protein function (peptidoglycan-active enzyme) clearly place it in the bacterium's own outer membrane."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (centrosome) and D (aggresome) are unambiguously eukaryotic structures incompatible with a bacterial protein. Option A (host cell) refers to the host organism's cellular component per GO definition, which does not match a protein with its own bacterial signal peptide. Option C is the only coherent choice for a Gram-negative bacterial outer membrane protein. No genuine ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (Q5F676, MPG_NEIG1) explicitly assigns GO:0009279 (cell outer membrane) with ISS evidence (by similarity to E0N688). The protein is named 'Outer membrane protein' (OMP) and described as a DD-carboxypeptidase/endopeptidase Mpg (M23B family metallopeptidase). The annotation note states: 'There is a signal or a transmembrane region in the N-terminus of the pre-protein (Probable). Mature protein is probably associated with the cell outer membrane (By similarity).' The evidence code is ECO:0000250 (inferred from sequence/structural similarity) rather than direct experimental localization, but the annotation is consistent with the protein's known function as a peptidoglycan-active metalloprotease in a Gram-negative bacterium. The sequence matches the benchmark exactly (430 AA, SHA256 confirmed).",
    "evidence_ids": ["C5", "C6", "C4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable biological facts allow a knowledgeable model to distinguish C from the alternatives: (1) The protein is bacterial (the sequence has no eukaryotic targeting motifs, and the overall composition is consistent with a bacterial proteome). Centrosome (B) and aggresome (D) are strictly eukaryotic structures (centrosomes require centrioles; aggresomes require dynein/microtubule transport), so both are immediately eliminable for a bacterial protein. (2) The N-terminus 'MAVFPLSAKHRKYALRALAVSIILVSAAYIASTEGT' contains a classic hydrophobic signal peptide (core: ALAVSIILVSAAYIAST), which in Gram-negative bacteria directs proteins through the Sec/Tat pathway to the outer membrane. (3) 'Host cell' (GO:0043657) refers to the host organism's cellular component (e.g., a human cell's membrane), not the bacterium's own envelope. Since the protein carries its own bacterial signal peptide and is a peptidoglycan-active enzyme (M23 peptidase family motifs visible: 'GGDGS', zinc-binding His residues), it belongs to the bacterium's own outer membrane, not the host cell. (4) M23-family peptidases are well-characterized as cell-wall/outer-membrane-associated enzymes in bacteria (e.g., LytM, SleB, autolysins), providing family-level transferable knowledge that supports outer membrane localization.",
    "missing_item_specific_fact": "",
    "reason": "The answer is reachable through standard biological reasoning: recognizing bacterial vs. eukaryotic cellular structures eliminates B and D; recognizing the N-terminal signal peptide and the Gram-negative bacterial context (implied by the sequence composition and absence of eukaryotic motifs) points to outer membrane targeting; and the M23 peptidase family association with peptidoglycan/outer membrane provides additional family-level support. No fact specific to this exact protein's database record is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (centrosome) and D (aggresome) are unambiguously eukaryotic structures incompatible with a bacterial protein. Option A (host cell) refers to the host organism's cellular component per GO definition, which does not match a protein with its own bacterial signal peptide. Option C is the only coherent choice for a Gram-negative bacterial outer membrane protein. No genuine ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The UniProt annotation for this protein's subcellular location is based on similarity (ISS/ECO:0000250) to E0N688, not direct experimental localization of Q5F676 itself.",
    "The organism identity (Neisseria gonorrhoeae) is not explicitly stated in the model's input; it must be inferred from sequence features or recognized from the sequence. However, the bacterial nature and Gram-negative cell envelope architecture can be inferred from the signal peptide and overall sequence composition.",
    "The GO term 'host cell' (GO:0043657) could theoretically apply if the protein were secreted into and localized within a host cell during infection, but the annotation and protein function (peptidoglycan-active enzyme) clearly place it in the bacterium's own outer membrane."
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
  "benchmark_sequence_length": 430,
  "benchmark_sequence_sha256": "69e7a45357ac9f20734736f0f30bb74890972c0311fb90e7d268f0a51f998813",
  "current_entry_audit": {
    "entryVersion": 90,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-03-15",
    "sequenceVersion": 1
  },
  "current_record_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 430,
  "current_source_sequence_sha256": "69e7a45357ac9f20734736f0f30bb74890972c0311fb90e7d268f0a51f998813",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 88,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5F676",
  "selected_historical_entry_version": 88,
  "selected_historical_record_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "selected_historical_source_sequence_length": 430,
  "selected_historical_source_sequence_sha256": "69e7a45357ac9f20734736f0f30bb74890972c0311fb90e7d268f0a51f998813",
  "selected_historical_version": {
    "accession": "Q5F676",
    "database": "Swiss-Prot",
    "entryVersion": 88,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MPG_NEIG1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5F676\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":90,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-03-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAW90311.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000535\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Neisseriales\",\"Neisseriaceae\",\"Neisseria\"],\"scientificName\":\"Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090)\",\"taxonId\":242231}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23839218\",\"source\":\"PubMed\"}],\"value\":\"Metalloprotease NGO1686\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23839218\",\"source\":\"PubMed\"}],\"value\":\"Metalloprotease active against peptidoglycan\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Outer membrane protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"OMP\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22334697\",\"source\":\"PubMed\"}],\"value\":\"Virulence factor NG1686\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22334697\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23839218\",\"source\":\"PubMed\"}],\"value\":\"Zinc metallopeptidase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16194237\",\"source\":\"PubMed\"}],\"value\":\"Zinc metalloprotease\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc-dependent metallopeptidase\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22334697\",\"source\":\"PubMed\"}],\"value\":\"3.4.17.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22334697\",\"source\":\"PubMed\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"DD-carboxypeptidase/endopeptidase Mpg\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E0N688\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"There is a signal or a transmembrane region in the N-terminus of the pre-protein (Probable). Mature protein is probably associated with the cell outer membrane (By similarity)\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E0N688\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0040\",\"value\":\"Cell outer membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009279\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cell outer membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Stohl E.A.\",\"Criss A.K.\",\"Seifert H.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16194237\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1365-2958.2005.04839.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"16194237\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"532\",\"publicationDate\":\"2005\",\"title\":\"The transcriptome response of Neisseria gonorrhoeae to hydrogen peroxide reveals genes with previously uncharacterized roles in oxidative damage protection.\",\"volume\":\"58\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16194237\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Stohl E.A.\",\"Chan Y.A.\",\"Hackett K.T.\",\"Kohler P.L.\",\"Dillard J.P.\",\"Seifert H.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22334697\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m111.338830\"}],\"citationType\":\"journal article\",\"firstPage\":\"11222\",\"id\":\"22334697\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"11233\",\"publicationDate\":\"2012\",\"title\":\"Neisseria gonorrhoeae virulence factor NG1686 is a bifunctional M23B family metallopeptidase that influences resistance to hydrogen peroxide and colony morphology.\",\"volume\":\"287\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22334697\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-295; ASP-299; HIS-373 AND HIS-375\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Stohl E.A.\",\"Dale E.M.\",\"Criss A.K.\",\"Seifert H.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23839218\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.00399-13\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"23839218\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2013\",\"title\":\"Neisseria gonorrhoeae metalloprotease NGO1686 is required for full piliation, and piliation is required for resistance to H2O2- and neutrophil-mediated killing.\",\"volume\":\"4\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23839218\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H1",
  "excerpt": "ID   MPG_NEIG1               Reviewed;         430 AA.\nAC   Q5F676;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-MAR-2005, sequence version 1.\nDT   28-JAN-2026, entry version 88.\nDE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};\nDE            EC=3.4.17.- {ECO:0000269|PubMed:22334697};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:22334697};\nDE   AltName: Full=Metalloprotease NGO1686 {ECO:0000303|PubMed:23839218};\nDE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000303|PubMed:23839218};\nDE   AltName: Full=Outer membrane protein {ECO:0000305};\nDE            Short=OMP {ECO:0000305};\nDE   AltName: Full=Virulence factor NG1686 {ECO:0000303|PubMed:22334697};\nDE   AltName: Full=Zinc metallopeptidase {ECO:0000303|PubMed:22334697, ECO:0000303|PubMed:23839218};\nDE   AltName: Full=Zinc metalloprotease {ECO:0000303|PubMed:16194237};\nDE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=mpg {ECO:0000303|PubMed:23839218};\nGN   OrderedLocusNames=NGO_1686 {ECO:0000312|EMBL:AAW90311.1};\nOS   Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;\nOC   Neisseriaceae; Neisseria.\nOX   NCBI_TaxID=242231 {ECO:0000312|EMBL:AAW90311.1, ECO:0000312|Proteomes:UP000000535};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, INDUCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 700825 / FA 1090 {ECO:0000303|PubMed:16194237};\nRX   PubMed=16194237; DOI=10.1111/j.1365-2958.2005.04839.x;\nRA   Stohl E.A., Criss A.K., Seifert H.S.;\nRT   \"The transcriptome response of Neisseria gonorrhoeae to hydrogen peroxide\nRT   reveals genes with previously uncharacterized roles in oxidative damage\nRT   protection.\";\nRL   Mol. Microbiol. 58:520-532(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, DISRUPTION PHENOTYPE,\nRP   AND MUTAGENESIS OF HIS-295; ASP-299; HIS-373 AND HIS-375.\nRC   STRAIN=ATCC 700825 / FA 1090 {ECO:0000303|PubMed:22334697};\nRX   PubMed=22334697; DOI=10.1074/jbc.m111.338830;\nRA   Stohl E.A., Chan Y.A., Hackett K.T., Kohler P.L., Dillard J.P.,\nRA   Seifert H.S.;\nRT   \"Neisseria gonorrhoeae virulence factor NG1686 is a bifunctional M23B\nRT   family metallopeptidase that influences resistance to hydrogen peroxide and\nRT   colony morphology.\";\nRL   J. Biol. Chem. 287:11222-11233(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H4",
  "excerpt": "RN   [5]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 700825 / FA 1090 {ECO:0000303|PubMed:23839218};\nRX   PubMed=23839218; DOI=10.1128/mbio.00399-13;\nRA   Stohl E.A., Dale E.M., Criss A.K., Seifert H.S.;\nRT   \"Neisseria gonorrhoeae metalloprotease NGO1686 is required for full\nRT   piliation, and piliation is required for resistance to H2O2- and\nRT   neutrophil-mediated killing.\";\nRL   MBio 4:0-0(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H5",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell outer membrane\nCC       {ECO:0000250|UniProtKB:E0N688}. Note=There is a signal or a\nCC       transmembrane region in the N-terminus of the pre-protein (Probable).\nCC       Mature protein is probably associated with the cell outer membrane (By\nCC       similarity). {ECO:0000250|UniProtKB:E0N688, ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0009279; C:cell outer membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 152-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005813\nname: centrosome\nnamespace: cellular_component\ndef: \"A structure comprised of a core structure (in most organisms, a pair of centrioles) and peripheral material from which a microtubule-based structure, such as a spindle apparatus, is organized. Centrosomes occur close to the nucleus during interphase in many eukaryotic cells, though in animal cells it changes continually during the cell-division cycle.\" [GOC:mah, ISBN:0198547684]\nsubset: goslim_pir\nxref: Wikipedia:Centrosome\nis_a: GO:0005815 ! microtubule organizing center\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005813",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59790-59798",
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
  "excerpt": "[Term]\nid: GO:0009279\nname: cell outer membrane\nnamespace: cellular_component\ndef: \"A lipid bilayer that forms the outermost membrane of the cell envelope; enriched in polysaccharide and protein; the outer leaflet of the membrane contains specific lipopolysaccharide structures.\" [GOC:md, GOC:mtg_sensu, ISBN:0135712254]\ncomment: To annotate the plasma (cytoplasmic) membrane, see instead GO:0005886.\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsynonym: \"outer membrane of cell\" EXACT []\nis_a: GO:0019867 ! outer membrane\nis_a: GO:0030312 ! external encapsulating structure\nrelationship: part_of GO:0030313 ! cell envelope\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009279",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 94785-94797",
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
  "excerpt": "[Term]\nid: GO:0016235\nname: aggresome\nnamespace: cellular_component\ndef: \"An inclusion body formed by dynein-dependent retrograde transport of an aggregated protein on microtubules.\" [PMID:11121744]\nxref: Wikipedia:Aggresome\nis_a: GO:0016234 ! inclusion body\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016235",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 124908-124915",
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
  "excerpt": "[Term]\nid: GO:0043657\nname: host cell\nnamespace: cellular_component\ndef: \"A cell within a host organism. Includes the host plasma membrane and any external encapsulating structures such as the host cell wall and cell envelope.\" [GOC:jl]\nis_a: GO:0018995 ! host cellular component\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043657",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 249498-249504",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 103. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
