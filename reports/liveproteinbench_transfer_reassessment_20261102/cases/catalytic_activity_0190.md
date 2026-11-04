# catalytic_activity_0190

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0190.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAAVTRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRALEQELSGTVFIPGDVTQERDLQTLVSETLSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEVNLLGTYTLIKLALPHLRKSRGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRHGVRVNCISPGNIWTPLWEELAASTSDPRATILEGTLAQPLGRMGQPAEVAAAAVFLASEATFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH

[Multiple Choices]
A. a 3-O-beta-D-glucosyl-beta-D-glucuronoside + phosphate = a beta-D-glucuronoside + alpha-D-glucose 1-phosphate
B. (2R,3R,5S)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)
C. demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine
D. L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)
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

> The sequence-matched UniProt record assigns this protein L-fucose dehydrogenase activity and the reaction in option D. The assignment is supported by similarity evidence from Q9BPX1 (ECO:0000250), so it is an annotation by transfer rather than evidence of direct experimental characterization of this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal glycine-rich Rossmann-like motif (around VVTGGSRGIG), consistent with an NAD-dependent oxidoreductase, and its length and motif pattern are compatible with the short-chain dehydrogenase/reductase family. That makes option D, an NAD-dependent sugar oxidation, meaningfully more plausible than the glycoside phosphorylase in A or the SAM-dependent reactions in B and C. This is a family-level inference, not proof of the exact substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and enzyme-family knowledge distinguishes the NAD-dependent dehydrogenase choice from the other reaction types. The exact substrate assignment is less certain from sequence alone, but the alternatives make the family-level distinction useful.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D matches the oxidoreductase class suggested by the sequence among the offered choices.


### Important caveats

