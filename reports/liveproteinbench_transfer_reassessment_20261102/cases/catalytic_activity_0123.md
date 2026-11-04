# catalytic_activity_0123

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0123.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — Hydrolysis of (1-&gt;4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.

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
A. Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.
B. (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O
C. 5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O
D. UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)
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

> The exact sequence matches a UniProt entry annotating the option A reaction as catalytic activity with experimental evidence (ECO:0000269), and the historical entry contains the same annotation. The primary study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is compatible with a fungal GH43-like glycoside hydrolase, a family that includes beta-xylosidases; transferable family recognition therefore favors the xylan hydrolysis in A. The other options describe substantially different enzyme activities and reaction classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference provides a meaningful basis for choosing A without relying on the exact protein's database record. The inference is not a guarantee of substrate specificity, but the alternatives are distinct enough that it supports the choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A matches the supported beta-xylosidase activity among the offered reactions.


### Important caveats

- The protein is also annotated with alpha-L-arabinofuranosidase activity, but that reaction is not among the options.
- The cited experimental evidence is represented here through database annotations; the underlying study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a fungal GH43-like glycoside hydrolase, a family that includes beta-xylosidases; transferable family recognition therefore favors the xylan hydrolysis in A. The other options describe substantially different enzyme activities and reaction classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing A without relying on the exact protein's database record. The inference is not a guarantee of substrate specificity, but the alternatives are distinct enough that it supports the choice."
  },
  "case_id": "catalytic_activity_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating the option A reaction as catalytic activity with experimental evidence (ECO:0000269), and the historical entry contains the same annotation. The primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The protein is also annotated with alpha-L-arabinofuranosidase activity, but that reaction is not among the options.",
    "The cited experimental evidence is represented here through database annotations; the underlying study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the supported beta-xylosidase activity among the offered reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating the option A reaction as catalytic activity with experimental evidence (ECO:0000269), and the historical entry contains the same annotation. The primary study was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is compatible with a fungal GH43-like glycoside hydrolase, a family that includes beta-xylosidases; transferable family recognition therefore favors the xylan hydrolysis in A. The other options describe substantially different enzyme activities and reaction classes.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing A without relying on the exact protein's database record. The inference is not a guarantee of substrate specificity, but the alternatives are distinct enough that it supports the choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the supported beta-xylosidase activity among the offered reactions."
  },
  "important_caveats": [
    "The protein is also annotated with alpha-L-arabinofuranosidase activity, but that reaction is not among the options.",
    "The cited experimental evidence is represented here through database annotations; the underlying study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry V9TT49 (sequence matched, 538 aa) records EC 3.2.1.37 with the exact catalytic activity text in option A: 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.' This is annotated with experimental evidence (ECO:0000269, PubMed:24262572). The protein is bifunctional (also EC 3.2.1.55, arabinofuranosidase), but option A correctly describes one of its experimentally verified activities.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark GH43 (Glycoside Hydrolase family 43) motifs: the conserved 'DPP' motif (DPSLFHDDDGRKW), the 'GTDL' and 'GPHLY' motifs (GPRKNIFTGTDLALVEGPHLY), and the overall ~538-aa fungal architecture. GH43 is a well-characterized family of glycoside hydrolases that hydrolyze glycosidic bonds in xylan/arabinose substrates. Among the four options, only A describes a glycoside hydrolase reaction (hydrolysis of a β-1,4-xylan bond). Option B is a lipoxygenase-type oxidation of a fatty acid hydroperoxide; C is a phosphatase/transferase reaction in PRPP metabolism; D is an NAD-dependent oxidoreductase reaction. A model recognizing the GH43 family from sequence motifs would know the family catalyzes glycosidic bond hydrolysis on xylan/arabinose polymers, immediately eliminating B, C, and D as mechanistically incompatible enzyme classes. The selection of A over an arabinofuranosidase option is not needed because no such option is offered.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of GH43 family motifs (DPP, GTDL, GPHLY) is transferable knowledge from the broader protein family. Family-level knowledge that GH43 members are glycoside hydrolases acting on xylan/arabinose substrates meaningfully distinguishes option A (glycosidic bond hydrolysis) from B (oxidation), C (phosphatase/transferase), and D (oxidoreductase). No target-specific database lookup is required to eliminate the three mechanistically unrelated alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55), only the xylosidase activity (A) is offered among the choices. The other three options belong to entirely different enzyme classes (oxidation, phosphatase/transferase, oxidoreductase) and cannot be defended for a glycoside hydrolase. No ambiguity exists among the offered alternatives.


### Important caveats

- The protein is bifunctional (beta-xylosidase EC 3.2.1.37 AND alpha-L-arabinofuranosidase EC 3.2.1.55). The question presents only one of its two activities as the correct answer, which is acceptable since the other activity is not offered as a distractor.
- The GH43 family identification from sequence motifs is probabilistic; a model would rely on learned family signatures rather than a single guaranteed motif match.
- The UniProt annotation is Swiss-Prot reviewed with experimental evidence (PubMed:24262572), lending strong support to the expected answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark GH43 (Glycoside Hydrolase family 43) motifs: the conserved 'DPP' motif (DPSLFHDDDGRKW), the 'GTDL' and 'GPHLY' motifs (GPRKNIFTGTDLALVEGPHLY), and the overall ~538-aa fungal architecture. GH43 is a well-characterized family of glycoside hydrolases that hydrolyze glycosidic bonds in xylan/arabinose substrates. Among the four options, only A describes a glycoside hydrolase reaction (hydrolysis of a β-1,4-xylan bond). Option B is a lipoxygenase-type oxidation of a fatty acid hydroperoxide; C is a phosphatase/transferase reaction in PRPP metabolism; D is an NAD-dependent oxidoreductase reaction. A model recognizing the GH43 family from sequence motifs would know the family catalyzes glycosidic bond hydrolysis on xylan/arabinose polymers, immediately eliminating B, C, and D as mechanistically incompatible enzyme classes. The selection of A over an arabinofuranosidase option is not needed because no such option is offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of GH43 family motifs (DPP, GTDL, GPHLY) is transferable knowledge from the broader protein family. Family-level knowledge that GH43 members are glycoside hydrolases acting on xylan/arabinose substrates meaningfully distinguishes option A (glycosidic bond hydrolysis) from B (oxidation), C (phosphatase/transferase), and D (oxidoreductase). No target-specific database lookup is required to eliminate the three mechanistically unrelated alternatives."
  },
  "case_id": "catalytic_activity_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry V9TT49 (sequence matched, 538 aa) records EC 3.2.1.37 with the exact catalytic activity text in option A: 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.' This is annotated with experimental evidence (ECO:0000269, PubMed:24262572). The protein is bifunctional (also EC 3.2.1.55, arabinofuranosidase), but option A correctly describes one of its experimentally verified activities."
  },
  "important_caveats": [
    "The protein is bifunctional (beta-xylosidase EC 3.2.1.37 AND alpha-L-arabinofuranosidase EC 3.2.1.55). The question presents only one of its two activities as the correct answer, which is acceptable since the other activity is not offered as a distractor.",
    "The GH43 family identification from sequence motifs is probabilistic; a model would rely on learned family signatures rather than a single guaranteed motif match.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence (PubMed:24262572), lending strong support to the expected answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55), only the xylosidase activity (A) is offered among the choices. The other three options belong to entirely different enzyme classes (oxidation, phosphatase/transferase, oxidoreductase) and cannot be defended for a glycoside hydrolase. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry V9TT49 (sequence matched, 538 aa) records EC 3.2.1.37 with the exact catalytic activity text in option A: 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.' This is annotated with experimental evidence (ECO:0000269, PubMed:24262572). The protein is bifunctional (also EC 3.2.1.55, arabinofuranosidase), but option A correctly describes one of its experimentally verified activities.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark GH43 (Glycoside Hydrolase family 43) motifs: the conserved 'DPP' motif (DPSLFHDDDGRKW), the 'GTDL' and 'GPHLY' motifs (GPRKNIFTGTDLALVEGPHLY), and the overall ~538-aa fungal architecture. GH43 is a well-characterized family of glycoside hydrolases that hydrolyze glycosidic bonds in xylan/arabinose substrates. Among the four options, only A describes a glycoside hydrolase reaction (hydrolysis of a β-1,4-xylan bond). Option B is a lipoxygenase-type oxidation of a fatty acid hydroperoxide; C is a phosphatase/transferase reaction in PRPP metabolism; D is an NAD-dependent oxidoreductase reaction. A model recognizing the GH43 family from sequence motifs would know the family catalyzes glycosidic bond hydrolysis on xylan/arabinose polymers, immediately eliminating B, C, and D as mechanistically incompatible enzyme classes. The selection of A over an arabinofuranosidase option is not needed because no such option is offered.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of GH43 family motifs (DPP, GTDL, GPHLY) is transferable knowledge from the broader protein family. Family-level knowledge that GH43 members are glycoside hydrolases acting on xylan/arabinose substrates meaningfully distinguishes option A (glycosidic bond hydrolysis) from B (oxidation), C (phosphatase/transferase), and D (oxidoreductase). No target-specific database lookup is required to eliminate the three mechanistically unrelated alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55), only the xylosidase activity (A) is offered among the choices. The other three options belong to entirely different enzyme classes (oxidation, phosphatase/transferase, oxidoreductase) and cannot be defended for a glycoside hydrolase. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The protein is bifunctional (beta-xylosidase EC 3.2.1.37 AND alpha-L-arabinofuranosidase EC 3.2.1.55). The question presents only one of its two activities as the correct answer, which is acceptable since the other activity is not offered as a distractor.",
    "The GH43 family identification from sequence motifs is probabilistic; a model would rely on learned family signatures rather than a single guaranteed motif match.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence (PubMed:24262572), lending strong support to the expected answer."
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

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C6",
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

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C7",
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
  "excerpt": "DE   RecName: Full=Xylosidase/arabinosidase 43B {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};\nDE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};\nDE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};\nDE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-15",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 123. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
