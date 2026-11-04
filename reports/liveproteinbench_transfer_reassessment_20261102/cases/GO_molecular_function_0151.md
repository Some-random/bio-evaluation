# GO_molecular_function_0151

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0151.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — oxidoreductase activity

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
A. oxidoreductase activity
B. beta-tubulin binding
C. mannose-6-phosphate isomerase activity
D. dynein complex binding
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

> The sequence-matched record annotates oxidoreductase activity (IEA:InterPro; C9, H8). Separately, experimental function evidence describes glutamine oxidation and a catalytic reaction involving FMN and oxygen (C5, C6; H3, H4), supporting redox activity. The enzyme is also classified as a lyase, so oxidoreductase activity need not be its only or principal catalytic classification.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1,282-residue sequence has the scale and conserved motifs of a multidomain nonribosomal peptide synthetase, rather than a mannose-6-phosphate isomerase or a protein whose molecular function is binding tubulin or dynein. Transferable knowledge of indigoidine-synthetase-like NRPSs connects this architecture to glutamine-based pigment synthesis involving oxidation, making oxidoreductase activity the meaningful choice among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level and sequence-architecture clues meaningfully favor A over the offered sugar-isomerase and protein-binding choices. This is a probabilistic inference; the sequence alone may not establish the detailed catalytic annotation or that redox activity is the enzyme's sole function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The enzyme has a lyase classification as well as evidence of redox chemistry, but lyase activity is not one of the choices. Of the offered options, oxidoreductase activity is the supported choice.


### Important caveats

- The direct GO annotation is computational (IEA:InterPro), while the cited functional and catalytic evidence is experimental.
- The experimental reaction and lyase classification make the description of oxidoreductase activity as the primary function less exclusive than the answer wording may imply.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1,282-residue sequence has the scale and conserved motifs of a multidomain nonribosomal peptide synthetase, rather than a mannose-6-phosphate isomerase or a protein whose molecular function is binding tubulin or dynein. Transferable knowledge of indigoidine-synthetase-like NRPSs connects this architecture to glutamine-based pigment synthesis involving oxidation, making oxidoreductase activity the meaningful choice among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level and sequence-architecture clues meaningfully favor A over the offered sugar-isomerase and protein-binding choices. This is a probabilistic inference; the sequence alone may not establish the detailed catalytic annotation or that redox activity is the enzyme's sole function."
  },
  "case_id": "GO_molecular_function_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C9",
      "H3",
      "H4",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates oxidoreductase activity (IEA:InterPro; C9, H8). Separately, experimental function evidence describes glutamine oxidation and a catalytic reaction involving FMN and oxygen (C5, C6; H3, H4), supporting redox activity. The enzyme is also classified as a lyase, so oxidoreductase activity need not be its only or principal catalytic classification."
  },
  "important_caveats": [
    "The direct GO annotation is computational (IEA:InterPro), while the cited functional and catalytic evidence is experimental.",
    "The experimental reaction and lyase classification make the description of oxidoreductase activity as the primary function less exclusive than the answer wording may imply."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme has a lyase classification as well as evidence of redox chemistry, but lyase activity is not one of the choices. Of the offered options, oxidoreductase activity is the supported choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates oxidoreductase activity (IEA:InterPro; C9, H8). Separately, experimental function evidence describes glutamine oxidation and a catalytic reaction involving FMN and oxygen (C5, C6; H3, H4), supporting redox activity. The enzyme is also classified as a lyase, so oxidoreductase activity need not be its only or principal catalytic classification.",
    "evidence_ids": ["C5", "C6", "C9", "H3", "H4", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1,282-residue sequence has the scale and conserved motifs of a multidomain nonribosomal peptide synthetase, rather than a mannose-6-phosphate isomerase or a protein whose molecular function is binding tubulin or dynein. Transferable knowledge of indigoidine-synthetase-like NRPSs connects this architecture to glutamine-based pigment synthesis involving oxidation, making oxidoreductase activity the meaningful choice among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Family-level and sequence-architecture clues meaningfully favor A over the offered sugar-isomerase and protein-binding choices. This is a probabilistic inference; the sequence alone may not establish the detailed catalytic annotation or that redox activity is the enzyme's sole function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme has a lyase classification as well as evidence of redox chemistry, but lyase activity is not one of the choices. Of the offered options, oxidoreductase activity is the supported choice."
  },
  "important_caveats": [
    "The direct GO annotation is computational (IEA:InterPro), while the cited functional and catalytic evidence is experimental.",
    "The experimental reaction and lyase classification make the description of oxidoreductase activity as the primary function less exclusive than the answer wording may imply."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q1MWN4) explicitly annotates GO:0016491 (oxidoreductase activity) with IEA:InterPro evidence (C9, H8). The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 → indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O) involves oxidation of FMN to FMNH2 and O2 consumption, which constitutes a redox reaction consistent with oxidoreductase activity. However, the primary EC classification is 4.3.3.9 (lyase class), and a lyase GO annotation (GO:0016829) also exists. The oxidoreductase annotation is computationally inferred (IEA) rather than experimentally assigned, but the chemistry genuinely involves oxidation, so the key is supported.

