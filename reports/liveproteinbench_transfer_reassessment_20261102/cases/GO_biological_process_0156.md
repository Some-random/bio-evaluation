# GO_biological_process_0156

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0156.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — RNA polymerase II preinitiation complex assembly

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKTSGASNTDELNKSSHSKVSKKSTKSRSKSAKLELTGKNSLSASASSSIASAVSGGVAVGSLPATPTHLNMVTTPTTPTSSLGNYNLFDASFAVAGSGGHGLAGGIAGAEASGNSSRMGHQKSYAGFDPRSIKIFWEQHDQTDVELSQDVCARLAEDASYKVWELINNVKIYSRHSGGVVTYDLVNEVLKDADVPPMLGAMDSDWDRIDYDGSFYFHSDKIFELSAEFQKEVNLCTPDDADFQSICPVEDKHMDQLRQCVQSLVTAALFADSKSQTAAVCHAFQTPLMGSIYRVIVSKMVQLLAFKQQDHLSQRCWRLLRACNYNATANHNACRPEYFNLAEVLVSQLMAPYETIKAPHVDPDPGQTTSIKMEFEEELKVEPDQCHNPETQENPEVMGVEKQEQEPQMFPGESTMEHTIYKLQSEEEELNPQPEAEHLSSYFACPVGNGLVDELCETIGQLASQSGYLHAECLFLIKRRLARFFEGRHVSSERDFRYISRAVRGLIALGEYAFREFIPYIYKLRVEEIPDSLWPDLAPAAIFLGGHDDVYLYEWLEYGCGAALQPFLVHYARAYEKMVTRRYVKAKQPAYRIESVPGVRRLEWSTLAAAMCHGDDPSKALKPKPTLCEAFPDLQSPNLQLNCAGNIRFKFAGCRPVLLKPKVATVPHSEDSPSSAANGGGGGGASSDILIAKRKLFKPLTNVRKWSPISGYHYLRI

[Multiple Choices]
A. cellular homeostasis
B. RNA polymerase II preinitiation complex assembly
C. heterotypic cell-cell adhesion
D. tRNA wobble cytosine modification
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

