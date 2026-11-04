# EC_number_0093

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0093.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 2.1.1.394

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTVPAARSGRKVYFIGLNAVPFLPLVAGLLRTYAEQDPRVAAGYDFQEPVFLVDGVQEMAAGITDPDVLALSCYVWNFRRQMKVARLVKERHPGMLVVAGGPHVPDRPGDFFARHPYVDVLVHGEGETAFRELLIERLADHPDYTRVPGVSVRHGTEAVPGRPAERLPRRIETPSPYLLGVMDGAVATCRQRDLRFYALWETNRGCPYSCAFCDWGSATMSALRLFDAERLQEEIEWFAEHDVEDLFVCDANFGILPRDLEIARALADARAATGAPKLIRVNFAKNSNDRVFEISKTWHDADLLMGTTLSMQSTDLDVLEAIDRKNIGLENYRKLQQRYATENIHTYTELILGLPLESPRSFRDGIGSLLEAGNHEDIRVYEFGILPNAPINTPEKIAGYGLRTVPKRLYVEEPGTPDDEAETVDMVMETNAMSRDEWVDCFGFVQAVQFLHNGCYTRYLSMYLRQRHDIGYTAFYERLQQYFGARPDTVLGSIYLRMRKLYHDYIDIPELPLANLVASQPDMAADLARYGKRRGWTIDNWGWLRIANDFERTYTELRDFVAALGVDDTSDPDLAEVFRFQQDVMLRPDYDPAAGRTTEYTADWPGYFTTGELRRRPVRMRLADQRFGANGRYTPVPGDLKAFARAAIGPSYPVSRIGHYRHRFEAAEVTSPAEPVLTEQR

[Multiple Choices]
A. 2.1.1.394
B. 2.1.1.393
C. 3.2.1.8
D. 3.1.1.4
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

> The sequence matches the UniProt entry whose recommended EC number is 2.1.1.394. The entry cites experimental evidence for that assignment and describes methylation reactions consistent with the EC number.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying a specialized methyltransferase, which favors the methyltransferase choices over the hydrolases. But that broad inference does not distinguish A from B: both are closely related EC classifications within EC 2.1.1.


**Missing item-specific fact**

> The exact substrate and reaction specificity needed to distinguish EC 2.1.1.394 from EC 2.1.1.393.


**Reason**

> The sequence alone, without pathway or substrate context, does not provide a concrete transferable feature that resolves the fine distinction between the two methyltransferase options. The exact EC assignment depends on protein-specific functional characterization or an annotation derived from it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The EC choices denote distinct reactions, so only one may be correct for the protein; the issue is that the original input does not establish which of the two methyltransferase reactions it performs.


### Important caveats

