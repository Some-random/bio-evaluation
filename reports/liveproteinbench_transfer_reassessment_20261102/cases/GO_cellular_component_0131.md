# GO_cellular_component_0131

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0131.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — nematocyst

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNHLIILVVAAVFLGMASAEDVFHKRFTVSCLCASDGPSVHGNKLTGTVAVGGCNPGWHKCNTEHNVLYECCKKN

[Multiple Choices]
A. inner membrane pellicle complex
B. mitochondrion
C. nematocyst
D. acrosomal membrane
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

> The sequence-matched UniProt record annotates the protein as secreted and located in a nematocyst, and assigns the GO nematocyst term. These are annotation-level support, not direct experimental localization evidence; the cited study evidence concerns peptide sequence, mass spectrometry, and toxicity rather than localization.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-peptide-like region followed by a short cysteine-rich peptide, a pattern consistent with a secreted disulfide-rich toxin. Transferable knowledge that cnidarian venom peptides are associated with nematocysts makes C a credible choice over the apicomplexan pellicle complex, mitochondrion, or sperm acrosomal membrane. The sequence alone does not prove nematocyst localization, but the alternatives make this family-level inference meaningfully discriminating.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A plausible inference comes from the secreted toxin-like sequence pattern and general knowledge of cnidarian venom storage, rather than requiring recall of this protein's database annotation. The inference is probabilistic because the input gives no organism or direct localization evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the signal-peptide-like, cysteine-rich toxin pattern.


### Important caveats

