# EC_number_0036

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0036.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 1.1.1.12

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVKPTKSNIGVYTNPAHDLWVAEAEPSLEQVQTGEKLAPGEVTVAVKSTGICGSDVHFWHAGCIGPMIVEDDHILGHESAGVVVAVHENVKSLKVGDRVAIEPNIICGECEPCLTGRYNGCDSVLFRSTPPVPGLLRRYVNHPAMWCHKIGDMSYENGSLLEPLSVALAGVQRAEVRLGDPILVCGAGPIGLVTLACVKAAGAEPIIITDIDEGRLAFAKEFCPSVRTHKVDFKHTPEDFAKAITELGGGVEPAIALECTGVESSIAGAIQTVKFGGKVFVIGVGKNEIKIPFMRLSTREVDLQFQYRYANTWPRAIRLLQGGVINLEKLVTHRFKIEDALEAFKTAADPKTGAIKVQIQSFEEGESR

[Multiple Choices]
A. 1.1.1.12
B. 1.1.1.336
C. 2.3.1.318
D. 2.3.1.319
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

> The exact sequence matches the UniProt entry annotated as L-arabinitol 4-dehydrogenase, EC 1.1.1.12. The annotation and catalytic reaction are supported by evidence transferred from another UniProt protein (ECO:0000250), not by direct experimental evidence for this sequence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a dehydrogenase, which can distinguish the 1.1.1 choices from the 2.3.1 acyltransferase choices. However, that broad classification does not distinguish A from B, which are both dehydrogenase ECs.


**Missing item-specific fact**

> The substrate specificity needed to distinguish EC 1.1.1.12 from EC 1.1.1.336, such as a reliable match to a characterized homolog with that specificity.


**Reason**

> The key’s specific EC assignment is supportable by a homology-transferred annotation, but the original sequence and options alone provide no identified feature that meaningfully resolves the remaining dehydrogenase alternatives. The reviewer-only annotation cannot be treated as input to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports A; no evidence establishes another option as an equally defensible EC assignment.


### Important caveats

