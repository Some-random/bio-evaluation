# catalytic_activity_0001

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0001.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)

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
A. (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O
B. 4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O
C. an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)
D. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as peptidyl-tRNA hydrolase, and its recorded catalytic reaction is the hydrolysis stated in choice C. The generic reaction annotation is attributed to a HAMAP rule (computational evidence); a separate annotation cites literature for hydrolysis of N-acetylglycyl-tRNA. This supports the key, while distinguishing annotation from direct experimental evidence in the excerpt.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 194-residue sequence has a compact bacterial-enzyme profile and a glycine/histidine-rich segment consistent with the peptidyl-tRNA hydrolase family. Transferable family knowledge links these enzymes to cleavage of the ester bond joining an aminoacyl/peptidyl group to tRNA, matching choice C. The other options describe unrelated transformations: lipid hydroperoxide dehydration, nitro-group reduction, and a branched-chain hydroxy-acid dehydration.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and the known substrate chemistry provide a meaningful basis to distinguish C from the offered alternatives without knowing this exact protein's database record. The inference is probabilistic, not a substitute for experimental characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed transformations, only C describes peptidyl-tRNA hydrolysis.


### Important caveats

- The generic reaction annotation is computationally assigned by a HAMAP rule; the cited literature annotation concerns a specific N-acetylglycyl-tRNA substrate.
- The sequence itself supplies no organism label or direct assay result.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 194-residue sequence has a compact bacterial-enzyme profile and a glycine/histidine-rich segment consistent with the peptidyl-tRNA hydrolase family. Transferable family knowledge links these enzymes to cleavage of the ester bond joining an aminoacyl/peptidyl group to tRNA, matching choice C. The other options describe unrelated transformations: lipid hydroperoxide dehydration, nitro-group reduction, and a branched-chain hydroxy-acid dehydration.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the known substrate chemistry provide a meaningful basis to distinguish C from the offered alternatives without knowing this exact protein's database record. The inference is probabilistic, not a substitute for experimental characterization."
  },
  "case_id": "catalytic_activity_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as peptidyl-tRNA hydrolase, and its recorded catalytic reaction is the hydrolysis stated in choice C. The generic reaction annotation is attributed to a HAMAP rule (computational evidence); a separate annotation cites literature for hydrolysis of N-acetylglycyl-tRNA. This supports the key, while distinguishing annotation from direct experimental evidence in the excerpt."
  },
  "important_caveats": [
    "The generic reaction annotation is computationally assigned by a HAMAP rule; the cited literature annotation concerns a specific N-acetylglycyl-tRNA substrate.",
    "The sequence itself supplies no organism label or direct assay result."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed transformations, only C describes peptidyl-tRNA hydrolysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as peptidyl-tRNA hydrolase, and its recorded catalytic reaction is the hydrolysis stated in choice C. The generic reaction annotation is attributed to a HAMAP rule (computational evidence); a separate annotation cites literature for hydrolysis of N-acetylglycyl-tRNA. This supports the key, while distinguishing annotation from direct experimental evidence in the excerpt.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 194-residue sequence has a compact bacterial-enzyme profile and a glycine/histidine-rich segment consistent with the peptidyl-tRNA hydrolase family. Transferable family knowledge links these enzymes to cleavage of the ester bond joining an aminoacyl/peptidyl group to tRNA, matching choice C. The other options describe unrelated transformations: lipid hydroperoxide dehydration, nitro-group reduction, and a branched-chain hydroxy-acid dehydration.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the known substrate chemistry provide a meaningful basis to distinguish C from the offered alternatives without knowing this exact protein's database record. The inference is probabilistic, not a substitute for experimental characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed transformations, only C describes peptidyl-tRNA hydrolysis."
  },
  "important_caveats": [
    "The generic reaction annotation is computationally assigned by a HAMAP rule; the cited literature annotation concerns a specific N-acetylglycyl-tRNA substrate.",
    "The sequence itself supplies no organism label or direct assay result."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0F6B281 (PTH_SALT1, sequence matched) annotates this protein as Peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29) with the exact catalytic reaction 'an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)' (Rhea:RHEA:54448), matching option C verbatim. The annotation is supported by HAMAP-Rule MF_00083 (family-level computational inference) and corroborated by experimental studies (PubMed 27264868, 29777131) demonstrating activity on N-acetylglycyl-tRNA.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 194-aa protein contains the distinctive 'GGGHGGHNG' motif with catalytic histidines characteristic of the Peptidyl-tRNA hydrolase (Pth) family (Pfam PF01325). Pth is a well-known small (~180-200 aa) bacterial enzyme that rescues ribosomes by hydrolyzing peptidyl-tRNA. The small size immediately eliminates lipoxygenase (option A, typically >700 aa) and dihydroxy-acid dehydratase (option D, typically >400 aa). Nitroreductases (option B) are ~220-250 aa FMN-dependent enzymes lacking the conserved His-rich catalytic motif seen here. The overall sequence architecture (small α/β fold, conserved catalytic His in the GGGHGGHNG loop, nucleotide-binding-like C-terminal region) matches the Pth family known from E. coli and other bacteria, making the peptidyl-tRNA hydrolysis reaction (option C) the most consistent choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the Pth family is based on transferable knowledge: the small protein size, the conserved catalytic His motif (GGGHGGHNG), and the overall fold architecture shared across bacterial Pth homologs. These family-level features meaningfully distinguish option C from the other three choices without requiring the specific Salmonella strain annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent very different enzyme classes with distinct size ranges, cofactor requirements, and sequence signatures. The Pth family features in the sequence clearly point to option C, while A (lipoxygenase), B (nitroreductase), and D (DHAD) are inconsistent with the protein's size and sequence motifs.


### Important caveats

