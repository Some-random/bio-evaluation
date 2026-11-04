# cofactor_0179

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0179.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSLVRNSSRLLRSQLKRVQSVPVALYHENVVEHYENPRNVGSLDKKDVTVGTGLVGAPACGDVMKLQIKVDENGKIVDAKFKTFGCGSAIASSSLATEWVKGKSIDEAGKLKNTDIAKELRLPPVKLHCSMLAEDAIKAALADYKVKQQKKVAN

[Multiple Choices]
A. Fe(2+)
B. Fe cation
C. Na(+)
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

> The sequence-matched annotation identifies this protein as an IscU iron-sulfur cluster assembly scaffold and reports Fe(2+) binding, with experimental evidence cited. That supports A, though the annotation also lists a &#91;2Fe-2S&#93; cluster, which is not an option.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short, cysteine-containing sequence is consistent with an IscU-like iron-sulfur cluster scaffold. Transferable knowledge of this protein family supports iron binding and makes Fe(2+) a meaningful choice over Na(+) or heme b; Fe(2+) is the more specific iron choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and knowledge of IscU scaffolds provide a credible basis for selecting iron without knowing this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Fe(2+) is itself an iron cation, so B can describe the same cofactor more broadly. A is the more specific and better-supported choice, but the options overlap.


### Important caveats

