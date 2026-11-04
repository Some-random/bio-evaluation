# pathway_0109

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0109.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MELITLLSALLVLAIVSLSTFFVLYYNTPTKDGKTLPPGRMGWPFIGESYDFFAAGWKGKPESFIFDRLKKFAKGNLNGQFRTSLFGNKSIVVAGAAANKLLFSNEKKLVTMWWPPSIDKAFPSTAQLSANEEALLMRKFFPSFLIRREALQRYIPIMDDCTRRHFATGAWGPSDKIEAFNVTQDYTFWVACRVFMSIDAQEDPETVDSLFRHFNVLKAGIYSMHIDLPWTNFHHAMKASHAIRSAVEQIAKKRRAELAEGKAFPTQDMLSYMLETPITSAEDSKDGKAKYLNDADIGTKILGLLVGGHDTSSTVIAFFFKFMAENPHVYEAIYKEQMEVAATKAPGELLNWDDLQKMKYSWCAICEVMRLTPPVQGAFRQAITDFTHNGYLIPKGWKIYWSTHSTHRNPEIFPQPEKFDPTRFEGNGPPAFSFVPFGGGPRMCPGKEYARLQVLTFVHHIVTKFKWEQILPNEKIIVSPMPYPEKNLPLRMIARSESATLA

[Multiple Choices]
A. L-valine from pyruvate: step 3/4. .
B. L-threonine from L-aspartate: step 2/5. .
C. Amino-acid degradation
D. Secondary metabolite biosynthesis
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

> The sequence-matched UniProt annotation assigns the protein to secondary metabolite biosynthesis, specifically terpenoid biosynthesis, and cites experimental evidence (ECO:0000269). This supports choice D, though the excerpts do not independently detail the underlying experiments.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the architecture and conserved heme-thiolate features of a microsomal cytochrome P450. A CYP716-like plant P450 family inference provides a transferable basis for favoring oxidation in terpenoid/specialized-metabolite biosynthesis over the specific valine- and threonine-biosynthesis steps or amino-acid degradation. This is a probabilistic family-level inference, not proof of the exact pathway.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A recognizable P450-family pattern and knowledge of related plant P450s can meaningfully favor D among these choices without relying on the target's recorded annotation. P450s have diverse functions, so sequence-family recognition may be imperfect and the sequence alone does not establish the precise substrate or pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The broad function of P450s is diverse, but the family-level inference favors D over the offered alternatives; no other option is comparably supported by the supplied sequence.


### Important caveats

