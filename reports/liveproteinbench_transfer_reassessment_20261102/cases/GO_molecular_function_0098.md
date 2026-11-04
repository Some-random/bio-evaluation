# GO_molecular_function_0098

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0098.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — peptidyl-tRNA hydrolase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAIKLIVGLANPGAEYAATRHNAGAWYVDLLAERLRAPLREEPKFFGYTSRITLEGEDVRLLVPTTFMNLSGKAVGAMASFYRIQPDEILVAHDELDLPPGVAKFKLGGGHGGHNGLKDIISKLGNNPNFHRLRVGIGHPGDKNKVVGFVLGKPPVSEQKLIDEAIDEAARCTELWFKEGLAKATSRLHTFKAQ

[Multiple Choices]
A. peptidyl-tRNA hydrolase activity
B. transcription coactivator activity
C. polyubiquitin modification-dependent protein binding
D. alpha-1,6-mannosyltransferase activity
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

> The supplied sequence matches the reviewed bacterial peptidyl-tRNA hydrolase record. That record assigns peptidyl-tRNA hydrolase activity by a HAMAP rule and describes the corresponding hydrolysis reaction; it also cites experimental work on tRNA deacetylation. The annotations combine computational inference and literature evidence, rather than constituting only a direct experimental assignment of the GO term.

