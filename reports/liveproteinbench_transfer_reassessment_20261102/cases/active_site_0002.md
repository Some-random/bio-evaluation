# active_site_0002

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0002.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 457 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNRSDAYGYFRNQGREYVITTPRTPARWFNYLFNDTYYTEISQTGQGDSVAFRPHNRTLTRGFRYFYLKDLETGGTWSPLYQPLKTEPEAYECIHSLGTTEIRSVSQEIASSIHVFVPRAGQQEIWTVTLTNTGVKPRSLSLFTAFSLENGGVMGSKCQFDQESQILSSYSFPYHVTYGQKAGCDDHTNVVYVYPDYPADSYDCSQRAFFGGDDIYELPAAVQKGRCSGGQAEAENPLGALQQTITLEPGEQAVRHFVVGCASSLEEIRSSKAELAAKGYAVLLQETEDYWEGITGMFRVETPDDDVNAFMNIWLKKQIVMQTRTNRMSSYCPVRNQLQDALGYALVDPAGAAEYMISVLQGQERSGFIQQWIMTDGSPPKNLCLLKHTDGPVWLIICITALLNQCGDTELLQRQVGFKGSSDSATIYQHLLLAADYMAGETGAHGLCLMGDGDWNDPINGPGRLGRGESAWNTMALVYAIQALIPFCEQLGDTENAEQLNTVARRLADAVNRICWDGGWYVAGFDDDGTPFGTAQDEEGKLFLNTQTWAIMSGIASGERLDQCLAAIDSLDTPFGPRLLEPPFSGWNPKWGRISLKLAGTTENGSVYCHASMFKAFADCIAGRGSEAWQTISRTLPTNPDNPPGQNGQVPIFVPNYYFGLADSPNFGKSSHHVSTGTVGWMLWTTLEYALGIRATANGLKIDPCIPADWPEYTVERKYRSASYRIHVLNPSGISRGTVKVTVDGEAWMAAALPYEAGREYQVTVQLEQ

[Multiple Choices]
A. Position 457 (Proton donor)
B. Position 2059 (For beta-ketoacyl synthase 2 activity)
C. Position 157 (Nucleophile; for glutaminase activity)
D. Position 83 (Acyl-ester intermediate)
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

> The matched-sequence UniProt annotation identifies residue 457 as the proton donor, and the archived record available by the historical cutoff carries the same annotation. Its evidence is transferred from a homolog, so this supports the key as a family-based annotation, not as direct experimental verification on this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 769-residue sequence is consistent with a glycoside phosphorylase family enzyme, for which a catalytic proton donor is a plausible active-site role. That transferable family-level chemistry favors A over the glutaminase nucleophile and acyl-ester-intermediate alternatives; B also names a position beyond the supplied sequence length. The sequence and choices provide a meaningful basis for preferring A without knowing this protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and catalytic-chemistry patterns distinguish the offered options. The exact residue assignment is less certain from sequence alone than the family-level choice, but that limitation does not make this distinction dependent on memorizing the target's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct catalytic roles, and no other listed choice is comparably plausible for the sequence context.


### Important caveats

