# GO_molecular_function_0085

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0085.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — endo-1,4-beta-xylanase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSYKAFLITLAAVTRVLTYPANSSFELVDRSGTPSSTGTSGGYYYSFWTDGGADVTYTNGAGGEYKLQWSGNGNLVGGKGWNPGSAKAVTYSGTYSPNGNSYLSLYGWTTSPLIEYYVVENFGTYDPSTGATLKGTVVSDGATYKIYQTQRVNQPSIIGTATFYQYWSVRQTKRTGGTVTTGNHFNAWKALGMNMGTFDYMIVATEGYFSSGSSDITVGSSTGGGDSGSPTSAPTTSPTTSPGGTCGALYSQCGGTGFTGSQCCASGTCKYANSYYSQCL

[Multiple Choices]
A. mannose-6-phosphate isomerase activity
B. endo-1,4-beta-xylanase activity
C. medium-chain fatty acyl-CoA dehydrogenase activity
D. lipid binding
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

> The supplied sequence matches a protein annotated as an endo-1,4-beta-xylanase, with the corresponding catalytic activity and GO term. The annotation combines similarity-based function assignment and a PROSITE-ProRule inference; it supports choice B, though it is not equivalent to direct experimental confirmation of the catalytic activity.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a hydrophobic signal-peptide-like region and is otherwise consistent with a secreted fungal carbohydrate-active enzyme: it is rich in aromatic residues that can support polysaccharide-substrate recognition and lacks the overall character of a mitochondrial acyl-CoA dehydrogenase or a typical sugar-phosphate isomerase. Transferable knowledge of secreted fungal cell-wall-degrading enzymes makes a xylanase a credible match among these choices, distinguishing B from A, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and offered alternatives support a meaningful family- and localization-level inference toward a secreted xylanase. The specific database annotation is not necessary to distinguish B from these alternatives, although sequence-based reasoning alone is not a direct assay of substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the sequence features and likely secreted carbohydrate-enzyme role favor xylanase activity; none of the other options is comparably supported.


### Important caveats

