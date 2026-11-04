# EC_number_0129

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0129.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 5.3.99.13

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQTYLSTKSIEYYLKELKEIFSQIWLKPSEIEKRCEELFKRSKEFDYKRILVSGETDNTTLYVIEDSSKIHVFSPNRDLRENPLLMRWHPSWYEIESKEIYYKCFLSCEELYEHLELPTVTLVNLCVIENFPIPRLNLSTGTLSSYLRKEQLAKVELIDMQVGTTINQIIKNLLDSQPDIIGLSVNFGQKKLAFEILDLIYSHIENGDLSSIITVGNVIPSFSPEQFFERYPSLLICDKEGEYTLRDLIKMLKKELKLDEVNGISYVDESGEVKHNVAETVNFKEEVPTPSLDILGEISKFRGALTLETSRGCDYSRCTFCPRDHKLRSWRPLSVEQTLKQLDDILRAGKHFNIKPHIYMADEEFIGELPNGTEAQRIIDICEGLLKREEKIKFDFAARADSVYEPKRTKEWNVERLKMWHYCALAGADRIFIGVESGSNQQLKRYGKGTTSEQNIIALRLVSALGINLRIGFIMFDQLMKGLDNLKENLDFLERTDALMKPIDIGDMTYEELYDKLLNDKEFIEKHKTGKPVYTIVSYMLASMEILMNTPYSRMVQLTERKEEVNLIMNDGKPDMNMGRYATSFVDKTNGNLSEACQMWIDSNFGVMYTIKSLHKVANPREKKKLYSYMETHREISHFLLKYLVYNLSPDKESQIILSDFLRMHSMEHILDNSKINVGDGSKENILNVMTNWQLIMEKLLRDVEADLNKGIITDSEDHRLHNTLKRWFSDMGNWSLINAYELN

[Multiple Choices]
A. 5.3.1.8
B. 2.3.1.312
C. 5.3.99.13
D. 2.3.1.290
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

> The sequence matches the cited UniProt record, which assigns EC 5.3.99.13 to its catalytic activity and cites experimental evidence for the reaction. The annotation describes dAMP conversion to 4'-phospho-dehydrooxetanocin, supporting choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence and cysteine-rich region are consistent with a radical-SAM enzyme, a family-level clue distinct from the offered acyltransferases and the ordinary phosphosugar-isomerase alternative. Transferable knowledge that specialized radical-SAM enzymes participate in nucleotide transformations makes the unusual isomerase choice C a meaningful fit, though the sequence alone may not establish the complete EC number with certainty.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a plausible family-level basis to distinguish C among these choices without needing the exact protein's recorded annotation. This supports a probabilistic inference, not a guarantee of the specific catalytic reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices represent distinct enzyme activities; the sequence's apparent radical-SAM family context favors C over the other listed activities.


### Important caveats

