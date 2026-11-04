# catalytic_activity_0119

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0119.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLNDYLQWEKFILRGVEFPTRYRVDGDEVEITPSSRLYVSGMGGSGVVGDLIRDFSIVWNWDVEVTVVKDYFLRARDGLLIAVSYSGNTVETLYSVEYAKKRRIPTVAITTGGKLAQMGVPTIIIPKASAPRAALPQMLTAALHVVRKVYGIPIEIPEALEPPNDPLIHKLMEDFQKRPTIVAPETMRGVAYRVKNEFNENAKIEPSVEILPEAHHNWIEGSERPIVALTSPHIPREHQERVKATLEILGGTLYVVEMSTRGVLTFLREVGVASIKLAESRGVNPLATPRIEALKRRLQ

[Multiple Choices]
A. L-lysine(in) = L-lysine(out)
B. cyclo(N(8)-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dimethylallyl)-L-Trp) + AH2 + O2 = okaramine C + A + H2O
C. a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)
D. alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated with the reaction in choice D, with an evidence code citing experimental evidence (ECO:0000269). The cited paper was not independently reviewed here, so this supports the key through the source annotation rather than independent validation.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 299-residue sequence is a compact, soluble enzyme sequence with a pattern consistent with the phosphoglucose/phosphomannose isomerase family. Transferable family knowledge connects phosphoglucose isomerase activity to the glucose-6-phosphate ⇌ fructose-6-phosphate interconversion in D. The sequence lacks the long hydrophobic segments expected for the lysine transporter in A; B describes a specialized oxidative cyclization, and C a glucosyl-transfer reaction, neither matching that isomerase-family inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference meaningfully distinguishes D among these choices without requiring the exact protein's database entry. The sequence alone does not establish every activity of a potentially bifunctional enzyme, but the additional activity is not among the options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source also annotates mannose-6-phosphate isomerization, but that reaction is not offered. Among the listed choices, D is the matching isomerase reaction.


### Important caveats

