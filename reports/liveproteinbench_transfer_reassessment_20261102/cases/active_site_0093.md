# active_site_0093

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0093.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 176 (Proton donor/acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKPHNSEKYFVKNGQPHFLISGEVHYFRINPKLWRNHLQLLKQTGADTVSTYIPWDWHEIEEDDFDFEGKTHPARNLIRFIKLCKEENLDLIVKPGPYILAEYENQGLPSWLLKKLSKNAFALDENGNVISPDLVSYLSDEFLEYTFKWYDKVMPIISKHQKEHYGPITMMQLCNEIGVFQWLSGKSDYNPKVINLYKEFIIQRYKTIEKLNSVYSTNYNSFDDLKAPSGKIKLRSDYCAYFDFHLFFREYYNKYISILKNKIRSFGINIKLTHNIPGWIYGNASELPMLISTYSEIMKNHPDIIFGLDHIPEFVSFRNAHSDLACNKILEAMQPEAPVWAAEFQAGTREHHVKAYAKDLETFYIASLAHGIKGFNYYMFSQGINPEGKGFYGKTFYFQTALDAASNKLALYDSIKKVNRFIRKEQKDLLRTNVNSEICVGFYKPYFFTELISSQLLKEKKLNVEELGLYIDPRFLREEILFNGLLRGLQTLNYNYDVVDLENCDLKSLTAYKQLWITSAEFMDAETQNLLSEFVLNGGNLILYPAVPTLDNYLNRCEILKNNFGIEFITKDSSHKVSAFGIEDVFTAFSKKQIYNDTNSKPIAFTQENEICGIRKKIGKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQFVVRENNKSRYIFFLNYHNERKTFNYRKSSELKKKKSEEISIAPFSYKVIKENK

[Multiple Choices]
A. Position 359 (For beta-ketoacyl synthase activity)
B. Position 2056 (For beta-ketoacyl synthase 2 activity)
C. Position 176 (Proton donor/acceptor)
D. Position 662 (For acyltransferase activity of LM)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies residue 176 as an active-site proton donor/acceptor. The cited paper also concerns active-site analysis and mutagenesis of Glu-176 and Glu-343. This supports C as a catalytic residue, though it does not mean residue 176 is the entire active site.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C26](#evidence-c26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The target-specific assignment of residue 176 as the proton donor/acceptor, established by its active-site annotation and supporting structural or mutagenesis work.


**Reason**

> The sequence reveals residues and their positions, but does not by itself establish which one performs proton transfer. A general expectation that acidic residues can act as acid/base catalysts does not distinguish position 176 from other acidic residues without a recognizable family-level feature or alignment that identifies this catalytic position. The alternative activity labels may look implausible, but that alone does not establish the exact target-specific assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports C among the offered choices. Other catalytic residues are annotated for this protein, but no other offered option is identified as a defensible alternative for the stated proton donor/acceptor role.


### Important caveats

- The active-site annotation is curator-attributed evidence linked to a paper; the excerpts do not independently reproduce the experimental results.
- The annotated active site includes another catalytic residue, so the keyed option should be understood as identifying one active-site residue, not a complete catalytic center.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The target-specific assignment of residue 176 as the proton donor/acceptor, established by its active-site annotation and supporting structural or mutagenesis work.",
    "reason": "The sequence reveals residues and their positions, but does not by itself establish which one performs proton transfer. A general expectation that acidic residues can act as acid/base catalysts does not distinguish position 176 from other acidic residues without a recognizable family-level feature or alignment that identifies this catalytic position. The alternative activity labels may look implausible, but that alone does not establish the exact target-specific assignment."
  },
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C26"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 176 as an active-site proton donor/acceptor. The cited paper also concerns active-site analysis and mutagenesis of Glu-176 and Glu-343. This supports C as a catalytic residue, though it does not mean residue 176 is the entire active site."
  },
  "important_caveats": [
    "The active-site annotation is curator-attributed evidence linked to a paper; the excerpts do not independently reproduce the experimental results.",
    "The annotated active site includes another catalytic residue, so the keyed option should be understood as identifying one active-site residue, not a complete catalytic center."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C among the offered choices. Other catalytic residues are annotated for this protein, but no other offered option is identified as a defensible alternative for the stated proton donor/acceptor role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 176 as an active-site proton donor/acceptor. The cited paper also concerns active-site analysis and mutagenesis of Glu-176 and Glu-343. This supports C as a catalytic residue, though it does not mean residue 176 is the entire active site.",
    "evidence_ids": ["C5", "H3", "C26"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The target-specific assignment of residue 176 as the proton donor/acceptor, established by its active-site annotation and supporting structural or mutagenesis work.",
    "reason": "The sequence reveals residues and their positions, but does not by itself establish which one performs proton transfer. A general expectation that acidic residues can act as acid/base catalysts does not distinguish position 176 from other acidic residues without a recognizable family-level feature or alignment that identifies this catalytic position. The alternative activity labels may look implausible, but that alone does not establish the exact target-specific assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C among the offered choices. Other catalytic residues are annotated for this protein, but no other offered option is identified as a defensible alternative for the stated proton donor/acceptor role."
  },
  "important_caveats": [
    "The active-site annotation is curator-attributed evidence linked to a paper; the excerpts do not independently reproduce the experimental results.",
    "The annotated active site includes another catalytic residue, so the keyed option should be understood as identifying one active-site residue, not a complete catalytic center."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (I0AIT9, sequence matched) annotates position 176 as 'Active site' with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074). The reference (PubMed:35065074) explicitly includes 'MUTAGENESIS OF GLU-176 AND GLU-343' and X-ray crystallography data, confirming experimental support. The residue at position 176 in the supplied sequence is indeed Glutamic acid (E), consistent with the annotation.

Citations as saved: [C5](#evidence-c5), [C26](#evidence-c26), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three elimination arguments distinguish C from the other options using transferable knowledge: (1) Option B (position 2056) is immediately impossible because the supplied sequence is only 716 residues long—any model can count or estimate sequence length. (2) Option A ('For beta-ketoacyl synthase activity') and Option D ('For acyltransferase activity of LM') carry functional annotations belonging to entirely different enzyme families. Beta-ketoacyl synthase (FabZ/FasB) is a ~400-residue thiolase-fold enzyme with a conserved Cys-His-His catalytic triad; acyltransferases feature a GxSxG serine nucleophile motif. The 716-residue sequence here matches neither family's characteristic architecture or motifs. (3) Option C ('Proton donor/acceptor') describes a generic catalytic role (general acid/base) consistent with glycosyltransferase chemistry, where Glu/Asp residues serve as proton shuttlers. Position 176 is indeed a Glutamic acid in the sequence. By elimination of the three clearly incompatible options, C is the only viable answer.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of B is trivial (position exceeds sequence length). The elimination of A and D relies on recognizing that their functional descriptions belong to well-known but unrelated enzyme families (fatty acid synthase thiolase, serine acyltransferase), which is standard transferable biochemistry knowledge. The remaining option C has a generic catalytic description compatible with the protein's likely function. No protein-specific database lookup is strictly required to reach C by elimination among the four offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only C is positionally valid and functionally consistent with the protein. B is impossible by sequence length; A and D describe activities of incompatible enzyme families. No ambiguity exists among the offered alternatives.


### Important caveats

- The UniProt entry also annotates position 343 (Glu, 'Nucleophile') as a second active site, but this is not offered as a choice, so it does not create ambiguity among the provided options.
- The elimination of A and D depends on the model recognizing that 'beta-ketoacyl synthase' and 'acyltransferase of LM' are specific annotations from other protein contexts rather than plausible descriptions for this sequence. A model unfamiliar with these enzyme families might struggle with this elimination step.
- The reviewer-only evidence confirms the protein is a Beta-1,2-glucosyltransferase (EC 2.4.1.391) from Ignavibacterium album, but this identity was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three elimination arguments distinguish C from the other options using transferable knowledge: (1) Option B (position 2056) is immediately impossible because the supplied sequence is only 716 residues long—any model can count or estimate sequence length. (2) Option A ('For beta-ketoacyl synthase activity') and Option D ('For acyltransferase activity of LM') carry functional annotations belonging to entirely different enzyme families. Beta-ketoacyl synthase (FabZ/FasB) is a ~400-residue thiolase-fold enzyme with a conserved Cys-His-His catalytic triad; acyltransferases feature a GxSxG serine nucleophile motif. The 716-residue sequence here matches neither family's characteristic architecture or motifs. (3) Option C ('Proton donor/acceptor') describes a generic catalytic role (general acid/base) consistent with glycosyltransferase chemistry, where Glu/Asp residues serve as proton shuttlers. Position 176 is indeed a Glutamic acid in the sequence. By elimination of the three clearly incompatible options, C is the only viable answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of B is trivial (position exceeds sequence length). The elimination of A and D relies on recognizing that their functional descriptions belong to well-known but unrelated enzyme families (fatty acid synthase thiolase, serine acyltransferase), which is standard transferable biochemistry knowledge. The remaining option C has a generic catalytic description compatible with the protein's likely function. No protein-specific database lookup is strictly required to reach C by elimination among the four offered choices."
  },
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C26",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (I0AIT9, sequence matched) annotates position 176 as 'Active site' with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074). The reference (PubMed:35065074) explicitly includes 'MUTAGENESIS OF GLU-176 AND GLU-343' and X-ray crystallography data, confirming experimental support. The residue at position 176 in the supplied sequence is indeed Glutamic acid (E), consistent with the annotation."
  },
  "important_caveats": [
    "The UniProt entry also annotates position 343 (Glu, 'Nucleophile') as a second active site, but this is not offered as a choice, so it does not create ambiguity among the provided options.",
    "The elimination of A and D depends on the model recognizing that 'beta-ketoacyl synthase' and 'acyltransferase of LM' are specific annotations from other protein contexts rather than plausible descriptions for this sequence. A model unfamiliar with these enzyme families might struggle with this elimination step.",
    "The reviewer-only evidence confirms the protein is a Beta-1,2-glucosyltransferase (EC 2.4.1.391) from Ignavibacterium album, but this identity was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only C is positionally valid and functionally consistent with the protein. B is impossible by sequence length; A and D describe activities of incompatible enzyme families. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (I0AIT9, sequence matched) annotates position 176 as 'Active site' with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074). The reference (PubMed:35065074) explicitly includes 'MUTAGENESIS OF GLU-176 AND GLU-343' and X-ray crystallography data, confirming experimental support. The residue at position 176 in the supplied sequence is indeed Glutamic acid (E), consistent with the annotation.",
    "evidence_ids": ["C5", "C26", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three elimination arguments distinguish C from the other options using transferable knowledge: (1) Option B (position 2056) is immediately impossible because the supplied sequence is only 716 residues long—any model can count or estimate sequence length. (2) Option A ('For beta-ketoacyl synthase activity') and Option D ('For acyltransferase activity of LM') carry functional annotations belonging to entirely different enzyme families. Beta-ketoacyl synthase (FabZ/FasB) is a ~400-residue thiolase-fold enzyme with a conserved Cys-His-His catalytic triad; acyltransferases feature a GxSxG serine nucleophile motif. The 716-residue sequence here matches neither family's characteristic architecture or motifs. (3) Option C ('Proton donor/acceptor') describes a generic catalytic role (general acid/base) consistent with glycosyltransferase chemistry, where Glu/Asp residues serve as proton shuttlers. Position 176 is indeed a Glutamic acid in the sequence. By elimination of the three clearly incompatible options, C is the only viable answer.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of B is trivial (position exceeds sequence length). The elimination of A and D relies on recognizing that their functional descriptions belong to well-known but unrelated enzyme families (fatty acid synthase thiolase, serine acyltransferase), which is standard transferable biochemistry knowledge. The remaining option C has a generic catalytic description compatible with the protein's likely function. No protein-specific database lookup is strictly required to reach C by elimination among the four offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only C is positionally valid and functionally consistent with the protein. B is impossible by sequence length; A and D describe activities of incompatible enzyme families. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The UniProt entry also annotates position 343 (Glu, 'Nucleophile') as a second active site, but this is not offered as a choice, so it does not create ambiguity among the provided options.",
    "The elimination of A and D depends on the model recognizing that 'beta-ketoacyl synthase' and 'acyltransferase of LM' are specific annotations from other protein contexts rather than plausible descriptions for this sequence. A model unfamiliar with these enzyme families might struggle with this elimination step.",
    "The reviewer-only evidence confirms the protein is a Beta-1,2-glucosyltransferase (EC 2.4.1.391) from Ignavibacterium album, but this identity was not provided to the evaluated model."
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
  "benchmark_sequence_length": 716,
  "benchmark_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "current_entry_audit": {
    "entryVersion": 57,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-06-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 716,
  "current_source_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "I0AIT9",
  "selected_historical_entry_version": 55,
  "selected_historical_record_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "selected_historical_source_sequence_length": 716,
  "selected_historical_source_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "selected_historical_version": {
    "accession": "I0AIT9",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "B12GT_IGNAJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"I0AIT9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":57,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-06-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Ignavibacteriota\",\"Ignavibacteria\",\"Ignavibacteriales\",\"Ignavibacteriaceae\",\"Ignavibacterium\"],\"scientificName\":\"Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16)\",\"taxonId\":945713}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"IaSGT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.391\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Beta-1,2-glucosyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor/acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":176},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":343},\"start\":{\"modifier\":\"EXACT\",\"value\":343}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":52},\"start\":{\"modifier\":\"EXACT\",\"value\":52}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":99},\"start\":{\"modifier\":\"EXACT\",\"value\":99}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":101},\"start\":{\"modifier\":\"EXACT\",\"value\":101}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":102},\"start\":{\"modifier\":\"EXACT\",\"value\":102}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":175},\"start\":{\"modifier\":\"EXACT\",\"value\":175}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"1\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":176},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":176},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"1\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":278},\"start\":{\"modifier\":\"EXACT\",\"value\":278}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":278},\"start\":{\"modifier\":\"EXACT\",\"value\":278}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"1\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":279},\"start\":{\"modifier\":\"EXACT\",\"value\":279}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":279},\"start\":{\"modifier\":\"EXACT\",\"value\":279}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":343},\"start\":{\"modifier\":\"EXACT\",\"value\":343}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"1\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":349},\"start\":{\"modifier\":\"EXACT\",\"value\":349}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":349},\"start\":{\"modifier\":\"EXACT\",\"value\":349}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"2\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":358},\"start\":{\"modifier\":\"EXACT\",\"value\":358}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"2\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":361},\"start\":{\"modifier\":\"EXACT\",\"value\":361}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":378},\"start\":{\"modifier\":\"EXACT\",\"value\":378}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"2\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":708},\"start\":{\"modifier\":\"EXACT\",\"value\":708}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"2\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":709},\"start\":{\"modifier\":\"EXACT\",\"value\":709}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"citation\":{\"authors\":[\"Kobayashi K.\",\"Shimizu H.\",\"Tanaka N.\",\"Kuramochi K.\",\"Nakai H.\",\"Nakajima M.\",\"Taguchi H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35065074\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2022.101606\"}],\"citationType\":\"journal article\",\"firstPage\":\"101606\",\"id\":\"35065074\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"101606\",\"publicationDate\":\"2022\",\"title\":\"Characterization and structural analyses of a novel glycosyltransferase acting on the beta-1,2-glucosidic linkages.\",\"volume\":\"298\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKW\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL0\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL1\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL3\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL4\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL6\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE; SOPHOROSE AND ALTERNATIVE SUBSTRATES\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"ACTIVE SITE\",\"MUTAGENESIS OF GLU-176 AND GLU-343\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H1",
  "excerpt": "ID   B12GT_IGNAJ             Reviewed;         716 AA.\nAC   I0AIT9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-JUN-2012, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};\nDE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};\nGN   OrderedLocusNames=IALB_1185 {ECO:0000312|EMBL:AFH48896.1};\nOS   Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 /\nOS   Mat9-16).\nOC   Bacteria; Pseudomonadati; Ignavibacteriota; Ignavibacteria;\nOC   Ignavibacteriales; Ignavibacteriaceae; Ignavibacterium.\nOX   NCBI_TaxID=945713;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7VKW, ECO:0007744|PDB:7VKX, ECO:0007744|PDB:7VKY, ECO:0007744|PDB:7VKZ, ECO:0007744|PDB:7VL0, ECO:0007744|PDB:7VL1, ECO:0007744|PDB:7VL2, ECO:0007744|PDB:7VL3, ECO:0007744|PDB:7VL4, ECO:0007744|PDB:7VL5, ECO:0007744|PDB:7VL6}\nRP   X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE;\nRP   SOPHOROSE AND ALTERNATIVE SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF\nRP   GLU-176 AND GLU-343.\nRC   STRAIN=DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16;\nRX   PubMed=35065074; DOI=10.1016/j.jbc.2022.101606;\nRA   Kobayashi K., Shimizu H., Tanaka N., Kuramochi K., Nakai H., Nakajima M.,\nRA   Taguchi H.;\nRT   \"Characterization and structural analyses of a novel glycosyltransferase\nRT   acting on the beta-1,2-glucosidic linkages.\";\nRL   J. Biol. Chem. 298:101606-101606(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        176\nFT                   /note=\"Proton donor/acceptor\"\nFT                   /evidence=\"ECO:0000305|PubMed:35065074\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 159-161",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        343\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000305|PubMed:35065074\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-164",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         52\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 165-169",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         99\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 170-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         101\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 175-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         102\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 180-184",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         175\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 185-189",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         176\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 190-195",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         176\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 196-200",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         278\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 201-206",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         278\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 207-211",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         279\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 212-217",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H15",
  "excerpt": "FT   BINDING         279\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 218-222",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H16",
  "excerpt": "FT   BINDING         343\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 223-227",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H17",
  "excerpt": "FT   BINDING         349\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 228-233",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H18",
  "excerpt": "FT   BINDING         349\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 234-238",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H19",
  "excerpt": "FT   BINDING         358\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 239-244",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H20",
  "excerpt": "FT   BINDING         361\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 245-250",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H21",
  "excerpt": "FT   BINDING         378\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 251-255",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H22",
  "excerpt": "FT   BINDING         708\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 256-261",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H23",
  "excerpt": "FT   BINDING         709\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 262-267",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
