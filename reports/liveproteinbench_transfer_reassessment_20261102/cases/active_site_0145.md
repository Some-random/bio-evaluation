# active_site_0145

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0145.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 188 (Glycyl thioester intermediate; for adenylyltransferase activity)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSLSLNEYLRYGRQLIVPEFGLQGQISLKNSRVLVVGAGGLGCPALQYLVGAGFGTVGIVDHDTVDISNLHRQILHTSETVEMLKCESAKLQLAKLNPLVQINTHPVALSPDNSFGIFEQYDIILDCTDTPATRYLINDTAVLLGLTVISGSGLKTEGQLSILNFNNTGPCYRCFYPTPPPPSSVTACSDGGVLGPVIGIMGVMMALEAIKVVSGYYLREDVEFQPFLSLYSGYGPLQSLRTFKMRRRSPKCRVCNAGTREITRHVIETELDYAVWCGKMDYNVLEKDERVSVEQLSAQRAPYLVDVRAKEQYSIVHLPNSINIPLNALKHMDTLDVPKETMIYVICRFGNDSQLAVKHLKSIGYENCVDVIGGLTQWSRQIDPNFPIY

[Multiple Choices]
A. Position 240 (Proton acceptor)
B. Position 188 (Glycyl thioester intermediate; for adenylyltransferase activity)
C. Position 118 (Nucleophile)
D. Position 203 (Proton donor)
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

> The sequence-matched UniProt annotation identifies position 188 as an active site involved in a glycyl thioester intermediate for adenylyltransferase activity. This is computational, rule-based annotation rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a glycine-rich region consistent with nucleotide-binding enzyme architecture, and position 188 is glycine. Transferable knowledge of UBA4-like sulfur-carrier activation enzymes connects an adenylyltransferase module to a catalytic glycine-bearing site; among these choices, that makes B a meaningful family-level inference, though not a sequence-only proof.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family/mechanism-based inference can distinguish B from the alternatives without recalling this exact protein's database record. The exact residue annotation is still target-specific evidence that strengthens the key but is not necessary to make B the best-supported option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option has comparable support as the adenylyltransferase catalytic-site choice.


### Important caveats

- The supplied source annotation is computational and rule-based; it does not establish experimental validation.
- The protein has another annotated active-site position not offered among the choices, so the options do not enumerate all catalytic sites.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich region consistent with nucleotide-binding enzyme architecture, and position 188 is glycine. Transferable knowledge of UBA4-like sulfur-carrier activation enzymes connects an adenylyltransferase module to a catalytic glycine-bearing site; among these choices, that makes B a meaningful family-level inference, though not a sequence-only proof.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family/mechanism-based inference can distinguish B from the alternatives without recalling this exact protein's database record. The exact residue annotation is still target-specific evidence that strengthens the key but is not necessary to make B the best-supported option."
  },
  "case_id": "active_site_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 188 as an active site involved in a glycyl thioester intermediate for adenylyltransferase activity. This is computational, rule-based annotation rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The supplied source annotation is computational and rule-based; it does not establish experimental validation.",
    "The protein has another annotated active-site position not offered among the choices, so the options do not enumerate all catalytic sites."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option has comparable support as the adenylyltransferase catalytic-site choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 188 as an active site involved in a glycyl thioester intermediate for adenylyltransferase activity. This is computational, rule-based annotation rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["H3", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a glycine-rich region consistent with nucleotide-binding enzyme architecture, and position 188 is glycine. Transferable knowledge of UBA4-like sulfur-carrier activation enzymes connects an adenylyltransferase module to a catalytic glycine-bearing site; among these choices, that makes B a meaningful family-level inference, though not a sequence-only proof.",
    "missing_item_specific_fact": "",
    "reason": "A family/mechanism-based inference can distinguish B from the alternatives without recalling this exact protein's database record. The exact residue annotation is still target-specific evidence that strengthens the key but is not necessary to make B the best-supported option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option has comparable support as the adenylyltransferase catalytic-site choice."
  },
  "important_caveats": [
    "The supplied source annotation is computational and rule-based; it does not establish experimental validation.",
    "The protein has another annotated active-site position not offered among the choices, so the options do not enumerate all catalytic sites."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5/H3) explicitly annotates position 188 as 'Glycyl thioester intermediate; for adenylyltransferase activity' (ECO:0000255, HAMAP-Rule MF_03049). The residue at position 188 in the supplied sequence is Cysteine (C), which is chemically consistent with forming a thioester bond. The protein is annotated as UBA4 (Adenylyltransferase and sulfurtransferase), an E1-like adenylyltransferase whose mechanism involves a catalytic cysteine forming a glycyl thioester intermediate. The annotation is computational (HAMAP rule) rather than directly experimental, but is consistent with the well-established E1-like enzyme mechanism.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region displays a classic Rossmann-fold nucleotide-binding motif (GAGGLGCPALQYLVGAGFGTVGIV at ~positions 37-60), identifying this as an E1-like adenylyltransferase (ubiquitin-activating enzyme superfamily). The key discriminating argument is residue chemistry: a glycyl thioester intermediate REQUIRES a cysteine (thiol group attacks the acyl-adenylate to form a thioester bond). Checking the offered positions: position 188 is Cysteine (C) — capable of thioester formation; position 240 is Leucine (L) — cannot act as a proton acceptor; position 118 is Phenylalanine (F) — cannot act as a nucleophile; position 203 is Valine (V) — cannot act as a proton donor. Thus, three of four options assign catalytic roles to residues that are chemically incapable of performing those functions. This is transferable knowledge from all E1-like enzymes (Uba1, Uba2, APPBP1, NEDD8-activating enzymes) where the catalytic Cys forms the thioester intermediate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can (1) recognize the Rossmann-fold motifs to identify the E1-like adenylyltransferase family, (2) recall that E1-like enzymes form thioester intermediates via a catalytic cysteine, and (3) verify that only position 188 harbors a cysteine while the other three positions have residues (Leu, Phe, Val) that are chemically incompatible with the described catalytic roles. This eliminates A, C, and D on purely chemical grounds without needing to know this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option B assigns a catalytic role to a residue (Cys) that is chemically capable of performing the stated function (thioester formation). The other three options assign roles (proton acceptor, nucleophile, proton donor) to residues (Leu, Phe, Val) that lack the necessary functional groups, making them chemically implausible.


