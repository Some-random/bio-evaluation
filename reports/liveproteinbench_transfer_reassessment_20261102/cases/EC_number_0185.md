# EC_number_0185

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0185.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.3.2.27

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPIMLNFSNGRILPESEVEALRNVARSNQSDVLLVGSRSLRLHHISFMDGFSVEPIPGSFLDRIGERRHRRLAESLERQLNGGSSFLQAFSQYIEQTSSAPPLQESVRNEVQSRVNSYAFSVNPGDFPCSVLHLSCPITLCVPETGVFVKNARCSKVCSLYDISALTEMLRRNASHPLSREAFTPGMIVHKEECNFNTTEQHFCILPRSDTRL

[Multiple Choices]
A. 2.3.1.322
B. 6.3.2.35
C. 1.11.1.24
D. 2.3.2.27
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

> The sequence matches the UniProt entry annotated as EC 2.3.2.27, and that entry cites experimental evidence for both the enzyme classification and the ubiquitin-transfer reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short bacterial protein sequence, including its cysteine-rich region, is consistent with the NleG/NEL effector family. Transferable knowledge that NleG-family proteins are E3 ubiquitin ligases points to EC 2.3.2.27 (D), distinguishing it from the acyltransferase, ligase, and peroxidase alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition from the sequence can meaningfully distinguish the offered EC choices without recalling this exact protein's annotation. This is a credible inference, though the family assignment and EC prediction are not guaranteed from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports D, and the alternatives describe different enzyme classifications.


### Important caveats

- The reviewer-only UniProt evidence is not an original input and is used only to assess whether the key is supported.
- The annotation cites experimental evidence, but the underlying publication was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short bacterial protein sequence, including its cysteine-rich region, is consistent with the NleG/NEL effector family. Transferable knowledge that NleG-family proteins are E3 ubiquitin ligases points to EC 2.3.2.27 (D), distinguishing it from the acyltransferase, ligase, and peroxidase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition from the sequence can meaningfully distinguish the offered EC choices without recalling this exact protein's annotation. This is a credible inference, though the family assignment and EC prediction are not guaranteed from the sequence alone."
  },
  "case_id": "EC_number_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as EC 2.3.2.27, and that entry cites experimental evidence for both the enzyme classification and the ubiquitin-transfer reaction."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence is not an original input and is used only to assess whether the key is supported.",
    "The annotation cites experimental evidence, but the underlying publication was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D, and the alternatives describe different enzyme classifications."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as EC 2.3.2.27, and that entry cites experimental evidence for both the enzyme classification and the ubiquitin-transfer reaction.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short bacterial protein sequence, including its cysteine-rich region, is consistent with the NleG/NEL effector family. Transferable knowledge that NleG-family proteins are E3 ubiquitin ligases points to EC 2.3.2.27 (D), distinguishing it from the acyltransferase, ligase, and peroxidase alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition from the sequence can meaningfully distinguish the offered EC choices without recalling this exact protein's annotation. This is a credible inference, though the family assignment and EC prediction are not guaranteed from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D, and the alternatives describe different enzyme classifications."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence is not an original input and is used only to assess whether the key is supported.",
    "The annotation cites experimental evidence, but the underlying publication was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A482PJY4 for this exact 213-aa sequence annotates EC 2.3.2.27 (E3 ubiquitin-protein ligase NleG8) with experimental evidence (ECO:0000269|PubMed:36511702). The catalytic activity is explicitly stated as the ubiquitin transfer reaction from E2 to acceptor protein lysine. The sequence matches the source record exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the 213-residue sequence contains a recognizable U-box domain motif: the pattern C-S-K-V-C-S-L-Y … K-E-E-C-N-F-N-T-T-E-Q-H-F-C-I-L mirrors the C-x2-C … C-x2-H … C arrangement characteristic of U-box E3 ubiquitin ligases (structurally related to RING domains but lacking zinc coordination). U-box domains are a well-known family feature shared across many E3 ubiquitin ligases (e.g., CHIP, plant PUB proteins, bacterial NleG effectors). Recognizing this domain identifies the protein as an E3 ubiquitin ligase, whose EC classification is 2.3.2.27 (a transferase transferring ubiquitin from E2-thioester to acceptor lysine). This eliminates: C (1.11.1.24, peroxidase – no heme-binding or peroxidase motifs present); B (6.3.2.35, a C-N bond ligase – E3 ubiquitin ligases are transferases because ubiquitin is pre-activated on E2, not de novo ligated); A (2.3.1.322, a specific acyltransferase – the U-box architecture and short effector-like length do not match any known acyltransferase fold). The combination of U-box domain recognition, the short bacterial-effector length, and the well-established EC assignment for E3 ubiquitin ligases provides a transferable reasoning path from other U-box-containing proteins to choice D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The U-box domain pattern in the C-terminal region is a transferable family-level feature. A knowledgeable model that recognizes U-box/RING-like C/C/H/C motifs and knows that E3 ubiquitin ligases carry EC 2.3.2.27 can meaningfully distinguish D from the other three options. The elimination of B (ligase vs. transferase distinction is mechanistic and well-known), C (no peroxidase features), and A (no acyltransferase features) further supports the choice without requiring the exact NleG8 record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The U-box domain pattern, the short effector-like length, and the mechanistic distinction between transferase (EC 2) and ligase (EC 6) for ubiquitin transfer provide a clear basis to select D. No other option is supported by the sequence features.


