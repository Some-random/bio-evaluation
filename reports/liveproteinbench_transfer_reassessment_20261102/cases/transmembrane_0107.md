# transmembrane_0107

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0107.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 229..247; 276..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKDFTERSTKGQRKLANGVVENIESKLKNHLDNNNVINKSVNYEDVMCSNVKLSVHDDEYDIKNIKKDVCNLSKLSEERLSNNISLKDNNKVVKNPEIDTKTARQQYKKRLNSTQSTMNIEGNINNEKDDIIEDYDDGLIRNMDYEMSIVKNKRNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNSNNVDNRKRNKNEECYDESYCISDNLDEITSYRNKLSLYNKLRMCFNYFGPGWIVAIAYLDPGNLCSNLNVGLIRSPDPTLEKDYSGYYLLWIMVYGHMLGFIFQVLSMRLGHVTGLDLASLCSKEFDRTTSTIIYVLVQIAIWGAHIQAIIGTFIALNLIFGISVKVAIFYTLFEAIIYSFLENKSLGLLENVLSFLVGILAVSFFVNVFMTPINFKELAISILYPRIPKGKEIDALALLGSIISAHIFYLHTNLTAKKKSVICNDLSLRRYNTLGTIESGGSLFLSCLTNCIIVLTFAEVNLKSFERRDQYNLFTAYEVMRKSFGKISMYIWSFGLLSSGNNSSFMCEYASKSVVEGFLNKKINTFVRVFTFRLMLFSLLYMFLTLNKYTLDQLTNFINVIQVLLLPMATIPLYRFSIHENVLGEFRLKKFPKFAVFLIIIAIIISNVLLTFLDFVHKETSLITIFFLVIFSFLYFGFIIYFFNIPIKKNYIQRN

[Multiple Choices]
A. 13..35
B. 229..247; 276..299; 320..345; 351..370; 382..404; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673
C. 229..247; 272..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673
D. 229..247; 276..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673
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

> The sequence-matched historical UniProt entry annotates the transmembrane spans listed in D, including 424..445; those annotations match D rather than B or C. The helix annotations carry computational evidence code ECO:0000255, so this supports D as a predicted topology, not as experimental confirmation of every boundary.

