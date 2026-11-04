# GO_molecular_function_0105

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0105.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — xylan 1,4-beta-xylosidase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPQVRNPILPGFNPDPSILRVGEDYYIATSTFEWYPGVQIHHSRDLANWELVARPLNRKSQLDMRGNPDSCGIWAPCLSHDGERFWLVYTDVKRKDGSFKDTPNYIVTAEKIEGPWSDPIYINSSGFDPSLFHDDDGRKWFVNMLWDHRRRPQLFEGIVLQEFDPKAGKLVGPRKNIFTGTDLALVEGPHLYKRNGWYYLLTAEGGTGYEHACTFARSRNIWGPYEVHPQKYILTSKDHPHAALQRAGHGDIVDTPDGRTYLVHLTGRPTTQFRRCVLGRETAIQEAYWGDDDWLYVKNGPVPSLWVDLPAARDDTKYWEEKRYTFESGLHKDFQWLRTPETDRIFRTREDGKLTLIGRESIGSWFEQALVARRQTHFSCDAETVIDFSPEDQRQFAGLTAYYCRYNFFYLAVSAHSDGQRELFIMASEASWPLGELRYPVPEGVRIPNEGKVRLALTIRGRELQFYYALEGEELKKIGPVLDASIVSDECGGHQKHGSFTGAFVGVAASDLNGTAAEATFDYFIYRPVQHPSDRYEI

[Multiple Choices]
A. chromatin insulator sequence binding
B. nucleotidyltransferase activity
C. enzyme activator activity
D. xylan 1,4-beta-xylosidase activity
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

> Evidence for the sequence-matched protein describes beta-xylosidase activity and the corresponding xylan-hydrolysis reaction. The cited experimental characterization reports its greatest activity on a beta-D-xylopyranoside substrate, supporting option D.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 538-residue sequence is a globular, enzyme-like protein with acidic catalytic-region patterns compatible with a carbohydrate hydrolase. Transferable recognition of GH43 glycosidase sequence patterns provides a plausible route to a beta-xylosidase inference; among these choices, D fits, whereas the other options describe DNA binding, nucleotide-group transfer, or regulation of another enzyme.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference can meaningfully favor D over these dissimilar alternatives without knowing this protein's recorded annotation. The sequence alone may not establish the precise substrate specificity or relative activities, so this is a probabilistic inference rather than an independent experimental determination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is reported to have more than one activity, but beta-xylosidase activity is supported and no other offered option describes the reported second activity.


### Important caveats

