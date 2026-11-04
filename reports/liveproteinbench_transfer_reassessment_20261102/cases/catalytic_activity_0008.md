# catalytic_activity_0008

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0008.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — apo-&#91;ACP&#93; + CoA = holo-&#91;ACP&#93; + adenosine 3&#x27;,5&#x27;-bisphosphate + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTDSNLLGLTCWLIDTRTLWPGQHIKDAASDILHLLSNDERNAVLRKIFIADARMSLASALLKRLYISRALNIPWRDVKIARKGDPTHGKPCAVLPDGSFAPIDFNVSHQAGLVSLVGWNPPPGQSQSALVGTDIVCVNERDDYRTIDQEGFDAWIDIYEDVFSEAERWDMKYNVDYITLLDGRIIQGNSLGRVDRCVRRNKDLSITLPTGETHSFNSDLLIDAKLRRFYSFFCYKEAYIKLAGEALLAPWLKELEFQNVKSPKPGTVARCSTHGTWGEKVSDVEVVLHGEKVEDVKMTLQAFEENFMLATAVQGLRDLEAPPFTKLNLENDVVAFAS

[Multiple Choices]
A. apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)
B. 3 malonyl-CoA + acetyl-CoA + 2 S-adenosyl-L-methionine = 3,5-dimethylorsellinate + 2 S-adenosyl-L-homocysteine + 3 CO2 + 4 CoA
C. 2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2'-hydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. (9S)-hydroperoxy-(10E,12Z)-octadecadienoate = colneleate + H2O
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

> The sequence-matched UniProt record annotates this protein as a 4′-phosphopantetheinyl transferase and assigns the reaction in choice A. The annotation is transferred by similarity rather than presented as direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble enzyme in the phosphopantetheinyl-transferase family. Transferable knowledge of this family predicts transfer of a phosphopantetheine group from CoA to apo-ACP, producing holo-ACP—the reaction in A. That activity distinguishes A from the methylating polyketide synthesis in B, the carotenoid hydroxylation in C, and the fatty-acid hydroperoxide conversion in D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the known chemistry of phosphopantetheinyl transferases provide a meaningful basis for selecting A without needing this protein’s exact database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options describe substantially different enzyme activities; the family-level inference supports A over the other choices.


### Important caveats