- The supplied input does not identify the organism, so the family-level inference is less certain than it would be with that context.
- The location annotation is not shown to be experimentally established; the cited experimental study evidence does not itself demonstrate nematocyst localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region followed by a short cysteine-rich peptide, a pattern consistent with a secreted disulfide-rich toxin. Transferable knowledge that cnidarian venom peptides are associated with nematocysts makes C a credible choice over the apicomplexan pellicle complex, mitochondrion, or sperm acrosomal membrane. The sequence alone does not prove nematocyst localization, but the alternatives make this family-level inference meaningfully discriminating.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A plausible inference comes from the secreted toxin-like sequence pattern and general knowledge of cnidarian venom storage, rather than requiring recall of this protein's database annotation. The inference is probabilistic because the input gives no organism or direct localization evidence."
  },
  "case_id": "GO_cellular_component_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H2",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as secreted and located in a nematocyst, and assigns the GO nematocyst term. These are annotation-level support, not direct experimental localization evidence; the cited study evidence concerns peptide sequence, mass spectrometry, and toxicity rather than localization."
  },
  "important_caveats": [
    "The supplied input does not identify the organism, so the family-level inference is less certain than it would be with that context.",
    "The location annotation is not shown to be experimentally established; the cited experimental study evidence does not itself demonstrate nematocyst localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the signal-peptide-like, cysteine-rich toxin pattern."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as secreted and located in a nematocyst, and assigns the GO nematocyst term. These are annotation-level support, not direct experimental localization evidence; the cited study evidence concerns peptide sequence, mass spectrometry, and toxicity rather than localization.",
    "evidence_ids": ["C5", "C7", "H2", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region followed by a short cysteine-rich peptide, a pattern consistent with a secreted disulfide-rich toxin. Transferable knowledge that cnidarian venom peptides are associated with nematocysts makes C a credible choice over the apicomplexan pellicle complex, mitochondrion, or sperm acrosomal membrane. The sequence alone does not prove nematocyst localization, but the alternatives make this family-level inference meaningfully discriminating.",
    "missing_item_specific_fact": "",
    "reason": "A plausible inference comes from the secreted toxin-like sequence pattern and general knowledge of cnidarian venom storage, rather than requiring recall of this protein's database annotation. The inference is probabilistic because the input gives no organism or direct localization evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the signal-peptide-like, cysteine-rich toxin pattern."
  },
  "important_caveats": [
    "The supplied input does not identify the organism, so the family-level inference is less certain than it would be with that context.",
    "The location annotation is not shown to be experimentally established; the cited experimental study evidence does not itself demonstrate nematocyst localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0N7KBN8 (U-stichotoxin-Hau3a from Heteractis aurora, a sea anemone) annotates the subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, curator inference from author statement). The GO cross-reference GO:0042151 (nematocyst) is present with IEA evidence. The sequence matches the benchmark input exactly (75 AA, same SHA256). The protein is a small peptide toxin isolated from a cnidarian, consistent with nematocyst localization.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [C3](#evidence-c3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear N-terminal signal peptide (hydrophobic stretch 'MNHLIILVVAAVFLGM' followed by 'ASA' cleavage motif), indicating entry into the secretory pathway—this eliminates mitochondrion (B), which uses an amphipathic targeting presequence rich in Arg/Ser/Thr. The mature portion (~54 residues) is a small, cysteine-rich peptide (7 cysteines in a compact domain forming multiple disulfide bonds), the hallmark of small peptide toxins. The GO definition of nematocyst (GO:0042151) explicitly states these organelles 'store toxins and can deliver them.' Inner membrane pellicle complex (A) is specific to apicomplexan parasites and comprises large structural proteins, not small disulfide-rich peptides. Acrosomal membrane (D) harbors larger hydrolytic enzymes (acrosin, hyaluronidase), not small toxin-like peptides. The combination of (1) signal peptide → secretory pathway, (2) very small size, and (3) dense cysteine/disulfide pattern uniquely matches the nematocyst toxin paradigm among the four offered choices. This reasoning relies on general principles of protein targeting, the well-known cysteine-rich toxin architecture of cnidarian peptides, and the functional definition of nematocyst as a toxin-storage organelle—all transferable knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the signal peptide morphology, the small cysteine-rich peptide architecture, and the functional definition of nematocyst as a toxin-storage organelle to eliminate the other three options and select C without needing to know this specific protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence features (signal peptide, small size, dense cysteine cluster) and the functional definitions of the four organelles cleanly distinguish C from A, B, and D. No alternative choice is defensible given the sequence.


### Important caveats

- The UniProt annotation evidence code is ECO:0000305 (curator inference from author statement), not direct experimental localization of the protein within the nematocyst; the GO annotation is IEA (inferred from electronic annotation).
- The reviewer identified the organism (Heteractis aurora, Cnidaria) from reviewer-only metadata; the evaluated model sees only the 75-aa sequence and the four choices. The reasoning above shows the sequence features alone support the answer without organism identity.
- The entry was first publicly released in April 2025; the benchmark construction date is unknown, so the author may have used a different annotation snapshot.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (hydrophobic stretch 'MNHLIILVVAAVFLGM' followed by 'ASA' cleavage motif), indicating entry into the secretory pathway—this eliminates mitochondrion (B), which uses an amphipathic targeting presequence rich in Arg/Ser/Thr. The mature portion (~54 residues) is a small, cysteine-rich peptide (7 cysteines in a compact domain forming multiple disulfide bonds), the hallmark of small peptide toxins. The GO definition of nematocyst (GO:0042151) explicitly states these organelles 'store toxins and can deliver them.' Inner membrane pellicle complex (A) is specific to apicomplexan parasites and comprises large structural proteins, not small disulfide-rich peptides. Acrosomal membrane (D) harbors larger hydrolytic enzymes (acrosin, hyaluronidase), not small toxin-like peptides. The combination of (1) signal peptide → secretory pathway, (2) very small size, and (3) dense cysteine/disulfide pattern uniquely matches the nematocyst toxin paradigm among the four offered choices. This reasoning relies on general principles of protein targeting, the well-known cysteine-rich toxin architecture of cnidarian peptides, and the functional definition of nematocyst as a toxin-storage organelle—all transferable knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the signal peptide morphology, the small cysteine-rich peptide architecture, and the functional definition of nematocyst as a toxin-storage organelle to eliminate the other three options and select C without needing to know this specific protein's database record."
  },
  "case_id": "GO_cellular_component_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5",
      "C3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0N7KBN8 (U-stichotoxin-Hau3a from Heteractis aurora, a sea anemone) annotates the subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, curator inference from author statement). The GO cross-reference GO:0042151 (nematocyst) is present with IEA evidence. The sequence matches the benchmark input exactly (75 AA, same SHA256). The protein is a small peptide toxin isolated from a cnidarian, consistent with nematocyst localization."
  },
  "important_caveats": [
    "The UniProt annotation evidence code is ECO:0000305 (curator inference from author statement), not direct experimental localization of the protein within the nematocyst; the GO annotation is IEA (inferred from electronic annotation).",
    "The reviewer identified the organism (Heteractis aurora, Cnidaria) from reviewer-only metadata; the evaluated model sees only the 75-aa sequence and the four choices. The reasoning above shows the sequence features alone support the answer without organism identity.",
    "The entry was first publicly released in April 2025; the benchmark construction date is unknown, so the author may have used a different annotation snapshot."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features (signal peptide, small size, dense cysteine cluster) and the functional definitions of the four organelles cleanly distinguish C from A, B, and D. No alternative choice is defensible given the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0N7KBN8 (U-stichotoxin-Hau3a from Heteractis aurora, a sea anemone) annotates the subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, curator inference from author statement). The GO cross-reference GO:0042151 (nematocyst) is present with IEA evidence. The sequence matches the benchmark input exactly (75 AA, same SHA256). The protein is a small peptide toxin isolated from a cnidarian, consistent with nematocyst localization.",
    "evidence_ids": ["C5", "C7", "H3", "H5", "C3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (hydrophobic stretch 'MNHLIILVVAAVFLGM' followed by 'ASA' cleavage motif), indicating entry into the secretory pathway—this eliminates mitochondrion (B), which uses an amphipathic targeting presequence rich in Arg/Ser/Thr. The mature portion (~54 residues) is a small, cysteine-rich peptide (7 cysteines in a compact domain forming multiple disulfide bonds), the hallmark of small peptide toxins. The GO definition of nematocyst (GO:0042151) explicitly states these organelles 'store toxins and can deliver them.' Inner membrane pellicle complex (A) is specific to apicomplexan parasites and comprises large structural proteins, not small disulfide-rich peptides. Acrosomal membrane (D) harbors larger hydrolytic enzymes (acrosin, hyaluronidase), not small toxin-like peptides. The combination of (1) signal peptide → secretory pathway, (2) very small size, and (3) dense cysteine/disulfide pattern uniquely matches the nematocyst toxin paradigm among the four offered choices. This reasoning relies on general principles of protein targeting, the well-known cysteine-rich toxin architecture of cnidarian peptides, and the functional definition of nematocyst as a toxin-storage organelle—all transferable knowledge.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the signal peptide morphology, the small cysteine-rich peptide architecture, and the functional definition of nematocyst as a toxin-storage organelle to eliminate the other three options and select C without needing to know this specific protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features (signal peptide, small size, dense cysteine cluster) and the functional definitions of the four organelles cleanly distinguish C from A, B, and D. No alternative choice is defensible given the sequence."
  },
  "important_caveats": [
    "The UniProt annotation evidence code is ECO:0000305 (curator inference from author statement), not direct experimental localization of the protein within the nematocyst; the GO annotation is IEA (inferred from electronic annotation).",
    "The reviewer identified the organism (Heteractis aurora, Cnidaria) from reviewer-only metadata; the evaluated model sees only the 75-aa sequence and the four choices. The reasoning above shows the sequence features alone support the answer without organism identity.",
    "The entry was first publicly released in April 2025; the benchmark construction date is unknown, so the author may have used a different annotation snapshot."
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
  "benchmark_sequence_length": 75,
  "benchmark_sequence_sha256": "d3ba29f7945503c50d555d8ce56e2e55320acdae069660dcd918d4cebfc05b41",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-01-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 75,
  "current_source_sequence_sha256": "d3ba29f7945503c50d555d8ce56e2e55320acdae069660dcd918d4cebfc05b41",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 27,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0N7KBN8",
  "selected_historical_entry_version": 27,
  "selected_historical_record_sha256": "1ce3ed23eec7f5b61c3571fb00341ae56831d6fb53df52f12c02ae9e520612ac",
  "selected_historical_source_sequence_length": 75,
  "selected_historical_source_sequence_sha256": "d3ba29f7945503c50d555d8ce56e2e55320acdae069660dcd918d4cebfc05b41",
  "selected_historical_version": {
    "accession": "A0A0N7KBN8",
    "database": "Swiss-Prot",
    "entryVersion": 27,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "NA3A_HETAU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0N7KBN8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:16.212733+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-01-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:16.212733+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Banded sea anemone\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Cnidaria\",\"Anthozoa\",\"Hexacorallia\",\"Actiniaria\",\"Stichodactylidae\",\"Heteractis\"],\"scientificName\":\"Heteractis aurora\",\"synonyms\":[\"Actinia aurora\"],\"taxonId\":478399}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:16.212733+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39530114\",\"source\":\"PubMed\"}],\"value\":\"Hau IV\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39530114\",\"source\":\"PubMed\"}],\"value\":\"U-stichotoxin-Hau3a\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39530114\",\"source\":\"PubMed\"}],\"value\":\"U-SHTX-Hau3a\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:16.212733+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"id\":\"SL-0177\",\"value\":\"Nematocyst\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:16.212733+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-02T04:24:16.212733+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0042151\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nematocyst\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:24:16.212733+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Homma T.\",\"Ishida M.\",\"Nagashima Y.\",\"Shiomi K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39530114\"},{\"database\":\"DOI\",\"id\":\"10.1590/1678-9199-jvatitd-2024-0019\"}],\"citationType\":\"journal article\",\"firstPage\":\"e20240019\",\"id\":\"39530114\",\"journal\":\"J. Venom. Anim. Toxins Incl. Trop. Dis.\",\"lastPage\":\"e20240019\",\"publicationDate\":\"2024\",\"title\":\"Isolation and cDNA cloning of four peptide toxins from the sea anemone Heteractis aurora.\",\"volume\":\"30\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAS68535.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"PROTEIN SEQUENCE OF 27-45\",\"MASS SPECTROMETRY\",\"TOXIC DOSE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:24:16.212733+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H1",
  "excerpt": "ID   NA3A_HETAU              Reviewed;          75 AA.\nAC   A0A0N7KBN8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-JAN-2016, sequence version 1.\nDT   28-JAN-2026, entry version 27.\nDE   RecName: Full=U-stichotoxin-Hau3a {ECO:0000303|PubMed:39530114};\nDE            Short=U-SHTX-Hau3a {ECO:0000303|PubMed:39530114};\nDE   AltName: Full=Hau IV {ECO:0000303|PubMed:39530114};\nDE   Flags: Precursor;\nGN   Name=HAUTX4 {ECO:0000312|EMBL:BAS68535.1};\nOS   Heteractis aurora (Banded sea anemone) (Actinia aurora).\nOC   Eukaryota; Metazoa; Cnidaria; Anthozoa; Hexacorallia; Actiniaria;\nOC   Stichodactylidae; Heteractis.\nOX   NCBI_TaxID=478399;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:19.138834+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce3ed23eec7f5b61c3571fb00341ae56831d6fb53df52f12c02ae9e520612ac",
  "url": "https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAS68535.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], PROTEIN SEQUENCE OF 27-45, MASS SPECTROMETRY,\nRP   AND TOXIC DOSE.\nRX   PubMed=39530114; DOI=10.1590/1678-9199-jvatitd-2024-0019;\nRA   Homma T., Ishida M., Nagashima Y., Shiomi K.;\nRT   \"Isolation and cDNA cloning of four peptide toxins from the sea anemone\nRT   Heteractis aurora.\";\nRL   J. Venom. Anim. Toxins Incl. Trop. Dis. 30:e20240019-e20240019(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:19.138834+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce3ed23eec7f5b61c3571fb00341ae56831d6fb53df52f12c02ae9e520612ac",
  "url": "https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305}. Nematocyst {ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:19.138834+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce3ed23eec7f5b61c3571fb00341ae56831d6fb53df52f12c02ae9e520612ac",
  "url": "https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:19.138834+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce3ed23eec7f5b61c3571fb00341ae56831d6fb53df52f12c02ae9e520612ac",
  "url": "https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0042151; C:nematocyst; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:19.138834+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce3ed23eec7f5b61c3571fb00341ae56831d6fb53df52f12c02ae9e520612ac",
  "url": "https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0002080\nname: acrosomal membrane\nnamespace: cellular_component\ndef: \"The membrane that surrounds the acrosomal lumen. The acrosome is a special type of lysosome in the head of a spermatozoon that contains acid hydrolases and is concerned with the breakdown of the outer membrane of the ovum during fertilization.\" [GOC:dph]\nis_a: GO:0030667 ! secretory granule membrane\nrelationship: part_of GO:0001669 ! acrosomal vesicle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0002080",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 14812-14819",
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
  "excerpt": "[Term]\nid: GO:0005739\nname: mitochondrion\nnamespace: cellular_component\ndef: \"A semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration.\" [GOC:giardia, ISBN:0198506732]\ncomment: Some anaerobic or microaerophilic organisms (e.g. Entamoeba histolytica, Giardia intestinalis and several Microsporidia species) do not have mitochondria, and contain mitochondrion-related organelles (MROs) instead, called mitosomes or hydrogenosomes, very likely derived from mitochondria. To annotate gene products located in these mitochondrial relics in species such as Entamoeba histolytica, Giardia intestinalis or others, please use GO:0032047 'mitosome' or GO:0042566 'hydrogenosome'. (See PMID:24316280 for a list of species currently known to contain mitochondrion-related organelles.)\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"mitochondria\" EXACT []\nxref: NIF_Subcellular:sao1860313010\nxref: Wikipedia:Mitochondrion\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005739",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58975-58998",
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
  "excerpt": "[Term]\nid: GO:0070258\nname: inner membrane pellicle complex\nnamespace: cellular_component\ndef: \"A membrane structure formed of two closely aligned lipid bilayers that lie beneath the plasma membrane and form part of the pellicle surrounding an apicomplexan parasite cell.\" [GOC:mah, PMID:12456714]\nsynonym: \"inner membrane complex\" BROAD []\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0020039 ! pellicle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0070258",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 365849-365857",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
