# GO_molecular_function_0120

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0120.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — aspartate kinase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSASTPTAPYLEDLVRNSLDQNLPWVVQKYGGTSVGKSLDNITKIVGSYIDNGSKVAIVCSARSTQTKSLGTTNLLLQASREALQPAMSSSGDGRSGSMSGTATPFYPKRVGSGFFGKDQSTSMTSSVSSLSQLESQLGRSGSPSPFQSSSSRSPPRSPATPSQDSSISQEPAFHATVDLIKKGHLEAARASLKGGPLRDELEEEIERDCESLRSFLYAAQIIDEISPRSQDSIVGTGERLACKIVAAALRDRGVDSELVVLDNIVDASMSAASEAVSVDAGDQGVAQLGQEFYDQLSFRLGERLRECGQRVPVVTGYFGPVPGSLLAQIGRGYTDLCAALCAVGLKASELQVWKEVDGIFTADPRKVPSARLVPIITPDEAAELTYYGSEVIHPFTMEQVIRARIPIRIKNVENPSGAGTVIYPDVGFPRGLDTEPPKAERIVEGVDERMPTAVTIKDEIIVLNIHSNRKTLSHGFLARIFGTLDRAGVVVDLISTSEVHVSMAMQDFLNRKRLERLVKDLEKIGEVTVSKDMAILSLVGRNMRNAIGSAGLMFASLARAMINIEMISQGASEINISCVIENKDAIKALNVIHESCLSYPRSPATEMAGLQLQ

[Multiple Choices]
A. phosphorelay response regulator activity
B. aspartate kinase activity
C. lysine-acetylated histone binding
D. hydrolase activity
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

> The supplied sequence matches the annotated protein sequence. Its functional annotation reports aspartate phosphorylation and identifies the aspartokinase reaction (C5, C6); the cited functional evidence is experimental (ECO:0000269), while the GO annotation itself is assigned by sequence similarity (C7). These support choice B, though the catalytic-reaction annotation also cites evidence transferred from a homolog.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 615-residue soluble sequence has the profile of a large amino-acid kinase enzyme, with conserved kinase-like catalytic sequence features. Transferable knowledge of aspartokinase-family proteins makes choice B a credible match. The alternatives describe a phosphorelay response regulator, a specific histone-binding function, or hydrolysis; none is as consistent with an ATP-dependent amino-acid kinase family inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and comparison with the offered functions provide a meaningful basis to choose aspartate kinase activity without knowing this exact protein's database annotation. The sequence alone may not prove the precise substrate or reaction, but the alternatives make the family-level inference discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, aspartate kinase activity is the clear functional match; the broad hydrolase option does not describe the annotated phosphorylation reaction.


### Important caveats

