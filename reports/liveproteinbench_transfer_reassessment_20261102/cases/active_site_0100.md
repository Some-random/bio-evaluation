# active_site_0100

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0100.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 221 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVASKIAWKFILPNCFKAKNDRNILPSETKIIQICKQINSDHHHSRLAISDISTDSRSVFISLDDLSSNAIIGSNLHIFTYAELKIITSKFSSANFLGKGGFGPVHKGFIDDKIKPGLKAQPVAVKLLDLDGNQGHQEWLTEVVFLGQLRHPHLVKLIGYCWEEEQRLLVYEYMARGNLENHLFSRYSSCLPWSTRIKIAVGAAKGLAFLHGEEKPVIYRDFKASNILLDSDYKAKLSDFGLAKDGPEGDDTHVSTRVMGTHGYAAPEYIMTGHLTSKSDVYSFGVVLLELITGRPAMDKNRPIRERNLVDWARPMLRDFHKLDRIMDPRLEGQYSTEGAKKVAALAYQCLSHQPRSRPTMSNVVKSLEPISELTDIPIGPFVYVVPSSECDKELEIGALKSKLDEEKKMNVNEDEQKGARRHGHRHKHRPKSSAAAAAVYSDTHMQNFALSHERTNKKHILK

[Multiple Choices]
A. Position 221 (Proton acceptor)
B. Position 981 (Proton acceptor; for dehydratase activity)
C. Position 176 (Proton donor/acceptor)
D. Position 2059 (For beta-ketoacyl synthase 2 activity)
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

> The sequence matches the annotated 463-residue kinase, and the matched UniProt record identifies position 221 as an active-site proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has kinase-family features, including an ATP-binding glycine-rich region and a catalytic-loop-like YRDF motif; position 221 is the Asp in that motif. In protein kinases, the catalytic-loop Asp can act as a proton-accepting catalytic residue. This supports A over C, while the positions in B and D exceed the 463-residue sequence length.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable kinase-family knowledge and the sequence motif provide a meaningful basis for distinguishing the offered answer, even though they do not independently establish experimental activity for this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A matches the relevant sequence position and kinase catalytic-residue inference among the offered choices.


### Important caveats

