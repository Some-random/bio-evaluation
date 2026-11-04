# catalytic_activity_0152

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0152.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — Hydrolysis of terminal, non-reducing (1-&gt;4)-linked alpha-D-glucose residues with release of alpha-D-glucose.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPPLGVLLLLVALGHSTQGHRPLPIRKAHKFDWWERGNFYQIYPRSFKDSDGDGIGDLKGITQTIDYLKTIGIDGVWLSPIFKSPMNDFGYDISDFYAIQEEYGTMEDFEELAAKCASIGLKLILDFVPNHSSDEHEHFRLSEEGIEPYKDYYIWHSGVLDANGTRHPPSNWISVFRGSAWQWSDKRQQYYLHQFQKKQPDLNYRNPALVEEMKNVMRFWLNKGIAGFRIDALPYLFESEEVDGHYRDEPLSGQATDDPDNPAYLTHTETKDQPETYDMVHQWRQVVDEYTARDNFTRIILTEAYTAVQNMTRFYGTPAAPGAQIPFNFQLITLLTVNSTGRDFVNAVQSWTRAMPSGAIANWVLGNHDNSRIASRLGVARADLYNIALQTLPGIAVTYYGEEIAMVDQWISWNDTIDPAACNADPATYELYSRDPVRTPFQWSNGTNAGFSNASRTWLPVADGYRELNVAAQLAAPRSHLKTFMQLTAYRKRRLLAEGNFVLRTVGRDLVMYKRSVPGVGYVVVALNFGPEPATLPVASQFPGTGEHWLKVIASSLQAQPQAGTWINTRLYKLAPDSGIVLERLTGRNDLMT

