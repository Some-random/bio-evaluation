# catalytic_activity_0063

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0063.txt)

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
MVSFSTLLTACTAITGALGTPDLDRRQNVTPNAQGTHNGYFYSWWSDGQSPVTYTNSAGGSYSVEWSSGGNLVGGKGWNPGSAKEIRYSASWQPTNNSNSYLTIYGWTRSPLVEYYIVESHGEYNPGSSAEPRGEIEAHGSIYKLYESTRVQQPSIDGTQTFQQYWAIRQTHRTSGTVTTGTFFNAWAAAGMPIGQHNYMIVATEAYNSAGRASVVVETPP

[Multiple Choices]
A. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
B. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
C. 32-oxoeburicol + reduced [NADPH--hemoprotein reductase] + O2 = 14-demethyleburicol + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)
D. (1S,4S)-4-[(4-methoxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + 2-oxoglutarate + O2 = (2S)-3-(4-methoxyphenyl)-2-[(3S)-3-(methylamino)-8-oxo-1-azaspiro[4.5]decan-1-yl]propanal + succinate + CO2
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

> The sequence-matched UniProt record annotates this protein with EC 3.2.1.8 and the reaction in choice B. The annotation is computationally supported by a PROSITE-ProRule, rather than shown here as direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-peptide-like region and a compact, aromatic-rich extracellular-enzyme sequence consistent with a fungal glycoside hydrolase/xylanase. Transferable knowledge of secreted fungal endoxylanases supports xylan hydrolysis, whereas A, C, and D describe unrelated metabolic or oxidative transformations.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family- and sequence-pattern knowledge gives a meaningful basis to select B among these alternatives without needing the exact protein's database entry. The sequence alone may not establish every detail of substrate specificity, but the alternatives are sufficiently distinct.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B matches the credible enzyme-family inference from the sequence and context.


### Important caveats

- The supplied source evidence supports B through a computational PROSITE-ProRule annotation; it does not independently establish direct experimental verification of the catalytic reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region and a compact, aromatic-rich extracellular-enzyme sequence consistent with a fungal glycoside hydrolase/xylanase. Transferable knowledge of secreted fungal endoxylanases supports xylan hydrolysis, whereas A, C, and D describe unrelated metabolic or oxidative transformations.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family- and sequence-pattern knowledge gives a meaningful basis to select B among these alternatives without needing the exact protein's database entry. The sequence alone may not establish every detail of substrate specificity, but the alternatives are sufficiently distinct."
  },
  "case_id": "catalytic_activity_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein with EC 3.2.1.8 and the reaction in choice B. The annotation is computationally supported by a PROSITE-ProRule, rather than shown here as direct experimental evidence."
  },
  "important_caveats": [
    "The supplied source evidence supports B through a computational PROSITE-ProRule annotation; it does not independently establish direct experimental verification of the catalytic reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B matches the credible enzyme-family inference from the sequence and context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein with EC 3.2.1.8 and the reaction in choice B. The annotation is computationally supported by a PROSITE-ProRule, rather than shown here as direct experimental evidence.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region and a compact, aromatic-rich extracellular-enzyme sequence consistent with a fungal glycoside hydrolase/xylanase. Transferable knowledge of secreted fungal endoxylanases supports xylan hydrolysis, whereas A, C, and D describe unrelated metabolic or oxidative transformations.",
    "missing_item_specific_fact": "",
    "reason": "Family- and sequence-pattern knowledge gives a meaningful basis to select B among these alternatives without needing the exact protein's database entry. The sequence alone may not establish every detail of substrate specificity, but the alternatives are sufficiently distinct."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B matches the credible enzyme-family inference from the sequence and context."
  },
  "important_caveats": [
    "The supplied source evidence supports B through a computational PROSITE-ProRule annotation; it does not independently establish direct experimental verification of the catalytic reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G2X5X8 annotates this 221-aa protein as EC 3.2.1.8 (Endo-1,4-beta-xylanase) with the catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The annotation evidence is ECO:0000255 (PROSITE-ProRule:PRU01097), a protein-family-based computational annotation identifying GH11 xylanase motifs. A supporting functional reference (PubMed:33205907) confirms the protein is an EIX-like (ethylene-inducing xylanase) protein from Verticillium dahliae. The sequence matches the benchmark exactly. The expected answer B matches the database annotation verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 221-aa sequence with a clear N-terminal signal peptide (MVSFSTLLTACTAITGALGTPDL) indicates a small secreted protein. Options C (cytochrome P450 sterol demethylase) and D (2-oxoglutarate-dependent dioxygenase) describe reactions catalyzed by enzymes that are typically 400–600+ amino acids and require cofactor-binding motifs (heme-binding FxxGxxxCxG for P450s; HxD/E…H for 2OG-DOs) entirely absent here; the 221-aa length alone effectively excludes both. Option A (dihydroxy-acid dehydratase, EC 4.2.1.9) is a lyase that in most organisms is ~500 aa with a TIM-barrel fold and distinct catalytic residues, inconsistent with this small secreted sequence. The remaining option B (GH11 endo-β-1,4-xylanase, EC 3.2.1.8) is consistent with: (i) the ~220-aa size typical of GH11 xylanases, (ii) the secretion signal, (iii) conserved sequence motifs recognizable as GH11 family features (e.g., the 'GKGW' and 'ESH' segments near the catalytic cleft, the 'GGNLVGGKGW' substrate-binding region, and the overall β-jelly-roll-compatible architecture). A knowledgeable model familiar with GH11 xylanases (e.g., Trichoderma EIX, Bacillus XynA) can recognize these family-level signatures and rule out the alternatives by size and cofactor requirements.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The size (~221 aa), presence of a secretion signal peptide, and GH11-conserved sequence motifs allow a model to eliminate C and D (too large, require cofactor motifs absent here) and A (wrong fold/size for dihydroxy-acid dehydratase), leaving B as the only consistent option. This relies on transferable knowledge of GH11 xylanase family architecture and general enzyme-size/cofactor constraints, not on memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent radically different enzyme classes (lyase, glycoside hydrolase, cytochrome P450, 2OG-dioxygenase) with distinct size, cofactor, and fold requirements. The 221-aa secreted sequence with GH11-like motifs uniquely points to B; no other option is defensible given the sequence constraints.


### Important caveats

- The UniProt catalytic-activity annotation is based on PROSITE-ProRule (ECO:0000255), a computational protein-family annotation, not direct experimental kinetic characterization of this specific protein.
- The functional reference (PubMed:33205907) demonstrates EIX-like elicitor activity in a plant-pathogen context; xylanase catalytic activity is inferred from family membership rather than measured in that paper.
- The sequence-to-GH11 recognition relies on the model's familiarity with the PROSITE PRU01097 motif set; a model unfamiliar with GH11 motifs would struggle to positively identify B from sequence alone, though it could still eliminate A, C, and D by size/cofactor logic.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 221-aa sequence with a clear N-terminal signal peptide (MVSFSTLLTACTAITGALGTPDL) indicates a small secreted protein. Options C (cytochrome P450 sterol demethylase) and D (2-oxoglutarate-dependent dioxygenase) describe reactions catalyzed by enzymes that are typically 400–600+ amino acids and require cofactor-binding motifs (heme-binding FxxGxxxCxG for P450s; HxD/E…H for 2OG-DOs) entirely absent here; the 221-aa length alone effectively excludes both. Option A (dihydroxy-acid dehydratase, EC 4.2.1.9) is a lyase that in most organisms is ~500 aa with a TIM-barrel fold and distinct catalytic residues, inconsistent with this small secreted sequence. The remaining option B (GH11 endo-β-1,4-xylanase, EC 3.2.1.8) is consistent with: (i) the ~220-aa size typical of GH11 xylanases, (ii) the secretion signal, (iii) conserved sequence motifs recognizable as GH11 family features (e.g., the 'GKGW' and 'ESH' segments near the catalytic cleft, the 'GGNLVGGKGW' substrate-binding region, and the overall β-jelly-roll-compatible architecture). A knowledgeable model familiar with GH11 xylanases (e.g., Trichoderma EIX, Bacillus XynA) can recognize these family-level signatures and rule out the alternatives by size and cofactor requirements.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The size (~221 aa), presence of a secretion signal peptide, and GH11-conserved sequence motifs allow a model to eliminate C and D (too large, require cofactor motifs absent here) and A (wrong fold/size for dihydroxy-acid dehydratase), leaving B as the only consistent option. This relies on transferable knowledge of GH11 xylanase family architecture and general enzyme-size/cofactor constraints, not on memorizing this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G2X5X8 annotates this 221-aa protein as EC 3.2.1.8 (Endo-1,4-beta-xylanase) with the catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The annotation evidence is ECO:0000255 (PROSITE-ProRule:PRU01097), a protein-family-based computational annotation identifying GH11 xylanase motifs. A supporting functional reference (PubMed:33205907) confirms the protein is an EIX-like (ethylene-inducing xylanase) protein from Verticillium dahliae. The sequence matches the benchmark exactly. The expected answer B matches the database annotation verbatim."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation is based on PROSITE-ProRule (ECO:0000255), a computational protein-family annotation, not direct experimental kinetic characterization of this specific protein.",
    "The functional reference (PubMed:33205907) demonstrates EIX-like elicitor activity in a plant-pathogen context; xylanase catalytic activity is inferred from family membership rather than measured in that paper.",
    "The sequence-to-GH11 recognition relies on the model's familiarity with the PROSITE PRU01097 motif set; a model unfamiliar with GH11 motifs would struggle to positively identify B from sequence alone, though it could still eliminate A, C, and D by size/cofactor logic."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent radically different enzyme classes (lyase, glycoside hydrolase, cytochrome P450, 2OG-dioxygenase) with distinct size, cofactor, and fold requirements. The 221-aa secreted sequence with GH11-like motifs uniquely points to B; no other option is defensible given the sequence constraints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G2X5X8 annotates this 221-aa protein as EC 3.2.1.8 (Endo-1,4-beta-xylanase) with the catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The annotation evidence is ECO:0000255 (PROSITE-ProRule:PRU01097), a protein-family-based computational annotation identifying GH11 xylanase motifs. A supporting functional reference (PubMed:33205907) confirms the protein is an EIX-like (ethylene-inducing xylanase) protein from Verticillium dahliae. The sequence matches the benchmark exactly. The expected answer B matches the database annotation verbatim.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 221-aa sequence with a clear N-terminal signal peptide (MVSFSTLLTACTAITGALGTPDL) indicates a small secreted protein. Options C (cytochrome P450 sterol demethylase) and D (2-oxoglutarate-dependent dioxygenase) describe reactions catalyzed by enzymes that are typically 400–600+ amino acids and require cofactor-binding motifs (heme-binding FxxGxxxCxG for P450s; HxD/E…H for 2OG-DOs) entirely absent here; the 221-aa length alone effectively excludes both. Option A (dihydroxy-acid dehydratase, EC 4.2.1.9) is a lyase that in most organisms is ~500 aa with a TIM-barrel fold and distinct catalytic residues, inconsistent with this small secreted sequence. The remaining option B (GH11 endo-β-1,4-xylanase, EC 3.2.1.8) is consistent with: (i) the ~220-aa size typical of GH11 xylanases, (ii) the secretion signal, (iii) conserved sequence motifs recognizable as GH11 family features (e.g., the 'GKGW' and 'ESH' segments near the catalytic cleft, the 'GGNLVGGKGW' substrate-binding region, and the overall β-jelly-roll-compatible architecture). A knowledgeable model familiar with GH11 xylanases (e.g., Trichoderma EIX, Bacillus XynA) can recognize these family-level signatures and rule out the alternatives by size and cofactor requirements.",
    "missing_item_specific_fact": "",
    "reason": "The size (~221 aa), presence of a secretion signal peptide, and GH11-conserved sequence motifs allow a model to eliminate C and D (too large, require cofactor motifs absent here) and A (wrong fold/size for dihydroxy-acid dehydratase), leaving B as the only consistent option. This relies on transferable knowledge of GH11 xylanase family architecture and general enzyme-size/cofactor constraints, not on memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent radically different enzyme classes (lyase, glycoside hydrolase, cytochrome P450, 2OG-dioxygenase) with distinct size, cofactor, and fold requirements. The 221-aa secreted sequence with GH11-like motifs uniquely points to B; no other option is defensible given the sequence constraints."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation is based on PROSITE-ProRule (ECO:0000255), a computational protein-family annotation, not direct experimental kinetic characterization of this specific protein.",
    "The functional reference (PubMed:33205907) demonstrates EIX-like elicitor activity in a plant-pathogen context; xylanase catalytic activity is inferred from family membership rather than measured in that paper.",
    "The sequence-to-GH11 recognition relies on the model's familiarity with the PROSITE PRU01097 motif set; a model unfamiliar with GH11 motifs would struggle to positively identify B from sequence alone, though it could still eliminate A, C, and D by size/cofactor logic."
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
  "benchmark_sequence_length": 221,
  "benchmark_sequence_sha256": "f1224442080bd4bf3f0c0d75eb06fb931d6239a2cc8449c269e3c313b81db8ac",
  "current_entry_audit": {
    "entryVersion": 60,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 221,
  "current_source_sequence_sha256": "f1224442080bd4bf3f0c0d75eb06fb931d6239a2cc8449c269e3c313b81db8ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G2X5X8",
  "selected_historical_entry_version": 59,
  "selected_historical_record_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "selected_historical_source_sequence_length": 221,
  "selected_historical_source_sequence_sha256": "f1224442080bd4bf3f0c0d75eb06fb931d6239a2cc8449c269e3c313b81db8ac",
  "selected_historical_version": {
    "accession": "G2X5X8",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX4_VERDV",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G2X5X8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":60,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium wilt\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\",\"taxonId\":498257}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX4\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX4\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H1",
  "excerpt": "ID   EIX4_VERDV              Reviewed;         221 AA.\nAC   G2X5X8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=Ethylene-inducing xylanase 4 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX4 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX4 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX4 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_05294;\nOS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\nOS   (Verticillium wilt).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=498257;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Ethylene-inducing xylanase 4 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX4 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX4 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 63. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
