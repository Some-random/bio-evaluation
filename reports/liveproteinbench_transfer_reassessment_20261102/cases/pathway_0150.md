# pathway_0150

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0150.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Pigment biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTLQETSVLEPTLQGTTTLPGLLAQRVAEHPEAIAVAYRDDKLTFRELASRSAALADYLEHLGVSADDCVGLFVEPSIDLMVGAWGILNAGAAYLPLSPEYPEDRLRYMIENSETKIILAQQRLVSRLRELAPKDVTIVTLRESEAFVRPEGTEAPAARSARPDTLAYVIYTSGSTGKPKGVMIEHRSIVNQLGWLRETYAIDRSKVILQKTPMSFDAAQWEILSPANGATVVMGAPGVYADPEGLIETIVKHNVTTLQCVPTLLQGLIDTEKFPECVSLQQIFSGGEALSRLLAIQTTQEMPGRALINVYGPTETTINSSSFPVDPADLDEGPQSISIGSPVHGTTYHILDKETLKPVGVGEIGELYIGGIQLARGYLHRDDLTAERFLEIELEEGAEPVRLYKTGDLGQWNNDGTVQFAGRADNQVKLRGYRVELDEISLAIENHDWVRNAAVIVKNDGRTGFQNLIACIELSEKEAALMDQGNHGSHHASKKSKLQVKAQLSNPGLRDDAELAARPAFDLEGAEPTPEQRARVFARKTYRFYEGGAVTQADLLGLLGATVTAGYSRKAADLAPAELGQILRWFGQYISEERLLPKYGYASPGALYATQMYFELEGVGGLKPGYYYYQPVRHQLVLISEREATGKATAQIHFIGKKSGIEPVYKNNILEVLEIETGHMVGLFEQILPAYGLDIHDRAYEPAVKDLLDVADEDYYLGTFELVPHAGARDDQAEVYVQTHGGKVAGLPEGQYRYENGELTRFSDDIVLKKHVIAINQSVYQAASFGISVYSRAEEEWLKYITLGKKLQHLMMNGLNLGFMSSGYSSKTGNPLPASRRMDAVLGANGVDSAPMYFFVGGRISDEQIGHEGMREDSVHMRGPAELIRDDLVSFLPDYMIPNRVVVFDRLPLSANGKIDVKALAASDQVNAELVERPFVAPRTETEKEIAAVWEKALRRENASVQDDFFESGGNSLIAVGLVRELNARLGVSLPLQSVLESPTIEKLARRLEREVAQESSRFVRLHAETGKARPVICWPGLGGYPMNLRSLAGEIGLGRSFYGVQSYGINEGETPYETITEMAKKDIEALKEIQPAGPYTLWGYSFGARVAFETAYQLEQAGEKVDNLFLIAPGSPKVRAENGKVWGREASFANRGYTTILFSVFTGTISGPDLDRCLETVTDEASFAEFISELKGIDVDLARRIISVVGQTYEFEYSFHELAERTLQAPISIFKAVGDDYSFLENSSGYSAEPPTVIDLDADHYSLLREDIGELVKHIRYLLGE

[Multiple Choices]
A. Antibiotic biosynthesis. .
B. Pigment biosynthesis. .
C. spheroidene biosynthesis. .
D. Carbohydrate degradation
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt record annotated as indigoidine synthase, with the pathway listed as pigment biosynthesis and attributed to experimental evidence (ECO:0000269). This supports B; the cited primary study is not independently assessed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a large, multidomain nonribosomal peptide synthetase, with recognizable NRPS-like catalytic motifs and a single-module architecture. Transferable knowledge of indigoidine-synthase homologs links this kind of single-module synthetase to production of a blue pigment, which favors pigment biosynthesis over antibiotic biosynthesis, spheroidene biosynthesis, or carbohydrate degradation among these options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The inference uses sequence features and family-level knowledge rather than requiring the exact protein's database annotation. NRPS architecture alone would not distinguish pigment from antibiotic production, but the more specific indigoidine-synthase family pattern provides a meaningful basis for choosing B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the options differ in specificity, pigment biosynthesis is the fitting offered category for an indigoidine-producing enzyme; spheroidene is a distinct pigment, and the other choices do not fit its product.