- The source annotation is homolog-transferred rather than direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 769-residue sequence is consistent with a glycoside phosphorylase family enzyme, for which a catalytic proton donor is a plausible active-site role. That transferable family-level chemistry favors A over the glutaminase nucleophile and acyl-ester-intermediate alternatives; B also names a position beyond the supplied sequence length. The sequence and choices provide a meaningful basis for preferring A without knowing this protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and catalytic-chemistry patterns distinguish the offered options. The exact residue assignment is less certain from sequence alone than the family-level choice, but that limitation does not make this distinction dependent on memorizing the target's annotation."
  },
  "case_id": "active_site_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies residue 457 as the proton donor, and the archived record available by the historical cutoff carries the same annotation. Its evidence is transferred from a homolog, so this supports the key as a family-based annotation, not as direct experimental verification on this exact protein."
  },
  "important_caveats": [
    "The source annotation is homolog-transferred rather than direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct catalytic roles, and no other listed choice is comparably plausible for the sequence context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies residue 457 as the proton donor, and the archived record available by the historical cutoff carries the same annotation. Its evidence is transferred from a homolog, so this supports the key as a family-based annotation, not as direct experimental verification on this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 769-residue sequence is consistent with a glycoside phosphorylase family enzyme, for which a catalytic proton donor is a plausible active-site role. That transferable family-level chemistry favors A over the glutaminase nucleophile and acyl-ester-intermediate alternatives; B also names a position beyond the supplied sequence length. The sequence and choices provide a meaningful basis for preferring A without knowing this protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and catalytic-chemistry patterns distinguish the offered options. The exact residue assignment is less certain from sequence alone than the family-level choice, but that limitation does not make this distinction dependent on memorizing the target's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct catalytic roles, and no other listed choice is comparably plausible for the sequence context."
  },
  "important_caveats": [
    "The source annotation is homolog-transferred rather than direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A089MMR2 annotates an active site at position 457 with the note 'Proton donor' (evidence C5, H3). However, the evidence code is ECO:0000250 (inferred by similarity to Q76IQ9), meaning this is a computational transfer from a related GH94 enzyme rather than direct experimental validation on this exact protein. The residue at position 457 in the 769-residue sequence is Asp (D), which is consistent with the conserved proton-donor aspartate in GH94 glycoside phosphorylases. The annotation supports the author's key, though it is similarity-based rather than experimentally determined for this specific enzyme.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The answer can be reached through elimination using general enzymology and sequence inspection: (1) Option B cites position 2059, which exceeds the 769-residue protein length — trivially eliminated by arithmetic. (2) Option C claims 'Nucleophile; for glutaminase activity' at position 157. Counting the sequence, position 157 is Lysine (K). Glutaminases use a Cys or Ser nucleophile, not Lys, and are typically 300–400 residues, not 769. The described mechanism is inconsistent. (3) Option D claims 'Acyl-ester intermediate' at position 83. Position 83 is Proline (P), which is conformationally incapable of forming a nucleophilic acyl-ester bond. Acyl-ester intermediates require Ser, Cys, or Thr nucleophiles. Eliminated. (4) Option A: position 457 is Asp (D), and 'proton donor' is a well-established catalytic role in GH-family glycoside phosphorylases (e.g., sucrose phosphorylase, maltose phosphorylase), where a conserved Asp protonates the glycosidic oxygen during phosphorolysis. This is transferable family-level knowledge about glycoside hydrolase/phosphorylase mechanisms. By elimination and positive mechanistic consistency, A is selected.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B by simple arithmetic, C by recognizing Lysine cannot serve as a glutaminase nucleophile and the protein size is wrong, and D by recognizing Proline cannot form an acyl-ester intermediate. The remaining option A is positively supported by the general principle that GH-family phosphorylases use a conserved Asp as proton donor. No fact specific to this exact protein beyond the sequence itself is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are each eliminated by straightforward factual checks (position exceeds sequence length; wrong residue type for claimed mechanism; Proline cannot form acyl-ester intermediate). Only A survives elimination and is mechanistically consistent with the residue identity (Asp) and a known phosphorylase catalytic role.


### Important caveats

- The UniProt annotation at position 457 carries evidence code ECO:0000250 (inferred by similarity to Q76IQ9), so it is a computational transfer rather than direct experimental characterization of this specific enzyme.
- Option B (position 2059) is a clearly impossible distractor for a 769-residue protein, making the question somewhat easier than a well-designed benchmark item.
- The 'proton donor' role is well-established for GH94 family phosphorylases, but the specific assignment to this exact protein relies on homology modeling/similarity rather than site-directed mutagenesis or crystallography on this enzyme.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The answer can be reached through elimination using general enzymology and sequence inspection: (1) Option B cites position 2059, which exceeds the 769-residue protein length — trivially eliminated by arithmetic. (2) Option C claims 'Nucleophile; for glutaminase activity' at position 157. Counting the sequence, position 157 is Lysine (K). Glutaminases use a Cys or Ser nucleophile, not Lys, and are typically 300–400 residues, not 769. The described mechanism is inconsistent. (3) Option D claims 'Acyl-ester intermediate' at position 83. Position 83 is Proline (P), which is conformationally incapable of forming a nucleophilic acyl-ester bond. Acyl-ester intermediates require Ser, Cys, or Thr nucleophiles. Eliminated. (4) Option A: position 457 is Asp (D), and 'proton donor' is a well-established catalytic role in GH-family glycoside phosphorylases (e.g., sucrose phosphorylase, maltose phosphorylase), where a conserved Asp protonates the glycosidic oxygen during phosphorolysis. This is transferable family-level knowledge about glycoside hydrolase/phosphorylase mechanisms. By elimination and positive mechanistic consistency, A is selected.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B by simple arithmetic, C by recognizing Lysine cannot serve as a glutaminase nucleophile and the protein size is wrong, and D by recognizing Proline cannot form an acyl-ester intermediate. The remaining option A is positively supported by the general principle that GH-family phosphorylases use a conserved Asp as proton donor. No fact specific to this exact protein beyond the sequence itself is required."
  },
  "case_id": "active_site_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A089MMR2 annotates an active site at position 457 with the note 'Proton donor' (evidence C5, H3). However, the evidence code is ECO:0000250 (inferred by similarity to Q76IQ9), meaning this is a computational transfer from a related GH94 enzyme rather than direct experimental validation on this exact protein. The residue at position 457 in the 769-residue sequence is Asp (D), which is consistent with the conserved proton-donor aspartate in GH94 glycoside phosphorylases. The annotation supports the author's key, though it is similarity-based rather than experimentally determined for this specific enzyme."
  },
  "important_caveats": [
    "The UniProt annotation at position 457 carries evidence code ECO:0000250 (inferred by similarity to Q76IQ9), so it is a computational transfer rather than direct experimental characterization of this specific enzyme.",
    "Option B (position 2059) is a clearly impossible distractor for a 769-residue protein, making the question somewhat easier than a well-designed benchmark item.",
    "The 'proton donor' role is well-established for GH94 family phosphorylases, but the specific assignment to this exact protein relies on homology modeling/similarity rather than site-directed mutagenesis or crystallography on this enzyme."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are each eliminated by straightforward factual checks (position exceeds sequence length; wrong residue type for claimed mechanism; Proline cannot form acyl-ester intermediate). Only A survives elimination and is mechanistically consistent with the residue identity (Asp) and a known phosphorylase catalytic role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A089MMR2 annotates an active site at position 457 with the note 'Proton donor' (evidence C5, H3). However, the evidence code is ECO:0000250 (inferred by similarity to Q76IQ9), meaning this is a computational transfer from a related GH94 enzyme rather than direct experimental validation on this exact protein. The residue at position 457 in the 769-residue sequence is Asp (D), which is consistent with the conserved proton-donor aspartate in GH94 glycoside phosphorylases. The annotation supports the author's key, though it is similarity-based rather than experimentally determined for this specific enzyme.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The answer can be reached through elimination using general enzymology and sequence inspection: (1) Option B cites position 2059, which exceeds the 769-residue protein length — trivially eliminated by arithmetic. (2) Option C claims 'Nucleophile; for glutaminase activity' at position 157. Counting the sequence, position 157 is Lysine (K). Glutaminases use a Cys or Ser nucleophile, not Lys, and are typically 300–400 residues, not 769. The described mechanism is inconsistent. (3) Option D claims 'Acyl-ester intermediate' at position 83. Position 83 is Proline (P), which is conformationally incapable of forming a nucleophilic acyl-ester bond. Acyl-ester intermediates require Ser, Cys, or Thr nucleophiles. Eliminated. (4) Option A: position 457 is Asp (D), and 'proton donor' is a well-established catalytic role in GH-family glycoside phosphorylases (e.g., sucrose phosphorylase, maltose phosphorylase), where a conserved Asp protonates the glycosidic oxygen during phosphorolysis. This is transferable family-level knowledge about glycoside hydrolase/phosphorylase mechanisms. By elimination and positive mechanistic consistency, A is selected.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B by simple arithmetic, C by recognizing Lysine cannot serve as a glutaminase nucleophile and the protein size is wrong, and D by recognizing Proline cannot form an acyl-ester intermediate. The remaining option A is positively supported by the general principle that GH-family phosphorylases use a conserved Asp as proton donor. No fact specific to this exact protein beyond the sequence itself is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are each eliminated by straightforward factual checks (position exceeds sequence length; wrong residue type for claimed mechanism; Proline cannot form acyl-ester intermediate). Only A survives elimination and is mechanistically consistent with the residue identity (Asp) and a known phosphorylase catalytic role."
  },
  "important_caveats": [
    "The UniProt annotation at position 457 carries evidence code ECO:0000250 (inferred by similarity to Q76IQ9), so it is a computational transfer rather than direct experimental characterization of this specific enzyme.",
    "Option B (position 2059) is a clearly impossible distractor for a 769-residue protein, making the question somewhat easier than a well-designed benchmark item.",
    "The 'proton donor' role is well-established for GH94 family phosphorylases, but the specific assignment to this exact protein relies on homology modeling/similarity rather than site-directed mutagenesis or crystallography on this enzyme."
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
  "benchmark_sequence_length": 769,
  "benchmark_sequence_sha256": "40a4249be74e7afcec5840e732edfa8379c2c5142a4cd41cbb1026a8b9c257e7",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-11-26",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 769,
  "current_source_sequence_sha256": "40a4249be74e7afcec5840e732edfa8379c2c5142a4cd41cbb1026a8b9c257e7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A089MMR2",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "selected_historical_source_sequence_length": 769,
  "selected_historical_source_sequence_sha256": "40a4249be74e7afcec5840e732edfa8379c2c5142a4cd41cbb1026a8b9c257e7",
  "selected_historical_version": {
    "accession": "A0A089MMR2",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BGBGP_PAEBO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A089MMR2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-11-26\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Paenibacillaceae\",\"Paenibacillus\"],\"scientificName\":\"Paenibacillus borealis\",\"taxonId\":160799}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.392\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"value\":\"3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q76IQ9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":457},\"start\":{\"modifier\":\"EXACT\",\"value\":457}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Isono N.\",\"Mizutani E.\",\"Hayashida H.\",\"Katsuzaki H.\",\"Saburi W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35947916\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbrc.2022.07.098\"}],\"citationType\":\"journal article\",\"firstPage\":\"60\",\"id\":\"35947916\",\"journal\":\"Biochem. Biophys. Res. Commun.\",\"lastPage\":\"65\",\"publicationDate\":\"2022\",\"title\":\"Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.\",\"volume\":\"625\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   BGBGP_PAEBO             Reviewed;         769 AA.\nAC   A0A089MMR2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   26-NOV-2014, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase {ECO:0000303|PubMed:35947916};\nDE            EC=2.4.1.392 {ECO:0000269|PubMed:35947916};\nGN   ORFNames=PBOR_13355 {ECO:0000312|EMBL:AIQ57809.1};\nOS   Paenibacillus borealis.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Paenibacillaceae;\nOC   Paenibacillus.\nOX   NCBI_TaxID=160799;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.632691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "url": "https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19;\nRX   PubMed=35947916; DOI=10.1016/j.bbrc.2022.07.098;\nRA   Isono N., Mizutani E., Hayashida H., Katsuzaki H., Saburi W.;\nRT   \"Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-\nRT   beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of\nRT   the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.\";\nRL   Biochem. Biophys. Res. Commun. 625:60-65(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.632691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "url": "https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        457\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q76IQ9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.632691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-125",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "url": "https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
