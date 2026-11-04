# pathway_0108

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0108.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Metabolic intermediate biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSYGESHGKAIGCVIDGFLSNIEINFDLIQKQLDRRRPNQSKLTSNRNEKDKLVILSGFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQVSKELENKNPPSRDLVDSYGTVRYNEKEKIFMDCFNRIYDMNASMLKTDEYNKNTLTIPSIDNTYINVKTNECNINQVDNNHNNYINDKDNTFNNSEKSDEWIYLQTRCPHPYTAVQICSYILKLKNKGDSVGGIATCIIQNPPIGIGEPIFDKLEAELAKMILSIPAVKGIEFGSGFNGTYMFGSMHNDIFIPVENMSTKKESDLLYDDKGECKNMSYHSTIQNNEDQILNSTKGFMPPKNDKNFNNIDDYNVTFNNNEEKLLITKTNNCGGILAGISTGNNIVFRSAIKPVSSIQIEKETSDFYGNMCNLKVQGRHDSCILPRLPPIIEASSSMVIGDLILRQISKYGDKKLPTLFRNM

[Multiple Choices]
A. Metabolic intermediate biosynthesis
B. Amino-acid degradation
C. protein glycosylation. .
D. chorismate biosynthesis
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis and specifically chorismate biosynthesis. Thus A is scientifically supported, although D is a more specific description of the same pathway. The pathway annotation is transferred by similarity, while the enzyme-name annotation has cited experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A sequence recognizable as belonging to the conserved chorismate-synthase family supports a role in chorismate production, a biosynthetic route for metabolic intermediates. That makes A and especially the more specific D more plausible than amino-acid degradation or protein glycosylation. This uses family-level sequence knowledge and pathway biology, not knowledge of this exact protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable recognition of chorismate-synthase homologs can meaningfully distinguish the biosynthetic choices from B and C. It does not uniquely select A over D because the two choices describe nested levels of the same pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Chorismate biosynthesis is a specific form of metabolic intermediate biosynthesis. The question does not specify whether to choose the broad pathway category or the most specific pathway offered, so both A and D are defensible.


### Important caveats

- The reviewer-only sequence-matched record supports the expected answer, but its pathway annotation is transferred by similarity rather than presented as direct experimental pathway evidence.
- The exact organism and target-specific annotations were not part of the original input and are not needed for the family-level inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A sequence recognizable as belonging to the conserved chorismate-synthase family supports a role in chorismate production, a biosynthetic route for metabolic intermediates. That makes A and especially the more specific D more plausible than amino-acid degradation or protein glycosylation. This uses family-level sequence knowledge and pathway biology, not knowledge of this exact protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of chorismate-synthase homologs can meaningfully distinguish the biosynthetic choices from B and C. It does not uniquely select A over D because the two choices describe nested levels of the same pathway."
  },
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis and specifically chorismate biosynthesis. Thus A is scientifically supported, although D is a more specific description of the same pathway. The pathway annotation is transferred by similarity, while the enzyme-name annotation has cited experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched record supports the expected answer, but its pathway annotation is transferred by similarity rather than presented as direct experimental pathway evidence.",
    "The exact organism and target-specific annotations were not part of the original input and are not needed for the family-level inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Chorismate biosynthesis is a specific form of metabolic intermediate biosynthesis. The question does not specify whether to choose the broad pathway category or the most specific pathway offered, so both A and D are defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis and specifically chorismate biosynthesis. Thus A is scientifically supported, although D is a more specific description of the same pathway. The pathway annotation is transferred by similarity, while the enzyme-name annotation has cited experimental evidence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A sequence recognizable as belonging to the conserved chorismate-synthase family supports a role in chorismate production, a biosynthetic route for metabolic intermediates. That makes A and especially the more specific D more plausible than amino-acid degradation or protein glycosylation. This uses family-level sequence knowledge and pathway biology, not knowledge of this exact protein's record.",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of chorismate-synthase homologs can meaningfully distinguish the biosynthetic choices from B and C. It does not uniquely select A over D because the two choices describe nested levels of the same pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Chorismate biosynthesis is a specific form of metabolic intermediate biosynthesis. The question does not specify whether to choose the broad pathway category or the most specific pathway offered, so both A and D are defensible."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched record supports the expected answer, but its pathway annotation is transferred by similarity rather than presented as direct experimental pathway evidence.",
    "The exact organism and target-specific annotations were not part of the original input and are not needed for the family-level inference."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt pathway annotation for C6KT66 (chorismate synthase from P. falciparum) reads: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' The phrase 'Metabolic intermediate biosynthesis' appears verbatim as the top-level pathway category, supporting choice A. However, 'chorismate biosynthesis' (choice D) also appears verbatim in the same annotation as the sub-pathway, so D is equally supported by the annotation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model recognizing the sequence as chorismate synthase (via the FMN-binding domain motifs, ~527 aa length, and characteristic sequence patterns shared with other chorismate synthases) would identify the enzyme's primary biochemical function as catalyzing the final step of chorismate biosynthesis (the shikimate pathway). This naturally maps to option D. Choosing A ('Metabolic intermediate biosynthesis') over D requires knowing that UniProt's hierarchical pathway annotation places 'chorismate biosynthesis' as a sub-pathway under the superpathway 'Metabolic intermediate biosynthesis,' and that the question intends the superpathway as the 'primary' pathway. This is an annotation-taxonomy convention, not a transferable biological inference.