### Important caveats

- The UniProt annotation for position 188 is based on HAMAP-Rule MF_03049 (ECO:0000255), a computational/curated inference from family rules rather than direct experimental mutagenesis on this specific protein.
- The protein also has a second active site (Cys347, Cysteine persulfide intermediate for sulfurtransferase activity per PROSITE-ProRule), but this is not offered as an option.
- Correct residue numbering requires accurate counting through the 389-residue sequence; the chemical-logic argument (only Cys can form a thioester) provides a robust shortcut that does not depend on perfect counting of all other positions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region displays a classic Rossmann-fold nucleotide-binding motif (GAGGLGCPALQYLVGAGFGTVGIV at ~positions 37-60), identifying this as an E1-like adenylyltransferase (ubiquitin-activating enzyme superfamily). The key discriminating argument is residue chemistry: a glycyl thioester intermediate REQUIRES a cysteine (thiol group attacks the acyl-adenylate to form a thioester bond). Checking the offered positions: position 188 is Cysteine (C) — capable of thioester formation; position 240 is Leucine (L) — cannot act as a proton acceptor; position 118 is Phenylalanine (F) — cannot act as a nucleophile; position 203 is Valine (V) — cannot act as a proton donor. Thus, three of four options assign catalytic roles to residues that are chemically incapable of performing those functions. This is transferable knowledge from all E1-like enzymes (Uba1, Uba2, APPBP1, NEDD8-activating enzymes) where the catalytic Cys forms the thioester intermediate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) recognize the Rossmann-fold motifs to identify the E1-like adenylyltransferase family, (2) recall that E1-like enzymes form thioester intermediates via a catalytic cysteine, and (3) verify that only position 188 harbors a cysteine while the other three positions have residues (Leu, Phe, Val) that are chemically incompatible with the described catalytic roles. This eliminates A, C, and D on purely chemical grounds without needing to know this specific protein's annotation."
  },
  "case_id": "active_site_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) explicitly annotates position 188 as 'Glycyl thioester intermediate; for adenylyltransferase activity' (ECO:0000255, HAMAP-Rule MF_03049). The residue at position 188 in the supplied sequence is Cysteine (C), which is chemically consistent with forming a thioester bond. The protein is annotated as UBA4 (Adenylyltransferase and sulfurtransferase), an E1-like adenylyltransferase whose mechanism involves a catalytic cysteine forming a glycyl thioester intermediate. The annotation is computational (HAMAP rule) rather than directly experimental, but is consistent with the well-established E1-like enzyme mechanism."
  },
  "important_caveats": [
    "The UniProt annotation for position 188 is based on HAMAP-Rule MF_03049 (ECO:0000255), a computational/curated inference from family rules rather than direct experimental mutagenesis on this specific protein.",
    "The protein also has a second active site (Cys347, Cysteine persulfide intermediate for sulfurtransferase activity per PROSITE-ProRule), but this is not offered as an option.",
    "Correct residue numbering requires accurate counting through the 389-residue sequence; the chemical-logic argument (only Cys can form a thioester) provides a robust shortcut that does not depend on perfect counting of all other positions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B assigns a catalytic role to a residue (Cys) that is chemically capable of performing the stated function (thioester formation). The other three options assign roles (proton acceptor, nucleophile, proton donor) to residues (Leu, Phe, Val) that lack the necessary functional groups, making them chemically implausible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) explicitly annotates position 188 as 'Glycyl thioester intermediate; for adenylyltransferase activity' (ECO:0000255, HAMAP-Rule MF_03049). The residue at position 188 in the supplied sequence is Cysteine (C), which is chemically consistent with forming a thioester bond. The protein is annotated as UBA4 (Adenylyltransferase and sulfurtransferase), an E1-like adenylyltransferase whose mechanism involves a catalytic cysteine forming a glycyl thioester intermediate. The annotation is computational (HAMAP rule) rather than directly experimental, but is consistent with the well-established E1-like enzyme mechanism.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region displays a classic Rossmann-fold nucleotide-binding motif (GAGGLGCPALQYLVGAGFGTVGIV at ~positions 37-60), identifying this as an E1-like adenylyltransferase (ubiquitin-activating enzyme superfamily). The key discriminating argument is residue chemistry: a glycyl thioester intermediate REQUIRES a cysteine (thiol group attacks the acyl-adenylate to form a thioester bond). Checking the offered positions: position 188 is Cysteine (C) — capable of thioester formation; position 240 is Leucine (L) — cannot act as a proton acceptor; position 118 is Phenylalanine (F) — cannot act as a nucleophile; position 203 is Valine (V) — cannot act as a proton donor. Thus, three of four options assign catalytic roles to residues that are chemically incapable of performing those functions. This is transferable knowledge from all E1-like enzymes (Uba1, Uba2, APPBP1, NEDD8-activating enzymes) where the catalytic Cys forms the thioester intermediate.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) recognize the Rossmann-fold motifs to identify the E1-like adenylyltransferase family, (2) recall that E1-like enzymes form thioester intermediates via a catalytic cysteine, and (3) verify that only position 188 harbors a cysteine while the other three positions have residues (Leu, Phe, Val) that are chemically incompatible with the described catalytic roles. This eliminates A, C, and D on purely chemical grounds without needing to know this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B assigns a catalytic role to a residue (Cys) that is chemically capable of performing the stated function (thioester formation). The other three options assign roles (proton acceptor, nucleophile, proton donor) to residues (Leu, Phe, Val) that lack the necessary functional groups, making them chemically implausible."
  },
  "important_caveats": [
    "The UniProt annotation for position 188 is based on HAMAP-Rule MF_03049 (ECO:0000255), a computational/curated inference from family rules rather than direct experimental mutagenesis on this specific protein.",
    "The protein also has a second active site (Cys347, Cysteine persulfide intermediate for sulfurtransferase activity per PROSITE-ProRule), but this is not offered as an option.",
    "Correct residue numbering requires accurate counting through the 389-residue sequence; the chemical-logic argument (only Cys can form a thioester) provides a robust shortcut that does not depend on perfect counting of all other positions."
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
  "benchmark_sequence_length": 389,
  "benchmark_sequence_sha256": "a901665ea3dc44218892e98264561a93d82231546cdf75b9015b7ec0eb86f63a",
  "current_entry_audit": {
    "entryVersion": 69,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 389,
  "current_source_sequence_sha256": "a901665ea3dc44218892e98264561a93d82231546cdf75b9015b7ec0eb86f63a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "W1QET1",
  "selected_historical_entry_version": 67,
  "selected_historical_record_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "selected_historical_source_sequence_length": 389,
  "selected_historical_source_sequence_sha256": "a901665ea3dc44218892e98264561a93d82231546cdf75b9015b7ec0eb86f63a",
  "selected_historical_version": {
    "accession": "W1QET1",
    "database": "Swiss-Prot",
    "entryVersion": 67,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UBA4_OGAPD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"W1QET1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":69,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008673\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Pichiales\",\"Pichiaceae\",\"Ogataea\"],\"scientificName\":\"Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL Y-7560 / DL-1)\",\"synonyms\":[\"Hansenula polymorpha\"],\"taxonId\":871575}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Ubiquitin-like protein activator 4\"}}],\"includes\":[{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Adenylyltransferase UBA4\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Sulfur carrier protein MOCS2A adenylyltransferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O95396\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.7.80\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Molybdopterin-synthase adenylyltransferase\"}}},{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Sulfur carrier protein MOCS2A sulfurtransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Sulfurtransferase UBA4\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O95396\",\"source\":\"UniProtKB\"}],\"value\":\"2.8.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Molybdopterin-synthase sulfurtransferase\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Adenylyltransferase and sulfurtransferase uba4\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Glycyl thioester intermediate; for adenylyltransferase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":188},\"start\":{\"modifier\":\"EXACT\",\"value\":188}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Cysteine persulfide intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00173\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":347},\"start\":{\"modifier\":\"EXACT\",\"value\":347}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":40},\"start\":{\"modifier\":\"EXACT\",\"value\":40}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":61},\"start\":{\"modifier\":\"EXACT\",\"value\":61}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":72},\"start\":{\"modifier\":\"EXACT\",\"value\":68}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":85},\"start\":{\"modifier\":\"EXACT\",\"value\":85}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":130},\"start\":{\"modifier\":\"EXACT\",\"value\":129}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":171},\"start\":{\"modifier\":\"EXACT\",\"value\":171}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":174},\"start\":{\"modifier\":\"EXACT\",\"value\":174}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":252},\"start\":{\"modifier\":\"EXACT\",\"value\":252}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_03049\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":255},\"start\":{\"modifier\":\"EXACT\",\"value\":255}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H1",
  "excerpt": "ID   UBA4_OGAPD              Reviewed;         389 AA.\nAC   W1QET1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Adenylyltransferase and sulfurtransferase uba4 {ECO:0000305};\nDE   AltName: Full=Ubiquitin-like protein activator 4 {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=Molybdopterin-synthase adenylyltransferase {ECO:0000305};\nDE              EC=2.7.7.80 {ECO:0000250|UniProtKB:O95396};\nDE     AltName: Full=Adenylyltransferase UBA4 {ECO:0000305};\nDE     AltName: Full=Sulfur carrier protein MOCS2A adenylyltransferase {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=Molybdopterin-synthase sulfurtransferase {ECO:0000305};\nDE              EC=2.8.1.11 {ECO:0000250|UniProtKB:O95396};\nDE     AltName: Full=Sulfur carrier protein MOCS2A sulfurtransferase {ECO:0000305};\nDE     AltName: Full=Sulfurtransferase UBA4 {ECO:0000305};\nGN   Name=UBA4 {ECO:0000305}; Synonyms=CNX4 {ECO:0000303|PubMed:33617956};\nGN   ORFNames=HPODL_00948 {ECO:0000312|EMBL:ESX00063.1};\nOS   Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL\nOS   Y-7560 / DL-1) (Yeast) (Hansenula polymorpha).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Pichiales; Pichiaceae; Ogataea.\nOX   NCBI_TaxID=871575 {ECO:0000312|Proteomes:UP000008673};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND PATHWAY.\nRX   PubMed=33617956; DOI=10.1016/j.ymben.2021.02.004;\nRA   Perli T., van der Vorm D.N.A., Wassink M., van den Broek M., Pronk J.T.,\nRA   Daran J.M.;\nRT   \"Engineering heterologous molybdenum-cofactor-biosynthesis and nitrate-\nRT   assimilation pathways enables nitrate utilization by Saccharomyces\nRT   cerevisiae.\";\nRL   Metab. Eng. 65:11-29(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        188\nFT                   /note=\"Glycyl thioester intermediate; for\nFT                   adenylyltransferase activity\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_03049\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        347\nFT                   /note=\"Cysteine persulfide intermediate\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00173\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 157-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         40\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_03049\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-163",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         61\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_03049\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 164-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         68..72\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_03049\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 168-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         85\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_03049\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-175",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         129..130\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_03049\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 176-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         171\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_03049\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 180-183",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         174\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_03049\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 184-187",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         252\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_03049\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 188-191",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         255\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_03049\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 192-195",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 145. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
