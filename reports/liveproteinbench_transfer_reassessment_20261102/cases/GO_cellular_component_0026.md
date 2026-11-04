# GO_cellular_component_0026

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0026.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — cytosol

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPAATAAASSGKGSFDLATLFVADKAARDEAGLALADAVKKSGVEFFTQIGFNDAIVKALNDKKSQSAREGACEVISTLCENGAAQLLEPHVISSAENTPFPALLEAFADKVAAVKTAAIAAVKAIVQSMNPWASFVLLPALLNLIRTSGKWQIKAGSLEILQQLITSAPFQMGEAMPDLVPVLAEAVWDTKSDVKKAAKATLEKAVSLVENKDIEKFVPALVKSLLNPIEEVPKTISLLSATTFVSEVTAPTISLIAPLLIRGLDERPTATKRKVCVIADNMSKLVDSEYTVRPFLPQLLPRLIKTSETIADPEARSVANRAIVTLRRIGKVPAESDGSDLPPLPVAEGPHLATNFVALVKKHGGVSVEQTNPGLAYAGVLAASLVNHHNFDQKTWESTLPPYLKLALPSYDSLPAVRELLQKKADEAETDDAKFPDEEEGEDLCNIEQFNLAYGAKILLHHANMRLKRGHRYGLCGRNGSGKSTLMNAIINNQVEGFPPPTEVRTFYVQHDIDGSEAEISILDWVLGDKRLLATPDEIKSTLESVGFDEVKQKNSIGSLSGGWKMKLALARAILFKADILLLDEPTNHLDVLNVDWLINYLTSLTRCTSIIVSHDSDFLNRTVTDVLHLNNFKLKRYPGNLEDFVQHVPEAKSYYQLDVAEDYQFKLPNPPLLDGVKTKEKSLLKMRNVSFQYPGSSIQQLYDISLQVSLSSRVAILGPNGSGKSTLVKLLTGETEPNLGGQVWKHPNLVIGYVAQHAFHHIDNHLDSTPLEYMLWRYQTGEDLEEMHKANRVMTEAEIAKMKEGATVIKDGVKRIIDELVARKKLKQSYEYEVSFKGMSSAENIWISRDELVARGFEKKVMELDTREAQRLGLMRPLVRREIEKHFEDFGLDAEFVSHNSMRGLSGGQKVKVVLGAATWRRPHIICLDEPTNYLDRESLAALIAALKNFEGGVLIITHNREFSESICTEVWAMREGYLEASGHNWVEGQGSGERIDKKAADDDEVEYDALGNPIVKAKKEKKLSAADKRKAKKDRMARRKRGEEVFSDEEL

[Multiple Choices]
A. chromosome, centromeric region
B. host cell mitochondrion
C. cytosol
D. recycling endosome membrane
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

> The sequence-matched UniProt record annotates cytosol, with the subcellular-location annotation transferred by similarity (ECO:0000250); the GO cytosol annotation is IEA. These support choice C, though they are not direct experimental localization evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence contains repeated P-loop NTPase/ABC-type ATPase motifs and is consistent with the soluble eukaryotic translation elongation factor 3 family. Family-level knowledge that eEF3 functions in cytosolic translation favors C. The sequence also lacks an evident transmembrane segment or a convincing N-terminal mitochondrial targeting presequence, making the endosome membrane and mitochondrion options poor fits; a centromeric component is likewise not suggested by the sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and protein-family features provide a meaningful basis for choosing cytosol among these alternatives without relying on the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives are sufficiently distinct, and the soluble translation-factor inference favors cytosol.


### Important caveats

