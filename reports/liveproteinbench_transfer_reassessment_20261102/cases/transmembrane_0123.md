# transmembrane_0123

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0123.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 31..51; 112..132; 133..153; 179..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTGQSAAVEGSNSALPWYRMGFHTLAEFNTYVTFVLLGMSIMMVTSAVTSAPDFVTKYFIYATGDPDAVAETPLFWNNANTFYNAGTYAMQVVTEIASLTPFMRSIPLGIRLFLGLGIPFVELVVIIAVPAATIPTQNGAIAVIMVVAMMGGLSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALFMSIIQIILQVSMGSTFQDVLTISRIYFGIGIGIQVMAIAALVLLRYNPFAQKYIAEFRAAALRRRGHVEPEESQDSKEPATGDVAEAPKAGEKEVTLDAMEEADEVRAVPSDAFVAKSGAVLQATGDADRMVDLDQTKNITSTEQMLRASVWSVFKRIYPMLLCAFTIFFTTLLVFPGVFFLVPARSGWYMTIIVTLFNAGDFVARVLLMIRVLRPSPKLVIVGTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITLTY

[Multiple Choices]
A. 31..51; 112..132; 133..153; 181..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495
B. 31..51; 112..132; 133..153; 179..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495
C. 31..51; 133..153; 179..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495
D. 4..24; 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
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

> The sequence-matched UniProt annotation lists all ten transmembrane segments in choice B, including 179..199. These are annotated as helical with computational evidence code ECO:0000255, so this supports the keyed annotation but is not, by itself, direct experimental confirmation of every boundary.