- The reviewer-only annotation is sequence-matched and supports the key, but was not part of the original model input.
- A P450 signature by itself does not uniquely identify a pathway; the transfer argument depends on recognizing a plant CYP716-like family pattern.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the architecture and conserved heme-thiolate features of a microsomal cytochrome P450. A CYP716-like plant P450 family inference provides a transferable basis for favoring oxidation in terpenoid/specialized-metabolite biosynthesis over the specific valine- and threonine-biosynthesis steps or amino-acid degradation. This is a probabilistic family-level inference, not proof of the exact pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A recognizable P450-family pattern and knowledge of related plant P450s can meaningfully favor D among these choices without relying on the target's recorded annotation. P450s have diverse functions, so sequence-family recognition may be imperfect and the sequence alone does not establish the precise substrate or pathway."
  },
  "case_id": "pathway_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns the protein to secondary metabolite biosynthesis, specifically terpenoid biosynthesis, and cites experimental evidence (ECO:0000269). This supports choice D, though the excerpts do not independently detail the underlying experiments."
  },
  "important_caveats": [
    "The reviewer-only annotation is sequence-matched and supports the key, but was not part of the original model input.",
    "A P450 signature by itself does not uniquely identify a pathway; the transfer argument depends on recognizing a plant CYP716-like family pattern."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad function of P450s is diverse, but the family-level inference favors D over the offered alternatives; no other option is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns the protein to secondary metabolite biosynthesis, specifically terpenoid biosynthesis, and cites experimental evidence (ECO:0000269). This supports choice D, though the excerpts do not independently detail the underlying experiments.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the architecture and conserved heme-thiolate features of a microsomal cytochrome P450. A CYP716-like plant P450 family inference provides a transferable basis for favoring oxidation in terpenoid/specialized-metabolite biosynthesis over the specific valine- and threonine-biosynthesis steps or amino-acid degradation. This is a probabilistic family-level inference, not proof of the exact pathway.",
    "missing_item_specific_fact": "",
    "reason": "A recognizable P450-family pattern and knowledge of related plant P450s can meaningfully favor D among these choices without relying on the target's recorded annotation. P450s have diverse functions, so sequence-family recognition may be imperfect and the sequence alone does not establish the precise substrate or pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad function of P450s is diverse, but the family-level inference favors D over the offered alternatives; no other option is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation is sequence-matched and supports the key, but was not part of the original model input.",
    "A P450 signature by itself does not uniquely identify a pathway; the transfer argument depends on recognizing a plant CYP716-like family pattern."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H3) explicitly states PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is CYP716A379, a beta-amyrin 28-monooxygenase catalyzing a step in saponin (triterpenoid) biosynthesis in Saponaria officinalis. Saponins are secondary metabolites, so option D is directly supported.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif 'FGGGPR' (visible near the C-terminal region as 'FSFVPFGGGPR'), identifying it as a P450 enzyme. P450s are NOT involved in amino acid biosynthesis pathways such as L-valine from pyruvate (option A) or L-threonine from L-aspartate (option B), which use dehydrogenases, transaminases, and synthases. This eliminates A and B. The protein also has a hydrophobic N-terminal signal/membrane anchor typical of plant ER-bound P450s. In plants, the overwhelming majority of P450 enzymes (especially those in the CYP716 family, identifiable by sequence similarity to well-characterized Medicago and Arabidopsis CYP716 enzymes) function in secondary metabolite biosynthesis (triterpenoids/saponins, alkaloids, phenylpropanoids) rather than amino acid degradation. The CYP716 family is a well-known clade of triterpenoid oxidases across multiple plant species, making option D the strongly favored answer over option C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can (1) identify the P450 heme-binding motif to eliminate amino acid biosynthesis options A and B, (2) recognize the plant membrane-bound P450 architecture, and (3) apply the well-established family-level pattern that plant CYP716 enzymes are triterpenoid/saponin oxidases involved in secondary metabolite biosynthesis. This transferable knowledge from related plant P450s meaningfully distinguishes D from C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are eliminated by P450 identification (P450s do not catalyze amino acid biosynthesis). Option C (amino-acid degradation) is a weak distractor because while rare P450s can participate in amino acid catabolism in some organisms, the CYP716 family is unambiguously a triterpenoid biosynthesis clade in plants. Only D is strongly supported.


### Important caveats

