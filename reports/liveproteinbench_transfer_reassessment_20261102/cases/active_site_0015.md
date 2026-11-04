# active_site_0015

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0015.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 385 (Glycyl thioester intermediate)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNLTLDHTTLHRAAKYFMDSGKAASHEAAMNLLQQFGLTIYVGEEIRSSAAHQIALLTIVNVTRRTLLGGVEVIGLPDCDSLTALAPNTGLKEAVMALGGTPVAVARPEWPTALIGSVEDYSNKDTAWRVTWEGWRAGAAPLMIGDRLSEDNSMALAPALAAAVCAGEVFSHYAGDHPMAGRRTAGLSLWQPGADWLDVDESEPELAFLPSNLWIIGLGNLGQAFAWLLALMPYETPQELQLVLQDYDRIAPSNDSTSLLSYKHDTNKMKARVVADWLDKRGFTTFIEERRFGPWTKRHADEPGVALCGVDNALARSALDQAGFPLIVEAGLGGGPQAFRSLGIHTFPSSRTAAEIWAKQVALADTSTEDMPAYQALKKSGIDACGLTQLASRTVGVPFVGLIAACLAMSELLRRLHGGKAFEFIAGSTATLQDIEFGTLHAPPYAHGYTRAMPMGWPTAP

[Multiple Choices]
A. Position 661 (For beta-ketoacyl synthase activity)
B. Position 385 (Glycyl thioester intermediate)
C. Position 10 (Proton donor)
D. Position 700 (For beta-ketoacyl synthase activity)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The matched sequence's position 385 is annotated as the active-site residue forming a glycyl thioester intermediate. The annotation cites a publication that includes mutagenesis of Cys-385, supporting choice B, though the supplied database annotation is not itself primary experimental data.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Position 385 is within the 461-residue sequence and is a cysteine. A transferable inference from E1-like enzyme chemistry is that a catalytic cysteine can form a thioester with a substrate's terminal glycine; this matches option B. Positions 661 and 700 are outside the sequence, while the stated glycyl-thioester role fits the cysteine better than the proton-donor role offered at position 10.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and answer choices permit a meaningful family/mechanism-level inference without needing the exact protein's database record. This supports B probabilistically; the original input alone does not independently prove the protein family or catalytic function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The two beta-ketoacyl synthase choices are outside the supplied sequence, and the glycyl-thioester description gives a distinct, biologically coherent match for the cysteine at position 385.


### Important caveats

