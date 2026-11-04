# transmembrane_0106

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0106.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 32..52; 730..750; 795..815; 845..865; 1111..1131

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNELSVNDAFDDIEIESFDFIWEEWEEYKGDVPLWQHIFCGSIAGLMEHVFMYPLDTLKTYFQTNGHMKYNMIYDNCNTINNNNNNIYRGNNSSYKNTCDKNYKDMNNHRNMQTFKRNFCSSTNCDKCIINNFCKYKTNCYNVMAALHTKNNRYIHNIAEPLKNMANYKINTTNNNNVNNIINNNNNNNKKKSRNIFSYPSHTKQYRNVTYVVNKKMQQNLFNNYISNKCINDPFCCRTKTNVLNMKKDIHKFCHLSKEKYNNVFYQNDTYHPNIYGRKRKTLCRNKNNINLFKNHVHKKYCHSLDDQICHSKIKEDMRNLQNFKNYTCAKNMKRHLYSTVPFFNLKNKGNKNITLPYKEIRSKYILKNGYKSMYQRNAGYYKNLIKMQSAKKNRHQLLALRKCLMSEKKYTIIKNEPFIIRKKKNMRNEYFIGNMKGRCIINTSLNSYTLKRNCLDYHHFVNNLKNICYSIMNICYNIKNTILINPSLPINNNNNNNNNTKMDTFIKLINKCLYNNNAHKIDHKILLSNYLNLFKHTNYSYYYILNNFLKNNAPCTSRKNEWNIFSNFINVLKNKIITNNVDYIRNPNVRRNQILRNNYLYSFLRNYNKNLKRNTHMILNKLTSFKYSIPYIKNKYSNVLINNINTNNNTYSNRNVLNSIRYNNIYKNIMHPIFFPGYYNTIHFRYYNYFSRIIDDKDKGKNKNIINISTKRNNCSSIIRNNLSNLYKGVNVVVLGCIPAHALYFSTFEYSKKYFSRMTSNNSSLKMNNRNISTVSNDIKSEKSNFKLYDLNYFSIAVSGFLATLVHDLIITPIDTLKQRIQLGINKNSKDSLKLLKQNGIRSLYLSLPITLLMNIPYQIIMICTNEKMKKIYFEYICGLNTQNNKKNMENKVIDKVHDETRNQDNIGKDIKNDTYNMDKNGTFLRNQEMINKENRIYNSGALEKHVTSQEKEDKILQSVKQENVSSNNDIVNFYEGQSIYNNDAHNIIRDDINKMTHKNLENNIDNTINSNESDVNRIDNMTNDMNKECDIFSINKNNNSTVLYDQIMKRLEMNSSNKNFSLNFHDKIIRQESSPFEKENYNMNLKNIWIDNYKNDFFNKPFNHITSYFVCAGIGGGIAAVLTNPLDVIKTRIQTECFQTKGFNFFRIVSNIYYREGMRSFFKGSLARMALCIPASAVSWGTYETMKRFFKINFNTT

[Multiple Choices]
A. 32..52; 730..750; 795..815; 1111..1131
B. 25..45; 55..75; 80..100; 116..136; 175..195; 211..231
C. 32..52; 730..750; 795..815; 845..865; 1111..1131
D. 32..52; 730..750; 795..815; 845..865; 1111..1135
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

> The sequence-matched UniProt annotations list all five spans in C. The annotations are computationally supported (ECO:0000255), not experimental measurements; the historical record available by the stated cutoff also lists these spans. The exact author source snapshot is unknown.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has several hydrophobic stretches consistent with membrane-spanning helices, including the late segment around 1111: its hydrophobic run is followed by polar/charged residues, making the longer endpoint in D less plausible. The spans around 730, 795, and 845 also fit the expected hydrophobic-helix pattern, distinguishing C from A, while B proposes unrelated early intervals.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of membrane-protein sequence patterns, applied to the supplied sequence and the alternatives, gives a meaningful basis for choosing C without needing the target's recorded annotation. Exact helix boundaries can be uncertain, but the options' differences are meaningfully distinguishable here.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although transmembrane boundaries are often approximate, the listed hydrophobic stretches and the polar/charged residues after the final span favor the boundaries in C over the alternatives.


### Important caveats

