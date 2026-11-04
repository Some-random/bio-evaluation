# transmembrane_0030

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0030.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 8..28

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDLLQRAGLVVGLWVTYHILLGTYNVFFHPLRRFPGPRLAAATQLVNVYYIIRGINCKYLYELHEKYGDVVRTGPNELSFRTASAIRTIYGGNPGPDDTFHKNMIANIQETGDSDNLFFATGQQHNRYRRLIMPVFAERTIQGQGPMMQEYCSQLIQGLRNRCGRGYFPTQDGVVDIVPWTHFIISDILSHMLFGSGMNCLLNGDYHPWVMAGYKALIESTYIEAAHRLRPYHRILEYLLIPTRLRDGFRVHSAVSREKLQARSKEAEPYQFSLPSFTSESLSEQELFDNINVIATAAGETTSSALSAIMYYLTANPAAYDKAVTEVRQAFSNEAEITAASSASLPYLKAVIREAFRIRPTIPVGLHRLTPKGGREIDGKWVPAGTWISVANLAACRTSSHWKEAGRFIPERWLGDPEFASDNRDTSVPYSIGVRNCIGMSHANTQLRLILSRLLWNFDFEACPGNADPYDYLEYGTWQVEPLKLRVVDIRGQPK

[Multiple Choices]
A. 8..28; 709..733
B. 5..30
C. 35..55
D. 8..28
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies residues 8–28 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational annotation, not direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus contains a strong hydrophobic stretch around residues 8–28, consistent with a membrane-spanning helix. The flanking Q/R and H/P residues make the shorter D interval more plausible than B's extended interval; C is not comparably hydrophobic, and A adds positions beyond the 495-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Hydropathy and the surrounding residues provide a transferable basis for distinguishing the offered intervals without needing an annotation for this exact protein. The precise boundaries remain predictive rather than experimentally established from the input alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B overlaps the predicted hydrophobic helix but includes less plausible flanking residues; D is the best-supported interval among the choices.


### Important caveats

