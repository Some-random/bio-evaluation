# transmembrane_0037

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0037.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 1..21

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEFSFSSPLLYILYFLLFFIVRQLLKPKSNRKLPPGPRTLPIIGNLHQLRGSLPHRTLKKLSDKHGPLMHLKMGERSAIIVSDARMAKIVLHNHGLAVADRSVNTVASIMTYNSLGVTFAQYGDYLTKLRQIYTLELLSPKKVRSFYNCFEDELDVFVKSIRSQVGQPMVLYEKVSTYLYATICRTIFGSVCKEREKMIKIVKRTSLLSGTPLRMEDLFPSMRVFCRFSKTLNQLRGLLQEMDGILEDIIVEREKTTEILKEAKDDEDMLSVLLRHKWYNPSGARFRITNADIKAIIFELILAATLSVADVVEWAMVEILRHPAILKKVYDEGRGICKEKKRVTGYDVEKMEYMRLCVKESTRVHPAAPLLVPRECREDFEVDGYTVPKGAWVLTNCWAIQMDPEIWPEPEKFDPERYIRNPMDFYGSNFELIPFGTGRRGCPGILYGVTNAELLLAAMFYHFDWEIADGKKPEDIDLTENFGAGCIMKYPLTLVPHLANE

[Multiple Choices]
A. 1..21
B. 6..26; 300..320; 337..357; 373..393; 416..436; 439..459
C. 1..20
D. 1..21; 221..245
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

> The sequence has a strongly hydrophobic N-terminal stretch consistent with a membrane-spanning helix. The sequence-matched UniProt record annotates residues 1..21 as a helical transmembrane feature, with computational evidence (ECO:0000255); the historical matched record has the same annotation. This supports the key, though it is not experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic stretch and transferable knowledge of membrane-anchored cytochrome P450 proteins support a single N-terminal membrane anchor, distinguishing that region from the proposed internal spans. But those features do not meaningfully determine whether its endpoint is residue 20 or 21.


**Missing item-specific fact**

> A precise annotation or measurement of the membrane-helix boundary is needed to prefer 1..21 over the nearly identical 1..20 option.


**Reason**

> Biology supports the location of the membrane anchor, but the exact one-residue boundary that separates the key from option C is not reliably inferable from the sequence or family pattern alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both options identify the same N-terminal hydrophobic segment and differ only by its final residue; the sequence does not establish that boundary precisely.


### Important caveats