> The matched protein has a GO annotation for RNA polymerase II preinitiation complex assembly (B). That annotation is IBA, a computational phylogenetic inference. Separately, the record describes experimentally supported participation in the SAGA transcriptional coactivator complex and transcriptional activation, which is consistent with the keyed process but does not by itself directly establish PIC assembly.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H7](#evidence-h7), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a eukaryotic transcription-regulatory protein with a conserved globular region rather than a membrane adhesion protein or a tRNA-modifying enzyme. Transferable knowledge that TAF6-like histone-fold proteins and SAGA-related transcription coactivators participate in promoter transcription machinery makes RNA polymerase II preinitiation complex assembly the meaningful choice among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference toward transcription initiation distinguishes B from the unrelated adhesion and tRNA-modification options and the broad homeostasis option. The inference is credible but does not independently prove this protein's exact GO annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the only offered choice that fits the sequence's plausible transcription-regulatory family context; the other options describe substantially different biological functions.


### Important caveats

- The supplied GO annotation for B is computationally transferred (IBA), not direct experimental evidence of PIC assembly by this exact protein.
- Experimental evidence in the reviewer-only source supports SAGA complex participation and transcriptional activation, rather than specifically demonstrating PIC assembly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a eukaryotic transcription-regulatory protein with a conserved globular region rather than a membrane adhesion protein or a tRNA-modifying enzyme. Transferable knowledge that TAF6-like histone-fold proteins and SAGA-related transcription coactivators participate in promoter transcription machinery makes RNA polymerase II preinitiation complex assembly the meaningful choice among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference toward transcription initiation distinguishes B from the unrelated adhesion and tRNA-modification options and the broad homeostasis option. The inference is credible but does not independently prove this protein's exact GO annotation."
  },
  "case_id": "GO_biological_process_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H7",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The matched protein has a GO annotation for RNA polymerase II preinitiation complex assembly (B). That annotation is IBA, a computational phylogenetic inference. Separately, the record describes experimentally supported participation in the SAGA transcriptional coactivator complex and transcriptional activation, which is consistent with the keyed process but does not by itself directly establish PIC assembly."
  },
  "important_caveats": [
    "The supplied GO annotation for B is computationally transferred (IBA), not direct experimental evidence of PIC assembly by this exact protein.",
    "Experimental evidence in the reviewer-only source supports SAGA complex participation and transcriptional activation, rather than specifically demonstrating PIC assembly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only offered choice that fits the sequence's plausible transcription-regulatory family context; the other options describe substantially different biological functions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein has a GO annotation for RNA polymerase II preinitiation complex assembly (B). That annotation is IBA, a computational phylogenetic inference. Separately, the record describes experimentally supported participation in the SAGA transcriptional coactivator complex and transcriptional activation, which is consistent with the keyed process but does not by itself directly establish PIC assembly.",
    "evidence_ids": ["C5", "C8", "H7", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a eukaryotic transcription-regulatory protein with a conserved globular region rather than a membrane adhesion protein or a tRNA-modifying enzyme. Transferable knowledge that TAF6-like histone-fold proteins and SAGA-related transcription coactivators participate in promoter transcription machinery makes RNA polymerase II preinitiation complex assembly the meaningful choice among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference toward transcription initiation distinguishes B from the unrelated adhesion and tRNA-modification options and the broad homeostasis option. The inference is credible but does not independently prove this protein's exact GO annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only offered choice that fits the sequence's plausible transcription-regulatory family context; the other options describe substantially different biological functions."
  },
  "important_caveats": [
    "The supplied GO annotation for B is computationally transferred (IBA), not direct experimental evidence of PIC assembly by this exact protein.",
    "Experimental evidence in the reviewer-only source supports SAGA complex participation and transcriptional activation, rather than specifically demonstrating PIC assembly."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (Q9VPT4, SAGA factor-like TAF6) includes GO:0051123 'RNA polymerase II preinitiation complex assembly' (C8/H9), albeit with IBA:GO_Central evidence (computational inference from complex membership). The protein is a confirmed component of the SAGA complex (experimental evidence from multiple PubMed references, C5/H7), which activates transcription by RNA Pol II. The protein also carries GO:0045944 'positive regulation of transcription by RNA polymerase II' with IMP:FlyBase (experimental mutant-phenotype evidence, C7/H8). The annotation of PIC assembly is consistent with the SAGA complex's well-established role as a transcription coactivator that participates in PIC formation. The expected answer B is thus supported by the database annotation, though the specific GO:0051123 term relies on computational (IBA) rather than direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 717-residue sequence contains recognizable histone-fold domains (HFDs), identifiable by their characteristic alpha-beta-alpha-beta-alpha topology with conserved hydrophobic core residues in helical segments (e.g., the regions 'WEQHDQTDVELSQDVCARLAEDASYKVWELINNVKIYSRHSGG…' and '…IFLGGHDDVYLYEWLEYGCGAALQPFLVHYARAYEKMVTRRYVKAKQPAYRIESVPGVRRLEWSTLAAAMCHG…'). HFDs are a well-known family-level feature of TAF proteins (TAF4, TAF5, TAF6, TAF9, TAF12), which are core subunits of the TFIID/SAGA transcription coactivator complexes. From transferable knowledge of other TAF-family proteins, a knowledgeable model can infer that an HFD-containing protein is a TAF-like transcription factor component, placing it squarely in the RNA Pol II transcription initiation/PIC assembly pathway. This distinguishes option B from C (heterotypic cell-cell adhesion, which involves cadherin/integrin/selectin domains absent here) and D (tRNA wobble cytosine modification, which involves methyltransferase or enzymatic domains, not HFDs). Option A (cellular homeostasis) is a very broad GO term referring to maintenance of internal steady state; while transcription broadly supports homeostasis, the specific HFD/TAF-family signature points to the more precise transcription-initiation annotation rather than the generic homeostasis term.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The histone-fold domain is a directly observable sequence feature that triggers a well-established family-level inference: HFD-containing proteins are TAF-like components of TFIID/SAGA, which participate in RNA Pol II preinitiation complex assembly. This reasoning uses knowledge transferable from other TAF proteins and the general architecture of the transcription machinery, without requiring recall of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly incompatible with HFD-containing TAF-like proteins. Option A (cellular homeostasis) is a broad GO term that does not capture the specific transcription-initiation role indicated by the HFD/TAF signature. Option B is the most specific and mechanistically appropriate choice given the sequence features.


### Important caveats

- The GO:0051123 annotation for this protein carries IBA:GO_Central evidence (computational inference from SAGA complex membership), not direct experimental evidence. The experimentally supported GO term is GO:0045944 (positive regulation of transcription by RNA Pol II, IMP).
- The protein is a Drosophila-specific SAGA subunit (Saf6) that replaces canonical TAF6 in Drosophila SAGA; its role in PIC assembly is inferred from complex membership rather than demonstrated directly for this paralog.
- The histone-fold domain recognition from raw sequence is a reasonable expert inference but is not trivially obvious to all models; it depends on pattern recognition of the HFD fold signature.
- The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt Q9VPT4, so the annotation applies to the exact sequence presented.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 717-residue sequence contains recognizable histone-fold domains (HFDs), identifiable by their characteristic alpha-beta-alpha-beta-alpha topology with conserved hydrophobic core residues in helical segments (e.g., the regions 'WEQHDQTDVELSQDVCARLAEDASYKVWELINNVKIYSRHSGG…' and '…IFLGGHDDVYLYEWLEYGCGAALQPFLVHYARAYEKMVTRRYVKAKQPAYRIESVPGVRRLEWSTLAAAMCHG…'). HFDs are a well-known family-level feature of TAF proteins (TAF4, TAF5, TAF6, TAF9, TAF12), which are core subunits of the TFIID/SAGA transcription coactivator complexes. From transferable knowledge of other TAF-family proteins, a knowledgeable model can infer that an HFD-containing protein is a TAF-like transcription factor component, placing it squarely in the RNA Pol II transcription initiation/PIC assembly pathway. This distinguishes option B from C (heterotypic cell-cell adhesion, which involves cadherin/integrin/selectin domains absent here) and D (tRNA wobble cytosine modification, which involves methyltransferase or enzymatic domains, not HFDs). Option A (cellular homeostasis) is a very broad GO term referring to maintenance of internal steady state; while transcription broadly supports homeostasis, the specific HFD/TAF-family signature points to the more precise transcription-initiation annotation rather than the generic homeostasis term.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The histone-fold domain is a directly observable sequence feature that triggers a well-established family-level inference: HFD-containing proteins are TAF-like components of TFIID/SAGA, which participate in RNA Pol II preinitiation complex assembly. This reasoning uses knowledge transferable from other TAF proteins and the general architecture of the transcription machinery, without requiring recall of this specific protein's database annotation."
  },
  "case_id": "GO_biological_process_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "H7",
      "H8",
      "H9",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (Q9VPT4, SAGA factor-like TAF6) includes GO:0051123 'RNA polymerase II preinitiation complex assembly' (C8/H9), albeit with IBA:GO_Central evidence (computational inference from complex membership). The protein is a confirmed component of the SAGA complex (experimental evidence from multiple PubMed references, C5/H7), which activates transcription by RNA Pol II. The protein also carries GO:0045944 'positive regulation of transcription by RNA polymerase II' with IMP:FlyBase (experimental mutant-phenotype evidence, C7/H8). The annotation of PIC assembly is consistent with the SAGA complex's well-established role as a transcription coactivator that participates in PIC formation. The expected answer B is thus supported by the database annotation, though the specific GO:0051123 term relies on computational (IBA) rather than direct experimental evidence."
  },
  "important_caveats": [
    "The GO:0051123 annotation for this protein carries IBA:GO_Central evidence (computational inference from SAGA complex membership), not direct experimental evidence. The experimentally supported GO term is GO:0045944 (positive regulation of transcription by RNA Pol II, IMP).",
    "The protein is a Drosophila-specific SAGA subunit (Saf6) that replaces canonical TAF6 in Drosophila SAGA; its role in PIC assembly is inferred from complex membership rather than demonstrated directly for this paralog.",
    "The histone-fold domain recognition from raw sequence is a reasonable expert inference but is not trivially obvious to all models; it depends on pattern recognition of the HFD fold signature.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt Q9VPT4, so the annotation applies to the exact sequence presented."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with HFD-containing TAF-like proteins. Option A (cellular homeostasis) is a broad GO term that does not capture the specific transcription-initiation role indicated by the HFD/TAF signature. Option B is the most specific and mechanistically appropriate choice given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (Q9VPT4, SAGA factor-like TAF6) includes GO:0051123 'RNA polymerase II preinitiation complex assembly' (C8/H9), albeit with IBA:GO_Central evidence (computational inference from complex membership). The protein is a confirmed component of the SAGA complex (experimental evidence from multiple PubMed references, C5/H7), which activates transcription by RNA Pol II. The protein also carries GO:0045944 'positive regulation of transcription by RNA polymerase II' with IMP:FlyBase (experimental mutant-phenotype evidence, C7/H8). The annotation of PIC assembly is consistent with the SAGA complex's well-established role as a transcription coactivator that participates in PIC formation. The expected answer B is thus supported by the database annotation, though the specific GO:0051123 term relies on computational (IBA) rather than direct experimental evidence.",
    "evidence_ids": ["C5", "C7", "C8", "H7", "H8", "H9", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 717-residue sequence contains recognizable histone-fold domains (HFDs), identifiable by their characteristic alpha-beta-alpha-beta-alpha topology with conserved hydrophobic core residues in helical segments (e.g., the regions 'WEQHDQTDVELSQDVCARLAEDASYKVWELINNVKIYSRHSGG…' and '…IFLGGHDDVYLYEWLEYGCGAALQPFLVHYARAYEKMVTRRYVKAKQPAYRIESVPGVRRLEWSTLAAAMCHG…'). HFDs are a well-known family-level feature of TAF proteins (TAF4, TAF5, TAF6, TAF9, TAF12), which are core subunits of the TFIID/SAGA transcription coactivator complexes. From transferable knowledge of other TAF-family proteins, a knowledgeable model can infer that an HFD-containing protein is a TAF-like transcription factor component, placing it squarely in the RNA Pol II transcription initiation/PIC assembly pathway. This distinguishes option B from C (heterotypic cell-cell adhesion, which involves cadherin/integrin/selectin domains absent here) and D (tRNA wobble cytosine modification, which involves methyltransferase or enzymatic domains, not HFDs). Option A (cellular homeostasis) is a very broad GO term referring to maintenance of internal steady state; while transcription broadly supports homeostasis, the specific HFD/TAF-family signature points to the more precise transcription-initiation annotation rather than the generic homeostasis term.",
    "missing_item_specific_fact": "",
    "reason": "The histone-fold domain is a directly observable sequence feature that triggers a well-established family-level inference: HFD-containing proteins are TAF-like components of TFIID/SAGA, which participate in RNA Pol II preinitiation complex assembly. This reasoning uses knowledge transferable from other TAF proteins and the general architecture of the transcription machinery, without requiring recall of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with HFD-containing TAF-like proteins. Option A (cellular homeostasis) is a broad GO term that does not capture the specific transcription-initiation role indicated by the HFD/TAF signature. Option B is the most specific and mechanistically appropriate choice given the sequence features."
  },
  "important_caveats": [
    "The GO:0051123 annotation for this protein carries IBA:GO_Central evidence (computational inference from SAGA complex membership), not direct experimental evidence. The experimentally supported GO term is GO:0045944 (positive regulation of transcription by RNA Pol II, IMP).",
    "The protein is a Drosophila-specific SAGA subunit (Saf6) that replaces canonical TAF6 in Drosophila SAGA; its role in PIC assembly is inferred from complex membership rather than demonstrated directly for this paralog.",
    "The histone-fold domain recognition from raw sequence is a reasonable expert inference but is not trivially obvious to all models; it depends on pattern recognition of the HFD fold signature.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt Q9VPT4, so the annotation applies to the exact sequence presented."
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
  "benchmark_sequence_length": 717,
  "benchmark_sequence_sha256": "dcc9cca01c70f93b7356a2220c9976ed7dbe8be815d3724a2a97d2007d295655",
  "current_entry_audit": {
    "entryVersion": 164,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-10-01",
    "sequenceVersion": 2
  },
  "current_record_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 717,
  "current_source_sequence_sha256": "dcc9cca01c70f93b7356a2220c9976ed7dbe8be815d3724a2a97d2007d295655",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 162,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VPT4",
  "selected_historical_entry_version": 162,
  "selected_historical_record_sha256": "0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063",
  "selected_historical_source_sequence_length": 717,
  "selected_historical_source_sequence_sha256": "dcc9cca01c70f93b7356a2220c9976ed7dbe8be815d3724a2a97d2007d295655",
  "selected_historical_version": {
    "accession": "Q9VPT4",
    "database": "Swiss-Prot",
    "entryVersion": 162,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SAF6_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VPT4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":164,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-10-01\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20008933\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0031281\",\"source\":\"FlyBase\"}],\"value\":\"SAGA factor-like TAF6\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20008933\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21764853\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24493646\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30559249\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34807910\",\"source\":\"PubMed\"}],\"value\":\"Component of the transcription regulatory complex SAGA, a multiprotein complex that activates transcription by remodeling chromatin and mediating histone acetylation and deubiquitination (PubMed:20008933, PubMed:21764853, PubMed:24493646, PubMed:30559249). The SAGA complex predominantly acetylates histone H3 (PubMed:30559249). Involved in SAGA complex coactivator function but not essential for SAGA complex assembly, histone-modifying activity or chromosomal recruitment (PubMed:20008933). Required for oogenesis; involved in transcriptional activation (PubMed:34807910)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33004486\",\"source\":\"PubMed\"}],\"id\":\"GO:0045893\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:positive regulation of DNA-templated transcription\"},{\"key\":\"GoEvidenceType\",\"value\":\"NAS:ComplexPortal\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/36",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000315\",\"id\":\"20008933\",\"source\":\"PubMed\"}],\"id\":\"GO:0045944\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:positive regulation of transcription by RNA polymerase II\"},{\"key\":\"GoEvidenceType\",\"value\":\"IMP:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/37",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0051123\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:RNA polymerase II preinitiation complex assembly\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/38",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Swanson S.K.\",\"Mushegian A.\",\"Florens L.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20008933\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.1846409\"}],\"citationType\":\"journal article\",\"firstPage\":\"2818\",\"id\":\"20008933\",\"journal\":\"Genes Dev.\",\"lastPage\":\"2823\",\"publicationDate\":\"2009\",\"title\":\"A novel histone fold domain-containing protein that replaces TAF6 in Drosophila SAGA is required for SAGA-dependent gene expression.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\",\"INTERACTION WITH TAF9\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Dyer J.O.\",\"Seidel C.\",\"Box A.\",\"Swanson S.K.\",\"Peak A.\",\"Florens L.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21764853\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.2046211\"}],\"citationType\":\"journal article\",\"firstPage\":\"1499\",\"id\":\"21764853\",\"journal\":\"Genes Dev.\",\"lastPage\":\"1509\",\"publicationDate\":\"2011\",\"title\":\"Post-transcription initiation function of the ubiquitous SAGA complex in tissue-specific gene activation.\",\"volume\":\"25\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\",\"DEVELOPMENTAL STAGE\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Mohan R.D.\",\"Dialynas G.\",\"Weake V.M.\",\"Liu J.\",\"Martin-Brown S.\",\"Florens L.\",\"Washburn M.P.\",\"Workman J.L.\",\"Abmayr S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24493646\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.225151.113\"}],\"citationType\":\"journal article\",\"firstPage\":\"259\",\"id\":\"24493646\",\"journal\":\"Genes Dev.\",\"lastPage\":\"272\",\"publicationDate\":\"2014\",\"title\":\"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination and leads to neural and retinal degeneration.\",\"volume\":\"28\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Torres-Zelada E.F.\",\"Stephenson R.E.\",\"Alpsoy A.\",\"Anderson B.D.\",\"Swanson S.K.\",\"Florens L.\",\"Dykhuizen E.C.\",\"Washburn M.P.\",\"Weake V.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30559249\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.214072\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30559249\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"The Drosophila Dbf4 ortholog Chiffon forms a complex with Gcn5 that is necessary for histone acetylation and viability.\",\"volume\":\"132\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Soffers J.H.M.\",\"Alcantara S.G.\",\"Li X.\",\"Shao W.\",\"Seidel C.W.\",\"Li H.\",\"Zeitlinger J.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34807910\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pgen.1009668\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1009668\",\"id\":\"34807910\",\"journal\":\"PLoS Genet.\",\"lastPage\":\"e1009668\",\"publicationDate\":\"2021\",\"title\":\"The SAGA core module is critical during Drosophila oogenesis and is broadly recruited to promoters.\",\"volume\":\"17\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":8,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH GCN5\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:33:33.097127+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VPT4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H1",
  "excerpt": "ID   SAF6_DROME              Reviewed;         717 AA.\nAC   Q9VPT4; Q8T039;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2002, sequence version 2.\nDT   28-JAN-2026, entry version 162.\nDE   RecName: Full=SAGA factor-like TAF6 {ECO:0000303|PubMed:20008933, ECO:0000312|FlyBase:FBgn0031281};\nGN   Name=Saf6 {ECO:0000303|PubMed:20008933, ECO:0000312|FlyBase:FBgn0031281};\nGN   ORFNames=CG3883 {ECO:0000312|FlyBase:FBgn0031281};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.451282+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063",
  "url": "https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, INTERACTION WITH TAF9,\nRP   SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, AND IDENTIFICATION BY MASS\nRP   SPECTROMETRY.\nRX   PubMed=20008933; DOI=10.1101/gad.1846409;\nRA   Weake V.M., Swanson S.K., Mushegian A., Florens L., Washburn M.P.,\nRA   Abmayr S.M., Workman J.L.;\nRT   \"A novel histone fold domain-containing protein that replaces TAF6 in\nRT   Drosophila SAGA is required for SAGA-dependent gene expression.\";\nRL   Genes Dev. 23:2818-2823(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.451282+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063",
  "url": "https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, DEVELOPMENTAL STAGE, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=21764853; DOI=10.1101/gad.2046211;\nRA   Weake V.M., Dyer J.O., Seidel C., Box A., Swanson S.K., Peak A.,\nRA   Florens L., Washburn M.P., Abmayr S.M., Workman J.L.;\nRT   \"Post-transcription initiation function of the ubiquitous SAGA complex in\nRT   tissue-specific gene activation.\";\nRL   Genes Dev. 25:1499-1509(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.451282+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063",
  "url": "https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H4",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, SUBCELLULAR LOCATION, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=24493646; DOI=10.1101/gad.225151.113;\nRA   Mohan R.D., Dialynas G., Weake V.M., Liu J., Martin-Brown S., Florens L.,\nRA   Washburn M.P., Workman J.L., Abmayr S.M.;\nRT   \"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination\nRT   and leads to neural and retinal degeneration.\";\nRL   Genes Dev. 28:259-272(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.451282+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063",
  "url": "https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H5",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, AND IDENTIFICATION BY MASS\nRP   SPECTROMETRY.\nRX   PubMed=30559249; DOI=10.1242/jcs.214072;\nRA   Torres-Zelada E.F., Stephenson R.E., Alpsoy A., Anderson B.D.,\nRA   Swanson S.K., Florens L., Dykhuizen E.C., Washburn M.P., Weake V.M.;\nRT   \"The Drosophila Dbf4 ortholog Chiffon forms a complex with Gcn5 that is\nRT   necessary for histone acetylation and viability.\";\nRL   J. Cell Sci. 132:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.451282+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063",
  "url": "https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H6",
  "excerpt": "RN   [8] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH GCN5, SUBCELLULAR LOCATION, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=34807910; DOI=10.1371/journal.pgen.1009668;\nRA   Soffers J.H.M., Alcantara S.G., Li X., Shao W., Seidel C.W., Li H.,\nRA   Zeitlinger J., Abmayr S.M., Workman J.L.;\nRT   \"The SAGA core module is critical during Drosophila oogenesis and is\nRT   broadly recruited to promoters.\";\nRL   PLoS Genet. 17:e1009668-e1009668(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.451282+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063",
  "url": "https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H7",
  "excerpt": "CC   -!- FUNCTION: Component of the transcription regulatory complex SAGA, a\nCC       multiprotein complex that activates transcription by remodeling\nCC       chromatin and mediating histone acetylation and deubiquitination\nCC       (PubMed:20008933, PubMed:21764853, PubMed:24493646, PubMed:30559249).\nCC       The SAGA complex predominantly acetylates histone H3 (PubMed:30559249).\nCC       Involved in SAGA complex coactivator function but not essential for\nCC       SAGA complex assembly, histone-modifying activity or chromosomal\nCC       recruitment (PubMed:20008933). Required for oogenesis; involved in\nCC       transcriptional activation (PubMed:34807910).\nCC       {ECO:0000269|PubMed:20008933, ECO:0000269|PubMed:21764853,\nCC       ECO:0000269|PubMed:24493646, ECO:0000269|PubMed:30559249,\nCC       ECO:0000269|PubMed:34807910}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.451282+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-134",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063",
  "url": "https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0045944; P:positive regulation of transcription by RNA polymerase II; IMP:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.451282+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 199-199",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063",
  "url": "https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)

```json
{
  "entry_version": 162,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0051123; P:RNA polymerase II preinitiation complex assembly; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.451282+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 200-200",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063",
  "url": "https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0002101\nname: tRNA wobble cytosine modification\nnamespace: biological_process\ndef: \"The process in which a cytosine at position 34 of a tRNA is post-transcriptionally modified. The wobble nucleoside of the tRNA sequence  (position 34) corresponds to the first position of the anticodon.\" [GOC:hjd, ISBN:155581073X]\nis_a: GO:0002097 ! tRNA wobble base modification\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0002101",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 15011-15017",
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
  "excerpt": "[Term]\nid: GO:0019725\nname: cellular homeostasis\nnamespace: biological_process\ndef: \"Any process involved in the maintenance of an internal steady state at the level of the cell.\" [GOC:isa_complete, GOC:jl, ISBN:0395825172]\nsubset: goslim_candida\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_plant\nis_a: GO:0042592 ! homeostatic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019725",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 152549-152558",
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
  "excerpt": "[Term]\nid: GO:0034113\nname: heterotypic cell-cell adhesion\nnamespace: biological_process\ndef: \"The attachment of a cell to a cell of a different type via adhesion molecules.\" [GOC:add]\ncomment: Note that this term is not synonymous with 'heterophilic cell adhesion ; GO:0007157'; the process may occur by homophilic or heterophilic mechanisms.\nis_a: GO:0098609 ! cell-cell adhesion\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0034113",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 205695-205702",
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
  "excerpt": "[Term]\nid: GO:0051123\nname: RNA polymerase II preinitiation complex assembly\nnamespace: biological_process\ndef: \"The formation of a large multiprotein-DNA complex that self-assembles on gene promoter through the sequential recruitment of the general initiation factors that compose the preinitiation complex (PIC) (which may include TFIIA, TFIIB, TFIID, TFIIE, TFIIF, and TFIIH complexes). The PIC engages RNA polymerase II on its DNA template strand and sparks polymerization of the first few RNA nucleotides of the nascent transcript, of which 8 are base-paired with the DNA template within a DNA bubble. PIC assembly may result in a pause step, which marks the end of the PIC assembly and may be followed by promoter clearance (exact synonym: promoter escape). For RNA polymerase II PIC assembly is preceded by the formation of a nucleosome-free region that allows the transcription machinery to access the promoter DNA.\" [GOC:txnOH, PMID:15020047, PMID:31300188]\nsynonym: \"RNA polymerase II transcription PIC biosynthesis\" EXACT []\nsynonym: \"RNA polymerase II transcription PIC formation\" EXACT []\nsynonym: \"RNA polymerase II transcriptional preinitiation complex assembly\" EXACT []\nsynonym: \"RNA polymerase II transcriptional preinitiation complex formation\" EXACT []\nis_a: GO:0070897 ! transcription preinitiation complex assembly\nrelationship: part_of GO:0006367 ! transcription initiation at RNA polymerase II promoter\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051123",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 323136-323147",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 156. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