Citations as saved: [H4](#evidence-h4), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [C7](#evidence-c7), [C9](#evidence-c9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 194-residue sequence is consistent with the compact bacterial Pth1 peptidyl-tRNA hydrolase family, including its conserved catalytic-region sequence pattern. Family knowledge links this type of protein to hydrolysis of peptidyl-tRNA, distinguishing A from the offered alternatives: B and C describe regulatory or modification-dependent binding functions, while D is a glycosyltransferase function generally associated with a different protein context. This is a credible family-level inference, not proof of the exact protein's annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable knowledge of bacterial Pth-family proteins provide a meaningful basis for selecting A without recalling this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, peptidyl-tRNA hydrolase activity is clearly the best-supported family-level match.


### Important caveats

- The database functional assignment is partly computational (HAMAP); the cited experimental evidence concerns specific tRNA-related activity and should not be mistaken for comprehensive validation of every annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 194-residue sequence is consistent with the compact bacterial Pth1 peptidyl-tRNA hydrolase family, including its conserved catalytic-region sequence pattern. Family knowledge links this type of protein to hydrolysis of peptidyl-tRNA, distinguishing A from the offered alternatives: B and C describe regulatory or modification-dependent binding functions, while D is a glycosyltransferase function generally associated with a different protein context. This is a credible family-level inference, not proof of the exact protein's annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of bacterial Pth-family proteins provide a meaningful basis for selecting A without recalling this exact protein's database record."
  },
  "case_id": "GO_molecular_function_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H7",
      "H8",
      "H9",
      "C7",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed bacterial peptidyl-tRNA hydrolase record. That record assigns peptidyl-tRNA hydrolase activity by a HAMAP rule and describes the corresponding hydrolysis reaction; it also cites experimental work on tRNA deacetylation. The annotations combine computational inference and literature evidence, rather than constituting only a direct experimental assignment of the GO term."
  },
  "important_caveats": [
    "The database functional assignment is partly computational (HAMAP); the cited experimental evidence concerns specific tRNA-related activity and should not be mistaken for comprehensive validation of every annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, peptidyl-tRNA hydrolase activity is clearly the best-supported family-level match."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed bacterial peptidyl-tRNA hydrolase record. That record assigns peptidyl-tRNA hydrolase activity by a HAMAP rule and describes the corresponding hydrolysis reaction; it also cites experimental work on tRNA deacetylation. The annotations combine computational inference and literature evidence, rather than constituting only a direct experimental assignment of the GO term.",
    "evidence_ids": ["H4", "H7", "H8", "H9", "C7", "C9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 194-residue sequence is consistent with the compact bacterial Pth1 peptidyl-tRNA hydrolase family, including its conserved catalytic-region sequence pattern. Family knowledge links this type of protein to hydrolysis of peptidyl-tRNA, distinguishing A from the offered alternatives: B and C describe regulatory or modification-dependent binding functions, while D is a glycosyltransferase function generally associated with a different protein context. This is a credible family-level inference, not proof of the exact protein's annotation.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of bacterial Pth-family proteins provide a meaningful basis for selecting A without recalling this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, peptidyl-tRNA hydrolase activity is clearly the best-supported family-level match."
  },
  "important_caveats": [
    "The database functional assignment is partly computational (HAMAP); the cited experimental evidence concerns specific tRNA-related activity and should not be mistaken for comprehensive validation of every annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0F6B281 (sequence matched exactly, 194 aa) annotates this protein as Peptidyl-tRNA hydrolase (EC 3.1.1.29, GO:0004045) via HAMAP-Rule MF_00083, with additional experimental support from PubMed 27264868 and 29777131 confirming catalytic activity on peptidyl-tRNAs. The GO term GO:0004045 'peptidyl-tRNA hydrolase activity' matches option A exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [C10](#evidence-c10), [H1](#evidence-h1), [H4](#evidence-h4), [H7](#evidence-h7), [H9](#evidence-h9), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable biological arguments distinguish option A from the alternatives. First, the 194-residue sequence has no signal peptide, no transmembrane segments, and a compact all-α/β architecture typical of small bacterial cytoplasmic enzymes. Options B (transcription coactivator activity, GO:0003713) and C (polyubiquitin modification-dependent protein binding, GO:0031593) describe activities intrinsically tied to eukaryotic machinery: GO:0003713 explicitly references Mediator complex, histone modification, and RNA Pol II, while ubiquitin is a eukaryotic-specific modification absent from bacteria. A small bacterial protein is essentially incompatible with these two choices. Option D (alpha-1,6-mannosyltransferase activity, GO:0000009) is primarily associated with eukaryotic N-glycan biosynthesis (ALG2); bacterial glycosyltransferases have different specificities and folds (GT-A/GT-B with ~250-400 aa). This leaves A. Furthermore, the sequence contains hallmark motifs of the highly conserved, essential bacterial Pth family (~194-200 aa): the 'GGGHGG' region and 'GHPGDKNK' segment correspond to conserved catalytic-site residues found across bacterial Pth orthologs (E. coli Pth, B. subtilis Pth, etc.), and the overall fold and size match the canonical Pth architecture. Recognizing a well-known, essential bacterial enzyme family by its conserved motifs and size is legitimate family-level transfer, not lookup of this specific entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of (1) eliminating eukaryotic-specific GO terms B and C from the clearly bacterial context, (2) eliminating D because alpha-1,6-mannosyltransferase is a eukaryotic glycosylation activity with incompatible size/fold expectations, and (3) recognizing conserved Pth-family motifs (GGGHGG, GHPGDKNK) and the canonical ~194-aa size provides a concrete, credible inference from the sequence and general protein-family knowledge that meaningfully distinguishes option A from the other three offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are eukaryotic-specific activities incompatible with a small bacterial protein. Option D describes a eukaryotic glycosyltransferase activity inconsistent with the sequence's size, composition, and lack of glycosyltransferase motifs. Only option A is consistent with a small bacterial hydrolase bearing Pth-family conserved motifs.


### Important caveats

- The primary annotation evidence is HAMAP-Rule MF_00083 (computational rule-based), supplemented by two experimental PubMed references (27264868, 29777131) providing direct biochemical validation.
- The reviewer identified the UniProt accession from dataset image-path metadata; this accession was not available to the evaluated model. The reasoning above relies solely on the raw sequence and general biological knowledge.
- The GO annotation evidence code is IEA:UniProtKB-UniRule (inferred from electronic annotation), though the underlying HAMAP rule is well-curated and experimentally corroborated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable biological arguments distinguish option A from the alternatives. First, the 194-residue sequence has no signal peptide, no transmembrane segments, and a compact all-α/β architecture typical of small bacterial cytoplasmic enzymes. Options B (transcription coactivator activity, GO:0003713) and C (polyubiquitin modification-dependent protein binding, GO:0031593) describe activities intrinsically tied to eukaryotic machinery: GO:0003713 explicitly references Mediator complex, histone modification, and RNA Pol II, while ubiquitin is a eukaryotic-specific modification absent from bacteria. A small bacterial protein is essentially incompatible with these two choices. Option D (alpha-1,6-mannosyltransferase activity, GO:0000009) is primarily associated with eukaryotic N-glycan biosynthesis (ALG2); bacterial glycosyltransferases have different specificities and folds (GT-A/GT-B with ~250-400 aa). This leaves A. Furthermore, the sequence contains hallmark motifs of the highly conserved, essential bacterial Pth family (~194-200 aa): the 'GGGHGG' region and 'GHPGDKNK' segment correspond to conserved catalytic-site residues found across bacterial Pth orthologs (E. coli Pth, B. subtilis Pth, etc.), and the overall fold and size match the canonical Pth architecture. Recognizing a well-known, essential bacterial enzyme family by its conserved motifs and size is legitimate family-level transfer, not lookup of this specific entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of (1) eliminating eukaryotic-specific GO terms B and C from the clearly bacterial context, (2) eliminating D because alpha-1,6-mannosyltransferase is a eukaryotic glycosylation activity with incompatible size/fold expectations, and (3) recognizing conserved Pth-family motifs (GGGHGG, GHPGDKNK) and the canonical ~194-aa size provides a concrete, credible inference from the sequence and general protein-family knowledge that meaningfully distinguishes option A from the other three offered choices."
  },
  "case_id": "GO_molecular_function_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "C10",
      "H1",
      "H4",
      "H7",
      "H9",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F6B281 (sequence matched exactly, 194 aa) annotates this protein as Peptidyl-tRNA hydrolase (EC 3.1.1.29, GO:0004045) via HAMAP-Rule MF_00083, with additional experimental support from PubMed 27264868 and 29777131 confirming catalytic activity on peptidyl-tRNAs. The GO term GO:0004045 'peptidyl-tRNA hydrolase activity' matches option A exactly."
  },
  "important_caveats": [
    "The primary annotation evidence is HAMAP-Rule MF_00083 (computational rule-based), supplemented by two experimental PubMed references (27264868, 29777131) providing direct biochemical validation.",
    "The reviewer identified the UniProt accession from dataset image-path metadata; this accession was not available to the evaluated model. The reasoning above relies solely on the raw sequence and general biological knowledge.",
    "The GO annotation evidence code is IEA:UniProtKB-UniRule (inferred from electronic annotation), though the underlying HAMAP rule is well-curated and experimentally corroborated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are eukaryotic-specific activities incompatible with a small bacterial protein. Option D describes a eukaryotic glycosyltransferase activity inconsistent with the sequence's size, composition, and lack of glycosyltransferase motifs. Only option A is consistent with a small bacterial hydrolase bearing Pth-family conserved motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F6B281 (sequence matched exactly, 194 aa) annotates this protein as Peptidyl-tRNA hydrolase (EC 3.1.1.29, GO:0004045) via HAMAP-Rule MF_00083, with additional experimental support from PubMed 27264868 and 29777131 confirming catalytic activity on peptidyl-tRNAs. The GO term GO:0004045 'peptidyl-tRNA hydrolase activity' matches option A exactly.",
    "evidence_ids": ["C4", "C5", "C8", "C10", "H1", "H4", "H7", "H9", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable biological arguments distinguish option A from the alternatives. First, the 194-residue sequence has no signal peptide, no transmembrane segments, and a compact all-α/β architecture typical of small bacterial cytoplasmic enzymes. Options B (transcription coactivator activity, GO:0003713) and C (polyubiquitin modification-dependent protein binding, GO:0031593) describe activities intrinsically tied to eukaryotic machinery: GO:0003713 explicitly references Mediator complex, histone modification, and RNA Pol II, while ubiquitin is a eukaryotic-specific modification absent from bacteria. A small bacterial protein is essentially incompatible with these two choices. Option D (alpha-1,6-mannosyltransferase activity, GO:0000009) is primarily associated with eukaryotic N-glycan biosynthesis (ALG2); bacterial glycosyltransferases have different specificities and folds (GT-A/GT-B with ~250-400 aa). This leaves A. Furthermore, the sequence contains hallmark motifs of the highly conserved, essential bacterial Pth family (~194-200 aa): the 'GGGHGG' region and 'GHPGDKNK' segment correspond to conserved catalytic-site residues found across bacterial Pth orthologs (E. coli Pth, B. subtilis Pth, etc.), and the overall fold and size match the canonical Pth architecture. Recognizing a well-known, essential bacterial enzyme family by its conserved motifs and size is legitimate family-level transfer, not lookup of this specific entry.",
    "missing_item_specific_fact": "",
    "reason": "The combination of (1) eliminating eukaryotic-specific GO terms B and C from the clearly bacterial context, (2) eliminating D because alpha-1,6-mannosyltransferase is a eukaryotic glycosylation activity with incompatible size/fold expectations, and (3) recognizing conserved Pth-family motifs (GGGHGG, GHPGDKNK) and the canonical ~194-aa size provides a concrete, credible inference from the sequence and general protein-family knowledge that meaningfully distinguishes option A from the other three offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are eukaryotic-specific activities incompatible with a small bacterial protein. Option D describes a eukaryotic glycosyltransferase activity inconsistent with the sequence's size, composition, and lack of glycosyltransferase motifs. Only option A is consistent with a small bacterial hydrolase bearing Pth-family conserved motifs."
  },
  "important_caveats": [
    "The primary annotation evidence is HAMAP-Rule MF_00083 (computational rule-based), supplemented by two experimental PubMed references (27264868, 29777131) providing direct biochemical validation.",
    "The reviewer identified the UniProt accession from dataset image-path metadata; this accession was not available to the evaluated model. The reasoning above relies solely on the raw sequence and general biological knowledge.",
    "The GO annotation evidence code is IEA:UniProtKB-UniRule (inferred from electronic annotation), though the underlying HAMAP rule is well-curated and experimentally corroborated."
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
  "benchmark_sequence_length": 194,
  "benchmark_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "current_entry_audit": {
    "entryVersion": 43,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2015-06-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 194,
  "current_source_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 42,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0F6B281",
  "selected_historical_entry_version": 42,
  "selected_historical_record_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "selected_historical_source_sequence_length": 194,
  "selected_historical_source_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "selected_historical_version": {
    "accession": "A0A0F6B281",
    "database": "Swiss-Prot",
    "entryVersion": 42,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PTH_SALT1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0F6B281\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":43,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2015-06-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Salmonella\"],\"scientificName\":\"Salmonella typhimurium (strain 14028s / SGSC 2262)\",\"taxonId\":588858}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"3.1.1.29\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Peptidyl-tRNA hydrolase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Pth\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Hydrolyzes ribosome-free peptidyl-tRNAs (with 1 or more amino acids incorporated), which drop off the ribosome during protein synthesis, or as a result of ribosome stalling\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Catalyzes the release of premature peptidyl moieties from peptidyl-tRNA molecules trapped in stalled 50S ribosomal subunits, and thus maintains levels of free tRNAs and 50S ribosomes\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27264868\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29777131\",\"source\":\"PubMed\"}],\"value\":\"Expression in lag phase counteracts expression of tRNA-acetylating toxin TacT, deacetylates bulk tRNA modified by TacT in vitro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.1.1.29\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"name\":\"an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:54448\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10123\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:13883\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59874\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:78442\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138191\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"27264868\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"29777131\",\"source\":\"PubMed\"}],\"name\":\"N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81979\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9664\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19766\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61887\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:78442\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232036\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004045\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:peptidyl-tRNA hydrolase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniRule\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0000049\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:tRNA binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniRule\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Cheverton A.M.\",\"Gollan B.\",\"Przydacz M.\",\"Wong C.T.\",\"Mylona A.\",\"Hare S.A.\",\"Helaine S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27264868\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molcel.2016.05.002\"}],\"citationType\":\"journal article\",\"firstPage\":\"86\",\"id\":\"27264868\",\"journal\":\"Mol. Cell\",\"lastPage\":\"96\",\"publicationDate\":\"2016\",\"title\":\"A Salmonella Toxin Promotes Persister Formation through Acetylation of tRNA.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Rycroft J.A.\",\"Gollan B.\",\"Grabe G.J.\",\"Hall A.\",\"Cheverton A.M.\",\"Larrouy-Maumus G.\",\"Hare S.A.\",\"Helaine S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29777131\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-018-04472-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"1993\",\"id\":\"29777131\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"1993\",\"publicationDate\":\"2018\",\"title\":\"Activity of acetyltransferase toxins involved in Salmonella persister formation during macrophage infection.\",\"volume\":\"9\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H1",
  "excerpt": "ID   PTH_SALT1               Reviewed;         194 AA.\nAC   A0A0F6B281;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JUN-2015, sequence version 1.\nDT   28-JAN-2026, entry version 42.\nDE   RecName: Full=Peptidyl-tRNA hydrolase {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            Short=Pth {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            EC=3.1.1.29 {ECO:0000255|HAMAP-Rule:MF_00083};\nGN   Name=pth {ECO:0000255|HAMAP-Rule:MF_00083, ECO:0000312|EMBL:ACY88619.1};\nGN   OrderedLocusNames=STM14_2156 {ECO:0000312|EMBL:ACY88619.1};\nOS   Salmonella typhimurium (strain 14028s / SGSC 2262).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Salmonella.\nOX   NCBI_TaxID=588858;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023;\nRX   PubMed=27264868; DOI=10.1016/j.molcel.2016.05.002;\nRA   Cheverton A.M., Gollan B., Przydacz M., Wong C.T., Mylona A., Hare S.A.,\nRA   Helaine S.;\nRT   \"A Salmonella Toxin Promotes Persister Formation through Acetylation of\nRT   tRNA.\";\nRL   Mol. Cell 63:86-96(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023;\nRX   PubMed=29777131; DOI=10.1038/s41467-018-04472-6;\nRA   Rycroft J.A., Gollan B., Grabe G.J., Hall A., Cheverton A.M.,\nRA   Larrouy-Maumus G., Hare S.A., Helaine S.;\nRT   \"Activity of acetyltransferase toxins involved in Salmonella persister\nRT   formation during macrophage infection.\";\nRL   Nat. Commun. 9:1993-1993(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Hydrolyzes ribosome-free peptidyl-tRNAs (with 1 or more amino\nCC       acids incorporated), which drop off the ribosome during protein\nCC       synthesis, or as a result of ribosome stalling. {ECO:0000255|HAMAP-\nCC       Rule:MF_00083}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H5",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the release of premature peptidyl moieties from\nCC       peptidyl-tRNA molecules trapped in stalled 50S ribosomal subunits, and\nCC       thus maintains levels of free tRNAs and 50S ribosomes.\nCC       {ECO:0000255|HAMAP-Rule:MF_00083}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H6",
  "excerpt": "CC   -!- FUNCTION: Expression in lag phase counteracts expression of tRNA-\nCC       acetylating toxin TacT, deacetylates bulk tRNA modified by TacT in\nCC       vitro. {ECO:0000269|PubMed:27264868, ECO:0000269|PubMed:29777131}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino\nCC         acid + a tRNA + H(+); Xref=Rhea:RHEA:54448, Rhea:RHEA-COMP:10123,\nCC         Rhea:RHEA-COMP:13883, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:59874, ChEBI:CHEBI:78442, ChEBI:CHEBI:138191;\nCC         EC=3.1.1.29; Evidence={ECO:0000255|HAMAP-Rule:MF_00083};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) +\nCC         H(+); Xref=Rhea:RHEA:81979, Rhea:RHEA-COMP:9664, Rhea:RHEA-\nCC         COMP:19766, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:61887,\nCC         ChEBI:CHEBI:78442, ChEBI:CHEBI:232036;\nCC         Evidence={ECO:0000305|PubMed:27264868, ECO:0000305|PubMed:29777131};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0004045; F:peptidyl-tRNA hydrolase activity; IEA:UniProtKB-UniRule.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0000049; F:tRNA binding; IEA:UniProtKB-UniRule.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000009\nname: alpha-1,6-mannosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a mannose residue to an oligosaccharide, forming an alpha-(1->6) linkage.\" [GOC:mcc, PMID:2644248]\nsynonym: \"1,6-alpha-mannosyltransferase activity\" EXACT []\nxref: Reactome:R-HSA-449718 \"Addition of a third mannose to the N-glycan precursor by ALG2\"\nis_a: GO:0000030 ! mannosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000009",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 117-125",
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
  "excerpt": "[Term]\nid: GO:0003713\nname: transcription coactivator activity\nnamespace: molecular_function\nalt_id: GO:0001105\ndef: \"A transcription coregulator activity that activates or increases the transcription of specific gene sets via binding to a DNA-binding transcription factor at a specific genomic locus, either on its own or as part of a complex. Coactivators often act by altering chromatin structure and modifications. For example, one class of transcription coactivators modifies chromatin structure through covalent modification of histones. A second class remodels the conformation of chromatin in an ATP-dependent fashion. A third class modulates interactions of DNA-bound DNA-binding transcription factors with other transcription coregulators. A fourth class of coactivator activity is the bridging of a DNA-binding transcription factor to the general (basal) transcription machinery. The Mediator complex, which bridges sequence-specific DNA binding transcription factors and RNA polymerase, is also a transcription coactivator.\" [GOC:txnOH-2018, PMID:10213677, PMID:16858867]\ncomment: For usage guidance, see comment in GO:0003712 ; transcription coregulator activity.\nsynonym: \"RNA polymerase II transcription co-activator activity\" RELATED []\nsynonym: \"RNA polymerase II transcription coactivator activity\" RELATED []\nsynonym: \"RNA polymerase II transcription mediator activity\" RELATED []\nsynonym: \"transcription co-activator activity\" EXACT []\nis_a: GO:0003712 ! transcription coregulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003713",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 28141-28153",
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

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0031593\nname: polyubiquitin modification-dependent protein binding\nnamespace: molecular_function\ndef: \"Binding to a protein upon poly-ubiquitination of the target protein.\" [GOC:pg]\nis_a: GO:0140030 ! modification-dependent protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031593",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 178132-178138",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 98. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
