# transmembrane_0103

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0103.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGKEQKEKKDGNLSIKEEVEKELNKKSTAELFRKIKNEKISFFLPFKCLPAQHRKLLFISFVCAVLSGGTLPFFISVFGVILKNMNLGDDINPIILSLVSIGLVQFILSMISSYCMDVITSKILKTLKLEYLRSVFYQDGQFHDNNPGSKLRSDLDFYLEQVSSGIGTKFITIFTYASSFLGLYIWSLIKNARLTLCITCVFPLIYVCGVICNKKVKLNKKTSLLYNNNTMSIIEEALMGIRTVASYCGEKTILNKFNLSETFYSKYILKANFVEALHIGLINGLILVSYAFGFWYGTRIIINSATNQYPNNDFNGASVISILLGVLISMFMLTIILPNITEYMKALEATNSLYEIINRKPLVENNDDGETLPNIKKIEFKNVRFHYDTRKDVEIYKDLSFTLKEGKTYAFVGESGCGKSTILKLIERLYDPTEGDIIVNDSHNLKDINLKWWRSKIGVVSQDPLLFSNSIKNNIKYSLYSLKDLEAMENYYEENTNDTYENKNFSLISNSMTSNELLEMKKEYQTIKDSDVVDVSKKVLIHDFVSSLPDKYDTLVGSNASKLSGGQKQRISIARAIMRNPKILILDEATSSLDNKSEYLVQKTINNLKGNENRITIIIAHRLSTIRYANTIFVLSNRERSDNNNNNNNDDNNNNNNNNNNKINNEGSYIIEQGTHDSLMKNKNGIYHLMINNQKISSNKSSNNGNDNGSDNKSSAYKDSDTGNDADNMNSLSIHENENISNNRNCKNTAENEKEEKVPFFKRMFRRKKKAPNNLRIIYKEIFSYKKDVTIIFFSILVAGGLYPVFALLYARYVSTLFDFANLEYNSNKYSIYILLIAIAMFISETLKNYYNNKIGEKVEKTMKRRLFENILYQEMSFFDQDKNTPGVLSAHINRDVHLLKTGLVNNIVIFSHFIMLFLVSMVMSFYFCPIVAAVLTFIYFINMRVFAVRARLTKSKEIEKKENMSSGVFAFSSDDEMFKDPSFLIQEAFYNMHTVINYGLEDYFCNLIEKAIDYKNKGQKRRIIVNAALWGFSQSAQLFINSFAYWFGSFLIKRGTILVDDFMKSLFTFIFTGSYAGKLMSLKGDSENAKLSFEKYYPLMIRKSNIDVRDDGGIRINKNLIKGKVDIKDVNFRYISRPNVPIYKNLSFTCDSKKTTAIVGETGSGKSTFMNLLLRFYDLKNDHIILKNDMTNFQDYQNNNNNSLVLKNVNEFSNQSGSAEDYTVFNNNGEILLDDINICDYNLRDLRNLFSIVSQEPMLFNMSIYENIKFGREDATLEDVKRVSKFAAIDEFIESLPNKYDTNVGPYGKSLSGGQKQRIAIARALLREPKILLLDEATSSLDSNSEKLIEKTIVDIKDKADKTIITIAHRIASIKRSDKIVVFNNPDRNGTFVQSHGTHDELLSAQDGIYKKYVKLAK

[Multiple Choices]
A. 3..23
B. 61..81; 91..111; 169..189; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
C. 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
D. 61..81; 91..111; 169..189; 192..212; 276..296; 318..338; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
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

> The matched UniProt entry annotates the transmembrane intervals listed in C, including 192..212 and 317..337. These are principally computational PROSITE-ProRule annotations, so they support the keyed coordinates as database annotations but are not, by themselves, experimental validation of every boundary.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has repeated hydrophobic stretches consistent with the multi-pass membrane domains of an ABC transporter, separated by long soluble regions containing nucleotide-binding motifs. In particular, the strongly hydrophobic stretch around 192..212 supports C over B, which omits it. Around 317..337, the sequence is hydrophobic, whereas the next residue is polar, favoring C's boundary over D's one-residue-shifted endpoint. These sequence patterns provide a transferable basis for selecting C, although they do not establish every boundary with experimental precision.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of ABC-transporter architecture and hydropathy patterns distinguishes the main candidate sets and gives a sequence-based reason to prefer C over the near-duplicate D. Exact helix boundaries remain less certain than the broad transmembrane regions.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> C and D differ only by shifting one helix by one residue. Both intervals cover essentially the same hydrophobic membrane-spanning segment, so the wording does not make clear that this boundary-level distinction is biologically decisive.


