# GO_cellular_component_0091

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0091.txt)

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
MAVMKFTWRSIIPRCSKGIEEAEAEAEAETKKQDSKQGSFSRLAMIDFSYPSSMFTEDLSTSLAGSNLYVFTLEELKVITQCFSSANFLGEGGFGPVHKGFIDDNLRPGLEAQPVAVKLLDLEGLQGHREWLTEVVFLAQLSHPHLVKLIGYCCEDENRLLVYEYMPRGSLENQLFAKYSVPLPWSTRMKIALGAAKGLAYLHEAEKPVIYRDFKASNILLDSDYSAKLSDFGLAKDGPEGDKTHVSTRVMGTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRSLDKSRSPREQNLAEWARPMLNESRRLARIMDPKLEGQYSETGARKAAALAYQCLSHRAKQRPKMSDVVNILEPLLDYGETSVASFVYTVPTHQKGGSPPKDDTDTKECEAKTELKKENGHHRNRHHHRRSHKSRDGHRHQNKSSSQSSVHSENDTSKQNLENGSNEECNID

[Multiple Choices]
A. inner membrane pellicle complex
B. plasma membrane
C. RQC complex
D. mitochondrial outer membrane
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

> The sequence-matched UniProt record assigns cell membrane localization by transfer from another protein and includes a plasma-membrane GO annotation with ISS evidence. The historical record also contains these annotations. This supports B as an annotation, but is not direct experimental localization evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable protein kinase catalytic domain but no long hydrophobic transmembrane segment or obvious mitochondrial targeting peptide. A soluble plant signaling kinase can associate with the plasma membrane through interactions or membrane-targeting features; that family-level pattern favors plasma membrane over mitochondrial outer membrane. The pellicle-complex option is specific to apicomplexan parasites, and RQC is a ribosome-quality-control complex, neither a natural fit for this sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable kinase and cellular-localization patterns give a meaningful, probabilistic basis for B among these choices. The sequence alone does not prove membrane localization, but exact-protein database recall is not necessary to distinguish the options plausibly.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence does not establish localization conclusively, but the offered alternatives and the signaling-kinase pattern favor plasma membrane; no alternative is comparably supported.


### Important caveats

