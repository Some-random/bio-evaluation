# catalytic_activity_0159

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0159.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — Endohydrolysis of (1-&gt;4)-beta-D-xylosidic linkages in xylans.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MHLASSLFLLATLPFGFAAGKGKGKGKDNSDVGLDVLAKKAGLKYFGAATDTPGQRERAGLEDKYPEYDRIMWHSPEFGSTTPTNGQKWLFVEPERGVFNFTEGDVVASKARQHGKLLRCHALVWHSQLAPWVEETEWTPEELRKVIVDHITAVAGHYKGQCYAWDVVNEALNEDGTYRESVFYKVLGEEYIKLAFETAAKVDPKAKLYYNDYNLEWPSAKTEGAKRIVKLLKDAKIPIHGVGLQAHLIAEQHPTLDDHIAAIRGFTQLGVEVALTELDIRLKTPATEENLALQREAYKNVVGACVQVCGCVGVTIWDFYDPFSWVPYFFEGEGAPLLWFEDFSKHPAYYGVVEALTNKTRRSKRSISDRRAKLLA

[Multiple Choices]
A. 4-methylmuconolactone = 3-methylmuconolactone
B. Co(2+)(in) = Co(2+)(out)
C. (13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O
D. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
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

> The matched sequence is annotated with the catalytic activity in choice D, with experimental evidence linked to a publication. This supports the keyed reaction for this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secretion signal, followed by a long soluble enzyme sequence—features compatible with a fungal extracellular plant-cell-wall hydrolase. Transferable knowledge of secreted fungal xylanases makes endo-xylan hydrolysis a plausible family-level inference; among the choices, D is the extracellular polysaccharide-hydrolysis reaction, unlike the small-molecule transformations or ion transport in A–C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and alternatives provide a meaningful, though not definitive, biological basis for choosing D without needing the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported by the secretion signal and enzyme-like sequence context.


### Important caveats

- The sequence context supports a probabilistic family-level inference, not an independent proof of substrate specificity.
- The cited source annotation is experimentally evidenced, but the primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretion signal, followed by a long soluble enzyme sequence—features compatible with a fungal extracellular plant-cell-wall hydrolase. Transferable knowledge of secreted fungal xylanases makes endo-xylan hydrolysis a plausible family-level inference; among the choices, D is the extracellular polysaccharide-hydrolysis reaction, unlike the small-molecule transformations or ion transport in A–C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and alternatives provide a meaningful, though not definitive, biological basis for choosing D without needing the exact protein's recorded annotation."
  },
  "case_id": "catalytic_activity_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated with the catalytic activity in choice D, with experimental evidence linked to a publication. This supports the keyed reaction for this protein."
  },
  "important_caveats": [
    "The sequence context supports a probabilistic family-level inference, not an independent proof of substrate specificity.",
    "The cited source annotation is experimentally evidenced, but the primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the secretion signal and enzyme-like sequence context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated with the catalytic activity in choice D, with experimental evidence linked to a publication. This supports the keyed reaction for this protein.",
    "evidence_ids": ["C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretion signal, followed by a long soluble enzyme sequence—features compatible with a fungal extracellular plant-cell-wall hydrolase. Transferable knowledge of secreted fungal xylanases makes endo-xylan hydrolysis a plausible family-level inference; among the choices, D is the extracellular polysaccharide-hydrolysis reaction, unlike the small-molecule transformations or ion transport in A–C.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and alternatives provide a meaningful, though not definitive, biological basis for choosing D without needing the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the secretion signal and enzyme-like sequence context."
  },
  "important_caveats": [
    "The sequence context supports a probabilistic family-level inference, not an independent proof of substrate specificity.",
    "The cited source annotation is experimentally evidenced, but the primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry M4MGK7 (XYNA_HUMIN) annotates this sequence as Endo-1,4-beta-xylanase A (EC 3.2.1.8) from Humicola insolens, with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The annotation is backed by experimental evidence (ECO:0000269, PubMed:23306124, a 2013 Bioresour. Technol. paper characterizing three thermophilic xylanases from H. insolens Y1). The sequence in the benchmark matches the UniProt sequence exactly (SHA256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark 'WHSPEFG' motif (residues ~70-76) and the 'WDFYDPFSWVPY' motif (residues ~295-307), both well-established signatures of glycoside hydrolase family 10 (GH10) xylanases. The 'WHSPEFG' motif harbors the catalytic acid/base glutamic acid, while 'WDFYDPFSWVPY' contains the catalytic nucleophile glutamic acid. These motifs are conserved across dozens of characterized GH10 xylanases from fungi and bacteria and are the primary sequence-level diagnostic for this family. Additionally, the N-terminal hydrophobic signal peptide (MHLASSLFLLATLPFGFAAG) followed by a short linker (GKGKGKGK) is consistent with a secreted fungal xylanase. None of the other options (muconolactone isomerase, cobalt transporter, hydroperoxide lyase) share any of these motifs or fold characteristics: a transporter would show multiple transmembrane helices, a P450-type lyase would contain a heme-binding Cys motif, and a muconolactone isomerase is a small α/β protein with entirely different sequence features. The GH10 motifs are transferable family-level knowledge that meaningfully and uniquely selects option D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH10 xylanase signature motifs (WHSPEFG, WDFYDPFSWVPY) are well-documented across many characterized xylanases and constitute a concrete, transferable sequence feature that distinguishes a xylanase from an isomerase, a transporter, or a hydroperoxide lyase. No target-specific annotation lookup is required; family-level recognition suffices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent entirely different enzyme classes (isomerase, membrane transporter, hydroperoxide lyase, glycoside hydrolase). The GH10-specific motifs unambiguously select the xylanase option and exclude the others.


### Important caveats

- The UniProt annotation is supported by experimental characterization (PubMed:23306124), not merely computational inference.
- The 'WHSPEFG' motif is a strong but not absolutely universal GH10 marker; some GH10 variants show minor substitutions. However, combined with 'WDFYDPFSWVPY' and overall sequence architecture, the family assignment is robust.
- The reviewer-only evidence confirms sequence identity to M4MGK7, but this accession was not provided to the evaluated model; the reasoning above relies solely on the raw sequence and transferable family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark 'WHSPEFG' motif (residues ~70-76) and the 'WDFYDPFSWVPY' motif (residues ~295-307), both well-established signatures of glycoside hydrolase family 10 (GH10) xylanases. The 'WHSPEFG' motif harbors the catalytic acid/base glutamic acid, while 'WDFYDPFSWVPY' contains the catalytic nucleophile glutamic acid. These motifs are conserved across dozens of characterized GH10 xylanases from fungi and bacteria and are the primary sequence-level diagnostic for this family. Additionally, the N-terminal hydrophobic signal peptide (MHLASSLFLLATLPFGFAAG) followed by a short linker (GKGKGKGK) is consistent with a secreted fungal xylanase. None of the other options (muconolactone isomerase, cobalt transporter, hydroperoxide lyase) share any of these motifs or fold characteristics: a transporter would show multiple transmembrane helices, a P450-type lyase would contain a heme-binding Cys motif, and a muconolactone isomerase is a small α/β protein with entirely different sequence features. The GH10 motifs are transferable family-level knowledge that meaningfully and uniquely selects option D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH10 xylanase signature motifs (WHSPEFG, WDFYDPFSWVPY) are well-documented across many characterized xylanases and constitute a concrete, transferable sequence feature that distinguishes a xylanase from an isomerase, a transporter, or a hydroperoxide lyase. No target-specific annotation lookup is required; family-level recognition suffices."
  },
  "case_id": "catalytic_activity_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry M4MGK7 (XYNA_HUMIN) annotates this sequence as Endo-1,4-beta-xylanase A (EC 3.2.1.8) from Humicola insolens, with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The annotation is backed by experimental evidence (ECO:0000269, PubMed:23306124, a 2013 Bioresour. Technol. paper characterizing three thermophilic xylanases from H. insolens Y1). The sequence in the benchmark matches the UniProt sequence exactly (SHA256 match confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental characterization (PubMed:23306124), not merely computational inference.",
    "The 'WHSPEFG' motif is a strong but not absolutely universal GH10 marker; some GH10 variants show minor substitutions. However, combined with 'WDFYDPFSWVPY' and overall sequence architecture, the family assignment is robust.",
    "The reviewer-only evidence confirms sequence identity to M4MGK7, but this accession was not provided to the evaluated model; the reasoning above relies solely on the raw sequence and transferable family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes (isomerase, membrane transporter, hydroperoxide lyase, glycoside hydrolase). The GH10-specific motifs unambiguously select the xylanase option and exclude the others."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry M4MGK7 (XYNA_HUMIN) annotates this sequence as Endo-1,4-beta-xylanase A (EC 3.2.1.8) from Humicola insolens, with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The annotation is backed by experimental evidence (ECO:0000269, PubMed:23306124, a 2013 Bioresour. Technol. paper characterizing three thermophilic xylanases from H. insolens Y1). The sequence in the benchmark matches the UniProt sequence exactly (SHA256 match confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark 'WHSPEFG' motif (residues ~70-76) and the 'WDFYDPFSWVPY' motif (residues ~295-307), both well-established signatures of glycoside hydrolase family 10 (GH10) xylanases. The 'WHSPEFG' motif harbors the catalytic acid/base glutamic acid, while 'WDFYDPFSWVPY' contains the catalytic nucleophile glutamic acid. These motifs are conserved across dozens of characterized GH10 xylanases from fungi and bacteria and are the primary sequence-level diagnostic for this family. Additionally, the N-terminal hydrophobic signal peptide (MHLASSLFLLATLPFGFAAG) followed by a short linker (GKGKGKGK) is consistent with a secreted fungal xylanase. None of the other options (muconolactone isomerase, cobalt transporter, hydroperoxide lyase) share any of these motifs or fold characteristics: a transporter would show multiple transmembrane helices, a P450-type lyase would contain a heme-binding Cys motif, and a muconolactone isomerase is a small α/β protein with entirely different sequence features. The GH10 motifs are transferable family-level knowledge that meaningfully and uniquely selects option D.",
    "missing_item_specific_fact": "",
    "reason": "The GH10 xylanase signature motifs (WHSPEFG, WDFYDPFSWVPY) are well-documented across many characterized xylanases and constitute a concrete, transferable sequence feature that distinguishes a xylanase from an isomerase, a transporter, or a hydroperoxide lyase. No target-specific annotation lookup is required; family-level recognition suffices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes (isomerase, membrane transporter, hydroperoxide lyase, glycoside hydrolase). The GH10-specific motifs unambiguously select the xylanase option and exclude the others."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental characterization (PubMed:23306124), not merely computational inference.",
    "The 'WHSPEFG' motif is a strong but not absolutely universal GH10 marker; some GH10 variants show minor substitutions. However, combined with 'WDFYDPFSWVPY' and overall sequence architecture, the family assignment is robust.",
    "The reviewer-only evidence confirms sequence identity to M4MGK7, but this accession was not provided to the evaluated model; the reasoning above relies solely on the raw sequence and transferable family knowledge."
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
  "benchmark_sequence_length": 376,
  "benchmark_sequence_sha256": "099e0d9d31b95aad01d9114eec635a5ba258509622920c5ebd279553304abc33",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 376,
  "current_source_sequence_sha256": "099e0d9d31b95aad01d9114eec635a5ba258509622920c5ebd279553304abc33",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "M4MGK7",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "selected_historical_source_sequence_length": 376,
  "selected_historical_source_sequence_sha256": "099e0d9d31b95aad01d9114eec635a5ba258509622920c5ebd279553304abc33",
  "selected_historical_version": {
    "accession": "M4MGK7",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XYNA_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"M4MGK7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase A\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Du Y.\",\"Shi P.\",\"Huang H.\",\"Zhang X.\",\"Luo H.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23306124\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biortech.2012.12.067\"}],\"citationType\":\"journal article\",\"firstPage\":\"161\",\"id\":\"23306124\",\"journal\":\"Bioresour. Technol.\",\"lastPage\":\"167\",\"publicationDate\":\"2013\",\"title\":\"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.\",\"volume\":\"130\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   XYNA_HUMIN              Reviewed;         376 AA.\nAC   M4MGK7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2013, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Endo-1,4-beta-xylanase A {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase A {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=XynA {ECO:0000303|PubMed:23306124};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Endo-1,4-beta-xylanase A {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase A {ECO:0000305};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;\nRA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;\nRT   \"Characterization of three novel thermophilic xylanases from Humicola\nRT   insolens Y1 with application potentials in the brewing industry.\";\nRL   Bioresour. Technol. 130:161-167(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:23306124};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 159. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
