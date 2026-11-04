# EC_number_0168

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0168.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 3.2.1.8

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
A. 3.2.1.20
B. 1.14.11.65
C. 3.2.1.8
D. 2.7.7.80
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

> The sequence-matched UniProt annotation assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans, supporting choice C. The EC assignment is attributed to a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal secretion signal followed by a compact, aromatic-rich fungal glycoside-hydrolase-like region, consistent with a secreted xylanase family. Transferable knowledge of fungal xylanases and their compact catalytic domains makes EC 3.2.1.8 a meaningful fit among these choices; the other options describe an alpha-glucosidase, an oxygenase, or a nucleotidyltransferase and fit the sequence context less well.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and the sharply different offered enzyme classes can distinguish C without recalling this exact protein's database entry. The inference is probabilistic; sequence alone does not establish the annotated reaction experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered choices represent substantially different enzyme activities, and the sequence context most strongly supports the xylanase option.


### Important caveats

- The reviewer evidence matches the supplied sequence, but the EC annotation is computationally assigned rather than shown here as an experimentally measured activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal secretion signal followed by a compact, aromatic-rich fungal glycoside-hydrolase-like region, consistent with a secreted xylanase family. Transferable knowledge of fungal xylanases and their compact catalytic domains makes EC 3.2.1.8 a meaningful fit among these choices; the other options describe an alpha-glucosidase, an oxygenase, or a nucleotidyltransferase and fit the sequence context less well.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the sharply different offered enzyme classes can distinguish C without recalling this exact protein's database entry. The inference is probabilistic; sequence alone does not establish the annotated reaction experimentally."
  },
  "case_id": "EC_number_0168",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans, supporting choice C. The EC assignment is attributed to a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the EC annotation is computationally assigned rather than shown here as an experimentally measured activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices represent substantially different enzyme activities, and the sequence context most strongly supports the xylanase option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0168",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans, supporting choice C. The EC assignment is attributed to a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal secretion signal followed by a compact, aromatic-rich fungal glycoside-hydrolase-like region, consistent with a secreted xylanase family. Transferable knowledge of fungal xylanases and their compact catalytic domains makes EC 3.2.1.8 a meaningful fit among these choices; the other options describe an alpha-glucosidase, an oxygenase, or a nucleotidyltransferase and fit the sequence context less well.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the sharply different offered enzyme classes can distinguish C without recalling this exact protein's database entry. The inference is probabilistic; sequence alone does not establish the annotated reaction experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices represent substantially different enzyme activities, and the sequence context most strongly supports the xylanase option."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the EC annotation is computationally assigned rather than shown here as an experimentally measured activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A384JXV5 (EIX1_BOTFB, Ethylene-inducing xylanase 1 from Botrytis cinerea) is annotated with EC 3.2.1.8 (Endo-1,4-beta-xylanase), matching the expected answer C. The sequence matches (281 aa, SHA-256 confirmed). The EC annotation carries evidence code ECO:0000255 (PROSITE-ProRule:PRU01097), indicating a computational family-based inference rather than direct experimental characterization. The alternative name 'Endo-1,4-beta-xylanase EIX1' and the catalytic activity description ('Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans') are consistent. The PubMed reference (33205907) discusses EIX-like proteins from Verticillium dahliae, supporting the xylanase/elicitor identity. The annotation is database-level and computational, but it is the standard basis for EC assignment in the absence of direct kinetic data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits several transferable features that distinguish GH10 xylanases (EC 3.2.1.8) from the other offered choices. (1) The N-terminal hydrophobic stretch 'MVSYKAFLITLAAVTRVLTYPANSS' is a classic fungal signal peptide, indicating a secreted enzyme, consistent with extracellular glycoside hydrolases. (2) The motif 'WSGNGN' (around residues ~60-66) is a well-documented conserved signature of glycoside hydrolase family 10 (GH10), learned from numerous other GH10 xylanases across fungi and bacteria. (3) The region 'GWTTSPLIEYY' contains the catalytic nucleophile Glu in a conserved GH10 context; a second catalytic Glu is embedded in the 'GTVVSDGATYKIY' stretch, matching the two-Glu catalytic mechanism of GH10. (4) The overall length (~281 aa), (β/α)8 TIM-barrel architecture implied by the alternating hydrophobic/polar segments, and the C-terminal cysteine-rich region (disulfide-stabilized secreted domain) are hallmarks of fungal GH10 xylanases. These features allow elimination of: A (3.2.1.20, α-amylase/GH13, which has distinct 'NEP' and 'DNE' motifs absent here), B (1.14.11.65, a 2-oxoglutarate-dependent dioxygenase requiring HXD/E…H metal-binding motifs absent here), and D (2.7.7.80, a transferase with no sequence resemblance). GH10 → EC 3.2.1.8 is a standard family-level mapping. The reasoning relies on motifs shared across many GH10 proteins, not on a fact unique to this exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the GH10 family signature motifs (WSGNGN, catalytic Glu positions in GWTTSPLIEYY and GTVVSDGATYKIY), the secreted fungal architecture, and the absence of features diagnostic of GH13 amylases, dioxygenases, or transferases. These are transferable family-level sequence features learned from many other GH10 xylanases. The mapping GH10 → EC 3.2.1.8 is standard enzymology. No fact unique to this particular protein record is required to distinguish among the four choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different EC classes (hydrolase, oxidoreductase, transferase) and within hydrolases two different GH families (GH10 xylanase vs GH13 amylase). The GH10-specific motifs present in the sequence (WSGNGN, catalytic Glu context) cleanly exclude GH13 (A), the absence of metal-binding HXD/E…H motifs excludes the dioxygenase (B), and the absence of any transferase-like fold or motif excludes (D). Only C (3.2.1.8) is consistent with the observed sequence features.


