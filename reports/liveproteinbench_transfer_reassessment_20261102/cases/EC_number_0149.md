# EC_number_0149

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0149.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 2.3.1.312

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIETPYLLFLGDAPDMLAAKVAIGIRDWRPDHAVGQISLPGCGANLGLTEMTLEEAKAAGAKTLVIGVANRGGKISQEWKKVLVQALEEGFDLASGLHNLLRDEPDLAAVAEATGRTLHDVRVPSVQYPIADGVKRRGKRCLAVGTDCSVGKMYTALAMDAEMQARGIKSTFRATGQTGILITGDGVPLDAVIADFMAGSIEYLTPDNDDDHWDLIEGQGSLFHVSYSGVTMALVHGGQPDALILCHEPTRTHMRGLPDYDVPSLEELRDVALPLAQRANKDCKIVGISVNTQHLGEEEAVAYLKEVEGRMGLPAVDPYRHGAGRLVDALAAV

[Multiple Choices]
A. 2.3.1.322
B. 2.7.7.43
C. 2.3.1.312
D. 5.4.99.14
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

> The sequence-matched UniProt record assigns EC 2.3.1.312 and reports the specific reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA, with experimental evidence (ECO:0000269). This supports choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad enzyme-class inference, but choices A and C are both EC 2.3.1 acyltransferases. The provided sequence has no evident feature that meaningfully distinguishes their substrate-specific reactions.


**Missing item-specific fact**

> Which substrate-specific reaction this protein catalyzes, or a functionally characterized close homolog that establishes that reaction.


**Reason**

> General transferase or cofactor-binding knowledge could help distinguish some alternatives, but it does not meaningfully resolve the key distinction between A and C. Choosing C requires protein-specific functional information or a sufficiently close, characterized homolog.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports C, and no evidence establishes another offered EC number as a valid annotation for this protein. The sequence-based distinction is underdetermined, but that alone does not show that multiple options are biochemically correct.


### Important caveats