- The supplied evidence reports both Fe(2+) binding and binding of a &#91;2Fe-2S&#93; cluster; the latter is absent from the choices.
- The source annotation cites experimental evidence, but the underlying primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short, cysteine-containing sequence is consistent with an IscU-like iron-sulfur cluster scaffold. Transferable knowledge of this protein family supports iron binding and makes Fe(2+) a meaningful choice over Na(+) or heme b; Fe(2+) is the more specific iron choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and knowledge of IscU scaffolds provide a credible basis for selecting iron without knowing this exact protein's database record."
  },
  "case_id": "cofactor_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies this protein as an IscU iron-sulfur cluster assembly scaffold and reports Fe(2+) binding, with experimental evidence cited. That supports A, though the annotation also lists a [2Fe-2S] cluster, which is not an option."
  },
  "important_caveats": [
    "The supplied evidence reports both Fe(2+) binding and binding of a [2Fe-2S] cluster; the latter is absent from the choices.",
    "The source annotation cites experimental evidence, but the underlying primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Fe(2+) is itself an iron cation, so B can describe the same cofactor more broadly. A is the more specific and better-supported choice, but the options overlap."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies this protein as an IscU iron-sulfur cluster assembly scaffold and reports Fe(2+) binding, with experimental evidence cited. That supports A, though the annotation also lists a [2Fe-2S] cluster, which is not an option.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short, cysteine-containing sequence is consistent with an IscU-like iron-sulfur cluster scaffold. Transferable knowledge of this protein family supports iron binding and makes Fe(2+) a meaningful choice over Na(+) or heme b; Fe(2+) is the more specific iron choice.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and knowledge of IscU scaffolds provide a credible basis for selecting iron without knowing this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Fe(2+) is itself an iron cation, so B can describe the same cofactor more broadly. A is the more specific and better-supported choice, but the options overlap."
  },
  "important_caveats": [
    "The supplied evidence reports both Fe(2+) binding and binding of a [2Fe-2S] cluster; the latter is absent from the choices.",
    "The source annotation cites experimental evidence, but the underlying primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VHK6 (ISCU_DROME) lists Fe(2+) as a cofactor with experimental evidence (ECO:0000269|PubMed:27738674). The annotation states: 'Fe(2+) binding protein that acts as a scaffold for the assembly of iron-sulfur clusters.' The Dzul et al. 2017 Metallomics paper experimentally characterized Fe(2+) binding. The answer A (Fe(2+)) matches the database annotation precisely.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark IscU/Isu scaffold protein motifs: the conserved Cys-containing segments 'ACGDVMK', 'GCGSAIASSS', and 'VKLHCS' are characteristic of the IscU/Isu family across organisms (E. coli IscU, yeast Isu1/Isu2, human ISCU). This family is universally characterized as binding Fe(2+) (ferrous iron) specifically as a substrate for de novo &#91;2Fe-2S&#93; cluster assembly. This eliminates C (Na+, no role in Fe-S assembly) and D (heme b, a prosthetic group unrelated to Fe-S cluster scaffolds). Between A (Fe(2+)) and B (Fe cation), the family-level mechanism is specific to the +2 oxidation state: IscU/Isu proteins coordinate ferrous Fe(2+) via conserved Cys residues and then oxidatively assemble it into &#91;2Fe-2S&#93; clusters. The question asks for the 'specific cofactor,' and Fe(2+) specifies the required oxidation state while 'Fe cation' is generic (could include Fe(3+), which is not the substrate for this scaffold). This oxidation-state specificity is a well-documented, transferable feature of the IscU/Isu family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the IscU/Isu protein family from conserved Cys motifs and the well-known family mechanism (specific Fe(2+) binding for &#91;2Fe-2S&#93; assembly) provides a concrete, transferable argument distinguishing A from B, C, and D without needing to look up this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Fe(2+) is technically an 'Fe cation,' so option B is not factually wrong—just less specific. The question asks for the 'specific cofactor,' which favors A, but a model could reasonably argue B is also correct since Fe(2+) is a subset of 'Fe cation.' The distinction rests on the question's emphasis on specificity rather than on a categorical exclusion of B.


### Important caveats

- The distinction between A (Fe(2+)) and B (Fe cation) is one of specificity rather than categorical correctness; Fe(2+) IS an iron cation.
- The UniProt annotation also lists &#91;2Fe-2S&#93; cluster as a cofactor, which is not offered as an option.
- The experimental evidence (PubMed:27738674) specifically characterizes Fe(2+) binding, supporting the oxidation-state specificity of answer A over the generic 'Fe cation' in B.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark IscU/Isu scaffold protein motifs: the conserved Cys-containing segments 'ACGDVMK', 'GCGSAIASSS', and 'VKLHCS' are characteristic of the IscU/Isu family across organisms (E. coli IscU, yeast Isu1/Isu2, human ISCU). This family is universally characterized as binding Fe(2+) (ferrous iron) specifically as a substrate for de novo [2Fe-2S] cluster assembly. This eliminates C (Na+, no role in Fe-S assembly) and D (heme b, a prosthetic group unrelated to Fe-S cluster scaffolds). Between A (Fe(2+)) and B (Fe cation), the family-level mechanism is specific to the +2 oxidation state: IscU/Isu proteins coordinate ferrous Fe(2+) via conserved Cys residues and then oxidatively assemble it into [2Fe-2S] clusters. The question asks for the 'specific cofactor,' and Fe(2+) specifies the required oxidation state while 'Fe cation' is generic (could include Fe(3+), which is not the substrate for this scaffold). This oxidation-state specificity is a well-documented, transferable feature of the IscU/Isu family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the IscU/Isu protein family from conserved Cys motifs and the well-known family mechanism (specific Fe(2+) binding for [2Fe-2S] assembly) provides a concrete, transferable argument distinguishing A from B, C, and D without needing to look up this exact protein's annotation."
  },
  "case_id": "cofactor_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VHK6 (ISCU_DROME) lists Fe(2+) as a cofactor with experimental evidence (ECO:0000269|PubMed:27738674). The annotation states: 'Fe(2+) binding protein that acts as a scaffold for the assembly of iron-sulfur clusters.' The Dzul et al. 2017 Metallomics paper experimentally characterized Fe(2+) binding. The answer A (Fe(2+)) matches the database annotation precisely."
  },
  "important_caveats": [
    "The distinction between A (Fe(2+)) and B (Fe cation) is one of specificity rather than categorical correctness; Fe(2+) IS an iron cation.",
    "The UniProt annotation also lists [2Fe-2S] cluster as a cofactor, which is not offered as an option.",
    "The experimental evidence (PubMed:27738674) specifically characterizes Fe(2+) binding, supporting the oxidation-state specificity of answer A over the generic 'Fe cation' in B."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Fe(2+) is technically an 'Fe cation,' so option B is not factually wrong—just less specific. The question asks for the 'specific cofactor,' which favors A, but a model could reasonably argue B is also correct since Fe(2+) is a subset of 'Fe cation.' The distinction rests on the question's emphasis on specificity rather than on a categorical exclusion of B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VHK6 (ISCU_DROME) lists Fe(2+) as a cofactor with experimental evidence (ECO:0000269|PubMed:27738674). The annotation states: 'Fe(2+) binding protein that acts as a scaffold for the assembly of iron-sulfur clusters.' The Dzul et al. 2017 Metallomics paper experimentally characterized Fe(2+) binding. The answer A (Fe(2+)) matches the database annotation precisely.",
    "evidence_ids": ["C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark IscU/Isu scaffold protein motifs: the conserved Cys-containing segments 'ACGDVMK', 'GCGSAIASSS', and 'VKLHCS' are characteristic of the IscU/Isu family across organisms (E. coli IscU, yeast Isu1/Isu2, human ISCU). This family is universally characterized as binding Fe(2+) (ferrous iron) specifically as a substrate for de novo [2Fe-2S] cluster assembly. This eliminates C (Na+, no role in Fe-S assembly) and D (heme b, a prosthetic group unrelated to Fe-S cluster scaffolds). Between A (Fe(2+)) and B (Fe cation), the family-level mechanism is specific to the +2 oxidation state: IscU/Isu proteins coordinate ferrous Fe(2+) via conserved Cys residues and then oxidatively assemble it into [2Fe-2S] clusters. The question asks for the 'specific cofactor,' and Fe(2+) specifies the required oxidation state while 'Fe cation' is generic (could include Fe(3+), which is not the substrate for this scaffold). This oxidation-state specificity is a well-documented, transferable feature of the IscU/Isu family.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the IscU/Isu protein family from conserved Cys motifs and the well-known family mechanism (specific Fe(2+) binding for [2Fe-2S] assembly) provides a concrete, transferable argument distinguishing A from B, C, and D without needing to look up this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Fe(2+) is technically an 'Fe cation,' so option B is not factually wrong—just less specific. The question asks for the 'specific cofactor,' which favors A, but a model could reasonably argue B is also correct since Fe(2+) is a subset of 'Fe cation.' The distinction rests on the question's emphasis on specificity rather than on a categorical exclusion of B."
  },
  "important_caveats": [
    "The distinction between A (Fe(2+)) and B (Fe cation) is one of specificity rather than categorical correctness; Fe(2+) IS an iron cation.",
    "The UniProt annotation also lists [2Fe-2S] cluster as a cofactor, which is not offered as an option.",
    "The experimental evidence (PubMed:27738674) specifically characterizes Fe(2+) binding, supporting the oxidation-state specificity of answer A over the generic 'Fe cation' in B."
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
  "benchmark_sequence_length": 154,
  "benchmark_sequence_sha256": "05d96ad7f89c4b2d79479233554410215049beb269b097bdc3f1d62855a807c4",
  "current_entry_audit": {
    "entryVersion": 198,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 154,
  "current_source_sequence_sha256": "05d96ad7f89c4b2d79479233554410215049beb269b097bdc3f1d62855a807c4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 196,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VHK6",
  "selected_historical_entry_version": 196,
  "selected_historical_record_sha256": "4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68",
  "selected_historical_source_sequence_length": 154,
  "selected_historical_source_sequence_sha256": "05d96ad7f89c4b2d79479233554410215049beb269b097bdc3f1d62855a807c4",
  "selected_historical_version": {
    "accession": "Q9VHK6",
    "database": "Swiss-Prot",
    "entryVersion": 196,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ISCU_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VHK6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:20.640117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHK6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":198,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:20.640117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHK6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:20.640117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHK6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0037637\",\"source\":\"FlyBase\"}],\"value\":\"Iron-sulfur cluster assembly enzyme IscU\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27738674\",\"source\":\"PubMed\"}],\"value\":\"fIscU\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:20.640117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHK6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29033\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27738674\",\"source\":\"PubMed\"}],\"name\":\"Fe(2+)\"},{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27738674\",\"source\":\"PubMed\"}],\"name\":\"[2Fe-2S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27738674\",\"source\":\"PubMed\"}],\"value\":\"Fe(2+) binding protein that acts as a scaffold for the assembly of iron-sulfur clusters (PubMed:27738674). Binds 1 [2Fe-2S] cluster per subunit (PubMed:27738674).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:20.640117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHK6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dzul S.P.\",\"Rocha A.G.\",\"Rawat S.\",\"Kandegedara A.\",\"Kusowski A.\",\"Pain J.\",\"Murari A.\",\"Pain D.\",\"Dancis A.\",\"Stemmler T.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27738674\"},{\"database\":\"DOI\",\"id\":\"10.1039/c6mt00163g\"}],\"citationType\":\"journal article\",\"firstPage\":\"48\",\"id\":\"27738674\",\"journal\":\"Metallomics\",\"lastPage\":\"60\",\"publicationDate\":\"2017\",\"title\":\"In vitro characterization of a novel Isu homologue from Drosophila melanogaster for de novo FeS-cluster formation.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"COFACTOR\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:20.640117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHK6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196)

```json
{
  "entry_version": 196,
  "evidence_id": "H1",
  "excerpt": "ID   ISCU_DROME              Reviewed;         154 AA.\nAC   Q9VHK6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 196.\nDE   RecName: Full=Iron-sulfur cluster assembly enzyme IscU {ECO:0000312|FlyBase:FBgn0037637};\nDE            Short=fIscU {ECO:0000303|PubMed:27738674};\nGN   Name=IscU {ECO:0000312|FlyBase:FBgn0037637};\nGN   Synonyms=Isu1 {ECO:0000312|FlyBase:FBgn0037637};\nGN   ORFNames=CG9836 {ECO:0000312|FlyBase:FBgn0037637};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:26.936483+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68",
  "url": "https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196)

```json
{
  "entry_version": 196,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Iron-sulfur cluster assembly enzyme IscU {ECO:0000312|FlyBase:FBgn0037637};\nDE            Short=fIscU {ECO:0000303|PubMed:27738674};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:26.936483+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68",
  "url": "https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196)

```json
{
  "entry_version": 196,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, COFACTOR, AND PATHWAY.\nRX   PubMed=27738674; DOI=10.1039/c6mt00163g;\nRA   Dzul S.P., Rocha A.G., Rawat S., Kandegedara A., Kusowski A., Pain J.,\nRA   Murari A., Pain D., Dancis A., Stemmler T.L.;\nRT   \"In vitro characterization of a novel Isu homologue from Drosophila\nRT   melanogaster for de novo FeS-cluster formation.\";\nRL   Metallomics 9:48-60(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:26.936483+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68",
  "url": "https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196)

```json
{
  "entry_version": 196,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;\nCC         Evidence={ECO:0000269|PubMed:27738674};\nCC       Name=[2Fe-2S] cluster; Xref=ChEBI:CHEBI:190135;\nCC         Evidence={ECO:0000269|PubMed:27738674};\nCC       Note=Fe(2+) binding protein that acts as a scaffold for the assembly of\nCC       iron-sulfur clusters (PubMed:27738674). Binds 1 [2Fe-2S] cluster per\nCC       subunit (PubMed:27738674). {ECO:0000269|PubMed:27738674};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:26.936483+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68",
  "url": "https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 179. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
