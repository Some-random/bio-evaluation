# cofactor_0026

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0026.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — Fe cation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTLTENVMKPQIQRFTRDHDPKVLWQVVEEDGAVIIEGFLPHEVIQKFDCELDVRSKATKGGEMNQEFYQMPVPTTTKWMNDLTATCPTFRHEILNNDILHSLCNVAFEPHGDYWLLNGMAMEMMPGNPTQQIHNDHGTHPILQYLRPDAPAPVFSIITAVTEFTESNGATRVILGSHRWPQGQKAKDDQAVRAALQPGDALVMHRSTKHGGAAHDADNQDHRRLLLTCMGTCQLAPYETNVTVPRPIVESMTPLAQKMIGWRSTRPVISNVTGLNTVRMKHLENQIELKSNVPLNVGGC

[Multiple Choices]
A. Fe cation
B. heme
C. Fe(2+)
D. heme b
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

> The sequence-matched UniProt annotation names Fe cation as the cofactor, but its evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein. The annotation is consistent with its classification as an iron/alpha-ketoglutarate-dependent dioxygenase.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an HxD-like motif (HGD) and a later histidine, a pattern compatible with the iron-binding site of Fe(II)/2-oxoglutarate-dependent dioxygenases. Transferable knowledge of this enzyme family supports an iron cofactor and distinguishes the iron choices from heme and heme b. The usual mechanistic description is Fe(II), although the choices also include the broader label “Fe cation.”


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference provides a meaningful basis for selecting an iron cofactor without knowing this protein’s database entry. It does not uniquely resolve whether the intended label is the broad A or the more specific C; that is an ambiguity in the alternatives rather than a need to memorize this exact protein’s record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Fe(II) is a cation and is the usual catalytic iron state for this enzyme family, so C is chemically more specific, while A is the broader cofactor label used by the annotation. The options do not make clear that these are mutually exclusive.


### Important caveats

