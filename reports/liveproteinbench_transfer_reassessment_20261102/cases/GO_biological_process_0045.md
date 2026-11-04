# GO_biological_process_0045

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0045.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **A** — regulation of transcription by RNA polymerase II

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLTDRVLATKEALVVALGDNWERYRANMKNWFRSRWTKEEFDAESRKILTPDKLHLHNQFLLALLNKIDAFAPLENPPAVQTSSSSGNRSKRRKRSSRTFAERLNFELSDVLDFVAEDNMQIIRPPTTIGIPSDQQQQQLQSQRYCAQELFLPDAGFIMGRFLIGAWEIGLVSVDDNVAEYVAMAVQVLLKDLLSAIIKKRKHYKTSGEGNFYYDVGAPLRDPSLRNTVTRQKVDDTPLELDKELNTANFMRRQNDDVTFLSACEEVQPTERTVITLKDCQLALRDRNLIGSHAVYSINMERLNMMMH

[Multiple Choices]
A. regulation of transcription by RNA polymerase II
B. negative regulation of protein catabolic process
C. mitotic DNA damage checkpoint signaling
D. modulation of process of another organism
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence matches the cited protein, and UniProt reports experimentally supported membership in SAGA, a complex that activates transcription through chromatin remodeling and histone modification (C5). The exact GO term is also annotated by IBA, a computational phylogenetic inference rather than direct experimental evidence for that precise term (C7). Together these support A.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has basic Lys/Arg-rich regions consistent with nuclear localization and no obvious transmembrane segment or catalytic kinase motif. That profile makes a nonenzymatic nuclear regulatory role, such as transcription regulation (A), more plausible than interspecies modulation (D), protein catabolism regulation (B), or the more specific checkpoint-signaling option (C).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> This is a probabilistic sequence-based distinction, not a definitive functional assignment. Nuclear localization is not specific to transcription, and the sequence alone does not establish a particular complex or process; nevertheless, the broad nuclear-regulatory profile provides a transferable basis favoring A among these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe substantially different processes, and the supplied evidence supports A; no other offered option is comparably supported.


### Important caveats

