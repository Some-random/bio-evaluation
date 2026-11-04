# active_site_0132

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0132.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 67 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDRKVQVLDFIKINPAGNITILIDNFDIYDKNIPKLSEEIMKETNLYAEQVGFIKDSHLQMMGGEFCGNASRAFASLLAFRDKDFSKQKNYNITCSGESKVLDVDVRNDGAKNKFLAKIKMPKFLSLEEINVDEYKLGLVRFSGINHFIFNIKENKETSFENIIDLVKKYLSNEEYSAFGIMFFDSDNLSMKPYVYVKEVGSGVYENSCASGTTALGYYLKKCKNLDRAKIVQPNGWLEYIIENDEMYIDGPVEIIAEGKIYIGK

[Multiple Choices]
A. Position 2428 (For thioesterase activity)
B. Position 67 (Proton acceptor)
C. Position 241 (Lowers pKa of active site Tyr)
D. Position 38 (Nucleophile)
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

> The sequence-matched historical UniProt record annotates residue 67 as the proton acceptor, matching choice B. This is a curated, literature-cited annotation; the annotation itself is not a direct experimental measurement.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model could recognize a compact, cofactor-independent racemase pattern: the sequence has cysteines at positions 67 and 209, consistent with the paired catalytic thiols used by cysteine-dependent racemases for acid-base chemistry. That makes the cysteine at 67 a credible catalytic residue and distinguishes choice B from the out-of-range position in A, the glutamate at position 38 proposed as a nucleophile in D, and the unrelated Tyr-pKa claim in C. Homologous-family knowledge can further support the proton-acceptor assignment, though that role is less obvious from the sequence alone than the catalytic-Cys inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choices and sequence provide a meaningful family/mechanism-based route to B, without requiring recall of this exact protein's database annotation. The precise acceptor-versus-donor assignment is the main uncertainty, not a reason to require target-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B is consistent with the supported active-site role among the offered choices.


### Important caveats

