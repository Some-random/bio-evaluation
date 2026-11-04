# pathway_0047

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0047.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Protein modification

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTALDTDTPTAGRSAPLISPGPVIPPPDFGPLDRAQGWAMTAIITALAAITRFLNLGSPTDAGTPIFDEKHYAPQAWQVLHNDGVEDNPGYGLVVHPPVGKQLIAIGEWLFGYNGLGWRFSGAVCGVIIVMLVTRIARRISRSTLVGAIAGLLIIADGVSFVSSRTALLDVFLVMFAVAAFACLMVDRDQVRERMYHAFLDGRIAETRWGTRLGVRWWRFGAGVLLGLACATKWSGLYFVLFFGVMTLVFDAIARKQYHVPHPWRGMLRRDLGPAAYVFGLIPFAVYLASYAPWFASETAVNRYEVGRSIGPDSILPIPDALRSLWHYTHAAYRFHSNLTNADGNHHPWESKPWTWPMSLRPVLYAIDNQDVPGCGAQSCVKAVMLVGTPAMWFIAVPVLGWALWRTVVRRDWRYGAVLVGYMAGFLPWFADIDRQMYFFYATVMAPFLVLAIALILGDILYKPNQNPERRTLGLLTVCFYVALVITNFAWMYPILTGLPISQTTWNLQIWLPSWR

[Multiple Choices]
A. IMP biosynthesis via de novo pathway
B. ubiquinone biosynthesis. .
C. L-cystathionine from O-succinyl-L-homoserine: step 1/1. .
D. Protein modification
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence matches the annotated protein, whose pathway is listed as protein modification, specifically protein glycosylation. The pathway annotation carries an experimental evidence code, though the underlying study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly membrane-associated, with many hydrophobic segments, consistent with a membrane glycosyltransferase that modifies proteins. Transferable knowledge of bacterial protein O-mannosyltransferases connects this kind of enzyme to protein glycosylation and thus to option D. The other options name specific small-molecule biosynthetic or conversion pathways and are less consistent with that enzyme-family inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the sequence's membrane-protein character provide a meaningful basis for distinguishing protein modification from the offered metabolic alternatives. This is a probabilistic inference, not proof of the exact annotation from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, protein modification is the defensible pathway category for a protein O-mannosylating enzyme.


### Important caveats

