# cofactor_0039

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0039.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSLSNKLAITDVDLKDKRVLIRVDFNVPLDADKKITNNQRIVGALPTIKYAIENGAKAVVLMSHLGRPDGKANPKYSLKPVATELEKLLSKSVIFAENCVGKETEEIVNKATGGQVILLENLRFHAEEEGSSKDAEGKKVKADKEKVEEFRKGLTALGDVYINDAFGTAHRAHSSMVGVDLPQKASGFLVKKELEYFAKALESPQRPFLAILGGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKKTLENVKIGNSLFDEAGSKIVGDIVEKAKKNNVKIVLPVDYVTADKFAADAKTGYATDADGIPDGYMGLDVGEKSVELYKKTIAEAKTILWNGPPGVFELEPFANATKKTLDAAVAAAQSGSIVIIGGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK

[Multiple Choices]
A. FAD
B. Fe(2+)
C. a divalent metal cation
D. Mg(2+)
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

> The sequence-matched UniProt annotation assigns Mg(2+) as the cofactor, with the annotation transferred by similarity rather than presented as direct experimental evidence for this exact protein. This is also consistent with phosphoglycerate kinase chemistry.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a phosphoglycerate kinase, a glycolytic phosphotransferase that uses ATP. Transferable knowledge of this enzyme family supports Mg(2+) coordinating ATP during phosphoryl transfer, making Mg(2+) a meaningful choice over FAD or Fe(2+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the enzyme family and its common Mg-dependent ATP chemistry provides a credible inference from the supplied sequence; the exact-protein annotation is not necessary to distinguish Mg from the unrelated cofactor options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Mg(2+) is itself a divalent metal cation, so option C is broadly true of the cofactor specified in D. D is the more specific answer, but the options are not mutually exclusive.


### Important caveats

- The supplied evidence supports the key through a similarity-transferred database annotation, not direct experimental evidence for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a phosphoglycerate kinase, a glycolytic phosphotransferase that uses ATP. Transferable knowledge of this enzyme family supports Mg(2+) coordinating ATP during phosphoryl transfer, making Mg(2+) a meaningful choice over FAD or Fe(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family and its common Mg-dependent ATP chemistry provides a credible inference from the supplied sequence; the exact-protein annotation is not necessary to distinguish Mg from the unrelated cofactor options."
  },
  "case_id": "cofactor_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns Mg(2+) as the cofactor, with the annotation transferred by similarity rather than presented as direct experimental evidence for this exact protein. This is also consistent with phosphoglycerate kinase chemistry."
  },
  "important_caveats": [
    "The supplied evidence supports the key through a similarity-transferred database annotation, not direct experimental evidence for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Mg(2+) is itself a divalent metal cation, so option C is broadly true of the cofactor specified in D. D is the more specific answer, but the options are not mutually exclusive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns Mg(2+) as the cofactor, with the annotation transferred by similarity rather than presented as direct experimental evidence for this exact protein. This is also consistent with phosphoglycerate kinase chemistry.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a phosphoglycerate kinase, a glycolytic phosphotransferase that uses ATP. Transferable knowledge of this enzyme family supports Mg(2+) coordinating ATP during phosphoryl transfer, making Mg(2+) a meaningful choice over FAD or Fe(2+).",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family and its common Mg-dependent ATP chemistry provides a credible inference from the supplied sequence; the exact-protein annotation is not necessary to distinguish Mg from the unrelated cofactor options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Mg(2+) is itself a divalent metal cation, so option C is broadly true of the cofactor specified in D. D is the more specific answer, but the options are not mutually exclusive."
  },
  "important_caveats": [
    "The supplied evidence supports the key through a similarity-transferred database annotation, not direct experimental evidence for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (A0A7G5KET3, PGK1_ASPFN) annotates Mg(2+) (CHEBI:18420) as the cofactor, with evidence code ECO:0000250 (transferred by similarity from human PGK1, P00558). While the annotation for this specific Aspergillus flavus entry is by similarity, the Mg(2+) requirement for phosphoglycerate kinase (EC 2.7.2.3) is universally established across all characterized PGK homologs and is standard textbook biochemistry. The underlying biology is robustly supported even though the entry-level evidence code is computational transfer.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains highly conserved PGK signature motifs: 'GGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKK' (the GGAKV motif unique to phosphoglycerate kinase), 'GGGDTATVAA' (nucleotide-binding P-loop variant in PGK), and 'GGGASLELLEG' (C-terminal PGK motif). These motifs are diagnostic of the PGK family across all kingdoms. PGK (EC 2.7.2.3) catalyzes the transfer of a phosphoryl group from 1,3-bisphosphoglycerate to ADP, and Mg(2+) is universally required to coordinate the phosphate groups of both substrates. This is textbook-level biochemistry learned from PGK in yeast, human, and bacterial homologs. Distinguishing D (Mg(2+)) from C (a divalent metal cation): the question asks for the specific cofactor. PGK has a specific, well-characterized requirement for Mg(2+) (not generically any divalent cation); the Mg(2+) ion forms a chelate with the β- and γ-phosphates of ATP and the carboxyl/phosphate of 3-PGA in a geometry specific to Mg(2+). While Mn(2+) can weakly substitute in vitro, the physiological and mechanistically required cofactor is Mg(2+). Thus, knowing PGK from any organism transfers the specific Mg(2+) requirement.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of PGK from conserved sequence motifs (GGAKV, GGGDTATVAA) is straightforward family-level pattern matching. The Mg(2+) requirement is universal across all PGK homologs and is standard biochemistry. The specificity distinguishing Mg(2+) from generic divalent cations is well-established mechanistic knowledge about PGK's active site.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While option C ('a divalent metal cation') is technically a superset containing Mg(2+), the question explicitly asks for the 'specific cofactor.' In standard biochemical convention, PGK's cofactor is stated as Mg(2+), not as a generic divalent cation. The mechanistic requirement is specific to Mg(2+) coordination geometry. Option D is the precise and expected answer; C is an overly general category that would not be the standard answer to 'what cofactor does PGK require.'


### Important caveats

- The UniProt cofactor annotation for this specific entry uses evidence code ECO:0000250 (similarity transfer from P00558), not direct experimental measurement on the A. flavus protein. However, PGK's Mg(2+) requirement is so universally conserved and well-characterized that this transfer is scientifically robust.
- Option C ('a divalent metal cation') is technically true as a category but lacks the specificity the question requests. Some in vitro studies show Mn(2+) partial substitution for Mg(2+) in PGK, but this does not change the physiological cofactor assignment.
- The sequence is 417 aa, matching the canonical PGK length in fungi, further supporting family identification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains highly conserved PGK signature motifs: 'GGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKK' (the GGAKV motif unique to phosphoglycerate kinase), 'GGGDTATVAA' (nucleotide-binding P-loop variant in PGK), and 'GGGASLELLEG' (C-terminal PGK motif). These motifs are diagnostic of the PGK family across all kingdoms. PGK (EC 2.7.2.3) catalyzes the transfer of a phosphoryl group from 1,3-bisphosphoglycerate to ADP, and Mg(2+) is universally required to coordinate the phosphate groups of both substrates. This is textbook-level biochemistry learned from PGK in yeast, human, and bacterial homologs. Distinguishing D (Mg(2+)) from C (a divalent metal cation): the question asks for the specific cofactor. PGK has a specific, well-characterized requirement for Mg(2+) (not generically any divalent cation); the Mg(2+) ion forms a chelate with the β- and γ-phosphates of ATP and the carboxyl/phosphate of 3-PGA in a geometry specific to Mg(2+). While Mn(2+) can weakly substitute in vitro, the physiological and mechanistically required cofactor is Mg(2+). Thus, knowing PGK from any organism transfers the specific Mg(2+) requirement.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of PGK from conserved sequence motifs (GGAKV, GGGDTATVAA) is straightforward family-level pattern matching. The Mg(2+) requirement is universal across all PGK homologs and is standard biochemistry. The specificity distinguishing Mg(2+) from generic divalent cations is well-established mechanistic knowledge about PGK's active site."
  },
  "case_id": "cofactor_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A7G5KET3, PGK1_ASPFN) annotates Mg(2+) (CHEBI:18420) as the cofactor, with evidence code ECO:0000250 (transferred by similarity from human PGK1, P00558). While the annotation for this specific Aspergillus flavus entry is by similarity, the Mg(2+) requirement for phosphoglycerate kinase (EC 2.7.2.3) is universally established across all characterized PGK homologs and is standard textbook biochemistry. The underlying biology is robustly supported even though the entry-level evidence code is computational transfer."
  },
  "important_caveats": [
    "The UniProt cofactor annotation for this specific entry uses evidence code ECO:0000250 (similarity transfer from P00558), not direct experimental measurement on the A. flavus protein. However, PGK's Mg(2+) requirement is so universally conserved and well-characterized that this transfer is scientifically robust.",
    "Option C ('a divalent metal cation') is technically true as a category but lacks the specificity the question requests. Some in vitro studies show Mn(2+) partial substitution for Mg(2+) in PGK, but this does not change the physiological cofactor assignment.",
    "The sequence is 417 aa, matching the canonical PGK length in fungi, further supporting family identification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option C ('a divalent metal cation') is technically a superset containing Mg(2+), the question explicitly asks for the 'specific cofactor.' In standard biochemical convention, PGK's cofactor is stated as Mg(2+), not as a generic divalent cation. The mechanistic requirement is specific to Mg(2+) coordination geometry. Option D is the precise and expected answer; C is an overly general category that would not be the standard answer to 'what cofactor does PGK require.'"
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A7G5KET3, PGK1_ASPFN) annotates Mg(2+) (CHEBI:18420) as the cofactor, with evidence code ECO:0000250 (transferred by similarity from human PGK1, P00558). While the annotation for this specific Aspergillus flavus entry is by similarity, the Mg(2+) requirement for phosphoglycerate kinase (EC 2.7.2.3) is universally established across all characterized PGK homologs and is standard textbook biochemistry. The underlying biology is robustly supported even though the entry-level evidence code is computational transfer.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains highly conserved PGK signature motifs: 'GGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKK' (the GGAKV motif unique to phosphoglycerate kinase), 'GGGDTATVAA' (nucleotide-binding P-loop variant in PGK), and 'GGGASLELLEG' (C-terminal PGK motif). These motifs are diagnostic of the PGK family across all kingdoms. PGK (EC 2.7.2.3) catalyzes the transfer of a phosphoryl group from 1,3-bisphosphoglycerate to ADP, and Mg(2+) is universally required to coordinate the phosphate groups of both substrates. This is textbook-level biochemistry learned from PGK in yeast, human, and bacterial homologs. Distinguishing D (Mg(2+)) from C (a divalent metal cation): the question asks for the specific cofactor. PGK has a specific, well-characterized requirement for Mg(2+) (not generically any divalent cation); the Mg(2+) ion forms a chelate with the β- and γ-phosphates of ATP and the carboxyl/phosphate of 3-PGA in a geometry specific to Mg(2+). While Mn(2+) can weakly substitute in vitro, the physiological and mechanistically required cofactor is Mg(2+). Thus, knowing PGK from any organism transfers the specific Mg(2+) requirement.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of PGK from conserved sequence motifs (GGAKV, GGGDTATVAA) is straightforward family-level pattern matching. The Mg(2+) requirement is universal across all PGK homologs and is standard biochemistry. The specificity distinguishing Mg(2+) from generic divalent cations is well-established mechanistic knowledge about PGK's active site."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option C ('a divalent metal cation') is technically a superset containing Mg(2+), the question explicitly asks for the 'specific cofactor.' In standard biochemical convention, PGK's cofactor is stated as Mg(2+), not as a generic divalent cation. The mechanistic requirement is specific to Mg(2+) coordination geometry. Option D is the precise and expected answer; C is an overly general category that would not be the standard answer to 'what cofactor does PGK require.'"
  },
  "important_caveats": [
    "The UniProt cofactor annotation for this specific entry uses evidence code ECO:0000250 (similarity transfer from P00558), not direct experimental measurement on the A. flavus protein. However, PGK's Mg(2+) requirement is so universally conserved and well-characterized that this transfer is scientifically robust.",
    "Option C ('a divalent metal cation') is technically true as a category but lacks the specificity the question requests. Some in vitro studies show Mn(2+) partial substitution for Mg(2+) in PGK, but this does not change the physiological cofactor assignment.",
    "The sequence is 417 aa, matching the canonical PGK length in fungi, further supporting family identification."
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
  "benchmark_sequence_length": 417,
  "benchmark_sequence_sha256": "275622872aa5039ffd4e2fafadfa8fcabe446204f6ab488fbd8b5e29f8a6b5e4",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-02-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 417,
  "current_source_sequence_sha256": "275622872aa5039ffd4e2fafadfa8fcabe446204f6ab488fbd8b5e29f8a6b5e4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7G5KET3",
  "selected_historical_entry_version": 18,
  "selected_historical_record_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "selected_historical_source_sequence_length": 417,
  "selected_historical_source_sequence_sha256": "275622872aa5039ffd4e2fafadfa8fcabe446204f6ab488fbd8b5e29f8a6b5e4",
  "selected_historical_version": {
    "accession": "A0A7G5KET3",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PGK1_ASPFN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7G5KET3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-02-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000596276\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357 / JCM 12722 / SRRC 167)\",\"taxonId\":332952}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00560\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.2.3\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU000532\",\"source\":\"RuleBase\"}],\"value\":\"Phosphoglycerate kinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00558\",\"source\":\"UniProtKB\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H1",
  "excerpt": "ID   PGK1_ASPFN              Reviewed;         417 AA.\nAC   A0A7G5KET3; B8NIQ9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-FEB-2021, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=Phosphoglycerate kinase {ECO:0000255|RuleBase:RU000532};\nDE            EC=2.7.2.3 {ECO:0000250|UniProtKB:P00560};\nGN   Name=pgk1 {ECO:0000303|PubMed:37754565};\nGN   ORFNames=F9C07_8361 {ECO:0000312|EMBL:QRD93909.1};\nOS   Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357\nOS   / JCM 12722 / SRRC 167).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=332952 {ECO:0000312|Proteomes:UP000596276};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Phosphoglycerate kinase {ECO:0000255|RuleBase:RU000532};\nDE            EC=2.7.2.3 {ECO:0000250|UniProtKB:P00560};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, PHOSPHORYLATION AT\nRP   SER-203, AND MUTAGENESIS OF SER-203.\nRX   PubMed=37754565; DOI=10.1128/mbio.00977-23;\nRA   Zhu Z., Yang M., Yang G., Zhang B., Cao X., Yuan J., Ge F., Wang S.;\nRT   \"PP2C phosphatases Ptc1 and Ptc2 dephosphorylate PGK1 to regulate autophagy\nRT   and aflatoxin synthesis in the pathogenic fungus Aspergillus flavus.\";\nRL   MBio 14:e0097723-e0097723(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000250|UniProtKB:P00558};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 39. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
