# transmembrane_0067

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0067.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDTAPDHREPQEQGESRKWYEMTASEFYVYVVAFMCGVSMMMPVNAVFSAPAYIMTYYRYAMQDPEAVPLYTNFWNNVMTYYNLIGIVTSLIMEPLTLLSWFRRIPMKVRLLGGLVILIVEIIVLMVVPARGTSEAGAVATICCTGFIGGFGKSIFESTTYGMFGAFPSSFTSTMMGGVGMSGVLTSLLQIIVKAALPDSYEGVKKQSKIYYGLDVGIQGMTFVALILLRFNSFAQNYFGDLGAVKSKVDAGKLSAEALCHTDEHPTHDKEGRNSSSGKEVPALGEVQTAAAKSEGPDAVEESSWPHEVEGPTSNEILVATAIFSTLRRVKWMFVACAFNFLITLFLFPGIAVGMFPDSKWFSTIAVFIFNVFDVLGRFSPSLKLMWPRSYKQRWIIVAASFARVIFVPLLLLHSYHYIPGEAYGYVMEVIFGFSNGYVGSMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRATY

[Multiple Choices]
A. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
B. 70..90; 96..116
C. 27..47; 82..102; 104..127; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
D. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 361..381; 395..415; 427..447; 460..480
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

> The supplied sequence matches the source sequence, and the database annotates the 11 regions listed in A as transmembrane helices. These annotations have computational evidence code ECO:0000255, so they support the key as database annotations but are not independent experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the long hydrophobic stretches expected for a multipass membrane transporter. In particular, the region corresponding to 333..353 lies in a strongly hydrophobic run, supporting A over D, which omits it; B omits most of the evident membrane-spanning regions. Around the 109..129 region, the strongly hydrophobic core follows a basic, less membrane-like stretch, making A's start more plausible than C's earlier start. This is a sequence-based, transferable hydropathy inference, although exact helix boundaries remain predictions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides meaningful evidence for the listed membrane-spanning regions and distinguishes the main alternatives. The inference does not require knowing this protein's recorded annotation, though it cannot establish exact boundaries with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options differ in ways that sequence hydropathy meaningfully addresses: B omits most spans, D omits a strongly hydrophobic region, and C starts its shifted span in a less membrane-like basic region. Boundary uncertainty is a caveat, but does not make these choices equally defensible.


### Important caveats

