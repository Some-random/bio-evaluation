# cofactor_0099

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0099.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — FAD

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPSAEGASGAPTPEDLKLHQLSQKYTAEAAKRFRPEGLGQFIRLKEVGNERFRALAEDPWVDHAALNAKEPVKDGSRYKFIILGAGYGGLLYAVRLAEAGLASGPDDILMVDAAGGFGGTWWWNRYPGLHCDVESYSYMPLLEETGYIPKSKYAAGPELLEHAYRIATQWKLHDKALFRSNVKTIRWDDESRLWSLEVTEGRGPGQQSRELKLQARYVLLASGILTNPQVPKIPGLETFTGPVFHTARWNYDVTGGSPTDEALNRLEGKRVGIIGTGATAIQVVPKLAKYAKELYVFQRTPSGVWWRGQRPTDPVEWKTKIARKKGWQRERMLNLDSYLTDAAEEGQENMVADGWTEMPAFSAVIGSPRHGIVEPTPEKIAEHLGRLYKLDLPHAEQVRARTDSIVKDPKTAAKLKAWYPTWCKRPTFSDEYLQTFNLPNVHLVDTDGKGVDAANPSGLVVADKEYPLDILVLSTGYVTPSIGGGSPAVRTGVDIYGRGGKSLDDKWQTHGAATLHGVCSNGFPNLFFTPLSQSSQAANNAFTLDVGTEHIVQVIKTAEDRVDGDALVEVTSEAEEAWSFEIMKHAGWFASVTGCTPGYITSEGEALRKSEDPMEMAKRARSGNLSQGMASYMKLLQEYRADGSLKGFDISSRA

[Multiple Choices]
A. Mn(2+)
B. FAD
C. [4Fe-4S] cluster
D. a divalent metal cation
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

> The sequence-matched UniProt annotation identifies FAD as the cofactor with experimental evidence, and the cited structural study reports the protein crystallized with FAD and NADPH.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a glycine-rich GxGxxG-like segment (GAGYGG), consistent with a dinucleotide-binding fold. Transferable knowledge of flavin-dependent monooxygenases, including Baeyer–Villiger monooxygenases, links this type of enzyme to FAD; that makes FAD a meaningful choice over the metal-ion and iron-sulfur alternatives. The motif is not unique by itself, so this is a family-level, probabilistic inference rather than proof.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A sequence-based flavoprotein/monooxygenase-family inference can distinguish FAD among the offered options without knowing this protein’s exact database annotation. The reviewer-only evidence supports the key but is not needed as an input to that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> FAD is distinct from the offered metal cofactors. Although Mn2+ is a divalent cation, the evidence and sequence-based inference favor FAD rather than either metal choice.


### Important caveats

