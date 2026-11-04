# GO_molecular_function_0147

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0147.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — 2 iron, 2 sulfur cluster binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKSKILCNLFKGKSCICLYTNCLNENNVNKCYYNLVRNYSDHVKDHFNKPRNVGSFDKNEKNIGTSIVGKASCGDVIKLQLKIENDVIKDARFMAFGCGSAIASSSYATELIKGKTIDEALKIKNNDIASHLSLPPVKIHCSLLAEDAIKHAIKNYREKVLT

[Multiple Choices]
A. estradiol 17-beta-dehydrogenase [NAD(P)+] activity
B. tau protein binding
C. beta-amyrin synthase activity
D. 2 iron, 2 sulfur cluster binding
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

> The sequence-matched record identifies the protein as IscU, an iron-sulfur assembly scaffold, and annotates 2Fe-2S cluster binding. The specific GO annotation is phylogenetically inferred (IBA), while the cited experimental function supports its broader role in Fe-S cluster assembly; it does not by itself establish direct experimental measurement of 2Fe-2S binding.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 162-residue sequence has a compact, cysteine-rich pattern consistent with an IscU-like Fe-S scaffold. IscU-family proteins bind and help assemble iron-sulfur clusters, making D a meaningful match; the alternatives describe unrelated activities and are not suggested by this sequence or family pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence features and transferable knowledge of IscU-like scaffolds distinguishes D without needing the target's exact database annotation. The inference supports Fe-S cluster binding generally; the exact cluster type is less certain from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only offered option consistent with an IscU-like Fe-S scaffold. The scaffold can be associated with different cluster types, but no other offered option captures that function.


### Important caveats

