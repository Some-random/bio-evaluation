# GO_molecular_function_0064

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0064.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — O-methyltransferase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTIRGTLSELSRAADAFAHEVDEAGYGDYTFLPDNSPFDLSFLTSKGLEARGSLIAAAEKILRLAKGPQGCLASFADTKGIEMGTIQALTQLEVPDKVPLQGSITYEELAGVIRVAPELLQRLVRLAALAGFLIEDESGAVRHTAMSAVFLRDTAAGDTARFLFDVDMRAYSFFADSLRLDPSGQNIGDGPTALAFQHDSDDQGNRPTIWDILERNPIQRARFHSTMQALGSFPSHLLKHILVAHDWHSIGSLVDVGGSLGHASLVIAENFPEIRITVQDLPDVVERGRSSLPTVPHAERVSFQAHDLFQEQAIIADAYFLRQILHDWPDGDAERIVRCLIPAMRPGAKLLIMDIVVPEPGAISPYMEKYLRTYDVSMFSMFSAKERTVQQLRDLVERCSARLQFQGISCPPGSATSLLSWVYSAE

[Multiple Choices]
A. O-methyltransferase activity
B. chromatin DNA binding
C. protein-membrane adaptor activity
D. lipid binding
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

> The sequence matches the protein in the supplied source evidence. That entry identifies it as an O-methyltransferase and reports experimentally supported methylation of a phenolic oxygen using S-adenosyl-L-methionine, which supports option A.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a soluble globular protein and contains a glycine-rich segment around DVGGSLG consistent with a SAM-dependent methyltransferase cofactor-binding motif. Transferable knowledge of methyltransferase families makes O-methyltransferase activity a credible choice over chromatin DNA binding, membrane adaptor activity, or lipid binding; the alternatives lack a comparable sequence-based rationale.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level motif and overall sequence context meaningfully distinguish the offered enzymatic option without requiring the exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, O-methyltransferase activity is the only one supported by the sequence-family inference.


### Important caveats