- The cited transmembrane feature is a sequence-matched computational database annotation, not experimental evidence.
- The source record supports the author's precise endpoint, but that reviewer-only information was not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch and transferable knowledge of membrane-anchored cytochrome P450 proteins support a single N-terminal membrane anchor, distinguishing that region from the proposed internal spans. But those features do not meaningfully determine whether its endpoint is residue 20 or 21.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A precise annotation or measurement of the membrane-helix boundary is needed to prefer 1..21 over the nearly identical 1..20 option.",
    "reason": "Biology supports the location of the membrane anchor, but the exact one-residue boundary that separates the key from option C is not reliably inferable from the sequence or family pattern alone."
  },
  "case_id": "transmembrane_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence has a strongly hydrophobic N-terminal stretch consistent with a membrane-spanning helix. The sequence-matched UniProt record annotates residues 1..21 as a helical transmembrane feature, with computational evidence (ECO:0000255); the historical matched record has the same annotation. This supports the key, though it is not experimental confirmation."
  },
  "important_caveats": [
    "The cited transmembrane feature is a sequence-matched computational database annotation, not experimental evidence.",
    "The source record supports the author's precise endpoint, but that reviewer-only information was not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both options identify the same N-terminal hydrophobic segment and differ only by its final residue; the sequence does not establish that boundary precisely."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence has a strongly hydrophobic N-terminal stretch consistent with a membrane-spanning helix. The sequence-matched UniProt record annotates residues 1..21 as a helical transmembrane feature, with computational evidence (ECO:0000255); the historical matched record has the same annotation. This supports the key, though it is not experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch and transferable knowledge of membrane-anchored cytochrome P450 proteins support a single N-terminal membrane anchor, distinguishing that region from the proposed internal spans. But those features do not meaningfully determine whether its endpoint is residue 20 or 21.",
    "missing_item_specific_fact": "A precise annotation or measurement of the membrane-helix boundary is needed to prefer 1..21 over the nearly identical 1..20 option.",
    "reason": "Biology supports the location of the membrane anchor, but the exact one-residue boundary that separates the key from option C is not reliably inferable from the sequence or family pattern alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both options identify the same N-terminal hydrophobic segment and differ only by its final residue; the sequence does not establish that boundary precisely."
  },
  "important_caveats": [
    "The cited transmembrane feature is a sequence-matched computational database annotation, not experimental evidence.",
    "The source record supports the author's precise endpoint, but that reviewer-only information was not part of the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A9E7S4M4, Geissoschizine oxidase / Cytochrome P450 GO from Alstonia scholaris) annotates a single Transmembrane helical region at positions 1..21 (evidence code ECO:0000255, PROSITE-ProRule computational annotation). The sequence M(1)E(2)F(3)S(4)F(5)S(6)S(7)P(8)L(9)L(10)Y(11)I(12)L(13)Y(14)F(15)L(16)L(17)F(18)F(19)I(20)V(21) followed by R(22) shows a hydrophobic core (positions 9–21: LLYILYFLLFFIV) with a sharp hydrophobicity drop at the charged Arg22, consistent with a single-pass N-terminal TM anchor. The annotation is computational (ECO:0000255), not experimentally validated, but it is the standard database annotation supporting the key.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains hallmark cytochrome P450 motifs (e.g., the heme-binding FxxGxxxCxG-like region 'FGTGRRGCPGILYG' near position 430, overall ~500 aa length, conserved P450 domain architecture). A well-established family-level fact is that cytochrome P450 enzymes are anchored to the ER (or mitochondrial) membrane by a SINGLE N-terminal transmembrane helix, not by multiple passes. This eliminates option B (six TM regions, typical of multi-pass channels/transporters) and option D (two TM regions, atypical for P450s). Hydrophobicity inspection of the N-terminus reveals a clear hydrophobic stretch LLYILYFLLFFIV (positions 9–21) followed immediately by charged R(22), giving a natural TM boundary ending at 21. Option C (1..20) truncates the last hydrophobic residue V(21) without a hydrophobicity-based reason to do so, whereas option A (1..21) captures the full hydrophobic stretch up to the charged boundary. Thus, P450 family topology knowledge plus straightforward hydrophobicity profiling distinguishes A from B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can (1) recognize the P450 fold from conserved motifs and length, (2) apply the well-known single-N-terminal-TM-anchor topology of the P450 superfamily to eliminate multi-pass options B and D, and (3) perform hydrophobicity analysis on the N-terminal 25 residues to identify the TM segment and its natural boundary at position 21 (last hydrophobic residue before charged Arg22), distinguishing A from C. All of this relies on transferable family-level and sequence-analysis knowledge, not on a lookup of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are eliminated by P450 family topology (single N-terminal anchor). Option C (1..20) is less defensible than A (1..21) because V(21) is hydrophobic and the next residue R(22) is charged, making 21 the natural hydrophobicity boundary. While the 1-vs-20/21 boundary is subtle, the hydrophobicity profile favors 21, and no strong argument supports exactly 20 over 21.


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is a computational/pattern-based prediction, not experimental validation. The TM assignment is a standard computational annotation.
- The N-terminal residues 1–8 (MEFSFSSP) include charged and polar residues and a proline, which are atypical for the core of a TM helix; the annotation extends the TM region to include them, likely reflecting the full predicted helical segment including flanking residues.
- The distinction between A (1..21) and C (1..20) is a single-residue boundary difference; while the hydrophobicity profile favors 21, both are within the normal range of TM helix lengths (18–25 residues).
- The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA-256 match), but the accession and organism identity were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains hallmark cytochrome P450 motifs (e.g., the heme-binding FxxGxxxCxG-like region 'FGTGRRGCPGILYG' near position 430, overall ~500 aa length, conserved P450 domain architecture). A well-established family-level fact is that cytochrome P450 enzymes are anchored to the ER (or mitochondrial) membrane by a SINGLE N-terminal transmembrane helix, not by multiple passes. This eliminates option B (six TM regions, typical of multi-pass channels/transporters) and option D (two TM regions, atypical for P450s). Hydrophobicity inspection of the N-terminus reveals a clear hydrophobic stretch LLYILYFLLFFIV (positions 9–21) followed immediately by charged R(22), giving a natural TM boundary ending at 21. Option C (1..20) truncates the last hydrophobic residue V(21) without a hydrophobicity-based reason to do so, whereas option A (1..21) captures the full hydrophobic stretch up to the charged boundary. Thus, P450 family topology knowledge plus straightforward hydrophobicity profiling distinguishes A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) recognize the P450 fold from conserved motifs and length, (2) apply the well-known single-N-terminal-TM-anchor topology of the P450 superfamily to eliminate multi-pass options B and D, and (3) perform hydrophobicity analysis on the N-terminal 25 residues to identify the TM segment and its natural boundary at position 21 (last hydrophobic residue before charged Arg22), distinguishing A from C. All of this relies on transferable family-level and sequence-analysis knowledge, not on a lookup of this specific protein's database entry."
  },
  "case_id": "transmembrane_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7S4M4, Geissoschizine oxidase / Cytochrome P450 GO from Alstonia scholaris) annotates a single Transmembrane helical region at positions 1..21 (evidence code ECO:0000255, PROSITE-ProRule computational annotation). The sequence M(1)E(2)F(3)S(4)F(5)S(6)S(7)P(8)L(9)L(10)Y(11)I(12)L(13)Y(14)F(15)L(16)L(17)F(18)F(19)I(20)V(21) followed by R(22) shows a hydrophobic core (positions 9–21: LLYILYFLLFFIV) with a sharp hydrophobicity drop at the charged Arg22, consistent with a single-pass N-terminal TM anchor. The annotation is computational (ECO:0000255), not experimentally validated, but it is the standard database annotation supporting the key."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is a computational/pattern-based prediction, not experimental validation. The TM assignment is a standard computational annotation.",
    "The N-terminal residues 1–8 (MEFSFSSP) include charged and polar residues and a proline, which are atypical for the core of a TM helix; the annotation extends the TM region to include them, likely reflecting the full predicted helical segment including flanking residues.",
    "The distinction between A (1..21) and C (1..20) is a single-residue boundary difference; while the hydrophobicity profile favors 21, both are within the normal range of TM helix lengths (18–25 residues).",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA-256 match), but the accession and organism identity were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are eliminated by P450 family topology (single N-terminal anchor). Option C (1..20) is less defensible than A (1..21) because V(21) is hydrophobic and the next residue R(22) is charged, making 21 the natural hydrophobicity boundary. While the 1-vs-20/21 boundary is subtle, the hydrophobicity profile favors 21, and no strong argument supports exactly 20 over 21."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7S4M4, Geissoschizine oxidase / Cytochrome P450 GO from Alstonia scholaris) annotates a single Transmembrane helical region at positions 1..21 (evidence code ECO:0000255, PROSITE-ProRule computational annotation). The sequence M(1)E(2)F(3)S(4)F(5)S(6)S(7)P(8)L(9)L(10)Y(11)I(12)L(13)Y(14)F(15)L(16)L(17)F(18)F(19)I(20)V(21) followed by R(22) shows a hydrophobic core (positions 9–21: LLYILYFLLFFIV) with a sharp hydrophobicity drop at the charged Arg22, consistent with a single-pass N-terminal TM anchor. The annotation is computational (ECO:0000255), not experimentally validated, but it is the standard database annotation supporting the key.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains hallmark cytochrome P450 motifs (e.g., the heme-binding FxxGxxxCxG-like region 'FGTGRRGCPGILYG' near position 430, overall ~500 aa length, conserved P450 domain architecture). A well-established family-level fact is that cytochrome P450 enzymes are anchored to the ER (or mitochondrial) membrane by a SINGLE N-terminal transmembrane helix, not by multiple passes. This eliminates option B (six TM regions, typical of multi-pass channels/transporters) and option D (two TM regions, atypical for P450s). Hydrophobicity inspection of the N-terminus reveals a clear hydrophobic stretch LLYILYFLLFFIV (positions 9–21) followed immediately by charged R(22), giving a natural TM boundary ending at 21. Option C (1..20) truncates the last hydrophobic residue V(21) without a hydrophobicity-based reason to do so, whereas option A (1..21) captures the full hydrophobic stretch up to the charged boundary. Thus, P450 family topology knowledge plus straightforward hydrophobicity profiling distinguishes A from B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) recognize the P450 fold from conserved motifs and length, (2) apply the well-known single-N-terminal-TM-anchor topology of the P450 superfamily to eliminate multi-pass options B and D, and (3) perform hydrophobicity analysis on the N-terminal 25 residues to identify the TM segment and its natural boundary at position 21 (last hydrophobic residue before charged Arg22), distinguishing A from C. All of this relies on transferable family-level and sequence-analysis knowledge, not on a lookup of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are eliminated by P450 family topology (single N-terminal anchor). Option C (1..20) is less defensible than A (1..21) because V(21) is hydrophobic and the next residue R(22) is charged, making 21 the natural hydrophobicity boundary. While the 1-vs-20/21 boundary is subtle, the hydrophobicity profile favors 21, and no strong argument supports exactly 20 over 21."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is a computational/pattern-based prediction, not experimental validation. The TM assignment is a standard computational annotation.",
    "The N-terminal residues 1–8 (MEFSFSSP) include charged and polar residues and a proline, which are atypical for the core of a TM helix; the annotation extends the TM region to include them, likely reflecting the full predicted helical segment including flanking residues.",
    "The distinction between A (1..21) and C (1..20) is a single-residue boundary difference; while the hydrophobicity profile favors 21, both are within the normal range of TM helix lengths (18–25 residues).",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA-256 match), but the accession and organism identity were not provided to the evaluated model."
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
  "benchmark_sequence_length": 501,
  "benchmark_sequence_sha256": "d3eae0cbb53ce9ef6fc350479b75f6672c3885569ccd784ba7d6639abdda8626",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 501,
  "current_source_sequence_sha256": "d3eae0cbb53ce9ef6fc350479b75f6672c3885569ccd784ba7d6639abdda8626",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7S4M4",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "991588eea7e058afe44fddcc48282d5e07529aa26a2d5757e5dbab96577b2d25",
  "selected_historical_source_sequence_length": 501,
  "selected_historical_source_sequence_sha256": "d3eae0cbb53ce9ef6fc350479b75f6672c3885569ccd784ba7d6639abdda8626",
  "selected_historical_version": {
    "accession": "A0A9E7S4M4",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GO_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7S4M4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:10.590145+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:10.590145+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:10.590145+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 GO\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.14.19.80\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Geissoschizine oxidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsGO\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:10.590145+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":21},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:26:10.590145+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65383.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"MUTAGENESIS OF ILE-109; VAL-202; THR-205; SER-209 AND VAL-372\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:10.590145+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   GO_ALSSC                Reviewed;         501 AA.\nAC   A0A9E7S4M4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Geissoschizine oxidase {ECO:0000303|PubMed:36349266};\nDE            Short=AsGO {ECO:0000303|PubMed:36349266};\nDE            EC=1.14.19.80 {ECO:0000269|PubMed:36349266};\nDE   AltName: Full=Cytochrome P450 GO {ECO:0000303|PubMed:36349266};\nGN   Name=GO {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.830408+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "991588eea7e058afe44fddcc48282d5e07529aa26a2d5757e5dbab96577b2d25",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S4M4?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65383.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, MUTAGENESIS OF ILE-109; VAL-202;\nRP   THR-205; SER-209 AND VAL-372, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.830408+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "991588eea7e058afe44fddcc48282d5e07529aa26a2d5757e5dbab96577b2d25",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S4M4?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        1..21\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.830408+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "991588eea7e058afe44fddcc48282d5e07529aa26a2d5757e5dbab96577b2d25",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S4M4?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