- The specific 2Fe-2S GO annotation is IBA, a phylogenetic inference, not direct experimental evidence in the supplied excerpts.
- The cited experimental description emphasizes assembly and transfer of 4Fe-4S clusters, so it supports the broader Fe-S function more directly than the exact 2Fe-2S specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 162-residue sequence has a compact, cysteine-rich pattern consistent with an IscU-like Fe-S scaffold. IscU-family proteins bind and help assemble iron-sulfur clusters, making D a meaningful match; the alternatives describe unrelated activities and are not suggested by this sequence or family pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features and transferable knowledge of IscU-like scaffolds distinguishes D without needing the target's exact database annotation. The inference supports Fe-S cluster binding generally; the exact cluster type is less certain from sequence alone."
  },
  "case_id": "GO_molecular_function_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as IscU, an iron-sulfur assembly scaffold, and annotates 2Fe-2S cluster binding. The specific GO annotation is phylogenetically inferred (IBA), while the cited experimental function supports its broader role in Fe-S cluster assembly; it does not by itself establish direct experimental measurement of 2Fe-2S binding."
  },
  "important_caveats": [
    "The specific 2Fe-2S GO annotation is IBA, a phylogenetic inference, not direct experimental evidence in the supplied excerpts.",
    "The cited experimental description emphasizes assembly and transfer of 4Fe-4S clusters, so it supports the broader Fe-S function more directly than the exact 2Fe-2S specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered option consistent with an IscU-like Fe-S scaffold. The scaffold can be associated with different cluster types, but no other offered option captures that function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as IscU, an iron-sulfur assembly scaffold, and annotates 2Fe-2S cluster binding. The specific GO annotation is phylogenetically inferred (IBA), while the cited experimental function supports its broader role in Fe-S cluster assembly; it does not by itself establish direct experimental measurement of 2Fe-2S binding.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 162-residue sequence has a compact, cysteine-rich pattern consistent with an IscU-like Fe-S scaffold. IscU-family proteins bind and help assemble iron-sulfur clusters, making D a meaningful match; the alternatives describe unrelated activities and are not suggested by this sequence or family pattern.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features and transferable knowledge of IscU-like scaffolds distinguishes D without needing the target's exact database annotation. The inference supports Fe-S cluster binding generally; the exact cluster type is less certain from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered option consistent with an IscU-like Fe-S scaffold. The scaffold can be associated with different cluster types, but no other offered option captures that function."
  },
  "important_caveats": [
    "The specific 2Fe-2S GO annotation is IBA, a phylogenetic inference, not direct experimental evidence in the supplied excerpts.",
    "The cited experimental description emphasizes assembly and transfer of 4Fe-4S clusters, so it supports the broader Fe-S function more directly than the exact 2Fe-2S specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IKT4 (IscU, Iron-sulfur cluster assembly protein from Plasmodium falciparum) carries GO:0051537 (2 iron, 2 sulfur cluster binding) with IBA:GO_Central evidence. The protein's experimentally confirmed function (PubMed:34032321, ECO:0000269) is scaffold for Fe-S cluster assembly. The 2Fe-2S binding annotation is present in the database. Note that the entry also carries GO:0051539 (4Fe-4S binding) via IEA keyword, and the function comment emphasizes &#91;4Fe-4S&#93; assembly, but the 2Fe-2S annotation is explicitly listed and the question offers only the 2Fe-2S option among the four choices.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 162-residue sequence contains at least 6-7 cysteine residues (positions ~6, 15, 17, 26, 64, 145) with spacing patterns including a conserved 'CG' motif (in 'ASCGD') and a 'GCG' motif, which are hallmarks of Fe-S cluster coordination proteins, particularly the IscU scaffold family. Transferable knowledge about Fe-S cluster proteins indicates that dense, regularly spaced cysteines in a compact (~130-160 aa) protein strongly suggest Fe-S cluster binding. This immediately eliminates: (C) beta-amyrin synthase, which requires a ~750+ residue oxidosqualene cyclase fold with multiple transmembrane helices; (A) estradiol 17β-dehydrogenase, which requires a Rossmann fold with GxGxxG-type NAD(P) binding motifs absent here; and (B) tau protein binding, which typically involves larger cytoskeletal-interaction domains. Among the four options, only D (Fe-S cluster binding) is consistent with a small cysteine-rich protein lacking dehydrogenase or cyclase motifs. The model need not distinguish 2Fe-2S from 4Fe-4S since only one Fe-S option is offered.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The cysteine density and spacing, the CG/GCG motifs, the compact 162-aa size, and the absence of Rossmann or cyclase fold signatures allow a knowledgeable model to identify this as an Fe-S cluster scaffold protein (IscU-like) and select D over the three clearly incompatible alternatives using family-level and structural knowledge transferable from other Fe-S proteins, dehydrogenases, and cyclases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors are eliminated by fundamental incompatibilities: beta-amyrin synthase requires a much larger protein with cyclase folds; estradiol 17β-dehydrogenase requires a Rossmann fold with NAD(P) motifs; tau binding requires cytoskeletal-interaction domains. Only D is consistent with a small cysteine-rich protein. The 2Fe-2S vs 4Fe-4S distinction is moot since only 2Fe-2S is offered.


### Important caveats

- The GO:0051537 annotation uses IBA (inferred by biological aspect) evidence, a computational inference from GO_Central rather than direct experimental measurement of 2Fe-2S binding on this specific protein.
- The UniProt entry also annotates GO:0051539 (4Fe-4S binding) via IEA keyword, and the experimental function comment emphasizes &#91;4Fe-4S&#93; assembly. IscU can bind both cluster types depending on conditions.
- The sequence is from Plasmodium falciparum (a eukaryote with a divergent IscU); the cysteine spacing differs from the canonical bacterial IscU CxxxC motif, but the overall CG/GCG motifs and cysteine density remain diagnostic.
- The reviewer-only evidence confirms the protein identity, but the model's reasoning must rely on sequence features and transferable family knowledge, which is sufficient here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 162-residue sequence contains at least 6-7 cysteine residues (positions ~6, 15, 17, 26, 64, 145) with spacing patterns including a conserved 'CG' motif (in 'ASCGD') and a 'GCG' motif, which are hallmarks of Fe-S cluster coordination proteins, particularly the IscU scaffold family. Transferable knowledge about Fe-S cluster proteins indicates that dense, regularly spaced cysteines in a compact (~130-160 aa) protein strongly suggest Fe-S cluster binding. This immediately eliminates: (C) beta-amyrin synthase, which requires a ~750+ residue oxidosqualene cyclase fold with multiple transmembrane helices; (A) estradiol 17β-dehydrogenase, which requires a Rossmann fold with GxGxxG-type NAD(P) binding motifs absent here; and (B) tau protein binding, which typically involves larger cytoskeletal-interaction domains. Among the four options, only D (Fe-S cluster binding) is consistent with a small cysteine-rich protein lacking dehydrogenase or cyclase motifs. The model need not distinguish 2Fe-2S from 4Fe-4S since only one Fe-S option is offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The cysteine density and spacing, the CG/GCG motifs, the compact 162-aa size, and the absence of Rossmann or cyclase fold signatures allow a knowledgeable model to identify this as an Fe-S cluster scaffold protein (IscU-like) and select D over the three clearly incompatible alternatives using family-level and structural knowledge transferable from other Fe-S proteins, dehydrogenases, and cyclases."
  },
  "case_id": "GO_molecular_function_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IKT4 (IscU, Iron-sulfur cluster assembly protein from Plasmodium falciparum) carries GO:0051537 (2 iron, 2 sulfur cluster binding) with IBA:GO_Central evidence. The protein's experimentally confirmed function (PubMed:34032321, ECO:0000269) is scaffold for Fe-S cluster assembly. The 2Fe-2S binding annotation is present in the database. Note that the entry also carries GO:0051539 (4Fe-4S binding) via IEA keyword, and the function comment emphasizes [4Fe-4S] assembly, but the 2Fe-2S annotation is explicitly listed and the question offers only the 2Fe-2S option among the four choices."
  },
  "important_caveats": [
    "The GO:0051537 annotation uses IBA (inferred by biological aspect) evidence, a computational inference from GO_Central rather than direct experimental measurement of 2Fe-2S binding on this specific protein.",
    "The UniProt entry also annotates GO:0051539 (4Fe-4S binding) via IEA keyword, and the experimental function comment emphasizes [4Fe-4S] assembly. IscU can bind both cluster types depending on conditions.",
    "The sequence is from Plasmodium falciparum (a eukaryote with a divergent IscU); the cysteine spacing differs from the canonical bacterial IscU CxxxC motif, but the overall CG/GCG motifs and cysteine density remain diagnostic.",
    "The reviewer-only evidence confirms the protein identity, but the model's reasoning must rely on sequence features and transferable family knowledge, which is sufficient here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are eliminated by fundamental incompatibilities: beta-amyrin synthase requires a much larger protein with cyclase folds; estradiol 17β-dehydrogenase requires a Rossmann fold with NAD(P) motifs; tau binding requires cytoskeletal-interaction domains. Only D is consistent with a small cysteine-rich protein. The 2Fe-2S vs 4Fe-4S distinction is moot since only 2Fe-2S is offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IKT4 (IscU, Iron-sulfur cluster assembly protein from Plasmodium falciparum) carries GO:0051537 (2 iron, 2 sulfur cluster binding) with IBA:GO_Central evidence. The protein's experimentally confirmed function (PubMed:34032321, ECO:0000269) is scaffold for Fe-S cluster assembly. The 2Fe-2S binding annotation is present in the database. Note that the entry also carries GO:0051539 (4Fe-4S binding) via IEA keyword, and the function comment emphasizes [4Fe-4S] assembly, but the 2Fe-2S annotation is explicitly listed and the question offers only the 2Fe-2S option among the four choices.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 162-residue sequence contains at least 6-7 cysteine residues (positions ~6, 15, 17, 26, 64, 145) with spacing patterns including a conserved 'CG' motif (in 'ASCGD') and a 'GCG' motif, which are hallmarks of Fe-S cluster coordination proteins, particularly the IscU scaffold family. Transferable knowledge about Fe-S cluster proteins indicates that dense, regularly spaced cysteines in a compact (~130-160 aa) protein strongly suggest Fe-S cluster binding. This immediately eliminates: (C) beta-amyrin synthase, which requires a ~750+ residue oxidosqualene cyclase fold with multiple transmembrane helices; (A) estradiol 17β-dehydrogenase, which requires a Rossmann fold with GxGxxG-type NAD(P) binding motifs absent here; and (B) tau protein binding, which typically involves larger cytoskeletal-interaction domains. Among the four options, only D (Fe-S cluster binding) is consistent with a small cysteine-rich protein lacking dehydrogenase or cyclase motifs. The model need not distinguish 2Fe-2S from 4Fe-4S since only one Fe-S option is offered.",
    "missing_item_specific_fact": "",
    "reason": "The cysteine density and spacing, the CG/GCG motifs, the compact 162-aa size, and the absence of Rossmann or cyclase fold signatures allow a knowledgeable model to identify this as an Fe-S cluster scaffold protein (IscU-like) and select D over the three clearly incompatible alternatives using family-level and structural knowledge transferable from other Fe-S proteins, dehydrogenases, and cyclases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are eliminated by fundamental incompatibilities: beta-amyrin synthase requires a much larger protein with cyclase folds; estradiol 17β-dehydrogenase requires a Rossmann fold with NAD(P) motifs; tau binding requires cytoskeletal-interaction domains. Only D is consistent with a small cysteine-rich protein. The 2Fe-2S vs 4Fe-4S distinction is moot since only 2Fe-2S is offered."
  },
  "important_caveats": [
    "The GO:0051537 annotation uses IBA (inferred by biological aspect) evidence, a computational inference from GO_Central rather than direct experimental measurement of 2Fe-2S binding on this specific protein.",
    "The UniProt entry also annotates GO:0051539 (4Fe-4S binding) via IEA keyword, and the experimental function comment emphasizes [4Fe-4S] assembly. IscU can bind both cluster types depending on conditions.",
    "The sequence is from Plasmodium falciparum (a eukaryote with a divergent IscU); the cysteine spacing differs from the canonical bacterial IscU CxxxC motif, but the overall CG/GCG motifs and cysteine density remain diagnostic.",
    "The reviewer-only evidence confirms the protein identity, but the model's reasoning must rely on sequence features and transferable family knowledge, which is sufficient here."
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
  "benchmark_sequence_length": 162,
  "benchmark_sequence_sha256": "8e140c4dbd21b2ba798ee3b637384532a5902af39272bee7a18981ab9ceabe88",
  "current_entry_audit": {
    "entryVersion": 125,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 162,
  "current_source_sequence_sha256": "8e140c4dbd21b2ba798ee3b637384532a5902af39272bee7a18981ab9ceabe88",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 123,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IKT4",
  "selected_historical_entry_version": 123,
  "selected_historical_record_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "selected_historical_source_sequence_length": 162,
  "selected_historical_source_sequence_sha256": "8e140c4dbd21b2ba798ee3b637384532a5902af39272bee7a18981ab9ceabe88",
  "selected_historical_version": {
    "accession": "Q8IKT4",
    "database": "Swiss-Prot",
    "entryVersion": 123,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ISCU_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IKT4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":125,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Iron-sulfur cluster assembly protein IscU\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"PfIscU\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"Participates in iron-sulfur cluster formation (ISC) pathway for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Plays a role of a major scaffold protein for [Fe-S] assembly; assembles [4Fe-4S] clusters directly upon interaction with the catalytic component IscS-Isd11 as part of the scaffold complex (PubMed:34032321). Can transfer [4Fe-4S] clusters to target apo-proteins (PubMed:34032321)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0051537\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:2 iron, 2 sulfur cluster binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/21",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0008198\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:ferrous iron binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/22",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"12368867\",\"source\":\"PubMed\"}],\"id\":\"GO:0005506\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:iron ion binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:GeneDB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/23",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Sadik M.\",\"Afsar M.\",\"Ramachandran R.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34032321\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.14735\"}],\"citationType\":\"journal article\",\"firstPage\":\"606\",\"id\":\"34032321\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"623\",\"publicationDate\":\"2021\",\"title\":\"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"COFACTOR\",\"SUBUNIT\",\"INTERACTION WITH ISCS\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:18.665288+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IKT4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H1",
  "excerpt": "ID   ISCU_PLAF7              Reviewed;         162 AA.\nAC   Q8IKT4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 123.\nDE   RecName: Full=Iron-sulfur cluster assembly protein IscU {ECO:0000305};\nDE            Short=PfIscU {ECO:0000303|PubMed:34032321};\nGN   Name=IscU {ECO:0000305};\nGN   ORFNames=PF3D7_1454500 {ECO:0000312|EMBL:CZU00240.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, COFACTOR, SUBUNIT, INTERACTION WITH ISCS, AND SUBCELLULAR\nRP   LOCATION.\nRX   PubMed=34032321; DOI=10.1111/mmi.14735;\nRA   Sadik M., Afsar M., Ramachandran R., Habib S.;\nRT   \"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the\nRT   Plasmodium falciparum mitochondrion.\";\nRL   Mol. Microbiol. 116:606-623(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Participates in iron-sulfur cluster formation (ISC) pathway\nCC       for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Plays a\nCC       role of a major scaffold protein for [Fe-S] assembly; assembles [4Fe-\nCC       4S] clusters directly upon interaction with the catalytic component\nCC       IscS-Isd11 as part of the scaffold complex (PubMed:34032321). Can\nCC       transfer [4Fe-4S] clusters to target apo-proteins (PubMed:34032321).\nCC       {ECO:0000269|PubMed:34032321}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0051537; F:2 iron, 2 sulfur cluster binding; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0051539; F:4 iron, 4 sulfur cluster binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0008198; F:ferrous iron binding; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)

```json
{
  "entry_version": 123,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0005506; F:iron ion binding; ISS:GeneDB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:21.146174+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181",
  "url": "https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004303\nname: estradiol 17-beta-dehydrogenase [NAD(P)+] activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: estradiol-17-beta + NAD(P)+ = estrone + NAD(P)H + H+. The activity can use NAD+ or NADP+ as the acceptor.\" [EC:1.1.1.62]\nsynonym: \"17-beta-estradiol dehydrogenase activity\" RELATED [EC:1.1.1.62]\nsynonym: \"17-beta-HSD activity\" BROAD [EC:1.1.1.62]\nsynonym: \"17-beta-hydroxysteroid dehydrogenase activity\" BROAD [EC:1.1.1.62]\nsynonym: \"17beta,20alpha-hydroxysteroid dehydrogenase activity\" RELATED [EC:1.1.1.62]\nsynonym: \"17beta-estradiol dehydrogenase activity\" RELATED [EC:1.1.1.62]\nsynonym: \"17beta-HSD\" RELATED [EC:1.1.1.62]\nsynonym: \"17beta-hydroxysteroid dehydrogenase activity\" RELATED [EC:1.1.1.62]\nsynonym: \"20alpha-hydroxysteroid dehydrogenase\" BROAD [EC:1.1.1.62]\nsynonym: \"estradiol 17-beta-dehydrogenase activity\" RELATED []\nsynonym: \"estradiol 17beta-dehydrogenase activity\" RELATED [EC:1.1.1.62]\nsynonym: \"estradiol dehydrogenase activity\" RELATED [EC:1.1.1.62]\nsynonym: \"estradiol-17beta:NAD(P)+ 17-oxidoreductase activity\" RELATED [EC:1.1.1.62]\nsynonym: \"estrogen 17-oxidoreductase activity\" RELATED [EC:1.1.1.62]\nxref: EC:1.1.1.62\nxref: MetaCyc:ESTRADIOL-17-BETA-DEHYDROGENASE-RXN\nxref: Reactome:R-HSA-5693390 \"HSD17B11 dehydrogenates EST17b to E1\"\nxref: Reactome:R-HSA-5696822 \"AKR1B15 reduces EST17b to E1\"\nxref: Reactome:R-HSA-6810594 \"HSD17B14 tetramer oxidises estradiol (EST17b) to estrone (E1)\"\nxref: Reactome:R-HSA-804969 \"HSD17B1 hydrogenates E1 to EST17b\"\nxref: Reactome:R-HSA-8862137 \"HSD17B2 oxidises estradiol (EST17b) to estrone (E1)\"\nxref: RHEA:24612\nxref: RHEA:24616\nis_a: GO:0033764 ! steroid dehydrogenase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor\nproperty_value: skos:exactMatch EC:1.1.1.62\nproperty_value: skos:narrowMatch RHEA:24612\nproperty_value: skos:narrowMatch RHEA:24616\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004303",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 39377-39408",
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
  "excerpt": "[Term]\nid: GO:0042300\nname: beta-amyrin synthase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: (S)-2,3-epoxysqualene = beta-amyrin.\" [PMID:9746369, RHEA:31007]\nsynonym: \"2,3-oxidosqualene beta-amyrin cyclase\" EXACT [EC:5.4.99.39]\nsynonym: \"oxidosqualene:beta-amyrin cyclase activity\" EXACT [PMID:18033581]\nxref: EC:5.4.99.39\nxref: MetaCyc:RXN-7570\nxref: RHEA:31007\nis_a: GO:0031559 ! oxidosqualene cyclase activity\nproperty_value: skos:exactMatch EC:5.4.99.39\nproperty_value: skos:exactMatch RHEA:31007\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042300",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 236107-236120",
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
  "excerpt": "[Term]\nid: GO:0048156\nname: tau protein binding\nnamespace: molecular_function\ndef: \"Binding to tau protein. tau is a microtubule-associated protein, implicated in Alzheimer's disease, Down Syndrome and ALS.\" [GOC:jid]\nis_a: GO:0008092 ! cytoskeletal protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0048156",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 300902-300908",
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
  "excerpt": "[Term]\nid: GO:0051537\nname: 2 iron, 2 sulfur cluster binding\nnamespace: molecular_function\ndef: \"Binding to a 2 iron, 2 sulfur (2Fe-2S) cluster; this cluster consists of two iron atoms, with two inorganic sulfur atoms found between the irons and acting as bridging ligands.\" [GOC:ai, PMID:15952888, Wikipedia:Iron-sulfur_cluster]\nsynonym: \"2 Fe 2 S cluster binding\" EXACT []\nsynonym: \"2 iron, 2 sulphur cluster binding\" EXACT []\nsynonym: \"2Fe-2S cluster binding\" EXACT []\nsynonym: \"diiron disulfide cluster binding\" EXACT []\nsynonym: \"diiron disulphide cluster binding\" EXACT []\nsynonym: \"iron-sulfur cluster 2Fe-2S binding\" EXACT []\nsynonym: \"iron-sulphur cluster 2Fe-2S binding\" EXACT []\nis_a: GO:0051536 ! iron-sulfur cluster binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051537",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 327878-327891",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
