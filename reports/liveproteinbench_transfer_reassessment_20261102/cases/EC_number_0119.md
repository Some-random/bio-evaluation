# EC_number_0119

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0119.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 1.1.1.122

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAAVGRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRAVEQELLGTVFIPGDVTQEGDLQTLISETVSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEENLLGAYTLIKLALPHLRKSKGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRYGVRVNCISPGNIWTPLWQELAAATSDPRATILEGTLAQPLGRMGQPAEVGAAAVFLASEATFCTGLELFMTGGAELGYGRKASSSTLVEVPILPP

[Multiple Choices]
A. 1.1.1.336
B. 5.4.99.39
C. 1.1.1.122
D. 3.1.1.29
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

> The reviewer evidence identifies the matched sequence as EC 1.1.1.122 and links that assignment to an experimentally supported L-fucose dehydrogenase reaction. The assigned option is C.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich Rossmann-like motif and the rest of the sequence are consistent with an NAD-dependent short-chain dehydrogenase/reductase. That supports an oxidoreductase-level inference, but does not meaningfully distinguish the substrate-specific EC choices A and C.


**Missing item-specific fact**

> The sequence input does not establish this protein's substrate specificity—particularly its experimentally reported oxidation of L-fucose—or otherwise distinguish EC 1.1.1.122 from the other dehydrogenase choice.


**Reason**

> The transferable sequence features support a dehydrogenase family/class inference, not the complete EC number. Selecting C depends on substrate-specific functional information for this protein that is not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The EC alternatives specify distinct activities; the question has a definite target property, although the supplied sequence alone does not resolve its substrate specificity.


### Important caveats

- The reviewer-only UniProt evidence matches the supplied sequence and cites an experimental publication, but that evidence was not available as original model input.
- A Rossmann-like motif indicates likely cofactor-binding chemistry, not a particular substrate or complete EC number.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich Rossmann-like motif and the rest of the sequence are consistent with an NAD-dependent short-chain dehydrogenase/reductase. That supports an oxidoreductase-level inference, but does not meaningfully distinguish the substrate-specific EC choices A and C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence input does not establish this protein's substrate specificity—particularly its experimentally reported oxidation of L-fucose—or otherwise distinguish EC 1.1.1.122 from the other dehydrogenase choice.",
    "reason": "The transferable sequence features support a dehydrogenase family/class inference, not the complete EC number. Selecting C depends on substrate-specific functional information for this protein that is not supplied in the question."
  },
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence identifies the matched sequence as EC 1.1.1.122 and links that assignment to an experimentally supported L-fucose dehydrogenase reaction. The assigned option is C."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the supplied sequence and cites an experimental publication, but that evidence was not available as original model input.",
    "A Rossmann-like motif indicates likely cofactor-binding chemistry, not a particular substrate or complete EC number."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC alternatives specify distinct activities; the question has a definite target property, although the supplied sequence alone does not resolve its substrate specificity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence identifies the matched sequence as EC 1.1.1.122 and links that assignment to an experimentally supported L-fucose dehydrogenase reaction. The assigned option is C.",
    "evidence_ids": ["C5", "C8", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich Rossmann-like motif and the rest of the sequence are consistent with an NAD-dependent short-chain dehydrogenase/reductase. That supports an oxidoreductase-level inference, but does not meaningfully distinguish the substrate-specific EC choices A and C.",
    "missing_item_specific_fact": "The sequence input does not establish this protein's substrate specificity—particularly its experimentally reported oxidation of L-fucose—or otherwise distinguish EC 1.1.1.122 from the other dehydrogenase choice.",
    "reason": "The transferable sequence features support a dehydrogenase family/class inference, not the complete EC number. Selecting C depends on substrate-specific functional information for this protein that is not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC alternatives specify distinct activities; the question has a definite target property, although the supplied sequence alone does not resolve its substrate specificity."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the supplied sequence and cites an experimental publication, but that evidence was not available as original model input.",
    "A Rossmann-like motif indicates likely cofactor-binding chemistry, not a particular substrate or complete EC number."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A8I6GJ95 (sequence matched) annotates this protein as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al. demonstrating HSD17B14 is an L-fucose dehydrogenase). The catalytic activity comments confirm the reaction L-fucose + NAD+ = L-fucono-1,5-lactone + NADH + H+ under EC 1.1.1.122.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD-binding motif (GSRGIGAAIVRA at the N-terminus), a short-chain dehydrogenase/reductase (SDR) catalytic architecture (~270 aa, VVG motif, and a YxxxK catalytic motif near the C-terminus in 'GYGRK'), and the 'VVFCDKDE' region. These features confidently identify the protein as an NAD-dependent dehydrogenase/reductase, eliminating option B (5.4.99.39, an isomerase) and option D (3.1.1.29, a carboxylester hydrolase). However, both remaining options A (1.1.1.336) and C (1.1.1.122) fall within the same EC class 1.1.1 (oxidoreductases acting on the CH-OH group with NAD+ as acceptor). General SDR superfamily knowledge establishes the 1.1.1.x assignment but does not resolve the fourth digit. The specific substrate (L-fucose vs. whatever 1.1.1.336 acts on) is determined by active-site geometry and experimental characterization, not by a broadly transferable sequence motif that distinguishes these two particular EC numbers.


