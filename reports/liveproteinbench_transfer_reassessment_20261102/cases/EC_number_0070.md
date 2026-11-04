# EC_number_0070

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0070.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 2.3.1.193

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTVKVRFDKEVREYAKGEKVKDSVLKITETALAQALEKFHRRMIVIEGDTLKKAELAGILAGASARVLSDIVGELIEKRLRDESEDKIEVLYATDALGEETFGRKRYEAFRKHFDVLAGSEVNVTAVTFKHTREILGRTYDLLILDMSYDYSPNDLGRIIETVRGGGLIFILAHPFEKWKDMWTGFHKSLVTPPYTIEDVKKRFNRRLIRKFTQHDGIYIITESGKAKKKPKKSKSQAKIRARKGVEIPEETLFPKELYEMALTRGQVEVLKAFEELVDKEGMLVLTADRGRGKSVSVGIAAIGLAVALKKRTRIVVTAPELENVQSLFRFAKRALEKLGFKPYVVEEKGLIKELYARKIGLRYYPPAEGYKKNADLYILDEAAGIHVPILHKYLNKPRVVYSSTIHGYEGAGRGFSVKFLKKAREKRSFKELHMEEPIRYAYGDPIEKWLFDVLLLDAEPVELTEEDYELIKRKEVYLEEPDLDDWFENDREDLRHFVGIYILAHYRNRPSDVALLADAPHHEARVLRLKNGKIVTAVQIAKEGGIPKNVIDKMAKGYKPRGNIIPDMMVKHHYLKEFARLKGYRIVRIATHPDAMDMGLGSKALELLEKEAREKGLDWIGSGFGASEELVRFWVRNGFAVVHLSPARNPVSGEFTAIVLKPISKKAKELIKKANDEFRIRFTEWLGDTHRELEPEIARWLFETPFGEAVDYPIHLTEIQKKRLDAFTGKVLTYDTVVDAVKPIVKLYFLDGWMKPYLDERQIKLLIYRVLQAHSWEETAKLIDRTEMFTMIEVRDIIRGLWYYYKRLLT

[Multiple Choices]
A. 2.3.1.193
B. 2.3.1.322
C. 3.2.1.8
D. 1.1.1.336
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

> The sequence-matched UniProt annotation assigns EC 2.3.1.193 to TmcA and gives the corresponding tRNA cytidine acetylation reaction. The annotation cites both a HAMAP rule and experimental evidence (PubMed 32555463), so the key is supported by computational annotation and experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence is consistent with the TmcA family of RNA-modification enzymes, whose transferable family-level function is ATP-dependent cytidine acetylation of tRNA. That family inference points to EC 2.3.1.193 among the choices; the other options describe different reaction classes or a different acetyltransferase activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference can meaningfully distinguish the tRNA cytidine acetyltransferase option without knowing this exact protein's database record. The inference is probabilistic, and the two acetyltransferase options make family recognition important, but the TmcA-family assignment provides a concrete basis for selecting A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative is comparably supported once the sequence is recognized as belonging to the TmcA tRNA-modification family.


### Important caveats