- The reviewer-only annotation supports the key, but its catalytic-activity assignment includes computational rule-based evidence and similarity-based function annotation; direct experimental validation of xylan hydrolysis is not established by these excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a hydrophobic signal-peptide-like region and is otherwise consistent with a secreted fungal carbohydrate-active enzyme: it is rich in aromatic residues that can support polysaccharide-substrate recognition and lacks the overall character of a mitochondrial acyl-CoA dehydrogenase or a typical sugar-phosphate isomerase. Transferable knowledge of secreted fungal cell-wall-degrading enzymes makes a xylanase a credible match among these choices, distinguishing B from A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and offered alternatives support a meaningful family- and localization-level inference toward a secreted xylanase. The specific database annotation is not necessary to distinguish B from these alternatives, although sequence-based reasoning alone is not a direct assay of substrate specificity."
  },
  "case_id": "GO_molecular_function_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches a protein annotated as an endo-1,4-beta-xylanase, with the corresponding catalytic activity and GO term. The annotation combines similarity-based function assignment and a PROSITE-ProRule inference; it supports choice B, though it is not equivalent to direct experimental confirmation of the catalytic activity."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key, but its catalytic-activity assignment includes computational rule-based evidence and similarity-based function annotation; direct experimental validation of xylan hydrolysis is not established by these excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the sequence features and likely secreted carbohydrate-enzyme role favor xylanase activity; none of the other options is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches a protein annotated as an endo-1,4-beta-xylanase, with the corresponding catalytic activity and GO term. The annotation combines similarity-based function assignment and a PROSITE-ProRule inference; it supports choice B, though it is not equivalent to direct experimental confirmation of the catalytic activity.",
    "evidence_ids": ["C5", "C6", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a hydrophobic signal-peptide-like region and is otherwise consistent with a secreted fungal carbohydrate-active enzyme: it is rich in aromatic residues that can support polysaccharide-substrate recognition and lacks the overall character of a mitochondrial acyl-CoA dehydrogenase or a typical sugar-phosphate isomerase. Transferable knowledge of secreted fungal cell-wall-degrading enzymes makes a xylanase a credible match among these choices, distinguishing B from A, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and offered alternatives support a meaningful family- and localization-level inference toward a secreted xylanase. The specific database annotation is not necessary to distinguish B from these alternatives, although sequence-based reasoning alone is not a direct assay of substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the sequence features and likely secreted carbohydrate-enzyme role favor xylanase activity; none of the other options is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key, but its catalytic-activity assignment includes computational rule-based evidence and similarity-based function annotation; direct experimental validation of xylan hydrolysis is not established by these excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A384JXV5 annotates this protein as Ethylene-inducing xylanase 1 (EIX1) with EC 3.2.1.8 (endo-1,4-beta-xylanase), assigned via PROSITE-ProRule PRU01097 (ECO:0000255). The GO term GO:0031176 (endo-1,4-beta-xylanase activity) is recorded with evidence IEA:UniProtKB-EC. The FUNCTION comment states 'Endo-1,4-beta-xylanase involved in the hydrolysis of xylan' with evidence by similarity to B3VSG7 and PubMed:33205907. The evidence is primarily computational (PROSITE pattern match) and by-similarity rather than direct experimental characterization of this specific protein's catalytic activity, but the annotation is consistent and not contradicted.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark GH11 (glycosyl hydrolase family 11) xylanase motif 'WSGNG' (at ~residue 65-69: 'YKLQWSGNGNLVGGKGWNPGSAKAVTYSGTYSPNGNSYLSLYGWTTSPLIEYYVVENFGTYDPSTGATLKGTVVSDGATYKIYQTQRVNQPSIIGTATFYQYWSVRQTKRTGGTVTTGNHFNAWKALGMNMGTFDYMIVATEGYFSSGSS'), along with two candidate catalytic glutamates in positions consistent with the GH11 β-jelly-roll fold. The N-terminal hydrophobic stretch (MVSYKAFLITLAAVTRVLTYPAN) indicates a signal peptide for secretion, typical of fungal GH11 xylanases. This family-level recognition (WSGNG motif, catalytic Glu spacing, small secreted β-jelly-roll architecture) is well-established from knowledge of other GH11 xylanases (e.g., Trichoderma, Bacillus, and other fungal xylanases). In contrast: (C) MCAD requires FAD-binding Rossmann-fold motifs (GGG, GxGxxG) and mitochondrial targeting—completely absent; (A) mannose-6-phosphate isomerase has a TIM-barrel fold with distinct motifs—absent; (D) lipid binding typically involves amphipathic helices or specific lipid-binding domains—no such features are present. The GH11 signature meaningfully and specifically selects B over the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the WSGNG motif and overall GH11 β-jelly-roll architecture from training on other GH11 xylanases, and can eliminate MCAD (no FAD-binding motifs), MPI (no TIM-barrel motifs), and lipid binding (no amphipathic helices or lipid-binding domains). This is a legitimate family-level inference from transferable knowledge of related proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GH11 xylanase signature (WSGNG motif, catalytic Glu positions, secreted β-jelly-roll architecture) is distinctive and incompatible with the structural requirements of MCAD (FAD-binding Rossmann fold), mannose-6-phosphate isomerase (TIM barrel), or generic lipid binding (amphipathic helices). Only B is consistent with the observed sequence features.


### Important caveats

- The EC 3.2.1.8 annotation is assigned via PROSITE-ProRule pattern match (computational) and by similarity to B3VSG7; direct experimental demonstration of xylanase activity on this specific EIX1 protein is not clearly documented in the supplied evidence.
- Some EIX-family proteins have been reported to lack catalytic xylanase activity while retaining elicitor function; however, the PROSITE annotation and the presence of catalytic Glu residues support the xylanase assignment.
- The PubMed reference (33205907) cited for FUNCTION is about perception of EIX-like proteins in plants, not direct enzymatic characterization of this protein.
- The GO annotation is IEA (Inferred from Electronic Annotation), derived from the EC assignment rather than independent experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark GH11 (glycosyl hydrolase family 11) xylanase motif 'WSGNG' (at ~residue 65-69: 'YKLQWSGNGNLVGGKGWNPGSAKAVTYSGTYSPNGNSYLSLYGWTTSPLIEYYVVENFGTYDPSTGATLKGTVVSDGATYKIYQTQRVNQPSIIGTATFYQYWSVRQTKRTGGTVTTGNHFNAWKALGMNMGTFDYMIVATEGYFSSGSS'), along with two candidate catalytic glutamates in positions consistent with the GH11 β-jelly-roll fold. The N-terminal hydrophobic stretch (MVSYKAFLITLAAVTRVLTYPAN) indicates a signal peptide for secretion, typical of fungal GH11 xylanases. This family-level recognition (WSGNG motif, catalytic Glu spacing, small secreted β-jelly-roll architecture) is well-established from knowledge of other GH11 xylanases (e.g., Trichoderma, Bacillus, and other fungal xylanases). In contrast: (C) MCAD requires FAD-binding Rossmann-fold motifs (GGG, GxGxxG) and mitochondrial targeting—completely absent; (A) mannose-6-phosphate isomerase has a TIM-barrel fold with distinct motifs—absent; (D) lipid binding typically involves amphipathic helices or specific lipid-binding domains—no such features are present. The GH11 signature meaningfully and specifically selects B over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the WSGNG motif and overall GH11 β-jelly-roll architecture from training on other GH11 xylanases, and can eliminate MCAD (no FAD-binding motifs), MPI (no TIM-barrel motifs), and lipid binding (no amphipathic helices or lipid-binding domains). This is a legitimate family-level inference from transferable knowledge of related proteins."
  },
  "case_id": "GO_molecular_function_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H1",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A384JXV5 annotates this protein as Ethylene-inducing xylanase 1 (EIX1) with EC 3.2.1.8 (endo-1,4-beta-xylanase), assigned via PROSITE-ProRule PRU01097 (ECO:0000255). The GO term GO:0031176 (endo-1,4-beta-xylanase activity) is recorded with evidence IEA:UniProtKB-EC. The FUNCTION comment states 'Endo-1,4-beta-xylanase involved in the hydrolysis of xylan' with evidence by similarity to B3VSG7 and PubMed:33205907. The evidence is primarily computational (PROSITE pattern match) and by-similarity rather than direct experimental characterization of this specific protein's catalytic activity, but the annotation is consistent and not contradicted."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation is assigned via PROSITE-ProRule pattern match (computational) and by similarity to B3VSG7; direct experimental demonstration of xylanase activity on this specific EIX1 protein is not clearly documented in the supplied evidence.",
    "Some EIX-family proteins have been reported to lack catalytic xylanase activity while retaining elicitor function; however, the PROSITE annotation and the presence of catalytic Glu residues support the xylanase assignment.",
    "The PubMed reference (33205907) cited for FUNCTION is about perception of EIX-like proteins in plants, not direct enzymatic characterization of this protein.",
    "The GO annotation is IEA (Inferred from Electronic Annotation), derived from the EC assignment rather than independent experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH11 xylanase signature (WSGNG motif, catalytic Glu positions, secreted β-jelly-roll architecture) is distinctive and incompatible with the structural requirements of MCAD (FAD-binding Rossmann fold), mannose-6-phosphate isomerase (TIM barrel), or generic lipid binding (amphipathic helices). Only B is consistent with the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A384JXV5 annotates this protein as Ethylene-inducing xylanase 1 (EIX1) with EC 3.2.1.8 (endo-1,4-beta-xylanase), assigned via PROSITE-ProRule PRU01097 (ECO:0000255). The GO term GO:0031176 (endo-1,4-beta-xylanase activity) is recorded with evidence IEA:UniProtKB-EC. The FUNCTION comment states 'Endo-1,4-beta-xylanase involved in the hydrolysis of xylan' with evidence by similarity to B3VSG7 and PubMed:33205907. The evidence is primarily computational (PROSITE pattern match) and by-similarity rather than direct experimental characterization of this specific protein's catalytic activity, but the annotation is consistent and not contradicted.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H1", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark GH11 (glycosyl hydrolase family 11) xylanase motif 'WSGNG' (at ~residue 65-69: 'YKLQWSGNGNLVGGKGWNPGSAKAVTYSGTYSPNGNSYLSLYGWTTSPLIEYYVVENFGTYDPSTGATLKGTVVSDGATYKIYQTQRVNQPSIIGTATFYQYWSVRQTKRTGGTVTTGNHFNAWKALGMNMGTFDYMIVATEGYFSSGSS'), along with two candidate catalytic glutamates in positions consistent with the GH11 β-jelly-roll fold. The N-terminal hydrophobic stretch (MVSYKAFLITLAAVTRVLTYPAN) indicates a signal peptide for secretion, typical of fungal GH11 xylanases. This family-level recognition (WSGNG motif, catalytic Glu spacing, small secreted β-jelly-roll architecture) is well-established from knowledge of other GH11 xylanases (e.g., Trichoderma, Bacillus, and other fungal xylanases). In contrast: (C) MCAD requires FAD-binding Rossmann-fold motifs (GGG, GxGxxG) and mitochondrial targeting—completely absent; (A) mannose-6-phosphate isomerase has a TIM-barrel fold with distinct motifs—absent; (D) lipid binding typically involves amphipathic helices or specific lipid-binding domains—no such features are present. The GH11 signature meaningfully and specifically selects B over the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the WSGNG motif and overall GH11 β-jelly-roll architecture from training on other GH11 xylanases, and can eliminate MCAD (no FAD-binding motifs), MPI (no TIM-barrel motifs), and lipid binding (no amphipathic helices or lipid-binding domains). This is a legitimate family-level inference from transferable knowledge of related proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH11 xylanase signature (WSGNG motif, catalytic Glu positions, secreted β-jelly-roll architecture) is distinctive and incompatible with the structural requirements of MCAD (FAD-binding Rossmann fold), mannose-6-phosphate isomerase (TIM barrel), or generic lipid binding (amphipathic helices). Only B is consistent with the observed sequence features."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation is assigned via PROSITE-ProRule pattern match (computational) and by similarity to B3VSG7; direct experimental demonstration of xylanase activity on this specific EIX1 protein is not clearly documented in the supplied evidence.",
    "Some EIX-family proteins have been reported to lack catalytic xylanase activity while retaining elicitor function; however, the PROSITE annotation and the presence of catalytic Glu residues support the xylanase assignment.",
    "The PubMed reference (33205907) cited for FUNCTION is about perception of EIX-like proteins in plants, not direct enzymatic characterization of this protein.",
    "The GO annotation is IEA (Inferred from Electronic Annotation), derived from the EC assignment rather than independent experimental evidence."
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
  "benchmark_sequence_length": 281,
  "benchmark_sequence_sha256": "01bc2397489efa344f606d78b71821f92a88f6b9264a6c8ef38136aff7712472",
  "current_entry_audit": {
    "entryVersion": 27,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 281,
  "current_source_sequence_sha256": "01bc2397489efa344f606d78b71821f92a88f6b9264a6c8ef38136aff7712472",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 25,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384JXV5",
  "selected_historical_entry_version": 25,
  "selected_historical_record_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "selected_historical_source_sequence_length": 281,
  "selected_historical_source_sequence_sha256": "01bc2397489efa344f606d78b71821f92a88f6b9264a6c8ef38136aff7712472",
  "selected_historical_version": {
    "accession": "A0A384JXV5",
    "database": "Swiss-Prot",
    "entryVersion": 25,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX1_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384JXV5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":27,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX1\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"B3VSG7\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (By similarity). May act as an elicitor of plant defense responses in certain plants but does not exhibit any cell death when transiently expressed in N.benthamiana (PubMed:33205907)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030248\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:cellulose binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031176\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:endo-1,4-beta-xylanase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-EC\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H1",
  "excerpt": "ID   EIX1_BOTFB              Reviewed;         281 AA.\nAC   A0A384JXV5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 25.\nDE   RecName: Full=Ethylene-inducing xylanase 1 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX1 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX1 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX1 {ECO:0000303|PubMed:33205907}; ORFNames=BCIN_12g00090;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.003931+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "url": "https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.003931+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "url": "https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a\nCC       major structural heterogeneous polysaccharide found in plant biomass\nCC       representing the second most abundant polysaccharide in the biosphere,\nCC       after cellulose (By similarity). May act as an elicitor of plant\nCC       defense responses in certain plants but does not exhibit any cell death\nCC       when transiently expressed in N.benthamiana (PubMed:33205907).\nCC       {ECO:0000250|UniProtKB:B3VSG7, ECO:0000269|PubMed:33205907}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.003931+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "url": "https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.003931+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "url": "https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0030248; F:cellulose binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.003931+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "url": "https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0031176; F:endo-1,4-beta-xylanase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.003931+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "url": "https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004476\nname: mannose-6-phosphate isomerase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: D-mannose 6-phosphate = D-fructose 6-phosphate.\" [RHEA:12356]\nsynonym: \"D-mannose-6-phosphate aldose-ketose-isomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"D-mannose-6-phosphate ketol-isomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"mannose phosphate isomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"phosphohexoisomerase activity\" BROAD [EC:5.3.1.8]\nsynonym: \"phosphohexomutase activity\" BROAD [EC:5.3.1.8]\nsynonym: \"phosphomannoisomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"phosphomannose isomerase activity\" RELATED [EC:5.3.1.8]\nxref: EC:5.3.1.8\nxref: MetaCyc:MANNPISOM-RXN\nxref: Reactome:R-HSA-3781832 \"Defective MPI does not  isomerize Fru6P to Man6P\"\nxref: Reactome:R-HSA-532549 \"MPI isomerises Fru6P to Man6P\"\nxref: RHEA:12356\nis_a: GO:0016861 ! intramolecular oxidoreductase activity, interconverting aldoses and ketoses\nproperty_value: skos:exactMatch EC:5.3.1.8\nproperty_value: skos:exactMatch RHEA:12356\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004476",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 42843-42863",
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
  "excerpt": "[Term]\nid: GO:0008289\nname: lipid binding\nnamespace: molecular_function\ndef: \"Binding to a lipid.\" [GOC:ai]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nis_a: GO:0005488 ! binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008289",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 81641-81661",
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
  "excerpt": "[Term]\nid: GO:0031176\nname: endo-1,4-beta-xylanase activity\nnamespace: molecular_function\ndef: \"Catalysis of the endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\" [EC:3.2.1.8]\nsynonym: \"1,4-beta-D-xylan xylanohydrolase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"1,4-beta-xylan xylanohydrolase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"beta-1,4-xylan xylanohydrolase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"beta-1,4-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"beta-D-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"beta-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"endo-(1,4)-beta-xylanase(1,4)-beta-xylan 4-xylanohydrolase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"endo-(1->4)-beta-xylanase(1->4)-beta-xylan 4-xylanohydrolase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"endo-1,4-beta-D-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"endo-1,4-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"endo-beta-1,4-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"xylanase\" BROAD [EC:3.2.1.8]\nxref: EC:3.2.1.8\nxref: MetaCyc:3.2.1.8-RXN\nis_a: GO:0097599 ! xylanase activity\nproperty_value: skos:exactMatch EC:3.2.1.8\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031176",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 173997-174018",
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
  "excerpt": "[Term]\nid: GO:0070991\nname: medium-chain fatty acyl-CoA dehydrogenase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a medium-chain 2,3-saturated fatty acyl-CoA + H+ + oxidized [electron-transfer flavoprotein] = a medium-chain trans-(2E)-enoyl-CoA + reduced [electron-transfer flavoprotein]. A medium-chain fatty acid has an aliphatic tail containing 6 to 12 carbons.\" [RHEA:14477]\ncomment: While there is not universal consensus on the lengths of short-, medium-, long- and very-long-chain fatty acids, the GO uses the definitions in ChEBI (see CHEBI:26666, CHEBI:59554, CHEBI:15904 and CHEBI:27283).\nsynonym: \"MCAD activity\" EXACT [GOC:mah]\nxref: EC:1.3.8.7\nxref: MetaCyc:RXN-11734\nxref: RHEA:14477\nxref: RHEA:43464\nxref: RHEA:47296\nxref: RHEA:48176\nxref: RHEA:48180\nxref: RHEA:48208\nxref: RHEA:82951\nxref: RHEA:84471\nxref: RHEA:84475\nxref: RHEA:84607\nxref: RHEA:84611\nxref: RHEA:84615\nis_a: GO:0003995 ! acyl-CoA dehydrogenase activity\nproperty_value: skos:exactMatch EC:1.3.8.7\nproperty_value: skos:exactMatch MetaCyc:RXN-11734\nproperty_value: skos:exactMatch RHEA:14477\nproperty_value: skos:narrowMatch RHEA:43464\nproperty_value: skos:narrowMatch RHEA:47296\nproperty_value: skos:narrowMatch RHEA:48176\nproperty_value: skos:narrowMatch RHEA:48180\nproperty_value: skos:narrowMatch RHEA:48208\nproperty_value: skos:narrowMatch RHEA:82951\nproperty_value: skos:narrowMatch RHEA:84471\nproperty_value: skos:narrowMatch RHEA:84475\nproperty_value: skos:narrowMatch RHEA:84607\nproperty_value: skos:narrowMatch RHEA:84611\nproperty_value: skos:narrowMatch RHEA:84615\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0070991",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 373007-373043",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
