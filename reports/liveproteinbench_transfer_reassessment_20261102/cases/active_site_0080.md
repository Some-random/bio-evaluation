# active_site_0080

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0080.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 146 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGPANSEGTMFDAFSREVGDYYDQANELLRAMFTDNVHYGYWPDPSSIDPLAEAGERMTEQLYERLDVSAGHKVLDVGCGVGKPAAWLARKTGATVKGANVSRNQLEVARDRVRSEGLEDRVSFDLADAMHLPYADDSFDRIWAIESMIHMPDRDQVMREMARVLRPGGRLAIADIVVRGTLDDVATAVVEGFCTLSTARSLEHIDNYPALVEKAGLDLLELTDVSEQTRPTGPAVLPAFDVLLPTLGEEGVAQSKKAWGDMFDLPQYGYVLLTAGKP

[Multiple Choices]
A. Position 112 (Nucleophile)
B. Position 286 (Charge relay system)
C. Position 957 (Proton acceptor; for dehydratase activity)
D. Position 146 (Proton acceptor)
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

> The sequence-matched UniProt record annotates residue 146 as a proton acceptor active-site residue. This is a database annotation linked to literature, not independently verified here from the primary study.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a glycine-rich motif consistent with SAM-dependent methyltransferases, whose chemistry can require a residue that accepts a proton from the substrate. Position 146 is Glu, a plausible general base; position 112 is Arg, a much less plausible nucleophile for this chemistry. Positions 286 and 957 are outside the 278-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of SAM-dependent methyltransferase chemistry, together with the residue identities and lengths in the input, meaningfully favors D over the alternatives. This is a plausible inference, not proof that Glu146 performs that role in this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives distinguish a plausible acidic proton acceptor from an unlikely arginine nucleophile, while two listed positions exceed the sequence length.


### Important caveats

