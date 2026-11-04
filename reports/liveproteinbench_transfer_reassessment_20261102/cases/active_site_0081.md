# active_site_0081

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0081.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 316 (Charge relay system)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVLTRRAALLLCPWVIQLVIKRTLAGDILPNEGKKEKDDVHKIISELRFLQKVETILESSNMSVSDVEADANAYNPDRDAPKEELQKLQDQQETPSKQPNNLRNSPQKRAEKKESPGKNKKSLRLIVSENHATSPSFFEESLLQEDVVSFIQSKGKLSNLKNLKSMIIDLNSDMTDEELAEYISLLERKGALIESDKLVGADDVSLASVKDAVRRGESSVNWGKLRSTMLEVPSGESPPSHAASSGSPFDDDDDLLSEAALHREEAHLAGSKTTKGYKFNDEYRNLQWGLDLARLDETQDLINANRVSVTKICVIDSGIDYNHPDLRNNIDVNVKELHGRKGVDDDSNGVVDDVYGANFVNNSGDPMDDNYHGTHVSGIISAVGNNGIGIVGVDGHSKLVICKALDQHKLGRLGDMFKCIDYCISRQAHMINGSFSFDEYSNIFNASVEHLRSLGILFFVSASNCAHDKLSKPDIAKCDLAVNHRYPPILSKTHNNVIAVANLKRDLDESYSLSVNSFYSNIYCQLAAPGTNIYSTTPMNNYRKLNGTSMASPHVAAIASIVRSINPNLTYLQIVEILRNAIVKLPSLTERVSWGGYVDILRAVNLAIDSKAAPYIKSHSWFRWKQGSRR