- The reviewer-only source reports an experimentally supported reaction for a sequence-matched entry; the primary paper was not independently reviewed here.
- The source identity and annotation were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad enzyme-class inference, but choices A and C are both EC 2.3.1 acyltransferases. The provided sequence has no evident feature that meaningfully distinguishes their substrate-specific reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Which substrate-specific reaction this protein catalyzes, or a functionally characterized close homolog that establishes that reaction.",
    "reason": "General transferase or cofactor-binding knowledge could help distinguish some alternatives, but it does not meaningfully resolve the key distinction between A and C. Choosing C requires protein-specific functional information or a sufficiently close, characterized homolog."
  },
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.3.1.312 and reports the specific reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA, with experimental evidence (ECO:0000269). This supports choice C."
  },
  "important_caveats": [
    "The reviewer-only source reports an experimentally supported reaction for a sequence-matched entry; the primary paper was not independently reviewed here.",
    "The source identity and annotation were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C, and no evidence establishes another offered EC number as a valid annotation for this protein. The sequence-based distinction is underdetermined, but that alone does not show that multiple options are biochemically correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.3.1.312 and reports the specific reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA, with experimental evidence (ECO:0000269). This supports choice C.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad enzyme-class inference, but choices A and C are both EC 2.3.1 acyltransferases. The provided sequence has no evident feature that meaningfully distinguishes their substrate-specific reactions.",
    "missing_item_specific_fact": "Which substrate-specific reaction this protein catalyzes, or a functionally characterized close homolog that establishes that reaction.",
    "reason": "General transferase or cofactor-binding knowledge could help distinguish some alternatives, but it does not meaningfully resolve the key distinction between A and C. Choosing C requires protein-specific functional information or a sufficiently close, characterized homolog."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C, and no evidence establishes another offered EC number as a valid annotation for this protein. The sequence-based distinction is underdetermined, but that alone does not show that multiple options are biochemically correct."
  },
  "important_caveats": [
    "The reviewer-only source reports an experimentally supported reaction for a sequence-matched entry; the primary paper was not independently reviewed here.",
    "The source identity and annotation were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A2T1AE85 (Swiss-Prot, reviewed) annotates this 333-aa protein as D-glutamate N-acetyltransferase with EC 2.3.1.312, supported by experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023) and X-ray crystallography (PDB:7XRJ, 2.20 Å). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H⁺ is confirmed by Rhea (RHEA:76495). The benchmark sequence SHA256 matches the source sequence exactly. The EC number assignment is experimentally validated, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable GNAT (GCN5-related N-acetyltransferase) fold signature, notably the 'VANRGGKISQ' motif (RGG pattern characteristic of the CoA-binding loop in GNAT enzymes) and the overall ~333-aa architecture with a central β-sheet core flanked by α-helices. This family-level recognition legitimately eliminates option B (EC 2.7.7.43, a nucleotidyltransferase with an entirely different fold and catalytic mechanism involving a nucleotidyl group transfer) and option D (EC 5.4.99.14, an isomerase catalyzing intramolecular rearrangements, not an intermolecular acyl transfer). However, both remaining options A (EC 2.3.1.322) and C (EC 2.3.1.312) are acyltransferases within the 2.3.1.x sub-subclass, which encompasses hundreds of GNAT-fold enzymes with diverse substrates (histones, polyamines, amino acids, aromatic amines, etc.). The specific substrate identity—D-glutamate for 2.3.1.312 versus whatever substrate 2.3.1.322 acts upon—is determined by a small set of active-site residues whose arrangement cannot be reliably predicted from general GNAT family knowledge. No conserved motif within the GNAT superfamily encodes D-glutamate specificity in a way that a model trained on other acetyltransferases could use to discriminate 312 from 322.


**Missing item-specific fact**

> The specific substrate identity of EC 2.3.1.322 and the precise active-site residue configuration that confers D-glutamate (as opposed to another substrate) specificity in this particular GNAT-fold enzyme. This enzyme was characterized experimentally only in 2023 (PubMed:36690779), so no well-established family-level substrate-specificity pattern exists that would allow transfer from other proteins.


**Reason**

> While the GNAT fold recognition is a valid transferable inference that narrows the four choices to two (eliminating the nucleotidyltransferase and isomerase options), the final distinction between EC 2.3.1.312 and EC 2.3.1.322 requires knowing the exact substrate specificity of this particular enzyme. Both are acyltransferases sharing the same broad fold. The substrate-determining residues in GNAT enzymes are highly variable and not predictable from general family-level knowledge, especially for a novel enzyme first characterized in 2023. This constitutes a fact about this exact protein that is not derivable from transferable knowledge of other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (2.3.1.322) and C (2.3.1.312) are acyltransferases in the 2.3.1.x sub-subclass. Without specific knowledge of the substrate of 2.3.1.322 and the active-site determinants of D-glutamate specificity, a knowledgeable model using only sequence and general family knowledge cannot confidently choose between them. The GNAT fold is shared by both.


### Important caveats

- The EC 2.3.1.312 assignment is experimentally validated (X-ray crystallography at 2.20 Å, mutagenesis of six active-site residues, enzymatic assay), making the key highly reliable.
- The GNAT fold recognition legitimately eliminates options B and D, so the question is not purely a four-way guess; it reduces to a two-way choice between closely related acyltransferase EC numbers.
- The enzyme and its EC number were first reported in 2023, meaning there is limited accumulated family-level knowledge from other proteins that could inform substrate-specificity predictions for this particular subfamily.
- The reviewer-only evidence confirms exact sequence match (SHA256) between the benchmark input and UniProt A0A2T1AE85, so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable GNAT (GCN5-related N-acetyltransferase) fold signature, notably the 'VANRGGKISQ' motif (RGG pattern characteristic of the CoA-binding loop in GNAT enzymes) and the overall ~333-aa architecture with a central β-sheet core flanked by α-helices. This family-level recognition legitimately eliminates option B (EC 2.7.7.43, a nucleotidyltransferase with an entirely different fold and catalytic mechanism involving a nucleotidyl group transfer) and option D (EC 5.4.99.14, an isomerase catalyzing intramolecular rearrangements, not an intermolecular acyl transfer). However, both remaining options A (EC 2.3.1.322) and C (EC 2.3.1.312) are acyltransferases within the 2.3.1.x sub-subclass, which encompasses hundreds of GNAT-fold enzymes with diverse substrates (histones, polyamines, amino acids, aromatic amines, etc.). The specific substrate identity—D-glutamate for 2.3.1.312 versus whatever substrate 2.3.1.322 acts upon—is determined by a small set of active-site residues whose arrangement cannot be reliably predicted from general GNAT family knowledge. No conserved motif within the GNAT superfamily encodes D-glutamate specificity in a way that a model trained on other acetyltransferases could use to discriminate 312 from 322.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity of EC 2.3.1.322 and the precise active-site residue configuration that confers D-glutamate (as opposed to another substrate) specificity in this particular GNAT-fold enzyme. This enzyme was characterized experimentally only in 2023 (PubMed:36690779), so no well-established family-level substrate-specificity pattern exists that would allow transfer from other proteins.",
    "reason": "While the GNAT fold recognition is a valid transferable inference that narrows the four choices to two (eliminating the nucleotidyltransferase and isomerase options), the final distinction between EC 2.3.1.312 and EC 2.3.1.322 requires knowing the exact substrate specificity of this particular enzyme. Both are acyltransferases sharing the same broad fold. The substrate-determining residues in GNAT enzymes are highly variable and not predictable from general family-level knowledge, especially for a novel enzyme first characterized in 2023. This constitutes a fact about this exact protein that is not derivable from transferable knowledge of other proteins."
  },
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A2T1AE85 (Swiss-Prot, reviewed) annotates this 333-aa protein as D-glutamate N-acetyltransferase with EC 2.3.1.312, supported by experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023) and X-ray crystallography (PDB:7XRJ, 2.20 Å). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H⁺ is confirmed by Rhea (RHEA:76495). The benchmark sequence SHA256 matches the source sequence exactly. The EC number assignment is experimentally validated, not merely computational."
  },
  "important_caveats": [
    "The EC 2.3.1.312 assignment is experimentally validated (X-ray crystallography at 2.20 Å, mutagenesis of six active-site residues, enzymatic assay), making the key highly reliable.",
    "The GNAT fold recognition legitimately eliminates options B and D, so the question is not purely a four-way guess; it reduces to a two-way choice between closely related acyltransferase EC numbers.",
    "The enzyme and its EC number were first reported in 2023, meaning there is limited accumulated family-level knowledge from other proteins that could inform substrate-specificity predictions for this particular subfamily.",
    "The reviewer-only evidence confirms exact sequence match (SHA256) between the benchmark input and UniProt A0A2T1AE85, so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (2.3.1.322) and C (2.3.1.312) are acyltransferases in the 2.3.1.x sub-subclass. Without specific knowledge of the substrate of 2.3.1.322 and the active-site determinants of D-glutamate specificity, a knowledgeable model using only sequence and general family knowledge cannot confidently choose between them. The GNAT fold is shared by both."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A2T1AE85 (Swiss-Prot, reviewed) annotates this 333-aa protein as D-glutamate N-acetyltransferase with EC 2.3.1.312, supported by experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023) and X-ray crystallography (PDB:7XRJ, 2.20 Å). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H⁺ is confirmed by Rhea (RHEA:76495). The benchmark sequence SHA256 matches the source sequence exactly. The EC number assignment is experimentally validated, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable GNAT (GCN5-related N-acetyltransferase) fold signature, notably the 'VANRGGKISQ' motif (RGG pattern characteristic of the CoA-binding loop in GNAT enzymes) and the overall ~333-aa architecture with a central β-sheet core flanked by α-helices. This family-level recognition legitimately eliminates option B (EC 2.7.7.43, a nucleotidyltransferase with an entirely different fold and catalytic mechanism involving a nucleotidyl group transfer) and option D (EC 5.4.99.14, an isomerase catalyzing intramolecular rearrangements, not an intermolecular acyl transfer). However, both remaining options A (EC 2.3.1.322) and C (EC 2.3.1.312) are acyltransferases within the 2.3.1.x sub-subclass, which encompasses hundreds of GNAT-fold enzymes with diverse substrates (histones, polyamines, amino acids, aromatic amines, etc.). The specific substrate identity—D-glutamate for 2.3.1.312 versus whatever substrate 2.3.1.322 acts upon—is determined by a small set of active-site residues whose arrangement cannot be reliably predicted from general GNAT family knowledge. No conserved motif within the GNAT superfamily encodes D-glutamate specificity in a way that a model trained on other acetyltransferases could use to discriminate 312 from 322.",
    "missing_item_specific_fact": "The specific substrate identity of EC 2.3.1.322 and the precise active-site residue configuration that confers D-glutamate (as opposed to another substrate) specificity in this particular GNAT-fold enzyme. This enzyme was characterized experimentally only in 2023 (PubMed:36690779), so no well-established family-level substrate-specificity pattern exists that would allow transfer from other proteins.",
    "reason": "While the GNAT fold recognition is a valid transferable inference that narrows the four choices to two (eliminating the nucleotidyltransferase and isomerase options), the final distinction between EC 2.3.1.312 and EC 2.3.1.322 requires knowing the exact substrate specificity of this particular enzyme. Both are acyltransferases sharing the same broad fold. The substrate-determining residues in GNAT enzymes are highly variable and not predictable from general family-level knowledge, especially for a novel enzyme first characterized in 2023. This constitutes a fact about this exact protein that is not derivable from transferable knowledge of other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (2.3.1.322) and C (2.3.1.312) are acyltransferases in the 2.3.1.x sub-subclass. Without specific knowledge of the substrate of 2.3.1.322 and the active-site determinants of D-glutamate specificity, a knowledgeable model using only sequence and general family knowledge cannot confidently choose between them. The GNAT fold is shared by both."
  },
  "important_caveats": [
    "The EC 2.3.1.312 assignment is experimentally validated (X-ray crystallography at 2.20 Å, mutagenesis of six active-site residues, enzymatic assay), making the key highly reliable.",
    "The GNAT fold recognition legitimately eliminates options B and D, so the question is not purely a four-way guess; it reduces to a two-way choice between closely related acyltransferase EC numbers.",
    "The enzyme and its EC number were first reported in 2023, meaning there is limited accumulated family-level knowledge from other proteins that could inform substrate-specificity predictions for this particular subfamily.",
    "The reviewer-only evidence confirms exact sequence match (SHA256) between the benchmark input and UniProt A0A2T1AE85, so the annotation applies directly to the supplied sequence."
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
  "benchmark_sequence_length": 333,
  "benchmark_sequence_sha256": "c0d9f366f41666bbc0ced1375f251e0666f921019f749a5a93a254b4c941f9e7",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-07-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 333,
  "current_source_sequence_sha256": "c0d9f366f41666bbc0ced1375f251e0666f921019f749a5a93a254b4c941f9e7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 17,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2T1AE85",
  "selected_historical_entry_version": 17,
  "selected_historical_record_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "selected_historical_source_sequence_length": 333,
  "selected_historical_source_sequence_sha256": "c0d9f366f41666bbc0ced1375f251e0666f921019f749a5a93a254b4c941f9e7",
  "selected_historical_version": {
    "accession": "A0A2T1AE85",
    "database": "Swiss-Prot",
    "entryVersion": 17,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DGCN_TRISK",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2T1AE85\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-07-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Epibacterium scottomollicae\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Alphaproteobacteria\",\"Rhodobacterales\",\"Paracoccaceae\",\"Tritonibacter\"],\"scientificName\":\"Tritonibacter scottomollicae\",\"taxonId\":483013}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.312\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"D-glutamate N-acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:76496\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76495\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29986\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:195260\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yu Y.\",\"Wang P.\",\"Cao H.Y.\",\"Teng Z.J.\",\"Zhu Y.\",\"Wang M.\",\"McMinn A.\",\"Chen Y.\",\"Xiang H.\",\"Zhang Y.Z.\",\"Chen X.L.\",\"Zhang Y.Q.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36690779\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41396-023-01364-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"537\",\"id\":\"36690779\",\"journal\":\"ISME J.\",\"lastPage\":\"548\",\"publicationDate\":\"2023\",\"title\":\"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.\",\"volume\":\"17\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7XRJ\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 25328 / CCUG 55858 / LMG 24367 / R-28751\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H1",
  "excerpt": "ID   DGCN_TRISK              Reviewed;         333 AA.\nAC   A0A2T1AE85;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUL-2018, sequence version 1.\nDT   28-JAN-2026, entry version 17.\nDE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\nGN   Name=dgcN {ECO:0000303|PubMed:36690779};\nGN   ORFNames=CLV89_10851 {ECO:0000312|EMBL:PRZ46905.1};\nOS   Tritonibacter scottomollicae (Epibacterium scottomollicae).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;\nOC   Rhodobacterales; Paracoccaceae; Tritonibacter.\nOX   NCBI_TaxID=483013;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7XRJ}\nRP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY, AND\nRP   MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190.\nRC   STRAIN=DSM 25328 / CCUG 55858 / LMG 24367 / R-28751;\nRX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;\nRA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,\nRA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;\nRT   \"Novel D-glutamate catabolic pathway in marine Proteobacteria and\nRT   halophilic archaea.\";\nRL   ISME J. 17:537-548(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+);\nCC         Xref=Rhea:RHEA:76495, ChEBI:CHEBI:15378, ChEBI:CHEBI:29986,\nCC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195260;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:76496;\nCC         Evidence={ECO:0000305|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
