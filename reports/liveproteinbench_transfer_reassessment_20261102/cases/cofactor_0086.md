# cofactor_0086: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0086.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **A** — heme

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | no saved label | no saved label | output error (invalid_review) |
| after | GPT-6 Luna | no saved label | no saved label | output error (invalid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MSKPAAAAPSDPSKPSKPLKEVPGSYGLPVLGAVKDRLDFYWFQGDTEFFRIRMEQHKSTVFRVNYSPGPPGYPDSRGIILLDQKSFSVLLDNSKVDKSDTLLGPYIPNLAFTGGYRVLPYLDTSEAKHTAYKDLIFELLHVNSSRIIPEYNKVFAETAGSWEERIAKSGKAEVFASSDSMITKFLLRTIVHKDPAEPGPASLGPKFRDTYQLWTGVNFAGIAHTPLPHFLEELLFHTFRLPPFLVKKQYKALANFYRTHATEVLDLAEKKYGLDREETVHQLILILGINARLGLHKMIPALIYYLGLLGEDFQAKIAAEVRSAVHKNRAQGEEGVNITTQALLEMPLLRSTVLETLRLTPSIFYIYGRAREDMVIESHDAAFQIKKGELLGGHQYFVMRDPEVFEEPHKFVADRFLGERGKAVLPYLVWSNGRETESPSSSNKQCPAKDVAELITMQFVAEMFLRYDSFEITKDSFINTTELNVHLKSLKKRSV

[Multiple Choices]
A. heme
B. Mg(2+)
C. cob(II)alamin
D. Mn(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact-matching sequence is annotated as CYP74M3, a divinyl ether synthase, with heme as its cofactor. The cofactor annotation is transferred from another UniProt entry (ECO:0000250), so this supports the key as a family-based annotation rather than establishing direct experimental measurement for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices alone and the supplied sequence do not provide a clear, reliable sequence-only argument for selecting heme over the listed ions and cobalamin. The relevant biological distinction is that this protein is a CYP74 divinyl ether synthase, a fact not supplied in the question.


**Missing item-specific fact**

> The protein's identity/family and its heme-cofactor annotation, which require a protein-specific annotation or external family identification.


**Reason**

> The key is supported by reviewer-only annotation, but that information was absent from the evaluated input. Identifying the exact protein or recalling its family annotation is lookup or memorization, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports heme for this protein; no other listed option is supported by the supplied reviewer evidence.


### Important caveats

- The heme annotation is transferred by similarity, not direct experimental evidence for this exact sequence in the excerpts.
- The sequence matches the cited current and historical UniProt records; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices alone and the supplied sequence do not provide a clear, reliable sequence-only argument for selecting heme over the listed ions and cobalamin. The relevant biological distinction is that this protein is a CYP74 divinyl ether synthase, a fact not supplied in the question.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity/family and its heme-cofactor annotation, which require a protein-specific annotation or external family identification.",
    "reason": "The key is supported by reviewer-only annotation, but that information was absent from the evaluated input. Identifying the exact protein or recalling its family annotation is lookup or memorization, not reasoning from supplied context."
  },
  "case_id": "cofactor_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact-matching sequence is annotated as CYP74M3, a divinyl ether synthase, with heme as its cofactor. The cofactor annotation is transferred from another UniProt entry (ECO:0000250), so this supports the key as a family-based annotation rather than establishing direct experimental measurement for this exact protein."
  },
  "important_caveats": [
    "The heme annotation is transferred by similarity, not direct experimental evidence for this exact sequence in the excerpts.",
    "The sequence matches the cited current and historical UniProt records; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports heme for this protein; no other listed option is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching sequence is annotated as CYP74M3, a divinyl ether synthase, with heme as its cofactor. The cofactor annotation is transferred from another UniProt entry (ECO:0000250), so this supports the key as a family-based annotation rather than establishing direct experimental measurement for this exact protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices alone and the supplied sequence do not provide a clear, reliable sequence-only argument for selecting heme over the listed ions and cobalamin. The relevant biological distinction is that this protein is a CYP74 divinyl ether synthase, a fact not supplied in the question.",
    "missing_item_specific_fact": "The protein's identity/family and its heme-cofactor annotation, which require a protein-specific annotation or external family identification.",
    "reason": "The key is supported by reviewer-only annotation, but that information was absent from the evaluated input. Identifying the exact protein or recalling its family annotation is lookup or memorization, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports heme for this protein; no other listed option is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The heme annotation is transferred by similarity, not direct experimental evidence for this exact sequence in the excerpts.",
    "The sequence matches the cited current and historical UniProt records; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

No visible final review text was saved. Internal model reasoning is not a substitute for a visible review and is not published. The final-content extraction failed because the saved final content was not text.

**Saved parsed visible review:** `null`.

**Exact saved visible final text:** empty string (`""`). No visible final is synthesized from private reasoning.

## After: GPT-6 Luna

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1144)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates heme as the cofactor, but the evidence is transferred by similarity from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein in the excerpts. This supports the key with that qualification.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could use sequence-profile or homology knowledge to recognize this as belonging to a plant cytochrome P450-type enzyme family. P450 enzymes use a heme catalytic center, making heme a meaningful choice over Mg(2+), Mn(2+), or cob(II)alamin. This is a family-level inference, not a guarantee based on an obvious single motif.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of P450-family sequences and their heme-dependent chemistry provides a credible basis for distinguishing heme among these options without recalling this exact protein's database record.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives distinguish heme from unrelated metal-ion and cobalamin cofactors; no second choice is comparably supported."
  },
  "important_caveats": [
    "The supplied source evidence supports heme by a similarity-based annotation; the excerpts do not establish direct experimental verification for this exact protein."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly lists heme (ChEBI:CHEBI:30413) as the cofactor for this protein (Divinyl ether synthase CYP74M3, a cytochrome P450). The evidence code ECO:0000250 indicates transfer by similarity from Q96242, but this is entirely consistent with the universal, defining property of the cytochrome P450 superfamily: all P450 enzymes use heme (iron-protoporphyrin IX) as their prosthetic group. The protein is confirmed as a CYP74 family member (EC 4.2.1.183) by experimental characterization (PubMed:26776054, C6/H3).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~495 aa) exhibits hallmarks of the cytochrome P450 superfamily: appropriate length for a P450, conserved regions consistent with the P450 fold (e.g., the 'FAG' region in 'WTGVNFAGIAHTPLPHF' near the heme-binding pocket, the I-helix 'AG' motif, and the overall domain architecture). The CYP nomenclature and P450 sequence signature are among the most recognizable and universally conserved features in biochemistry. The defining, universal property of ALL cytochrome P450 enzymes is the use of heme (Fe-protoporphyrin IX) as their cofactor/prosthetic group — this is not a probabilistic association but a structural and mechanistic necessity (the heme iron performs substrate oxidation). The other options (Mg²⁺, cob(II)alamin, Mn²⁺) are cofactors for entirely different enzyme classes (kinases/polymerases, methyltransferases/isomerases, and certain oxidoreductases/SODs respectively) and are never associated with P450 enzymes. Thus, recognizing the P450 family from sequence features and applying the universal P450→heme rule meaningfully and decisively distinguishes option A from B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The inference relies on well-established, transferable family-level knowledge: (1) recognizing cytochrome P450 sequence features from the provided sequence, and (2) applying the universal, textbook fact that all P450 enzymes require heme. This does not require knowing the specific annotation for this exact Selaginella protein. The P450-heme connection is one of the most fundamental and universally taught facts in enzymology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the protein is recognized as a cytochrome P450 (which the sequence supports through conserved motifs and architecture), heme is the only defensible cofactor among the four options. Mg²⁺, cob(II)alamin, and Mn²⁺ have no association with P450 enzymes. There is no meaningful ambiguity.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity from Q96242), not direct experimental determination for this specific protein. However, the P450-heme connection is a universal family property, making this transfer entirely reliable.
