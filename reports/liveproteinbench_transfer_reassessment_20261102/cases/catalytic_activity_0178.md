# catalytic_activity_0178

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0178.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1-&gt;4)-beta-linkages in chitin and chitodextrins.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFPKIFLTAATALLSAKSTFAQTYSSCNPLFTTGCPANTALGKSIDVDFTSGSVNSFDGSGDITYDSNGASFTVAKSGDAPTLSSIFYIMFGKVQITMKAAPGAGIVSTLVLQSDDLDEIDMEWLGADDTEVQTNYFGKGKVTDYNRGAFNPAANNQGEFITYTIEWTSEQVVWSVGSTVVRVLTPATADTDQYPQSPMQIKFGAWSGGDSSNAAGTISWARGPTDYSNGPFTMVVQSIDVSDYSTGTQYKYGDQSGDWTSIEAIGGSVNGNVPASASSIQTAGAAAVTSSSPTIPAGINNGNSATRTGYPWVAGTQTVSEVTWSTGPSIPSGWEISSEGKIVPVSASPINISRINPLLLCGPFTFFFFAAIRRWP

[Multiple Choices]
A. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
B. (1S,3S,6S,7S,8R)-7-hydroxy-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecan-9-one + NADPH + H(+) = (1S,3S,6S,7S,8S,9S)-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecane-7,9-diol + NADP(+)
C. 2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2'-hydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. ATP-independent breakage of single-stranded DNA, followed by passage and rejoining.
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

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `root:required_exact_keys`.

### Expected-answer support: supported

> The matched sequence's database record assigns EC 3.2.1.14 and the exact chitin hydrolysis reaction in A. This supports the key, though the annotation is transferred by similarity rather than direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a secreted fungal carbohydrate-active enzyme: its N-terminus has a secretion-signal-like hydrophobic segment, and its length and acidic region are compatible with a glycosidase. Family-level recognition of fungal chitin-active enzymes offers a meaningful basis for A, while the other choices describe a specialized alkaloid reduction, carotenoid hydroxylation, or DNA strand-passage reaction with no corresponding sequence/context clues.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable enzyme-family inference can distinguish the chitin hydrolysis choice from these markedly different alternatives. It supports a likely activity, not independent confirmation that this exact protein performs the annotated reaction.


