# GO_molecular_function_0020

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0020.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — polynucleotide 5&#x27;-phosphatase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATPKSFRDNLAEILKTHDFRTVELEFRLGFQAPGEFITNINKHVWTTAKEKLGTPAQELVMVDKYIRSTPGESSRYVVFPDGQGYWEHKKKVAKETTTGGKYGVRSAFSLERRENGKPPVSFRMQRTKYRTTFVKGPWKIDFTRVESIPATDRDCESTYEIEVELYDMFYLFEKELDIIIQEGNKLVQSIVM

[Multiple Choices]
A. peptidyl-arginine 3-dioxygenase activity
B. ubiquitin-like protein transferase activity
C. polynucleotide 5'-phosphatase activity
D. aspartic-type endopeptidase activity
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

> The sequence-matched record reports experimentally supported removal of the gamma-phosphate from nascent mRNA, yielding a diphosphate end. That activity falls under the broader polynucleotide 5′-phosphatase term in choice C.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO2](#evidence-go2), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 193-aa sequence is compatible with a compact enzyme family involved in RNA 5′-end triphosphate hydrolysis. Homology/profile recognition of related RNA triphosphatases, whose activity is removal of phosphate from a polynucleotide 5′ end, would favor C over the offered protein hydroxylase, ubiquitin-like transferase, and peptide-cleaving protease alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference can distinguish the broad nucleic-acid phosphatase activity from the three alternatives without knowing this protein’s exact database entry. The sequence alone does not establish substrate specificity or experimental activity, so the inference is probabilistic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reported mRNA 5′-triphosphate hydrolysis is encompassed by choice C; the other options describe distinct activities.


### Important caveats

- The source record is sequence-matched and cites experimental evidence, but the author's exact database snapshot is unknown.
- The evidence supports a more specific mRNA 5′-triphosphate monophosphatase activity; choice C is its broader GO parent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 193-aa sequence is compatible with a compact enzyme family involved in RNA 5′-end triphosphate hydrolysis. Homology/profile recognition of related RNA triphosphatases, whose activity is removal of phosphate from a polynucleotide 5′ end, would favor C over the offered protein hydroxylase, ubiquitin-like transferase, and peptide-cleaving protease alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can distinguish the broad nucleic-acid phosphatase activity from the three alternatives without knowing this protein’s exact database entry. The sequence alone does not establish substrate specificity or experimental activity, so the inference is probabilistic."
  },
  "case_id": "GO_molecular_function_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "GO2",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record reports experimentally supported removal of the gamma-phosphate from nascent mRNA, yielding a diphosphate end. That activity falls under the broader polynucleotide 5′-phosphatase term in choice C."
  },
  "important_caveats": [
    "The source record is sequence-matched and cites experimental evidence, but the author's exact database snapshot is unknown.",
    "The evidence supports a more specific mRNA 5′-triphosphate monophosphatase activity; choice C is its broader GO parent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reported mRNA 5′-triphosphate hydrolysis is encompassed by choice C; the other options describe distinct activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record reports experimentally supported removal of the gamma-phosphate from nascent mRNA, yielding a diphosphate end. That activity falls under the broader polynucleotide 5′-phosphatase term in choice C.",
    "evidence_ids": ["C5", "C6", "C7", "GO2", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 193-aa sequence is compatible with a compact enzyme family involved in RNA 5′-end triphosphate hydrolysis. Homology/profile recognition of related RNA triphosphatases, whose activity is removal of phosphate from a polynucleotide 5′ end, would favor C over the offered protein hydroxylase, ubiquitin-like transferase, and peptide-cleaving protease alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can distinguish the broad nucleic-acid phosphatase activity from the three alternatives without knowing this protein’s exact database entry. The sequence alone does not establish substrate specificity or experimental activity, so the inference is probabilistic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reported mRNA 5′-triphosphate hydrolysis is encompassed by choice C; the other options describe distinct activities."
  },
  "important_caveats": [
    "The source record is sequence-matched and cites experimental evidence, but the author's exact database snapshot is unknown.",
    "The evidence supports a more specific mRNA 5′-triphosphate monophosphatase activity; choice C is its broader GO parent."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q98500 (sequence matched) annotates GO:0004651 (polynucleotide 5'-phosphatase activity) via IEA:InterPro, and the experimentally supported term GO:0140818 (mRNA 5'-triphosphate monophosphatase activity, EXP from PubMed:11160672) is a child of GO:0004651 in the ontology (is_a edge confirmed in GO5). The protein's EC 3.6.1.74 reaction (removing gamma-phosphate from 5'-triphosphate mRNA) is thus encompassed by the broader GO:0004651 definition within the GO hierarchy. The answer is the parent/broader term rather than the most specific experimental annotation, but it is a valid GO assignment for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [H6](#evidence-h6), [GO2](#evidence-go2), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable VDK phosphatase catalytic motif ('VMVDKYIRSTPG'), a well-known signature across multiple phosphatase families (serine/threonine phosphatases, tunnel-family RNA triphosphatases, etc.) where the aspartate serves as the catalytic residue. Among the four offered choices, only C (polynucleotide 5'-phosphatase activity) describes a phosphatase reaction; A is a 2-oxoglutarate-dependent dioxygenase (requires HxD/E-H...H facial triad, absent here), B is a ubiquitin-like protein transferase (requires RING/U-box/HECT/RBR domains, absent), and D is an aspartic endopeptidase (requires D-T-G-S or D-S-T-G-S active-site motifs and a bilobal fold, absent). Recognizing the VDK motif as a phosphatase signature eliminates A, B, and D, leaving C. Additionally, the small size (~193 aa) and the context of encoding a capping-enzyme component are consistent with tunnel-family viral RNA triphosphatases found across large DNA viruses (vaccinia, ASFV, PBCV-1), a family-level pattern learned from other viral proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the VDK phosphatase motif in the sequence, recognize the absence of protease, transferase, and dioxygenase structural motifs, and use family-level knowledge of viral capping enzymes to select the only phosphatase option. This does not require recalling the specific UniProt annotation for Q98500.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four distinct enzyme classes (dioxygenase, transferase, phosphatase, endopeptidase). The VDK motif and absence of other catalytic signatures clearly favor the phosphatase option. No two options are defensible given the sequence features.


### Important caveats

- The expected answer C (GO:0004651) is the parent/broader term; the most specific experimental annotation is GO:0140818 (mRNA 5'-triphosphate monophosphatase activity). The GO hierarchy (GO:0140818 is_a GO:0004651) makes C valid but less precise.
- The GO:0004651 annotation in UniProt is IEA:InterPro (inferred), while the experimental evidence (EXP) supports the child term GO:0140818.
- The EC numbers differ: GO:0004651 maps to EC 3.1.3.33 (phosphoric monoester hydrolase), while the protein's actual EC is 3.6.1.74 (phosphoric diester hydrolase). The ontology nonetheless subsumes the latter under the former.
- The reviewer-only evidence identifies the protein as PBCV-1 A449R, but this organism/accession information was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable VDK phosphatase catalytic motif ('VMVDKYIRSTPG'), a well-known signature across multiple phosphatase families (serine/threonine phosphatases, tunnel-family RNA triphosphatases, etc.) where the aspartate serves as the catalytic residue. Among the four offered choices, only C (polynucleotide 5'-phosphatase activity) describes a phosphatase reaction; A is a 2-oxoglutarate-dependent dioxygenase (requires HxD/E-H...H facial triad, absent here), B is a ubiquitin-like protein transferase (requires RING/U-box/HECT/RBR domains, absent), and D is an aspartic endopeptidase (requires D-T-G-S or D-S-T-G-S active-site motifs and a bilobal fold, absent). Recognizing the VDK motif as a phosphatase signature eliminates A, B, and D, leaving C. Additionally, the small size (~193 aa) and the context of encoding a capping-enzyme component are consistent with tunnel-family viral RNA triphosphatases found across large DNA viruses (vaccinia, ASFV, PBCV-1), a family-level pattern learned from other viral proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the VDK phosphatase motif in the sequence, recognize the absence of protease, transferase, and dioxygenase structural motifs, and use family-level knowledge of viral capping enzymes to select the only phosphatase option. This does not require recalling the specific UniProt annotation for Q98500."
  },
  "case_id": "GO_molecular_function_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H5",
      "H6",
      "GO2",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q98500 (sequence matched) annotates GO:0004651 (polynucleotide 5'-phosphatase activity) via IEA:InterPro, and the experimentally supported term GO:0140818 (mRNA 5'-triphosphate monophosphatase activity, EXP from PubMed:11160672) is a child of GO:0004651 in the ontology (is_a edge confirmed in GO5). The protein's EC 3.6.1.74 reaction (removing gamma-phosphate from 5'-triphosphate mRNA) is thus encompassed by the broader GO:0004651 definition within the GO hierarchy. The answer is the parent/broader term rather than the most specific experimental annotation, but it is a valid GO assignment for this protein."
  },
  "important_caveats": [
    "The expected answer C (GO:0004651) is the parent/broader term; the most specific experimental annotation is GO:0140818 (mRNA 5'-triphosphate monophosphatase activity). The GO hierarchy (GO:0140818 is_a GO:0004651) makes C valid but less precise.",
    "The GO:0004651 annotation in UniProt is IEA:InterPro (inferred), while the experimental evidence (EXP) supports the child term GO:0140818.",
    "The EC numbers differ: GO:0004651 maps to EC 3.1.3.33 (phosphoric monoester hydrolase), while the protein's actual EC is 3.6.1.74 (phosphoric diester hydrolase). The ontology nonetheless subsumes the latter under the former.",
    "The reviewer-only evidence identifies the protein as PBCV-1 A449R, but this organism/accession information was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four distinct enzyme classes (dioxygenase, transferase, phosphatase, endopeptidase). The VDK motif and absence of other catalytic signatures clearly favor the phosphatase option. No two options are defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q98500 (sequence matched) annotates GO:0004651 (polynucleotide 5'-phosphatase activity) via IEA:InterPro, and the experimentally supported term GO:0140818 (mRNA 5'-triphosphate monophosphatase activity, EXP from PubMed:11160672) is a child of GO:0004651 in the ontology (is_a edge confirmed in GO5). The protein's EC 3.6.1.74 reaction (removing gamma-phosphate from 5'-triphosphate mRNA) is thus encompassed by the broader GO:0004651 definition within the GO hierarchy. The answer is the parent/broader term rather than the most specific experimental annotation, but it is a valid GO assignment for this protein.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H5", "H6", "GO2", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable VDK phosphatase catalytic motif ('VMVDKYIRSTPG'), a well-known signature across multiple phosphatase families (serine/threonine phosphatases, tunnel-family RNA triphosphatases, etc.) where the aspartate serves as the catalytic residue. Among the four offered choices, only C (polynucleotide 5'-phosphatase activity) describes a phosphatase reaction; A is a 2-oxoglutarate-dependent dioxygenase (requires HxD/E-H...H facial triad, absent here), B is a ubiquitin-like protein transferase (requires RING/U-box/HECT/RBR domains, absent), and D is an aspartic endopeptidase (requires D-T-G-S or D-S-T-G-S active-site motifs and a bilobal fold, absent). Recognizing the VDK motif as a phosphatase signature eliminates A, B, and D, leaving C. Additionally, the small size (~193 aa) and the context of encoding a capping-enzyme component are consistent with tunnel-family viral RNA triphosphatases found across large DNA viruses (vaccinia, ASFV, PBCV-1), a family-level pattern learned from other viral proteins.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the VDK phosphatase motif in the sequence, recognize the absence of protease, transferase, and dioxygenase structural motifs, and use family-level knowledge of viral capping enzymes to select the only phosphatase option. This does not require recalling the specific UniProt annotation for Q98500."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four distinct enzyme classes (dioxygenase, transferase, phosphatase, endopeptidase). The VDK motif and absence of other catalytic signatures clearly favor the phosphatase option. No two options are defensible given the sequence features."
  },
  "important_caveats": [
    "The expected answer C (GO:0004651) is the parent/broader term; the most specific experimental annotation is GO:0140818 (mRNA 5'-triphosphate monophosphatase activity). The GO hierarchy (GO:0140818 is_a GO:0004651) makes C valid but less precise.",
    "The GO:0004651 annotation in UniProt is IEA:InterPro (inferred), while the experimental evidence (EXP) supports the child term GO:0140818.",
    "The EC numbers differ: GO:0004651 maps to EC 3.1.3.33 (phosphoric monoester hydrolase), while the protein's actual EC is 3.6.1.74 (phosphoric diester hydrolase). The ontology nonetheless subsumes the latter under the former.",
    "The reviewer-only evidence identifies the protein as PBCV-1 A449R, but this organism/accession information was not available to the evaluated model."
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
  "benchmark_sequence_length": 193,
  "benchmark_sequence_sha256": "2e3ef2dd5cc36f7f2ffcab76a32ce1bb6958f79ccde3e9c943bcd61f8649ed54",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1997-02-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 193,
  "current_source_sequence_sha256": "2e3ef2dd5cc36f7f2ffcab76a32ce1bb6958f79ccde3e9c943bcd61f8649ed54",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 85,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q98500",
  "selected_historical_entry_version": 85,
  "selected_historical_record_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "selected_historical_source_sequence_length": 193,
  "selected_historical_source_sequence_sha256": "2e3ef2dd5cc36f7f2ffcab76a32ce1bb6958f79ccde3e9c943bcd61f8649ed54",
  "selected_historical_version": {
    "accession": "Q98500",
    "database": "Swiss-Prot",
    "entryVersion": 85,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "TPASE_PBCV1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q98500\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1997-02-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"PBCV-1\",\"lineage\":[\"Viruses\",\"Varidnaviria\",\"Bamfordvirae\",\"Nucleocytoviricota\",\"Megaviricetes\",\"Algavirales\",\"Phycodnaviridae\",\"Chlorovirus\",\"Chlorovirus vanettense\"],\"scientificName\":\"Paramecium bursaria Chlorella virus 1\",\"taxonId\":10506}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"value\":\"3.6.1.74\"}],\"fullName\":{\"value\":\"5'RNA triphosphatase A449R\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11160672\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the first stes of cap formation: by removing the gamma-phosphate from the 5'-triphosphate end of nascent mRNA to yield a diphosphate end\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11160672\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:67005\"}}],\"reaction\":{\"ecNumber\":\"3.6.1.74\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11160672\",\"source\":\"PubMed\"}],\"name\":\"a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end diphospho-ribonucleoside in mRNA + phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:67004\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:17164\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:17165\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:167616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:167618\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11160672\",\"source\":\"PubMed\"}],\"id\":\"GO:0140818\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:mRNA 5'-triphosphate monophosphatase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/8",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Ho C.K.\",\"Gong C.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11160672\"},{\"database\":\"DOI\",\"id\":\"10.1128/jvi.75.4.1744-1750.2001\"}],\"citationType\":\"journal article\",\"firstPage\":\"1744\",\"id\":\"11160672\",\"journal\":\"J. Virol.\",\"lastPage\":\"1750\",\"publicationDate\":\"2001\",\"title\":\"RNA triphosphatase component of the mRNA capping apparatus of Paramecium bursaria Chlorella virus 1.\",\"volume\":\"75\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CHARACTERIZATION OF TRIPHOSPHATASE ACTIVITY\",\"MUTAGENESIS OF GLU-26\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H1",
  "excerpt": "ID   TPASE_PBCV1             Reviewed;         193 AA.\nAC   Q98500;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-FEB-1997, sequence version 1.\nDT   28-JAN-2026, entry version 85.\nDE   RecName: Full=5'RNA triphosphatase A449R;\nDE            EC=3.6.1.74;\nGN   Name=A449R;\nOS   Paramecium bursaria Chlorella virus 1 (PBCV-1).\nOC   Viruses; Varidnaviria; Bamfordvirae; Nucleocytoviricota; Megaviricetes;\nOC   Algavirales; Phycodnaviridae; Chlorovirus; Chlorovirus vanettense.\nOX   NCBI_TaxID=10506;\nOH   NCBI_TaxID=3071; Chlorella.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CHARACTERIZATION OF TRIPHOSPHATASE ACTIVITY, AND MUTAGENESIS OF\nRP   GLU-26.\nRX   PubMed=11160672; DOI=10.1128/jvi.75.4.1744-1750.2001;\nRA   Ho C.K., Gong C., Shuman S.;\nRT   \"RNA triphosphatase component of the mRNA capping apparatus of Paramecium\nRT   bursaria Chlorella virus 1.\";\nRL   J. Virol. 75:1744-1750(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the first stes of cap formation: by removing the\nCC       gamma-phosphate from the 5'-triphosphate end of nascent mRNA to yield a\nCC       diphosphate end. {ECO:0000269|PubMed:11160672}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end\nCC         diphospho-ribonucleoside in mRNA + phosphate + H(+);\nCC         Xref=Rhea:RHEA:67004, Rhea:RHEA-COMP:17164, Rhea:RHEA-COMP:17165,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:167616, ChEBI:CHEBI:167618; EC=3.6.1.74;\nCC         Evidence={ECO:0000269|PubMed:11160672};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:67005;\nCC         Evidence={ECO:0000269|PubMed:11160672};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0140818; F:mRNA 5'-triphosphate monophosphatase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0004651; F:polynucleotide 5'-phosphatase activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004190\nname: aspartic-type endopeptidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of internal, alpha-peptide bonds in a polypeptide chain by a mechanism in which a water molecule bound by the side chains of aspartic residues at the active center acts as a nucleophile.\" [ISBN:0198506732]\nsynonym: \"aspartate protease activity\" NARROW [GOC:mah, GOC:vw]\nsynonym: \"aspartic endopeptidase activity\" EXACT []\nsynonym: \"aspartic protease activity\" NARROW []\nsynonym: \"aspartyl protease activity\" NARROW []\nsynonym: \"carboxyl protease activity\" NARROW []\nxref: EC:3.4.23.-\nxref: EC:3.4.23.1\nxref: EC:3.4.23.15\nxref: EC:3.4.23.20\nxref: EC:3.4.23.25\nxref: EC:3.4.23.32\nxref: EC:3.4.23.34\nxref: EC:3.4.23.35\nxref: EC:3.4.23.36\nxref: EC:3.4.23.4\nxref: EC:3.4.23.43\nxref: EC:3.4.23.49\nxref: EC:3.4.23.5\nxref: MetaCyc:3.4.23.1-RXN\nxref: MetaCyc:3.4.23.15-RXN\nxref: MetaCyc:3.4.23.20-RXN\nxref: MetaCyc:3.4.23.25-RXN\nxref: MetaCyc:3.4.23.32-RXN\nxref: MetaCyc:3.4.23.34-RXN\nxref: MetaCyc:3.4.23.35-RXN\nxref: MetaCyc:3.4.23.4-RXN\nxref: MetaCyc:3.4.23.43-RXN\nxref: MetaCyc:3.4.23.5-RXN\nxref: Reactome:R-HSA-157353 \"NEXT1 is cleaved to produce NICD1\"\nxref: Reactome:R-HSA-157640 \"NEXT2 is cleaved to produce NICD2\"\nxref: Reactome:R-HSA-2022403 \"Renin:Prorenin Receptor hydrolyzes Angiotensinogen to AGT(25-34) (Angiotensin-(1-10))\"\nxref: Reactome:R-HSA-2022412 \"Renin hydrolyzes Angiotensinogen to AGT(25-34) (Angiotensin-(1-10))\"\nxref: Reactome:R-HSA-2065357 \"Prorenin:Prorenin Receptor hydrolyzes Angiotensinogen to AGT(25-35) (Angiotensin-(1-10))\"\nxref: Reactome:R-HSA-2220988 \"NEXT1 PEST domain mutants are cleaved to produce NICD1 PEST domain mutants\"\nxref: Reactome:R-HSA-373705 \"Caspase cleavage of DCC\"\nxref: Reactome:R-HSA-9013361 \"NEXT3 is cleaved to produce NICD3\"\nxref: Reactome:R-HSA-9017817 \"Gamma-secretase cleaves YBX1:NOTCH3\"\nxref: Reactome:R-HSA-9604294 \"Gamma-secretase cleaves NOTCH4\"\nis_a: GO:0004175 ! endopeptidase activity\nis_a: GO:0070001 ! aspartic-type peptidase activity\nproperty_value: skos:exactMatch EC:3.4.23.-\nproperty_value: skos:narrowMatch EC:3.4.23.1\nproperty_value: skos:narrowMatch EC:3.4.23.15\nproperty_value: skos:narrowMatch EC:3.4.23.20\nproperty_value: skos:narrowMatch EC:3.4.23.25\nproperty_value: skos:narrowMatch EC:3.4.23.32\nproperty_value: skos:narrowMatch EC:3.4.23.34\nproperty_value: skos:narrowMatch EC:3.4.23.35\nproperty_value: skos:narrowMatch EC:3.4.23.36\nproperty_value: skos:narrowMatch EC:3.4.23.4\nproperty_value: skos:narrowMatch EC:3.4.23.43\nproperty_value: skos:narrowMatch EC:3.4.23.49\nproperty_value: skos:narrowMatch EC:3.4.23.5\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.1-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.15-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.20-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.25-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.32-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.34-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.35-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.4-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.43-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.5-RXN\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004190",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 37379-37447",
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
  "excerpt": "[Term]\nid: GO:0004651\nname: polynucleotide 5'-phosphatase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a 5'-phosphopolynucleotide + H2O = a polynucleotide + phosphate.\" [EC:3.1.3.33]\nsynonym: \"5'-polynucleotidase activity\" RELATED [EC:3.1.3.33]\nsynonym: \"polynucleotide 5'-phosphohydrolase activity\" RELATED [EC:3.1.3.33]\nsynonym: \"polynucleotide 5'-triphosphatase activity\" RELATED [EC:3.1.3.33]\nxref: EC:3.1.3.33\nxref: MetaCyc:RXN-21861\nxref: Reactome:R-HSA-77078 \"Hydrolysis of the 5'-end of the nascent transcript by the capping enzyme\"\nxref: Reactome:R-HSA-9923980 \"NS3 cleaves triphosphate moiety of genomic +ssRNA\"\nxref: RHEA:67772\nxref: RHEA:67776\nis_a: GO:0016791 ! phosphatase activity\nproperty_value: skos:exactMatch EC:3.1.3.33\nproperty_value: skos:narrowMatch RHEA:67772\nproperty_value: skos:narrowMatch RHEA:67776\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004651",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 46274-46292",
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
  "excerpt": "[Term]\nid: GO:0019787\nname: ubiquitin-like protein transferase activity\nnamespace: molecular_function\nalt_id: GO:0008639\nalt_id: GO:0008640\ndef: \"Catalysis of the transfer of a ubiquitin-like from one protein to another via the reaction X-ULP + Y = Y-ULP + X, where both X-ULP and Y-ULP are covalent linkages. ULP represents a ubiquitin-like protein.\" [GOC:mah, GOC:rn, PMID:10806345, PMID:10884686]\nsubset: goslim_drosophila\nsubset: goslim_pir\nsynonym: \"E2\" BROAD []\nsynonym: \"E3\" RELATED [GOC:dph]\nsynonym: \"small conjugating protein ligase activity\" NARROW [GOC:dph]\nsynonym: \"small conjugating protein transferase activity\" EXACT [GOC:dph]\nsynonym: \"small protein conjugating enzyme activity\" NARROW []\nsynonym: \"ubiquitin-like conjugating enzyme activity\" NARROW []\nsynonym: \"ubiquitin-like-protein ligase activity\" NARROW []\nxref: Reactome:R-HSA-5678490 \"ATG16L1 complex transfers LC3 from ATG3 to PE\"\nxref: Reactome:R-HSA-688137 \"RIP2 is K63 polyubiquitinated\"\nis_a: GO:0016755 ! aminoacyltransferase activity\nis_a: GO:0140096 ! catalytic activity, acting on a protein\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019787",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 153098-153118",
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
  "excerpt": "[Term]\nid: GO:0106157\nname: peptidyl-arginine 3-dioxygenase activity\nnamespace: molecular_function\nalt_id: GO:0140554\ndef: \"Catalyzes the reaction: 2-oxoglutarate + [protein]-L-arginine + O2 = [protein]-(3R)-3-hydroxy-L-arginine + CO2 + succinate.\" [PMID:29563586]\nsynonym: \"L-arginine 3-hydroxylase activity\" EXACT []\nxref: EC:1.14.11.73\nxref: Reactome:R-HSA-9629869 \"KDM8:Fe2+ hydroxylates an arginine residue of RPS6\"\nxref: Reactome:R-HSA-9629888 \"KDM8:Fe2+ hydroxylates an arginine residue of RCCD1\"\nxref: RHEA:41556\nxref: RHEA:56744\nxref: RHEA:57160\nxref: RHEA:57164\nis_a: GO:0016706 ! 2-oxoglutarate-dependent dioxygenase activity\nis_a: GO:0140096 ! catalytic activity, acting on a protein\nproperty_value: skos:exactMatch EC:1.14.11.73\nproperty_value: skos:exactMatch RHEA:56744\nproperty_value: skos:narrowMatch RHEA:41556\nproperty_value: skos:narrowMatch RHEA:57160\nproperty_value: skos:narrowMatch RHEA:57164\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0106157",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 428096-428117",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0140818\nname: mRNA 5'-triphosphate monophosphatase activity\nnamespace: molecular_function\ndef: \"A 5'-end triphospho-[mRNA] + H2O = a 5'-end diphospho-[mRNA] + H+ + phosphate.\" [PMID:9473487]\nsynonym: \"mRNA 5'-phosphatase activity\" EXACT []\nxref: EC:3.6.1.74\nxref: MetaCyc:POLYNUCLEOTIDE-5-PHOSPHATASE-RXN\nxref: RHEA:11008\nxref: RHEA:60828\nxref: RHEA:60832\nxref: RHEA:67004\nis_a: GO:0004651 ! polynucleotide 5'-phosphatase activity\nis_a: GO:0016462 ! pyrophosphatase activity\nis_a: GO:0140098 ! catalytic activity, acting on RNA\nproperty_value: skos:exactMatch EC:3.6.1.74\nproperty_value: skos:exactMatch RHEA:67004\nproperty_value: skos:narrowMatch RHEA:11008\nproperty_value: skos:narrowMatch RHEA:60828\nproperty_value: skos:narrowMatch RHEA:60832\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140818",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 443789-443809",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