### Important caveats

- The EC 3.2.1.8 annotation in UniProt is based on PROSITE-ProRule (ECO:0000255), a computational family-based inference, not on direct experimental kinetic characterization of this specific protein. The protein is also known as an ethylene-inducing elicitor (EIX), and its elicitor activity may involve additional biological functions beyond xylan hydrolysis.
- The PubMed reference (33205907) discusses EIX-like proteins from Verticillium dahliae and their perception by plant receptors, supporting the xylanase/elicitor identity but not providing direct enzymatic kinetics for this exact protein.
- The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must rely on sequence-intrinsic features and transferable family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits several transferable features that distinguish GH10 xylanases (EC 3.2.1.8) from the other offered choices. (1) The N-terminal hydrophobic stretch 'MVSYKAFLITLAAVTRVLTYPANSS' is a classic fungal signal peptide, indicating a secreted enzyme, consistent with extracellular glycoside hydrolases. (2) The motif 'WSGNGN' (around residues ~60-66) is a well-documented conserved signature of glycoside hydrolase family 10 (GH10), learned from numerous other GH10 xylanases across fungi and bacteria. (3) The region 'GWTTSPLIEYY' contains the catalytic nucleophile Glu in a conserved GH10 context; a second catalytic Glu is embedded in the 'GTVVSDGATYKIY' stretch, matching the two-Glu catalytic mechanism of GH10. (4) The overall length (~281 aa), (β/α)8 TIM-barrel architecture implied by the alternating hydrophobic/polar segments, and the C-terminal cysteine-rich region (disulfide-stabilized secreted domain) are hallmarks of fungal GH10 xylanases. These features allow elimination of: A (3.2.1.20, α-amylase/GH13, which has distinct 'NEP' and 'DNE' motifs absent here), B (1.14.11.65, a 2-oxoglutarate-dependent dioxygenase requiring HXD/E…H metal-binding motifs absent here), and D (2.7.7.80, a transferase with no sequence resemblance). GH10 → EC 3.2.1.8 is a standard family-level mapping. The reasoning relies on motifs shared across many GH10 proteins, not on a fact unique to this exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the GH10 family signature motifs (WSGNGN, catalytic Glu positions in GWTTSPLIEYY and GTVVSDGATYKIY), the secreted fungal architecture, and the absence of features diagnostic of GH13 amylases, dioxygenases, or transferases. These are transferable family-level sequence features learned from many other GH10 xylanases. The mapping GH10 → EC 3.2.1.8 is standard enzymology. No fact unique to this particular protein record is required to distinguish among the four choices."
  },
  "case_id": "EC_number_0168",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A384JXV5 (EIX1_BOTFB, Ethylene-inducing xylanase 1 from Botrytis cinerea) is annotated with EC 3.2.1.8 (Endo-1,4-beta-xylanase), matching the expected answer C. The sequence matches (281 aa, SHA-256 confirmed). The EC annotation carries evidence code ECO:0000255 (PROSITE-ProRule:PRU01097), indicating a computational family-based inference rather than direct experimental characterization. The alternative name 'Endo-1,4-beta-xylanase EIX1' and the catalytic activity description ('Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans') are consistent. The PubMed reference (33205907) discusses EIX-like proteins from Verticillium dahliae, supporting the xylanase/elicitor identity. The annotation is database-level and computational, but it is the standard basis for EC assignment in the absence of direct kinetic data."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation in UniProt is based on PROSITE-ProRule (ECO:0000255), a computational family-based inference, not on direct experimental kinetic characterization of this specific protein. The protein is also known as an ethylene-inducing elicitor (EIX), and its elicitor activity may involve additional biological functions beyond xylan hydrolysis.",
    "The PubMed reference (33205907) discusses EIX-like proteins from Verticillium dahliae and their perception by plant receptors, supporting the xylanase/elicitor identity but not providing direct enzymatic kinetics for this exact protein.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must rely on sequence-intrinsic features and transferable family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC classes (hydrolase, oxidoreductase, transferase) and within hydrolases two different GH families (GH10 xylanase vs GH13 amylase). The GH10-specific motifs present in the sequence (WSGNGN, catalytic Glu context) cleanly exclude GH13 (A), the absence of metal-binding HXD/E…H motifs excludes the dioxygenase (B), and the absence of any transferase-like fold or motif excludes (D). Only C (3.2.1.8) is consistent with the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0168",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A384JXV5 (EIX1_BOTFB, Ethylene-inducing xylanase 1 from Botrytis cinerea) is annotated with EC 3.2.1.8 (Endo-1,4-beta-xylanase), matching the expected answer C. The sequence matches (281 aa, SHA-256 confirmed). The EC annotation carries evidence code ECO:0000255 (PROSITE-ProRule:PRU01097), indicating a computational family-based inference rather than direct experimental characterization. The alternative name 'Endo-1,4-beta-xylanase EIX1' and the catalytic activity description ('Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans') are consistent. The PubMed reference (33205907) discusses EIX-like proteins from Verticillium dahliae, supporting the xylanase/elicitor identity. The annotation is database-level and computational, but it is the standard basis for EC assignment in the absence of direct kinetic data.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits several transferable features that distinguish GH10 xylanases (EC 3.2.1.8) from the other offered choices. (1) The N-terminal hydrophobic stretch 'MVSYKAFLITLAAVTRVLTYPANSS' is a classic fungal signal peptide, indicating a secreted enzyme, consistent with extracellular glycoside hydrolases. (2) The motif 'WSGNGN' (around residues ~60-66) is a well-documented conserved signature of glycoside hydrolase family 10 (GH10), learned from numerous other GH10 xylanases across fungi and bacteria. (3) The region 'GWTTSPLIEYY' contains the catalytic nucleophile Glu in a conserved GH10 context; a second catalytic Glu is embedded in the 'GTVVSDGATYKIY' stretch, matching the two-Glu catalytic mechanism of GH10. (4) The overall length (~281 aa), (β/α)8 TIM-barrel architecture implied by the alternating hydrophobic/polar segments, and the C-terminal cysteine-rich region (disulfide-stabilized secreted domain) are hallmarks of fungal GH10 xylanases. These features allow elimination of: A (3.2.1.20, α-amylase/GH13, which has distinct 'NEP' and 'DNE' motifs absent here), B (1.14.11.65, a 2-oxoglutarate-dependent dioxygenase requiring HXD/E…H metal-binding motifs absent here), and D (2.7.7.80, a transferase with no sequence resemblance). GH10 → EC 3.2.1.8 is a standard family-level mapping. The reasoning relies on motifs shared across many GH10 proteins, not on a fact unique to this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the GH10 family signature motifs (WSGNGN, catalytic Glu positions in GWTTSPLIEYY and GTVVSDGATYKIY), the secreted fungal architecture, and the absence of features diagnostic of GH13 amylases, dioxygenases, or transferases. These are transferable family-level sequence features learned from many other GH10 xylanases. The mapping GH10 → EC 3.2.1.8 is standard enzymology. No fact unique to this particular protein record is required to distinguish among the four choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC classes (hydrolase, oxidoreductase, transferase) and within hydrolases two different GH families (GH10 xylanase vs GH13 amylase). The GH10-specific motifs present in the sequence (WSGNGN, catalytic Glu context) cleanly exclude GH13 (A), the absence of metal-binding HXD/E…H motifs excludes the dioxygenase (B), and the absence of any transferase-like fold or motif excludes (D). Only C (3.2.1.8) is consistent with the observed sequence features."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation in UniProt is based on PROSITE-ProRule (ECO:0000255), a computational family-based inference, not on direct experimental kinetic characterization of this specific protein. The protein is also known as an ethylene-inducing elicitor (EIX), and its elicitor activity may involve additional biological functions beyond xylan hydrolysis.",
    "The PubMed reference (33205907) discusses EIX-like proteins from Verticillium dahliae and their perception by plant receptors, supporting the xylanase/elicitor identity but not providing direct enzymatic kinetics for this exact protein.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must rely on sequence-intrinsic features and transferable family knowledge."
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

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C6",
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
  "excerpt": "DE   RecName: Full=Ethylene-inducing xylanase 1 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX1 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX1 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.003931+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 168. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
