# GO_molecular_function_0127

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0127.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — sodium channel inhibitor activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMKTVIVLIVFSLVMIVVKSDNGYLLDKYTGCKIWCVINNDSCNSHCIGSGGYYGYCYFWKLACYCQGAPRSELWHYETNRCRA

[Multiple Choices]
A. protein folding chaperone
B. calcium channel activity
C. sodium channel inhibitor activity
D. histone reader activity
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

> The sequence-matched historical UniProt record annotates sodium channel inhibitor activity, but as an IEA:InterPro computational inference (H4), not direct experimental evidence. The record separately reports experimentally supported antimicrobial activity (H3), which does not itself establish sodium-channel inhibition.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal signal-like region followed by a short, cysteine-rich peptide, a pattern compatible with secreted scorpion-toxin-like peptides. Transferable knowledge that such disulfide-rich venom peptides often act on ion channels makes C a meaningful choice over a calcium channel protein, a folding chaperone, or a histone reader. This supports a probabilistic family-level inference, not proof of sodium-channel inhibition.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence pattern and venom-peptide family knowledge provide a concrete basis for distinguishing C among these alternatives, although the specific activity is not established experimentally by the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second offered option has comparable support from the sequence pattern or the supplied annotation.


### Important caveats

- The GO sodium-channel inhibitor annotation is computationally inferred; the supplied experimental function evidence instead supports antimicrobial activity.
- The sequence-matched evidence supports applying the annotation to this sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal signal-like region followed by a short, cysteine-rich peptide, a pattern compatible with secreted scorpion-toxin-like peptides. Transferable knowledge that such disulfide-rich venom peptides often act on ion channels makes C a meaningful choice over a calcium channel protein, a folding chaperone, or a histone reader. This supports a probabilistic family-level inference, not proof of sodium-channel inhibition.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence pattern and venom-peptide family knowledge provide a concrete basis for distinguishing C among these alternatives, although the specific activity is not established experimentally by the supplied evidence."
  },
  "case_id": "GO_molecular_function_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates sodium channel inhibitor activity, but as an IEA:InterPro computational inference (H4), not direct experimental evidence. The record separately reports experimentally supported antimicrobial activity (H3), which does not itself establish sodium-channel inhibition."
  },
  "important_caveats": [
    "The GO sodium-channel inhibitor annotation is computationally inferred; the supplied experimental function evidence instead supports antimicrobial activity.",
    "The sequence-matched evidence supports applying the annotation to this sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered option has comparable support from the sequence pattern or the supplied annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates sodium channel inhibitor activity, but as an IEA:InterPro computational inference (H4), not direct experimental evidence. The record separately reports experimentally supported antimicrobial activity (H3), which does not itself establish sodium-channel inhibition.",
    "evidence_ids": ["H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal signal-like region followed by a short, cysteine-rich peptide, a pattern compatible with secreted scorpion-toxin-like peptides. Transferable knowledge that such disulfide-rich venom peptides often act on ion channels makes C a meaningful choice over a calcium channel protein, a folding chaperone, or a histone reader. This supports a probabilistic family-level inference, not proof of sodium-channel inhibition.",
    "missing_item_specific_fact": "",
    "reason": "The sequence pattern and venom-peptide family knowledge provide a concrete basis for distinguishing C among these alternatives, although the specific activity is not established experimentally by the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered option has comparable support from the sequence pattern or the supplied annotation."
  },
  "important_caveats": [
    "The GO sodium-channel inhibitor annotation is computationally inferred; the supplied experimental function evidence instead supports antimicrobial activity.",
    "The sequence-matched evidence supports applying the annotation to this sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry F6K6F3 carries the GO:0019871 (sodium channel inhibitor activity) annotation (evidence C6, H4), matching the author's expected answer. However, this annotation is IEA:InterPro (computational inference by domain match), not experimentally validated for this specific peptide. The experimentally supported function (ECO:0000269, PubMed:29770866) is antimicrobial activity (C5, H3). The protein name 'MeuNaTxbeta-2' reflects its membership in the NaTx (sodium channel toxin) superfamily, and the InterPro domain match triggers the GO annotation. The expected answer is supported by the database record, though the annotation level is computational rather than experimental.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is an 84-aa precursor with a hydrophobic signal peptide (~20 residues) followed by a small mature peptide (~64 aa) containing 7-8 cysteines in a characteristic spacing pattern. This architecture—a small, cysteine-rich, secreted peptide—is the hallmark of animal venom toxins (especially scorpion/buthid toxins), which form disulfide-stabilized scaffolds. From general knowledge of protein families: (1) A ~60-aa peptide cannot constitute a transmembrane ion channel (eliminates B: calcium channel activity, which requires a large multi-pass membrane protein); (2) Small cysteine-rich secreted peptides are not molecular chaperones (eliminates A); (3) They are not chromatin-associated histone readers (eliminates D). The remaining option C (sodium channel inhibitor activity) is the only one consistent with a small peptide toxin that modulates ion channels by binding to them externally, as is well established for scorpion NaTx-family peptides. The cysteine knot/inhibitor cystine knot motif common to this family is visible in the sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate all distractors using general structural and functional principles: small secreted cysteine-rich peptides are toxins that inhibit channels rather than being channels themselves. The distinction between 'being a channel' (B) and 'inhibiting a channel' (C) is a fundamental structural principle (a 60-aa peptide cannot span a membrane), and the elimination of A and D is straightforward from the sequence composition. The specific sub-family assignment (NaTx vs KTx) is not needed because only one channel-inhibitor option is offered.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four options, A (chaperone), B (calcium channel activity), and D (histone reader) are structurally and functionally incompatible with a small cysteine-rich secreted peptide toxin. Only C is consistent with the sequence features. While the experimental evidence for this specific peptide emphasizes antimicrobial activity, that option is not offered, so no ambiguity arises among the presented choices.


### Important caveats

- The GO:0019871 annotation is IEA:InterPro (computational inference), not experimentally validated for this specific peptide; the experimental evidence (PubMed:29770866) describes antimicrobial activity.
- The protein belongs to the NaTx superfamily by name and InterPro domain, but its experimentally characterized primary activity is antimicrobial, not sodium channel inhibition.
- The reasoning argument eliminates B because a small peptide cannot be an ion channel, but does not independently prove sodium vs. potassium channel specificity; this is acceptable because only one channel-inhibitor option is offered.
- The reviewer-only evidence (accession, organism, protein name) was not available to the evaluated model; the reasoning argument relies solely on sequence features and general family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is an 84-aa precursor with a hydrophobic signal peptide (~20 residues) followed by a small mature peptide (~64 aa) containing 7-8 cysteines in a characteristic spacing pattern. This architecture—a small, cysteine-rich, secreted peptide—is the hallmark of animal venom toxins (especially scorpion/buthid toxins), which form disulfide-stabilized scaffolds. From general knowledge of protein families: (1) A ~60-aa peptide cannot constitute a transmembrane ion channel (eliminates B: calcium channel activity, which requires a large multi-pass membrane protein); (2) Small cysteine-rich secreted peptides are not molecular chaperones (eliminates A); (3) They are not chromatin-associated histone readers (eliminates D). The remaining option C (sodium channel inhibitor activity) is the only one consistent with a small peptide toxin that modulates ion channels by binding to them externally, as is well established for scorpion NaTx-family peptides. The cysteine knot/inhibitor cystine knot motif common to this family is visible in the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate all distractors using general structural and functional principles: small secreted cysteine-rich peptides are toxins that inhibit channels rather than being channels themselves. The distinction between 'being a channel' (B) and 'inhibiting a channel' (C) is a fundamental structural principle (a 60-aa peptide cannot span a membrane), and the elimination of A and D is straightforward from the sequence composition. The specific sub-family assignment (NaTx vs KTx) is not needed because only one channel-inhibitor option is offered."
  },
  "case_id": "GO_molecular_function_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry F6K6F3 carries the GO:0019871 (sodium channel inhibitor activity) annotation (evidence C6, H4), matching the author's expected answer. However, this annotation is IEA:InterPro (computational inference by domain match), not experimentally validated for this specific peptide. The experimentally supported function (ECO:0000269, PubMed:29770866) is antimicrobial activity (C5, H3). The protein name 'MeuNaTxbeta-2' reflects its membership in the NaTx (sodium channel toxin) superfamily, and the InterPro domain match triggers the GO annotation. The expected answer is supported by the database record, though the annotation level is computational rather than experimental."
  },
  "important_caveats": [
    "The GO:0019871 annotation is IEA:InterPro (computational inference), not experimentally validated for this specific peptide; the experimental evidence (PubMed:29770866) describes antimicrobial activity.",
    "The protein belongs to the NaTx superfamily by name and InterPro domain, but its experimentally characterized primary activity is antimicrobial, not sodium channel inhibition.",
    "The reasoning argument eliminates B because a small peptide cannot be an ion channel, but does not independently prove sodium vs. potassium channel specificity; this is acceptable because only one channel-inhibitor option is offered.",
    "The reviewer-only evidence (accession, organism, protein name) was not available to the evaluated model; the reasoning argument relies solely on sequence features and general family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, A (chaperone), B (calcium channel activity), and D (histone reader) are structurally and functionally incompatible with a small cysteine-rich secreted peptide toxin. Only C is consistent with the sequence features. While the experimental evidence for this specific peptide emphasizes antimicrobial activity, that option is not offered, so no ambiguity arises among the presented choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry F6K6F3 carries the GO:0019871 (sodium channel inhibitor activity) annotation (evidence C6, H4), matching the author's expected answer. However, this annotation is IEA:InterPro (computational inference by domain match), not experimentally validated for this specific peptide. The experimentally supported function (ECO:0000269, PubMed:29770866) is antimicrobial activity (C5, H3). The protein name 'MeuNaTxbeta-2' reflects its membership in the NaTx (sodium channel toxin) superfamily, and the InterPro domain match triggers the GO annotation. The expected answer is supported by the database record, though the annotation level is computational rather than experimental.",
    "evidence_ids": ["C6", "H4", "C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is an 84-aa precursor with a hydrophobic signal peptide (~20 residues) followed by a small mature peptide (~64 aa) containing 7-8 cysteines in a characteristic spacing pattern. This architecture—a small, cysteine-rich, secreted peptide—is the hallmark of animal venom toxins (especially scorpion/buthid toxins), which form disulfide-stabilized scaffolds. From general knowledge of protein families: (1) A ~60-aa peptide cannot constitute a transmembrane ion channel (eliminates B: calcium channel activity, which requires a large multi-pass membrane protein); (2) Small cysteine-rich secreted peptides are not molecular chaperones (eliminates A); (3) They are not chromatin-associated histone readers (eliminates D). The remaining option C (sodium channel inhibitor activity) is the only one consistent with a small peptide toxin that modulates ion channels by binding to them externally, as is well established for scorpion NaTx-family peptides. The cysteine knot/inhibitor cystine knot motif common to this family is visible in the sequence.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate all distractors using general structural and functional principles: small secreted cysteine-rich peptides are toxins that inhibit channels rather than being channels themselves. The distinction between 'being a channel' (B) and 'inhibiting a channel' (C) is a fundamental structural principle (a 60-aa peptide cannot span a membrane), and the elimination of A and D is straightforward from the sequence composition. The specific sub-family assignment (NaTx vs KTx) is not needed because only one channel-inhibitor option is offered."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, A (chaperone), B (calcium channel activity), and D (histone reader) are structurally and functionally incompatible with a small cysteine-rich secreted peptide toxin. Only C is consistent with the sequence features. While the experimental evidence for this specific peptide emphasizes antimicrobial activity, that option is not offered, so no ambiguity arises among the presented choices."
  },
  "important_caveats": [
    "The GO:0019871 annotation is IEA:InterPro (computational inference), not experimentally validated for this specific peptide; the experimental evidence (PubMed:29770866) describes antimicrobial activity.",
    "The protein belongs to the NaTx superfamily by name and InterPro domain, but its experimentally characterized primary activity is antimicrobial, not sodium channel inhibition.",
    "The reasoning argument eliminates B because a small peptide cannot be an ion channel, but does not independently prove sodium vs. potassium channel specificity; this is acceptable because only one channel-inhibitor option is offered.",
    "The reviewer-only evidence (accession, organism, protein name) was not available to the evaluated model; the reasoning argument relies solely on sequence features and general family knowledge."
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
  "benchmark_sequence_length": 84,
  "benchmark_sequence_sha256": "8ddf03e7da5886480794207cdf93801cb23edc44e73f775d93b94c5133a566fe",
  "current_entry_audit": {
    "entryVersion": 46,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-07-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2f8ddf5a02bb62a6e8fdafffdf12262a0a9c5e67c732840115366acaca672a71",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 84,
  "current_source_sequence_sha256": "8ddf03e7da5886480794207cdf93801cb23edc44e73f775d93b94c5133a566fe",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 45,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "F6K6F3",
  "selected_historical_entry_version": 45,
  "selected_historical_record_sha256": "4f110a7548ccfcd43132cf259deffb971397d09e10bfe54c7983dbaabaeaa24c",
  "selected_historical_source_sequence_length": 84,
  "selected_historical_source_sequence_sha256": "8ddf03e7da5886480794207cdf93801cb23edc44e73f775d93b94c5133a566fe",
  "selected_historical_version": {
    "accession": "F6K6F3",
    "database": "Swiss-Prot",
    "entryVersion": 45,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "SCX2_MESEU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F6K6F3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"F6K6F3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:17.591838+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f8ddf5a02bb62a6e8fdafffdf12262a0a9c5e67c732840115366acaca672a71",
  "url": "https://rest.uniprot.org/uniprotkb/F6K6F3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F6K6F3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":46,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-07-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:17.591838+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f8ddf5a02bb62a6e8fdafffdf12262a0a9c5e67c732840115366acaca672a71",
  "url": "https://rest.uniprot.org/uniprotkb/F6K6F3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F6K6F3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Lesser Asian scorpion\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Chelicerata\",\"Arachnida\",\"Scorpiones\",\"Buthida\",\"Buthoidea\",\"Buthidae\",\"Mesobuthus\"],\"scientificName\":\"Mesobuthus eupeus\",\"synonyms\":[\"Buthus eupeus\"],\"taxonId\":34648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:17.591838+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f8ddf5a02bb62a6e8fdafffdf12262a0a9c5e67c732840115366acaca672a71",
  "url": "https://rest.uniprot.org/uniprotkb/F6K6F3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F6K6F3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADT89767.1\",\"source\":\"EMBL\"}],\"value\":\"Antibacterial peptide MeuNaTx-15\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29770866\",\"source\":\"PubMed\"}],\"value\":\"Antimicrobial peptide MeuNaTxbeta-2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29770866\",\"source\":\"PubMed\"}],\"value\":\"MTbeta-2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:17.591838+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f8ddf5a02bb62a6e8fdafffdf12262a0a9c5e67c732840115366acaca672a71",
  "url": "https://rest.uniprot.org/uniprotkb/F6K6F3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F6K6F3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29770866\",\"source\":\"PubMed\"}],\"value\":\"Antimicrobial peptide with activity against both Gram-positive and -negative bacteria\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:28:17.591838+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f8ddf5a02bb62a6e8fdafffdf12262a0a9c5e67c732840115366acaca672a71",
  "url": "https://rest.uniprot.org/uniprotkb/F6K6F3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F6K6F3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0019871\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:sodium channel inhibitor activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:28:17.591838+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f8ddf5a02bb62a6e8fdafffdf12262a0a9c5e67c732840115366acaca672a71",
  "url": "https://rest.uniprot.org/uniprotkb/F6K6F3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F6K6F3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0090729\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:toxin activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:28:17.591838+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f8ddf5a02bb62a6e8fdafffdf12262a0a9c5e67c732840115366acaca672a71",
  "url": "https://rest.uniprot.org/uniprotkb/F6K6F3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F6K6F3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Gao B.\",\"Dalziel J.\",\"Tanzi S.\",\"Zhu S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29770866\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00726-018-2580-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"1025\",\"id\":\"29770866\",\"journal\":\"Amino Acids\",\"lastPage\":\"1043\",\"publicationDate\":\"2018\",\"title\":\"Meucin-49, a multifunctional scorpion venom peptide with bactericidal synergy with neurotoxins.\",\"volume\":\"50\"},\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Venom\"},{\"type\":\"TISSUE\",\"value\":\"Venom gland\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] OF 21-84\",\"PROTEIN SEQUENCE OF 21-40\",\"FUNCTION\",\"MASS SPECTROMETRY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:17.591838+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f8ddf5a02bb62a6e8fdafffdf12262a0a9c5e67c732840115366acaca672a71",
  "url": "https://rest.uniprot.org/uniprotkb/F6K6F3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F6K6F3?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H1",
  "excerpt": "ID   SCX2_MESEU              Reviewed;          84 AA.\nAC   F6K6F3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-JUL-2011, sequence version 1.\nDT   28-JAN-2026, entry version 45.\nDE   RecName: Full=Antimicrobial peptide MeuNaTxbeta-2 {ECO:0000303|PubMed:29770866};\nDE            Short=MTbeta-2 {ECO:0000303|PubMed:29770866};\nDE   AltName: Full=Antibacterial peptide MeuNaTx-15 {ECO:0000312|EMBL:ADT89767.1};\nDE   Flags: Precursor;\nOS   Mesobuthus eupeus (Lesser Asian scorpion) (Buthus eupeus).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Chelicerata; Arachnida;\nOC   Scorpiones; Buthida; Buthoidea; Buthidae; Mesobuthus.\nOX   NCBI_TaxID=34648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:19.832132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f110a7548ccfcd43132cf259deffb971397d09e10bfe54c7983dbaabaeaa24c",
  "url": "https://rest.uniprot.org/unisave/F6K6F3?format=txt&versions=45"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F6K6F3?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   NUCLEOTIDE SEQUENCE [MRNA] OF 21-84, PROTEIN SEQUENCE OF 21-40, FUNCTION,\nRP   MASS SPECTROMETRY, AND SUBCELLULAR LOCATION.\nRC   TISSUE=Venom, and Venom gland;\nRX   PubMed=29770866; DOI=10.1007/s00726-018-2580-0;\nRA   Gao B., Dalziel J., Tanzi S., Zhu S.;\nRT   \"Meucin-49, a multifunctional scorpion venom peptide with bactericidal\nRT   synergy with neurotoxins.\";\nRL   Amino Acids 50:1025-1043(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:19.832132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f110a7548ccfcd43132cf259deffb971397d09e10bfe54c7983dbaabaeaa24c",
  "url": "https://rest.uniprot.org/unisave/F6K6F3?format=txt&versions=45"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F6K6F3?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Antimicrobial peptide with activity against both Gram-\nCC       positive and -negative bacteria. {ECO:0000269|PubMed:29770866}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:19.832132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f110a7548ccfcd43132cf259deffb971397d09e10bfe54c7983dbaabaeaa24c",
  "url": "https://rest.uniprot.org/unisave/F6K6F3?format=txt&versions=45"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F6K6F3?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0019871; F:sodium channel inhibitor activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:19.832132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f110a7548ccfcd43132cf259deffb971397d09e10bfe54c7983dbaabaeaa24c",
  "url": "https://rest.uniprot.org/unisave/F6K6F3?format=txt&versions=45"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F6K6F3?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0090729; F:toxin activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:19.832132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f110a7548ccfcd43132cf259deffb971397d09e10bfe54c7983dbaabaeaa24c",
  "url": "https://rest.uniprot.org/unisave/F6K6F3?format=txt&versions=45"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005262\nname: calcium channel activity\nnamespace: molecular_function\ndef: \"Enables the energy-independent facilitated diffusion of a calcium ion through a transmembrane aqueous pore or channel.\" [GOC:mtg_transport, GOC:pr, ISBN:0815340729]\nxref: Reactome:R-HSA-139854 \"IP3R tetramer:I(1,4,5)P3:4xCa2+ transports Ca2+ from platelet dense tubular system to cytosol\"\nxref: Reactome:R-HSA-139855 \"P2X1-mediated entry of Ca++ from plasma\"\nxref: Reactome:R-HSA-210420 \"Ca2+ influx through voltage gated Ca2+ channels\"\nxref: Reactome:R-HSA-3295579 \"TRPs transport extracellular Ca2+ to cytosol\"\nxref: Reactome:R-HSA-8949145 \"VDAC1,2,3 translocate calcium from the cytosol to the mitochondrial intermembrane space\"\nxref: Reactome:R-HSA-8949178 \"MCU translocates calcium from the mitochondrial intermembrane space to the mitochondrial matrix\"\nxref: Reactome:R-HSA-9663785 \"CHRNA9:CHRNA10:AcCho transports Ca2+ from the extracellular region to the cytosol\"\nxref: Reactome:R-HSA-9858800 \"TRPV4 tetramer:CALM1:Ca2+ transports calcium ions (Ca2+) from the extracellular region to the cytosol\"\nis_a: GO:0005261 ! monoatomic cation channel activity\nis_a: GO:0015085 ! calcium ion transmembrane transporter activity\nproperty_value: skos:broadMatch RHEA:29671\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005262",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 55239-55255",
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
  "excerpt": "[Term]\nid: GO:0019871\nname: sodium channel inhibitor activity\nnamespace: molecular_function\nalt_id: GO:0019868\ndef: \"Binds to and stops, prevents, or reduces the activity of a sodium channel.\" [GOC:mah]\nis_a: GO:0008200 ! ion channel inhibitor activity\nis_a: GO:0017080 ! sodium channel regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019871",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 154099-154107",
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
  "excerpt": "[Term]\nid: GO:0044183\nname: protein folding chaperone\nnamespace: molecular_function\ndef: \"Binding to a protein or a protein-containing complex to assist the protein folding process.\" [GOC:mtg_cambridge_2009]\ncomment: Note that a protein folding chaperone binds an unfolded protein to fold it. Do not confuse with unfolded protein holdase activity, which binds an unfolded protein and keeps it unfolded to deliver it to its final destination.\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_prokaryote\nsynonym: \"chaperone activity\" BROAD []\nsynonym: \"protein binding involved in protein folding\" EXACT []\nxref: Reactome:R-HSA-9018785 \"RHOBTB2 binds GTP\"\nxref: Reactome:R-HSA-9855212 \"SDHA binds to SDHB\"\nxref: Reactome:R-HSA-9865893 \"MT-CYB is translated\"\nxref: Reactome:R-HSA-9866253 \"apo-UQCRFS1 binds LYRM7\"\nis_a: GO:0003674 ! molecular_function\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044183",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 255011-255028",
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
  "excerpt": "[Term]\nid: GO:0140566\nname: histone reader activity\nnamespace: molecular_function\ndef: \"A chromatin adaptor activity that brings together a protein and a specific form of histone, either modified by a post-translational modification, or the unmodified form. Histone readers have roles in many processes, including in centromere function or in modulating the accessibility of cis-regulatory regions to the transcription machinery.\" [PMID:11498575, PMID:25688442, PMID:31082667, PMID:34726351]\nsynonym: \"epigenetic reader\" BROAD []\nsynonym: \"histone reader\" EXACT []\nis_a: GO:0140463 ! chromatin-protein adaptor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140566",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 441462-441470",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 127. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