- The exact heme-binding motif (FxxGxxxCxG) is somewhat degenerate in plant P450s; the Cys ligand in this sequence appears in the context 'KQCPAKD' rather than the textbook-perfect motif, but the overall P450 architecture is maintained.
- The reviewer-only evidence (UniProt accession, organism, protein name) was not available to the evaluated model; the reasoning must rely solely on sequence features and general P450 biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~495 aa) exhibits hallmarks of the cytochrome P450 superfamily: appropriate length for a P450, conserved regions consistent with the P450 fold (e.g., the 'FAG' region in 'WTGVNFAGIAHTPLPHF' near the heme-binding pocket, the I-helix 'AG' motif, and the overall domain architecture). The CYP nomenclature and P450 sequence signature are among the most recognizable and universally conserved features in biochemistry. The defining, universal property of ALL cytochrome P450 enzymes is the use of heme (Fe-protoporphyrin IX) as their cofactor/prosthetic group — this is not a probabilistic association but a structural and mechanistic necessity (the heme iron performs substrate oxidation). The other options (Mg²⁺, cob(II)alamin, Mn²⁺) are cofactors for entirely different enzyme classes (kinases/polymerases, methyltransferases/isomerases, and certain oxidoreductases/SODs respectively) and are never associated with P450 enzymes. Thus, recognizing the P450 family from sequence features and applying the universal P450→heme rule meaningfully and decisively distinguishes option A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on well-established, transferable family-level knowledge: (1) recognizing cytochrome P450 sequence features from the provided sequence, and (2) applying the universal, textbook fact that all P450 enzymes require heme. This does not require knowing the specific annotation for this exact Selaginella protein. The P450-heme connection is one of the most fundamental and universally taught facts in enzymology."
  },
  "case_id": "cofactor_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists heme (ChEBI:CHEBI:30413) as the cofactor for this protein (Divinyl ether synthase CYP74M3, a cytochrome P450). The evidence code ECO:0000250 indicates transfer by similarity from Q96242, but this is entirely consistent with the universal, defining property of the cytochrome P450 superfamily: all P450 enzymes use heme (iron-protoporphyrin IX) as their prosthetic group. The protein is confirmed as a CYP74 family member (EC 4.2.1.183) by experimental characterization (PubMed:26776054, C6/H3)."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity from Q96242), not direct experimental determination for this specific protein. However, the P450-heme connection is a universal family property, making this transfer entirely reliable.",
    "The exact heme-binding motif (FxxGxxxCxG) is somewhat degenerate in plant P450s; the Cys ligand in this sequence appears in the context 'KQCPAKD' rather than the textbook-perfect motif, but the overall P450 architecture is maintained.",
    "The reviewer-only evidence (UniProt accession, organism, protein name) was not available to the evaluated model; the reasoning must rely solely on sequence features and general P450 biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is recognized as a cytochrome P450 (which the sequence supports through conserved motifs and architecture), heme is the only defensible cofactor among the four options. Mg²⁺, cob(II)alamin, and Mn²⁺ have no association with P450 enzymes. There is no meaningful ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists heme (ChEBI:CHEBI:30413) as the cofactor for this protein (Divinyl ether synthase CYP74M3, a cytochrome P450). The evidence code ECO:0000250 indicates transfer by similarity from Q96242, but this is entirely consistent with the universal, defining property of the cytochrome P450 superfamily: all P450 enzymes use heme (iron-protoporphyrin IX) as their prosthetic group. The protein is confirmed as a CYP74 family member (EC 4.2.1.183) by experimental characterization (PubMed:26776054, C6/H3).",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~495 aa) exhibits hallmarks of the cytochrome P450 superfamily: appropriate length for a P450, conserved regions consistent with the P450 fold (e.g., the 'FAG' region in 'WTGVNFAGIAHTPLPHF' near the heme-binding pocket, the I-helix 'AG' motif, and the overall domain architecture). The CYP nomenclature and P450 sequence signature are among the most recognizable and universally conserved features in biochemistry. The defining, universal property of ALL cytochrome P450 enzymes is the use of heme (Fe-protoporphyrin IX) as their cofactor/prosthetic group — this is not a probabilistic association but a structural and mechanistic necessity (the heme iron performs substrate oxidation). The other options (Mg²⁺, cob(II)alamin, Mn²⁺) are cofactors for entirely different enzyme classes (kinases/polymerases, methyltransferases/isomerases, and certain oxidoreductases/SODs respectively) and are never associated with P450 enzymes. Thus, recognizing the P450 family from sequence features and applying the universal P450→heme rule meaningfully and decisively distinguishes option A from B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on well-established, transferable family-level knowledge: (1) recognizing cytochrome P450 sequence features from the provided sequence, and (2) applying the universal, textbook fact that all P450 enzymes require heme. This does not require knowing the specific annotation for this exact Selaginella protein. The P450-heme connection is one of the most fundamental and universally taught facts in enzymology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is recognized as a cytochrome P450 (which the sequence supports through conserved motifs and architecture), heme is the only defensible cofactor among the four options. Mg²⁺, cob(II)alamin, and Mn²⁺ have no association with P450 enzymes. There is no meaningful ambiguity."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity from Q96242), not direct experimental determination for this specific protein. However, the P450-heme connection is a universal family property, making this transfer entirely reliable.",
    "The exact heme-binding motif (FxxGxxxCxG) is somewhat degenerate in plant P450s; the Cys ligand in this sequence appears in the context 'KQCPAKD' rather than the textbook-perfect motif, but the overall P450 architecture is maintained.",
    "The reviewer-only evidence (UniProt accession, organism, protein name) was not available to the evaluated model; the reasoning must rely solely on sequence features and general P450 biology."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "D8QZ31",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "0b22ddba73dd0ac278bf9cedf5b7de50ecaf7f1f1efc3e1bef923293962e731d",
  "benchmark_sequence_length": 495,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 70,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-10-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "current_source_sequence_sha256": "0b22ddba73dd0ac278bf9cedf5b7de50ecaf7f1f1efc3e1bef923293962e731d",
  "current_source_sequence_length": 495,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 68,
  "selected_historical_version": {
    "accession": "D8QZ31",
    "database": "Swiss-Prot",
    "entryVersion": 68,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C74M3_SELML",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "selected_historical_source_sequence_sha256": "0b22ddba73dd0ac278bf9cedf5b7de50ecaf7f1f1efc3e1bef923293962e731d",
  "selected_historical_source_sequence_length": 495,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 68,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"D8QZ31\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":70,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-10-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Gemmiferous spikemoss\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Lycopodiopsida\",\"Selaginellales\",\"Selaginellaceae\",\"Selaginelloideae\",\"Selaginella\"],\"scientificName\":\"Selaginella moellendorffii\",\"synonyms\":[\"Kungiselaginella moellendorffii\"],\"taxonId\":88036}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.183\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"Etheroleic acid synthase CYP74M3\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"Divinyl ether synthase CYP74M3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q96242\",\"source\":\"UniProtKB\"}],\"name\":\"heme\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Gorina S.S.\",\"Toporkova Y.Y.\",\"Mukhtarova L.S.\",\"Smirnova E.O.\",\"Chechetkin I.R.\",\"Khairutdinov B.I.\",\"Gogolev Y.V.\",\"Grechkin A.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26776054\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbalip.2016.01.001\"}],\"citationType\":\"journal article\",\"firstPage\":\"301\",\"id\":\"26776054\",\"journal\":\"Biochim. Biophys. Acta\",\"lastPage\":\"309\",\"publicationDate\":\"2016\",\"title\":\"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular cloning and identification of divinyl ether synthases CYP74M1 and CYP74M3.\",\"volume\":\"1861\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   C74M3_SELML             Reviewed;         495 AA.\nAC   D8QZ31;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-OCT-2010, sequence version 1.\nDT   28-JAN-2026, entry version 68.\nDE   RecName: Full=Divinyl ether synthase CYP74M3 {ECO:0000303|PubMed:26776054};\nDE   AltName: Full=Etheroleic acid synthase CYP74M3 {ECO:0000305|PubMed:26776054};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};\nGN   Name=CYP74M3 {ECO:0000303|PubMed:26776054};\nGN   Synonyms=DES2 {ECO:0000303|PubMed:26776054};\nGN   ORFNames=SELMODRAFT_81998 {ECO:0000312|EMBL:EFJ34345.1};\nOS   Selaginella moellendorffii (Spikemoss).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Lycopodiopsida; Selaginellales; Selaginellaceae; Selaginella.\nOX   NCBI_TaxID=88036;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 68,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=Divinyl ether synthase CYP74M3 {ECO:0000303|PubMed:26776054};\nDE   AltName: Full=Etheroleic acid synthase CYP74M3 {ECO:0000305|PubMed:26776054};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 68,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "source_locator": "lines 40-48",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRX   PubMed=26776054; DOI=10.1016/j.bbalip.2016.01.001;\nRA   Gorina S.S., Toporkova Y.Y., Mukhtarova L.S., Smirnova E.O.,\nRA   Chechetkin I.R., Khairutdinov B.I., Gogolev Y.V., Grechkin A.N.;\nRT   \"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular\nRT   cloning and identification of divinyl ether synthases CYP74M1 and\nRT   CYP74M3.\";\nRL   Biochim. Biophys. Acta 1861:301-309(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 68,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "source_locator": "lines 70-72",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=heme; Xref=ChEBI:CHEBI:30413;\nCC         Evidence={ECO:0000250|UniProtKB:Q96242};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 68,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 86. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