- The reviewer-only source record matches the supplied sequence, but its annotations were not part of the original model input.
- The GO annotation is similarity-based; the source's functional description cites experimental evidence, which was not independently checked against the primary paper here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 615-residue soluble sequence has the profile of a large amino-acid kinase enzyme, with conserved kinase-like catalytic sequence features. Transferable knowledge of aspartokinase-family proteins makes choice B a credible match. The alternatives describe a phosphorelay response regulator, a specific histone-binding function, or hydrolysis; none is as consistent with an ATP-dependent amino-acid kinase family inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and comparison with the offered functions provide a meaningful basis to choose aspartate kinase activity without knowing this exact protein's database annotation. The sequence alone may not prove the precise substrate or reaction, but the alternatives make the family-level inference discriminating."
  },
  "case_id": "GO_molecular_function_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein sequence. Its functional annotation reports aspartate phosphorylation and identifies the aspartokinase reaction (C5, C6); the cited functional evidence is experimental (ECO:0000269), while the GO annotation itself is assigned by sequence similarity (C7). These support choice B, though the catalytic-reaction annotation also cites evidence transferred from a homolog."
  },
  "important_caveats": [
    "The reviewer-only source record matches the supplied sequence, but its annotations were not part of the original model input.",
    "The GO annotation is similarity-based; the source's functional description cites experimental evidence, which was not independently checked against the primary paper here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, aspartate kinase activity is the clear functional match; the broad hydrolase option does not describe the annotated phosphorylation reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein sequence. Its functional annotation reports aspartate phosphorylation and identifies the aspartokinase reaction (C5, C6); the cited functional evidence is experimental (ECO:0000269), while the GO annotation itself is assigned by sequence similarity (C7). These support choice B, though the catalytic-reaction annotation also cites evidence transferred from a homolog.",
    "evidence_ids": ["C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 615-residue soluble sequence has the profile of a large amino-acid kinase enzyme, with conserved kinase-like catalytic sequence features. Transferable knowledge of aspartokinase-family proteins makes choice B a credible match. The alternatives describe a phosphorelay response regulator, a specific histone-binding function, or hydrolysis; none is as consistent with an ATP-dependent amino-acid kinase family inference.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and comparison with the offered functions provide a meaningful basis to choose aspartate kinase activity without knowing this exact protein's database annotation. The sequence alone may not prove the precise substrate or reaction, but the alternatives make the family-level inference discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, aspartate kinase activity is the clear functional match; the broad hydrolase option does not describe the annotated phosphorylation reaction."
  },
  "important_caveats": [
    "The reviewer-only source record matches the supplied sequence, but its annotations were not part of the original model input.",
    "The GO annotation is similarity-based; the source's functional description cites experimental evidence, which was not independently checked against the primary paper here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry J9VS37 (AK_CRYN9) annotates this protein as Aspartokinase (EC 2.7.2.4) with GO:0004072 (aspartate kinase activity). The FUNCTION comment cites experimental evidence (ECO:0000269, PubMed:18757810, Kingsbury & McCusker 2008) demonstrating phosphorylation of aspartate. The catalytic reaction L-aspartate + ATP = 4-phospho-L-aspartate + ADP is confirmed. The EC assignment itself is by similarity (ECO:0000250|P10869), but the experimental function annotation independently supports the kinase activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains 'GGTSVGKS', a Walker A / P-loop motif (GxxxxGK&#91;S/T&#93;) characteristic of ATP-binding kinases. The overall architecture shows a regulatory N-terminal domain followed by a catalytic domain with additional kinase-conserved motifs (e.g., the 'PIITPDEAAELTYYGSEVIHPFTMEQVIRARIPIRIKN' region resembles the amino acid kinase superfamily catalytic fold). Among the four choices: (A) phosphorelay response regulators require a ~120-aa CheY-like receiver domain with a conserved phospho-acceptor Asp and specific Thr/Ser/Lys triad — absent here; (C) lysine-acetylated histone binding implies a bromodomain (~110 aa, four-helix bundle with conserved Asn/Tyr) — no such motif is present; (D) hydrolase activity involves water-mediated bond cleavage with motifs like Ser-His-Asp triads or metalloprotease HxxH — inconsistent with the observed P-loop/ATP-binding architecture. The P-loop and kinase-fold features positively identify a transferase/kinase, and among the four options only B is a kinase. While distinguishing aspartate kinase from other amino acid kinases (e.g., N-acetylglutamate kinase) might require additional specificity, the question only requires choosing among these four very different functional classes, for which the kinase motifs are decisive.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P-loop motif and amino acid kinase–like catalytic architecture visible in the sequence provide a concrete, transferable inference that distinguishes option B (the only kinase among the choices) from options A, C, and D. Family-level knowledge of amino acid kinases (P-loop ATP binding, two-domain architecture with regulatory + catalytic regions) supports this without needing the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular function classes (response regulator, kinase, binding protein, hydrolase). The P-loop/kinase motifs clearly point to a kinase, making B the only defensible choice among the offered alternatives. No two options are functionally overlapping or ambiguous given the sequence features.


### Important caveats

- The EC 2.7.2.4 assignment in UniProt is by similarity to P10869 (E. coli aspartokinase), but the FUNCTION annotation is supported by experimental evidence (PubMed:18757810) showing aspartate phosphorylation in Cryptococcus neoformans.
- The P-loop motif 'GGTSVGKS' is a general Walker A signature shared across many NTP-binding proteins; its specificity for amino acid kinase over other kinase families relies on the broader domain architecture context rather than the motif alone.
- The sequence is 615 aa, consistent with fungal aspartokinases which often have an N-terminal ACT/regulatory domain fused to the catalytic domain.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains 'GGTSVGKS', a Walker A / P-loop motif (GxxxxGK[S/T]) characteristic of ATP-binding kinases. The overall architecture shows a regulatory N-terminal domain followed by a catalytic domain with additional kinase-conserved motifs (e.g., the 'PIITPDEAAELTYYGSEVIHPFTMEQVIRARIPIRIKN' region resembles the amino acid kinase superfamily catalytic fold). Among the four choices: (A) phosphorelay response regulators require a ~120-aa CheY-like receiver domain with a conserved phospho-acceptor Asp and specific Thr/Ser/Lys triad — absent here; (C) lysine-acetylated histone binding implies a bromodomain (~110 aa, four-helix bundle with conserved Asn/Tyr) — no such motif is present; (D) hydrolase activity involves water-mediated bond cleavage with motifs like Ser-His-Asp triads or metalloprotease HxxH — inconsistent with the observed P-loop/ATP-binding architecture. The P-loop and kinase-fold features positively identify a transferase/kinase, and among the four options only B is a kinase. While distinguishing aspartate kinase from other amino acid kinases (e.g., N-acetylglutamate kinase) might require additional specificity, the question only requires choosing among these four very different functional classes, for which the kinase motifs are decisive.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P-loop motif and amino acid kinase–like catalytic architecture visible in the sequence provide a concrete, transferable inference that distinguishes option B (the only kinase among the choices) from options A, C, and D. Family-level knowledge of amino acid kinases (P-loop ATP binding, two-domain architecture with regulatory + catalytic regions) supports this without needing the specific UniProt annotation for this exact protein."
  },
  "case_id": "GO_molecular_function_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry J9VS37 (AK_CRYN9) annotates this protein as Aspartokinase (EC 2.7.2.4) with GO:0004072 (aspartate kinase activity). The FUNCTION comment cites experimental evidence (ECO:0000269, PubMed:18757810, Kingsbury & McCusker 2008) demonstrating phosphorylation of aspartate. The catalytic reaction L-aspartate + ATP = 4-phospho-L-aspartate + ADP is confirmed. The EC assignment itself is by similarity (ECO:0000250|P10869), but the experimental function annotation independently supports the kinase activity."
  },
  "important_caveats": [
    "The EC 2.7.2.4 assignment in UniProt is by similarity to P10869 (E. coli aspartokinase), but the FUNCTION annotation is supported by experimental evidence (PubMed:18757810) showing aspartate phosphorylation in Cryptococcus neoformans.",
    "The P-loop motif 'GGTSVGKS' is a general Walker A signature shared across many NTP-binding proteins; its specificity for amino acid kinase over other kinase families relies on the broader domain architecture context rather than the motif alone.",
    "The sequence is 615 aa, consistent with fungal aspartokinases which often have an N-terminal ACT/regulatory domain fused to the catalytic domain."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular function classes (response regulator, kinase, binding protein, hydrolase). The P-loop/kinase motifs clearly point to a kinase, making B the only defensible choice among the offered alternatives. No two options are functionally overlapping or ambiguous given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry J9VS37 (AK_CRYN9) annotates this protein as Aspartokinase (EC 2.7.2.4) with GO:0004072 (aspartate kinase activity). The FUNCTION comment cites experimental evidence (ECO:0000269, PubMed:18757810, Kingsbury & McCusker 2008) demonstrating phosphorylation of aspartate. The catalytic reaction L-aspartate + ATP = 4-phospho-L-aspartate + ADP is confirmed. The EC assignment itself is by similarity (ECO:0000250|P10869), but the experimental function annotation independently supports the kinase activity.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains 'GGTSVGKS', a Walker A / P-loop motif (GxxxxGK[S/T]) characteristic of ATP-binding kinases. The overall architecture shows a regulatory N-terminal domain followed by a catalytic domain with additional kinase-conserved motifs (e.g., the 'PIITPDEAAELTYYGSEVIHPFTMEQVIRARIPIRIKN' region resembles the amino acid kinase superfamily catalytic fold). Among the four choices: (A) phosphorelay response regulators require a ~120-aa CheY-like receiver domain with a conserved phospho-acceptor Asp and specific Thr/Ser/Lys triad — absent here; (C) lysine-acetylated histone binding implies a bromodomain (~110 aa, four-helix bundle with conserved Asn/Tyr) — no such motif is present; (D) hydrolase activity involves water-mediated bond cleavage with motifs like Ser-His-Asp triads or metalloprotease HxxH — inconsistent with the observed P-loop/ATP-binding architecture. The P-loop and kinase-fold features positively identify a transferase/kinase, and among the four options only B is a kinase. While distinguishing aspartate kinase from other amino acid kinases (e.g., N-acetylglutamate kinase) might require additional specificity, the question only requires choosing among these four very different functional classes, for which the kinase motifs are decisive.",
    "missing_item_specific_fact": "",
    "reason": "The P-loop motif and amino acid kinase–like catalytic architecture visible in the sequence provide a concrete, transferable inference that distinguishes option B (the only kinase among the choices) from options A, C, and D. Family-level knowledge of amino acid kinases (P-loop ATP binding, two-domain architecture with regulatory + catalytic regions) supports this without needing the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular function classes (response regulator, kinase, binding protein, hydrolase). The P-loop/kinase motifs clearly point to a kinase, making B the only defensible choice among the offered alternatives. No two options are functionally overlapping or ambiguous given the sequence features."
  },
  "important_caveats": [
    "The EC 2.7.2.4 assignment in UniProt is by similarity to P10869 (E. coli aspartokinase), but the FUNCTION annotation is supported by experimental evidence (PubMed:18757810) showing aspartate phosphorylation in Cryptococcus neoformans.",
    "The P-loop motif 'GGTSVGKS' is a general Walker A signature shared across many NTP-binding proteins; its specificity for amino acid kinase over other kinase families relies on the broader domain architecture context rather than the motif alone.",
    "The sequence is 615 aa, consistent with fungal aspartokinases which often have an N-terminal ACT/regulatory domain fused to the catalytic domain."
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
  "benchmark_sequence_length": 615,
  "benchmark_sequence_sha256": "536d54264e6ff3f5d7f7604b6c1376b560b69f4005ef267570182f96dffb6a42",
  "current_entry_audit": {
    "entryVersion": 68,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 615,
  "current_source_sequence_sha256": "536d54264e6ff3f5d7f7604b6c1376b560b69f4005ef267570182f96dffb6a42",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 66,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VS37",
  "selected_historical_entry_version": 66,
  "selected_historical_record_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "selected_historical_source_sequence_length": 615,
  "selected_historical_source_sequence_sha256": "536d54264e6ff3f5d7f7604b6c1376b560b69f4005ef267570182f96dffb6a42",
  "selected_historical_version": {
    "accession": "J9VS37",
    "database": "Swiss-Prot",
    "entryVersion": 66,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AK_CRYN9",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VS37\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":68,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.2.4\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartokinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18757810\",\"source\":\"PubMed\"}],\"value\":\"Phosphorylates aspartate, the first step in the biosynthesis of amino acids that derive from aspartate (the aspartate family of amino acids), including methioinine and threonine, the latter of which is a precursor to isoleucine\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23777\"}}],\"reaction\":{\"ecNumber\":\"2.7.2.4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"name\":\"L-aspartate + ATP = 4-phospho-L-aspartate + ADP\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23776\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29991\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004072\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:aspartate kinase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Kingsbury J.M.\",\"McCusker J.H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18757810\"},{\"database\":\"DOI\",\"id\":\"10.1099/mic.0.2008/019729-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"2767\",\"id\":\"18757810\",\"journal\":\"Microbiology\",\"lastPage\":\"2775\",\"publicationDate\":\"2008\",\"title\":\"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\",\"volume\":\"154\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H1",
  "excerpt": "ID   AK_CRYN9                Reviewed;         615 AA.\nAC   J9VS37;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 66.\nDE   RecName: Full=Aspartokinase {ECO:0000305};\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\nGN   Name=HOM3 {ECO:0000303|PubMed:18757810};\nGN   ORFNames=CNAG_04347 {ECO:0000312|EMBL:AFR97078.1};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;\nRA   Kingsbury J.M., McCusker J.H.;\nRT   \"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\";\nRL   Microbiology 154:2767-2775(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Phosphorylates aspartate, the first step in the biosynthesis\nCC       of amino acids that derive from aspartate (the aspartate family of\nCC       amino acids), including methioinine and threonine, the latter of which\nCC       is a precursor to isoleucine. {ECO:0000269|PubMed:18757810}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;\nCC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0004072; F:aspartate kinase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000156\nname: phosphorelay response regulator activity\nnamespace: molecular_function\ndef: \"Responds to a phosphorelay sensor to initiate a change in cell state or activity. The activity of the response regulator is regulated by transfer of a phosphate from a histidine residue in the sensor, to an aspartate residue in the response regulator. Many but not all response regulators act as transcriptional regulators to elicit a response.\" [GOC:bf, PMID:10966457, PMID:11842140]\nsynonym: \"two-component response regulator activity\" NARROW []\nis_a: GO:0060089 ! molecular transducer activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000156",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1561-1568",
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
  "excerpt": "[Term]\nid: GO:0004072\nname: aspartate kinase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: L-aspartate + ATP = 4-phospho-L-aspartate + ADP + H+.\" [EC:2.7.2.4, RHEA:23776]\nsynonym: \"aspartic kinase activity\" RELATED [EC:2.7.2.4]\nsynonym: \"aspartokinase activity\" RELATED [EC:2.7.2.4]\nsynonym: \"ATP:L-aspartate 4-phosphotransferase activity\" RELATED [EC:2.7.2.4]\nsynonym: \"beta-aspartokinase activity\" RELATED [EC:2.7.2.4]\nxref: EC:2.7.2.4\nxref: KEGG_REACTION:R00480\nxref: MetaCyc:ASPARTATEKIN-RXN\nxref: RHEA:23776\nis_a: GO:0016774 ! phosphotransferase activity, carboxyl group as acceptor\nis_a: GO:0019202 ! amino acid kinase activity\nproperty_value: skos:exactMatch EC:2.7.2.4\nproperty_value: skos:exactMatch RHEA:23776\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004072",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 34816-34833",
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
  "excerpt": "[Term]\nid: GO:0016787\nname: hydrolase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of various bonds, e.g. C-O, C-N, C-C, phosphoric anhydride bonds, etc.\" [ISBN:0198506732]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nxref: EC:3.-.-.-\nxref: Reactome:R-HSA-1236938 \"Partial proteolysis of antigen in phagolysosomes\"\nxref: Reactome:R-HSA-2029475 \"Production of AA by iPLA2 upon FCGR activation\"\nxref: Reactome:R-HSA-5694583 \"ABHD4 hydrolyses NAPE\"\nxref: Reactome:R-HSA-5695964 \"ABHD14B hydrolyses PNPB\"\nxref: Reactome:R-HSA-6786190 \"CMBL hydrolyses OM to OLMS\"\nxref: Reactome:R-HSA-6788295 \"HDHD1:Mg2+ dephosphorylates PURIDP\"\nxref: Reactome:R-HSA-8938314 \"ENPPs hydrolyse CoA-SH to PPANT, PAP\"\nxref: Reactome:R-HSA-8952137 \"Phospholipid phosphatase 6 hydrolyses Presqualene diphosphate to presqualene monophosphate\"\nxref: Reactome:R-HSA-9942295 \"QNG1 hydrolyzes queuosine 5'-monophosphate yielding queuine and ribose 5'-monophosphate\"\nis_a: GO:0003824 ! catalytic activity\nproperty_value: skos:exactMatch EC:3.-.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016787",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 130166-130193",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 120. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
