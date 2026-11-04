# GO_biological_process_0154

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0154.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **A** — lysine biosynthetic process via diaminopimelate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | contradicted | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSVKKAGVLGATGSVGQRFILLLSKHPEFEIHALGASSRSAGKKYKDAASWKQTETLPETEQDIVVQECKPEGNFLECDVVFSGLDADVAGDIEKSFVEAGLAVVSNAKNYRREKDVPLVVPIVNPEHIDVVENKVKQAVSKGGKKPGFIICISNCSTAGLVAPLKPLVEKFGPIDALTTTTLQAISGAGFSPGVSGMDILDNIVPYISGEEDKLEWETKKILGGVNAEGTEFVPIPESEMKVSAQCNRVPVIDGHTECISLRFANRPAPSVEDVKQCLREYECAASKLGCHSAPKQTIHVLDQPDRPQPRLDRDRDSGYGVSVGRIREDSLLDFKMVVLSHNTIIGAAGAGILIAEILKAKNII

[Multiple Choices]
A. lysine biosynthetic process via diaminopimelate
B. axonal transport of mitochondrion
C. protein destabilization
D. heme biosynthetic process
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

### Expected-answer support: contradicted

> The sequence-matched record identifies a Candida albicans aspartate-semialdehyde dehydrogenase. Its documented reaction supplies the aspartate-family amino-acid pathway, including homoserine/threonine branches. The key's DAP-dependent lysine process is not the lysine biosynthetic route used by fungi. Although the record contains a lysine-via-DAP GO annotation, it is computationally assigned and does not outweigh the organism-specific pathway evidence.

