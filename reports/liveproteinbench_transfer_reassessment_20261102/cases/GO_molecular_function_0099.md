# GO_molecular_function_0099

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0099.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — dioxygenase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSRVQLALRVPDLEASIGFYSKLFGTGPAKVRPGYANFAIAEPPLKLVLIEGAGEDATRLDHLGVEVEDSAQVGHAARRLKESGLATVEENDTACCYAVQDKVWVTGPGGEPWEVYVVKGDADTLAKADDSACCTPRDSGSAGAAVGADCC

[Multiple Choices]
A. N-acetylglucosamine-6-sulfatase activity
B. dioxygenase activity
C. peptidase inhibitor activity
D. rRNA binding
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record describes this protein as a nonheme iron-dependent dioxygenase, and reports an oxygen-dependent catalytic reaction with experimental evidence. This supports option B, though the database annotation and functional characterization are distinct types of evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 151-residue sequence is compatible with a compact soluble metalloenzyme and contains histidine and acidic residues that could contribute to metal coordination, making a nonheme-metal oxygenase a plausible choice. The alternatives are less consistent: no evident sulfatase catalytic signature, no obvious peptidase-inhibitor character, and no conspicuous RNA-binding signature. This is a probabilistic sequence-based distinction, not proof of the precise reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices are broad and biologically distinct enough that transferable sequence and protein-family patterns can favor dioxygenase activity without knowing this protein’s recorded annotation. The exact organoarsenical substrate specificity would require more information, but is not needed to choose among these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, dioxygenase activity is the best-supported broad molecular function; no second option is comparably defensible.


### Important caveats

