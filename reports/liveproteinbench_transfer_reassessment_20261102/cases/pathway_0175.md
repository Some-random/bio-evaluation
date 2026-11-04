# pathway_0175

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0175.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Cofactor biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSKIFGIVNITTDSFSDGGLYLDTDKAIEHALHLVEDGADVIDLGAASSNPDTTEVGVVEEIKRLKPVIKALKEKGISISVDTFKPEVQSFCIEQKVDFINDIQGFPYPEIYSGLAKSDCKLVLMHSVQRIGAATKVETNPEEVFTSMMEFFKERIAALVEAGVKRERIILDPGMGFFLGSNPETSILVLKRFPEIQEAFNLQVMIAVSRKSFLGKITGTDVKSRLAPTLAAEMYAYKKGADYLRTHDVKSLSDALKISKALG

[Multiple Choices]
A. Cofactor biosynthesis
B. molybdopterin biosynthesis. .
C. L-homoserine from L-aspartate: step 2/3. .
D. NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1. .
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

> The sequence-matched record annotates the protein as dihydropteroate synthase and places it in cofactor and tetrahydrofolate biosynthesis, supporting A. The pathway annotation cites both RuleBase and a publication; this supports the key but does not, by itself, establish that every part of the annotation was experimentally demonstrated.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A credible family-level sequence match to bacterial dihydropteroate synthase would distinguish A: this enzyme catalyzes a step in folate (tetrahydrofolate) biosynthesis, categorized here under cofactor biosynthesis. That is distinct from molybdopterin biosynthesis, homoserine synthesis, and the specified NAD pathway.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered alternatives are separated by pathway, and transferable knowledge of the DHPS family and its conserved function provides a meaningful basis for choosing A without requiring the exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The broader cofactor-biosynthesis choice fits the DHPS/folate pathway; the other listed pathways describe different biosynthetic processes.


### Important caveats