- The glycine-rich motif supports a SAM-dependent methyltransferase-family inference but does not, by itself, establish the exact methyl acceptor or substrate specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble globular protein and contains a glycine-rich segment around DVGGSLG consistent with a SAM-dependent methyltransferase cofactor-binding motif. Transferable knowledge of methyltransferase families makes O-methyltransferase activity a credible choice over chromatin DNA binding, membrane adaptor activity, or lipid binding; the alternatives lack a comparable sequence-based rationale.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level motif and overall sequence context meaningfully distinguish the offered enzymatic option without requiring the exact protein's database annotation."
  },
  "case_id": "GO_molecular_function_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the protein in the supplied source evidence. That entry identifies it as an O-methyltransferase and reports experimentally supported methylation of a phenolic oxygen using S-adenosyl-L-methionine, which supports option A."
  },
  "important_caveats": [
    "The glycine-rich motif supports a SAM-dependent methyltransferase-family inference but does not, by itself, establish the exact methyl acceptor or substrate specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, O-methyltransferase activity is the only one supported by the sequence-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the protein in the supplied source evidence. That entry identifies it as an O-methyltransferase and reports experimentally supported methylation of a phenolic oxygen using S-adenosyl-L-methionine, which supports option A.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a soluble globular protein and contains a glycine-rich segment around DVGGSLG consistent with a SAM-dependent methyltransferase cofactor-binding motif. Transferable knowledge of methyltransferase families makes O-methyltransferase activity a credible choice over chromatin DNA binding, membrane adaptor activity, or lipid binding; the alternatives lack a comparable sequence-based rationale.",
    "missing_item_specific_fact": "",
    "reason": "The family-level motif and overall sequence context meaningfully distinguish the offered enzymatic option without requiring the exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, O-methyltransferase activity is the only one supported by the sequence-family inference."
  },
  "important_caveats": [
    "The glycine-rich motif supports a SAM-dependent methyltransferase-family inference but does not, by itself, establish the exact methyl acceptor or substrate specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7T8J1Z8) is annotated as 'O-methyltransferase FrzF' with EC 2.1.1.- based on experimental evidence (ECO:0000269, PubMed:33372776). The catalytic activity reactions explicitly show O-methylation (hydroxyphenyl → methoxyphenyl) using SAM as methyl donor. GO:0008171 (O-methyltransferase activity) is annotated with IEA:InterPro evidence. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains textbook Class I (Rossmann-fold) methyltransferase motifs: a glycine-rich SAM-binding loop 'GGSLGH' (~residues 228-233, matching the GxGxG consensus), the 'GDL' SAM-contact motif (~residues 247-249), and the catalytic-core 'DIVVPE' motif (~residues 310-315). These features are shared across hundreds of characterized SAM-dependent methyltransferases (e.g., catechol-O-methyltransferase, DNA methyltransferases, small-molecule O-methyltransferases). The ~427-aa single-domain architecture is consistent with a standalone methyltransferase. In contrast, chromatin DNA binding (B) requires histone-fold, zinc-finger, or winged-helix motifs; protein-membrane adaptor activity (C) requires PH, C1/C2, or BAR domains; lipid binding (D) requires START, CRAL-TRIO, or amphipathic helix motifs. None of these alternative structural signatures are present. Since only one methyltransferase option (A) is offered among the four choices, recognizing the Rossmann-fold methyltransferase superfamily from its conserved motifs suffices to select A over B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GxGxG and DIVVPE motifs are among the most widely recognized sequence signatures in protein biochemistry, learned from numerous characterized methyltransferases across all domains of life. Their presence in this sequence, combined with the absence of any DNA-binding, membrane-binding, or lipid-binding structural motifs, provides a concrete and transferable basis to select option A over the other three alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent entirely different molecular function categories (catalysis vs. DNA binding vs. adaptor vs. lipid binding). The methyltransferase motifs clearly point to A, and the other three options require structurally distinct domains that are absent from the sequence. No ambiguity exists among the offered choices.


### Important caveats

- The GO annotation for this protein is IEA:InterPro (inferred from domain match), while the functional characterization is experimental (ECO:0000269). The sequence-level motifs support the methyltransferase assignment independently.
- The specific 'O-' prefix in O-methyltransferase activity cannot be distinguished from N- or C-methyltransferase by sequence motifs alone within the Rossmann-fold superfamily. However, since no other methyltransferase subtype is offered as a distractor, this does not create ambiguity among the four choices.
- The protein is a fungal natural-product biosynthetic enzyme (FR901483 cluster), a context not provided in the original input but irrelevant to the sequence-motif-based inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains textbook Class I (Rossmann-fold) methyltransferase motifs: a glycine-rich SAM-binding loop 'GGSLGH' (~residues 228-233, matching the GxGxG consensus), the 'GDL' SAM-contact motif (~residues 247-249), and the catalytic-core 'DIVVPE' motif (~residues 310-315). These features are shared across hundreds of characterized SAM-dependent methyltransferases (e.g., catechol-O-methyltransferase, DNA methyltransferases, small-molecule O-methyltransferases). The ~427-aa single-domain architecture is consistent with a standalone methyltransferase. In contrast, chromatin DNA binding (B) requires histone-fold, zinc-finger, or winged-helix motifs; protein-membrane adaptor activity (C) requires PH, C1/C2, or BAR domains; lipid binding (D) requires START, CRAL-TRIO, or amphipathic helix motifs. None of these alternative structural signatures are present. Since only one methyltransferase option (A) is offered among the four choices, recognizing the Rossmann-fold methyltransferase superfamily from its conserved motifs suffices to select A over B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GxGxG and DIVVPE motifs are among the most widely recognized sequence signatures in protein biochemistry, learned from numerous characterized methyltransferases across all domains of life. Their presence in this sequence, combined with the absence of any DNA-binding, membrane-binding, or lipid-binding structural motifs, provides a concrete and transferable basis to select option A over the other three alternatives."
  },
  "case_id": "GO_molecular_function_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H3",
      "H4",
      "H5",
      "H6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8J1Z8) is annotated as 'O-methyltransferase FrzF' with EC 2.1.1.- based on experimental evidence (ECO:0000269, PubMed:33372776). The catalytic activity reactions explicitly show O-methylation (hydroxyphenyl → methoxyphenyl) using SAM as methyl donor. GO:0008171 (O-methyltransferase activity) is annotated with IEA:InterPro evidence. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA:InterPro (inferred from domain match), while the functional characterization is experimental (ECO:0000269). The sequence-level motifs support the methyltransferase assignment independently.",
    "The specific 'O-' prefix in O-methyltransferase activity cannot be distinguished from N- or C-methyltransferase by sequence motifs alone within the Rossmann-fold superfamily. However, since no other methyltransferase subtype is offered as a distractor, this does not create ambiguity among the four choices.",
    "The protein is a fungal natural-product biosynthetic enzyme (FR901483 cluster), a context not provided in the original input but irrelevant to the sequence-motif-based inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different molecular function categories (catalysis vs. DNA binding vs. adaptor vs. lipid binding). The methyltransferase motifs clearly point to A, and the other three options require structurally distinct domains that are absent from the sequence. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8J1Z8) is annotated as 'O-methyltransferase FrzF' with EC 2.1.1.- based on experimental evidence (ECO:0000269, PubMed:33372776). The catalytic activity reactions explicitly show O-methylation (hydroxyphenyl → methoxyphenyl) using SAM as methyl donor. GO:0008171 (O-methyltransferase activity) is annotated with IEA:InterPro evidence. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H3", "H4", "H5", "H6", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains textbook Class I (Rossmann-fold) methyltransferase motifs: a glycine-rich SAM-binding loop 'GGSLGH' (~residues 228-233, matching the GxGxG consensus), the 'GDL' SAM-contact motif (~residues 247-249), and the catalytic-core 'DIVVPE' motif (~residues 310-315). These features are shared across hundreds of characterized SAM-dependent methyltransferases (e.g., catechol-O-methyltransferase, DNA methyltransferases, small-molecule O-methyltransferases). The ~427-aa single-domain architecture is consistent with a standalone methyltransferase. In contrast, chromatin DNA binding (B) requires histone-fold, zinc-finger, or winged-helix motifs; protein-membrane adaptor activity (C) requires PH, C1/C2, or BAR domains; lipid binding (D) requires START, CRAL-TRIO, or amphipathic helix motifs. None of these alternative structural signatures are present. Since only one methyltransferase option (A) is offered among the four choices, recognizing the Rossmann-fold methyltransferase superfamily from its conserved motifs suffices to select A over B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The GxGxG and DIVVPE motifs are among the most widely recognized sequence signatures in protein biochemistry, learned from numerous characterized methyltransferases across all domains of life. Their presence in this sequence, combined with the absence of any DNA-binding, membrane-binding, or lipid-binding structural motifs, provides a concrete and transferable basis to select option A over the other three alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different molecular function categories (catalysis vs. DNA binding vs. adaptor vs. lipid binding). The methyltransferase motifs clearly point to A, and the other three options require structurally distinct domains that are absent from the sequence. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA:InterPro (inferred from domain match), while the functional characterization is experimental (ECO:0000269). The sequence-level motifs support the methyltransferase assignment independently.",
    "The specific 'O-' prefix in O-methyltransferase activity cannot be distinguished from N- or C-methyltransferase by sequence motifs alone within the Rossmann-fold superfamily. However, since no other methyltransferase subtype is offered as a distractor, this does not create ambiguity among the four choices.",
    "The protein is a fungal natural-product biosynthetic enzyme (FR901483 cluster), a context not provided in the original input but irrelevant to the sequence-motif-based inference."
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
  "benchmark_sequence_length": 427,
  "benchmark_sequence_sha256": "6ca0908cdd116ff442cc6cf6287077f0ed455a179f72a73421b513fdffa4f3b0",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 427,
  "current_source_sequence_sha256": "6ca0908cdd116ff442cc6cf6287077f0ed455a179f72a73421b513fdffa4f3b0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8J1Z8",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "selected_historical_source_sequence_length": 427,
  "selected_historical_source_sequence_sha256": "6ca0908cdd116ff442cc6cf6287077f0ed455a179f72a73421b513fdffa4f3b0",
  "selected_historical_version": {
    "accession": "A0A7T8J1Z8",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZF_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8J1Z8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein F\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase FrzF\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase; part of the gene cluster that mediates the biosynthesis of the alkaloid (-)-FR901483, a potent immunosuppressant that shows efficacy in animal models and a probable inhibitor of purine nucleotide biosynthesis by targeting phosphoribosylpyrophosphate amidotransferase (PPAT) (PubMed:33372776). Within the pathway, FrzF methylates the phenolic oxygen at position C4 (PubMed:33372776). The biosynthesis of (-)-FR901483 starts with the condensation of two L-tyrosines to yield (S,S)-dityrosyl-piperazine. This process occurs in 3 steps with the non-canonical nonribosomal peptide synthetase FrzA catalyzing the reduction of L-tyrosine into L-tyrosinal, the spontaneous condensation of 2 L-tyrosinal units, and the subsequent reduction by the NmrA-like family domain-containing oxidoreductase FrzB. The cytochrome P450 monooxygenase FrzC then performs coupling between N10 and C1' to morph the piperazine into a 1,4-diazabicyclo[3.2.1]octane spiro-fused to a 2,5-cyclohexadienone. The dienone portion is further reduced to cyclohexanone by the flavin-dependent reductase FrzD. The methyltranserases (MTs) FrzE and FrzF are then involved in the methylation at the C10' amine and the C4 phenolic oxygen, respectively. The order of the two MTs appear to be interchangeable. Cleavage of the C9-N10' bond by the dioxygenase FrzG then leads to formation of a conjugated iminium. In addition to the oxidation of C9, an additional dehydrogenation between C7 and C8 can occur to give a likely shunt product. The next biosynthetic step is the intramolecular aldol condensation catalyzed by the newly identified aldolase FrzH to yield an aza-tricyclic product with the formation of a C9-C3' bond (PubMed:33372776). The short-chain dehydrogenase/reductase FrzI then produces dephospho-(-)-FR901483 that is phosphorylated at C4'-OH into (-)-FR901483 by the phosphotransferase FrzJ (PubMed:33372776)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:83592\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"name\":\"(1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:83591\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:233175\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:233177\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:83596\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"name\":\"(1S,4S)-4-[(4-hydroxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:83595\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:233176\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:233178\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0008171\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:O-methyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0046983\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:protein dimerization activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   FRZF_CLASX              Reviewed;         427 AA.\nAC   A0A7T8J1Z8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=O-methyltransferase FrzF {ECO:0000303|PubMed:33372776};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein F {ECO:0000303|PubMed:33372776};\nGN   Name=FrzF {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: O-methyltransferase; part of the gene cluster that mediates\nCC       the biosynthesis of the alkaloid (-)-FR901483, a potent\nCC       immunosuppressant that shows efficacy in animal models and a probable\nCC       inhibitor of purine nucleotide biosynthesis by targeting\nCC       phosphoribosylpyrophosphate amidotransferase (PPAT) (PubMed:33372776).\nCC       Within the pathway, FrzF methylates the phenolic oxygen at position C4\nCC       (PubMed:33372776). The biosynthesis of (-)-FR901483 starts with the\nCC       condensation of two L-tyrosines to yield (S,S)-dityrosyl-piperazine.\nCC       This process occurs in 3 steps with the non-canonical nonribosomal\nCC       peptide synthetase FrzA catalyzing the reduction of L-tyrosine into L-\nCC       tyrosinal, the spontaneous condensation of 2 L-tyrosinal units, and the\nCC       subsequent reduction by the NmrA-like family domain-containing\nCC       oxidoreductase FrzB. The cytochrome P450 monooxygenase FrzC then\nCC       performs coupling between N10 and C1' to morph the piperazine into a\nCC       1,4-diazabicyclo[3.2.1]octane spiro-fused to a 2,5-cyclohexadienone.\nCC       The dienone portion is further reduced to cyclohexanone by the flavin-\nCC       dependent reductase FrzD. The methyltranserases (MTs) FrzE and FrzF are\nCC       then involved in the methylation at the C10' amine and the C4 phenolic\nCC       oxygen, respectively. The order of the two MTs appear to be\nCC       interchangeable. Cleavage of the C9-N10' bond by the dioxygenase FrzG\nCC       then leads to formation of a conjugated iminium. In addition to the\nCC       oxidation of C9, an additional dehydrogenation between C7 and C8 can\nCC       occur to give a likely shunt product. The next biosynthetic step is the\nCC       intramolecular aldol condensation catalyzed by the newly identified\nCC       aldolase FrzH to yield an aza-tricyclic product with the formation of a\nCC       C9-C3' bond (PubMed:33372776). The short-chain dehydrogenase/reductase\nCC       FrzI then produces dephospho-(-)-FR901483 that is phosphorylated at\nCC       C4'-OH into (-)-FR901483 by the phosphotransferase FrzJ\nCC       (PubMed:33372776). {ECO:0000269|PubMed:33372776}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-\nCC         diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-\nCC         L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2,5-\nCC         diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-\nCC         L-homocysteine + H(+); Xref=Rhea:RHEA:83591, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:233175,\nCC         ChEBI:CHEBI:233177; Evidence={ECO:0000269|PubMed:33372776};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83592;\nCC         Evidence={ECO:0000269|PubMed:33372776};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(1S,4S)-4-[(4-hydroxyphenyl)methyl]-2-methyl-2,5-\nCC         diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-\nCC         L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2-methyl-2,5-\nCC         diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-\nCC         L-homocysteine + H(+); Xref=Rhea:RHEA:83595, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:233176,\nCC         ChEBI:CHEBI:233178; Evidence={ECO:0000269|PubMed:33372776};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83596;\nCC         Evidence={ECO:0000269|PubMed:33372776};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0008171; F:O-methyltransferase activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0008171\nname: O-methyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a methyl group to the oxygen atom of an acceptor molecule.\" [GOC:ai]\nxref: Reactome:R-HSA-5578717 \"BCDIN3D dimethylates 5' phosphate of pre-miR-145\"\nxref: Reactome:R-HSA-5629203 \"HENMT1 methylates 2' hydroxyl at 3' end of piRNA in 4xMeR-PIWIL1:piRNA:TDRD6:TDRKH\"\nxref: Reactome:R-HSA-5629218 \"HENMT1 methylates 2' hydroxyl at 3' end of piRNA in 6xMeR-PIWIL2:piRNA:TDRD1:TDRD12:DDX4:ASZ:MOV10L1\"\nxref: Reactome:R-HSA-5629237 \"HENMT1 methylates 2' hydroxyl at 3' end of piRNA in MeR-PIWIL4:piRNA:TDRD9:MAEL:TDRKH\"\nxref: Reactome:R-HSA-6790907 \"Box C/D snoRNP methylates ribonucleotides in pre-rRNA yielding 2'-O-methylribonucleotides\"\nis_a: GO:0008168 ! methyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008171",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 80302-80313",
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
  "excerpt": "[Term]\nid: GO:0008289\nname: lipid binding\nnamespace: molecular_function\ndef: \"Binding to a lipid.\" [GOC:ai]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nis_a: GO:0005488 ! binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008289",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 81641-81661",
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
  "excerpt": "[Term]\nid: GO:0031490\nname: chromatin DNA binding\nnamespace: molecular_function\ndef: \"Binding to DNA that is assembled into chromatin.\" [GOC:mah]\nis_a: GO:0003677 ! DNA binding\nis_a: GO:0003682 ! chromatin binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031490",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 177022-177029",
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
  "excerpt": "[Term]\nid: GO:0043495\nname: protein-membrane adaptor activity\nnamespace: molecular_function\ndef: \"The binding activity of a molecule that brings together a protein or a protein complex with a membrane, either via membrane lipid binding or by interacting with a membrane protein, to establish or maintain the localization of the protein, protein complex or organelle.\" [GOC:curators]\nsynonym: \"anchoring\" RELATED []\nsynonym: \"protein membrane adaptor\" EXACT []\nsynonym: \"protein membrane adaptor activity\" EXACT []\nsynonym: \"protein membrane anchor\" RELATED []\nxref: Reactome:R-HSA-5333678 \"CPNEs bind PL\"\nxref: Reactome:R-HSA-6809764 \"SBF1 binds MTMR2\"\nis_a: GO:0030674 ! protein-macromolecule adaptor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043495",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 247862-247874",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
