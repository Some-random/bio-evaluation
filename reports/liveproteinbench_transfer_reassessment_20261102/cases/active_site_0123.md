# active_site_0123

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0123.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 119 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRLSLVGVAIGLLSSSAIVTAQTYTDCNPLQKTCPPDPALGRSVTYDFTKGSSPDFKPVGSPTYDSNNGAAFSVAKQGDAPLIQSNWYMMFGHVEFVIKTAPGKGIVSSAVLQSDDLDEIDWEWLGANNLYVQTNYFGKGDTGSYNRGAAHDNAGNQDGFHTYTIDWTSTQIVWQIDGKTVRVLTAESAGDHFPQSPMMVKVGVWAGGDPNNAPGTIQWAGGETDYSAGPYTMYLKSLVATDYSTGKSYTYSDKSGSWRSITSDGGQINGNSDAESISTVESAPPVTATIDSAPIPFSGTHRETSSFVTPSIWPWVPKPTTLSSSVAKDTTLPSGWTFSGSRQVQPPSAASSTPPCTSSSLVSSLASPSHSGLKTSSISSVPNSSSATKSTGHLASTATYQISTYDSTLPSFSASIAHVAPTVAAANDLLEAPLGMGVFCALLGGLIAIF

[Multiple Choices]
A. Position 119 (Nucleophile)
B. Position 1469 (Proton donor; for dehydratase activity)
C. Position 2882 (Proton donor; for dehydratase activity 2)
D. Position 226 (Proton acceptor)
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

> The sequence-matched UniProt annotation identifies residue 119 as the nucleophile. This is support by homology transfer, not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 450-residue sequence rules out positions 1469 and 2882. Its secreted-enzyme architecture and acidic catalytic-domain sequence are consistent with a fungal glycoside hydrolase, where a conserved catalytic glutamate can act as a nucleophile. Residue 119 is glutamate, whereas residue 226 is alanine, making A a substantially better fit than D for the stated nucleophile role.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence and catalytic-residue patterns provide a meaningful basis to choose A among the offered options, although they do not independently establish the exact annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The two very distant positions are outside the sequence, and the residue and role at position 119 are a better catalytic fit than the offered position 226.


### Important caveats