[Multiple Choices]
A. (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate
B. Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.
C. O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine + succinate + H(+)
D. pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1184)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.1.20 and gives the same alpha-glucosidase reaction as option B. The catalytic-activity annotation carries experimental evidence code ECO:0000269.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region and a long enzyme-sized domain with features consistent with a secreted glycoside hydrolase. Transferable knowledge of alpha-glucosidase families connects that kind of sequence to hydrolysis of terminal alpha-linked glucose residues, distinguishing B from the terpene-forming, cystathionine-forming, and pyrrolizine-amide hydrolysis alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and secretion clues provide a meaningful basis for choosing the alpha-glucosidase reaction. The exact activity is not guaranteed from sequence alone, but the offered alternatives are sufficiently distinct for this inference.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction classes, and the sequence supports the alpha-glucosidase choice."
  },
  "important_caveats": [
    "The reviewer-only record supports the key, but its annotations were not available as original model input.",
    "The sequence-based family inference is probabilistic; it does not independently establish every substrate-specific detail of the reaction."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q7PYT9 (MALT_ANOGA) is annotated as 'Salivary alpha-glucosidase' with EC 3.2.1.20, and the catalytic activity comment states exactly: 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' This is supported by experimental evidence (ECO:0000269, PubMed:38428508, a 2024 structural and functional study). The benchmark sequence matches the source entry (593 aa, SHA256 confirmed). Option B text matches the annotation verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable sequence features support identifying this as a GH31 alpha-glucosidase and distinguishing it from the three distractors: (1) A clear N-terminal signal peptide (MPPLGVLLLLVALGHSTQG) indicates a secreted protein, consistent with a salivary glycosidase rather than a cytoplasmic terpene synthase (A), a PLP-dependent cystathionine gamma-synthase (C), or a specialized amidase (D). (2) The sequence contains an unusually high density of tryptophan residues clustered in the central region (WLSPI, WISVFRGSAWQWS, WLNK, WVLGN, WISWND, WLPVADG, WIKVI, WLNTR), which is a hallmark of GH31 glycoside hydrolases whose active-site sugar-binding pockets are lined with multiple Trp residues. This Trp-rich pattern is not a feature of terpene cyclases (which use DDxxD motifs), PLP enzymes (which use a conserved Lys for Schiff-base formation), or simple amidases. (3) The ~593 aa length is consistent with the TIM-barrel fold of GH31 enzymes. (4) The 'WLSPI' motif near the N-terminus resembles the conserved 'WID/WLD' nucleophile region of GH31, and 'DEHEHFRL' contains the 'HE' acid/base signature. (5) The distractors represent entirely different enzyme classes with incompatible sequence signatures: option A requires a terpene cyclase fold with DDxxD motifs; option C requires a PLP-binding lysine and the fold of a gamma-synthase; option D is a highly specialized amidase with no recognizable glycosidase features. The combination of signal peptide, Trp-rich GH31 architecture, and length provides a credible, transferable inference favoring B over A, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the signal peptide, the distinctive Trp-rich pattern characteristic of GH31 alpha-glucosidases, the approximate length, and the absence of terpene-cyclase (DDxxD), PLP-binding (conserved Lys), or amidase signatures to meaningfully favor option B over the three clearly different enzyme classes offered. This is family-level pattern recognition transferable from other GH31 proteins, not a lookup of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different enzyme classes (terpene synthase, alpha-glucosidase, PLP-dependent synthase, specialized amidase) with incompatible sequence and mechanistic signatures. The GH31 Trp-rich pattern and signal peptide clearly favor B; no other option is defensible given the sequence features.


### Important caveats

- The GH31 identification relies on recognizing the Trp-rich active-site architecture and approximate motif patterns; a model unfamiliar with GH31-specific signatures might find the inference less certain, though the elimination of clearly incompatible distractor classes still strongly favors B.
- The experimental evidence (PubMed:38428508, 2024) post-dates the original sequence submission (2007); the annotation was added after the sequence was deposited, so the original record may have lacked the EC assignment at the time of benchmark construction. However, the sequence itself carries the GH31 family features regardless of annotation timing.
- Distinguishing alpha-glucosidase (EC 3.2.1.20) from other GH31 members (e.g., alpha-xylosidase, EC 3.2.1.100) purely from sequence is not trivial, but the offered options do not include such a close alternative.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable sequence features support identifying this as a GH31 alpha-glucosidase and distinguishing it from the three distractors: (1) A clear N-terminal signal peptide (MPPLGVLLLLVALGHSTQG) indicates a secreted protein, consistent with a salivary glycosidase rather than a cytoplasmic terpene synthase (A), a PLP-dependent cystathionine gamma-synthase (C), or a specialized amidase (D). (2) The sequence contains an unusually high density of tryptophan residues clustered in the central region (WLSPI, WISVFRGSAWQWS, WLNK, WVLGN, WISWND, WLPVADG, WIKVI, WLNTR), which is a hallmark of GH31 glycoside hydrolases whose active-site sugar-binding pockets are lined with multiple Trp residues. This Trp-rich pattern is not a feature of terpene cyclases (which use DDxxD motifs), PLP enzymes (which use a conserved Lys for Schiff-base formation), or simple amidases. (3) The ~593 aa length is consistent with the TIM-barrel fold of GH31 enzymes. (4) The 'WLSPI' motif near the N-terminus resembles the conserved 'WID/WLD' nucleophile region of GH31, and 'DEHEHFRL' contains the 'HE' acid/base signature. (5) The distractors represent entirely different enzyme classes with incompatible sequence signatures: option A requires a terpene cyclase fold with DDxxD motifs; option C requires a PLP-binding lysine and the fold of a gamma-synthase; option D is a highly specialized amidase with no recognizable glycosidase features. The combination of signal peptide, Trp-rich GH31 architecture, and length provides a credible, transferable inference favoring B over A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the signal peptide, the distinctive Trp-rich pattern characteristic of GH31 alpha-glucosidases, the approximate length, and the absence of terpene-cyclase (DDxxD), PLP-binding (conserved Lys), or amidase signatures to meaningfully favor option B over the three clearly different enzyme classes offered. This is family-level pattern recognition transferable from other GH31 proteins, not a lookup of this specific entry's annotation."
  },
  "case_id": "catalytic_activity_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q7PYT9 (MALT_ANOGA) is annotated as 'Salivary alpha-glucosidase' with EC 3.2.1.20, and the catalytic activity comment states exactly: 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' This is supported by experimental evidence (ECO:0000269, PubMed:38428508, a 2024 structural and functional study). The benchmark sequence matches the source entry (593 aa, SHA256 confirmed). Option B text matches the annotation verbatim."
  },
  "important_caveats": [
    "The GH31 identification relies on recognizing the Trp-rich active-site architecture and approximate motif patterns; a model unfamiliar with GH31-specific signatures might find the inference less certain, though the elimination of clearly incompatible distractor classes still strongly favors B.",
    "The experimental evidence (PubMed:38428508, 2024) post-dates the original sequence submission (2007); the annotation was added after the sequence was deposited, so the original record may have lacked the EC assignment at the time of benchmark construction. However, the sequence itself carries the GH31 family features regardless of annotation timing.",
    "Distinguishing alpha-glucosidase (EC 3.2.1.20) from other GH31 members (e.g., alpha-xylosidase, EC 3.2.1.100) purely from sequence is not trivial, but the offered options do not include such a close alternative."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (terpene synthase, alpha-glucosidase, PLP-dependent synthase, specialized amidase) with incompatible sequence and mechanistic signatures. The GH31 Trp-rich pattern and signal peptide clearly favor B; no other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q7PYT9 (MALT_ANOGA) is annotated as 'Salivary alpha-glucosidase' with EC 3.2.1.20, and the catalytic activity comment states exactly: 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' This is supported by experimental evidence (ECO:0000269, PubMed:38428508, a 2024 structural and functional study). The benchmark sequence matches the source entry (593 aa, SHA256 confirmed). Option B text matches the annotation verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable sequence features support identifying this as a GH31 alpha-glucosidase and distinguishing it from the three distractors: (1) A clear N-terminal signal peptide (MPPLGVLLLLVALGHSTQG) indicates a secreted protein, consistent with a salivary glycosidase rather than a cytoplasmic terpene synthase (A), a PLP-dependent cystathionine gamma-synthase (C), or a specialized amidase (D). (2) The sequence contains an unusually high density of tryptophan residues clustered in the central region (WLSPI, WISVFRGSAWQWS, WLNK, WVLGN, WISWND, WLPVADG, WIKVI, WLNTR), which is a hallmark of GH31 glycoside hydrolases whose active-site sugar-binding pockets are lined with multiple Trp residues. This Trp-rich pattern is not a feature of terpene cyclases (which use DDxxD motifs), PLP enzymes (which use a conserved Lys for Schiff-base formation), or simple amidases. (3) The ~593 aa length is consistent with the TIM-barrel fold of GH31 enzymes. (4) The 'WLSPI' motif near the N-terminus resembles the conserved 'WID/WLD' nucleophile region of GH31, and 'DEHEHFRL' contains the 'HE' acid/base signature. (5) The distractors represent entirely different enzyme classes with incompatible sequence signatures: option A requires a terpene cyclase fold with DDxxD motifs; option C requires a PLP-binding lysine and the fold of a gamma-synthase; option D is a highly specialized amidase with no recognizable glycosidase features. The combination of signal peptide, Trp-rich GH31 architecture, and length provides a credible, transferable inference favoring B over A, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the signal peptide, the distinctive Trp-rich pattern characteristic of GH31 alpha-glucosidases, the approximate length, and the absence of terpene-cyclase (DDxxD), PLP-binding (conserved Lys), or amidase signatures to meaningfully favor option B over the three clearly different enzyme classes offered. This is family-level pattern recognition transferable from other GH31 proteins, not a lookup of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (terpene synthase, alpha-glucosidase, PLP-dependent synthase, specialized amidase) with incompatible sequence and mechanistic signatures. The GH31 Trp-rich pattern and signal peptide clearly favor B; no other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GH31 identification relies on recognizing the Trp-rich active-site architecture and approximate motif patterns; a model unfamiliar with GH31-specific signatures might find the inference less certain, though the elimination of clearly incompatible distractor classes still strongly favors B.",
    "The experimental evidence (PubMed:38428508, 2024) post-dates the original sequence submission (2007); the annotation was added after the sequence was deposited, so the original record may have lacked the EC assignment at the time of benchmark construction. However, the sequence itself carries the GH31 family features regardless of annotation timing.",
    "Distinguishing alpha-glucosidase (EC 3.2.1.20) from other GH31 members (e.g., alpha-xylosidase, EC 3.2.1.100) purely from sequence is not trivial, but the offered options do not include such a close alternative."
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
  "benchmark_sequence_length": 593,
  "benchmark_sequence_sha256": "b5c0d534d7a7b2a76bff2705c7926754dc64b40cdbcc8632b99a9db0d4f8a9b7",
  "current_entry_audit": {
    "entryVersion": 134,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-01-09",
    "sequenceVersion": 3
  },
  "current_record_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 593,
  "current_source_sequence_sha256": "b5c0d534d7a7b2a76bff2705c7926754dc64b40cdbcc8632b99a9db0d4f8a9b7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 132,
      "exact_sequence_comparison": "matched",
      "sequence_version": 3
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q7PYT9",
  "selected_historical_entry_version": 132,
  "selected_historical_record_sha256": "de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052",
  "selected_historical_source_sequence_length": 593,
  "selected_historical_source_sequence_sha256": "b5c0d534d7a7b2a76bff2705c7926754dc64b40cdbcc8632b99a9db0d4f8a9b7",
  "selected_historical_version": {
    "accession": "Q7PYT9",
    "database": "Swiss-Prot",
    "entryVersion": 132,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MALT_ANOGA",
    "sequenceVersion": 3
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q7PYT9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":134,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-01-09\",\"sequenceVersion\":3}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"African malaria mosquito\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"EAA00998.3\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Nematocera\",\"Culicoidea\",\"Culicidae\",\"Anophelinae\",\"Anopheles\"],\"scientificName\":\"Anopheles gambiae\",\"taxonId\":7165}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.20\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"Salivary alpha-glucosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"AnGluc\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.20\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Williams A.E.\",\"Gittis A.G.\",\"Botello K.\",\"Cruz P.\",\"Martin-Martin I.\",\"Valenzuela Leon P.C.\",\"Sumner B.\",\"Bonilla B.\",\"Calvo E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38428508\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ibmb.2024.104097\"}],\"citationType\":\"journal article\",\"firstPage\":\"104097\",\"id\":\"38428508\",\"journal\":\"Insect Biochem. Mol. Biol.\",\"lastPage\":\"104097\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.\",\"volume\":\"167\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H1",
  "excerpt": "ID   MALT_ANOGA              Reviewed;         593 AA.\nAC   Q7PYT9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-JAN-2007, sequence version 3.\nDT   28-JAN-2026, entry version 132.\nDE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=AnGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:38428508};\nDE   Flags: Precursor;\nGN   Name=MAL1 {ECO:0000250|UniProtKB:P13080};\nGN   ORFNames=AgaP_AGAP002102 {ECO:0000312|EMBL:EAA00998.3};\nOS   Anopheles gambiae (African malaria mosquito).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;\nOC   Anophelinae; Anopheles.\nOX   NCBI_TaxID=7165 {ECO:0000312|EMBL:EAA00998.3};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:03.279027+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052",
  "url": "https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=AnGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:38428508};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:03.279027+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052",
  "url": "https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR\nRP   LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=38428508; DOI=10.1016/j.ibmb.2024.104097;\nRA   Williams A.E., Gittis A.G., Botello K., Cruz P., Martin-Martin I.,\nRA   Valenzuela Leon P.C., Sumner B., Bonilla B., Calvo E.;\nRT   \"Structural and functional comparisons of salivary alpha-glucosidases from\nRT   the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex\nRT   quinquefasciatus.\";\nRL   Insect Biochem. Mol. Biol. 167:104097-104097(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:03.279027+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052",
  "url": "https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-\nCC         glucose residues with release of alpha-D-glucose.; EC=3.2.1.20;\nCC         Evidence={ECO:0000269|PubMed:38428508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:03.279027+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052",
  "url": "https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 152. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
