# GO_biological_process_0130

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0130.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — intracellular protein transport

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMKINLYKLLCFICVIFLLHKNVVRSGDNMKYNDMKGLDDLSKLNDDQVKDILGLKIDGAKERIEKLFHLIDKNNDKEITEEELNTWSSFLKNEIFLKQVQAEMGQIDSDKDGFISLNELNDAFAQNLDAKEVEKHSEGLLKRFQIVDKDKDGKLSINEVGLLIDPMKDEELKELEINEILEHHDVNKDGKISLDEFKQTRSDESSGVKKDDEMALDDFNFFDANKDGFIDKEEIIKVYFDPAHESGAINVNEIKENIFEGKKITYDLWNEKALKIAVTSLTDYGDVIRYPEDFKLDIGKNVILPTARSRAFEDDDMDADNTEDDKDEADDASQQKSPAIDEL

[Multiple Choices]
A. negative regulation of neuron projection development
B. intracellular protein transport
C. negative regulation of induction of conjugation with cellular fusion
D. G protein-coupled receptor signaling pathway
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

> The sequence-matched UniProt record assigns GO:0006886, intracellular protein transport, to this protein. The assignment is supported as a database annotation, though its TAS:GeneDB evidence is not itself direct experimental proof that this is the protein's primary process.