- The glycine-rich motif alone is not diagnostic of FAD binding.
- The cited structure includes NADPH as well as FAD, but NADPH is not among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a glycine-rich GxGxxG-like segment (GAGYGG), consistent with a dinucleotide-binding fold. Transferable knowledge of flavin-dependent monooxygenases, including Baeyer–Villiger monooxygenases, links this type of enzyme to FAD; that makes FAD a meaningful choice over the metal-ion and iron-sulfur alternatives. The motif is not unique by itself, so this is a family-level, probabilistic inference rather than proof.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A sequence-based flavoprotein/monooxygenase-family inference can distinguish FAD among the offered options without knowing this protein’s exact database annotation. The reviewer-only evidence supports the key but is not needed as an input to that inference."
  },
  "case_id": "cofactor_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies FAD as the cofactor with experimental evidence, and the cited structural study reports the protein crystallized with FAD and NADPH."
  },
  "important_caveats": [
    "The glycine-rich motif alone is not diagnostic of FAD binding.",
    "The cited structure includes NADPH as well as FAD, but NADPH is not among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FAD is distinct from the offered metal cofactors. Although Mn2+ is a divalent cation, the evidence and sequence-based inference favor FAD rather than either metal choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies FAD as the cofactor with experimental evidence, and the cited structural study reports the protein crystallized with FAD and NADPH.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a glycine-rich GxGxxG-like segment (GAGYGG), consistent with a dinucleotide-binding fold. Transferable knowledge of flavin-dependent monooxygenases, including Baeyer–Villiger monooxygenases, links this type of enzyme to FAD; that makes FAD a meaningful choice over the metal-ion and iron-sulfur alternatives. The motif is not unique by itself, so this is a family-level, probabilistic inference rather than proof.",
    "missing_item_specific_fact": "",
    "reason": "A sequence-based flavoprotein/monooxygenase-family inference can distinguish FAD among the offered options without knowing this protein’s exact database annotation. The reviewer-only evidence supports the key but is not needed as an input to that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FAD is distinct from the offered metal cofactors. Although Mn2+ is a divalent cation, the evidence and sequence-based inference favor FAD rather than either metal choice."
  },
  "important_caveats": [
    "The glycine-rich motif alone is not diagnostic of FAD binding.",
    "The cited structure includes NADPH as well as FAD, but NADPH is not among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms this protein (G2QA95) is a Polycyclic ketone monooxygenase / Baeyer-Villiger monooxygenase from Thermothelomyces thermophilus. The cofactor FAD is annotated with experimental evidence (ECO:0000269|PubMed:28010060), and the 2.00 Å X-ray crystal structure (PDB: 5MQ6) was solved in complex with FAD and NADPH. The sequence matches the benchmark exactly. The expected answer B (FAD) is strongly supported by experimental crystallographic and biochemical evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the classic Rossmann fold motif GxGxxG: 'GAGYGGLLYAVRLA' (residues ~85-98) is a textbook dinucleotide-binding motif, and a second putative Rossmann-like segment 'GIGTGATAIQVVPKL' (~residues 320-335) is also present. Two Rossmann folds in a ~655-residue protein is a hallmark of FAD-dependent oxidoreductases (e.g., glutathione reductase, D-amino acid oxidase, BVMO family). Transferable knowledge from the BVMO/flavoprotein superfamily establishes that these enzymes universally require FAD as a tightly bound cofactor with NADPH as a cosubstrate. The sequence lacks the Cys-rich clusters (CxxCxxC…C) needed for &#91;4Fe-4S&#93; coordination (eliminating C), and lacks the compact His/Asp/Glu triads or tetrad motifs typical of Mn²⁺ or generic divalent-metal sites (weakening A and D). The protein length (655 AA) is also more consistent with a two-domain flavoprotein than a small metalloenzyme. Among the four offered choices, only FAD is compatible with the observed Rossmann-fold architecture and overall size.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the GxGxxG Rossmann-fold motif (one of the most widely taught and transferable sequence signatures in biochemistry), the presence of a second Rossmann-like region, the 655-aa length, and the absence of metal- or Fe-S-cluster-binding motifs to distinguish FAD from the other three options. This relies on family-level and motif-level knowledge learned from many other flavoproteins, not on memorizing this particular entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D ('a divalent metal cation') is very generic, but the sequence provides no convincing metal-binding motif, and the strong Rossmann-fold signal points specifically to FAD. Option A (Mn²⁺) is a subset of D and similarly unsupported. Option C (&#91;4Fe-4S&#93;) requires a Cys-rich motif absent here. The Rossmann-fold evidence cleanly separates B from the other three.


### Important caveats

- The Rossmann fold motif can in principle bind NAD(P) as well as FAD; however, NAD/NADP are not among the offered choices, so this ambiguity does not affect the answer.
- The BVMO family assignment, if recognized, would further confirm FAD, but the Rossmann-fold argument alone is sufficient to distinguish the offered alternatives.
- The reviewer-only evidence (accession, organism, PDB structure) was not available to the evaluated model; the reasoning above relies solely on sequence features and general transferable knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the classic Rossmann fold motif GxGxxG: 'GAGYGGLLYAVRLA' (residues ~85-98) is a textbook dinucleotide-binding motif, and a second putative Rossmann-like segment 'GIGTGATAIQVVPKL' (~residues 320-335) is also present. Two Rossmann folds in a ~655-residue protein is a hallmark of FAD-dependent oxidoreductases (e.g., glutathione reductase, D-amino acid oxidase, BVMO family). Transferable knowledge from the BVMO/flavoprotein superfamily establishes that these enzymes universally require FAD as a tightly bound cofactor with NADPH as a cosubstrate. The sequence lacks the Cys-rich clusters (CxxCxxC…C) needed for [4Fe-4S] coordination (eliminating C), and lacks the compact His/Asp/Glu triads or tetrad motifs typical of Mn²⁺ or generic divalent-metal sites (weakening A and D). The protein length (655 AA) is also more consistent with a two-domain flavoprotein than a small metalloenzyme. Among the four offered choices, only FAD is compatible with the observed Rossmann-fold architecture and overall size.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the GxGxxG Rossmann-fold motif (one of the most widely taught and transferable sequence signatures in biochemistry), the presence of a second Rossmann-like region, the 655-aa length, and the absence of metal- or Fe-S-cluster-binding motifs to distinguish FAD from the other three options. This relies on family-level and motif-level knowledge learned from many other flavoproteins, not on memorizing this particular entry."
  },
  "case_id": "cofactor_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms this protein (G2QA95) is a Polycyclic ketone monooxygenase / Baeyer-Villiger monooxygenase from Thermothelomyces thermophilus. The cofactor FAD is annotated with experimental evidence (ECO:0000269|PubMed:28010060), and the 2.00 Å X-ray crystal structure (PDB: 5MQ6) was solved in complex with FAD and NADPH. The sequence matches the benchmark exactly. The expected answer B (FAD) is strongly supported by experimental crystallographic and biochemical evidence."
  },
  "important_caveats": [
    "The Rossmann fold motif can in principle bind NAD(P) as well as FAD; however, NAD/NADP are not among the offered choices, so this ambiguity does not affect the answer.",
    "The BVMO family assignment, if recognized, would further confirm FAD, but the Rossmann-fold argument alone is sufficient to distinguish the offered alternatives.",
    "The reviewer-only evidence (accession, organism, PDB structure) was not available to the evaluated model; the reasoning above relies solely on sequence features and general transferable knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D ('a divalent metal cation') is very generic, but the sequence provides no convincing metal-binding motif, and the strong Rossmann-fold signal points specifically to FAD. Option A (Mn²⁺) is a subset of D and similarly unsupported. Option C ([4Fe-4S]) requires a Cys-rich motif absent here. The Rossmann-fold evidence cleanly separates B from the other three."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms this protein (G2QA95) is a Polycyclic ketone monooxygenase / Baeyer-Villiger monooxygenase from Thermothelomyces thermophilus. The cofactor FAD is annotated with experimental evidence (ECO:0000269|PubMed:28010060), and the 2.00 Å X-ray crystal structure (PDB: 5MQ6) was solved in complex with FAD and NADPH. The sequence matches the benchmark exactly. The expected answer B (FAD) is strongly supported by experimental crystallographic and biochemical evidence.",
    "evidence_ids": ["C5", "C6", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the classic Rossmann fold motif GxGxxG: 'GAGYGGLLYAVRLA' (residues ~85-98) is a textbook dinucleotide-binding motif, and a second putative Rossmann-like segment 'GIGTGATAIQVVPKL' (~residues 320-335) is also present. Two Rossmann folds in a ~655-residue protein is a hallmark of FAD-dependent oxidoreductases (e.g., glutathione reductase, D-amino acid oxidase, BVMO family). Transferable knowledge from the BVMO/flavoprotein superfamily establishes that these enzymes universally require FAD as a tightly bound cofactor with NADPH as a cosubstrate. The sequence lacks the Cys-rich clusters (CxxCxxC…C) needed for [4Fe-4S] coordination (eliminating C), and lacks the compact His/Asp/Glu triads or tetrad motifs typical of Mn²⁺ or generic divalent-metal sites (weakening A and D). The protein length (655 AA) is also more consistent with a two-domain flavoprotein than a small metalloenzyme. Among the four offered choices, only FAD is compatible with the observed Rossmann-fold architecture and overall size.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the GxGxxG Rossmann-fold motif (one of the most widely taught and transferable sequence signatures in biochemistry), the presence of a second Rossmann-like region, the 655-aa length, and the absence of metal- or Fe-S-cluster-binding motifs to distinguish FAD from the other three options. This relies on family-level and motif-level knowledge learned from many other flavoproteins, not on memorizing this particular entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D ('a divalent metal cation') is very generic, but the sequence provides no convincing metal-binding motif, and the strong Rossmann-fold signal points specifically to FAD. Option A (Mn²⁺) is a subset of D and similarly unsupported. Option C ([4Fe-4S]) requires a Cys-rich motif absent here. The Rossmann-fold evidence cleanly separates B from the other three."
  },
  "important_caveats": [
    "The Rossmann fold motif can in principle bind NAD(P) as well as FAD; however, NAD/NADP are not among the offered choices, so this ambiguity does not affect the answer.",
    "The BVMO family assignment, if recognized, would further confirm FAD, but the Rossmann-fold argument alone is sufficient to distinguish the offered alternatives.",
    "The reviewer-only evidence (accession, organism, PDB structure) was not available to the evaluated model; the reasoning above relies solely on sequence features and general transferable knowledge."
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
  "benchmark_sequence_length": 655,
  "benchmark_sequence_sha256": "09b636920a3f5f3b7e69fa4f71f91685b6346b6eef60641ed9e987c21d819e93",
  "current_entry_audit": {
    "entryVersion": 58,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 655,
  "current_source_sequence_sha256": "09b636920a3f5f3b7e69fa4f71f91685b6346b6eef60641ed9e987c21d819e93",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 56,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G2QA95",
  "selected_historical_entry_version": 56,
  "selected_historical_record_sha256": "0318176fb6154b708d301de6d2e3ad08fef54e818227bdd198fb527dc3b65386",
  "selected_historical_source_sequence_length": 655,
  "selected_historical_source_sequence_sha256": "09b636920a3f5f3b7e69fa4f71f91685b6346b6eef60641ed9e987c21d819e93",
  "selected_historical_version": {
    "accession": "G2QA95",
    "database": "Swiss-Prot",
    "entryVersion": 56,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BVMO_THET4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2QA95.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G2QA95\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:06.440589+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb",
  "url": "https://rest.uniprot.org/uniprotkb/G2QA95.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2QA95.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":58,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:06.440589+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb",
  "url": "https://rest.uniprot.org/uniprotkb/G2QA95.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2QA95.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Sporotrichum thermophile\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Thermothelomyces\"],\"scientificName\":\"Thermothelomyces thermophilus (strain ATCC 42464 / BCRC 31852 / DSM 1799)\",\"taxonId\":573729}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:06.440589+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb",
  "url": "https://rest.uniprot.org/uniprotkb/G2QA95.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2QA95.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28010060\",\"source\":\"PubMed\"}],\"value\":\"Baeyer-Villiger monooxygenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28010060\",\"source\":\"PubMed\"}],\"value\":\"BVMO\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28010060\",\"source\":\"PubMed\"}],\"value\":\"1.14.13.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28010060\",\"source\":\"PubMed\"}],\"value\":\"Polycyclic ketone monooxygenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28010060\",\"source\":\"PubMed\"}],\"value\":\"PockeMO\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:06.440589+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb",
  "url": "https://rest.uniprot.org/uniprotkb/G2QA95.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2QA95.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28010060\",\"source\":\"PubMed\"}],\"name\":\"FAD\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:06.440589+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb",
  "url": "https://rest.uniprot.org/uniprotkb/G2QA95.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2QA95.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Furst M.J.\",\"Savino S.\",\"Dudek H.M.\",\"Gomez Castellanos J.R.\",\"Gutierrez de Souza C.\",\"Rovida S.\",\"Fraaije M.W.\",\"Mattevi A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28010060\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.6b12246\"}],\"citationType\":\"journal article\",\"firstPage\":\"627\",\"id\":\"28010060\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"630\",\"publicationDate\":\"2017\",\"title\":\"Polycyclic Ketone Monooxygenase from the Thermophilic Fungus Thermothelomyces thermophila: A Structurally Distinct Biocatalyst for Bulky Substrates.\",\"volume\":\"139\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5MQ6\",\"source\":\"PDB\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) IN COMPLEX WITH FAD AND NADPH\",\"DISULFIDE BONDS\",\"COFACTOR\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBSTRATE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:06.440589+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d68b3a6b723a763aeede4c3561c77e9b98dcca4238897f1ddbc147129fd1cfeb",
  "url": "https://rest.uniprot.org/uniprotkb/G2QA95.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H1",
  "excerpt": "ID   BVMO_THET4              Reviewed;         655 AA.\nAC   G2QA95;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 56.\nDE   RecName: Full=Polycyclic ketone monooxygenase {ECO:0000303|PubMed:28010060};\nDE            Short=PockeMO {ECO:0000303|PubMed:28010060};\nDE            EC=1.14.13.- {ECO:0000269|PubMed:28010060};\nDE   AltName: Full=Baeyer-Villiger monooxygenase {ECO:0000303|PubMed:28010060};\nDE            Short=BVMO {ECO:0000303|PubMed:28010060};\nGN   ORFNames=MYCTH_65400;\nOS   Thermothelomyces thermophilus (strain ATCC 42464 / BCRC 31852 / DSM 1799)\nOS   (Sporotrichum thermophile).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Thermothelomyces.\nOX   NCBI_TaxID=573729;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:01.571843+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0318176fb6154b708d301de6d2e3ad08fef54e818227bdd198fb527dc3b65386",
  "url": "https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Polycyclic ketone monooxygenase {ECO:0000303|PubMed:28010060};\nDE            Short=PockeMO {ECO:0000303|PubMed:28010060};\nDE            EC=1.14.13.- {ECO:0000269|PubMed:28010060};\nDE   AltName: Full=Baeyer-Villiger monooxygenase {ECO:0000303|PubMed:28010060};\nDE            Short=BVMO {ECO:0000303|PubMed:28010060};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:01.571843+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0318176fb6154b708d301de6d2e3ad08fef54e818227bdd198fb527dc3b65386",
  "url": "https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:5MQ6}\nRP   X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) IN COMPLEX WITH FAD AND NADPH,\nRP   DISULFIDE BONDS, COFACTOR, FUNCTION, CATALYTIC ACTIVITY, SUBSTRATE\nRP   SPECIFICITY, BIOPHYSICOCHEMICAL PROPERTIES, AND BIOTECHNOLOGY.\nRX   PubMed=28010060; DOI=10.1021/jacs.6b12246;\nRA   Furst M.J., Savino S., Dudek H.M., Gomez Castellanos J.R.,\nRA   Gutierrez de Souza C., Rovida S., Fraaije M.W., Mattevi A.;\nRT   \"Polycyclic Ketone Monooxygenase from the Thermophilic Fungus\nRT   Thermothelomyces thermophila: A Structurally Distinct Biocatalyst for Bulky\nRT   Substrates.\";\nRL   J. Am. Chem. Soc. 139:627-630(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:01.571843+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0318176fb6154b708d301de6d2e3ad08fef54e818227bdd198fb527dc3b65386",
  "url": "https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FAD; Xref=ChEBI:CHEBI:57692;\nCC         Evidence={ECO:0000269|PubMed:28010060};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:01.571843+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0318176fb6154b708d301de6d2e3ad08fef54e818227bdd198fb527dc3b65386",
  "url": "https://rest.uniprot.org/unisave/G2QA95?format=txt&versions=56"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