- The UniProt active-site note is evidence for the expected answer, but its ECO:0000305 evidence code denotes a literature-based annotation rather than direct experimental evidence in the excerpt.
- The family-level inference supports B probabilistically; the exact assignment of the two catalytic cysteines' proton-transfer roles is not directly established by the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize a compact, cofactor-independent racemase pattern: the sequence has cysteines at positions 67 and 209, consistent with the paired catalytic thiols used by cysteine-dependent racemases for acid-base chemistry. That makes the cysteine at 67 a credible catalytic residue and distinguishes choice B from the out-of-range position in A, the glutamate at position 38 proposed as a nucleophile in D, and the unrelated Tyr-pKa claim in C. Homologous-family knowledge can further support the proton-acceptor assignment, though that role is less obvious from the sequence alone than the catalytic-Cys inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choices and sequence provide a meaningful family/mechanism-based route to B, without requiring recall of this exact protein's database annotation. The precise acceptor-versus-donor assignment is the main uncertainty, not a reason to require target-specific lookup."
  },
  "case_id": "active_site_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates residue 67 as the proton acceptor, matching choice B. This is a curated, literature-cited annotation; the annotation itself is not a direct experimental measurement."
  },
  "important_caveats": [
    "The UniProt active-site note is evidence for the expected answer, but its ECO:0000305 evidence code denotes a literature-based annotation rather than direct experimental evidence in the excerpt.",
    "The family-level inference supports B probabilistically; the exact assignment of the two catalytic cysteines' proton-transfer roles is not directly established by the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B is consistent with the supported active-site role among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates residue 67 as the proton acceptor, matching choice B. This is a curated, literature-cited annotation; the annotation itself is not a direct experimental measurement.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could recognize a compact, cofactor-independent racemase pattern: the sequence has cysteines at positions 67 and 209, consistent with the paired catalytic thiols used by cysteine-dependent racemases for acid-base chemistry. That makes the cysteine at 67 a credible catalytic residue and distinguishes choice B from the out-of-range position in A, the glutamate at position 38 proposed as a nucleophile in D, and the unrelated Tyr-pKa claim in C. Homologous-family knowledge can further support the proton-acceptor assignment, though that role is less obvious from the sequence alone than the catalytic-Cys inference.",
    "missing_item_specific_fact": "",
    "reason": "The choices and sequence provide a meaningful family/mechanism-based route to B, without requiring recall of this exact protein's database annotation. The precise acceptor-versus-donor assignment is the main uncertainty, not a reason to require target-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B is consistent with the supported active-site role among the offered choices."
  },
  "important_caveats": [
    "The UniProt active-site note is evidence for the expected answer, but its ECO:0000305 evidence code denotes a literature-based annotation rather than direct experimental evidence in the excerpt.",
    "The family-level inference supports B probabilistically; the exact assignment of the two catalytic cysteines' proton-transfer roles is not directly established by the sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) explicitly lists Active site 67 as 'Proton acceptor' with experimental evidence (ECO:0000305|PubMed:39424140, PDB 9CR1/9CR6). The reference (C7, H2) confirms X-ray crystallography of C67S and C209S mutants and mutagenesis studies. Position 67 in the 265-aa sequence is indeed Cys, consistent with the known amino acid racemase mechanism.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can eliminate option A immediately since the protein is only 265 residues long, making position 2428 impossible. Among the remaining options, general knowledge of amino acid racemase catalysis (learned from glutamate racemase, alanine racemase, and other family members) establishes that Cys residues serve as proton acceptor and proton donor in the two-step racemization mechanism. Scanning the sequence reveals Cys at position 67 and Cys at position 209. Option B pairs position 67 (Cys) with 'Proton acceptor,' which is mechanistically consistent with amino acid racemase chemistry. Option D pairs position 38 (Glu) with 'Nucleophile,' which does not match racemase catalysis. Option C pairs position 241 (Ile) with 'Lowers pKa of active site Tyr,' which is mechanistically incoherent (Ile has no side-chain chemistry to modulate Tyr pKa). Thus, family-level knowledge of racemase mechanisms combined with sequence inspection meaningfully distinguishes B from the other offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The model can use transferable knowledge: (1) eliminate A by length, (2) recognize that amino acid racemases universally employ Cys as proton acceptor/donor (glutamate racemase, alanine racemase, proline racemase family), (3) identify Cys at position 67 in the sequence, and (4) match the 'Proton acceptor' mechanistic label to the Cys residue. The other options are mechanistically inconsistent with racemase chemistry or reference non-existent positions.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is trivially impossible. Option C references Ile at 241 with a pKa-lowering role that has no biochemical basis. Option D assigns nucleophile role to Glu at 38, inconsistent with racemase mechanism. Only B is mechanistically coherent with the Cys at position 67 and amino acid racemase catalysis.


### Important caveats

- The protein is annotated as a histidine racemase (EC 5.1.1.24), a cofactor-independent enzyme. Recognition of this specific enzyme class from sequence alone is non-trivial, but the mechanistic language in the answer choices ('Proton acceptor') and the presence of catalytic Cys residues provide sufficient clues for family-level inference.
- The UniProt annotation is based on a 2024 publication (PubMed:39424140) and PDB structures 9CR1/9CR6, indicating experimental rather than purely computational evidence.
- Position 209 (also Cys, proton donor) is not offered as an alternative, reducing ambiguity between the two catalytic Cys residues.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate option A immediately since the protein is only 265 residues long, making position 2428 impossible. Among the remaining options, general knowledge of amino acid racemase catalysis (learned from glutamate racemase, alanine racemase, and other family members) establishes that Cys residues serve as proton acceptor and proton donor in the two-step racemization mechanism. Scanning the sequence reveals Cys at position 67 and Cys at position 209. Option B pairs position 67 (Cys) with 'Proton acceptor,' which is mechanistically consistent with amino acid racemase chemistry. Option D pairs position 38 (Glu) with 'Nucleophile,' which does not match racemase catalysis. Option C pairs position 241 (Ile) with 'Lowers pKa of active site Tyr,' which is mechanistically incoherent (Ile has no side-chain chemistry to modulate Tyr pKa). Thus, family-level knowledge of racemase mechanisms combined with sequence inspection meaningfully distinguishes B from the other offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The model can use transferable knowledge: (1) eliminate A by length, (2) recognize that amino acid racemases universally employ Cys as proton acceptor/donor (glutamate racemase, alanine racemase, proline racemase family), (3) identify Cys at position 67 in the sequence, and (4) match the 'Proton acceptor' mechanistic label to the Cys residue. The other options are mechanistically inconsistent with racemase chemistry or reference non-existent positions."
  },
  "case_id": "active_site_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly lists Active site 67 as 'Proton acceptor' with experimental evidence (ECO:0000305|PubMed:39424140, PDB 9CR1/9CR6). The reference (C7, H2) confirms X-ray crystallography of C67S and C209S mutants and mutagenesis studies. Position 67 in the 265-aa sequence is indeed Cys, consistent with the known amino acid racemase mechanism."
  },
  "important_caveats": [
    "The protein is annotated as a histidine racemase (EC 5.1.1.24), a cofactor-independent enzyme. Recognition of this specific enzyme class from sequence alone is non-trivial, but the mechanistic language in the answer choices ('Proton acceptor') and the presence of catalytic Cys residues provide sufficient clues for family-level inference.",
    "The UniProt annotation is based on a 2024 publication (PubMed:39424140) and PDB structures 9CR1/9CR6, indicating experimental rather than purely computational evidence.",
    "Position 209 (also Cys, proton donor) is not offered as an alternative, reducing ambiguity between the two catalytic Cys residues."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is trivially impossible. Option C references Ile at 241 with a pKa-lowering role that has no biochemical basis. Option D assigns nucleophile role to Glu at 38, inconsistent with racemase mechanism. Only B is mechanistically coherent with the Cys at position 67 and amino acid racemase catalysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id": "active_site_0132", "expected_answer_check": {"judgment": "supported", "reason": "The UniProt annotation (C5, H3) explicitly lists Active site 67 as 'Proton acceptor' with experimental evidence (ECO:0000305|PubMed:39424140, PDB 9CR1/9CR6). The reference (C7, H2) confirms X-ray crystallography of C67S and C209S mutants and mutagenesis studies. Position 67 in the 265-aa sequence is indeed Cys, consistent with the known amino acid racemase mechanism.", "evidence_ids": ["C5", "C6", "C7", "H3", "H4"]}, "answerability_check": {"judgment": "reasoning_supported", "discriminating_biological_argument": "A knowledgeable model can eliminate option A immediately since the protein is only 265 residues long, making position 2428 impossible. Among the remaining options, general knowledge of amino acid racemase catalysis (learned from glutamate racemase, alanine racemase, and other family members) establishes that Cys residues serve as proton acceptor and proton donor in the two-step racemization mechanism. Scanning the sequence reveals Cys at position 67 and Cys at position 209. Option B pairs position 67 (Cys) with 'Proton acceptor,' which is mechanistically consistent with amino acid racemase chemistry. Option D pairs position 38 (Glu) with 'Nucleophile,' which does not match racemase catalysis. Option C pairs position 241 (Ile) with 'Lowers pKa of active site Tyr,' which is mechanistically incoherent (Ile has no side-chain chemistry to modulate Tyr pKa). Thus, family-level knowledge of racemase mechanisms combined with sequence inspection meaningfully distinguishes B from the other offered choices.", "missing_item_specific_fact": "", "reason": "The model can use transferable knowledge: (1) eliminate A by length, (2) recognize that amino acid racemases universally employ Cys as proton acceptor/donor (glutamate racemase, alanine racemase, proline racemase family), (3) identify Cys at position 67 in the sequence, and (4) match the 'Proton acceptor' mechanistic label to the Cys residue. The other options are mechanistically inconsistent with racemase chemistry or reference non-existent positions."}, "question_ambiguity": {"multiple_defensible_options": [], "reason": "Option A is trivially impossible. Option C references Ile at 241 with a pKa-lowering role that has no biochemical basis. Option D assigns nucleophile role to Glu at 38, inconsistent with racemase mechanism. Only B is mechanistically coherent with the Cys at position 67 and amino acid racemase catalysis."}, "important_caveats": ["The protein is annotated as a histidine racemase (EC 5.1.1.24), a cofactor-independent enzyme. Recognition of this specific enzyme class from sequence alone is non-trivial, but the mechanistic language in the answer choices ('Proton acceptor') and the presence of catalytic Cys residues provide sufficient clues for family-level inference.", "The UniProt annotation is based on a 2024 publication (PubMed:39424140) and PDB structures 9CR1/9CR6, indicating experimental rather than purely computational evidence.", "Position 209 (also Cys, proton donor) is not offered as an alternative, reducing ambiguity between the two catalytic Cys residues."]}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 265,
  "benchmark_sequence_sha256": "366955426ff1f55c671654b2e899936080724ffe2dc1099a5aecf063554e039c",
  "current_entry_audit": {
    "entryVersion": 81,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 265,
  "current_source_sequence_sha256": "366955426ff1f55c671654b2e899936080724ffe2dc1099a5aecf063554e039c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 79,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8RI81",
  "selected_historical_entry_version": 79,
  "selected_historical_record_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "selected_historical_source_sequence_length": 265,
  "selected_historical_source_sequence_sha256": "366955426ff1f55c671654b2e899936080724ffe2dc1099a5aecf063554e039c",
  "selected_historical_version": {
    "accession": "Q8RI81",
    "database": "Swiss-Prot",
    "entryVersion": 79,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HISR_FUSNN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8RI81\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":81,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Fusobacteriati\",\"Fusobacteriota\",\"Fusobacteriia\",\"Fusobacteriales\",\"Fusobacteriaceae\",\"Fusobacterium\"],\"scientificName\":\"Fusobacterium nucleatum subsp. nucleatum (strain ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355)\",\"taxonId\":190304}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"value\":\"5.1.1.24\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"value\":\"Histidine racemase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":67},\"start\":{\"modifier\":\"EXACT\",\"value\":67}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":209},\"start\":{\"modifier\":\"EXACT\",\"value\":209}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Lamer T.\",\"Chen P.\",\"Venter M.J.\",\"van Belkum M.J.\",\"Wijewardane A.\",\"Wu C.\",\"Lemieux M.J.\",\"Vederas J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39424140\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107896\"}],\"citationType\":\"journal article\",\"firstPage\":\"107896\",\"id\":\"39424140\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107896\",\"publicationDate\":\"2024\",\"title\":\"Discovery, characterization, and structure of a cofactor-independent histidine racemase from the oral pathogen Fusobacterium nucleatum.\",\"volume\":\"300\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9CR1\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9CR6\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"ACTIVE SITE\",\"MUTAGENESIS OF CYS-67 AND CYS-209\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H1",
  "excerpt": "ID   HISR_FUSNN              Reviewed;         265 AA.\nAC   Q8RI81;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2002, sequence version 1.\nDT   28-JAN-2026, entry version 79.\nDE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};\nDE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};\nGN   Name=hisR {ECO:0000303|PubMed:39424140};\nGN   OrderedLocusNames=FN1732 {ECO:0000312|EMBL:AAL93847.1};\nOS   Fusobacterium nucleatum subsp. nucleatum (strain ATCC 25586 / DSM 15643 /\nOS   BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355).\nOC   Bacteria; Fusobacteriati; Fusobacteriota; Fusobacteriia; Fusobacteriales;\nOC   Fusobacteriaceae; Fusobacterium.\nOX   NCBI_TaxID=190304;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0007744|PDB:9CR1, ECO:0007744|PDB:9CR6}\nRP   X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209,\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF CYS-67 AND CYS-209.\nRC   STRAIN=ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC\nRC   2640 / LMG 13131 / VPI 4355;\nRX   PubMed=39424140; DOI=10.1016/j.jbc.2024.107896;\nRA   Lamer T., Chen P., Venter M.J., van Belkum M.J., Wijewardane A., Wu C.,\nRA   Lemieux M.J., Vederas J.C.;\nRT   \"Discovery, characterization, and structure of a cofactor-independent\nRT   histidine racemase from the oral pathogen Fusobacterium nucleatum.\";\nRL   J. Biol. Chem. 300:107896-107896(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        67\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000305|PubMed:39424140\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        209\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000305|PubMed:39424140\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 132. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