- The evidence is a database annotation citing a paper with an experimental evidence code; the primary paper was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 299-residue sequence is a compact, soluble enzyme sequence with a pattern consistent with the phosphoglucose/phosphomannose isomerase family. Transferable family knowledge connects phosphoglucose isomerase activity to the glucose-6-phosphate ⇌ fructose-6-phosphate interconversion in D. The sequence lacks the long hydrophobic segments expected for the lysine transporter in A; B describes a specialized oxidative cyclization, and C a glucosyl-transfer reaction, neither matching that isomerase-family inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully distinguishes D among these choices without requiring the exact protein's database entry. The sequence alone does not establish every activity of a potentially bifunctional enzyme, but the additional activity is not among the options."
  },
  "case_id": "catalytic_activity_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated with the reaction in choice D, with an evidence code citing experimental evidence (ECO:0000269). The cited paper was not independently reviewed here, so this supports the key through the source annotation rather than independent validation."
  },
  "important_caveats": [
    "The evidence is a database annotation citing a paper with an experimental evidence code; the primary paper was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source also annotates mannose-6-phosphate isomerization, but that reaction is not offered. Among the listed choices, D is the matching isomerase reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated with the reaction in choice D, with an evidence code citing experimental evidence (ECO:0000269). The cited paper was not independently reviewed here, so this supports the key through the source annotation rather than independent validation.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 299-residue sequence is a compact, soluble enzyme sequence with a pattern consistent with the phosphoglucose/phosphomannose isomerase family. Transferable family knowledge connects phosphoglucose isomerase activity to the glucose-6-phosphate ⇌ fructose-6-phosphate interconversion in D. The sequence lacks the long hydrophobic segments expected for the lysine transporter in A; B describes a specialized oxidative cyclization, and C a glucosyl-transfer reaction, neither matching that isomerase-family inference.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully distinguishes D among these choices without requiring the exact protein's database entry. The sequence alone does not establish every activity of a potentially bifunctional enzyme, but the additional activity is not among the options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source also annotates mannose-6-phosphate isomerization, but that reaction is not offered. Among the listed choices, D is the matching isomerase reaction."
  },
  "important_caveats": [
    "The evidence is a database annotation citing a paper with an experimental evidence code; the primary paper was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A3MTR6 (PGMI_PYRCJ) is annotated as a bifunctional phosphoglucose/phosphomannose isomerase (EC 5.3.1.9 and 5.3.1.8) with experimental evidence (ECO:0000269, PubMed 39208883). The catalytic activity 'alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate' (EC 5.3.1.9) is explicitly listed, matching choice D. The sequence in the question matches the UniProt entry (299 aa, SHA-256 match).

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple well-known phosphoglucose isomerase (PGI, PF00341) family motifs: 'SGMGGSG' near residues 30-36 (the classic PGI substrate-binding glycine-rich motif), 'GGK' around residue 100, and 'GGTLYVVEMSTRGV' near the C-terminus. These motifs are extensively documented across PGI homologs in E. coli, yeast, and human GPI. A knowledgeable model recognizing these family signatures would identify the protein as a phosphoglucose isomerase, directly matching choice D. The distractors are easily excluded: A is a membrane transporter (no isomerase motifs), B is a specialized alkaloid biosynthesis reaction (no relevant sequence features), and C is a glycosidase/transglycosidase reaction (different fold and motifs). The overall ~299 aa length is also consistent with archaeal PGI.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PGI family sequence signatures (SGMGGSG, GGTLY, GGK) are highly conserved across all domains of life and are textbook-level biochemistry knowledge. These motifs meaningfully distinguish D (phosphoglucose isomerase) from the three unrelated distractors without requiring recall of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is bifunctional (also catalyzes mannose-6-phosphate = fructose-6-phosphate, EC 5.3.1.8), that reaction is not offered among the choices. Only choice D corresponds to a reaction actually catalyzed by this enzyme. The other three choices correspond to entirely different enzyme classes.


### Important caveats

- The protein is bifunctional (PGI/PMI); the PMI activity (EC 5.3.1.8) is not among the offered choices, so it does not create ambiguity.
- The experimental evidence (PubMed 39208883, 2024) is relatively recent; the UniProt entry was first public in Feb 2025. The author's source snapshot is unknown but the sequence matches.
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model; however, the PGI family motifs in the sequence provide an independent, transferable basis for selecting D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple well-known phosphoglucose isomerase (PGI, PF00341) family motifs: 'SGMGGSG' near residues 30-36 (the classic PGI substrate-binding glycine-rich motif), 'GGK' around residue 100, and 'GGTLYVVEMSTRGV' near the C-terminus. These motifs are extensively documented across PGI homologs in E. coli, yeast, and human GPI. A knowledgeable model recognizing these family signatures would identify the protein as a phosphoglucose isomerase, directly matching choice D. The distractors are easily excluded: A is a membrane transporter (no isomerase motifs), B is a specialized alkaloid biosynthesis reaction (no relevant sequence features), and C is a glycosidase/transglycosidase reaction (different fold and motifs). The overall ~299 aa length is also consistent with archaeal PGI.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PGI family sequence signatures (SGMGGSG, GGTLY, GGK) are highly conserved across all domains of life and are textbook-level biochemistry knowledge. These motifs meaningfully distinguish D (phosphoglucose isomerase) from the three unrelated distractors without requiring recall of this specific protein's database annotation."
  },
  "case_id": "catalytic_activity_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A3MTR6 (PGMI_PYRCJ) is annotated as a bifunctional phosphoglucose/phosphomannose isomerase (EC 5.3.1.9 and 5.3.1.8) with experimental evidence (ECO:0000269, PubMed 39208883). The catalytic activity 'alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate' (EC 5.3.1.9) is explicitly listed, matching choice D. The sequence in the question matches the UniProt entry (299 aa, SHA-256 match)."
  },
  "important_caveats": [
    "The protein is bifunctional (PGI/PMI); the PMI activity (EC 5.3.1.8) is not among the offered choices, so it does not create ambiguity.",
    "The experimental evidence (PubMed 39208883, 2024) is relatively recent; the UniProt entry was first public in Feb 2025. The author's source snapshot is unknown but the sequence matches.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; however, the PGI family motifs in the sequence provide an independent, transferable basis for selecting D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (also catalyzes mannose-6-phosphate = fructose-6-phosphate, EC 5.3.1.8), that reaction is not offered among the choices. Only choice D corresponds to a reaction actually catalyzed by this enzyme. The other three choices correspond to entirely different enzyme classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A3MTR6 (PGMI_PYRCJ) is annotated as a bifunctional phosphoglucose/phosphomannose isomerase (EC 5.3.1.9 and 5.3.1.8) with experimental evidence (ECO:0000269, PubMed 39208883). The catalytic activity 'alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate' (EC 5.3.1.9) is explicitly listed, matching choice D. The sequence in the question matches the UniProt entry (299 aa, SHA-256 match).",
    "evidence_ids": ["C5", "C4", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple well-known phosphoglucose isomerase (PGI, PF00341) family motifs: 'SGMGGSG' near residues 30-36 (the classic PGI substrate-binding glycine-rich motif), 'GGK' around residue 100, and 'GGTLYVVEMSTRGV' near the C-terminus. These motifs are extensively documented across PGI homologs in E. coli, yeast, and human GPI. A knowledgeable model recognizing these family signatures would identify the protein as a phosphoglucose isomerase, directly matching choice D. The distractors are easily excluded: A is a membrane transporter (no isomerase motifs), B is a specialized alkaloid biosynthesis reaction (no relevant sequence features), and C is a glycosidase/transglycosidase reaction (different fold and motifs). The overall ~299 aa length is also consistent with archaeal PGI.",
    "missing_item_specific_fact": "",
    "reason": "The PGI family sequence signatures (SGMGGSG, GGTLY, GGK) are highly conserved across all domains of life and are textbook-level biochemistry knowledge. These motifs meaningfully distinguish D (phosphoglucose isomerase) from the three unrelated distractors without requiring recall of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (also catalyzes mannose-6-phosphate = fructose-6-phosphate, EC 5.3.1.8), that reaction is not offered among the choices. Only choice D corresponds to a reaction actually catalyzed by this enzyme. The other three choices correspond to entirely different enzyme classes."
  },
  "important_caveats": [
    "The protein is bifunctional (PGI/PMI); the PMI activity (EC 5.3.1.8) is not among the offered choices, so it does not create ambiguity.",
    "The experimental evidence (PubMed 39208883, 2024) is relatively recent; the UniProt entry was first public in Feb 2025. The author's source snapshot is unknown but the sequence matches.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; however, the PGI family motifs in the sequence provide an independent, transferable basis for selecting D."
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
  "benchmark_sequence_length": 299,
  "benchmark_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "current_entry_audit": {
    "entryVersion": 75,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-04-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 299,
  "current_source_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 74,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A3MTR6",
  "selected_historical_entry_version": 74,
  "selected_historical_record_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "selected_historical_source_sequence_length": 299,
  "selected_historical_source_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "selected_historical_version": {
    "accession": "A3MTR6",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PGMI_PYRCJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A3MTR6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":75,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-04-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Thermoproteota\",\"Thermoprotei\",\"Thermoproteales\",\"Thermoproteaceae\",\"Pyrobaculum\"],\"scientificName\":\"Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1)\",\"taxonId\":410359}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Glucose-6-phosphate isomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"GPI\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Mannose-6-phosphate isomerase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.8\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional phosphoglucose/phosphomannose isomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Bifunctional PGI/PMI\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.3.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"name\":\"alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:11816\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57634\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58225\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.3.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"name\":\"D-mannose 6-phosphate = D-fructose 6-phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:12356\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58735\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61527\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Maqsood A.\",\"Shakir N.A.\",\"Aslam M.\",\"Rahman M.\",\"Rashid N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39208883\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijbiomac.2024.135127\"}],\"citationType\":\"journal article\",\"firstPage\":\"135127\",\"id\":\"39208883\",\"journal\":\"Int. J. Biol. Macromol.\",\"lastPage\":\"135127\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional investigations of Pcal_0606, a bifunctional phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.\",\"volume\":\"279\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 21063 / JCM 11548 / VA1\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H1",
  "excerpt": "ID   PGMI_PYRCJ              Reviewed;         299 AA.\nAC   A3MTR6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-APR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 74.\nDE   RecName: Full=Bifunctional phosphoglucose/phosphomannose isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=Bifunctional PGI/PMI {ECO:0000305};\nDE            EC=5.3.1.8 {ECO:0000269|PubMed:39208883};\nDE            EC=5.3.1.9 {ECO:0000269|PubMed:39208883};\nDE   AltName: Full=Glucose-6-phosphate isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=GPI {ECO:0000305};\nDE   AltName: Full=Mannose-6-phosphate isomerase {ECO:0000305};\nGN   OrderedLocusNames=Pcal_0606 {ECO:0000312|EMBL:ABO08033.1};\nOS   Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1).\nOC   Archaea; Thermoproteota; Thermoprotei; Thermoproteales; Thermoproteaceae;\nOC   Pyrobaculum.\nOX   NCBI_TaxID=410359;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Bifunctional phosphoglucose/phosphomannose isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=Bifunctional PGI/PMI {ECO:0000305};\nDE            EC=5.3.1.8 {ECO:0000269|PubMed:39208883};\nDE            EC=5.3.1.9 {ECO:0000269|PubMed:39208883};\nDE   AltName: Full=Glucose-6-phosphate isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=GPI {ECO:0000305};\nDE   AltName: Full=Mannose-6-phosphate isomerase {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 21063 / JCM 11548 / VA1;\nRX   PubMed=39208883; DOI=10.1016/j.ijbiomac.2024.135127;\nRA   Maqsood A., Shakir N.A., Aslam M., Rahman M., Rashid N.;\nRT   \"Structural and functional investigations of Pcal_0606, a bifunctional\nRT   phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.\";\nRL   Int. J. Biol. Macromol. 279:135127-135127(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate;\nCC         Xref=Rhea:RHEA:11816, ChEBI:CHEBI:57634, ChEBI:CHEBI:58225;\nCC         EC=5.3.1.9; Evidence={ECO:0000269|PubMed:39208883};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-mannose 6-phosphate = D-fructose 6-phosphate;\nCC         Xref=Rhea:RHEA:12356, ChEBI:CHEBI:58735, ChEBI:CHEBI:61527;\nCC         EC=5.3.1.8; Evidence={ECO:0000269|PubMed:39208883};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
