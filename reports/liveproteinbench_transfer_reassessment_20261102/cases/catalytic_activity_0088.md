# catalytic_activity_0088

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0088.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSQPEFTRSIVGASFLLPVINGAMHIPPAVSATRVTLEDNQPRDAPILVLLFALSVLIDVMDKAADLPRQTRKTWLMTIVVFASPFVVLAVYGTMHCGLLALLRLLGVPLLAVVHAMPLIPVYSWKTGSISTVKLKYFLGPFKSLFGATCIGLMDVTAVVLYLRGTMLHPENASSAGHFRVLMYTITYDFLWESICDVRDIQEDEQNNITTLATAFGVRPTLIFLGGSTMMGDLSITLLGGGSAVLSVVRSTVFWGAFAALALHKPRSAVYPWGLATLFGLLPVWLASLGART

[Multiple Choices]
A. 2 5'-deoxyadenosin-5'-yl radical + 2 dAMP + A = 2 4'-phospho-dehydrooxetanocin + 2 5'-deoxyadenosine + AH2
B. (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate
C. peramine + 2-oxoglutarate + O2 = 8-hydroxyperamine + succinate + CO2
D. a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
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

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The matched-sequence UniProt annotation assigns this catalytic reaction to the protein and cites experimental evidence (ECO:0000269, PubMed 39310987). This supports B, though the supplied excerpts do not independently detail or validate the underlying experiments.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is unusually hydrophobic and appears strongly membrane-associated, with no evident radical-SAM CxxxCxxC motif, canonical P450 heme-binding cysteine motif, or characteristic 2-oxoglutarate-dioxygenase HxD/E motif. Among the choices, B is the prenylation reaction and is the most plausible fit for a membrane-associated prenyltransferase; the other choices imply distinct radical, dioxygenase, or P450 chemistry. This is a family-level, probabilistic distinction, not a way to infer the exact substrates from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable enzyme-family and sequence-pattern knowledge provides a meaningful basis to favor B over these alternatives. It does not establish every detail of B's specific reaction, but the choices do not require distinguishing among other prenyltransferase reactions.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is meaningfully better supported by the sequence context and enzyme-class distinction than the other listed reaction types.


### Important caveats

- The reviewer-only database annotation and organism identity were not original model inputs and are not used as the basis for the transferability judgment.
- The sequence-based argument favors a reaction class; it does not independently prove the precise substrates or products.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is unusually hydrophobic and appears strongly membrane-associated, with no evident radical-SAM CxxxCxxC motif, canonical P450 heme-binding cysteine motif, or characteristic 2-oxoglutarate-dioxygenase HxD/E motif. Among the choices, B is the prenylation reaction and is the most plausible fit for a membrane-associated prenyltransferase; the other choices imply distinct radical, dioxygenase, or P450 chemistry. This is a family-level, probabilistic distinction, not a way to infer the exact substrates from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable enzyme-family and sequence-pattern knowledge provides a meaningful basis to favor B over these alternatives. It does not establish every detail of B's specific reaction, but the choices do not require distinguishing among other prenyltransferase reactions."
  },
  "case_id": "catalytic_activity_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns this catalytic reaction to the protein and cites experimental evidence (ECO:0000269, PubMed 39310987). This supports B, though the supplied excerpts do not independently detail or validate the underlying experiments."
  },
  "important_caveats": [
    "The reviewer-only database annotation and organism identity were not original model inputs and are not used as the basis for the transferability judgment.",
    "The sequence-based argument favors a reaction class; it does not independently prove the precise substrates or products."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is meaningfully better supported by the sequence context and enzyme-class distinction than the other listed reaction types."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns this catalytic reaction to the protein and cites experimental evidence (ECO:0000269, PubMed 39310987). This supports B, though the supplied excerpts do not independently detail or validate the underlying experiments.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is unusually hydrophobic and appears strongly membrane-associated, with no evident radical-SAM CxxxCxxC motif, canonical P450 heme-binding cysteine motif, or characteristic 2-oxoglutarate-dioxygenase HxD/E motif. Among the choices, B is the prenylation reaction and is the most plausible fit for a membrane-associated prenyltransferase; the other choices imply distinct radical, dioxygenase, or P450 chemistry. This is a family-level, probabilistic distinction, not a way to infer the exact substrates from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "Transferable enzyme-family and sequence-pattern knowledge provides a meaningful basis to favor B over these alternatives. It does not establish every detail of B's specific reaction, but the choices do not require distinguishing among other prenyltransferase reactions."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is meaningfully better supported by the sequence context and enzyme-class distinction than the other listed reaction types."
  },
  "important_caveats": [
    "The reviewer-only database annotation and organism identity were not original model inputs and are not used as the basis for the transferability judgment.",
    "The sequence-based argument favors a reaction class; it does not independently prove the precise substrates or products."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A6A6H402 (sequence matched) annotates this protein as Prenyltransferase vviA (EC 2.5.1.-) with the exact catalytic reaction: (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate. The annotation carries ECO:0000269 (direct assay evidence) from PubMed:39310987 (Tang & Zou, Org. Lett. 2024), indicating experimental characterization. The expected answer B matches the annotated reaction verbatim.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 293-aa sequence is overwhelmingly hydrophobic with multiple predicted transmembrane helices (e.g., VLLFALSVLIDV, WLMTIVVFASPFVVLAV, CIGLMDVTAVVLYLRG, VFWGAFAALAL) and contains GGxxxG motifs typical of membrane protein helix packing. Critically, it lacks: (1) the CxxxCxxC radical SAM cluster needed for option A; (2) the HxD…H facial triad of Fe(II)/2OG dioxygenases needed for option C; (3) the FxxGxxxCxG heme-ligating motif of cytochrome P450s needed for option D. The membrane-bound topology with D residues in loop regions (DLSITLL, DVRDIQEDEQ) is consistent with membrane-bound prenyltransferases (a well-known family in fungal secondary metabolism, e.g., indole prenyltransferases). Option B is the only prenyltransferase reaction (prenyl-diphosphate + acceptor → product + diphosphate), matching the enzyme class identifiable from topology and motif absence. A model recognizing membrane-prenyltransferase architecture and ruling out radical-SAM, 2OG-dioxygenase, and P450 chemistries by motif absence can select B without knowing the specific substrates.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The protein's strongly hydrophobic, multi-TM topology combined with the absence of signature motifs for the three distractor enzyme classes (radical SAM, 2OG dioxygenase, P450) provides a concrete, transferable argument for identifying the enzyme as a membrane-bound prenyltransferase. Among the four offered reactions, only B is a prenyltransferase (diphosphate-transfer) reaction. This reasoning relies on general protein-family knowledge (membrane prenyltransferase architecture, P450 heme motif, radical SAM Cys cluster, 2OG facial triad) rather than a fact specific to this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor requires a distinct catalytic machinery (radical SAM cluster, 2OG/Fe(II) triad, P450 heme) whose signature motifs are absent from the sequence. The membrane-prenyltransferase topology uniquely selects option B among the four alternatives.


### Important caveats

- The specific substrates (drim-8-en-11-yl diphosphate, D-mannitol, sporulositol A) are unusual and not derivable from sequence alone; however, the question only requires identifying the reaction type (prenyltransferase), which is distinguishable by topology and motif absence.
- The annotation is from a 2024 experimental study (PubMed:39310987); the protein was only integrated into Swiss-Prot in April 2025, so this is relatively recent knowledge.
- Membrane-bound prenyltransferases can have diverse substrate specificities; the reasoning identifies the enzyme class but not the exact substrates. The question design compensates by making only one option a prenyltransferase reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 293-aa sequence is overwhelmingly hydrophobic with multiple predicted transmembrane helices (e.g., VLLFALSVLIDV, WLMTIVVFASPFVVLAV, CIGLMDVTAVVLYLRG, VFWGAFAALAL) and contains GGxxxG motifs typical of membrane protein helix packing. Critically, it lacks: (1) the CxxxCxxC radical SAM cluster needed for option A; (2) the HxD…H facial triad of Fe(II)/2OG dioxygenases needed for option C; (3) the FxxGxxxCxG heme-ligating motif of cytochrome P450s needed for option D. The membrane-bound topology with D residues in loop regions (DLSITLL, DVRDIQEDEQ) is consistent with membrane-bound prenyltransferases (a well-known family in fungal secondary metabolism, e.g., indole prenyltransferases). Option B is the only prenyltransferase reaction (prenyl-diphosphate + acceptor → product + diphosphate), matching the enzyme class identifiable from topology and motif absence. A model recognizing membrane-prenyltransferase architecture and ruling out radical-SAM, 2OG-dioxygenase, and P450 chemistries by motif absence can select B without knowing the specific substrates.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The protein's strongly hydrophobic, multi-TM topology combined with the absence of signature motifs for the three distractor enzyme classes (radical SAM, 2OG dioxygenase, P450) provides a concrete, transferable argument for identifying the enzyme as a membrane-bound prenyltransferase. Among the four offered reactions, only B is a prenyltransferase (diphosphate-transfer) reaction. This reasoning relies on general protein-family knowledge (membrane prenyltransferase architecture, P450 heme motif, radical SAM Cys cluster, 2OG facial triad) rather than a fact specific to this exact protein."
  },
  "case_id": "catalytic_activity_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A6A6H402 (sequence matched) annotates this protein as Prenyltransferase vviA (EC 2.5.1.-) with the exact catalytic reaction: (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate. The annotation carries ECO:0000269 (direct assay evidence) from PubMed:39310987 (Tang & Zou, Org. Lett. 2024), indicating experimental characterization. The expected answer B matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The specific substrates (drim-8-en-11-yl diphosphate, D-mannitol, sporulositol A) are unusual and not derivable from sequence alone; however, the question only requires identifying the reaction type (prenyltransferase), which is distinguishable by topology and motif absence.",
    "The annotation is from a 2024 experimental study (PubMed:39310987); the protein was only integrated into Swiss-Prot in April 2025, so this is relatively recent knowledge.",
    "Membrane-bound prenyltransferases can have diverse substrate specificities; the reasoning identifies the enzyme class but not the exact substrates. The question design compensates by making only one option a prenyltransferase reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor requires a distinct catalytic machinery (radical SAM cluster, 2OG/Fe(II) triad, P450 heme) whose signature motifs are absent from the sequence. The membrane-prenyltransferase topology uniquely selects option B among the four alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A6A6H402 (sequence matched) annotates this protein as Prenyltransferase vviA (EC 2.5.1.-) with the exact catalytic reaction: (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate. The annotation carries ECO:0000269 (direct assay evidence) from PubMed:39310987 (Tang & Zou, Org. Lett. 2024), indicating experimental characterization. The expected answer B matches the annotated reaction verbatim.",
    "evidence_ids": ["C5", "C4", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 293-aa sequence is overwhelmingly hydrophobic with multiple predicted transmembrane helices (e.g., VLLFALSVLIDV, WLMTIVVFASPFVVLAV, CIGLMDVTAVVLYLRG, VFWGAFAALAL) and contains GGxxxG motifs typical of membrane protein helix packing. Critically, it lacks: (1) the CxxxCxxC radical SAM cluster needed for option A; (2) the HxD…H facial triad of Fe(II)/2OG dioxygenases needed for option C; (3) the FxxGxxxCxG heme-ligating motif of cytochrome P450s needed for option D. The membrane-bound topology with D residues in loop regions (DLSITLL, DVRDIQEDEQ) is consistent with membrane-bound prenyltransferases (a well-known family in fungal secondary metabolism, e.g., indole prenyltransferases). Option B is the only prenyltransferase reaction (prenyl-diphosphate + acceptor → product + diphosphate), matching the enzyme class identifiable from topology and motif absence. A model recognizing membrane-prenyltransferase architecture and ruling out radical-SAM, 2OG-dioxygenase, and P450 chemistries by motif absence can select B without knowing the specific substrates.",
    "missing_item_specific_fact": "",
    "reason": "The protein's strongly hydrophobic, multi-TM topology combined with the absence of signature motifs for the three distractor enzyme classes (radical SAM, 2OG dioxygenase, P450) provides a concrete, transferable argument for identifying the enzyme as a membrane-bound prenyltransferase. Among the four offered reactions, only B is a prenyltransferase (diphosphate-transfer) reaction. This reasoning relies on general protein-family knowledge (membrane prenyltransferase architecture, P450 heme motif, radical SAM Cys cluster, 2OG facial triad) rather than a fact specific to this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor requires a distinct catalytic machinery (radical SAM cluster, 2OG/Fe(II) triad, P450 heme) whose signature motifs are absent from the sequence. The membrane-prenyltransferase topology uniquely selects option B among the four alternatives."
  },
  "important_caveats": [
    "The specific substrates (drim-8-en-11-yl diphosphate, D-mannitol, sporulositol A) are unusual and not derivable from sequence alone; however, the question only requires identifying the reaction type (prenyltransferase), which is distinguishable by topology and motif absence.",
    "The annotation is from a 2024 experimental study (PubMed:39310987); the protein was only integrated into Swiss-Prot in April 2025, so this is relatively recent knowledge.",
    "Membrane-bound prenyltransferases can have diverse substrate specificities; the reasoning identifies the enzyme class but not the exact substrates. The question design compensates by making only one option a prenyltransferase reaction."
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
  "benchmark_sequence_length": 293,
  "benchmark_sequence_sha256": "897fc4df843bf85f1cdd0a1f4daa86fcaba8dd7ff09001216f7df7ed7a613ef7",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2020-06-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 293,
  "current_source_sequence_sha256": "897fc4df843bf85f1cdd0a1f4daa86fcaba8dd7ff09001216f7df7ed7a613ef7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A6A6H402",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "selected_historical_source_sequence_length": 293,
  "selected_historical_source_sequence_sha256": "897fc4df843bf85f1cdd0a1f4daa86fcaba8dd7ff09001216f7df7ed7a613ef7",
  "selected_historical_version": {
    "accession": "A0A6A6H402",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "VVIA_VIRVR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A6A6H402\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2020-06-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Speckled blister lichen\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetes incertae sedis\",\"Trypetheliales\",\"Trypetheliaceae\",\"Viridothelium\"],\"scientificName\":\"Viridothelium virens\",\"synonyms\":[\"Trypethelium virens\"],\"taxonId\":1048519}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"Sporulositol A biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"Prenyltransferase vviA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82588\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"name\":\"(S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82587\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16899\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:206556\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231796\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Tang Y.J.\",\"Zou Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39310987\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.orglett.4c03154\"}],\"citationType\":\"journal article\",\"firstPage\":\"8366\",\"id\":\"39310987\",\"journal\":\"Org. Lett.\",\"lastPage\":\"8370\",\"publicationDate\":\"2024\",\"title\":\"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.\",\"volume\":\"26\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"PATHWAY\",\"MUTAGENESIS OF LEU-17; ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND THR-277\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   VVIA_VIRVR              Reviewed;         293 AA.\nAC   A0A6A6H402;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-JUN-2020, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Prenyltransferase vviA {ECO:0000303|PubMed:39310987};\nDE            EC=2.5.1.- {ECO:0000269|PubMed:39310987};\nDE   AltName: Full=Sporulositol A biosynthesis cluster protein A {ECO:0000303|PubMed:39310987};\nGN   Name=vviA {ECO:0000303|PubMed:39310987}; ORFNames=EV356DRAFT_253807;\nOS   Viridothelium virens (Speckled blister lichen) (Trypethelium virens).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetes incertae sedis; Trypetheliales; Trypetheliaceae;\nOC   Viridothelium.\nOX   NCBI_TaxID=1048519;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Prenyltransferase vviA {ECO:0000303|PubMed:39310987};\nDE            EC=2.5.1.- {ECO:0000269|PubMed:39310987};\nDE   AltName: Full=Sporulositol A biosynthesis cluster protein A {ECO:0000303|PubMed:39310987};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, PATHWAY, AND MUTAGENESIS OF LEU-17;\nRP   ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND\nRP   THR-277.\nRX   PubMed=39310987; DOI=10.1021/acs.orglett.4c03154;\nRA   Tang Y.J., Zou Y.;\nRT   \"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.\";\nRL   Org. Lett. 26:8366-8370(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol\nCC         A + diphosphate; Xref=Rhea:RHEA:82587, ChEBI:CHEBI:16899,\nCC         ChEBI:CHEBI:33019, ChEBI:CHEBI:206556, ChEBI:CHEBI:231796;\nCC         Evidence={ECO:0000269|PubMed:39310987};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82588;\nCC         Evidence={ECO:0000269|PubMed:39310987};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 88. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