- The available annotation supports position 119 by similarity to another protein; it does not demonstrate that role experimentally in this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 450-residue sequence rules out positions 1469 and 2882. Its secreted-enzyme architecture and acidic catalytic-domain sequence are consistent with a fungal glycoside hydrolase, where a conserved catalytic glutamate can act as a nucleophile. Residue 119 is glutamate, whereas residue 226 is alanine, making A a substantially better fit than D for the stated nucleophile role.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and catalytic-residue patterns provide a meaningful basis to choose A among the offered options, although they do not independently establish the exact annotation."
  },
  "case_id": "active_site_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 119 as the nucleophile. This is support by homology transfer, not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The available annotation supports position 119 by similarity to another protein; it does not demonstrate that role experimentally in this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The two very distant positions are outside the sequence, and the residue and role at position 119 are a better catalytic fit than the offered position 226."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 119 as the nucleophile. This is support by homology transfer, not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 450-residue sequence rules out positions 1469 and 2882. Its secreted-enzyme architecture and acidic catalytic-domain sequence are consistent with a fungal glycoside hydrolase, where a conserved catalytic glutamate can act as a nucleophile. Residue 119 is glutamate, whereas residue 226 is alanine, making A a substantially better fit than D for the stated nucleophile role.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and catalytic-residue patterns provide a meaningful basis to choose A among the offered options, although they do not independently establish the exact annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The two very distant positions are outside the sequence, and the residue and role at position 119 are a better catalytic fit than the offered position 226."
  },
  "important_caveats": [
    "The available annotation supports position 119 by similarity to another protein; it does not demonstrate that role experimentally in this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4WMW2 annotates position 119 as 'Active site: Nucleophile' (evidence ECO:0000250, similarity-based from P27051). The 2019 Nature Communications paper (PubMed:30971696) provides experimental evidence for Crh4's chitinase/transglycosylase function. The annotation is a similarity-based inference rather than direct experimental proof for this specific residue, but it is consistent with the recognized DXDXE catalytic motif in the sequence and the published functional characterization. The expected answer matches the database annotation exactly.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C11](#evidence-c11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence is 450 amino acids long. Options B (position 1469) and C (position 2882) reference positions that do not exist in this protein, eliminating them immediately by simple sequence counting. This leaves A (position 119) and D (position 226). The sequence around positions 115-119 reads D-D-L-D-E, a recognizable variant of the DXXDXDXE catalytic motif found in GH18 glycosidases/chitinases. In this well-characterized family, the terminal glutamate (E) in the DXDXE motif acts as the catalytic nucleophile via a retaining mechanism. Position 119 is E, consistent with this role. Position 226 is Y (tyrosine), which is not a typical proton acceptor in glycosidase catalytic centers and is not located in the conserved catalytic motif. A model with knowledge of glycosidase families can thus distinguish A from D using family-level motif recognition.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer is reachable through two layers of transferable reasoning: (1) sequence-length constraint eliminates B and C, and (2) recognition of the DXDXE motif in a glycosidase context identifies E119 as the nucleophile. Both rely on general protein-family knowledge, not on memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are physically impossible for a 450-residue protein. Between A and D, the DXDXE motif at positions 115-119 and the well-established role of the terminal E as nucleophile in glycosidases strongly favor A. Y226 has no recognized catalytic role in this enzyme family. No ambiguity remains among the offered choices.


### Important caveats

- The UniProt annotation for position 119 as 'Nucleophile' carries evidence code ECO:0000250 (inferred by similarity from P27051), not direct experimental mutagenesis evidence for Crh4 itself. The 2019 paper provides experimental functional characterization but the specific residue assignment is by homology.
- The catalytic motif in Crh4 (D-D-L-D-E) is a slightly modified version of the canonical GH18 DXXDXDXE motif; the assignment of E119 as nucleophile is consistent with the shortened motif observed in Crh-family proteins.
- Options B and C are trivially eliminated by sequence length, making the effective discrimination only between A and D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence is 450 amino acids long. Options B (position 1469) and C (position 2882) reference positions that do not exist in this protein, eliminating them immediately by simple sequence counting. This leaves A (position 119) and D (position 226). The sequence around positions 115-119 reads D-D-L-D-E, a recognizable variant of the DXXDXDXE catalytic motif found in GH18 glycosidases/chitinases. In this well-characterized family, the terminal glutamate (E) in the DXDXE motif acts as the catalytic nucleophile via a retaining mechanism. Position 119 is E, consistent with this role. Position 226 is Y (tyrosine), which is not a typical proton acceptor in glycosidase catalytic centers and is not located in the conserved catalytic motif. A model with knowledge of glycosidase families can thus distinguish A from D using family-level motif recognition.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer is reachable through two layers of transferable reasoning: (1) sequence-length constraint eliminates B and C, and (2) recognition of the DXDXE motif in a glycosidase context identifies E119 as the nucleophile. Both rely on general protein-family knowledge, not on memorizing this specific protein's database entry."
  },
  "case_id": "active_site_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C11"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4WMW2 annotates position 119 as 'Active site: Nucleophile' (evidence ECO:0000250, similarity-based from P27051). The 2019 Nature Communications paper (PubMed:30971696) provides experimental evidence for Crh4's chitinase/transglycosylase function. The annotation is a similarity-based inference rather than direct experimental proof for this specific residue, but it is consistent with the recognized DXDXE catalytic motif in the sequence and the published functional characterization. The expected answer matches the database annotation exactly."
  },
  "important_caveats": [
    "The UniProt annotation for position 119 as 'Nucleophile' carries evidence code ECO:0000250 (inferred by similarity from P27051), not direct experimental mutagenesis evidence for Crh4 itself. The 2019 paper provides experimental functional characterization but the specific residue assignment is by homology.",
    "The catalytic motif in Crh4 (D-D-L-D-E) is a slightly modified version of the canonical GH18 DXXDXDXE motif; the assignment of E119 as nucleophile is consistent with the shortened motif observed in Crh-family proteins.",
    "Options B and C are trivially eliminated by sequence length, making the effective discrimination only between A and D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are physically impossible for a 450-residue protein. Between A and D, the DXDXE motif at positions 115-119 and the well-established role of the terminal E as nucleophile in glycosidases strongly favor A. Y226 has no recognized catalytic role in this enzyme family. No ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4WMW2 annotates position 119 as 'Active site: Nucleophile' (evidence ECO:0000250, similarity-based from P27051). The 2019 Nature Communications paper (PubMed:30971696) provides experimental evidence for Crh4's chitinase/transglycosylase function. The annotation is a similarity-based inference rather than direct experimental proof for this specific residue, but it is consistent with the recognized DXDXE catalytic motif in the sequence and the published functional characterization. The expected answer matches the database annotation exactly.",
    "evidence_ids": ["C5", "H3", "C11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence is 450 amino acids long. Options B (position 1469) and C (position 2882) reference positions that do not exist in this protein, eliminating them immediately by simple sequence counting. This leaves A (position 119) and D (position 226). The sequence around positions 115-119 reads D-D-L-D-E, a recognizable variant of the DXXDXDXE catalytic motif found in GH18 glycosidases/chitinases. In this well-characterized family, the terminal glutamate (E) in the DXDXE motif acts as the catalytic nucleophile via a retaining mechanism. Position 119 is E, consistent with this role. Position 226 is Y (tyrosine), which is not a typical proton acceptor in glycosidase catalytic centers and is not located in the conserved catalytic motif. A model with knowledge of glycosidase families can thus distinguish A from D using family-level motif recognition.",
    "missing_item_specific_fact": "",
    "reason": "The answer is reachable through two layers of transferable reasoning: (1) sequence-length constraint eliminates B and C, and (2) recognition of the DXDXE motif in a glycosidase context identifies E119 as the nucleophile. Both rely on general protein-family knowledge, not on memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are physically impossible for a 450-residue protein. Between A and D, the DXDXE motif at positions 115-119 and the well-established role of the terminal E as nucleophile in glycosidases strongly favor A. Y226 has no recognized catalytic role in this enzyme family. No ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for position 119 as 'Nucleophile' carries evidence code ECO:0000250 (inferred by similarity from P27051), not direct experimental mutagenesis evidence for Crh4 itself. The 2019 paper provides experimental functional characterization but the specific residue assignment is by homology.",
    "The catalytic motif in Crh4 (D-D-L-D-E) is a slightly modified version of the canonical GH18 DXXDXDXE motif; the assignment of E119 as nucleophile is consistent with the shortened motif observed in Crh-family proteins.",
    "Options B and C are trivially eliminated by sequence length, making the effective discrimination only between A and D."
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
  "benchmark_sequence_length": 450,
  "benchmark_sequence_sha256": "04601653eafe86ebbbaab3cb019bcbf23ea7d99baf8fb8d80cf3264e77cb5e45",
  "current_entry_audit": {
    "entryVersion": 111,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 450,
  "current_source_sequence_sha256": "04601653eafe86ebbbaab3cb019bcbf23ea7d99baf8fb8d80cf3264e77cb5e45",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 109,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q4WMW2",
  "selected_historical_entry_version": 109,
  "selected_historical_record_sha256": "b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82",
  "selected_historical_source_sequence_length": 450,
  "selected_historical_source_sequence_sha256": "04601653eafe86ebbbaab3cb019bcbf23ea7d99baf8fb8d80cf3264e77cb5e45",
  "selected_historical_version": {
    "accession": "Q4WMW2",
    "database": "Swiss-Prot",
    "entryVersion": 109,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH4_ASPFU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4WMW2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":111,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitinase crh4\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitin transglycosylase crh4\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 4\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P27051\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":119},\"start\":{\"modifier\":\"EXACT\",\"value\":119}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P27051\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":123},\"start\":{\"modifier\":\"EXACT\",\"value\":123}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":123},\"start\":{\"modifier\":\"EXACT\",\"value\":123}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":201},\"start\":{\"modifier\":\"EXACT\",\"value\":201}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":205},\"start\":{\"modifier\":\"EXACT\",\"value\":205}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":216},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Fang W.\",\"Sanz A.B.\",\"Bartual S.G.\",\"Wang B.\",\"Ferenbach A.T.\",\"Farkas V.\",\"Hurtado-Guerrero R.\",\"Arroyo J.\",\"van Aalten D.M.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30971696\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-019-09674-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"1669\",\"id\":\"30971696\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"1669\",\"publicationDate\":\"2019\",\"title\":\"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh transglycosylases.\",\"volume\":\"10\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:21.573750+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WMW2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)

