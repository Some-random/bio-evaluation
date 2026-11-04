# cofactor_0118

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0118.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTTASSDPLLQPFTLKHLVLKNRVMSTSHASRLTRDEFPQEVYQRYHEEKAKGGLALTMFGGSSNVSLDSPNTFQQINLSADAVVPHLRRFSDRIHTHGAALMCQITHLGRRGDAYTEPWLPMIAPSPVRETLHRAMPQAIHDADIKRVIRDFGLAAKRCRDGGLDGIETHAGGHLIGQFMDPTVNLRTDKYGGSTANRVRFAIEVHEEIRKQVGDDFVVGFRFALEDGCSFEEGLEMSRILQGTGLFDFFNVTFGRMDTKMALAVNSMPGMFVPSAPWLPKAAAFKRAVDLPVFHAAKIADLATARYAIREGLLDMVGMTRAHIAEPHLVKLVEAGKEDEARPCVGASFCRNFRATCIHNPATSRETYLTHDIPKAAQTKRVLIVGAGPAGLEAARICATRGHDVTVLEANSTAGGQLLLAATGSWRRDLIGIVDWRVSALERLSVDVRYNHYAELSDVLDHGADVVIIATGGLPNLDALPGAEHCKSVFDALTETPPREGSVIVYDGTGRHNAYLCAERYVDAGLDVSLALIDSMPAQETGGRGDDQVWMRNIARWDVPVRTNIELIEVTASSNGKRRAVFQHHLTNERVELEADHVVVERGMLAVEDLFEAARMYSANDGYTDLEAFATGKPQPGHEAEEGQFHLYRIGDASASRDIHTAIYDAYRLCLAL

[Multiple Choices]
A. Zn(2+)
B. [4Fe-4S] cluster
C. pyridoxal 5'-phosphate
D. Fe cation
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

> The sequence-matched UniProt annotation reports one &#91;4Fe-4S&#93; cluster per monomer and cites experimental evidence from a publication. This supports choice B, though the annotation is not independent validation of the underlying study.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a cysteine-rich segment with a C-X5-C-X6-C pattern. Multiple suitably spaced cysteines are a plausible transferable feature of iron-sulfur cluster-binding sites, distinguishing a &#91;4Fe-4S&#93; cluster from a single Fe cation and making it more suggestive than a PLP cofactor. Cysteines can also coordinate Zn, so the motif is suggestive rather than conclusive.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A recognizable multi-cysteine motif provides a meaningful sequence-based basis for choosing the iron-sulfur cluster among these alternatives. The exact protein annotation is not necessary for that probabilistic inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the sequence motif is not definitive by itself, the offered choices distinguish an iron-sulfur cluster from the alternative cofactors; no second choice is comparably supported.


### Important caveats