- The pathway annotation is supported by a cited experimental evidence code, but the primary study was not independently assessed.
- The exact protein identity and its database annotation were reviewer-only evidence and are not used as the basis for transferability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly membrane-associated, with many hydrophobic segments, consistent with a membrane glycosyltransferase that modifies proteins. Transferable knowledge of bacterial protein O-mannosyltransferases connects this kind of enzyme to protein glycosylation and thus to option D. The other options name specific small-molecule biosynthetic or conversion pathways and are less consistent with that enzyme-family inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the sequence's membrane-protein character provide a meaningful basis for distinguishing protein modification from the offered metabolic alternatives. This is a probabilistic inference, not proof of the exact annotation from sequence alone."
  },
  "case_id": "pathway_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, whose pathway is listed as protein modification, specifically protein glycosylation. The pathway annotation carries an experimental evidence code, though the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The pathway annotation is supported by a cited experimental evidence code, but the primary study was not independently assessed.",
    "The exact protein identity and its database annotation were reviewer-only evidence and are not used as the basis for transferability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, protein modification is the defensible pathway category for a protein O-mannosylating enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, whose pathway is listed as protein modification, specifically protein glycosylation. The pathway annotation carries an experimental evidence code, though the underlying study was not independently reviewed here.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly membrane-associated, with many hydrophobic segments, consistent with a membrane glycosyltransferase that modifies proteins. Transferable knowledge of bacterial protein O-mannosyltransferases connects this kind of enzyme to protein glycosylation and thus to option D. The other options name specific small-molecule biosynthetic or conversion pathways and are less consistent with that enzyme-family inference.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the sequence's membrane-protein character provide a meaningful basis for distinguishing protein modification from the offered metabolic alternatives. This is a probabilistic inference, not proof of the exact annotation from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, protein modification is the defensible pathway category for a protein O-mannosylating enzyme."
  },
  "important_caveats": [
    "The pathway annotation is supported by a cited experimental evidence code, but the primary study was not independently assessed.",
    "The exact protein identity and its database annotation were reviewer-only evidence and are not used as the basis for transferability."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (both current and historical, evidence C5 and H3) annotates the pathway as 'Protein modification; protein glycosylation.' The protein is a polyprenol-phosphate-mannose--protein mannosyltransferase (PMT, EC 2.4.1.-), which catalyzes O-mannosylation of proteins—a protein modification reaction. The author's answer D ('Protein modification') aligns directly with this annotation, which is supported by experimental evidence (PubMed:23550160, ECO:0000269).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmarks of the DUF2666/PMT (polyprenol-phosphate-mannose protein mannosyltransferase) family: (1) an N-terminal signal peptide followed by approximately 8–10 transmembrane helices, consistent with membrane-bound glycosyltransferases; (2) characteristic 'QY' and 'DR' motifs embedded within hydrophobic segments (e.g., '…FDAIARKQY', '…ADIDRQMY…', '…GDILYKPNQNPERR…'), which are signature residues of the DUF2666/PMT domain found across eukaryotic and bacterial PMT homologs; (3) a cytoplasmic loop region with '…PDALRSLWHYTHAAYRFHSN…' resembling the catalytic loop of PMT family members. A model with knowledge of the PMT/DUF2666 family (e.g., eukaryotic PMT1/PMT2, bacterial PmtA) would recognize this multi-pass membrane glycosyltransferase architecture and infer protein O-mannosylation—a protein modification. The distractors are architecturally and mechanistically distinct: IMP biosynthesis (A) involves soluble purine-pathway enzymes; ubiquinone biosynthesis (B) involves prenyltransferases (UbiA-type) and hydroxylases with different domain topologies; cystathionine synthesis (C) is a single-step reaction by a soluble PLP-dependent enzyme. None of these alternatives feature the DUF2666 multi-TM membrane glycosyltransferase architecture.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the DUF2666/PMT domain family and its multi-pass membrane topology is transferable knowledge from well-characterized eukaryotic and bacterial PMT homologs. The distinctive QY/DR motifs within transmembrane segments, combined with the overall membrane architecture, meaningfully distinguish 'Protein modification' (D) from the three soluble or mechanistically unrelated pathway options. This does not require memorizing this exact protein's UniProt record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent clearly distinct biochemical pathways. Option D ('Protein modification') is the broad UniProt pathway category encompassing glycosylation, and the other three options describe specific metabolic steps (purine synthesis, ubiquinone synthesis, amino acid biosynthesis) that are mechanistically and structurally incompatible with a multi-pass membrane DUF2666/PMT glycosyltransferase. No ambiguity in selecting the correct option.


### Important caveats

- The UniProt pathway annotation 'Protein modification; protein glycosylation' is supported by experimental evidence (ECO:0000269, PubMed:23550160), not merely computational inference.
- The DUF2666 domain recognition argument relies on the model's familiarity with the PMT family across organisms; a model lacking this family-level knowledge might struggle with the motif identification.
- Option D uses the broad UniProt pathway category name rather than the specific sub-pathway ('protein glycosylation'), which is acceptable but less precise.
- The reviewer-only evidence confirms sequence match and annotation, but the evaluated model only had the raw sequence and four options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmarks of the DUF2666/PMT (polyprenol-phosphate-mannose protein mannosyltransferase) family: (1) an N-terminal signal peptide followed by approximately 8–10 transmembrane helices, consistent with membrane-bound glycosyltransferases; (2) characteristic 'QY' and 'DR' motifs embedded within hydrophobic segments (e.g., '…FDAIARKQY', '…ADIDRQMY…', '…GDILYKPNQNPERR…'), which are signature residues of the DUF2666/PMT domain found across eukaryotic and bacterial PMT homologs; (3) a cytoplasmic loop region with '…PDALRSLWHYTHAAYRFHSN…' resembling the catalytic loop of PMT family members. A model with knowledge of the PMT/DUF2666 family (e.g., eukaryotic PMT1/PMT2, bacterial PmtA) would recognize this multi-pass membrane glycosyltransferase architecture and infer protein O-mannosylation—a protein modification. The distractors are architecturally and mechanistically distinct: IMP biosynthesis (A) involves soluble purine-pathway enzymes; ubiquinone biosynthesis (B) involves prenyltransferases (UbiA-type) and hydroxylases with different domain topologies; cystathionine synthesis (C) is a single-step reaction by a soluble PLP-dependent enzyme. None of these alternatives feature the DUF2666 multi-TM membrane glycosyltransferase architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the DUF2666/PMT domain family and its multi-pass membrane topology is transferable knowledge from well-characterized eukaryotic and bacterial PMT homologs. The distinctive QY/DR motifs within transmembrane segments, combined with the overall membrane architecture, meaningfully distinguish 'Protein modification' (D) from the three soluble or mechanistically unrelated pathway options. This does not require memorizing this exact protein's UniProt record."
  },
  "case_id": "pathway_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (both current and historical, evidence C5 and H3) annotates the pathway as 'Protein modification; protein glycosylation.' The protein is a polyprenol-phosphate-mannose--protein mannosyltransferase (PMT, EC 2.4.1.-), which catalyzes O-mannosylation of proteins—a protein modification reaction. The author's answer D ('Protein modification') aligns directly with this annotation, which is supported by experimental evidence (PubMed:23550160, ECO:0000269)."
  },
  "important_caveats": [
    "The UniProt pathway annotation 'Protein modification; protein glycosylation' is supported by experimental evidence (ECO:0000269, PubMed:23550160), not merely computational inference.",
    "The DUF2666 domain recognition argument relies on the model's familiarity with the PMT family across organisms; a model lacking this family-level knowledge might struggle with the motif identification.",
    "Option D uses the broad UniProt pathway category name rather than the specific sub-pathway ('protein glycosylation'), which is acceptable but less precise.",
    "The reviewer-only evidence confirms sequence match and annotation, but the evaluated model only had the raw sequence and four options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct biochemical pathways. Option D ('Protein modification') is the broad UniProt pathway category encompassing glycosylation, and the other three options describe specific metabolic steps (purine synthesis, ubiquinone synthesis, amino acid biosynthesis) that are mechanistically and structurally incompatible with a multi-pass membrane DUF2666/PMT glycosyltransferase. No ambiguity in selecting the correct option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (both current and historical, evidence C5 and H3) annotates the pathway as 'Protein modification; protein glycosylation.' The protein is a polyprenol-phosphate-mannose--protein mannosyltransferase (PMT, EC 2.4.1.-), which catalyzes O-mannosylation of proteins—a protein modification reaction. The author's answer D ('Protein modification') aligns directly with this annotation, which is supported by experimental evidence (PubMed:23550160, ECO:0000269).",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmarks of the DUF2666/PMT (polyprenol-phosphate-mannose protein mannosyltransferase) family: (1) an N-terminal signal peptide followed by approximately 8–10 transmembrane helices, consistent with membrane-bound glycosyltransferases; (2) characteristic 'QY' and 'DR' motifs embedded within hydrophobic segments (e.g., '…FDAIARKQY', '…ADIDRQMY…', '…GDILYKPNQNPERR…'), which are signature residues of the DUF2666/PMT domain found across eukaryotic and bacterial PMT homologs; (3) a cytoplasmic loop region with '…PDALRSLWHYTHAAYRFHSN…' resembling the catalytic loop of PMT family members. A model with knowledge of the PMT/DUF2666 family (e.g., eukaryotic PMT1/PMT2, bacterial PmtA) would recognize this multi-pass membrane glycosyltransferase architecture and infer protein O-mannosylation—a protein modification. The distractors are architecturally and mechanistically distinct: IMP biosynthesis (A) involves soluble purine-pathway enzymes; ubiquinone biosynthesis (B) involves prenyltransferases (UbiA-type) and hydroxylases with different domain topologies; cystathionine synthesis (C) is a single-step reaction by a soluble PLP-dependent enzyme. None of these alternatives feature the DUF2666 multi-TM membrane glycosyltransferase architecture.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the DUF2666/PMT domain family and its multi-pass membrane topology is transferable knowledge from well-characterized eukaryotic and bacterial PMT homologs. The distinctive QY/DR motifs within transmembrane segments, combined with the overall membrane architecture, meaningfully distinguish 'Protein modification' (D) from the three soluble or mechanistically unrelated pathway options. This does not require memorizing this exact protein's UniProt record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct biochemical pathways. Option D ('Protein modification') is the broad UniProt pathway category encompassing glycosylation, and the other three options describe specific metabolic steps (purine synthesis, ubiquinone synthesis, amino acid biosynthesis) that are mechanistically and structurally incompatible with a multi-pass membrane DUF2666/PMT glycosyltransferase. No ambiguity in selecting the correct option."
  },
  "important_caveats": [
    "The UniProt pathway annotation 'Protein modification; protein glycosylation' is supported by experimental evidence (ECO:0000269, PubMed:23550160), not merely computational inference.",
    "The DUF2666 domain recognition argument relies on the model's familiarity with the PMT family across organisms; a model lacking this family-level knowledge might struggle with the motif identification.",
    "Option D uses the broad UniProt pathway category name rather than the specific sub-pathway ('protein glycosylation'), which is acceptable but less precise.",
    "The reviewer-only evidence confirms sequence match and annotation, but the evaluated model only had the raw sequence and four options."
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
  "benchmark_sequence_length": 516,
  "benchmark_sequence_sha256": "283fcdf8941135b9c8b4851bf735e03f92c71bebe99b9f17b27ab97279f6a1a0",
  "current_entry_audit": {
    "entryVersion": 116,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-01-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 516,
  "current_source_sequence_sha256": "283fcdf8941135b9c8b4851bf735e03f92c71bebe99b9f17b27ab97279f6a1a0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 114,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0R3E8",
  "selected_historical_entry_version": 114,
  "selected_historical_record_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "selected_historical_source_sequence_length": 516,
  "selected_historical_source_sequence_sha256": "283fcdf8941135b9c8b4851bf735e03f92c71bebe99b9f17b27ab97279f6a1a0",
  "selected_historical_version": {
    "accession": "A0R3E8",
    "database": "Swiss-Prot",
    "entryVersion": 114,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PMT_MYCS2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0R3E8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":116,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-01-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mycobacterium smegmatis\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Mycobacteriales\",\"Mycobacteriaceae\",\"Mycolicibacterium\"],\"scientificName\":\"Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155)\",\"taxonId\":246196}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23550160\",\"source\":\"PubMed\"}],\"value\":\"Protein O-mannosyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23550160\",\"source\":\"PubMed\"}],\"value\":\"PMT\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23550160\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Polyprenol-phosphate-mannose--protein mannosyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23550160\",\"source\":\"PubMed\"}],\"value\":\"Protein modification; protein glycosylation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu C.F.\",\"Tonini L.\",\"Malaga W.\",\"Beau M.\",\"Stella A.\",\"Bouyssie D.\",\"Jackson M.C.\",\"Nigou J.\",\"Puzo G.\",\"Guilhot C.\",\"Burlet-Schiltz O.\",\"Riviere M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23550160\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1219704110\"}],\"citationType\":\"journal article\",\"firstPage\":\"6560\",\"id\":\"23550160\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"6565\",\"publicationDate\":\"2013\",\"title\":\"Bacterial protein-O-mannosylating enzyme is crucial for virulence of Mycobacterium tuberculosis.\",\"volume\":\"110\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700084 / mc(2)155\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H1",
  "excerpt": "ID   PMT_MYCS2               Reviewed;         516 AA.\nAC   A0R3E8; I7GFC3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-JAN-2007, sequence version 1.\nDT   28-JAN-2026, entry version 114.\nDE   RecName: Full=Polyprenol-phosphate-mannose--protein mannosyltransferase {ECO:0000305};\nDE            EC=2.4.1.- {ECO:0000305|PubMed:23550160};\nDE   AltName: Full=Protein O-mannosyltransferase {ECO:0000303|PubMed:23550160};\nDE            Short=PMT {ECO:0000303|PubMed:23550160};\nGN   OrderedLocusNames=MSMEG_5447 {ECO:0000312|EMBL:ABK72177.1},\nGN   MSMEI_5297 {ECO:0000312|EMBL:AFP41739.1};\nOS   Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155) (Mycobacterium\nOS   smegmatis).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales;\nOC   Mycobacteriaceae; Mycolicibacterium.\nOX   NCBI_TaxID=246196;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 700084 / mc(2)155;\nRX   PubMed=23550160; DOI=10.1073/pnas.1219704110;\nRA   Liu C.F., Tonini L., Malaga W., Beau M., Stella A., Bouyssie D.,\nRA   Jackson M.C., Nigou J., Puzo G., Guilhot C., Burlet-Schiltz O., Riviere M.;\nRT   \"Bacterial protein-O-mannosylating enzyme is crucial for virulence of\nRT   Mycobacterium tuberculosis.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 110:6560-6565(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Protein modification; protein glycosylation.\nCC       {ECO:0000269|PubMed:23550160}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 47. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