- The exact GO annotation is supported by an IBA inference, while the cited experimental evidence supports SAGA membership and its transcription-activating function more broadly.
- Sequence features cited for answerability are suggestive, not diagnostic.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has basic Lys/Arg-rich regions consistent with nuclear localization and no obvious transmembrane segment or catalytic kinase motif. That profile makes a nonenzymatic nuclear regulatory role, such as transcription regulation (A), more plausible than interspecies modulation (D), protein catabolism regulation (B), or the more specific checkpoint-signaling option (C).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "This is a probabilistic sequence-based distinction, not a definitive functional assignment. Nuclear localization is not specific to transcription, and the sequence alone does not establish a particular complex or process; nevertheless, the broad nuclear-regulatory profile provides a transferable basis favoring A among these choices."
  },
  "case_id": "GO_biological_process_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited protein, and UniProt reports experimentally supported membership in SAGA, a complex that activates transcription through chromatin remodeling and histone modification (C5). The exact GO term is also annotated by IBA, a computational phylogenetic inference rather than direct experimental evidence for that precise term (C7). Together these support A."
  },
  "important_caveats": [
    "The exact GO annotation is supported by an IBA inference, while the cited experimental evidence supports SAGA membership and its transcription-activating function more broadly.",
    "Sequence features cited for answerability are suggestive, not diagnostic."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe substantially different processes, and the supplied evidence supports A; no other offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited protein, and UniProt reports experimentally supported membership in SAGA, a complex that activates transcription through chromatin remodeling and histone modification (C5). The exact GO term is also annotated by IBA, a computational phylogenetic inference rather than direct experimental evidence for that precise term (C7). Together these support A.",
    "evidence_ids": ["C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has basic Lys/Arg-rich regions consistent with nuclear localization and no obvious transmembrane segment or catalytic kinase motif. That profile makes a nonenzymatic nuclear regulatory role, such as transcription regulation (A), more plausible than interspecies modulation (D), protein catabolism regulation (B), or the more specific checkpoint-signaling option (C).",
    "missing_item_specific_fact": "",
    "reason": "This is a probabilistic sequence-based distinction, not a definitive functional assignment. Nuclear localization is not specific to transcription, and the sequence alone does not establish a particular complex or process; nevertheless, the broad nuclear-regulatory profile provides a transferable basis favoring A among these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe substantially different processes, and the supplied evidence supports A; no other offered option is comparably supported."
  },
  "important_caveats": [
    "The exact GO annotation is supported by an IBA inference, while the cited experimental evidence supports SAGA membership and its transcription-activating function more broadly.",
    "Sequence features cited for answerability are suggestive, not diagnostic."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IPA1 (Transcriptional adapter 1-2, Ada1-2) is directly annotated with GO:0006357 'regulation of transcription by RNA polymerase II' via IBA:GO_Central (evidence C7/H7). The function comment (C5/H6) confirms the protein is a component of the SAGA transcriptional regulatory complex that activates transcription by remodeling chromatin and mediating histone acetylation. The GO term definition (GO1) matches the option text exactly. Multiple experimental references (PubMed 16980620, 21764853, 24493646, 30559249) support the SAGA complex's role in transcription activation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [H6](#evidence-h6), [H7](#evidence-h7), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 308-aa sequence contains WD40 repeat signatures: the 'IGSH' dipeptide near the C-terminus (G followed by H is the canonical WD40 repeat-ending motif), alternating hydrophobic residues forming beta-propeller blades, and a 'RRKR' region resembling a bipartite nuclear localization signal. From well-characterized homologs (yeast Ada1, human Ada1, TAF proteins), WD40-repeat adapter proteins of this size (~250-350 aa) with NLS-like motifs are overwhelmingly associated with transcriptional co-activator complexes (SAGA, Mediator, TFIIH) rather than DNA damage checkpoint signaling (which requires kinase/FHA/BRCT domains absent here), protein catabolic regulation (which requires protease/deubiquitinase/proteasome-interaction domains absent here), or interspecies modulation (which requires pathogen-effector or immune-evasion architectures absent here). The absence of kinase domains rules out C; the absence of proteolytic or ubiquitin-removal catalytic motifs rules out B; the nuclear/chromatin-associated architecture rules out D. The WD40 adapter + NLS + small size pattern learned from Ada1-family proteins across species meaningfully distinguishes option A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the WD40 repeat architecture, note the nuclear localization signal, observe the absence of kinase/BRCT/protease domains, and apply transferable knowledge from Ada1, TAF, and other WD40 transcriptional adapter proteins to conclude this protein participates in transcription regulation by RNA Pol II. The distractors (B, C, D) require domain architectures or functional contexts clearly absent from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent very different biological processes (transcription regulation, protein catabolism, DNA damage checkpoint, interspecies interaction). The WD40 adapter architecture with NLS and absence of kinase, protease, or pathogen-effector domains clearly favors transcriptional regulation over the other three alternatives.


### Important caveats

- The GO:0006357 annotation is via IBA:GO_Central (inferred by biological aspect), not a direct experimental annotation on this protein itself, though the SAGA complex function is well-supported by multiple experimental studies.
- WD40 repeats are found in proteins with diverse functions; the inference relies on the combination of WD40 + small adapter size + NLS + absence of other catalytic/regulatory domains, which is a probabilistic family-level pattern rather than a deterministic rule.
- The reviewer-only evidence confirms identity as Q8IPA1 (Ada1-2, Drosophila), but this accession was not available to the evaluated model; the reasoning must rely on sequence features and transferable knowledge from homologs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 308-aa sequence contains WD40 repeat signatures: the 'IGSH' dipeptide near the C-terminus (G followed by H is the canonical WD40 repeat-ending motif), alternating hydrophobic residues forming beta-propeller blades, and a 'RRKR' region resembling a bipartite nuclear localization signal. From well-characterized homologs (yeast Ada1, human Ada1, TAF proteins), WD40-repeat adapter proteins of this size (~250-350 aa) with NLS-like motifs are overwhelmingly associated with transcriptional co-activator complexes (SAGA, Mediator, TFIIH) rather than DNA damage checkpoint signaling (which requires kinase/FHA/BRCT domains absent here), protein catabolic regulation (which requires protease/deubiquitinase/proteasome-interaction domains absent here), or interspecies modulation (which requires pathogen-effector or immune-evasion architectures absent here). The absence of kinase domains rules out C; the absence of proteolytic or ubiquitin-removal catalytic motifs rules out B; the nuclear/chromatin-associated architecture rules out D. The WD40 adapter + NLS + small size pattern learned from Ada1-family proteins across species meaningfully distinguishes option A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the WD40 repeat architecture, note the nuclear localization signal, observe the absence of kinase/BRCT/protease domains, and apply transferable knowledge from Ada1, TAF, and other WD40 transcriptional adapter proteins to conclude this protein participates in transcription regulation by RNA Pol II. The distractors (B, C, D) require domain architectures or functional contexts clearly absent from the sequence."
  },
  "case_id": "GO_biological_process_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "H6",
      "H7",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IPA1 (Transcriptional adapter 1-2, Ada1-2) is directly annotated with GO:0006357 'regulation of transcription by RNA polymerase II' via IBA:GO_Central (evidence C7/H7). The function comment (C5/H6) confirms the protein is a component of the SAGA transcriptional regulatory complex that activates transcription by remodeling chromatin and mediating histone acetylation. The GO term definition (GO1) matches the option text exactly. Multiple experimental references (PubMed 16980620, 21764853, 24493646, 30559249) support the SAGA complex's role in transcription activation."
  },
  "important_caveats": [
    "The GO:0006357 annotation is via IBA:GO_Central (inferred by biological aspect), not a direct experimental annotation on this protein itself, though the SAGA complex function is well-supported by multiple experimental studies.",
    "WD40 repeats are found in proteins with diverse functions; the inference relies on the combination of WD40 + small adapter size + NLS + absence of other catalytic/regulatory domains, which is a probabilistic family-level pattern rather than a deterministic rule.",
    "The reviewer-only evidence confirms identity as Q8IPA1 (Ada1-2, Drosophila), but this accession was not available to the evaluated model; the reasoning must rely on sequence features and transferable knowledge from homologs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different biological processes (transcription regulation, protein catabolism, DNA damage checkpoint, interspecies interaction). The WD40 adapter architecture with NLS and absence of kinase, protease, or pathogen-effector domains clearly favors transcriptional regulation over the other three alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IPA1 (Transcriptional adapter 1-2, Ada1-2) is directly annotated with GO:0006357 'regulation of transcription by RNA polymerase II' via IBA:GO_Central (evidence C7/H7). The function comment (C5/H6) confirms the protein is a component of the SAGA transcriptional regulatory complex that activates transcription by remodeling chromatin and mediating histone acetylation. The GO term definition (GO1) matches the option text exactly. Multiple experimental references (PubMed 16980620, 21764853, 24493646, 30559249) support the SAGA complex's role in transcription activation.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "C9", "C10", "C11", "H6", "H7", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 308-aa sequence contains WD40 repeat signatures: the 'IGSH' dipeptide near the C-terminus (G followed by H is the canonical WD40 repeat-ending motif), alternating hydrophobic residues forming beta-propeller blades, and a 'RRKR' region resembling a bipartite nuclear localization signal. From well-characterized homologs (yeast Ada1, human Ada1, TAF proteins), WD40-repeat adapter proteins of this size (~250-350 aa) with NLS-like motifs are overwhelmingly associated with transcriptional co-activator complexes (SAGA, Mediator, TFIIH) rather than DNA damage checkpoint signaling (which requires kinase/FHA/BRCT domains absent here), protein catabolic regulation (which requires protease/deubiquitinase/proteasome-interaction domains absent here), or interspecies modulation (which requires pathogen-effector or immune-evasion architectures absent here). The absence of kinase domains rules out C; the absence of proteolytic or ubiquitin-removal catalytic motifs rules out B; the nuclear/chromatin-associated architecture rules out D. The WD40 adapter + NLS + small size pattern learned from Ada1-family proteins across species meaningfully distinguishes option A.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the WD40 repeat architecture, note the nuclear localization signal, observe the absence of kinase/BRCT/protease domains, and apply transferable knowledge from Ada1, TAF, and other WD40 transcriptional adapter proteins to conclude this protein participates in transcription regulation by RNA Pol II. The distractors (B, C, D) require domain architectures or functional contexts clearly absent from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different biological processes (transcription regulation, protein catabolism, DNA damage checkpoint, interspecies interaction). The WD40 adapter architecture with NLS and absence of kinase, protease, or pathogen-effector domains clearly favors transcriptional regulation over the other three alternatives."
  },
  "important_caveats": [
    "The GO:0006357 annotation is via IBA:GO_Central (inferred by biological aspect), not a direct experimental annotation on this protein itself, though the SAGA complex function is well-supported by multiple experimental studies.",
    "WD40 repeats are found in proteins with diverse functions; the inference relies on the combination of WD40 + small adapter size + NLS + absence of other catalytic/regulatory domains, which is a probabilistic family-level pattern rather than a deterministic rule.",
    "The reviewer-only evidence confirms identity as Q8IPA1 (Ada1-2, Drosophila), but this accession was not available to the evaluated model; the reasoning must rely on sequence features and transferable knowledge from homologs."
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
  "benchmark_sequence_length": 308,
  "benchmark_sequence_sha256": "1d9917a21c4cade4f635f32453cfa7d8c133a4e80ba749a31492043a52bd7f9e",
  "current_entry_audit": {
    "entryVersion": 171,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 308,
  "current_source_sequence_sha256": "1d9917a21c4cade4f635f32453cfa7d8c133a4e80ba749a31492043a52bd7f9e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 169,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IPA1",
  "selected_historical_entry_version": 169,
  "selected_historical_record_sha256": "87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a",
  "selected_historical_source_sequence_length": 308,
  "selected_historical_source_sequence_sha256": "1d9917a21c4cade4f635f32453cfa7d8c133a4e80ba749a31492043a52bd7f9e",
  "selected_historical_version": {
    "accession": "Q8IPA1",
    "database": "Swiss-Prot",
    "entryVersion": 169,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TAD12_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IPA1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":171,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0051866\",\"source\":\"FlyBase\"}],\"value\":\"Transcriptional adapter 1-2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16980620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21764853\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24493646\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30559249\",\"source\":\"PubMed\"}],\"value\":\"Component of the transcription regulatory complex SAGA, a multiprotein complex that activates transcription by remodeling chromatin and mediating histone acetylation and deubiquitination (PubMed:16980620, PubMed:21764853, PubMed:24493646, PubMed:30559249). The SAGA complex predominantly acetylates histone H3 (PubMed:30559249)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33004486\",\"source\":\"PubMed\"}],\"id\":\"GO:0045893\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:positive regulation of DNA-templated transcription\"},{\"key\":\"GoEvidenceType\",\"value\":\"NAS:ComplexPortal\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/30",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0006357\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:regulation of transcription by RNA polymerase II\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/31",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Guelman S.\",\"Suganuma T.\",\"Florens L.\",\"Weake V.\",\"Swanson S.K.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16980620\"},{\"database\":\"DOI\",\"id\":\"10.1128/mcb.00130-06\"}],\"citationType\":\"journal article\",\"firstPage\":\"7178\",\"id\":\"16980620\",\"journal\":\"Mol. Cell. Biol.\",\"lastPage\":\"7189\",\"publicationDate\":\"2006\",\"title\":\"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA required for histone H3 acetylation.\",\"volume\":\"26\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"INTERACTION WITH GCN5; SPT3 AND ADA2B\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Dyer J.O.\",\"Seidel C.\",\"Box A.\",\"Swanson S.K.\",\"Peak A.\",\"Florens L.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21764853\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.2046211\"}],\"citationType\":\"journal article\",\"firstPage\":\"1499\",\"id\":\"21764853\",\"journal\":\"Genes Dev.\",\"lastPage\":\"1509\",\"publicationDate\":\"2011\",\"title\":\"Post-transcription initiation function of the ubiquitous SAGA complex in tissue-specific gene activation.\",\"volume\":\"25\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"DEVELOPMENTAL STAGE\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Mohan R.D.\",\"Dialynas G.\",\"Weake V.M.\",\"Liu J.\",\"Martin-Brown S.\",\"Florens L.\",\"Washburn M.P.\",\"Workman J.L.\",\"Abmayr S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24493646\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.225151.113\"}],\"citationType\":\"journal article\",\"firstPage\":\"259\",\"id\":\"24493646\",\"journal\":\"Genes Dev.\",\"lastPage\":\"272\",\"publicationDate\":\"2014\",\"title\":\"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination and leads to neural and retinal degeneration.\",\"volume\":\"28\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Torres-Zelada E.F.\",\"Stephenson R.E.\",\"Alpsoy A.\",\"Anderson B.D.\",\"Swanson S.K.\",\"Florens L.\",\"Dykhuizen E.C.\",\"Washburn M.P.\",\"Weake V.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30559249\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.214072\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30559249\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"The Drosophila Dbf4 ortholog Chiffon forms a complex with Gcn5 that is necessary for histone acetylation and viability.\",\"volume\":\"132\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:32:17.256572+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPA1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)

```json
{
  "entry_version": 169,
  "evidence_id": "H1",
  "excerpt": "ID   TAD12_DROME             Reviewed;         308 AA.\nAC   Q8IPA1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 169.\nDE   RecName: Full=Transcriptional adapter 1-2 {ECO:0000312|FlyBase:FBgn0051866};\nGN   Name=Ada1-2 {ECO:0000312|FlyBase:FBgn0051866};\nGN   Synonyms=Ada1 {ECO:0000303|PubMed:16980620},\nGN   Ada2 {ECO:0000312|EMBL:AAN10793.1};\nGN   ORFNames=CG31866 {ECO:0000312|FlyBase:FBgn0051866};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.664157+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a",
  "url": "https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)

```json
{
  "entry_version": 169,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, INTERACTION WITH GCN5; SPT3 AND\nRP   ADA2B, AND IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=16980620; DOI=10.1128/mcb.00130-06;\nRA   Guelman S., Suganuma T., Florens L., Weake V., Swanson S.K., Washburn M.P.,\nRA   Abmayr S.M., Workman J.L.;\nRT   \"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA\nRT   required for histone H3 acetylation.\";\nRL   Mol. Cell. Biol. 26:7178-7189(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.664157+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a",
  "url": "https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)

```json
{
  "entry_version": 169,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, DEVELOPMENTAL STAGE, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=21764853; DOI=10.1101/gad.2046211;\nRA   Weake V.M., Dyer J.O., Seidel C., Box A., Swanson S.K., Peak A.,\nRA   Florens L., Washburn M.P., Abmayr S.M., Workman J.L.;\nRT   \"Post-transcription initiation function of the ubiquitous SAGA complex in\nRT   tissue-specific gene activation.\";\nRL   Genes Dev. 25:1499-1509(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.664157+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a",
  "url": "https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)

```json
{
  "entry_version": 169,
  "evidence_id": "H4",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, SUBCELLULAR LOCATION, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=24493646; DOI=10.1101/gad.225151.113;\nRA   Mohan R.D., Dialynas G., Weake V.M., Liu J., Martin-Brown S., Florens L.,\nRA   Washburn M.P., Workman J.L., Abmayr S.M.;\nRT   \"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination\nRT   and leads to neural and retinal degeneration.\";\nRL   Genes Dev. 28:259-272(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.664157+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a",
  "url": "https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)

```json
{
  "entry_version": 169,
  "evidence_id": "H5",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, AND IDENTIFICATION BY MASS\nRP   SPECTROMETRY.\nRX   PubMed=30559249; DOI=10.1242/jcs.214072;\nRA   Torres-Zelada E.F., Stephenson R.E., Alpsoy A., Anderson B.D.,\nRA   Swanson S.K., Florens L., Dykhuizen E.C., Washburn M.P., Weake V.M.;\nRT   \"The Drosophila Dbf4 ortholog Chiffon forms a complex with Gcn5 that is\nRT   necessary for histone acetylation and viability.\";\nRL   J. Cell Sci. 132:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.664157+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a",
  "url": "https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)

```json
{
  "entry_version": 169,
  "evidence_id": "H6",
  "excerpt": "CC   -!- FUNCTION: Component of the transcription regulatory complex SAGA, a\nCC       multiprotein complex that activates transcription by remodeling\nCC       chromatin and mediating histone acetylation and deubiquitination\nCC       (PubMed:16980620, PubMed:21764853, PubMed:24493646, PubMed:30559249).\nCC       The SAGA complex predominantly acetylates histone H3 (PubMed:30559249).\nCC       {ECO:0000269|PubMed:16980620, ECO:0000269|PubMed:21764853,\nCC       ECO:0000269|PubMed:24493646, ECO:0000269|PubMed:30559249}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.664157+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a",
  "url": "https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)

```json
{
  "entry_version": 169,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0006357; P:regulation of transcription by RNA polymerase II; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.664157+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 169-169",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a",
  "url": "https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006357\nname: regulation of transcription by RNA polymerase II\nnamespace: biological_process\nalt_id: GO:0006358\nalt_id: GO:0010551\ndef: \"Any process that modulates the frequency, rate or extent of transcription mediated by RNA polymerase II.\" [GOC:curators, GOC:txnOH]\nsynonym: \"global transcription regulation from Pol II promoter\" RELATED []\nsynonym: \"regulation of gene-specific transcription from RNA polymerase II promoter\" RELATED []\nsynonym: \"regulation of global transcription from Pol II promoter\" RELATED []\nsynonym: \"regulation of transcription from Pol II promoter\" EXACT []\nsynonym: \"regulation of transcription from RNA polymerase II promoter\" EXACT []\nsynonym: \"regulation of transcription from RNA polymerase II promoter, global\" RELATED []\nxref: Reactome:R-HSA-8864260 \"Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors\"\nis_a: GO:0006355 ! regulation of DNA-templated transcription\nrelationship: regulates GO:0006366 ! transcription by RNA polymerase II\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006357",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 65427-65443",
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
  "excerpt": "[Term]\nid: GO:0035821\nname: modulation of process of another organism\nnamespace: biological_process\ndef: \"A process in which an organism effects a change in a biological process in another organism.\" [GOC:bf]\nsynonym: \"modification of morphology or physiology of other organism\" EXACT []\nsynonym: \"modulation of process of other organism\" EXACT []\nsynonym: \"regulation of morphology of other organism\" NARROW [GOC:bf]\nsynonym: \"regulation of morphology or physiology of other organism\" RELATED [GOC:bf]\nsynonym: \"regulation of physiological process of other organism\" NARROW [GOC:bf]\nsynonym: \"regulation of physiology of other organism\" NARROW [GOC:bf]\nis_a: GO:0044419 ! biological process involved in interspecies interaction between organisms\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0035821",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 221582-221594",
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
  "excerpt": "[Term]\nid: GO:0042177\nname: negative regulation of protein catabolic process\nnamespace: biological_process\nalt_id: GO:1903363\nalt_id: GO:2000599\ndef: \"Any process that stops, prevents or reduces the frequency, rate or extent of protein catabolic process.\" [GO_REF:0000058, GOC:kmv, GOC:obol, GOC:TermGenie, PMID:24785082]\nsynonym: \"down regulation of cellular protein breakdown\" EXACT [GOC:TermGenie]\nsynonym: \"down regulation of cellular protein catabolic process\" EXACT [GOC:TermGenie]\nsynonym: \"down regulation of cellular protein catabolism\" EXACT [GOC:TermGenie]\nsynonym: \"down regulation of cellular protein degradation\" EXACT [GOC:TermGenie]\nsynonym: \"down regulation of protein catabolic process\" EXACT []\nsynonym: \"down-regulation of cellular protein breakdown\" EXACT [GOC:TermGenie]\nsynonym: \"down-regulation of cellular protein catabolic process\" EXACT [GOC:TermGenie]\nsynonym: \"down-regulation of cellular protein catabolism\" EXACT [GOC:TermGenie]\nsynonym: \"down-regulation of cellular protein degradation\" EXACT [GOC:TermGenie]\nsynonym: \"down-regulation of protein catabolic process\" EXACT []\nsynonym: \"downregulation of cellular protein breakdown\" EXACT [GOC:TermGenie]\nsynonym: \"downregulation of cellular protein catabolic process\" EXACT [GOC:TermGenie]\nsynonym: \"downregulation of cellular protein catabolism\" EXACT [GOC:TermGenie]\nsynonym: \"downregulation of cellular protein degradation\" EXACT [GOC:TermGenie]\nsynonym: \"downregulation of protein catabolic process\" EXACT []\nsynonym: \"inhibition of cellular protein breakdown\" NARROW [GOC:TermGenie]\nsynonym: \"inhibition of cellular protein catabolic process\" NARROW [GOC:TermGenie]\nsynonym: \"inhibition of cellular protein catabolism\" NARROW [GOC:TermGenie]\nsynonym: \"inhibition of cellular protein degradation\" NARROW [GOC:TermGenie]\nsynonym: \"inhibition of protein catabolic process\" NARROW []\nsynonym: \"negative regulation of cellular protein breakdown\" EXACT [GOC:TermGenie]\nsynonym: \"negative regulation of cellular protein catabolic process\" EXACT []\nsynonym: \"negative regulation of cellular protein catabolism\" EXACT [GOC:TermGenie]\nsynonym: \"negative regulation of cellular protein degradation\" EXACT [GOC:TermGenie]\nsynonym: \"negative regulation of protein breakdown\" EXACT []\nsynonym: \"negative regulation of protein catabolism\" EXACT []\nsynonym: \"negative regulation of protein degradation\" EXACT []\nis_a: GO:0009895 ! negative regulation of catabolic process\nis_a: GO:0042176 ! regulation of protein catabolic process\nis_a: GO:0051248 ! negative regulation of protein metabolic process\nrelationship: negatively_regulates GO:0030163 ! protein catabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042177",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 234991-235029",
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
  "excerpt": "[Term]\nid: GO:0044773\nname: mitotic DNA damage checkpoint signaling\nnamespace: biological_process\nalt_id: GO:1902402\ndef: \"A signal transduction process involved in mitotic DNA damage checkpoint.\" [GOC:mtg_cell_cycle, GOC:TermGenie]\nsynonym: \"intracellular signal transduction pathway involved in mitotic DNA damage checkpoint\" NARROW [GOC:TermGenie]\nsynonym: \"intracellular signaling cascade involved in mitotic DNA damage checkpoint\" EXACT [GOC:TermGenie]\nsynonym: \"intracellular signaling pathway involved in mitotic DNA damage checkpoint\" RELATED [GOC:TermGenie]\nsynonym: \"mitotic DNA damage checkpoint\" EXACT []\nsynonym: \"signal transduction involved in mitotic DNA damage checkpoint\" EXACT []\nis_a: GO:0000077 ! DNA damage checkpoint signaling\nis_a: GO:0044774 ! mitotic DNA integrity checkpoint signaling\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044773",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 260080-260093",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