- The source annotation is similarity-transferred rather than direct experimental evidence for the supplied protein.
- The sequence motifs support a family-level inference but do not independently establish the exact metal oxidation state for this particular protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an HxD-like motif (HGD) and a later histidine, a pattern compatible with the iron-binding site of Fe(II)/2-oxoglutarate-dependent dioxygenases. Transferable knowledge of this enzyme family supports an iron cofactor and distinguishes the iron choices from heme and heme b. The usual mechanistic description is Fe(II), although the choices also include the broader label “Fe cation.”",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for selecting an iron cofactor without knowing this protein’s database entry. It does not uniquely resolve whether the intended label is the broad A or the more specific C; that is an ambiguity in the alternatives rather than a need to memorize this exact protein’s record."
  },
  "case_id": "cofactor_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation names Fe cation as the cofactor, but its evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein. The annotation is consistent with its classification as an iron/alpha-ketoglutarate-dependent dioxygenase."
  },
  "important_caveats": [
    "The source annotation is similarity-transferred rather than direct experimental evidence for the supplied protein.",
    "The sequence motifs support a family-level inference but do not independently establish the exact metal oxidation state for this particular protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Fe(II) is a cation and is the usual catalytic iron state for this enzyme family, so C is chemically more specific, while A is the broader cofactor label used by the annotation. The options do not make clear that these are mutually exclusive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation names Fe cation as the cofactor, but its evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein. The annotation is consistent with its classification as an iron/alpha-ketoglutarate-dependent dioxygenase.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an HxD-like motif (HGD) and a later histidine, a pattern compatible with the iron-binding site of Fe(II)/2-oxoglutarate-dependent dioxygenases. Transferable knowledge of this enzyme family supports an iron cofactor and distinguishes the iron choices from heme and heme b. The usual mechanistic description is Fe(II), although the choices also include the broader label “Fe cation.”",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for selecting an iron cofactor without knowing this protein’s database entry. It does not uniquely resolve whether the intended label is the broad A or the more specific C; that is an ambiguity in the alternatives rather than a need to memorize this exact protein’s record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Fe(II) is a cation and is the usual catalytic iron state for this enzyme family, so C is chemically more specific, while A is the broader cofactor label used by the annotation. The options do not make clear that these are mutually exclusive."
  },
  "important_caveats": [
    "The source annotation is similarity-transferred rather than direct experimental evidence for the supplied protein.",
    "The sequence motifs support a family-level inference but do not independently establish the exact metal oxidation state for this particular protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A2Z5U507) explicitly annotates the cofactor as 'Fe cation' (ChEBI:CHEBI:24875) with evidence code ECO:0000250 (inferred by similarity from Q5AR53). The protein is named 'Iron/alpha-ketoglutarate-dependent dioxygenase okaE' (EC 1.14.20.-), confirming iron as the metal cofactor. The annotation is transferred by similarity rather than directly experimentally determined for this exact protein, but it is the recorded database fact.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains features of the Fe/αKG dioxygenase superfamily: the 'GSHR' motif (~res 158) and the 'HRSTKHGGAAHDADNQDHRR' region (~res 195-215) are consistent with the 2-His-1-carboxylate facial triad (HxD/E...H) characteristic of this large enzyme family. This family knowledge clearly excludes heme (B) and heme b (D), as heme-binding proteins use CXXCH motifs and single-histidine axial ligation rather than the 2-His-1-carboxylate triad. Across the Fe/αKG dioxygenase superfamily in UniProt, the standard cofactor annotation is 'Fe cation' (ChEBI:24875), a pattern observable in dozens of related entries. This family-level annotation convention distinguishes A from C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition of the 2-His-1-carboxylate facial triad and the overall ~300-residue Fe/αKG dioxygenase fold rules out heme-containing options. The consistent use of 'Fe cation' (rather than 'Fe(2+)') as the cofactor label across the Fe/αKG dioxygenase family in UniProt is a transferable pattern learned from many homologous entries. However, the A vs C distinction is extremely fine: biologically, the active species is specifically Fe(II), so a strict biochemist might prefer C. The key relies on the database annotation convention rather than a sharp biochemical distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both 'Fe cation' (A) and 'Fe(2+)' (C) describe the same chemical entity in the context of Fe/αKG dioxygenases. ChEBI:24875 is 'iron(2+)', making the UniProt display name 'Fe cation' essentially synonymous with Fe(2+). A biochemist reasoning from catalytic mechanism would specify Fe(II) (choice C), while the UniProt annotation convention for this family uses 'Fe cation' (choice A). The distinction is a nomenclature/annotation preference rather than a biological fact, making both choices defensible.


### Important caveats

- The cofactor annotation evidence code is ECO:0000250 (inferred by similarity), meaning it is transferred from another entry (Q5AR53) rather than directly measured for okaE.
- The distinction between choices A ('Fe cation') and C ('Fe(2+)') is essentially a database naming convention, not a biological distinction; both refer to the same divalent iron species used by Fe/αKG dioxygenases.
- The protein name explicitly includes 'Iron/alpha-ketoglutarate-dependent' which strongly supports an iron cofactor, but does not resolve the A-vs-C nomenclature question.
- Sequence-based family recognition (2-His-1-carboxylate facial triad) is feasible but requires careful motif identification in a 300-residue sequence without explicit family labels.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features of the Fe/αKG dioxygenase superfamily: the 'GSHR' motif (~res 158) and the 'HRSTKHGGAAHDADNQDHRR' region (~res 195-215) are consistent with the 2-His-1-carboxylate facial triad (HxD/E...H) characteristic of this large enzyme family. This family knowledge clearly excludes heme (B) and heme b (D), as heme-binding proteins use CXXCH motifs and single-histidine axial ligation rather than the 2-His-1-carboxylate triad. Across the Fe/αKG dioxygenase superfamily in UniProt, the standard cofactor annotation is 'Fe cation' (ChEBI:24875), a pattern observable in dozens of related entries. This family-level annotation convention distinguishes A from C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition of the 2-His-1-carboxylate facial triad and the overall ~300-residue Fe/αKG dioxygenase fold rules out heme-containing options. The consistent use of 'Fe cation' (rather than 'Fe(2+)') as the cofactor label across the Fe/αKG dioxygenase family in UniProt is a transferable pattern learned from many homologous entries. However, the A vs C distinction is extremely fine: biologically, the active species is specifically Fe(II), so a strict biochemist might prefer C. The key relies on the database annotation convention rather than a sharp biochemical distinction."
  },
  "case_id": "cofactor_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A2Z5U507) explicitly annotates the cofactor as 'Fe cation' (ChEBI:CHEBI:24875) with evidence code ECO:0000250 (inferred by similarity from Q5AR53). The protein is named 'Iron/alpha-ketoglutarate-dependent dioxygenase okaE' (EC 1.14.20.-), confirming iron as the metal cofactor. The annotation is transferred by similarity rather than directly experimentally determined for this exact protein, but it is the recorded database fact."
  },
  "important_caveats": [
    "The cofactor annotation evidence code is ECO:0000250 (inferred by similarity), meaning it is transferred from another entry (Q5AR53) rather than directly measured for okaE.",
    "The distinction between choices A ('Fe cation') and C ('Fe(2+)') is essentially a database naming convention, not a biological distinction; both refer to the same divalent iron species used by Fe/αKG dioxygenases.",
    "The protein name explicitly includes 'Iron/alpha-ketoglutarate-dependent' which strongly supports an iron cofactor, but does not resolve the A-vs-C nomenclature question.",
    "Sequence-based family recognition (2-His-1-carboxylate facial triad) is feasible but requires careful motif identification in a 300-residue sequence without explicit family labels."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both 'Fe cation' (A) and 'Fe(2+)' (C) describe the same chemical entity in the context of Fe/αKG dioxygenases. ChEBI:24875 is 'iron(2+)', making the UniProt display name 'Fe cation' essentially synonymous with Fe(2+). A biochemist reasoning from catalytic mechanism would specify Fe(II) (choice C), while the UniProt annotation convention for this family uses 'Fe cation' (choice A). The distinction is a nomenclature/annotation preference rather than a biological fact, making both choices defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A2Z5U507) explicitly annotates the cofactor as 'Fe cation' (ChEBI:CHEBI:24875) with evidence code ECO:0000250 (inferred by similarity from Q5AR53). The protein is named 'Iron/alpha-ketoglutarate-dependent dioxygenase okaE' (EC 1.14.20.-), confirming iron as the metal cofactor. The annotation is transferred by similarity rather than directly experimentally determined for this exact protein, but it is the recorded database fact.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains features of the Fe/αKG dioxygenase superfamily: the 'GSHR' motif (~res 158) and the 'HRSTKHGGAAHDADNQDHRR' region (~res 195-215) are consistent with the 2-His-1-carboxylate facial triad (HxD/E...H) characteristic of this large enzyme family. This family knowledge clearly excludes heme (B) and heme b (D), as heme-binding proteins use CXXCH motifs and single-histidine axial ligation rather than the 2-His-1-carboxylate triad. Across the Fe/αKG dioxygenase superfamily in UniProt, the standard cofactor annotation is 'Fe cation' (ChEBI:24875), a pattern observable in dozens of related entries. This family-level annotation convention distinguishes A from C.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition of the 2-His-1-carboxylate facial triad and the overall ~300-residue Fe/αKG dioxygenase fold rules out heme-containing options. The consistent use of 'Fe cation' (rather than 'Fe(2+)') as the cofactor label across the Fe/αKG dioxygenase family in UniProt is a transferable pattern learned from many homologous entries. However, the A vs C distinction is extremely fine: biologically, the active species is specifically Fe(II), so a strict biochemist might prefer C. The key relies on the database annotation convention rather than a sharp biochemical distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both 'Fe cation' (A) and 'Fe(2+)' (C) describe the same chemical entity in the context of Fe/αKG dioxygenases. ChEBI:24875 is 'iron(2+)', making the UniProt display name 'Fe cation' essentially synonymous with Fe(2+). A biochemist reasoning from catalytic mechanism would specify Fe(II) (choice C), while the UniProt annotation convention for this family uses 'Fe cation' (choice A). The distinction is a nomenclature/annotation preference rather than a biological fact, making both choices defensible."
  },
  "important_caveats": [
    "The cofactor annotation evidence code is ECO:0000250 (inferred by similarity), meaning it is transferred from another entry (Q5AR53) rather than directly measured for okaE.",
    "The distinction between choices A ('Fe cation') and C ('Fe(2+)') is essentially a database naming convention, not a biological distinction; both refer to the same divalent iron species used by Fe/αKG dioxygenases.",
    "The protein name explicitly includes 'Iron/alpha-ketoglutarate-dependent' which strongly supports an iron cofactor, but does not resolve the A-vs-C nomenclature question.",
    "Sequence-based family recognition (2-His-1-carboxylate facial triad) is feasible but requires careful motif identification in a 300-residue sequence without explicit family labels."
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
  "benchmark_sequence_length": 300,
  "benchmark_sequence_sha256": "d3f6009a2039d1f44694d93a97eabb6e8a8f1adccc44678bab4dee0033d44a8e",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-10-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 300,
  "current_source_sequence_sha256": "d3f6009a2039d1f44694d93a97eabb6e8a8f1adccc44678bab4dee0033d44a8e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 21,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2Z5U507",
  "selected_historical_entry_version": 21,
  "selected_historical_record_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "selected_historical_source_sequence_length": 300,
  "selected_historical_source_sequence_sha256": "d3f6009a2039d1f44694d93a97eabb6e8a8f1adccc44678bab4dee0033d44a8e",
  "selected_historical_version": {
    "accession": "A0A2Z5U507",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "OKAE_PENOH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2Z5U507\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-10-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Penicillium\"],\"scientificName\":\"Penicillium ochrochloron\",\"taxonId\":69780}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"Okaramines biosynthesis cluster protein E\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"1.14.20.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"Iron/alpha-ketoglutarate-dependent dioxygenase okaE\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:24875\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5AR53\",\"source\":\"UniProtKB\"}],\"name\":\"Fe cation\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lai C.Y.\",\"Lo I.W.\",\"Hewage R.T.\",\"Chen Y.C.\",\"Chen C.T.\",\"Lee C.F.\",\"Lin S.\",\"Tang M.C.\",\"Lin H.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28631282\"},{\"database\":\"DOI\",\"id\":\"10.1002/anie.201705501\"}],\"citationType\":\"journal article\",\"firstPage\":\"9478\",\"id\":\"28631282\",\"journal\":\"Angew. Chem. Int. Ed.\",\"lastPage\":\"9482\",\"publicationDate\":\"2017\",\"title\":\"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise Pathway of Okaramines.\",\"volume\":\"56\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H1",
  "excerpt": "ID   OKAE_PENOH              Reviewed;         300 AA.\nAC   A0A2Z5U507;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-OCT-2018, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=Iron/alpha-ketoglutarate-dependent dioxygenase okaE {ECO:0000303|PubMed:28631282};\nDE            EC=1.14.20.- {ECO:0000269|PubMed:28631282};\nDE   AltName: Full=Okaramines biosynthesis cluster protein E {ECO:0000303|PubMed:28631282};\nGN   Name=okaE {ECO:0000303|PubMed:28631282};\nOS   Penicillium ochrochloron.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.\nOX   NCBI_TaxID=69780;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:56.491248+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Iron/alpha-ketoglutarate-dependent dioxygenase okaE {ECO:0000303|PubMed:28631282};\nDE            EC=1.14.20.- {ECO:0000269|PubMed:28631282};\nDE   AltName: Full=Okaramines biosynthesis cluster protein E {ECO:0000303|PubMed:28631282};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:56.491248+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=28631282; DOI=10.1002/anie.201705501;\nRA   Lai C.Y., Lo I.W., Hewage R.T., Chen Y.C., Chen C.T., Lee C.F., Lin S.,\nRA   Tang M.C., Lin H.C.;\nRT   \"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise\nRT   Pathway of Okaramines.\";\nRL   Angew. Chem. Int. Ed. 56:9478-9482(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:56.491248+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Fe cation; Xref=ChEBI:CHEBI:24875;\nCC         Evidence={ECO:0000250|UniProtKB:Q5AR53};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:56.491248+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
