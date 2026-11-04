# transmembrane_0060

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0060.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 37..57; 333..353

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGLLLKMKMQNQHHPLASKLQEQTGNKRYTFIQAHRAWLLKLMFLWILLMALISRIIYSKMDVGTKVRRKEVLGSLCDQRARMLQDQFSVSVNHVHALAILVSTFHYYRNPSAIDQETFAEYTARTAFERPLLSGVAYAQRVVNSEREQFEKQHGVVIKTMEREASPVRDEYAPVIFAQETVSYLESIDMMSGEEDRENIMRARATGKAVLTSPFRLLGSHHLGVVLTFPVYKSKLPPNPTTEELIKATAGYVGGSFDVESLVENLLGQLAGHQAILVNVYDVTNSSDPLIMYGNQYEEGDVSLVHESKLDFGDPYRKHQMICRYHQKAPPNWTALSTAILFFVILLLIGYILYGAGNHIVKVEDDFHEMQELKVRAEAADVAKSQFLATVSHEIRTPMNGILGMLGLLLRTELNSTQRDYAQTAQACGKALIALINEVLDRAKIEAGKLELEAVPFDLRSILDDVLSLFSEKSRHKGLELAVFVSDKVPDIVMGDPGRFRQIVTNLVGNSVKFTERGHIFVKVHLSENRKPVTNGKHETYRNGGSEEVVHASGGYNLKTLSGYEAADERNNWDNFNHLIADEEFFCDASTKKVASNEFYEQVTLMVCVEDTGIGIPFSAQDRIFMPFVQADSSTSRNYGGTGIGLSISKCLVELMGGQINFISRPQVGSTFSFTADFGIFKKNPITEVKKVNYEDLPSSFRGLKAVVVDGKPVRAAVTRYHLKRLGIQVKVANAINKAVSLCGKNGASSTGLFQPDIIFVEKDSWVCGEDGIFSVRQLDWKQNGHIFKMPQMILLATNISNDEFDKAKSAGFSDTVIMKPLRASMVGACLQQVLGTGKKRQLGKEMPNGSTSVRSLLFGKKILVVDDNVVNRRVAAGALKNFGADVKCADSGKAALEMLQFPHKFDACFMDIQMPEMDGFEATRRIREMERTANEETNSECGERKSEFHLPILAMTADVIHATYEECLKCGMDGYVSKPFEEENLYQAVAKFFQTKPTSVDS

[Multiple Choices]
A. 37..57; 333..353
B. 222..242
C. 333..353
D. 37..57; 330..352
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

> The matched UniProt entry annotates helical transmembrane regions at 37–57 and 333–353. These are computational annotations (ECO:0000255), not direct experimental demonstrations of membrane crossing.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly hydrophobic stretch around residues 37–57 and another around 333–353, consistent with membrane-spanning helices; this distinguishes A from B and C. Between A and D, A better fits the second helix: D starts at residue 330, a proline, and includes the following asparagine, while A captures the more plausible helix span and includes the terminal glycine at 353. Hydrophobicity and typical helix length provide a credible, though not certain, basis for preferring A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The two hydrophobic sequence segments and standard transmembrane-helix patterns support the keyed choice without requiring recall of this protein's database entry. Exact helix boundaries are inherently less certain from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is a close boundary alternative for the second segment, but its inclusion of a proline and asparagine before the hydrophobic stretch and omission of residue 353 make A the more credible choice.


### Important caveats