**Missing item-specific fact**

> The specific UniProt pathway annotation hierarchy convention that designates 'Metabolic intermediate biosynthesis' as the top-level 'primary pathway' while treating 'chorismate biosynthesis' as a sub-pathway, and the benchmark's convention of selecting the top-level category as the correct answer rather than the more specific sub-pathway.


**Reason**

> Biological reasoning from the sequence (recognizing chorismate synthase via conserved FMN-binding motifs and family features) leads most naturally to 'chorismate biosynthesis' (D) as the primary pathway. Distinguishing A from D requires knowledge of UniProt's specific pathway annotation hierarchy and the benchmark's convention of selecting the superpathway. This is an annotation-convention fact specific to how UniProt structures pathway names, not a transferable biological principle.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both 'Metabolic intermediate biosynthesis' (A) and 'chorismate biosynthesis' (D) appear verbatim in the same UniProt pathway annotation string. The question asks for the 'primary metabolic or signaling pathway,' but the annotation is hierarchical ('Metabolic intermediate biosynthesis; chorismate biosynthesis; ...'), making it ambiguous whether 'primary' refers to the top-level superpathway (A) or the specific sub-pathway (D). From standard biochemical usage, D is the more natural and specific answer for chorismate synthase; A is the broader UniProt category.


### Important caveats