- The cited UniProt record matches the supplied sequence, but the author’s exact source snapshot is unknown.
- The evidence includes experimental evidence codes, although the underlying publications were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying a specialized methyltransferase, which favors the methyltransferase choices over the hydrolases. But that broad inference does not distinguish A from B: both are closely related EC classifications within EC 2.1.1.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact substrate and reaction specificity needed to distinguish EC 2.1.1.394 from EC 2.1.1.393.",
    "reason": "The sequence alone, without pathway or substrate context, does not provide a concrete transferable feature that resolves the fine distinction between the two methyltransferase options. The exact EC assignment depends on protein-specific functional characterization or an annotation derived from it."
  },
  "case_id": "EC_number_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry whose recommended EC number is 2.1.1.394. The entry cites experimental evidence for that assignment and describes methylation reactions consistent with the EC number."
  },
  "important_caveats": [
    "The cited UniProt record matches the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The evidence includes experimental evidence codes, although the underlying publications were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC choices denote distinct reactions, so only one may be correct for the protein; the issue is that the original input does not establish which of the two methyltransferase reactions it performs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry whose recommended EC number is 2.1.1.394. The entry cites experimental evidence for that assignment and describes methylation reactions consistent with the EC number.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying a specialized methyltransferase, which favors the methyltransferase choices over the hydrolases. But that broad inference does not distinguish A from B: both are closely related EC classifications within EC 2.1.1.",
    "missing_item_specific_fact": "The exact substrate and reaction specificity needed to distinguish EC 2.1.1.394 from EC 2.1.1.393.",
    "reason": "The sequence alone, without pathway or substrate context, does not provide a concrete transferable feature that resolves the fine distinction between the two methyltransferase options. The exact EC assignment depends on protein-specific functional characterization or an annotation derived from it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC choices denote distinct reactions, so only one may be correct for the protein; the issue is that the original input does not establish which of the two methyltransferase reactions it performs."
  },
  "important_caveats": [
    "The cited UniProt record matches the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The evidence includes experimental evidence codes, although the underlying publications were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q83XP3 (sequence matched, 681 aa) annotates this protein as 2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase with EC 2.1.1.394, supported by experimental evidence (ECO:0000269) from three independent PubMed publications (26240322, 31774078, 36042702). The catalytic activity describes consecutive radical SAM methylations forming the ethyl side chain in thienamycin biosynthesis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the canonical radical SAM CX3CX2C motif (CPYSCAFC region), which reliably identifies this as a radical SAM enzyme and, in the context of SAM-dependent methyl transfer, a methyltransferase (EC 2.1.1.x). This eliminates options C (3.2.1.8, beta-glucosidase) and D (3.1.1.4, phospholipase A2) by family-level reasoning. However, options A (2.1.1.394, ThnK) and B (2.1.1.393, TokK) are both cobalamin-dependent radical SAM methyltransferases performing nearly identical methyl-transfer reactions on carbapenam intermediates in different carbapenem biosynthetic pathways (thienamycin vs. tokaramycin). No transferable family-level, mechanistic, or sequence-feature argument distinguishes these two EC numbers: they belong to the same enzyme family, use the same cofactors (SAM, cobalamin, &#91;4Fe-4S&#93;), catalyze the same reaction type, and differ only in the specific biosynthetic pathway/organism from which the EC number was assigned. Distinguishing 394 from 393 requires knowing the specific database annotation for this exact sequence.


**Missing item-specific fact**

> The specific EC number assignment (2.1.1.394 vs. 2.1.1.393) for this exact protein sequence, which depends on knowing the organism (Streptomyces cattleya vs. Streptomyces tokaraensis) and the specific carbapenem biosynthetic pathway (thienamycin vs. tokaramycin), information not derivable from the sequence alone through transferable family knowledge.


**Reason**

> While the radical SAM motif allows elimination of hydrolase options C and D through legitimate family recognition, the critical distinction between the two methyltransferase options (A and B) cannot be made by transferable knowledge. Both are homologous cobalamin-dependent radical SAM methyltransferases with the same reaction chemistry; the EC number difference is pathway/organism-specific and requires the exact database annotation for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 2.1.1.394 and 2.1.1.393 describe cobalamin-dependent radical SAM methyltransferases catalyzing methyl transfer on carbapenam intermediates. Without organism or pathway context provided in the question, a knowledgeable model cannot determine from the sequence alone which specific EC number applies, as both represent the same enzyme class performing the same reaction type.


### Important caveats

- The radical SAM CX3CX2C motif in the sequence is a legitimate transferable feature that eliminates hydrolase distractors (C, D).
- The A vs B distinction is essentially an organism/pathway-level annotation choice between two homologous enzymes, not a mechanistic or functional class distinction.
- The EC number 2.1.1.394 was assigned based on experimental characterization (2015-2022 publications); the historical annotation timeline means this EC number may not have existed when the benchmark was constructed.
- The sequence matches Q83XP3 exactly (681 aa, SHA256 confirmed), but the accession and organism were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical radical SAM CX3CX2C motif (CPYSCAFC region), which reliably identifies this as a radical SAM enzyme and, in the context of SAM-dependent methyl transfer, a methyltransferase (EC 2.1.1.x). This eliminates options C (3.2.1.8, beta-glucosidase) and D (3.1.1.4, phospholipase A2) by family-level reasoning. However, options A (2.1.1.394, ThnK) and B (2.1.1.393, TokK) are both cobalamin-dependent radical SAM methyltransferases performing nearly identical methyl-transfer reactions on carbapenam intermediates in different carbapenem biosynthetic pathways (thienamycin vs. tokaramycin). No transferable family-level, mechanistic, or sequence-feature argument distinguishes these two EC numbers: they belong to the same enzyme family, use the same cofactors (SAM, cobalamin, [4Fe-4S]), catalyze the same reaction type, and differ only in the specific biosynthetic pathway/organism from which the EC number was assigned. Distinguishing 394 from 393 requires knowing the specific database annotation for this exact sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific EC number assignment (2.1.1.394 vs. 2.1.1.393) for this exact protein sequence, which depends on knowing the organism (Streptomyces cattleya vs. Streptomyces tokaraensis) and the specific carbapenem biosynthetic pathway (thienamycin vs. tokaramycin), information not derivable from the sequence alone through transferable family knowledge.",
    "reason": "While the radical SAM motif allows elimination of hydrolase options C and D through legitimate family recognition, the critical distinction between the two methyltransferase options (A and B) cannot be made by transferable knowledge. Both are homologous cobalamin-dependent radical SAM methyltransferases with the same reaction chemistry; the EC number difference is pathway/organism-specific and requires the exact database annotation for this protein."
  },
  "case_id": "EC_number_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q83XP3 (sequence matched, 681 aa) annotates this protein as 2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase with EC 2.1.1.394, supported by experimental evidence (ECO:0000269) from three independent PubMed publications (26240322, 31774078, 36042702). The catalytic activity describes consecutive radical SAM methylations forming the ethyl side chain in thienamycin biosynthesis."
  },
  "important_caveats": [
    "The radical SAM CX3CX2C motif in the sequence is a legitimate transferable feature that eliminates hydrolase distractors (C, D).",
    "The A vs B distinction is essentially an organism/pathway-level annotation choice between two homologous enzymes, not a mechanistic or functional class distinction.",
    "The EC number 2.1.1.394 was assigned based on experimental characterization (2015-2022 publications); the historical annotation timeline means this EC number may not have existed when the benchmark was constructed.",
    "The sequence matches Q83XP3 exactly (681 aa, SHA256 confirmed), but the accession and organism were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 2.1.1.394 and 2.1.1.393 describe cobalamin-dependent radical SAM methyltransferases catalyzing methyl transfer on carbapenam intermediates. Without organism or pathway context provided in the question, a knowledgeable model cannot determine from the sequence alone which specific EC number applies, as both represent the same enzyme class performing the same reaction type."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q83XP3 (sequence matched, 681 aa) annotates this protein as 2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase with EC 2.1.1.394, supported by experimental evidence (ECO:0000269) from three independent PubMed publications (26240322, 31774078, 36042702). The catalytic activity describes consecutive radical SAM methylations forming the ethyl side chain in thienamycin biosynthesis.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the canonical radical SAM CX3CX2C motif (CPYSCAFC region), which reliably identifies this as a radical SAM enzyme and, in the context of SAM-dependent methyl transfer, a methyltransferase (EC 2.1.1.x). This eliminates options C (3.2.1.8, beta-glucosidase) and D (3.1.1.4, phospholipase A2) by family-level reasoning. However, options A (2.1.1.394, ThnK) and B (2.1.1.393, TokK) are both cobalamin-dependent radical SAM methyltransferases performing nearly identical methyl-transfer reactions on carbapenam intermediates in different carbapenem biosynthetic pathways (thienamycin vs. tokaramycin). No transferable family-level, mechanistic, or sequence-feature argument distinguishes these two EC numbers: they belong to the same enzyme family, use the same cofactors (SAM, cobalamin, [4Fe-4S]), catalyze the same reaction type, and differ only in the specific biosynthetic pathway/organism from which the EC number was assigned. Distinguishing 394 from 393 requires knowing the specific database annotation for this exact sequence.",
    "missing_item_specific_fact": "The specific EC number assignment (2.1.1.394 vs. 2.1.1.393) for this exact protein sequence, which depends on knowing the organism (Streptomyces cattleya vs. Streptomyces tokaraensis) and the specific carbapenem biosynthetic pathway (thienamycin vs. tokaramycin), information not derivable from the sequence alone through transferable family knowledge.",
    "reason": "While the radical SAM motif allows elimination of hydrolase options C and D through legitimate family recognition, the critical distinction between the two methyltransferase options (A and B) cannot be made by transferable knowledge. Both are homologous cobalamin-dependent radical SAM methyltransferases with the same reaction chemistry; the EC number difference is pathway/organism-specific and requires the exact database annotation for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 2.1.1.394 and 2.1.1.393 describe cobalamin-dependent radical SAM methyltransferases catalyzing methyl transfer on carbapenam intermediates. Without organism or pathway context provided in the question, a knowledgeable model cannot determine from the sequence alone which specific EC number applies, as both represent the same enzyme class performing the same reaction type."
  },
  "important_caveats": [
    "The radical SAM CX3CX2C motif in the sequence is a legitimate transferable feature that eliminates hydrolase distractors (C, D).",
    "The A vs B distinction is essentially an organism/pathway-level annotation choice between two homologous enzymes, not a mechanistic or functional class distinction.",
    "The EC number 2.1.1.394 was assigned based on experimental characterization (2015-2022 publications); the historical annotation timeline means this EC number may not have existed when the benchmark was constructed.",
    "The sequence matches Q83XP3 exactly (681 aa, SHA256 confirmed), but the accession and organism were not provided to the evaluated model."
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
  "benchmark_sequence_length": 681,
  "benchmark_sequence_sha256": "9af3f057a63063df67b1505a5dd7494c95280d99f3fa45c9786ad221469f52c2",
  "current_entry_audit": {
    "entryVersion": 76,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 681,
  "current_source_sequence_sha256": "9af3f057a63063df67b1505a5dd7494c95280d99f3fa45c9786ad221469f52c2",
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
  "requested_accession": "Q83XP3",
  "selected_historical_entry_version": 74,
  "selected_historical_record_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "selected_historical_source_sequence_length": 681,
  "selected_historical_source_sequence_sha256": "9af3f057a63063df67b1505a5dd7494c95280d99f3fa45c9786ad221469f52c2",
  "selected_historical_version": {
    "accession": "Q83XP3",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "THNK_STREN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q83XP3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":76,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Streptomyces cattleya\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptantibioticus\"],\"scientificName\":\"Streptantibioticus cattleyicolor (strain ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NRRL 8057)\",\"taxonId\":1003195}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26240322\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31774078\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36042702\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.394\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26240322\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79660\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.394\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26240322\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31774078\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36042702\",\"source\":\"PubMed\"}],\"name\":\"(2R,3R,5R)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79659\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17319\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57844\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230520\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230521\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26240322\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79664\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.394\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26240322\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31774078\",\"source\":\"PubMed\"}],\"name\":\"(2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(ethyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79663\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17319\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57844\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230521\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230522\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Marous D.R.\",\"Lloyd E.P.\",\"Buller A.R.\",\"Moshos K.A.\",\"Grove T.L.\",\"Blaszczyk A.J.\",\"Booker S.J.\",\"Townsend C.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26240322\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1508615112\"}],\"citationType\":\"journal article\",\"firstPage\":\"10354\",\"id\":\"26240322\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"10358\",\"publicationDate\":\"2015\",\"title\":\"Consecutive radical S-adenosylmethionine methylations form the ethyl side chain in thienamycin biosynthesis.\",\"volume\":\"112\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NCIMB 11928 / NRRL 8057 / MA-4297\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Sinner E.K.\",\"Lichstrahl M.S.\",\"Li R.\",\"Marous D.R.\",\"Townsend C.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31774078\"},{\"database\":\"DOI\",\"id\":\"10.1039/c9cc07197k\"}],\"citationType\":\"journal article\",\"firstPage\":\"14934\",\"id\":\"31774078\",\"journal\":\"Chem. Commun. (Camb.)\",\"lastPage\":\"14937\",\"publicationDate\":\"2019\",\"title\":\"Methylations in complex carbapenem biosynthesis are catalyzed by a single cobalamin-dependent radical S-adenosylmethionine enzyme.\",\"volume\":\"55\"},\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Lichstrahl M.S.\",\"Townsend C.A.\",\"Sinner E.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36042702\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2cb00113f\"}],\"citationType\":\"journal article\",\"firstPage\":\"1028\",\"id\":\"36042702\",\"journal\":\"RSC Chem. Biol.\",\"lastPage\":\"1034\",\"publicationDate\":\"2022\",\"title\":\"Stereochemical course of cobalamin-dependent radical SAM methylation by TokK and ThnK.\",\"volume\":\"3\"},\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"REACTION MECHANISM FOR THE FIRST METHYLATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H1",
  "excerpt": "ID   THNK_STREN              Reviewed;         681 AA.\nAC   Q83XP3; F8JND9; G8XDF2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2003, sequence version 1.\nDT   28-JAN-2026, entry version 74.\nDE   RecName: Full=2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase {ECO:0000305};\nDE            EC=2.1.1.394 {ECO:0000269|PubMed:26240322, ECO:0000269|PubMed:31774078, ECO:0000269|PubMed:36042702};\nGN   Name=thnK {ECO:0000303|PubMed:12725858};\nGN   OrderedLocusNames=SCATT_p09050 {ECO:0000312|EMBL:AEW99098.1};\nOS   Streptantibioticus cattleyicolor (strain ATCC 35852 / DSM 46488 / JCM 4925\nOS   / NBRC 14057 / NRRL 8057) (Streptomyces cattleya).\nOG   Plasmid pSCATT {ECO:0000312|EMBL:AEW99098.1}.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptantibioticus.\nOX   NCBI_TaxID=1003195;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase {ECO:0000305};\nDE            EC=2.1.1.394 {ECO:0000269|PubMed:26240322, ECO:0000269|PubMed:31774078, ECO:0000269|PubMed:36042702};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAD18979.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND GENE CLUSTER.\nRC   STRAIN=ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NCIMB 11928 / NRRL\nRC   8057 / MA-4297;\nRX   PubMed=12725858; DOI=10.1016/s1074-5521(03)00069-3;\nRA   Nunez L.E., Mendez C., Brana A.F., Blanco G., Salas J.A.;\nRT   \"The biosynthetic gene cluster for the beta-lactam carbapenem thienamycin\nRT   in Streptomyces cattleya.\";\nRL   Chem. Biol. 10:301-311(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H4",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, AND PATHWAY.\nRC   STRAIN=ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NCIMB 11928 / NRRL\nRC   8057 / MA-4297;\nRX   PubMed=26240322; DOI=10.1073/pnas.1508615112;\nRA   Marous D.R., Lloyd E.P., Buller A.R., Moshos K.A., Grove T.L.,\nRA   Blaszczyk A.J., Booker S.J., Townsend C.A.;\nRT   \"Consecutive radical S-adenosylmethionine methylations form the ethyl side\nRT   chain in thienamycin biosynthesis.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 112:10354-10358(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H5",
  "excerpt": "RN   [5]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=31774078; DOI=10.1039/c9cc07197k;\nRA   Sinner E.K., Lichstrahl M.S., Li R., Marous D.R., Townsend C.A.;\nRT   \"Methylations in complex carbapenem biosynthesis are catalyzed by a single\nRT   cobalamin-dependent radical S-adenosylmethionine enzyme.\";\nRL   Chem. Commun. (Camb.) 55:14934-14937(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H6",
  "excerpt": "RN   [6]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND REACTION MECHANISM FOR THE FIRST\nRP   METHYLATION.\nRX   PubMed=36042702; DOI=10.1039/d2cb00113f;\nRA   Lichstrahl M.S., Townsend C.A., Sinner E.K.;\nRT   \"Stereochemical course of cobalamin-dependent radical SAM methylation by\nRT   TokK and ThnK.\";\nRL   RSC Chem. Biol. 3:1028-1034(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R,3R,5R)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 +\nCC         2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(methyl)-2-(S-\nCC         pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-\nCC         methionine + A + S-adenosyl-L-homocysteine + 2 H(+);\nCC         Xref=Rhea:RHEA:79659, ChEBI:CHEBI:13193, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:17319, ChEBI:CHEBI:17499, ChEBI:CHEBI:57844,\nCC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:230520,\nCC         ChEBI:CHEBI:230521; EC=2.1.1.394;\nCC         Evidence={ECO:0000269|PubMed:26240322, ECO:0000269|PubMed:31774078,\nCC         ECO:0000269|PubMed:36042702};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79660;\nCC         Evidence={ECO:0000269|PubMed:26240322};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-\nCC         carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-\nCC         (ethyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-\nCC         deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2\nCC         H(+); Xref=Rhea:RHEA:79663, ChEBI:CHEBI:13193, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:17319, ChEBI:CHEBI:17499, ChEBI:CHEBI:57844,\nCC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:230521,\nCC         ChEBI:CHEBI:230522; EC=2.1.1.394;\nCC         Evidence={ECO:0000269|PubMed:26240322, ECO:0000269|PubMed:31774078};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79664;\nCC         Evidence={ECO:0000269|PubMed:26240322};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