- The supplied source annotations support the key but include similarity-based and electronic inference; they do not establish direct experimental localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence contains repeated P-loop NTPase/ABC-type ATPase motifs and is consistent with the soluble eukaryotic translation elongation factor 3 family. Family-level knowledge that eEF3 functions in cytosolic translation favors C. The sequence also lacks an evident transmembrane segment or a convincing N-terminal mitochondrial targeting presequence, making the endosome membrane and mitochondrion options poor fits; a centromeric component is likewise not suggested by the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and protein-family features provide a meaningful basis for choosing cytosol among these alternatives without relying on the exact protein's recorded annotation."
  },
  "case_id": "GO_cellular_component_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates cytosol, with the subcellular-location annotation transferred by similarity (ECO:0000250); the GO cytosol annotation is IEA. These support choice C, though they are not direct experimental localization evidence."
  },
  "important_caveats": [
    "The supplied source annotations support the key but include similarity-based and electronic inference; they do not establish direct experimental localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives are sufficiently distinct, and the soluble translation-factor inference favors cytosol."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates cytosol, with the subcellular-location annotation transferred by similarity (ECO:0000250); the GO cytosol annotation is IEA. These support choice C, though they are not direct experimental localization evidence.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence contains repeated P-loop NTPase/ABC-type ATPase motifs and is consistent with the soluble eukaryotic translation elongation factor 3 family. Family-level knowledge that eEF3 functions in cytosolic translation favors C. The sequence also lacks an evident transmembrane segment or a convincing N-terminal mitochondrial targeting presequence, making the endosome membrane and mitochondrion options poor fits; a centromeric component is likewise not suggested by the sequence.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and protein-family features provide a meaningful basis for choosing cytosol among these alternatives without relying on the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives are sufficiently distinct, and the soluble translation-factor inference favors cytosol."
  },
  "important_caveats": [
    "The supplied source annotations support the key but include similarity-based and electronic inference; they do not establish direct experimental localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry J9VQZ9 annotates this protein (Elongation Factor 3 from Cryptococcus neoformans) as 'Cytoplasm, cytosol' with evidence code ECO:0000250 (inferred from similarity to yeast eEF3, P16521). The GO cross-reference assigns GO:0005829 (cytosol) via IEA:UniProtKB-SubCell. The annotation is computational/similarity-based rather than directly experimental for this exact protein, but it is consistent with the well-established cytoplasmic localization of eEF3 in fungi. The sequence matches the benchmark input exactly.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple ABC-transporter-like domains (Walker A motifs: GSGKST appearing three times; Walker B motifs: DEPTNH/DEPTNY) arranged in the characteristic tandem architecture of eukaryotic elongation factor 3 (eEF3), a fungal-specific translation factor. Transferable knowledge from studying EF-Tu, EF-G, EF-1, EF-2, and eEF3 across many organisms establishes that all translation elongation factors function in the cytoplasm/cytosol as part of the ribosomal translation machinery. The ABC domains in eEF3 are used for ATP-driven conformational changes during translation, not for membrane transport. The sequence lacks: (1) an N-terminal mitochondrial targeting presequence (no amphipathic arginine-rich helix), ruling out option B; (2) transmembrane domains or endosomal targeting signals, ruling out option D; (3) DNA-binding or centromere-associated domains, ruling out option A. The 'host cell mitochondrion' qualifier in option B specifically refers to pathogen effector proteins translocated into host mitochondria during infection—eEF3 is an intracellular fungal translation factor, not a secreted effector. The absence of any compartment-targeting signal combined with the universal cytoplasmic localization of elongation factors across all studied species provides a strong family-level inference favoring cytosol.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the eEF3/ABC-domain architecture and the universal cytoplasmic localization of translation elongation factors (learned from EF-Tu, EF-G, EF-1, EF-2, eEF3 in yeast, Candida, and other fungi) provides a concrete, transferable argument that distinguishes cytosol from the other three options. The absence of targeting signals for mitochondria, endosomes, or chromatin further eliminates distractors. No fact specific to this exact protein beyond its sequence is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent clearly distinct cellular compartments. A translation elongation factor with no targeting signals, no transmembrane domains, and no DNA-binding motifs can only be cytosolic. The 'host cell mitochondrion' option is a plausible distractor for a pathogen protein but is eliminated by the protein's identity as an intracellular translation factor. No two options are defensible for this protein.


### Important caveats

- The UniProt subcellular localization annotation is based on similarity (ECO:0000250) to yeast eEF3 (P16521), not on direct experimental localization of the Cryptococcus protein itself.
- The GO annotation uses IEA (Inferred from Electronic Annotation) evidence, which is computationally derived.
- The N-terminal region (MAPAATAAASSGKGSFDLATLFVADKAARDEAGLALADAVKKSGVEFFTQ...) contains some small polar residues that could superficially resemble a weak targeting extension, but it lacks the hallmark arginine-rich amphipathic helix of a mitochondrial presequence.
- The protein is from Cryptococcus neoformans, a pathogenic fungus; the 'host cell mitochondrion' distractor exploits the pathogen context but is eliminated by the protein's well-characterized role as a cytoplasmic translation factor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple ABC-transporter-like domains (Walker A motifs: GSGKST appearing three times; Walker B motifs: DEPTNH/DEPTNY) arranged in the characteristic tandem architecture of eukaryotic elongation factor 3 (eEF3), a fungal-specific translation factor. Transferable knowledge from studying EF-Tu, EF-G, EF-1, EF-2, and eEF3 across many organisms establishes that all translation elongation factors function in the cytoplasm/cytosol as part of the ribosomal translation machinery. The ABC domains in eEF3 are used for ATP-driven conformational changes during translation, not for membrane transport. The sequence lacks: (1) an N-terminal mitochondrial targeting presequence (no amphipathic arginine-rich helix), ruling out option B; (2) transmembrane domains or endosomal targeting signals, ruling out option D; (3) DNA-binding or centromere-associated domains, ruling out option A. The 'host cell mitochondrion' qualifier in option B specifically refers to pathogen effector proteins translocated into host mitochondria during infection—eEF3 is an intracellular fungal translation factor, not a secreted effector. The absence of any compartment-targeting signal combined with the universal cytoplasmic localization of elongation factors across all studied species provides a strong family-level inference favoring cytosol.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the eEF3/ABC-domain architecture and the universal cytoplasmic localization of translation elongation factors (learned from EF-Tu, EF-G, EF-1, EF-2, eEF3 in yeast, Candida, and other fungi) provides a concrete, transferable argument that distinguishes cytosol from the other three options. The absence of targeting signals for mitochondria, endosomes, or chromatin further eliminates distractors. No fact specific to this exact protein beyond its sequence is needed."
  },
  "case_id": "GO_cellular_component_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry J9VQZ9 annotates this protein (Elongation Factor 3 from Cryptococcus neoformans) as 'Cytoplasm, cytosol' with evidence code ECO:0000250 (inferred from similarity to yeast eEF3, P16521). The GO cross-reference assigns GO:0005829 (cytosol) via IEA:UniProtKB-SubCell. The annotation is computational/similarity-based rather than directly experimental for this exact protein, but it is consistent with the well-established cytoplasmic localization of eEF3 in fungi. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The UniProt subcellular localization annotation is based on similarity (ECO:0000250) to yeast eEF3 (P16521), not on direct experimental localization of the Cryptococcus protein itself.",
    "The GO annotation uses IEA (Inferred from Electronic Annotation) evidence, which is computationally derived.",
    "The N-terminal region (MAPAATAAASSGKGSFDLATLFVADKAARDEAGLALADAVKKSGVEFFTQ...) contains some small polar residues that could superficially resemble a weak targeting extension, but it lacks the hallmark arginine-rich amphipathic helix of a mitochondrial presequence.",
    "The protein is from Cryptococcus neoformans, a pathogenic fungus; the 'host cell mitochondrion' distractor exploits the pathogen context but is eliminated by the protein's well-characterized role as a cytoplasmic translation factor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct cellular compartments. A translation elongation factor with no targeting signals, no transmembrane domains, and no DNA-binding motifs can only be cytosolic. The 'host cell mitochondrion' option is a plausible distractor for a pathogen protein but is eliminated by the protein's identity as an intracellular translation factor. No two options are defensible for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry J9VQZ9 annotates this protein (Elongation Factor 3 from Cryptococcus neoformans) as 'Cytoplasm, cytosol' with evidence code ECO:0000250 (inferred from similarity to yeast eEF3, P16521). The GO cross-reference assigns GO:0005829 (cytosol) via IEA:UniProtKB-SubCell. The annotation is computational/similarity-based rather than directly experimental for this exact protein, but it is consistent with the well-established cytoplasmic localization of eEF3 in fungi. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple ABC-transporter-like domains (Walker A motifs: GSGKST appearing three times; Walker B motifs: DEPTNH/DEPTNY) arranged in the characteristic tandem architecture of eukaryotic elongation factor 3 (eEF3), a fungal-specific translation factor. Transferable knowledge from studying EF-Tu, EF-G, EF-1, EF-2, and eEF3 across many organisms establishes that all translation elongation factors function in the cytoplasm/cytosol as part of the ribosomal translation machinery. The ABC domains in eEF3 are used for ATP-driven conformational changes during translation, not for membrane transport. The sequence lacks: (1) an N-terminal mitochondrial targeting presequence (no amphipathic arginine-rich helix), ruling out option B; (2) transmembrane domains or endosomal targeting signals, ruling out option D; (3) DNA-binding or centromere-associated domains, ruling out option A. The 'host cell mitochondrion' qualifier in option B specifically refers to pathogen effector proteins translocated into host mitochondria during infection—eEF3 is an intracellular fungal translation factor, not a secreted effector. The absence of any compartment-targeting signal combined with the universal cytoplasmic localization of elongation factors across all studied species provides a strong family-level inference favoring cytosol.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the eEF3/ABC-domain architecture and the universal cytoplasmic localization of translation elongation factors (learned from EF-Tu, EF-G, EF-1, EF-2, eEF3 in yeast, Candida, and other fungi) provides a concrete, transferable argument that distinguishes cytosol from the other three options. The absence of targeting signals for mitochondria, endosomes, or chromatin further eliminates distractors. No fact specific to this exact protein beyond its sequence is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct cellular compartments. A translation elongation factor with no targeting signals, no transmembrane domains, and no DNA-binding motifs can only be cytosolic. The 'host cell mitochondrion' option is a plausible distractor for a pathogen protein but is eliminated by the protein's identity as an intracellular translation factor. No two options are defensible for this protein."
  },
  "important_caveats": [
    "The UniProt subcellular localization annotation is based on similarity (ECO:0000250) to yeast eEF3 (P16521), not on direct experimental localization of the Cryptococcus protein itself.",
    "The GO annotation uses IEA (Inferred from Electronic Annotation) evidence, which is computationally derived.",
    "The N-terminal region (MAPAATAAASSGKGSFDLATLFVADKAARDEAGLALADAVKKSGVEFFTQ...) contains some small polar residues that could superficially resemble a weak targeting extension, but it lacks the hallmark arginine-rich amphipathic helix of a mitochondrial presequence.",
    "The protein is from Cryptococcus neoformans, a pathogenic fungus; the 'host cell mitochondrion' distractor exploits the pathogen context but is eliminated by the protein's well-characterized role as a cytoplasmic translation factor."
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
  "benchmark_sequence_length": 1055,
  "benchmark_sequence_sha256": "6ac3a0db14920eb77abf52193ecd849165175b8df860637dda883591fdc7e600",
  "current_entry_audit": {
    "entryVersion": 68,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-11-13",
    "sequenceVersion": 2
  },
  "current_record_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1055,
  "current_source_sequence_sha256": "6ac3a0db14920eb77abf52193ecd849165175b8df860637dda883591fdc7e600",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 66,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VQZ9",
  "selected_historical_entry_version": 66,
  "selected_historical_record_sha256": "a7573f1eb27ed3976b103711b49783a1b1b870f6216c255c67bfd6b86729ee7d",
  "selected_historical_source_sequence_length": 1055,
  "selected_historical_source_sequence_sha256": "6ac3a0db14920eb77abf52193ecd849165175b8df860637dda883591fdc7e600",
  "selected_historical_version": {
    "accession": "J9VQZ9",
    "database": "Swiss-Prot",
    "entryVersion": 66,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EF3_CRYN9",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VQZ9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":68,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-11-13\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFR95029.2\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Eukaryotic elongation factor 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"eEF3\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5KIM6\",\"source\":\"UniProtKB\"}],\"value\":\"3.6.4.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Elongation factor 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"EF-3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P16521\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0091\",\"value\":\"Cytoplasm, cytosol\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005829\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosol\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H1",
  "excerpt": "ID   EF3_CRYN9               Reviewed;        1055 AA.\nAC   J9VQZ9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-NOV-2013, sequence version 2.\nDT   28-JAN-2026, entry version 66.\nDE   RecName: Full=Elongation factor 3 {ECO:0000305};\nDE            Short=EF-3 {ECO:0000305};\nDE            EC=3.6.4.- {ECO:0000250|UniProtKB:Q5KIM6};\nDE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};\nDE            Short=eEF3 {ECO:0000305};\nGN   Name=TEF3 {ECO:0000305}; ORFNames=CNAG_01117 {ECO:0000312|EMBL:AFR95029.2};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|EMBL:AFR95029.2, ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.511490+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a7573f1eb27ed3976b103711b49783a1b1b870f6216c255c67bfd6b86729ee7d",
  "url": "https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H2",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cytoplasm, cytosol\nCC       {ECO:0000250|UniProtKB:P16521}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.511490+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a7573f1eb27ed3976b103711b49783a1b1b870f6216c255c67bfd6b86729ee7d",
  "url": "https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0005829; C:cytosol; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.511490+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a7573f1eb27ed3976b103711b49783a1b1b870f6216c255c67bfd6b86729ee7d",
  "url": "https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000775\nname: chromosome, centromeric region\nnamespace: cellular_component\nalt_id: GO:0097521\ndef: \"The region of a chromosome that includes the centromeric DNA and associated proteins. In monocentric chromosomes, this region corresponds to a single area of the chromosome, whereas in holocentric chromosomes, it is evenly distributed along the chromosome.\" [GOC:cjm, GOC:elh, GOC:kmv, GOC:pr]\ncomment: Note that this term can be used in place of the obsolete cellular component term 'centromere ; GO:0005698'.\nsynonym: \"centromere\" RELATED []\nsynonym: \"centromere complex\" EXACT []\nsynonym: \"chromosome, centric region\" EXACT []\nsynonym: \"chromosome, pericentric region\" RELATED []\nxref: SO:0000577\nis_a: GO:0098687 ! chromosomal region\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000775",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 5824-5837",
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
  "excerpt": "[Term]\nid: GO:0005829\nname: cytosol\nnamespace: cellular_component\ndef: \"The part of the cytoplasm that does not contain organelles but which does contain other particulate matter, such as protein complexes.\" [GOC:hjd, GOC:jl]\nsubset: goslim_agr\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_plant\nxref: NIF_Subcellular:sao101633890\nxref: Wikipedia:Cytosol\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005829",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59936-59953",
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
  "excerpt": "[Term]\nid: GO:0033650\nname: host cell mitochondrion\nnamespace: cellular_component\ndef: \"A semiautonomous, self replicating organelle as found in host cells that occurs in varying numbers, shapes, and sizes in the cell cytoplasm. The host is defined as the larger of the organisms involved in a symbiotic interaction.\" [GOC:pamgo_curators]\nsynonym: \"host mitochondria\" EXACT []\nis_a: GO:0033648 ! host intracellular membrane-bounded organelle\nis_a: GO:0033655 ! host cell cytoplasm part\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0033650",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 199319-199327",
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
  "excerpt": "[Term]\nid: GO:0055038\nname: recycling endosome membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding a recycling endosome.\" [GOC:jid, GOC:rph, PMID:10930469, PMID:15601896, PMID:16246101]\nis_a: GO:0010008 ! endosome membrane\nrelationship: part_of GO:0055037 ! recycling endosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0055038",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 342824-342831",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