- Both A and D appear in the same UniProt annotation; the question's wording 'primary pathway' does not unambiguously select between the superpathway and sub-pathway levels.
- The sequence is recognizable as chorismate synthase from conserved FMN-binding domain motifs shared with homologs in other organisms, making family-level identification feasible.
- The author's choice of A follows UniProt's top-level pathway category convention, but this is an annotation taxonomy choice rather than a biological fact that would override the more specific pathway name D.
- The pathway annotation evidence code is ECO:0000250 (similarity to Q12640, a bacterial chorismate synthase), indicating the pathway assignment is by similarity rather than direct experimental pathway tracing in P. falciparum.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model recognizing the sequence as chorismate synthase (via the FMN-binding domain motifs, ~527 aa length, and characteristic sequence patterns shared with other chorismate synthases) would identify the enzyme's primary biochemical function as catalyzing the final step of chorismate biosynthesis (the shikimate pathway). This naturally maps to option D. Choosing A ('Metabolic intermediate biosynthesis') over D requires knowing that UniProt's hierarchical pathway annotation places 'chorismate biosynthesis' as a sub-pathway under the superpathway 'Metabolic intermediate biosynthesis,' and that the question intends the superpathway as the 'primary' pathway. This is an annotation-taxonomy convention, not a transferable biological inference.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt pathway annotation hierarchy convention that designates 'Metabolic intermediate biosynthesis' as the top-level 'primary pathway' while treating 'chorismate biosynthesis' as a sub-pathway, and the benchmark's convention of selecting the top-level category as the correct answer rather than the more specific sub-pathway.",
    "reason": "Biological reasoning from the sequence (recognizing chorismate synthase via conserved FMN-binding motifs and family features) leads most naturally to 'chorismate biosynthesis' (D) as the primary pathway. Distinguishing A from D requires knowledge of UniProt's specific pathway annotation hierarchy and the benchmark's convention of selecting the superpathway. This is an annotation-convention fact specific to how UniProt structures pathway names, not a transferable biological principle."
  },
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for C6KT66 (chorismate synthase from P. falciparum) reads: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' The phrase 'Metabolic intermediate biosynthesis' appears verbatim as the top-level pathway category, supporting choice A. However, 'chorismate biosynthesis' (choice D) also appears verbatim in the same annotation as the sub-pathway, so D is equally supported by the annotation."
  },
  "important_caveats": [
    "Both A and D appear in the same UniProt annotation; the question's wording 'primary pathway' does not unambiguously select between the superpathway and sub-pathway levels.",
    "The sequence is recognizable as chorismate synthase from conserved FMN-binding domain motifs shared with homologs in other organisms, making family-level identification feasible.",
    "The author's choice of A follows UniProt's top-level pathway category convention, but this is an annotation taxonomy choice rather than a biological fact that would override the more specific pathway name D.",
    "The pathway annotation evidence code is ECO:0000250 (similarity to Q12640, a bacterial chorismate synthase), indicating the pathway assignment is by similarity rather than direct experimental pathway tracing in P. falciparum."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both 'Metabolic intermediate biosynthesis' (A) and 'chorismate biosynthesis' (D) appear verbatim in the same UniProt pathway annotation string. The question asks for the 'primary metabolic or signaling pathway,' but the annotation is hierarchical ('Metabolic intermediate biosynthesis; chorismate biosynthesis; ...'), making it ambiguous whether 'primary' refers to the top-level superpathway (A) or the specific sub-pathway (D). From standard biochemical usage, D is the more natural and specific answer for chorismate synthase; A is the broader UniProt category."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for C6KT66 (chorismate synthase from P. falciparum) reads: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' The phrase 'Metabolic intermediate biosynthesis' appears verbatim as the top-level pathway category, supporting choice A. However, 'chorismate biosynthesis' (choice D) also appears verbatim in the same annotation as the sub-pathway, so D is equally supported by the annotation.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model recognizing the sequence as chorismate synthase (via the FMN-binding domain motifs, ~527 aa length, and characteristic sequence patterns shared with other chorismate synthases) would identify the enzyme's primary biochemical function as catalyzing the final step of chorismate biosynthesis (the shikimate pathway). This naturally maps to option D. Choosing A ('Metabolic intermediate biosynthesis') over D requires knowing that UniProt's hierarchical pathway annotation places 'chorismate biosynthesis' as a sub-pathway under the superpathway 'Metabolic intermediate biosynthesis,' and that the question intends the superpathway as the 'primary' pathway. This is an annotation-taxonomy convention, not a transferable biological inference.",
    "missing_item_specific_fact": "The specific UniProt pathway annotation hierarchy convention that designates 'Metabolic intermediate biosynthesis' as the top-level 'primary pathway' while treating 'chorismate biosynthesis' as a sub-pathway, and the benchmark's convention of selecting the top-level category as the correct answer rather than the more specific sub-pathway.",
    "reason": "Biological reasoning from the sequence (recognizing chorismate synthase via conserved FMN-binding motifs and family features) leads most naturally to 'chorismate biosynthesis' (D) as the primary pathway. Distinguishing A from D requires knowledge of UniProt's specific pathway annotation hierarchy and the benchmark's convention of selecting the superpathway. This is an annotation-convention fact specific to how UniProt structures pathway names, not a transferable biological principle."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both 'Metabolic intermediate biosynthesis' (A) and 'chorismate biosynthesis' (D) appear verbatim in the same UniProt pathway annotation string. The question asks for the 'primary metabolic or signaling pathway,' but the annotation is hierarchical ('Metabolic intermediate biosynthesis; chorismate biosynthesis; ...'), making it ambiguous whether 'primary' refers to the top-level superpathway (A) or the specific sub-pathway (D). From standard biochemical usage, D is the more natural and specific answer for chorismate synthase; A is the broader UniProt category."
  },
  "important_caveats": [
    "Both A and D appear in the same UniProt annotation; the question's wording 'primary pathway' does not unambiguously select between the superpathway and sub-pathway levels.",
    "The sequence is recognizable as chorismate synthase from conserved FMN-binding domain motifs shared with homologs in other organisms, making family-level identification feasible.",
    "The author's choice of A follows UniProt's top-level pathway category convention, but this is an annotation taxonomy choice rather than a biological fact that would override the more specific pathway name D.",
    "The pathway annotation evidence code is ECO:0000250 (similarity to Q12640, a bacterial chorismate synthase), indicating the pathway assignment is by similarity rather than direct experimental pathway tracing in P. falciparum."
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
  "benchmark_sequence_length": 527,
  "benchmark_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "current_entry_audit": {
    "entryVersion": 91,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 527,
  "current_source_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 89,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C6KT66",
  "selected_historical_entry_version": 89,
  "selected_historical_record_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "selected_historical_source_sequence_length": 527,
  "selected_historical_source_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "selected_historical_version": {
    "accession": "C6KT66",
    "database": "Swiss-Prot",
    "entryVersion": 89,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AROC_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C6KT66\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":91,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.38\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"Chorismate synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"value\":\"PfCS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q12640\",\"source\":\"UniProtKB\"}],\"value\":\"Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Fitzpatrick T.\",\"Ricken S.\",\"Lanzer M.\",\"Amrhein N.\",\"Macheroux P.\",\"Kappes B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11298276\"},{\"database\":\"DOI\",\"id\":\"10.1046/j.1365-2958.2001.02366.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"65\",\"id\":\"11298276\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"75\",\"publicationDate\":\"2001\",\"title\":\"Subcellular localization and characterization of chorismate synthase in the apicomplexan Plasmodium falciparum.\",\"volume\":\"40\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"DD2\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Khera H.K.\",\"Singh S.K.\",\"Singh S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31381947\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2019.111202\"}],\"citationType\":\"journal article\",\"firstPage\":\"111202\",\"id\":\"31381947\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"111202\",\"publicationDate\":\"2019\",\"title\":\"Chorismate synthase from malaria parasites is bifunctional enzyme.\",\"volume\":\"233\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H1",
  "excerpt": "ID   AROC_PLAF7              Reviewed;         527 AA.\nAC   C6KT66;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 89.\nDE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:11298276, ECO:0000303|PubMed:31381947};\nDE            Short=PfCS {ECO:0000303|PubMed:11298276};\nDE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};\nDE            EC=4.2.3.5 {ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};\nGN   Name=CS {ECO:0000305}; Synonyms=AROC {ECO:0000303|PubMed:11298276};\nGN   ORFNames=PF3D7_0623000 {ECO:0000312|EMBL:CAG25042.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, AND DEVELOPMENTAL\nRP   STAGE.\nRC   STRAIN=DD2 {ECO:0000303|PubMed:11298276};\nRX   PubMed=11298276; DOI=10.1046/j.1365-2958.2001.02366.x;\nRA   Fitzpatrick T., Ricken S., Lanzer M., Amrhein N., Macheroux P., Kappes B.;\nRT   \"Subcellular localization and characterization of chorismate synthase in\nRT   the apicomplexan Plasmodium falciparum.\";\nRL   Mol. Microbiol. 40:65-75(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=31381947; DOI=10.1016/j.molbiopara.2019.111202;\nRA   Khera H.K., Singh S.K., Singh S.;\nRT   \"Chorismate synthase from malaria parasites is bifunctional enzyme.\";\nRL   Mol. Biochem. Parasitol. 233:111202-111202(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Metabolic intermediate biosynthesis; chorismate biosynthesis;\nCC       chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step\nCC       7/7. {ECO:0000250|UniProtKB:Q12640}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