- The supplied localization annotations are computational or transferred rather than direct experimental evidence for this exact protein.
- The kinase domain itself does not establish plasma-membrane localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable protein kinase catalytic domain but no long hydrophobic transmembrane segment or obvious mitochondrial targeting peptide. A soluble plant signaling kinase can associate with the plasma membrane through interactions or membrane-targeting features; that family-level pattern favors plasma membrane over mitochondrial outer membrane. The pellicle-complex option is specific to apicomplexan parasites, and RQC is a ribosome-quality-control complex, neither a natural fit for this sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase and cellular-localization patterns give a meaningful, probabilistic basis for B among these choices. The sequence alone does not prove membrane localization, but exact-protein database recall is not necessary to distinguish the options plausibly."
  },
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns cell membrane localization by transfer from another protein and includes a plasma-membrane GO annotation with ISS evidence. The historical record also contains these annotations. This supports B as an annotation, but is not direct experimental localization evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied localization annotations are computational or transferred rather than direct experimental evidence for this exact protein.",
    "The kinase domain itself does not establish plasma-membrane localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not establish localization conclusively, but the offered alternatives and the signaling-kinase pattern favor plasma membrane; no alternative is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns cell membrane localization by transfer from another protein and includes a plasma-membrane GO annotation with ISS evidence. The historical record also contains these annotations. This supports B as an annotation, but is not direct experimental localization evidence for this exact protein.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable protein kinase catalytic domain but no long hydrophobic transmembrane segment or obvious mitochondrial targeting peptide. A soluble plant signaling kinase can associate with the plasma membrane through interactions or membrane-targeting features; that family-level pattern favors plasma membrane over mitochondrial outer membrane. The pellicle-complex option is specific to apicomplexan parasites, and RQC is a ribosome-quality-control complex, neither a natural fit for this sequence.",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase and cellular-localization patterns give a meaningful, probabilistic basis for B among these choices. The sequence alone does not prove membrane localization, but exact-protein database recall is not necessary to distinguish the options plausibly."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not establish localization conclusively, but the offered alternatives and the signaling-kinase pattern favor plasma membrane; no alternative is comparably supported."
  },
  "important_caveats": [
    "The supplied localization annotations are computational or transferred rather than direct experimental evidence for this exact protein.",
    "The kinase domain itself does not establish plasma-membrane localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A5J5NT52) annotates the subcellular location as 'Cell membrane' (SL-0039) with evidence code ECO:0000250 (Inferred by Similarity to Q9ZUF4), and the GO cross-reference lists GO:0005886 (plasma membrane) with IEA:UniProtKB-SubCell. The evidence is computational/inference-based (ISS/IEA) rather than direct experimental measurement for this specific protein, but it does support the expected answer B (plasma membrane). The protein is an EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase, consistent with plasma membrane association in plant immune signaling.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an unambiguous Ser/Thr kinase domain (GxGxxG glycine-rich loop 'GGFGPVHKGF', DFG motif 'DFGLAKDG', activation segment, APE motif 'GTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRS'), which eliminates the RQC complex (a ribosome-associated quality-control assembly, not a kinase). The sequence lacks apicomplexan-specific features and the protein's overall composition is consistent with a plant/eukaryotic kinase, eliminating the inner membrane pellicle complex (a structure unique to apicomplexan parasites). The N-terminus lacks a canonical mitochondrial targeting signal (no amphipathic helix with clustered Arg/Lys and hydroxylated residues typical of MTS), making mitochondrial outer membrane unlikely. Critically, the protein belongs to the receptor-like cytoplasmic kinase (RLCK) family in plants: the N-terminal region contains potential N-acylation sites (Ala2 after Met cleavage, Cys residues around positions 16-17 in 'PRCSKGIEEAEAEAEAETKKQ') consistent with myristoylation/palmitoylation that anchors RLCKs (e.g., BIK1, PBS1 in Arabidopsis) to the plasma membrane. Plant RLCKs are well-characterized as plasma membrane-associated kinases in PAMP-triggered immunity, providing strong family-level transferable knowledge that distinguishes plasma membrane from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can identify the kinase domain to eliminate the RQC complex, recognize the absence of an apicomplexan context to eliminate the pellicle complex, note the absence of a mitochondrial targeting signal to disfavour mitochondrial outer membrane, and apply well-established RLCK family biology (N-terminal acylation, plasma membrane association in plant immunity) to select plasma membrane. This is a multi-step inference using conserved sequence motifs, family-level knowledge, and structural principles learned from other plant RLCKs, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated: the pellicle complex is apicomplexan-specific, the RQC complex is a ribosomal quality-control assembly incompatible with a kinase domain, and the mitochondrial outer membrane lacks supporting sequence features. The plasma membrane is the only option consistent with the RLCK family biology, N-terminal acylation potential, and absence of organellar targeting signals.


### Important caveats

- The UniProt annotation for this protein's localization is ISS (inferred by similarity to Q9ZUF4) and IEA, not direct experimental evidence for this specific protein.
- The N-terminal Ala2 is a non-canonical myristoylation site (Gly is typical); membrane association may also be mediated by palmitoylation at internal Cys residues or protein-protein interaction with receptor kinases.
- The model is not given the protein name, organism, or family label; it must infer the RLCK family context from sequence features alone.
- The reviewer-only evidence confirms sequence match to UniProt A0A5J5NT52, but this accession and organism identity were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an unambiguous Ser/Thr kinase domain (GxGxxG glycine-rich loop 'GGFGPVHKGF', DFG motif 'DFGLAKDG', activation segment, APE motif 'GTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRS'), which eliminates the RQC complex (a ribosome-associated quality-control assembly, not a kinase). The sequence lacks apicomplexan-specific features and the protein's overall composition is consistent with a plant/eukaryotic kinase, eliminating the inner membrane pellicle complex (a structure unique to apicomplexan parasites). The N-terminus lacks a canonical mitochondrial targeting signal (no amphipathic helix with clustered Arg/Lys and hydroxylated residues typical of MTS), making mitochondrial outer membrane unlikely. Critically, the protein belongs to the receptor-like cytoplasmic kinase (RLCK) family in plants: the N-terminal region contains potential N-acylation sites (Ala2 after Met cleavage, Cys residues around positions 16-17 in 'PRCSKGIEEAEAEAEAETKKQ') consistent with myristoylation/palmitoylation that anchors RLCKs (e.g., BIK1, PBS1 in Arabidopsis) to the plasma membrane. Plant RLCKs are well-characterized as plasma membrane-associated kinases in PAMP-triggered immunity, providing strong family-level transferable knowledge that distinguishes plasma membrane from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the kinase domain to eliminate the RQC complex, recognize the absence of an apicomplexan context to eliminate the pellicle complex, note the absence of a mitochondrial targeting signal to disfavour mitochondrial outer membrane, and apply well-established RLCK family biology (N-terminal acylation, plasma membrane association in plant immunity) to select plasma membrane. This is a multi-step inference using conserved sequence motifs, family-level knowledge, and structural principles learned from other plant RLCKs, not a lookup of this protein's specific annotation."
  },
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A5J5NT52) annotates the subcellular location as 'Cell membrane' (SL-0039) with evidence code ECO:0000250 (Inferred by Similarity to Q9ZUF4), and the GO cross-reference lists GO:0005886 (plasma membrane) with IEA:UniProtKB-SubCell. The evidence is computational/inference-based (ISS/IEA) rather than direct experimental measurement for this specific protein, but it does support the expected answer B (plasma membrane). The protein is an EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase, consistent with plasma membrane association in plant immune signaling."
  },
  "important_caveats": [
    "The UniProt annotation for this protein's localization is ISS (inferred by similarity to Q9ZUF4) and IEA, not direct experimental evidence for this specific protein.",
    "The N-terminal Ala2 is a non-canonical myristoylation site (Gly is typical); membrane association may also be mediated by palmitoylation at internal Cys residues or protein-protein interaction with receptor kinases.",
    "The model is not given the protein name, organism, or family label; it must infer the RLCK family context from sequence features alone.",
    "The reviewer-only evidence confirms sequence match to UniProt A0A5J5NT52, but this accession and organism identity were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: the pellicle complex is apicomplexan-specific, the RQC complex is a ribosomal quality-control assembly incompatible with a kinase domain, and the mitochondrial outer membrane lacks supporting sequence features. The plasma membrane is the only option consistent with the RLCK family biology, N-terminal acylation potential, and absence of organellar targeting signals."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A5J5NT52) annotates the subcellular location as 'Cell membrane' (SL-0039) with evidence code ECO:0000250 (Inferred by Similarity to Q9ZUF4), and the GO cross-reference lists GO:0005886 (plasma membrane) with IEA:UniProtKB-SubCell. The evidence is computational/inference-based (ISS/IEA) rather than direct experimental measurement for this specific protein, but it does support the expected answer B (plasma membrane). The protein is an EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase, consistent with plasma membrane association in plant immune signaling.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an unambiguous Ser/Thr kinase domain (GxGxxG glycine-rich loop 'GGFGPVHKGF', DFG motif 'DFGLAKDG', activation segment, APE motif 'GTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRS'), which eliminates the RQC complex (a ribosome-associated quality-control assembly, not a kinase). The sequence lacks apicomplexan-specific features and the protein's overall composition is consistent with a plant/eukaryotic kinase, eliminating the inner membrane pellicle complex (a structure unique to apicomplexan parasites). The N-terminus lacks a canonical mitochondrial targeting signal (no amphipathic helix with clustered Arg/Lys and hydroxylated residues typical of MTS), making mitochondrial outer membrane unlikely. Critically, the protein belongs to the receptor-like cytoplasmic kinase (RLCK) family in plants: the N-terminal region contains potential N-acylation sites (Ala2 after Met cleavage, Cys residues around positions 16-17 in 'PRCSKGIEEAEAEAEAETKKQ') consistent with myristoylation/palmitoylation that anchors RLCKs (e.g., BIK1, PBS1 in Arabidopsis) to the plasma membrane. Plant RLCKs are well-characterized as plasma membrane-associated kinases in PAMP-triggered immunity, providing strong family-level transferable knowledge that distinguishes plasma membrane from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the kinase domain to eliminate the RQC complex, recognize the absence of an apicomplexan context to eliminate the pellicle complex, note the absence of a mitochondrial targeting signal to disfavour mitochondrial outer membrane, and apply well-established RLCK family biology (N-terminal acylation, plasma membrane association in plant immunity) to select plasma membrane. This is a multi-step inference using conserved sequence motifs, family-level knowledge, and structural principles learned from other plant RLCKs, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: the pellicle complex is apicomplexan-specific, the RQC complex is a ribosomal quality-control assembly incompatible with a kinase domain, and the mitochondrial outer membrane lacks supporting sequence features. The plasma membrane is the only option consistent with the RLCK family biology, N-terminal acylation potential, and absence of organellar targeting signals."
  },
  "important_caveats": [
    "The UniProt annotation for this protein's localization is ISS (inferred by similarity to Q9ZUF4) and IEA, not direct experimental evidence for this specific protein.",
    "The N-terminal Ala2 is a non-canonical myristoylation site (Gly is typical); membrane association may also be mediated by palmitoylation at internal Cys residues or protein-protein interaction with receptor kinases.",
    "The model is not given the protein name, organism, or family label; it must infer the RLCK family context from sequence features alone.",
    "The reviewer-only evidence confirms sequence match to UniProt A0A5J5NT52, but this accession and organism identity were not provided to the evaluated model."
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
  "benchmark_sequence_length": 460,
  "benchmark_sequence_sha256": "d7e15719160373fd4dde713a8a3f3afa041b4c4e33dab33f3231fec4ccd04df4",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-12-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 460,
  "current_source_sequence_sha256": "d7e15719160373fd4dde713a8a3f3afa041b4c4e33dab33f3231fec4ccd04df4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 17,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A5J5NT52",
  "selected_historical_entry_version": 17,
  "selected_historical_record_sha256": "e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a",
  "selected_historical_source_sequence_length": 460,
  "selected_historical_source_sequence_sha256": "d7e15719160373fd4dde713a8a3f3afa041b4c4e33dab33f3231fec4ccd04df4",
  "selected_historical_version": {
    "accession": "A0A5J5NT52",
    "database": "Swiss-Prot",
    "entryVersion": 17,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIR5D_GOSBA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A5J5NT52\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-12-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Sea Island cotton\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"malvids\",\"Malvales\",\"Malvaceae\",\"Malvoideae\",\"Gossypium\"],\"scientificName\":\"Gossypium barbadense\",\"synonyms\":[\"Hibiscus barbadensis\"],\"taxonId\":3634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10027\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"2.7.11.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39488762\",\"source\":\"PubMed\"}],\"value\":\"EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5D\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39488762\",\"source\":\"PubMed\"}],\"value\":\"GbEIR5D\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9ZUF4\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Sun L.\",\"Li X.\",\"Zhong J.\",\"Wang Y.\",\"Li B.\",\"Ye Z.\",\"Zhang J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39488762\"},{\"database\":\"DOI\",\"id\":\"10.1002/advs.202407787\"}],\"citationType\":\"journal article\",\"firstPage\":\"e2407787\",\"id\":\"39488762\",\"journal\":\"Adv. Sci.\",\"lastPage\":\"e2407787\",\"publicationDate\":\"2025\",\"title\":\"Recognition of a fungal effector potentiates pathogen-associated molecular pattern-triggered immunity in cotton.\",\"volume\":\"12\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Hai7124\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"INTERACTION WITH V.DAHLIAE EPD1\",\"INDUCTION BY V.DAHLIAE EPD1\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:28.363840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H1",
  "excerpt": "ID   EIR5D_GOSBA             Reviewed;         460 AA.\nAC   A0A5J5NT52;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-DEC-2019, sequence version 1.\nDT   28-JAN-2026, entry version 17.\nDE   RecName: Full=EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5D {ECO:0000303|PubMed:39488762};\nDE            Short=GbEIR5D {ECO:0000303|PubMed:39488762};\nDE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};\nGN   Name=EIR5D {ECO:0000303|PubMed:39488762};\nGN   ORFNames=ES319_D13G225100v1 {ECO:0000312|EMBL:KAB1996350.1};\nOS   Gossypium barbadense (Sea Island cotton) (Hibiscus barbadensis).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; malvids; Malvales; Malvaceae; Malvoideae; Gossypium.\nOX   NCBI_TaxID=3634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:32.436038+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a",
  "url": "https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, INTERACTION WITH V.DAHLIAE EPD1, INDUCTION\nRP   BY V.DAHLIAE EPD1, AND TISSUE SPECIFICITY.\nRC   STRAIN=cv. Hai7124;\nRX   PubMed=39488762; DOI=10.1002/advs.202407787;\nRA   Sun L., Li X., Zhong J., Wang Y., Li B., Ye Z., Zhang J.;\nRT   \"Recognition of a fungal effector potentiates pathogen-associated molecular\nRT   pattern-triggered immunity in cotton.\";\nRL   Adv. Sci. 12:e2407787-e2407787(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:32.436038+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a",
  "url": "https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:Q9ZUF4}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:32.436038+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a",
  "url": "https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:32.436038+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a",
  "url": "https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005741\nname: mitochondrial outer membrane\nnamespace: cellular_component\ndef: \"The outer, i.e. cytoplasm-facing, lipid bilayer of the mitochondrial envelope.\" [GOC:ai]\nsynonym: \"mitochondrion outer membrane\" EXACT []\nsynonym: \"outer mitochondrial membrane\" EXACT []\nsynonym: \"outer mitochondrion membrane\" EXACT []\nxref: NIF_Subcellular:sao1289741256\nxref: Wikipedia:Outer_mitochondrial_membrane\nis_a: GO:0031966 ! mitochondrial membrane\nis_a: GO:0031968 ! organelle outer membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005741",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59009-59021",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0070258\nname: inner membrane pellicle complex\nnamespace: cellular_component\ndef: \"A membrane structure formed of two closely aligned lipid bilayers that lie beneath the plasma membrane and form part of the pellicle surrounding an apicomplexan parasite cell.\" [GOC:mah, PMID:12456714]\nsynonym: \"inner membrane complex\" BROAD []\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0020039 ! pellicle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0070258",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 365849-365857",
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
  "excerpt": "[Term]\nid: GO:1990112\nname: RQC complex\nnamespace: cellular_component\ndef: \"A multiprotein complex that forms a stable complex with large ribosomal subunits (60S in eukaryotes and 50S in prokaryotes) containing stalled polypeptides and triggers their degradation (ribosomal quality control). In budding yeast, this complex includes Cdc48p, Rkr1p, Tae2p, Rqc1p, Npl4p and Ufd1p proteins.\" [GOC:rb, PMID:23178123, PMID:23232563]\nsynonym: \"ribosome quality control complex\" EXACT [PMID:23178123, PMID:23232563]\nsynonym: \"ribosome-bound quality control complex\" EXACT []\nis_a: GO:0032991 ! protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990112",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 549333-549341",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
