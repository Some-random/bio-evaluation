# GO_cellular_component_0126

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0126.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — mitochondrial outer membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRAGRVRPLRASDMKKDVRILLVGEPRVGKTSLIMSLVSEEFPEEVPPRAEEITIPADVTPERVPTHIVDYSEAEQSDEQLHQEISQANVICIVYAVNNKHSIDKVTSRWIPLINERTDKDSRLPLILVGNKSDLVEYSSMETILPIMNQYTEIETCVECSAKNLKNISELFYYAQKAVLHPTGPLYCPEEKEMKPACIKALTRIFKISDQDNDGTLNDAELNFFQRICFNTPLAPQALEDVKNVVRKHLSDGVADSGLTLRGFLFLHTLFIQRGRHETTWTVLRRFGYDDDLDLTPEYLFPLLKIPPDCTTELNHHAYLFLQSTFDKHDLDRDCALSPDELKDLFQVFPYIPWGPDVNNTVCTNESGWITYQGFLSQWTLTTYLDVQRCLEYLGYLGYSILTEQESQASAITVTRDKKIDLQKKQTQRNVFRCNVIGVKGCGKTGVLQSLLGRNLMRQKKIRDDHKSYYAINTVYVYGQEKYLLLHDISESEFLTEAEIVCDVVCLVYDVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLKSSTFWLRASFGATVFAVVGFAMYRALLKQR

[Multiple Choices]
A. nuclear envelope
B. vitelline envelope
C. mitochondrial outer membrane
D. nematocyst
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates the protein to the mitochondrial outer membrane. The GO annotation is computationally transferred (ISS), and the subcellular-location annotation is based on another UniProt protein, so this supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the characteristic organization of a Miro/RHOT-family mitochondrial Rho GTPase: GTPase motifs, EF-hand-like regions, and a hydrophobic C-terminal membrane anchor. Knowledge of this protein family and its membrane-anchoring pattern provides a meaningful basis for choosing the mitochondrial outer membrane over the nuclear envelope, vitelline envelope, or nematocyst.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence architecture distinguishes the offered mitochondrial option without requiring the exact protein's database annotation. The inference is strong but does not itself constitute experimental localization evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the family-level sequence features favor mitochondrial outer-membrane localization; the other choices are not comparably supported.


### Important caveats