- The cited catalytic-activity annotation is transferred from a homolog and should not be described as direct experimental confirmation for this exact protein.
- The record also lists related sugar oxidation reactions, so the sequence-based choice among these options does not establish that L-fucose is the only substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich Rossmann-like motif (around VVTGGSRGIG), consistent with an NAD-dependent oxidoreductase, and its length and motif pattern are compatible with the short-chain dehydrogenase/reductase family. That makes option D, an NAD-dependent sugar oxidation, meaningfully more plausible than the glycoside phosphorylase in A or the SAM-dependent reactions in B and C. This is a family-level inference, not proof of the exact substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-family knowledge distinguishes the NAD-dependent dehydrogenase choice from the other reaction types. The exact substrate assignment is less certain from sequence alone, but the alternatives make the family-level distinction useful."
  },
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein L-fucose dehydrogenase activity and the reaction in option D. The assignment is supported by similarity evidence from Q9BPX1 (ECO:0000250), so it is an annotation by transfer rather than evidence of direct experimental characterization of this protein."
  },
  "important_caveats": [
    "The cited catalytic-activity annotation is transferred from a homolog and should not be described as direct experimental confirmation for this exact protein.",
    "The record also lists related sugar oxidation reactions, so the sequence-based choice among these options does not establish that L-fucose is the only substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D matches the oxidoreductase class suggested by the sequence among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein L-fucose dehydrogenase activity and the reaction in option D. The assignment is supported by similarity evidence from Q9BPX1 (ECO:0000250), so it is an annotation by transfer rather than evidence of direct experimental characterization of this protein.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich Rossmann-like motif (around VVTGGSRGIG), consistent with an NAD-dependent oxidoreductase, and its length and motif pattern are compatible with the short-chain dehydrogenase/reductase family. That makes option D, an NAD-dependent sugar oxidation, meaningfully more plausible than the glycoside phosphorylase in A or the SAM-dependent reactions in B and C. This is a family-level inference, not proof of the exact substrate.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-family knowledge distinguishes the NAD-dependent dehydrogenase choice from the other reaction types. The exact substrate assignment is less certain from sequence alone, but the alternatives make the family-level distinction useful."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D matches the oxidoreductase class suggested by the sequence among the offered choices."
  },
  "important_caveats": [
    "The cited catalytic-activity annotation is transferred from a homolog and should not be described as direct experimental confirmation for this exact protein.",
    "The record also lists related sugar oxidation reactions, so the sequence-based choice among these options does not establish that L-fucose is the only substrate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E9Q3D4 annotates this sequence as L-fucose dehydrogenase (EC 1.1.1.122) with the catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+). The annotation evidence code is ECO:0000250 (transferred by similarity from human ortholog Q9BPX1), meaning this is a computational/similarity-based annotation rather than direct experimental characterization of this exact mouse protein. The annotation nonetheless supports the expected answer as the recorded function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an unambiguous Rossmann-fold NAD(P)-binding motif at the N-terminus: 'VVVVTGGSRGIGAAIVRAF' (the GGxGxG glycine-rich loop). This immediately identifies the protein as an NAD(P)-dependent oxidoreductase. Among the four choices, only D (L-fucose + NAD(+) → L-fucono-1,5-lactone + NADH + H+) is an NAD-dependent dehydrogenase reaction. Choice A is a phosphorylase (no cofactor), B is a radical-SAM enzyme (uses SAM and a reductant AH2, not NAD), and C is a SAM-dependent methyltransferase (no NAD). Furthermore, the overall length (273 aa) and conserved SDR-family motifs ('NISSLVGA' catalytic region, 'TGGAELGYGRK' C-terminal motif) confirm membership in the short-chain dehydrogenase/reductase superfamily, which is exclusively composed of NAD(P)-dependent enzymes. This family-level identification plus the NAD-binding motif cleanly eliminates A, B, and C and selects D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold NAD-binding motif and SDR-family sequence architecture are directly readable from the input sequence and represent transferable knowledge about protein families. Since D is the only NAD-dependent dehydrogenase among the four options, family-level recognition of an SDR/NAD-binding enzyme is sufficient to select D without needing to recall the exact substrate specificity of this particular mouse protein. The other three choices are mechanistically incompatible with the visible cofactor-binding architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (D) is an NAD-dependent dehydrogenase reaction. The Rossmann-fold motif unambiguously identifies the enzyme as an NAD(P)-dependent oxidoreductase, making A (phosphorylase), B (radical SAM), and C (methyltransferase) clearly incompatible. No other option is defensible given the sequence features.


### Important caveats

- The UniProt annotation for E9Q3D4 is based on similarity transfer (ECO:0000250) from the human ortholog Q9BPX1, not direct experimental characterization of the mouse protein itself.
- The SDR family is very large and functionally diverse; identifying the specific substrate (L-fucose) among many possible SDR substrates would require more detailed knowledge. However, this is unnecessary here because D is the sole dehydrogenase option among the four choices.
- The protein is also annotated with alternative names including 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its historical classification. The reannotation as L-fucose dehydrogenase is relatively recent (entry first public 2025-04-09).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an unambiguous Rossmann-fold NAD(P)-binding motif at the N-terminus: 'VVVVTGGSRGIGAAIVRAF' (the GGxGxG glycine-rich loop). This immediately identifies the protein as an NAD(P)-dependent oxidoreductase. Among the four choices, only D (L-fucose + NAD(+) → L-fucono-1,5-lactone + NADH + H+) is an NAD-dependent dehydrogenase reaction. Choice A is a phosphorylase (no cofactor), B is a radical-SAM enzyme (uses SAM and a reductant AH2, not NAD), and C is a SAM-dependent methyltransferase (no NAD). Furthermore, the overall length (273 aa) and conserved SDR-family motifs ('NISSLVGA' catalytic region, 'TGGAELGYGRK' C-terminal motif) confirm membership in the short-chain dehydrogenase/reductase superfamily, which is exclusively composed of NAD(P)-dependent enzymes. This family-level identification plus the NAD-binding motif cleanly eliminates A, B, and C and selects D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold NAD-binding motif and SDR-family sequence architecture are directly readable from the input sequence and represent transferable knowledge about protein families. Since D is the only NAD-dependent dehydrogenase among the four options, family-level recognition of an SDR/NAD-binding enzyme is sufficient to select D without needing to recall the exact substrate specificity of this particular mouse protein. The other three choices are mechanistically incompatible with the visible cofactor-binding architecture."
  },
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E9Q3D4 annotates this sequence as L-fucose dehydrogenase (EC 1.1.1.122) with the catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+). The annotation evidence code is ECO:0000250 (transferred by similarity from human ortholog Q9BPX1), meaning this is a computational/similarity-based annotation rather than direct experimental characterization of this exact mouse protein. The annotation nonetheless supports the expected answer as the recorded function."
  },
  "important_caveats": [
    "The UniProt annotation for E9Q3D4 is based on similarity transfer (ECO:0000250) from the human ortholog Q9BPX1, not direct experimental characterization of the mouse protein itself.",
    "The SDR family is very large and functionally diverse; identifying the specific substrate (L-fucose) among many possible SDR substrates would require more detailed knowledge. However, this is unnecessary here because D is the sole dehydrogenase option among the four choices.",
    "The protein is also annotated with alternative names including 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its historical classification. The reannotation as L-fucose dehydrogenase is relatively recent (entry first public 2025-04-09)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (D) is an NAD-dependent dehydrogenase reaction. The Rossmann-fold motif unambiguously identifies the enzyme as an NAD(P)-dependent oxidoreductase, making A (phosphorylase), B (radical SAM), and C (methyltransferase) clearly incompatible. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E9Q3D4 annotates this sequence as L-fucose dehydrogenase (EC 1.1.1.122) with the catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+). The annotation evidence code is ECO:0000250 (transferred by similarity from human ortholog Q9BPX1), meaning this is a computational/similarity-based annotation rather than direct experimental characterization of this exact mouse protein. The annotation nonetheless supports the expected answer as the recorded function.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an unambiguous Rossmann-fold NAD(P)-binding motif at the N-terminus: 'VVVVTGGSRGIGAAIVRAF' (the GGxGxG glycine-rich loop). This immediately identifies the protein as an NAD(P)-dependent oxidoreductase. Among the four choices, only D (L-fucose + NAD(+) → L-fucono-1,5-lactone + NADH + H+) is an NAD-dependent dehydrogenase reaction. Choice A is a phosphorylase (no cofactor), B is a radical-SAM enzyme (uses SAM and a reductant AH2, not NAD), and C is a SAM-dependent methyltransferase (no NAD). Furthermore, the overall length (273 aa) and conserved SDR-family motifs ('NISSLVGA' catalytic region, 'TGGAELGYGRK' C-terminal motif) confirm membership in the short-chain dehydrogenase/reductase superfamily, which is exclusively composed of NAD(P)-dependent enzymes. This family-level identification plus the NAD-binding motif cleanly eliminates A, B, and C and selects D.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold NAD-binding motif and SDR-family sequence architecture are directly readable from the input sequence and represent transferable knowledge about protein families. Since D is the only NAD-dependent dehydrogenase among the four options, family-level recognition of an SDR/NAD-binding enzyme is sufficient to select D without needing to recall the exact substrate specificity of this particular mouse protein. The other three choices are mechanistically incompatible with the visible cofactor-binding architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (D) is an NAD-dependent dehydrogenase reaction. The Rossmann-fold motif unambiguously identifies the enzyme as an NAD(P)-dependent oxidoreductase, making A (phosphorylase), B (radical SAM), and C (methyltransferase) clearly incompatible. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt annotation for E9Q3D4 is based on similarity transfer (ECO:0000250) from the human ortholog Q9BPX1, not direct experimental characterization of the mouse protein itself.",
    "The SDR family is very large and functionally diverse; identifying the specific substrate (L-fucose) among many possible SDR substrates would require more detailed knowledge. However, this is unnecessary here because D is the sole dehydrogenase option among the four choices.",
    "The protein is also annotated with alternative names including 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its historical classification. The reannotation as L-fucose dehydrogenase is relatively recent (entry first public 2025-04-09)."
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
  "benchmark_sequence_length": 273,
  "benchmark_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "current_entry_audit": {
    "entryVersion": 97,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-04-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 273,
  "current_source_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 95,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E9Q3D4",
  "selected_historical_entry_version": 95,
  "selected_historical_record_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "selected_historical_source_sequence_length": 273,
  "selected_historical_source_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "selected_historical_version": {
    "accession": "E9Q3D4",
    "database": "Swiss-Prot",
    "entryVersion": 95,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHB14_MOUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E9Q3D4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":97,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-04-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mouse\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Mus\",\"Mus\"],\"scientificName\":\"Mus musculus\",\"taxonId\":10090}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Hydroxysteroid 17-beta dehydrogenase 14\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"value\":\"1.1.1.122\"}],\"fullName\":{\"value\":\"L-fucose dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81516\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"name\":\"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81515\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:2181\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:81457\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"name\":\"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:46994\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194242\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"name\":\"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81523\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37619\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:182410\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H1",
  "excerpt": "ID   DHB14_MOUSE             Reviewed;         273 AA.\nAC   E9Q3D4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-APR-2011, sequence version 1.\nDT   28-JAN-2026, entry version 95.\nDE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000250|UniProtKB:Q9BPX1};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\nGN   Name=Hsd17b14 {ECO:0000312|MGI:MGI:1913315}; Synonyms=Dhrs10, retSDR3;\nOS   Mus musculus (Mouse).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Mus; Mus.\nOX   NCBI_TaxID=10090;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000250|UniProtKB:Q9BPX1};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;\nCC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;\nCC         Evidence={ECO:0000250|UniProtKB:Q9BPX1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81519, ChEBI:CHEBI:15378, ChEBI:CHEBI:46994,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:194242;\nCC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81523, ChEBI:CHEBI:15378, ChEBI:CHEBI:37619,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:182410;\nCC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 190. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
