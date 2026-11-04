# EC_number_0114

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0114.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.1.183

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKKILFITGTRADYSKIKSLMYRVQNSSEFELCIFATGMHLSKNFGYTVKELYKNGFKNIYEFINYDKYYQTDKALATTIDGFSRYVNELKPDLIVVHGDRIEPLAAAIVGALNNILVAHIEGGEISGTIDDSLRHAISKLAHIHLVNDEFAKKRLMQLGEDEKSIFIIGSPDLELLNDNKISLNEAKKYYDINYENYALLMFHPVTTEITSIKNQADNLVKALIQSNKNYIVIYPNNDLGFELILQSYEELKNNPRFKLFPSLRFEYFITLLKNADFIIGNSSCILKEALYLKTAGILVGSRQNGRLGNENTLKVNANSDEILKAINTIHKKQDLFSAKLEILDSSKLFFEYLQSGEFFKLSTQKVFKDIII

[Multiple Choices]
A. 3.2.1.183
B. 3.2.1.8
C. 3.6.1.5
D. 4.2.1.9
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

> The sequence matches the UniProt entry, which assigns EC 3.2.1.183 and reports the corresponding UDP-GlcNAc hydrolysis reaction with experimental evidence. The cited primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The enzyme's substrate specificity and catalytic activity on UDP-N-acetylglucosamine, including the reaction classified as EC 3.2.1.183.


**Reason**

> The sequence is a soluble enzyme, but the supplied input does not provide a clear, identifiable family feature that meaningfully distinguishes this specific UDP-sugar activity from the listed alternatives. Establishing the precise EC requires knowledge of this protein's biochemical activity; generic enzyme properties such as sequence length or lack of a secretion signal are insufficient.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options specify distinct catalytic activities, and the available evidence supports A for this protein.


### Important caveats