- The supplied source annotation is computational, so it supports the key but does not establish experimental confirmation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus contains a strong hydrophobic stretch around residues 8–28, consistent with a membrane-spanning helix. The flanking Q/R and H/P residues make the shorter D interval more plausible than B's extended interval; C is not comparably hydrophobic, and A adds positions beyond the 495-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Hydropathy and the surrounding residues provide a transferable basis for distinguishing the offered intervals without needing an annotation for this exact protein. The precise boundaries remain predictive rather than experimentally established from the input alone."
  },
  "case_id": "transmembrane_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 8–28 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational annotation, not direct experimental confirmation."
  },
  "important_caveats": [
    "The supplied source annotation is computational, so it supports the key but does not establish experimental confirmation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B overlaps the predicted hydrophobic helix but includes less plausible flanking residues; D is the best-supported interval among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 8–28 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational annotation, not direct experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus contains a strong hydrophobic stretch around residues 8–28, consistent with a membrane-spanning helix. The flanking Q/R and H/P residues make the shorter D interval more plausible than B's extended interval; C is not comparably hydrophobic, and A adds positions beyond the 495-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "Hydropathy and the surrounding residues provide a transferable basis for distinguishing the offered intervals without needing an annotation for this exact protein. The precise boundaries remain predictive rather than experimentally established from the input alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B overlaps the predicted hydrophobic helix but includes less plausible flanking residues; D is the best-supported interval among the choices."
  },
  "important_caveats": [
    "The supplied source annotation is computational, so it supports the key but does not establish experimental confirmation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7T8F1I4) annotates a helical transmembrane region at positions 8..28 (evidence code ECO:0000255, inferred by similarity). The sequence at positions 8-28 (GLVVGLWVTYHILLGTYNVFF) is a 21-residue hydrophobic stretch consistent with a single-pass TM alpha-helix. The annotation is computational/predictive rather than experimentally determined, but the sequence itself supports the prediction.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option A is eliminated because position 709 exceeds the 495-residue protein length. Option C (35..55: PGPR LAAATQLVNVYYIIRGI) contains multiple polar/charged residues (P, G, R, T, Q, N, R, G) and lacks sufficient hydrophobicity for a TM helix. The key distinction is between B (5..30) and D (8..28). Position 5 is Q (glutamine, polar), position 6 is R (arginine, positively charged), and position 30 is P (proline, a well-known helix breaker). TM helices require a continuous stretch of hydrophobic residues; charged side chains (Q, R) are energetically prohibitive inside the lipid bilayer, and proline disrupts alpha-helical structure. A knowledgeable model applying the rule that TM segments exclude charged residues and helix-breaking proline would narrow from 5..30 to 8..28. Additionally, cytochrome P450 monooxygenases are well-known to possess a single N-terminal TM anchor helix that tethers them to the ER membrane—a family-level pattern that directs attention to the N-terminal hydrophobic region.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinction between B and D relies on general biophysical rules (charged residues incompatible with TM helices, proline breaks helicity) and family-level knowledge (P450 N-terminal TM anchor), all transferable from other proteins. The exact boundaries are determined by sequence composition visible in the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B (5..30) overlaps the true TM core, the inclusion of two charged residues (Q5, R6) and a helix-breaking proline (P30) makes it clearly inferior to D under standard TM prediction criteria. No other option is genuinely defensible.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational/predictive, not experimentally validated.
- The protein is identified as a cytochrome P450 monooxygenase (FrzC) from Cladobotryum sp., but this identification is reviewer-only and was not provided to the evaluated model; however, the N-terminal TM anchor pattern is recognizable from sequence alone.
- The protein is 495 residues; option A's second segment (709..733) is trivially impossible, making that option a pure distractor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option A is eliminated because position 709 exceeds the 495-residue protein length. Option C (35..55: PGPR LAAATQLVNVYYIIRGI) contains multiple polar/charged residues (P, G, R, T, Q, N, R, G) and lacks sufficient hydrophobicity for a TM helix. The key distinction is between B (5..30) and D (8..28). Position 5 is Q (glutamine, polar), position 6 is R (arginine, positively charged), and position 30 is P (proline, a well-known helix breaker). TM helices require a continuous stretch of hydrophobic residues; charged side chains (Q, R) are energetically prohibitive inside the lipid bilayer, and proline disrupts alpha-helical structure. A knowledgeable model applying the rule that TM segments exclude charged residues and helix-breaking proline would narrow from 5..30 to 8..28. Additionally, cytochrome P450 monooxygenases are well-known to possess a single N-terminal TM anchor helix that tethers them to the ER membrane—a family-level pattern that directs attention to the N-terminal hydrophobic region.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinction between B and D relies on general biophysical rules (charged residues incompatible with TM helices, proline breaks helicity) and family-level knowledge (P450 N-terminal TM anchor), all transferable from other proteins. The exact boundaries are determined by sequence composition visible in the input."
  },
  "case_id": "transmembrane_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1I4) annotates a helical transmembrane region at positions 8..28 (evidence code ECO:0000255, inferred by similarity). The sequence at positions 8-28 (GLVVGLWVTYHILLGTYNVFF) is a 21-residue hydrophobic stretch consistent with a single-pass TM alpha-helix. The annotation is computational/predictive rather than experimentally determined, but the sequence itself supports the prediction."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational/predictive, not experimentally validated.",
    "The protein is identified as a cytochrome P450 monooxygenase (FrzC) from Cladobotryum sp., but this identification is reviewer-only and was not provided to the evaluated model; however, the N-terminal TM anchor pattern is recognizable from sequence alone.",
    "The protein is 495 residues; option A's second segment (709..733) is trivially impossible, making that option a pure distractor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B (5..30) overlaps the true TM core, the inclusion of two charged residues (Q5, R6) and a helix-breaking proline (P30) makes it clearly inferior to D under standard TM prediction criteria. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1I4) annotates a helical transmembrane region at positions 8..28 (evidence code ECO:0000255, inferred by similarity). The sequence at positions 8-28 (GLVVGLWVTYHILLGTYNVFF) is a 21-residue hydrophobic stretch consistent with a single-pass TM alpha-helix. The annotation is computational/predictive rather than experimentally determined, but the sequence itself supports the prediction.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option A is eliminated because position 709 exceeds the 495-residue protein length. Option C (35..55: PGPR LAAATQLVNVYYIIRGI) contains multiple polar/charged residues (P, G, R, T, Q, N, R, G) and lacks sufficient hydrophobicity for a TM helix. The key distinction is between B (5..30) and D (8..28). Position 5 is Q (glutamine, polar), position 6 is R (arginine, positively charged), and position 30 is P (proline, a well-known helix breaker). TM helices require a continuous stretch of hydrophobic residues; charged side chains (Q, R) are energetically prohibitive inside the lipid bilayer, and proline disrupts alpha-helical structure. A knowledgeable model applying the rule that TM segments exclude charged residues and helix-breaking proline would narrow from 5..30 to 8..28. Additionally, cytochrome P450 monooxygenases are well-known to possess a single N-terminal TM anchor helix that tethers them to the ER membrane—a family-level pattern that directs attention to the N-terminal hydrophobic region.",
    "missing_item_specific_fact": "",
    "reason": "The distinction between B and D relies on general biophysical rules (charged residues incompatible with TM helices, proline breaks helicity) and family-level knowledge (P450 N-terminal TM anchor), all transferable from other proteins. The exact boundaries are determined by sequence composition visible in the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B (5..30) overlaps the true TM core, the inclusion of two charged residues (Q5, R6) and a helix-breaking proline (P30) makes it clearly inferior to D under standard TM prediction criteria. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational/predictive, not experimentally validated.",
    "The protein is identified as a cytochrome P450 monooxygenase (FrzC) from Cladobotryum sp., but this identification is reviewer-only and was not provided to the evaluated model; however, the N-terminal TM anchor pattern is recognizable from sequence alone.",
    "The protein is 495 residues; option A's second segment (709..733) is trivially impossible, making that option a pure distractor."
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
  "benchmark_sequence_length": 495,
  "benchmark_sequence_sha256": "33136adb3fb622649a4deb8775bb79a2e51befd4b556c2131d0cea6fc396df9b",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 495,
  "current_source_sequence_sha256": "33136adb3fb622649a4deb8775bb79a2e51befd4b556c2131d0cea6fc396df9b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8F1I4",
  "selected_historical_entry_version": 18,
  "selected_historical_record_sha256": "9364b021301c1c0c3fb659db92b723838ee62210edc6aa3fb3422781d6bcadb6",
  "selected_historical_source_sequence_length": 495,
  "selected_historical_source_sequence_sha256": "33136adb3fb622649a4deb8775bb79a2e51befd4b556c2131d0cea6fc396df9b",
  "selected_historical_version": {
    "accession": "A0A7T8F1I4",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZC_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1I4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:44.613598+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:44.613598+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:44.613598+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein C\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase FrzC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:44.613598+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":28},\"start\":{\"modifier\":\"EXACT\",\"value\":8}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:25:44.613598+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:44.613598+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1I4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H1",
  "excerpt": "ID   FRZC_CLASX              Reviewed;         495 AA.\nAC   A0A7T8F1I4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=Cytochrome P450 monooxygenase FrzC {ECO:0000303|PubMed:33372776};\nDE            EC=1.14.14.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein C {ECO:0000303|PubMed:33372776};\nGN   Name=FrzC {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:47.051386+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9364b021301c1c0c3fb659db92b723838ee62210edc6aa3fb3422781d6bcadb6",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1I4?format=txt&versions=18"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1I4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:47.051386+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9364b021301c1c0c3fb659db92b723838ee62210edc6aa3fb3422781d6bcadb6",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1I4?format=txt&versions=18"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1I4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        8..28\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:47.051386+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9364b021301c1c0c3fb659db92b723838ee62210edc6aa3fb3422781d6bcadb6",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1I4?format=txt&versions=18"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 30. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
