# GO_molecular_function_0102

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0102.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — protein dimerization activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
METVQSSSSAELLRAQTHFSTQLFSFQNYASLKCALHLGIPDAIKQHGKPMNLSELTSALPIKPSKAPYIHRLMRMLVKAGYFAQENECFDLTPIGLLLLKDDPINIRALVLLELHPALLLPWIALSEWFQNDDATPFVTAHGKSFWDYTSRDPEFRKLFDEAMAGDSELISKVLVTEFKYVFEGLKSLVDVGGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSIPVKDKGGKVIIIEGVVELEKNAGNEYAGLENLDMEMLVLYNSKERTKKEWAKLFSDAGFSDYKFIPALDSWCIIELTP

[Multiple Choices]
A. oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor
B. single-stranded DNA endodeoxyribonuclease activity
C. protein dimerization activity
D. NF-kappaB binding
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

### Expected-answer support: contradicted

> The sequence-matched record reports experimentally supported O-methyltransferase activity, while protein dimerization is only an InterPro-based computational annotation. The evidence does not show that dimerization is the protein's primary molecular function; the experimentally supported catalytic function is not offered among the choices.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a glycine-rich SAM-dependent methyltransferase motif, supporting an O-methyltransferase-family inference. That catalytic function is absent from the choices, and recognizing the family does not by itself establish protein dimerization activity. A family-based or exact-sequence annotation specifically linking this protein to dimerization would be needed to select C on that basis.


**Missing item-specific fact**

> The exact-sequence InterPro-based assignment of protein dimerization activity, or other evidence that dimerization is a relevant function of this protein.


**Reason**

> Transferable sequence knowledge points to methyltransferase activity, not to any offered primary function. The remaining alternatives are poor matches, but eliminating them does not provide a biological basis for treating dimerization as primary; that choice depends on an unavailable protein-specific annotation or evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No offered option describes the experimentally supported O-methyltransferase activity. The evidence does not establish another offered function as primary.


### Important caveats