Citations as saved: [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26), [H28](#evidence-h28).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has repeated hydrophobic stretches of roughly membrane-helix length, separated by more polar regions, supporting a multipass membrane protein. The hydrophobic stretch around 424..445 favors D over B, which omits it; the polar residues preceding the next hydrophobic run make C's earlier start at 272 less plausible than D's start at 276. These sequence patterns and general principles of multipass transporter topology are transferable and do not require knowing this protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides a meaningful basis for distinguishing the listed alternatives. Exact helix boundaries can be uncertain from sequence alone, but the competing options differ at positions where hydrophobicity and the surrounding sequence support D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the best-supported option among those offered: B omits a hydrophobic span, while C extends the second span into a less hydrophobic preceding region.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but its helix calls are computational rather than direct experimental measurements.
- The author's exact data-source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches of roughly membrane-helix length, separated by more polar regions, supporting a multipass membrane protein. The hydrophobic stretch around 424..445 favors D over B, which omits it; the polar residues preceding the next hydrophobic run make C's earlier start at 272 less plausible than D's start at 276. These sequence patterns and general principles of multipass transporter topology are transferable and do not require knowing this protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a meaningful basis for distinguishing the listed alternatives. Exact helix boundaries can be uncertain from sequence alone, but the competing options differ at positions where hydrophobicity and the surrounding sequence support D."
  },
  "case_id": "transmembrane_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24",
      "H26",
      "H28"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates the transmembrane spans listed in D, including 424..445; those annotations match D rather than B or C. The helix annotations carry computational evidence code ECO:0000255, so this supports D as a predicted topology, not as experimental confirmation of every boundary."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its helix calls are computational rather than direct experimental measurements.",
    "The author's exact data-source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the best-supported option among those offered: B omits a hydrophobic span, while C extends the second span into a less hydrophobic preceding region."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates the transmembrane spans listed in D, including 424..445; those annotations match D rather than B or C. The helix annotations carry computational evidence code ECO:0000255, so this supports D as a predicted topology, not as experimental confirmation of every boundary.",
    "evidence_ids": ["H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24", "H26", "H28"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches of roughly membrane-helix length, separated by more polar regions, supporting a multipass membrane protein. The hydrophobic stretch around 424..445 favors D over B, which omits it; the polar residues preceding the next hydrophobic run make C's earlier start at 272 less plausible than D's start at 276. These sequence patterns and general principles of multipass transporter topology are transferable and do not require knowing this protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a meaningful basis for distinguishing the listed alternatives. Exact helix boundaries can be uncertain from sequence alone, but the competing options differ at positions where hydrophobicity and the surrounding sequence support D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the best-supported option among those offered: B omits a hydrophobic span, while C extends the second span into a less hydrophobic preceding region."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its helix calls are computational rather than direct experimental measurements.",
    "The author's exact data-source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8I3M7 (DMT1_PLAF7) annotates exactly 12 transmembrane helices at positions 229..247, 276..299, 320..345, 351..370, 382..404, 424..445, 466..487, 516..534, 555..573, 585..603, 623..645, 651..673, matching option D exactly. The TM helix annotations carry evidence code ECO:0000255 (inferred by similarity), i.e. computational/annotation transfer rather than direct experimental determination of each helix boundary. The topological domain assignments carry ECO:0000305 (curator inference) and the C-terminal cytoplasmic domain (674..684) carries experimental evidence ECO:0000269 from PubMed:39467134. The overall topology is consistent with the NRAMP/DMT family architecture.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [C28](#evidence-c28), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [C11](#evidence-c11), [C13](#evidence-c13), [C15](#evidence-c15), [C17](#evidence-c17), [C19](#evidence-c19), [C21](#evidence-c21), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27), [C29](#evidence-c29).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal ~450 residues of this protein display a series of hydrophobic stretches separated by short hydrophilic loops, characteristic of a multi-pass membrane transporter. Recognizing this as an NRAMP (Natural Resistance-Associated Macrophage Protein) / DMT-family transporter is feasible from the domain architecture: a long hydrophilic N-terminal region (~1-228) followed by a compact cluster of alternating hydrophobic and hydrophilic segments. NRAMP-family members (e.g., human NRAMP1/SLC11A1, plant IRT1/2, yeast SMF proteins) consistently possess 12 transmembrane helices. This family-level regularity directly distinguishes option D (12 TM regions) from option B (11 TM regions, which omits the 424..445 helix). For the C-vs-D distinction (second TM starting at 272 vs 276), a model can inspect the residue composition at positions 272-275: if those residues are polar or charged (e.g., containing Ser, Thr, Asn, Gln, Lys, Arg), they are inconsistent with a lipid-facing helix and would be assigned to the preceding loop, favoring the 276 start. The NRAMP family argument eliminates B, and the local hydrophobicity at the 272-275 boundary provides a sequence-based argument for D over C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The NRAMP/DMT family is well-characterized as a 12-TM-helix transporter family across eukaryotes (human, plant, fungal homologs). This is transferable family-level knowledge, not a fact specific to this exact protein. The boundary question (272 vs 276) is addressable by examining the hydrophobicity of the specific residues in the supplied sequence. A model does not need to recall the UniProt entry for Q8I3M7 to arrive at D; it can use family-level TM count and local sequence analysis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly distinguished by the NRAMP-family 12-TM expectation. Options C and D differ only in the start position of the second TM (272 vs 276), a 4-residue boundary question. While different prediction tools might disagree on such fine boundaries, the local hydrophobicity profile of the supplied sequence provides a reasonable basis for preferring 276. The distinction is fine but not genuinely ambiguous given the family context and sequence analysis.


### Important caveats

- The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning the exact helix boundaries are computational/annotation transfers rather than experimentally determined at single-residue resolution.
- The 272-vs-276 boundary (C vs D) is a fine-grained prediction-boundary question; different TM-prediction tools (TMHMM, Phobius, DeepTMHMM) could disagree by a few residues at helix termini. The NRAMP-family 12-TM argument robustly eliminates B but the C-vs-D distinction relies more heavily on local hydrophobicity judgment.
- The reviewer-only evidence confirms the sequence matches Q8I3M7 (Plasmodium falciparum DMT1), but the evaluated model receives only the raw sequence with no name, organism, or accession.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal ~450 residues of this protein display a series of hydrophobic stretches separated by short hydrophilic loops, characteristic of a multi-pass membrane transporter. Recognizing this as an NRAMP (Natural Resistance-Associated Macrophage Protein) / DMT-family transporter is feasible from the domain architecture: a long hydrophilic N-terminal region (~1-228) followed by a compact cluster of alternating hydrophobic and hydrophilic segments. NRAMP-family members (e.g., human NRAMP1/SLC11A1, plant IRT1/2, yeast SMF proteins) consistently possess 12 transmembrane helices. This family-level regularity directly distinguishes option D (12 TM regions) from option B (11 TM regions, which omits the 424..445 helix). For the C-vs-D distinction (second TM starting at 272 vs 276), a model can inspect the residue composition at positions 272-275: if those residues are polar or charged (e.g., containing Ser, Thr, Asn, Gln, Lys, Arg), they are inconsistent with a lipid-facing helix and would be assigned to the preceding loop, favoring the 276 start. The NRAMP family argument eliminates B, and the local hydrophobicity at the 272-275 boundary provides a sequence-based argument for D over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The NRAMP/DMT family is well-characterized as a 12-TM-helix transporter family across eukaryotes (human, plant, fungal homologs). This is transferable family-level knowledge, not a fact specific to this exact protein. The boundary question (272 vs 276) is addressable by examining the hydrophobicity of the specific residues in the supplied sequence. A model does not need to recall the UniProt entry for Q8I3M7 to arrive at D; it can use family-level TM count and local sequence analysis."
  },
  "case_id": "transmembrane_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24",
      "C26",
      "C28",
      "C5",
      "C7",
      "C9",
      "C11",
      "C13",
      "C15",
      "C17",
      "C19",
      "C21",
      "C23",
      "C25",
      "C27",
      "C29"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8I3M7 (DMT1_PLAF7) annotates exactly 12 transmembrane helices at positions 229..247, 276..299, 320..345, 351..370, 382..404, 424..445, 466..487, 516..534, 555..573, 585..603, 623..645, 651..673, matching option D exactly. The TM helix annotations carry evidence code ECO:0000255 (inferred by similarity), i.e. computational/annotation transfer rather than direct experimental determination of each helix boundary. The topological domain assignments carry ECO:0000305 (curator inference) and the C-terminal cytoplasmic domain (674..684) carries experimental evidence ECO:0000269 from PubMed:39467134. The overall topology is consistent with the NRAMP/DMT family architecture."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning the exact helix boundaries are computational/annotation transfers rather than experimentally determined at single-residue resolution.",
    "The 272-vs-276 boundary (C vs D) is a fine-grained prediction-boundary question; different TM-prediction tools (TMHMM, Phobius, DeepTMHMM) could disagree by a few residues at helix termini. The NRAMP-family 12-TM argument robustly eliminates B but the C-vs-D distinction relies more heavily on local hydrophobicity judgment.",
    "The reviewer-only evidence confirms the sequence matches Q8I3M7 (Plasmodium falciparum DMT1), but the evaluated model receives only the raw sequence with no name, organism, or accession."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly distinguished by the NRAMP-family 12-TM expectation. Options C and D differ only in the start position of the second TM (272 vs 276), a 4-residue boundary question. While different prediction tools might disagree on such fine boundaries, the local hydrophobicity profile of the supplied sequence provides a reasonable basis for preferring 276. The distinction is fine but not genuinely ambiguous given the family context and sequence analysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8I3M7 (DMT1_PLAF7) annotates exactly 12 transmembrane helices at positions 229..247, 276..299, 320..345, 351..370, 382..404, 424..445, 466..487, 516..534, 555..573, 585..603, 623..645, 651..673, matching option D exactly. The TM helix annotations carry evidence code ECO:0000255 (inferred by similarity), i.e. computational/annotation transfer rather than direct experimental determination of each helix boundary. The topological domain assignments carry ECO:0000305 (curator inference) and the C-terminal cytoplasmic domain (674..684) carries experimental evidence ECO:0000269 from PubMed:39467134. The overall topology is consistent with the NRAMP/DMT family architecture.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26", "C28", "C5", "C7", "C9", "C11", "C13", "C15", "C17", "C19", "C21", "C23", "C25", "C27", "C29"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal ~450 residues of this protein display a series of hydrophobic stretches separated by short hydrophilic loops, characteristic of a multi-pass membrane transporter. Recognizing this as an NRAMP (Natural Resistance-Associated Macrophage Protein) / DMT-family transporter is feasible from the domain architecture: a long hydrophilic N-terminal region (~1-228) followed by a compact cluster of alternating hydrophobic and hydrophilic segments. NRAMP-family members (e.g., human NRAMP1/SLC11A1, plant IRT1/2, yeast SMF proteins) consistently possess 12 transmembrane helices. This family-level regularity directly distinguishes option D (12 TM regions) from option B (11 TM regions, which omits the 424..445 helix). For the C-vs-D distinction (second TM starting at 272 vs 276), a model can inspect the residue composition at positions 272-275: if those residues are polar or charged (e.g., containing Ser, Thr, Asn, Gln, Lys, Arg), they are inconsistent with a lipid-facing helix and would be assigned to the preceding loop, favoring the 276 start. The NRAMP family argument eliminates B, and the local hydrophobicity at the 272-275 boundary provides a sequence-based argument for D over C.",
    "missing_item_specific_fact": "",
    "reason": "The NRAMP/DMT family is well-characterized as a 12-TM-helix transporter family across eukaryotes (human, plant, fungal homologs). This is transferable family-level knowledge, not a fact specific to this exact protein. The boundary question (272 vs 276) is addressable by examining the hydrophobicity of the specific residues in the supplied sequence. A model does not need to recall the UniProt entry for Q8I3M7 to arrive at D; it can use family-level TM count and local sequence analysis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly distinguished by the NRAMP-family 12-TM expectation. Options C and D differ only in the start position of the second TM (272 vs 276), a 4-residue boundary question. While different prediction tools might disagree on such fine boundaries, the local hydrophobicity profile of the supplied sequence provides a reasonable basis for preferring 276. The distinction is fine but not genuinely ambiguous given the family context and sequence analysis."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning the exact helix boundaries are computational/annotation transfers rather than experimentally determined at single-residue resolution.",
    "The 272-vs-276 boundary (C vs D) is a fine-grained prediction-boundary question; different TM-prediction tools (TMHMM, Phobius, DeepTMHMM) could disagree by a few residues at helix termini. The NRAMP-family 12-TM argument robustly eliminates B but the C-vs-D distinction relies more heavily on local hydrophobicity judgment.",
    "The reviewer-only evidence confirms the sequence matches Q8I3M7 (Plasmodium falciparum DMT1), but the evaluated model receives only the raw sequence with no name, organism, or accession."
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
  "benchmark_sequence_length": 684,
  "benchmark_sequence_sha256": "ad3e4f51961e13a279b7a2c9a8d92d3b0cb723ff3f0b8baf5ac09b89a6e02c7c",
  "current_entry_audit": {
    "entryVersion": 119,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 684,
  "current_source_sequence_sha256": "ad3e4f51961e13a279b7a2c9a8d92d3b0cb723ff3f0b8baf5ac09b89a6e02c7c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 117,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8I3M7",
  "selected_historical_entry_version": 117,
  "selected_historical_record_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "selected_historical_source_sequence_length": 684,
  "selected_historical_source_sequence_sha256": "ad3e4f51961e13a279b7a2c9a8d92d3b0cb723ff3f0b8baf5ac09b89a6e02c7c",
  "selected_historical_version": {
    "accession": "Q8I3M7",
    "database": "Swiss-Prot",
    "entryVersion": 117,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DMT1_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8I3M7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":119,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35404116\",\"source\":\"PubMed\"}],\"value\":\"Food vacuole resident transporter 1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"PfNRAMP\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39467134\",\"source\":\"PubMed\"}],\"value\":\"Divalent metal transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39467134\",\"source\":\"PubMed\"}],\"value\":\"DMT1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39467134\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"PfDMT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":228},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":247},\"start\":{\"modifier\":\"EXACT\",\"value\":229}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":275},\"start\":{\"modifier\":\"EXACT\",\"value\":248}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":299},\"start\":{\"modifier\":\"EXACT\",\"value\":276}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":319},\"start\":{\"modifier\":\"EXACT\",\"value\":300}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":345},\"start\":{\"modifier\":\"EXACT\",\"value\":320}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":350},\"start\":{\"modifier\":\"EXACT\",\"value\":346}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":370},\"start\":{\"modifier\":\"EXACT\",\"value\":351}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":381},\"start\":{\"modifier\":\"EXACT\",\"value\":371}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":404},\"start\":{\"modifier\":\"EXACT\",\"value\":382}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":423},\"start\":{\"modifier\":\"EXACT\",\"value\":405}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":445},\"start\":{\"modifier\":\"EXACT\",\"value\":424}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":465},\"start\":{\"modifier\":\"EXACT\",\"value\":446}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":487},\"start\":{\"modifier\":\"EXACT\",\"value\":466}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":515},\"start\":{\"modifier\":\"EXACT\",\"value\":488}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":534},\"start\":{\"modifier\":\"EXACT\",\"value\":516}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":554},\"start\":{\"modifier\":\"EXACT\",\"value\":535}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":573},\"start\":{\"modifier\":\"EXACT\",\"value\":555}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":584},\"start\":{\"modifier\":\"EXACT\",\"value\":574}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":603},\"start\":{\"modifier\":\"EXACT\",\"value\":585}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":622},\"start\":{\"modifier\":\"EXACT\",\"value\":604}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":645},\"start\":{\"modifier\":\"EXACT\",\"value\":623}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/22",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C27",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":650},\"start\":{\"modifier\":\"EXACT\",\"value\":646}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/23",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C28",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":673},\"start\":{\"modifier\":\"EXACT\",\"value\":651}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/24",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C29",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39467134\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":684},\"start\":{\"modifier\":\"EXACT\",\"value\":674}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/25",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C30

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C30",
  "excerpt": "{\"citation\":{\"authors\":[\"Wichers J.S.\",\"Mesen-Ramirez P.\",\"Fuchs G.\",\"Yu-Strzelczyk J.\",\"Staecker J.\",\"von Thien H.\",\"Alder A.\",\"Henshall I.\",\"Liffner B.\",\"Nagel G.\",\"Loew C.\",\"Wilson D.\",\"Spielmann T.\",\"Gao S.\",\"Gilberger T.W.\",\"Bachmann A.\",\"Strauss J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35404116\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.00623-22\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0062322\",\"id\":\"35404116\",\"journal\":\"MBio\",\"lastPage\":\"e0062322\",\"publicationDate\":\"2022\",\"title\":\"PMRT1, a Plasmodium-Specific Parasite Plasma Membrane Transporter, Is Essential for Asexual and Sexual Blood Stage Development.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C31

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C31",
  "excerpt": "{\"citation\":{\"authors\":[\"Wunderlich J.\",\"Kotov V.\",\"Votborg-Novel L.\",\"Ntalla C.\",\"Geffken M.\",\"Peine S.\",\"Portugal S.\",\"Strauss J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39575308\"},{\"database\":\"DOI\",\"id\":\"10.3389/fcimb.2024.1480076\"}],\"citationType\":\"journal article\",\"firstPage\":\"1480076\",\"id\":\"39575308\",\"journal\":\"Front. Cell. Infect. Microbiol.\",\"lastPage\":\"1480076\",\"publicationDate\":\"2024\",\"title\":\"Iron transport pathways in the human malaria parasite Plasmodium falciparum revealed by RNA-sequencing.\",\"volume\":\"14\"},\"referenceNumber\":4,\"referencePositions\":[\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence C32

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C32",
  "excerpt": "{\"citation\":{\"authors\":[\"Loveridge K.M.\",\"Sigala P.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39467134\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.2411631121\"}],\"citationType\":\"journal article\",\"firstPage\":\"e2411631121\",\"id\":\"39467134\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"e2411631121\",\"publicationDate\":\"2024\",\"title\":\"Identification of a divalent metal transporter required for cellular iron metabolism in malaria parasites.\",\"volume\":\"121\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"TOPOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H1",
  "excerpt": "ID   DMT1_PLAF7              Reviewed;         684 AA.\nAC   Q8I3M7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 117.\nDE   RecName: Full=Divalent metal transporter 1 {ECO:0000303|PubMed:39467134};\nDE            Short=DMT1 {ECO:0000303|PubMed:39467134};\nDE            Short=PfDMT1 {ECO:0000303|PubMed:39467134, ECO:0000303|PubMed:39575308};\nDE   AltName: Full=Food vacuole resident transporter 1 {ECO:0000303|PubMed:35404116};\nDE   AltName: Full=PfNRAMP {ECO:0000303|PubMed:39575308};\nGN   Name=FVRT1 {ECO:0000303|PubMed:35404116};\nGN   ORFNames=PF3D7_0523800 {ECO:0000312|EMBL:CAD51601.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION PHENOTYPE.\nRX   PubMed=35404116; DOI=10.1128/mbio.00623-22;\nRA   Wichers J.S., Mesen-Ramirez P., Fuchs G., Yu-Strzelczyk J., Staecker J.,\nRA   von Thien H., Alder A., Henshall I., Liffner B., Nagel G., Loew C.,\nRA   Wilson D., Spielmann T., Gao S., Gilberger T.W., Bachmann A., Strauss J.;\nRT   \"PMRT1, a Plasmodium-Specific Parasite Plasma Membrane Transporter, Is\nRT   Essential for Asexual and Sexual Blood Stage Development.\";\nRL   MBio 13:e0062322-e0062322(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   INDUCTION.\nRX   PubMed=39575308; DOI=10.3389/fcimb.2024.1480076;\nRA   Wunderlich J., Kotov V., Votborg-Novel L., Ntalla C., Geffken M., Peine S.,\nRA   Portugal S., Strauss J.;\nRT   \"Iron transport pathways in the human malaria parasite Plasmodium\nRT   falciparum revealed by RNA-sequencing.\";\nRL   Front. Cell. Infect. Microbiol. 14:1480076-1480076(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H4",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, AND TOPOLOGY.\nRX   PubMed=39467134; DOI=10.1073/pnas.2411631121;\nRA   Loveridge K.M., Sigala P.A.;\nRT   \"Identification of a divalent metal transporter required for cellular iron\nRT   metabolism in malaria parasites.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 121:e2411631121-e2411631121(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H5",
  "excerpt": "FT   TOPO_DOM        1..228\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 150-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        229..247\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H7",
  "excerpt": "FT   TOPO_DOM        248..275\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 156-158",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        276..299\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 159-161",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H9",
  "excerpt": "FT   TOPO_DOM        300..319\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-164",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        320..345\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 165-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H11",
  "excerpt": "FT   TOPO_DOM        346..350\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 168-170",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        351..370\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 171-173",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H13",
  "excerpt": "FT   TOPO_DOM        371..381\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 174-176",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        382..404\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 177-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H15",
  "excerpt": "FT   TOPO_DOM        405..423\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 180-182",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H16",
  "excerpt": "FT   TRANSMEM        424..445\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 183-185",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H17",
  "excerpt": "FT   TOPO_DOM        446..465\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 186-188",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H18",
  "excerpt": "FT   TRANSMEM        466..487\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 189-191",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H19",
  "excerpt": "FT   TOPO_DOM        488..515\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 192-194",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H20",
  "excerpt": "FT   TRANSMEM        516..534\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 195-197",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H21",
  "excerpt": "FT   TOPO_DOM        535..554\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 198-200",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H22",
  "excerpt": "FT   TRANSMEM        555..573\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 201-203",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H23",
  "excerpt": "FT   TOPO_DOM        574..584\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 204-206",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H24",
  "excerpt": "FT   TRANSMEM        585..603\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 207-209",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H25",
  "excerpt": "FT   TOPO_DOM        604..622\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 210-212",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H26",
  "excerpt": "FT   TRANSMEM        623..645\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 213-215",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H27",
  "excerpt": "FT   TOPO_DOM        646..650\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 216-218",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H28

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H28",
  "excerpt": "FT   TRANSMEM        651..673\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 219-221",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

### Evidence H29

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H29",
  "excerpt": "FT   TOPO_DOM        674..684\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39467134\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 222-224",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