- The source annotation is literature-linked and cites mutagenesis, but the excerpts do not provide the underlying experimental results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Position 385 is within the 461-residue sequence and is a cysteine. A transferable inference from E1-like enzyme chemistry is that a catalytic cysteine can form a thioester with a substrate's terminal glycine; this matches option B. Positions 661 and 700 are outside the sequence, while the stated glycyl-thioester role fits the cysteine better than the proton-donor role offered at position 10.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and answer choices permit a meaningful family/mechanism-level inference without needing the exact protein's database record. This supports B probabilistically; the original input alone does not independently prove the protein family or catalytic function."
  },
  "case_id": "active_site_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence's position 385 is annotated as the active-site residue forming a glycyl thioester intermediate. The annotation cites a publication that includes mutagenesis of Cys-385, supporting choice B, though the supplied database annotation is not itself primary experimental data."
  },
  "important_caveats": [
    "The source annotation is literature-linked and cites mutagenesis, but the excerpts do not provide the underlying experimental results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The two beta-ketoacyl synthase choices are outside the supplied sequence, and the glycyl-thioester description gives a distinct, biologically coherent match for the cysteine at position 385."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence's position 385 is annotated as the active-site residue forming a glycyl thioester intermediate. The annotation cites a publication that includes mutagenesis of Cys-385, supporting choice B, though the supplied database annotation is not itself primary experimental data.",
    "evidence_ids": ["C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Position 385 is within the 461-residue sequence and is a cysteine. A transferable inference from E1-like enzyme chemistry is that a catalytic cysteine can form a thioester with a substrate's terminal glycine; this matches option B. Positions 661 and 700 are outside the sequence, while the stated glycyl-thioester role fits the cysteine better than the proton-donor role offered at position 10.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and answer choices permit a meaningful family/mechanism-level inference without needing the exact protein's database record. This supports B probabilistically; the original input alone does not independently prove the protein family or catalytic function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The two beta-ketoacyl synthase choices are outside the supplied sequence, and the glycyl-thioester description gives a distinct, biologically coherent match for the cysteine at position 385."
  },
  "important_caveats": [
    "The source annotation is literature-linked and cites mutagenesis, but the excerpts do not provide the underlying experimental results."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates ACT_SITE at position 385 with 'Glycyl thioester intermediate' (ECO:0000305, inferred by curator based on PubMed:39020165). The cited Nature 2024 reference (Hoer et al.) reports 'PROBABLE ACTIVE SITE' and 'MUTAGENESIS OF CYS-385,' providing experimental mutagenesis support for Cys-385 as the catalytic residue. The evidence code is ECO:0000305 (curator inference) rather than direct experimental proof, but the underlying mutagenesis data in the primary paper substantiates the annotation. The description 'Glycyl thioester intermediate' is mechanistically consistent with E1 enzyme catalysis.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent lines of transferable reasoning distinguish B from the other options: (1) The protein is 461 amino acids long, so positions 661 (A) and 700 (D) are physically impossible and can be eliminated by simple arithmetic. (2) Position 10 is Leucine (M-N-L-T-L-D-H-T-T-L), which is a hydrophobic, non-catalytic residue incapable of acting as a proton donor or forming a thioester, eliminating C. (3) The protein sequence exhibits hallmarks of the E1 enzyme superfamily (ubiquitin-activating enzymes): a conserved 'GLGG' nucleotide-binding motif near the middle of the sequence, overall domain architecture consistent with adenylation and thioester-forming domains, and the 'ACGLT' motif near position 385 containing a cysteine. Across all known E1 enzymes (human UBA1, yeast Uba1, bacterial E1-like proteins), the universal catalytic mechanism involves an active-site cysteine forming a thioester bond with the C-terminal glycine of the substrate (ubiquitin or ubiquitin-like protein). The descriptor 'Glycyl thioester intermediate' in option B is the mechanistic signature of E1 catalysis. A model recognizing E1 family features and applying the conserved thioester-intermediate mechanism can identify position 385 as the catalytic cysteine without knowing this protein's specific database record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question is answerable through: (a) elimination of positions exceeding the 461-aa sequence length (A, D), (b) recognition that position 10 is Leucine and cannot be a proton donor (C), and (c) E1 enzyme family knowledge that the catalytic mechanism universally involves a Cys forming a glycyl thioester intermediate, pointing to position 385. The 'Glycyl thioester intermediate' label in option B is a mechanistic descriptor shared across the entire E1 superfamily, making it transferable knowledge rather than a protein-specific annotation lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D reference positions beyond the 461-residue protein and are physically impossible. Option C assigns a proton-donor role to Leucine at position 10, which is biochemically implausible. Only option B is mechanistically and structurally consistent with the sequence and E1 enzyme biology.


### Important caveats

- The UniProt annotation uses ECO:0000305 (inferred by curator), and the primary reference qualifies the site as 'PROBABLE ACTIVE SITE' with mutagenesis of Cys-385 as supporting evidence. This is not a direct crystallographic or kinetic determination but is backed by functional mutagenesis data.
- The protein identity (BilD, Collimonas sp. OK412) and its E1-like classification were not provided in the original model input; the model must infer E1 family membership from sequence features alone.
- Positions 661 and 700 being impossible is a trivial elimination based on sequence length, which makes the question somewhat easier than a typical active-site prediction task.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent lines of transferable reasoning distinguish B from the other options: (1) The protein is 461 amino acids long, so positions 661 (A) and 700 (D) are physically impossible and can be eliminated by simple arithmetic. (2) Position 10 is Leucine (M-N-L-T-L-D-H-T-T-L), which is a hydrophobic, non-catalytic residue incapable of acting as a proton donor or forming a thioester, eliminating C. (3) The protein sequence exhibits hallmarks of the E1 enzyme superfamily (ubiquitin-activating enzymes): a conserved 'GLGG' nucleotide-binding motif near the middle of the sequence, overall domain architecture consistent with adenylation and thioester-forming domains, and the 'ACGLT' motif near position 385 containing a cysteine. Across all known E1 enzymes (human UBA1, yeast Uba1, bacterial E1-like proteins), the universal catalytic mechanism involves an active-site cysteine forming a thioester bond with the C-terminal glycine of the substrate (ubiquitin or ubiquitin-like protein). The descriptor 'Glycyl thioester intermediate' in option B is the mechanistic signature of E1 catalysis. A model recognizing E1 family features and applying the conserved thioester-intermediate mechanism can identify position 385 as the catalytic cysteine without knowing this protein's specific database record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through: (a) elimination of positions exceeding the 461-aa sequence length (A, D), (b) recognition that position 10 is Leucine and cannot be a proton donor (C), and (c) E1 enzyme family knowledge that the catalytic mechanism universally involves a Cys forming a glycyl thioester intermediate, pointing to position 385. The 'Glycyl thioester intermediate' label in option B is a mechanistic descriptor shared across the entire E1 superfamily, making it transferable knowledge rather than a protein-specific annotation lookup."
  },
  "case_id": "active_site_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates ACT_SITE at position 385 with 'Glycyl thioester intermediate' (ECO:0000305, inferred by curator based on PubMed:39020165). The cited Nature 2024 reference (Hoer et al.) reports 'PROBABLE ACTIVE SITE' and 'MUTAGENESIS OF CYS-385,' providing experimental mutagenesis support for Cys-385 as the catalytic residue. The evidence code is ECO:0000305 (curator inference) rather than direct experimental proof, but the underlying mutagenesis data in the primary paper substantiates the annotation. The description 'Glycyl thioester intermediate' is mechanistically consistent with E1 enzyme catalysis."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (inferred by curator), and the primary reference qualifies the site as 'PROBABLE ACTIVE SITE' with mutagenesis of Cys-385 as supporting evidence. This is not a direct crystallographic or kinetic determination but is backed by functional mutagenesis data.",
    "The protein identity (BilD, Collimonas sp. OK412) and its E1-like classification were not provided in the original model input; the model must infer E1 family membership from sequence features alone.",
    "Positions 661 and 700 being impossible is a trivial elimination based on sequence length, which makes the question somewhat easier than a typical active-site prediction task."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D reference positions beyond the 461-residue protein and are physically impossible. Option C assigns a proton-donor role to Leucine at position 10, which is biochemically implausible. Only option B is mechanistically and structurally consistent with the sequence and E1 enzyme biology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates ACT_SITE at position 385 with 'Glycyl thioester intermediate' (ECO:0000305, inferred by curator based on PubMed:39020165). The cited Nature 2024 reference (Hoer et al.) reports 'PROBABLE ACTIVE SITE' and 'MUTAGENESIS OF CYS-385,' providing experimental mutagenesis support for Cys-385 as the catalytic residue. The evidence code is ECO:0000305 (curator inference) rather than direct experimental proof, but the underlying mutagenesis data in the primary paper substantiates the annotation. The description 'Glycyl thioester intermediate' is mechanistically consistent with E1 enzyme catalysis.",
    "evidence_ids": ["C5", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent lines of transferable reasoning distinguish B from the other options: (1) The protein is 461 amino acids long, so positions 661 (A) and 700 (D) are physically impossible and can be eliminated by simple arithmetic. (2) Position 10 is Leucine (M-N-L-T-L-D-H-T-T-L), which is a hydrophobic, non-catalytic residue incapable of acting as a proton donor or forming a thioester, eliminating C. (3) The protein sequence exhibits hallmarks of the E1 enzyme superfamily (ubiquitin-activating enzymes): a conserved 'GLGG' nucleotide-binding motif near the middle of the sequence, overall domain architecture consistent with adenylation and thioester-forming domains, and the 'ACGLT' motif near position 385 containing a cysteine. Across all known E1 enzymes (human UBA1, yeast Uba1, bacterial E1-like proteins), the universal catalytic mechanism involves an active-site cysteine forming a thioester bond with the C-terminal glycine of the substrate (ubiquitin or ubiquitin-like protein). The descriptor 'Glycyl thioester intermediate' in option B is the mechanistic signature of E1 catalysis. A model recognizing E1 family features and applying the conserved thioester-intermediate mechanism can identify position 385 as the catalytic cysteine without knowing this protein's specific database record.",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through: (a) elimination of positions exceeding the 461-aa sequence length (A, D), (b) recognition that position 10 is Leucine and cannot be a proton donor (C), and (c) E1 enzyme family knowledge that the catalytic mechanism universally involves a Cys forming a glycyl thioester intermediate, pointing to position 385. The 'Glycyl thioester intermediate' label in option B is a mechanistic descriptor shared across the entire E1 superfamily, making it transferable knowledge rather than a protein-specific annotation lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D reference positions beyond the 461-residue protein and are physically impossible. Option C assigns a proton-donor role to Leucine at position 10, which is biochemically implausible. Only option B is mechanistically and structurally consistent with the sequence and E1 enzyme biology."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (inferred by curator), and the primary reference qualifies the site as 'PROBABLE ACTIVE SITE' with mutagenesis of Cys-385 as supporting evidence. This is not a direct crystallographic or kinetic determination but is backed by functional mutagenesis data.",
    "The protein identity (BilD, Collimonas sp. OK412) and its E1-like classification were not provided in the original model input; the model must infer E1 family membership from sequence features alone.",
    "Positions 661 and 700 being impossible is a trivial elimination based on sequence length, which makes the question somewhat easier than a typical active-site prediction task."
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
  "benchmark_sequence_length": 461,
  "benchmark_sequence_sha256": "41932a11ef3e7a2f44ccd75bad17dee7b891dfe4dd486698c3c078f6b2c6f62e",
  "current_entry_audit": {
    "entryVersion": 15,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-11-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 461,
  "current_source_sequence_sha256": "41932a11ef3e7a2f44ccd75bad17dee7b891dfe4dd486698c3c078f6b2c6f62e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1I1P074",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "a37af1ad780f0f67b0b403cc351978c7e209c2d02ee53894ad0fc5e2c09bea6a",
  "selected_historical_source_sequence_length": 461,
  "selected_historical_source_sequence_sha256": "41932a11ef3e7a2f44ccd75bad17dee7b891dfe4dd486698c3c078f6b2c6f62e",
  "selected_historical_version": {
    "accession": "A0A1I1P074",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BILD_COLS4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1P074.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1I1P074\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:37.902008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1P074.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1P074.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":15,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-11-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:37.902008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1P074.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1P074.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Oxalobacteraceae\",\"Collimonas\"],\"scientificName\":\"Collimonas sp. (strain OK412)\",\"taxonId\":1801619}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:37.902008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1P074.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1P074.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"E1 ubiquitin-conjugating enzyme BilD\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39020165\",\"source\":\"PubMed\"}],\"value\":\"6.2.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39020165\",\"source\":\"PubMed\"}],\"value\":\"Bacterial E1-like protein BilD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:37.902008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1P074.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1P074.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Glycyl thioester intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39020165\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":385},\"start\":{\"modifier\":\"EXACT\",\"value\":385}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:24:37.902008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1P074.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1P074.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Hoer J.\",\"Wolf S.G.\",\"Sorek R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39020165\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-024-07616-5\"}],\"citationType\":\"journal article\",\"firstPage\":\"850\",\"id\":\"39020165\",\"journal\":\"Nature\",\"lastPage\":\"856\",\"publicationDate\":\"2024\",\"title\":\"Bacteria conjugate ubiquitin-like proteins to interfere with phage assembly.\",\"volume\":\"631\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"PROBABLE ACTIVE SITE\",\"MUTAGENESIS OF CYS-385\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:37.902008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "85e7a104b9ec3fed02e35ea4232cf86a383df56f7435a81173e8fa183bf247be",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1P074.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1P074?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   BILD_COLS4              Reviewed;         461 AA.\nAC   A0A1I1P074;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-NOV-2017, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Bacterial E1-like protein BilD {ECO:0000303|PubMed:39020165};\nDE            EC=6.2.1.- {ECO:0000305|PubMed:39020165};\nDE   AltName: Full=E1 ubiquitin-conjugating enzyme BilD;\nGN   Name=bilD {ECO:0000303|PubMed:39020165};\nGN   ORFNames=SAMN04515619_11955 {ECO:0000312|EMBL:SFD01128.1};\nOS   Collimonas sp. (strain OK412).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Oxalobacteraceae; Collimonas.\nOX   NCBI_TaxID=1801619;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:41.131133+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a37af1ad780f0f67b0b403cc351978c7e209c2d02ee53894ad0fc5e2c09bea6a",
  "url": "https://rest.uniprot.org/unisave/A0A1I1P074?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1P074?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, PROBABLE ACTIVE SITE, AND MUTAGENESIS OF CYS-385.\nRX   PubMed=39020165; DOI=10.1038/s41586-024-07616-5;\nRA   Hoer J., Wolf S.G., Sorek R.;\nRT   \"Bacteria conjugate ubiquitin-like proteins to interfere with phage\nRT   assembly.\";\nRL   Nature 631:850-856(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:41.131133+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a37af1ad780f0f67b0b403cc351978c7e209c2d02ee53894ad0fc5e2c09bea6a",
  "url": "https://rest.uniprot.org/unisave/A0A1I1P074?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1P074?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        385\nFT                   /note=\"Glycyl thioester intermediate\"\nFT                   /evidence=\"ECO:0000305|PubMed:39020165\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:41.131133+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a37af1ad780f0f67b0b403cc351978c7e209c2d02ee53894ad0fc5e2c09bea6a",
  "url": "https://rest.uniprot.org/unisave/A0A1I1P074?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 15. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
