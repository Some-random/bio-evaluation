# active_site_0009

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0009.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 154 (Acyl-thioester intermediate)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTPSKKRCGVLGATGAVGTRFILLLEQSPLLELVAVGASERSAGKKYRDAVRWKQASPMPASVADLTVRRCAPSEFSDCDIIFSGLDPVAAGDIEMAFLKANFAVFSNAKNYRLDPIVPLVVPLVNAGHIDVIPAQRKHYGLDKGLIVCNSNCAVVGLVIPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPFIPGEEGKIATESRKILGNLNPDLAGFSDQQPLQVSVACNRVPVLDGHTVCASLRFVNRPAPTASQVRDALREYKSEVQLLGCPSAPRQAIHVLDDVDRPQPRLDRDTEAGYACSVGRIREDDSGVFDIQFVALSHNTVLGASGSSILNAESAILKGYI

[Multiple Choices]
A. Position 148 (Proton acceptor)
B. Position 159 (Proton donor)
C. Position 308 (Proton acceptor)
D. Position 154 (Acyl-thioester intermediate)
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

> The sequence-matched UniProt record annotates position 154 as the acyl-thioester intermediate site, matching option D. This is a computational PIRSR annotation, not direct experimental evidence for that residue in this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable solver could recognize the sequence as consistent with the aspartate-semialdehyde dehydrogenase family. In this enzyme family, a conserved catalytic cysteine attacks the substrate and forms a covalent acyl-thioester intermediate. The cysteine at position 154 is therefore a credible match for D, distinguishing it from the offered proton-transfer roles.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level catalytic mechanism and conserved cysteine feature provide a transferable basis for selecting D; the exact protein annotation is not necessary to make that inference, though it would strengthen it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered roles distinguish the catalytic cysteine intermediate from the proton-transfer alternatives.


### Important caveats

