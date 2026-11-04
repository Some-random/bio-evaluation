# transmembrane_0074

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0074.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 41..61

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGLSHSGEIVYIHPSSPVDLFTTCASLPTKPPPSFSDMPSPLFLVSGFLGVCVAYAVANIIRQLLFPNAKEPPVVFHWFPWLGSALTYGKDPYKFLFAARAKYGDVFTFVLLGRNVTVHLGVAGNDFVFNGKETHMNAEEIYGPLCNPVFGEGVVYDCPNSKLMEQKKFVKFGLTTDALKAHVRLIEHEVVNYIKSSRDFKGPSGVINVPPVMAQITIFTAAIALQGPEVRSKLTNEFASLYHDLDGGFSPINFVLPHAPFPHNIKRDRAQLKMRKIYEAIIAERRAGKIPPTTDMISHLMQCSYKNGRPIPDSEISNMMITILMAGQHNSSNIASWIMLHLANEPQLCEELYQEQLDQLADEHGNLPELELHTVEKLKLHSSVVKETLRMHNAIHSIMRLVKQPLPVPNTSWTVPPGHAVLASPGVSANSNEYFLNPTKWDPHRWDDRVIEEDDESEMVDYGYGRTSRGTKSAYLPFGGGRHRCIGEKFAYLNLEVITAVMVRNFRFKNVDGRVDVPGTDYSTMFSRPLEPAEICWERR

[Multiple Choices]
A. 41..61; 374..395
B. 41..61
C. 3..23
D. 44..62
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

> The sequence-matched UniProt record annotates residues 41–61 as a helical transmembrane region. This is computational annotation evidence, not experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a prominent hydrophobic stretch around residues 42–61, consistent with the N-terminal membrane anchor found in microsomal cytochrome P450 proteins. That feature favors B over the nonmatching early interval in C and the internal interval in A; the predicted interval also provides a credible basis for preferring B to the slightly shifted D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and family-level knowledge meaningfully identifies the membrane-spanning region without requiring the exact protein's database record. The precise endpoints are less certain from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The wording asks for a segment that crosses the membrane, and D is a shifted interval that still covers most of the same hydrophobic stretch. The evidence supports B's exact annotation, but the biological wording alone does not make the boundary distinction from D sharp.


### Important caveats