- The supporting database active-site annotation is computationally inferred rather than shown here to be experimentally validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has kinase-family features, including an ATP-binding glycine-rich region and a catalytic-loop-like YRDF motif; position 221 is the Asp in that motif. In protein kinases, the catalytic-loop Asp can act as a proton-accepting catalytic residue. This supports A over C, while the positions in B and D exceed the 463-residue sequence length.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase-family knowledge and the sequence motif provide a meaningful basis for distinguishing the offered answer, even though they do not independently establish experimental activity for this particular protein."
  },
  "case_id": "active_site_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated 463-residue kinase, and the matched UniProt record identifies position 221 as an active-site proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental evidence."
  },
  "important_caveats": [
    "The supporting database active-site annotation is computationally inferred rather than shown here to be experimentally validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the relevant sequence position and kinase catalytic-residue inference among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated 463-residue kinase, and the matched UniProt record identifies position 221 as an active-site proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental evidence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has kinase-family features, including an ATP-binding glycine-rich region and a catalytic-loop-like YRDF motif; position 221 is the Asp in that motif. In protein kinases, the catalytic-loop Asp can act as a proton-accepting catalytic residue. This supports A over C, while the positions in B and D exceed the 463-residue sequence length.",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase-family knowledge and the sequence motif provide a meaningful basis for distinguishing the offered answer, even though they do not independently establish experimental activity for this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the relevant sequence position and kinase catalytic-residue inference among the offered choices."
  },
  "important_caveats": [
    "The supporting database active-site annotation is computationally inferred rather than shown here to be experimentally validated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) explicitly records position 221 as an 'Active site' with description 'Proton acceptor', supported by PROSITE-ProRule pattern matches (PRU00159, PRU10027). The sequence at position 221 is D (Aspartate), located in the catalytic loop of a protein kinase domain (between the β3 lysine at ~205 and the DFG motif at 239-241). The annotation is computational (PROSITE-ProRule pattern-based), not experimentally validated, but is the standard method for assigning the catalytic aspartate in kinases. The functional description 'Proton acceptor' matches the established mechanism where the catalytic loop aspartate deprotonates the substrate hydroxyl during phosphotransfer.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options B (position 981) and D (position 2059) are immediately eliminated because they reference positions far exceeding the 463-residue protein length. Between A (position 221) and C (position 176), a model can recognize this as a protein kinase from conserved domain architecture: the glycine-rich loop (~GxGxxG at ~97-105), the β3 lysine (K at ~205 in 'AAKGL'), the DFG motif (D239-F240-G241), and the APE motif (~266-268). The catalytic loop lies between the β3 lysine and DFG; position 221 contains D (Aspartate) in a 'YRD' context (a variant of the canonical HRD catalytic motif), while position 176 is R (Arginine), which is not a catalytic residue in kinases. Knowledge from hundreds of characterized protein kinases establishes that the catalytic-loop aspartate serves as the proton acceptor (general base) during phosphoryl transfer. This family-level inference reliably distinguishes A from C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The protein kinase catalytic mechanism and domain architecture are among the most thoroughly characterized in biology. Recognizing kinase motifs (Gly-rich loop, VAIK, HRD/variant, DFG, APE) from sequence and knowing the catalytic aspartate's role as proton acceptor is standard transferable knowledge applicable across the entire kinase superfamily. The elimination of B and D by sequence length is trivial. The distinction between A and C relies on identifying the correct catalytic-loop aspartate versus a non-catalytic arginine.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are impossible (positions exceed protein length). Option C places a 'proton donor/acceptor' at an arginine residue, which is not a catalytic residue in protein kinases. Only option A correctly identifies the catalytic-loop aspartate as the proton acceptor.


### Important caveats

- The UniProt annotation is computational (PROSITE-ProRule pattern matching, ECO:0000255), not experimentally validated. However, the kinase catalytic mechanism is well-established across the superfamily.
- The catalytic loop motif here is 'YRD' rather than the canonical 'HRD'; this is a recognized variant in some kinase subfamilies, and the aspartate retains its catalytic role.
- Options B and D reference positions (981, 2059) far beyond the 463-residue sequence, making them trivially eliminable and reducing the question to a binary A-vs-C choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (position 981) and D (position 2059) are immediately eliminated because they reference positions far exceeding the 463-residue protein length. Between A (position 221) and C (position 176), a model can recognize this as a protein kinase from conserved domain architecture: the glycine-rich loop (~GxGxxG at ~97-105), the β3 lysine (K at ~205 in 'AAKGL'), the DFG motif (D239-F240-G241), and the APE motif (~266-268). The catalytic loop lies between the β3 lysine and DFG; position 221 contains D (Aspartate) in a 'YRD' context (a variant of the canonical HRD catalytic motif), while position 176 is R (Arginine), which is not a catalytic residue in kinases. Knowledge from hundreds of characterized protein kinases establishes that the catalytic-loop aspartate serves as the proton acceptor (general base) during phosphoryl transfer. This family-level inference reliably distinguishes A from C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The protein kinase catalytic mechanism and domain architecture are among the most thoroughly characterized in biology. Recognizing kinase motifs (Gly-rich loop, VAIK, HRD/variant, DFG, APE) from sequence and knowing the catalytic aspartate's role as proton acceptor is standard transferable knowledge applicable across the entire kinase superfamily. The elimination of B and D by sequence length is trivial. The distinction between A and C relies on identifying the correct catalytic-loop aspartate versus a non-catalytic arginine."
  },
  "case_id": "active_site_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly records position 221 as an 'Active site' with description 'Proton acceptor', supported by PROSITE-ProRule pattern matches (PRU00159, PRU10027). The sequence at position 221 is D (Aspartate), located in the catalytic loop of a protein kinase domain (between the β3 lysine at ~205 and the DFG motif at 239-241). The annotation is computational (PROSITE-ProRule pattern-based), not experimentally validated, but is the standard method for assigning the catalytic aspartate in kinases. The functional description 'Proton acceptor' matches the established mechanism where the catalytic loop aspartate deprotonates the substrate hydroxyl during phosphotransfer."
  },
  "important_caveats": [
    "The UniProt annotation is computational (PROSITE-ProRule pattern matching, ECO:0000255), not experimentally validated. However, the kinase catalytic mechanism is well-established across the superfamily.",
    "The catalytic loop motif here is 'YRD' rather than the canonical 'HRD'; this is a recognized variant in some kinase subfamilies, and the aspartate retains its catalytic role.",
    "Options B and D reference positions (981, 2059) far beyond the 463-residue sequence, making them trivially eliminable and reducing the question to a binary A-vs-C choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are impossible (positions exceed protein length). Option C places a 'proton donor/acceptor' at an arginine residue, which is not a catalytic residue in protein kinases. Only option A correctly identifies the catalytic-loop aspartate as the proton acceptor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly records position 221 as an 'Active site' with description 'Proton acceptor', supported by PROSITE-ProRule pattern matches (PRU00159, PRU10027). The sequence at position 221 is D (Aspartate), located in the catalytic loop of a protein kinase domain (between the β3 lysine at ~205 and the DFG motif at 239-241). The annotation is computational (PROSITE-ProRule pattern-based), not experimentally validated, but is the standard method for assigning the catalytic aspartate in kinases. The functional description 'Proton acceptor' matches the established mechanism where the catalytic loop aspartate deprotonates the substrate hydroxyl during phosphotransfer.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options B (position 981) and D (position 2059) are immediately eliminated because they reference positions far exceeding the 463-residue protein length. Between A (position 221) and C (position 176), a model can recognize this as a protein kinase from conserved domain architecture: the glycine-rich loop (~GxGxxG at ~97-105), the β3 lysine (K at ~205 in 'AAKGL'), the DFG motif (D239-F240-G241), and the APE motif (~266-268). The catalytic loop lies between the β3 lysine and DFG; position 221 contains D (Aspartate) in a 'YRD' context (a variant of the canonical HRD catalytic motif), while position 176 is R (Arginine), which is not a catalytic residue in kinases. Knowledge from hundreds of characterized protein kinases establishes that the catalytic-loop aspartate serves as the proton acceptor (general base) during phosphoryl transfer. This family-level inference reliably distinguishes A from C.",
    "missing_item_specific_fact": "",
    "reason": "The protein kinase catalytic mechanism and domain architecture are among the most thoroughly characterized in biology. Recognizing kinase motifs (Gly-rich loop, VAIK, HRD/variant, DFG, APE) from sequence and knowing the catalytic aspartate's role as proton acceptor is standard transferable knowledge applicable across the entire kinase superfamily. The elimination of B and D by sequence length is trivial. The distinction between A and C relies on identifying the correct catalytic-loop aspartate versus a non-catalytic arginine."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are impossible (positions exceed protein length). Option C places a 'proton donor/acceptor' at an arginine residue, which is not a catalytic residue in protein kinases. Only option A correctly identifies the catalytic-loop aspartate as the proton acceptor."
  },
  "important_caveats": [
    "The UniProt annotation is computational (PROSITE-ProRule pattern matching, ECO:0000255), not experimentally validated. However, the kinase catalytic mechanism is well-established across the superfamily.",
    "The catalytic loop motif here is 'YRD' rather than the canonical 'HRD'; this is a recognized variant in some kinase subfamilies, and the aspartate retains its catalytic role.",
    "Options B and D reference positions (981, 2059) far beyond the 463-residue sequence, making them trivially eliminable and reducing the question to a binary A-vs-C choice."
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
  "benchmark_sequence_length": 463,
  "benchmark_sequence_sha256": "cbfd347d07189b0822d33d2796743f860cc8f31b600bad993a5e1f6bcfca7a17",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 463,
  "current_source_sequence_sha256": "cbfd347d07189b0822d33d2796743f860cc8f31b600bad993a5e1f6bcfca7a17",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXJ0",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "dfc72a9fe284e8d09ff624e621a36800a15b634cee3411254b16ccf4f17ccdc8",
  "selected_historical_source_sequence_length": 463,
  "selected_historical_source_sequence_sha256": "cbfd347d07189b0822d33d2796743f860cc8f31b600bad993a5e1f6bcfca7a17",
  "selected_historical_version": {
    "accession": "P0DXJ0",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIR_NICBE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:15.004320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:15.004320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Solanales\",\"Solanaceae\",\"Nicotianoideae\",\"Nicotianeae\",\"Nicotiana\"],\"scientificName\":\"Nicotiana benthamiana\",\"taxonId\":4100}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:15.004320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10027\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"2.7.11.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39488762\",\"source\":\"PubMed\"}],\"value\":\"EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39488762\",\"source\":\"PubMed\"}],\"value\":\"NbEIR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:15.004320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00159\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10027\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":221},\"start\":{\"modifier\":\"EXACT\",\"value\":221}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:15.004320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00159\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":105},\"start\":{\"modifier\":\"EXACT\",\"value\":97}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:15.004320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00159\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":126},\"start\":{\"modifier\":\"EXACT\",\"value\":126}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:25:15.004320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Sun L.\",\"Li X.\",\"Zhong J.\",\"Wang Y.\",\"Li B.\",\"Ye Z.\",\"Zhang J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39488762\"},{\"database\":\"DOI\",\"id\":\"10.1002/advs.202407787\"}],\"citationType\":\"journal article\",\"firstPage\":\"e2407787\",\"id\":\"39488762\",\"journal\":\"Adv. Sci.\",\"lastPage\":\"e2407787\",\"publicationDate\":\"2025\",\"title\":\"Recognition of a fungal effector potentiates pathogen-associated molecular pattern-triggered immunity in cotton.\",\"volume\":\"12\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"INTERACTION WITH V.DAHLIAE EPD1\",\"INDUCTION BY V.DAHLIAE EPD1\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:15.004320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   EIR_NICBE               Reviewed;         463 AA.\nAC   P0DXJ0;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase {ECO:0000303|PubMed:39488762};\nDE            Short=NbEIR {ECO:0000303|PubMed:39488762};\nDE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};\nGN   Name=EIR {ECO:0000303|PubMed:39488762};\nGN   ORFNames=NbS00058880g0009 {ECO:0000303|PubMed:39488762};\nOS   Nicotiana benthamiana.\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Solanales; Solanaceae; Nicotianoideae; Nicotianeae;\nOC   Nicotiana.\nOX   NCBI_TaxID=4100;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:19.546423+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dfc72a9fe284e8d09ff624e621a36800a15b634cee3411254b16ccf4f17ccdc8",
  "url": "https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, INTERACTION WITH V.DAHLIAE EPD1, AND\nRP   INDUCTION BY V.DAHLIAE EPD1.\nRX   PubMed=39488762; DOI=10.1002/advs.202407787;\nRA   Sun L., Li X., Zhong J., Wang Y., Li B., Ye Z., Zhang J.;\nRT   \"Recognition of a fungal effector potentiates pathogen-associated molecular\nRT   pattern-triggered immunity in cotton.\";\nRL   Adv. Sci. 12:e2407787-e2407787(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:19.546423+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dfc72a9fe284e8d09ff624e621a36800a15b634cee3411254b16ccf4f17ccdc8",
  "url": "https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        221\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00159,\nFT                   ECO:0000255|PROSITE-ProRule:PRU10027\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:19.546423+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dfc72a9fe284e8d09ff624e621a36800a15b634cee3411254b16ccf4f17ccdc8",
  "url": "https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         97..105\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00159\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:19.546423+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dfc72a9fe284e8d09ff624e621a36800a15b634cee3411254b16ccf4f17ccdc8",
  "url": "https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         126\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00159\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:19.546423+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dfc72a9fe284e8d09ff624e621a36800a15b634cee3411254b16ccf4f17ccdc8",
  "url": "https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 100. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