- The source annotation is computationally transferred rather than direct experimental evidence for the matched sequence.
- The author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a dehydrogenase, which can distinguish the 1.1.1 choices from the 2.3.1 acyltransferase choices. However, that broad classification does not distinguish A from B, which are both dehydrogenase ECs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The substrate specificity needed to distinguish EC 1.1.1.12 from EC 1.1.1.336, such as a reliable match to a characterized homolog with that specificity.",
    "reason": "The key’s specific EC assignment is supportable by a homology-transferred annotation, but the original sequence and options alone provide no identified feature that meaningfully resolves the remaining dehydrogenase alternatives. The reviewer-only annotation cannot be treated as input to the evaluated model."
  },
  "case_id": "EC_number_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as L-arabinitol 4-dehydrogenase, EC 1.1.1.12. The annotation and catalytic reaction are supported by evidence transferred from another UniProt protein (ECO:0000250), not by direct experimental evidence for this sequence in the supplied excerpts."
  },
  "important_caveats": [
    "The source annotation is computationally transferred rather than direct experimental evidence for the matched sequence.",
    "The author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A; no evidence establishes another option as an equally defensible EC assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as L-arabinitol 4-dehydrogenase, EC 1.1.1.12. The annotation and catalytic reaction are supported by evidence transferred from another UniProt protein (ECO:0000250), not by direct experimental evidence for this sequence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a dehydrogenase, which can distinguish the 1.1.1 choices from the 2.3.1 acyltransferase choices. However, that broad classification does not distinguish A from B, which are both dehydrogenase ECs.",
    "missing_item_specific_fact": "The substrate specificity needed to distinguish EC 1.1.1.12 from EC 1.1.1.336, such as a reliable match to a characterized homolog with that specificity.",
    "reason": "The key’s specific EC assignment is supportable by a homology-transferred annotation, but the original sequence and options alone provide no identified feature that meaningfully resolves the remaining dehydrogenase alternatives. The reviewer-only annotation cannot be treated as input to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A; no evidence establishes another option as an equally defensible EC assignment."
  },
  "important_caveats": [
    "The source annotation is computationally transferred rather than direct experimental evidence for the matched sequence.",
    "The author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A385XI11) annotates this protein as L-arabinitol 4-dehydrogenase with EC 1.1.1.12. The EC assignment is by similarity (ECO:0000250 to Q7SI09), but the protein name and short name are supported by experimental evidence from PubMed 32003433 (liamocin biosynthesis in Aureobasidium melanogenum). The catalytic activity (L-arabinitol + NAD+ = L-xylulose + NADH + H+) is consistent with EC 1.1.1.12. The annotation is computational transfer rather than direct assay of this exact protein, but the functional context from the liamocin pathway paper provides experimental backing.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD-binding motif (GAGPIGLVTLACVKAAGAEPIIITDIDEGRLAFAKEF) and multiple zinc-coordinating cysteines (CGECEPCLTGRYNGCDS...CHKIG), identifying it as a zinc-dependent alcohol dehydrogenase (ADH) family member. This immediately eliminates EC 2.x.x.x transferases (C, D), which lack NAD-binding Rossmann folds and zinc-ADH architecture. Between the two remaining oxidoreductase options (1.1.1.12 vs 1.1.1.336), both act on L-arabinitol with NAD+ but differ in regioselectivity (C4 vs C2 oxidation). In fungal zinc-ADH enzymes involved in L-arabinitol metabolism (e.g., Candida, Trichosporon, and related Dothideomycetes), the characterized enzymes with this zinc-ADH architecture are predominantly L-arabinitol 4-dehydrogenases (EC 1.1.1.12). EC 1.1.1.336 (L-arabinitol 2-dehydrogenase) is an extremely rare entry with very few characterized examples. The combination of (a) zinc-ADH family membership, (b) fungal context, and (c) the statistical predominance of 4-dehydrogenase activity among characterized fungal L-arabinitol dehydrogenases provides a transferable, family-level inference favoring EC 1.1.1.12 over EC 1.1.1.336.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The EC 1 vs EC 2 distinction is clearly supported by the Rossmann fold and zinc-binding motifs in the sequence. The 1.1.1.12 vs 1.1.1.336 distinction relies on family-level statistical knowledge that fungal zinc-ADH enzymes acting on L-arabinitol are overwhelmingly 4-dehydrogenases, which is a legitimate transferable pattern learned from characterized homologs in other fungal species. While the C4-vs-C2 regioselectivity is a fine distinction, the family-level association and the extreme rarity of EC 1.1.1.336 provide a meaningful probabilistic basis for selecting A over B without requiring the exact recorded annotation for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D (transferases) are clearly eliminated by the NAD-binding Rossmann fold and zinc-ADH architecture. The distinction between A and B is fine but the family-level evidence (zinc-ADH → 4-dehydrogenase in fungi; rarity of EC 1.1.1.336) provides a clear preference for A. No other option is genuinely defensible given the sequence features.


### Important caveats

- The EC 1.1.1.12 annotation in UniProt is by computational similarity (ECO:0000250 to Q7SI09), not by direct enzymatic assay of this exact protein, though the liamocin pathway paper (PubMed 32003433) provides experimental functional context.
- The distinction between EC 1.1.1.12 (C4 oxidation) and EC 1.1.1.336 (C2 oxidation) is extremely fine and relies on family-level statistical patterns rather than a clear sequence motif that encodes regioselectivity.
- EC 1.1.1.336 is an extremely rare EC number with very few characterized examples, making it a weak distractor in practice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD-binding motif (GAGPIGLVTLACVKAAGAEPIIITDIDEGRLAFAKEF) and multiple zinc-coordinating cysteines (CGECEPCLTGRYNGCDS...CHKIG), identifying it as a zinc-dependent alcohol dehydrogenase (ADH) family member. This immediately eliminates EC 2.x.x.x transferases (C, D), which lack NAD-binding Rossmann folds and zinc-ADH architecture. Between the two remaining oxidoreductase options (1.1.1.12 vs 1.1.1.336), both act on L-arabinitol with NAD+ but differ in regioselectivity (C4 vs C2 oxidation). In fungal zinc-ADH enzymes involved in L-arabinitol metabolism (e.g., Candida, Trichosporon, and related Dothideomycetes), the characterized enzymes with this zinc-ADH architecture are predominantly L-arabinitol 4-dehydrogenases (EC 1.1.1.12). EC 1.1.1.336 (L-arabinitol 2-dehydrogenase) is an extremely rare entry with very few characterized examples. The combination of (a) zinc-ADH family membership, (b) fungal context, and (c) the statistical predominance of 4-dehydrogenase activity among characterized fungal L-arabinitol dehydrogenases provides a transferable, family-level inference favoring EC 1.1.1.12 over EC 1.1.1.336.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The EC 1 vs EC 2 distinction is clearly supported by the Rossmann fold and zinc-binding motifs in the sequence. The 1.1.1.12 vs 1.1.1.336 distinction relies on family-level statistical knowledge that fungal zinc-ADH enzymes acting on L-arabinitol are overwhelmingly 4-dehydrogenases, which is a legitimate transferable pattern learned from characterized homologs in other fungal species. While the C4-vs-C2 regioselectivity is a fine distinction, the family-level association and the extreme rarity of EC 1.1.1.336 provide a meaningful probabilistic basis for selecting A over B without requiring the exact recorded annotation for this protein."
  },
  "case_id": "EC_number_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A385XI11) annotates this protein as L-arabinitol 4-dehydrogenase with EC 1.1.1.12. The EC assignment is by similarity (ECO:0000250 to Q7SI09), but the protein name and short name are supported by experimental evidence from PubMed 32003433 (liamocin biosynthesis in Aureobasidium melanogenum). The catalytic activity (L-arabinitol + NAD+ = L-xylulose + NADH + H+) is consistent with EC 1.1.1.12. The annotation is computational transfer rather than direct assay of this exact protein, but the functional context from the liamocin pathway paper provides experimental backing."
  },
  "important_caveats": [
    "The EC 1.1.1.12 annotation in UniProt is by computational similarity (ECO:0000250 to Q7SI09), not by direct enzymatic assay of this exact protein, though the liamocin pathway paper (PubMed 32003433) provides experimental functional context.",
    "The distinction between EC 1.1.1.12 (C4 oxidation) and EC 1.1.1.336 (C2 oxidation) is extremely fine and relies on family-level statistical patterns rather than a clear sequence motif that encodes regioselectivity.",
    "EC 1.1.1.336 is an extremely rare EC number with very few characterized examples, making it a weak distractor in practice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D (transferases) are clearly eliminated by the NAD-binding Rossmann fold and zinc-ADH architecture. The distinction between A and B is fine but the family-level evidence (zinc-ADH → 4-dehydrogenase in fungi; rarity of EC 1.1.1.336) provides a clear preference for A. No other option is genuinely defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A385XI11) annotates this protein as L-arabinitol 4-dehydrogenase with EC 1.1.1.12. The EC assignment is by similarity (ECO:0000250 to Q7SI09), but the protein name and short name are supported by experimental evidence from PubMed 32003433 (liamocin biosynthesis in Aureobasidium melanogenum). The catalytic activity (L-arabinitol + NAD+ = L-xylulose + NADH + H+) is consistent with EC 1.1.1.12. The annotation is computational transfer rather than direct assay of this exact protein, but the functional context from the liamocin pathway paper provides experimental backing.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD-binding motif (GAGPIGLVTLACVKAAGAEPIIITDIDEGRLAFAKEF) and multiple zinc-coordinating cysteines (CGECEPCLTGRYNGCDS...CHKIG), identifying it as a zinc-dependent alcohol dehydrogenase (ADH) family member. This immediately eliminates EC 2.x.x.x transferases (C, D), which lack NAD-binding Rossmann folds and zinc-ADH architecture. Between the two remaining oxidoreductase options (1.1.1.12 vs 1.1.1.336), both act on L-arabinitol with NAD+ but differ in regioselectivity (C4 vs C2 oxidation). In fungal zinc-ADH enzymes involved in L-arabinitol metabolism (e.g., Candida, Trichosporon, and related Dothideomycetes), the characterized enzymes with this zinc-ADH architecture are predominantly L-arabinitol 4-dehydrogenases (EC 1.1.1.12). EC 1.1.1.336 (L-arabinitol 2-dehydrogenase) is an extremely rare entry with very few characterized examples. The combination of (a) zinc-ADH family membership, (b) fungal context, and (c) the statistical predominance of 4-dehydrogenase activity among characterized fungal L-arabinitol dehydrogenases provides a transferable, family-level inference favoring EC 1.1.1.12 over EC 1.1.1.336.",
    "missing_item_specific_fact": "",
    "reason": "The EC 1 vs EC 2 distinction is clearly supported by the Rossmann fold and zinc-binding motifs in the sequence. The 1.1.1.12 vs 1.1.1.336 distinction relies on family-level statistical knowledge that fungal zinc-ADH enzymes acting on L-arabinitol are overwhelmingly 4-dehydrogenases, which is a legitimate transferable pattern learned from characterized homologs in other fungal species. While the C4-vs-C2 regioselectivity is a fine distinction, the family-level association and the extreme rarity of EC 1.1.1.336 provide a meaningful probabilistic basis for selecting A over B without requiring the exact recorded annotation for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D (transferases) are clearly eliminated by the NAD-binding Rossmann fold and zinc-ADH architecture. The distinction between A and B is fine but the family-level evidence (zinc-ADH → 4-dehydrogenase in fungi; rarity of EC 1.1.1.336) provides a clear preference for A. No other option is genuinely defensible given the sequence features."
  },
  "important_caveats": [
    "The EC 1.1.1.12 annotation in UniProt is by computational similarity (ECO:0000250 to Q7SI09), not by direct enzymatic assay of this exact protein, though the liamocin pathway paper (PubMed 32003433) provides experimental functional context.",
    "The distinction between EC 1.1.1.12 (C4 oxidation) and EC 1.1.1.336 (C2 oxidation) is extremely fine and relies on family-level statistical patterns rather than a clear sequence motif that encodes regioselectivity.",
    "EC 1.1.1.336 is an extremely rare EC number with very few characterized examples, making it a weak distractor in practice."
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
  "benchmark_sequence_length": 368,
  "benchmark_sequence_sha256": "b6243c25f76bd5341c3276e5e72351d95b636da19da05dae2fa407490c6e3c1c",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-12-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 368,
  "current_source_sequence_sha256": "b6243c25f76bd5341c3276e5e72351d95b636da19da05dae2fa407490c6e3c1c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 21,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A385XI11",
  "selected_historical_entry_version": 21,
  "selected_historical_record_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "selected_historical_source_sequence_length": 368,
  "selected_historical_source_sequence_sha256": "b6243c25f76bd5341c3276e5e72351d95b636da19da05dae2fa407490c6e3c1c",
  "selected_historical_version": {
    "accession": "A0A385XI11",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "LAD_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A385XI11\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-12-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7SI09\",\"source\":\"UniProtKB\"}],\"value\":\"1.1.1.12\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"L-arabinitol 4-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"ArDH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.1.1.12\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7SI09\",\"source\":\"UniProtKB\"}],\"name\":\"L-arabinitol + NAD(+) = L-xylulose + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:16381\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17399\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:18403\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI11.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:25:01.614534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c0f4e12f3c5638b0c24763ce28172b6f2345a6e21ca287d93bc736545c524a59",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI11.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H1",
  "excerpt": "ID   LAD_AURME               Reviewed;         368 AA.\nAC   A0A385XI11;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-DEC-2018, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=L-arabinitol 4-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=ArDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.12 {ECO:0000250|UniProtKB:Q7SI09};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=L-arabinitol 4-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=ArDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.12 {ECO:0000250|UniProtKB:Q7SI09};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-arabinitol + NAD(+) = L-xylulose + NADH + H(+);\nCC         Xref=Rhea:RHEA:16381, ChEBI:CHEBI:15378, ChEBI:CHEBI:17399,\nCC         ChEBI:CHEBI:18403, ChEBI:CHEBI:57540, ChEBI:CHEBI:57945; EC=1.1.1.12;\nCC         Evidence={ECO:0000250|UniProtKB:Q7SI09};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:08.764058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c615e0fdf8aac79a43f24c537604725504bfa82d8a9e8beaddd17caae9d44a9",
  "url": "https://rest.uniprot.org/unisave/A0A385XI11?format=txt&versions=21"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 36. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