Citations as saved: [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has many hydrophobic stretches, consistent with a multipass membrane protein, and transferable knowledge can identify the broad transmembrane regions. But choices A and B differ only in whether the same hydrophobic helix begins at 179 or 181; both ranges are plausible membrane-spanning segments.


**Missing item-specific fact**

> The intended exact boundary annotation for this protein's helix at 179..199, rather than the alternative 181..199.


**Reason**

> Family-level or hydropathy reasoning supports a helix in this region but does not meaningfully resolve its N-terminal boundary to this two-residue difference. Distinguishing the keyed range from the near-identical alternative requires the protein-specific boundary annotation or equivalent exact prediction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both choices include the same strongly hydrophobic helix and differ only by two residues at its start. The question gives no boundary tolerance or criterion that makes one range, as a membrane-spanning segment, uniquely correct.


### Important caveats

- The supporting transmembrane annotations are computationally evidenced; the supplied excerpts do not establish that every boundary was experimentally measured.
- The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many hydrophobic stretches, consistent with a multipass membrane protein, and transferable knowledge can identify the broad transmembrane regions. But choices A and B differ only in whether the same hydrophobic helix begins at 179 or 181; both ranges are plausible membrane-spanning segments.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The intended exact boundary annotation for this protein's helix at 179..199, rather than the alternative 181..199.",
    "reason": "Family-level or hydropathy reasoning supports a helix in this region but does not meaningfully resolve its N-terminal boundary to this two-residue difference. Distinguishing the keyed range from the near-identical alternative requires the protein-specific boundary annotation or equivalent exact prediction."
  },
  "case_id": "transmembrane_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all ten transmembrane segments in choice B, including 179..199. These are annotated as helical with computational evidence code ECO:0000255, so this supports the keyed annotation but is not, by itself, direct experimental confirmation of every boundary."
  },
  "important_caveats": [
    "The supporting transmembrane annotations are computationally evidenced; the supplied excerpts do not establish that every boundary was experimentally measured.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both choices include the same strongly hydrophobic helix and differ only by two residues at its start. The question gives no boundary tolerance or criterion that makes one range, as a membrane-spanning segment, uniquely correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all ten transmembrane segments in choice B, including 179..199. These are annotated as helical with computational evidence code ECO:0000255, so this supports the keyed annotation but is not, by itself, direct experimental confirmation of every boundary.",
    "evidence_ids": ["H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has many hydrophobic stretches, consistent with a multipass membrane protein, and transferable knowledge can identify the broad transmembrane regions. But choices A and B differ only in whether the same hydrophobic helix begins at 179 or 181; both ranges are plausible membrane-spanning segments.",
    "missing_item_specific_fact": "The intended exact boundary annotation for this protein's helix at 179..199, rather than the alternative 181..199.",
    "reason": "Family-level or hydropathy reasoning supports a helix in this region but does not meaningfully resolve its N-terminal boundary to this two-residue difference. Distinguishing the keyed range from the near-identical alternative requires the protein-specific boundary annotation or equivalent exact prediction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both choices include the same strongly hydrophobic helix and differ only by two residues at its start. The question gives no boundary tolerance or criterion that makes one range, as a membrane-spanning segment, uniquely correct."
  },
  "important_caveats": [
    "The supporting transmembrane annotations are computationally evidenced; the supplied excerpts do not establish that every boundary was experimentally measured.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9NBV4 (LdNT2, Leishmania donovani nucleoside transporter 2, 499 aa) annotates exactly ten transmembrane helices at positions 31..51, 112..132, 133..153, 179..199, 212..232, 350..370, 378..398, 406..426, 428..448, and 475..495, all with ECO:0000255 (inferred by similarity/proRule). Choice B matches these boundaries exactly. The sequence match between the benchmark input and the source entry is confirmed (SHA-256 identical, 499 aa).

Citations as saved: [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The critical distinction between A and B is the 4th TM start: 181..199 (A) vs 179..199 (B). Position 179 is Trp (W), position 180 is Gly (G), and position 181 is Leu (L). A well-established principle in membrane protein biology is the 'aromatic belt' or 'aromatic interface' rule: TM helices frequently begin and/or end with aromatic residues (W, Y, F) that anchor at the lipid-water interface. W at position 179 is consistent with an N-terminal membrane-interface anchor, supporting inclusion of W (and the adjacent G) in the helix and favoring a start at 179 over 181. Additionally, the first TM (31..51) in this same protein also begins with an aromatic residue (Tyr at 31), reinforcing the pattern within this topology. Choice C omits the clearly hydrophobic TM2 (112..132: LFLGLGIPFVELVVIIAVPAA), which a hydropathy scan would identify. Choice D uses entirely different coordinates inconsistent with the hydrophobic stretches in the sequence. Thus, family-level membrane-topology knowledge (aromatic interface rule, ENT-family 10-TM architecture, hydrophobicity of the identified segments) provides a transferable, if probabilistic, basis to prefer B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 2-residue difference between A (181..199) and B (179..199) is fine-grained, but the aromatic-belt principle—well-documented across many membrane proteins—gives a knowledgeable model a concrete, transferable reason to include the Trp at 179 as the helix boundary rather than starting at Leu-181. This is not a certainty (Gly-180 slightly weakens the argument, and the annotation is computational, ECO:0000255), but it constitutes a defensible probabilistic inference from general membrane-protein biology rather than a lookup of this protein's specific record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The only difference between A and B is a 2-residue shift in the 4th TM start (181 vs 179). While the aromatic-belt argument favors 179 (W), the intervening Gly-180 and the marginal hydropathy difference make 181 (L) a defensible alternative under a strict hydrophobicity threshold. The distinction is within the typical uncertainty of TM-boundary prediction methods, so a careful model could reasonably select either A or B without the specific annotation.


### Important caveats

- All ten TM annotations carry ECO:0000255 (inferred by similarity/proRule), i.e., computational prediction rather than direct experimental determination. The 2-residue boundary between 179 and 181 is within the expected error of such methods.
- The aromatic-belt argument is probabilistic, not deterministic; not all TM helices begin with aromatic residues, and the Gly at position 180 partially interrupts the hydrophobic stretch.
- The UniProt entry is flagged as a Fragment (499 aa), which could affect boundary annotations near the termini, though this does not affect the 179/181 question.
- The author's source snapshot is unknown; the current entry (v62, 2025-04-09) matches the benchmark sequence, but the annotation may have been refined since the benchmark was constructed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The critical distinction between A and B is the 4th TM start: 181..199 (A) vs 179..199 (B). Position 179 is Trp (W), position 180 is Gly (G), and position 181 is Leu (L). A well-established principle in membrane protein biology is the 'aromatic belt' or 'aromatic interface' rule: TM helices frequently begin and/or end with aromatic residues (W, Y, F) that anchor at the lipid-water interface. W at position 179 is consistent with an N-terminal membrane-interface anchor, supporting inclusion of W (and the adjacent G) in the helix and favoring a start at 179 over 181. Additionally, the first TM (31..51) in this same protein also begins with an aromatic residue (Tyr at 31), reinforcing the pattern within this topology. Choice C omits the clearly hydrophobic TM2 (112..132: LFLGLGIPFVELVVIIAVPAA), which a hydropathy scan would identify. Choice D uses entirely different coordinates inconsistent with the hydrophobic stretches in the sequence. Thus, family-level membrane-topology knowledge (aromatic interface rule, ENT-family 10-TM architecture, hydrophobicity of the identified segments) provides a transferable, if probabilistic, basis to prefer B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 2-residue difference between A (181..199) and B (179..199) is fine-grained, but the aromatic-belt principle—well-documented across many membrane proteins—gives a knowledgeable model a concrete, transferable reason to include the Trp at 179 as the helix boundary rather than starting at Leu-181. This is not a certainty (Gly-180 slightly weakens the argument, and the annotation is computational, ECO:0000255), but it constitutes a defensible probabilistic inference from general membrane-protein biology rather than a lookup of this protein's specific record."
  },
  "case_id": "transmembrane_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9NBV4 (LdNT2, Leishmania donovani nucleoside transporter 2, 499 aa) annotates exactly ten transmembrane helices at positions 31..51, 112..132, 133..153, 179..199, 212..232, 350..370, 378..398, 406..426, 428..448, and 475..495, all with ECO:0000255 (inferred by similarity/proRule). Choice B matches these boundaries exactly. The sequence match between the benchmark input and the source entry is confirmed (SHA-256 identical, 499 aa)."
  },
  "important_caveats": [
    "All ten TM annotations carry ECO:0000255 (inferred by similarity/proRule), i.e., computational prediction rather than direct experimental determination. The 2-residue boundary between 179 and 181 is within the expected error of such methods.",
    "The aromatic-belt argument is probabilistic, not deterministic; not all TM helices begin with aromatic residues, and the Gly at position 180 partially interrupts the hydrophobic stretch.",
    "The UniProt entry is flagged as a Fragment (499 aa), which could affect boundary annotations near the termini, though this does not affect the 179/181 question.",
    "The author's source snapshot is unknown; the current entry (v62, 2025-04-09) matches the benchmark sequence, but the annotation may have been refined since the benchmark was constructed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The only difference between A and B is a 2-residue shift in the 4th TM start (181 vs 179). While the aromatic-belt argument favors 179 (W), the intervening Gly-180 and the marginal hydropathy difference make 181 (L) a defensible alternative under a strict hydrophobicity threshold. The distinction is within the typical uncertainty of TM-boundary prediction methods, so a careful model could reasonably select either A or B without the specific annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9NBV4 (LdNT2, Leishmania donovani nucleoside transporter 2, 499 aa) annotates exactly ten transmembrane helices at positions 31..51, 112..132, 133..153, 179..199, 212..232, 350..370, 378..398, 406..426, 428..448, and 475..495, all with ECO:0000255 (inferred by similarity/proRule). Choice B matches these boundaries exactly. The sequence match between the benchmark input and the source entry is confirmed (SHA-256 identical, 499 aa).",
    "evidence_ids": ["C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The critical distinction between A and B is the 4th TM start: 181..199 (A) vs 179..199 (B). Position 179 is Trp (W), position 180 is Gly (G), and position 181 is Leu (L). A well-established principle in membrane protein biology is the 'aromatic belt' or 'aromatic interface' rule: TM helices frequently begin and/or end with aromatic residues (W, Y, F) that anchor at the lipid-water interface. W at position 179 is consistent with an N-terminal membrane-interface anchor, supporting inclusion of W (and the adjacent G) in the helix and favoring a start at 179 over 181. Additionally, the first TM (31..51) in this same protein also begins with an aromatic residue (Tyr at 31), reinforcing the pattern within this topology. Choice C omits the clearly hydrophobic TM2 (112..132: LFLGLGIPFVELVVIIAVPAA), which a hydropathy scan would identify. Choice D uses entirely different coordinates inconsistent with the hydrophobic stretches in the sequence. Thus, family-level membrane-topology knowledge (aromatic interface rule, ENT-family 10-TM architecture, hydrophobicity of the identified segments) provides a transferable, if probabilistic, basis to prefer B.",
    "missing_item_specific_fact": "",
    "reason": "The 2-residue difference between A (181..199) and B (179..199) is fine-grained, but the aromatic-belt principle—well-documented across many membrane proteins—gives a knowledgeable model a concrete, transferable reason to include the Trp at 179 as the helix boundary rather than starting at Leu-181. This is not a certainty (Gly-180 slightly weakens the argument, and the annotation is computational, ECO:0000255), but it constitutes a defensible probabilistic inference from general membrane-protein biology rather than a lookup of this protein's specific record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The only difference between A and B is a 2-residue shift in the 4th TM start (181 vs 179). While the aromatic-belt argument favors 179 (W), the intervening Gly-180 and the marginal hydropathy difference make 181 (L) a defensible alternative under a strict hydrophobicity threshold. The distinction is within the typical uncertainty of TM-boundary prediction methods, so a careful model could reasonably select either A or B without the specific annotation."
  },
  "important_caveats": [
    "All ten TM annotations carry ECO:0000255 (inferred by similarity/proRule), i.e., computational prediction rather than direct experimental determination. The 2-residue boundary between 179 and 181 is within the expected error of such methods.",
    "The aromatic-belt argument is probabilistic, not deterministic; not all TM helices begin with aromatic residues, and the Gly at position 180 partially interrupts the hydrophobic stretch.",
    "The UniProt entry is flagged as a Fragment (499 aa), which could affect boundary annotations near the termini, though this does not affect the 179/181 question.",
    "The author's source snapshot is unknown; the current entry (v62, 2025-04-09) matches the benchmark sequence, but the annotation may have been refined since the benchmark was constructed."
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
  "benchmark_sequence_length": 499,
  "benchmark_sequence_sha256": "99913046670b07d17f5e37245b365956cb766f4099d4fd004331889bf4858b34",
  "current_entry_audit": {
    "entryVersion": 62,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2025-06-18",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 499,
  "current_source_sequence_sha256": "99913046670b07d17f5e37245b365956cb766f4099d4fd004331889bf4858b34",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 62,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9NBV4",
  "selected_historical_entry_version": 62,
  "selected_historical_record_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "selected_historical_source_sequence_length": 499,
  "selected_historical_source_sequence_sha256": "99913046670b07d17f5e37245b365956cb766f4099d4fd004331889bf4858b34",
  "selected_historical_version": {
    "accession": "Q9NBV4",
    "database": "Swiss-Prot",
    "entryVersion": 62,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_03/2026_03",
    "lastReleaseDate": "02-Sep-2026",
    "name": "NT2_LEIDO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9NBV4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":62,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2025-06-18\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF74264.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Leishmania\"],\"scientificName\":\"Leishmania donovani\",\"taxonId\":5661}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"12835315\",\"source\":\"PubMed\"}],\"value\":\"Equilibrative nucleoside transporter 2\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF74264.1\",\"source\":\"EMBL\"}],\"value\":\"Inosine-guanosine nucleoside transporter\"}}],\"flag\":\"Fragment\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10783393\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10783393\",\"source\":\"PubMed\"}],\"value\":\"LdNT2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12807872\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":30},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":51},\"start\":{\"modifier\":\"EXACT\",\"value\":31}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":132},\"start\":{\"modifier\":\"EXACT\",\"value\":112}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":153},\"start\":{\"modifier\":\"EXACT\",\"value\":133}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":199},\"start\":{\"modifier\":\"EXACT\",\"value\":179}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":232},\"start\":{\"modifier\":\"EXACT\",\"value\":212}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":370},\"start\":{\"modifier\":\"EXACT\",\"value\":350}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":398},\"start\":{\"modifier\":\"EXACT\",\"value\":378}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":426},\"start\":{\"modifier\":\"EXACT\",\"value\":406}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":448},\"start\":{\"modifier\":\"EXACT\",\"value\":428}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":495},\"start\":{\"modifier\":\"EXACT\",\"value\":475}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Carter N.S.\",\"Drew M.E.\",\"Sanchez M.\",\"Vasudevan G.\",\"Landfear S.M.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10783393\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m002418200\"}],\"citationType\":\"journal article\",\"firstPage\":\"20935\",\"id\":\"10783393\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"20941\",\"publicationDate\":\"2000\",\"title\":\"Cloning of a novel inosine-guanosine transporter gene from Leishmania donovani by functional rescue of a transport-deficient mutant.\",\"volume\":\"275\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF74264.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Arastu-Kapur S.\",\"Ford E.\",\"Ullman B.\",\"Carter N.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12807872\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m305141200\"}],\"citationType\":\"journal article\",\"firstPage\":\"33327\",\"id\":\"12807872\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"33333\",\"publicationDate\":\"2003\",\"title\":\"Functional analysis of an inosine-guanosine transporter from Leishmania donovani. The role of conserved residues, aspartate 389 and arginine 393.\",\"volume\":\"278\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"TOPOLOGY\",\"MUTAGENESIS OF ASP-389 AND ARG-393\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"citation\":{\"authors\":[\"Stein A.\",\"Vaseduvan G.\",\"Carter N.S.\",\"Ullman B.\",\"Landfear S.M.\",\"Kavanaugh M.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12835315\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m306188200\"}],\"citationType\":\"journal article\",\"firstPage\":\"35127\",\"id\":\"12835315\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"35134\",\"publicationDate\":\"2003\",\"title\":\"Equilibrative nucleoside transporter family members from Leishmania donovani are electrogenic proton symporters.\",\"volume\":\"278\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H1",
  "excerpt": "ID   NT2_LEIDO               Reviewed;         499 AA.\nAC   Q9NBV4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   18-JUN-2025, entry version 62.\nDE   RecName: Full=Nucleoside transporter 2 {ECO:0000303|PubMed:10783393};\nDE            Short=LdNT2 {ECO:0000303|PubMed:10783393};\nDE   AltName: Full=Equilibrative nucleoside transporter 2 {ECO:0000303|PubMed:12835315};\nDE   AltName: Full=Inosine-guanosine nucleoside transporter {ECO:0000312|EMBL:AAF74264.1};\nDE   Flags: Fragment;\nGN   Name=NT2 {ECO:0000312|EMBL:AAF74264.1};\nOS   Leishmania donovani.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Leishmania.\nOX   NCBI_TaxID=5661 {ECO:0000312|EMBL:AAF74264.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAF74264.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, TRANSPORTER ACTIVITY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=10783393; DOI=10.1074/jbc.m002418200;\nRA   Carter N.S., Drew M.E., Sanchez M., Vasudevan G., Landfear S.M., Ullman B.;\nRT   \"Cloning of a novel inosine-guanosine transporter gene from Leishmania\nRT   donovani by functional rescue of a transport-deficient mutant.\";\nRL   J. Biol. Chem. 275:20935-20941(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR\nRP   LOCATION, DISRUPTION PHENOTYPE, TOPOLOGY, AND MUTAGENESIS OF ASP-389 AND\nRP   ARG-393.\nRX   PubMed=12807872; DOI=10.1074/jbc.m305141200;\nRA   Arastu-Kapur S., Ford E., Ullman B., Carter N.S.;\nRT   \"Functional analysis of an inosine-guanosine transporter from Leishmania\nRT   donovani. The role of conserved residues, aspartate 389 and arginine 393.\";\nRL   J. Biol. Chem. 278:33327-33333(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H4",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND TRANSPORTER ACTIVITY.\nRX   PubMed=12835315; DOI=10.1074/jbc.m306188200;\nRA   Stein A., Vaseduvan G., Carter N.S., Ullman B., Landfear S.M.,\nRA   Kavanaugh M.P.;\nRT   \"Equilibrative nucleoside transporter family members from Leishmania\nRT   donovani are electrogenic proton symporters.\";\nRL   J. Biol. Chem. 278:35127-35134(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H5",
  "excerpt": "FT   TOPO_DOM        1..30\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:12807872\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        31..51\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        112..132\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-150",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        133..153\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 151-153",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        179..199\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 154-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        212..232\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 157-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        350..370\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        378..398\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-165",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        406..426\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 166-168",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        428..448\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 169-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H15",
  "excerpt": "FT   TRANSMEM        475..495\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 123. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