- The supporting residue annotation is computationally transferred by a family rule; the supplied evidence does not independently establish it through a direct experiment on this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable solver could recognize the sequence as consistent with the aspartate-semialdehyde dehydrogenase family. In this enzyme family, a conserved catalytic cysteine attacks the substrate and forms a covalent acyl-thioester intermediate. The cysteine at position 154 is therefore a credible match for D, distinguishing it from the offered proton-transfer roles.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level catalytic mechanism and conserved cysteine feature provide a transferable basis for selecting D; the exact protein annotation is not necessary to make that inference, though it would strengthen it."
  },
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 154 as the acyl-thioester intermediate site, matching option D. This is a computational PIRSR annotation, not direct experimental evidence for that residue in this protein."
  },
  "important_caveats": [
    "The supporting residue annotation is computationally transferred by a family rule; the supplied evidence does not independently establish it through a direct experiment on this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered roles distinguish the catalytic cysteine intermediate from the proton-transfer alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 154 as the acyl-thioester intermediate site, matching option D. This is a computational PIRSR annotation, not direct experimental evidence for that residue in this protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable solver could recognize the sequence as consistent with the aspartate-semialdehyde dehydrogenase family. In this enzyme family, a conserved catalytic cysteine attacks the substrate and forms a covalent acyl-thioester intermediate. The cysteine at position 154 is therefore a credible match for D, distinguishing it from the offered proton-transfer roles.",
    "missing_item_specific_fact": "",
    "reason": "The family-level catalytic mechanism and conserved cysteine feature provide a transferable basis for selecting D; the exact protein annotation is not necessary to make that inference, though it would strengthen it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered roles distinguish the catalytic cysteine intermediate from the proton-transfer alternatives."
  },
  "important_caveats": [
    "The supporting residue annotation is computationally transferred by a family rule; the supplied evidence does not independently establish it through a direct experiment on this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5/H4) explicitly annotates position 154 as 'Acyl-thioester intermediate' active site with evidence code ECO:0000255 (PIRSR curated annotation). The residue at position 154 in the provided sequence is Cysteine (C), which is chemically consistent with forming an acyl-thioester intermediate. The protein is identified as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism involves a Cys-His dyad where the Cys forms the thioester. The annotation is a curated computational assignment (PIRSR000148-1) rather than direct experimental mutagenesis on this specific protein, but it is well-supported by the conserved mechanism across the ASADH family and corroborated by PDB structures (6C8W, 6C85) of the same enzyme.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable knowledge pathways converge on D: (1) The N-terminal region (GATGAVGT around positions 12-19) shows a degenerate Rossmann-fold motif indicating an NAD(P)-binding dehydrogenase. (2) The 'CNSNCA' motif at positions 151-156 is a well-known ASADH family signature observed across E. coli, M. tuberculosis, and other ASADH orthologs. (3) ASADH mechanism (known from multiple family members): the catalytic Cys in this motif attacks the substrate carboxyl to form an acyl-thioester intermediate, while a His (here at position 251 in the 'HTVCASL' context) acts as proton acceptor. (4) Even without family identification, chemical consistency eliminates alternatives: position 148 is Ile (cannot be proton acceptor), position 159 is Leu (cannot be proton donor), position 308 is Asp (not the catalytic proton acceptor in this enzyme class). Only position 154 (Cys) is chemically compatible with forming a thioester intermediate, which is the hallmark of Cys-dependent dehydrogenase catalysis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of dehydrogenase families, the Cys-His catalytic dyad mechanism, and the CNSNCA ASADH signature can identify position 154 (Cys) as the thioester-forming residue. The other options are eliminated by basic residue chemistry (Ile, Leu, Asp cannot perform the stated roles in this enzyme context). The inference relies on family-level mechanism knowledge transferable from other ASADH proteins, not on memorizing this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D presents a chemically consistent residue-role pair (Cys-thioester). Options A (Ile as proton acceptor), B (Leu as proton donor), and C (Asp as proton acceptor in this enzyme context) are all chemically implausible for the described roles. No ambiguity exists among the offered choices.


### Important caveats

- The active site annotation uses evidence code ECO:0000255 (PIRSR), which is a curated computational/protein-family assignment rather than site-directed mutagenesis on this exact protein. However, the mechanism is well-established across the ASADH family and supported by crystal structures of this enzyme.
- The UniProt entry was first released in January 2026; the benchmark author's source snapshot timing is unknown, though the sequence matches.
- Position numbering is canonical (362 aa full-length); no construct or isoform adjustments apply.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable knowledge pathways converge on D: (1) The N-terminal region (GATGAVGT around positions 12-19) shows a degenerate Rossmann-fold motif indicating an NAD(P)-binding dehydrogenase. (2) The 'CNSNCA' motif at positions 151-156 is a well-known ASADH family signature observed across E. coli, M. tuberculosis, and other ASADH orthologs. (3) ASADH mechanism (known from multiple family members): the catalytic Cys in this motif attacks the substrate carboxyl to form an acyl-thioester intermediate, while a His (here at position 251 in the 'HTVCASL' context) acts as proton acceptor. (4) Even without family identification, chemical consistency eliminates alternatives: position 148 is Ile (cannot be proton acceptor), position 159 is Leu (cannot be proton donor), position 308 is Asp (not the catalytic proton acceptor in this enzyme class). Only position 154 (Cys) is chemically compatible with forming a thioester intermediate, which is the hallmark of Cys-dependent dehydrogenase catalysis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of dehydrogenase families, the Cys-His catalytic dyad mechanism, and the CNSNCA ASADH signature can identify position 154 (Cys) as the thioester-forming residue. The other options are eliminated by basic residue chemistry (Ile, Leu, Asp cannot perform the stated roles in this enzyme context). The inference relies on family-level mechanism knowledge transferable from other ASADH proteins, not on memorizing this specific entry's annotation."
  },
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H4) explicitly annotates position 154 as 'Acyl-thioester intermediate' active site with evidence code ECO:0000255 (PIRSR curated annotation). The residue at position 154 in the provided sequence is Cysteine (C), which is chemically consistent with forming an acyl-thioester intermediate. The protein is identified as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism involves a Cys-His dyad where the Cys forms the thioester. The annotation is a curated computational assignment (PIRSR000148-1) rather than direct experimental mutagenesis on this specific protein, but it is well-supported by the conserved mechanism across the ASADH family and corroborated by PDB structures (6C8W, 6C85) of the same enzyme."
  },
  "important_caveats": [
    "The active site annotation uses evidence code ECO:0000255 (PIRSR), which is a curated computational/protein-family assignment rather than site-directed mutagenesis on this exact protein. However, the mechanism is well-established across the ASADH family and supported by crystal structures of this enzyme.",
    "The UniProt entry was first released in January 2026; the benchmark author's source snapshot timing is unknown, though the sequence matches.",
    "Position numbering is canonical (362 aa full-length); no construct or isoform adjustments apply."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D presents a chemically consistent residue-role pair (Cys-thioester). Options A (Ile as proton acceptor), B (Leu as proton donor), and C (Asp as proton acceptor in this enzyme context) are all chemically implausible for the described roles. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H4) explicitly annotates position 154 as 'Acyl-thioester intermediate' active site with evidence code ECO:0000255 (PIRSR curated annotation). The residue at position 154 in the provided sequence is Cysteine (C), which is chemically consistent with forming an acyl-thioester intermediate. The protein is identified as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism involves a Cys-His dyad where the Cys forms the thioester. The annotation is a curated computational assignment (PIRSR000148-1) rather than direct experimental mutagenesis on this specific protein, but it is well-supported by the conserved mechanism across the ASADH family and corroborated by PDB structures (6C8W, 6C85) of the same enzyme.",
    "evidence_ids": ["C5", "H4", "C4", "C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable knowledge pathways converge on D: (1) The N-terminal region (GATGAVGT around positions 12-19) shows a degenerate Rossmann-fold motif indicating an NAD(P)-binding dehydrogenase. (2) The 'CNSNCA' motif at positions 151-156 is a well-known ASADH family signature observed across E. coli, M. tuberculosis, and other ASADH orthologs. (3) ASADH mechanism (known from multiple family members): the catalytic Cys in this motif attacks the substrate carboxyl to form an acyl-thioester intermediate, while a His (here at position 251 in the 'HTVCASL' context) acts as proton acceptor. (4) Even without family identification, chemical consistency eliminates alternatives: position 148 is Ile (cannot be proton acceptor), position 159 is Leu (cannot be proton donor), position 308 is Asp (not the catalytic proton acceptor in this enzyme class). Only position 154 (Cys) is chemically compatible with forming a thioester intermediate, which is the hallmark of Cys-dependent dehydrogenase catalysis.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of dehydrogenase families, the Cys-His catalytic dyad mechanism, and the CNSNCA ASADH signature can identify position 154 (Cys) as the thioester-forming residue. The other options are eliminated by basic residue chemistry (Ile, Leu, Asp cannot perform the stated roles in this enzyme context). The inference relies on family-level mechanism knowledge transferable from other ASADH proteins, not on memorizing this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D presents a chemically consistent residue-role pair (Cys-thioester). Options A (Ile as proton acceptor), B (Leu as proton donor), and C (Asp as proton acceptor in this enzyme context) are all chemically implausible for the described roles. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The active site annotation uses evidence code ECO:0000255 (PIRSR), which is a curated computational/protein-family assignment rather than site-directed mutagenesis on this exact protein. However, the mechanism is well-established across the ASADH family and supported by crystal structures of this enzyme.",
    "The UniProt entry was first released in January 2026; the benchmark author's source snapshot timing is unknown, though the sequence matches.",
    "Position numbering is canonical (362 aa full-length); no construct or isoform adjustments apply."
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
  "benchmark_sequence_length": 362,
  "benchmark_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 362,
  "current_source_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A179UL48",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "selected_historical_source_sequence_length": 362,
  "selected_historical_source_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "selected_historical_version": {
    "accession": "A0A179UL48",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_BLAGS",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A179UL48\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Blastomyces dermatitidis\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002038\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Onygenales\",\"Ajellomycetaceae\",\"Blastomyces\"],\"scientificName\":\"Blastomyces gilchristii (strain SLH14081)\",\"taxonId\":559298}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Acyl-thioester intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":154},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":251},\"start\":{\"modifier\":\"EXACT\",\"value\":251}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":15},\"start\":{\"modifier\":\"EXACT\",\"value\":15}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":16},\"start\":{\"modifier\":\"EXACT\",\"value\":16}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":17},\"start\":{\"modifier\":\"EXACT\",\"value\":17}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":18},\"start\":{\"modifier\":\"EXACT\",\"value\":18}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":40},\"start\":{\"modifier\":\"EXACT\",\"value\":40}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":43},\"start\":{\"modifier\":\"EXACT\",\"value\":43}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":87},\"start\":{\"modifier\":\"EXACT\",\"value\":87}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":88},\"start\":{\"modifier\":\"EXACT\",\"value\":88}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":340},\"start\":{\"modifier\":\"EXACT\",\"value\":340}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30107909\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbrc.2018.08.053\"}],\"citationType\":\"journal article\",\"firstPage\":\"2848\",\"id\":\"30107909\",\"journal\":\"Biochem. Biophys. Res. Commun.\",\"lastPage\":\"2854\",\"publicationDate\":\"2018\",\"title\":\"Structural insights into inhibitor binding to a fungal ortholog of aspartate semialdehyde dehydrogenase.\",\"volume\":\"503\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C85\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND NADP(+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_BLAGS              Reviewed;         362 AA.\nAC   A0A179UL48;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};\nGN   ORFNames=BDBG_16922 {ECO:0000312|EMBL:OAT07949.1};\nOS   Blastomyces gilchristii (strain SLH14081) (Blastomyces dermatitidis).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Onygenales; Ajellomycetaceae; Blastomyces.\nOX   NCBI_TaxID=559298 {ECO:0000312|Proteomes:UP000002038};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:6C85, ECO:0007744|PDB:6C8W}\nRP   X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND\nRP   NADP(+), FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=30107909; DOI=10.1016/j.bbrc.2018.08.053;\nRA   Dahal G.P., Viola R.E.;\nRT   \"Structural insights into inhibitor binding to a fungal ortholog of\nRT   aspartate semialdehyde dehydrogenase.\";\nRL   Biochem. Biophys. Res. Commun. 503:2848-2854(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        154\nFT                   /note=\"Acyl-thioester intermediate\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 133-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        251\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         15\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         16\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         17\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         18\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-157",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         40\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 158-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         43\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         87\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 168-172",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         88\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 173-176",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         186\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 177-180",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H15",
  "excerpt": "FT   BINDING         340\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:30107909,\nFT                   ECO:0007744|PDB:6C8W\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 181-185",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
