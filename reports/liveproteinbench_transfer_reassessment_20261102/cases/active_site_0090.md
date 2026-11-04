# active_site_0090

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0090.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 114 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSFSTLLTACTAITGALGTPDLDRRQNVTPNAQGTHNGYFYSWWSDGQSPVTYTNSAGGSYSVEWSSGGNLVGGKGWNPGSAKEIRYSASWQPTNNSNSYLTIYGWTRSPLVEYYIVESHGEYNPGSSAEPRGEIEAHGSIYKLYESTRVQQPSIDGTQTFQQYWAIRQTHRTSGTVTTGTFFNAWAAAGMPIGQHNYMIVATEAYNSAGRASVVVETPP

[Multiple Choices]
A. Position 2 (Nucleophile)
B. Position 114 (Nucleophile)
C. Position 237 (Proton donor)
D. Position 341 (For beta-ketoacyl synthase activity)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry annotates position 114 as the nucleophile, with evidence attributed to a PROSITE-ProRule. This supports the key as a computational annotation, not as direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 221-residue sequence has an N-terminal hydrophobic signal-peptide-like segment and a length and sequence composition consistent with a secreted fungal xylanase. In the sequence, position 114 is glutamate, a plausible catalytic residue in xylanases; family-level knowledge of conserved catalytic glutamates makes this a meaningful candidate for the nucleophile. Position 2 is valine in the signal-peptide region, while positions 237 and 341 are beyond the sequence length, so the alternatives distinguish B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable knowledge about secreted xylanases meaningfully favor B without needing the target's recorded annotation. The family inference is not itself experimental proof of the residue's role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only position 114 is both within the supplied sequence and plausibly a catalytic nucleophile; the other listed positions are either in the N-terminal signal-peptide-like region or outside the sequence.


### Important caveats