- The source's transmembrane-region evidence is computational; the supplied evidence does not independently establish each span experimentally.
- Predicted transmembrane boundaries can vary by a few residues.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the long hydrophobic stretches expected for a multipass membrane transporter. In particular, the region corresponding to 333..353 lies in a strongly hydrophobic run, supporting A over D, which omits it; B omits most of the evident membrane-spanning regions. Around the 109..129 region, the strongly hydrophobic core follows a basic, less membrane-like stretch, making A's start more plausible than C's earlier start. This is a sequence-based, transferable hydropathy inference, although exact helix boundaries remain predictions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides meaningful evidence for the listed membrane-spanning regions and distinguishes the main alternatives. The inference does not require knowing this protein's recorded annotation, though it cannot establish exact boundaries with certainty."
  },
  "case_id": "transmembrane_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
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
    "reason": "The supplied sequence matches the source sequence, and the database annotates the 11 regions listed in A as transmembrane helices. These annotations have computational evidence code ECO:0000255, so they support the key as database annotations but are not independent experimental confirmation."
  },
  "important_caveats": [
    "The source's transmembrane-region evidence is computational; the supplied evidence does not independently establish each span experimentally.",
    "Predicted transmembrane boundaries can vary by a few residues."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options differ in ways that sequence hydropathy meaningfully addresses: B omits most spans, D omits a strongly hydrophobic region, and C starts its shifted span in a less membrane-like basic region. Boundary uncertainty is a caveat, but does not make these choices equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence, and the database annotates the 11 regions listed in A as transmembrane helices. These annotations have computational evidence code ECO:0000255, so they support the key as database annotations but are not independent experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the long hydrophobic stretches expected for a multipass membrane transporter. In particular, the region corresponding to 333..353 lies in a strongly hydrophobic run, supporting A over D, which omits it; B omits most of the evident membrane-spanning regions. Around the 109..129 region, the strongly hydrophobic core follows a basic, less membrane-like stretch, making A's start more plausible than C's earlier start. This is a sequence-based, transferable hydropathy inference, although exact helix boundaries remain predictions.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides meaningful evidence for the listed membrane-spanning regions and distinguishes the main alternatives. The inference does not require knowing this protein's recorded annotation, though it cannot establish exact boundaries with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options differ in ways that sequence hydropathy meaningfully addresses: B omits most spans, D omits a strongly hydrophobic region, and C starts its shifted span in a less membrane-like basic region. Boundary uncertainty is a caveat, but does not make these choices equally defensible."
  },
  "important_caveats": [
    "The source's transmembrane-region evidence is computational; the supplied evidence does not independently establish each span experimentally.",
    "Predicted transmembrane boundaries can vary by a few residues."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry O76343 (Nucleoside transporter 1.1, LdNT1.1) annotates exactly 11 transmembrane helices at positions 27-47, 82-102, 109-129, 136-156, 173-193, 209-229, 333-353, 361-381, 395-415, 427-447, and 460-480, matching option A precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins rather than experimental measurements. The annotation is consistent with the expected answer but is not experimentally verified.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence exhibits the hallmarks of a multi-pass membrane transporter with numerous hydrophobic stretches. The equilibrative nucleoside transporter (ENT) family is well-characterized as having 11 transmembrane helices, a topology conserved across ENT1-ENT4 members in humans, Leishmania, and other organisms. This family-level feature immediately eliminates option B (only 2 TM regions, far too few for any multi-pass transporter) and option D (10 TM regions, missing the 333-353 helix, which contains a clear hydrophobic stretch FVAFAFLIFLFPGIAVG). Between options A and C, the only difference is the third TM boundary: A gives 109-129 while C gives 104-127. Inspecting the sequence at positions 104-108 reveals I-P-M-K-V, where Pro(105) is a strong helix breaker and Lys(107) carries a positive charge—both highly unfavorable within a transmembrane alpha-helix. Option C therefore places a proline and a lysine inside the proposed TM helix, whereas option A starts at R(109), placing the charged residue at the helix boundary (consistent with the 'positive-inside' or interfacial positioning common in TM helix annotations). The core hydrophobic segment (~110-127, LLGGLVILIV-EIIVLMVV) is shared by both options, but the inclusion of P and K in option C is a clear sequence-level argument against it. Thus, family topology (11 TMs) plus local hydropathy/sequence-feature analysis meaningfully distinguishes A from the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use ENT-family topology (11 TM helices) to eliminate B and D, and can use local sequence features (Pro and Lys at positions 105-107 being incompatible with a TM helix) to prefer option A over C. These are transferable arguments based on family-level structural knowledge and general principles of membrane protein biophysics, not requiring recall of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B (2 TMs) and D (10 TMs) are clearly incompatible with the multi-pass transporter architecture and the 11-TM ENT family topology. Option C includes a proline and a lysine within the proposed TM3 helix, which is a clear sequence-level disqualifier. Option A is the only choice consistent with both family topology and local hydropathy. While the A-vs-C boundary difference is fine-grained, the unfavorable residues in C provide a concrete basis for discrimination.


### Important caveats

- All UniProt transmembrane annotations for this entry use evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimental measurements (e.g., cryo-EM or cross-linking).
- The reviewer-only evidence identifies the protein as O76343 (LdNT1.1, Leishmania donovani), but this identity was not provided to the evaluated model; the model must rely on sequence features and family-level knowledge.
- The A-vs-C distinction (TM3 starting at 109 vs 104) is a 5-residue shift. While the hydropathy argument favors A, a very different hydropathy window or scoring function could potentially yield C's boundaries, making this a somewhat fine-grained distinction.
- The ENT family 11-TM topology is well-established from structural studies of human ENT1/ENT2, but the exact boundary definitions for individual helices in Leishmania homologs rely on prediction rather than direct structural determination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence exhibits the hallmarks of a multi-pass membrane transporter with numerous hydrophobic stretches. The equilibrative nucleoside transporter (ENT) family is well-characterized as having 11 transmembrane helices, a topology conserved across ENT1-ENT4 members in humans, Leishmania, and other organisms. This family-level feature immediately eliminates option B (only 2 TM regions, far too few for any multi-pass transporter) and option D (10 TM regions, missing the 333-353 helix, which contains a clear hydrophobic stretch FVAFAFLIFLFPGIAVG). Between options A and C, the only difference is the third TM boundary: A gives 109-129 while C gives 104-127. Inspecting the sequence at positions 104-108 reveals I-P-M-K-V, where Pro(105) is a strong helix breaker and Lys(107) carries a positive charge—both highly unfavorable within a transmembrane alpha-helix. Option C therefore places a proline and a lysine inside the proposed TM helix, whereas option A starts at R(109), placing the charged residue at the helix boundary (consistent with the 'positive-inside' or interfacial positioning common in TM helix annotations). The core hydrophobic segment (~110-127, LLGGLVILIV-EIIVLMVV) is shared by both options, but the inclusion of P and K in option C is a clear sequence-level argument against it. Thus, family topology (11 TMs) plus local hydropathy/sequence-feature analysis meaningfully distinguishes A from the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use ENT-family topology (11 TM helices) to eliminate B and D, and can use local sequence features (Pro and Lys at positions 105-107 being incompatible with a TM helix) to prefer option A over C. These are transferable arguments based on family-level structural knowledge and general principles of membrane protein biophysics, not requiring recall of this specific protein's database annotation."
  },
  "case_id": "transmembrane_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry O76343 (Nucleoside transporter 1.1, LdNT1.1) annotates exactly 11 transmembrane helices at positions 27-47, 82-102, 109-129, 136-156, 173-193, 209-229, 333-353, 361-381, 395-415, 427-447, and 460-480, matching option A precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins rather than experimental measurements. The annotation is consistent with the expected answer but is not experimentally verified."
  },
  "important_caveats": [
    "All UniProt transmembrane annotations for this entry use evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimental measurements (e.g., cryo-EM or cross-linking).",
    "The reviewer-only evidence identifies the protein as O76343 (LdNT1.1, Leishmania donovani), but this identity was not provided to the evaluated model; the model must rely on sequence features and family-level knowledge.",
    "The A-vs-C distinction (TM3 starting at 109 vs 104) is a 5-residue shift. While the hydropathy argument favors A, a very different hydropathy window or scoring function could potentially yield C's boundaries, making this a somewhat fine-grained distinction.",
    "The ENT family 11-TM topology is well-established from structural studies of human ENT1/ENT2, but the exact boundary definitions for individual helices in Leishmania homologs rely on prediction rather than direct structural determination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B (2 TMs) and D (10 TMs) are clearly incompatible with the multi-pass transporter architecture and the 11-TM ENT family topology. Option C includes a proline and a lysine within the proposed TM3 helix, which is a clear sequence-level disqualifier. Option A is the only choice consistent with both family topology and local hydropathy. While the A-vs-C boundary difference is fine-grained, the unfavorable residues in C provide a concrete basis for discrimination."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry O76343 (Nucleoside transporter 1.1, LdNT1.1) annotates exactly 11 transmembrane helices at positions 27-47, 82-102, 109-129, 136-156, 173-193, 209-229, 333-353, 361-381, 395-415, 427-447, and 460-480, matching option A precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins rather than experimental measurements. The annotation is consistent with the expected answer but is not experimentally verified.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence exhibits the hallmarks of a multi-pass membrane transporter with numerous hydrophobic stretches. The equilibrative nucleoside transporter (ENT) family is well-characterized as having 11 transmembrane helices, a topology conserved across ENT1-ENT4 members in humans, Leishmania, and other organisms. This family-level feature immediately eliminates option B (only 2 TM regions, far too few for any multi-pass transporter) and option D (10 TM regions, missing the 333-353 helix, which contains a clear hydrophobic stretch FVAFAFLIFLFPGIAVG). Between options A and C, the only difference is the third TM boundary: A gives 109-129 while C gives 104-127. Inspecting the sequence at positions 104-108 reveals I-P-M-K-V, where Pro(105) is a strong helix breaker and Lys(107) carries a positive charge—both highly unfavorable within a transmembrane alpha-helix. Option C therefore places a proline and a lysine inside the proposed TM helix, whereas option A starts at R(109), placing the charged residue at the helix boundary (consistent with the 'positive-inside' or interfacial positioning common in TM helix annotations). The core hydrophobic segment (~110-127, LLGGLVILIV-EIIVLMVV) is shared by both options, but the inclusion of P and K in option C is a clear sequence-level argument against it. Thus, family topology (11 TMs) plus local hydropathy/sequence-feature analysis meaningfully distinguishes A from the other options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use ENT-family topology (11 TM helices) to eliminate B and D, and can use local sequence features (Pro and Lys at positions 105-107 being incompatible with a TM helix) to prefer option A over C. These are transferable arguments based on family-level structural knowledge and general principles of membrane protein biophysics, not requiring recall of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B (2 TMs) and D (10 TMs) are clearly incompatible with the multi-pass transporter architecture and the 11-TM ENT family topology. Option C includes a proline and a lysine within the proposed TM3 helix, which is a clear sequence-level disqualifier. Option A is the only choice consistent with both family topology and local hydropathy. While the A-vs-C boundary difference is fine-grained, the unfavorable residues in C provide a concrete basis for discrimination."
  },
  "important_caveats": [
    "All UniProt transmembrane annotations for this entry use evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimental measurements (e.g., cryo-EM or cross-linking).",
    "The reviewer-only evidence identifies the protein as O76343 (LdNT1.1, Leishmania donovani), but this identity was not provided to the evaluated model; the model must rely on sequence features and family-level knowledge.",
    "The A-vs-C distinction (TM3 starting at 109 vs 104) is a 5-residue shift. While the hydropathy argument favors A, a very different hydropathy window or scoring function could potentially yield C's boundaries, making this a somewhat fine-grained distinction.",
    "The ENT family 11-TM topology is well-established from structural studies of human ENT1/ENT2, but the exact boundary definitions for individual helices in Leishmania homologs rely on prediction rather than direct structural determination."
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
  "benchmark_sequence_length": 491,
  "benchmark_sequence_sha256": "d64970eec213a81b1bb8c504a7b46c7621212ff726e7abba5ac1e9cf9ffc63c5",
  "current_entry_audit": {
    "entryVersion": 72,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1998-11-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 491,
  "current_source_sequence_sha256": "d64970eec213a81b1bb8c504a7b46c7621212ff726e7abba5ac1e9cf9ffc63c5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 70,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O76343",
  "selected_historical_entry_version": 70,
  "selected_historical_record_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "selected_historical_source_sequence_length": 491,
  "selected_historical_source_sequence_sha256": "d64970eec213a81b1bb8c504a7b46c7621212ff726e7abba5ac1e9cf9ffc63c5",
  "selected_historical_version": {
    "accession": "O76343",
    "database": "Swiss-Prot",
    "entryVersion": 70,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NT11_LEIDO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O76343\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":72,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1998-11-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAC32597.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Leishmania\"],\"scientificName\":\"Leishmania donovani\",\"taxonId\":5661}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"12835315\",\"source\":\"PubMed\"}],\"value\":\"Equilibrative nucleoside transporter 1.1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9707568\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 1.1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9707568\",\"source\":\"PubMed\"}],\"value\":\"LdNT1.1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":47},\"start\":{\"modifier\":\"EXACT\",\"value\":27}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":102},\"start\":{\"modifier\":\"EXACT\",\"value\":82}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":129},\"start\":{\"modifier\":\"EXACT\",\"value\":109}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":156},\"start\":{\"modifier\":\"EXACT\",\"value\":136}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":173}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":229},\"start\":{\"modifier\":\"EXACT\",\"value\":209}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":353},\"start\":{\"modifier\":\"EXACT\",\"value\":333}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":381},\"start\":{\"modifier\":\"EXACT\",\"value\":361}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":415},\"start\":{\"modifier\":\"EXACT\",\"value\":395}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":447},\"start\":{\"modifier\":\"EXACT\",\"value\":427}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":480},\"start\":{\"modifier\":\"EXACT\",\"value\":460}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Vasudevan G.\",\"Carter N.S.\",\"Drew M.E.\",\"Beverley S.M.\",\"Sanchez M.A.\",\"Seyfang A.\",\"Ullman B.\",\"Landfear S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9707568\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.95.17.9873\"}],\"citationType\":\"journal article\",\"firstPage\":\"9873\",\"id\":\"9707568\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"9878\",\"publicationDate\":\"1998\",\"title\":\"Cloning of Leishmania nucleoside transporter genes by rescue of a transport-deficient mutant.\",\"volume\":\"95\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAC32597.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAC32597.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"1S\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Stein A.\",\"Vaseduvan G.\",\"Carter N.S.\",\"Ullman B.\",\"Landfear S.M.\",\"Kavanaugh M.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12835315\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m306188200\"}],\"citationType\":\"journal article\",\"firstPage\":\"35127\",\"id\":\"12835315\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"35134\",\"publicationDate\":\"2003\",\"title\":\"Equilibrative nucleoside transporter family members from Leishmania donovani are electrogenic proton symporters.\",\"volume\":\"278\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H1",
  "excerpt": "ID   NT11_LEIDO              Reviewed;         491 AA.\nAC   O76343;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-NOV-1998, sequence version 1.\nDT   28-JAN-2026, entry version 70.\nDE   RecName: Full=Nucleoside transporter 1.1 {ECO:0000303|PubMed:9707568};\nDE            Short=LdNT1.1 {ECO:0000303|PubMed:9707568};\nDE   AltName: Full=Equilibrative nucleoside transporter 1.1 {ECO:0000303|PubMed:12835315};\nGN   Name=NT1.1 {ECO:0000303|PubMed:9707568};\nGN   ORFNames=CGC20_30430 {ECO:0000312|EMBL:TPP53190.1},\nGN   LdCL_150017900 {ECO:0000312|EMBL:AYU77538.1},\nGN   LDHU3_15.1550 {ECO:0000312|EMBL:CAC5428821.1};\nOS   Leishmania donovani.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Leishmania.\nOX   NCBI_TaxID=5661 {ECO:0000312|EMBL:AAC32597.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAC32597.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, TRANSPORTER ACTIVITY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=1S {ECO:0000312|EMBL:AAC32597.1};\nRX   PubMed=9707568; DOI=10.1073/pnas.95.17.9873;\nRA   Vasudevan G., Carter N.S., Drew M.E., Beverley S.M., Sanchez M.A.,\nRA   Seyfang A., Ullman B., Landfear S.M.;\nRT   \"Cloning of Leishmania nucleoside transporter genes by rescue of a\nRT   transport-deficient mutant.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 95:9873-9878(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, AND TRANSPORTER ACTIVITY.\nRX   PubMed=12835315; DOI=10.1074/jbc.m306188200;\nRA   Stein A., Vaseduvan G., Carter N.S., Ullman B., Landfear S.M.,\nRA   Kavanaugh M.P.;\nRT   \"Equilibrative nucleoside transporter family members from Leishmania\nRT   donovani are electrogenic proton symporters.\";\nRL   J. Biol. Chem. 278:35127-35134(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        27..47\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        82..102\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        109..129\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        136..156\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-125",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        173..193\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        209..229\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        333..353\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 132-134",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        361..381\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 135-137",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        395..415\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 138-140",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        427..447\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 141-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        460..480\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-146",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
