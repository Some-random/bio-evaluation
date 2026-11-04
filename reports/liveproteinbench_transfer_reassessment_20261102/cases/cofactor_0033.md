# cofactor_0033

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0033.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSVSPQSTMARIPERRVRTLDFAQFRHGEPSGSRGFCRELVDCLSSVGFVKIRNHGISGQEIENVFVMSQLFFSLPQAAKGKAAHPPEANPHRGYSYVGQEKLSRVKDYEKGKREITDVYDIKHYPIDRDARQESYDQGAAVDNLYPNRWPDEQDIPGFRVLMETFYERCHEVHQDILRAIAIGFDLSPSFLTDLCCQNTSELRLNHYPSVHPSSLRKGAKRISEHTDFGTVTLLFQDSVGGLEIEDQNTPGTYFPVLSERKSDIIVNIGDCIQRWTNDKIHSTSHRVVLPEDTDALTKDRYSVAYFGKPSRSQLVGSLREFVKEGEKPKYNDISAWQYNQEKLVLTY

[Multiple Choices]
A. tungstopterin
B. pantetheine 4'-phosphate
C. FAD
D. Fe(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched annotation identifies this protein as a 2-oxoglutarate/Fe(II)-type oxidoreductase and explicitly lists Fe(2+) as its cofactor. The cofactor entry cites a computational PROSITE rule, rather than direct binding evidence, but the enzyme classification is linked to a publication reporting catalytic activity; the cited work is specifically about iron(II), alpha-ketoglutarate-dependent enzymes in this cluster.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a compact enzyme-like length and a His/Asp-rich region compatible with the metal-binding core found in non-heme Fe(II)/2-oxoglutarate oxygenases. Transferable knowledge of that enzyme family makes Fe(2+) a meaningful choice over FAD, tungstopterin, or pantetheine 4'-phosphate. The sequence alone does not prove the annotation, but the alternatives are sufficiently distinct for this family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence features can distinguish the offered metal cofactor without recalling this exact protein's database record. The inference is probabilistic, not a direct demonstration of metal binding.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, Fe(2+) is the distinctive expected cofactor for an Fe-dependent oxygenase; no competing option is similarly supported by the sequence-level inference.


### Important caveats

- The explicit cofactor annotation is computationally assigned by a PROSITE rule; the supplied evidence does not include a direct metal-binding assay.
- The reviewer-only source identity and annotations were not part of the original input and are used only to assess expected-answer support.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a compact enzyme-like length and a His/Asp-rich region compatible with the metal-binding core found in non-heme Fe(II)/2-oxoglutarate oxygenases. Transferable knowledge of that enzyme family makes Fe(2+) a meaningful choice over FAD, tungstopterin, or pantetheine 4'-phosphate. The sequence alone does not prove the annotation, but the alternatives are sufficiently distinct for this family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features can distinguish the offered metal cofactor without recalling this exact protein's database record. The inference is probabilistic, not a direct demonstration of metal binding."
  },
  "case_id": "cofactor_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies this protein as a 2-oxoglutarate/Fe(II)-type oxidoreductase and explicitly lists Fe(2+) as its cofactor. The cofactor entry cites a computational PROSITE rule, rather than direct binding evidence, but the enzyme classification is linked to a publication reporting catalytic activity; the cited work is specifically about iron(II), alpha-ketoglutarate-dependent enzymes in this cluster."
  },
  "important_caveats": [
    "The explicit cofactor annotation is computationally assigned by a PROSITE rule; the supplied evidence does not include a direct metal-binding assay.",
    "The reviewer-only source identity and annotations were not part of the original input and are used only to assess expected-answer support."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, Fe(2+) is the distinctive expected cofactor for an Fe-dependent oxygenase; no competing option is similarly supported by the sequence-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies this protein as a 2-oxoglutarate/Fe(II)-type oxidoreductase and explicitly lists Fe(2+) as its cofactor. The cofactor entry cites a computational PROSITE rule, rather than direct binding evidence, but the enzyme classification is linked to a publication reporting catalytic activity; the cited work is specifically about iron(II), alpha-ketoglutarate-dependent enzymes in this cluster.",
    "evidence_ids": ["C4", "C5", "C7", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a compact enzyme-like length and a His/Asp-rich region compatible with the metal-binding core found in non-heme Fe(II)/2-oxoglutarate oxygenases. Transferable knowledge of that enzyme family makes Fe(2+) a meaningful choice over FAD, tungstopterin, or pantetheine 4'-phosphate. The sequence alone does not prove the annotation, but the alternatives are sufficiently distinct for this family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features can distinguish the offered metal cofactor without recalling this exact protein's database record. The inference is probabilistic, not a direct demonstration of metal binding."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, Fe(2+) is the distinctive expected cofactor for an Fe-dependent oxygenase; no competing option is similarly supported by the sequence-level inference."
  },
  "important_caveats": [
    "The explicit cofactor annotation is computationally assigned by a PROSITE rule; the supplied evidence does not include a direct metal-binding assay.",
    "The reviewer-only source identity and annotations were not part of the original input and are used only to assess expected-answer support."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry explicitly annotates the protein as a '2-oxoglutarate-Fe(II) type oxidoreductase ppzD' (C4) with COFACTOR Fe(2+) (C5, H5, evidence ECO:0000255|PROSITE-ProRule:PRU00805). The 2024 JACS paper (C7, H4) experimentally confirms 'Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes' in the PPZ cluster. The expected answer D (Fe(2+)) is directly and strongly supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2-oxoglutarate/Fe(II) oxygenase superfamily (PF03348) is one of the largest and best-characterized enzyme families in biology. Its defining feature is the HxD/E…H facial triad that coordinates a single Fe(II) ion at the active site. Scanning the supplied 349-residue sequence reveals HxD/E…H motifs (e.g., 'CHEVHQD…' and 'HSTSHRVVLPEDTDALTKDRYSVAYFGKPSRSQLVGSLREF') consistent with this fold. A model trained on general biochemistry knows that this superfamily (prolyl hydroxylases, taurine dioxygenase, phytoene synthase, thousands of others) universally requires Fe(II) as its metal cofactor. The three distractors are mechanistically incompatible: tungstopterin is restricted to tungsten-containing oxidoreductases (primarily archaeal, with distinct W-bisPGD motifs); pantetheine 4'-phosphate is a prosthetic group of acyl-CoA synthetases/fatty-acid synthases with adenylate-forming domains; FAD-binding enzymes display Rossmann-fold GxGxxG motifs absent here. Family-level recognition of the 2-OG/Fe(II) oxygenase architecture and its obligate Fe(II) cofactor meaningfully and uniquely selects D over A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HxD/E…H facial triad and overall sequence architecture are recognizable family signatures shared with thousands of characterized 2-OG/Fe(II) oxygenases. Transferable knowledge of this superfamily's universal Fe(II) requirement, combined with the absence of motifs diagnostic for tungstopterin, pantetheine-4'-P, or FAD enzymes, provides a concrete and credible inference that distinguishes D from the other three options without needing the specific ppzD annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four cofactor choices correspond to mechanistically distinct enzyme classes (tungsten enzymes, acyl-CoA synthetases, flavoproteins, 2-OG/Fe(II) oxygenases). The HxD…H facial triad and absence of Rossmann-fold or pantetheine-binding motifs make only Fe(2+) defensible.


### Important caveats

- The cofactor annotation in UniProt is based on PROSITE-ProRule (ECO:0000255), i.e., a computational/pattern-based inference from family membership, not a direct experimental metal-binding measurement for this exact protein. However, the 2024 JACS paper (PubMed 38578094) provides experimental functional characterization of Fe(II)-dependent activity for PPZ-cluster enzymes, strengthening the annotation.
- The reviewer-only evidence (organism, accession, paper titles) was not available to the evaluated model; the answerability argument relies solely on sequence motifs and general family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2-oxoglutarate/Fe(II) oxygenase superfamily (PF03348) is one of the largest and best-characterized enzyme families in biology. Its defining feature is the HxD/E…H facial triad that coordinates a single Fe(II) ion at the active site. Scanning the supplied 349-residue sequence reveals HxD/E…H motifs (e.g., 'CHEVHQD…' and 'HSTSHRVVLPEDTDALTKDRYSVAYFGKPSRSQLVGSLREF') consistent with this fold. A model trained on general biochemistry knows that this superfamily (prolyl hydroxylases, taurine dioxygenase, phytoene synthase, thousands of others) universally requires Fe(II) as its metal cofactor. The three distractors are mechanistically incompatible: tungstopterin is restricted to tungsten-containing oxidoreductases (primarily archaeal, with distinct W-bisPGD motifs); pantetheine 4'-phosphate is a prosthetic group of acyl-CoA synthetases/fatty-acid synthases with adenylate-forming domains; FAD-binding enzymes display Rossmann-fold GxGxxG motifs absent here. Family-level recognition of the 2-OG/Fe(II) oxygenase architecture and its obligate Fe(II) cofactor meaningfully and uniquely selects D over A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HxD/E…H facial triad and overall sequence architecture are recognizable family signatures shared with thousands of characterized 2-OG/Fe(II) oxygenases. Transferable knowledge of this superfamily's universal Fe(II) requirement, combined with the absence of motifs diagnostic for tungstopterin, pantetheine-4'-P, or FAD enzymes, provides a concrete and credible inference that distinguishes D from the other three options without needing the specific ppzD annotation."
  },
  "case_id": "cofactor_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry explicitly annotates the protein as a '2-oxoglutarate-Fe(II) type oxidoreductase ppzD' (C4) with COFACTOR Fe(2+) (C5, H5, evidence ECO:0000255|PROSITE-ProRule:PRU00805). The 2024 JACS paper (C7, H4) experimentally confirms 'Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes' in the PPZ cluster. The expected answer D (Fe(2+)) is directly and strongly supported."
  },
  "important_caveats": [
    "The cofactor annotation in UniProt is based on PROSITE-ProRule (ECO:0000255), i.e., a computational/pattern-based inference from family membership, not a direct experimental metal-binding measurement for this exact protein. However, the 2024 JACS paper (PubMed 38578094) provides experimental functional characterization of Fe(II)-dependent activity for PPZ-cluster enzymes, strengthening the annotation.",
    "The reviewer-only evidence (organism, accession, paper titles) was not available to the evaluated model; the answerability argument relies solely on sequence motifs and general family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor choices correspond to mechanistically distinct enzyme classes (tungsten enzymes, acyl-CoA synthetases, flavoproteins, 2-OG/Fe(II) oxygenases). The HxD…H facial triad and absence of Rossmann-fold or pantetheine-binding motifs make only Fe(2+) defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry explicitly annotates the protein as a '2-oxoglutarate-Fe(II) type oxidoreductase ppzD' (C4) with COFACTOR Fe(2+) (C5, H5, evidence ECO:0000255|PROSITE-ProRule:PRU00805). The 2024 JACS paper (C7, H4) experimentally confirms 'Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes' in the PPZ cluster. The expected answer D (Fe(2+)) is directly and strongly supported.",
    "evidence_ids": ["C4", "C5", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2-oxoglutarate/Fe(II) oxygenase superfamily (PF03348) is one of the largest and best-characterized enzyme families in biology. Its defining feature is the HxD/E…H facial triad that coordinates a single Fe(II) ion at the active site. Scanning the supplied 349-residue sequence reveals HxD/E…H motifs (e.g., 'CHEVHQD…' and 'HSTSHRVVLPEDTDALTKDRYSVAYFGKPSRSQLVGSLREF') consistent with this fold. A model trained on general biochemistry knows that this superfamily (prolyl hydroxylases, taurine dioxygenase, phytoene synthase, thousands of others) universally requires Fe(II) as its metal cofactor. The three distractors are mechanistically incompatible: tungstopterin is restricted to tungsten-containing oxidoreductases (primarily archaeal, with distinct W-bisPGD motifs); pantetheine 4'-phosphate is a prosthetic group of acyl-CoA synthetases/fatty-acid synthases with adenylate-forming domains; FAD-binding enzymes display Rossmann-fold GxGxxG motifs absent here. Family-level recognition of the 2-OG/Fe(II) oxygenase architecture and its obligate Fe(II) cofactor meaningfully and uniquely selects D over A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "The HxD/E…H facial triad and overall sequence architecture are recognizable family signatures shared with thousands of characterized 2-OG/Fe(II) oxygenases. Transferable knowledge of this superfamily's universal Fe(II) requirement, combined with the absence of motifs diagnostic for tungstopterin, pantetheine-4'-P, or FAD enzymes, provides a concrete and credible inference that distinguishes D from the other three options without needing the specific ppzD annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor choices correspond to mechanistically distinct enzyme classes (tungsten enzymes, acyl-CoA synthetases, flavoproteins, 2-OG/Fe(II) oxygenases). The HxD…H facial triad and absence of Rossmann-fold or pantetheine-binding motifs make only Fe(2+) defensible."
  },
  "important_caveats": [
    "The cofactor annotation in UniProt is based on PROSITE-ProRule (ECO:0000255), i.e., a computational/pattern-based inference from family membership, not a direct experimental metal-binding measurement for this exact protein. However, the 2024 JACS paper (PubMed 38578094) provides experimental functional characterization of Fe(II)-dependent activity for PPZ-cluster enzymes, strengthening the annotation.",
    "The reviewer-only evidence (organism, accession, paper titles) was not available to the evaluated model; the answerability argument relies solely on sequence motifs and general family knowledge."
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
  "benchmark_sequence_length": 349,
  "benchmark_sequence_sha256": "c00401d878260e5a5c15ceaae3e9851159bc2fc996a8543018238eee1e7f810e",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 349,
  "current_source_sequence_sha256": "c00401d878260e5a5c15ceaae3e9851159bc2fc996a8543018238eee1e7f810e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 20,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A455ZMR3",
  "selected_historical_entry_version": 20,
  "selected_historical_record_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "selected_historical_source_sequence_length": 349,
  "selected_historical_source_sequence_sha256": "c00401d878260e5a5c15ceaae3e9851159bc2fc996a8543018238eee1e7f810e",
  "selected_historical_version": {
    "accession": "A0A455ZMR3",
    "database": "Swiss-Prot",
    "entryVersion": 20,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PPZD_METMF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A455ZMR3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein D\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"1.14.11.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"1.14.11.57\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"2-oxoglutarate-Fe(II) type oxidoreductase ppzD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29033\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00805\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Fe(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00805\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"Binds 1 Fe(2+) ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Rothchild K.W.\",\"Hagar M.\",\"Berry D.\",\"Ryan K.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38578094\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.4c01419\"}],\"citationType\":\"journal article\",\"firstPage\":\"10263\",\"id\":\"38578094\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"10267\",\"publicationDate\":\"2024\",\"title\":\"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\",\"volume\":\"146\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H1",
  "excerpt": "ID   PPZD_METMF              Reviewed;         349 AA.\nAC   A0A455ZMR3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 20.\nDE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzD {ECO:0000303|PubMed:30452111};\nDE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};\nDE            EC=1.14.11.57 {ECO:0000269|PubMed:38578094};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein D {ECO:0000303|PubMed:30452111};\nGN   Name=ppzD;\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzD {ECO:0000303|PubMed:30452111};\nDE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};\nDE            EC=1.14.11.57 {ECO:0000269|PubMed:38578094};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein D {ECO:0000303|PubMed:30452111};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=38578094; DOI=10.1021/jacs.4c01419;\nRA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;\nRT   \"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ\nRT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\";\nRL   J. Am. Chem. Soc. 146:10263-10267(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00805};\nCC       Note=Binds 1 Fe(2+) ion per subunit. {ECO:0000255|PROSITE-\nCC       ProRule:PRU00805};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
