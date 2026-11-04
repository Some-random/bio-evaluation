# active_site_0014

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0014.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 113 (Glycyl thioester intermediate)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MISAPSPDHLLLEQDLATPEIRCGEIEERWRHIRTSWPHVFFAVSAPQRPNGPKEFGFRFEYTGYRQTPVTAQLWDLEADAPLPHAKWPTGTYVVPSVFRKDWQQGNCLYIPCDRISIQGHTAWLNDHPSRLWQPARGIICYLEQLYELFNQGDYTGLVSA

[Multiple Choices]
A. Position 154 (Nucleophile)
B. Position 113 (Glycyl thioester intermediate)
C. Position 1142 (Proton donor; for dehydratase activity 1)
D. Position 4261 (For beta-ketoacyl synthase 3 activity)
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

> The sequence-matched UniProt record annotates position 113 as the active site for a glycyl thioester intermediate. Its cited reference concerns mutagenesis of Cys-113, though the supplied excerpts do not give the experimental result itself; the annotation is curator-supported rather than direct experimental evidence shown here.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The input sequence is 161 residues long, and position 113 is cysteine. A catalytic cysteine can form a thioester with a substrate's terminal glycine, making B a coherent transferable biochemical inference. Positions 1142 and 4261 are outside the sequence, while position 154 is tyrosine, which is a poor fit for the stated nucleophile role.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and the thioester mechanism described in the choices provide a meaningful basis for preferring B without needing the target's database record. This supports a plausible inference, not independent confirmation of the particular protein's activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other options are inconsistent with the sequence length or with the residue and mechanism at the stated position.


### Important caveats