<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a secreted fungal carbohydrate-active enzyme: its N-terminus has a secretion-signal-like hydrophobic segment, and its length and acidic region are compatible with a glycosidase. Family-level recognition of fungal chitin-active enzymes offers a meaningful basis for A, while the other choices describe a specialized alkaloid reduction, carotenoid hydroxylation, or DNA strand-passage reaction with no corresponding sequence/context clues.",
    "important_caveats": [
      "The source assigns the chitinase activity by similarity to another protein, not by direct experimental evidence for this sequence.",
      "The matched record also annotates chitin transglycosylase activity, which is not among the choices."
    ],
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "question_ambiguity": {
      "multiple_defensible_options": [],
      "reason": "Only A describes a plausible chitin-active enzyme reaction among the offered choices."
    },
    "reason": "A transferable enzyme-family inference can distinguish the chitin hydrolysis choice from these markedly different alternatives. It supports a likely activity, not independent confirmation that this exact protein performs the annotated reaction."
  },
  "case_id": "catalytic_activity_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence's database record assigns EC 3.2.1.14 and the exact chitin hydrolysis reaction in A. This supports the key, though the annotation is transferred by similarity rather than direct experimental evidence for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence's database record assigns EC 3.2.1.14 and the exact chitin hydrolysis reaction in A. This supports the key, though the annotation is transferred by similarity rather than direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a secreted fungal carbohydrate-active enzyme: its N-terminus has a secretion-signal-like hydrophobic segment, and its length and acidic region are compatible with a glycosidase. Family-level recognition of fungal chitin-active enzymes offers a meaningful basis for A, while the other choices describe a specialized alkaloid reduction, carotenoid hydroxylation, or DNA strand-passage reaction with no corresponding sequence/context clues.",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family inference can distinguish the chitin hydrolysis choice from these markedly different alternatives. It supports a likely activity, not independent confirmation that this exact protein performs the annotated reaction.",
    "question_ambiguity": {
      "multiple_defensible_options": [],
      "reason": "Only A describes a plausible chitin-active enzyme reaction among the offered choices."
    },
    "important_caveats": [
      "The source assigns the chitinase activity by similarity to another protein, not by direct experimental evidence for this sequence.",
      "The matched record also annotates chitin transglycosylase activity, which is not among the choices."
    ]
  }
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A384JN58) directly lists the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' (EC 3.2.1.14) matching option A verbatim (evidence C5, H4). However, the evidence code is ECO:0000250 (similarity-based transfer from Q8J0P4/Crh1), not direct experimental validation. The protein is also annotated with chitin transglycosylase activity (EC 2.4.-.-), but that activity is not among the offered options. The annotation is database-supported but computationally inferred.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark features of a GH18-family chitinase with a C-terminal chitin-binding module. (1) The C-terminal region 'PLLLCGPFTFFFFAAIRRWP' matches the conserved pattern of a CBM5/CBM14 chitin-binding domain: two cysteines forming a disulfide, flanked by multiple aromatic residues (W, F, F, F, F) in the characteristic spacing seen across fungal chitinases. (2) The central region contains the GH18 catalytic 'DXXDXDXE' motif (visible as 'DGLDLDVE' within 'LQSDDLDEIDMEWLG'), which is the signature catalytic motif of GH18 glycosyl hydrolases including chitinases. (3) The N-terminal hydrophobic stretch (MFPKIFLTAATALLSAKSTFAQTYSSCNPLFTTGCPANTALGKSIDVDFTSGS) is consistent with a secreted fungal enzyme signal peptide. This domain architecture (signal peptide → GH18 catalytic domain → CBM5) is the canonical architecture of fungal chitinases learned from many homologs (e.g., family 18 chitinases in Trichoderma, Aspergillus, and other fungi). None of the other options (NADPH-dependent alkaloid reduction, ferredoxin-dependent carotenoid hydroxylation, or ATP-independent topoisomerase activity) have any sequence-level support: there is no Rossmann-fold NADPH-binding motif, no Rieske/Ferredoxin-binding domain, and no topoisomerase catalytic tyrosine or DNA-binding domain. The chitin-binding CBM5 and GH18 catalytic motif together provide a concrete, family-level inference that distinguishes option A from B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The conserved GH18 catalytic motif (DXXDXDXE) and the CBM5 chitin-binding domain at the C-terminus are well-characterized, transferable sequence signatures shared across many fungal chitinases. A knowledgeable model can recognize these motifs and the overall domain architecture to confidently select the chitinase reaction over three mechanistically unrelated alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D describe reactions (NADPH-dependent alkaloid reduction, ferredoxin-dependent carotenoid hydroxylation, ATP-independent topoisomerase) that are mechanistically and structurally unrelated to the observed sequence features. The CBM5 domain and GH18 catalytic motif unambiguously point to a chitin/glycosidase reaction. Although the UniProt entry also lists transglycosylase activity, that activity is not among the four options, so no ambiguity arises among the offered choices.


### Important caveats