### Important caveats

- The U-box domain recognition from a raw 213-aa sequence is non-trivial; the C/C/H/C spacing pattern is subtle and could be confused with a RING domain or other zinc-binding motif without prior familiarity.
- EC 2.3.2.27 is a relatively specialized EC number; a model must know the specific 4-digit assignment for E3 ubiquitin-protein ligase rather than only the general EC 2 class.
- The reviewer evidence confirms experimental annotation (PubMed 36511702), but the evaluated model had access only to the sequence and choices.
- The protein is a bacterial Type III secretion effector (NleG family from Citrobacter rodentium), which is not stated in the original input; this context would aid recognition but is not strictly required given the U-box motif.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the 213-residue sequence contains a recognizable U-box domain motif: the pattern C-S-K-V-C-S-L-Y … K-E-E-C-N-F-N-T-T-E-Q-H-F-C-I-L mirrors the C-x2-C … C-x2-H … C arrangement characteristic of U-box E3 ubiquitin ligases (structurally related to RING domains but lacking zinc coordination). U-box domains are a well-known family feature shared across many E3 ubiquitin ligases (e.g., CHIP, plant PUB proteins, bacterial NleG effectors). Recognizing this domain identifies the protein as an E3 ubiquitin ligase, whose EC classification is 2.3.2.27 (a transferase transferring ubiquitin from E2-thioester to acceptor lysine). This eliminates: C (1.11.1.24, peroxidase – no heme-binding or peroxidase motifs present); B (6.3.2.35, a C-N bond ligase – E3 ubiquitin ligases are transferases because ubiquitin is pre-activated on E2, not de novo ligated); A (2.3.1.322, a specific acyltransferase – the U-box architecture and short effector-like length do not match any known acyltransferase fold). The combination of U-box domain recognition, the short bacterial-effector length, and the well-established EC assignment for E3 ubiquitin ligases provides a transferable reasoning path from other U-box-containing proteins to choice D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The U-box domain pattern in the C-terminal region is a transferable family-level feature. A knowledgeable model that recognizes U-box/RING-like C/C/H/C motifs and knows that E3 ubiquitin ligases carry EC 2.3.2.27 can meaningfully distinguish D from the other three options. The elimination of B (ligase vs. transferase distinction is mechanistic and well-known), C (no peroxidase features), and A (no acyltransferase features) further supports the choice without requiring the exact NleG8 record."
  },
  "case_id": "EC_number_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A482PJY4 for this exact 213-aa sequence annotates EC 2.3.2.27 (E3 ubiquitin-protein ligase NleG8) with experimental evidence (ECO:0000269|PubMed:36511702). The catalytic activity is explicitly stated as the ubiquitin transfer reaction from E2 to acceptor protein lysine. The sequence matches the source record exactly."
  },
  "important_caveats": [
    "The U-box domain recognition from a raw 213-aa sequence is non-trivial; the C/C/H/C spacing pattern is subtle and could be confused with a RING domain or other zinc-binding motif without prior familiarity.",
    "EC 2.3.2.27 is a relatively specialized EC number; a model must know the specific 4-digit assignment for E3 ubiquitin-protein ligase rather than only the general EC 2 class.",
    "The reviewer evidence confirms experimental annotation (PubMed 36511702), but the evaluated model had access only to the sequence and choices.",
    "The protein is a bacterial Type III secretion effector (NleG family from Citrobacter rodentium), which is not stated in the original input; this context would aid recognition but is not strictly required given the U-box motif."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The U-box domain pattern, the short effector-like length, and the mechanistic distinction between transferase (EC 2) and ligase (EC 6) for ubiquitin transfer provide a clear basis to select D. No other option is supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A482PJY4 for this exact 213-aa sequence annotates EC 2.3.2.27 (E3 ubiquitin-protein ligase NleG8) with experimental evidence (ECO:0000269|PubMed:36511702). The catalytic activity is explicitly stated as the ubiquitin transfer reaction from E2 to acceptor protein lysine. The sequence matches the source record exactly.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the 213-residue sequence contains a recognizable U-box domain motif: the pattern C-S-K-V-C-S-L-Y … K-E-E-C-N-F-N-T-T-E-Q-H-F-C-I-L mirrors the C-x2-C … C-x2-H … C arrangement characteristic of U-box E3 ubiquitin ligases (structurally related to RING domains but lacking zinc coordination). U-box domains are a well-known family feature shared across many E3 ubiquitin ligases (e.g., CHIP, plant PUB proteins, bacterial NleG effectors). Recognizing this domain identifies the protein as an E3 ubiquitin ligase, whose EC classification is 2.3.2.27 (a transferase transferring ubiquitin from E2-thioester to acceptor lysine). This eliminates: C (1.11.1.24, peroxidase – no heme-binding or peroxidase motifs present); B (6.3.2.35, a C-N bond ligase – E3 ubiquitin ligases are transferases because ubiquitin is pre-activated on E2, not de novo ligated); A (2.3.1.322, a specific acyltransferase – the U-box architecture and short effector-like length do not match any known acyltransferase fold). The combination of U-box domain recognition, the short bacterial-effector length, and the well-established EC assignment for E3 ubiquitin ligases provides a transferable reasoning path from other U-box-containing proteins to choice D.",
    "missing_item_specific_fact": "",
    "reason": "The U-box domain pattern in the C-terminal region is a transferable family-level feature. A knowledgeable model that recognizes U-box/RING-like C/C/H/C motifs and knows that E3 ubiquitin ligases carry EC 2.3.2.27 can meaningfully distinguish D from the other three options. The elimination of B (ligase vs. transferase distinction is mechanistic and well-known), C (no peroxidase features), and A (no acyltransferase features) further supports the choice without requiring the exact NleG8 record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The U-box domain pattern, the short effector-like length, and the mechanistic distinction between transferase (EC 2) and ligase (EC 6) for ubiquitin transfer provide a clear basis to select D. No other option is supported by the sequence features."
  },
  "important_caveats": [
    "The U-box domain recognition from a raw 213-aa sequence is non-trivial; the C/C/H/C spacing pattern is subtle and could be confused with a RING domain or other zinc-binding motif without prior familiarity.",
    "EC 2.3.2.27 is a relatively specialized EC number; a model must know the specific 4-digit assignment for E3 ubiquitin-protein ligase rather than only the general EC 2 class.",
    "The reviewer evidence confirms experimental annotation (PubMed 36511702), but the evaluated model had access only to the sequence and choices.",
    "The protein is a bacterial Type III secretion effector (NleG family from Citrobacter rodentium), which is not stated in the original input; this context would aid recognition but is not strictly required given the U-box motif."
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
  "benchmark_sequence_length": 213,
  "benchmark_sequence_sha256": "16612f731de98766170a931a61e51f7339aa7a0030ef42fd419a95fcd5450328",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 213,
  "current_source_sequence_sha256": "16612f731de98766170a931a61e51f7339aa7a0030ef42fd419a95fcd5450328",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A482PJY4",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f",
  "selected_historical_source_sequence_length": 213,
  "selected_historical_source_sequence_sha256": "16612f731de98766170a931a61e51f7339aa7a0030ef42fd419a95fcd5450328",
  "selected_historical_version": {
    "accession": "A0A482PJY4",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "NLEG8_CITRO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A482PJY4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Citrobacter\"],\"scientificName\":\"Citrobacter rodentium\",\"taxonId\":67825}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"value\":\"2.3.2.27\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"E3 ubiquitin-protein ligase NleG8\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.2.27\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"name\":\"S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Popov G.\",\"Fiebig-Comyn A.\",\"Syriste L.\",\"Little D.J.\",\"Skarina T.\",\"Stogios P.J.\",\"Birstonas S.\",\"Coombes B.K.\",\"Savchenko A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36511702\"},{\"database\":\"DOI\",\"id\":\"10.1128/iai.00505-22\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0050522\",\"id\":\"36511702\",\"journal\":\"Infect. Immun.\",\"lastPage\":\"e0050522\",\"publicationDate\":\"2023\",\"title\":\"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for Different Roles during Citrobacter rodentium Infection in Mice.\",\"volume\":\"91\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DBS100\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"INTERACTION WITH HOST GOPC\",\"SUBCELLULAR LOCATION\",\"INDUCTION\",\"DOMAIN\",\"DISRUPTION PHENOTYPE\",\"MOTIF\",\"MUTAGENESIS OF ILE-138 AND 210-ASP--LEU-213\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   NLEG8_CITRO             Reviewed;         213 AA.\nAC   A0A482PJY4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=E3 ubiquitin-protein ligase NleG8 {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};\nGN   Name=nleG8 {ECO:0000303|PubMed:36511702};\nGN   ORFNames=E2R62_17250 {ECO:0000312|EMBL:QBY30403.1};\nOS   Citrobacter rodentium.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Citrobacter.\nOX   NCBI_TaxID=67825;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:23.897522+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f",
  "url": "https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=E3 ubiquitin-protein ligase NleG8 {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:23.897522+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f",
  "url": "https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBUNIT, INTERACTION WITH HOST GOPC,\nRP   SUBCELLULAR LOCATION, INDUCTION, DOMAIN, DISRUPTION PHENOTYPE, MOTIF, AND\nRP   MUTAGENESIS OF ILE-138 AND 210-ASP--LEU-213.\nRC   STRAIN=DBS100;\nRX   PubMed=36511702; DOI=10.1128/iai.00505-22;\nRA   Popov G., Fiebig-Comyn A., Syriste L., Little D.J., Skarina T.,\nRA   Stogios P.J., Birstonas S., Coombes B.K., Savchenko A.;\nRT   \"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for\nRT   Different Roles during Citrobacter rodentium Infection in Mice.\";\nRL   Infect. Immun. 91:e0050522-e0050522(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:23.897522+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f",
  "url": "https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine +\nCC         [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-\nCC         cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.;\nCC         EC=2.3.2.27; Evidence={ECO:0000269|PubMed:36511702};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:23.897522+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f",
  "url": "https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 185. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