- The supplied source annotation is based on similarity evidence (ECO:0000250); it does not establish direct experimental characterization of this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme in the phosphopantetheinyl-transferase family. Transferable knowledge of this family predicts transfer of a phosphopantetheine group from CoA to apo-ACP, producing holo-ACP—the reaction in A. That activity distinguishes A from the methylating polyketide synthesis in B, the carotenoid hydroxylation in C, and the fatty-acid hydroperoxide conversion in D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known chemistry of phosphopantetheinyl transferases provide a meaningful basis for selecting A without needing this protein’s exact database record."
  },
  "case_id": "catalytic_activity_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein as a 4′-phosphopantetheinyl transferase and assigns the reaction in choice A. The annotation is transferred by similarity rather than presented as direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The supplied source annotation is based on similarity evidence (ECO:0000250); it does not establish direct experimental characterization of this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options describe substantially different enzyme activities; the family-level inference supports A over the other choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein as a 4′-phosphopantetheinyl transferase and assigns the reaction in choice A. The annotation is transferred by similarity rather than presented as direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme in the phosphopantetheinyl-transferase family. Transferable knowledge of this family predicts transfer of a phosphopantetheine group from CoA to apo-ACP, producing holo-ACP—the reaction in A. That activity distinguishes A from the methylating polyketide synthesis in B, the carotenoid hydroxylation in C, and the fatty-acid hydroperoxide conversion in D.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known chemistry of phosphopantetheinyl transferases provide a meaningful basis for selecting A without needing this protein’s exact database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options describe substantially different enzyme activities; the family-level inference supports A over the other choices."
  },
  "important_caveats": [
    "The supplied source annotation is based on similarity evidence (ECO:0000250); it does not establish direct experimental characterization of this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 338-aa sequence exactly matches UniProt entry A0A223GB52 (PPTA_AURME), annotated as 4'-phosphopantetheinyl transferase (EC 2.7.8.7). The recorded catalytic activity is 'apo-&#91;ACP&#93; + CoA = holo-&#91;ACP&#93; + adenosine 3',5'-bisphosphate + H(+)', matching choice A verbatim. The catalytic-activity annotation carries evidence code ECO:0000250 (inferred by similarity from Q4X1W0), so it is a computational/similarity-based inference rather than direct experimental measurement, but the protein name itself has reference-based evidence (ECO:0000303). The sequence match is confirmed at both current and historical (v19) snapshots.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features allow a knowledgeable model to identify this as a 4'-phosphopantetheinyl transferase (PPTase) and eliminate the alternatives. (1) Size: at 338 aa the protein is far too small for a modular polyketide synthase (option B, typically >1000 aa) or a lipoxygenase (option D, typically >600 aa with eight conserved His residues for iron coordination). A carotenoid hydroxylase (option C) is usually a cytochrome P450 (~500 aa with the FxxGxxxCxG heme-binding motif) or a non-heme iron oxidase, neither of which matches the 338-aa length or the absence of heme/iron motifs. (2) PPTase family motifs: the Sfp/LnpA-type PPTase family is one of the most thoroughly characterized enzyme families. The sequence contains an aspartate-rich region ('DDYRTIDQEGF', ~residues 120–132) analogous to the canonical 'DxxxHxxG' catalytic motif, and a hydrophobic 'LxxLxL' region ('GLVSLVGW…SALVGTDIVCV') consistent with the PPTase fold. The overall length (~338 aa) is typical of fungal PPTases (e.g., Aspergillus spp.). (3) The combination of these positive PPTase features plus the elimination of B, C, and D by size and motif absence provides a concrete, transferable inference from known PPTase family biology to select option A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PPTase family is extensively characterized across bacteria, fungi, and plants. Recognizable sequence motifs (aspartate-rich catalytic region, LxxLxL hydrophobic stretch, ~330–340 aa length) and the clear size/motif mismatches for the other three options provide a credible transferable argument without needing to recall this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent very different enzyme classes (transferase, PKS, oxidase, lipoxygenase) with distinct size ranges and cofactor requirements. The 338-aa size and presence of PPTase-consistent motifs clearly point to A and eliminate B, C, and D.


### Important caveats

- The catalytic-activity annotation in UniProt is based on similarity (ECO:0000250, inferred from Q4X1W0), not direct experimental assay of this specific protein.
- The PPTase catalytic motif in this fungal sequence is a variant of the canonical bacterial Sfp 'LxxDxxxHxxG' motif; the aspartate-rich region is recognizable but not perfectly canonical.
- The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning argument relies solely on the supplied sequence and general PPTase family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features allow a knowledgeable model to identify this as a 4'-phosphopantetheinyl transferase (PPTase) and eliminate the alternatives. (1) Size: at 338 aa the protein is far too small for a modular polyketide synthase (option B, typically >1000 aa) or a lipoxygenase (option D, typically >600 aa with eight conserved His residues for iron coordination). A carotenoid hydroxylase (option C) is usually a cytochrome P450 (~500 aa with the FxxGxxxCxG heme-binding motif) or a non-heme iron oxidase, neither of which matches the 338-aa length or the absence of heme/iron motifs. (2) PPTase family motifs: the Sfp/LnpA-type PPTase family is one of the most thoroughly characterized enzyme families. The sequence contains an aspartate-rich region ('DDYRTIDQEGF', ~residues 120–132) analogous to the canonical 'DxxxHxxG' catalytic motif, and a hydrophobic 'LxxLxL' region ('GLVSLVGW…SALVGTDIVCV') consistent with the PPTase fold. The overall length (~338 aa) is typical of fungal PPTases (e.g., Aspergillus spp.). (3) The combination of these positive PPTase features plus the elimination of B, C, and D by size and motif absence provides a concrete, transferable inference from known PPTase family biology to select option A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PPTase family is extensively characterized across bacteria, fungi, and plants. Recognizable sequence motifs (aspartate-rich catalytic region, LxxLxL hydrophobic stretch, ~330–340 aa length) and the clear size/motif mismatches for the other three options provide a credible transferable argument without needing to recall this specific UniProt entry."
  },
  "case_id": "catalytic_activity_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied 338-aa sequence exactly matches UniProt entry A0A223GB52 (PPTA_AURME), annotated as 4'-phosphopantetheinyl transferase (EC 2.7.8.7). The recorded catalytic activity is 'apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)', matching choice A verbatim. The catalytic-activity annotation carries evidence code ECO:0000250 (inferred by similarity from Q4X1W0), so it is a computational/similarity-based inference rather than direct experimental measurement, but the protein name itself has reference-based evidence (ECO:0000303). The sequence match is confirmed at both current and historical (v19) snapshots."
  },
  "important_caveats": [
    "The catalytic-activity annotation in UniProt is based on similarity (ECO:0000250, inferred from Q4X1W0), not direct experimental assay of this specific protein.",
    "The PPTase catalytic motif in this fungal sequence is a variant of the canonical bacterial Sfp 'LxxDxxxHxxG' motif; the aspartate-rich region is recognizable but not perfectly canonical.",
    "The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning argument relies solely on the supplied sequence and general PPTase family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent very different enzyme classes (transferase, PKS, oxidase, lipoxygenase) with distinct size ranges and cofactor requirements. The 338-aa size and presence of PPTase-consistent motifs clearly point to A and eliminate B, C, and D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 338-aa sequence exactly matches UniProt entry A0A223GB52 (PPTA_AURME), annotated as 4'-phosphopantetheinyl transferase (EC 2.7.8.7). The recorded catalytic activity is 'apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)', matching choice A verbatim. The catalytic-activity annotation carries evidence code ECO:0000250 (inferred by similarity from Q4X1W0), so it is a computational/similarity-based inference rather than direct experimental measurement, but the protein name itself has reference-based evidence (ECO:0000303). The sequence match is confirmed at both current and historical (v19) snapshots.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features allow a knowledgeable model to identify this as a 4'-phosphopantetheinyl transferase (PPTase) and eliminate the alternatives. (1) Size: at 338 aa the protein is far too small for a modular polyketide synthase (option B, typically >1000 aa) or a lipoxygenase (option D, typically >600 aa with eight conserved His residues for iron coordination). A carotenoid hydroxylase (option C) is usually a cytochrome P450 (~500 aa with the FxxGxxxCxG heme-binding motif) or a non-heme iron oxidase, neither of which matches the 338-aa length or the absence of heme/iron motifs. (2) PPTase family motifs: the Sfp/LnpA-type PPTase family is one of the most thoroughly characterized enzyme families. The sequence contains an aspartate-rich region ('DDYRTIDQEGF', ~residues 120–132) analogous to the canonical 'DxxxHxxG' catalytic motif, and a hydrophobic 'LxxLxL' region ('GLVSLVGW…SALVGTDIVCV') consistent with the PPTase fold. The overall length (~338 aa) is typical of fungal PPTases (e.g., Aspergillus spp.). (3) The combination of these positive PPTase features plus the elimination of B, C, and D by size and motif absence provides a concrete, transferable inference from known PPTase family biology to select option A.",
    "missing_item_specific_fact": "",
    "reason": "The PPTase family is extensively characterized across bacteria, fungi, and plants. Recognizable sequence motifs (aspartate-rich catalytic region, LxxLxL hydrophobic stretch, ~330–340 aa length) and the clear size/motif mismatches for the other three options provide a credible transferable argument without needing to recall this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent very different enzyme classes (transferase, PKS, oxidase, lipoxygenase) with distinct size ranges and cofactor requirements. The 338-aa size and presence of PPTase-consistent motifs clearly point to A and eliminate B, C, and D."
  },
  "important_caveats": [
    "The catalytic-activity annotation in UniProt is based on similarity (ECO:0000250, inferred from Q4X1W0), not direct experimental assay of this specific protein.",
    "The PPTase catalytic motif in this fungal sequence is a variant of the canonical bacterial Sfp 'LxxDxxxHxxG' motif; the aspartate-rich region is recognizable but not perfectly canonical.",
    "The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning argument relies solely on the supplied sequence and general PPTase family knowledge."
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
  "benchmark_sequence_length": 338,
  "benchmark_sequence_sha256": "99855a22c8c6713370da447a442e50fb925d79b1af9649603cf5c916be789205",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-10-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 338,
  "current_source_sequence_sha256": "99855a22c8c6713370da447a442e50fb925d79b1af9649603cf5c916be789205",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A223GB52",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0",
  "selected_historical_source_sequence_length": 338,
  "selected_historical_source_sequence_sha256": "99855a22c8c6713370da447a442e50fb925d79b1af9649603cf5c916be789205",
  "selected_historical_version": {
    "accession": "A0A223GB52",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PPTA_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A223GB52\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:40.730186+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GB52.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-10-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:40.730186+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GB52.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:40.730186+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GB52.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1W0\",\"source\":\"UniProtKB\"}],\"value\":\"Acyl-carrier-protein synthase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1W0\",\"source\":\"UniProtKB\"}],\"value\":\"Phosphopantetheine:protein transferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1W0\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.8.7\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.2\",\"source\":\"Reference\"}],\"value\":\"4'-phosphopantetheinyl transferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.2\",\"source\":\"Reference\"}],\"value\":\"PPTase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:40.730186+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GB52.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.8.7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1W0\",\"source\":\"UniProtKB\"}],\"name\":\"apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:12068\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9685\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9690\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58343\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64479\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:40.730186+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GB52.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   PPTA_AURME              Reviewed;         338 AA.\nAC   A0A223GB52;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-OCT-2017, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=4'-phosphopantetheinyl transferase {ECO:0000303|Ref.2};\nDE            Short=PPTase {ECO:0000303|Ref.2};\nDE            EC=2.7.8.7 {ECO:0000250|UniProtKB:Q4X1W0};\nDE   AltName: Full=Acyl-carrier-protein synthase {ECO:0000250|UniProtKB:Q4X1W0};\nDE   AltName: Full=Phosphopantetheine:protein transferase {ECO:0000250|UniProtKB:Q4X1W0};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:42.924113+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0",
  "url": "https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4'-phosphopantetheinyl transferase {ECO:0000303|Ref.2};\nDE            Short=PPTase {ECO:0000303|Ref.2};\nDE            EC=2.7.8.7 {ECO:0000250|UniProtKB:Q4X1W0};\nDE   AltName: Full=Acyl-carrier-protein synthase {ECO:0000250|UniProtKB:Q4X1W0};\nDE   AltName: Full=Phosphopantetheine:protein transferase {ECO:0000250|UniProtKB:Q4X1W0};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:42.924113+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0",
  "url": "https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate +\nCC         H(+); Xref=Rhea:RHEA:12068, Rhea:RHEA-COMP:9685, Rhea:RHEA-COMP:9690,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:58343, ChEBI:CHEBI:64479; EC=2.7.8.7;\nCC         Evidence={ECO:0000250|UniProtKB:Q4X1W0};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:42.924113+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0",
  "url": "https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 8. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