- The experimental support comes from reviewer-only annotations and cited studies, not from information supplied to the model.
- The family-level sequence inference is less conclusive than direct functional evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence and cysteine-rich region are consistent with a radical-SAM enzyme, a family-level clue distinct from the offered acyltransferases and the ordinary phosphosugar-isomerase alternative. Transferable knowledge that specialized radical-SAM enzymes participate in nucleotide transformations makes the unusual isomerase choice C a meaningful fit, though the sequence alone may not establish the complete EC number with certainty.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a plausible family-level basis to distinguish C among these choices without needing the exact protein's recorded annotation. This supports a probabilistic inference, not a guarantee of the specific catalytic reaction."
  },
  "case_id": "EC_number_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, which assigns EC 5.3.99.13 to its catalytic activity and cites experimental evidence for the reaction. The annotation describes dAMP conversion to 4'-phospho-dehydrooxetanocin, supporting choice C."
  },
  "important_caveats": [
    "The experimental support comes from reviewer-only annotations and cited studies, not from information supplied to the model.",
    "The family-level sequence inference is less conclusive than direct functional evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices represent distinct enzyme activities; the sequence's apparent radical-SAM family context favors C over the other listed activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, which assigns EC 5.3.99.13 to its catalytic activity and cites experimental evidence for the reaction. The annotation describes dAMP conversion to 4'-phospho-dehydrooxetanocin, supporting choice C.",
    "evidence_ids": ["C4", "C5", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence and cysteine-rich region are consistent with a radical-SAM enzyme, a family-level clue distinct from the offered acyltransferases and the ordinary phosphosugar-isomerase alternative. Transferable knowledge that specialized radical-SAM enzymes participate in nucleotide transformations makes the unusual isomerase choice C a meaningful fit, though the sequence alone may not establish the complete EC number with certainty.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a plausible family-level basis to distinguish C among these choices without needing the exact protein's recorded annotation. This supports a probabilistic inference, not a guarantee of the specific catalytic reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices represent distinct enzyme activities; the sequence's apparent radical-SAM family context favors C over the other listed activities."
  },
  "important_caveats": [
    "The experimental support comes from reviewer-only annotations and cited studies, not from information supplied to the model.",
    "The family-level sequence inference is less conclusive than direct functional evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry O24770 (OXSB_PRIMG) assigns EC 5.3.99.13 to this 744-aa protein with experimental evidence codes (ECO:0000269) from two independent biochemical studies (PubMed:28346939, PubMed:33560833) and corroborating X-ray crystallography at 1.80 Å (PDB:5UL2, 5UL3, 5UL4). The catalytic reaction (dAMP → 4'-phospho-dehydrooxetanocin, an intramolecular ring-contraction isomerization using SAM and B12) is consistent with EC 5.3.99.13. Sequence match is exact (SHA-256 identical, 744 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H6](#evidence-h6), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a variant radical SAM cluster-binding motif in the region 'CDYSRCTFC' (C-X4-C-X2-C), a recognized variant of the canonical C-X3-C-X2-C motif found in B12-dependent radical SAM enzymes (e.g., PylB, OxsB). This motif is a well-known family-level feature transferable across many radical SAM proteins. Its presence argues against EC 5.3.1.8 (glucose-6-phosphate isomerase, a TIM-barrel enzyme using simple acid-base catalysis with no metal-cluster chemistry) and against EC 2.3.1.312/2.3.1.290 (acyltransferases that typically employ nucleophilic Ser/Cys catalysis, not radical SAM). Among the four choices, only 5.3.99.13 is a radical SAM isomerase, and the '99' subclass (other intramolecular oxidoreductases) is consistent with an unusual ring-contraction reaction. The large C-terminal hydrophobic domain (~400 aa) is also consistent with a B12-binding domain architecture shared by B12-dependent radical SAM enzymes, further supporting an EC 5 isomerase with radical SAM chemistry rather than a simple isomerase or acyltransferase.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the variant radical SAM motif (CX4CX2C) from the sequence, recall that this motif is associated with radical SAM enzymes (a large protein family), and reason that such enzymes are incompatible with the catalytic mechanisms of glucose-6-phosphate isomerase (EC 5.3.1.8) or acyltransferases (EC 2.3.1.x). The only remaining option consistent with radical SAM isomerase chemistry is 5.3.99.13. This is a family-level sequence-feature inference, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The radical SAM motif and domain architecture provide a clear basis to eliminate 5.3.1.8 (no radical SAM, TIM-barrel) and 2.3.1.312/2.3.1.290 (acyltransferases without radical SAM chemistry). Only 5.3.99.13 is consistent with a radical SAM isomerase among the offered choices.


### Important caveats

- The radical SAM motif in this sequence is a variant (C-X4-C-X2-C rather than the canonical C-X3-C-X2-C), which is characteristic of B12-dependent radical SAM enzymes but may make automated motif detection less straightforward.
- Distinguishing 5.3.99.13 from other 5.3.99.x entries would require knowing the specific reaction; however, among the four offered choices, only one is 5.3.99.x, so the family-level inference suffices for this MCQ.
- The EC 5.3.99.13 assignment is relatively recent (first characterized 2017, EC formally assigned later), so the '99' subclass reflects a recently discovered reaction type rather than a long-established family.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a variant radical SAM cluster-binding motif in the region 'CDYSRCTFC' (C-X4-C-X2-C), a recognized variant of the canonical C-X3-C-X2-C motif found in B12-dependent radical SAM enzymes (e.g., PylB, OxsB). This motif is a well-known family-level feature transferable across many radical SAM proteins. Its presence argues against EC 5.3.1.8 (glucose-6-phosphate isomerase, a TIM-barrel enzyme using simple acid-base catalysis with no metal-cluster chemistry) and against EC 2.3.1.312/2.3.1.290 (acyltransferases that typically employ nucleophilic Ser/Cys catalysis, not radical SAM). Among the four choices, only 5.3.99.13 is a radical SAM isomerase, and the '99' subclass (other intramolecular oxidoreductases) is consistent with an unusual ring-contraction reaction. The large C-terminal hydrophobic domain (~400 aa) is also consistent with a B12-binding domain architecture shared by B12-dependent radical SAM enzymes, further supporting an EC 5 isomerase with radical SAM chemistry rather than a simple isomerase or acyltransferase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the variant radical SAM motif (CX4CX2C) from the sequence, recall that this motif is associated with radical SAM enzymes (a large protein family), and reason that such enzymes are incompatible with the catalytic mechanisms of glucose-6-phosphate isomerase (EC 5.3.1.8) or acyltransferases (EC 2.3.1.x). The only remaining option consistent with radical SAM isomerase chemistry is 5.3.99.13. This is a family-level sequence-feature inference, not a lookup of this specific protein's annotation."
  },
  "case_id": "EC_number_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H1",
      "H2",
      "H6",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry O24770 (OXSB_PRIMG) assigns EC 5.3.99.13 to this 744-aa protein with experimental evidence codes (ECO:0000269) from two independent biochemical studies (PubMed:28346939, PubMed:33560833) and corroborating X-ray crystallography at 1.80 Å (PDB:5UL2, 5UL3, 5UL4). The catalytic reaction (dAMP → 4'-phospho-dehydrooxetanocin, an intramolecular ring-contraction isomerization using SAM and B12) is consistent with EC 5.3.99.13. Sequence match is exact (SHA-256 identical, 744 aa)."
  },
  "important_caveats": [
    "The radical SAM motif in this sequence is a variant (C-X4-C-X2-C rather than the canonical C-X3-C-X2-C), which is characteristic of B12-dependent radical SAM enzymes but may make automated motif detection less straightforward.",
    "Distinguishing 5.3.99.13 from other 5.3.99.x entries would require knowing the specific reaction; however, among the four offered choices, only one is 5.3.99.x, so the family-level inference suffices for this MCQ.",
    "The EC 5.3.99.13 assignment is relatively recent (first characterized 2017, EC formally assigned later), so the '99' subclass reflects a recently discovered reaction type rather than a long-established family."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The radical SAM motif and domain architecture provide a clear basis to eliminate 5.3.1.8 (no radical SAM, TIM-barrel) and 2.3.1.312/2.3.1.290 (acyltransferases without radical SAM chemistry). Only 5.3.99.13 is consistent with a radical SAM isomerase among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry O24770 (OXSB_PRIMG) assigns EC 5.3.99.13 to this 744-aa protein with experimental evidence codes (ECO:0000269) from two independent biochemical studies (PubMed:28346939, PubMed:33560833) and corroborating X-ray crystallography at 1.80 Å (PDB:5UL2, 5UL3, 5UL4). The catalytic reaction (dAMP → 4'-phospho-dehydrooxetanocin, an intramolecular ring-contraction isomerization using SAM and B12) is consistent with EC 5.3.99.13. Sequence match is exact (SHA-256 identical, 744 aa).",
    "evidence_ids": ["C4", "C5", "C9", "H1", "H2", "H6", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a variant radical SAM cluster-binding motif in the region 'CDYSRCTFC' (C-X4-C-X2-C), a recognized variant of the canonical C-X3-C-X2-C motif found in B12-dependent radical SAM enzymes (e.g., PylB, OxsB). This motif is a well-known family-level feature transferable across many radical SAM proteins. Its presence argues against EC 5.3.1.8 (glucose-6-phosphate isomerase, a TIM-barrel enzyme using simple acid-base catalysis with no metal-cluster chemistry) and against EC 2.3.1.312/2.3.1.290 (acyltransferases that typically employ nucleophilic Ser/Cys catalysis, not radical SAM). Among the four choices, only 5.3.99.13 is a radical SAM isomerase, and the '99' subclass (other intramolecular oxidoreductases) is consistent with an unusual ring-contraction reaction. The large C-terminal hydrophobic domain (~400 aa) is also consistent with a B12-binding domain architecture shared by B12-dependent radical SAM enzymes, further supporting an EC 5 isomerase with radical SAM chemistry rather than a simple isomerase or acyltransferase.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the variant radical SAM motif (CX4CX2C) from the sequence, recall that this motif is associated with radical SAM enzymes (a large protein family), and reason that such enzymes are incompatible with the catalytic mechanisms of glucose-6-phosphate isomerase (EC 5.3.1.8) or acyltransferases (EC 2.3.1.x). The only remaining option consistent with radical SAM isomerase chemistry is 5.3.99.13. This is a family-level sequence-feature inference, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The radical SAM motif and domain architecture provide a clear basis to eliminate 5.3.1.8 (no radical SAM, TIM-barrel) and 2.3.1.312/2.3.1.290 (acyltransferases without radical SAM chemistry). Only 5.3.99.13 is consistent with a radical SAM isomerase among the offered choices."
  },
  "important_caveats": [
    "The radical SAM motif in this sequence is a variant (C-X4-C-X2-C rather than the canonical C-X3-C-X2-C), which is characteristic of B12-dependent radical SAM enzymes but may make automated motif detection less straightforward.",
    "Distinguishing 5.3.99.13 from other 5.3.99.x entries would require knowing the specific reaction; however, among the four offered choices, only one is 5.3.99.x, so the family-level inference suffices for this MCQ.",
    "The EC 5.3.99.13 assignment is relatively recent (first characterized 2017, EC formally assigned later), so the '99' subclass reflects a recently discovered reaction type rather than a long-established family."
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
  "benchmark_sequence_length": 744,
  "benchmark_sequence_sha256": "0af3073a7c236a71413178dc89485593fd423e6ef4fe0e3dbe801a5e5e561220",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1998-01-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 744,
  "current_source_sequence_sha256": "0af3073a7c236a71413178dc89485593fd423e6ef4fe0e3dbe801a5e5e561220",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O24770",
  "selected_historical_entry_version": 90,
  "selected_historical_record_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "selected_historical_source_sequence_length": 744,
  "selected_historical_source_sequence_sha256": "0af3073a7c236a71413178dc89485593fd423e6ef4fe0e3dbe801a5e5e561220",
  "selected_historical_version": {
    "accession": "O24770",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OXSB_PRIMG",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O24770\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1998-01-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacillus megaterium\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Priestia\"],\"scientificName\":\"Priestia megaterium\",\"taxonId\":1404}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"value\":\"Cobalamin-dependent S-adenosylmethionine radical enzyme OxsB\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"dAMP isomerase (4'-phospho-dehydrooxetanocin-forming)\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33560833\",\"source\":\"PubMed\"}],\"value\":\"5.3.99.13\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"4'-phospho-dehydrooxetanocin synthase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33560833\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81408\"}}],\"reaction\":{\"ecNumber\":\"5.3.99.13\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33560833\",\"source\":\"PubMed\"}],\"name\":\"dAMP + S-adenosyl-L-methionine = 4'-phospho-dehydrooxetanocin + 5'-deoxyadenosine + L-methionine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81407\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17319\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57844\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58245\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231877\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33560833\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81412\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33560833\",\"source\":\"PubMed\"}],\"name\":\"AH2 + 2 S-adenosyl-L-methionine = 2 5'-deoxyadenosin-5'-yl radical + 2 L-methionine + A + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81411\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57844\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231878\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33560833\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81416\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33560833\",\"source\":\"PubMed\"}],\"name\":\"2 5'-deoxyadenosin-5'-yl radical + 2 dAMP + A = 2 4'-phospho-dehydrooxetanocin + 2 5'-deoxyadenosine + AH2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81415\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17319\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58245\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231877\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231878\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhong A.\",\"Lee Y.H.\",\"Liu Y.N.\",\"Liu H.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33560833\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.0c00915\"}],\"citationType\":\"journal article\",\"firstPage\":\"537\",\"id\":\"33560833\",\"journal\":\"Biochemistry\",\"lastPage\":\"546\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of Oxetanocin-A Includes a B12-Dependent Radical SAM Enzyme That Can Catalyze both Oxidative Ring Contraction and the Demethylation of SAM.\",\"volume\":\"60\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Bridwell-Rabb J.\",\"Zhong A.\",\"Sun H.G.\",\"Drennan C.L.\",\"Liu H.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28346939\"},{\"database\":\"DOI\",\"id\":\"10.1038/nature21689\"}],\"citationType\":\"journal article\",\"firstPage\":\"322\",\"id\":\"28346939\",\"journal\":\"Nature\",\"lastPage\":\"326\",\"publicationDate\":\"2017\",\"title\":\"A B12-dependent radical SAM enzyme involved in oxetanocin A biosynthesis.\",\"volume\":\"544\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5UL2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5UL3\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5UL4\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) IN COMPLEXES WITH [4FE-4S] CLUSTER; COB(II)ALAMIN AND S-ADENOSYL-L-METHIONINE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"DOMAIN\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H1",
  "excerpt": "ID   OXSB_PRIMG              Reviewed;         744 AA.\nAC   O24770;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JAN-1998, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=4'-phospho-dehydrooxetanocin synthase {ECO:0000305};\nDE            EC=5.3.99.13 {ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};\nDE   AltName: Full=Cobalamin-dependent S-adenosylmethionine radical enzyme OxsB {ECO:0000303|PubMed:28346939};\nDE   AltName: Full=dAMP isomerase (4'-phospho-dehydrooxetanocin-forming) {ECO:0000305};\nGN   Name=oxsB {ECO:0000312|EMBL:BAA21631.1};\nOS   Priestia megaterium (Bacillus megaterium).\nOG   Plasmid pOXT1 {ECO:0000303|PubMed:10227144}.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Priestia.\nOX   NCBI_TaxID=1404;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4'-phospho-dehydrooxetanocin synthase {ECO:0000305};\nDE            EC=5.3.99.13 {ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};\nDE   AltName: Full=Cobalamin-dependent S-adenosylmethionine radical enzyme OxsB {ECO:0000303|PubMed:28346939};\nDE   AltName: Full=dAMP isomerase (4'-phospho-dehydrooxetanocin-forming) {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=NK84-0128; PLASMID=pOXT1;\nRX   PubMed=10227144; DOI=10.1271/bbb.63.563;\nRA   Morita M., Tomita K., Ishizawa M., Takagi K., Kawamura F., Takahashi H.,\nRA   Morino T.;\nRT   \"Cloning of oxetanocin A biosynthetic and resistance genes that reside on a\nRT   plasmid of Bacillus megaterium strain NK84-0128.\";\nRL   Biosci. Biotechnol. Biochem. 63:563-566(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=33560833; DOI=10.1021/acs.biochem.0c00915;\nRA   Zhong A., Lee Y.H., Liu Y.N., Liu H.W.;\nRT   \"Biosynthesis of Oxetanocin-A Includes a B12-Dependent Radical SAM Enzyme\nRT   That Can Catalyze both Oxidative Ring Contraction and the Demethylation of\nRT   SAM.\";\nRL   Biochemistry 60:537-546(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H5",
  "excerpt": "RN   [4] {ECO:0007744|PDB:5UL2, ECO:0007744|PDB:5UL3, ECO:0007744|PDB:5UL4}\nRP   X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) IN COMPLEXES WITH [4FE-4S] CLUSTER;\nRP   COB(II)ALAMIN AND S-ADENOSYL-L-METHIONINE, FUNCTION, CATALYTIC ACTIVITY,\nRP   COFACTOR, ACTIVITY REGULATION, AND DOMAIN.\nRX   PubMed=28346939; DOI=10.1038/nature21689;\nRA   Bridwell-Rabb J., Zhong A., Sun H.G., Drennan C.L., Liu H.W.;\nRT   \"A B12-dependent radical SAM enzyme involved in oxetanocin A\nRT   biosynthesis.\";\nRL   Nature 544:322-326(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=dAMP + S-adenosyl-L-methionine = 4'-phospho-dehydrooxetanocin\nCC         + 5'-deoxyadenosine + L-methionine + H(+); Xref=Rhea:RHEA:81407,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17319, ChEBI:CHEBI:57844,\nCC         ChEBI:CHEBI:58245, ChEBI:CHEBI:59789, ChEBI:CHEBI:231877;\nCC         EC=5.3.99.13; Evidence={ECO:0000269|PubMed:28346939,\nCC         ECO:0000269|PubMed:33560833};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81408;\nCC         Evidence={ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=AH2 + 2 S-adenosyl-L-methionine = 2 5'-deoxyadenosin-5'-yl\nCC         radical + 2 L-methionine + A + 2 H(+); Xref=Rhea:RHEA:81411,\nCC         ChEBI:CHEBI:13193, ChEBI:CHEBI:15378, ChEBI:CHEBI:17499,\nCC         ChEBI:CHEBI:57844, ChEBI:CHEBI:59789, ChEBI:CHEBI:231878;\nCC         Evidence={ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81412;\nCC         Evidence={ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 5'-deoxyadenosin-5'-yl radical + 2 dAMP + A = 2 4'-phospho-\nCC         dehydrooxetanocin + 2 5'-deoxyadenosine + AH2; Xref=Rhea:RHEA:81415,\nCC         ChEBI:CHEBI:13193, ChEBI:CHEBI:17319, ChEBI:CHEBI:17499,\nCC         ChEBI:CHEBI:58245, ChEBI:CHEBI:231877, ChEBI:CHEBI:231878;\nCC         Evidence={ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81416;\nCC         Evidence={ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
