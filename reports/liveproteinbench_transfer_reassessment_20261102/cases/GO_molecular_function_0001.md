# GO_molecular_function_0001

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0001.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — endo-1,4-beta-xylanase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVCFSSLFVAASAIAGVFASPVDHEQLAKRQSTPSSQGTHDGYFYSWWTDGGAAATYTNLAGGEYSVSWSNGGNLVGGKGWNPGSARTITYSGTYNPNGNSYLAVYGWTRNPQPWLTPLVVEYYVVENFGTYNPSSGATARGQVTHDGALYRLFESTRTNQPSIDGTATFQQYWAVRDVKRTGGTVNMATFFNAWTAAGMRLGTHNYQVVATEGYFSSGSARINVAGGGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL

[Multiple Choices]
A. lyase activity
B. tau protein binding
C. endo-1,4-beta-xylanase activity
D. D-lactate dehydrogenase activity
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

> The sequence-matched UniProt record annotates the protein as an endo-1,4-beta-xylanase and specifies hydrolysis of beta-xylosidic linkages in xylans. The annotation is qualified: the catalytic-activity assignment is based on a PROSITE rule, and the function comment includes transfer by similarity; the cited paper evidence concerns immunity-inducing activity. Thus the key is scientifically supported, though these excerpts do not establish a direct experimental assay of this protein's catalysis.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic segment consistent with secretion, followed by a compact, aromatic-rich domain consistent with a fungal glycoside hydrolase/xylanase rather than a dehydrogenase. Transferable family knowledge about secreted fungal xylanases makes xylan hydrolysis (C) a credible inference. That reaction is hydrolysis, distinguishing C from the nonhydrolytic lyase activity in A; tau binding (B) and D-lactate dehydrogenase activity (D) fit the sequence context and likely enzyme family poorly.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable knowledge of fungal secreted glycoside hydrolases provide a meaningful basis for choosing C among these alternatives. The inference is not certain from sequence alone, but it does not require knowing this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered catalytic alternatives distinguish hydrolysis of xylan from lyase and dehydrogenase reactions, while tau protein binding is not a comparable fit to the sequence-based enzyme-family inference.


### Important caveats

