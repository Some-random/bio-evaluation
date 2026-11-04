# EC_number_0170

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0170.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 3.1.1.29

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAIKLIVGLANPGAEYAATRHNAGAWYVDLLAERLRAPLREEPKFFGYTSRITLEGEDVRLLVPTTFMNLSGKAVGAMASFYRIQPDEILVAHDELDLPPGVAKFKLGGGHGGHNGLKDIISKLGNNPNFHRLRVGIGHPGDKNKVVGFVLGKPPVSEQKLIDEAIDEAARCTELWFKEGLAKATSRLHTFKAQ

[Multiple Choices]
A. 3.1.1.80
B. 3.1.1.29
C. 2.3.2.27
D. 1.1.1.12
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry assigns this protein EC 3.1.1.29 as peptidyl-tRNA hydrolase, though that general assignment is attributed to a HAMAP computational rule. The entry also records a cited catalytic reaction involving hydrolysis of N-acetylglycyl-tRNA, supporting the relevant activity. Thus choice B is supported, while the evidence does not imply that every detail of the general reaction assignment was independently established experimentally.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 194-residue sequence is consistent with the conserved, compact bacterial peptidyl-tRNA hydrolase family. Family recognition and transferable knowledge of Pth proteins support EC 3.1.1.29, a hydrolase, over the offered alternative EC classes for a different hydrolase, a transferase, or an oxidoreductase. This is a family-level inference, not reliance on the exact protein's database record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A credible family-level inference meaningfully distinguishes B from the actual alternatives. It need not establish the exact substrate range or independently prove all aspects of the EC annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the Pth-family inference supports EC 3.1.1.29; no competing option is comparably supported.


### Important caveats