- The reviewer-only annotation supports the key but was not part of the original model input.
- The sequence alone does not establish the enzyme’s particular substrate or full catalytic mechanism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 151-residue sequence is compatible with a compact soluble metalloenzyme and contains histidine and acidic residues that could contribute to metal coordination, making a nonheme-metal oxygenase a plausible choice. The alternatives are less consistent: no evident sulfatase catalytic signature, no obvious peptidase-inhibitor character, and no conspicuous RNA-binding signature. This is a probabilistic sequence-based distinction, not proof of the precise reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices are broad and biologically distinct enough that transferable sequence and protein-family patterns can favor dioxygenase activity without knowing this protein’s recorded annotation. The exact organoarsenical substrate specificity would require more information, but is not needed to choose among these alternatives."
  },
  "case_id": "GO_molecular_function_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes this protein as a nonheme iron-dependent dioxygenase, and reports an oxygen-dependent catalytic reaction with experimental evidence. This supports option B, though the database annotation and functional characterization are distinct types of evidence."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not part of the original model input.",
    "The sequence alone does not establish the enzyme’s particular substrate or full catalytic mechanism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, dioxygenase activity is the best-supported broad molecular function; no second option is comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes this protein as a nonheme iron-dependent dioxygenase, and reports an oxygen-dependent catalytic reaction with experimental evidence. This supports option B, though the database annotation and functional characterization are distinct types of evidence.",
    "evidence_ids": ["C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 151-residue sequence is compatible with a compact soluble metalloenzyme and contains histidine and acidic residues that could contribute to metal coordination, making a nonheme-metal oxygenase a plausible choice. The alternatives are less consistent: no evident sulfatase catalytic signature, no obvious peptidase-inhibitor character, and no conspicuous RNA-binding signature. This is a probabilistic sequence-based distinction, not proof of the precise reaction.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices are broad and biologically distinct enough that transferable sequence and protein-family patterns can favor dioxygenase activity without knowing this protein’s recorded annotation. The exact organoarsenical substrate specificity would require more information, but is not needed to choose among these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, dioxygenase activity is the best-supported broad molecular function; no second option is comparably defensible."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not part of the original model input.",
    "The sequence alone does not establish the enzyme’s particular substrate or full catalytic mechanism."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (D1A230, ArsI from Thermomonospora curvata) is explicitly annotated as a 'Nonheme iron-dependent dioxygenase' (H5, C5) with EC 1.13.11.- (dioxygenase class). The GO annotation GO:0051213 (dioxygenase activity) is directly assigned (H10). Catalytic activity reactions (C6–C9) all show O2 incorporation into substrate. The functional annotation is backed by experimental evidence (ECO:0000269, PubMed:27107642 and 35487149) including X-ray crystallography of Fe(II)-bound complexes. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO4](#evidence-go4), [H5](#evidence-h5), [H6](#evidence-h6), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish the answer through a combination of elimination and positive sequence features. (1) Option A (N-acetylglucosamine-6-sulfatase) requires the canonical C-X-P-X-R sulfatase catalytic motif and typically a 400–600 aa protein; the 151-aa sequence lacks this motif and is far too short, strongly eliminating A. (2) Option D (rRNA binding) proteins characteristically contain arginine-rich patches, KOW domains, or specific RNA-recognition motifs; the sequence has no such features, eliminating D. (3) Option C (peptidase inhibitor activity) proteins typically possess a reactive-site loop (serpins, cystatins with QxxVxGxExV) or a small disulfide-stabilized inhibitor fold; the sequence lacks these hallmarks. (4) Positive evidence for B: the region 'DHLGVEVEDSAQVGHAARR' contains His-Asp/Glu-Glu-His residues in spacing consistent with a variant Fe(II) facial triad (HxD/E...H), a hallmark shared with the large family of non-heme Fe(II)/2-oxoglutarate dioxygenases learned from other proteins (TauD, AlkB, prolyl hydroxylases). Combined with the elimination of A, C, and D, the metalloenzyme catalytic signature points to dioxygenase activity. In a 4-choice MCQ, eliminating three clearly mismatched options and identifying metal-coordinating residues consistent with the dioxygenase superfamily provides a defensible inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of options A and D is robust based on well-known family-level sequence signatures (sulfatase CXPXR motif, RNA-binding arginine-rich/KOW features) transferable from other proteins. The distinction between B and C is supported by the presence of a putative Fe-coordinating HxD/E...H triad pattern, which is a conserved feature across the broad dioxygenase superfamily learned from many other proteins. While the positive identification of 'dioxygenase' from a 151-aa sequence is not trivial, the combination of elimination and the metal-binding signature provides a credible, non-memorization-based pathway to answer B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are clearly eliminated by the absence of their defining sequence motifs and by size/fold mismatch. Option C is inconsistent with the metal-binding catalytic residues present. Only B remains as a defensible choice given the sequence features and the four offered alternatives.


### Important caveats

- The ArsI protein is a relatively unusual and small (151 aa) dioxygenase; its Fe-coordination geometry differs from the canonical HxD/E...H facial triad spacing seen in classic 2OG dioxygenases, making the positive identification somewhat less straightforward than for a typical TauD/AlkB-family member.
- The GO annotation in UniProt carries an IEA (Inferred from Electronic Annotation) evidence code via UniProtKB keyword, though the underlying functional characterization is experimentally supported (ECO:0000269).
- The protein's unusual cysteine-rich C-terminal region could superficially resemble small disulfide-bonded inhibitor proteins (option C), but the overall sequence context and metal-binding residues argue against this interpretation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish the answer through a combination of elimination and positive sequence features. (1) Option A (N-acetylglucosamine-6-sulfatase) requires the canonical C-X-P-X-R sulfatase catalytic motif and typically a 400–600 aa protein; the 151-aa sequence lacks this motif and is far too short, strongly eliminating A. (2) Option D (rRNA binding) proteins characteristically contain arginine-rich patches, KOW domains, or specific RNA-recognition motifs; the sequence has no such features, eliminating D. (3) Option C (peptidase inhibitor activity) proteins typically possess a reactive-site loop (serpins, cystatins with QxxVxGxExV) or a small disulfide-stabilized inhibitor fold; the sequence lacks these hallmarks. (4) Positive evidence for B: the region 'DHLGVEVEDSAQVGHAARR' contains His-Asp/Glu-Glu-His residues in spacing consistent with a variant Fe(II) facial triad (HxD/E...H), a hallmark shared with the large family of non-heme Fe(II)/2-oxoglutarate dioxygenases learned from other proteins (TauD, AlkB, prolyl hydroxylases). Combined with the elimination of A, C, and D, the metalloenzyme catalytic signature points to dioxygenase activity. In a 4-choice MCQ, eliminating three clearly mismatched options and identifying metal-coordinating residues consistent with the dioxygenase superfamily provides a defensible inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of options A and D is robust based on well-known family-level sequence signatures (sulfatase CXPXR motif, RNA-binding arginine-rich/KOW features) transferable from other proteins. The distinction between B and C is supported by the presence of a putative Fe-coordinating HxD/E...H triad pattern, which is a conserved feature across the broad dioxygenase superfamily learned from many other proteins. While the positive identification of 'dioxygenase' from a 151-aa sequence is not trivial, the combination of elimination and the metal-binding signature provides a credible, non-memorization-based pathway to answer B."
  },
  "case_id": "GO_molecular_function_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "GO4",
      "H5",
      "H6",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (D1A230, ArsI from Thermomonospora curvata) is explicitly annotated as a 'Nonheme iron-dependent dioxygenase' (H5, C5) with EC 1.13.11.- (dioxygenase class). The GO annotation GO:0051213 (dioxygenase activity) is directly assigned (H10). Catalytic activity reactions (C6–C9) all show O2 incorporation into substrate. The functional annotation is backed by experimental evidence (ECO:0000269, PubMed:27107642 and 35487149) including X-ray crystallography of Fe(II)-bound complexes. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The ArsI protein is a relatively unusual and small (151 aa) dioxygenase; its Fe-coordination geometry differs from the canonical HxD/E...H facial triad spacing seen in classic 2OG dioxygenases, making the positive identification somewhat less straightforward than for a typical TauD/AlkB-family member.",
    "The GO annotation in UniProt carries an IEA (Inferred from Electronic Annotation) evidence code via UniProtKB keyword, though the underlying functional characterization is experimentally supported (ECO:0000269).",
    "The protein's unusual cysteine-rich C-terminal region could superficially resemble small disulfide-bonded inhibitor proteins (option C), but the overall sequence context and metal-binding residues argue against this interpretation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are clearly eliminated by the absence of their defining sequence motifs and by size/fold mismatch. Option C is inconsistent with the metal-binding catalytic residues present. Only B remains as a defensible choice given the sequence features and the four offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (D1A230, ArsI from Thermomonospora curvata) is explicitly annotated as a 'Nonheme iron-dependent dioxygenase' (H5, C5) with EC 1.13.11.- (dioxygenase class). The GO annotation GO:0051213 (dioxygenase activity) is directly assigned (H10). Catalytic activity reactions (C6–C9) all show O2 incorporation into substrate. The functional annotation is backed by experimental evidence (ECO:0000269, PubMed:27107642 and 35487149) including X-ray crystallography of Fe(II)-bound complexes. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "C6", "GO4", "H5", "H6", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish the answer through a combination of elimination and positive sequence features. (1) Option A (N-acetylglucosamine-6-sulfatase) requires the canonical C-X-P-X-R sulfatase catalytic motif and typically a 400–600 aa protein; the 151-aa sequence lacks this motif and is far too short, strongly eliminating A. (2) Option D (rRNA binding) proteins characteristically contain arginine-rich patches, KOW domains, or specific RNA-recognition motifs; the sequence has no such features, eliminating D. (3) Option C (peptidase inhibitor activity) proteins typically possess a reactive-site loop (serpins, cystatins with QxxVxGxExV) or a small disulfide-stabilized inhibitor fold; the sequence lacks these hallmarks. (4) Positive evidence for B: the region 'DHLGVEVEDSAQVGHAARR' contains His-Asp/Glu-Glu-His residues in spacing consistent with a variant Fe(II) facial triad (HxD/E...H), a hallmark shared with the large family of non-heme Fe(II)/2-oxoglutarate dioxygenases learned from other proteins (TauD, AlkB, prolyl hydroxylases). Combined with the elimination of A, C, and D, the metalloenzyme catalytic signature points to dioxygenase activity. In a 4-choice MCQ, eliminating three clearly mismatched options and identifying metal-coordinating residues consistent with the dioxygenase superfamily provides a defensible inference.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of options A and D is robust based on well-known family-level sequence signatures (sulfatase CXPXR motif, RNA-binding arginine-rich/KOW features) transferable from other proteins. The distinction between B and C is supported by the presence of a putative Fe-coordinating HxD/E...H triad pattern, which is a conserved feature across the broad dioxygenase superfamily learned from many other proteins. While the positive identification of 'dioxygenase' from a 151-aa sequence is not trivial, the combination of elimination and the metal-binding signature provides a credible, non-memorization-based pathway to answer B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are clearly eliminated by the absence of their defining sequence motifs and by size/fold mismatch. Option C is inconsistent with the metal-binding catalytic residues present. Only B remains as a defensible choice given the sequence features and the four offered alternatives."
  },
  "important_caveats": [
    "The ArsI protein is a relatively unusual and small (151 aa) dioxygenase; its Fe-coordination geometry differs from the canonical HxD/E...H facial triad spacing seen in classic 2OG dioxygenases, making the positive identification somewhat less straightforward than for a typical TauD/AlkB-family member.",
    "The GO annotation in UniProt carries an IEA (Inferred from Electronic Annotation) evidence code via UniProtKB keyword, though the underlying functional characterization is experimentally supported (ECO:0000269).",
    "The protein's unusual cysteine-rich C-terminal region could superficially resemble small disulfide-bonded inhibitor proteins (option C), but the overall sequence context and metal-binding residues argue against this interpretation."
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
  "benchmark_sequence_length": 151,
  "benchmark_sequence_sha256": "96f901d3406d3fc76b1b13d6687ce5e7fc465abc1cc4f694dd78fac7c7851ba3",
  "current_entry_audit": {
    "entryVersion": 78,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-01-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 151,
  "current_source_sequence_sha256": "96f901d3406d3fc76b1b13d6687ce5e7fc465abc1cc4f694dd78fac7c7851ba3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 77,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D1A230",
  "selected_historical_entry_version": 77,
  "selected_historical_record_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "selected_historical_source_sequence_length": 151,
  "selected_historical_source_sequence_sha256": "96f901d3406d3fc76b1b13d6687ce5e7fc465abc1cc4f694dd78fac7c7851ba3",
  "selected_historical_version": {
    "accession": "D1A230",
    "database": "Swiss-Prot",
    "entryVersion": 77,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "ARSI_THECD",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D1A230\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":78,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-01-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Streptosporangiales\",\"Thermomonosporaceae\",\"Thermomonospora\"],\"scientificName\":\"Thermomonospora curvata (strain ATCC 19995 / DSM 43183 / JCM 3096 / KCTC 9072 / NBRC 15933 / NCIMB 10081 / Henssen B9)\",\"taxonId\":471852}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24915088\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27107642\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35487149\",\"source\":\"PubMed\"}],\"value\":\"C-As lyase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"27107642\",\"source\":\"PubMed\"}],\"value\":\"Methylarsonous acid demethylase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"27107642\",\"source\":\"PubMed\"}],\"value\":\"MAs(III) demethylase\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27107642\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35487149\",\"source\":\"PubMed\"}],\"value\":\"1.13.11.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Trivalent organoarsenical cleaving enzyme\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A059WI14\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27107642\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35487149\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"27107642\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"35487149\",\"source\":\"PubMed\"}],\"value\":\"Nonheme iron-dependent dioxygenase that can break carbon-arsenic bonds, playing a role in the detoxification of environmental organoarsenical compounds. Catalyzes the oxygen-dependent demethylation of highly toxic methylarsonous acid (MAs(III)) to arsenite, which can then be exported out of the cell (PubMed:27107642, PubMed:35487149). Can also cleave the C-As bond in several trivalent aromatic arsenicals, including roxarsone (III), nitarsone (III) and (4-aminophenyl)arsonous acid (By similarity). Organoarsenical degradation by this enzyme is proposed to have a significant impact on the arsenic biogeocycle that maintains a balance between organic and inorganic species (Probable)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"27107642\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"35487149\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82324\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27107642\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35487149\",\"source\":\"PubMed\"}],\"name\":\"methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82323\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17790\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17826\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29242\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A059WI14\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82364\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A059WI14\",\"source\":\"UniProtKB\"}],\"name\":\"roxarsone (III) + AH2 + O2 = 4-hydroxy-3-nitrocyclohexa-2,5-dien-1-one + arsenite + A + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82363\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29242\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231974\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231975\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A059WI14\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82440\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A059WI14\",\"source\":\"UniProtKB\"}],\"name\":\"nitarsone (III) + AH2 + O2 = 4-nitrocyclohexa-2,5-dien-1-one + arsenite + A + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82439\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29242\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232329\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232330\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A059WI14\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82444\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A059WI14\",\"source\":\"UniProtKB\"}],\"name\":\"4-aminophenylarsonous acid + AH2 + O2 = 4-aminocyclohexa-2,5-dien-1-one + arsenite + A\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82443\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29242\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:50022\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232331\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Nadar S.V.\",\"Yoshinaga M.\",\"Kandavelu P.\",\"Sankaran B.\",\"Rosen B.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24915088\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2053230x14008814\"}],\"citationType\":\"journal article\",\"firstPage\":\"761\",\"id\":\"24915088\",\"journal\":\"Acta Crystallogr. F Struct. Biol. Commun.\",\"lastPage\":\"764\",\"publicationDate\":\"2014\",\"title\":\"Crystallization and preliminary X-ray crystallographic studies of the ArsI C-As lyase from Thermomonospora curvata.\",\"volume\":\"70\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 19995 / DSM 43183 / JCM 3096 / KCTC 9072 / NBRC 15933 / NCIMB 10081 / Henssen B9\"}],\"referenceNumber\":2,\"referencePositions\":[\"CRYSTALLIZATION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Nadar V.S.\",\"Yoshinaga M.\",\"Pawitwar S.S.\",\"Kandavelu P.\",\"Sankaran B.\",\"Rosen B.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27107642\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jmb.2016.04.022\"}],\"citationType\":\"journal article\",\"firstPage\":\"2462\",\"id\":\"27107642\",\"journal\":\"J. Mol. Biol.\",\"lastPage\":\"2473\",\"publicationDate\":\"2016\",\"title\":\"Structure of the ArsI C-As Lyase: Insights into the Mechanism of Degradation of Organoarsenical Herbicides and Growth Promoters.\",\"volume\":\"428\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5C4P\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5C68\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5C6X\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5CB9\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5D4F\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5DFG\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5DRH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5HCW\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 19995 / DSM 43183 / JCM 3096 / KCTC 9072 / NBRC 15933 / NCIMB 10081 / Henssen B9\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.46 ANGSTROMS) OF 1-123 OF WILD TYPE AND MUTANT HIS-97/PHE-99 IN COMPLEXES WITH FE(3+); NI(2+) AND CO(2+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Nadar V.S.\",\"Kandavelu P.\",\"Sankaran B.\",\"Rosen B.P.\",\"Yoshinaga M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35487149\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jinorgbio.2022.111836\"}],\"citationType\":\"journal article\",\"firstPage\":\"111836\",\"id\":\"35487149\",\"journal\":\"J. Inorg. Biochem.\",\"lastPage\":\"111836\",\"publicationDate\":\"2022\",\"title\":\"The ArsI C-As lyase: Elucidating the catalytic mechanism of degradation of organoarsenicals.\",\"volume\":\"232\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5V0F\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6XA0\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6XCK\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 19995 / DSM 43183 / JCM 3096 / KCTC 9072 / NBRC 15933 / NCIMB 10081 / Henssen B9\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.15 ANGSTROMS) OF 1-123 OF MUTANT ALA-102 IN COMPLEX WITH SUBSTRATE ROXARSONE (III) AND FE(2+); MUTANT ARG-102 IN COMPLEX WITH NI(2+) AND MUTANT GLU-102\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"REACTION MECHANISM\",\"MUTAGENESIS OF TYR-35; GLN-100 AND LYS-102\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:27:37.960057+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8dad989ed29fb7ada17e387219e7b659eae84dce16c4879193b7897bab3a769",
  "url": "https://rest.uniprot.org/uniprotkb/D1A230.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H1",
  "excerpt": "ID   ARSI_THECD              Reviewed;         151 AA.\nAC   D1A230;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-JAN-2010, sequence version 1.\nDT   28-JAN-2026, entry version 77.\nDE   RecName: Full=Trivalent organoarsenical cleaving enzyme {ECO:0000305};\nDE            EC=1.13.11.- {ECO:0000269|PubMed:27107642, ECO:0000269|PubMed:35487149};\nDE   AltName: Full=C-As lyase {ECO:0000303|PubMed:24915088, ECO:0000303|PubMed:27107642, ECO:0000303|PubMed:35487149};\nDE   AltName: Full=Methylarsonous acid demethylase {ECO:0000305|PubMed:27107642};\nDE            Short=MAs(III) demethylase {ECO:0000305|PubMed:27107642};\nGN   Name=arsI {ECO:0000303|PubMed:24915088};\nGN   OrderedLocusNames=Tcur_4156 {ECO:0000312|EMBL:ACY99683.1};\nOS   Thermomonospora curvata (strain ATCC 19995 / DSM 43183 / JCM 3096 / KCTC\nOS   9072 / NBRC 15933 / NCIMB 10081 / Henssen B9).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Streptosporangiales;\nOC   Thermomonosporaceae; Thermomonospora.\nOX   NCBI_TaxID=471852;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   CRYSTALLIZATION, AND SUBUNIT.\nRC   STRAIN=ATCC 19995 / DSM 43183 / JCM 3096 / KCTC 9072 / NBRC 15933 / NCIMB\nRC   10081 / Henssen B9;\nRX   PubMed=24915088; DOI=10.1107/s2053230x14008814;\nRA   Nadar S.V., Yoshinaga M., Kandavelu P., Sankaran B., Rosen B.P.;\nRT   \"Crystallization and preliminary X-ray crystallographic studies of the ArsI\nRT   C-As lyase from Thermomonospora curvata.\";\nRL   Acta Crystallogr. F Struct. Biol. Commun. 70:761-764(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:5C4P, ECO:0007744|PDB:5C68, ECO:0007744|PDB:5C6X, ECO:0007744|PDB:5CB9, ECO:0007744|PDB:5D4F, ECO:0007744|PDB:5DFG, ECO:0007744|PDB:5DRH, ECO:0007744|PDB:5HCW}\nRP   X-RAY CRYSTALLOGRAPHY (1.46 ANGSTROMS) OF 1-123 OF WILD TYPE AND MUTANT\nRP   HIS-97/PHE-99 IN COMPLEXES WITH FE(3+); NI(2+) AND CO(2+), FUNCTION,\nRP   CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=ATCC 19995 / DSM 43183 / JCM 3096 / KCTC 9072 / NBRC 15933 / NCIMB\nRC   10081 / Henssen B9;\nRX   PubMed=27107642; DOI=10.1016/j.jmb.2016.04.022;\nRA   Nadar V.S., Yoshinaga M., Pawitwar S.S., Kandavelu P., Sankaran B.,\nRA   Rosen B.P.;\nRT   \"Structure of the ArsI C-As Lyase: Insights into the Mechanism of\nRT   Degradation of Organoarsenical Herbicides and Growth Promoters.\";\nRL   J. Mol. Biol. 428:2462-2473(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:5V0F, ECO:0007744|PDB:6XA0, ECO:0007744|PDB:6XCK}\nRP   X-RAY CRYSTALLOGRAPHY (2.15 ANGSTROMS) OF 1-123 OF MUTANT ALA-102 IN\nRP   COMPLEX WITH SUBSTRATE ROXARSONE (III) AND FE(2+); MUTANT ARG-102 IN\nRP   COMPLEX WITH NI(2+) AND MUTANT GLU-102, FUNCTION, CATALYTIC ACTIVITY,\nRP   COFACTOR, REACTION MECHANISM, AND MUTAGENESIS OF TYR-35; GLN-100 AND\nRP   LYS-102.\nRC   STRAIN=ATCC 19995 / DSM 43183 / JCM 3096 / KCTC 9072 / NBRC 15933 / NCIMB\nRC   10081 / Henssen B9;\nRX   PubMed=35487149; DOI=10.1016/j.jinorgbio.2022.111836;\nRA   Nadar V.S., Kandavelu P., Sankaran B., Rosen B.P., Yoshinaga M.;\nRT   \"The ArsI C-As lyase: Elucidating the catalytic mechanism of degradation of\nRT   organoarsenicals.\";\nRL   J. Inorg. Biochem. 232:111836-111836(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H5",
  "excerpt": "CC   -!- FUNCTION: Nonheme iron-dependent dioxygenase that can break carbon-\nCC       arsenic bonds, playing a role in the detoxification of environmental\nCC       organoarsenical compounds. Catalyzes the oxygen-dependent demethylation\nCC       of highly toxic methylarsonous acid (MAs(III)) to arsenite, which can\nCC       then be exported out of the cell (PubMed:27107642, PubMed:35487149).\nCC       Can also cleave the C-As bond in several trivalent aromatic arsenicals,\nCC       including roxarsone (III), nitarsone (III) and (4-aminophenyl)arsonous\nCC       acid (By similarity). Organoarsenical degradation by this enzyme is\nCC       proposed to have a significant impact on the arsenic biogeocycle that\nCC       maintains a balance between organic and inorganic species (Probable).\nCC       {ECO:0000250|UniProtKB:A0A059WI14, ECO:0000269|PubMed:27107642,\nCC       ECO:0000269|PubMed:35487149, ECO:0000305|PubMed:27107642,\nCC       ECO:0000305|PubMed:35487149}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=methylarsonous acid + AH2 + O2 = arsenite + methanol + A +\nCC         H(+); Xref=Rhea:RHEA:82323, ChEBI:CHEBI:13193, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:17499, ChEBI:CHEBI:17790,\nCC         ChEBI:CHEBI:17826, ChEBI:CHEBI:29242;\nCC         Evidence={ECO:0000269|PubMed:27107642, ECO:0000269|PubMed:35487149};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82324;\nCC         Evidence={ECO:0000305|PubMed:27107642, ECO:0000305|PubMed:35487149};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=roxarsone (III) + AH2 + O2 = 4-hydroxy-3-nitrocyclohexa-2,5-\nCC         dien-1-one + arsenite + A + H(+); Xref=Rhea:RHEA:82363,\nCC         ChEBI:CHEBI:13193, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:17499, ChEBI:CHEBI:29242, ChEBI:CHEBI:231974,\nCC         ChEBI:CHEBI:231975; Evidence={ECO:0000250|UniProtKB:A0A059WI14};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82364;\nCC         Evidence={ECO:0000250|UniProtKB:A0A059WI14};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=nitarsone (III) + AH2 + O2 = 4-nitrocyclohexa-2,5-dien-1-one +\nCC         arsenite + A + H(+); Xref=Rhea:RHEA:82439, ChEBI:CHEBI:13193,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:17499,\nCC         ChEBI:CHEBI:29242, ChEBI:CHEBI:232329, ChEBI:CHEBI:232330;\nCC         Evidence={ECO:0000250|UniProtKB:A0A059WI14};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82440;\nCC         Evidence={ECO:0000250|UniProtKB:A0A059WI14};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-aminophenylarsonous acid + AH2 + O2 = 4-aminocyclohexa-2,5-\nCC         dien-1-one + arsenite + A; Xref=Rhea:RHEA:82443, ChEBI:CHEBI:13193,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:17499, ChEBI:CHEBI:29242,\nCC         ChEBI:CHEBI:50022, ChEBI:CHEBI:232331;\nCC         Evidence={ECO:0000250|UniProtKB:A0A059WI14};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82444;\nCC         Evidence={ECO:0000250|UniProtKB:A0A059WI14};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0051213; F:dioxygenase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H11",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-163",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0008449\nname: N-acetylglucosamine-6-sulfatase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of the 6-sulfate group of the N-acetyl-D-glucosamine 6-sulfate units of heparan sulfate and keratan sulfate.\" [EC:3.1.6.14]\nsynonym: \"2-acetamido-2-deoxy-D-glucose 6-sulfate sulfatase activity\" RELATED [EC:3.1.6.14]\nsynonym: \"acetylglucosamine 6-sulfatase activity\" RELATED [EC:3.1.6.14]\nsynonym: \"chondroitinsulfatase\" BROAD [EC:3.1.6.14]\nsynonym: \"glucosamine-6-sulfatase activity\" RELATED [EC:3.1.6.14]\nsynonym: \"N-acetyl-D-glucosamine-6-sulfate 6-sulfohydrolase activity\" RELATED [EC:3.1.6.14]\nsynonym: \"N-acetylglucosamine 6-sulfate sulfatase activity\" RELATED [EC:3.1.6.14]\nsynonym: \"N-acetylglucosamine-6-sulphatase activity\" EXACT []\nsynonym: \"O,N-disulfate O-sulfohydrolase activity\" RELATED [EC:3.1.6.14]\nxref: EC:3.1.6.14\nxref: MetaCyc:3.1.6.14-RXN\nxref: Reactome:R-HSA-1638032 \"GNS:Ca2+ cleaves sulfate from GlcNAc-6-sulfate units of keratan sulfate\"\nxref: Reactome:R-HSA-2263495 \"Defective GNS does not hydrolyse 6-sulfate from GlcNAc6S\"\nis_a: GO:0008484 ! sulfuric ester hydrolase activity\nproperty_value: skos:exactMatch EC:3.1.6.14\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008449",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 83469-83488",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0019843\nname: rRNA binding\nnamespace: molecular_function\nalt_id: GO:0000944\ndef: \"Binding to a ribosomal RNA.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_yeast\nsynonym: \"base pairing with rRNA\" NARROW []\nis_a: GO:0003723 ! RNA binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019843",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 153826-153836",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0030414\nname: peptidase inhibitor activity\nnamespace: molecular_function\ndef: \"Binds to and stops, prevents or reduces the activity of a peptidase, any enzyme that catalyzes the hydrolysis peptide bonds.\" [GOC:jl]\nsynonym: \"protease inhibitor activity\" NARROW [GOC:mah]\nis_a: GO:0004857 ! enzyme inhibitor activity\nis_a: GO:0061134 ! peptidase regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030414",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 165960-165968",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0051213\nname: dioxygenase activity\nnamespace: molecular_function\ndef: \"Catalysis of the incorporation of both atoms of molecular oxygen (O2) into the substrate.\" [PMID:1444267]\nsubset: goslim_pir\nxref: Reactome:R-HSA-112120 \"Oxidative demethylation of 3-meC damaged DNA by ALKBH2\"\nxref: Reactome:R-HSA-112121 \"Oxidative dealkylation of 1-etA damaged DNA By ALKBH2\"\nxref: Reactome:R-HSA-112124 \"Oxidative demethylation of 3-meC damaged DNA By ALKBH3\"\nxref: Reactome:R-HSA-112125 \"Oxidative dealkylation of 1-EtA damaged DNA by ABH3\"\nis_a: GO:0016491 ! oxidoreductase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051213",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 324234-324245",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
