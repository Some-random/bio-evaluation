# catalytic_activity_0140

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0140.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — Endohydrolysis of (1-&gt;4)-beta-D-xylosidic linkages in xylans.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSFSSLFVAACAAVTAFALPSELEKRAITTSQQGTSNGYFYSFWTNGGGSVSYNNGASGEYSVSWSNCGSFTSGKGWATGSSRNINFSGSFKPSGNAYLAVYGWTTSPLVEYYIMENYGDYNPGRSMTFKGTVTSDGSVYDIYTHQQVNQPSISGTATFEQYWSIRRTKRSSGTVTTANHFKAWASHGMYLGSHNYQIVSTEGYQSSGSSDITVS

[Multiple Choices]
A. UTP + H2O = UDP + phosphate + H(+)
B. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
C. guanosine(18) in tRNA + S-adenosyl-L-methionine = 2'-O-methylguanosine(18) in tRNA + S-adenosyl-L-homocysteine + H(+)
D. a 14alpha-formyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a Delta(14) steroid + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation assigns EC 3.2.1.8 and the exact xylan hydrolysis reaction in choice B. Its evidence is a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with a secretion signal, followed by a compact enzyme-sized sequence. Small secreted fungal enzymes are a familiar pattern for endo-xylanases, which hydrolyze xylan linkages as in B. This contrasts with the nucleotide-hydrolysis, tRNA methylation, and steroid-transforming reactions in A, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of secreted fungal enzyme families and their typical size and role provides a meaningful, though not definitive, basis for selecting B among these choices without needing this protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct reaction classes, and the sequence features support the xylanase-type choice over the other offered reactions.


### Important caveats