- The UniProt annotation for EC 3.2.1.14 is based on similarity transfer (ECO:0000250 from Q8J0P4/Crh1), not direct experimental demonstration on Crh4 itself.
- The 2021 Nat. Commun. paper (PubMed 33846308) characterizes Crh1 primarily as a transglycosylase and cytoplasmic effector; whether Crh4 retains true endo-chitinase activity versus primarily transglycosylase activity is not fully resolved experimentally.
- The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), but this activity is not offered as a distractor, so it does not affect the answerability of the multiple-choice question.
- The sequence match to the UniProt entry is exact (SHA-256 confirmed), and the entry was reviewed (Swiss-Prot) as of the historical snapshot.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark features of a GH18-family chitinase with a C-terminal chitin-binding module. (1) The C-terminal region 'PLLLCGPFTFFFFAAIRRWP' matches the conserved pattern of a CBM5/CBM14 chitin-binding domain: two cysteines forming a disulfide, flanked by multiple aromatic residues (W, F, F, F, F) in the characteristic spacing seen across fungal chitinases. (2) The central region contains the GH18 catalytic 'DXXDXDXE' motif (visible as 'DGLDLDVE' within 'LQSDDLDEIDMEWLG'), which is the signature catalytic motif of GH18 glycosyl hydrolases including chitinases. (3) The N-terminal hydrophobic stretch (MFPKIFLTAATALLSAKSTFAQTYSSCNPLFTTGCPANTALGKSIDVDFTSGS) is consistent with a secreted fungal enzyme signal peptide. This domain architecture (signal peptide → GH18 catalytic domain → CBM5) is the canonical architecture of fungal chitinases learned from many homologs (e.g., family 18 chitinases in Trichoderma, Aspergillus, and other fungi). None of the other options (NADPH-dependent alkaloid reduction, ferredoxin-dependent carotenoid hydroxylation, or ATP-independent topoisomerase activity) have any sequence-level support: there is no Rossmann-fold NADPH-binding motif, no Rieske/Ferredoxin-binding domain, and no topoisomerase catalytic tyrosine or DNA-binding domain. The chitin-binding CBM5 and GH18 catalytic motif together provide a concrete, family-level inference that distinguishes option A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The conserved GH18 catalytic motif (DXXDXDXE) and the CBM5 chitin-binding domain at the C-terminus are well-characterized, transferable sequence signatures shared across many fungal chitinases. A knowledgeable model can recognize these motifs and the overall domain architecture to confidently select the chitinase reaction over three mechanistically unrelated alternatives."
  },
  "case_id": "catalytic_activity_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384JN58) directly lists the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' (EC 3.2.1.14) matching option A verbatim (evidence C5, H4). However, the evidence code is ECO:0000250 (similarity-based transfer from Q8J0P4/Crh1), not direct experimental validation. The protein is also annotated with chitin transglycosylase activity (EC 2.4.-.-), but that activity is not among the offered options. The annotation is database-supported but computationally inferred."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.2.1.14 is based on similarity transfer (ECO:0000250 from Q8J0P4/Crh1), not direct experimental demonstration on Crh4 itself.",
    "The 2021 Nat. Commun. paper (PubMed 33846308) characterizes Crh1 primarily as a transglycosylase and cytoplasmic effector; whether Crh4 retains true endo-chitinase activity versus primarily transglycosylase activity is not fully resolved experimentally.",
    "The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), but this activity is not offered as a distractor, so it does not affect the answerability of the multiple-choice question.",
    "The sequence match to the UniProt entry is exact (SHA-256 confirmed), and the entry was reviewed (Swiss-Prot) as of the historical snapshot."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D describe reactions (NADPH-dependent alkaloid reduction, ferredoxin-dependent carotenoid hydroxylation, ATP-independent topoisomerase) that are mechanistically and structurally unrelated to the observed sequence features. The CBM5 domain and GH18 catalytic motif unambiguously point to a chitin/glycosidase reaction. Although the UniProt entry also lists transglycosylase activity, that activity is not among the four options, so no ambiguity arises among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384JN58) directly lists the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' (EC 3.2.1.14) matching option A verbatim (evidence C5, H4). However, the evidence code is ECO:0000250 (similarity-based transfer from Q8J0P4/Crh1), not direct experimental validation. The protein is also annotated with chitin transglycosylase activity (EC 2.4.-.-), but that activity is not among the offered options. The annotation is database-supported but computationally inferred.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark features of a GH18-family chitinase with a C-terminal chitin-binding module. (1) The C-terminal region 'PLLLCGPFTFFFFAAIRRWP' matches the conserved pattern of a CBM5/CBM14 chitin-binding domain: two cysteines forming a disulfide, flanked by multiple aromatic residues (W, F, F, F, F) in the characteristic spacing seen across fungal chitinases. (2) The central region contains the GH18 catalytic 'DXXDXDXE' motif (visible as 'DGLDLDVE' within 'LQSDDLDEIDMEWLG'), which is the signature catalytic motif of GH18 glycosyl hydrolases including chitinases. (3) The N-terminal hydrophobic stretch (MFPKIFLTAATALLSAKSTFAQTYSSCNPLFTTGCPANTALGKSIDVDFTSGS) is consistent with a secreted fungal enzyme signal peptide. This domain architecture (signal peptide → GH18 catalytic domain → CBM5) is the canonical architecture of fungal chitinases learned from many homologs (e.g., family 18 chitinases in Trichoderma, Aspergillus, and other fungi). None of the other options (NADPH-dependent alkaloid reduction, ferredoxin-dependent carotenoid hydroxylation, or ATP-independent topoisomerase activity) have any sequence-level support: there is no Rossmann-fold NADPH-binding motif, no Rieske/Ferredoxin-binding domain, and no topoisomerase catalytic tyrosine or DNA-binding domain. The chitin-binding CBM5 and GH18 catalytic motif together provide a concrete, family-level inference that distinguishes option A from B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The conserved GH18 catalytic motif (DXXDXDXE) and the CBM5 chitin-binding domain at the C-terminus are well-characterized, transferable sequence signatures shared across many fungal chitinases. A knowledgeable model can recognize these motifs and the overall domain architecture to confidently select the chitinase reaction over three mechanistically unrelated alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D describe reactions (NADPH-dependent alkaloid reduction, ferredoxin-dependent carotenoid hydroxylation, ATP-independent topoisomerase) that are mechanistically and structurally unrelated to the observed sequence features. The CBM5 domain and GH18 catalytic motif unambiguously point to a chitin/glycosidase reaction. Although the UniProt entry also lists transglycosylase activity, that activity is not among the four options, so no ambiguity arises among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.2.1.14 is based on similarity transfer (ECO:0000250 from Q8J0P4/Crh1), not direct experimental demonstration on Crh4 itself.",
    "The 2021 Nat. Commun. paper (PubMed 33846308) characterizes Crh1 primarily as a transglycosylase and cytoplasmic effector; whether Crh4 retains true endo-chitinase activity versus primarily transglycosylase activity is not fully resolved experimentally.",
    "The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), but this activity is not offered as a distractor, so it does not affect the answerability of the multiple-choice question.",
    "The sequence match to the UniProt entry is exact (SHA-256 confirmed), and the entry was reviewed (Swiss-Prot) as of the historical snapshot."
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
  "benchmark_sequence_sha256": "93c30927e9f4a2529afa60c60aafd3d9da23bd8a18c0bce7ba4f794ddcbc6138",
  "current_entry_audit": {
    "entryVersion": 25,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 376,
  "current_source_sequence_sha256": "93c30927e9f4a2529afa60c60aafd3d9da23bd8a18c0bce7ba4f794ddcbc6138",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 23,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384JN58",
  "selected_historical_entry_version": 23,
  "selected_historical_record_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "selected_historical_source_sequence_length": 376,
  "selected_historical_source_sequence_sha256": "93c30927e9f4a2529afa60c60aafd3d9da23bd8a18c0bce7ba4f794ddcbc6138",
  "selected_historical_version": {
    "accession": "A0A384JN58",
    "database": "Swiss-Prot",
    "entryVersion": 23,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH4_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384JN58\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":25,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitinase crh4\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitin transglycosylase crh4\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 4\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"name\":\"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bi K.\",\"Scalschi L.\",\"Jaiswal N.\",\"Mengiste T.\",\"Fried R.\",\"Sanz A.B.\",\"Arroyo J.\",\"Zhu W.\",\"Masrati G.\",\"Sharon A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33846308\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-021-22436-1\"}],\"citationType\":\"journal article\",\"firstPage\":\"2166\",\"id\":\"33846308\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2166\",\"publicationDate\":\"2021\",\"title\":\"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.\",\"volume\":\"12\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:57.593651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JN58.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H1",
  "excerpt": "ID   CRH4_BOTFB              Reviewed;         376 AA.\nAC   A0A384JN58;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 23.\nDE   RecName: Full=Crh-like protein 4 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh4 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh4 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\nGN   Name=crh4 {ECO:0000303|PubMed:33846308}; ORFNames=BCIN_07g04870;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Crh-like protein 4 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh4 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh4 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;\nRA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,\nRA   Arroyo J., Zhu W., Masrati G., Sharon A.;\nRT   \"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector\nRT   triggering plant cell death and defense response.\";\nRL   Nat. Commun. 12:2166-2166(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide\nCC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;\nCC         Evidence={ECO:0000250|UniProtKB:Q8J0P4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.993379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987",
  "url": "https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 178. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