Citations as saved: [C9](#evidence-c9), [C6](#evidence-c6), [H8](#evidence-h8), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical NRPS adenylation-domain motifs: the 'YTS' signature (IYTSGSTGKPKG at ~residue 280), the 'HHxxxD' motif (HHASKKSK), and the overall ~1282-residue single-module NRPS architecture (A-C-T domains). This identifies the protein as an enzyme, not a binding protein. Options B (beta-tubulin binding) and D (dynein complex binding) describe interactions with eukaryotic cytoskeletal proteins; a protein with NRPS catalytic domains from a prokaryote-like sequence (no eukaryotic signal peptides, bacterial codon-usage-like composition) would not perform these functions. Option C (mannose-6-phosphate isomerase, EC 5.3.1.8) requires a TIM-barrel fold with a completely different sequence signature and is incompatible with the NRPS domain architecture. By elimination, A (oxidoreductase activity) is the only remaining option, and it is mechanistically plausible because NRPS reactions involving FMN-dependent oxidation (FMN→FMNH2, O2→H2O) constitute redox chemistry. A knowledgeable model can perform this elimination using family recognition (NRPS motifs), general biology (tubulin/dynein are eukaryotic), and enzyme-class knowledge (isomerase fold vs. NRPS fold).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of B, C, and D relies on transferable knowledge: NRPS domain recognition from sequence motifs, the eukaryotic-specificity of tubulin/dynein interactions, and the distinct fold/sequence of mannose-6-phosphate isomerase. The remaining option A is consistent with the redox chemistry inherent in FMN-dependent NRPS catalysis. No target-specific database lookup is required to distinguish the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly incompatible with a bacterial NRPS enzyme. Option C requires a specific TIM-barrel isomerase fold inconsistent with the observed NRPS architecture. Only A remains as a catalytic activity compatible with the sequence. Although the EC class is technically lyase (4.3.3.9) and 'lyase activity' is not offered, among the four given choices A is unambiguously the best fit.


### Important caveats

- The primary EC classification (4.3.3.9) places this enzyme in the lyase class, not the oxidoreductase class (EC 1.-.-.-). The oxidoreductase GO annotation is computationally inferred (IEA:InterPro), not experimentally assigned.
- The reaction genuinely involves oxidation (FMN→FMNH2, O2 reduction), so 'oxidoreductase activity' is a valid mechanistic description even if the EC system classifies the overall transformation as a lyase reaction.
- The organism identity (Streptomyces lavendulae) was not provided to the model; the bacterial inference relies on sequence composition and the absence of eukaryotic features, which is a reasonable but not airtight inference from sequence alone.
- The GO annotation for oxidoreductase activity is IEA (inferred by electronic annotation via InterPro), meaning it is a computational transfer rather than direct experimental evidence for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical NRPS adenylation-domain motifs: the 'YTS' signature (IYTSGSTGKPKG at ~residue 280), the 'HHxxxD' motif (HHASKKSK), and the overall ~1282-residue single-module NRPS architecture (A-C-T domains). This identifies the protein as an enzyme, not a binding protein. Options B (beta-tubulin binding) and D (dynein complex binding) describe interactions with eukaryotic cytoskeletal proteins; a protein with NRPS catalytic domains from a prokaryote-like sequence (no eukaryotic signal peptides, bacterial codon-usage-like composition) would not perform these functions. Option C (mannose-6-phosphate isomerase, EC 5.3.1.8) requires a TIM-barrel fold with a completely different sequence signature and is incompatible with the NRPS domain architecture. By elimination, A (oxidoreductase activity) is the only remaining option, and it is mechanistically plausible because NRPS reactions involving FMN-dependent oxidation (FMN→FMNH2, O2→H2O) constitute redox chemistry. A knowledgeable model can perform this elimination using family recognition (NRPS motifs), general biology (tubulin/dynein are eukaryotic), and enzyme-class knowledge (isomerase fold vs. NRPS fold).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of B, C, and D relies on transferable knowledge: NRPS domain recognition from sequence motifs, the eukaryotic-specificity of tubulin/dynein interactions, and the distinct fold/sequence of mannose-6-phosphate isomerase. The remaining option A is consistent with the redox chemistry inherent in FMN-dependent NRPS catalysis. No target-specific database lookup is required to distinguish the choices."
  },
  "case_id": "GO_molecular_function_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "C9",
      "C6",
      "H8",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q1MWN4) explicitly annotates GO:0016491 (oxidoreductase activity) with IEA:InterPro evidence (C9, H8). The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 → indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O) involves oxidation of FMN to FMNH2 and O2 consumption, which constitutes a redox reaction consistent with oxidoreductase activity. However, the primary EC classification is 4.3.3.9 (lyase class), and a lyase GO annotation (GO:0016829) also exists. The oxidoreductase annotation is computationally inferred (IEA) rather than experimentally assigned, but the chemistry genuinely involves oxidation, so the key is supported."
  },
  "important_caveats": [
    "The primary EC classification (4.3.3.9) places this enzyme in the lyase class, not the oxidoreductase class (EC 1.-.-.-). The oxidoreductase GO annotation is computationally inferred (IEA:InterPro), not experimentally assigned.",
    "The reaction genuinely involves oxidation (FMN→FMNH2, O2 reduction), so 'oxidoreductase activity' is a valid mechanistic description even if the EC system classifies the overall transformation as a lyase reaction.",
    "The organism identity (Streptomyces lavendulae) was not provided to the model; the bacterial inference relies on sequence composition and the absence of eukaryotic features, which is a reasonable but not airtight inference from sequence alone.",
    "The GO annotation for oxidoreductase activity is IEA (inferred by electronic annotation via InterPro), meaning it is a computational transfer rather than direct experimental evidence for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with a bacterial NRPS enzyme. Option C requires a specific TIM-barrel isomerase fold inconsistent with the observed NRPS architecture. Only A remains as a catalytic activity compatible with the sequence. Although the EC class is technically lyase (4.3.3.9) and 'lyase activity' is not offered, among the four given choices A is unambiguously the best fit."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q1MWN4) explicitly annotates GO:0016491 (oxidoreductase activity) with IEA:InterPro evidence (C9, H8). The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 → indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O) involves oxidation of FMN to FMNH2 and O2 consumption, which constitutes a redox reaction consistent with oxidoreductase activity. However, the primary EC classification is 4.3.3.9 (lyase class), and a lyase GO annotation (GO:0016829) also exists. The oxidoreductase annotation is computationally inferred (IEA) rather than experimentally assigned, but the chemistry genuinely involves oxidation, so the key is supported.",
    "evidence_ids": ["C9", "C6", "H8", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical NRPS adenylation-domain motifs: the 'YTS' signature (IYTSGSTGKPKG at ~residue 280), the 'HHxxxD' motif (HHASKKSK), and the overall ~1282-residue single-module NRPS architecture (A-C-T domains). This identifies the protein as an enzyme, not a binding protein. Options B (beta-tubulin binding) and D (dynein complex binding) describe interactions with eukaryotic cytoskeletal proteins; a protein with NRPS catalytic domains from a prokaryote-like sequence (no eukaryotic signal peptides, bacterial codon-usage-like composition) would not perform these functions. Option C (mannose-6-phosphate isomerase, EC 5.3.1.8) requires a TIM-barrel fold with a completely different sequence signature and is incompatible with the NRPS domain architecture. By elimination, A (oxidoreductase activity) is the only remaining option, and it is mechanistically plausible because NRPS reactions involving FMN-dependent oxidation (FMN→FMNH2, O2→H2O) constitute redox chemistry. A knowledgeable model can perform this elimination using family recognition (NRPS motifs), general biology (tubulin/dynein are eukaryotic), and enzyme-class knowledge (isomerase fold vs. NRPS fold).",
    "missing_item_specific_fact": "",
    "reason": "The elimination of B, C, and D relies on transferable knowledge: NRPS domain recognition from sequence motifs, the eukaryotic-specificity of tubulin/dynein interactions, and the distinct fold/sequence of mannose-6-phosphate isomerase. The remaining option A is consistent with the redox chemistry inherent in FMN-dependent NRPS catalysis. No target-specific database lookup is required to distinguish the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with a bacterial NRPS enzyme. Option C requires a specific TIM-barrel isomerase fold inconsistent with the observed NRPS architecture. Only A remains as a catalytic activity compatible with the sequence. Although the EC class is technically lyase (4.3.3.9) and 'lyase activity' is not offered, among the four given choices A is unambiguously the best fit."
  },
  "important_caveats": [
    "The primary EC classification (4.3.3.9) places this enzyme in the lyase class, not the oxidoreductase class (EC 1.-.-.-). The oxidoreductase GO annotation is computationally inferred (IEA:InterPro), not experimentally assigned.",
    "The reaction genuinely involves oxidation (FMN→FMNH2, O2 reduction), so 'oxidoreductase activity' is a valid mechanistic description even if the EC system classifies the overall transformation as a lyase reaction.",
    "The organism identity (Streptomyces lavendulae) was not provided to the model; the bacterial inference relies on sequence composition and the absence of eukaryotic features, which is a reasonable but not airtight inference from sequence alone.",
    "The GO annotation for oxidoreductase activity is IEA (inferred by electronic annotation via InterPro), meaning it is a computational transfer rather than direct experimental evidence for this specific protein."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"value\":\"Nonribosomal peptide synthetase involved in the biosynthesis of the blue pigment indigoidine (PubMed:17237222). Catalyzes the synthesis of the blue pigment using L-Gln as a substrate (PubMed:17237222). Two glutamine molecules are cyclized and oxidized to form indigoidine (PubMed:17237222)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81500\"}}],\"reaction\":{\"ecNumber\":\"4.3.3.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"name\":\"2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:79296\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456215\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81504\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"name\":\"FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-dione + FMNH2 + AMP + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81503\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231893\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456215\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81508\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"name\":\"2 3-amino-1,5-dihydropyridine-2,6-dione + O2 = indigoidine + 2 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81507\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:79296\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231893\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0016491\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:oxidoreductase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031177\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:phosphopantetheine binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C11",
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
  "excerpt": "CC   -!- FUNCTION: Nonribosomal peptide synthetase involved in the biosynthesis\nCC       of the blue pigment indigoidine (PubMed:17237222). Catalyzes the\nCC       synthesis of the blue pigment using L-Gln as a substrate\nCC       (PubMed:17237222). Two glutamine molecules are cyclized and oxidized to\nCC       form indigoidine (PubMed:17237222). {ECO:0000269|PubMed:17237222}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2\nCC         AMP + 2 diphosphate + 2 H2O; Xref=Rhea:RHEA:81499, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:30616, ChEBI:CHEBI:33019,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:58359,\nCC         ChEBI:CHEBI:79296, ChEBI:CHEBI:456215; EC=4.3.3.9;\nCC         Evidence={ECO:0000269|PubMed:17237222};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81500;\nCC         Evidence={ECO:0000269|PubMed:17237222};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-\nCC         dione + FMNH2 + AMP + diphosphate; Xref=Rhea:RHEA:81503,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:58359, ChEBI:CHEBI:231893,\nCC         ChEBI:CHEBI:456215; Evidence={ECO:0000305|PubMed:17237222};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81504;\nCC         Evidence={ECO:0000305|PubMed:17237222};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 3-amino-1,5-dihydropyridine-2,6-dione + O2 = indigoidine + 2\nCC         H2O; Xref=Rhea:RHEA:81507, ChEBI:CHEBI:15377, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:79296, ChEBI:CHEBI:231893;\nCC         Evidence={ECO:0000305|PubMed:17237222};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81508;\nCC         Evidence={ECO:0000305|PubMed:17237222};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0016829; F:lyase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0016491; F:oxidoreductase activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0031177; F:phosphopantetheine binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004476\nname: mannose-6-phosphate isomerase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: D-mannose 6-phosphate = D-fructose 6-phosphate.\" [RHEA:12356]\nsynonym: \"D-mannose-6-phosphate aldose-ketose-isomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"D-mannose-6-phosphate ketol-isomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"mannose phosphate isomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"phosphohexoisomerase activity\" BROAD [EC:5.3.1.8]\nsynonym: \"phosphohexomutase activity\" BROAD [EC:5.3.1.8]\nsynonym: \"phosphomannoisomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"phosphomannose isomerase activity\" RELATED [EC:5.3.1.8]\nxref: EC:5.3.1.8\nxref: MetaCyc:MANNPISOM-RXN\nxref: Reactome:R-HSA-3781832 \"Defective MPI does not  isomerize Fru6P to Man6P\"\nxref: Reactome:R-HSA-532549 \"MPI isomerises Fru6P to Man6P\"\nxref: RHEA:12356\nis_a: GO:0016861 ! intramolecular oxidoreductase activity, interconverting aldoses and ketoses\nproperty_value: skos:exactMatch EC:5.3.1.8\nproperty_value: skos:exactMatch RHEA:12356\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004476",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 42843-42863",
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
  "excerpt": "[Term]\nid: GO:0016491\nname: oxidoreductase activity\nnamespace: molecular_function\ndef: \"Catalysis of an oxidation-reduction (redox) reaction, a reversible chemical reaction in which the oxidation state of an atom or atoms within a molecule is altered. One substrate acts as a hydrogen or electron donor and becomes oxidized, while the other acts as hydrogen or electron acceptor and becomes reduced.\" [EC:1.-.-.-]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nsynonym: \"oxidoreductase activity, acting on other substrates\" NARROW []\nsynonym: \"redox activity\" EXACT []\nxref: EC:1.-.-.-\nxref: Reactome:R-HSA-1614362 \"SUMF1 mediates the oxidation of cysteine to formylglycine, producing active arylsulfatases\"\nxref: Reactome:R-HSA-2161612 \"PGH2 is reduced to PGF2a by FAM213B\"\nxref: Reactome:R-HSA-265296 \"Arachidonate is oxidised to 5S-HpETE by ALOX5\"\nxref: Reactome:R-HSA-266051 \"5S-HpETE is dehydrated to LTA4 by ALOX5\"\nxref: Reactome:R-HSA-390425 \"FAR1 reduces PalmCoA to HXOL\"\nxref: Reactome:R-HSA-390438 \"FAR2 reduces PalmCoA to HXOL\"\nxref: Reactome:R-HSA-8936442 \"MARC1,MARC2 reduce N-hydroxylated compounds\"\nxref: Reactome:R-HSA-9020249 \"Hydroperoxy reductase reduces 4(S)-Hp-17(S)-HDHA to RvD6\"\nxref: Reactome:R-HSA-9020260 \"Hydroperoxy reductase reduces 7(S)-Hp-17(S)-HDHA to RvD5\"\nxref: Reactome:R-HSA-9024624 \"Hydroperoxy reductase reduces 4(S)-Hp-17(R)-HDHA to AT-RvD6\"\nxref: Reactome:R-HSA-9024630 \"Hydroperoxy reductase reduces 7(S)-Hp-17(R)-HDHA to AT-RvD5\"\nxref: Reactome:R-HSA-9025007 \"Hydroperoxy reductase reduces 7(S),14(S)-diHp-DHA to 7-epi-MaR1\"\nxref: Reactome:R-HSA-9026001 \"Hydroperoxy reductase reduces 7,17-diHp-DPAn-3 to RvD5n-3DPA\"\nxref: Reactome:R-HSA-9026917 \"Lipoxygenase dehydrogenates 7(S),17(S)-diHp-DHA to 7S(8)-epoxy-17(S)-HDHA\"\nxref: Reactome:R-HSA-9027033 \"Hydroperoxy reducatase reduces 14(S)-Hp-DHA to 14(S)-HDHA\"\nxref: Reactome:R-HSA-9693722 \"Unknown sepiapterin synthase transforms PTHP to sepiapterin\"\nxref: Reactome:R-HSA-9759549 \"Cob(I)alamin bound to MMACHC is oxidized to cob(II)alamin\"\nis_a: GO:0003824 ! catalytic activity\nproperty_value: skos:exactMatch EC:1.-.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016491",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 127101-127137",
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
  "excerpt": "[Term]\nid: GO:0048487\nname: beta-tubulin binding\nnamespace: molecular_function\ndef: \"Binding to the microtubule constituent protein beta-tubulin.\" [GOC:krc]\nsynonym: \"beta tubulin binding\" EXACT []\nis_a: GO:0015631 ! tubulin binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0048487",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 303668-303675",
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 151. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
