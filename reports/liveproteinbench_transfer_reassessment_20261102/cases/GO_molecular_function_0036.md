# GO_molecular_function_0036

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0036.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — cadmium ion transmembrane transporter activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MHQDNSMRRAINQSRNGGSDSCDINNDREHDNINRNSYINNFHIENINSDKNEQSYIYCSDRAQVTDSILGNRKYTHEENINSTEMFSRTNYEYSNKNNVDIEMYNISNNNFYNGNNNGHSNDIIDYINNNNVNKDLSNTSNNADINTYIKKLTSNQSTAYCDGKGYNESANGSNFDINFRDVIKNNNNKNYKNNNHVPDDMLELGDRSFDSSFYIHNNVEEIDTERSNRLSFMSKLKMYFNYFGPGWIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS

[Multiple Choices]
A. dynein complex binding
B. beta-glucuronidase activity
C. cadmium ion transmembrane transporter activity
D. D-lactate dehydrogenase (cytochrome) activity
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

> The sequence-matched UniProt record assigns the exact cadmium-transporter GO term, but as an IEA:TreeGrafter computational annotation, not direct experimental evidence. The cited experimental function and reaction concern iron transport, so cadmium transport is supported at the annotation/inference level but is not independently established experimentally by these excerpts.

Citations as saved: [C7](#evidence-c7), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has many hydrophobic transmembrane segments and a DPGN motif characteristic of the DMT/NRAMP-like divalent-metal transporter family. Transferable family knowledge supports a membrane metal-transport function, with cadmium among the divalent-metal substrates associated with this class. That meaningfully favors C over the hydrolase and dehydrogenase choices, which require catalytic enzyme features, and the dynein-binding choice, which does not fit the transporter-like sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features provide a credible, probabilistic basis for selecting the only transporter option without recalling this exact protein's record. The sequence alone does not prove cadmium is its preferred or experimentally verified substrate, but that limitation does not erase the meaningful distinction among the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C matches the strong transporter-family signal among the choices; the other options describe unrelated binding or enzyme activities.


### Important caveats

- The exact cadmium GO annotation is computational (IEA:TreeGrafter), whereas the cited experimental evidence identifies iron transport.
- The choices omit iron transport, and the evidence does not establish cadmium as the protein's primary substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many hydrophobic transmembrane segments and a DPGN motif characteristic of the DMT/NRAMP-like divalent-metal transporter family. Transferable family knowledge supports a membrane metal-transport function, with cadmium among the divalent-metal substrates associated with this class. That meaningfully favors C over the hydrolase and dehydrogenase choices, which require catalytic enzyme features, and the dynein-binding choice, which does not fit the transporter-like sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features provide a credible, probabilistic basis for selecting the only transporter option without recalling this exact protein's record. The sequence alone does not prove cadmium is its preferred or experimentally verified substrate, but that limitation does not erase the meaningful distinction among the offered choices."
  },
  "case_id": "GO_molecular_function_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns the exact cadmium-transporter GO term, but as an IEA:TreeGrafter computational annotation, not direct experimental evidence. The cited experimental function and reaction concern iron transport, so cadmium transport is supported at the annotation/inference level but is not independently established experimentally by these excerpts."
  },
  "important_caveats": [
    "The exact cadmium GO annotation is computational (IEA:TreeGrafter), whereas the cited experimental evidence identifies iron transport.",
    "The choices omit iron transport, and the evidence does not establish cadmium as the protein's primary substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C matches the strong transporter-family signal among the choices; the other options describe unrelated binding or enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns the exact cadmium-transporter GO term, but as an IEA:TreeGrafter computational annotation, not direct experimental evidence. The cited experimental function and reaction concern iron transport, so cadmium transport is supported at the annotation/inference level but is not independently established experimentally by these excerpts.",
    "evidence_ids": ["C7", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has many hydrophobic transmembrane segments and a DPGN motif characteristic of the DMT/NRAMP-like divalent-metal transporter family. Transferable family knowledge supports a membrane metal-transport function, with cadmium among the divalent-metal substrates associated with this class. That meaningfully favors C over the hydrolase and dehydrogenase choices, which require catalytic enzyme features, and the dynein-binding choice, which does not fit the transporter-like sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features provide a credible, probabilistic basis for selecting the only transporter option without recalling this exact protein's record. The sequence alone does not prove cadmium is its preferred or experimentally verified substrate, but that limitation does not erase the meaningful distinction among the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C matches the strong transporter-family signal among the choices; the other options describe unrelated binding or enzyme activities."
  },
  "important_caveats": [
    "The exact cadmium GO annotation is computational (IEA:TreeGrafter), whereas the cited experimental evidence identifies iron transport.",
    "The choices omit iron transport, and the evidence does not establish cadmium as the protein's primary substrate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (A0A077Y877, PyDMT1) carries GO:0015086 (cadmium ion transmembrane transporter activity) as an IEA:TreeGrafter annotation. While the primary experimentally-validated function is iron transport (ECO:0000269, PubMed:38049852), the cadmium transport annotation is a legitimate computational inference consistent with the DMT1/NRAMP family's known ability to transport multiple divalent metals including Cd²⁺. The GO term is present in the database for this exact sequence (sequence matched). The annotation is computational rather than experimental, and calling cadmium transport the 'primary' function is imprecise (iron transport is primary), but the annotation itself is supported as a valid property of this protein family.

Citations as saved: [C7](#evidence-c7), [H5](#evidence-h5), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence clearly encodes a multi-pass transmembrane protein: after a hydrophilic N-terminal extension (~280 residues), there are multiple long hydrophobic stretches (e.g., regions around residues 280-690) consistent with 10-12 transmembrane helices typical of the NRAMP/DMT1 metal transporter family. Among the four options, only C (cadmium ion transmembrane transporter activity, GO:0015086) describes a transmembrane transporter activity. Option A (dynein complex binding) describes a cytoplasmic protein-protein interaction, inconsistent with a multi-TM membrane protein. Option B (beta-glucuronidase activity, EC 3.2.1.31) is a soluble glycosidase with no membrane-spanning architecture. Option D (D-lactate dehydrogenase (cytochrome) activity, EC 1.1.2.4) is a soluble oxidoreductase. Recognizing the NRAMP/DMT1 family pattern (divalent metal transporters with ~12 TM helices) further supports that this protein transports divalent metal ions. Cadmium (Cd²⁺) is a divalent transition metal, and DMT1 family members are well-documented to transport Cd²⁺ alongside Fe²⁺, Mn²⁺, and Zn²⁺. The GO hierarchy places GO:0015086 under 'transition metal ion transmembrane transporter activity' (GO:0046915), making it the only option consistent with a multi-TM divalent metal transporter architecture.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can distinguish C from A, B, D by recognizing the multi-pass transmembrane architecture from the hydrophobic stretches in the sequence, which eliminates the three non-transporter options (binding, glycosidase, oxidoreductase). Family-level knowledge of NRAMP/DMT1 divalent metal transporters and their known substrate range (including Cd²⁺) provides a concrete basis for selecting C. No fact specific to this exact protein's database record is needed beyond what is inferable from the sequence and general transporter biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe activities (protein binding, glycosidase catalysis, oxidoreductase catalysis) that are fundamentally incompatible with a multi-pass transmembrane protein architecture evident from the sequence. Only C describes a transmembrane transporter activity. While the protein's primary experimentally-validated function is iron transport (not cadmium), iron transport is not among the choices, and cadmium transport is a well-established property of the DMT1 family. No other option is defensible for this sequence.


### Important caveats

- The cadmium transport annotation (GO:0015086) is IEA:TreeGrafter (computational inference by similarity), not experimentally validated for this specific protein. The experimental evidence supports iron transport as the primary function.
- The question asks for 'primary molecular function' but the correct answer (cadmium transport) is a secondary/annotated property rather than the primary experimentally-determined function (iron transport). However, among the four offered choices, C is the only viable option.
- The GO term synonyms include 'zinc, cadmium uptake permease activity,' reflecting the broad divalent metal specificity of the DMT1/NRAMP family.
- The reviewer identified the protein via accession A0A077Y877 from dataset metadata; the evaluated model only had the raw sequence and four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly encodes a multi-pass transmembrane protein: after a hydrophilic N-terminal extension (~280 residues), there are multiple long hydrophobic stretches (e.g., regions around residues 280-690) consistent with 10-12 transmembrane helices typical of the NRAMP/DMT1 metal transporter family. Among the four options, only C (cadmium ion transmembrane transporter activity, GO:0015086) describes a transmembrane transporter activity. Option A (dynein complex binding) describes a cytoplasmic protein-protein interaction, inconsistent with a multi-TM membrane protein. Option B (beta-glucuronidase activity, EC 3.2.1.31) is a soluble glycosidase with no membrane-spanning architecture. Option D (D-lactate dehydrogenase (cytochrome) activity, EC 1.1.2.4) is a soluble oxidoreductase. Recognizing the NRAMP/DMT1 family pattern (divalent metal transporters with ~12 TM helices) further supports that this protein transports divalent metal ions. Cadmium (Cd²⁺) is a divalent transition metal, and DMT1 family members are well-documented to transport Cd²⁺ alongside Fe²⁺, Mn²⁺, and Zn²⁺. The GO hierarchy places GO:0015086 under 'transition metal ion transmembrane transporter activity' (GO:0046915), making it the only option consistent with a multi-TM divalent metal transporter architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish C from A, B, D by recognizing the multi-pass transmembrane architecture from the hydrophobic stretches in the sequence, which eliminates the three non-transporter options (binding, glycosidase, oxidoreductase). Family-level knowledge of NRAMP/DMT1 divalent metal transporters and their known substrate range (including Cd²⁺) provides a concrete basis for selecting C. No fact specific to this exact protein's database record is needed beyond what is inferable from the sequence and general transporter biology."
  },
  "case_id": "GO_molecular_function_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H5",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A077Y877, PyDMT1) carries GO:0015086 (cadmium ion transmembrane transporter activity) as an IEA:TreeGrafter annotation. While the primary experimentally-validated function is iron transport (ECO:0000269, PubMed:38049852), the cadmium transport annotation is a legitimate computational inference consistent with the DMT1/NRAMP family's known ability to transport multiple divalent metals including Cd²⁺. The GO term is present in the database for this exact sequence (sequence matched). The annotation is computational rather than experimental, and calling cadmium transport the 'primary' function is imprecise (iron transport is primary), but the annotation itself is supported as a valid property of this protein family."
  },
  "important_caveats": [
    "The cadmium transport annotation (GO:0015086) is IEA:TreeGrafter (computational inference by similarity), not experimentally validated for this specific protein. The experimental evidence supports iron transport as the primary function.",
    "The question asks for 'primary molecular function' but the correct answer (cadmium transport) is a secondary/annotated property rather than the primary experimentally-determined function (iron transport). However, among the four offered choices, C is the only viable option.",
    "The GO term synonyms include 'zinc, cadmium uptake permease activity,' reflecting the broad divalent metal specificity of the DMT1/NRAMP family.",
    "The reviewer identified the protein via accession A0A077Y877 from dataset metadata; the evaluated model only had the raw sequence and four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe activities (protein binding, glycosidase catalysis, oxidoreductase catalysis) that are fundamentally incompatible with a multi-pass transmembrane protein architecture evident from the sequence. Only C describes a transmembrane transporter activity. While the protein's primary experimentally-validated function is iron transport (not cadmium), iron transport is not among the choices, and cadmium transport is a well-established property of the DMT1 family. No other option is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A077Y877, PyDMT1) carries GO:0015086 (cadmium ion transmembrane transporter activity) as an IEA:TreeGrafter annotation. While the primary experimentally-validated function is iron transport (ECO:0000269, PubMed:38049852), the cadmium transport annotation is a legitimate computational inference consistent with the DMT1/NRAMP family's known ability to transport multiple divalent metals including Cd²⁺. The GO term is present in the database for this exact sequence (sequence matched). The annotation is computational rather than experimental, and calling cadmium transport the 'primary' function is imprecise (iron transport is primary), but the annotation itself is supported as a valid property of this protein family.",
    "evidence_ids": ["C7", "H5", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence clearly encodes a multi-pass transmembrane protein: after a hydrophilic N-terminal extension (~280 residues), there are multiple long hydrophobic stretches (e.g., regions around residues 280-690) consistent with 10-12 transmembrane helices typical of the NRAMP/DMT1 metal transporter family. Among the four options, only C (cadmium ion transmembrane transporter activity, GO:0015086) describes a transmembrane transporter activity. Option A (dynein complex binding) describes a cytoplasmic protein-protein interaction, inconsistent with a multi-TM membrane protein. Option B (beta-glucuronidase activity, EC 3.2.1.31) is a soluble glycosidase with no membrane-spanning architecture. Option D (D-lactate dehydrogenase (cytochrome) activity, EC 1.1.2.4) is a soluble oxidoreductase. Recognizing the NRAMP/DMT1 family pattern (divalent metal transporters with ~12 TM helices) further supports that this protein transports divalent metal ions. Cadmium (Cd²⁺) is a divalent transition metal, and DMT1 family members are well-documented to transport Cd²⁺ alongside Fe²⁺, Mn²⁺, and Zn²⁺. The GO hierarchy places GO:0015086 under 'transition metal ion transmembrane transporter activity' (GO:0046915), making it the only option consistent with a multi-TM divalent metal transporter architecture.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish C from A, B, D by recognizing the multi-pass transmembrane architecture from the hydrophobic stretches in the sequence, which eliminates the three non-transporter options (binding, glycosidase, oxidoreductase). Family-level knowledge of NRAMP/DMT1 divalent metal transporters and their known substrate range (including Cd²⁺) provides a concrete basis for selecting C. No fact specific to this exact protein's database record is needed beyond what is inferable from the sequence and general transporter biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe activities (protein binding, glycosidase catalysis, oxidoreductase catalysis) that are fundamentally incompatible with a multi-pass transmembrane protein architecture evident from the sequence. Only C describes a transmembrane transporter activity. While the protein's primary experimentally-validated function is iron transport (not cadmium), iron transport is not among the choices, and cadmium transport is a well-established property of the DMT1 family. No other option is defensible for this sequence."
  },
  "important_caveats": [
    "The cadmium transport annotation (GO:0015086) is IEA:TreeGrafter (computational inference by similarity), not experimentally validated for this specific protein. The experimental evidence supports iron transport as the primary function.",
    "The question asks for 'primary molecular function' but the correct answer (cadmium transport) is a secondary/annotated property rather than the primary experimentally-determined function (iron transport). However, among the four offered choices, C is the only viable option.",
    "The GO term synonyms include 'zinc, cadmium uptake permease activity,' reflecting the broad divalent metal specificity of the DMT1/NRAMP family.",
    "The reviewer identified the protein via accession A0A077Y877 from dataset metadata; the evaluated model only had the raw sequence and four choices."
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
  "benchmark_sequence_length": 696,
  "benchmark_sequence_sha256": "5ba561d59da02d1e0aa0316281aa8d6da8602c10efd3e007cc12440132bf882d",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 696,
  "current_source_sequence_sha256": "5ba561d59da02d1e0aa0316281aa8d6da8602c10efd3e007cc12440132bf882d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A077Y877",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "selected_historical_source_sequence_length": 696,
  "selected_historical_source_sequence_sha256": "5ba561d59da02d1e0aa0316281aa8d6da8602c10efd3e007cc12440132bf882d",
  "selected_historical_version": {
    "accession": "A0A077Y877",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DMT1_PLAYE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A077Y877\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Vinckeia\"],\"scientificName\":\"Plasmodium yoelii\",\"taxonId\":5861}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I3M7\",\"source\":\"UniProtKB\"}],\"value\":\"Food vacuole resident transporter 1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38049852\",\"source\":\"PubMed\"}],\"value\":\"Divalent metal transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38049852\",\"source\":\"PubMed\"}],\"value\":\"PyDMT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38049852\",\"source\":\"PubMed\"}],\"value\":\"Iron transporter (PubMed:38049852). Required for parasite development during the blood stages (PubMed:38049852). Required for full pathogenicity (PubMed:38049852)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38049852\",\"source\":\"PubMed\"}],\"name\":\"Fe(2+)(in) = Fe(2+)(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:28486\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29033\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0015086\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:cadmium ion transmembrane transporter activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005384\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:manganese ion transmembrane transporter activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/15",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhong M.\",\"Zhou B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38049852\"},{\"database\":\"DOI\",\"id\":\"10.1186/s12915-023-01776-y\"}],\"citationType\":\"journal article\",\"firstPage\":\"279\",\"id\":\"38049852\",\"journal\":\"BMC Biol.\",\"lastPage\":\"279\",\"publicationDate\":\"2023\",\"title\":\"Plasmodium yoelii iron transporter PyDMT1 interacts with host ferritin and is required in full activity for malarial pathogenesis.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   DMT1_PLAYE              Reviewed;         696 AA.\nAC   A0A077Y877;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Divalent metal transporter 1 {ECO:0000303|PubMed:38049852};\nDE            Short=PyDMT1 {ECO:0000303|PubMed:38049852};\nDE   AltName: Full=Food vacuole resident transporter 1 {ECO:0000250|UniProtKB:Q8I3M7};\nGN   Name=FVRT1 {ECO:0000250|UniProtKB:Q8I3M7};\nGN   ORFNames=PY17X_1241800 {ECO:0000312|EMBL:VTZ80216.1},\nGN   PYYM_1241000 {ECO:0000312|EMBL:CDU19580.1};\nOS   Plasmodium yoelii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).\nOX   NCBI_TaxID=5861 {ECO:0000312|Proteomes:UP000072904};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, SUBCELLULAR LOCATION, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=38049852; DOI=10.1186/s12915-023-01776-y;\nRA   Zhong M., Zhou B.;\nRT   \"Plasmodium yoelii iron transporter PyDMT1 interacts with host ferritin and\nRT   is required in full activity for malarial pathogenesis.\";\nRL   BMC Biol. 21:279-279(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Iron transporter (PubMed:38049852). Required for parasite\nCC       development during the blood stages (PubMed:38049852). Required for\nCC       full pathogenicity (PubMed:38049852). {ECO:0000269|PubMed:38049852}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Fe(2+)(in) = Fe(2+)(out); Xref=Rhea:RHEA:28486,\nCC         ChEBI:CHEBI:29033; Evidence={ECO:0000269|PubMed:38049852};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0015086; F:cadmium ion transmembrane transporter activity; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005384; F:manganese ion transmembrane transporter activity; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004458\nname: D-lactate dehydrogenase (cytochrome) activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: (R)-lactate + 2 [Fe(III)cytochrome c] = 2 [Fe(II)cytochrome c] + 2 H+ + pyruvate.\" [RHEA:13521]\nsynonym: \"(R)-lactate:ferricytochrome-c 2-oxidoreductase activity\" EXACT []\nsynonym: \"cytochrome-dependent D-(-)-lactate dehydrogenase activity\" RELATED []\nsynonym: \"D-(-)-lactic cytochrome c reductase activity\" RELATED [EC:1.1.2.4]\nsynonym: \"D-lactate (cytochrome) dehydrogenase activity\" RELATED [EC:1.1.2.4]\nsynonym: \"D-lactate dehydrogenase activity\" BROAD []\nsynonym: \"D-lactate ferricytochrome c oxidoreductase activity\" RELATED [EC:1.1.2.4]\nsynonym: \"D-lactate-cytochrome c reductase activity\" RELATED []\nsynonym: \"lactic acid dehydrogenase activity\" BROAD [EC:1.1.2.4]\nxref: EC:1.1.2.4\nxref: MetaCyc:D-LACTATE-DEHYDROGENASE-CYTOCHROME-RXN\nxref: RHEA:13521\nis_a: GO:0016898 ! oxidoreductase activity, acting on the CH-OH group of donors, cytochrome as acceptor\nis_a: GO:0047809 ! D-lactate dehydrogenase activity\nproperty_value: skos:exactMatch EC:1.1.2.4\nproperty_value: skos:exactMatch RHEA:13521\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004458",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 42341-42361",
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
  "excerpt": "[Term]\nid: GO:0004566\nname: beta-glucuronidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a beta-D-glucuronoside + H2O = an alcohol + D-glucuronate.\" [EC:3.2.1.31]\nsynonym: \"beta-D-glucuronoside glucuronosohydrolase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"beta-glucuronide glucuronohydrolase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"exo-beta-D-glucuronidase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"glucuronidase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"ketodase activity\" RELATED [EC:3.2.1.31]\nxref: EC:3.2.1.31\nxref: MetaCyc:BETA-GLUCURONID-RXN\nxref: Reactome:R-HSA-1678854 \"GUSB tetramer hydrolyses CS/HS precursor\"\nxref: Reactome:R-HSA-2162226 \"GUSB tetramer hydrolyzes GlcA-1,3-GlcNAc\"\nxref: Reactome:R-HSA-2162227 \"GUSB tetramer hydrolyses (HA)2\"\nxref: Reactome:R-HSA-2318373 \"Defective GUSB does not hydrolyse (HA)2\"\nxref: Reactome:R-HSA-9036068 \"Defective GUSB does not hydrolyse GlcA-1,3-GlcNAc\"\nxref: Reactome:R-HSA-9036070 \"Defective GUSB does not hydrolyse CS/HS precursor\"\nxref: RHEA:17633\nxref: RHEA:28326\nxref: RHEA:30475\nxref: RHEA:76111\nis_a: GO:0046574 ! glucuronidase activity\nproperty_value: skos:exactMatch EC:3.2.1.31\nproperty_value: skos:exactMatch RHEA:17633\nproperty_value: skos:narrowMatch RHEA:28326\nproperty_value: skos:narrowMatch RHEA:30475\nproperty_value: skos:narrowMatch RHEA:76111\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004566",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 44488-44516",
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
  "excerpt": "[Term]\nid: GO:0015086\nname: cadmium ion transmembrane transporter activity\nnamespace: molecular_function\ndef: \"Enables the transfer of cadmium (Cd) ions from one side of a membrane to the other.\" [GOC:dgf]\nsynonym: \"zinc, cadmium uptake permease activity\" RELATED []\nsynonym: \"zinc, cadmium, cobalt, nickel, lead-efflux ATPase activity\" RELATED []\nis_a: GO:0046915 ! transition metal ion transmembrane transporter activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015086",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 114385-114393",
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
  "excerpt": "[Term]\nid: GO:0070840\nname: dynein complex binding\nnamespace: molecular_function\nalt_id: GO:0045502\ndef: \"Binding to a dynein complex, a protein complex that contains two or three dynein heavy chains and several light chains, and has microtubule motor activity.\" [GOC:bf, GOC:BHF, GOC:mah]\nsynonym: \"dynein binding\" RELATED []\nis_a: GO:0044877 ! protein-containing complex binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0070840",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 371558-371566",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 36. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
