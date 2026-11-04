# GO_molecular_function_0113

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0113.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — D-threo-aldose 1-dehydrogenase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASGARYAGKVVVVTGAARGIGAGIARAFVDSGAQVVICDKDERGGRALEQELRGAVFIRCDVTREEDVRALLSDTVHRFGRLDCVVNNAGSHPPLQPLEETTAQGFRELLELNLLGTYTLCKLAFPHLRRSRGNIINISTLVGAVGQLQGVPYAATKGAVTALTKALALDESQYGVRVNCISPGNIWTPLWQELAALAPDPRAAIREGAMAQPLGRMGQPAEVGAAAVFLASEASFCTGLELFVTGGAELGSGPENFFRSLGLCVVPEDVPPPTSRPRICSYK

[Multiple Choices]
A. DNA topoisomerase type I (single strand cut, ATP-independent) activity
B. peptidyl-tRNA hydrolase activity
C. oxidoreductase activity, acting on NAD(P)H
D. D-threo-aldose 1-dehydrogenase activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched source reports an experimentally supported NAD(+)-dependent aldose oxidation reaction and a directly assayed GO annotation for the keyed activity. This supports D; it is more than a computationally transferred annotation.

Citations as saved: [C6](#evidence-c6), [C9](#evidence-c9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a glycine-rich Rossmann-like cofactor-binding motif near its N-terminus and the characteristic Tyr-x-x-x-Lys motif of short-chain dehydrogenase/reductases, supporting an NAD-dependent dehydrogenase rather than a topoisomerase or tRNA hydrolase. Among the choices, D describes oxidation using NAD+ as acceptor, whereas C specifies NAD(P)H as the electron donor. This makes D a credible best fit from transferable family and reaction-direction knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The motifs support the relevant oxidoreductase family and make the offered alternatives meaningfully distinguishable, though they do not independently establish the enzyme's exact sugar substrate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the best fit among the listed alternatives; C specifies the opposite cofactor role, and A and B describe unrelated activities.


### Important caveats

- Sequence motifs alone do not prove D-threo-aldose substrate specificity; the reviewer-only matched-sequence evidence supplies that confirmation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich Rossmann-like cofactor-binding motif near its N-terminus and the characteristic Tyr-x-x-x-Lys motif of short-chain dehydrogenase/reductases, supporting an NAD-dependent dehydrogenase rather than a topoisomerase or tRNA hydrolase. Among the choices, D describes oxidation using NAD+ as acceptor, whereas C specifies NAD(P)H as the electron donor. This makes D a credible best fit from transferable family and reaction-direction knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The motifs support the relevant oxidoreductase family and make the offered alternatives meaningfully distinguishable, though they do not independently establish the enzyme's exact sugar substrate."
  },
  "case_id": "GO_molecular_function_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched source reports an experimentally supported NAD(+)-dependent aldose oxidation reaction and a directly assayed GO annotation for the keyed activity. This supports D; it is more than a computationally transferred annotation."
  },
  "important_caveats": [
    "Sequence motifs alone do not prove D-threo-aldose substrate specificity; the reviewer-only matched-sequence evidence supplies that confirmation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the best fit among the listed alternatives; C specifies the opposite cofactor role, and A and B describe unrelated activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched source reports an experimentally supported NAD(+)-dependent aldose oxidation reaction and a directly assayed GO annotation for the keyed activity. This supports D; it is more than a computationally transferred annotation.",
    "evidence_ids": ["C6", "C9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a glycine-rich Rossmann-like cofactor-binding motif near its N-terminus and the characteristic Tyr-x-x-x-Lys motif of short-chain dehydrogenase/reductases, supporting an NAD-dependent dehydrogenase rather than a topoisomerase or tRNA hydrolase. Among the choices, D describes oxidation using NAD+ as acceptor, whereas C specifies NAD(P)H as the electron donor. This makes D a credible best fit from transferable family and reaction-direction knowledge.",
    "missing_item_specific_fact": "",
    "reason": "The motifs support the relevant oxidoreductase family and make the offered alternatives meaningfully distinguishable, though they do not independently establish the enzyme's exact sugar substrate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the best fit among the listed alternatives; C specifies the opposite cofactor role, and A and B describe unrelated activities."
  },
  "important_caveats": [
    "Sequence motifs alone do not prove D-threo-aldose substrate specificity; the reviewer-only matched-sequence evidence supplies that confirmation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAT9JA24 (sequence matched) annotates this protein with GO:0047834 'D-threo-aldose 1-dehydrogenase activity' with evidence code IDA:UniProtKB, based on experimental data from PubMed:38944119 (2024). The protein is characterized as L-fucose dehydrogenase (EC 1.1.1.122), catalyzing NAD(+)-dependent oxidation of L-fucose, D-arabinose, and L-galactose. The GO term GO:0047834 explicitly includes 'L-fucose dehydrogenase activity' as a synonym and is defined by EC 1.1.1.122, matching the experimental catalytic activities documented in the entry.

Citations as saved: [C9](#evidence-c9), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H7](#evidence-h7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'VVVVTGAARGIGAGIARAF' contains a canonical Rossmann-fold GxGxxG motif (TGAARGIGAG), a hallmark of NAD(P)-binding dehydrogenases. This immediately eliminates options A (DNA topoisomerase, which uses a completely different catalytic fold) and B (peptidyl-tRNA hydrolase, a carboxylic ester hydrolase with no Rossmann fold). The remaining distinction is between C (GO:0016651, EC 1.6.-.-, where NAD(P)H is the electron DONOR being oxidized) and D (GO:0047834, EC 1.1.1.122, where NAD+ is the electron ACCEPTOR oxidizing a CH-OH group). Transferable family knowledge of the HSD17B (hydroxysteroid 17β-dehydrogenase) family and the broader short-chain dehydrogenase/reductase (SDR) superfamily indicates these are soluble, typically 250–350 aa monomeric/dimeric enzymes classified under EC 1.1.1.- (acting on CH-OH group of donors, NAD/NADP as acceptor). In contrast, EC 1.6.-.- enzymes (NADH oxidases, NAD(P)H dehydrogenases of respiratory complexes) are typically membrane-associated or part of large multi-subunit assemblies. The 284-aa soluble architecture with a single Rossmann fold is inconsistent with EC 1.6.-.-. Furthermore, the GO ontology places EC 1.1.1.- under 'oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor' (GO:0016616), which is a sibling—not a child—of GO:0016651. Recognizing the HSD17B/SDR family thus places the enzyme on the EC 1.1.1.- branch, making D the correct choice among the offered alternatives. The specific substrate 'D-threo-aldose' is the only EC 1.1.1.- option presented, so family-level EC assignment suffices to select D over C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann fold motif eliminates A and B. Recognition of the HSD17B/SDR family (a well-characterized group of soluble EC 1.1.1.- dehydrogenases) and the GO ontology hierarchy distinguishing 'acting on CH-OH group' (parent of D) from 'acting on NAD(P)H' (option C) provides a concrete, transferable inference from sequence features and family-level knowledge to select D over C without needing the specific experimental annotation of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C (GO:0016651, EC 1.6.-.-) describes enzymes where NAD(P)H is the substrate being oxidized, which is mechanistically opposite to the enzyme's actual function (NAD+ as acceptor oxidizing a sugar). The GO ontology hierarchy and EC classification clearly separate these branches. Options A and B are eliminated by the absence of any topoisomerase or hydrolase structural motifs. Only D correctly matches the EC 1.1.1.- classification indicated by the family and fold.


### Important caveats

- The specific substrate 'D-threo-aldose' (L-fucose/D-arabinose) is not trivially predictable from sequence alone; the argument relies on the fact that D is the only EC 1.1.1.- option offered among the four choices.
- The HSD17B family name suggests steroid dehydrogenase activity; the L-fucose dehydrogenase function of HSD17B14 was only experimentally demonstrated in 2024. A model relying solely on family name might expect steroid activity, but since no steroid-dehydrogenase option is offered, this does not create ambiguity among the given choices.
- The Rossmann fold is shared across many EC classes; the family-level inference (HSD17B/SDR → EC 1.1.1.-) is probabilistic but strongly supported by the soluble monomeric architecture and sequence similarity to known family members.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'VVVVTGAARGIGAGIARAF' contains a canonical Rossmann-fold GxGxxG motif (TGAARGIGAG), a hallmark of NAD(P)-binding dehydrogenases. This immediately eliminates options A (DNA topoisomerase, which uses a completely different catalytic fold) and B (peptidyl-tRNA hydrolase, a carboxylic ester hydrolase with no Rossmann fold). The remaining distinction is between C (GO:0016651, EC 1.6.-.-, where NAD(P)H is the electron DONOR being oxidized) and D (GO:0047834, EC 1.1.1.122, where NAD+ is the electron ACCEPTOR oxidizing a CH-OH group). Transferable family knowledge of the HSD17B (hydroxysteroid 17β-dehydrogenase) family and the broader short-chain dehydrogenase/reductase (SDR) superfamily indicates these are soluble, typically 250–350 aa monomeric/dimeric enzymes classified under EC 1.1.1.- (acting on CH-OH group of donors, NAD/NADP as acceptor). In contrast, EC 1.6.-.- enzymes (NADH oxidases, NAD(P)H dehydrogenases of respiratory complexes) are typically membrane-associated or part of large multi-subunit assemblies. The 284-aa soluble architecture with a single Rossmann fold is inconsistent with EC 1.6.-.-. Furthermore, the GO ontology places EC 1.1.1.- under 'oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor' (GO:0016616), which is a sibling—not a child—of GO:0016651. Recognizing the HSD17B/SDR family thus places the enzyme on the EC 1.1.1.- branch, making D the correct choice among the offered alternatives. The specific substrate 'D-threo-aldose' is the only EC 1.1.1.- option presented, so family-level EC assignment suffices to select D over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold motif eliminates A and B. Recognition of the HSD17B/SDR family (a well-characterized group of soluble EC 1.1.1.- dehydrogenases) and the GO ontology hierarchy distinguishing 'acting on CH-OH group' (parent of D) from 'acting on NAD(P)H' (option C) provides a concrete, transferable inference from sequence features and family-level knowledge to select D over C without needing the specific experimental annotation of this exact protein."
  },
  "case_id": "GO_molecular_function_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C9",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H7",
      "H4",
      "H5",
      "H6",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAT9JA24 (sequence matched) annotates this protein with GO:0047834 'D-threo-aldose 1-dehydrogenase activity' with evidence code IDA:UniProtKB, based on experimental data from PubMed:38944119 (2024). The protein is characterized as L-fucose dehydrogenase (EC 1.1.1.122), catalyzing NAD(+)-dependent oxidation of L-fucose, D-arabinose, and L-galactose. The GO term GO:0047834 explicitly includes 'L-fucose dehydrogenase activity' as a synonym and is defined by EC 1.1.1.122, matching the experimental catalytic activities documented in the entry."
  },
  "important_caveats": [
    "The specific substrate 'D-threo-aldose' (L-fucose/D-arabinose) is not trivially predictable from sequence alone; the argument relies on the fact that D is the only EC 1.1.1.- option offered among the four choices.",
    "The HSD17B family name suggests steroid dehydrogenase activity; the L-fucose dehydrogenase function of HSD17B14 was only experimentally demonstrated in 2024. A model relying solely on family name might expect steroid activity, but since no steroid-dehydrogenase option is offered, this does not create ambiguity among the given choices.",
    "The Rossmann fold is shared across many EC classes; the family-level inference (HSD17B/SDR → EC 1.1.1.-) is probabilistic but strongly supported by the soluble monomeric architecture and sequence similarity to known family members."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (GO:0016651, EC 1.6.-.-) describes enzymes where NAD(P)H is the substrate being oxidized, which is mechanistically opposite to the enzyme's actual function (NAD+ as acceptor oxidizing a sugar). The GO ontology hierarchy and EC classification clearly separate these branches. Options A and B are eliminated by the absence of any topoisomerase or hydrolase structural motifs. Only D correctly matches the EC 1.1.1.- classification indicated by the family and fold."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAT9JA24 (sequence matched) annotates this protein with GO:0047834 'D-threo-aldose 1-dehydrogenase activity' with evidence code IDA:UniProtKB, based on experimental data from PubMed:38944119 (2024). The protein is characterized as L-fucose dehydrogenase (EC 1.1.1.122), catalyzing NAD(+)-dependent oxidation of L-fucose, D-arabinose, and L-galactose. The GO term GO:0047834 explicitly includes 'L-fucose dehydrogenase activity' as a synonym and is defined by EC 1.1.1.122, matching the experimental catalytic activities documented in the entry.",
    "evidence_ids": ["C9", "C4", "C5", "C6", "C7", "C8", "H7", "H4", "H5", "H6", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'VVVVTGAARGIGAGIARAF' contains a canonical Rossmann-fold GxGxxG motif (TGAARGIGAG), a hallmark of NAD(P)-binding dehydrogenases. This immediately eliminates options A (DNA topoisomerase, which uses a completely different catalytic fold) and B (peptidyl-tRNA hydrolase, a carboxylic ester hydrolase with no Rossmann fold). The remaining distinction is between C (GO:0016651, EC 1.6.-.-, where NAD(P)H is the electron DONOR being oxidized) and D (GO:0047834, EC 1.1.1.122, where NAD+ is the electron ACCEPTOR oxidizing a CH-OH group). Transferable family knowledge of the HSD17B (hydroxysteroid 17β-dehydrogenase) family and the broader short-chain dehydrogenase/reductase (SDR) superfamily indicates these are soluble, typically 250–350 aa monomeric/dimeric enzymes classified under EC 1.1.1.- (acting on CH-OH group of donors, NAD/NADP as acceptor). In contrast, EC 1.6.-.- enzymes (NADH oxidases, NAD(P)H dehydrogenases of respiratory complexes) are typically membrane-associated or part of large multi-subunit assemblies. The 284-aa soluble architecture with a single Rossmann fold is inconsistent with EC 1.6.-.-. Furthermore, the GO ontology places EC 1.1.1.- under 'oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor' (GO:0016616), which is a sibling—not a child—of GO:0016651. Recognizing the HSD17B/SDR family thus places the enzyme on the EC 1.1.1.- branch, making D the correct choice among the offered alternatives. The specific substrate 'D-threo-aldose' is the only EC 1.1.1.- option presented, so family-level EC assignment suffices to select D over C.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold motif eliminates A and B. Recognition of the HSD17B/SDR family (a well-characterized group of soluble EC 1.1.1.- dehydrogenases) and the GO ontology hierarchy distinguishing 'acting on CH-OH group' (parent of D) from 'acting on NAD(P)H' (option C) provides a concrete, transferable inference from sequence features and family-level knowledge to select D over C without needing the specific experimental annotation of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (GO:0016651, EC 1.6.-.-) describes enzymes where NAD(P)H is the substrate being oxidized, which is mechanistically opposite to the enzyme's actual function (NAD+ as acceptor oxidizing a sugar). The GO ontology hierarchy and EC classification clearly separate these branches. Options A and B are eliminated by the absence of any topoisomerase or hydrolase structural motifs. Only D correctly matches the EC 1.1.1.- classification indicated by the family and fold."
  },
  "important_caveats": [
    "The specific substrate 'D-threo-aldose' (L-fucose/D-arabinose) is not trivially predictable from sequence alone; the argument relies on the fact that D is the only EC 1.1.1.- option offered among the four choices.",
    "The HSD17B family name suggests steroid dehydrogenase activity; the L-fucose dehydrogenase function of HSD17B14 was only experimentally demonstrated in 2024. A model relying solely on family name might expect steroid activity, but since no steroid-dehydrogenase option is offered, this does not create ambiguity among the given choices.",
    "The Rossmann fold is shared across many EC classes; the family-level inference (HSD17B/SDR → EC 1.1.1.-) is probabilistic but strongly supported by the soluble monomeric architecture and sequence similarity to known family members."
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
  "benchmark_sequence_length": 284,
  "benchmark_sequence_sha256": "866d78afb63c4ef17950a8b38eb26f81ee9da683687494456a69d4262af65809",
  "current_entry_audit": {
    "entryVersion": 7,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 2
  },
  "current_record_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 284,
  "current_source_sequence_sha256": "866d78afb63c4ef17950a8b38eb26f81ee9da683687494456a69d4262af65809",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAT9JA24",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "selected_historical_source_sequence_length": 284,
  "selected_historical_source_sequence_sha256": "866d78afb63c4ef17950a8b38eb26f81ee9da683687494456a69d4262af65809",
  "selected_historical_version": {
    "accession": "A0AAT9JA24",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHB14_RABIT",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAT9JA24\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":7,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rabbit\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Lagomorpha\",\"Leporidae\",\"Oryctolagus\"],\"scientificName\":\"Oryctolagus cuniculus\",\"taxonId\":9986}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Hydroxysteroid 17-beta dehydrogenase 14\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.122\"}],\"fullName\":{\"value\":\"L-fucose dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"value\":\"Catalyzes the NAD(+)-dependent oxidation of L-fucose, yielding L-fucono-1,5-lactone, which rapidly converts spontaneously to L-fucone-1,4-lactone. Can also act on D-arabinose and L-galactose, with lower catalytic efficiency. Does not use NADPH. May be the initial enzyme of the putative L-fucose degradation pathway in mammals\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81516\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81515\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:2181\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:81457\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81520\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:46994\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194242\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81524\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81523\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37619\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:182410\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"id\":\"GO:0047834\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:D-threo-aldose 1-dehydrogenase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004303\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:estradiol 17-beta-dehydrogenase [NAD(P)+] activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0042802\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:identical protein binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:Ensembl\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Witecka A.\",\"Kazak V.\",\"Kwiatkowski S.\",\"Kiersztan A.\",\"Jagielski A.K.\",\"Kozminski W.\",\"Augustyniak R.\",\"Drozak J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38944119\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107501\"}],\"citationType\":\"journal article\",\"firstPage\":\"107501\",\"id\":\"38944119\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107501\",\"publicationDate\":\"2024\",\"title\":\"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\",\"volume\":\"300\"},\"referenceNumber\":2,\"referencePositions\":[\"IDENTIFICATION\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF TYR-154\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   DHB14_RABIT             Reviewed;         284 AA.\nAC   A0AAT9JA24; A0A5F9CLT4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 2.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\nGN   Name=HSD17B14;\nOS   Oryctolagus cuniculus (Rabbit).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Lagomorpha; Leporidae; Oryctolagus.\nOX   NCBI_TaxID=9986;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   IDENTIFICATION, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND MUTAGENESIS OF TYR-154.\nRX   PubMed=38944119; DOI=10.1016/j.jbc.2024.107501;\nRA   Witecka A., Kazak V., Kwiatkowski S., Kiersztan A., Jagielski A.K.,\nRA   Kozminski W., Augustyniak R., Drozak J.;\nRT   \"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose\nRT   dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\";\nRL   J. Biol. Chem. 300:107501-107501(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the NAD(+)-dependent oxidation of L-fucose,\nCC       yielding L-fucono-1,5-lactone, which rapidly converts spontaneously to\nCC       L-fucone-1,4-lactone. Can also act on D-arabinose and L-galactose, with\nCC       lower catalytic efficiency. Does not use NADPH. May be the initial\nCC       enzyme of the putative L-fucose degradation pathway in mammals.\nCC       {ECO:0000250|UniProtKB:Q9BPX1}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81519, ChEBI:CHEBI:15378, ChEBI:CHEBI:46994,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:194242;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81520;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81523, ChEBI:CHEBI:15378, ChEBI:CHEBI:37619,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:182410;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81524;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0047834; F:D-threo-aldose 1-dehydrogenase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0004303; F:estradiol 17-beta-dehydrogenase [NAD(P)+] activity; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003917\nname: DNA topoisomerase type I (single strand cut, ATP-independent) activity\nnamespace: molecular_function\ndef: \"Catalysis of a DNA topological transformation by transiently cleaving one DNA strand at a time to allow passage of another strand; changes the linking number by +1 per catalytic cycle.\" [PMID:8811192]\ncomment: Note that a further distinction, between type IA and type IB topoisomerases, is based on sequence or structural similarity between gene products that possess type I catalytic activity.\nsynonym: \"deoxyribonucleate topoisomerase\" BROAD []\nsynonym: \"DNA topoisomerase I activity\" NARROW []\nsynonym: \"nicking-closing enzyme activity\" RELATED [EC:5.6.2.1]\nsynonym: \"omega-protein activity\" RELATED [EC:5.6.2.1]\nsynonym: \"relaxing enzyme activity\" RELATED [EC:5.6.2.1]\nsynonym: \"swivelase activity\" RELATED [EC:5.6.2.1]\nsynonym: \"topoisomerase\" BROAD [EC:5.6.2.1]\nsynonym: \"type I DNA topoisomerase activity\" EXACT []\nsynonym: \"type I topoisomerase activity\" EXACT []\nsynonym: \"untwisting enzyme activity\" RELATED [EC:5.6.2.1]\nxref: EC:5.6.2.1\nxref: MetaCyc:5.99.1.2-RXN\nxref: Reactome:R-HSA-9914922 \"TOP3A (Topoisomerase 3a) decatenates mitochondrial DNA\"\nis_a: GO:0003916 ! DNA topoisomerase activity\nproperty_value: skos:exactMatch EC:5.6.2.1\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003917",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 31305-31326",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0004045\nname: peptidyl-tRNA hydrolase activity\nnamespace: molecular_function\nalt_id: GO:0019850\nalt_id: GO:0019851\ndef: \"Catalysis of the reaction: an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H+.\" [RHEA:54448]\nsynonym: \"aminoacyl-transfer ribonucleate hydrolase activity\" RELATED [EC:3.1.1.29]\nsynonym: \"aminoacyl-tRNA aminoacylhydrolase activity\" RELATED [EC:3.1.1.29]\nsynonym: \"aminoacyl-tRNA hydrolase reaction\" EXACT []\nsynonym: \"D-tyrosyl-tRNA hydrolase activity\" NARROW [PMID:15292242]\nsynonym: \"N-substituted aminoacyl transfer RNA hydrolase activity\" RELATED [EC:3.1.1.29]\nxref: EC:3.1.1.29\nxref: MetaCyc:AMINOCYL-TRNA-HYDROLASE-RXN\nxref: Reactome:R-HSA-9937374 \"MTRFR:MTRES1:39S ribosomal subunit:mRNA:peptidyl-tRNA:MALSU1:MIEF1:NDUFAB1 dissociates\"\nxref: Reactome:R-HSA-9937719 \"ICT1 hydrolyzes the peptidyl-tRNA bond of the nascent polypeptide\"\nxref: RHEA:54448\nxref: RHEA:81979\nis_a: GO:0052689 ! carboxylic ester hydrolase activity\nis_a: GO:0140101 ! catalytic activity, acting on a tRNA\nproperty_value: skos:exactMatch EC:3.1.1.29\nproperty_value: skos:exactMatch RHEA:54448\nproperty_value: skos:narrowMatch RHEA:81979\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004045",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 34055-34078",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0016651\nname: oxidoreductase activity, acting on NAD(P)H\nnamespace: molecular_function\ndef: \"Catalysis of an oxidation-reduction (redox) reaction in which NADH or NADPH acts as a hydrogen or electron donor and reduces a hydrogen or electron acceptor.\" [GOC:ai]\nsynonym: \"NAD(P)H dehydrogenase\" NARROW []\nsynonym: \"oxidoreductase activity, acting on NADH or NADPH\" RELATED []\nsynonym: \"oxidoreductase activity, acting on NADH or NADPH, other acceptor\" NARROW []\nxref: EC:1.6.-.-\nxref: Reactome:R-HSA-109343 \"Reduction of 2-trans-4-cis-decadienoyl-CoA to form 3-trans-decenoyl-CoA\"\nxref: Reactome:R-HSA-8956458 \"RNLS:FAD oxidises dh-beta-NAD to NAD+\"\nis_a: GO:0016491 ! oxidoreductase activity\nproperty_value: skos:exactMatch EC:1.6.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016651",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 128650-128663",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0047834\nname: D-threo-aldose 1-dehydrogenase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a D-threo-aldose + NAD+ = a D-threo-aldono-1,5-lactone + NADH.\" [EC:1.1.1.122, MetaCyc:D-THREO-ALDOSE-1-DEHYDROGENASE-RXN]\nsynonym: \"(2S,3R)-aldose dehydrogenase activity\" RELATED [EC:1.1.1.122]\nsynonym: \"D-threo-aldose:NAD+ 1-oxidoreductase activity\" RELATED [EC:1.1.1.122]\nsynonym: \"dehydrogenase, L-fucose\" RELATED [EC:1.1.1.122]\nsynonym: \"L-fucose (D-arabinose) dehydrogenase activity\" RELATED [EC:1.1.1.122]\nsynonym: \"L-fucose dehydrogenase activity\" RELATED [EC:1.1.1.122]\nxref: EC:1.1.1.122\nxref: MetaCyc:D-THREO-ALDOSE-1-DEHYDROGENASE-RXN\nxref: RHEA:19645\nxref: RHEA:81515\nxref: RHEA:81519\nxref: RHEA:81523\nis_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor\nproperty_value: skos:exactMatch EC:1.1.1.122\nproperty_value: skos:exactMatch RHEA:19645\nproperty_value: skos:narrowMatch RHEA:81515\nproperty_value: skos:narrowMatch RHEA:81519\nproperty_value: skos:narrowMatch RHEA:81523\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0047834",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 296916-296938",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 113. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