- The dimerization annotation is computational (IEA:InterPro), not reported here as experimentally demonstrated.
- The evidence for methyltransferase activity applies to the sequence-matched protein, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich SAM-dependent methyltransferase motif, supporting an O-methyltransferase-family inference. That catalytic function is absent from the choices, and recognizing the family does not by itself establish protein dimerization activity. A family-based or exact-sequence annotation specifically linking this protein to dimerization would be needed to select C on that basis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact-sequence InterPro-based assignment of protein dimerization activity, or other evidence that dimerization is a relevant function of this protein.",
    "reason": "Transferable sequence knowledge points to methyltransferase activity, not to any offered primary function. The remaining alternatives are poor matches, but eliminating them does not provide a biological basis for treating dimerization as primary; that choice depends on an unavailable protein-specific annotation or evidence."
  },
  "case_id": "GO_molecular_function_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports experimentally supported O-methyltransferase activity, while protein dimerization is only an InterPro-based computational annotation. The evidence does not show that dimerization is the protein's primary molecular function; the experimentally supported catalytic function is not offered among the choices."
  },
  "important_caveats": [
    "The dimerization annotation is computational (IEA:InterPro), not reported here as experimentally demonstrated.",
    "The evidence for methyltransferase activity applies to the sequence-matched protein, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No offered option describes the experimentally supported O-methyltransferase activity. The evidence does not establish another offered function as primary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0102",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports experimentally supported O-methyltransferase activity, while protein dimerization is only an InterPro-based computational annotation. The evidence does not show that dimerization is the protein's primary molecular function; the experimentally supported catalytic function is not offered among the choices.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a glycine-rich SAM-dependent methyltransferase motif, supporting an O-methyltransferase-family inference. That catalytic function is absent from the choices, and recognizing the family does not by itself establish protein dimerization activity. A family-based or exact-sequence annotation specifically linking this protein to dimerization would be needed to select C on that basis.",
    "missing_item_specific_fact": "The exact-sequence InterPro-based assignment of protein dimerization activity, or other evidence that dimerization is a relevant function of this protein.",
    "reason": "Transferable sequence knowledge points to methyltransferase activity, not to any offered primary function. The remaining alternatives are poor matches, but eliminating them does not provide a biological basis for treating dimerization as primary; that choice depends on an unavailable protein-specific annotation or evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No offered option describes the experimentally supported O-methyltransferase activity. The evidence does not establish another offered function as primary."
  },
  "important_caveats": [
    "The dimerization annotation is computational (IEA:InterPro), not reported here as experimentally demonstrated.",
    "The evidence for methyltransferase activity applies to the sequence-matched protein, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E7FL15 does carry GO:0046983 (protein dimerization activity) with IEA:InterPro evidence (C9, H7). However, the PRIMARY molecular function annotated with experimental IDA evidence is GO:0008171 (O-methyltransferase activity), which is not offered among the choices. The author's key C is technically supported as a database annotation, but it is a secondary, automated annotation rather than the protein's primary catalytic function. Among the four offered options, C is the only one with any annotation on this protein.

Citations as saved: [C9](#evidence-c9), [H7](#evidence-h7), [C8](#evidence-c8), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of class I plant O-methyltransferases (SAM-dependent OMTs), including the conserved C-terminal region with 'GDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSI' and the 'GGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRV' region characteristic of the VQSSSSAELLRAQTHFSTQLFSFQNYASLKCALHLGIPDAIKQHGKPMNLSELTSALPIKPSKAPYIHRLMRMLVKAGYFAQENECFDLTPIGLLLLKDDPINIRALVLLELHPALLLPWIALSEWFQNDDATPFVTAHGKSFWDYTSRDPEFRKLFDEAMAGDSELISKVLVTEFKYVFEGLKSLVDVGGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSIPVKDKGGKVIIIEGVVELEKNAGNEYAGLENLDMEMLVLYNSKERTKKEWAKLFSDAGFSDYKFIPALDSWCIIELTP pattern. From family knowledge, plant class I OMTs are well-documented to form homodimers (e.g., caffeic acid OMTs, isoflavone OMTs, and many others across the family). Option A (oxidoreductase acting on NAD(P)H/O2) can be eliminated: no NAD/FAD-binding Rossmann motifs or redox-active residues are present. Option B (ssDNA endonuclease) can be eliminated: no nuclease catalytic motifs (e.g., DEDD, ExoI, or restriction-enzyme motifs) and no DNA-binding basic patches. Option D (NF-kappaB binding) can be eliminated: NF-kappaB is a mammalian transcription factor; a plant protein of this size and sequence context would not have evolved NF-kappaB-binding capability. This leaves C as the only option with a credible family-level basis: plant OMTs commonly function as homodimers, making protein dimerization activity the best available answer among the four choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the plant class I OMT family from sequence motifs can apply the well-known family-level regularity that these enzymes form homodimers, while eliminating A (no redox motifs), B (no nuclease motifs), and D (mammalian-specific interaction irrelevant to a plant enzyme). This is legitimate transferable knowledge about the protein family, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the question asks for 'primary molecular function' and the true primary function (O-methyltransferase activity, GO:0008171) is not offered, among the four choices only C has any biological basis. A, B, and D are clearly incompatible with the protein's identity. No ambiguity among the offered options.


### Important caveats

- The author's key C (protein dimerization activity) is an IEA:InterPro automated annotation, not an experimentally determined primary function. The actual primary molecular function is O-methyltransferase activity (GO:0008171, IDA evidence), which is absent from the choices.
- The question stem asks for 'primary molecular function' but the correct answer is a secondary structural/assembly property, making the question somewhat misleading even though C is the best among the four offered options.
- The protein is from Carapichea ipecacuanha (plant), which is relevant for eliminating option D (NF-kappaB is mammalian) but this organism identity was not provided in the original input; it is inferred from the sequence's plant OMT family context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of class I plant O-methyltransferases (SAM-dependent OMTs), including the conserved C-terminal region with 'GDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSI' and the 'GGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRV' region characteristic of the VQSSSSAELLRAQTHFSTQLFSFQNYASLKCALHLGIPDAIKQHGKPMNLSELTSALPIKPSKAPYIHRLMRMLVKAGYFAQENECFDLTPIGLLLLKDDPINIRALVLLELHPALLLPWIALSEWFQNDDATPFVTAHGKSFWDYTSRDPEFRKLFDEAMAGDSELISKVLVTEFKYVFEGLKSLVDVGGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSIPVKDKGGKVIIIEGVVELEKNAGNEYAGLENLDMEMLVLYNSKERTKKEWAKLFSDAGFSDYKFIPALDSWCIIELTP pattern. From family knowledge, plant class I OMTs are well-documented to form homodimers (e.g., caffeic acid OMTs, isoflavone OMTs, and many others across the family). Option A (oxidoreductase acting on NAD(P)H/O2) can be eliminated: no NAD/FAD-binding Rossmann motifs or redox-active residues are present. Option B (ssDNA endonuclease) can be eliminated: no nuclease catalytic motifs (e.g., DEDD, ExoI, or restriction-enzyme motifs) and no DNA-binding basic patches. Option D (NF-kappaB binding) can be eliminated: NF-kappaB is a mammalian transcription factor; a plant protein of this size and sequence context would not have evolved NF-kappaB-binding capability. This leaves C as the only option with a credible family-level basis: plant OMTs commonly function as homodimers, making protein dimerization activity the best available answer among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the plant class I OMT family from sequence motifs can apply the well-known family-level regularity that these enzymes form homodimers, while eliminating A (no redox motifs), B (no nuclease motifs), and D (mammalian-specific interaction irrelevant to a plant enzyme). This is legitimate transferable knowledge about the protein family, not a lookup of this specific protein's annotation."
  },
  "case_id": "GO_molecular_function_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C9",
      "H7",
      "C8",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E7FL15 does carry GO:0046983 (protein dimerization activity) with IEA:InterPro evidence (C9, H7). However, the PRIMARY molecular function annotated with experimental IDA evidence is GO:0008171 (O-methyltransferase activity), which is not offered among the choices. The author's key C is technically supported as a database annotation, but it is a secondary, automated annotation rather than the protein's primary catalytic function. Among the four offered options, C is the only one with any annotation on this protein."
  },
  "important_caveats": [
    "The author's key C (protein dimerization activity) is an IEA:InterPro automated annotation, not an experimentally determined primary function. The actual primary molecular function is O-methyltransferase activity (GO:0008171, IDA evidence), which is absent from the choices.",
    "The question stem asks for 'primary molecular function' but the correct answer is a secondary structural/assembly property, making the question somewhat misleading even though C is the best among the four offered options.",
    "The protein is from Carapichea ipecacuanha (plant), which is relevant for eliminating option D (NF-kappaB is mammalian) but this organism identity was not provided in the original input; it is inferred from the sequence's plant OMT family context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the question asks for 'primary molecular function' and the true primary function (O-methyltransferase activity, GO:0008171) is not offered, among the four choices only C has any biological basis. A, B, and D are clearly incompatible with the protein's identity. No ambiguity among the offered options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E7FL15 does carry GO:0046983 (protein dimerization activity) with IEA:InterPro evidence (C9, H7). However, the PRIMARY molecular function annotated with experimental IDA evidence is GO:0008171 (O-methyltransferase activity), which is not offered among the choices. The author's key C is technically supported as a database annotation, but it is a secondary, automated annotation rather than the protein's primary catalytic function. Among the four offered options, C is the only one with any annotation on this protein.",
    "evidence_ids": ["C9", "H7", "C8", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of class I plant O-methyltransferases (SAM-dependent OMTs), including the conserved C-terminal region with 'GDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSI' and the 'GGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRV' region characteristic of the VQSSSSAELLRAQTHFSTQLFSFQNYASLKCALHLGIPDAIKQHGKPMNLSELTSALPIKPSKAPYIHRLMRMLVKAGYFAQENECFDLTPIGLLLLKDDPINIRALVLLELHPALLLPWIALSEWFQNDDATPFVTAHGKSFWDYTSRDPEFRKLFDEAMAGDSELISKVLVTEFKYVFEGLKSLVDVGGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSIPVKDKGGKVIIIEGVVELEKNAGNEYAGLENLDMEMLVLYNSKERTKKEWAKLFSDAGFSDYKFIPALDSWCIIELTP pattern. From family knowledge, plant class I OMTs are well-documented to form homodimers (e.g., caffeic acid OMTs, isoflavone OMTs, and many others across the family). Option A (oxidoreductase acting on NAD(P)H/O2) can be eliminated: no NAD/FAD-binding Rossmann motifs or redox-active residues are present. Option B (ssDNA endonuclease) can be eliminated: no nuclease catalytic motifs (e.g., DEDD, ExoI, or restriction-enzyme motifs) and no DNA-binding basic patches. Option D (NF-kappaB binding) can be eliminated: NF-kappaB is a mammalian transcription factor; a plant protein of this size and sequence context would not have evolved NF-kappaB-binding capability. This leaves C as the only option with a credible family-level basis: plant OMTs commonly function as homodimers, making protein dimerization activity the best available answer among the four choices.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the plant class I OMT family from sequence motifs can apply the well-known family-level regularity that these enzymes form homodimers, while eliminating A (no redox motifs), B (no nuclease motifs), and D (mammalian-specific interaction irrelevant to a plant enzyme). This is legitimate transferable knowledge about the protein family, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the question asks for 'primary molecular function' and the true primary function (O-methyltransferase activity, GO:0008171) is not offered, among the four choices only C has any biological basis. A, B, and D are clearly incompatible with the protein's identity. No ambiguity among the offered options."
  },
  "important_caveats": [
    "The author's key C (protein dimerization activity) is an IEA:InterPro automated annotation, not an experimentally determined primary function. The actual primary molecular function is O-methyltransferase activity (GO:0008171, IDA evidence), which is absent from the choices.",
    "The question stem asks for 'primary molecular function' but the correct answer is a secondary structural/assembly property, making the question somewhat misleading even though C is the best among the four offered options.",
    "The protein is from Carapichea ipecacuanha (plant), which is relevant for eliminating option D (NF-kappaB is mammalian) but this organism identity was not provided in the original input; it is inferred from the sequence's plant OMT family context."
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
  "benchmark_sequence_length": 350,
  "benchmark_sequence_sha256": "06d60d20d59ec0d189d9e458b41043b823eff47106d90b331759a7a28b559f05",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-04-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 350,
  "current_source_sequence_sha256": "06d60d20d59ec0d189d9e458b41043b823eff47106d90b331759a7a28b559f05",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E7FL15",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "selected_historical_source_sequence_length": 350,
  "selected_historical_source_sequence_sha256": "06d60d20d59ec0d189d9e458b41043b823eff47106d90b331759a7a28b559f05",
  "selected_historical_version": {
    "accession": "E7FL15",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CIOMT_CARIP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E7FL15\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-04-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ipecac\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Rubiaceae\",\"Rubioideae\",\"Palicoureeae\",\"Carapichea\"],\"scientificName\":\"Carapichea ipecacuanha\",\"synonyms\":[\"Callicocca ipecacuanha\"],\"taxonId\":77880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.395\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"7'-O-demethylcephaeline 7'-O-methyltransferase CiOMT\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"Cephaeline synthase CiOMT\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ72588.1\",\"source\":\"EMBL\"}],\"value\":\"7'-O-demethylcephaeline/cephaeline O-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ72588.1\",\"source\":\"EMBL\"}],\"value\":\"7'OMT\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"CiOMT\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.396\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"Cephaeline 6'-O-methyltransferase CiOMT\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"Emetine synthase CiOMT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase involved in the biosynthesis of ipecac and benzylisoquinoline monoterpenoid-isoquinoline alkaloids natural products, starting by the condensation of dopamine and secologanin, and including emetine and cephaeline, drugs used both as anti-protozoal (e.g. treatment of ameobiasis) and as emetic agents (PubMed:21228475). Catalyzes successively the 7'-O-methylation of 7'-O-demethylcephaeline to produce cephaeline, and its 6'-O-methylation to produce emetine (PubMed:21228475)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80556\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.395\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"name\":\"7'-O-demethylcephaeline + S-adenosyl-L-methionine = cephaeline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80555\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231587\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231589\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80660\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.396\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"name\":\"cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80659\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:149548\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231587\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"id\":\"GO:0008171\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:O-methyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0046983\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:protein dimerization activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Cheong B.E.\",\"Takemura T.\",\"Yoshimatsu K.\",\"Sato F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21228475\"},{\"database\":\"DOI\",\"id\":\"10.1271/bbb.100605\"}],\"citationType\":\"journal article\",\"firstPage\":\"107\",\"id\":\"21228475\",\"journal\":\"Biosci. Biotechnol. Biochem.\",\"lastPage\":\"113\",\"publicationDate\":\"2011\",\"title\":\"Molecular cloning of an O-methyltransferase from adventitious roots of Carapichea ipecacuanha.\",\"volume\":\"75\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ72588.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Root\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   CIOMT_CARIP             Reviewed;         350 AA.\nAC   E7FL15;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-APR-2011, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=Cephaeline 6'-O-methyltransferase CiOMT {ECO:0000303|PubMed:21228475};\nDE            Short=Emetine synthase CiOMT {ECO:0000303|PubMed:21228475};\nDE            EC=2.1.1.396 {ECO:0000269|PubMed:21228475};\nDE   AltName: Full=7'-O-demethylcephaeline 7'-O-methyltransferase CiOMT {ECO:0000303|PubMed:21228475};\nDE            Short=Cephaeline synthase CiOMT {ECO:0000303|PubMed:21228475};\nDE            EC=2.1.1.395 {ECO:0000269|PubMed:21228475};\nDE   AltName: Full=7'-O-demethylcephaeline/cephaeline O-methyltransferase {ECO:0000303|PubMed:21228475, ECO:0000312|EMBL:BAJ72588.1};\nDE            Short=7'OMT {ECO:0000312|EMBL:BAJ72588.1};\nDE            Short=CiOMT {ECO:0000303|PubMed:21228475};\nGN   Name=OMT {ECO:0000303|PubMed:21228475};\nOS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;\nOC   Carapichea.\nOX   NCBI_TaxID=77880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAJ72588.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.\nRC   TISSUE=Root;\nRX   PubMed=21228475; DOI=10.1271/bbb.100605;\nRA   Cheong B.E., Takemura T., Yoshimatsu K., Sato F.;\nRT   \"Molecular cloning of an O-methyltransferase from adventitious roots of\nRT   Carapichea ipecacuanha.\";\nRL   Biosci. Biotechnol. Biochem. 75:107-113(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 22-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: O-methyltransferase involved in the biosynthesis of ipecac\nCC       and benzylisoquinoline monoterpenoid-isoquinoline alkaloids natural\nCC       products, starting by the condensation of dopamine and secologanin, and\nCC       including emetine and cephaeline, drugs used both as anti-protozoal\nCC       (e.g. treatment of ameobiasis) and as emetic agents (PubMed:21228475).\nCC       Catalyzes successively the 7'-O-methylation of 7'-O-demethylcephaeline\nCC       to produce cephaeline, and its 6'-O-methylation to produce emetine\nCC       (PubMed:21228475). {ECO:0000269|PubMed:21228475}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=7'-O-demethylcephaeline + S-adenosyl-L-methionine = cephaeline\nCC         + S-adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:80555,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231587, ChEBI:CHEBI:231589; EC=2.1.1.395;\nCC         Evidence={ECO:0000269|PubMed:21228475};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80556;\nCC         Evidence={ECO:0000269|PubMed:21228475};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-\nCC         homocysteine + H(+); Xref=Rhea:RHEA:80659, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:149548,\nCC         ChEBI:CHEBI:231587; EC=2.1.1.396;\nCC         Evidence={ECO:0000269|PubMed:21228475};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80660;\nCC         Evidence={ECO:0000269|PubMed:21228475};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0008171; F:O-methyltransferase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0046983; F:protein dimerization activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000014\nname: single-stranded DNA endonuclease activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of ester linkages within a single-stranded deoxyribonucleic acid molecule by creating internal breaks.\" [GOC:mah]\nsynonym: \"single-stranded DNA endodeoxyribonuclease activity\" EXACT []\nsynonym: \"single-stranded DNA specific endodeoxyribonuclease activity\" RELATED []\nsynonym: \"ssDNA-specific endodeoxyribonuclease activity\" RELATED [GOC:mah]\nis_a: GO:0004520 ! DNA endonuclease activity\nis_a: GO:0016788 ! hydrolase activity, acting on ester bonds\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000014",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 159-169",
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
  "excerpt": "[Term]\nid: GO:0046983\nname: protein dimerization activity\nnamespace: molecular_function\ndef: \"The formation of a protein dimer, a macromolecular structure consists of two noncovalently associated identical or nonidentical subunits.\" [ISBN:0198506732]\nis_a: GO:0005515 ! protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046983",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 282554-282560",
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
  "excerpt": "[Term]\nid: GO:0050664\nname: oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor\nnamespace: molecular_function\ndef: \"Catalysis of an oxidation-reduction (redox) reaction in which NADH or NADPH acts as a hydrogen or electron donor and reduces an oxygen molecule.\" [EC:1.6.3.-]\nsynonym: \"oxidoreductase activity, acting on NADH or NADPH, oxygen as acceptor\" RELATED []\nxref: EC:1.6.3.-\nis_a: GO:0016651 ! oxidoreductase activity, acting on NAD(P)H\nproperty_value: skos:exactMatch EC:1.6.3.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0050664",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 318421-318430",
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
  "excerpt": "[Term]\nid: GO:0051059\nname: NF-kappaB binding\nnamespace: molecular_function\ndef: \"Binding to NF-kappaB, a transcription factor for eukaryotic RNA polymerase II promoters.\" [GOC:ai]\nis_a: GO:0061629 ! RNA polymerase II-specific DNA-binding transcription factor binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051059",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 322427-322433",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 102. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