- The supporting active-site annotation is linked to literature, but the supplied excerpts do not independently establish the experimental basis or details of the study.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a glycine-rich motif consistent with SAM-dependent methyltransferases, whose chemistry can require a residue that accepts a proton from the substrate. Position 146 is Glu, a plausible general base; position 112 is Arg, a much less plausible nucleophile for this chemistry. Positions 286 and 957 are outside the 278-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of SAM-dependent methyltransferase chemistry, together with the residue identities and lengths in the input, meaningfully favors D over the alternatives. This is a plausible inference, not proof that Glu146 performs that role in this exact protein."
  },
  "case_id": "active_site_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 146 as a proton acceptor active-site residue. This is a database annotation linked to literature, not independently verified here from the primary study."
  },
  "important_caveats": [
    "The supporting active-site annotation is linked to literature, but the supplied excerpts do not independently establish the experimental basis or details of the study."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives distinguish a plausible acidic proton acceptor from an unlikely arginine nucleophile, while two listed positions exceed the sequence length."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 146 as a proton acceptor active-site residue. This is a database annotation linked to literature, not independently verified here from the primary study.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a glycine-rich motif consistent with SAM-dependent methyltransferases, whose chemistry can require a residue that accepts a proton from the substrate. Position 146 is Glu, a plausible general base; position 112 is Arg, a much less plausible nucleophile for this chemistry. Positions 286 and 957 are outside the 278-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of SAM-dependent methyltransferase chemistry, together with the residue identities and lengths in the input, meaningfully favors D over the alternatives. This is a plausible inference, not proof that Glu146 performs that role in this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives distinguish a plausible acidic proton acceptor from an unlikely arginine nucleophile, while two listed positions exceed the sequence length."
  },
  "important_caveats": [
    "The supporting active-site annotation is linked to literature, but the supplied excerpts do not independently establish the experimental basis or details of the study."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5/H4) explicitly lists position 146 as 'Active site: Proton acceptor' with evidence code ECO:0000305 from PubMed:26630077, which includes mutagenesis of GLU-146, HIS-150, and ASP-175. The residue at position 146 in the provided sequence is E (Glutamic acid), chemically consistent with a proton acceptor. The annotation is experimentally supported by the cited mutagenesis study.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C9](#evidence-c9), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent lines of transferable reasoning distinguish D from the alternatives: (1) The protein is 278 residues long, so options B (position 286) and C (position 957) reference non-existent positions and are eliminated by simple arithmetic on the input sequence. (2) Residue 112 is Arginine (R), which is not a recognized nucleophile in enzyme catalysis (nucleophiles are typically Ser, Cys, Thr, or Tyr), eliminating option A. (3) Residue 146 is Glutamic acid (E), a canonical proton acceptor in enzyme active sites. Additionally, the sequence contains a 'GCGVGKPAAW' motif (~positions 78-87) resembling the SAM-binding Rossmann-fold motif of methyltransferases, and methyltransferases commonly employ a Glu/Asp proton acceptor to deprotonate the substrate nucleophile, further supporting the proton-acceptor assignment at position 146.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B and C by noting the sequence is only 278 residues long. Between A and D, basic amino-acid chemistry (Arg is not a nucleophile; Glu is a classic proton acceptor) and recognition of methyltransferase SAM-binding motifs provide a concrete, transferable inference that selects D without needing the specific database annotation for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are impossible (positions exceed sequence length). Option A assigns 'Nucleophile' to Arginine, which contradicts standard enzyme chemistry. Only D (Glu-146 as proton acceptor) is chemically and structurally defensible.


### Important caveats

- The UniProt annotation evidence code ECO:0000305 indicates the assignment is based on the cited experimental study (PubMed:26630077), which included site-directed mutagenesis of Glu-146, His-150, and Asp-175.
- The protein is annotated as Methyltransferase GfsG (EC 2.1.1.-) from Streptomyces halstedii, but this identity was not provided to the evaluated model; the reasoning above relies only on the sequence and general knowledge.
- Options B and C are trivially eliminated by sequence length, making the effective choice between A and D, which is resolved by amino-acid chemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent lines of transferable reasoning distinguish D from the alternatives: (1) The protein is 278 residues long, so options B (position 286) and C (position 957) reference non-existent positions and are eliminated by simple arithmetic on the input sequence. (2) Residue 112 is Arginine (R), which is not a recognized nucleophile in enzyme catalysis (nucleophiles are typically Ser, Cys, Thr, or Tyr), eliminating option A. (3) Residue 146 is Glutamic acid (E), a canonical proton acceptor in enzyme active sites. Additionally, the sequence contains a 'GCGVGKPAAW' motif (~positions 78-87) resembling the SAM-binding Rossmann-fold motif of methyltransferases, and methyltransferases commonly employ a Glu/Asp proton acceptor to deprotonate the substrate nucleophile, further supporting the proton-acceptor assignment at position 146.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B and C by noting the sequence is only 278 residues long. Between A and D, basic amino-acid chemistry (Arg is not a nucleophile; Glu is a classic proton acceptor) and recognition of methyltransferase SAM-binding motifs provide a concrete, transferable inference that selects D without needing the specific database annotation for this protein."
  },
  "case_id": "active_site_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C9",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H4) explicitly lists position 146 as 'Active site: Proton acceptor' with evidence code ECO:0000305 from PubMed:26630077, which includes mutagenesis of GLU-146, HIS-150, and ASP-175. The residue at position 146 in the provided sequence is E (Glutamic acid), chemically consistent with a proton acceptor. The annotation is experimentally supported by the cited mutagenesis study."
  },
  "important_caveats": [
    "The UniProt annotation evidence code ECO:0000305 indicates the assignment is based on the cited experimental study (PubMed:26630077), which included site-directed mutagenesis of Glu-146, His-150, and Asp-175.",
    "The protein is annotated as Methyltransferase GfsG (EC 2.1.1.-) from Streptomyces halstedii, but this identity was not provided to the evaluated model; the reasoning above relies only on the sequence and general knowledge.",
    "Options B and C are trivially eliminated by sequence length, making the effective choice between A and D, which is resolved by amino-acid chemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are impossible (positions exceed sequence length). Option A assigns 'Nucleophile' to Arginine, which contradicts standard enzyme chemistry. Only D (Glu-146 as proton acceptor) is chemically and structurally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H4) explicitly lists position 146 as 'Active site: Proton acceptor' with evidence code ECO:0000305 from PubMed:26630077, which includes mutagenesis of GLU-146, HIS-150, and ASP-175. The residue at position 146 in the provided sequence is E (Glutamic acid), chemically consistent with a proton acceptor. The annotation is experimentally supported by the cited mutagenesis study.",
    "evidence_ids": ["C5", "H4", "C9", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent lines of transferable reasoning distinguish D from the alternatives: (1) The protein is 278 residues long, so options B (position 286) and C (position 957) reference non-existent positions and are eliminated by simple arithmetic on the input sequence. (2) Residue 112 is Arginine (R), which is not a recognized nucleophile in enzyme catalysis (nucleophiles are typically Ser, Cys, Thr, or Tyr), eliminating option A. (3) Residue 146 is Glutamic acid (E), a canonical proton acceptor in enzyme active sites. Additionally, the sequence contains a 'GCGVGKPAAW' motif (~positions 78-87) resembling the SAM-binding Rossmann-fold motif of methyltransferases, and methyltransferases commonly employ a Glu/Asp proton acceptor to deprotonate the substrate nucleophile, further supporting the proton-acceptor assignment at position 146.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B and C by noting the sequence is only 278 residues long. Between A and D, basic amino-acid chemistry (Arg is not a nucleophile; Glu is a classic proton acceptor) and recognition of methyltransferase SAM-binding motifs provide a concrete, transferable inference that selects D without needing the specific database annotation for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are impossible (positions exceed sequence length). Option A assigns 'Nucleophile' to Arginine, which contradicts standard enzyme chemistry. Only D (Glu-146 as proton acceptor) is chemically and structurally defensible."
  },
  "important_caveats": [
    "The UniProt annotation evidence code ECO:0000305 indicates the assignment is based on the cited experimental study (PubMed:26630077), which included site-directed mutagenesis of Glu-146, His-150, and Asp-175.",
    "The protein is annotated as Methyltransferase GfsG (EC 2.1.1.-) from Streptomyces halstedii, but this identity was not provided to the evaluated model; the reasoning above relies only on the sequence and general knowledge.",
    "Options B and C are trivially eliminated by sequence length, making the effective choice between A and D, which is resolved by amino-acid chemistry."
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
  "benchmark_sequence_length": 278,
  "benchmark_sequence_sha256": "446c919f832e44a2cb7c48c753dd503d70b078244fdd1258da6a8d172c0385a4",
  "current_entry_audit": {
    "entryVersion": 29,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "85a828a87c51921c250c7dfea7e360da93d816eafd568bf000dc2c70ce5c24c0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 278,
  "current_source_sequence_sha256": "446c919f832e44a2cb7c48c753dd503d70b078244fdd1258da6a8d172c0385a4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 28,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E0D208",
  "selected_historical_entry_version": 28,
  "selected_historical_record_sha256": "b7192a0f66b33ae1c0454812f81ce6522ffac94ec64111595e98e4c543e8a6ef",
  "selected_historical_source_sequence_length": 278,
  "selected_historical_source_sequence_sha256": "446c919f832e44a2cb7c48c753dd503d70b078244fdd1258da6a8d172c0385a4",
  "selected_historical_version": {
    "accession": "E0D208",
    "database": "Swiss-Prot",
    "entryVersion": 28,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "GFSG_STRHA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D208.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E0D208\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:56.118083+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85a828a87c51921c250c7dfea7e360da93d816eafd568bf000dc2c70ce5c24c0",
  "url": "https://rest.uniprot.org/uniprotkb/E0D208.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D208.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":29,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:56.118083+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85a828a87c51921c250c7dfea7e360da93d816eafd568bf000dc2c70ce5c24c0",
  "url": "https://rest.uniprot.org/uniprotkb/E0D208.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D208.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces halstedii\",\"taxonId\":1944}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:56.118083+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85a828a87c51921c250c7dfea7e360da93d816eafd568bf000dc2c70ce5c24c0",
  "url": "https://rest.uniprot.org/uniprotkb/E0D208.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D208.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26630077\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Methyltransferase GfsG\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:56.118083+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85a828a87c51921c250c7dfea7e360da93d816eafd568bf000dc2c70ce5c24c0",
  "url": "https://rest.uniprot.org/uniprotkb/E0D208.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D208.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26630077\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":146},\"start\":{\"modifier\":\"EXACT\",\"value\":146}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:27:56.118083+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85a828a87c51921c250c7dfea7e360da93d816eafd568bf000dc2c70ce5c24c0",
  "url": "https://rest.uniprot.org/uniprotkb/E0D208.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D208.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8KZ94\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":105},\"start\":{\"modifier\":\"EXACT\",\"value\":105}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:27:56.118083+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85a828a87c51921c250c7dfea7e360da93d816eafd568bf000dc2c70ce5c24c0",
  "url": "https://rest.uniprot.org/uniprotkb/E0D208.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D208.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8KZ94\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":129},\"start\":{\"modifier\":\"EXACT\",\"value\":128}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:27:56.118083+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85a828a87c51921c250c7dfea7e360da93d816eafd568bf000dc2c70ce5c24c0",
  "url": "https://rest.uniprot.org/uniprotkb/E0D208.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D208.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26630077\",\"source\":\"PubMed\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":150},\"start\":{\"modifier\":\"EXACT\",\"value\":150}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:27:56.118083+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85a828a87c51921c250c7dfea7e360da93d816eafd568bf000dc2c70ce5c24c0",
  "url": "https://rest.uniprot.org/uniprotkb/E0D208.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D208.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Kudo F.\",\"Kawamura K.\",\"Furuya T.\",\"Yamanishi H.\",\"Motegi A.\",\"Komatsubara A.\",\"Numakura M.\",\"Miyanaga A.\",\"Eguchi T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26630077\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.201500533\"}],\"citationType\":\"journal article\",\"firstPage\":\"233\",\"id\":\"26630077\",\"journal\":\"ChemBioChem\",\"lastPage\":\"238\",\"publicationDate\":\"2016\",\"title\":\"Parallel Post-Polyketide Synthase Modification Mechanism Involved in FD-891 Biosynthesis in Streptomyces graminofaciens A-8890.\",\"volume\":\"17\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"A-8890\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"POSSIBLE ACTIVE SITE\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF GLU-146; HIS-150 AND ASP-175\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:27:56.118083+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85a828a87c51921c250c7dfea7e360da93d816eafd568bf000dc2c70ce5c24c0",
  "url": "https://rest.uniprot.org/uniprotkb/E0D208.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H1",
  "excerpt": "ID   GFSG_STRHA              Reviewed;         278 AA.\nAC   E0D208;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2010, sequence version 1.\nDT   28-JAN-2026, entry version 28.\nDE   RecName: Full=Methyltransferase GfsG {ECO:0000305};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:26630077};\nGN   Name=gfsG {ECO:0000303|PubMed:20589823};\nOS   Streptomyces halstedii.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=1944;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:00.650050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b7192a0f66b33ae1c0454812f81ce6522ffac94ec64111595e98e4c543e8a6ef",
  "url": "https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAJ16473.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=A-8890;\nRX   PubMed=20589823; DOI=10.1002/cbic.201000214;\nRA   Kudo F., Motegi A., Mizoue K., Eguchi T.;\nRT   \"Cloning and characterization of the biosynthetic gene cluster of 16-\nRT   membered macrolide antibiotic FD-891: involvement of a dual functional\nRT   cytochrome P450 monooxygenase catalyzing epoxidation and hydroxylation.\";\nRL   ChemBioChem 11:1574-1582(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:00.650050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 13-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b7192a0f66b33ae1c0454812f81ce6522ffac94ec64111595e98e4c543e8a6ef",
  "url": "https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H3",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, POSSIBLE ACTIVE SITE, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, PATHWAY, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF GLU-146;\nRP   HIS-150 AND ASP-175.\nRC   STRAIN=A-8890;\nRX   PubMed=26630077; DOI=10.1002/cbic.201500533;\nRA   Kudo F., Kawamura K., Furuya T., Yamanishi H., Motegi A., Komatsubara A.,\nRA   Numakura M., Miyanaga A., Eguchi T.;\nRT   \"Parallel Post-Polyketide Synthase Modification Mechanism Involved in FD-\nRT   891 Biosynthesis in Streptomyces graminofaciens A-8890.\";\nRL   ChemBioChem 17:233-238(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:00.650050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b7192a0f66b33ae1c0454812f81ce6522ffac94ec64111595e98e4c543e8a6ef",
  "url": "https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        146\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000305|PubMed:26630077\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:00.650050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b7192a0f66b33ae1c0454812f81ce6522ffac94ec64111595e98e4c543e8a6ef",
  "url": "https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         105\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8KZ94\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:00.650050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b7192a0f66b33ae1c0454812f81ce6522ffac94ec64111595e98e4c543e8a6ef",
  "url": "https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         128..129\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8KZ94\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:00.650050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b7192a0f66b33ae1c0454812f81ce6522ffac94ec64111595e98e4c543e8a6ef",
  "url": "https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         150\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000305|PubMed:26630077\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:00.650050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b7192a0f66b33ae1c0454812f81ce6522ffac94ec64111595e98e4c543e8a6ef",
  "url": "https://rest.uniprot.org/unisave/E0D208?format=txt&versions=28"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 80. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
