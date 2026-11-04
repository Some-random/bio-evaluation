# pathway_0055

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0055.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Metabolic intermediate biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSFGESHGKAIGCVIDGFLPNVEINFDLIQRQLNRRRPNQSKLTSNRNEPDKLIVLSGFDENKTLGTPITFLINNEDVIKKNYSSFIDIPRPGHGDYTYFKKYNVKNKSGSSRFSGRETATRVAAGACIEQWLHTFYNCTIVCYVHSVGNIKLPEQVSKDFERNPPSRDLVDAHGAVKYHQGRGTFTDFFGNVYNANGEFLRGGEAAPEGATPADGTPTDGNPTDDPLANARERLSDPGECTLLQTRCPHPLTAVKICSYILKLKKAGDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGEVTPGGSRAQEGTSFEKDACHRSGHLSNLSGYPSNGSGNPPNGSDHPSNRSGNPPNRSDPRVDESTRETSPPSGEKLLVTTSNNCGGILAGITTGNNIVFRSAIKPVSSIQIEKETCNFFGEKCKLKVTGMHDCCILPRLPPIIEASTSIVIGDMILRQVAKYGHSKLPSVGSLSRSTRE

[Multiple Choices]
A. 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2. .
B. One-carbon metabolism
C. Antifungal biosynthesis. .
D. Metabolic intermediate biosynthesis
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

> The sequence-matched UniProt record identifies the protein as chorismate synthase and annotates its pathway as metabolic intermediate biosynthesis, specifically chorismate biosynthesis (step 7/7). The pathway annotation is transferred by similarity, while the record also cites a publication for the enzyme characterization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model could recognize the sequence as belonging to the chorismate synthase family from its conserved enzyme-family features. Chorismate synthase catalyzes the final step of chorismate biosynthesis, producing a metabolic intermediate; this makes D a better fit than folate synthesis, one-carbon metabolism, or antifungal biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-to-pathway connection is transferable biological knowledge and meaningfully distinguishes the broad pathway choice D. The exact protein's database annotation is not necessary for that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives point to distinct pathway categories, and chorismate biosynthesis fits D rather than the specific folate, one-carbon, or antifungal options.


### Important caveats

