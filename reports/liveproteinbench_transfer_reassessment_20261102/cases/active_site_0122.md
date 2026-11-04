# active_site_0122

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0122.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 109 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMLPLLAVSAFASLGAAQTYTSCNPTNSLKTWSLSTDFTQGSSDGWTAISGNVTYGSNGAEFTINKRYDAPTLETNFYIFFGEVEVVMRAANGTGIVSSIVMESDDLDEIDWECTGTDTTQIQTNYFGKGNTTTYDRAIWETVSSPQDEFHTYKVVWTAAAITWYIDGTAVRTLEYADAVDGKNYPQTPMVVKLGIWAGGDPSNSEGTIEWAGGETDYDEVPFTMYVKSVNIINYNPAASYNYTDKTGSYTSIVASNSTTGSGIHSSNSVSVFAPSSSTSTFTSSRALIATASTYPASVQTSSSGVVSLSSSSASSSSAAASSTSGSASAVFTGAAVTNLPSFFFTVFFALAIALAF

[Multiple Choices]
A. Position 92 (Proton donor)
B. Position 109 (Nucleophile)
C. Position 975 (Proton acceptor; for dehydratase activity 1)
D. Position 151 (Proton acceptor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies residue 109 as the nucleophile. This is a homology-transferred annotation, not direct experimental validation in this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conspicuous acidic motif around positions 109–113 (EIDWE), consistent with the conserved catalytic acidic region of related carbohydrate-active enzymes. Transferable family knowledge makes a catalytic glutamate at 109 a credible nucleophile candidate; among the choices, this favors B. The 975 option is also outside the 357-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A conserved catalytic motif and the offered residue/role pair provide a meaningful family-level inference without requiring the exact protein's annotation, though sequence alone does not prove the catalytic assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported: position 975 is beyond the sequence length, and the sequence motif supports the glutamate at 109 over the other listed positions.


### Important caveats

- The source annotation is supported by similarity evidence from another protein; it is not direct experimental evidence for residue 109 in this exact protein.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conspicuous acidic motif around positions 109–113 (EIDWE), consistent with the conserved catalytic acidic region of related carbohydrate-active enzymes. Transferable family knowledge makes a catalytic glutamate at 109 a credible nucleophile candidate; among the choices, this favors B. The 975 option is also outside the 357-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A conserved catalytic motif and the offered residue/role pair provide a meaningful family-level inference without requiring the exact protein's annotation, though sequence alone does not prove the catalytic assignment."
  },
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 109 as the nucleophile. This is a homology-transferred annotation, not direct experimental validation in this protein."
  },
  "important_caveats": [
    "The source annotation is supported by similarity evidence from another protein; it is not direct experimental evidence for residue 109 in this exact protein.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported: position 975 is beyond the sequence length, and the sequence motif supports the glutamate at 109 over the other listed positions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 109 as the nucleophile. This is a homology-transferred annotation, not direct experimental validation in this protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conspicuous acidic motif around positions 109–113 (EIDWE), consistent with the conserved catalytic acidic region of related carbohydrate-active enzymes. Transferable family knowledge makes a catalytic glutamate at 109 a credible nucleophile candidate; among the choices, this favors B. The 975 option is also outside the 357-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "A conserved catalytic motif and the offered residue/role pair provide a meaningful family-level inference without requiring the exact protein's annotation, though sequence alone does not prove the catalytic assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported: position 975 is beyond the sequence length, and the sequence motif supports the glutamate at 109 over the other listed positions."
  },
  "important_caveats": [
    "The source annotation is supported by similarity evidence from another protein; it is not direct experimental evidence for residue 109 in this exact protein.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WD22 annotates position 109 as 'Active site: Nucleophile' (evidence C5/H3). The evidence code is ECO:0000250 (inferred by similarity from P27051, another chitinase), making this a transfer annotation rather than direct experimental evidence for this exact protein. However, the protein (Crh1, a GH18 chitin transglycosylase) has been functionally characterized (PubMed:30971696), and the Glu nucleophile at position 109 in the 'DDE' motif is consistent with the well-established GH18 catalytic mechanism. The annotation is present and consistent with family-level biochemistry.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can recognize this as a GH18-family chitinase/chitin transglycosylase from sequence features: the N-terminal signal peptide, the conserved 'IWW' motif (~positions 156-158), the 'DGKNYPQTP' motif (~positions 182-190), and the Ser/Thr-rich C-terminal linker. GH18 enzymes use a retaining mechanism with a Glu nucleophile in a conserved 'DGXE' or 'DDE' motif and a Glu proton donor 4 residues downstream. In this sequence, positions 107-109 form 'DDE' (D107-D108-E109) and position 113 is E (the proton donor, 4 residues after E109). This matches the canonical GH18 catalytic arrangement. Option C (position 975) is eliminated because the protein is only 357 residues long. Option A (position 92 = Asn, 'proton donor') is inconsistent because Asn is not a proton-donating catalytic residue in glycosidases. Option D (position 151 = His, 'proton acceptor') is inconsistent because GH18 does not employ a separate proton acceptor; the nucleophile Glu serves as both nucleophile and general base in the deglycosylation step. Thus, family-level knowledge of GH18 catalytic mechanism meaningfully distinguishes B from the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH18 family catalytic mechanism (Glu nucleophile + Glu proton donor in a DxE/DDE context, 4-residue spacing) is well-established transferable knowledge from hundreds of characterized GH18 chitinases. The sequence motifs (IWW, DGKNYPQTP, signal peptide, Ser-rich linker) allow family assignment. The 'DDE' at 107-109 with E113 four residues downstream matches the canonical pattern. The distractors are eliminated by basic biochemistry (Asn ≠ proton donor; His ≠ proton acceptor in GH18; position 975 > protein length).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is impossible (position exceeds protein length). Option A assigns 'proton donor' to Asn, which is not a catalytic acid in glycosidases. Option D assigns 'proton acceptor' to His, which does not participate in the GH18 retaining mechanism. Only option B is consistent with both the sequence context and the established GH18 catalytic mechanism.


### Important caveats

- The UniProt annotation for position 109 uses evidence code ECO:0000250 (similarity-based transfer from P27051), not direct experimental mutagenesis evidence for Crh1 itself. However, functional characterization of Crh1 exists (PubMed:30971696).
- The annotation was first integrated into Swiss-Prot on 2025-06-18; the benchmark author's source snapshot is unknown. The sequence and annotation are stable (sequence version 1 since 2005).
- Option C (position 975) is a trivially eliminable distractor since the protein is 357 residues, which may reduce the question's difficulty beyond what the family-knowledge reasoning alone would require.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can recognize this as a GH18-family chitinase/chitin transglycosylase from sequence features: the N-terminal signal peptide, the conserved 'IWW' motif (~positions 156-158), the 'DGKNYPQTP' motif (~positions 182-190), and the Ser/Thr-rich C-terminal linker. GH18 enzymes use a retaining mechanism with a Glu nucleophile in a conserved 'DGXE' or 'DDE' motif and a Glu proton donor 4 residues downstream. In this sequence, positions 107-109 form 'DDE' (D107-D108-E109) and position 113 is E (the proton donor, 4 residues after E109). This matches the canonical GH18 catalytic arrangement. Option C (position 975) is eliminated because the protein is only 357 residues long. Option A (position 92 = Asn, 'proton donor') is inconsistent because Asn is not a proton-donating catalytic residue in glycosidases. Option D (position 151 = His, 'proton acceptor') is inconsistent because GH18 does not employ a separate proton acceptor; the nucleophile Glu serves as both nucleophile and general base in the deglycosylation step. Thus, family-level knowledge of GH18 catalytic mechanism meaningfully distinguishes B from the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH18 family catalytic mechanism (Glu nucleophile + Glu proton donor in a DxE/DDE context, 4-residue spacing) is well-established transferable knowledge from hundreds of characterized GH18 chitinases. The sequence motifs (IWW, DGKNYPQTP, signal peptide, Ser-rich linker) allow family assignment. The 'DDE' at 107-109 with E113 four residues downstream matches the canonical pattern. The distractors are eliminated by basic biochemistry (Asn ≠ proton donor; His ≠ proton acceptor in GH18; position 975 > protein length)."
  },
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WD22 annotates position 109 as 'Active site: Nucleophile' (evidence C5/H3). The evidence code is ECO:0000250 (inferred by similarity from P27051, another chitinase), making this a transfer annotation rather than direct experimental evidence for this exact protein. However, the protein (Crh1, a GH18 chitin transglycosylase) has been functionally characterized (PubMed:30971696), and the Glu nucleophile at position 109 in the 'DDE' motif is consistent with the well-established GH18 catalytic mechanism. The annotation is present and consistent with family-level biochemistry."
  },
  "important_caveats": [
    "The UniProt annotation for position 109 uses evidence code ECO:0000250 (similarity-based transfer from P27051), not direct experimental mutagenesis evidence for Crh1 itself. However, functional characterization of Crh1 exists (PubMed:30971696).",
    "The annotation was first integrated into Swiss-Prot on 2025-06-18; the benchmark author's source snapshot is unknown. The sequence and annotation are stable (sequence version 1 since 2005).",
    "Option C (position 975) is a trivially eliminable distractor since the protein is 357 residues, which may reduce the question's difficulty beyond what the family-knowledge reasoning alone would require."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is impossible (position exceeds protein length). Option A assigns 'proton donor' to Asn, which is not a catalytic acid in glycosidases. Option D assigns 'proton acceptor' to His, which does not participate in the GH18 retaining mechanism. Only option B is consistent with both the sequence context and the established GH18 catalytic mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WD22 annotates position 109 as 'Active site: Nucleophile' (evidence C5/H3). The evidence code is ECO:0000250 (inferred by similarity from P27051, another chitinase), making this a transfer annotation rather than direct experimental evidence for this exact protein. However, the protein (Crh1, a GH18 chitin transglycosylase) has been functionally characterized (PubMed:30971696), and the Glu nucleophile at position 109 in the 'DDE' motif is consistent with the well-established GH18 catalytic mechanism. The annotation is present and consistent with family-level biochemistry.",
    "evidence_ids": ["C5", "H3", "C6", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can recognize this as a GH18-family chitinase/chitin transglycosylase from sequence features: the N-terminal signal peptide, the conserved 'IWW' motif (~positions 156-158), the 'DGKNYPQTP' motif (~positions 182-190), and the Ser/Thr-rich C-terminal linker. GH18 enzymes use a retaining mechanism with a Glu nucleophile in a conserved 'DGXE' or 'DDE' motif and a Glu proton donor 4 residues downstream. In this sequence, positions 107-109 form 'DDE' (D107-D108-E109) and position 113 is E (the proton donor, 4 residues after E109). This matches the canonical GH18 catalytic arrangement. Option C (position 975) is eliminated because the protein is only 357 residues long. Option A (position 92 = Asn, 'proton donor') is inconsistent because Asn is not a proton-donating catalytic residue in glycosidases. Option D (position 151 = His, 'proton acceptor') is inconsistent because GH18 does not employ a separate proton acceptor; the nucleophile Glu serves as both nucleophile and general base in the deglycosylation step. Thus, family-level knowledge of GH18 catalytic mechanism meaningfully distinguishes B from the other options.",
    "missing_item_specific_fact": "",
    "reason": "The GH18 family catalytic mechanism (Glu nucleophile + Glu proton donor in a DxE/DDE context, 4-residue spacing) is well-established transferable knowledge from hundreds of characterized GH18 chitinases. The sequence motifs (IWW, DGKNYPQTP, signal peptide, Ser-rich linker) allow family assignment. The 'DDE' at 107-109 with E113 four residues downstream matches the canonical pattern. The distractors are eliminated by basic biochemistry (Asn ≠ proton donor; His ≠ proton acceptor in GH18; position 975 > protein length)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is impossible (position exceeds protein length). Option A assigns 'proton donor' to Asn, which is not a catalytic acid in glycosidases. Option D assigns 'proton acceptor' to His, which does not participate in the GH18 retaining mechanism. Only option B is consistent with both the sequence context and the established GH18 catalytic mechanism."
  },
  "important_caveats": [
    "The UniProt annotation for position 109 uses evidence code ECO:0000250 (similarity-based transfer from P27051), not direct experimental mutagenesis evidence for Crh1 itself. However, functional characterization of Crh1 exists (PubMed:30971696).",
    "The annotation was first integrated into Swiss-Prot on 2025-06-18; the benchmark author's source snapshot is unknown. The sequence and annotation are stable (sequence version 1 since 2005).",
    "Option C (position 975) is a trivially eliminable distractor since the protein is 357 residues, which may reduce the question's difficulty beyond what the family-knowledge reasoning alone would require."
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
  "benchmark_sequence_length": 357,
  "benchmark_sequence_sha256": "ec9eee989d92a990718dcd7214cf49eeaec45c138b491bd8fd04ef815d8dc8af",
  "current_entry_audit": {
    "entryVersion": 109,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 357,
  "current_source_sequence_sha256": "ec9eee989d92a990718dcd7214cf49eeaec45c138b491bd8fd04ef815d8dc8af",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 107,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q4WD22",
  "selected_historical_entry_version": 107,
  "selected_historical_record_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "selected_historical_source_sequence_length": 357,
  "selected_historical_source_sequence_sha256": "ec9eee989d92a990718dcd7214cf49eeaec45c138b491bd8fd04ef815d8dc8af",
  "selected_historical_version": {
    "accession": "Q4WD22",
    "database": "Swiss-Prot",
    "entryVersion": 107,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH1_ASPFU",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4WD22\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":109,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitinase crh1\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitin transglycosylase crh1\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P27051\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":109},\"start\":{\"modifier\":\"EXACT\",\"value\":109}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P27051\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":113},\"start\":{\"modifier\":\"EXACT\",\"value\":113}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":113},\"start\":{\"modifier\":\"EXACT\",\"value\":113}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":193}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":197},\"start\":{\"modifier\":\"EXACT\",\"value\":197}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":208},\"start\":{\"modifier\":\"EXACT\",\"value\":208}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Fang W.\",\"Sanz A.B.\",\"Bartual S.G.\",\"Wang B.\",\"Ferenbach A.T.\",\"Farkas V.\",\"Hurtado-Guerrero R.\",\"Arroyo J.\",\"van Aalten D.M.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30971696\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-019-09674-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"1669\",\"id\":\"30971696\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"1669\",\"publicationDate\":\"2019\",\"title\":\"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh transglycosylases.\",\"volume\":\"10\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H1",
  "excerpt": "ID   CRH1_ASPFU              Reviewed;         357 AA.\nAC   Q4WD22;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 107.\nDE   RecName: Full=Crh-like protein 1 {ECO:0000303|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitinase crh1 {ECO:0000303|PubMed:30971696};\nDE              EC=3.2.1.14 {ECO:0000305|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh1 {ECO:0000303|PubMed:30971696};\nDE              EC=2.4.-.- {ECO:0000269|PubMed:30971696};\nDE   Flags: Precursor;\nGN   Name=crh1 {ECO:0000303|PubMed:30971696}; ORFNames=AFUA_6G03230;\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30971696; DOI=10.1038/s41467-019-09674-0;\nRA   Fang W., Sanz A.B., Bartual S.G., Wang B., Ferenbach A.T., Farkas V.,\nRA   Hurtado-Guerrero R., Arroyo J., van Aalten D.M.F.;\nRT   \"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh\nRT   transglycosylases.\";\nRL   Nat. Commun. 10:1669-1669(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        109\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P27051\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 132-134",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        113\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P27051\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 135-137",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         113\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 138-141",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         193\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-145",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         197\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 146-149",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         208\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 150-153",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 122. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