**Missing item-specific fact**

> The specific substrate specificity of this enzyme (L-fucose dehydrogenase activity, EC 1.1.1.122) was established experimentally only in 2024 (PubMed:38944119). Distinguishing EC 1.1.1.122 from EC 1.1.1.336 requires knowing which specific CH-OH substrate this particular SDR enzyme oxidizes, a fact about this exact protein that is not encoded in a recognizable sequence motif distinguishable from other 1.1.1.x enzymes using general SDR family knowledge.


**Reason**

> The sequence unambiguously identifies an SDR/NAD-dependent dehydrogenase, ruling out the isomerase (B) and hydrolase (D) options through well-established family-level knowledge. However, the critical A-vs-C distinction (both 1.1.1.x) requires knowing the specific substrate of this protein, which was determined experimentally in 2024 and is not inferable from general SDR or Rossmann-fold knowledge. No conserved subfamily motif in the sequence reliably separates 1.1.1.336 from 1.1.1.122.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly incompatible with the Rossmann-fold SDR architecture. Between A and C, the evidence supports C, and while the A-vs-C distinction is hard to make from sequence alone, only one is the experimentally validated annotation. No genuine ambiguity in the sense of two equally defensible choices exists given the evidence.


### Important caveats

- EC 1.1.1.336 is a less commonly referenced EC number; if it is obscure or not well-characterized, a model might default to the more familiar 1.1.1.122, but this would reflect familiarity bias rather than biological reasoning.
- The L-fucose dehydrogenase activity of HSD17B14 was only established in 2024; the protein was previously annotated under its HSD17B family name, so the EC 1.1.1.122 assignment is very recent.
- The sequence features (Rossmann fold, SDR catalytic tetrad, ~270 aa length) are consistent with the broad SDR superfamily but do not pinpoint the specific substrate class needed to resolve the fourth EC digit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD-binding motif (GSRGIGAAIVRA at the N-terminus), a short-chain dehydrogenase/reductase (SDR) catalytic architecture (~270 aa, VVG motif, and a YxxxK catalytic motif near the C-terminus in 'GYGRK'), and the 'VVFCDKDE' region. These features confidently identify the protein as an NAD-dependent dehydrogenase/reductase, eliminating option B (5.4.99.39, an isomerase) and option D (3.1.1.29, a carboxylester hydrolase). However, both remaining options A (1.1.1.336) and C (1.1.1.122) fall within the same EC class 1.1.1 (oxidoreductases acting on the CH-OH group with NAD+ as acceptor). General SDR superfamily knowledge establishes the 1.1.1.x assignment but does not resolve the fourth digit. The specific substrate (L-fucose vs. whatever 1.1.1.336 acts on) is determined by active-site geometry and experimental characterization, not by a broadly transferable sequence motif that distinguishes these two particular EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this enzyme (L-fucose dehydrogenase activity, EC 1.1.1.122) was established experimentally only in 2024 (PubMed:38944119). Distinguishing EC 1.1.1.122 from EC 1.1.1.336 requires knowing which specific CH-OH substrate this particular SDR enzyme oxidizes, a fact about this exact protein that is not encoded in a recognizable sequence motif distinguishable from other 1.1.1.x enzymes using general SDR family knowledge.",
    "reason": "The sequence unambiguously identifies an SDR/NAD-dependent dehydrogenase, ruling out the isomerase (B) and hydrolase (D) options through well-established family-level knowledge. However, the critical A-vs-C distinction (both 1.1.1.x) requires knowing the specific substrate of this protein, which was determined experimentally in 2024 and is not inferable from general SDR or Rossmann-fold knowledge. No conserved subfamily motif in the sequence reliably separates 1.1.1.336 from 1.1.1.122."
  },
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A8I6GJ95 (sequence matched) annotates this protein as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al. demonstrating HSD17B14 is an L-fucose dehydrogenase). The catalytic activity comments confirm the reaction L-fucose + NAD+ = L-fucono-1,5-lactone + NADH + H+ under EC 1.1.1.122."
  },
  "important_caveats": [
    "EC 1.1.1.336 is a less commonly referenced EC number; if it is obscure or not well-characterized, a model might default to the more familiar 1.1.1.122, but this would reflect familiarity bias rather than biological reasoning.",
    "The L-fucose dehydrogenase activity of HSD17B14 was only established in 2024; the protein was previously annotated under its HSD17B family name, so the EC 1.1.1.122 assignment is very recent.",
    "The sequence features (Rossmann fold, SDR catalytic tetrad, ~270 aa length) are consistent with the broad SDR superfamily but do not pinpoint the specific substrate class needed to resolve the fourth EC digit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with the Rossmann-fold SDR architecture. Between A and C, the evidence supports C, and while the A-vs-C distinction is hard to make from sequence alone, only one is the experimentally validated annotation. No genuine ambiguity in the sense of two equally defensible choices exists given the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A8I6GJ95 (sequence matched) annotates this protein as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al. demonstrating HSD17B14 is an L-fucose dehydrogenase). The catalytic activity comments confirm the reaction L-fucose + NAD+ = L-fucono-1,5-lactone + NADH + H+ under EC 1.1.1.122.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD-binding motif (GSRGIGAAIVRA at the N-terminus), a short-chain dehydrogenase/reductase (SDR) catalytic architecture (~270 aa, VVG motif, and a YxxxK catalytic motif near the C-terminus in 'GYGRK'), and the 'VVFCDKDE' region. These features confidently identify the protein as an NAD-dependent dehydrogenase/reductase, eliminating option B (5.4.99.39, an isomerase) and option D (3.1.1.29, a carboxylester hydrolase). However, both remaining options A (1.1.1.336) and C (1.1.1.122) fall within the same EC class 1.1.1 (oxidoreductases acting on the CH-OH group with NAD+ as acceptor). General SDR superfamily knowledge establishes the 1.1.1.x assignment but does not resolve the fourth digit. The specific substrate (L-fucose vs. whatever 1.1.1.336 acts on) is determined by active-site geometry and experimental characterization, not by a broadly transferable sequence motif that distinguishes these two particular EC numbers.",
    "missing_item_specific_fact": "The specific substrate specificity of this enzyme (L-fucose dehydrogenase activity, EC 1.1.1.122) was established experimentally only in 2024 (PubMed:38944119). Distinguishing EC 1.1.1.122 from EC 1.1.1.336 requires knowing which specific CH-OH substrate this particular SDR enzyme oxidizes, a fact about this exact protein that is not encoded in a recognizable sequence motif distinguishable from other 1.1.1.x enzymes using general SDR family knowledge.",
    "reason": "The sequence unambiguously identifies an SDR/NAD-dependent dehydrogenase, ruling out the isomerase (B) and hydrolase (D) options through well-established family-level knowledge. However, the critical A-vs-C distinction (both 1.1.1.x) requires knowing the specific substrate of this protein, which was determined experimentally in 2024 and is not inferable from general SDR or Rossmann-fold knowledge. No conserved subfamily motif in the sequence reliably separates 1.1.1.336 from 1.1.1.122."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with the Rossmann-fold SDR architecture. Between A and C, the evidence supports C, and while the A-vs-C distinction is hard to make from sequence alone, only one is the experimentally validated annotation. No genuine ambiguity in the sense of two equally defensible choices exists given the evidence."
  },
  "important_caveats": [
    "EC 1.1.1.336 is a less commonly referenced EC number; if it is obscure or not well-characterized, a model might default to the more familiar 1.1.1.122, but this would reflect familiarity bias rather than biological reasoning.",
    "The L-fucose dehydrogenase activity of HSD17B14 was only established in 2024; the protein was previously annotated under its HSD17B family name, so the EC 1.1.1.122 assignment is very recent.",
    "The sequence features (Rossmann fold, SDR catalytic tetrad, ~270 aa length) are consistent with the broad SDR superfamily but do not pinpoint the specific substrate class needed to resolve the fourth EC digit."
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
  "benchmark_sequence_length": 270,
  "benchmark_sequence_sha256": "bd37d1d516e73777e155d3437157c555ba99078fd50abfd1f3899c2c20580fad",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-05-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 270,
  "current_source_sequence_sha256": "bd37d1d516e73777e155d3437157c555ba99078fd50abfd1f3899c2c20580fad",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A8I6GJ95",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "selected_historical_source_sequence_length": 270,
  "selected_historical_source_sequence_sha256": "bd37d1d516e73777e155d3437157c555ba99078fd50abfd1f3899c2c20580fad",
  "selected_historical_version": {
    "accession": "A0A8I6GJ95",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHB14_RAT",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A8I6GJ95\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-05-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rat\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Hydroxysteroid 17-beta dehydrogenase 14\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.122\"}],\"fullName\":{\"value\":\"L-fucose dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81516\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81515\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:2181\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:81457\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81520\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:46994\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194242\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81524\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81523\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37619\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:182410\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Witecka A.\",\"Kazak V.\",\"Kwiatkowski S.\",\"Kiersztan A.\",\"Jagielski A.K.\",\"Kozminski W.\",\"Augustyniak R.\",\"Drozak J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38944119\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107501\"}],\"citationType\":\"journal article\",\"firstPage\":\"107501\",\"id\":\"38944119\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107501\",\"publicationDate\":\"2024\",\"title\":\"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\",\"volume\":\"300\"},\"referenceNumber\":2,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"FUNCTION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   DHB14_RAT               Reviewed;         270 AA.\nAC   A0A8I6GJ95;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-MAY-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\nGN   Name=Hsd17b14;\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   CATALYTIC ACTIVITY, FUNCTION, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=38944119; DOI=10.1016/j.jbc.2024.107501;\nRA   Witecka A., Kazak V., Kwiatkowski S., Kiersztan A., Jagielski A.K.,\nRA   Kozminski W., Augustyniak R., Drozak J.;\nRT   \"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose\nRT   dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\";\nRL   J. Biol. Chem. 300:107501-107501(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81519, ChEBI:CHEBI:15378, ChEBI:CHEBI:46994,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:194242;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81520;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81523, ChEBI:CHEBI:15378, ChEBI:CHEBI:37619,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:182410;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81524;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