- The CYP716 family identification from sequence alone requires trained pattern recognition; a model without exposure to plant P450 family classifications might struggle to distinguish CYP716 from other P450 families that could participate in amino acid degradation.
- The reviewer-only evidence confirms the annotation is experimentally supported (PubMed:39043959, Nat. Chem. Biol. 2025), but this was not available to the evaluated model.
- The sequence length (502 AA) and N-terminal hydrophobic stretch are consistent with a plant microsomal P450, aiding family assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'FGGGPR' (visible near the C-terminal region as 'FSFVPFGGGPR'), identifying it as a P450 enzyme. P450s are NOT involved in amino acid biosynthesis pathways such as L-valine from pyruvate (option A) or L-threonine from L-aspartate (option B), which use dehydrogenases, transaminases, and synthases. This eliminates A and B. The protein also has a hydrophobic N-terminal signal/membrane anchor typical of plant ER-bound P450s. In plants, the overwhelming majority of P450 enzymes (especially those in the CYP716 family, identifiable by sequence similarity to well-characterized Medicago and Arabidopsis CYP716 enzymes) function in secondary metabolite biosynthesis (triterpenoids/saponins, alkaloids, phenylpropanoids) rather than amino acid degradation. The CYP716 family is a well-known clade of triterpenoid oxidases across multiple plant species, making option D the strongly favored answer over option C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) identify the P450 heme-binding motif to eliminate amino acid biosynthesis options A and B, (2) recognize the plant membrane-bound P450 architecture, and (3) apply the well-established family-level pattern that plant CYP716 enzymes are triterpenoid/saponin oxidases involved in secondary metabolite biosynthesis. This transferable knowledge from related plant P450s meaningfully distinguishes D from C."
  },
  "case_id": "pathway_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly states PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is CYP716A379, a beta-amyrin 28-monooxygenase catalyzing a step in saponin (triterpenoid) biosynthesis in Saponaria officinalis. Saponins are secondary metabolites, so option D is directly supported."
  },
  "important_caveats": [
    "The CYP716 family identification from sequence alone requires trained pattern recognition; a model without exposure to plant P450 family classifications might struggle to distinguish CYP716 from other P450 families that could participate in amino acid degradation.",
    "The reviewer-only evidence confirms the annotation is experimentally supported (PubMed:39043959, Nat. Chem. Biol. 2025), but this was not available to the evaluated model.",
    "The sequence length (502 AA) and N-terminal hydrophobic stretch are consistent with a plant microsomal P450, aiding family assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are eliminated by P450 identification (P450s do not catalyze amino acid biosynthesis). Option C (amino-acid degradation) is a weak distractor because while rare P450s can participate in amino acid catabolism in some organisms, the CYP716 family is unambiguously a triterpenoid biosynthesis clade in plants. Only D is strongly supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly states PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is CYP716A379, a beta-amyrin 28-monooxygenase catalyzing a step in saponin (triterpenoid) biosynthesis in Saponaria officinalis. Saponins are secondary metabolites, so option D is directly supported.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'FGGGPR' (visible near the C-terminal region as 'FSFVPFGGGPR'), identifying it as a P450 enzyme. P450s are NOT involved in amino acid biosynthesis pathways such as L-valine from pyruvate (option A) or L-threonine from L-aspartate (option B), which use dehydrogenases, transaminases, and synthases. This eliminates A and B. The protein also has a hydrophobic N-terminal signal/membrane anchor typical of plant ER-bound P450s. In plants, the overwhelming majority of P450 enzymes (especially those in the CYP716 family, identifiable by sequence similarity to well-characterized Medicago and Arabidopsis CYP716 enzymes) function in secondary metabolite biosynthesis (triterpenoids/saponins, alkaloids, phenylpropanoids) rather than amino acid degradation. The CYP716 family is a well-known clade of triterpenoid oxidases across multiple plant species, making option D the strongly favored answer over option C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) identify the P450 heme-binding motif to eliminate amino acid biosynthesis options A and B, (2) recognize the plant membrane-bound P450 architecture, and (3) apply the well-established family-level pattern that plant CYP716 enzymes are triterpenoid/saponin oxidases involved in secondary metabolite biosynthesis. This transferable knowledge from related plant P450s meaningfully distinguishes D from C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are eliminated by P450 identification (P450s do not catalyze amino acid biosynthesis). Option C (amino-acid degradation) is a weak distractor because while rare P450s can participate in amino acid catabolism in some organisms, the CYP716 family is unambiguously a triterpenoid biosynthesis clade in plants. Only D is strongly supported."
  },
  "important_caveats": [
    "The CYP716 family identification from sequence alone requires trained pattern recognition; a model without exposure to plant P450 family classifications might struggle to distinguish CYP716 from other P450 families that could participate in amino acid degradation.",
    "The reviewer-only evidence confirms the annotation is experimentally supported (PubMed:39043959, Nat. Chem. Biol. 2025), but this was not available to the evaluated model.",
    "The sequence length (502 AA) and N-terminal hydrophobic stretch are consistent with a plant microsomal P450, aiding family assignment."
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
  "benchmark_sequence_length": 502,
  "benchmark_sequence_sha256": "a27906e96c4671d9e4d58120851aefbfda32a7b83248e671ac9d77994264a654",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 502,
  "current_source_sequence_sha256": "a27906e96c4671d9e4d58120851aefbfda32a7b83248e671ac9d77994264a654",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAW1JA93",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "selected_historical_source_sequence_length": 502,
  "selected_historical_source_sequence_sha256": "a27906e96c4671d9e4d58120851aefbfda32a7b83248e671ac9d77994264a654",
  "selected_historical_version": {
    "accession": "A0AAW1JA93",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C7169_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1JA93\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 716A379\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoCYP716A379\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Oleanolic acid 16-monooxygenase CYP716A379\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.126\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Beta-amyrin 28-monooxygenase CYP716A379\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48155.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   C7169_SAPOF             Reviewed;         502 AA.\nAC   A0AAW1JA93;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=Beta-amyrin 28-monooxygenase CYP716A379 {ECO:0000305};\nDE            EC=1.14.14.126 {ECO:0000269|PubMed:39043959};\nDE   AltName: Full=Cytochrome P450 716A379 {ECO:0000303|PubMed:39043959};\nDE            Short=SoCYP716A379 {ECO:0000303|PubMed:39043959};\nDE   AltName: Full=Oleanolic acid 16-monooxygenase CYP716A379 {ECO:0000305};\nDE            EC=1.14.14.- {ECO:0000269|PubMed:39043959};\nGN   Name=CYP716A379 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11043486m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_08G189800 {ECO:0000312|EMBL:KAK9699696.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:38.624320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "url": "https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48155.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:38.624320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "url": "https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:38.624320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "url": "https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