- The supporting database annotations are computational rather than experimental.
- The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic stretch around residues 37–57 and another around 333–353, consistent with membrane-spanning helices; this distinguishes A from B and C. Between A and D, A better fits the second helix: D starts at residue 330, a proline, and includes the following asparagine, while A captures the more plausible helix span and includes the terminal glycine at 353. Hydrophobicity and typical helix length provide a credible, though not certain, basis for preferring A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The two hydrophobic sequence segments and standard transmembrane-helix patterns support the keyed choice without requiring recall of this protein's database entry. Exact helix boundaries are inherently less certain from sequence alone."
  },
  "case_id": "transmembrane_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates helical transmembrane regions at 37–57 and 333–353. These are computational annotations (ECO:0000255), not direct experimental demonstrations of membrane crossing."
  },
  "important_caveats": [
    "The supporting database annotations are computational rather than experimental.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is a close boundary alternative for the second segment, but its inclusion of a proline and asparagine before the hydrophobic stretch and omission of residue 353 make A the more credible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates helical transmembrane regions at 37–57 and 333–353. These are computational annotations (ECO:0000255), not direct experimental demonstrations of membrane crossing.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic stretch around residues 37–57 and another around 333–353, consistent with membrane-spanning helices; this distinguishes A from B and C. Between A and D, A better fits the second helix: D starts at residue 330, a proline, and includes the following asparagine, while A captures the more plausible helix span and includes the terminal glycine at 353. Hydrophobicity and typical helix length provide a credible, though not certain, basis for preferring A.",
    "missing_item_specific_fact": "",
    "reason": "The two hydrophobic sequence segments and standard transmembrane-helix patterns support the keyed choice without requiring recall of this protein's database entry. Exact helix boundaries are inherently less certain from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is a close boundary alternative for the second segment, but its inclusion of a proline and asparagine before the hydrophobic stretch and omission of residue 353 make A the more credible choice."
  },
  "important_caveats": [
    "The supporting database annotations are computational rather than experimental.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (evidence codes C5, C6, H3, H4) explicitly lists two Transmembrane Helical features at 37..57 and 333..353, matching choice A exactly. However, the evidence code is ECO:0000255 (By similarity), indicating computational inference by homology rather than direct experimental determination. The annotation is consistent with the protein being a two-component histidine kinase/cytokinin receptor (CRE1) with a canonical two-TM-helix sensor domain architecture.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The critical distinction is between A (37..57; 333..353) and D (37..57; 330..352). The second TM helix in option D includes positions 330-332 (Ala-Pro-Pro). Two consecutive proline residues are well-established alpha-helix breakers: proline cannot donate a backbone amide hydrogen bond and introduces a rigid kink, making it highly incompatible with a continuous transmembrane alpha-helix. Starting the helix at W333 (option A) avoids these prolines and places a hydrophobic aromatic residue (Trp) at the membrane-water interface, consistent with the 'aromatic belt' principle for TM helix boundaries. Ending at L353 (option A) rather than I352 (option D) is a minor difference, but the PP exclusion at the N-terminal boundary is the decisive structural argument. Option B (222..242) is easily eliminated because it contains charged residues (K233, K235) and multiple prolines (P230, P237, P238, P240), making it incompatible with a TM helix. Option C (333..353) is incomplete, omitting the clearly hydrophobic segment at 37..57 (AWLLKLMFLWILLMALISRII).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can apply general knowledge of proline as a helix breaker, the aromatic-residue-at-membrane-interface principle, and the hydrophobicity requirements of TM helices to distinguish the boundaries. The PP at positions 331-332 is visible directly in the supplied sequence and provides a concrete structural reason to prefer starting at 333 over 330. This is transferable knowledge from TM helix biophysics, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the boundary difference between A and D is only 3 residues at the start and 1 at the end, the presence of two consecutive prolines at 331-332 provides a clear structural argument against including them in a helical TM domain. Option B is eliminated by charged residues and prolines; option C is incomplete. The PP argument, while not mathematically airtight (some TM helices tolerate isolated prolines), strongly disfavors two consecutive prolines in a TM helix core.


### Important caveats

- The UniProt TM annotations use evidence code ECO:0000255 (By similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries. The 'correct' boundaries reflect a database convention rather than a single experimental measurement.
- TM helix boundary prediction is inherently imprecise; different tools and algorithms can differ by 2-5 residues. The A vs D distinction (333 vs 330 start) is at the edge of typical prediction uncertainty.
- The protein is a plant histidine kinase (CRE1 from Medicago truncatula) with a canonical two-TM sensor domain architecture, which is consistent with exactly two TM helices.
- The reviewer-only evidence confirms the sequence matches the UniProt entry G7LCC3 (sequence version 2, 1003 aa), but this accession was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The critical distinction is between A (37..57; 333..353) and D (37..57; 330..352). The second TM helix in option D includes positions 330-332 (Ala-Pro-Pro). Two consecutive proline residues are well-established alpha-helix breakers: proline cannot donate a backbone amide hydrogen bond and introduces a rigid kink, making it highly incompatible with a continuous transmembrane alpha-helix. Starting the helix at W333 (option A) avoids these prolines and places a hydrophobic aromatic residue (Trp) at the membrane-water interface, consistent with the 'aromatic belt' principle for TM helix boundaries. Ending at L353 (option A) rather than I352 (option D) is a minor difference, but the PP exclusion at the N-terminal boundary is the decisive structural argument. Option B (222..242) is easily eliminated because it contains charged residues (K233, K235) and multiple prolines (P230, P237, P238, P240), making it incompatible with a TM helix. Option C (333..353) is incomplete, omitting the clearly hydrophobic segment at 37..57 (AWLLKLMFLWILLMALISRII).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can apply general knowledge of proline as a helix breaker, the aromatic-residue-at-membrane-interface principle, and the hydrophobicity requirements of TM helices to distinguish the boundaries. The PP at positions 331-332 is visible directly in the supplied sequence and provides a concrete structural reason to prefer starting at 333 over 330. This is transferable knowledge from TM helix biophysics, not a lookup of this specific protein's annotation."
  },
  "case_id": "transmembrane_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (evidence codes C5, C6, H3, H4) explicitly lists two Transmembrane Helical features at 37..57 and 333..353, matching choice A exactly. However, the evidence code is ECO:0000255 (By similarity), indicating computational inference by homology rather than direct experimental determination. The annotation is consistent with the protein being a two-component histidine kinase/cytokinin receptor (CRE1) with a canonical two-TM-helix sensor domain architecture."
  },
  "important_caveats": [
    "The UniProt TM annotations use evidence code ECO:0000255 (By similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries. The 'correct' boundaries reflect a database convention rather than a single experimental measurement.",
    "TM helix boundary prediction is inherently imprecise; different tools and algorithms can differ by 2-5 residues. The A vs D distinction (333 vs 330 start) is at the edge of typical prediction uncertainty.",
    "The protein is a plant histidine kinase (CRE1 from Medicago truncatula) with a canonical two-TM sensor domain architecture, which is consistent with exactly two TM helices.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry G7LCC3 (sequence version 2, 1003 aa), but this accession was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the boundary difference between A and D is only 3 residues at the start and 1 at the end, the presence of two consecutive prolines at 331-332 provides a clear structural argument against including them in a helical TM domain. Option B is eliminated by charged residues and prolines; option C is incomplete. The PP argument, while not mathematically airtight (some TM helices tolerate isolated prolines), strongly disfavors two consecutive prolines in a TM helix core."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (evidence codes C5, C6, H3, H4) explicitly lists two Transmembrane Helical features at 37..57 and 333..353, matching choice A exactly. However, the evidence code is ECO:0000255 (By similarity), indicating computational inference by homology rather than direct experimental determination. The annotation is consistent with the protein being a two-component histidine kinase/cytokinin receptor (CRE1) with a canonical two-TM-helix sensor domain architecture.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The critical distinction is between A (37..57; 333..353) and D (37..57; 330..352). The second TM helix in option D includes positions 330-332 (Ala-Pro-Pro). Two consecutive proline residues are well-established alpha-helix breakers: proline cannot donate a backbone amide hydrogen bond and introduces a rigid kink, making it highly incompatible with a continuous transmembrane alpha-helix. Starting the helix at W333 (option A) avoids these prolines and places a hydrophobic aromatic residue (Trp) at the membrane-water interface, consistent with the 'aromatic belt' principle for TM helix boundaries. Ending at L353 (option A) rather than I352 (option D) is a minor difference, but the PP exclusion at the N-terminal boundary is the decisive structural argument. Option B (222..242) is easily eliminated because it contains charged residues (K233, K235) and multiple prolines (P230, P237, P238, P240), making it incompatible with a TM helix. Option C (333..353) is incomplete, omitting the clearly hydrophobic segment at 37..57 (AWLLKLMFLWILLMALISRII).",
    "missing_item_specific_fact": "",
    "reason": "A model can apply general knowledge of proline as a helix breaker, the aromatic-residue-at-membrane-interface principle, and the hydrophobicity requirements of TM helices to distinguish the boundaries. The PP at positions 331-332 is visible directly in the supplied sequence and provides a concrete structural reason to prefer starting at 333 over 330. This is transferable knowledge from TM helix biophysics, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the boundary difference between A and D is only 3 residues at the start and 1 at the end, the presence of two consecutive prolines at 331-332 provides a clear structural argument against including them in a helical TM domain. Option B is eliminated by charged residues and prolines; option C is incomplete. The PP argument, while not mathematically airtight (some TM helices tolerate isolated prolines), strongly disfavors two consecutive prolines in a TM helix core."
  },
  "important_caveats": [
    "The UniProt TM annotations use evidence code ECO:0000255 (By similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries. The 'correct' boundaries reflect a database convention rather than a single experimental measurement.",
    "TM helix boundary prediction is inherently imprecise; different tools and algorithms can differ by 2-5 residues. The A vs D distinction (333 vs 330 start) is at the edge of typical prediction uncertainty.",
    "The protein is a plant histidine kinase (CRE1 from Medicago truncatula) with a canonical two-TM sensor domain architecture, which is consistent with exactly two TM helices.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry G7LCC3 (sequence version 2, 1003 aa), but this accession was not provided to the evaluated model."
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
  "benchmark_sequence_length": 1003,
  "benchmark_sequence_sha256": "7101a9a6b74fa50d6e114ab0532171d5d35bde533b69ae26373f47846b5f18a6",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-01",
    "sequenceVersion": 2
  },
  "current_record_sha256": "d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1003,
  "current_source_sequence_sha256": "7101a9a6b74fa50d6e114ab0532171d5d35bde533b69ae26373f47846b5f18a6",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 84,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G7LCC3",
  "selected_historical_entry_version": 84,
  "selected_historical_record_sha256": "026a53a56a232a58bac5538cce4d8ffd143200e6dd576544a82b544bfe64f8af",
  "selected_historical_source_sequence_length": 1003,
  "selected_historical_source_sequence_sha256": "7101a9a6b74fa50d6e114ab0532171d5d35bde533b69ae26373f47846b5f18a6",
  "selected_historical_version": {
    "accession": "G7LCC3",
    "database": "Swiss-Prot",
    "entryVersion": 84,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRE1_MEDTR",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G7LCC3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:09.681318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b",
  "url": "https://rest.uniprot.org/uniprotkb/G7LCC3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-01\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:09.681318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b",
  "url": "https://rest.uniprot.org/uniprotkb/G7LCC3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Barrel medic\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Fabales\",\"Fabaceae\",\"Papilionoideae\",\"50 kb inversion clade\",\"NPAAA clade\",\"Hologalegina\",\"IRL clade\",\"Trifolieae\",\"Medicago\"],\"scientificName\":\"Medicago truncatula\",\"synonyms\":[\"Medicago tribuloides\"],\"taxonId\":3880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:09.681318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b",
  "url": "https://rest.uniprot.org/uniprotkb/G7LCC3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34630499\",\"source\":\"PubMed\"}],\"value\":\"Cytokinin receptor CYTOKININ RESPONSE 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34630499\",\"source\":\"PubMed\"}],\"value\":\"Cytokinin receptor CRE1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34630499\",\"source\":\"PubMed\"}],\"value\":\"MtCRE1\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9C5U0\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.13.3\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34630499\",\"source\":\"PubMed\"}],\"value\":\"Histidine kinase CRE1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:09.681318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b",
  "url": "https://rest.uniprot.org/uniprotkb/G7LCC3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":57},\"start\":{\"modifier\":\"EXACT\",\"value\":37}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:09.681318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b",
  "url": "https://rest.uniprot.org/uniprotkb/G7LCC3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":353},\"start\":{\"modifier\":\"EXACT\",\"value\":333}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:09.681318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b",
  "url": "https://rest.uniprot.org/uniprotkb/G7LCC3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7LCC3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Tran L.H.\",\"Urbanowicz A.\",\"Jasinski M.\",\"Jaskolski M.\",\"Ruszkowski M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34630499\"},{\"database\":\"DOI\",\"id\":\"10.3389/fpls.2021.756341\"}],\"citationType\":\"journal article\",\"firstPage\":\"756341\",\"id\":\"34630499\",\"journal\":\"Front. Plant Sci.\",\"lastPage\":\"756341\",\"publicationDate\":\"2021\",\"title\":\"3D domain swapping dimerization of the receiver domain of cytokinin receptor CRE1 from Arabidopsis thaliana and Medicago truncatula.\",\"volume\":\"12\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7P8E\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.50 ANGSTROMS) OF 351-994 IN COMPLEX WITH CA(2+)\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:09.681318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d540f6305c9d128af7aa4ffb15254c3d79657e1e42f99e3b7f07f6438cabd19b",
  "url": "https://rest.uniprot.org/uniprotkb/G7LCC3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7LCC3?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H1",
  "excerpt": "ID   CRE1_MEDTR              Reviewed;        1003 AA.\nAC   G7LCC3; A0A0C3Y896;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2014, sequence version 2.\nDT   28-JAN-2026, entry version 84.\nDE   RecName: Full=Histidine kinase CRE1 {ECO:0000303|PubMed:34630499};\nDE            EC=2.7.13.3 {ECO:0000250|UniProtKB:Q9C5U0};\nDE   AltName: Full=Cytokinin receptor CYTOKININ RESPONSE 1 {ECO:0000303|PubMed:34630499};\nDE            Short=Cytokinin receptor CRE1 {ECO:0000303|PubMed:34630499};\nDE            Short=MtCRE1 {ECO:0000303|PubMed:34630499};\nGN   Name=CRE1 {ECO:0000303|PubMed:34630499};\nGN   OrderedLocusNames=MTR_8g106150 {ECO:0000312|EMBL:AET05490.2};\nGN   ORFNames=MtrunA17_Chr8g0392301 {ECO:0000312|EMBL:RHN43850.1};\nOS   Medicago truncatula (Barrel medic) (Medicago tribuloides).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;\nOC   NPAAA clade; Hologalegina; IRL clade; Trifolieae; Medicago.\nOX   NCBI_TaxID=3880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.918748+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "026a53a56a232a58bac5538cce4d8ffd143200e6dd576544a82b544bfe64f8af",
  "url": "https://rest.uniprot.org/unisave/G7LCC3?format=txt&versions=84"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7LCC3?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0007744|PDB:7P8E}\nRP   X-RAY CRYSTALLOGRAPHY (2.50 ANGSTROMS) OF 351-994 IN COMPLEX WITH CA(2+).\nRX   PubMed=34630499; DOI=10.3389/fpls.2021.756341;\nRA   Tran L.H., Urbanowicz A., Jasinski M., Jaskolski M., Ruszkowski M.;\nRT   \"3D domain swapping dimerization of the receiver domain of cytokinin\nRT   receptor CRE1 from Arabidopsis thaliana and Medicago truncatula.\";\nRL   Front. Plant Sci. 12:756341-756341(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.918748+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "026a53a56a232a58bac5538cce4d8ffd143200e6dd576544a82b544bfe64f8af",
  "url": "https://rest.uniprot.org/unisave/G7LCC3?format=txt&versions=84"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7LCC3?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        37..57\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.918748+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 187-189",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "026a53a56a232a58bac5538cce4d8ffd143200e6dd576544a82b544bfe64f8af",
  "url": "https://rest.uniprot.org/unisave/G7LCC3?format=txt&versions=84"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7LCC3?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        333..353\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.918748+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 190-192",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "026a53a56a232a58bac5538cce4d8ffd143200e6dd576544a82b544bfe64f8af",
  "url": "https://rest.uniprot.org/unisave/G7LCC3?format=txt&versions=84"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 60. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