- The cited transmembrane annotation is computational, not experimental.
- Option A also includes 41–61 but adds a separate interval, so it does not cleanly identify only the supported region.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a prominent hydrophobic stretch around residues 42–61, consistent with the N-terminal membrane anchor found in microsomal cytochrome P450 proteins. That feature favors B over the nonmatching early interval in C and the internal interval in A; the predicted interval also provides a credible basis for preferring B to the slightly shifted D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and family-level knowledge meaningfully identifies the membrane-spanning region without requiring the exact protein's database record. The precise endpoints are less certain from sequence alone."
  },
  "case_id": "transmembrane_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residues 41–61 as a helical transmembrane region. This is computational annotation evidence, not experimental confirmation."
  },
  "important_caveats": [
    "The cited transmembrane annotation is computational, not experimental.",
    "Option A also includes 41–61 but adds a separate interval, so it does not cleanly identify only the supported region."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The wording asks for a segment that crosses the membrane, and D is a shifted interval that still covers most of the same hydrophobic stretch. The evidence supports B's exact annotation, but the biological wording alone does not make the boundary distinction from D sharp."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residues 41–61 as a helical transmembrane region. This is computational annotation evidence, not experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a prominent hydrophobic stretch around residues 42–61, consistent with the N-terminal membrane anchor found in microsomal cytochrome P450 proteins. That feature favors B over the nonmatching early interval in C and the internal interval in A; the predicted interval also provides a credible basis for preferring B to the slightly shifted D.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and family-level knowledge meaningfully identifies the membrane-spanning region without requiring the exact protein's database record. The precise endpoints are less certain from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The wording asks for a segment that crosses the membrane, and D is a shifted interval that still covers most of the same hydrophobic stretch. The evidence supports B's exact annotation, but the biological wording alone does not make the boundary distinction from D sharp."
  },
  "important_caveats": [
    "The cited transmembrane annotation is computational, not experimental.",
    "Option A also includes 41–61 but adds a separate interval, so it does not cleanly identify only the supported region."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXV0 annotates a single transmembrane helical region at exactly 41..61 (evidence ECO:0000255, by similarity). The sequence at positions 41-61 (PLFLVSGFLGVCVAYAVANI I) is predominantly hydrophobic over 21 residues, consistent with a single-pass TM helix. The annotation is computational (by similarity), not experimentally verified, but it directly supports choice B. No other TM region is annotated, making the second region in option A (374..395) unsupported.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish the choices through several transferable lines of reasoning: (1) Hydrophobicity window analysis of the sequence clearly identifies a ~20-residue hydrophobic stretch around positions 41-61 as the only plausible TM helix; option C (3..23) contains many polar/charged residues (H, S, G, E, H, S, P, D, T, T) and is not hydrophobic enough; option A's second region (374..395: TVEKLKHSSVVKETLRMHNAI) is heavily charged/polar and clearly not TM. (2) The distinction between B (41..61) and D (44..62) hinges on residue 62 = Arg, a positively charged residue. Transmembrane helices of ~20 residues span the ~30 Å hydrophobic core of the lipid bilayer; placing a charged Arg within this core is energetically highly unfavorable. This is a well-established principle in membrane protein biophysics. Option B ends at Ile61 (hydrophobic), while D includes Arg62 (charged), making D less consistent with a TM helix. (3) CYP51 (sterol 14-alpha demethylase) family knowledge: CYP51 enzymes across fungi, plants, and animals are anchored to the ER membrane by a single N-terminal transmembrane helix typically located within the first ~60 residues. This family-level pattern points to a single TM region near the N-terminus, consistent with B and inconsistent with the additional region in A. (4) Option B's 21-residue length matches the canonical TM helix length (~19-23 residues) for a single-pass membrane protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of sequence-level hydrophobicity analysis, the biophysical principle that charged residues (Arg62) are incompatible with the hydrophobic TM core, and CYP51-family knowledge about a single N-terminal TM helix provides a concrete, transferable argument that meaningfully distinguishes B from the other options. The charged Arg62 at the terminus of D is the key discriminator against D, while hydrophobicity eliminates A and C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are clearly eliminated by hydrophobicity analysis. Between B and D, the presence of a charged Arg62 at the end of D provides a principled biophysical discriminator. While the boundary difference is small (3 residues), the charged-residue argument is a standard and well-known criterion in TM helix prediction, making B the more defensible choice.


### Important caveats

- The UniProt annotation at 41..61 carries evidence code ECO:0000255 (by similarity), meaning it is a computational/transferred prediction, not an experimentally determined TM boundary.
- The distinction between B (41..61) and D (44..62) is narrow; in practice, TM helix boundary predictions vary by a few residues. The Arg62 argument is the primary discriminator but is not absolute—some TM helices do contain charged residues at their termini.
- The protein is a CYP51 sterol 14-alpha demethylase from Pyrenophora dematioidea; CYP51 family TM helix location knowledge is transferable but the exact boundary for this specific protein is a computational prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish the choices through several transferable lines of reasoning: (1) Hydrophobicity window analysis of the sequence clearly identifies a ~20-residue hydrophobic stretch around positions 41-61 as the only plausible TM helix; option C (3..23) contains many polar/charged residues (H, S, G, E, H, S, P, D, T, T) and is not hydrophobic enough; option A's second region (374..395: TVEKLKHSSVVKETLRMHNAI) is heavily charged/polar and clearly not TM. (2) The distinction between B (41..61) and D (44..62) hinges on residue 62 = Arg, a positively charged residue. Transmembrane helices of ~20 residues span the ~30 Å hydrophobic core of the lipid bilayer; placing a charged Arg within this core is energetically highly unfavorable. This is a well-established principle in membrane protein biophysics. Option B ends at Ile61 (hydrophobic), while D includes Arg62 (charged), making D less consistent with a TM helix. (3) CYP51 (sterol 14-alpha demethylase) family knowledge: CYP51 enzymes across fungi, plants, and animals are anchored to the ER membrane by a single N-terminal transmembrane helix typically located within the first ~60 residues. This family-level pattern points to a single TM region near the N-terminus, consistent with B and inconsistent with the additional region in A. (4) Option B's 21-residue length matches the canonical TM helix length (~19-23 residues) for a single-pass membrane protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of sequence-level hydrophobicity analysis, the biophysical principle that charged residues (Arg62) are incompatible with the hydrophobic TM core, and CYP51-family knowledge about a single N-terminal TM helix provides a concrete, transferable argument that meaningfully distinguishes B from the other options. The charged Arg62 at the terminus of D is the key discriminator against D, while hydrophobicity eliminates A and C."
  },
  "case_id": "transmembrane_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXV0 annotates a single transmembrane helical region at exactly 41..61 (evidence ECO:0000255, by similarity). The sequence at positions 41-61 (PLFLVSGFLGVCVAYAVANI I) is predominantly hydrophobic over 21 residues, consistent with a single-pass TM helix. The annotation is computational (by similarity), not experimentally verified, but it directly supports choice B. No other TM region is annotated, making the second region in option A (374..395) unsupported."
  },
  "important_caveats": [
    "The UniProt annotation at 41..61 carries evidence code ECO:0000255 (by similarity), meaning it is a computational/transferred prediction, not an experimentally determined TM boundary.",
    "The distinction between B (41..61) and D (44..62) is narrow; in practice, TM helix boundary predictions vary by a few residues. The Arg62 argument is the primary discriminator but is not absolute—some TM helices do contain charged residues at their termini.",
    "The protein is a CYP51 sterol 14-alpha demethylase from Pyrenophora dematioidea; CYP51 family TM helix location knowledge is transferable but the exact boundary for this specific protein is a computational prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly eliminated by hydrophobicity analysis. Between B and D, the presence of a charged Arg62 at the end of D provides a principled biophysical discriminator. While the boundary difference is small (3 residues), the charged-residue argument is a standard and well-known criterion in TM helix prediction, making B the more defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXV0 annotates a single transmembrane helical region at exactly 41..61 (evidence ECO:0000255, by similarity). The sequence at positions 41-61 (PLFLVSGFLGVCVAYAVANI I) is predominantly hydrophobic over 21 residues, consistent with a single-pass TM helix. The annotation is computational (by similarity), not experimentally verified, but it directly supports choice B. No other TM region is annotated, making the second region in option A (374..395) unsupported.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish the choices through several transferable lines of reasoning: (1) Hydrophobicity window analysis of the sequence clearly identifies a ~20-residue hydrophobic stretch around positions 41-61 as the only plausible TM helix; option C (3..23) contains many polar/charged residues (H, S, G, E, H, S, P, D, T, T) and is not hydrophobic enough; option A's second region (374..395: TVEKLKHSSVVKETLRMHNAI) is heavily charged/polar and clearly not TM. (2) The distinction between B (41..61) and D (44..62) hinges on residue 62 = Arg, a positively charged residue. Transmembrane helices of ~20 residues span the ~30 Å hydrophobic core of the lipid bilayer; placing a charged Arg within this core is energetically highly unfavorable. This is a well-established principle in membrane protein biophysics. Option B ends at Ile61 (hydrophobic), while D includes Arg62 (charged), making D less consistent with a TM helix. (3) CYP51 (sterol 14-alpha demethylase) family knowledge: CYP51 enzymes across fungi, plants, and animals are anchored to the ER membrane by a single N-terminal transmembrane helix typically located within the first ~60 residues. This family-level pattern points to a single TM region near the N-terminus, consistent with B and inconsistent with the additional region in A. (4) Option B's 21-residue length matches the canonical TM helix length (~19-23 residues) for a single-pass membrane protein.",
    "missing_item_specific_fact": "",
    "reason": "The combination of sequence-level hydrophobicity analysis, the biophysical principle that charged residues (Arg62) are incompatible with the hydrophobic TM core, and CYP51-family knowledge about a single N-terminal TM helix provides a concrete, transferable argument that meaningfully distinguishes B from the other options. The charged Arg62 at the terminus of D is the key discriminator against D, while hydrophobicity eliminates A and C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly eliminated by hydrophobicity analysis. Between B and D, the presence of a charged Arg62 at the end of D provides a principled biophysical discriminator. While the boundary difference is small (3 residues), the charged-residue argument is a standard and well-known criterion in TM helix prediction, making B the more defensible choice."
  },
  "important_caveats": [
    "The UniProt annotation at 41..61 carries evidence code ECO:0000255 (by similarity), meaning it is a computational/transferred prediction, not an experimentally determined TM boundary.",
    "The distinction between B (41..61) and D (44..62) is narrow; in practice, TM helix boundary predictions vary by a few residues. The Arg62 argument is the primary discriminator but is not absolute—some TM helices do contain charged residues at their termini.",
    "The protein is a CYP51 sterol 14-alpha demethylase from Pyrenophora dematioidea; CYP51 family TM helix location knowledge is transferable but the exact boundary for this specific protein is a computational prediction."
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
  "benchmark_sequence_length": 540,
  "benchmark_sequence_sha256": "7892b58432fcc729eff0e7866dfac47e6055a778388a0efd41daa5ff7eb4bdd5",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 540,
  "current_source_sequence_sha256": "7892b58432fcc729eff0e7866dfac47e6055a778388a0efd41daa5ff7eb4bdd5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXV0",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "selected_historical_source_sequence_length": 540,
  "selected_historical_source_sequence_sha256": "7892b58432fcc729eff0e7866dfac47e6055a778388a0efd41daa5ff7eb4bdd5",
  "selected_historical_version": {
    "accession": "P0DXV0",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "LAN1_PYRDE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXV0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Helminthosporium dematioideum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Pleosporomycetidae\",\"Pleosporales\",\"Pleosporineae\",\"Pleosporaceae\",\"Pyrenophora\"],\"scientificName\":\"Pyrenophora dematioidea\",\"taxonId\":139229}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Ergosterol biosynthesis protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Lanomycin biosynthesis cluster protein 1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.154\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Sterol 14-alpha demethylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":61},\"start\":{\"modifier\":\"EXACT\",\"value\":41}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu N.\",\"Abramyan E.D.\",\"Cheng W.\",\"Perlatti B.\",\"Harvey C.J.B.\",\"Bills G.F.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33857369\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.1c01516\"}],\"citationType\":\"journal article\",\"firstPage\":\"6043\",\"id\":\"33857369\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"6047\",\"publicationDate\":\"2021\",\"title\":\"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"TTI-1096\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   LAN1_PYRDE              Reviewed;         540 AA.\nAC   P0DXV0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Sterol 14-alpha demethylase {ECO:0000303|PubMed:33857369};\nDE            EC=1.14.14.154 {ECO:0000305|PubMed:33857369};\nDE   AltName: Full=Cytochrome P450 monooxygenase {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Ergosterol biosynthesis protein {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Lanomycin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};\nGN   Name=ORF1 {ECO:0000303|PubMed:33857369};\nOS   Pyrenophora dematioidea (Helminthosporium dematioideum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Pleosporomycetidae; Pleosporales; Pleosporineae; Pleosporaceae;\nOC   Pyrenophora.\nOX   NCBI_TaxID=139229;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=TTI-1096;\nRX   PubMed=33857369; DOI=10.1021/jacs.1c01516;\nRA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,\nRA   Tang Y.;\nRT   \"Targeted genome mining reveals the biosynthetic gene clusters of natural\nRT   product CYP51 inhibitors.\";\nRL   J. Am. Chem. Soc. 143:6043-6047(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        41..61\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 197-199",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 74. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