- The evidence supports a sequence-matched database annotation citing a mutagenesis reference; the supplied excerpts do not independently establish the experiment's outcome.
- The option describes the glycyl thioester intermediate rather than explicitly naming cysteine as the residue type.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The input sequence is 161 residues long, and position 113 is cysteine. A catalytic cysteine can form a thioester with a substrate's terminal glycine, making B a coherent transferable biochemical inference. Positions 1142 and 4261 are outside the sequence, while position 154 is tyrosine, which is a poor fit for the stated nucleophile role.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the thioester mechanism described in the choices provide a meaningful basis for preferring B without needing the target's database record. This supports a plausible inference, not independent confirmation of the particular protein's activity."
  },
  "case_id": "active_site_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 113 as the active site for a glycyl thioester intermediate. Its cited reference concerns mutagenesis of Cys-113, though the supplied excerpts do not give the experimental result itself; the annotation is curator-supported rather than direct experimental evidence shown here."
  },
  "important_caveats": [
    "The evidence supports a sequence-matched database annotation citing a mutagenesis reference; the supplied excerpts do not independently establish the experiment's outcome.",
    "The option describes the glycyl thioester intermediate rather than explicitly naming cysteine as the residue type."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other options are inconsistent with the sequence length or with the residue and mechanism at the stated position."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 113 as the active site for a glycyl thioester intermediate. Its cited reference concerns mutagenesis of Cys-113, though the supplied excerpts do not give the experimental result itself; the annotation is curator-supported rather than direct experimental evidence shown here.",
    "evidence_ids": ["C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The input sequence is 161 residues long, and position 113 is cysteine. A catalytic cysteine can form a thioester with a substrate's terminal glycine, making B a coherent transferable biochemical inference. Positions 1142 and 4261 are outside the sequence, while position 154 is tyrosine, which is a poor fit for the stated nucleophile role.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the thioester mechanism described in the choices provide a meaningful basis for preferring B without needing the target's database record. This supports a plausible inference, not independent confirmation of the particular protein's activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other options are inconsistent with the sequence length or with the residue and mechanism at the stated position."
  },
  "important_caveats": [
    "The evidence supports a sequence-matched database annotation citing a mutagenesis reference; the supplied excerpts do not independently establish the experiment's outcome.",
    "The option describes the glycyl thioester intermediate rather than explicitly naming cysteine as the residue type."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A1I1NU27 annotates position 113 as 'Glycyl thioester intermediate' active site (evidence_id C5, H3). The evidence code is ECO:0000305 (inferred by similarity), but the cited reference (Hoer et al., Nature 2024, PubMed:39020165) explicitly mentions 'PROBABLE ACTIVE SITE, AND MUTAGENESIS OF CYS-113' (evidence_id C6, H2), indicating experimental support through mutagenesis. Position 113 in the provided sequence is indeed Cysteine (C), consistent with a thioester-forming catalytic residue in E2-like enzymes.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is only 161 residues long, immediately eliminating options C (position 1142) and D (position 4261) as physically impossible. Between A (position 154, 'Nucleophile') and B (position 113, 'Glycyl thioester intermediate'): a thioester intermediate chemically requires a sulfur-containing nucleophile, specifically a cysteine residue. Inspecting the sequence, position 113 is C (Cysteine) while position 154 is D (Aspartate). E2-like ubiquitin/ubiquitin-like conjugating enzymes universally use a catalytic cysteine to form a thioester intermediate with the substrate — this is a deeply conserved mechanistic feature across the E1/E2/E3 cascade in eukaryotes and analogous bacterial systems. The term 'glycyl thioester intermediate' specifically describes the mechanism of ubiquitin-like protein conjugation where the C-terminal glycine forms a thioester with the E2's active-site cysteine. A knowledgeable model can (1) eliminate out-of-range positions, (2) recognize that thioester chemistry mandates cysteine, and (3) verify position 113 is C while position 154 is D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of C and D is trivial (sequence length). The distinction between A and B relies on general biochemical knowledge: thioester intermediates require cysteine, and E2-like enzymes use catalytic cysteines. This is transferable knowledge about enzyme mechanisms and amino acid chemistry, not a fact unique to this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are impossible (positions exceed the 161-residue sequence). Between A and B, the thioester chemistry requirement for cysteine uniquely identifies position 113 (C) over position 154 (D). No ambiguity remains.


### Important caveats

- The UniProt annotation uses ECO:0000305 (inferred by similarity), but the primary reference includes mutagenesis data for Cys-113, providing experimental corroboration.
- Options C and D (positions 1142 and 4261) are absurdly out of range for a 161-residue protein, making them trivially eliminable and reducing the effective discrimination to A vs. B.
- The protein is annotated as a 'Bacterial E2-like ubiquitin protein BilB' from Collimonas sp., a recently characterized system (2024 Nature paper), so this is not a well-known textbook enzyme but the mechanistic principle (catalytic cysteine for thioester intermediates in E2-like enzymes) is broadly conserved.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is only 161 residues long, immediately eliminating options C (position 1142) and D (position 4261) as physically impossible. Between A (position 154, 'Nucleophile') and B (position 113, 'Glycyl thioester intermediate'): a thioester intermediate chemically requires a sulfur-containing nucleophile, specifically a cysteine residue. Inspecting the sequence, position 113 is C (Cysteine) while position 154 is D (Aspartate). E2-like ubiquitin/ubiquitin-like conjugating enzymes universally use a catalytic cysteine to form a thioester intermediate with the substrate — this is a deeply conserved mechanistic feature across the E1/E2/E3 cascade in eukaryotes and analogous bacterial systems. The term 'glycyl thioester intermediate' specifically describes the mechanism of ubiquitin-like protein conjugation where the C-terminal glycine forms a thioester with the E2's active-site cysteine. A knowledgeable model can (1) eliminate out-of-range positions, (2) recognize that thioester chemistry mandates cysteine, and (3) verify position 113 is C while position 154 is D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of C and D is trivial (sequence length). The distinction between A and B relies on general biochemical knowledge: thioester intermediates require cysteine, and E2-like enzymes use catalytic cysteines. This is transferable knowledge about enzyme mechanisms and amino acid chemistry, not a fact unique to this exact protein's annotation."
  },
  "case_id": "active_site_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A1I1NU27 annotates position 113 as 'Glycyl thioester intermediate' active site (evidence_id C5, H3). The evidence code is ECO:0000305 (inferred by similarity), but the cited reference (Hoer et al., Nature 2024, PubMed:39020165) explicitly mentions 'PROBABLE ACTIVE SITE, AND MUTAGENESIS OF CYS-113' (evidence_id C6, H2), indicating experimental support through mutagenesis. Position 113 in the provided sequence is indeed Cysteine (C), consistent with a thioester-forming catalytic residue in E2-like enzymes."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (inferred by similarity), but the primary reference includes mutagenesis data for Cys-113, providing experimental corroboration.",
    "Options C and D (positions 1142 and 4261) are absurdly out of range for a 161-residue protein, making them trivially eliminable and reducing the effective discrimination to A vs. B.",
    "The protein is annotated as a 'Bacterial E2-like ubiquitin protein BilB' from Collimonas sp., a recently characterized system (2024 Nature paper), so this is not a well-known textbook enzyme but the mechanistic principle (catalytic cysteine for thioester intermediates in E2-like enzymes) is broadly conserved."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are impossible (positions exceed the 161-residue sequence). Between A and B, the thioester chemistry requirement for cysteine uniquely identifies position 113 (C) over position 154 (D). No ambiguity remains."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A1I1NU27 annotates position 113 as 'Glycyl thioester intermediate' active site (evidence_id C5, H3). The evidence code is ECO:0000305 (inferred by similarity), but the cited reference (Hoer et al., Nature 2024, PubMed:39020165) explicitly mentions 'PROBABLE ACTIVE SITE, AND MUTAGENESIS OF CYS-113' (evidence_id C6, H2), indicating experimental support through mutagenesis. Position 113 in the provided sequence is indeed Cysteine (C), consistent with a thioester-forming catalytic residue in E2-like enzymes.",
    "evidence_ids": ["C5", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is only 161 residues long, immediately eliminating options C (position 1142) and D (position 4261) as physically impossible. Between A (position 154, 'Nucleophile') and B (position 113, 'Glycyl thioester intermediate'): a thioester intermediate chemically requires a sulfur-containing nucleophile, specifically a cysteine residue. Inspecting the sequence, position 113 is C (Cysteine) while position 154 is D (Aspartate). E2-like ubiquitin/ubiquitin-like conjugating enzymes universally use a catalytic cysteine to form a thioester intermediate with the substrate — this is a deeply conserved mechanistic feature across the E1/E2/E3 cascade in eukaryotes and analogous bacterial systems. The term 'glycyl thioester intermediate' specifically describes the mechanism of ubiquitin-like protein conjugation where the C-terminal glycine forms a thioester with the E2's active-site cysteine. A knowledgeable model can (1) eliminate out-of-range positions, (2) recognize that thioester chemistry mandates cysteine, and (3) verify position 113 is C while position 154 is D.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of C and D is trivial (sequence length). The distinction between A and B relies on general biochemical knowledge: thioester intermediates require cysteine, and E2-like enzymes use catalytic cysteines. This is transferable knowledge about enzyme mechanisms and amino acid chemistry, not a fact unique to this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are impossible (positions exceed the 161-residue sequence). Between A and B, the thioester chemistry requirement for cysteine uniquely identifies position 113 (C) over position 154 (D). No ambiguity remains."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (inferred by similarity), but the primary reference includes mutagenesis data for Cys-113, providing experimental corroboration.",
    "Options C and D (positions 1142 and 4261) are absurdly out of range for a 161-residue protein, making them trivially eliminable and reducing the effective discrimination to A vs. B.",
    "The protein is annotated as a 'Bacterial E2-like ubiquitin protein BilB' from Collimonas sp., a recently characterized system (2024 Nature paper), so this is not a well-known textbook enzyme but the mechanistic principle (catalytic cysteine for thioester intermediates in E2-like enzymes) is broadly conserved."
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
  "benchmark_sequence_length": 161,
  "benchmark_sequence_sha256": "3646da7e5f755e00a2cd4a2c090e3de055c0fb0383323a7b1c9eea3986ed9213",
  "current_entry_audit": {
    "entryVersion": 12,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-11-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 161,
  "current_source_sequence_sha256": "3646da7e5f755e00a2cd4a2c090e3de055c0fb0383323a7b1c9eea3986ed9213",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 11,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1I1NU27",
  "selected_historical_entry_version": 11,
  "selected_historical_record_sha256": "02140c806e50b7c8fba6442df748ac8050a6b50ee7a254e8a2d0deb6a7a2c0c9",
  "selected_historical_source_sequence_length": 161,
  "selected_historical_source_sequence_sha256": "3646da7e5f755e00a2cd4a2c090e3de055c0fb0383323a7b1c9eea3986ed9213",
  "selected_historical_version": {
    "accession": "A0A1I1NU27",
    "database": "Swiss-Prot",
    "entryVersion": 11,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "BILB_COLS4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1I1NU27\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:36.666780+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":12,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-11-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:36.666780+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Oxalobacteraceae\",\"Collimonas\"],\"scientificName\":\"Collimonas sp. (strain OK412)\",\"taxonId\":1801619}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:36.666780+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"E2 ubiquitin-conjugating enzyme BilB\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39020165\",\"source\":\"PubMed\"}],\"value\":\"2.3.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39020165\",\"source\":\"PubMed\"}],\"value\":\"Bacterial E2-like ubiquitin protein BilB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:36.666780+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Glycyl thioester intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39020165\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":113},\"start\":{\"modifier\":\"EXACT\",\"value\":113}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:24:36.666780+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Hoer J.\",\"Wolf S.G.\",\"Sorek R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39020165\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-024-07616-5\"}],\"citationType\":\"journal article\",\"firstPage\":\"850\",\"id\":\"39020165\",\"journal\":\"Nature\",\"lastPage\":\"856\",\"publicationDate\":\"2024\",\"title\":\"Bacteria conjugate ubiquitin-like proteins to interfere with phage assembly.\",\"volume\":\"631\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"PROBABLE ACTIVE SITE\",\"MUTAGENESIS OF CYS-113\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:36.666780+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1NU27?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H1",
  "excerpt": "ID   BILB_COLS4              Reviewed;         161 AA.\nAC   A0A1I1NU27;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-NOV-2017, sequence version 1.\nDT   28-JAN-2026, entry version 11.\nDE   RecName: Full=Bacterial E2-like ubiquitin protein BilB {ECO:0000303|PubMed:39020165};\nDE            EC=2.3.2.- {ECO:0000305|PubMed:39020165};\nDE   AltName: Full=E2 ubiquitin-conjugating enzyme BilB;\nGN   Name=bilB {ECO:0000303|PubMed:39020165};\nGN   ORFNames=SAMN04515619_11957 {ECO:0000312|EMBL:SFD01174.1};\nOS   Collimonas sp. (strain OK412).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Oxalobacteraceae; Collimonas.\nOX   NCBI_TaxID=1801619;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:42.543529+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02140c806e50b7c8fba6442df748ac8050a6b50ee7a254e8a2d0deb6a7a2c0c9",
  "url": "https://rest.uniprot.org/unisave/A0A1I1NU27?format=txt&versions=11"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1NU27?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, PROBABLE ACTIVE SITE, AND MUTAGENESIS OF CYS-113.\nRX   PubMed=39020165; DOI=10.1038/s41586-024-07616-5;\nRA   Hoer J., Wolf S.G., Sorek R.;\nRT   \"Bacteria conjugate ubiquitin-like proteins to interfere with phage\nRT   assembly.\";\nRL   Nature 631:850-856(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:42.543529+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02140c806e50b7c8fba6442df748ac8050a6b50ee7a254e8a2d0deb6a7a2c0c9",
  "url": "https://rest.uniprot.org/unisave/A0A1I1NU27?format=txt&versions=11"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1NU27?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        113\nFT                   /note=\"Glycyl thioester intermediate\"\nFT                   /evidence=\"ECO:0000305|PubMed:39020165\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:42.543529+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02140c806e50b7c8fba6442df748ac8050a6b50ee7a254e8a2d0deb6a7a2c0c9",
  "url": "https://rest.uniprot.org/unisave/A0A1I1NU27?format=txt&versions=11"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 14. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