[Multiple Choices]
A. Position 176 (Proton donor)
B. Position 316 (Charge relay system)
C. Position 238 (Lowers pKa of active site Tyr)
D. Position 21 (Proton acceptor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The matched UniProt entry annotates position 316 as part of the charge relay system, supporting choice B. This annotation is based on a PROSITE computational rule rather than direct experimental evidence for that individual residue.

Citations as saved: [C5](#evidence-c5), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a subtilisin-like serine protease. Transferable knowledge of this family identifies a catalytic Asp-His-Ser charge-relay system; that makes a charge-relay role at a catalytic-domain position such as 316 more plausible than a role at position 21 in the N-terminal signal region or the distractor descriptions at the other positions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and knowledge of subtilisin catalytic mechanisms provide a meaningful basis to select B among these alternatives, even though exact residue-role assignment is not proven from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B matches the known subtilisin-like charge-relay mechanism among the offered choices.


### Important caveats

- The source annotation is computational; the supplied evidence does not establish experimental validation of the specific role at position 316.
- A subtilisin-like catalytic center contains multiple charge-relay residues, while the options ask about individual positions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a subtilisin-like serine protease. Transferable knowledge of this family identifies a catalytic Asp-His-Ser charge-relay system; that makes a charge-relay role at a catalytic-domain position such as 316 more plausible than a role at position 21 in the N-terminal signal region or the distractor descriptions at the other positions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and knowledge of subtilisin catalytic mechanisms provide a meaningful basis to select B among these alternatives, even though exact residue-role assignment is not proven from sequence alone."
  },
  "case_id": "active_site_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates position 316 as part of the charge relay system, supporting choice B. This annotation is based on a PROSITE computational rule rather than direct experimental evidence for that individual residue."
  },
  "important_caveats": [
    "The source annotation is computational; the supplied evidence does not establish experimental validation of the specific role at position 316.",
    "A subtilisin-like catalytic center contains multiple charge-relay residues, while the options ask about individual positions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B matches the known subtilisin-like charge-relay mechanism among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates position 316 as part of the charge relay system, supporting choice B. This annotation is based on a PROSITE computational rule rather than direct experimental evidence for that individual residue.",
    "evidence_ids": ["C5", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a subtilisin-like serine protease. Transferable knowledge of this family identifies a catalytic Asp-His-Ser charge-relay system; that makes a charge-relay role at a catalytic-domain position such as 316 more plausible than a role at position 21 in the N-terminal signal region or the distractor descriptions at the other positions.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and knowledge of subtilisin catalytic mechanisms provide a meaningful basis to select B among these alternatives, even though exact residue-role assignment is not proven from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B matches the known subtilisin-like charge-relay mechanism among the offered choices."
  },
  "important_caveats": [
    "The source annotation is computational; the supplied evidence does not establish experimental validation of the specific role at position 316.",
    "A subtilisin-like catalytic center contains multiple charge-relay residues, while the options ask about individual positions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Position 316 is annotated in UniProt (E6Y8B9) as 'Charge relay system' (Active site) via PROSITE-ProRule PRU01240 (evidence code ECO:0000255, inferred by similarity). The protein is confirmed as a subtilisin-like protease (EC 3.4.21.62) with multiple crystal structures (4TR2, 8COY, 8COZ, 8QKE, 8QKG) and experimentally verified catalytic activity. The charge relay system (Asp-His-Ser triad) is the canonical catalytic mechanism for subtilases, and positions 316, 372, and 549 are annotated together as the triad. The annotation is computational (pattern-based) rather than direct site-directed mutagenesis on this exact protein, but it is consistent with the experimentally confirmed subtilase family assignment and the well-established catalytic mechanism of the family.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [C4](#evidence-c4), [C36](#evidence-c36), [C37](#evidence-c37).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains subtilisin-like protease features (recognizable by the GDSGS-type serine nucleophile motif and overall domain architecture of a ~630-residue protease with a large N-terminal prodomain). Subtilases universally use an Asp-His-Ser catalytic triad described as a 'charge relay system'—this is the standard, family-specific terminology. Option B's mechanism description ('Charge relay system') matches subtilase catalysis exactly. Options A ('Proton donor') and D ('Proton acceptor') describe acid-base catalysis terminology not used for subtilase triads, and option C ('Lowers pKa of active site Tyr') refers to tyrosine-containing active sites (e.g., tyrosine kinases or specific oxidases), which are irrelevant to subtilases. Additionally, positions 21 (in the signal peptide, ~residues 1-25) and 176, 238 (within the prodomain, before the experimentally documented prodomain cleavage sites at 202-203, 243-244, 270-271) fall outside the mature catalytic domain, whereas position 316 lies in the catalytic domain after prodomain processing. A model familiar with subtilase family biology can therefore select B on both mechanism terminology and domain-position grounds.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The key discriminator is the mechanism label paired with each position. 'Charge relay system' is the universally recognized term for the subtilase Asp-His-Ser catalytic triad, learned from subtilisin Carlsberg, subtilisin BPN', and many homologs. The other three options use mechanism descriptions (proton donor/acceptor, Tyr pKa lowering) that are inconsistent with subtilase catalysis. Position-based reasoning (signal peptide vs. prodomain vs. catalytic domain) provides a second, independent line of discrimination. Both lines rely on transferable family-level knowledge, not on memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options pair distinct positions with mutually exclusive mechanism descriptions. Only 'charge relay system' is consistent with subtilase catalysis. The other three mechanism labels (proton donor, proton acceptor, Tyr pKa lowering) describe fundamentally different catalytic strategies not used by subtilases. No ambiguity arises among the offered choices.


### Important caveats

- The position 316 annotation carries evidence code ECO:0000255 (inferred by similarity via PROSITE-ProRule), meaning it is a computational pattern assignment rather than a direct mutagenesis result on this exact protein. However, the protein's identity as a subtilase and its catalytic activity are experimentally confirmed.
- The reviewer-only evidence identifies the protein as Plasmodium vivax SUB1 (E6Y8B9); this identification was not available to the evaluated model. The model must infer the subtilase family from sequence features alone.
- The three catalytic triad positions (316, 372, 549) are all annotated as 'Charge relay system'; the question asks for a single position, and only 316 appears among the options, so no ambiguity among the triad members arises within the offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains subtilisin-like protease features (recognizable by the GDSGS-type serine nucleophile motif and overall domain architecture of a ~630-residue protease with a large N-terminal prodomain). Subtilases universally use an Asp-His-Ser catalytic triad described as a 'charge relay system'—this is the standard, family-specific terminology. Option B's mechanism description ('Charge relay system') matches subtilase catalysis exactly. Options A ('Proton donor') and D ('Proton acceptor') describe acid-base catalysis terminology not used for subtilase triads, and option C ('Lowers pKa of active site Tyr') refers to tyrosine-containing active sites (e.g., tyrosine kinases or specific oxidases), which are irrelevant to subtilases. Additionally, positions 21 (in the signal peptide, ~residues 1-25) and 176, 238 (within the prodomain, before the experimentally documented prodomain cleavage sites at 202-203, 243-244, 270-271) fall outside the mature catalytic domain, whereas position 316 lies in the catalytic domain after prodomain processing. A model familiar with subtilase family biology can therefore select B on both mechanism terminology and domain-position grounds.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The key discriminator is the mechanism label paired with each position. 'Charge relay system' is the universally recognized term for the subtilase Asp-His-Ser catalytic triad, learned from subtilisin Carlsberg, subtilisin BPN', and many homologs. The other three options use mechanism descriptions (proton donor/acceptor, Tyr pKa lowering) that are inconsistent with subtilase catalysis. Position-based reasoning (signal peptide vs. prodomain vs. catalytic domain) provides a second, independent line of discrimination. Both lines rely on transferable family-level knowledge, not on memorizing this specific protein's annotation."
  },
  "case_id": "active_site_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H7",
      "H8",
      "H9",
      "C4",
      "C36",
      "C37"
    ],
    "judgment": "supported",
    "reason": "Position 316 is annotated in UniProt (E6Y8B9) as 'Charge relay system' (Active site) via PROSITE-ProRule PRU01240 (evidence code ECO:0000255, inferred by similarity). The protein is confirmed as a subtilisin-like protease (EC 3.4.21.62) with multiple crystal structures (4TR2, 8COY, 8COZ, 8QKE, 8QKG) and experimentally verified catalytic activity. The charge relay system (Asp-His-Ser triad) is the canonical catalytic mechanism for subtilases, and positions 316, 372, and 549 are annotated together as the triad. The annotation is computational (pattern-based) rather than direct site-directed mutagenesis on this exact protein, but it is consistent with the experimentally confirmed subtilase family assignment and the well-established catalytic mechanism of the family."
  },
  "important_caveats": [
    "The position 316 annotation carries evidence code ECO:0000255 (inferred by similarity via PROSITE-ProRule), meaning it is a computational pattern assignment rather than a direct mutagenesis result on this exact protein. However, the protein's identity as a subtilase and its catalytic activity are experimentally confirmed.",
    "The reviewer-only evidence identifies the protein as Plasmodium vivax SUB1 (E6Y8B9); this identification was not available to the evaluated model. The model must infer the subtilase family from sequence features alone.",
    "The three catalytic triad positions (316, 372, 549) are all annotated as 'Charge relay system'; the question asks for a single position, and only 316 appears among the options, so no ambiguity among the triad members arises within the offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options pair distinct positions with mutually exclusive mechanism descriptions. Only 'charge relay system' is consistent with subtilase catalysis. The other three mechanism labels (proton donor, proton acceptor, Tyr pKa lowering) describe fundamentally different catalytic strategies not used by subtilases. No ambiguity arises among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Position 316 is annotated in UniProt (E6Y8B9) as 'Charge relay system' (Active site) via PROSITE-ProRule PRU01240 (evidence code ECO:0000255, inferred by similarity). The protein is confirmed as a subtilisin-like protease (EC 3.4.21.62) with multiple crystal structures (4TR2, 8COY, 8COZ, 8QKE, 8QKG) and experimentally verified catalytic activity. The charge relay system (Asp-His-Ser triad) is the canonical catalytic mechanism for subtilases, and positions 316, 372, and 549 are annotated together as the triad. The annotation is computational (pattern-based) rather than direct site-directed mutagenesis on this exact protein, but it is consistent with the experimentally confirmed subtilase family assignment and the well-established catalytic mechanism of the family.",
    "evidence_ids": ["C5", "C6", "C7", "H7", "H8", "H9", "C4", "C36", "C37"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains subtilisin-like protease features (recognizable by the GDSGS-type serine nucleophile motif and overall domain architecture of a ~630-residue protease with a large N-terminal prodomain). Subtilases universally use an Asp-His-Ser catalytic triad described as a 'charge relay system'—this is the standard, family-specific terminology. Option B's mechanism description ('Charge relay system') matches subtilase catalysis exactly. Options A ('Proton donor') and D ('Proton acceptor') describe acid-base catalysis terminology not used for subtilase triads, and option C ('Lowers pKa of active site Tyr') refers to tyrosine-containing active sites (e.g., tyrosine kinases or specific oxidases), which are irrelevant to subtilases. Additionally, positions 21 (in the signal peptide, ~residues 1-25) and 176, 238 (within the prodomain, before the experimentally documented prodomain cleavage sites at 202-203, 243-244, 270-271) fall outside the mature catalytic domain, whereas position 316 lies in the catalytic domain after prodomain processing. A model familiar with subtilase family biology can therefore select B on both mechanism terminology and domain-position grounds.",
    "missing_item_specific_fact": "",
    "reason": "The key discriminator is the mechanism label paired with each position. 'Charge relay system' is the universally recognized term for the subtilase Asp-His-Ser catalytic triad, learned from subtilisin Carlsberg, subtilisin BPN', and many homologs. The other three options use mechanism descriptions (proton donor/acceptor, Tyr pKa lowering) that are inconsistent with subtilase catalysis. Position-based reasoning (signal peptide vs. prodomain vs. catalytic domain) provides a second, independent line of discrimination. Both lines rely on transferable family-level knowledge, not on memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options pair distinct positions with mutually exclusive mechanism descriptions. Only 'charge relay system' is consistent with subtilase catalysis. The other three mechanism labels (proton donor, proton acceptor, Tyr pKa lowering) describe fundamentally different catalytic strategies not used by subtilases. No ambiguity arises among the offered choices."
  },
  "important_caveats": [
    "The position 316 annotation carries evidence code ECO:0000255 (inferred by similarity via PROSITE-ProRule), meaning it is a computational pattern assignment rather than a direct mutagenesis result on this exact protein. However, the protein's identity as a subtilase and its catalytic activity are experimentally confirmed.",
    "The reviewer-only evidence identifies the protein as Plasmodium vivax SUB1 (E6Y8B9); this identification was not available to the evaluated model. The model must infer the subtilase family from sequence features alone.",
    "The three catalytic triad positions (316, 372, 549) are all annotated as 'Charge relay system'; the question asks for a single position, and only 316 appears among the options, so no ambiguity among the triad members arises within the offered choices."
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
  "benchmark_sequence_length": 630,
  "benchmark_sequence_sha256": "26d75cef4b12afe63e95e1e558255f990bc3a1fb29980dad1ff271270e9bc1c3",
  "current_entry_audit": {
    "entryVersion": 80,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-03-08",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 630,
  "current_source_sequence_sha256": "26d75cef4b12afe63e95e1e558255f990bc3a1fb29980dad1ff271270e9bc1c3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 78,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E6Y8B9",
  "selected_historical_entry_version": 78,
  "selected_historical_record_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "selected_historical_source_sequence_length": 630,
  "selected_historical_source_sequence_sha256": "26d75cef4b12afe63e95e1e558255f990bc3a1fb29980dad1ff271270e9bc1c3",
  "selected_historical_version": {
    "accession": "E6Y8B9",
    "database": "Swiss-Prot",
    "entryVersion": 78,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SUB1_PLAVI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E6Y8B9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":80,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-03-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ACT76164.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Plasmodium\"],\"scientificName\":\"Plasmodium vivax\",\"taxonId\":5855}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"PvS1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25204226\",\"source\":\"PubMed\"}],\"value\":\"PvSUB1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"SUB1 protease\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25204226\",\"source\":\"PubMed\"}],\"value\":\"Subtilase SUB1\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"3.4.21.62\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"Subtilisin-like protease 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Charge relay system\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01240\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":316},\"start\":{\"modifier\":\"EXACT\",\"value\":316}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Charge relay system\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01240\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":372},\"start\":{\"modifier\":\"EXACT\",\"value\":372}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Charge relay system\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01240\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":549},\"start\":{\"modifier\":\"EXACT\",\"value\":549}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":129},\"start\":{\"modifier\":\"EXACT\",\"value\":129}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":130},\"start\":{\"modifier\":\"EXACT\",\"value\":130}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":133},\"start\":{\"modifier\":\"EXACT\",\"value\":133}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":135},\"start\":{\"modifier\":\"EXACT\",\"value\":135}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":190},\"start\":{\"modifier\":\"EXACT\",\"value\":190}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":281},\"start\":{\"modifier\":\"EXACT\",\"value\":281}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":325},\"start\":{\"modifier\":\"EXACT\",\"value\":325}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":336},\"start\":{\"modifier\":\"EXACT\",\"value\":336}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":336},\"start\":{\"modifier\":\"EXACT\",\"value\":336}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":340},\"start\":{\"modifier\":\"EXACT\",\"value\":340}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/22",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":343},\"start\":{\"modifier\":\"EXACT\",\"value\":343}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/23",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":344},\"start\":{\"modifier\":\"EXACT\",\"value\":344}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/24",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":345},\"start\":{\"modifier\":\"EXACT\",\"value\":345}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/25",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":346},\"start\":{\"modifier\":\"EXACT\",\"value\":346}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/26",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":348},\"start\":{\"modifier\":\"EXACT\",\"value\":348}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/27",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":350},\"start\":{\"modifier\":\"EXACT\",\"value\":350}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/28",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":352},\"start\":{\"modifier\":\"EXACT\",\"value\":352}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/29",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":353},\"start\":{\"modifier\":\"EXACT\",\"value\":353}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/30",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":383},\"start\":{\"modifier\":\"EXACT\",\"value\":383}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/31",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C27",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":386},\"start\":{\"modifier\":\"EXACT\",\"value\":386}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/32",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C28",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":388},\"start\":{\"modifier\":\"EXACT\",\"value\":388}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/33",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C29",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":390},\"start\":{\"modifier\":\"EXACT\",\"value\":390}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/34",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C30

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C30",
  "excerpt": "{\"description\":\"Cleavage\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":203},\"start\":{\"modifier\":\"EXACT\",\"value\":202}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/35",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C31

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C31",
  "excerpt": "{\"description\":\"Cleavage\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":244},\"start\":{\"modifier\":\"EXACT\",\"value\":243}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/36",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C32

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C32",
  "excerpt": "{\"description\":\"Cleavage\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":271},\"start\":{\"modifier\":\"EXACT\",\"value\":270}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/37",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C33

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C33",
  "excerpt": "{\"description\":\"Cleavage\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":358},\"start\":{\"modifier\":\"EXACT\",\"value\":357}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/38",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C34

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C34",
  "excerpt": "{\"citation\":{\"authors\":[\"Bouillon A.\",\"Giganti D.\",\"Benedet C.\",\"Gorgette O.\",\"Petres S.\",\"Crublet E.\",\"Girard-Blanc C.\",\"Witkowski B.\",\"Menard D.\",\"Nilges M.\",\"Mercereau-Puijalon O.\",\"Stoven V.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23653352\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m113.456764\"}],\"citationType\":\"journal article\",\"firstPage\":\"18561\",\"id\":\"23653352\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"18573\",\"publicationDate\":\"2013\",\"title\":\"In Silico screening on the three-dimensional model of the Plasmodium vivax SUB1 protease leads to the validation of a novel anti-parasite compound.\",\"volume\":\"288\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"DEVELOPMENTAL STAGE\",\"PROTEOLYTIC CLEAVAGE\",\"CLEAVAGE SITES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C35

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C35",
  "excerpt": "{\"citation\":{\"authors\":[\"Martinez M.\",\"Bouillon A.\",\"Brule S.\",\"Raynal B.\",\"Haouz A.\",\"Alzari P.M.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38386597\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.00198-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0019824\",\"id\":\"38386597\",\"journal\":\"MBio\",\"lastPage\":\"e0019824\",\"publicationDate\":\"2024\",\"title\":\"Prodomain-driven enzyme dimerization: a pH-dependent autoinhibition mechanism that controls Plasmodium Sub1 activity before merozoite egress.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C36

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C36",
  "excerpt": "{\"citation\":{\"authors\":[\"Giganti D.\",\"Bouillon A.\",\"Tawk L.\",\"Robert F.\",\"Martinez M.\",\"Crublet E.\",\"Weber P.\",\"Girard-Blanc C.\",\"Petres S.\",\"Haouz A.\",\"Hernandez J.F.\",\"Mercereau-Puijalon O.\",\"Alzari P.M.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25204226\"},{\"database\":\"DOI\",\"id\":\"10.1038/ncomms5833\"}],\"citationType\":\"journal article\",\"firstPage\":\"4833\",\"id\":\"25204226\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"4833\",\"publicationDate\":\"2014\",\"title\":\"A novel Plasmodium-specific prodomain fold regulates the malaria drug target SUB1 subtilase.\",\"volume\":\"5\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"}],\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) OF 26-630 IN COMPLEX WITH CALCIUM\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"SUBUNIT\",\"PROTEOLYTIC CLEAVAGE\",\"CLEAVAGE SITE\",\"DISULFIDE BONDS\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C37

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C37",
  "excerpt": "{\"citation\":{\"authors\":[\"Martinez M.\",\"Batista F.A.\",\"Maurel M.\",\"Bouillon A.\",\"Ortega Varga L.\",\"Wehenkel A.M.\",\"Le Chevalier-Sontag L.\",\"Blondel A.\",\"Haouz A.\",\"Hernandez J.F.\",\"Alzari P.M.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37428845\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2059798323004710\"}],\"citationType\":\"journal article\",\"firstPage\":\"721\",\"id\":\"37428845\",\"journal\":\"Acta Crystallogr. D Struct. Biol.\",\"lastPage\":\"734\",\"publicationDate\":\"2023\",\"title\":\"3D structures of the Plasmodium vivax subtilisin-like drug target SUB1 reveal conformational changes to accommodate a substrate-derived alpha-ketoamide inhibitor.\",\"volume\":\"79\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"}],\"referenceNumber\":6,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.44 ANGSTROMS) OF 273-617 IN COMPLEX WITH CA(2+) AND PEPTIDE INHIBITOR\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PROTEOLYTIC CLEAVAGE\",\"GLYCOSYLATION\",\"GLYCOSYLATION AT ASN-546\",\"DISULFIDE BONDS\",\"MUTAGENESIS OF ASN-361; ASN-432 AND ASN-445\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C38

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C38",
  "excerpt": "{\"citation\":{\"authors\":[\"Legru A.\",\"Batista F.A.\",\"Puszko A.K.\",\"Bouillon A.\",\"Maurel M.\",\"Martinez M.\",\"Ejjoummany A.\",\"Ortega Varga L.\",\"Adler P.\",\"Mechaly A.\",\"Hadjadj M.\",\"Sosnowski P.\",\"Hopfgartner G.\",\"Alzari P.M.\",\"Blondel A.\",\"Haouz A.\",\"Barale J.C.\",\"Hernandez J.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38503166\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ejmech.2024.116308\"}],\"citationType\":\"journal article\",\"firstPage\":\"116308\",\"id\":\"38503166\",\"journal\":\"Eur. J. Med. Chem.\",\"lastPage\":\"116308\",\"publicationDate\":\"2024\",\"title\":\"Insights from structure-activity relationships and the binding mode of peptidic alpha-ketoamide inhibitors of the malaria drug target subtilisin-like SUB1.\",\"volume\":\"269\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"referenceNumber\":7,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.50 ANGSTROMS) OF 26-630 IN COMPLEX WITH CA(2+) AND PEPTIDE INHIBITORS\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"GLYCOSYLATION AT ASN-546\",\"DISULFIDE BONDS\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H1",
  "excerpt": "ID   SUB1_PLAVI              Reviewed;         630 AA.\nAC   E6Y8B9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-MAR-2011, sequence version 1.\nDT   28-JAN-2026, entry version 78.\nDE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};\nDE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226, ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597, ECO:0000269|PubMed:38503166};\nDE   AltName: Full=PvS1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};\nDE   AltName: Full=PvSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:25204226};\nDE   AltName: Full=SUB1 protease {ECO:0000303|PubMed:38503166};\nDE   AltName: Full=Subtilase SUB1 {ECO:0000303|PubMed:25204226};\nDE   Flags: Precursor;\nGN   Name=sub1 {ECO:0000312|EMBL:ACT76164.1};\nGN   ORFNames=PVC01_100035100 {ECO:0000312|EMBL:SCO73277.1},\nGN   PVT01_100029100 {ECO:0000312|EMBL:SCO67822.1},\nGN   PVW1_100050600 {ECO:0000312|EMBL:CAG9475055.1};\nOS   Plasmodium vivax.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).\nOX   NCBI_TaxID=5855 {ECO:0000312|EMBL:ACT76164.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, SUBUNIT, DEVELOPMENTAL STAGE, PROTEOLYTIC CLEAVAGE, AND\nRP   CLEAVAGE SITES.\nRX   PubMed=23653352; DOI=10.1074/jbc.m113.456764;\nRA   Bouillon A., Giganti D., Benedet C., Gorgette O., Petres S., Crublet E.,\nRA   Girard-Blanc C., Witkowski B., Menard D., Nilges M., Mercereau-Puijalon O.,\nRA   Stoven V., Barale J.C.;\nRT   \"In Silico screening on the three-dimensional model of the Plasmodium vivax\nRT   SUB1 protease leads to the validation of a novel anti-parasite compound.\";\nRL   J. Biol. Chem. 288:18561-18573(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRX   PubMed=38386597; DOI=10.1128/mbio.00198-24;\nRA   Martinez M., Bouillon A., Brule S., Raynal B., Haouz A., Alzari P.M.,\nRA   Barale J.C.;\nRT   \"Prodomain-driven enzyme dimerization: a pH-dependent autoinhibition\nRT   mechanism that controls Plasmodium Sub1 activity before merozoite egress.\";\nRL   MBio 15:e0019824-e0019824(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H4",
  "excerpt": "RN   [5] {ECO:0007744|PDB:4TR2}\nRP   X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) OF 26-630 IN COMPLEX WITH CALCIUM,\nRP   CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, SUBUNIT, PROTEOLYTIC\nRP   CLEAVAGE, CLEAVAGE SITE, AND DISULFIDE BONDS.\nRX   PubMed=25204226; DOI=10.1038/ncomms5833;\nRA   Giganti D., Bouillon A., Tawk L., Robert F., Martinez M., Crublet E.,\nRA   Weber P., Girard-Blanc C., Petres S., Haouz A., Hernandez J.F.,\nRA   Mercereau-Puijalon O., Alzari P.M., Barale J.C.;\nRT   \"A novel Plasmodium-specific prodomain fold regulates the malaria drug\nRT   target SUB1 subtilase.\";\nRL   Nat. Commun. 5:4833-4833(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H5",
  "excerpt": "RN   [6] {ECO:0007744|PDB:8COY, ECO:0007744|PDB:8COZ}\nRP   X-RAY CRYSTALLOGRAPHY (1.44 ANGSTROMS) OF 273-617 IN COMPLEX WITH CA(2+)\nRP   AND PEPTIDE INHIBITOR, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PROTEOLYTIC\nRP   CLEAVAGE, GLYCOSYLATION, GLYCOSYLATION AT ASN-546, DISULFIDE BONDS, AND\nRP   MUTAGENESIS OF ASN-361; ASN-432 AND ASN-445.\nRX   PubMed=37428845; DOI=10.1107/s2059798323004710;\nRA   Martinez M., Batista F.A., Maurel M., Bouillon A., Ortega Varga L.,\nRA   Wehenkel A.M., Le Chevalier-Sontag L., Blondel A., Haouz A.,\nRA   Hernandez J.F., Alzari P.M., Barale J.C.;\nRT   \"3D structures of the Plasmodium vivax subtilisin-like drug target SUB1\nRT   reveal conformational changes to accommodate a substrate-derived alpha-\nRT   ketoamide inhibitor.\";\nRL   Acta Crystallogr. D Struct. Biol. 79:721-734(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H6",
  "excerpt": "RN   [7] {ECO:0007744|PDB:8QKE, ECO:0007744|PDB:8QKG}\nRP   X-RAY CRYSTALLOGRAPHY (1.50 ANGSTROMS) OF 26-630 IN COMPLEX WITH CA(2+) AND\nRP   PEPTIDE INHIBITORS, CATALYTIC ACTIVITY, ACTIVITY REGULATION, GLYCOSYLATION\nRP   AT ASN-546, AND DISULFIDE BONDS.\nRX   PubMed=38503166; DOI=10.1016/j.ejmech.2024.116308;\nRA   Legru A., Batista F.A., Puszko A.K., Bouillon A., Maurel M., Martinez M.,\nRA   Ejjoummany A., Ortega Varga L., Adler P., Mechaly A., Hadjadj M.,\nRA   Sosnowski P., Hopfgartner G., Alzari P.M., Blondel A., Haouz A.,\nRA   Barale J.C., Hernandez J.F.;\nRT   \"Insights from structure-activity relationships and the binding mode of\nRT   peptidic alpha-ketoamide inhibitors of the malaria drug target subtilisin-\nRT   like SUB1.\";\nRL   Eur. J. Med. Chem. 269:116308-116308(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H7",
  "excerpt": "FT   ACT_SITE        316\nFT                   /note=\"Charge relay system\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01240\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 233-235",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H8",
  "excerpt": "FT   ACT_SITE        372\nFT                   /note=\"Charge relay system\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01240\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 236-238",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H9",
  "excerpt": "FT   ACT_SITE        549\nFT                   /note=\"Charge relay system\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01240\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 239-241",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         129\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0007744|PDB:4TR2\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 242-247",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         130\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0007744|PDB:4TR2\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 248-253",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         133\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0007744|PDB:4TR2\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 254-259",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         135\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0007744|PDB:4TR2\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 260-265",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         190\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0007744|PDB:4TR2\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 266-271",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H15",
  "excerpt": "FT   BINDING         281\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 272-280",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H16",
  "excerpt": "FT   BINDING         325\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 281-289",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H17",
  "excerpt": "FT   BINDING         336\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 290-298",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H18",
  "excerpt": "FT   BINDING         336\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 299-307",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H19",
  "excerpt": "FT   BINDING         340\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 308-316",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H20",
  "excerpt": "FT   BINDING         343\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 317-325",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H21",
  "excerpt": "FT   BINDING         344\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 326-334",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H22",
  "excerpt": "FT   BINDING         345\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 335-343",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H23",
  "excerpt": "FT   BINDING         346\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 344-352",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H24",
  "excerpt": "FT   BINDING         348\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 353-361",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H25",
  "excerpt": "FT   BINDING         350\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 362-370",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H26",
  "excerpt": "FT   BINDING         352\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 371-379",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H27",
  "excerpt": "FT   BINDING         353\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 380-388",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H28

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H28",
  "excerpt": "FT   BINDING         383\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 389-397",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H29

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H29",
  "excerpt": "FT   BINDING         386\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 398-405",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H30

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H30",
  "excerpt": "FT   BINDING         388\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 406-414",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H31

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H31",
  "excerpt": "FT   BINDING         390\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:25204226,\nFT                   ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38503166,\nFT                   ECO:0007744|PDB:4TR2, ECO:0007744|PDB:8COY,\nFT                   ECO:0007744|PDB:8COZ, ECO:0007744|PDB:8QKE,\nFT                   ECO:0007744|PDB:8QKG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 415-423",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H32

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H32",
  "excerpt": "FT   SITE            202..203\nFT                   /note=\"Cleavage\"\nFT                   /evidence=\"ECO:0000269|PubMed:23653352,\nFT                   ECO:0000269|PubMed:25204226, ECO:0000269|PubMed:37428845\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 424-427",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H33

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H33",
  "excerpt": "FT   SITE            243..244\nFT                   /note=\"Cleavage\"\nFT                   /evidence=\"ECO:0000269|PubMed:23653352,\nFT                   ECO:0000269|PubMed:37428845\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 428-431",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H34

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H34",
  "excerpt": "FT   SITE            270..271\nFT                   /note=\"Cleavage\"\nFT                   /evidence=\"ECO:0000269|PubMed:23653352\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 432-434",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H35

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H35",
  "excerpt": "FT   SITE            357..358\nFT                   /note=\"Cleavage\"\nFT                   /evidence=\"ECO:0000269|PubMed:37428845\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 435-437",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