### Important caveats

- The pathway annotation is database evidence attributed to an experimental publication; the publication was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a large, multidomain nonribosomal peptide synthetase, with recognizable NRPS-like catalytic motifs and a single-module architecture. Transferable knowledge of indigoidine-synthase homologs links this kind of single-module synthetase to production of a blue pigment, which favors pigment biosynthesis over antibiotic biosynthesis, spheroidene biosynthesis, or carbohydrate degradation among these options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The inference uses sequence features and family-level knowledge rather than requiring the exact protein's database annotation. NRPS architecture alone would not distinguish pigment from antibiotic production, but the more specific indigoidine-synthase family pattern provides a meaningful basis for choosing B."
  },
  "case_id": "pathway_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated as indigoidine synthase, with the pathway listed as pigment biosynthesis and attributed to experimental evidence (ECO:0000269). This supports B; the cited primary study is not independently assessed here."
  },
  "important_caveats": [
    "The pathway annotation is database evidence attributed to an experimental publication; the publication was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the options differ in specificity, pigment biosynthesis is the fitting offered category for an indigoidine-producing enzyme; spheroidene is a distinct pigment, and the other choices do not fit its product."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated as indigoidine synthase, with the pathway listed as pigment biosynthesis and attributed to experimental evidence (ECO:0000269). This supports B; the cited primary study is not independently assessed here.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a large, multidomain nonribosomal peptide synthetase, with recognizable NRPS-like catalytic motifs and a single-module architecture. Transferable knowledge of indigoidine-synthase homologs links this kind of single-module synthetase to production of a blue pigment, which favors pigment biosynthesis over antibiotic biosynthesis, spheroidene biosynthesis, or carbohydrate degradation among these options.",
    "missing_item_specific_fact": "",
    "reason": "The inference uses sequence features and family-level knowledge rather than requiring the exact protein's database annotation. NRPS architecture alone would not distinguish pigment from antibiotic production, but the more specific indigoidine-synthase family pattern provides a meaningful basis for choosing B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the options differ in specificity, pigment biosynthesis is the fitting offered category for an indigoidine-producing enzyme; spheroidene is a distinct pigment, and the other choices do not fit its product."
  },
  "important_caveats": [
    "The pathway annotation is database evidence attributed to an experimental publication; the publication was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q1MWN4 (INDGS_STRLA) annotates the pathway as 'Pigment biosynthesis' with experimental evidence (ECO:0000269|PubMed:17237222). The protein is indigoidine synthase (EC 4.3.3.9), also called 'Blue pigment synthetase,' which catalyzes the condensation of two L-glutamine molecules to form the blue pigment indigoidine. The supporting reference (Takahashi et al., JBC 2007) experimentally characterized this enzyme as a single-module NRPS catalyzing blue pigment synthesis. The expected answer B matches the annotation exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark non-ribosomal peptide synthetase (NRPS) domain motifs: the adenylation (A) domain signature 'TSGSTGKPKG', a condensation (C) domain region ('YTTILFSVFTGTISGPD'), and thiolation/PCP domain motifs ('GYSFGAR' containing the phosphopantetheine-attachment serine). This immediately eliminates C (spheroidene/carotenoid biosynthesis, which uses phytoene synthase, desaturases, and cyclases—entirely different enzyme classes) and D (carbohydrate degradation, which uses glycosidases, not NRPS domains). The protein length (~1282 aa) and the presence of a single A-PCP-C-TE module architecture identify it as a single-module NRPS. Transferable knowledge from other NRPS enzymes shows a strong family-level pattern: multi-module NRPS (3+ modules, often 5000–20000+ aa) produce complex peptide antibiotics (vancomycin, daptomycin, bleomycin), while single-module NRPS (~1000–1500 aa) typically produce simple dipeptides, most commonly pigments (e.g., violacein synthase VioB, indigoidine synthase BpsA) or signaling molecules. This architecture-to-product-complexity correlation, learned from studying many NRPS homologs, meaningfully tilts the A-vs-B choice toward B (Pigment biosynthesis) over A (Antibiotic biosynthesis), since single-module NRPS products are far more often pigments than antibiotics.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The NRPS domain motifs are directly visible in the sequence, allowing elimination of C and D. The single-module architecture is a genuine, transferable family-level feature (learned from violacein synthases, vancomycin synthetases, etc.) that provides a probabilistic but meaningful distinction between A and B. No fact specific to this exact protein's database record is needed to construct the argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C and D are clearly eliminable by NRPS domain recognition. Between A and B, the single-module NRPS pattern provides a genuine though probabilistic tilt toward B. While Streptomyces context might tempt a model toward 'antibiotic,' the architecture-based argument is a recognized family-level regularity. A is a weaker but not absurd alternative; however, the single-module NRPS → simple dipeptide → pigment pattern is a meaningful discriminator that a knowledgeable model can apply.


### Important caveats

- The A-vs-B distinction rests on a probabilistic family-level pattern (single-module NRPS → pigment vs multi-module NRPS → antibiotic), not on a deterministic sequence signature. A model that does not know this NRPS architecture-product correlation could still be uncertain between A and B.
- The single-module NRPS → pigment pattern has exceptions; some single-module NRPS produce simple peptides with antibiotic activity, and the Streptomyces genus is heavily associated with antibiotic production.
- The UniProt pathway annotation 'Pigment biosynthesis' (ECO:0000269) is based on experimental characterization of indigoidine as a blue pigment, not on a broader biosynthetic pathway; indigoidine synthesis is essentially a single enzymatic step, making the 'pathway' label somewhat loose.
- The reviewer-only evidence (accession Q1MWN4, organism Streptomyces lavendulae, gene name bpsA) was not available to the evaluated model; the reasoning above relies solely on sequence motifs and transferable NRPS family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark non-ribosomal peptide synthetase (NRPS) domain motifs: the adenylation (A) domain signature 'TSGSTGKPKG', a condensation (C) domain region ('YTTILFSVFTGTISGPD'), and thiolation/PCP domain motifs ('GYSFGAR' containing the phosphopantetheine-attachment serine). This immediately eliminates C (spheroidene/carotenoid biosynthesis, which uses phytoene synthase, desaturases, and cyclases—entirely different enzyme classes) and D (carbohydrate degradation, which uses glycosidases, not NRPS domains). The protein length (~1282 aa) and the presence of a single A-PCP-C-TE module architecture identify it as a single-module NRPS. Transferable knowledge from other NRPS enzymes shows a strong family-level pattern: multi-module NRPS (3+ modules, often 5000–20000+ aa) produce complex peptide antibiotics (vancomycin, daptomycin, bleomycin), while single-module NRPS (~1000–1500 aa) typically produce simple dipeptides, most commonly pigments (e.g., violacein synthase VioB, indigoidine synthase BpsA) or signaling molecules. This architecture-to-product-complexity correlation, learned from studying many NRPS homologs, meaningfully tilts the A-vs-B choice toward B (Pigment biosynthesis) over A (Antibiotic biosynthesis), since single-module NRPS products are far more often pigments than antibiotics.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The NRPS domain motifs are directly visible in the sequence, allowing elimination of C and D. The single-module architecture is a genuine, transferable family-level feature (learned from violacein synthases, vancomycin synthetases, etc.) that provides a probabilistic but meaningful distinction between A and B. No fact specific to this exact protein's database record is needed to construct the argument."
  },
  "case_id": "pathway_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q1MWN4 (INDGS_STRLA) annotates the pathway as 'Pigment biosynthesis' with experimental evidence (ECO:0000269|PubMed:17237222). The protein is indigoidine synthase (EC 4.3.3.9), also called 'Blue pigment synthetase,' which catalyzes the condensation of two L-glutamine molecules to form the blue pigment indigoidine. The supporting reference (Takahashi et al., JBC 2007) experimentally characterized this enzyme as a single-module NRPS catalyzing blue pigment synthesis. The expected answer B matches the annotation exactly."
  },
  "important_caveats": [
    "The A-vs-B distinction rests on a probabilistic family-level pattern (single-module NRPS → pigment vs multi-module NRPS → antibiotic), not on a deterministic sequence signature. A model that does not know this NRPS architecture-product correlation could still be uncertain between A and B.",
    "The single-module NRPS → pigment pattern has exceptions; some single-module NRPS produce simple peptides with antibiotic activity, and the Streptomyces genus is heavily associated with antibiotic production.",
    "The UniProt pathway annotation 'Pigment biosynthesis' (ECO:0000269) is based on experimental characterization of indigoidine as a blue pigment, not on a broader biosynthetic pathway; indigoidine synthesis is essentially a single enzymatic step, making the 'pathway' label somewhat loose.",
    "The reviewer-only evidence (accession Q1MWN4, organism Streptomyces lavendulae, gene name bpsA) was not available to the evaluated model; the reasoning above relies solely on sequence motifs and transferable NRPS family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are clearly eliminable by NRPS domain recognition. Between A and B, the single-module NRPS pattern provides a genuine though probabilistic tilt toward B. While Streptomyces context might tempt a model toward 'antibiotic,' the architecture-based argument is a recognized family-level regularity. A is a weaker but not absurd alternative; however, the single-module NRPS → simple dipeptide → pigment pattern is a meaningful discriminator that a knowledgeable model can apply."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q1MWN4 (INDGS_STRLA) annotates the pathway as 'Pigment biosynthesis' with experimental evidence (ECO:0000269|PubMed:17237222). The protein is indigoidine synthase (EC 4.3.3.9), also called 'Blue pigment synthetase,' which catalyzes the condensation of two L-glutamine molecules to form the blue pigment indigoidine. The supporting reference (Takahashi et al., JBC 2007) experimentally characterized this enzyme as a single-module NRPS catalyzing blue pigment synthesis. The expected answer B matches the annotation exactly.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark non-ribosomal peptide synthetase (NRPS) domain motifs: the adenylation (A) domain signature 'TSGSTGKPKG', a condensation (C) domain region ('YTTILFSVFTGTISGPD'), and thiolation/PCP domain motifs ('GYSFGAR' containing the phosphopantetheine-attachment serine). This immediately eliminates C (spheroidene/carotenoid biosynthesis, which uses phytoene synthase, desaturases, and cyclases—entirely different enzyme classes) and D (carbohydrate degradation, which uses glycosidases, not NRPS domains). The protein length (~1282 aa) and the presence of a single A-PCP-C-TE module architecture identify it as a single-module NRPS. Transferable knowledge from other NRPS enzymes shows a strong family-level pattern: multi-module NRPS (3+ modules, often 5000–20000+ aa) produce complex peptide antibiotics (vancomycin, daptomycin, bleomycin), while single-module NRPS (~1000–1500 aa) typically produce simple dipeptides, most commonly pigments (e.g., violacein synthase VioB, indigoidine synthase BpsA) or signaling molecules. This architecture-to-product-complexity correlation, learned from studying many NRPS homologs, meaningfully tilts the A-vs-B choice toward B (Pigment biosynthesis) over A (Antibiotic biosynthesis), since single-module NRPS products are far more often pigments than antibiotics.",
    "missing_item_specific_fact": "",
    "reason": "The NRPS domain motifs are directly visible in the sequence, allowing elimination of C and D. The single-module architecture is a genuine, transferable family-level feature (learned from violacein synthases, vancomycin synthetases, etc.) that provides a probabilistic but meaningful distinction between A and B. No fact specific to this exact protein's database record is needed to construct the argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are clearly eliminable by NRPS domain recognition. Between A and B, the single-module NRPS pattern provides a genuine though probabilistic tilt toward B. While Streptomyces context might tempt a model toward 'antibiotic,' the architecture-based argument is a recognized family-level regularity. A is a weaker but not absurd alternative; however, the single-module NRPS → simple dipeptide → pigment pattern is a meaningful discriminator that a knowledgeable model can apply."
  },
  "important_caveats": [
    "The A-vs-B distinction rests on a probabilistic family-level pattern (single-module NRPS → pigment vs multi-module NRPS → antibiotic), not on a deterministic sequence signature. A model that does not know this NRPS architecture-product correlation could still be uncertain between A and B.",
    "The single-module NRPS → pigment pattern has exceptions; some single-module NRPS produce simple peptides with antibiotic activity, and the Streptomyces genus is heavily associated with antibiotic production.",
    "The UniProt pathway annotation 'Pigment biosynthesis' (ECO:0000269) is based on experimental characterization of indigoidine as a blue pigment, not on a broader biosynthetic pathway; indigoidine synthesis is essentially a single enzymatic step, making the 'pathway' label somewhat loose.",
    "The reviewer-only evidence (accession Q1MWN4, organism Streptomyces lavendulae, gene name bpsA) was not available to the evaluated model; the reasoning above relies solely on sequence motifs and transferable NRPS family knowledge."
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
  "benchmark_sequence_length": 1282,
  "benchmark_sequence_sha256": "15bb18089a044204b45b7f6a6f05b7d317f19a85a8c8fc99093082e6b56646a0",
  "current_entry_audit": {
    "entryVersion": 88,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-05-30",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1282,
  "current_source_sequence_sha256": "15bb18089a044204b45b7f6a6f05b7d317f19a85a8c8fc99093082e6b56646a0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 86,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q1MWN4",
  "selected_historical_entry_version": 86,
  "selected_historical_record_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "selected_historical_source_sequence_length": 1282,
  "selected_historical_source_sequence_sha256": "15bb18089a044204b45b7f6a6f05b7d317f19a85a8c8fc99093082e6b56646a0",
  "selected_historical_version": {
    "accession": "Q1MWN4",
    "database": "Swiss-Prot",
    "entryVersion": 86,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "INDGS_STRLA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q1MWN4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":88,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-05-30\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces lavendulae\",\"taxonId\":1914}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"value\":\"Blue pigment synthetase-encoding gene A\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"value\":\"Blue-pigment synthetase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"value\":\"4.3.3.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Indigoidine synthase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"value\":\"Pigment biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Takahashi H.\",\"Kumagai T.\",\"Kitani K.\",\"Mori M.\",\"Matoba Y.\",\"Sugiyama M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17237222\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m611319200\"}],\"citationType\":\"journal article\",\"firstPage\":\"9073\",\"id\":\"17237222\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"9081\",\"publicationDate\":\"2007\",\"title\":\"Cloning and characterization of a Streptomyces single module type non-ribosomal peptide synthetase catalyzing a blue pigment synthesis.\",\"volume\":\"282\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAE93896.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 11924 / 8197-20\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"DOMAIN\",\"PHOSPHOPANTETHEINYLATION AT SER-972\",\"MUTAGENESIS OF LYS-598; TYR-601; SER-603 AND TYR-608\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H1",
  "excerpt": "ID   INDGS_STRLA             Reviewed;        1282 AA.\nAC   Q1MWN4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   30-MAY-2006, sequence version 1.\nDT   28-JAN-2026, entry version 86.\nDE   RecName: Full=Indigoidine synthase {ECO:0000305};\nDE            EC=4.3.3.9 {ECO:0000269|PubMed:17237222};\nDE   AltName: Full=Blue pigment synthetase-encoding gene A {ECO:0000303|PubMed:17237222};\nDE   AltName: Full=Blue-pigment synthetase {ECO:0000303|PubMed:17237222};\nGN   Name=bpsA {ECO:0000303|PubMed:17237222};\nOS   Streptomyces lavendulae.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=1914;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAE93896.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, DOMAIN, PHOSPHOPANTETHEINYLATION AT\nRP   SER-972, AND MUTAGENESIS OF LYS-598; TYR-601; SER-603 AND TYR-608.\nRC   STRAIN=ATCC 11924 / 8197-20;\nRX   PubMed=17237222; DOI=10.1074/jbc.m611319200;\nRA   Takahashi H., Kumagai T., Kitani K., Mori M., Matoba Y., Sugiyama M.;\nRT   \"Cloning and characterization of a Streptomyces single module type non-\nRT   ribosomal peptide synthetase catalyzing a blue pigment synthesis.\";\nRL   J. Biol. Chem. 282:9073-9081(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Pigment biosynthesis. {ECO:0000269|PubMed:17237222}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 150. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