- The reviewer-only annotation also lists FAD and FMN, neither of which is offered. Thus B is supported among the choices, but the options may not enumerate every cofactor associated with the protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine-rich segment with a C-X5-C-X6-C pattern. Multiple suitably spaced cysteines are a plausible transferable feature of iron-sulfur cluster-binding sites, distinguishing a [4Fe-4S] cluster from a single Fe cation and making it more suggestive than a PLP cofactor. Cysteines can also coordinate Zn, so the motif is suggestive rather than conclusive.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A recognizable multi-cysteine motif provides a meaningful sequence-based basis for choosing the iron-sulfur cluster among these alternatives. The exact protein annotation is not necessary for that probabilistic inference."
  },
  "case_id": "cofactor_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports one [4Fe-4S] cluster per monomer and cites experimental evidence from a publication. This supports choice B, though the annotation is not independent validation of the underlying study."
  },
  "important_caveats": [
    "The reviewer-only annotation also lists FAD and FMN, neither of which is offered. Thus B is supported among the choices, but the options may not enumerate every cofactor associated with the protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the sequence motif is not definitive by itself, the offered choices distinguish an iron-sulfur cluster from the alternative cofactors; no second choice is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports one [4Fe-4S] cluster per monomer and cites experimental evidence from a publication. This supports choice B, though the annotation is not independent validation of the underlying study.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a cysteine-rich segment with a C-X5-C-X6-C pattern. Multiple suitably spaced cysteines are a plausible transferable feature of iron-sulfur cluster-binding sites, distinguishing a [4Fe-4S] cluster from a single Fe cation and making it more suggestive than a PLP cofactor. Cysteines can also coordinate Zn, so the motif is suggestive rather than conclusive.",
    "missing_item_specific_fact": "",
    "reason": "A recognizable multi-cysteine motif provides a meaningful sequence-based basis for choosing the iron-sulfur cluster among these alternatives. The exact protein annotation is not necessary for that probabilistic inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the sequence motif is not definitive by itself, the offered choices distinguish an iron-sulfur cluster from the alternative cofactors; no second choice is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only annotation also lists FAD and FMN, neither of which is offered. Thus B is supported among the choices, but the options may not enumerate every cofactor associated with the protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXY1 (OYE_CABCO) annotates a &#91;4Fe-4S&#93; cluster cofactor with experimental evidence (ECO:0000269|PubMed:39867842), stating 'Binds 1 &#91;4Fe-4S&#93; cluster per monomer via a modified motif.' The sequence matches exactly (SHA256 confirmed). The FAD and FMN cofactors listed in the same entry are annotated only with inferred evidence (ECO:0000305), and neither is among the answer choices. Among the four offered options, &#91;4Fe-4S&#93; is the experimentally supported cofactor.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The specific experimental finding (PubMed:39867842, 2025) that the 2-ER subfamily of OYE proteins binds a &#91;4Fe-4S&#93; cluster via a modified (non-canonical) cysteine motif. This is a novel, subfamily-specific discovery that contradicts the classical OYE family paradigm of flavin-only cofactors.


**Reason**

> Recognizing this protein as an Old Yellow Enzyme (OYE) family member from sequence motifs (TIM-barrel fold, conserved catalytic residues) would lead a knowledgeable model toward flavin cofactors (FMN/FAD), which are NOT among the answer choices. Classical OYE knowledge actually argues AGAINST &#91;4Fe-4S&#93; clusters, as OYEs are canonically flavoproteins without iron-sulfur centers. The &#91;4Fe-4S&#93; binding in this 2-ER subfamily is a novel 2025 experimental finding. The binding motif is explicitly annotated as 'modified'—the cysteine spacing in the sequence (~C6C7C3P) deviates drastically from the canonical &#91;4Fe-4S&#93; motif (CxxCxxCxxxCP), making reliable sequence-based identification of the cluster site essentially impossible without prior knowledge of this specific finding. Transferable knowledge of Fe-S clusters in other oxidoreductases (ferredoxins, hydrogenases) does not apply to the OYE fold. Among the four choices, none can be confidently eliminated or selected using family-level reasoning alone: Zn2+ is atypical for OYEs, PLP is for aminotransferases, and Fe cation vs &#91;4Fe-4S&#93; cannot be distinguished from the modified motif without knowing the experimental result.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While FAD and FMN are also annotated cofactors for this protein (inferred evidence), neither appears among the four choices. Among the offered options, only &#91;4Fe-4S&#93; has experimental support. The other three (Zn2+, PLP, Fe cation) have no annotation or experimental backing for this protein. No ambiguity among the offered choices exists given the experimental evidence, though the question's difficulty lies in identifying the correct answer from sequence alone.


### Important caveats

- The &#91;4Fe-4S&#93; cluster finding is from a 2025 publication (PubMed:39867842) and represents a novel activity in the 2-ER OYE subfamily, discovered via bioinformatic and biochemical analysis.
- The binding motif is explicitly described as 'modified,' meaning it does not follow the canonical CxxCxxCxxxCP pattern, making sequence-based detection extremely challenging.
- FAD and FMN are also listed as cofactors (inferred by similarity) but are not among the answer choices.
- The protein is 674 AA long and belongs to the OYE/ene reductase superfamily, which is classically a flavoprotein family without iron-sulfur clusters.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental finding (PubMed:39867842, 2025) that the 2-ER subfamily of OYE proteins binds a [4Fe-4S] cluster via a modified (non-canonical) cysteine motif. This is a novel, subfamily-specific discovery that contradicts the classical OYE family paradigm of flavin-only cofactors.",
    "reason": "Recognizing this protein as an Old Yellow Enzyme (OYE) family member from sequence motifs (TIM-barrel fold, conserved catalytic residues) would lead a knowledgeable model toward flavin cofactors (FMN/FAD), which are NOT among the answer choices. Classical OYE knowledge actually argues AGAINST [4Fe-4S] clusters, as OYEs are canonically flavoproteins without iron-sulfur centers. The [4Fe-4S] binding in this 2-ER subfamily is a novel 2025 experimental finding. The binding motif is explicitly annotated as 'modified'—the cysteine spacing in the sequence (~C6C7C3P) deviates drastically from the canonical [4Fe-4S] motif (CxxCxxCxxxCP), making reliable sequence-based identification of the cluster site essentially impossible without prior knowledge of this specific finding. Transferable knowledge of Fe-S clusters in other oxidoreductases (ferredoxins, hydrogenases) does not apply to the OYE fold. Among the four choices, none can be confidently eliminated or selected using family-level reasoning alone: Zn2+ is atypical for OYEs, PLP is for aminotransferases, and Fe cation vs [4Fe-4S] cannot be distinguished from the modified motif without knowing the experimental result."
  },
  "case_id": "cofactor_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXY1 (OYE_CABCO) annotates a [4Fe-4S] cluster cofactor with experimental evidence (ECO:0000269|PubMed:39867842), stating 'Binds 1 [4Fe-4S] cluster per monomer via a modified motif.' The sequence matches exactly (SHA256 confirmed). The FAD and FMN cofactors listed in the same entry are annotated only with inferred evidence (ECO:0000305), and neither is among the answer choices. Among the four offered options, [4Fe-4S] is the experimentally supported cofactor."
  },
  "important_caveats": [
    "The [4Fe-4S] cluster finding is from a 2025 publication (PubMed:39867842) and represents a novel activity in the 2-ER OYE subfamily, discovered via bioinformatic and biochemical analysis.",
    "The binding motif is explicitly described as 'modified,' meaning it does not follow the canonical CxxCxxCxxxCP pattern, making sequence-based detection extremely challenging.",
    "FAD and FMN are also listed as cofactors (inferred by similarity) but are not among the answer choices.",
    "The protein is 674 AA long and belongs to the OYE/ene reductase superfamily, which is classically a flavoprotein family without iron-sulfur clusters."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While FAD and FMN are also annotated cofactors for this protein (inferred evidence), neither appears among the four choices. Among the offered options, only [4Fe-4S] has experimental support. The other three (Zn2+, PLP, Fe cation) have no annotation or experimental backing for this protein. No ambiguity among the offered choices exists given the experimental evidence, though the question's difficulty lies in identifying the correct answer from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXY1 (OYE_CABCO) annotates a [4Fe-4S] cluster cofactor with experimental evidence (ECO:0000269|PubMed:39867842), stating 'Binds 1 [4Fe-4S] cluster per monomer via a modified motif.' The sequence matches exactly (SHA256 confirmed). The FAD and FMN cofactors listed in the same entry are annotated only with inferred evidence (ECO:0000305), and neither is among the answer choices. Among the four offered options, [4Fe-4S] is the experimentally supported cofactor.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The specific experimental finding (PubMed:39867842, 2025) that the 2-ER subfamily of OYE proteins binds a [4Fe-4S] cluster via a modified (non-canonical) cysteine motif. This is a novel, subfamily-specific discovery that contradicts the classical OYE family paradigm of flavin-only cofactors.",
    "reason": "Recognizing this protein as an Old Yellow Enzyme (OYE) family member from sequence motifs (TIM-barrel fold, conserved catalytic residues) would lead a knowledgeable model toward flavin cofactors (FMN/FAD), which are NOT among the answer choices. Classical OYE knowledge actually argues AGAINST [4Fe-4S] clusters, as OYEs are canonically flavoproteins without iron-sulfur centers. The [4Fe-4S] binding in this 2-ER subfamily is a novel 2025 experimental finding. The binding motif is explicitly annotated as 'modified'—the cysteine spacing in the sequence (~C6C7C3P) deviates drastically from the canonical [4Fe-4S] motif (CxxCxxCxxxCP), making reliable sequence-based identification of the cluster site essentially impossible without prior knowledge of this specific finding. Transferable knowledge of Fe-S clusters in other oxidoreductases (ferredoxins, hydrogenases) does not apply to the OYE fold. Among the four choices, none can be confidently eliminated or selected using family-level reasoning alone: Zn2+ is atypical for OYEs, PLP is for aminotransferases, and Fe cation vs [4Fe-4S] cannot be distinguished from the modified motif without knowing the experimental result."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While FAD and FMN are also annotated cofactors for this protein (inferred evidence), neither appears among the four choices. Among the offered options, only [4Fe-4S] has experimental support. The other three (Zn2+, PLP, Fe cation) have no annotation or experimental backing for this protein. No ambiguity among the offered choices exists given the experimental evidence, though the question's difficulty lies in identifying the correct answer from sequence alone."
  },
  "important_caveats": [
    "The [4Fe-4S] cluster finding is from a 2025 publication (PubMed:39867842) and represents a novel activity in the 2-ER OYE subfamily, discovered via bioinformatic and biochemical analysis.",
    "The binding motif is explicitly described as 'modified,' meaning it does not follow the canonical CxxCxxCxxxCP pattern, making sequence-based detection extremely challenging.",
    "FAD and FMN are also listed as cofactors (inferred by similarity) but are not among the answer choices.",
    "The protein is 674 AA long and belongs to the OYE/ene reductase superfamily, which is classically a flavoprotein family without iron-sulfur clusters."
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
  "benchmark_sequence_length": 674,
  "benchmark_sequence_sha256": "d0a9daceb358a7ab215246a52585cb052774e4be4676ac0c90d1d7ce1289a52e",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 674,
  "current_source_sequence_sha256": "d0a9daceb358a7ab215246a52585cb052774e4be4676ac0c90d1d7ce1289a52e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXY1",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "selected_historical_source_sequence_length": 674,
  "selected_historical_source_sequence_sha256": "d0a9daceb358a7ab215246a52585cb052774e4be4676ac0c90d1d7ce1289a52e",
  "selected_historical_version": {
    "accession": "P0DXY1",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OYE_CABCO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXY1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Burkholderia cordobensis\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Burkholderiaceae\",\"Caballeronia\"],\"scientificName\":\"Caballeronia cordobensis\",\"taxonId\":1353886}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"value\":\"Old yellow enzyme\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"value\":\"OYE\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"value\":\"1.14.13.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"value\":\"1.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Multifunctional alkene reductase/demethylase OYE\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:49883\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"name\":\"[4Fe-4S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 [4Fe-4S] cluster per monomer via a modified motif.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"name\":\"FAD\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39867842\",\"source\":\"PubMed\"}],\"name\":\"FMN\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXY1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Blue-Lahom T.C.\",\"Jones S.K.\",\"Davis K.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39867842\"},{\"database\":\"DOI\",\"id\":\"10.1039/d4cb00289j\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"39867842\",\"journal\":\"RSC Chem. Biol.\",\"lastPage\":\"0\",\"publicationDate\":\"2025\",\"title\":\"Bioinformatic and biochemical analysis uncovers novel activity in the 2-ER subfamily of OYEs.\",\"volume\":\"0\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"RPE67\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PROBABLE ACTIVE SITE\",\"COFACTORS\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:16.880149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3fba688935042654968bdf1fadb0a0c52f92e43252c7775d80a434e6cfed86b1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXY1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   OYE_CABCO               Reviewed;         674 AA.\nAC   P0DXY1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Multifunctional alkene reductase/demethylase OYE {ECO:0000305};\nDE            EC=1.14.13.- {ECO:0000269|PubMed:39867842};\nDE            EC=1.3.1.- {ECO:0000269|PubMed:39867842};\nDE   AltName: Full=Old yellow enzyme {ECO:0000303|PubMed:39867842};\nDE            Short=OYE {ECO:0000303|PubMed:39867842};\nGN   ORFNames=BRPE67_CCDS01850;\nOS   Caballeronia cordobensis (Burkholderia cordobensis).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Burkholderiaceae; Caballeronia.\nOX   NCBI_TaxID=1353886;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Multifunctional alkene reductase/demethylase OYE {ECO:0000305};\nDE            EC=1.14.13.- {ECO:0000269|PubMed:39867842};\nDE            EC=1.3.1.- {ECO:0000269|PubMed:39867842};\nDE   AltName: Full=Old yellow enzyme {ECO:0000303|PubMed:39867842};\nDE            Short=OYE {ECO:0000303|PubMed:39867842};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PROBABLE ACTIVE SITE, COFACTORS, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=RPE67;\nRX   PubMed=39867842; DOI=10.1039/d4cb00289j;\nRA   Blue-Lahom T.C., Jones S.K., Davis K.M.;\nRT   \"Bioinformatic and biochemical analysis uncovers novel activity in the 2-ER\nRT   subfamily of OYEs.\";\nRL   RSC Chem. Biol. 0:0-0(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;\nCC         Evidence={ECO:0000269|PubMed:39867842};\nCC       Note=Binds 1 [4Fe-4S] cluster per monomer via a modified motif.\nCC       {ECO:0000269|PubMed:39867842};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FAD; Xref=ChEBI:CHEBI:57692;\nCC         Evidence={ECO:0000305|PubMed:39867842};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FMN; Xref=ChEBI:CHEBI:58210;\nCC         Evidence={ECO:0000305|PubMed:39867842};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.698464+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b8b06905ea45150fa9b6f70f9b288d08c0b0848d8de03baf3ae90bcfae3ac1",
  "url": "https://rest.uniprot.org/unisave/P0DXY1?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