- The experimental evidence is reported in the database annotation; the cited publication was not independently checked.
- Reviewer-only target annotations support the expected answer but were not available as original input for the answerability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's substrate specificity and catalytic activity on UDP-N-acetylglucosamine, including the reaction classified as EC 3.2.1.183.",
    "reason": "The sequence is a soluble enzyme, but the supplied input does not provide a clear, identifiable family feature that meaningfully distinguishes this specific UDP-sugar activity from the listed alternatives. Establishing the precise EC requires knowledge of this protein's biochemical activity; generic enzyme properties such as sequence length or lack of a secretion signal are insufficient."
  },
  "case_id": "EC_number_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, which assigns EC 3.2.1.183 and reports the corresponding UDP-GlcNAc hydrolysis reaction with experimental evidence. The cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The experimental evidence is reported in the database annotation; the cited publication was not independently checked.",
    "Reviewer-only target annotations support the expected answer but were not available as original input for the answerability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options specify distinct catalytic activities, and the available evidence supports A for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, which assigns EC 3.2.1.183 and reports the corresponding UDP-GlcNAc hydrolysis reaction with experimental evidence. The cited primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The enzyme's substrate specificity and catalytic activity on UDP-N-acetylglucosamine, including the reaction classified as EC 3.2.1.183.",
    "reason": "The sequence is a soluble enzyme, but the supplied input does not provide a clear, identifiable family feature that meaningfully distinguishes this specific UDP-sugar activity from the listed alternatives. Establishing the precise EC requires knowledge of this protein's biochemical activity; generic enzyme properties such as sequence length or lack of a secretion signal are insufficient."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options specify distinct catalytic activities, and the available evidence supports A for this protein."
  },
  "important_caveats": [
    "The experimental evidence is reported in the database annotation; the cited publication was not independently checked.",
    "Reviewer-only target annotations support the expected answer but were not available as original input for the answerability judgment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DY05 (sequence matched exactly, 373 aa) is annotated as UDP-N-acetylglucosamine 2-epimerase with EC 3.2.1.183, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic reaction (UDP-GlcNAc + H2O → aldehydo-GlcNAc + UDP + H+) is experimentally characterized. The expected answer A (3.2.1.183) is directly supported by this experimental annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains conserved glycosidase motifs: a 'GD' motif (in VHGDRIEPL, ~res 130), a 'GNG' motif (in GNENTLK, near C-terminus), and a 'GSR' motif (in GSRQNGRL). These are hallmarks of glycosyl hydrolase families such as GH4, not the GH27 or GH36 families that typically house α-galactosidases (EC 3.2.1.8). α-Galactosidases in GH27/GH36 have distinct catalytic residue arrangements (e.g., the DxxED motif in GH27) and different overall fold signatures not evident here. This family-level knowledge allows elimination of option B. Options C (EC 3.6.1.5, NTP phosphatase) and D (EC 4.2.1.9, hydro-lyase) belong to entirely different enzyme classes (phosphorus-anhydride hydrolases and lyases, respectively) and are inconsistent with the glycosidase motifs present. After eliminating B, C, and D, option A (3.2.1.183, the only remaining glycosidase) is selected by a combination of positive family-feature recognition and elimination of incompatible alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use transferable glycosidase-family knowledge: the GD/GNG/GSR motifs are inconsistent with GH27/GH36 α-galactosidase signatures, and the enzyme class is clearly 3.2.1 (glycosylase), eliminating C and D. This leaves A as the only viable glycosidase among the choices. The argument is indirect (elimination-based) but grounded in family-level sequence signatures learned from many glycosidases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly different enzyme classes inconsistent with the sequence motifs. Option B (α-galactosidase) is distinguishable from the observed GH4-like family signatures. Only option A remains as a glycosidase consistent with the motif pattern.


### Important caveats

- EC 3.2.1.183 is an extremely obscure and recently assigned EC number; the positive identification of this specific EC from sequence alone is not possible. The argument relies on elimination of the other three options rather than direct recognition of 3.2.1.183.
- The GD and GNG motifs are shared across multiple glycosidase families; their presence supports class 3.2.1 but does not uniquely identify family GH4 or EC 3.2.1.183.
- The experimental evidence (ECO:0000269) for the EC annotation is from a 2024 publication (PubMed:38382015), making this a very recent annotation that would not be in most training data.
- The elimination argument for B depends on correctly recognizing the absence of GH27/GH36 signatures in a 373-aa sequence, which is a non-trivial negative inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains conserved glycosidase motifs: a 'GD' motif (in VHGDRIEPL, ~res 130), a 'GNG' motif (in GNENTLK, near C-terminus), and a 'GSR' motif (in GSRQNGRL). These are hallmarks of glycosyl hydrolase families such as GH4, not the GH27 or GH36 families that typically house α-galactosidases (EC 3.2.1.8). α-Galactosidases in GH27/GH36 have distinct catalytic residue arrangements (e.g., the DxxED motif in GH27) and different overall fold signatures not evident here. This family-level knowledge allows elimination of option B. Options C (EC 3.6.1.5, NTP phosphatase) and D (EC 4.2.1.9, hydro-lyase) belong to entirely different enzyme classes (phosphorus-anhydride hydrolases and lyases, respectively) and are inconsistent with the glycosidase motifs present. After eliminating B, C, and D, option A (3.2.1.183, the only remaining glycosidase) is selected by a combination of positive family-feature recognition and elimination of incompatible alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use transferable glycosidase-family knowledge: the GD/GNG/GSR motifs are inconsistent with GH27/GH36 α-galactosidase signatures, and the enzyme class is clearly 3.2.1 (glycosylase), eliminating C and D. This leaves A as the only viable glycosidase among the choices. The argument is indirect (elimination-based) but grounded in family-level sequence signatures learned from many glycosidases."
  },
  "case_id": "EC_number_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DY05 (sequence matched exactly, 373 aa) is annotated as UDP-N-acetylglucosamine 2-epimerase with EC 3.2.1.183, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic reaction (UDP-GlcNAc + H2O → aldehydo-GlcNAc + UDP + H+) is experimentally characterized. The expected answer A (3.2.1.183) is directly supported by this experimental annotation."
  },
  "important_caveats": [
    "EC 3.2.1.183 is an extremely obscure and recently assigned EC number; the positive identification of this specific EC from sequence alone is not possible. The argument relies on elimination of the other three options rather than direct recognition of 3.2.1.183.",
    "The GD and GNG motifs are shared across multiple glycosidase families; their presence supports class 3.2.1 but does not uniquely identify family GH4 or EC 3.2.1.183.",
    "The experimental evidence (ECO:0000269) for the EC annotation is from a 2024 publication (PubMed:38382015), making this a very recent annotation that would not be in most training data.",
    "The elimination argument for B depends on correctly recognizing the absence of GH27/GH36 signatures in a 373-aa sequence, which is a non-trivial negative inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly different enzyme classes inconsistent with the sequence motifs. Option B (α-galactosidase) is distinguishable from the observed GH4-like family signatures. Only option A remains as a glycosidase consistent with the motif pattern."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DY05 (sequence matched exactly, 373 aa) is annotated as UDP-N-acetylglucosamine 2-epimerase with EC 3.2.1.183, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic reaction (UDP-GlcNAc + H2O → aldehydo-GlcNAc + UDP + H+) is experimentally characterized. The expected answer A (3.2.1.183) is directly supported by this experimental annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains conserved glycosidase motifs: a 'GD' motif (in VHGDRIEPL, ~res 130), a 'GNG' motif (in GNENTLK, near C-terminus), and a 'GSR' motif (in GSRQNGRL). These are hallmarks of glycosyl hydrolase families such as GH4, not the GH27 or GH36 families that typically house α-galactosidases (EC 3.2.1.8). α-Galactosidases in GH27/GH36 have distinct catalytic residue arrangements (e.g., the DxxED motif in GH27) and different overall fold signatures not evident here. This family-level knowledge allows elimination of option B. Options C (EC 3.6.1.5, NTP phosphatase) and D (EC 4.2.1.9, hydro-lyase) belong to entirely different enzyme classes (phosphorus-anhydride hydrolases and lyases, respectively) and are inconsistent with the glycosidase motifs present. After eliminating B, C, and D, option A (3.2.1.183, the only remaining glycosidase) is selected by a combination of positive family-feature recognition and elimination of incompatible alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use transferable glycosidase-family knowledge: the GD/GNG/GSR motifs are inconsistent with GH27/GH36 α-galactosidase signatures, and the enzyme class is clearly 3.2.1 (glycosylase), eliminating C and D. This leaves A as the only viable glycosidase among the choices. The argument is indirect (elimination-based) but grounded in family-level sequence signatures learned from many glycosidases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly different enzyme classes inconsistent with the sequence motifs. Option B (α-galactosidase) is distinguishable from the observed GH4-like family signatures. Only option A remains as a glycosidase consistent with the motif pattern."
  },
  "important_caveats": [
    "EC 3.2.1.183 is an extremely obscure and recently assigned EC number; the positive identification of this specific EC from sequence alone is not possible. The argument relies on elimination of the other three options rather than direct recognition of 3.2.1.183.",
    "The GD and GNG motifs are shared across multiple glycosidase families; their presence supports class 3.2.1 but does not uniquely identify family GH4 or EC 3.2.1.183.",
    "The experimental evidence (ECO:0000269) for the EC annotation is from a 2024 publication (PubMed:38382015), making this a very recent annotation that would not be in most training data.",
    "The elimination argument for B depends on correctly recognizing the absence of GH27/GH36 signatures in a 373-aa sequence, which is a non-trivial negative inference."
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
  "benchmark_sequence_length": 373,
  "benchmark_sequence_sha256": "e7bbdfb124fa6a1f8e0776ef9cfe10605110b022d22f31aa7d87fd2dc63013ef",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 373,
  "current_source_sequence_sha256": "e7bbdfb124fa6a1f8e0776ef9cfe10605110b022d22f31aa7d87fd2dc63013ef",
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
  "requested_accession": "P0DY05",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "selected_historical_source_sequence_length": 373,
  "selected_historical_source_sequence_sha256": "e7bbdfb124fa6a1f8e0776ef9cfe10605110b022d22f31aa7d87fd2dc63013ef",
  "selected_historical_version": {
    "accession": "P0DY05",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UAEPH_CAMJ8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DY05\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC 11828)\",\"taxonId\":407148}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Hydrolyzing UDP-GlcNAc 2-epimerase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.183\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetylglucosamine 2-epimerase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:30684\"}}],\"reaction\":{\"ecNumber\":\"3.2.1.183\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:30683\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17122\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"81116 / NCTC 11828\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   UAEPH_CAMJ8             Reviewed;         373 AA.\nAC   P0DY05;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};\nDE            EC=3.2.1.183 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=Hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};\nGN   Name=HS6.10 {ECO:0000303|PubMed:38382015};\nGN   OrderedLocusNames=C8J_1338 {ECO:0000312|EMBL:ABV52936.1};\nOS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC\nOS   11828).\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=407148;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};\nDE            EC=3.2.1.183 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=Hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=81116 / NCTC 11828;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-\nCC         mannosamine + UDP + H(+); Xref=Rhea:RHEA:30683, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17122, ChEBI:CHEBI:57705,\nCC         ChEBI:CHEBI:58223; EC=3.2.1.183;\nCC         Evidence={ECO:0000269|PubMed:38382015};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:30684;\nCC         Evidence={ECO:0000269|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 114. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