- The reviewer-only annotations support the key but do not all represent direct experimental evidence for xylan hydrolysis by this exact protein.
- The sequence-based family inference is probabilistic rather than a direct demonstration of catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic segment consistent with secretion, followed by a compact, aromatic-rich domain consistent with a fungal glycoside hydrolase/xylanase rather than a dehydrogenase. Transferable family knowledge about secreted fungal xylanases makes xylan hydrolysis (C) a credible inference. That reaction is hydrolysis, distinguishing C from the nonhydrolytic lyase activity in A; tau binding (B) and D-lactate dehydrogenase activity (D) fit the sequence context and likely enzyme family poorly.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of fungal secreted glycoside hydrolases provide a meaningful basis for choosing C among these alternatives. The inference is not certain from sequence alone, but it does not require knowing this exact protein's database annotation."
  },
  "case_id": "GO_molecular_function_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as an endo-1,4-beta-xylanase and specifies hydrolysis of beta-xylosidic linkages in xylans. The annotation is qualified: the catalytic-activity assignment is based on a PROSITE rule, and the function comment includes transfer by similarity; the cited paper evidence concerns immunity-inducing activity. Thus the key is scientifically supported, though these excerpts do not establish a direct experimental assay of this protein's catalysis."
  },
  "important_caveats": [
    "The reviewer-only annotations support the key but do not all represent direct experimental evidence for xylan hydrolysis by this exact protein.",
    "The sequence-based family inference is probabilistic rather than a direct demonstration of catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered catalytic alternatives distinguish hydrolysis of xylan from lyase and dehydrogenase reactions, while tau protein binding is not a comparable fit to the sequence-based enzyme-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as an endo-1,4-beta-xylanase and specifies hydrolysis of beta-xylosidic linkages in xylans. The annotation is qualified: the catalytic-activity assignment is based on a PROSITE rule, and the function comment includes transfer by similarity; the cited paper evidence concerns immunity-inducing activity. Thus the key is scientifically supported, though these excerpts do not establish a direct experimental assay of this protein's catalysis.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic segment consistent with secretion, followed by a compact, aromatic-rich domain consistent with a fungal glycoside hydrolase/xylanase rather than a dehydrogenase. Transferable family knowledge about secreted fungal xylanases makes xylan hydrolysis (C) a credible inference. That reaction is hydrolysis, distinguishing C from the nonhydrolytic lyase activity in A; tau binding (B) and D-lactate dehydrogenase activity (D) fit the sequence context and likely enzyme family poorly.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of fungal secreted glycoside hydrolases provide a meaningful basis for choosing C among these alternatives. The inference is not certain from sequence alone, but it does not require knowing this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered catalytic alternatives distinguish hydrolysis of xylan from lyase and dehydrogenase reactions, while tau protein binding is not a comparable fit to the sequence-based enzyme-family inference."
  },
  "important_caveats": [
    "The reviewer-only annotations support the key but do not all represent direct experimental evidence for xylan hydrolysis by this exact protein.",
    "The sequence-based family inference is probabilistic rather than a direct demonstration of catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G2X8M4 (EIX3_VERDV) is annotated with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The protein is named 'Ethylene-inducing xylanase 3' and the FUNCTION comment describes it as an endo-1,4-beta-xylanase involved in hydrolysis of xylan. The EC assignment is via PROSITE-ProRule PRU01097 (ECO:0000255, computational/family-based), and the xylanase function is noted 'By similarity' (ECO:0000250|UniProtKB:B3VSG7). The PubMed reference (33205907) documents immunity-inducing activity rather than direct xylanase assay. Nonetheless, the annotation is internally consistent, the sequence matches the benchmark input exactly, and GO:0031176 maps directly to option C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits multiple hallmarks of glycoside hydrolase family 11 (GH11) xylanases, a well-characterized family learned from many homologs (Trichoderma, Bacillus, Streptomyces xylanases): (1) an N-terminal hydrophobic signal peptide (MVCFSSLFVAASAIAGVFA) indicating a secreted protein; (2) the conserved 'GTHD' motif appearing at least three times (GTHDGYFYS, GTHDGALY, GTHNYQ); (3) the 'NPNG' motif (TYNPNG); (4) the 'TYY'/'TY' aromatic motif (TITYSG, TYYVVENF); (5) a small overall size (~294 aa) typical of GH11 enzymes; (6) a C-terminal cysteine-rich region (CAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL) consistent with a carbohydrate-binding or disulfide-stabilized domain seen in fungal GH11 enzymes. These features are transferable from the broader GH11 family. Against the distractors: (A) lyase activity (EC 4.-.-.-) requires elimination-type active-site chemistry with no hydrolytic architecture; no lyase motifs are present. (B) tau protein binding is a mammalian intracellular protein-protein interaction; a secreted fungal protein with a signal peptide and GH11 motifs cannot plausibly bind tau. (D) D-lactate dehydrogenase (EC 1.1.99.6) requires a Rossmann-fold NAD(P)-binding motif (GXGXXG) and is typically intracellular; no such motif or dehydrogenase architecture is present. The GH11 family pattern recognition meaningfully and credibly distinguishes C from all three alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the GH11 xylanase family signature (GTHD, NPNG, TYY motifs, small secreted fungal protein with cysteine-rich C-terminus) from transferable knowledge of many other GH11 enzymes. The signal peptide eliminates intracellular functions (B, D). The absence of Rossmann-fold motifs eliminates D. The absence of lyase-specific architecture eliminates A. The positive GH11 family evidence points specifically to C. This is legitimate family-level pattern recognition, not memorization of this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GH11 motifs are distinctive and the three distractors (lyase, tau binding, D-lactate dehydrogenase) lack any supporting sequence features. The signal peptide and secreted-protein context further exclude B and D. No alternative option is defensible given the sequence architecture.


### Important caveats

- The EC 3.2.1.8 assignment in UniProt is via PROSITE-ProRule (ECO:0000255), a computational/family-based annotation, not direct experimental measurement of xylanase activity on this specific protein.
- The xylanase function comment includes 'By similarity' (ECO:0000250), meaning the catalytic activity was inferred from a related protein (B3VSG7) rather than assayed directly on EIX3.
- The PubMed reference (33205907) documents immunity-inducing/elicitor activity, not xylanase catalysis per se.
- The GO annotation GO:0031176 carries IEA:UniProtKB-EC evidence, i.e., it is automatically propagated from the EC number, not independently curated.
- The reviewer-only accession G2X8M4 and organism identity (Verticillium dahliae) were not available to the evaluated model; the analysis above relies only on sequence-derived features and general family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits multiple hallmarks of glycoside hydrolase family 11 (GH11) xylanases, a well-characterized family learned from many homologs (Trichoderma, Bacillus, Streptomyces xylanases): (1) an N-terminal hydrophobic signal peptide (MVCFSSLFVAASAIAGVFA) indicating a secreted protein; (2) the conserved 'GTHD' motif appearing at least three times (GTHDGYFYS, GTHDGALY, GTHNYQ); (3) the 'NPNG' motif (TYNPNG); (4) the 'TYY'/'TY' aromatic motif (TITYSG, TYYVVENF); (5) a small overall size (~294 aa) typical of GH11 enzymes; (6) a C-terminal cysteine-rich region (CAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL) consistent with a carbohydrate-binding or disulfide-stabilized domain seen in fungal GH11 enzymes. These features are transferable from the broader GH11 family. Against the distractors: (A) lyase activity (EC 4.-.-.-) requires elimination-type active-site chemistry with no hydrolytic architecture; no lyase motifs are present. (B) tau protein binding is a mammalian intracellular protein-protein interaction; a secreted fungal protein with a signal peptide and GH11 motifs cannot plausibly bind tau. (D) D-lactate dehydrogenase (EC 1.1.99.6) requires a Rossmann-fold NAD(P)-binding motif (GXGXXG) and is typically intracellular; no such motif or dehydrogenase architecture is present. The GH11 family pattern recognition meaningfully and credibly distinguishes C from all three alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the GH11 xylanase family signature (GTHD, NPNG, TYY motifs, small secreted fungal protein with cysteine-rich C-terminus) from transferable knowledge of many other GH11 enzymes. The signal peptide eliminates intracellular functions (B, D). The absence of Rossmann-fold motifs eliminates D. The absence of lyase-specific architecture eliminates A. The positive GH11 family evidence points specifically to C. This is legitimate family-level pattern recognition, not memorization of this exact protein's annotation."
  },
  "case_id": "GO_molecular_function_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H1",
      "H3",
      "H4",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G2X8M4 (EIX3_VERDV) is annotated with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The protein is named 'Ethylene-inducing xylanase 3' and the FUNCTION comment describes it as an endo-1,4-beta-xylanase involved in hydrolysis of xylan. The EC assignment is via PROSITE-ProRule PRU01097 (ECO:0000255, computational/family-based), and the xylanase function is noted 'By similarity' (ECO:0000250|UniProtKB:B3VSG7). The PubMed reference (33205907) documents immunity-inducing activity rather than direct xylanase assay. Nonetheless, the annotation is internally consistent, the sequence matches the benchmark input exactly, and GO:0031176 maps directly to option C."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment in UniProt is via PROSITE-ProRule (ECO:0000255), a computational/family-based annotation, not direct experimental measurement of xylanase activity on this specific protein.",
    "The xylanase function comment includes 'By similarity' (ECO:0000250), meaning the catalytic activity was inferred from a related protein (B3VSG7) rather than assayed directly on EIX3.",
    "The PubMed reference (33205907) documents immunity-inducing/elicitor activity, not xylanase catalysis per se.",
    "The GO annotation GO:0031176 carries IEA:UniProtKB-EC evidence, i.e., it is automatically propagated from the EC number, not independently curated.",
    "The reviewer-only accession G2X8M4 and organism identity (Verticillium dahliae) were not available to the evaluated model; the analysis above relies only on sequence-derived features and general family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH11 motifs are distinctive and the three distractors (lyase, tau binding, D-lactate dehydrogenase) lack any supporting sequence features. The signal peptide and secreted-protein context further exclude B and D. No alternative option is defensible given the sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G2X8M4 (EIX3_VERDV) is annotated with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The protein is named 'Ethylene-inducing xylanase 3' and the FUNCTION comment describes it as an endo-1,4-beta-xylanase involved in hydrolysis of xylan. The EC assignment is via PROSITE-ProRule PRU01097 (ECO:0000255, computational/family-based), and the xylanase function is noted 'By similarity' (ECO:0000250|UniProtKB:B3VSG7). The PubMed reference (33205907) documents immunity-inducing activity rather than direct xylanase assay. Nonetheless, the annotation is internally consistent, the sequence matches the benchmark input exactly, and GO:0031176 maps directly to option C.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H1", "H3", "H4", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits multiple hallmarks of glycoside hydrolase family 11 (GH11) xylanases, a well-characterized family learned from many homologs (Trichoderma, Bacillus, Streptomyces xylanases): (1) an N-terminal hydrophobic signal peptide (MVCFSSLFVAASAIAGVFA) indicating a secreted protein; (2) the conserved 'GTHD' motif appearing at least three times (GTHDGYFYS, GTHDGALY, GTHNYQ); (3) the 'NPNG' motif (TYNPNG); (4) the 'TYY'/'TY' aromatic motif (TITYSG, TYYVVENF); (5) a small overall size (~294 aa) typical of GH11 enzymes; (6) a C-terminal cysteine-rich region (CAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL) consistent with a carbohydrate-binding or disulfide-stabilized domain seen in fungal GH11 enzymes. These features are transferable from the broader GH11 family. Against the distractors: (A) lyase activity (EC 4.-.-.-) requires elimination-type active-site chemistry with no hydrolytic architecture; no lyase motifs are present. (B) tau protein binding is a mammalian intracellular protein-protein interaction; a secreted fungal protein with a signal peptide and GH11 motifs cannot plausibly bind tau. (D) D-lactate dehydrogenase (EC 1.1.99.6) requires a Rossmann-fold NAD(P)-binding motif (GXGXXG) and is typically intracellular; no such motif or dehydrogenase architecture is present. The GH11 family pattern recognition meaningfully and credibly distinguishes C from all three alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the GH11 xylanase family signature (GTHD, NPNG, TYY motifs, small secreted fungal protein with cysteine-rich C-terminus) from transferable knowledge of many other GH11 enzymes. The signal peptide eliminates intracellular functions (B, D). The absence of Rossmann-fold motifs eliminates D. The absence of lyase-specific architecture eliminates A. The positive GH11 family evidence points specifically to C. This is legitimate family-level pattern recognition, not memorization of this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH11 motifs are distinctive and the three distractors (lyase, tau binding, D-lactate dehydrogenase) lack any supporting sequence features. The signal peptide and secreted-protein context further exclude B and D. No alternative option is defensible given the sequence architecture."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment in UniProt is via PROSITE-ProRule (ECO:0000255), a computational/family-based annotation, not direct experimental measurement of xylanase activity on this specific protein.",
    "The xylanase function comment includes 'By similarity' (ECO:0000250), meaning the catalytic activity was inferred from a related protein (B3VSG7) rather than assayed directly on EIX3.",
    "The PubMed reference (33205907) documents immunity-inducing/elicitor activity, not xylanase catalysis per se.",
    "The GO annotation GO:0031176 carries IEA:UniProtKB-EC evidence, i.e., it is automatically propagated from the EC number, not independently curated.",
    "The reviewer-only accession G2X8M4 and organism identity (Verticillium dahliae) were not available to the evaluated model; the analysis above relies only on sequence-derived features and general family knowledge."
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
  "benchmark_sequence_length": 294,
  "benchmark_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "current_entry_audit": {
    "entryVersion": 62,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 294,
  "current_source_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 61,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G2X8M4",
  "selected_historical_entry_version": 61,
  "selected_historical_record_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "selected_historical_source_sequence_length": 294,
  "selected_historical_source_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "selected_historical_version": {
    "accession": "G2X8M4",
    "database": "Swiss-Prot",
    "entryVersion": 61,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX3_VERDV",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G2X8M4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":62,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium wilt\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\",\"taxonId\":498257}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX3\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"B3VSG7\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (By similarity). Exhibits immunity-inducing activity in Nicotiana benthamiana (PubMed:33205907). Can induce strong oxidative burst, activate the expression of defense-related genes, and increase resistance against oomycete and fungal pathogens in N.benthamiana (PubMed:33205907)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030248\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:cellulose binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/16",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031176\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:endo-1,4-beta-xylanase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-EC\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H1",
  "excerpt": "ID   EIX3_VERDV              Reviewed;         294 AA.\nAC   G2X8M4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 61.\nDE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX3 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX3 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_06165;\nOS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\nOS   (Verticillium wilt).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=498257;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a\nCC       major structural heterogeneous polysaccharide found in plant biomass\nCC       representing the second most abundant polysaccharide in the biosphere,\nCC       after cellulose (By similarity). Exhibits immunity-inducing activity in\nCC       Nicotiana benthamiana (PubMed:33205907). Can induce strong oxidative\nCC       burst, activate the expression of defense-related genes, and increase\nCC       resistance against oomycete and fungal pathogens in N.benthamiana\nCC       (PubMed:33205907). {ECO:0000250|UniProtKB:B3VSG7,\nCC       ECO:0000269|PubMed:33205907}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0030248; F:cellulose binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0031176; F:endo-1,4-beta-xylanase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0016829\nname: lyase activity\nnamespace: molecular_function\ndef: \"Catalysis of the cleavage of C-C, C-O, C-N and other bonds by other means than by hydrolysis or oxidation, or conversely adding a group to a double bond. They differ from other enzymes in that two substrates are involved in one reaction direction, but only one in the other direction. When acting on the single substrate, a molecule is eliminated and this generates either a new double bond or a new ring.\" [EC:4.-.-.-]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nxref: EC:4.-.-.-\nxref: Reactome:R-HSA-5696408 \"PXLP-K278-PHYKPL tetramer hydrolyses 5PHL\"\nxref: Reactome:R-HSA-6782895 \"TYW1:FMN:4Fe-4S  transforms 1-methylguanosine yielding yW-187 (4-demethylwyosine) at nucleotide 37 of tRNA(Phe)\"\nis_a: GO:0003824 ! catalytic activity\nproperty_value: skos:exactMatch EC:4.-.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016829",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 130596-130614",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0047809\nname: D-lactate dehydrogenase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: (R)-lactate + A = AH(2) + pyruvate.\" [RHEA:15089]\nsynonym: \"(R)-2-hydroxy-acid:(acceptor) 2-oxidoreductase activity\" RELATED [EC:1.1.99.6]\nsynonym: \"(R)-lactate dehydrogenase activity\" EXACT []\nsynonym: \"2-hydroxy acid dehydrogenase activity\" RELATED [EC:1.1.99.6]\nsynonym: \"D-2-hydroxy-acid dehydrogenase activity\" BROAD []\nxref: EC:1.1.99.6\nxref: KEGG_REACTION:R00297\nxref: MetaCyc:D-2-HYDROXY-ACID-DEHYDROGENASE-RXN\nxref: RHEA:15089\nxref: RHEA:62968\nis_a: GO:0004457 ! lactate dehydrogenase activity\nis_a: GO:0033719 ! (2R)-oxo-acid reductase activity\nproperty_value: skos:exactMatch EC:1.1.99.6\nproperty_value: skos:exactMatch RHEA:15089\nproperty_value: skos:narrowMatch RHEA:62968\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0047809",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 296518-296537",
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
  "excerpt": "[Term]\nid: GO:0048156\nname: tau protein binding\nnamespace: molecular_function\ndef: \"Binding to tau protein. tau is a microtubule-associated protein, implicated in Alzheimer's disease, Down Syndrome and ALS.\" [GOC:jid]\nis_a: GO:0008092 ! cytoskeletal protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0048156",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 300902-300908",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