- The UniProt annotation for the general Pth reaction (EC 3.1.1.29) is based on HAMAP-Rule MF_00083 (computational family inference, ECO:0000255), while the specific N-acetylglycyl-tRNA activity is experimentally supported (ECO:0000305).
- The benchmark sequence is nearly identical to E. coli Pth (P0A6Y9); recognition may partly rely on familiarity with the canonical E. coli Pth sequence rather than purely de novo family inference, though the family-level features (size, His motif, architecture) remain transferable.
- Reviewer-only evidence confirms the sequence matches A0A0F6B281 exactly (SHA-256 match), but this accession was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 194-aa protein contains the distinctive 'GGGHGGHNG' motif with catalytic histidines characteristic of the Peptidyl-tRNA hydrolase (Pth) family (Pfam PF01325). Pth is a well-known small (~180-200 aa) bacterial enzyme that rescues ribosomes by hydrolyzing peptidyl-tRNA. The small size immediately eliminates lipoxygenase (option A, typically >700 aa) and dihydroxy-acid dehydratase (option D, typically >400 aa). Nitroreductases (option B) are ~220-250 aa FMN-dependent enzymes lacking the conserved His-rich catalytic motif seen here. The overall sequence architecture (small α/β fold, conserved catalytic His in the GGGHGGHNG loop, nucleotide-binding-like C-terminal region) matches the Pth family known from E. coli and other bacteria, making the peptidyl-tRNA hydrolysis reaction (option C) the most consistent choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the Pth family is based on transferable knowledge: the small protein size, the conserved catalytic His motif (GGGHGGHNG), and the overall fold architecture shared across bacterial Pth homologs. These family-level features meaningfully distinguish option C from the other three choices without requiring the specific Salmonella strain annotation."
  },
  "case_id": "catalytic_activity_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F6B281 (PTH_SALT1, sequence matched) annotates this protein as Peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29) with the exact catalytic reaction 'an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)' (Rhea:RHEA:54448), matching option C verbatim. The annotation is supported by HAMAP-Rule MF_00083 (family-level computational inference) and corroborated by experimental studies (PubMed 27264868, 29777131) demonstrating activity on N-acetylglycyl-tRNA."
  },
  "important_caveats": [
    "The UniProt annotation for the general Pth reaction (EC 3.1.1.29) is based on HAMAP-Rule MF_00083 (computational family inference, ECO:0000255), while the specific N-acetylglycyl-tRNA activity is experimentally supported (ECO:0000305).",
    "The benchmark sequence is nearly identical to E. coli Pth (P0A6Y9); recognition may partly rely on familiarity with the canonical E. coli Pth sequence rather than purely de novo family inference, though the family-level features (size, His motif, architecture) remain transferable.",
    "Reviewer-only evidence confirms the sequence matches A0A0F6B281 exactly (SHA-256 match), but this accession was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes with distinct size ranges, cofactor requirements, and sequence signatures. The Pth family features in the sequence clearly point to option C, while A (lipoxygenase), B (nitroreductase), and D (DHAD) are inconsistent with the protein's size and sequence motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F6B281 (PTH_SALT1, sequence matched) annotates this protein as Peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29) with the exact catalytic reaction 'an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)' (Rhea:RHEA:54448), matching option C verbatim. The annotation is supported by HAMAP-Rule MF_00083 (family-level computational inference) and corroborated by experimental studies (PubMed 27264868, 29777131) demonstrating activity on N-acetylglycyl-tRNA.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 194-aa protein contains the distinctive 'GGGHGGHNG' motif with catalytic histidines characteristic of the Peptidyl-tRNA hydrolase (Pth) family (Pfam PF01325). Pth is a well-known small (~180-200 aa) bacterial enzyme that rescues ribosomes by hydrolyzing peptidyl-tRNA. The small size immediately eliminates lipoxygenase (option A, typically >700 aa) and dihydroxy-acid dehydratase (option D, typically >400 aa). Nitroreductases (option B) are ~220-250 aa FMN-dependent enzymes lacking the conserved His-rich catalytic motif seen here. The overall sequence architecture (small α/β fold, conserved catalytic His in the GGGHGGHNG loop, nucleotide-binding-like C-terminal region) matches the Pth family known from E. coli and other bacteria, making the peptidyl-tRNA hydrolysis reaction (option C) the most consistent choice.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the Pth family is based on transferable knowledge: the small protein size, the conserved catalytic His motif (GGGHGGHNG), and the overall fold architecture shared across bacterial Pth homologs. These family-level features meaningfully distinguish option C from the other three choices without requiring the specific Salmonella strain annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes with distinct size ranges, cofactor requirements, and sequence signatures. The Pth family features in the sequence clearly point to option C, while A (lipoxygenase), B (nitroreductase), and D (DHAD) are inconsistent with the protein's size and sequence motifs."
  },
  "important_caveats": [
    "The UniProt annotation for the general Pth reaction (EC 3.1.1.29) is based on HAMAP-Rule MF_00083 (computational family inference, ECO:0000255), while the specific N-acetylglycyl-tRNA activity is experimentally supported (ECO:0000305).",
    "The benchmark sequence is nearly identical to E. coli Pth (P0A6Y9); recognition may partly rely on familiarity with the canonical E. coli Pth sequence rather than purely de novo family inference, though the family-level features (size, His motif, architecture) remain transferable.",
    "Reviewer-only evidence confirms the sequence matches A0A0F6B281 exactly (SHA-256 match), but this accession was not provided to the evaluated model."
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

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C6",
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

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C7",
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

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C8",
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
  "excerpt": "DE   RecName: Full=Peptidyl-tRNA hydrolase {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            Short=Pth {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            EC=3.1.1.29 {ECO:0000255|HAMAP-Rule:MF_00083};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H4",
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

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H5",
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

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H6",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