- The supplied source annotation is computationally inferred by PROSITE-ProRule; no direct experimental validation is provided here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 221-residue sequence has an N-terminal hydrophobic signal-peptide-like segment and a length and sequence composition consistent with a secreted fungal xylanase. In the sequence, position 114 is glutamate, a plausible catalytic residue in xylanases; family-level knowledge of conserved catalytic glutamates makes this a meaningful candidate for the nucleophile. Position 2 is valine in the signal-peptide region, while positions 237 and 341 are beyond the sequence length, so the alternatives distinguish B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge about secreted xylanases meaningfully favor B without needing the target's recorded annotation. The family inference is not itself experimental proof of the residue's role."
  },
  "case_id": "active_site_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates position 114 as the nucleophile, with evidence attributed to a PROSITE-ProRule. This supports the key as a computational annotation, not as direct experimental evidence."
  },
  "important_caveats": [
    "The supplied source annotation is computationally inferred by PROSITE-ProRule; no direct experimental validation is provided here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 114 is both within the supplied sequence and plausibly a catalytic nucleophile; the other listed positions are either in the N-terminal signal-peptide-like region or outside the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates position 114 as the nucleophile, with evidence attributed to a PROSITE-ProRule. This supports the key as a computational annotation, not as direct experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 221-residue sequence has an N-terminal hydrophobic signal-peptide-like segment and a length and sequence composition consistent with a secreted fungal xylanase. In the sequence, position 114 is glutamate, a plausible catalytic residue in xylanases; family-level knowledge of conserved catalytic glutamates makes this a meaningful candidate for the nucleophile. Position 2 is valine in the signal-peptide region, while positions 237 and 341 are beyond the sequence length, so the alternatives distinguish B.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge about secreted xylanases meaningfully favor B without needing the target's recorded annotation. The family inference is not itself experimental proof of the residue's role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 114 is both within the supplied sequence and plausibly a catalytic nucleophile; the other listed positions are either in the N-terminal signal-peptide-like region or outside the sequence."
  },
  "important_caveats": [
    "The supplied source annotation is computationally inferred by PROSITE-ProRule; no direct experimental validation is provided here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G2X5X8 (EIX4_VERDV, Ethylene-inducing xylanase 4, EC 3.2.1.8) annotates position 114 as 'Nucleophile' (evidence ECO:0000255|PROSITE-ProRule:PRU01097, GH11 family). The amino acid at position 114 in the provided sequence is Glutamic acid (E), which is the canonical nucleophile in glycoside hydrolase family 11. The annotation is computational (PROSITE-ProRule family assignment) rather than direct experimental mutagenesis, but it is consistent with the well-established catalytic mechanism of GH11 xylanases. The author's expected answer B matches this annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options C (position 237) and D (position 341) are trivially eliminated because the protein is only 221 residues long—those positions do not exist. Option A (position 2, Nucleophile) is eliminated because position 2 is Valine (V), which has an isopropyl side chain with no nucleophilic capability; Val is never a catalytic nucleophile in any known enzyme family. This leaves only option B. Position 114 is Glutamic acid (E), and the surrounding sequence context ('LVEYYIVESHG') is consistent with the nucleophile motif in glycoside hydrolases. Knowledgeable transfer from other GH-family proteins (e.g., GH11 xylanases like Bacillus circulans xylanase, where Glu78 is the nucleophile; GH10, GH5) establishes that Glu/Asp are the canonical nucleophiles in retaining glycosidases. The small protein size (~221 aa), hydrophobic N-terminal signal peptide, and overall composition are consistent with a fungal xylanase. Thus, basic biochemistry (Val ≠ nucleophile) plus family-level knowledge (Glu = nucleophile in glycosidases) plus arithmetic (eliminating C and D) uniquely identifies B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C and D by noting the protein is 221 residues, eliminate A because Valine cannot serve as a nucleophile, and confirm B because Glutamic acid at position 114 in a small secreted protein with signal-peptide-like N-terminus is consistent with the nucleophile in glycoside hydrolase families. No target-specific memorization is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (B) survives elimination: C and D reference non-existent positions, and A assigns nucleophile role to Valine, which is biochemically impossible. No ambiguity exists among the offered choices.


### Important caveats

- The UniProt annotation at position 114 is based on PROSITE-ProRule family assignment (ECO:0000255), i.e., computational inference from GH11 family membership, not direct experimental mutagenesis of this specific protein.
- The model was not given the protein name, organism, or EC number; identification of the protein family must rely on sequence features (size, signal peptide, active-site motif context).
- The proton donor is annotated at position 205 (also Glu), but this is not offered as a distractor, so it does not create ambiguity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options C (position 237) and D (position 341) are trivially eliminated because the protein is only 221 residues long—those positions do not exist. Option A (position 2, Nucleophile) is eliminated because position 2 is Valine (V), which has an isopropyl side chain with no nucleophilic capability; Val is never a catalytic nucleophile in any known enzyme family. This leaves only option B. Position 114 is Glutamic acid (E), and the surrounding sequence context ('LVEYYIVESHG') is consistent with the nucleophile motif in glycoside hydrolases. Knowledgeable transfer from other GH-family proteins (e.g., GH11 xylanases like Bacillus circulans xylanase, where Glu78 is the nucleophile; GH10, GH5) establishes that Glu/Asp are the canonical nucleophiles in retaining glycosidases. The small protein size (~221 aa), hydrophobic N-terminal signal peptide, and overall composition are consistent with a fungal xylanase. Thus, basic biochemistry (Val ≠ nucleophile) plus family-level knowledge (Glu = nucleophile in glycosidases) plus arithmetic (eliminating C and D) uniquely identifies B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D by noting the protein is 221 residues, eliminate A because Valine cannot serve as a nucleophile, and confirm B because Glutamic acid at position 114 in a small secreted protein with signal-peptide-like N-terminus is consistent with the nucleophile in glycoside hydrolase families. No target-specific memorization is required."
  },
  "case_id": "active_site_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G2X5X8 (EIX4_VERDV, Ethylene-inducing xylanase 4, EC 3.2.1.8) annotates position 114 as 'Nucleophile' (evidence ECO:0000255|PROSITE-ProRule:PRU01097, GH11 family). The amino acid at position 114 in the provided sequence is Glutamic acid (E), which is the canonical nucleophile in glycoside hydrolase family 11. The annotation is computational (PROSITE-ProRule family assignment) rather than direct experimental mutagenesis, but it is consistent with the well-established catalytic mechanism of GH11 xylanases. The author's expected answer B matches this annotation."
  },
  "important_caveats": [
    "The UniProt annotation at position 114 is based on PROSITE-ProRule family assignment (ECO:0000255), i.e., computational inference from GH11 family membership, not direct experimental mutagenesis of this specific protein.",
    "The model was not given the protein name, organism, or EC number; identification of the protein family must rely on sequence features (size, signal peptide, active-site motif context).",
    "The proton donor is annotated at position 205 (also Glu), but this is not offered as a distractor, so it does not create ambiguity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (B) survives elimination: C and D reference non-existent positions, and A assigns nucleophile role to Valine, which is biochemically impossible. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G2X5X8 (EIX4_VERDV, Ethylene-inducing xylanase 4, EC 3.2.1.8) annotates position 114 as 'Nucleophile' (evidence ECO:0000255|PROSITE-ProRule:PRU01097, GH11 family). The amino acid at position 114 in the provided sequence is Glutamic acid (E), which is the canonical nucleophile in glycoside hydrolase family 11. The annotation is computational (PROSITE-ProRule family assignment) rather than direct experimental mutagenesis, but it is consistent with the well-established catalytic mechanism of GH11 xylanases. The author's expected answer B matches this annotation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options C (position 237) and D (position 341) are trivially eliminated because the protein is only 221 residues long—those positions do not exist. Option A (position 2, Nucleophile) is eliminated because position 2 is Valine (V), which has an isopropyl side chain with no nucleophilic capability; Val is never a catalytic nucleophile in any known enzyme family. This leaves only option B. Position 114 is Glutamic acid (E), and the surrounding sequence context ('LVEYYIVESHG') is consistent with the nucleophile motif in glycoside hydrolases. Knowledgeable transfer from other GH-family proteins (e.g., GH11 xylanases like Bacillus circulans xylanase, where Glu78 is the nucleophile; GH10, GH5) establishes that Glu/Asp are the canonical nucleophiles in retaining glycosidases. The small protein size (~221 aa), hydrophobic N-terminal signal peptide, and overall composition are consistent with a fungal xylanase. Thus, basic biochemistry (Val ≠ nucleophile) plus family-level knowledge (Glu = nucleophile in glycosidases) plus arithmetic (eliminating C and D) uniquely identifies B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D by noting the protein is 221 residues, eliminate A because Valine cannot serve as a nucleophile, and confirm B because Glutamic acid at position 114 in a small secreted protein with signal-peptide-like N-terminus is consistent with the nucleophile in glycoside hydrolase families. No target-specific memorization is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (B) survives elimination: C and D reference non-existent positions, and A assigns nucleophile role to Valine, which is biochemically impossible. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation at position 114 is based on PROSITE-ProRule family assignment (ECO:0000255), i.e., computational inference from GH11 family membership, not direct experimental mutagenesis of this specific protein.",
    "The model was not given the protein name, organism, or EC number; identification of the protein family must rely on sequence features (size, signal peptide, active-site motif context).",
    "The proton donor is annotated at position 205 (also Glu), but this is not offered as a distractor, so it does not create ambiguity."
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
  "benchmark_sequence_length": 221,
  "benchmark_sequence_sha256": "f1224442080bd4bf3f0c0d75eb06fb931d6239a2cc8449c269e3c313b81db8ac",
  "current_entry_audit": {
    "entryVersion": 60,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 221,
  "current_source_sequence_sha256": "f1224442080bd4bf3f0c0d75eb06fb931d6239a2cc8449c269e3c313b81db8ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G2X5X8",
  "selected_historical_entry_version": 59,
  "selected_historical_record_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "selected_historical_source_sequence_length": 221,
  "selected_historical_source_sequence_sha256": "f1224442080bd4bf3f0c0d75eb06fb931d6239a2cc8449c269e3c313b81db8ac",
  "selected_historical_version": {
    "accession": "G2X5X8",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX4_VERDV",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G2X5X8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":60,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium wilt\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\",\"taxonId\":498257}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX4\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX4\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":114},\"start\":{\"modifier\":\"EXACT\",\"value\":114}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":205},\"start\":{\"modifier\":\"EXACT\",\"value\":205}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:38.390496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012",
  "url": "https://rest.uniprot.org/uniprotkb/G2X5X8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H1",
  "excerpt": "ID   EIX4_VERDV              Reviewed;         221 AA.\nAC   G2X5X8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=Ethylene-inducing xylanase 4 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX4 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX4 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX4 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_05294;\nOS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\nOS   (Verticillium wilt).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=498257;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        114\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        205\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.014577+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c",
  "url": "https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 90. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