- The supporting database annotations are computational rather than experimental.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several hydrophobic stretches consistent with membrane-spanning helices, including the late segment around 1111: its hydrophobic run is followed by polar/charged residues, making the longer endpoint in D less plausible. The spans around 730, 795, and 845 also fit the expected hydrophobic-helix pattern, distinguishing C from A, while B proposes unrelated early intervals.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of membrane-protein sequence patterns, applied to the supplied sequence and the alternatives, gives a meaningful basis for choosing C without needing the target's recorded annotation. Exact helix boundaries can be uncertain, but the options' differences are meaningfully distinguishable here."
  },
  "case_id": "transmembrane_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotations list all five spans in C. The annotations are computationally supported (ECO:0000255), not experimental measurements; the historical record available by the stated cutoff also lists these spans. The exact author source snapshot is unknown."
  },
  "important_caveats": [
    "The supporting database annotations are computational rather than experimental.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although transmembrane boundaries are often approximate, the listed hydrophobic stretches and the polar/charged residues after the final span favor the boundaries in C over the alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotations list all five spans in C. The annotations are computationally supported (ECO:0000255), not experimental measurements; the historical record available by the stated cutoff also lists these spans. The exact author source snapshot is unknown.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has several hydrophobic stretches consistent with membrane-spanning helices, including the late segment around 1111: its hydrophobic run is followed by polar/charged residues, making the longer endpoint in D less plausible. The spans around 730, 795, and 845 also fit the expected hydrophobic-helix pattern, distinguishing C from A, while B proposes unrelated early intervals.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of membrane-protein sequence patterns, applied to the supplied sequence and the alternatives, gives a meaningful basis for choosing C without needing the target's recorded annotation. Exact helix boundaries can be uncertain, but the options' differences are meaningfully distinguishable here."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although transmembrane boundaries are often approximate, the listed hydrophobic stretches and the polar/charged residues after the final span favor the boundaries in C over the alternatives."
  },
  "important_caveats": [
    "The supporting database annotations are computational rather than experimental.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q8I397 (Putative mitoferrin, Plasmodium falciparum) lists exactly five transmembrane helical segments at 32-52, 730-750, 795-815, 845-865, and 1111-1131, matching option C precisely. All five annotations carry evidence code ECO:0000255 (similarity-based computational prediction), so these are in silico predictions transferred by sequence similarity rather than experimentally validated measurements. The sequence match between the benchmark input and the UniProt entry is confirmed (SHA256 match, 1199 residues). The annotation supports the key, though it is computational rather than experimental.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option B is trivially eliminated: positions 25-231 fall entirely within an extremely hydrophilic N-terminal region dominated by Asn, Ser, Thr, Lys, and Cys residues, precluding any membrane-spanning helix. The remaining three options (A, C, D) share TMs at 32-52, 730-750, 795-815, and differ in two respects. (1) A vs C: A omits the TM at 845-865. The mitoferrin/mitochondrial carrier family (SLC25A37/38 homologs) characteristically contains multiple TM helices arranged in internal repeats; a hydrophobicity scan of the sequence in the 845-865 window reveals a hydrophobic stretch consistent with an additional membrane-spanning segment, supporting its inclusion. (2) C vs D: The last TM ends at 1131 (C) vs 1135 (D). Residues at positions 1132-1134 are Lys, Thr, Arg—two strongly charged residues flanking a polar one—which constitute a canonical hydrophilic boundary that terminates a transmembrane helix. Any reasonable hydrophobicity-based analysis (e.g., a sliding-window or per-residue hydrophobicity scale) would stop the helix at Ile-1131 rather than extend through K-T-R. Thus, family-level expectations (multiple TMs in carrier/mitoferrin proteins) plus sequence-level hydrophobicity boundaries meaningfully distinguish C from both A and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B by recognizing the hydrophilic N-terminal composition, identify the 845-865 TM through hydrophobicity scanning supported by family-level expectations of multiple TMs in mitochondrial carrier/mitoferrin proteins, and resolve the 1131-vs-1135 endpoint by observing the charged K/R residues immediately after position 1131. These are transferable sequence-analysis and family-knowledge arguments, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is clearly wrong (hydrophilic region). Option D is disfavored by the charged K/R residues at 1132-1134 that would not be part of a TM helix. Option A omits a hydrophobic stretch at 845-865 that a hydrophobicity scan should detect, and the mitoferrin/carrier family context supports five TMs rather than four. Option C is the most defensible choice.


### Important caveats

- All five TM annotations are computational predictions (ECO:0000255, similarity-based), not experimentally determined. The 'correct' boundaries reflect an algorithm's output and could differ with a different prediction tool.
- The distinction between options C and D (1131 vs 1135) hinges on a 4-residue boundary; while the K/T/R residues strongly favor 1131, very fine boundary placement is inherently algorithm-sensitive.
- The distinction between A and C (presence of the 845-865 TM) depends on whether a model's hydrophobicity scan identifies that particular stretch; a less sensitive scan might miss it and select A.
- The protein is 1199 residues, far longer than canonical mitoferrins (~350-400 aa), so it likely contains additional domains beyond the carrier core; the 5-TM topology is consistent with the carrier-like region embedded in a larger protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option B is trivially eliminated: positions 25-231 fall entirely within an extremely hydrophilic N-terminal region dominated by Asn, Ser, Thr, Lys, and Cys residues, precluding any membrane-spanning helix. The remaining three options (A, C, D) share TMs at 32-52, 730-750, 795-815, and differ in two respects. (1) A vs C: A omits the TM at 845-865. The mitoferrin/mitochondrial carrier family (SLC25A37/38 homologs) characteristically contains multiple TM helices arranged in internal repeats; a hydrophobicity scan of the sequence in the 845-865 window reveals a hydrophobic stretch consistent with an additional membrane-spanning segment, supporting its inclusion. (2) C vs D: The last TM ends at 1131 (C) vs 1135 (D). Residues at positions 1132-1134 are Lys, Thr, Arg—two strongly charged residues flanking a polar one—which constitute a canonical hydrophilic boundary that terminates a transmembrane helix. Any reasonable hydrophobicity-based analysis (e.g., a sliding-window or per-residue hydrophobicity scale) would stop the helix at Ile-1131 rather than extend through K-T-R. Thus, family-level expectations (multiple TMs in carrier/mitoferrin proteins) plus sequence-level hydrophobicity boundaries meaningfully distinguish C from both A and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B by recognizing the hydrophilic N-terminal composition, identify the 845-865 TM through hydrophobicity scanning supported by family-level expectations of multiple TMs in mitochondrial carrier/mitoferrin proteins, and resolve the 1131-vs-1135 endpoint by observing the charged K/R residues immediately after position 1131. These are transferable sequence-analysis and family-knowledge arguments, not a lookup of this protein's specific annotation."
  },
  "case_id": "transmembrane_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8I397 (Putative mitoferrin, Plasmodium falciparum) lists exactly five transmembrane helical segments at 32-52, 730-750, 795-815, 845-865, and 1111-1131, matching option C precisely. All five annotations carry evidence code ECO:0000255 (similarity-based computational prediction), so these are in silico predictions transferred by sequence similarity rather than experimentally validated measurements. The sequence match between the benchmark input and the UniProt entry is confirmed (SHA256 match, 1199 residues). The annotation supports the key, though it is computational rather than experimental."
  },
  "important_caveats": [
    "All five TM annotations are computational predictions (ECO:0000255, similarity-based), not experimentally determined. The 'correct' boundaries reflect an algorithm's output and could differ with a different prediction tool.",
    "The distinction between options C and D (1131 vs 1135) hinges on a 4-residue boundary; while the K/T/R residues strongly favor 1131, very fine boundary placement is inherently algorithm-sensitive.",
    "The distinction between A and C (presence of the 845-865 TM) depends on whether a model's hydrophobicity scan identifies that particular stretch; a less sensitive scan might miss it and select A.",
    "The protein is 1199 residues, far longer than canonical mitoferrins (~350-400 aa), so it likely contains additional domains beyond the carrier core; the 5-TM topology is consistent with the carrier-like region embedded in a larger protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is clearly wrong (hydrophilic region). Option D is disfavored by the charged K/R residues at 1132-1134 that would not be part of a TM helix. Option A omits a hydrophobic stretch at 845-865 that a hydrophobicity scan should detect, and the mitoferrin/carrier family context supports five TMs rather than four. Option C is the most defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8I397 (Putative mitoferrin, Plasmodium falciparum) lists exactly five transmembrane helical segments at 32-52, 730-750, 795-815, 845-865, and 1111-1131, matching option C precisely. All five annotations carry evidence code ECO:0000255 (similarity-based computational prediction), so these are in silico predictions transferred by sequence similarity rather than experimentally validated measurements. The sequence match between the benchmark input and the UniProt entry is confirmed (SHA256 match, 1199 residues). The annotation supports the key, though it is computational rather than experimental.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option B is trivially eliminated: positions 25-231 fall entirely within an extremely hydrophilic N-terminal region dominated by Asn, Ser, Thr, Lys, and Cys residues, precluding any membrane-spanning helix. The remaining three options (A, C, D) share TMs at 32-52, 730-750, 795-815, and differ in two respects. (1) A vs C: A omits the TM at 845-865. The mitoferrin/mitochondrial carrier family (SLC25A37/38 homologs) characteristically contains multiple TM helices arranged in internal repeats; a hydrophobicity scan of the sequence in the 845-865 window reveals a hydrophobic stretch consistent with an additional membrane-spanning segment, supporting its inclusion. (2) C vs D: The last TM ends at 1131 (C) vs 1135 (D). Residues at positions 1132-1134 are Lys, Thr, Arg—two strongly charged residues flanking a polar one—which constitute a canonical hydrophilic boundary that terminates a transmembrane helix. Any reasonable hydrophobicity-based analysis (e.g., a sliding-window or per-residue hydrophobicity scale) would stop the helix at Ile-1131 rather than extend through K-T-R. Thus, family-level expectations (multiple TMs in carrier/mitoferrin proteins) plus sequence-level hydrophobicity boundaries meaningfully distinguish C from both A and D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B by recognizing the hydrophilic N-terminal composition, identify the 845-865 TM through hydrophobicity scanning supported by family-level expectations of multiple TMs in mitochondrial carrier/mitoferrin proteins, and resolve the 1131-vs-1135 endpoint by observing the charged K/R residues immediately after position 1131. These are transferable sequence-analysis and family-knowledge arguments, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is clearly wrong (hydrophilic region). Option D is disfavored by the charged K/R residues at 1132-1134 that would not be part of a TM helix. Option A omits a hydrophobic stretch at 845-865 that a hydrophobicity scan should detect, and the mitoferrin/carrier family context supports five TMs rather than four. Option C is the most defensible choice."
  },
  "important_caveats": [
    "All five TM annotations are computational predictions (ECO:0000255, similarity-based), not experimentally determined. The 'correct' boundaries reflect an algorithm's output and could differ with a different prediction tool.",
    "The distinction between options C and D (1131 vs 1135) hinges on a 4-residue boundary; while the K/T/R residues strongly favor 1131, very fine boundary placement is inherently algorithm-sensitive.",
    "The distinction between A and C (presence of the 845-865 TM) depends on whether a model's hydrophobicity scan identifies that particular stretch; a less sensitive scan might miss it and select A.",
    "The protein is 1199 residues, far longer than canonical mitoferrins (~350-400 aa), so it likely contains additional domains beyond the carrier core; the 5-TM topology is consistent with the carrier-like region embedded in a larger protein."
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
  "benchmark_sequence_length": 1199,
  "benchmark_sequence_sha256": "0aec190e1890daaba4890c14f5ccf9dc2d066473eaed63c4598f14eb646271c7",
  "current_entry_audit": {
    "entryVersion": 137,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1199,
  "current_source_sequence_sha256": "0aec190e1890daaba4890c14f5ccf9dc2d066473eaed63c4598f14eb646271c7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 135,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8I397",
  "selected_historical_entry_version": 135,
  "selected_historical_record_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "selected_historical_source_sequence_length": 1199,
  "selected_historical_source_sequence_sha256": "0aec190e1890daaba4890c14f5ccf9dc2d066473eaed63c4598f14eb646271c7",
  "selected_historical_version": {
    "accession": "Q8I397",
    "database": "Swiss-Prot",
    "entryVersion": 135,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFRN_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8I397\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":137,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"Mitochondrial carrier protein MRS3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"PfMRS3\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Putative mitoferrin\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"PfMFRN\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":52},\"start\":{\"modifier\":\"EXACT\",\"value\":32}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":750},\"start\":{\"modifier\":\"EXACT\",\"value\":730}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":815},\"start\":{\"modifier\":\"EXACT\",\"value\":795}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":865},\"start\":{\"modifier\":\"EXACT\",\"value\":845}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1131},\"start\":{\"modifier\":\"EXACT\",\"value\":1111}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Wunderlich J.\",\"Kotov V.\",\"Votborg-Novel L.\",\"Ntalla C.\",\"Geffken M.\",\"Peine S.\",\"Portugal S.\",\"Strauss J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39575308\"},{\"database\":\"DOI\",\"id\":\"10.3389/fcimb.2024.1480076\"}],\"citationType\":\"journal article\",\"firstPage\":\"1480076\",\"id\":\"39575308\",\"journal\":\"Front. Cell. Infect. Microbiol.\",\"lastPage\":\"1480076\",\"publicationDate\":\"2024\",\"title\":\"Iron transport pathways in the human malaria parasite Plasmodium falciparum revealed by RNA-sequencing.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H1",
  "excerpt": "ID   MFRN_PLAF7              Reviewed;        1199 AA.\nAC   Q8I397;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 135.\nDE   RecName: Full=Putative mitoferrin {ECO:0000305};\nDE            Short=PfMFRN {ECO:0000303|PubMed:39575308};\nDE   AltName: Full=Mitochondrial carrier protein MRS3 {ECO:0000303|PubMed:39575308};\nDE            Short=PfMRS3 {ECO:0000303|PubMed:39575308};\nGN   ORFNames=PF3D7_0905200 {ECO:0000312|EMBL:CAD51737.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, INDUCTION, AND\nRP   DISRUPTION PHENOTYPE.\nRX   PubMed=39575308; DOI=10.3389/fcimb.2024.1480076;\nRA   Wunderlich J., Kotov V., Votborg-Novel L., Ntalla C., Geffken M., Peine S.,\nRA   Portugal S., Strauss J.;\nRT   \"Iron transport pathways in the human malaria parasite Plasmodium\nRT   falciparum revealed by RNA-sequencing.\";\nRL   Front. Cell. Infect. Microbiol. 14:1480076-1480076(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        32..52\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        730..750\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        795..815\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        845..865\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        1111..1131\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