- The supplied annotation supports B but is computationally assigned by PROSITE-ProRule; the excerpts do not independently establish experimental catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a secretion signal, followed by a compact enzyme-sized sequence. Small secreted fungal enzymes are a familiar pattern for endo-xylanases, which hydrolyze xylan linkages as in B. This contrasts with the nucleotide-hydrolysis, tRNA methylation, and steroid-transforming reactions in A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of secreted fungal enzyme families and their typical size and role provides a meaningful, though not definitive, basis for selecting B among these choices without needing this protein's recorded annotation."
  },
  "case_id": "catalytic_activity_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 3.2.1.8 and the exact xylan hydrolysis reaction in choice B. Its evidence is a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The supplied annotation supports B but is computationally assigned by PROSITE-ProRule; the excerpts do not independently establish experimental catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction classes, and the sequence features support the xylanase-type choice over the other offered reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 3.2.1.8 and the exact xylan hydrolysis reaction in choice B. Its evidence is a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a secretion signal, followed by a compact enzyme-sized sequence. Small secreted fungal enzymes are a familiar pattern for endo-xylanases, which hydrolyze xylan linkages as in B. This contrasts with the nucleotide-hydrolysis, tRNA methylation, and steroid-transforming reactions in A, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of secreted fungal enzyme families and their typical size and role provides a meaningful, though not definitive, basis for selecting B among these choices without needing this protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction classes, and the sequence features support the xylanase-type choice over the other offered reactions."
  },
  "important_caveats": [
    "The supplied annotation supports B but is computationally assigned by PROSITE-ProRule; the excerpts do not independently establish experimental catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry K9GHZ3 annotates this protein as Ethylene-inducing xylanase (EIX) with EC 3.2.1.8, catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The EC number is assigned via PROSITE-ProRule PRU01097 (ECO:0000255), a pattern-based computational annotation derived from experimentally characterized xylanases. The protein name and function are supported by PubMed:39718348 (ECO:0000303). The sequence matches the benchmark input exactly (216 AA, SHA-256 confirmed). The annotation is consistent with the visible GH10 family motifs in the sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark motifs of Glycoside Hydrolase family 10 (GH10) endo-1,4-beta-xylanases: the 'GTSNGYFYSFW' motif near the N-terminus (a conserved GH10 signature), the 'GYS' and 'GWS' repeats, and critically the 'NEYY' catalytic nucleophile region within 'PLVEYYIMENYGDYNPGR' (the Glu-Asn pair serving as acid/base and nucleophile in GH10). These motifs are extensively documented across GH10 xylanases from diverse organisms (Bacillus, Trichoderma, Aspergillus, Streptomyces, etc.) and constitute well-known transferable family-level knowledge. In contrast: option A (nucleotide pyrophosphatase) would show HKD or HD phosphodiesterase motifs absent here; option C (tRNA methyltransferase) would show a Rossmann-fold SAM-binding motif (e.g., 'VLDLGCG') and a catalytic Asp/Asn; option D (P450) would require the highly conserved heme-binding motif 'FGAG' and 'FxxGxxxCxG' (cysteine ligand), none of which appear in this sequence. The fungal signal peptide (MVSFSSLFVAACAAVTAFALPSELEKR) further supports a secreted carbohydrate-active enzyme rather than an intracellular P450 or methyltransferase. Thus, GH10 family recognition from other xylanases meaningfully and uniquely selects option B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH10 xylanase motifs (GTSNGYFYSFW, NEYY, GYS/GWS repeats) are textbook family-level features learned from numerous characterized xylanases across bacteria, fungi, and archaea. Recognizing these patterns and ruling out P450, methyltransferase, and nucleotide pyrophosphatase signatures constitutes legitimate transferable knowledge that distinguishes option B from the alternatives without needing to look up this specific protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GH10 motifs are distinctive and none of the other three options (nucleotide phosphatase, tRNA methyltransferase, P450) share any of the sequence features present. The alternatives are clearly eliminable by family-level reasoning.


### Important caveats

- The EC annotation in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), i.e., computational inference from family motifs rather than direct experimental kinetic characterization of this specific enzyme.
- The protein is named 'ethylene-inducing xylanase' (EIX) based on PubMed:39718348, suggesting it also functions as a PAMP in plant defense, but its catalytic activity is xylan hydrolysis.
- The PROSITE-ProRule PRU01097 pattern for GH10 is derived from experimentally validated xylanases, so the computational annotation rests on well-established family biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark motifs of Glycoside Hydrolase family 10 (GH10) endo-1,4-beta-xylanases: the 'GTSNGYFYSFW' motif near the N-terminus (a conserved GH10 signature), the 'GYS' and 'GWS' repeats, and critically the 'NEYY' catalytic nucleophile region within 'PLVEYYIMENYGDYNPGR' (the Glu-Asn pair serving as acid/base and nucleophile in GH10). These motifs are extensively documented across GH10 xylanases from diverse organisms (Bacillus, Trichoderma, Aspergillus, Streptomyces, etc.) and constitute well-known transferable family-level knowledge. In contrast: option A (nucleotide pyrophosphatase) would show HKD or HD phosphodiesterase motifs absent here; option C (tRNA methyltransferase) would show a Rossmann-fold SAM-binding motif (e.g., 'VLDLGCG') and a catalytic Asp/Asn; option D (P450) would require the highly conserved heme-binding motif 'FGAG' and 'FxxGxxxCxG' (cysteine ligand), none of which appear in this sequence. The fungal signal peptide (MVSFSSLFVAACAAVTAFALPSELEKR) further supports a secreted carbohydrate-active enzyme rather than an intracellular P450 or methyltransferase. Thus, GH10 family recognition from other xylanases meaningfully and uniquely selects option B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH10 xylanase motifs (GTSNGYFYSFW, NEYY, GYS/GWS repeats) are textbook family-level features learned from numerous characterized xylanases across bacteria, fungi, and archaea. Recognizing these patterns and ruling out P450, methyltransferase, and nucleotide pyrophosphatase signatures constitutes legitimate transferable knowledge that distinguishes option B from the alternatives without needing to look up this specific protein's database record."
  },
  "case_id": "catalytic_activity_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry K9GHZ3 annotates this protein as Ethylene-inducing xylanase (EIX) with EC 3.2.1.8, catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The EC number is assigned via PROSITE-ProRule PRU01097 (ECO:0000255), a pattern-based computational annotation derived from experimentally characterized xylanases. The protein name and function are supported by PubMed:39718348 (ECO:0000303). The sequence matches the benchmark input exactly (216 AA, SHA-256 confirmed). The annotation is consistent with the visible GH10 family motifs in the sequence."
  },
  "important_caveats": [
    "The EC annotation in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), i.e., computational inference from family motifs rather than direct experimental kinetic characterization of this specific enzyme.",
    "The protein is named 'ethylene-inducing xylanase' (EIX) based on PubMed:39718348, suggesting it also functions as a PAMP in plant defense, but its catalytic activity is xylan hydrolysis.",
    "The PROSITE-ProRule PRU01097 pattern for GH10 is derived from experimentally validated xylanases, so the computational annotation rests on well-established family biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH10 motifs are distinctive and none of the other three options (nucleotide phosphatase, tRNA methyltransferase, P450) share any of the sequence features present. The alternatives are clearly eliminable by family-level reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry K9GHZ3 annotates this protein as Ethylene-inducing xylanase (EIX) with EC 3.2.1.8, catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The EC number is assigned via PROSITE-ProRule PRU01097 (ECO:0000255), a pattern-based computational annotation derived from experimentally characterized xylanases. The protein name and function are supported by PubMed:39718348 (ECO:0000303). The sequence matches the benchmark input exactly (216 AA, SHA-256 confirmed). The annotation is consistent with the visible GH10 family motifs in the sequence.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark motifs of Glycoside Hydrolase family 10 (GH10) endo-1,4-beta-xylanases: the 'GTSNGYFYSFW' motif near the N-terminus (a conserved GH10 signature), the 'GYS' and 'GWS' repeats, and critically the 'NEYY' catalytic nucleophile region within 'PLVEYYIMENYGDYNPGR' (the Glu-Asn pair serving as acid/base and nucleophile in GH10). These motifs are extensively documented across GH10 xylanases from diverse organisms (Bacillus, Trichoderma, Aspergillus, Streptomyces, etc.) and constitute well-known transferable family-level knowledge. In contrast: option A (nucleotide pyrophosphatase) would show HKD or HD phosphodiesterase motifs absent here; option C (tRNA methyltransferase) would show a Rossmann-fold SAM-binding motif (e.g., 'VLDLGCG') and a catalytic Asp/Asn; option D (P450) would require the highly conserved heme-binding motif 'FGAG' and 'FxxGxxxCxG' (cysteine ligand), none of which appear in this sequence. The fungal signal peptide (MVSFSSLFVAACAAVTAFALPSELEKR) further supports a secreted carbohydrate-active enzyme rather than an intracellular P450 or methyltransferase. Thus, GH10 family recognition from other xylanases meaningfully and uniquely selects option B.",
    "missing_item_specific_fact": "",
    "reason": "The GH10 xylanase motifs (GTSNGYFYSFW, NEYY, GYS/GWS repeats) are textbook family-level features learned from numerous characterized xylanases across bacteria, fungi, and archaea. Recognizing these patterns and ruling out P450, methyltransferase, and nucleotide pyrophosphatase signatures constitutes legitimate transferable knowledge that distinguishes option B from the alternatives without needing to look up this specific protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH10 motifs are distinctive and none of the other three options (nucleotide phosphatase, tRNA methyltransferase, P450) share any of the sequence features present. The alternatives are clearly eliminable by family-level reasoning."
  },
  "important_caveats": [
    "The EC annotation in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), i.e., computational inference from family motifs rather than direct experimental kinetic characterization of this specific enzyme.",
    "The protein is named 'ethylene-inducing xylanase' (EIX) based on PubMed:39718348, suggesting it also functions as a PAMP in plant defense, but its catalytic activity is xylan hydrolysis.",
    "The PROSITE-ProRule PRU01097 pattern for GH10 is derived from experimentally validated xylanases, so the computational annotation rests on well-established family biochemistry."
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
  "benchmark_sequence_length": 216,
  "benchmark_sequence_sha256": "a43bc3a676b5d19b8e6508b04a2c94642fc3a180c24cd6d47e5e6705a113a73e",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-02-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 216,
  "current_source_sequence_sha256": "a43bc3a676b5d19b8e6508b04a2c94642fc3a180c24cd6d47e5e6705a113a73e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "K9GHZ3",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3",
  "selected_historical_source_sequence_length": 216,
  "selected_historical_source_sequence_sha256": "a43bc3a676b5d19b8e6508b04a2c94642fc3a180c24cd6d47e5e6705a113a73e",
  "selected_historical_version": {
    "accession": "K9GHZ3",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX_PEND1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"K9GHZ3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-02-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Green mold\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Penicillium\"],\"scientificName\":\"Penicillium digitatum (strain Pd1 / CECT 20795)\",\"taxonId\":1170230}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39718348\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39718348\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39718348\",\"source\":\"PubMed\"}],\"value\":\"EIX\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"He J.\",\"Li R.\",\"Xu C.\",\"Chen X.\",\"Yao J.\",\"Li Z.\",\"Cheng Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39718348\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.jafc.4c07212\"}],\"citationType\":\"journal article\",\"firstPage\":\"135\",\"id\":\"39718348\",\"journal\":\"J. Agric. Food Chem.\",\"lastPage\":\"146\",\"publicationDate\":\"2025\",\"title\":\"Enhancing Fruit Resistance against Fungal Pathogens Using a Pathogen-Associated Molecular Pattern PdEIX.\",\"volume\":\"73\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   EIX_PEND1               Reviewed;         216 AA.\nAC   K9GHZ3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-FEB-2013, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:39718348};\nDE            Short=EIX {ECO:0000303|PubMed:39718348};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:39718348};\nDE   Flags: Precursor;\nGN   Name=EIX {ECO:0000303|PubMed:39718348}; ORFNames=PDIP_02920;\nOS   Penicillium digitatum (strain Pd1 / CECT 20795) (Green mold).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.\nOX   NCBI_TaxID=1170230;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:01.625551+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3",
  "url": "https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:39718348};\nDE            Short=EIX {ECO:0000303|PubMed:39718348};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:39718348};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:01.625551+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3",
  "url": "https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND SUBCELLULAR LOCATION.\nRX   PubMed=39718348; DOI=10.1021/acs.jafc.4c07212;\nRA   He J., Li R., Xu C., Chen X., Yao J., Li Z., Cheng Y.;\nRT   \"Enhancing Fruit Resistance against Fungal Pathogens Using a Pathogen-\nRT   Associated Molecular Pattern PdEIX.\";\nRL   J. Agric. Food Chem. 73:135-146(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:01.625551+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3",
  "url": "https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:01.625551+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3",
  "url": "https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 140. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