### Important caveats

- The supporting database coordinates are computational annotations; the supplied reviewer evidence does not establish experimental validation of each endpoint.
- The sequence supports membrane-spanning helices, but predicted boundaries can vary by a residue.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with the multi-pass membrane domains of an ABC transporter, separated by long soluble regions containing nucleotide-binding motifs. In particular, the strongly hydrophobic stretch around 192..212 supports C over B, which omits it. Around 317..337, the sequence is hydrophobic, whereas the next residue is polar, favoring C's boundary over D's one-residue-shifted endpoint. These sequence patterns provide a transferable basis for selecting C, although they do not establish every boundary with experimental precision.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of ABC-transporter architecture and hydropathy patterns distinguishes the main candidate sets and gives a sequence-based reason to prefer C over the near-duplicate D. Exact helix boundaries remain less certain than the broad transmembrane regions."
  },
  "case_id": "transmembrane_0103",
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
      "C23",
      "C25",
      "C27"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates the transmembrane intervals listed in C, including 192..212 and 317..337. These are principally computational PROSITE-ProRule annotations, so they support the keyed coordinates as database annotations but are not, by themselves, experimental validation of every boundary."
  },
  "important_caveats": [
    "The supporting database coordinates are computational annotations; the supplied reviewer evidence does not establish experimental validation of each endpoint.",
    "The sequence supports membrane-spanning helices, but predicted boundaries can vary by a residue."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "C and D differ only by shifting one helix by one residue. Both intervals cover essentially the same hydrophobic membrane-spanning segment, so the wording does not make clear that this boundary-level distinction is biologically decisive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates the transmembrane intervals listed in C, including 192..212 and 317..337. These are principally computational PROSITE-ProRule annotations, so they support the keyed coordinates as database annotations but are not, by themselves, experimental validation of every boundary.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C23", "C25", "C27"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with the multi-pass membrane domains of an ABC transporter, separated by long soluble regions containing nucleotide-binding motifs. In particular, the strongly hydrophobic stretch around 192..212 supports C over B, which omits it. Around 317..337, the sequence is hydrophobic, whereas the next residue is polar, favoring C's boundary over D's one-residue-shifted endpoint. These sequence patterns provide a transferable basis for selecting C, although they do not establish every boundary with experimental precision.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of ABC-transporter architecture and hydropathy patterns distinguishes the main candidate sets and gives a sequence-based reason to prefer C over the near-duplicate D. Exact helix boundaries remain less certain than the broad transmembrane regions."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "C and D differ only by shifting one helix by one residue. Both intervals cover essentially the same hydrophobic membrane-spanning segment, so the wording does not make clear that this boundary-level distinction is biologically decisive."
  },
  "important_caveats": [
    "The supporting database coordinates are computational annotations; the supplied reviewer evidence does not establish experimental validation of each endpoint.",
    "The sequence supports membrane-spanning helices, but predicted boundaries can vary by a residue."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q7K6A5 (PfMDR1) lists exactly 12 transmembrane helices at 61..81, 91..111, 169..189, 192..212, 276..296, 317..337, 789..809, 830..850, 908..928, 929..949, 1033..1053, 1058..1078, matching option C precisely. All TM annotations carry evidence code ECO:0000255 (PROSITE-ProRule PRU00441), indicating computational/profiling annotation rather than direct experimental determination.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical ABC transporter motifs (Walker A: GESGCGKST at ~positions 380-390 and 1190-1200; ABC signature: LSGGQ at ~positions 455-460 and 1265-1270), identifying this as a P-glycoprotein/ABC transporter family member. ABC transporters have a canonical 6+6 TM topology (12 TM helices total, six per nucleotide-binding domain half). Option B lists only 11 TM regions (5 in the first half, missing 192..212), violating the canonical fold. Option A (a single 21-residue N-terminal segment) is incompatible with a multi-pass membrane transporter. For C vs D, the 6th TM boundary differs by one residue: C has 317..337, D has 318..338. Examining the sequence at these positions, residue 317 is A (hydrophobic), 318 is S (polar), 337 is L (hydrophobic), and 338 is P (helix-breaking). A TM helix should begin and end with hydrophobic residues and avoid a proline at the C-terminal boundary, favoring 317..337 (option C) over 318..338 (option D).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The ABC transporter family topology (6+6 TM) is well-established transferable knowledge that eliminates B. Hydrophobicity boundary analysis (A at 317 vs S at 318; L at 337 vs P at 338) provides a sequence-based argument favoring C over D. Option A is eliminated by the multi-pass membrane protein context. The reasoning chain uses family-level biology and standard hydrophobicity principles without requiring the exact database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While C vs D differs by only one residue at a TM boundary, the hydrophobicity argument (A/S at the N-terminus of the helix, L/P at the C-terminus) provides a reasonable sequence-based distinction. B is eliminated by the canonical 12-TM ABC transporter topology. No two options are equally defensible given the available evidence.


### Important caveats

- All TM annotations in the source are computational (PROSITE-ProRule PRU00441, ECO:0000255), not experimentally determined by crystallography or cryo-EM at single-residue resolution for each helix boundary.
- The C vs D distinction (1-residue shift at the 6th TM boundary) is within the typical uncertainty of hydrophobicity-based TM prediction; the argument relies on identifying a polar (S) and helix-breaking (P) residue at the proposed D boundaries.
- The 2023 cryo-EM structures (PDB 8JVH etc.) resolve the full protein but the UniProt TM boundaries are still annotated via PROSITE-ProRule profiling, not directly from the structure.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical ABC transporter motifs (Walker A: GESGCGKST at ~positions 380-390 and 1190-1200; ABC signature: LSGGQ at ~positions 455-460 and 1265-1270), identifying this as a P-glycoprotein/ABC transporter family member. ABC transporters have a canonical 6+6 TM topology (12 TM helices total, six per nucleotide-binding domain half). Option B lists only 11 TM regions (5 in the first half, missing 192..212), violating the canonical fold. Option A (a single 21-residue N-terminal segment) is incompatible with a multi-pass membrane transporter. For C vs D, the 6th TM boundary differs by one residue: C has 317..337, D has 318..338. Examining the sequence at these positions, residue 317 is A (hydrophobic), 318 is S (polar), 337 is L (hydrophobic), and 338 is P (helix-breaking). A TM helix should begin and end with hydrophobic residues and avoid a proline at the C-terminal boundary, favoring 317..337 (option C) over 318..338 (option D).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The ABC transporter family topology (6+6 TM) is well-established transferable knowledge that eliminates B. Hydrophobicity boundary analysis (A at 317 vs S at 318; L at 337 vs P at 338) provides a sequence-based argument favoring C over D. Option A is eliminated by the multi-pass membrane protein context. The reasoning chain uses family-level biology and standard hydrophobicity principles without requiring the exact database annotation."
  },
  "case_id": "transmembrane_0103",
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
      "C23",
      "C25",
      "C27"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q7K6A5 (PfMDR1) lists exactly 12 transmembrane helices at 61..81, 91..111, 169..189, 192..212, 276..296, 317..337, 789..809, 830..850, 908..928, 929..949, 1033..1053, 1058..1078, matching option C precisely. All TM annotations carry evidence code ECO:0000255 (PROSITE-ProRule PRU00441), indicating computational/profiling annotation rather than direct experimental determination."
  },
  "important_caveats": [
    "All TM annotations in the source are computational (PROSITE-ProRule PRU00441, ECO:0000255), not experimentally determined by crystallography or cryo-EM at single-residue resolution for each helix boundary.",
    "The C vs D distinction (1-residue shift at the 6th TM boundary) is within the typical uncertainty of hydrophobicity-based TM prediction; the argument relies on identifying a polar (S) and helix-breaking (P) residue at the proposed D boundaries.",
    "The 2023 cryo-EM structures (PDB 8JVH etc.) resolve the full protein but the UniProt TM boundaries are still annotated via PROSITE-ProRule profiling, not directly from the structure."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While C vs D differs by only one residue at a TM boundary, the hydrophobicity argument (A/S at the N-terminus of the helix, L/P at the C-terminus) provides a reasonable sequence-based distinction. B is eliminated by the canonical 12-TM ABC transporter topology. No two options are equally defensible given the available evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q7K6A5 (PfMDR1) lists exactly 12 transmembrane helices at 61..81, 91..111, 169..189, 192..212, 276..296, 317..337, 789..809, 830..850, 908..928, 929..949, 1033..1053, 1058..1078, matching option C precisely. All TM annotations carry evidence code ECO:0000255 (PROSITE-ProRule PRU00441), indicating computational/profiling annotation rather than direct experimental determination.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C23", "C25", "C27"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical ABC transporter motifs (Walker A: GESGCGKST at ~positions 380-390 and 1190-1200; ABC signature: LSGGQ at ~positions 455-460 and 1265-1270), identifying this as a P-glycoprotein/ABC transporter family member. ABC transporters have a canonical 6+6 TM topology (12 TM helices total, six per nucleotide-binding domain half). Option B lists only 11 TM regions (5 in the first half, missing 192..212), violating the canonical fold. Option A (a single 21-residue N-terminal segment) is incompatible with a multi-pass membrane transporter. For C vs D, the 6th TM boundary differs by one residue: C has 317..337, D has 318..338. Examining the sequence at these positions, residue 317 is A (hydrophobic), 318 is S (polar), 337 is L (hydrophobic), and 338 is P (helix-breaking). A TM helix should begin and end with hydrophobic residues and avoid a proline at the C-terminal boundary, favoring 317..337 (option C) over 318..338 (option D).",
    "missing_item_specific_fact": "",
    "reason": "The ABC transporter family topology (6+6 TM) is well-established transferable knowledge that eliminates B. Hydrophobicity boundary analysis (A at 317 vs S at 318; L at 337 vs P at 338) provides a sequence-based argument favoring C over D. Option A is eliminated by the multi-pass membrane protein context. The reasoning chain uses family-level biology and standard hydrophobicity principles without requiring the exact database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While C vs D differs by only one residue at a TM boundary, the hydrophobicity argument (A/S at the N-terminus of the helix, L/P at the C-terminus) provides a reasonable sequence-based distinction. B is eliminated by the canonical 12-TM ABC transporter topology. No two options are equally defensible given the available evidence."
  },
  "important_caveats": [
    "All TM annotations in the source are computational (PROSITE-ProRule PRU00441, ECO:0000255), not experimentally determined by crystallography or cryo-EM at single-residue resolution for each helix boundary.",
    "The C vs D distinction (1-residue shift at the 6th TM boundary) is within the typical uncertainty of hydrophobicity-based TM prediction; the argument relies on identifying a polar (S) and helix-breaking (P) residue at the proposed D boundaries.",
    "The 2023 cryo-EM structures (PDB 8JVH etc.) resolve the full protein but the UniProt TM boundaries are still annotated via PROSITE-ProRule profiling, not directly from the structure."
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
  "benchmark_sequence_length": 1419,
  "benchmark_sequence_sha256": "814492b7a3ffcadbd0dde392964e9ba403451c8c63dbc1231fa05df226af501f",
  "current_entry_audit": {
    "entryVersion": 161,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1419,
  "current_source_sequence_sha256": "814492b7a3ffcadbd0dde392964e9ba403451c8c63dbc1231fa05df226af501f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 159,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q7K6A5",
  "selected_historical_entry_version": 159,
  "selected_historical_record_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "selected_historical_source_sequence_length": 1419,
  "selected_historical_source_sequence_sha256": "814492b7a3ffcadbd0dde392964e9ba403451c8c63dbc1231fa05df226af501f",
  "selected_historical_version": {
    "accession": "Q7K6A5",
    "database": "Swiss-Prot",
    "entryVersion": 159,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MDR_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q7K6A5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":161,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"1674943\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"8097560\",\"source\":\"PubMed\"}],\"value\":\"P-glycoprotein homolog\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"1674943\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"8097560\",\"source\":\"PubMed\"}],\"value\":\"PGH1\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37527341\",\"source\":\"PubMed\"}],\"value\":\"7.6.2.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"1674943\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37527341\",\"source\":\"PubMed\"}],\"value\":\"Multidrug resistance protein 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"1674943\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37527341\",\"source\":\"PubMed\"}],\"value\":\"PfMDR1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":60},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":81},\"start\":{\"modifier\":\"EXACT\",\"value\":61}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":90},\"start\":{\"modifier\":\"EXACT\",\"value\":82}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":111},\"start\":{\"modifier\":\"EXACT\",\"value\":91}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":168},\"start\":{\"modifier\":\"EXACT\",\"value\":112}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":189},\"start\":{\"modifier\":\"EXACT\",\"value\":169}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":191},\"start\":{\"modifier\":\"EXACT\",\"value\":190}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":212},\"start\":{\"modifier\":\"EXACT\",\"value\":192}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":275},\"start\":{\"modifier\":\"EXACT\",\"value\":213}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":296},\"start\":{\"modifier\":\"EXACT\",\"value\":276}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":316},\"start\":{\"modifier\":\"EXACT\",\"value\":297}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":337},\"start\":{\"modifier\":\"EXACT\",\"value\":317}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":788},\"start\":{\"modifier\":\"EXACT\",\"value\":338}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":809},\"start\":{\"modifier\":\"EXACT\",\"value\":789}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":829},\"start\":{\"modifier\":\"EXACT\",\"value\":810}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":850},\"start\":{\"modifier\":\"EXACT\",\"value\":830}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":907},\"start\":{\"modifier\":\"EXACT\",\"value\":851}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":928},\"start\":{\"modifier\":\"EXACT\",\"value\":908}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":949},\"start\":{\"modifier\":\"EXACT\",\"value\":929}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1032},\"start\":{\"modifier\":\"EXACT\",\"value\":950}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1053},\"start\":{\"modifier\":\"EXACT\",\"value\":1033}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1057},\"start\":{\"modifier\":\"EXACT\",\"value\":1054}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/22",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C27",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1078},\"start\":{\"modifier\":\"EXACT\",\"value\":1058}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/23",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C28",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1419},\"start\":{\"modifier\":\"EXACT\",\"value\":1079}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/24",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C29",
  "excerpt": "{\"citation\":{\"authors\":[\"Cowman A.F.\",\"Karcz S.\",\"Galatis D.\",\"Culvenor J.G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"1674943\"},{\"database\":\"DOI\",\"id\":\"10.1083/jcb.113.5.1033\"}],\"citationType\":\"journal article\",\"firstPage\":\"1033\",\"id\":\"1674943\",\"journal\":\"J. Cell Biol.\",\"lastPage\":\"1042\",\"publicationDate\":\"1991\",\"title\":\"A P-glycoprotein homologue of Plasmodium falciparum is localized on the digestive vacuole.\",\"volume\":\"113\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C30

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C30",
  "excerpt": "{\"citation\":{\"authors\":[\"Karcz S.R.\",\"Galatis D.\",\"Cowman A.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"8097560\"},{\"database\":\"DOI\",\"id\":\"10.1016/0166-6851(93)90048-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"269\",\"id\":\"8097560\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"276\",\"publicationDate\":\"1993\",\"title\":\"Nucleotide binding properties of a P-glycoprotein homologue from Plasmodium falciparum.\",\"volume\":\"58\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence C31

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C31",
  "excerpt": "{\"citation\":{\"authors\":[\"Si K.\",\"He X.\",\"Chen L.\",\"Zhang A.\",\"Guo C.\",\"Li M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37527341\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.2219905120\"}],\"citationType\":\"journal article\",\"firstPage\":\"e2219905120\",\"id\":\"37527341\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"e2219905120\",\"publicationDate\":\"2023\",\"title\":\"The structure of <i>Plasmodium falciparum</i> multidrug resistance protein 1 reveals an N-terminal regulatory domain.\",\"volume\":\"120\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8JVH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8JW4\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8JWF\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8JWG\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8JWI\",\"source\":\"PDB\"}],\"referenceNumber\":6,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (2.94 ANGSTROMS) OF 38-1419 IN COMPLEX WITH ATP; MAGNESIUM ION AND MEFLOQUINE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"R DOMAIN\",\"MUTAGENESIS OF 1-MET--ASN-37; ASN-86; TYR-184; THR-199; LYS-217; LYS-220; LYS-221; PHE-331; GLU-588; SER-1034; ASN-1042; ASP-1246 AND GLU-1337\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H1",
  "excerpt": "ID   MDR_PLAF7               Reviewed;        1419 AA.\nAC   Q7K6A5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 159.\nDE   RecName: Full=Multidrug resistance protein 1 {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:37527341};\nDE            Short=PfMDR1 {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:37527341};\nDE            EC=7.6.2.2 {ECO:0000269|PubMed:37527341};\nDE   AltName: Full=P-glycoprotein homolog {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:8097560};\nDE            Short=PGH1 {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:8097560};\nGN   ORFNames=PF3D7_0523000 {ECO:0000312|EMBL:CAD51594.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   SUBCELLULAR LOCATION, AND DEVELOPMENTAL STAGE.\nRX   PubMed=1674943; DOI=10.1083/jcb.113.5.1033;\nRA   Cowman A.F., Karcz S., Galatis D., Culvenor J.G.;\nRT   \"A P-glycoprotein homologue of Plasmodium falciparum is localized on the\nRT   digestive vacuole.\";\nRL   J. Cell Biol. 113:1033-1042(1991).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   SUBCELLULAR LOCATION.\nRX   PubMed=8097560; DOI=10.1016/0166-6851(93)90048-3;\nRA   Karcz S.R., Galatis D., Cowman A.F.;\nRT   \"Nucleotide binding properties of a P-glycoprotein homologue from\nRT   Plasmodium falciparum.\";\nRL   Mol. Biochem. Parasitol. 58:269-276(1993).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H4",
  "excerpt": "RN   [6] {ECO:0007744|PDB:8JVH, ECO:0007744|PDB:8JW4, ECO:0007744|PDB:8JWF, ECO:0007744|PDB:8JWG, ECO:0007744|PDB:8JWI}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (2.94 ANGSTROMS) OF 38-1419 IN COMPLEX\nRP   WITH ATP; MAGNESIUM ION AND MEFLOQUINE, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, R DOMAIN, AND MUTAGENESIS OF 1-MET--ASN-37;\nRP   ASN-86; TYR-184; THR-199; LYS-217; LYS-220; LYS-221; PHE-331; GLU-588;\nRP   SER-1034; ASN-1042; ASP-1246 AND GLU-1337.\nRX   PubMed=37527341; DOI=10.1073/pnas.2219905120;\nRA   Si K., He X., Chen L., Zhang A., Guo C., Li M.;\nRT   \"The structure of <i>Plasmodium falciparum</i> multidrug resistance protein\nRT   1 reveals an N-terminal regulatory domain.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 120:e2219905120-e2219905120(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H5",
  "excerpt": "FT   TOPO_DOM        1..60\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 219-221",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        61..81\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 222-224",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H7",
  "excerpt": "FT   TOPO_DOM        82..90\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 225-227",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        91..111\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 228-230",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H9",
  "excerpt": "FT   TOPO_DOM        112..168\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 231-233",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        169..189\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 234-236",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H11",
  "excerpt": "FT   TOPO_DOM        190..191\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 237-239",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        192..212\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 240-242",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H13",
  "excerpt": "FT   TOPO_DOM        213..275\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 243-245",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        276..296\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 246-248",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H15",
  "excerpt": "FT   TOPO_DOM        297..316\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 249-251",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H16",
  "excerpt": "FT   TRANSMEM        317..337\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 252-254",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H17",
  "excerpt": "FT   TOPO_DOM        338..788\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 255-257",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H18",
  "excerpt": "FT   TRANSMEM        789..809\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 258-260",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H19",
  "excerpt": "FT   TOPO_DOM        810..829\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 261-263",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H20",
  "excerpt": "FT   TRANSMEM        830..850\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 264-266",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H21",
  "excerpt": "FT   TOPO_DOM        851..907\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 267-269",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H22",
  "excerpt": "FT   TRANSMEM        908..928\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 270-272",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H23",
  "excerpt": "FT   TRANSMEM        929..949\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 273-275",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H24",
  "excerpt": "FT   TOPO_DOM        950..1032\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 276-278",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H25",
  "excerpt": "FT   TRANSMEM        1033..1053\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 279-281",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H26",
  "excerpt": "FT   TOPO_DOM        1054..1057\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 282-284",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H27",
  "excerpt": "FT   TRANSMEM        1058..1078\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 285-287",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

### Evidence H28

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "entry_version": 159,
  "evidence_id": "H28",
  "excerpt": "FT   TOPO_DOM        1079..1419\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 288-290",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 103. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
