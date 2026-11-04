# EC_number_0123

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0123.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.1.37

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
A. 3.2.1.37
B. 3.2.1.18
C. 2.7.8.7
D. 1.5.1.38
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

> The sequence-matched UniProt entry assigns EC 3.2.1.37 and describes the corresponding xylan-hydrolysis reaction, citing experimental evidence (ECO:0000269). The protein is also annotated with an additional EC activity, but that number is not among the choices.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a fungal GH43 glycoside hydrolase. Transferable knowledge of this family supports pentose-directed glycosidase activity, including beta-xylosidases; among the choices, EC 3.2.1.37 is the matching xylan-degrading activity. The other options describe distinct enzyme activities, including cellulose hydrolysis or unrelated reaction classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence features and the offered alternatives meaningfully favors beta-xylosidase without needing the exact protein's database record. The inference is not a guarantee of substrate specificity, and the protein may have other activities, but those do not prevent distinguishing the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein has an additional annotated arabinosidase activity, but its EC number is not offered; among the listed options, only A is supported.


### Important caveats

- The evidence is a database annotation citing experimental evidence, not an independent review of the cited study.
- Reviewer-only sequence matching establishes applicability of the annotation; that identity information was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a fungal GH43 glycoside hydrolase. Transferable knowledge of this family supports pentose-directed glycosidase activity, including beta-xylosidases; among the choices, EC 3.2.1.37 is the matching xylan-degrading activity. The other options describe distinct enzyme activities, including cellulose hydrolysis or unrelated reaction classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features and the offered alternatives meaningfully favors beta-xylosidase without needing the exact protein's database record. The inference is not a guarantee of substrate specificity, and the protein may have other activities, but those do not prevent distinguishing the offered choices."
  },
  "case_id": "EC_number_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.2.1.37 and describes the corresponding xylan-hydrolysis reaction, citing experimental evidence (ECO:0000269). The protein is also annotated with an additional EC activity, but that number is not among the choices."
  },
  "important_caveats": [
    "The evidence is a database annotation citing experimental evidence, not an independent review of the cited study.",
    "Reviewer-only sequence matching establishes applicability of the annotation; that identity information was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has an additional annotated arabinosidase activity, but its EC number is not offered; among the listed options, only A is supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.2.1.37 and describes the corresponding xylan-hydrolysis reaction, citing experimental evidence (ECO:0000269). The protein is also annotated with an additional EC activity, but that number is not among the choices.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a fungal GH43 glycoside hydrolase. Transferable knowledge of this family supports pentose-directed glycosidase activity, including beta-xylosidases; among the choices, EC 3.2.1.37 is the matching xylan-degrading activity. The other options describe distinct enzyme activities, including cellulose hydrolysis or unrelated reaction classes.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features and the offered alternatives meaningfully favors beta-xylosidase without needing the exact protein's database record. The inference is not a guarantee of substrate specificity, and the protein may have other activities, but those do not prevent distinguishing the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has an additional annotated arabinosidase activity, but its EC number is not offered; among the listed options, only A is supported."
  },
  "important_caveats": [
    "The evidence is a database annotation citing experimental evidence, not an independent review of the cited study.",
    "Reviewer-only sequence matching establishes applicability of the annotation; that identity information was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry V9TT49 (XY43B_HUMIN) confirms EC 3.2.1.37 (beta-xylosidase) with experimental evidence (ECO:0000269, PubMed:24262572). The protein is a bifunctional GH43 xylosidase/arabinosidase, and EC 3.2.1.37 is its primary listed activity. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark GH43 family motifs: the 'WAPCLSHDGERFWLVYTDVKRKDGSFKDTPNYIVTAEKIEGPWSDPIYINSSGFDPSLFHDDDGRKWFVNMLWDHRRRPQLFEG' region shows the characteristic tryptophan-rich loops and conserved Asp residues of the first half of the GH43 five-bladed beta-propeller, and the downstream 'WYYLLTAEGGTGYEHACTFARSRNIWGPYEVHPQKYILTSKDHPHAALQRAGHGDIVDTPDGRTYLVHLTGRPTTQFRRCVLGRETAIQEAYWGDDDWLYVKNGPVPSLWVDLPAARDDTKYWEEKRYTFESGLHKDFQWLRTPETDRIFRTREDGKLTLIGRESIGSWFEQALVARRQTHFSCDAETVIDFSPEDQRQFAGLTAYYCRYNFFYLAVSAHSDGQRELFIMASEASWPLGELRYPVPEGVRIPNEGKVRLALTIRGRELQFYYALEGEELKKIGPVLDASIVSDECGGHQKHGSFTGAFVGVAASDLNGTAAEATFDYFIYRPVQHPSDRYEI' region shows the second half. GH43 family enzymes are canonically assigned EC 3.2.1.37 (beta-xylosidase) and sometimes EC 3.2.1.55 (alpha-L-arabinofuranosidase). EC 3.2.1.18 (alpha-L-arabinofuranosidase) belongs to GH51/GH54/GH62/GH93 families, not GH43. EC 2.7.8.7 is a phosphatidyltransferase (transferase class) and EC 1.5.1.38 is an oxidoreductase — both are incompatible with a glycoside hydrolase fold. Thus family-level knowledge of GH43 distinguishes A from B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the GH43 beta-propeller fold from conserved sequence motifs is transferable knowledge applicable across all GH43 proteins. The EC assignment for GH43 (3.2.1.37) is a well-established family-level annotation, and the distinction between 3.2.1.37 (GH43) and 3.2.1.18 (GH51/GH54/GH62/GH93) is a standard family-to-EC mapping. Options C and D are eliminated by the obvious glycoside hydrolase character. No target-specific memorization is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only EC 3.2.1.37 is correct for a GH43 beta-xylosidase. EC 3.2.1.55 (the arabinosidase activity of this bifunctional enzyme) is not among the options, and EC 3.2.1.18 is the wrong EC for GH43 arabinosidase activity. C and D are entirely different enzyme classes. No ambiguity exists among the offered choices.


### Important caveats

- The protein is bifunctional (xylosidase + arabinosidase), but only 3.2.1.37 is offered; 3.2.1.55 is not an option, so no ambiguity arises.
- The GH43 family assignment relies on sequence motif recognition; a model unfamiliar with GH43 signatures might struggle, but this is legitimate family-level knowledge, not target-specific lookup.
- The experimental evidence (ECO:0000269) confirms both activities, but the question asks for the primary EC, which is 3.2.1.37.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark GH43 family motifs: the 'WAPCLSHDGERFWLVYTDVKRKDGSFKDTPNYIVTAEKIEGPWSDPIYINSSGFDPSLFHDDDGRKWFVNMLWDHRRRPQLFEG' region shows the characteristic tryptophan-rich loops and conserved Asp residues of the first half of the GH43 five-bladed beta-propeller, and the downstream 'WYYLLTAEGGTGYEHACTFARSRNIWGPYEVHPQKYILTSKDHPHAALQRAGHGDIVDTPDGRTYLVHLTGRPTTQFRRCVLGRETAIQEAYWGDDDWLYVKNGPVPSLWVDLPAARDDTKYWEEKRYTFESGLHKDFQWLRTPETDRIFRTREDGKLTLIGRESIGSWFEQALVARRQTHFSCDAETVIDFSPEDQRQFAGLTAYYCRYNFFYLAVSAHSDGQRELFIMASEASWPLGELRYPVPEGVRIPNEGKVRLALTIRGRELQFYYALEGEELKKIGPVLDASIVSDECGGHQKHGSFTGAFVGVAASDLNGTAAEATFDYFIYRPVQHPSDRYEI' region shows the second half. GH43 family enzymes are canonically assigned EC 3.2.1.37 (beta-xylosidase) and sometimes EC 3.2.1.55 (alpha-L-arabinofuranosidase). EC 3.2.1.18 (alpha-L-arabinofuranosidase) belongs to GH51/GH54/GH62/GH93 families, not GH43. EC 2.7.8.7 is a phosphatidyltransferase (transferase class) and EC 1.5.1.38 is an oxidoreductase — both are incompatible with a glycoside hydrolase fold. Thus family-level knowledge of GH43 distinguishes A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the GH43 beta-propeller fold from conserved sequence motifs is transferable knowledge applicable across all GH43 proteins. The EC assignment for GH43 (3.2.1.37) is a well-established family-level annotation, and the distinction between 3.2.1.37 (GH43) and 3.2.1.18 (GH51/GH54/GH62/GH93) is a standard family-to-EC mapping. Options C and D are eliminated by the obvious glycoside hydrolase character. No target-specific memorization is required."
  },
  "case_id": "EC_number_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry V9TT49 (XY43B_HUMIN) confirms EC 3.2.1.37 (beta-xylosidase) with experimental evidence (ECO:0000269, PubMed:24262572). The protein is a bifunctional GH43 xylosidase/arabinosidase, and EC 3.2.1.37 is its primary listed activity. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The protein is bifunctional (xylosidase + arabinosidase), but only 3.2.1.37 is offered; 3.2.1.55 is not an option, so no ambiguity arises.",
    "The GH43 family assignment relies on sequence motif recognition; a model unfamiliar with GH43 signatures might struggle, but this is legitimate family-level knowledge, not target-specific lookup.",
    "The experimental evidence (ECO:0000269) confirms both activities, but the question asks for the primary EC, which is 3.2.1.37."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only EC 3.2.1.37 is correct for a GH43 beta-xylosidase. EC 3.2.1.55 (the arabinosidase activity of this bifunctional enzyme) is not among the options, and EC 3.2.1.18 is the wrong EC for GH43 arabinosidase activity. C and D are entirely different enzyme classes. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry V9TT49 (XY43B_HUMIN) confirms EC 3.2.1.37 (beta-xylosidase) with experimental evidence (ECO:0000269, PubMed:24262572). The protein is a bifunctional GH43 xylosidase/arabinosidase, and EC 3.2.1.37 is its primary listed activity. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark GH43 family motifs: the 'WAPCLSHDGERFWLVYTDVKRKDGSFKDTPNYIVTAEKIEGPWSDPIYINSSGFDPSLFHDDDGRKWFVNMLWDHRRRPQLFEG' region shows the characteristic tryptophan-rich loops and conserved Asp residues of the first half of the GH43 five-bladed beta-propeller, and the downstream 'WYYLLTAEGGTGYEHACTFARSRNIWGPYEVHPQKYILTSKDHPHAALQRAGHGDIVDTPDGRTYLVHLTGRPTTQFRRCVLGRETAIQEAYWGDDDWLYVKNGPVPSLWVDLPAARDDTKYWEEKRYTFESGLHKDFQWLRTPETDRIFRTREDGKLTLIGRESIGSWFEQALVARRQTHFSCDAETVIDFSPEDQRQFAGLTAYYCRYNFFYLAVSAHSDGQRELFIMASEASWPLGELRYPVPEGVRIPNEGKVRLALTIRGRELQFYYALEGEELKKIGPVLDASIVSDECGGHQKHGSFTGAFVGVAASDLNGTAAEATFDYFIYRPVQHPSDRYEI' region shows the second half. GH43 family enzymes are canonically assigned EC 3.2.1.37 (beta-xylosidase) and sometimes EC 3.2.1.55 (alpha-L-arabinofuranosidase). EC 3.2.1.18 (alpha-L-arabinofuranosidase) belongs to GH51/GH54/GH62/GH93 families, not GH43. EC 2.7.8.7 is a phosphatidyltransferase (transferase class) and EC 1.5.1.38 is an oxidoreductase — both are incompatible with a glycoside hydrolase fold. Thus family-level knowledge of GH43 distinguishes A from B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the GH43 beta-propeller fold from conserved sequence motifs is transferable knowledge applicable across all GH43 proteins. The EC assignment for GH43 (3.2.1.37) is a well-established family-level annotation, and the distinction between 3.2.1.37 (GH43) and 3.2.1.18 (GH51/GH54/GH62/GH93) is a standard family-to-EC mapping. Options C and D are eliminated by the obvious glycoside hydrolase character. No target-specific memorization is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only EC 3.2.1.37 is correct for a GH43 beta-xylosidase. EC 3.2.1.55 (the arabinosidase activity of this bifunctional enzyme) is not among the options, and EC 3.2.1.18 is the wrong EC for GH43 arabinosidase activity. C and D are entirely different enzyme classes. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The protein is bifunctional (xylosidase + arabinosidase), but only 3.2.1.37 is offered; 3.2.1.55 is not an option, so no ambiguity arises.",
    "The GH43 family assignment relies on sequence motif recognition; a model unfamiliar with GH43 signatures might struggle, but this is legitimate family-level knowledge, not target-specific lookup.",
    "The experimental evidence (ECO:0000269) confirms both activities, but the question asks for the primary EC, which is 3.2.1.37."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 123. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