- The reviewer-only source confirms an exact sequence match, but its accession and annotations were not part of the original input.
- The family-level inference is not direct experimental proof for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is consistent with the TmcA family of RNA-modification enzymes, whose transferable family-level function is ATP-dependent cytidine acetylation of tRNA. That family inference points to EC 2.3.1.193 among the choices; the other options describe different reaction classes or a different acetyltransferase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can meaningfully distinguish the tRNA cytidine acetyltransferase option without knowing this exact protein's database record. The inference is probabilistic, and the two acetyltransferase options make family recognition important, but the TmcA-family assignment provides a concrete basis for selecting A."
  },
  "case_id": "EC_number_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.3.1.193 to TmcA and gives the corresponding tRNA cytidine acetylation reaction. The annotation cites both a HAMAP rule and experimental evidence (PubMed 32555463), so the key is supported by computational annotation and experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only source confirms an exact sequence match, but its accession and annotations were not part of the original input.",
    "The family-level inference is not direct experimental proof for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported once the sequence is recognized as belonging to the TmcA tRNA-modification family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.3.1.193 to TmcA and gives the corresponding tRNA cytidine acetylation reaction. The annotation cites both a HAMAP rule and experimental evidence (PubMed 32555463), so the key is supported by computational annotation and experimental evidence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence is consistent with the TmcA family of RNA-modification enzymes, whose transferable family-level function is ATP-dependent cytidine acetylation of tRNA. That family inference points to EC 2.3.1.193 among the choices; the other options describe different reaction classes or a different acetyltransferase activity.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can meaningfully distinguish the tRNA cytidine acetyltransferase option without knowing this exact protein's database record. The inference is probabilistic, and the two acetyltransferase options make family recognition important, but the TmcA-family assignment provides a concrete basis for selecting A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported once the sequence is recognized as belonging to the TmcA tRNA-modification family."
  },
  "important_caveats": [
    "The reviewer-only source confirms an exact sequence match, but its accession and annotations were not part of the original input.",
    "The family-level inference is not direct experimental proof for this sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5JHC6 (TmcA from Thermococcus kodakarensis, sequence matched at 811 AA) is annotated with EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase) with both HAMAP-Rule (ECO:0000255|MF_01886) and experimental evidence (ECO:0000269|PubMed:32555463, Nature 2020). The catalytic activity comments confirm acetylation of cytidine(34) in elongator tRNA(Met) using acetyl-CoA and ATP.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~300 residues contain a recognizable GNAT (GCN5-related N-acetyltransferase) fold, identifiable by the 'GDT' motif and the characteristic β-sheet/α-helix architecture of acetyltransferases. This immediately eliminates C (EC 3.2.1.8, a hydrolase/glycosidase) and D (EC 1.1.1.336, an oxidoreductase). The C-terminal ~500 residues display a DNA/RNA methyltransferase-like fold (motif I 'GMLVLT', motif II 'DRGRGK', and downstream catalytic-loop motifs), which in TmcA/NAT10 family members serves as an RNA-binding/substrate-recognition module rather than a methyl-transfer catalytic domain. The combined GNAT + MTase-like RNA-binding architecture is a well-known hallmark of the TmcA/NAT10 family of RNA acetyltransferases. Among the remaining choices (both EC 2.3.1.x acetyltransferases), EC 2.3.1.193 specifically denotes a tRNA cytidine acetyltransferase whose architecture matches this GNAT+MTase-fold combination, whereas EC 2.3.1.322 (if it exists as a distinct entry) would be expected to have a different domain architecture for a different substrate class. The hyperthermophile-like sequence composition (high charged-residue density, short loops) is also consistent with archaeal TmcA homologs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GNAT fold identifies the enzyme class (acetyltransferase, EC 2.3.1.x), eliminating C and D. The C-terminal methyltransferase-like fold functioning as an RNA-binding module is a transferable family-level feature (shared with NAT10/TmcA homologs across Archaea and Eukarya) that points specifically to an RNA acetyltransferase rather than a protein or small-molecule acetyltransferase, distinguishing A from B. This is a legitimate family-architecture inference, not mere memorization of one protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C (hydrolase) and D (oxidoreductase) are clearly excluded by the GNAT fold. Between A and B, the RNA-binding MTase-like fold in the C-terminus provides a meaningful architectural basis to favor the tRNA acetyltransferase (2.3.1.193) over a hypothetical non-RNA acetyltransferase (2.3.1.322). No other option is defensible given the domain architecture.


### Important caveats

- EC 2.3.1.322 may be a very recent, obscure, or non-existent EC number; its exact identity could not be independently confirmed from the supplied evidence. If it were also an RNA acetyltransferase with a similar architecture, the A-vs-B distinction would weaken.
- The GNAT fold identification relies on pattern recognition of the 'GDT' motif and overall fold topology visible in the sequence; no structural coordinates were provided.
- The C-terminal MTase-like fold is used for RNA binding in TmcA, not for methyl transfer; misidentifying it as a methyltransferase catalytic domain could mislead toward an EC 2.1.x answer, but no such option was offered.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~300 residues contain a recognizable GNAT (GCN5-related N-acetyltransferase) fold, identifiable by the 'GDT' motif and the characteristic β-sheet/α-helix architecture of acetyltransferases. This immediately eliminates C (EC 3.2.1.8, a hydrolase/glycosidase) and D (EC 1.1.1.336, an oxidoreductase). The C-terminal ~500 residues display a DNA/RNA methyltransferase-like fold (motif I 'GMLVLT', motif II 'DRGRGK', and downstream catalytic-loop motifs), which in TmcA/NAT10 family members serves as an RNA-binding/substrate-recognition module rather than a methyl-transfer catalytic domain. The combined GNAT + MTase-like RNA-binding architecture is a well-known hallmark of the TmcA/NAT10 family of RNA acetyltransferases. Among the remaining choices (both EC 2.3.1.x acetyltransferases), EC 2.3.1.193 specifically denotes a tRNA cytidine acetyltransferase whose architecture matches this GNAT+MTase-fold combination, whereas EC 2.3.1.322 (if it exists as a distinct entry) would be expected to have a different domain architecture for a different substrate class. The hyperthermophile-like sequence composition (high charged-residue density, short loops) is also consistent with archaeal TmcA homologs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GNAT fold identifies the enzyme class (acetyltransferase, EC 2.3.1.x), eliminating C and D. The C-terminal methyltransferase-like fold functioning as an RNA-binding module is a transferable family-level feature (shared with NAT10/TmcA homologs across Archaea and Eukarya) that points specifically to an RNA acetyltransferase rather than a protein or small-molecule acetyltransferase, distinguishing A from B. This is a legitimate family-architecture inference, not mere memorization of one protein's record."
  },
  "case_id": "EC_number_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5JHC6 (TmcA from Thermococcus kodakarensis, sequence matched at 811 AA) is annotated with EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase) with both HAMAP-Rule (ECO:0000255|MF_01886) and experimental evidence (ECO:0000269|PubMed:32555463, Nature 2020). The catalytic activity comments confirm acetylation of cytidine(34) in elongator tRNA(Met) using acetyl-CoA and ATP."
  },
  "important_caveats": [
    "EC 2.3.1.322 may be a very recent, obscure, or non-existent EC number; its exact identity could not be independently confirmed from the supplied evidence. If it were also an RNA acetyltransferase with a similar architecture, the A-vs-B distinction would weaken.",
    "The GNAT fold identification relies on pattern recognition of the 'GDT' motif and overall fold topology visible in the sequence; no structural coordinates were provided.",
    "The C-terminal MTase-like fold is used for RNA binding in TmcA, not for methyl transfer; misidentifying it as a methyltransferase catalytic domain could mislead toward an EC 2.1.x answer, but no such option was offered."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C (hydrolase) and D (oxidoreductase) are clearly excluded by the GNAT fold. Between A and B, the RNA-binding MTase-like fold in the C-terminus provides a meaningful architectural basis to favor the tRNA acetyltransferase (2.3.1.193) over a hypothetical non-RNA acetyltransferase (2.3.1.322). No other option is defensible given the domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5JHC6 (TmcA from Thermococcus kodakarensis, sequence matched at 811 AA) is annotated with EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase) with both HAMAP-Rule (ECO:0000255|MF_01886) and experimental evidence (ECO:0000269|PubMed:32555463, Nature 2020). The catalytic activity comments confirm acetylation of cytidine(34) in elongator tRNA(Met) using acetyl-CoA and ATP.",
    "evidence_ids": ["C4", "C5", "C9", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~300 residues contain a recognizable GNAT (GCN5-related N-acetyltransferase) fold, identifiable by the 'GDT' motif and the characteristic β-sheet/α-helix architecture of acetyltransferases. This immediately eliminates C (EC 3.2.1.8, a hydrolase/glycosidase) and D (EC 1.1.1.336, an oxidoreductase). The C-terminal ~500 residues display a DNA/RNA methyltransferase-like fold (motif I 'GMLVLT', motif II 'DRGRGK', and downstream catalytic-loop motifs), which in TmcA/NAT10 family members serves as an RNA-binding/substrate-recognition module rather than a methyl-transfer catalytic domain. The combined GNAT + MTase-like RNA-binding architecture is a well-known hallmark of the TmcA/NAT10 family of RNA acetyltransferases. Among the remaining choices (both EC 2.3.1.x acetyltransferases), EC 2.3.1.193 specifically denotes a tRNA cytidine acetyltransferase whose architecture matches this GNAT+MTase-fold combination, whereas EC 2.3.1.322 (if it exists as a distinct entry) would be expected to have a different domain architecture for a different substrate class. The hyperthermophile-like sequence composition (high charged-residue density, short loops) is also consistent with archaeal TmcA homologs.",
    "missing_item_specific_fact": "",
    "reason": "The GNAT fold identifies the enzyme class (acetyltransferase, EC 2.3.1.x), eliminating C and D. The C-terminal methyltransferase-like fold functioning as an RNA-binding module is a transferable family-level feature (shared with NAT10/TmcA homologs across Archaea and Eukarya) that points specifically to an RNA acetyltransferase rather than a protein or small-molecule acetyltransferase, distinguishing A from B. This is a legitimate family-architecture inference, not mere memorization of one protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C (hydrolase) and D (oxidoreductase) are clearly excluded by the GNAT fold. Between A and B, the RNA-binding MTase-like fold in the C-terminus provides a meaningful architectural basis to favor the tRNA acetyltransferase (2.3.1.193) over a hypothetical non-RNA acetyltransferase (2.3.1.322). No other option is defensible given the domain architecture."
  },
  "important_caveats": [
    "EC 2.3.1.322 may be a very recent, obscure, or non-existent EC number; its exact identity could not be independently confirmed from the supplied evidence. If it were also an RNA acetyltransferase with a similar architecture, the A-vs-B distinction would weaken.",
    "The GNAT fold identification relies on pattern recognition of the 'GDT' motif and overall fold topology visible in the sequence; no structural coordinates were provided.",
    "The C-terminal MTase-like fold is used for RNA binding in TmcA, not for methyl transfer; misidentifying it as a methyltransferase catalytic domain could mislead toward an EC 2.1.x answer, but no such option was offered."
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
  "benchmark_sequence_length": 811,
  "benchmark_sequence_sha256": "54beed0f1c05c798248d154a7e8ad0383a6ab7c487ffdd87fd0c8eb435930b3f",
  "current_entry_audit": {
    "entryVersion": 117,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-02-15",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 811,
  "current_source_sequence_sha256": "54beed0f1c05c798248d154a7e8ad0383a6ab7c487ffdd87fd0c8eb435930b3f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 116,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5JHC6",
  "selected_historical_entry_version": 116,
  "selected_historical_record_sha256": "c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7",
  "selected_historical_source_sequence_length": 811,
  "selected_historical_source_sequence_sha256": "54beed0f1c05c798248d154a7e8ad0383a6ab7c487ffdd87fd0c8eb435930b3f",
  "selected_historical_version": {
    "accession": "Q5JHC6",
    "database": "Swiss-Prot",
    "entryVersion": 116,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "TMCA_THEKO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5JHC6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:20.774043+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JHC6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":117,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-02-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:20.774043+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JHC6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Pyrococcus kodakaraensis (strain KOD1)\",\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Thermococcus\"],\"scientificName\":\"Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)\",\"taxonId\":69014}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:20.774043+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JHC6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"value\":\"TkNAT10\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.193\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"}],\"value\":\"tRNA(Met) cytidine acetyltransferase TmcA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:20.774043+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JHC6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.193\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:43788\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10693\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:31:20.774043+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JHC6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in RNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82211\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15704\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19834\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:31:20.774043+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JHC6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:53876\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:13670\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:13671\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:31:20.774043+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JHC6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in mRNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:58480\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15145\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:31:20.774043+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JHC6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Sas-Chen A.\",\"Thomas J.M.\",\"Matzov D.\",\"Taoka M.\",\"Nance K.D.\",\"Nir R.\",\"Bryson K.M.\",\"Shachar R.\",\"Liman G.L.S.\",\"Burkhart B.W.\",\"Gamage S.T.\",\"Nobe Y.\",\"Briney C.A.\",\"Levy M.J.\",\"Fuchs R.T.\",\"Robb G.B.\",\"Hartmann J.\",\"Sharma S.\",\"Lin Q.\",\"Florens L.\",\"Washburn M.P.\",\"Isobe T.\",\"Santangelo T.J.\",\"Shalev-Benami M.\",\"Meier J.L.\",\"Schwartz S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32555463\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-020-2418-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"638\",\"id\":\"32555463\",\"journal\":\"Nature\",\"lastPage\":\"643\",\"publicationDate\":\"2020\",\"title\":\"Dynamic RNA acetylation revealed by quantitative cross-evolutionary mapping.\",\"volume\":\"583\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC BAA-918 / TS559\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:20.774043+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JHC6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H1",
  "excerpt": "ID   TMCA_THEKO              Reviewed;         811 AA.\nAC   Q5JHC6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-FEB-2005, sequence version 1.\nDT   28-JAN-2026, entry version 116.\nDE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};\nDE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000269|PubMed:32555463};\nDE   AltName: Full=TkNAT10 {ECO:0000303|PubMed:32555463};\nGN   Name=tmcA {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000303|PubMed:30605516};\nGN   Synonyms=Nat10 {ECO:0000303|PubMed:32555463};\nGN   OrderedLocusNames=TK0754 {ECO:0000312|EMBL:BAD84943.1};\nOS   Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)\nOS   (Pyrococcus kodakaraensis (strain KOD1)).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Thermococcus.\nOX   NCBI_TaxID=69014;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:24.956546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7",
  "url": "https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};\nDE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000269|PubMed:32555463};\nDE   AltName: Full=TkNAT10 {ECO:0000303|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:24.956546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7",
  "url": "https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC BAA-918 / JCM 12380 / KOD1;\nRX   PubMed=30605516; DOI=10.1093/nar/gky1313;\nRA   Orita I., Futatsuishi R., Adachi K., Ohira T., Kaneko A., Minowa K.,\nRA   Suzuki M., Tamura T., Nakamura S., Imanaka T., Suzuki T., Fukui T.;\nRT   \"Random mutagenesis of a hyperthermophilic archaeon identified tRNA\nRT   modifications associated with cellular hyperthermotolerance.\";\nRL   Nucleic Acids Res. 47:1964-1976(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:24.956546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7",
  "url": "https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, INDUCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC BAA-918 / TS559;\nRX   PubMed=32555463; DOI=10.1038/s41586-020-2418-2;\nRA   Sas-Chen A., Thomas J.M., Matzov D., Taoka M., Nance K.D., Nir R.,\nRA   Bryson K.M., Shachar R., Liman G.L.S., Burkhart B.W., Gamage S.T., Nobe Y.,\nRA   Briney C.A., Levy M.J., Fuchs R.T., Robb G.B., Hartmann J., Sharma S.,\nRA   Lin Q., Florens L., Washburn M.P., Isobe T., Santangelo T.J.,\nRA   Shalev-Benami M., Meier J.L., Schwartz S.;\nRT   \"Dynamic RNA acetylation revealed by quantitative cross-evolutionary\nRT   mapping.\";\nRL   Nature 583:638-643(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:24.956546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7",
  "url": "https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O =\nCC         N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate +\nCC         CoA + H(+); Xref=Rhea:RHEA:43788, Rhea:RHEA-COMP:10693, Rhea:RHEA-\nCC         COMP:10694, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         EC=2.3.1.193; Evidence={ECO:0000255|HAMAP-Rule:MF_01886,\nCC         ECO:0000269|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:24.956546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7",
  "url": "https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in RNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:82211, Rhea:RHEA-COMP:15704, Rhea:RHEA-COMP:19834,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:24.956546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7",
  "url": "https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in tRNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:53876, Rhea:RHEA-COMP:13670, Rhea:RHEA-COMP:13671,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000269|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:24.956546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7",
  "url": "https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in mRNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:58480, Rhea:RHEA-COMP:15145, Rhea:RHEA-COMP:15146,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000269|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:24.956546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7",
  "url": "https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