- The supplied evidence supports the key through annotations that are computationally transferred or based on a homolog, rather than demonstrating direct experimental localization for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the characteristic organization of a Miro/RHOT-family mitochondrial Rho GTPase: GTPase motifs, EF-hand-like regions, and a hydrophobic C-terminal membrane anchor. Knowledge of this protein family and its membrane-anchoring pattern provides a meaningful basis for choosing the mitochondrial outer membrane over the nuclear envelope, vitelline envelope, or nematocyst.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence architecture distinguishes the offered mitochondrial option without requiring the exact protein's database annotation. The inference is strong but does not itself constitute experimental localization evidence."
  },
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the mitochondrial outer membrane. The GO annotation is computationally transferred (ISS), and the subcellular-location annotation is based on another UniProt protein, so this supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied evidence supports the key through annotations that are computationally transferred or based on a homolog, rather than demonstrating direct experimental localization for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the family-level sequence features favor mitochondrial outer-membrane localization; the other choices are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the mitochondrial outer membrane. The GO annotation is computationally transferred (ISS), and the subcellular-location annotation is based on another UniProt protein, so this supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "C8", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the characteristic organization of a Miro/RHOT-family mitochondrial Rho GTPase: GTPase motifs, EF-hand-like regions, and a hydrophobic C-terminal membrane anchor. Knowledge of this protein family and its membrane-anchoring pattern provides a meaningful basis for choosing the mitochondrial outer membrane over the nuclear envelope, vitelline envelope, or nematocyst.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence architecture distinguishes the offered mitochondrial option without requiring the exact protein's database annotation. The inference is strong but does not itself constitute experimental localization evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the family-level sequence features favor mitochondrial outer-membrane localization; the other choices are not comparably supported."
  },
  "important_caveats": [
    "The supplied evidence supports the key through annotations that are computationally transferred or based on a homolog, rather than demonstrating direct experimental localization for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A1L1L6, MIRO1_RAT) annotates the protein as 'Mitochondrial Rho GTPase' (MIRO-1) with subcellular location 'Mitochondrion outer membrane; Single-pass type IV membrane protein' and GO:0005741 (mitochondrial outer membrane). However, the evidence code is ECO:0000250/ISS:UniProtKB (inferred from similarity to human Q8IXI2), not direct experimental evidence. The protein name itself contains 'Mitochondrial,' and the annotation is consistent with well-established family knowledge about MIRO/RHOT proteins. The key is supported by annotation, though the annotation is computational inference from homolog similarity rather than independent experimental validation.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays recognizable features of the MIRO/RHOT protein family: (1) Two Ras-superfamily GTPase domains with identifiable P-loop (GKTSLIMSL, matching GxxxxGK&#91;ST&#93; motif), NKxD switch-region motifs (NKSDLVEYSS), and downstream effector-binding regions; (2) Two EF-hand calcium-binding domains in the central region (recognizable by the DxDxDGxD loop patterns in 'DVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLK'); (3) A C-terminal hydrophobic transmembrane segment ('GATVFAVVGFAMYRALLKQR') consistent with a single-pass TM anchor. The combination of two GTPase domains + two EF-hands + C-terminal TM is the hallmark architecture of MIRO/RHOT proteins, a well-characterized family of mitochondrial outer membrane proteins involved in mitochondrial trafficking. This family-level knowledge allows elimination of distractors: nematocyst (D) is a cnidarian-specific organelle, impossible in a mammalian sequence; vitelline envelope (B) is an extracellular egg-coat glycoprotein structure, inconsistent with an intracellular GTPase; nuclear envelope (A) would require nuclear targeting signals absent here. The TM anchor at the C-terminus is specifically associated with outer membrane insertion (type IV topology), not inner membrane or matrix localization.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the Ras-like GTPase motifs, EF-hand calcium-binding domains, and C-terminal hydrophobic TM segment from the sequence. The combination of these three domain types is a well-established signature of the MIRO/RHOT protein family, which is broadly known from other species (human, Drosophila, yeast) to localize to the mitochondrial outer membrane. This family-level inference meaningfully distinguishes choice C from the alternatives without requiring recall of this specific rat protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are highly distinct: nuclear envelope (A), vitelline envelope (B), mitochondrial outer membrane (C), and nematocyst (D). The protein's domain architecture (GTPase + EF-hand + TM) and mammalian origin clearly point to C and eliminate B (egg coat glycoprotein), D (cnidarian stinging organelle), and A (would require NLS or nuclear membrane targeting). No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation for mitochondrial outer membrane is based on ISS/ECO:0000250 (similarity to human MIRO1), not direct experimental evidence for this rat sequence. However, the family-level inference from transferable knowledge is strong and well-supported.
- The protein also carries GO annotations for cytoplasm, cytoplasmic stress granule, and ribonucleoprotein complex (ISO:RGD), but these are secondary locations and the question asks for the primary cellular component.
- The reviewer identified the accession A1L1L6 from dataset metadata, but the model was given only the sequence. The reasoning above relies solely on sequence features and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays recognizable features of the MIRO/RHOT protein family: (1) Two Ras-superfamily GTPase domains with identifiable P-loop (GKTSLIMSL, matching GxxxxGK[ST] motif), NKxD switch-region motifs (NKSDLVEYSS), and downstream effector-binding regions; (2) Two EF-hand calcium-binding domains in the central region (recognizable by the DxDxDGxD loop patterns in 'DVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLK'); (3) A C-terminal hydrophobic transmembrane segment ('GATVFAVVGFAMYRALLKQR') consistent with a single-pass TM anchor. The combination of two GTPase domains + two EF-hands + C-terminal TM is the hallmark architecture of MIRO/RHOT proteins, a well-characterized family of mitochondrial outer membrane proteins involved in mitochondrial trafficking. This family-level knowledge allows elimination of distractors: nematocyst (D) is a cnidarian-specific organelle, impossible in a mammalian sequence; vitelline envelope (B) is an extracellular egg-coat glycoprotein structure, inconsistent with an intracellular GTPase; nuclear envelope (A) would require nuclear targeting signals absent here. The TM anchor at the C-terminus is specifically associated with outer membrane insertion (type IV topology), not inner membrane or matrix localization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the Ras-like GTPase motifs, EF-hand calcium-binding domains, and C-terminal hydrophobic TM segment from the sequence. The combination of these three domain types is a well-established signature of the MIRO/RHOT protein family, which is broadly known from other species (human, Drosophila, yeast) to localize to the mitochondrial outer membrane. This family-level inference meaningfully distinguishes choice C from the alternatives without requiring recall of this specific rat protein's database entry."
  },
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A1L1L6, MIRO1_RAT) annotates the protein as 'Mitochondrial Rho GTPase' (MIRO-1) with subcellular location 'Mitochondrion outer membrane; Single-pass type IV membrane protein' and GO:0005741 (mitochondrial outer membrane). However, the evidence code is ECO:0000250/ISS:UniProtKB (inferred from similarity to human Q8IXI2), not direct experimental evidence. The protein name itself contains 'Mitochondrial,' and the annotation is consistent with well-established family knowledge about MIRO/RHOT proteins. The key is supported by annotation, though the annotation is computational inference from homolog similarity rather than independent experimental validation."
  },
  "important_caveats": [
    "The UniProt annotation for mitochondrial outer membrane is based on ISS/ECO:0000250 (similarity to human MIRO1), not direct experimental evidence for this rat sequence. However, the family-level inference from transferable knowledge is strong and well-supported.",
    "The protein also carries GO annotations for cytoplasm, cytoplasmic stress granule, and ribonucleoprotein complex (ISO:RGD), but these are secondary locations and the question asks for the primary cellular component.",
    "The reviewer identified the accession A1L1L6 from dataset metadata, but the model was given only the sequence. The reasoning above relies solely on sequence features and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are highly distinct: nuclear envelope (A), vitelline envelope (B), mitochondrial outer membrane (C), and nematocyst (D). The protein's domain architecture (GTPase + EF-hand + TM) and mammalian origin clearly point to C and eliminate B (egg coat glycoprotein), D (cnidarian stinging organelle), and A (would require NLS or nuclear membrane targeting). No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A1L1L6, MIRO1_RAT) annotates the protein as 'Mitochondrial Rho GTPase' (MIRO-1) with subcellular location 'Mitochondrion outer membrane; Single-pass type IV membrane protein' and GO:0005741 (mitochondrial outer membrane). However, the evidence code is ECO:0000250/ISS:UniProtKB (inferred from similarity to human Q8IXI2), not direct experimental evidence. The protein name itself contains 'Mitochondrial,' and the annotation is consistent with well-established family knowledge about MIRO/RHOT proteins. The key is supported by annotation, though the annotation is computational inference from homolog similarity rather than independent experimental validation.",
    "evidence_ids": ["C5", "C8", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays recognizable features of the MIRO/RHOT protein family: (1) Two Ras-superfamily GTPase domains with identifiable P-loop (GKTSLIMSL, matching GxxxxGK[ST] motif), NKxD switch-region motifs (NKSDLVEYSS), and downstream effector-binding regions; (2) Two EF-hand calcium-binding domains in the central region (recognizable by the DxDxDGxD loop patterns in 'DVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLK'); (3) A C-terminal hydrophobic transmembrane segment ('GATVFAVVGFAMYRALLKQR') consistent with a single-pass TM anchor. The combination of two GTPase domains + two EF-hands + C-terminal TM is the hallmark architecture of MIRO/RHOT proteins, a well-characterized family of mitochondrial outer membrane proteins involved in mitochondrial trafficking. This family-level knowledge allows elimination of distractors: nematocyst (D) is a cnidarian-specific organelle, impossible in a mammalian sequence; vitelline envelope (B) is an extracellular egg-coat glycoprotein structure, inconsistent with an intracellular GTPase; nuclear envelope (A) would require nuclear targeting signals absent here. The TM anchor at the C-terminus is specifically associated with outer membrane insertion (type IV topology), not inner membrane or matrix localization.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the Ras-like GTPase motifs, EF-hand calcium-binding domains, and C-terminal hydrophobic TM segment from the sequence. The combination of these three domain types is a well-established signature of the MIRO/RHOT protein family, which is broadly known from other species (human, Drosophila, yeast) to localize to the mitochondrial outer membrane. This family-level inference meaningfully distinguishes choice C from the alternatives without requiring recall of this specific rat protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are highly distinct: nuclear envelope (A), vitelline envelope (B), mitochondrial outer membrane (C), and nematocyst (D). The protein's domain architecture (GTPase + EF-hand + TM) and mammalian origin clearly point to C and eliminate B (egg coat glycoprotein), D (cnidarian stinging organelle), and A (would require NLS or nuclear membrane targeting). No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for mitochondrial outer membrane is based on ISS/ECO:0000250 (similarity to human MIRO1), not direct experimental evidence for this rat sequence. However, the family-level inference from transferable knowledge is strong and well-supported.",
    "The protein also carries GO annotations for cytoplasm, cytoplasmic stress granule, and ribonucleoprotein complex (ISO:RGD), but these are secondary locations and the question asks for the primary cellular component.",
    "The reviewer identified the accession A1L1L6 from dataset metadata, but the model was given only the sequence. The reasoning above relies solely on sequence features and family-level knowledge."
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
  "benchmark_sequence_length": 631,
  "benchmark_sequence_sha256": "a7756948eb1b32092363ec26631ecb58f113dac469b17c79f967f052e05b6ef8",
  "current_entry_audit": {
    "entryVersion": 149,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-02-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 631,
  "current_source_sequence_sha256": "a7756948eb1b32092363ec26631ecb58f113dac469b17c79f967f052e05b6ef8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 147,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A1L1L6",
  "selected_historical_entry_version": 147,
  "selected_historical_record_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "selected_historical_source_sequence_length": 631,
  "selected_historical_source_sequence_sha256": "a7756948eb1b32092363ec26631ecb58f113dac469b17c79f967f052e05b6ef8",
  "selected_historical_version": {
    "accession": "A1L1L6",
    "database": "Swiss-Prot",
    "entryVersion": 147,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MIRO1_RAT",
    "sequenceVersion": 1
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A1L1L6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":149,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-02-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rat\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAI29124.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"1307023\",\"source\":\"RGD\"}],\"value\":\"Ras homolog gene family member T1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IXI2\",\"source\":\"UniProtKB\"}],\"value\":\"3.6.5.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRNR037488\",\"source\":\"PIRNR\"}],\"value\":\"Mitochondrial Rho GTPase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"MIRO-1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IXI2\",\"source\":\"UniProtKB\"}],\"value\":\"Colocalizes with MGARP and RHOT2 at the mitochondria\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IXI2\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0172\",\"value\":\"Mitochondrion outer membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IXI2\",\"source\":\"UniProtKB\"}],\"id\":\"SL-9908\",\"value\":\"Single-pass type IV membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005737\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:RGD\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/22",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0010494\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytoplasmic stress granule\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:RGD\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/23",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005741\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrial outer membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/24",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:1990904\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:ribonucleoprotein complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:RGD\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/25",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H1",
  "excerpt": "ID   MIRO1_RAT               Reviewed;         631 AA.\nAC   A1L1L6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-FEB-2007, sequence version 1.\nDT   28-JAN-2026, entry version 147.\nDE   RecName: Full=Mitochondrial Rho GTPase {ECO:0000255|PIRNR:PIRNR037488};\nDE            Short=MIRO-1 {ECO:0000305};\nDE            EC=3.6.5.- {ECO:0000250|UniProtKB:Q8IXI2};\nDE   AltName: Full=Ras homolog gene family member T1 {ECO:0000312|RGD:1307023};\nGN   Name=Rhot1 {ECO:0000312|RGD:1307023};\nGN   Synonyms=Rnf135 {ECO:0000312|RGD:1307023};\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116 {ECO:0000312|EMBL:AAI29124.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H2",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Mitochondrion outer membrane\nCC       {ECO:0000250|UniProtKB:Q8IXI2}; Single-pass type IV membrane protein\nCC       {ECO:0000250|UniProtKB:Q8IXI2}. Note=Colocalizes with MGARP and RHOT2\nCC       at the mitochondria. {ECO:0000250|UniProtKB:Q8IXI2}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0005737; C:cytoplasm; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0010494; C:cytoplasmic stress granule; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005741; C:mitochondrial outer membrane; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 115-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:1990904; C:ribonucleoprotein complex; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005635\nname: nuclear envelope\nnamespace: cellular_component\nalt_id: GO:0005636\ndef: \"The double lipid bilayer that encloses the nucleus, separating its contents from the cytoplasm. It consists of an inner and outer nuclear membrane, with an intermembrane space (20-40 nm wide, also called the perinuclear space) between them. The envelope is supported by the nuclear lamina and contains nuclear pore complexes, which regulate molecular transport.\" [ISBN:0198547684, PMID:16164970]\nsubset: goslim_chembl\nsubset: goslim_generic\nsubset: goslim_plant\nxref: Wikipedia:Nuclear_envelope\nis_a: GO:0031967 ! organelle envelope\nrelationship: part_of GO:0005634 ! nucleus\nrelationship: part_of GO:0012505 ! endomembrane system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005635",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58026-58039",
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
  "excerpt": "[Term]\nid: GO:0005741\nname: mitochondrial outer membrane\nnamespace: cellular_component\ndef: \"The outer, i.e. cytoplasm-facing, lipid bilayer of the mitochondrial envelope.\" [GOC:ai]\nsynonym: \"mitochondrion outer membrane\" EXACT []\nsynonym: \"outer mitochondrial membrane\" EXACT []\nsynonym: \"outer mitochondrion membrane\" EXACT []\nxref: NIF_Subcellular:sao1289741256\nxref: Wikipedia:Outer_mitochondrial_membrane\nis_a: GO:0031966 ! mitochondrial membrane\nis_a: GO:0031968 ! organelle outer membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005741",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59009-59021",
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
  "excerpt": "[Term]\nid: GO:0042151\nname: nematocyst\nnamespace: cellular_component\ndef: \"An organelle found in cnidoblast (nematoblast) cells. When matured, these stinging organelles store toxins and can deliver them when the cnidocil (a short extension of the cnidocyst) is stimulated by a prey or another stimulus.\" [DOI:10.1139/z02-135, GOC:jl]\nsynonym: \"cnidocyst\" EXACT []\nxref: Wikipedia:Cnidocyte\nis_a: GO:0043232 ! intracellular membraneless organelle\nrelationship: part_of GO:0005938 ! cell cortex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042151",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 234754-234763",
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
  "excerpt": "[Term]\nid: GO:0060388\nname: vitelline envelope\nnamespace: cellular_component\ndef: \"A glycoprotein-based structure that lies outside the plasma membrane and surrounds the egg before fertilization.\" [GOC:dph, ISBN:0878932437]\nsynonym: \"fertilization membrane\" RELATED []\nis_a: GO:0035805 ! egg coat\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0060388",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 347268-347275",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 126. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