- The experimental evidence also describes alpha-L-arabinofuranosidase activity and low xylanase activity; it reports the strongest activity on a beta-xyloside substrate.
- The reviewer-only source matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 538-residue sequence is a globular, enzyme-like protein with acidic catalytic-region patterns compatible with a carbohydrate hydrolase. Transferable recognition of GH43 glycosidase sequence patterns provides a plausible route to a beta-xylosidase inference; among these choices, D fits, whereas the other options describe DNA binding, nucleotide-group transfer, or regulation of another enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can meaningfully favor D over these dissimilar alternatives without knowing this protein's recorded annotation. The sequence alone may not establish the precise substrate specificity or relative activities, so this is a probabilistic inference rather than an independent experimental determination."
  },
  "case_id": "GO_molecular_function_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "Evidence for the sequence-matched protein describes beta-xylosidase activity and the corresponding xylan-hydrolysis reaction. The cited experimental characterization reports its greatest activity on a beta-D-xylopyranoside substrate, supporting option D."
  },
  "important_caveats": [
    "The experimental evidence also describes alpha-L-arabinofuranosidase activity and low xylanase activity; it reports the strongest activity on a beta-xyloside substrate.",
    "The reviewer-only source matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is reported to have more than one activity, but beta-xylosidase activity is supported and no other offered option describes the reported second activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Evidence for the sequence-matched protein describes beta-xylosidase activity and the corresponding xylan-hydrolysis reaction. The cited experimental characterization reports its greatest activity on a beta-D-xylopyranoside substrate, supporting option D.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 538-residue sequence is a globular, enzyme-like protein with acidic catalytic-region patterns compatible with a carbohydrate hydrolase. Transferable recognition of GH43 glycosidase sequence patterns provides a plausible route to a beta-xylosidase inference; among these choices, D fits, whereas the other options describe DNA binding, nucleotide-group transfer, or regulation of another enzyme.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can meaningfully favor D over these dissimilar alternatives without knowing this protein's recorded annotation. The sequence alone may not establish the precise substrate specificity or relative activities, so this is a probabilistic inference rather than an independent experimental determination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is reported to have more than one activity, but beta-xylosidase activity is supported and no other offered option describes the reported second activity."
  },
  "important_caveats": [
    "The experimental evidence also describes alpha-L-arabinofuranosidase activity and low xylanase activity; it reports the strongest activity on a beta-xyloside substrate.",
    "The reviewer-only source matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry V9TT49 (sequence matched) is annotated with GO:0009044 'xylan 1,4-beta-xylosidase activity' with EXP:UniProtKB evidence code (ECO:0000269, PubMed:24262572). The protein is characterized experimentally as a bifunctional beta-xylosidase/alpha-L-arabinosidase (EC 3.2.1.37 and EC 3.2.1.55), with beta-xylosidase being the primary activity (100% relative activity on pNPX). The catalytic activity comment confirms hydrolysis of (1->4)-beta-D-xylans to remove D-xylose residues from non-reducing termini, matching GO:0009044 definition exactly.

Citations as saved: [C9](#evidence-c9), [C6](#evidence-c6), [C5](#evidence-c5), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~538 aa) exhibits features consistent with Glycoside Hydrolase family 43 (GH43): (1) multiple 'G'-rich loop regions forming a five-bladed beta-propeller architecture (e.g., 'GPRKNIFTGTDLALVEGPHLYKRNGWYYLL', 'GTVHLTGRPTTQ'); (2) conserved catalytic Asp and Glu residues in the 'TGTDLALVEGPHLY' motif typical of GH43 nucleophile/acid-base pairs; (3) overall length and amino acid composition (aromatic-rich, moderate hydrophobicity) consistent with secreted fungal glycoside hydrolases. Against the distractors: (A) chromatin insulator binding requires DNA-binding domains (zinc fingers, HTH) entirely absent here; (B) nucleotidyltransferase activity requires transferase-specific motifs (e.g., GDD, nucleotidyltransferase fold) not present; (C) enzyme activator activity implies protein-protein interaction regulatory domains, inconsistent with the catalytic architecture shown. Recognizing the protein as a glycoside hydrolase from beta-propeller-like sequence patterns and catalytic residue conservation (transferable from many characterized GH43 homologs like those from Aspergillus, Trichoderma, and bacterial GH43 enzymes) uniquely selects D, the only glycoside hydrolase option among the four choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of GH43 family architecture (five-bladed beta-propeller, conserved Asp/Glu catalytic pair, ~400-600 aa length) and general protein classification (DNA-binding domains for insulators, transferase motifs for nucleotidyltransferases, PPI domains for activators) can meaningfully eliminate A, B, and C and identify D as the glycoside hydrolase option. The sequence patterns are consistent with GH43 and with glycoside hydrolases broadly, and D is the only glycoside hydrolase among the four choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is bifunctional (beta-xylosidase and alpha-L-arabinofuranosidase), only D (xylan 1,4-beta-xylosidase activity) appears among the choices. The other three options (chromatin insulator binding, nucleotidyltransferase, enzyme activator) represent entirely different molecular function classes and are not plausible for a glycoside hydrolase sequence. No ambiguity exists among the offered alternatives.


### Important caveats

- The protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55); the alpha-L-arabinofuranosidase activity is not offered as a distractor, so the question does not test discrimination between the two activities.
- GH43 family recognition from sequence alone is probabilistic; the model relies on pattern matching to known family members rather than de novo structural prediction.
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning argument uses only the sequence and general GH43/glycoside hydrolase family knowledge.
- The sequence is 538 aa and matches the canonical UniProt entry V9TT49 exactly (SHA256 confirmed).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~538 aa) exhibits features consistent with Glycoside Hydrolase family 43 (GH43): (1) multiple 'G'-rich loop regions forming a five-bladed beta-propeller architecture (e.g., 'GPRKNIFTGTDLALVEGPHLYKRNGWYYLL', 'GTVHLTGRPTTQ'); (2) conserved catalytic Asp and Glu residues in the 'TGTDLALVEGPHLY' motif typical of GH43 nucleophile/acid-base pairs; (3) overall length and amino acid composition (aromatic-rich, moderate hydrophobicity) consistent with secreted fungal glycoside hydrolases. Against the distractors: (A) chromatin insulator binding requires DNA-binding domains (zinc fingers, HTH) entirely absent here; (B) nucleotidyltransferase activity requires transferase-specific motifs (e.g., GDD, nucleotidyltransferase fold) not present; (C) enzyme activator activity implies protein-protein interaction regulatory domains, inconsistent with the catalytic architecture shown. Recognizing the protein as a glycoside hydrolase from beta-propeller-like sequence patterns and catalytic residue conservation (transferable from many characterized GH43 homologs like those from Aspergillus, Trichoderma, and bacterial GH43 enzymes) uniquely selects D, the only glycoside hydrolase option among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of GH43 family architecture (five-bladed beta-propeller, conserved Asp/Glu catalytic pair, ~400-600 aa length) and general protein classification (DNA-binding domains for insulators, transferase motifs for nucleotidyltransferases, PPI domains for activators) can meaningfully eliminate A, B, and C and identify D as the glycoside hydrolase option. The sequence patterns are consistent with GH43 and with glycoside hydrolases broadly, and D is the only glycoside hydrolase among the four choices."
  },
  "case_id": "GO_molecular_function_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C9",
      "C6",
      "C5",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry V9TT49 (sequence matched) is annotated with GO:0009044 'xylan 1,4-beta-xylosidase activity' with EXP:UniProtKB evidence code (ECO:0000269, PubMed:24262572). The protein is characterized experimentally as a bifunctional beta-xylosidase/alpha-L-arabinosidase (EC 3.2.1.37 and EC 3.2.1.55), with beta-xylosidase being the primary activity (100% relative activity on pNPX). The catalytic activity comment confirms hydrolysis of (1->4)-beta-D-xylans to remove D-xylose residues from non-reducing termini, matching GO:0009044 definition exactly."
  },
  "important_caveats": [
    "The protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55); the alpha-L-arabinofuranosidase activity is not offered as a distractor, so the question does not test discrimination between the two activities.",
    "GH43 family recognition from sequence alone is probabilistic; the model relies on pattern matching to known family members rather than de novo structural prediction.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning argument uses only the sequence and general GH43/glycoside hydrolase family knowledge.",
    "The sequence is 538 aa and matches the canonical UniProt entry V9TT49 exactly (SHA256 confirmed)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (beta-xylosidase and alpha-L-arabinofuranosidase), only D (xylan 1,4-beta-xylosidase activity) appears among the choices. The other three options (chromatin insulator binding, nucleotidyltransferase, enzyme activator) represent entirely different molecular function classes and are not plausible for a glycoside hydrolase sequence. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry V9TT49 (sequence matched) is annotated with GO:0009044 'xylan 1,4-beta-xylosidase activity' with EXP:UniProtKB evidence code (ECO:0000269, PubMed:24262572). The protein is characterized experimentally as a bifunctional beta-xylosidase/alpha-L-arabinosidase (EC 3.2.1.37 and EC 3.2.1.55), with beta-xylosidase being the primary activity (100% relative activity on pNPX). The catalytic activity comment confirms hydrolysis of (1->4)-beta-D-xylans to remove D-xylose residues from non-reducing termini, matching GO:0009044 definition exactly.",
    "evidence_ids": ["C9", "C6", "C5", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~538 aa) exhibits features consistent with Glycoside Hydrolase family 43 (GH43): (1) multiple 'G'-rich loop regions forming a five-bladed beta-propeller architecture (e.g., 'GPRKNIFTGTDLALVEGPHLYKRNGWYYLL', 'GTVHLTGRPTTQ'); (2) conserved catalytic Asp and Glu residues in the 'TGTDLALVEGPHLY' motif typical of GH43 nucleophile/acid-base pairs; (3) overall length and amino acid composition (aromatic-rich, moderate hydrophobicity) consistent with secreted fungal glycoside hydrolases. Against the distractors: (A) chromatin insulator binding requires DNA-binding domains (zinc fingers, HTH) entirely absent here; (B) nucleotidyltransferase activity requires transferase-specific motifs (e.g., GDD, nucleotidyltransferase fold) not present; (C) enzyme activator activity implies protein-protein interaction regulatory domains, inconsistent with the catalytic architecture shown. Recognizing the protein as a glycoside hydrolase from beta-propeller-like sequence patterns and catalytic residue conservation (transferable from many characterized GH43 homologs like those from Aspergillus, Trichoderma, and bacterial GH43 enzymes) uniquely selects D, the only glycoside hydrolase option among the four choices.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of GH43 family architecture (five-bladed beta-propeller, conserved Asp/Glu catalytic pair, ~400-600 aa length) and general protein classification (DNA-binding domains for insulators, transferase motifs for nucleotidyltransferases, PPI domains for activators) can meaningfully eliminate A, B, and C and identify D as the glycoside hydrolase option. The sequence patterns are consistent with GH43 and with glycoside hydrolases broadly, and D is the only glycoside hydrolase among the four choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (beta-xylosidase and alpha-L-arabinofuranosidase), only D (xylan 1,4-beta-xylosidase activity) appears among the choices. The other three options (chromatin insulator binding, nucleotidyltransferase, enzyme activator) represent entirely different molecular function classes and are not plausible for a glycoside hydrolase sequence. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55); the alpha-L-arabinofuranosidase activity is not offered as a distractor, so the question does not test discrimination between the two activities.",
    "GH43 family recognition from sequence alone is probabilistic; the model relies on pattern matching to known family members rather than de novo structural prediction.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning argument uses only the sequence and general GH43/glycoside hydrolase family knowledge.",
    "The sequence is 538 aa and matches the canonical UniProt entry V9TT49 exactly (SHA256 confirmed)."
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
  "benchmark_sequence_length": 538,
  "benchmark_sequence_sha256": "4c5f6ce116665066820aa85f61aa5d53cbd37564158534eb94cfe0b3bdb23c65",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 538,
  "current_source_sequence_sha256": "4c5f6ce116665066820aa85f61aa5d53cbd37564158534eb94cfe0b3bdb23c65",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "V9TT49",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "selected_historical_source_sequence_length": 538,
  "selected_historical_source_sequence_sha256": "4c5f6ce116665066820aa85f61aa5d53cbd37564158534eb94cfe0b3bdb23c65",
  "selected_historical_version": {
    "accession": "V9TT49",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XY43B_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"V9TT49\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"includes\":[{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"1,4-beta-D-xylan xylohydrolase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Xylan 1,4-beta-xylosidase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.37\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Beta-xylosidase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.55\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Alpha-L-arabinofuranosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Arabinosidase\"}]}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Xylosidase/arabinosidase 43B\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional beta-xylosidase/alpha-L-arabinosidases with a low level of xylanase activity (PubMed:24262572). Is most active on 4-nitrophenyl beta-D-xylopyranoside (pNPX) (defined as 100%), moderate on p-nitrophenyl-alpha-L-arabinofuranoside (pNPA) (56.6%), and weak on beechwood xylan (5.7%) and birchwood xylan (2.7%) (PubMed:24262572). Is able to attack xylooligosacchardies with degrees of polymerization of 2-5, releasing the amounts of reducing sugars in the order of xylopentose > xylotetraose > xylotriose > xylobiose, i.e. the rate of xylose released from xylooligosacchardies increased with the chain length (PubMed:24262572). No activity was detected in the presence of carboxymethyl cellulose-sodium (CMC-Na), sugar beet arabinan, AZCL-arabinan (debranched), 4-nitrophenyl a-D - galactopyranoside, 2-nitrophenyl beta-D-galactopyranoside, and 4-nitrophenyl alpha-D-glucopyranoside (PubMed:24262572)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.37\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.55\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"id\":\"GO:0046556\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:alpha-L-arabinofuranosidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"id\":\"GO:0009044\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:xylan 1,4-beta-xylosidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.\",\"Shi P.\",\"Huang H.\",\"Luo H.\",\"Wang Y.\",\"Zhang W.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24262572\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.foodchem.2013.10.062\"}],\"citationType\":\"journal article\",\"firstPage\":\"381\",\"id\":\"24262572\",\"journal\":\"Food Chem.\",\"lastPage\":\"387\",\"publicationDate\":\"2014\",\"title\":\"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and one GH11 xylanase from Humicola insolens and their synergy in the degradation of xylan.\",\"volume\":\"148\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   XY43B_HUMIN             Reviewed;         538 AA.\nAC   V9TT49;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Xylosidase/arabinosidase 43B {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};\nDE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};\nDE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};\nDE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};\nGN   Name=Xyl43B {ECO:0000303|PubMed:24262572};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "url": "https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   SUBCELLULAR LOCATION, AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=24262572; DOI=10.1016/j.foodchem.2013.10.062;\nRA   Yang X., Shi P., Huang H., Luo H., Wang Y., Zhang W., Yao B.;\nRT   \"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and\nRT   one GH11 xylanase from Humicola insolens and their synergy in the\nRT   degradation of xylan.\";\nRL   Food Chem. 148:381-387(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "url": "https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Bifunctional beta-xylosidase/alpha-L-arabinosidases with a\nCC       low level of xylanase activity (PubMed:24262572). Is most active on 4-\nCC       nitrophenyl beta-D-xylopyranoside (pNPX) (defined as 100%), moderate on\nCC       p-nitrophenyl-alpha-L-arabinofuranoside (pNPA) (56.6%), and weak on\nCC       beechwood xylan (5.7%) and birchwood xylan (2.7%) (PubMed:24262572). Is\nCC       able to attack xylooligosacchardies with degrees of polymerisation of\nCC       2-5, releasing the amounts of reducing sugars in the order of\nCC       xylopentose > xylotetraose > xylotriose > xylobiose, i.e. the rate of\nCC       xylose released from xylooligosacchardies increased with the chain\nCC       length (PubMed:24262572). No activity was detected in the presence of\nCC       carboxymethyl cellulose-sodium (CMC-Na), sugar beet arabinan, AZCL-\nCC       arabinan (debranched), 4-nitrophenyl a-D - galactopyranoside, 2-\nCC       nitrophenyl beta-D-galactopyranoside, and 4-nitrophenyl alpha-D-\nCC       glucopyranoside (PubMed:24262572). {ECO:0000269|PubMed:24262572}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "url": "https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-\nCC         xylose residues from the non-reducing termini.; EC=3.2.1.37;\nCC         Evidence={ECO:0000269|PubMed:24262572};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "url": "https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside\nCC         residues in alpha-L-arabinosides.; EC=3.2.1.55;\nCC         Evidence={ECO:0000269|PubMed:24262572};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "url": "https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0046556; F:alpha-L-arabinofuranosidase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "url": "https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0009044; F:xylan 1,4-beta-xylosidase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "url": "https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0008047\nname: enzyme activator activity\nnamespace: molecular_function\nalt_id: GO:0010577\ndef: \"A molecular function regulator that increases a catalytic activity.\" [GOC:pdt]\ncomment: This term should only be used in cases when the regulator directly interacts with the enzyme, but does not result in a covalent modification.\nsynonym: \"metalloenzyme activator activity\" NARROW []\nxref: Reactome:R-HSA-9948070 \"POMGNT1 catalyzes FKRP:FKTN:RXYLT1 formation\"\nis_a: GO:0030234 ! enzyme regulator activity\nis_a: GO:0140677 ! molecular function activator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008047",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 78691-78702",
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
  "excerpt": "[Term]\nid: GO:0009044\nname: xylan 1,4-beta-xylosidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of (1->4)-beta-D-xylans so as to remove successive D-xylose residues from the non-reducing termini.\" [EC:3.2.1.37]\nsynonym: \"1,4-beta-D-xylan xylohydrolase activity\" RELATED [EC:3.2.1.37]\nsynonym: \"beta-D-xylopyranosidase activity\" RELATED [EC:3.2.1.37]\nsynonym: \"beta-xylosidase activity\" RELATED [EC:3.2.1.37]\nsynonym: \"exo-1,4-beta-D-xylosidase activity\" RELATED [EC:3.2.1.37]\nsynonym: \"exo-1,4-beta-xylosidase activity\" RELATED [EC:3.2.1.37]\nsynonym: \"exo-1,4-xylosidase activity\" RELATED [EC:3.2.1.37]\nsynonym: \"xylobiase activity\" RELATED [EC:3.2.1.37]\nxref: EC:3.2.1.37\nxref: MetaCyc:3.2.1.37-RXN\nis_a: GO:0097599 ! xylanase activity\nproperty_value: skos:exactMatch EC:3.2.1.37\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009044",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 92065-92081",
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
  "excerpt": "[Term]\nid: GO:0016779\nname: nucleotidyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a nucleotidyl group from one compound (donor) to another (acceptor).\" [EC:2.7.7.-]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_metagenomics\nsubset: goslim_yeast\nxref: EC:2.7.7.-\nxref: Reactome:R-HSA-6782434 \"THG1L transfers GMP to 5' end of tRNA(His)\"\nis_a: GO:0016772 ! transferase activity, transferring phosphorus-containing groups\nproperty_value: skos:exactMatch EC:2.7.7.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016779",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 130076-130090",
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
  "excerpt": "[Term]\nid: GO:0043035\nname: chromatin insulator sequence binding\nnamespace: molecular_function\ndef: \"Binding to a chromatin insulator sequence, a DNA sequence that prevents enhancer-mediated activation or repression of transcription.\" [GOC:jl, PMID:12783795]\nis_a: GO:0031490 ! chromatin DNA binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043035",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 243359-243365",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 105. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