Citations as saved: [C3](#evidence-c3), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H11](#evidence-h11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an aspartate-semialdehyde-dehydrogenase family enzyme: its conserved enzyme motifs and nucleotide-binding fold support a metabolic enzyme rather than a mitochondrial transport or protein-destabilization role. Transferable knowledge that this enzyme acts in aspartate-family amino-acid biosynthesis makes option A the only remotely relevant offered choice; in organisms with the DAP lysine route, this enzyme is part of that pathway.


**Missing item-specific fact**

> Whether this particular protein's organism uses the DAP-dependent lysine pathway. Family-level recognition alone does not establish that pathway for this fungal protein.


**Reason**

> A family-based inference meaningfully separates A from the unrelated alternatives, so the choice is not purely lookup-dependent. But the inference is only a plausible match among these choices, not a reliable conclusion about this protein's organism-specific lysine pathway; the supplied key appears biologically incorrect for the matched fungal protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second option is comparably plausible. The concern is that the keyed option is an inappropriate pathway for this protein, not that multiple offered options fit equally well.


### Important caveats

- The matched UniProt record includes option A as an IEA:UniProtKB-UniPathway annotation, but that computational annotation does not establish that the Candida protein participates in DAP-dependent lysine biosynthesis.
- The source snapshot used by the benchmark author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an aspartate-semialdehyde-dehydrogenase family enzyme: its conserved enzyme motifs and nucleotide-binding fold support a metabolic enzyme rather than a mitochondrial transport or protein-destabilization role. Transferable knowledge that this enzyme acts in aspartate-family amino-acid biosynthesis makes option A the only remotely relevant offered choice; in organisms with the DAP lysine route, this enzyme is part of that pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Whether this particular protein's organism uses the DAP-dependent lysine pathway. Family-level recognition alone does not establish that pathway for this fungal protein.",
    "reason": "A family-based inference meaningfully separates A from the unrelated alternatives, so the choice is not purely lookup-dependent. But the inference is only a plausible match among these choices, not a reliable conclusion about this protein's organism-specific lysine pathway; the supplied key appears biologically incorrect for the matched fungal protein."
  },
  "case_id": "GO_biological_process_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C3",
      "C5",
      "C6",
      "C7",
      "H11"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched record identifies a Candida albicans aspartate-semialdehyde dehydrogenase. Its documented reaction supplies the aspartate-family amino-acid pathway, including homoserine/threonine branches. The key's DAP-dependent lysine process is not the lysine biosynthetic route used by fungi. Although the record contains a lysine-via-DAP GO annotation, it is computationally assigned and does not outweigh the organism-specific pathway evidence."
  },
  "important_caveats": [
    "The matched UniProt record includes option A as an IEA:UniProtKB-UniPathway annotation, but that computational annotation does not establish that the Candida protein participates in DAP-dependent lysine biosynthesis.",
    "The source snapshot used by the benchmark author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second option is comparably plausible. The concern is that the keyed option is an inappropriate pathway for this protein, not that multiple offered options fit equally well."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0154",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched record identifies a Candida albicans aspartate-semialdehyde dehydrogenase. Its documented reaction supplies the aspartate-family amino-acid pathway, including homoserine/threonine branches. The key's DAP-dependent lysine process is not the lysine biosynthetic route used by fungi. Although the record contains a lysine-via-DAP GO annotation, it is computationally assigned and does not outweigh the organism-specific pathway evidence.",
    "evidence_ids": ["C3", "C5", "C6", "C7", "H11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an aspartate-semialdehyde-dehydrogenase family enzyme: its conserved enzyme motifs and nucleotide-binding fold support a metabolic enzyme rather than a mitochondrial transport or protein-destabilization role. Transferable knowledge that this enzyme acts in aspartate-family amino-acid biosynthesis makes option A the only remotely relevant offered choice; in organisms with the DAP lysine route, this enzyme is part of that pathway.",
    "missing_item_specific_fact": "Whether this particular protein's organism uses the DAP-dependent lysine pathway. Family-level recognition alone does not establish that pathway for this fungal protein.",
    "reason": "A family-based inference meaningfully separates A from the unrelated alternatives, so the choice is not purely lookup-dependent. But the inference is only a plausible match among these choices, not a reliable conclusion about this protein's organism-specific lysine pathway; the supplied key appears biologically incorrect for the matched fungal protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second option is comparably plausible. The concern is that the keyed option is an inappropriate pathway for this protein, not that multiple offered options fit equally well."
  },
  "important_caveats": [
    "The matched UniProt record includes option A as an IEA:UniProtKB-UniPathway annotation, but that computational annotation does not establish that the Candida protein participates in DAP-dependent lysine biosynthesis.",
    "The source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q5ALM0) annotates GO:0009089 (lysine biosynthetic process via diaminopimelate) with evidence code IEA:UniProtKB-UniPathway (evidence H11). The protein is experimentally confirmed as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) catalyzing the second step in aspartate-family amino acid biosynthesis (evidence C5, H7, multiple PubMed references with ECO:0000269). The DAP-pathway annotation is a computational assignment from UniPathway rather than direct experimental evidence for this fungal enzyme; experimental evidence specifically supports methionine and threonine biosynthesis (H8, H9). However, ASADH is a shared upstream enzyme in the aspartate biosynthetic network, and GO:0009089 is a legitimate database annotation for this entry. Among the four offered choices, A is the only amino acid biosynthesis option and is the only one consistent with the enzyme's catalytic role.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H7](#evidence-h7), [H11](#evidence-h11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two highly diagnostic family-level motifs: (1) the Rossmann-fold NAD(P)-binding motif 'GVLGATGSVGQRF' (GxGxxG pattern) indicating an NAD(P)-dependent dehydrogenase, and (2) the 'IDGHTEC' motif, which is a well-known catalytic signature of the aspartate-semialdehyde dehydrogenase (ASADH) protein family, conserved across bacterial, archaeal, and fungal orthologs. A knowledgeable model recognizing these motifs can infer the enzyme belongs to the ASADH family, which catalyzes a committed step in aspartate-derived amino acid biosynthesis. Among the four choices, only A (lysine biosynthetic process via diaminopimelate) falls within amino acid biosynthesis. The distractors are clearly incompatible: B (axonal transport of mitochondrion) requires motor/adaptor proteins (kinesin, Milton, Miro) with entirely different architectures; C (protein destabilization) involves E3 ligases or degrons, not a small dehydrogenase; D (heme biosynthetic process) involves porphyrin-pathway enzymes (ALA synthase, porphobilinogen deaminase, ferrochelatase) with distinct folds and motifs. The family-level inference from the IDGH motif and Rossmann fold meaningfully and uniquely selects A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The IDGH catalytic motif and the GxGxxG Rossmann fold are transferable, family-level sequence features recognized across the ASADH superfamily in bacteria, archaea, and fungi. A model trained on protein families can connect these motifs to aspartate-semialdehyde dehydrogenase and hence to amino acid biosynthesis. The three distractors (mitochondrial transport, protein destabilization, heme biosynthesis) involve entirely different protein classes and sequence architectures, making them readily eliminable by a knowledgeable model without needing the exact UniProt annotation for this specific Candida albicans entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the DAP pathway annotation is more typical of bacteria and fungi generally use the α-aminoadipate pathway for lysine, among the four offered choices only A relates to amino acid biosynthesis. No alternative amino acid biosynthesis option (e.g., methionine or threonine biosynthesis) is provided. Options B, C, and D are unambiguously incompatible with a small NAD(P)-dependent dehydrogenase. No two options are defensible simultaneously.


### Important caveats

- The GO:0009089 annotation is IEA (Inferred from Electronic Annotation) from UniPathway, a computational assignment. Experimental evidence (ECO:0000269) specifically supports methionine and threonine biosynthesis, not lysine via DAP, for this fungal enzyme.
- Candida albicans synthesizes lysine primarily via the α-aminoadipate (AAA) pathway, not the DAP pathway. The DAP-pathway annotation may reflect pathway-network membership rather than direct enzymatic involvement in lysine synthesis in this organism.
- The question asks for the 'primary biological process,' and among the four choices A is the only amino acid biosynthesis option, so the pathway-specificity concern does not affect the correct selection from the offered alternatives.
- The sequence is from Candida albicans (a fungus), but this organism identity is not provided in the original model input; the model must rely on sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two highly diagnostic family-level motifs: (1) the Rossmann-fold NAD(P)-binding motif 'GVLGATGSVGQRF' (GxGxxG pattern) indicating an NAD(P)-dependent dehydrogenase, and (2) the 'IDGHTEC' motif, which is a well-known catalytic signature of the aspartate-semialdehyde dehydrogenase (ASADH) protein family, conserved across bacterial, archaeal, and fungal orthologs. A knowledgeable model recognizing these motifs can infer the enzyme belongs to the ASADH family, which catalyzes a committed step in aspartate-derived amino acid biosynthesis. Among the four choices, only A (lysine biosynthetic process via diaminopimelate) falls within amino acid biosynthesis. The distractors are clearly incompatible: B (axonal transport of mitochondrion) requires motor/adaptor proteins (kinesin, Milton, Miro) with entirely different architectures; C (protein destabilization) involves E3 ligases or degrons, not a small dehydrogenase; D (heme biosynthetic process) involves porphyrin-pathway enzymes (ALA synthase, porphobilinogen deaminase, ferrochelatase) with distinct folds and motifs. The family-level inference from the IDGH motif and Rossmann fold meaningfully and uniquely selects A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The IDGH catalytic motif and the GxGxxG Rossmann fold are transferable, family-level sequence features recognized across the ASADH superfamily in bacteria, archaea, and fungi. A model trained on protein families can connect these motifs to aspartate-semialdehyde dehydrogenase and hence to amino acid biosynthesis. The three distractors (mitochondrial transport, protein destabilization, heme biosynthesis) involve entirely different protein classes and sequence architectures, making them readily eliminable by a knowledgeable model without needing the exact UniProt annotation for this specific Candida albicans entry."
  },
  "case_id": "GO_biological_process_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H7",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q5ALM0) annotates GO:0009089 (lysine biosynthetic process via diaminopimelate) with evidence code IEA:UniProtKB-UniPathway (evidence H11). The protein is experimentally confirmed as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) catalyzing the second step in aspartate-family amino acid biosynthesis (evidence C5, H7, multiple PubMed references with ECO:0000269). The DAP-pathway annotation is a computational assignment from UniPathway rather than direct experimental evidence for this fungal enzyme; experimental evidence specifically supports methionine and threonine biosynthesis (H8, H9). However, ASADH is a shared upstream enzyme in the aspartate biosynthetic network, and GO:0009089 is a legitimate database annotation for this entry. Among the four offered choices, A is the only amino acid biosynthesis option and is the only one consistent with the enzyme's catalytic role."
  },
  "important_caveats": [
    "The GO:0009089 annotation is IEA (Inferred from Electronic Annotation) from UniPathway, a computational assignment. Experimental evidence (ECO:0000269) specifically supports methionine and threonine biosynthesis, not lysine via DAP, for this fungal enzyme.",
    "Candida albicans synthesizes lysine primarily via the α-aminoadipate (AAA) pathway, not the DAP pathway. The DAP-pathway annotation may reflect pathway-network membership rather than direct enzymatic involvement in lysine synthesis in this organism.",
    "The question asks for the 'primary biological process,' and among the four choices A is the only amino acid biosynthesis option, so the pathway-specificity concern does not affect the correct selection from the offered alternatives.",
    "The sequence is from Candida albicans (a fungus), but this organism identity is not provided in the original model input; the model must rely on sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the DAP pathway annotation is more typical of bacteria and fungi generally use the α-aminoadipate pathway for lysine, among the four offered choices only A relates to amino acid biosynthesis. No alternative amino acid biosynthesis option (e.g., methionine or threonine biosynthesis) is provided. Options B, C, and D are unambiguously incompatible with a small NAD(P)-dependent dehydrogenase. No two options are defensible simultaneously."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0154",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q5ALM0) annotates GO:0009089 (lysine biosynthetic process via diaminopimelate) with evidence code IEA:UniProtKB-UniPathway (evidence H11). The protein is experimentally confirmed as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) catalyzing the second step in aspartate-family amino acid biosynthesis (evidence C5, H7, multiple PubMed references with ECO:0000269). The DAP-pathway annotation is a computational assignment from UniPathway rather than direct experimental evidence for this fungal enzyme; experimental evidence specifically supports methionine and threonine biosynthesis (H8, H9). However, ASADH is a shared upstream enzyme in the aspartate biosynthetic network, and GO:0009089 is a legitimate database annotation for this entry. Among the four offered choices, A is the only amino acid biosynthesis option and is the only one consistent with the enzyme's catalytic role.",
    "evidence_ids": ["C4", "C5", "H7", "H11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two highly diagnostic family-level motifs: (1) the Rossmann-fold NAD(P)-binding motif 'GVLGATGSVGQRF' (GxGxxG pattern) indicating an NAD(P)-dependent dehydrogenase, and (2) the 'IDGHTEC' motif, which is a well-known catalytic signature of the aspartate-semialdehyde dehydrogenase (ASADH) protein family, conserved across bacterial, archaeal, and fungal orthologs. A knowledgeable model recognizing these motifs can infer the enzyme belongs to the ASADH family, which catalyzes a committed step in aspartate-derived amino acid biosynthesis. Among the four choices, only A (lysine biosynthetic process via diaminopimelate) falls within amino acid biosynthesis. The distractors are clearly incompatible: B (axonal transport of mitochondrion) requires motor/adaptor proteins (kinesin, Milton, Miro) with entirely different architectures; C (protein destabilization) involves E3 ligases or degrons, not a small dehydrogenase; D (heme biosynthetic process) involves porphyrin-pathway enzymes (ALA synthase, porphobilinogen deaminase, ferrochelatase) with distinct folds and motifs. The family-level inference from the IDGH motif and Rossmann fold meaningfully and uniquely selects A.",
    "missing_item_specific_fact": "",
    "reason": "The IDGH catalytic motif and the GxGxxG Rossmann fold are transferable, family-level sequence features recognized across the ASADH superfamily in bacteria, archaea, and fungi. A model trained on protein families can connect these motifs to aspartate-semialdehyde dehydrogenase and hence to amino acid biosynthesis. The three distractors (mitochondrial transport, protein destabilization, heme biosynthesis) involve entirely different protein classes and sequence architectures, making them readily eliminable by a knowledgeable model without needing the exact UniProt annotation for this specific Candida albicans entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the DAP pathway annotation is more typical of bacteria and fungi generally use the α-aminoadipate pathway for lysine, among the four offered choices only A relates to amino acid biosynthesis. No alternative amino acid biosynthesis option (e.g., methionine or threonine biosynthesis) is provided. Options B, C, and D are unambiguously incompatible with a small NAD(P)-dependent dehydrogenase. No two options are defensible simultaneously."
  },
  "important_caveats": [
    "The GO:0009089 annotation is IEA (Inferred from Electronic Annotation) from UniPathway, a computational assignment. Experimental evidence (ECO:0000269) specifically supports methionine and threonine biosynthesis, not lysine via DAP, for this fungal enzyme.",
    "Candida albicans synthesizes lysine primarily via the α-aminoadipate (AAA) pathway, not the DAP pathway. The DAP-pathway annotation may reflect pathway-network membership rather than direct enzymatic involvement in lysine synthesis in this organism.",
    "The question asks for the 'primary biological process,' and among the four choices A is the only amino acid biosynthesis option, so the pathway-specificity concern does not affect the correct selection from the offered alternatives.",
    "The sequence is from Candida albicans (a fungus), but this organism identity is not provided in the original model input; the model must rely on sequence features alone."
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
  "benchmark_sequence_length": 365,
  "benchmark_sequence_sha256": "6addf96ce62cae01385fdd88f8e959e42e783ffb39b551e1fdaa9f5898f59f56",
  "current_entry_audit": {
    "entryVersion": 147,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-04-26",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 365,
  "current_source_sequence_sha256": "6addf96ce62cae01385fdd88f8e959e42e783ffb39b551e1fdaa9f5898f59f56",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 145,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5ALM0",
  "selected_historical_entry_version": 145,
  "selected_historical_record_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "selected_historical_source_sequence_length": 365,
  "selected_historical_source_sequence_sha256": "6addf96ce62cae01385fdd88f8e959e42e783ffb39b551e1fdaa9f5898f59f56",
  "selected_historical_version": {
    "accession": "Q5ALM0",
    "database": "Swiss-Prot",
    "entryVersion": 145,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_CANAL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5ALM0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":147,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-04-26\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Debaryomycetaceae\",\"Candida/Lodderomyces clade\",\"Candida\"],\"scientificName\":\"Candida albicans (strain SC5314 / ATCC MYA-2876)\",\"taxonId\":237561}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17419877\",\"source\":\"PubMed\"}],\"value\":\"CaASADH\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20124701\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32383780\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34469014\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20124701\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32383780\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34469014\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the NADPH-dependent formation of L-aspartate 4-semialdehyde (L-ASA) by the reductive dephosphorylation of 4-phospho-L-aspartate (PubMed:20124701, PubMed:29608391, PubMed:32383780, PubMed:34469014). Mediates the second step in the biosynthesis of amino acids that derive from aspartate (the aspartate family of amino acids), including methioinine and threonine, the latter of which is a precursor to isoleucine (PubMed:20124701)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20124701\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20124701\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009088\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:L-threonine biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/30",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"van het Hoog M.\",\"Rast T.J.\",\"Martchenko M.\",\"Grindle S.\",\"Dignard D.\",\"Hogues H.\",\"Cuomo C.\",\"Berriman M.\",\"Scherer S.\",\"Magee B.B.\",\"Whiteway M.\",\"Chibana H.\",\"Nantel A.\",\"Magee P.T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17419877\"},{\"database\":\"DOI\",\"id\":\"10.1186/gb-2007-8-4-r52\"}],\"citationType\":\"journal article\",\"firstPage\":\"RESEARCH52.1\",\"id\":\"17419877\",\"journal\":\"Genome Biol.\",\"lastPage\":\"RESEARCH52.12\",\"publicationDate\":\"2007\",\"title\":\"Assembly of the Candida albicans genome into sixteen supercontigs aligned on the eight chromosomes.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"type\":\"STRAIN\",\"value\":\"SC5314 / ATCC MYA-2876\"}],\"referenceNumber\":2,\"referencePositions\":[\"GENOME REANNOTATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Launder D.\",\"McKeone K.M.M.\",\"Hunter J.P.\",\"Conti H.R.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32383780\"},{\"database\":\"DOI\",\"id\":\"10.1002/ddr.21682\"}],\"citationType\":\"journal article\",\"firstPage\":\"736\",\"id\":\"32383780\",\"journal\":\"Drug Dev. Res.\",\"lastPage\":\"744\",\"publicationDate\":\"2020\",\"title\":\"Aspartate semialdehyde dehydrogenase inhibition suppresses the growth of the pathogenic fungus Candida albicans.\",\"volume\":\"81\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Friday S.N.\",\"Cheng D.W.\",\"Zagler S.G.\",\"Zanella B.S.\",\"Dietz J.D.\",\"Calbat C.N.\",\"Roach L.T.\",\"Bagnal C.\",\"Faile I.S.\",\"Halkides C.J.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34469014\"},{\"database\":\"DOI\",\"id\":\"10.1002/ddr.21875\"}],\"citationType\":\"journal article\",\"firstPage\":\"447\",\"id\":\"34469014\",\"journal\":\"Drug Dev. Res.\",\"lastPage\":\"460\",\"publicationDate\":\"2022\",\"title\":\"Design and testing of selective inactivators against an antifungal enzyme target.\",\"volume\":\"83\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Arachea B.T.\",\"Liu X.\",\"Pavlovsky A.G.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20124701\"},{\"database\":\"DOI\",\"id\":\"10.1107/s0907444909052834\"}],\"citationType\":\"journal article\",\"firstPage\":\"205\",\"id\":\"20124701\",\"journal\":\"Acta Crystallogr. D\",\"lastPage\":\"212\",\"publicationDate\":\"2010\",\"title\":\"Expansion of the aspartate beta-semialdehyde dehydrogenase family: the first structure of a fungal ortholog.\",\"volume\":\"66\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HSK\",\"source\":\"PDB\"}],\"referenceNumber\":8,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH NADP(+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_CANAL              Reviewed;         365 AA.\nAC   Q5ALM0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   26-APR-2005, sequence version 1.\nDT   18-JUN-2025, entry version 145.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};\nDE   AltName: Full=CaASADH {ECO:0000303|PubMed:17419877};\nGN   Name=HOM2 {ECO:0000303|PubMed:17419877};\nGN   OrderedLocusNames=CAALFM_C202370CA {ECO:0000312|EMBL:AOW27277.1},\nGN   orf19.9132 {ECO:0000312|CGD:CAL0000179646};\nOS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.\nOX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000312|Proteomes:UP000000559}\nRP   GENOME REANNOTATION.\nRC   STRAIN=SC5314 / ATCC MYA-2876 {ECO:0000312|Proteomes:UP000000559};\nRX   PubMed=17419877; DOI=10.1186/gb-2007-8-4-r52;\nRA   van het Hoog M., Rast T.J., Martchenko M., Grindle S., Dignard D.,\nRA   Hogues H., Cuomo C., Berriman M., Scherer S., Magee B.B., Whiteway M.,\nRA   Chibana H., Nantel A., Magee P.T.;\nRT   \"Assembly of the Candida albicans genome into sixteen supercontigs aligned\nRT   on the eight chromosomes.\";\nRL   Genome Biol. 8:RESEARCH52.1-RESEARCH52.12(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H4",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=32383780; DOI=10.1002/ddr.21682;\nRA   Dahal G.P., Launder D., McKeone K.M.M., Hunter J.P., Conti H.R.,\nRA   Viola R.E.;\nRT   \"Aspartate semialdehyde dehydrogenase inhibition suppresses the growth of\nRT   the pathogenic fungus Candida albicans.\";\nRL   Drug Dev. Res. 81:736-744(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H5",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=34469014; DOI=10.1002/ddr.21875;\nRA   Friday S.N., Cheng D.W., Zagler S.G., Zanella B.S., Dietz J.D.,\nRA   Calbat C.N., Roach L.T., Bagnal C., Faile I.S., Halkides C.J., Viola R.E.;\nRT   \"Design and testing of selective inactivators against an antifungal enzyme\nRT   target.\";\nRL   Drug Dev. Res. 83:447-460(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H6",
  "excerpt": "RN   [8] {ECO:0007744|PDB:3HSK}\nRP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH NADP(+), FUNCTION,\nRP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=20124701; DOI=10.1107/s0907444909052834;\nRA   Arachea B.T., Liu X., Pavlovsky A.G., Viola R.E.;\nRT   \"Expansion of the aspartate beta-semialdehyde dehydrogenase family: the\nRT   first structure of a fungal ortholog.\";\nRL   Acta Crystallogr. D 66:205-212(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H7",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate 4-\nCC       semialdehyde (L-ASA) by the reductive dephosphorylation of 4-phospho-L-\nCC       aspartate (PubMed:20124701, PubMed:29608391, PubMed:32383780,\nCC       PubMed:34469014). Mediates the second step in the biosynthesis of amino\nCC       acids that derive from aspartate (the aspartate family of amino acids),\nCC       including methioinine and threonine, the latter of which is a precursor\nCC       to isoleucine (PubMed:20124701). {ECO:0000269|PubMed:20124701,\nCC       ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:32383780,\nCC       ECO:0000269|PubMed:34469014}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H8",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; L-homoserine from L-aspartate: step 2/3.\nCC       {ECO:0000269|PubMed:20124701}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H9",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:20124701}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0009090; P:homoserine biosynthetic process; IEA:EnsemblFungi.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-160",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H11",
  "excerpt": "DR   GO; GO:0009089; P:lysine biosynthetic process via diaminopimelate; IEA:UniProtKB-UniPathway.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 161-161",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H12",
  "excerpt": "DR   GO; GO:0009086; P:methionine biosynthetic process; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H13",
  "excerpt": "DR   GO; GO:0009088; P:threonine biosynthetic process; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-163",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006783\nname: heme biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of heme, any compound of iron complexed in a porphyrin (tetrapyrrole) ring, from less complex precursors.\" [GOC:jl, PMID:11788607]\nsynonym: \"haem biosynthesis\" EXACT []\nsynonym: \"haem biosynthetic process\" EXACT []\nsynonym: \"heme anabolism\" EXACT []\nsynonym: \"heme biosynthesis\" EXACT []\nsynonym: \"heme formation\" EXACT []\nsynonym: \"heme synthesis\" EXACT []\nxref: Reactome:R-HSA-189451 \"Heme biosynthesis\"\nis_a: GO:0006779 ! porphyrin-containing compound biosynthetic process\nis_a: GO:0042168 ! heme metabolic process\nis_a: GO:0046148 ! pigment biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006783",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 70266-70281",
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
  "excerpt": "[Term]\nid: GO:0019896\nname: axonal transport of mitochondrion\nnamespace: biological_process\ndef: \"The directed movement of mitochondria along microtubules in nerve cell axons.\" [GOC:ai]\nsubset: goslim_synapse\nsynonym: \"axon transport of mitochondria\" EXACT []\nis_a: GO:0047497 ! mitochondrion transport along microtubule\nis_a: GO:0098930 ! axonal transport\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019896",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 154351-154360",
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
  "excerpt": "[Term]\nid: GO:0031648\nname: protein destabilization\nnamespace: biological_process\ndef: \"Any process that decreases the stability of a protein, making it more vulnerable to degradative processes or aggregation.\" [GOC:mah]\nsynonym: \"negative regulation of protein stability\" EXACT []\nsynonym: \"protein destabilisation\" EXACT [GOC:ah]\nis_a: GO:0031647 ! regulation of protein stability\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031648",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 178651-178659",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 154. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