- The broad EC assignment in the source entry is computationally supported by a HAMAP rule; the cited reaction evidence concerns a particular N-acetylglycyl-tRNA substrate.
- The source entry matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 194-residue sequence is consistent with the conserved, compact bacterial peptidyl-tRNA hydrolase family. Family recognition and transferable knowledge of Pth proteins support EC 3.1.1.29, a hydrolase, over the offered alternative EC classes for a different hydrolase, a transferase, or an oxidoreductase. This is a family-level inference, not reliance on the exact protein's database record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A credible family-level inference meaningfully distinguishes B from the actual alternatives. It need not establish the exact substrate range or independently prove all aspects of the EC annotation."
  },
  "case_id": "EC_number_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns this protein EC 3.1.1.29 as peptidyl-tRNA hydrolase, though that general assignment is attributed to a HAMAP computational rule. The entry also records a cited catalytic reaction involving hydrolysis of N-acetylglycyl-tRNA, supporting the relevant activity. Thus choice B is supported, while the evidence does not imply that every detail of the general reaction assignment was independently established experimentally."
  },
  "important_caveats": [
    "The broad EC assignment in the source entry is computationally supported by a HAMAP rule; the cited reaction evidence concerns a particular N-acetylglycyl-tRNA substrate.",
    "The source entry matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the Pth-family inference supports EC 3.1.1.29; no competing option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns this protein EC 3.1.1.29 as peptidyl-tRNA hydrolase, though that general assignment is attributed to a HAMAP computational rule. The entry also records a cited catalytic reaction involving hydrolysis of N-acetylglycyl-tRNA, supporting the relevant activity. Thus choice B is supported, while the evidence does not imply that every detail of the general reaction assignment was independently established experimentally.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 194-residue sequence is consistent with the conserved, compact bacterial peptidyl-tRNA hydrolase family. Family recognition and transferable knowledge of Pth proteins support EC 3.1.1.29, a hydrolase, over the offered alternative EC classes for a different hydrolase, a transferase, or an oxidoreductase. This is a family-level inference, not reliance on the exact protein's database record.",
    "missing_item_specific_fact": "",
    "reason": "A credible family-level inference meaningfully distinguishes B from the actual alternatives. It need not establish the exact substrate range or independently prove all aspects of the EC annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the Pth-family inference supports EC 3.1.1.29; no competing option is comparably supported."
  },
  "important_caveats": [
    "The broad EC assignment in the source entry is computationally supported by a HAMAP rule; the cited reaction evidence concerns a particular N-acetylglycyl-tRNA substrate.",
    "The source entry matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0F6B281 (PTH_SALT1) is annotated with EC 3.1.1.29 (Peptidyl-tRNA hydrolase) via HAMAP-Rule MF_00083 (ECO:0000255, computational). Two independent experimental studies (PubMed 27264868, 29777131) confirm the catalytic activity (ECO:0000305, direct assay) showing hydrolysis of N-acyl-L-alpha-aminoacyl-tRNA and N-acetylglycyl-tRNA(Gly). The sequence matches the benchmark sequence exactly. The EC assignment is supported by both computational family annotation and experimental catalytic data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two highly diagnostic motifs of the peptidyl-tRNA hydrolase (Pth) family: (1) 'GGGHGGHN' near position ~120, which is a signature of the Pth active site conserved across Pth homologs in E. coli, Staphylococcus, and other bacteria, and (2) 'GHPGD' near position ~140, part of the catalytic loop unique to Pth. These motifs are NOT found in generic esterases/lipases (ruling out 3.1.1.80), transferases (ruling out 2.3.2.27), or oxidoreductases (ruling out 1.1.1.12). The protein length (~194 aa) and β-sheet-rich composition are also consistent with the Pth fold. A model trained on Pth homologs from E. coli or other bacteria would recognize these conserved active-site motifs and assign EC 3.1.1.29 over the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 'GGGHGGHN' and 'GHPGD' motifs are well-known, transferable family-level signatures of Pth enzymes, shared across many bacterial species. They are not specific to this exact Salmonella protein but are conserved features learned from Pth homologs. These motifs meaningfully distinguish 3.1.1.29 (Pth) from the other three options, which belong to entirely different enzyme classes or unrelated esterases lacking these motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The conserved Pth-specific motifs ('GGGHGGHN', 'GHPGD') clearly identify the enzyme as peptidyl-tRNA hydrolase. The other options (3.1.1.80 esterase, 2.3.2.27 transferase, 1.1.1.12 oxidoreductase) lack these motifs and belong to different enzyme classes. No ambiguity among the four choices.


### Important caveats

- The primary EC annotation is via HAMAP-Rule (computational similarity, ECO:0000255), not direct experimental determination of the full 4-digit EC number, though catalytic activity was experimentally confirmed.
- EC 3.1.1.80 is a less common esterase; a model unfamiliar with this specific EC number might find it harder to exclude, but the Pth-specific motifs still distinguish it.
- The sequence is 194 aa, slightly shorter than E. coli Pth (~205 aa), but the conserved motifs are intact.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two highly diagnostic motifs of the peptidyl-tRNA hydrolase (Pth) family: (1) 'GGGHGGHN' near position ~120, which is a signature of the Pth active site conserved across Pth homologs in E. coli, Staphylococcus, and other bacteria, and (2) 'GHPGD' near position ~140, part of the catalytic loop unique to Pth. These motifs are NOT found in generic esterases/lipases (ruling out 3.1.1.80), transferases (ruling out 2.3.2.27), or oxidoreductases (ruling out 1.1.1.12). The protein length (~194 aa) and β-sheet-rich composition are also consistent with the Pth fold. A model trained on Pth homologs from E. coli or other bacteria would recognize these conserved active-site motifs and assign EC 3.1.1.29 over the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 'GGGHGGHN' and 'GHPGD' motifs are well-known, transferable family-level signatures of Pth enzymes, shared across many bacterial species. They are not specific to this exact Salmonella protein but are conserved features learned from Pth homologs. These motifs meaningfully distinguish 3.1.1.29 (Pth) from the other three options, which belong to entirely different enzyme classes or unrelated esterases lacking these motifs."
  },
  "case_id": "EC_number_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F6B281 (PTH_SALT1) is annotated with EC 3.1.1.29 (Peptidyl-tRNA hydrolase) via HAMAP-Rule MF_00083 (ECO:0000255, computational). Two independent experimental studies (PubMed 27264868, 29777131) confirm the catalytic activity (ECO:0000305, direct assay) showing hydrolysis of N-acyl-L-alpha-aminoacyl-tRNA and N-acetylglycyl-tRNA(Gly). The sequence matches the benchmark sequence exactly. The EC assignment is supported by both computational family annotation and experimental catalytic data."
  },
  "important_caveats": [
    "The primary EC annotation is via HAMAP-Rule (computational similarity, ECO:0000255), not direct experimental determination of the full 4-digit EC number, though catalytic activity was experimentally confirmed.",
    "EC 3.1.1.80 is a less common esterase; a model unfamiliar with this specific EC number might find it harder to exclude, but the Pth-specific motifs still distinguish it.",
    "The sequence is 194 aa, slightly shorter than E. coli Pth (~205 aa), but the conserved motifs are intact."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved Pth-specific motifs ('GGGHGGHN', 'GHPGD') clearly identify the enzyme as peptidyl-tRNA hydrolase. The other options (3.1.1.80 esterase, 2.3.2.27 transferase, 1.1.1.12 oxidoreductase) lack these motifs and belong to different enzyme classes. No ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F6B281 (PTH_SALT1) is annotated with EC 3.1.1.29 (Peptidyl-tRNA hydrolase) via HAMAP-Rule MF_00083 (ECO:0000255, computational). Two independent experimental studies (PubMed 27264868, 29777131) confirm the catalytic activity (ECO:0000305, direct assay) showing hydrolysis of N-acyl-L-alpha-aminoacyl-tRNA and N-acetylglycyl-tRNA(Gly). The sequence matches the benchmark sequence exactly. The EC assignment is supported by both computational family annotation and experimental catalytic data.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two highly diagnostic motifs of the peptidyl-tRNA hydrolase (Pth) family: (1) 'GGGHGGHN' near position ~120, which is a signature of the Pth active site conserved across Pth homologs in E. coli, Staphylococcus, and other bacteria, and (2) 'GHPGD' near position ~140, part of the catalytic loop unique to Pth. These motifs are NOT found in generic esterases/lipases (ruling out 3.1.1.80), transferases (ruling out 2.3.2.27), or oxidoreductases (ruling out 1.1.1.12). The protein length (~194 aa) and β-sheet-rich composition are also consistent with the Pth fold. A model trained on Pth homologs from E. coli or other bacteria would recognize these conserved active-site motifs and assign EC 3.1.1.29 over the other options.",
    "missing_item_specific_fact": "",
    "reason": "The 'GGGHGGHN' and 'GHPGD' motifs are well-known, transferable family-level signatures of Pth enzymes, shared across many bacterial species. They are not specific to this exact Salmonella protein but are conserved features learned from Pth homologs. These motifs meaningfully distinguish 3.1.1.29 (Pth) from the other three options, which belong to entirely different enzyme classes or unrelated esterases lacking these motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved Pth-specific motifs ('GGGHGGHN', 'GHPGD') clearly identify the enzyme as peptidyl-tRNA hydrolase. The other options (3.1.1.80 esterase, 2.3.2.27 transferase, 1.1.1.12 oxidoreductase) lack these motifs and belong to different enzyme classes. No ambiguity among the four choices."
  },
  "important_caveats": [
    "The primary EC annotation is via HAMAP-Rule (computational similarity, ECO:0000255), not direct experimental determination of the full 4-digit EC number, though catalytic activity was experimentally confirmed.",
    "EC 3.1.1.80 is a less common esterase; a model unfamiliar with this specific EC number might find it harder to exclude, but the Pth-specific motifs still distinguish it.",
    "The sequence is 194 aa, slightly shorter than E. coli Pth (~205 aa), but the conserved motifs are intact."
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
  "benchmark_sequence_length": 194,
  "benchmark_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "current_entry_audit": {
    "entryVersion": 43,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2015-06-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 194,
  "current_source_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 42,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0F6B281",
  "selected_historical_entry_version": 42,
  "selected_historical_record_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "selected_historical_source_sequence_length": 194,
  "selected_historical_source_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "selected_historical_version": {
    "accession": "A0A0F6B281",
    "database": "Swiss-Prot",
    "entryVersion": 42,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PTH_SALT1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0F6B281\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":43,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2015-06-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Salmonella\"],\"scientificName\":\"Salmonella typhimurium (strain 14028s / SGSC 2262)\",\"taxonId\":588858}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"3.1.1.29\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Peptidyl-tRNA hydrolase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Pth\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.1.1.29\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"name\":\"an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:54448\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10123\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:13883\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59874\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:78442\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138191\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"27264868\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"29777131\",\"source\":\"PubMed\"}],\"name\":\"N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81979\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9664\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19766\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61887\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:78442\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232036\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Cheverton A.M.\",\"Gollan B.\",\"Przydacz M.\",\"Wong C.T.\",\"Mylona A.\",\"Hare S.A.\",\"Helaine S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27264868\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molcel.2016.05.002\"}],\"citationType\":\"journal article\",\"firstPage\":\"86\",\"id\":\"27264868\",\"journal\":\"Mol. Cell\",\"lastPage\":\"96\",\"publicationDate\":\"2016\",\"title\":\"A Salmonella Toxin Promotes Persister Formation through Acetylation of tRNA.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Rycroft J.A.\",\"Gollan B.\",\"Grabe G.J.\",\"Hall A.\",\"Cheverton A.M.\",\"Larrouy-Maumus G.\",\"Hare S.A.\",\"Helaine S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29777131\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-018-04472-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"1993\",\"id\":\"29777131\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"1993\",\"publicationDate\":\"2018\",\"title\":\"Activity of acetyltransferase toxins involved in Salmonella persister formation during macrophage infection.\",\"volume\":\"9\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H1",
  "excerpt": "ID   PTH_SALT1               Reviewed;         194 AA.\nAC   A0A0F6B281;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JUN-2015, sequence version 1.\nDT   28-JAN-2026, entry version 42.\nDE   RecName: Full=Peptidyl-tRNA hydrolase {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            Short=Pth {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            EC=3.1.1.29 {ECO:0000255|HAMAP-Rule:MF_00083};\nGN   Name=pth {ECO:0000255|HAMAP-Rule:MF_00083, ECO:0000312|EMBL:ACY88619.1};\nGN   OrderedLocusNames=STM14_2156 {ECO:0000312|EMBL:ACY88619.1};\nOS   Salmonella typhimurium (strain 14028s / SGSC 2262).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Salmonella.\nOX   NCBI_TaxID=588858;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Peptidyl-tRNA hydrolase {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            Short=Pth {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            EC=3.1.1.29 {ECO:0000255|HAMAP-Rule:MF_00083};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023;\nRX   PubMed=27264868; DOI=10.1016/j.molcel.2016.05.002;\nRA   Cheverton A.M., Gollan B., Przydacz M., Wong C.T., Mylona A., Hare S.A.,\nRA   Helaine S.;\nRT   \"A Salmonella Toxin Promotes Persister Formation through Acetylation of\nRT   tRNA.\";\nRL   Mol. Cell 63:86-96(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023;\nRX   PubMed=29777131; DOI=10.1038/s41467-018-04472-6;\nRA   Rycroft J.A., Gollan B., Grabe G.J., Hall A., Cheverton A.M.,\nRA   Larrouy-Maumus G., Hare S.A., Helaine S.;\nRT   \"Activity of acetyltransferase toxins involved in Salmonella persister\nRT   formation during macrophage infection.\";\nRL   Nat. Commun. 9:1993-1993(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino\nCC         acid + a tRNA + H(+); Xref=Rhea:RHEA:54448, Rhea:RHEA-COMP:10123,\nCC         Rhea:RHEA-COMP:13883, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:59874, ChEBI:CHEBI:78442, ChEBI:CHEBI:138191;\nCC         EC=3.1.1.29; Evidence={ECO:0000255|HAMAP-Rule:MF_00083};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) +\nCC         H(+); Xref=Rhea:RHEA:81979, Rhea:RHEA-COMP:9664, Rhea:RHEA-\nCC         COMP:19766, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:61887,\nCC         ChEBI:CHEBI:78442, ChEBI:CHEBI:232036;\nCC         Evidence={ECO:0000305|PubMed:27264868, ECO:0000305|PubMed:29777131};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 170. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