- The pathway evidence is database annotation with RuleBase and publication attribution; it should not be represented as exclusively direct experimental pathway evidence.
- Reviewer-only annotations support the key but are not original input to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A credible family-level sequence match to bacterial dihydropteroate synthase would distinguish A: this enzyme catalyzes a step in folate (tetrahydrofolate) biosynthesis, categorized here under cofactor biosynthesis. That is distinct from molybdopterin biosynthesis, homoserine synthesis, and the specified NAD pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered alternatives are separated by pathway, and transferable knowledge of the DHPS family and its conserved function provides a meaningful basis for choosing A without requiring the exact protein's database entry."
  },
  "case_id": "pathway_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates the protein as dihydropteroate synthase and places it in cofactor and tetrahydrofolate biosynthesis, supporting A. The pathway annotation cites both RuleBase and a publication; this supports the key but does not, by itself, establish that every part of the annotation was experimentally demonstrated."
  },
  "important_caveats": [
    "The pathway evidence is database annotation with RuleBase and publication attribution; it should not be represented as exclusively direct experimental pathway evidence.",
    "Reviewer-only annotations support the key but are not original input to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broader cofactor-biosynthesis choice fits the DHPS/folate pathway; the other listed pathways describe different biosynthetic processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates the protein as dihydropteroate synthase and places it in cofactor and tetrahydrofolate biosynthesis, supporting A. The pathway annotation cites both RuleBase and a publication; this supports the key but does not, by itself, establish that every part of the annotation was experimentally demonstrated.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A credible family-level sequence match to bacterial dihydropteroate synthase would distinguish A: this enzyme catalyzes a step in folate (tetrahydrofolate) biosynthesis, categorized here under cofactor biosynthesis. That is distinct from molybdopterin biosynthesis, homoserine synthesis, and the specified NAD pathway.",
    "missing_item_specific_fact": "",
    "reason": "The offered alternatives are separated by pathway, and transferable knowledge of the DHPS family and its conserved function provides a meaningful basis for choosing A without requiring the exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broader cofactor-biosynthesis choice fits the DHPS/folate pathway; the other listed pathways describe different biosynthetic processes."
  },
  "important_caveats": [
    "The pathway evidence is database annotation with RuleBase and publication attribution; it should not be represented as exclusively direct experimental pathway evidence.",
    "Reviewer-only annotations support the key but are not original input to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C0HMD9 (Dihydropteroate synthase type-3, sul3, EC 2.5.1.15) carries the pathway annotation 'Cofactor biosynthesis; tetrahydrofolate biosynthesis; 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2' (evidence codes ECO:0000255 RuleBase and ECO:0000303 PubMed:37419898). The top-level pathway category is 'Cofactor biosynthesis', matching option A. The 2023 Nature Communications paper (PDB 7S2L, 7S2M, 8SCD) provides experimental X-ray crystallographic confirmation of function and catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is ~263 amino acids long, which immediately disfavors option C (L-homoserine dehydrogenase in the aspartate→homoserine pathway is typically ~450 aa with an ACT regulatory domain and Rossmann fold) and option D (NAD synthetase NadE is ~300+ aa with a glutamine amidotransferase domain). The sequence exhibits a TIM-barrel-like β/α architecture (alternating hydrophobic β-strand and α-helix motifs visible in the central region), which is the hallmark fold of dihydropteroate synthase (DHPS, EC 2.5.1.15). Molybdopterin biosynthesis (option B) involves enzymes of different sizes and folds (MoaA ~300 aa radical SAM, MoaD ~75 aa ubiquitin-like, MoaE ~300 aa, MogA/B ~200 aa), none matching a ~263 aa TIM barrel. Among the four choices, a ~263 aa TIM-barrel enzyme is most naturally assigned to folate (tetrahydrofolate) biosynthesis, which UniProt classifies under 'Cofactor biosynthesis' (option A). Additionally, the sul family of sulfonamide resistance genes (sul1, sul2, sul3) are well-known plasmid-encoded DHPS variants; recognizing the sul3-like architecture connects the sequence to the folate pathway via established antibiotic-resistance biology learned from other proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use protein length (~263 aa) to eliminate the much larger homoserine dehydrogenase (~450 aa) and NAD synthetase (~300+ aa) options, recognize the TIM-barrel fold pattern consistent with DHPS, and leverage family-level knowledge of the sul (sulfonamide resistance) gene family encoding DHPS-type enzymes in folate biosynthesis. This constitutes legitimate transfer from other proteins (folP, sul1, sul2, and general enzyme-size/fold knowledge) rather than a lookup of C0HMD9's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct pathways with different enzyme sizes and folds. The ~263 aa TIM-barrel architecture is a strong discriminator for folate/cofactor biosynthesis over the other three choices. No other option plausibly accommodates a ~263 aa TIM-barrel enzyme.


### Important caveats

- The sul3 protein (type III DHPS) is significantly divergent from canonical chromosomal folP (type I DHPS); sequence identity to folP is low, so fold recognition relies on overall architecture rather than high sequence similarity.
- The UniProt pathway annotation uses a RuleBase (ECO:0000255) computational inference cross-referenced with experimental data from the 2023 Nat. Commun. paper (ECO:0000303, PDB structures 7S2L/7S2M/8SCD), so the functional assignment has experimental backing.
- Option A ('Cofactor biosynthesis') is the top-level UniProt pathway category; the more specific sub-pathway is 'tetrahydrofolate biosynthesis.' The question asks for the 'primary pathway,' and the top-level category is a valid and commonly used answer format.
- The reviewer-only evidence identifies the protein as C0HMD9 from plasmid pVP440 in E. coli; this accession and organism identity were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is ~263 amino acids long, which immediately disfavors option C (L-homoserine dehydrogenase in the aspartate→homoserine pathway is typically ~450 aa with an ACT regulatory domain and Rossmann fold) and option D (NAD synthetase NadE is ~300+ aa with a glutamine amidotransferase domain). The sequence exhibits a TIM-barrel-like β/α architecture (alternating hydrophobic β-strand and α-helix motifs visible in the central region), which is the hallmark fold of dihydropteroate synthase (DHPS, EC 2.5.1.15). Molybdopterin biosynthesis (option B) involves enzymes of different sizes and folds (MoaA ~300 aa radical SAM, MoaD ~75 aa ubiquitin-like, MoaE ~300 aa, MogA/B ~200 aa), none matching a ~263 aa TIM barrel. Among the four choices, a ~263 aa TIM-barrel enzyme is most naturally assigned to folate (tetrahydrofolate) biosynthesis, which UniProt classifies under 'Cofactor biosynthesis' (option A). Additionally, the sul family of sulfonamide resistance genes (sul1, sul2, sul3) are well-known plasmid-encoded DHPS variants; recognizing the sul3-like architecture connects the sequence to the folate pathway via established antibiotic-resistance biology learned from other proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use protein length (~263 aa) to eliminate the much larger homoserine dehydrogenase (~450 aa) and NAD synthetase (~300+ aa) options, recognize the TIM-barrel fold pattern consistent with DHPS, and leverage family-level knowledge of the sul (sulfonamide resistance) gene family encoding DHPS-type enzymes in folate biosynthesis. This constitutes legitimate transfer from other proteins (folP, sul1, sul2, and general enzyme-size/fold knowledge) rather than a lookup of C0HMD9's specific annotation."
  },
  "case_id": "pathway_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C0HMD9 (Dihydropteroate synthase type-3, sul3, EC 2.5.1.15) carries the pathway annotation 'Cofactor biosynthesis; tetrahydrofolate biosynthesis; 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2' (evidence codes ECO:0000255 RuleBase and ECO:0000303 PubMed:37419898). The top-level pathway category is 'Cofactor biosynthesis', matching option A. The 2023 Nature Communications paper (PDB 7S2L, 7S2M, 8SCD) provides experimental X-ray crystallographic confirmation of function and catalytic activity."
  },
  "important_caveats": [
    "The sul3 protein (type III DHPS) is significantly divergent from canonical chromosomal folP (type I DHPS); sequence identity to folP is low, so fold recognition relies on overall architecture rather than high sequence similarity.",
    "The UniProt pathway annotation uses a RuleBase (ECO:0000255) computational inference cross-referenced with experimental data from the 2023 Nat. Commun. paper (ECO:0000303, PDB structures 7S2L/7S2M/8SCD), so the functional assignment has experimental backing.",
    "Option A ('Cofactor biosynthesis') is the top-level UniProt pathway category; the more specific sub-pathway is 'tetrahydrofolate biosynthesis.' The question asks for the 'primary pathway,' and the top-level category is a valid and commonly used answer format.",
    "The reviewer-only evidence identifies the protein as C0HMD9 from plasmid pVP440 in E. coli; this accession and organism identity were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct pathways with different enzyme sizes and folds. The ~263 aa TIM-barrel architecture is a strong discriminator for folate/cofactor biosynthesis over the other three choices. No other option plausibly accommodates a ~263 aa TIM-barrel enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C0HMD9 (Dihydropteroate synthase type-3, sul3, EC 2.5.1.15) carries the pathway annotation 'Cofactor biosynthesis; tetrahydrofolate biosynthesis; 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2' (evidence codes ECO:0000255 RuleBase and ECO:0000303 PubMed:37419898). The top-level pathway category is 'Cofactor biosynthesis', matching option A. The 2023 Nature Communications paper (PDB 7S2L, 7S2M, 8SCD) provides experimental X-ray crystallographic confirmation of function and catalytic activity.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is ~263 amino acids long, which immediately disfavors option C (L-homoserine dehydrogenase in the aspartate→homoserine pathway is typically ~450 aa with an ACT regulatory domain and Rossmann fold) and option D (NAD synthetase NadE is ~300+ aa with a glutamine amidotransferase domain). The sequence exhibits a TIM-barrel-like β/α architecture (alternating hydrophobic β-strand and α-helix motifs visible in the central region), which is the hallmark fold of dihydropteroate synthase (DHPS, EC 2.5.1.15). Molybdopterin biosynthesis (option B) involves enzymes of different sizes and folds (MoaA ~300 aa radical SAM, MoaD ~75 aa ubiquitin-like, MoaE ~300 aa, MogA/B ~200 aa), none matching a ~263 aa TIM barrel. Among the four choices, a ~263 aa TIM-barrel enzyme is most naturally assigned to folate (tetrahydrofolate) biosynthesis, which UniProt classifies under 'Cofactor biosynthesis' (option A). Additionally, the sul family of sulfonamide resistance genes (sul1, sul2, sul3) are well-known plasmid-encoded DHPS variants; recognizing the sul3-like architecture connects the sequence to the folate pathway via established antibiotic-resistance biology learned from other proteins.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use protein length (~263 aa) to eliminate the much larger homoserine dehydrogenase (~450 aa) and NAD synthetase (~300+ aa) options, recognize the TIM-barrel fold pattern consistent with DHPS, and leverage family-level knowledge of the sul (sulfonamide resistance) gene family encoding DHPS-type enzymes in folate biosynthesis. This constitutes legitimate transfer from other proteins (folP, sul1, sul2, and general enzyme-size/fold knowledge) rather than a lookup of C0HMD9's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct pathways with different enzyme sizes and folds. The ~263 aa TIM-barrel architecture is a strong discriminator for folate/cofactor biosynthesis over the other three choices. No other option plausibly accommodates a ~263 aa TIM-barrel enzyme."
  },
  "important_caveats": [
    "The sul3 protein (type III DHPS) is significantly divergent from canonical chromosomal folP (type I DHPS); sequence identity to folP is low, so fold recognition relies on overall architecture rather than high sequence similarity.",
    "The UniProt pathway annotation uses a RuleBase (ECO:0000255) computational inference cross-referenced with experimental data from the 2023 Nat. Commun. paper (ECO:0000303, PDB structures 7S2L/7S2M/8SCD), so the functional assignment has experimental backing.",
    "Option A ('Cofactor biosynthesis') is the top-level UniProt pathway category; the more specific sub-pathway is 'tetrahydrofolate biosynthesis.' The question asks for the 'primary pathway,' and the top-level category is a valid and commonly used answer format.",
    "The reviewer-only evidence identifies the protein as C0HMD9 from plasmid pVP440 in E. coli; this accession and organism identity were not provided to the evaluated model."
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
  "benchmark_sequence_length": 263,
  "benchmark_sequence_sha256": "9c1e668c6f38602c788bb8303e6683a5269f3afe52684cb7a7d4ed2d2985b67a",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 263,
  "current_source_sequence_sha256": "9c1e668c6f38602c788bb8303e6683a5269f3afe52684cb7a7d4ed2d2985b67a",
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
  "requested_accession": "C0HMD9",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "selected_historical_source_sequence_length": 263,
  "selected_historical_source_sequence_sha256": "9c1e668c6f38602c788bb8303e6683a5269f3afe52684cb7a7d4ed2d2985b67a",
  "selected_historical_version": {
    "accession": "C0HMD9",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHP3_ECOLX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C0HMD9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAD30683.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Escherichia\"],\"scientificName\":\"Escherichia coli\",\"taxonId\":562}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C002\",\"source\":\"UniProtKB\"}],\"value\":\"Dihydropteroate pyrophosphorylase type III\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C002\",\"source\":\"UniProtKB\"}],\"value\":\"Dihydropteroate synthase type III\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.15\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"value\":\"Dihydropteroate synthase type-3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"value\":\"DHPS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"value\":\"Cofactor biosynthesis; tetrahydrofolate biosynthesis; 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Venkatesan M.\",\"Fruci M.\",\"Verellen L.A.\",\"Skarina T.\",\"Mesa N.\",\"Flick R.\",\"Pham C.\",\"Mahadevan R.\",\"Stogios P.J.\",\"Savchenko A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37419898\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-023-39778-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"4031\",\"id\":\"37419898\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"4031\",\"publicationDate\":\"2023\",\"title\":\"Molecular mechanism of plasmid-borne resistance to sulfonamide antibiotics.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7S2L\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7S2M\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8SCD\",\"source\":\"PDB\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.06 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH MG(2+) AND WITH SUBSTRATES\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF PHE-177 AND LEU-179\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   DHP3_ECOLX              Reviewed;         263 AA.\nAC   C0HMD9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Dihydropteroate synthase type-3 {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};\nDE            Short=DHPS {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};\nDE            EC=2.5.1.15 {ECO:0000255|RuleBase:RU361205, ECO:0000269|PubMed:37419898};\nDE   AltName: Full=Dihydropteroate pyrophosphorylase type III {ECO:0000250|UniProtKB:P0C002};\nDE   AltName: Full=Dihydropteroate synthase type III {ECO:0000250|UniProtKB:P0C002};\nGN   Name=sul3 {ECO:0000303|PubMed:12604565, ECO:0000312|EMBL:CAD30683.1};\nOS   Escherichia coli.\nOG   Plasmid pVP440 {ECO:0000312|EMBL:CAD30683.1}.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Escherichia.\nOX   NCBI_TaxID=562 {ECO:0000312|EMBL:CAD30683.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAD30683.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], AND FUNCTION.\nRC   STRAIN=Rl0044 {ECO:0000312|EMBL:CAD30683.1};\nRC   PLASMID=pVP440 {ECO:0000312|EMBL:CAD30683.1};\nRX   PubMed=12604565; DOI=10.1128/aac.47.3.1169-1172.2003;\nRA   Perreten V., Boerlin P.;\nRT   \"A new sulfonamide resistance gene (sul3) in Escherichia coli is widespread\nRT   in the pig population of Switzerland.\";\nRL   Antimicrob. Agents Chemother. 47:1169-1172(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7S2L, ECO:0007744|PDB:7S2M, ECO:0007744|PDB:8SCD}\nRP   X-RAY CRYSTALLOGRAPHY (2.06 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH\nRP   MG(2+) AND WITH SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND MUTAGENESIS OF PHE-177 AND LEU-179.\nRX   PubMed=37419898; DOI=10.1038/s41467-023-39778-7;\nRA   Venkatesan M., Fruci M., Verellen L.A., Skarina T., Mesa N., Flick R.,\nRA   Pham C., Mahadevan R., Stogios P.J., Savchenko A.;\nRT   \"Molecular mechanism of plasmid-borne resistance to sulfonamide\nRT   antibiotics.\";\nRL   Nat. Commun. 14:4031-4031(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Cofactor biosynthesis; tetrahydrofolate biosynthesis; 7,8-\nCC       dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-\nCC       dihydropteridine diphosphate and 4-aminobenzoate: step 1/2.\nCC       {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 175. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