Citations as saved: [C6](#evidence-c6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic signal-peptide-like region and repeated calcium-binding EF-hand-like motifs are consistent with a secretory-pathway/ER calcium-binding protein. Transferable knowledge of such proteins makes an intracellular trafficking or protein-handling role a plausible choice among these options; neuron projection development, conjugation, and GPCR signaling fit the sequence features much less well.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence offers a credible, probabilistic basis for preferring the broad intracellular transport option over the conspicuously less compatible alternatives. It does not independently establish that transport is the protein's primary process, and the inference is less specific than the recorded GO annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based inference favors B among the offered choices; no other option is comparably supported by the sequence features.


### Important caveats

- The supplied GO annotation is database evidence, not by itself proof of an experimentally established primary function.
- A signal peptide and EF-hand-like motifs suggest secretory-pathway calcium binding but do not alone prove a role in intracellular protein transport.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal-peptide-like region and repeated calcium-binding EF-hand-like motifs are consistent with a secretory-pathway/ER calcium-binding protein. Transferable knowledge of such proteins makes an intracellular trafficking or protein-handling role a plausible choice among these options; neuron projection development, conjugation, and GPCR signaling fit the sequence features much less well.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a credible, probabilistic basis for preferring the broad intracellular transport option over the conspicuously less compatible alternatives. It does not independently establish that transport is the protein's primary process, and the inference is less specific than the recorded GO annotation."
  },
  "case_id": "GO_biological_process_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns GO:0006886, intracellular protein transport, to this protein. The assignment is supported as a database annotation, though its TAS:GeneDB evidence is not itself direct experimental proof that this is the protein's primary process."
  },
  "important_caveats": [
    "The supplied GO annotation is database evidence, not by itself proof of an experimentally established primary function.",
    "A signal peptide and EF-hand-like motifs suggest secretory-pathway calcium binding but do not alone prove a role in intracellular protein transport."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference favors B among the offered choices; no other option is comparably supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns GO:0006886, intracellular protein transport, to this protein. The assignment is supported as a database annotation, though its TAS:GeneDB evidence is not itself direct experimental proof that this is the protein's primary process.",
    "evidence_ids": ["C6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal-peptide-like region and repeated calcium-binding EF-hand-like motifs are consistent with a secretory-pathway/ER calcium-binding protein. Transferable knowledge of such proteins makes an intracellular trafficking or protein-handling role a plausible choice among these options; neuron projection development, conjugation, and GPCR signaling fit the sequence features much less well.",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a credible, probabilistic basis for preferring the broad intracellular transport option over the conspicuously less compatible alternatives. It does not independently establish that transport is the protein's primary process, and the inference is less specific than the recorded GO annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference favors B among the offered choices; no other option is comparably supported by the sequence features."
  },
  "important_caveats": [
    "The supplied GO annotation is database evidence, not by itself proof of an experimentally established primary function.",
    "A signal peptide and EF-hand-like motifs suggest secretory-pathway calcium binding but do not alone prove a role in intracellular protein transport."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q8IIR7, PfERC) annotates this protein with GO:0006886 (intracellular protein transport) via TAS:GeneDB evidence (C6, H7). The protein is an ER-resident calcium-binding protein of the CREC family, experimentally shown to be required for proteolytic maturation of egress proteins (AMA-1, SUB1, PMX) and breakdown of the parasitophorous vacuole membrane (PubMed:32098818). Its ER residency and role in processing/trafficking secretory proteins are consistent with the broad GO term 'intracellular protein transport.' The evidence code is a Traceable Author Statement from GeneDB (a database curation annotation) rather than a direct experimental assay of transport per se, but it is consistent with the protein's demonstrated function in the secretory/ER pathway.

Citations as saved: [C6](#evidence-c6), [H7](#evidence-h7), [C5](#evidence-c5), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'MMKINLYKLLCFICVIFLLHKNV' is a canonical hydrophobic signal peptide directing the protein to the ER/secretory pathway. This is a universally recognized feature: any protein with a cleavable signal peptide enters the secretory pathway, whose core biological process is intracellular protein transport. Additionally, the sequence contains multiple EF-hand calcium-binding motifs (repeated 'DKDGK' loops, e.g., 'DKDGKLSINEVGLLIDPMKDEELKELEINEILEHHDVNKDGKISLDEFKQTRSDESSGVKKDDEMALDDFNFFDANKDGFIDKEEIIKVYFDPAHESGAINVNEIKENIFEGKKITYDLWNEKALKIAVTSLTDYGDVIRYPEDFKLDIGKNVILPTARSRAFEDDDMDADNTEDDKDEADDASQQKSPAIDEL'), characteristic of ER-resident calcium-binding proteins (calreticulin, calnexin, CREC family) that assist protein folding and trafficking within the ER. Against the distractors: (D) GPCRs require 7 transmembrane helices, which would appear as multiple hydrophobic stretches; this sequence has only one N-terminal hydrophobic segment followed by a soluble domain, definitively excluding GPCR architecture. (A) Neuron projection development requires neural-specific domains (e.g., semaphorin, ephrin, or growth-cone-related motifs) absent here. (C) Conjugation/fusion machinery involves mating-specific proteins with no resemblance to this EF-hand-rich soluble protein. Thus, the signal peptide + EF-hand combination uniquely and credibly points to B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the clearly identifiable N-terminal signal peptide (universal indicator of ER/secretory pathway entry → intracellular protein transport) and the EF-hand calcium-binding motifs (hallmark of ER-resident trafficking/folding proteins like calreticulin and CREC family members) to select option B. The absence of 7TM architecture excludes GPCR, and the lack of neural or mating-specific features excludes A and C. This reasoning relies on transferable knowledge of signal peptides, EF-hand domains, and GPCR architecture learned from many other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The signal peptide and EF-hand motifs provide a clear, unambiguous signature pointing to ER/secretory pathway function (option B). The other options are excluded by well-established structural and functional criteria (7TM for GPCR, neural domains for neurite development, mating machinery for conjugation).


### Important caveats

- The GO annotation 'intracellular protein transport' (GO:0006886) is a broad term; the protein's experimentally demonstrated role is more specifically in proteolytic maturation during egress. However, among the four offered choices, B is the only one consistent with an ER-resident protein.
- The TAS:GeneDB evidence code indicates a database curation annotation rather than a direct experimental assay specifically measuring 'transport' as defined by GO:0006886.
- The organism (Plasmodium falciparum) is not provided in the original input, but the sequence features alone are sufficient to answer the question without organism-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MMKINLYKLLCFICVIFLLHKNV' is a canonical hydrophobic signal peptide directing the protein to the ER/secretory pathway. This is a universally recognized feature: any protein with a cleavable signal peptide enters the secretory pathway, whose core biological process is intracellular protein transport. Additionally, the sequence contains multiple EF-hand calcium-binding motifs (repeated 'DKDGK' loops, e.g., 'DKDGKLSINEVGLLIDPMKDEELKELEINEILEHHDVNKDGKISLDEFKQTRSDESSGVKKDDEMALDDFNFFDANKDGFIDKEEIIKVYFDPAHESGAINVNEIKENIFEGKKITYDLWNEKALKIAVTSLTDYGDVIRYPEDFKLDIGKNVILPTARSRAFEDDDMDADNTEDDKDEADDASQQKSPAIDEL'), characteristic of ER-resident calcium-binding proteins (calreticulin, calnexin, CREC family) that assist protein folding and trafficking within the ER. Against the distractors: (D) GPCRs require 7 transmembrane helices, which would appear as multiple hydrophobic stretches; this sequence has only one N-terminal hydrophobic segment followed by a soluble domain, definitively excluding GPCR architecture. (A) Neuron projection development requires neural-specific domains (e.g., semaphorin, ephrin, or growth-cone-related motifs) absent here. (C) Conjugation/fusion machinery involves mating-specific proteins with no resemblance to this EF-hand-rich soluble protein. Thus, the signal peptide + EF-hand combination uniquely and credibly points to B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the clearly identifiable N-terminal signal peptide (universal indicator of ER/secretory pathway entry → intracellular protein transport) and the EF-hand calcium-binding motifs (hallmark of ER-resident trafficking/folding proteins like calreticulin and CREC family members) to select option B. The absence of 7TM architecture excludes GPCR, and the lack of neural or mating-specific features excludes A and C. This reasoning relies on transferable knowledge of signal peptides, EF-hand domains, and GPCR architecture learned from many other proteins."
  },
  "case_id": "GO_biological_process_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H7",
      "C5",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q8IIR7, PfERC) annotates this protein with GO:0006886 (intracellular protein transport) via TAS:GeneDB evidence (C6, H7). The protein is an ER-resident calcium-binding protein of the CREC family, experimentally shown to be required for proteolytic maturation of egress proteins (AMA-1, SUB1, PMX) and breakdown of the parasitophorous vacuole membrane (PubMed:32098818). Its ER residency and role in processing/trafficking secretory proteins are consistent with the broad GO term 'intracellular protein transport.' The evidence code is a Traceable Author Statement from GeneDB (a database curation annotation) rather than a direct experimental assay of transport per se, but it is consistent with the protein's demonstrated function in the secretory/ER pathway."
  },
  "important_caveats": [
    "The GO annotation 'intracellular protein transport' (GO:0006886) is a broad term; the protein's experimentally demonstrated role is more specifically in proteolytic maturation during egress. However, among the four offered choices, B is the only one consistent with an ER-resident protein.",
    "The TAS:GeneDB evidence code indicates a database curation annotation rather than a direct experimental assay specifically measuring 'transport' as defined by GO:0006886.",
    "The organism (Plasmodium falciparum) is not provided in the original input, but the sequence features alone are sufficient to answer the question without organism-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide and EF-hand motifs provide a clear, unambiguous signature pointing to ER/secretory pathway function (option B). The other options are excluded by well-established structural and functional criteria (7TM for GPCR, neural domains for neurite development, mating machinery for conjugation)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q8IIR7, PfERC) annotates this protein with GO:0006886 (intracellular protein transport) via TAS:GeneDB evidence (C6, H7). The protein is an ER-resident calcium-binding protein of the CREC family, experimentally shown to be required for proteolytic maturation of egress proteins (AMA-1, SUB1, PMX) and breakdown of the parasitophorous vacuole membrane (PubMed:32098818). Its ER residency and role in processing/trafficking secretory proteins are consistent with the broad GO term 'intracellular protein transport.' The evidence code is a Traceable Author Statement from GeneDB (a database curation annotation) rather than a direct experimental assay of transport per se, but it is consistent with the protein's demonstrated function in the secretory/ER pathway.",
    "evidence_ids": ["C6", "H7", "C5", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'MMKINLYKLLCFICVIFLLHKNV' is a canonical hydrophobic signal peptide directing the protein to the ER/secretory pathway. This is a universally recognized feature: any protein with a cleavable signal peptide enters the secretory pathway, whose core biological process is intracellular protein transport. Additionally, the sequence contains multiple EF-hand calcium-binding motifs (repeated 'DKDGK' loops, e.g., 'DKDGKLSINEVGLLIDPMKDEELKELEINEILEHHDVNKDGKISLDEFKQTRSDESSGVKKDDEMALDDFNFFDANKDGFIDKEEIIKVYFDPAHESGAINVNEIKENIFEGKKITYDLWNEKALKIAVTSLTDYGDVIRYPEDFKLDIGKNVILPTARSRAFEDDDMDADNTEDDKDEADDASQQKSPAIDEL'), characteristic of ER-resident calcium-binding proteins (calreticulin, calnexin, CREC family) that assist protein folding and trafficking within the ER. Against the distractors: (D) GPCRs require 7 transmembrane helices, which would appear as multiple hydrophobic stretches; this sequence has only one N-terminal hydrophobic segment followed by a soluble domain, definitively excluding GPCR architecture. (A) Neuron projection development requires neural-specific domains (e.g., semaphorin, ephrin, or growth-cone-related motifs) absent here. (C) Conjugation/fusion machinery involves mating-specific proteins with no resemblance to this EF-hand-rich soluble protein. Thus, the signal peptide + EF-hand combination uniquely and credibly points to B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the clearly identifiable N-terminal signal peptide (universal indicator of ER/secretory pathway entry → intracellular protein transport) and the EF-hand calcium-binding motifs (hallmark of ER-resident trafficking/folding proteins like calreticulin and CREC family members) to select option B. The absence of 7TM architecture excludes GPCR, and the lack of neural or mating-specific features excludes A and C. This reasoning relies on transferable knowledge of signal peptides, EF-hand domains, and GPCR architecture learned from many other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide and EF-hand motifs provide a clear, unambiguous signature pointing to ER/secretory pathway function (option B). The other options are excluded by well-established structural and functional criteria (7TM for GPCR, neural domains for neurite development, mating machinery for conjugation)."
  },
  "important_caveats": [
    "The GO annotation 'intracellular protein transport' (GO:0006886) is a broad term; the protein's experimentally demonstrated role is more specifically in proteolytic maturation during egress. However, among the four offered choices, B is the only one consistent with an ER-resident protein.",
    "The TAS:GeneDB evidence code indicates a database curation annotation rather than a direct experimental assay specifically measuring 'transport' as defined by GO:0006886.",
    "The organism (Plasmodium falciparum) is not provided in the original input, but the sequence features alone are sufficient to answer the question without organism-specific knowledge."
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
  "benchmark_sequence_length": 343,
  "benchmark_sequence_sha256": "5aaa315c0f202540b1464349f5584d0b2d8ead010738a7162723881d6234a475",
  "current_entry_audit": {
    "entryVersion": 148,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 343,
  "current_source_sequence_sha256": "5aaa315c0f202540b1464349f5584d0b2d8ead010738a7162723881d6234a475",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 146,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IIR7",
  "selected_historical_entry_version": 146,
  "selected_historical_record_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "selected_historical_source_sequence_length": 343,
  "selected_historical_source_sequence_sha256": "5aaa315c0f202540b1464349f5584d0b2d8ead010738a7162723881d6234a475",
  "selected_historical_version": {
    "accession": "Q8IIR7",
    "database": "Swiss-Prot",
    "entryVersion": 146,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PFERC_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IIR7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":148,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9497061\",\"source\":\"PubMed\"}],\"value\":\"Pf39\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9364972\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9497061\",\"source\":\"PubMed\"}],\"value\":\"Pfs40\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23061985\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32098818\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"value\":\"Endoplasmic reticulum-resident calcium binding protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23061985\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32098818\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"value\":\"PfERC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32098818\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"value\":\"Calcium-binding protein (PubMed:9364972). Required for schizont to ring transition (PubMed:32098818). Required for the breakdown of the parasitophorous vacuole membrane during egress (PubMed:32098818). Required for the proteolytic maturation of apical membrane antigen 1 (AMA-1) during egress (PubMed:32098818). Required for the proteolytic maturation of subtilisin-like protease 1 (SUB1) during egress (PubMed:32098818). Required for the proteolytic maturation of plasmepsin X (PMX) during egress (PubMed:32098818)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000304\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"id\":\"GO:0006886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:intracellular protein transport\"},{\"key\":\"GoEvidenceType\",\"value\":\"TAS:GeneDB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"La Greca N.\",\"Hibbs A.R.\",\"Riffkin C.\",\"Foley M.\",\"Tilley L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9364972\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0166-6851(97)00134-5\"}],\"citationType\":\"journal article\",\"firstPage\":\"283\",\"id\":\"9364972\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"293\",\"publicationDate\":\"1997\",\"title\":\"Identification of an endoplasmic reticulum-resident calcium-binding protein with multiple EF-hand motifs in asexual stages of Plasmodium falciparum.\",\"volume\":\"89\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"D10\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"FCR3\"}],\"referenceNumber\":2,\"referencePositions\":[\"PROTEIN SEQUENCE OF 238-249\",\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Templeton T.J.\",\"Fujioka H.\",\"Aikawa M.\",\"Parker K.C.\",\"Kaslow D.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9497061\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0166-6851(97)00164-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"359\",\"id\":\"9497061\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"365\",\"publicationDate\":\"1997\",\"title\":\"Plasmodium falciparum Pfs40, renamed Pf39, is localized to an intracellular membrane-bound compartment and is not sexual stage-specific.\",\"volume\":\"90\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Morita M.\",\"Sanai H.\",\"Hiramoto A.\",\"Sato A.\",\"Hiraoka O.\",\"Sakura T.\",\"Kaneko O.\",\"Masuyama A.\",\"Nojima M.\",\"Wataya Y.\",\"Kim H.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23061985\"},{\"database\":\"DOI\",\"id\":\"10.1021/pr3005315\"}],\"citationType\":\"journal article\",\"firstPage\":\"5704\",\"id\":\"23061985\",\"journal\":\"J. Proteome Res.\",\"lastPage\":\"5711\",\"publicationDate\":\"2012\",\"title\":\"Plasmodium falciparum endoplasmic reticulum-resident calcium binding protein is a possible target of synthetic antimalarial endoperoxides, N-89 and N-251.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23061985\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"FCR3\"}],\"referenceNumber\":4,\"referencePositions\":[\"IDENTIFICATION BY MASS SPECTROMETRY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Fierro M.A.\",\"Asady B.\",\"Brooks C.F.\",\"Cobb D.W.\",\"Villegas A.\",\"Moreno S.N.J.\",\"Muralidharan V.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32098818\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.03078-19\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"32098818\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2020\",\"title\":\"An Endoplasmic Reticulum CREC Family Protein Regulates the Egress Proteolytic Cascade in Malaria Parasites.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H1",
  "excerpt": "ID   PFERC_PLAF7             Reviewed;         343 AA.\nAC   Q8IIR7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 146.\nDE   RecName: Full=Endoplasmic reticulum-resident calcium binding protein {ECO:0000303|PubMed:23061985, ECO:0000303|PubMed:32098818, ECO:0000303|PubMed:9364972};\nDE            Short=PfERC {ECO:0000303|PubMed:23061985, ECO:0000303|PubMed:32098818, ECO:0000303|PubMed:9364972};\nDE   AltName: Full=Pf39 {ECO:0000303|PubMed:9497061};\nDE   AltName: Full=Pfs40 {ECO:0000303|PubMed:9364972, ECO:0000303|PubMed:9497061};\nDE   Flags: Precursor;\nGN   Name=ERC {ECO:0000305};\nGN   ORFNames=PF3D7_1108600 {ECO:0000312|EMBL:CZT98752.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   PROTEIN SEQUENCE OF 238-249, FUNCTION, SUBCELLULAR LOCATION, AND\nRP   DEVELOPMENTAL STAGE.\nRC   STRAIN=D10 {ECO:0000303|PubMed:9364972}, and\nRC   FCR3 {ECO:0000303|PubMed:9364972};\nRX   PubMed=9364972; DOI=10.1016/s0166-6851(97)00134-5;\nRA   La Greca N., Hibbs A.R., Riffkin C., Foley M., Tilley L.;\nRT   \"Identification of an endoplasmic reticulum-resident calcium-binding\nRT   protein with multiple EF-hand motifs in asexual stages of Plasmodium\nRT   falciparum.\";\nRL   Mol. Biochem. Parasitol. 89:283-293(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   SUBCELLULAR LOCATION, AND DEVELOPMENTAL STAGE.\nRX   PubMed=9497061; DOI=10.1016/s0166-6851(97)00164-3;\nRA   Templeton T.J., Fujioka H., Aikawa M., Parker K.C., Kaslow D.C.;\nRT   \"Plasmodium falciparum Pfs40, renamed Pf39, is localized to an\nRT   intracellular membrane-bound compartment and is not sexual stage-\nRT   specific.\";\nRL   Mol. Biochem. Parasitol. 90:359-365(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   IDENTIFICATION BY MASS SPECTROMETRY, AND SUBCELLULAR LOCATION.\nRC   STRAIN=FCR3 {ECO:0000303|PubMed:23061985};\nRX   PubMed=23061985; DOI=10.1021/pr3005315;\nRA   Morita M., Sanai H., Hiramoto A., Sato A., Hiraoka O., Sakura T.,\nRA   Kaneko O., Masuyama A., Nojima M., Wataya Y., Kim H.S.;\nRT   \"Plasmodium falciparum endoplasmic reticulum-resident calcium binding\nRT   protein is a possible target of synthetic antimalarial endoperoxides, N-89\nRT   and N-251.\";\nRL   J. Proteome Res. 11:5704-5711(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H5",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32098818; DOI=10.1128/mbio.03078-19;\nRA   Fierro M.A., Asady B., Brooks C.F., Cobb D.W., Villegas A., Moreno S.N.J.,\nRA   Muralidharan V.;\nRT   \"An Endoplasmic Reticulum CREC Family Protein Regulates the Egress\nRT   Proteolytic Cascade in Malaria Parasites.\";\nRL   MBio 11:0-0(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H6",
  "excerpt": "CC   -!- FUNCTION: Calcium-binding protein (PubMed:9364972). Required for\nCC       schizont to ring transition (PubMed:32098818). Required for the\nCC       breakdown of the parasitophorous vacuole membrane during egress\nCC       (PubMed:32098818). Required for the proteolytic maturation of apical\nCC       membrane antigen 1 (AMA-1) during egress (PubMed:32098818). Required\nCC       for the proteolytic maturation of subtilisin-like protease 1 (SUB1)\nCC       during egress (PubMed:32098818). Required for the proteolytic\nCC       maturation of plasmepsin X (PMX) during egress (PubMed:32098818).\nCC       {ECO:0000269|PubMed:32098818, ECO:0000269|PubMed:9364972}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0006886; P:intracellular protein transport; TAS:GeneDB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006886\nname: intracellular protein transport\nnamespace: biological_process\nalt_id: GO:0032779\ndef: \"The directed movement of proteins in a cell, including the movement of proteins between specific compartments or structures within a cell, such as organelles of a eukaryotic cell.\" [GOC:mah]\nsubset: goslim_generic\nsubset: goslim_prokaryote\nsynonym: \"copper-induced intracellular protein transport\" RELATED [GOC:al]\nis_a: GO:0015031 ! protein transport\nis_a: GO:0046907 ! intracellular transport\nrelationship: part_of GO:0008104 ! intracellular protein localization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 71242-71254",
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
  "excerpt": "[Term]\nid: GO:0007186\nname: G protein-coupled receptor signaling pathway\nnamespace: biological_process\nalt_id: GO:0038042\ndef: \"The series of molecular signals initiated by a ligand binding to its receptor, in which the activated receptor promotes the exchange of GDP for GTP on the alpha-subunit of an associated heterotrimeric G-protein complex. The GTP-bound activated alpha-G-protein then dissociates from the beta- and gamma-subunits to further transmit the signal within the cell. The pathway begins with receptor-ligand interaction, and ends with regulation of a downstream cellular process. The pathway can start from the plasma membrane, Golgi or nuclear membrane.\" [GOC:bf, GOC:mah, PMID:16902576, PMID:24568158, Wikipedia:G_protein-coupled_receptor]\nsubset: goslim_drosophila\nsynonym: \"dimeric G-protein coupled receptor signaling pathway\" NARROW []\nsynonym: \"dimeric G-protein coupled receptor signalling pathway\" NARROW [GOC:mah]\nsynonym: \"G protein coupled receptor protein signaling pathway\" EXACT []\nsynonym: \"G protein coupled receptor protein signalling pathway\" EXACT []\nsynonym: \"G-protein coupled receptor protein signal transduction\" EXACT []\nsynonym: \"G-protein coupled receptor protein signaling pathway\" EXACT [GOC:bf]\nsynonym: \"G-protein coupled receptor signaling pathway via GPCR dimer\" NARROW [GOC:bf]\nsynonym: \"G-protein coupled receptor signalling pathway\" EXACT []\nsynonym: \"G-protein-coupled receptor protein signalling pathway\" EXACT []\nsynonym: \"GPCR signaling pathway\" EXACT []\nsynonym: \"GPCR signalling pathway\" EXACT []\nxref: Reactome:R-HSA-373076 \"Class A/1 (Rhodopsin-like receptors)\"\nxref: Reactome:R-HSA-388396 \"GPCR downstream signalling\"\nis_a: GO:0007165 ! signal transduction\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007186",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 74132-74153",
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
  "excerpt": "[Term]\nid: GO:0010977\nname: negative regulation of neuron projection development\nnamespace: biological_process\ndef: \"Any process that decreases the rate, frequency or extent of neuron projection development. Neuron projection development is the process whose specific outcome is the progression of a neuron projection over time, from its formation to the mature structure. A neuron projection is any process extending from a neural cell, such as axons or dendrites (collectively called neurites).\" [GOC:dph, GOC:tb]\nsynonym: \"growth cone collapse\" RELATED [GOC:pr]\nsynonym: \"negative regulation of neurite biosynthesis\" NARROW [GOC:mah]\nsynonym: \"negative regulation of neurite development\" NARROW [GOC:mah]\nsynonym: \"negative regulation of neurite formation\" NARROW [GOC:mah]\nsynonym: \"negative regulation of neurite growth\" NARROW [GOC:mah]\nis_a: GO:0010975 ! regulation of neuron projection development\nis_a: GO:0031345 ! negative regulation of cell projection organization\nrelationship: negatively_regulates GO:0031175 ! neuron projection development\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0010977",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 110813-110826",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