```json
{
  "entry_version": 109,
  "evidence_id": "H1",
  "excerpt": "ID   CRH4_ASPFU              Reviewed;         450 AA.\nAC   Q4WMW2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 109.\nDE   RecName: Full=Crh-like protein 4 {ECO:0000303|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitinase crh4 {ECO:0000303|PubMed:30971696};\nDE              EC=3.2.1.14 {ECO:0000305|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh4 {ECO:0000303|PubMed:30971696};\nDE              EC=2.4.-.- {ECO:0000269|PubMed:30971696};\nDE   Flags: Precursor;\nGN   Name=crh4 {ECO:0000303|PubMed:30971696}; ORFNames=AFUA_6G08510;\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:35.372546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82",
  "url": "https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)

```json
{
  "entry_version": 109,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30971696; DOI=10.1038/s41467-019-09674-0;\nRA   Fang W., Sanz A.B., Bartual S.G., Wang B., Ferenbach A.T., Farkas V.,\nRA   Hurtado-Guerrero R., Arroyo J., van Aalten D.M.F.;\nRT   \"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh\nRT   transglycosylases.\";\nRL   Nat. Commun. 10:1669-1669(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:35.372546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82",
  "url": "https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)

```json
{
  "entry_version": 109,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        119\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P27051\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:35.372546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82",
  "url": "https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)

```json
{
  "entry_version": 109,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        123\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P27051\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:35.372546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-141",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82",
  "url": "https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)

```json
{
  "entry_version": 109,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         123\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:35.372546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-145",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82",
  "url": "https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)

```json
{
  "entry_version": 109,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         201\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:35.372546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 146-149",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82",
  "url": "https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)

```json
{
  "entry_version": 109,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         205\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:35.372546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 150-153",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82",
  "url": "https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)

```json
{
  "entry_version": 109,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         216\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:35.372546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 154-157",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82",
  "url": "https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 123. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