- The supplied sequence does not state the protein name or organism; family recognition from sequence is the transferable inference.
- The cited pathway annotation is similarity-transferred, not itself direct experimental evidence for the pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as belonging to the chorismate synthase family from its conserved enzyme-family features. Chorismate synthase catalyzes the final step of chorismate biosynthesis, producing a metabolic intermediate; this makes D a better fit than folate synthesis, one-carbon metabolism, or antifungal biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-to-pathway connection is transferable biological knowledge and meaningfully distinguishes the broad pathway choice D. The exact protein's database annotation is not necessary for that inference."
  },
  "case_id": "pathway_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as chorismate synthase and annotates its pathway as metabolic intermediate biosynthesis, specifically chorismate biosynthesis (step 7/7). The pathway annotation is transferred by similarity, while the record also cites a publication for the enzyme characterization."
  },
  "important_caveats": [
    "The supplied sequence does not state the protein name or organism; family recognition from sequence is the transferable inference.",
    "The cited pathway annotation is similarity-transferred, not itself direct experimental evidence for the pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives point to distinct pathway categories, and chorismate biosynthesis fits D rather than the specific folate, one-carbon, or antifungal options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as chorismate synthase and annotates its pathway as metabolic intermediate biosynthesis, specifically chorismate biosynthesis (step 7/7). The pathway annotation is transferred by similarity, while the record also cites a publication for the enzyme characterization.",
    "evidence_ids": ["C4", "C5", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as belonging to the chorismate synthase family from its conserved enzyme-family features. Chorismate synthase catalyzes the final step of chorismate biosynthesis, producing a metabolic intermediate; this makes D a better fit than folate synthesis, one-carbon metabolism, or antifungal biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "The family-to-pathway connection is transferable biological knowledge and meaningfully distinguishes the broad pathway choice D. The exact protein's database annotation is not necessary for that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives point to distinct pathway categories, and chorismate biosynthesis fits D rather than the specific folate, one-carbon, or antifungal options."
  },
  "important_caveats": [
    "The supplied sequence does not state the protein name or organism; family recognition from sequence is the transferable inference.",
    "The cited pathway annotation is similarity-transferred, not itself direct experimental evidence for the pathway."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (A5K264, Plasmodium vivax chorismate synthase) explicitly assigns the pathway as 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7' (evidence C5, H3). The expected answer 'Metabolic intermediate biosynthesis' is the top-level UniProt pathway category for chorismate biosynthesis. The enzyme identity (chorismate synthase, EC 4.2.3.5) is supported by experimental evidence (PubMed:31381947, evidence code ECO:0000269). The pathway assignment itself uses similarity evidence (ECO:0000250 to Q12640), but the logical connection between chorismate synthase function and the 'Metabolic intermediate biosynthesis' pathway category is sound.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains highly conserved chorismate synthase motifs, most notably 'GFDENK' in the region 'SGFDENKTLGTPITFLINNED' and 'GSGFDGTYMLGSDHNDLFGTLD', which are signature FMN-binding motifs of the chorismate synthase family. A knowledgeable model recognizing these motifs would identify the enzyme as chorismate synthase, which catalyzes the final step of the shikimate pathway (conversion of 5-enolpyruvylshikimate-3-phosphate to chorismate). Chorismate is universally classified as a metabolic intermediate (it is the branch-point precursor for aromatic amino acids, folates, ubiquinone, and other compounds), and its biosynthesis falls under the UniProt 'Metabolic intermediate biosynthesis' pathway category. Option A describes dihydropteroate synthase (DHPS), a completely different enzyme with distinct sequence motifs. Option B (one-carbon metabolism) is unrelated to the shikimate pathway. Option C ('Antifungal biosynthesis') is not a recognized metabolic pathway. The transferable knowledge that chorismate is a metabolic intermediate and that the shikimate/chorismate biosynthesis pathway is classified under this heading in pathway databases (learned from E. coli, Bacillus, and other chorismate synthases) allows meaningful discrimination among the four choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence contains recognizable chorismate synthase family motifs (GFDENK, conserved architecture). Identifying the enzyme as chorismate synthase via these motifs, combined with the general knowledge that chorismate is a metabolic intermediate and its biosynthesis is classified under 'Metabolic intermediate biosynthesis' in pathway taxonomy (a pattern learned from other organisms' chorismate synthases), provides a concrete and credible inference to select D over A (different enzyme, DHPS), B (different metabolic process), and C (nonsensical pathway name).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the enzyme is identified as chorismate synthase via conserved motifs, only D correctly describes its pathway. A refers to DHPS (a different enzyme with different motifs), B refers to one-carbon/folate metabolism (not the shikimate pathway), and C is not a recognized pathway. No ambiguity among the offered choices.


### Important caveats

- The pathway annotation uses similarity evidence (ECO:0000250) rather than direct experimental pathway determination for this specific protein, but the enzyme's catalytic function is experimentally confirmed.
- The bifunctional nature of Plasmodium chorismate synthase (also having EC 1.5.1.38, dihydroneopterin aldolase activity) could theoretically create confusion with folate-related pathways, but the primary pathway annotation remains chorismate biosynthesis.
- The option text for A contains a trailing period and slightly unusual formatting, but its content clearly describes DHPS and is distinguishable from chorismate synthase.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains highly conserved chorismate synthase motifs, most notably 'GFDENK' in the region 'SGFDENKTLGTPITFLINNED' and 'GSGFDGTYMLGSDHNDLFGTLD', which are signature FMN-binding motifs of the chorismate synthase family. A knowledgeable model recognizing these motifs would identify the enzyme as chorismate synthase, which catalyzes the final step of the shikimate pathway (conversion of 5-enolpyruvylshikimate-3-phosphate to chorismate). Chorismate is universally classified as a metabolic intermediate (it is the branch-point precursor for aromatic amino acids, folates, ubiquinone, and other compounds), and its biosynthesis falls under the UniProt 'Metabolic intermediate biosynthesis' pathway category. Option A describes dihydropteroate synthase (DHPS), a completely different enzyme with distinct sequence motifs. Option B (one-carbon metabolism) is unrelated to the shikimate pathway. Option C ('Antifungal biosynthesis') is not a recognized metabolic pathway. The transferable knowledge that chorismate is a metabolic intermediate and that the shikimate/chorismate biosynthesis pathway is classified under this heading in pathway databases (learned from E. coli, Bacillus, and other chorismate synthases) allows meaningful discrimination among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains recognizable chorismate synthase family motifs (GFDENK, conserved architecture). Identifying the enzyme as chorismate synthase via these motifs, combined with the general knowledge that chorismate is a metabolic intermediate and its biosynthesis is classified under 'Metabolic intermediate biosynthesis' in pathway taxonomy (a pattern learned from other organisms' chorismate synthases), provides a concrete and credible inference to select D over A (different enzyme, DHPS), B (different metabolic process), and C (nonsensical pathway name)."
  },
  "case_id": "pathway_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A5K264, Plasmodium vivax chorismate synthase) explicitly assigns the pathway as 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7' (evidence C5, H3). The expected answer 'Metabolic intermediate biosynthesis' is the top-level UniProt pathway category for chorismate biosynthesis. The enzyme identity (chorismate synthase, EC 4.2.3.5) is supported by experimental evidence (PubMed:31381947, evidence code ECO:0000269). The pathway assignment itself uses similarity evidence (ECO:0000250 to Q12640), but the logical connection between chorismate synthase function and the 'Metabolic intermediate biosynthesis' pathway category is sound."
  },
  "important_caveats": [
    "The pathway annotation uses similarity evidence (ECO:0000250) rather than direct experimental pathway determination for this specific protein, but the enzyme's catalytic function is experimentally confirmed.",
    "The bifunctional nature of Plasmodium chorismate synthase (also having EC 1.5.1.38, dihydroneopterin aldolase activity) could theoretically create confusion with folate-related pathways, but the primary pathway annotation remains chorismate biosynthesis.",
    "The option text for A contains a trailing period and slightly unusual formatting, but its content clearly describes DHPS and is distinguishable from chorismate synthase."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the enzyme is identified as chorismate synthase via conserved motifs, only D correctly describes its pathway. A refers to DHPS (a different enzyme with different motifs), B refers to one-carbon/folate metabolism (not the shikimate pathway), and C is not a recognized pathway. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A5K264, Plasmodium vivax chorismate synthase) explicitly assigns the pathway as 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7' (evidence C5, H3). The expected answer 'Metabolic intermediate biosynthesis' is the top-level UniProt pathway category for chorismate biosynthesis. The enzyme identity (chorismate synthase, EC 4.2.3.5) is supported by experimental evidence (PubMed:31381947, evidence code ECO:0000269). The pathway assignment itself uses similarity evidence (ECO:0000250 to Q12640), but the logical connection between chorismate synthase function and the 'Metabolic intermediate biosynthesis' pathway category is sound.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains highly conserved chorismate synthase motifs, most notably 'GFDENK' in the region 'SGFDENKTLGTPITFLINNED' and 'GSGFDGTYMLGSDHNDLFGTLD', which are signature FMN-binding motifs of the chorismate synthase family. A knowledgeable model recognizing these motifs would identify the enzyme as chorismate synthase, which catalyzes the final step of the shikimate pathway (conversion of 5-enolpyruvylshikimate-3-phosphate to chorismate). Chorismate is universally classified as a metabolic intermediate (it is the branch-point precursor for aromatic amino acids, folates, ubiquinone, and other compounds), and its biosynthesis falls under the UniProt 'Metabolic intermediate biosynthesis' pathway category. Option A describes dihydropteroate synthase (DHPS), a completely different enzyme with distinct sequence motifs. Option B (one-carbon metabolism) is unrelated to the shikimate pathway. Option C ('Antifungal biosynthesis') is not a recognized metabolic pathway. The transferable knowledge that chorismate is a metabolic intermediate and that the shikimate/chorismate biosynthesis pathway is classified under this heading in pathway databases (learned from E. coli, Bacillus, and other chorismate synthases) allows meaningful discrimination among the four choices.",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains recognizable chorismate synthase family motifs (GFDENK, conserved architecture). Identifying the enzyme as chorismate synthase via these motifs, combined with the general knowledge that chorismate is a metabolic intermediate and its biosynthesis is classified under 'Metabolic intermediate biosynthesis' in pathway taxonomy (a pattern learned from other organisms' chorismate synthases), provides a concrete and credible inference to select D over A (different enzyme, DHPS), B (different metabolic process), and C (nonsensical pathway name)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the enzyme is identified as chorismate synthase via conserved motifs, only D correctly describes its pathway. A refers to DHPS (a different enzyme with different motifs), B refers to one-carbon/folate metabolism (not the shikimate pathway), and C is not a recognized pathway. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The pathway annotation uses similarity evidence (ECO:0000250) rather than direct experimental pathway determination for this specific protein, but the enzyme's catalytic function is experimentally confirmed.",
    "The bifunctional nature of Plasmodium chorismate synthase (also having EC 1.5.1.38, dihydroneopterin aldolase activity) could theoretically create confusion with folate-related pathways, but the primary pathway annotation remains chorismate biosynthesis.",
    "The option text for A contains a trailing period and slightly unusual formatting, but its content clearly describes DHPS and is distinguishable from chorismate synthase."
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
  "benchmark_sequence_length": 547,
  "benchmark_sequence_sha256": "dd6cd0d6b670d3bec55a95f172073170bd0c4383312200bc83dee06a611f059e",
  "current_entry_audit": {
    "entryVersion": 65,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-02-08",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 547,
  "current_source_sequence_sha256": "dd6cd0d6b670d3bec55a95f172073170bd0c4383312200bc83dee06a611f059e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 64,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A5K264",
  "selected_historical_entry_version": 64,
  "selected_historical_record_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "selected_historical_source_sequence_length": 547,
  "selected_historical_source_sequence_sha256": "dd6cd0d6b670d3bec55a95f172073170bd0c4383312200bc83dee06a611f059e",
  "selected_historical_version": {
    "accession": "A5K264",
    "database": "Swiss-Prot",
    "entryVersion": 64,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "AROC_PLAVS",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A5K264\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":65,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-02-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008333\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Plasmodium\"],\"scientificName\":\"Plasmodium vivax (strain Salvador I)\",\"taxonId\":126793}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.38\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"Chorismate synthase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q12640\",\"source\":\"UniProtKB\"}],\"value\":\"Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Khera H.K.\",\"Singh S.K.\",\"Singh S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31381947\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2019.111202\"}],\"citationType\":\"journal article\",\"firstPage\":\"111202\",\"id\":\"31381947\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"111202\",\"publicationDate\":\"2019\",\"title\":\"Chorismate synthase from malaria parasites is bifunctional enzyme.\",\"volume\":\"233\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H1",
  "excerpt": "ID   AROC_PLAVS              Reviewed;         547 AA.\nAC   A5K264;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-FEB-2011, sequence version 1.\nDT   28-JAN-2026, entry version 64.\nDE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:31381947};\nDE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};\nDE            EC=4.2.3.5 {ECO:0000269|PubMed:31381947};\nGN   Name=CS {ECO:0000305}; ORFNames=PVX_114265 {ECO:0000312|EMBL:EDL46514.1};\nOS   Plasmodium vivax (strain Salvador I).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).\nOX   NCBI_TaxID=126793 {ECO:0000312|Proteomes:UP000008333};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=31381947; DOI=10.1016/j.molbiopara.2019.111202;\nRA   Khera H.K., Singh S.K., Singh S.;\nRT   \"Chorismate synthase from malaria parasites is bifunctional enzyme.\";\nRL   Mol. Biochem. Parasitol. 233:111202-111202(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Metabolic intermediate biosynthesis; chorismate biosynthesis;\nCC       chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step\nCC       7/7. {ECO:0000250|UniProtKB:Q12640}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
