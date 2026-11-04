# cofactor_0084

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0084.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Fe(2+)

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
A. Na(+)
B. heme b
C. Mg(2+)
D. Fe(2+)
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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates Fe(2+) as the cofactor, with experimental evidence attributed to a 2022 publication. This supports the key, although the underlying study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the small ArsI/C-As-lyase family, whose transferable family-level characterization is a non-heme Fe(2+)-dependent catalytic mechanism. Conserved histidine and acidic residues are also compatible with a non-heme metal-binding site. This favors Fe(2+) over heme b, Na(+) or Mg(2+) among the offered choices; the sequence-based identification is probabilistic, not a substitute for a direct cofactor assay.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A recognizable family-level inference and metal-binding pattern provide a meaningful basis for distinguishing the choices without needing the exact protein's database annotation. The original input does not name the family, so the inference depends on sequence recognition and knowledge of related proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports Fe(2+), and no other offered option is comparably supported.


### Important caveats

- The experimental basis is represented here by a database annotation citing a publication; that primary study was not independently assessed.
- The family-level inference from sequence is less certain than the reviewer-only, sequence-matched annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the small ArsI/C-As-lyase family, whose transferable family-level characterization is a non-heme Fe(2+)-dependent catalytic mechanism. Conserved histidine and acidic residues are also compatible with a non-heme metal-binding site. This favors Fe(2+) over heme b, Na(+) or Mg(2+) among the offered choices; the sequence-based identification is probabilistic, not a substitute for a direct cofactor assay.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A recognizable family-level inference and metal-binding pattern provide a meaningful basis for distinguishing the choices without needing the exact protein's database annotation. The original input does not name the family, so the inference depends on sequence recognition and knowledge of related proteins."
  },
  "case_id": "cofactor_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Fe(2+) as the cofactor, with experimental evidence attributed to a 2022 publication. This supports the key, although the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The experimental basis is represented here by a database annotation citing a publication; that primary study was not independently assessed.",
    "The family-level inference from sequence is less certain than the reviewer-only, sequence-matched annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports Fe(2+), and no other offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Fe(2+) as the cofactor, with experimental evidence attributed to a 2022 publication. This supports the key, although the underlying study was not independently reviewed here.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the small ArsI/C-As-lyase family, whose transferable family-level characterization is a non-heme Fe(2+)-dependent catalytic mechanism. Conserved histidine and acidic residues are also compatible with a non-heme metal-binding site. This favors Fe(2+) over heme b, Na(+) or Mg(2+) among the offered choices; the sequence-based identification is probabilistic, not a substitute for a direct cofactor assay.",
    "missing_item_specific_fact": "",
    "reason": "A recognizable family-level inference and metal-binding pattern provide a meaningful basis for distinguishing the choices without needing the exact protein's database annotation. The original input does not name the family, so the inference depends on sequence recognition and knowledge of related proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports Fe(2+), and no other offered option is comparably supported."
  },
  "important_caveats": [
    "The experimental basis is represented here by a database annotation citing a publication; that primary study was not independently assessed.",
    "The family-level inference from sequence is less certain than the reviewer-only, sequence-matched annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (D1A230, ARSI_THECD) explicitly annotates Fe(2+) (ChEBI:29033) as the cofactor with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:35487149. The 2022 crystallographic study (PDB:5V0F) shows the enzyme in complex with Fe(2+) and substrate roxarsone(III). The earlier 2016 crystallography (PubMed:27107642) also resolved Fe(3+) complexes, confirming a metal site involving His-97 and Glu-102. The annotation is experimentally grounded, not merely computational.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can apply metal-coordination chemistry preferences to eliminate alternatives. (1) Na(+) is essentially never a catalytic cofactor for oxidoreductase/lyase-type enzymes; it serves structural or transport roles, making A a clear distractor. (2) Heme b requires specific motifs (Cys-X-X-Cys in the right context, bis-His ligation, hydrophobic heme pocket) and heme proteins are typically much larger than 151 aa; the Cys pairs here (e.g., 'DTACCYAV', 'DSACCTPRDSG') are not in a canonical CXXC heme-binding arrangement, making B unlikely. (3) Mg(2+) strongly prefers O-donor ligands (Asp, Glu, backbone carbonyls, water) and very rarely uses His or Cys as primary coordination sphere residues. The sequence prominently features His residues (e.g., 'GHAARR' near position 74-79, 'RLDHLG') and multiple Cys pairs, which are hallmarks of Fe(2+) coordination (2-His-1-carboxylate facial triad or His/Cys/Asp/Glu sites common in Fe-dependent dioxygenases and lyases). This His/Cys-rich coordination signature is a well-established, transferable distinction between Fe and Mg sites learned from hundreds of metalloenzyme structures. The small size (~151 aa) and bacterial origin are also consistent with the large family of small Fe(2+)-dependent bacterial enzymes. While the exact protein identity (ArsI) is not needed, the metal-ligand preference pattern meaningfully favors D over C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of Na(+) and heme b relies on well-known functional and structural constraints. The distinction between Mg(2+) and Fe(2+) rests on the well-established coordination chemistry preference: Mg(2+) uses O-donors (Asp/Glu/water), while Fe(2+) commonly uses His and Cys ligands. The sequence's prominent His and Cys residues provide a transferable, family-level inference that meaningfully favors Fe(2+) over Mg(2+) without requiring the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Na(+) is eliminated as a catalytic cofactor for this enzyme class. Heme b is eliminated by the absence of canonical heme-binding motifs and the small protein size. The Mg(2+) vs Fe(2+) distinction is resolved by the His/Cys coordination signature, which is inconsistent with Mg(2+) chemistry. Only Fe(2+) is consistent with the observed ligand set.


### Important caveats

- The reasoning relies on statistical/empirical metal-coordination preferences (His/Cys favor Fe over Mg) rather than a first-principles derivation. Some Mg(2+) enzymes do use His as a secondary ligand, but the prominent His+Cys pattern here strongly favors Fe.
- The Cys pairs could in principle form structural disulfides rather than metal ligands, though in a bacterial cytoplasmic protein free Cys is more typical.
- The specific identification of the protein as ArsI (C-As lyase) and its EC 1.13.11.- classification would require database lookup, but the metal-coordination chemistry argument does not depend on that identification.
- The UniProt annotation is from a Swiss-Prot reviewed entry with experimental evidence (ECO:0000269), providing high confidence in the Fe(2+) assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can apply metal-coordination chemistry preferences to eliminate alternatives. (1) Na(+) is essentially never a catalytic cofactor for oxidoreductase/lyase-type enzymes; it serves structural or transport roles, making A a clear distractor. (2) Heme b requires specific motifs (Cys-X-X-Cys in the right context, bis-His ligation, hydrophobic heme pocket) and heme proteins are typically much larger than 151 aa; the Cys pairs here (e.g., 'DTACCYAV', 'DSACCTPRDSG') are not in a canonical CXXC heme-binding arrangement, making B unlikely. (3) Mg(2+) strongly prefers O-donor ligands (Asp, Glu, backbone carbonyls, water) and very rarely uses His or Cys as primary coordination sphere residues. The sequence prominently features His residues (e.g., 'GHAARR' near position 74-79, 'RLDHLG') and multiple Cys pairs, which are hallmarks of Fe(2+) coordination (2-His-1-carboxylate facial triad or His/Cys/Asp/Glu sites common in Fe-dependent dioxygenases and lyases). This His/Cys-rich coordination signature is a well-established, transferable distinction between Fe and Mg sites learned from hundreds of metalloenzyme structures. The small size (~151 aa) and bacterial origin are also consistent with the large family of small Fe(2+)-dependent bacterial enzymes. While the exact protein identity (ArsI) is not needed, the metal-ligand preference pattern meaningfully favors D over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of Na(+) and heme b relies on well-known functional and structural constraints. The distinction between Mg(2+) and Fe(2+) rests on the well-established coordination chemistry preference: Mg(2+) uses O-donors (Asp/Glu/water), while Fe(2+) commonly uses His and Cys ligands. The sequence's prominent His and Cys residues provide a transferable, family-level inference that meaningfully favors Fe(2+) over Mg(2+) without requiring the specific UniProt annotation for this exact protein."
  },
  "case_id": "cofactor_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (D1A230, ARSI_THECD) explicitly annotates Fe(2+) (ChEBI:29033) as the cofactor with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:35487149. The 2022 crystallographic study (PDB:5V0F) shows the enzyme in complex with Fe(2+) and substrate roxarsone(III). The earlier 2016 crystallography (PubMed:27107642) also resolved Fe(3+) complexes, confirming a metal site involving His-97 and Glu-102. The annotation is experimentally grounded, not merely computational."
  },
  "important_caveats": [
    "The reasoning relies on statistical/empirical metal-coordination preferences (His/Cys favor Fe over Mg) rather than a first-principles derivation. Some Mg(2+) enzymes do use His as a secondary ligand, but the prominent His+Cys pattern here strongly favors Fe.",
    "The Cys pairs could in principle form structural disulfides rather than metal ligands, though in a bacterial cytoplasmic protein free Cys is more typical.",
    "The specific identification of the protein as ArsI (C-As lyase) and its EC 1.13.11.- classification would require database lookup, but the metal-coordination chemistry argument does not depend on that identification.",
    "The UniProt annotation is from a Swiss-Prot reviewed entry with experimental evidence (ECO:0000269), providing high confidence in the Fe(2+) assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Na(+) is eliminated as a catalytic cofactor for this enzyme class. Heme b is eliminated by the absence of canonical heme-binding motifs and the small protein size. The Mg(2+) vs Fe(2+) distinction is resolved by the His/Cys coordination signature, which is inconsistent with Mg(2+) chemistry. Only Fe(2+) is consistent with the observed ligand set."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (D1A230, ARSI_THECD) explicitly annotates Fe(2+) (ChEBI:29033) as the cofactor with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:35487149. The 2022 crystallographic study (PDB:5V0F) shows the enzyme in complex with Fe(2+) and substrate roxarsone(III). The earlier 2016 crystallography (PubMed:27107642) also resolved Fe(3+) complexes, confirming a metal site involving His-97 and Glu-102. The annotation is experimentally grounded, not merely computational.",
    "evidence_ids": ["C5", "C8", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can apply metal-coordination chemistry preferences to eliminate alternatives. (1) Na(+) is essentially never a catalytic cofactor for oxidoreductase/lyase-type enzymes; it serves structural or transport roles, making A a clear distractor. (2) Heme b requires specific motifs (Cys-X-X-Cys in the right context, bis-His ligation, hydrophobic heme pocket) and heme proteins are typically much larger than 151 aa; the Cys pairs here (e.g., 'DTACCYAV', 'DSACCTPRDSG') are not in a canonical CXXC heme-binding arrangement, making B unlikely. (3) Mg(2+) strongly prefers O-donor ligands (Asp, Glu, backbone carbonyls, water) and very rarely uses His or Cys as primary coordination sphere residues. The sequence prominently features His residues (e.g., 'GHAARR' near position 74-79, 'RLDHLG') and multiple Cys pairs, which are hallmarks of Fe(2+) coordination (2-His-1-carboxylate facial triad or His/Cys/Asp/Glu sites common in Fe-dependent dioxygenases and lyases). This His/Cys-rich coordination signature is a well-established, transferable distinction between Fe and Mg sites learned from hundreds of metalloenzyme structures. The small size (~151 aa) and bacterial origin are also consistent with the large family of small Fe(2+)-dependent bacterial enzymes. While the exact protein identity (ArsI) is not needed, the metal-ligand preference pattern meaningfully favors D over C.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of Na(+) and heme b relies on well-known functional and structural constraints. The distinction between Mg(2+) and Fe(2+) rests on the well-established coordination chemistry preference: Mg(2+) uses O-donors (Asp/Glu/water), while Fe(2+) commonly uses His and Cys ligands. The sequence's prominent His and Cys residues provide a transferable, family-level inference that meaningfully favors Fe(2+) over Mg(2+) without requiring the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Na(+) is eliminated as a catalytic cofactor for this enzyme class. Heme b is eliminated by the absence of canonical heme-binding motifs and the small protein size. The Mg(2+) vs Fe(2+) distinction is resolved by the His/Cys coordination signature, which is inconsistent with Mg(2+) chemistry. Only Fe(2+) is consistent with the observed ligand set."
  },
  "important_caveats": [
    "The reasoning relies on statistical/empirical metal-coordination preferences (His/Cys favor Fe over Mg) rather than a first-principles derivation. Some Mg(2+) enzymes do use His as a secondary ligand, but the prominent His+Cys pattern here strongly favors Fe.",
    "The Cys pairs could in principle form structural disulfides rather than metal ligands, though in a bacterial cytoplasmic protein free Cys is more typical.",
    "The specific identification of the protein as ArsI (C-As lyase) and its EC 1.13.11.- classification would require database lookup, but the metal-coordination chemistry argument does not depend on that identification.",
    "The UniProt annotation is from a Swiss-Prot reviewed entry with experimental evidence (ECO:0000269), providing high confidence in the Fe(2+) assignment."
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
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29033\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35487149\",\"source\":\"PubMed\"}],\"name\":\"Fe(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
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

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C7",
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

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1A230.json)

```json
{
  "evidence_id": "C8",
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
  "excerpt": "DE   RecName: Full=Trivalent organoarsenical cleaving enzyme {ECO:0000305};\nDE            EC=1.13.11.- {ECO:0000269|PubMed:27107642, ECO:0000269|PubMed:35487149};\nDE   AltName: Full=C-As lyase {ECO:0000303|PubMed:24915088, ECO:0000303|PubMed:27107642, ECO:0000303|PubMed:35487149};\nDE   AltName: Full=Methylarsonous acid demethylase {ECO:0000305|PubMed:27107642};\nDE            Short=MAs(III) demethylase {ECO:0000305|PubMed:27107642};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H4",
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

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H5",
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

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;\nCC         Evidence={ECO:0000269|PubMed:35487149};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:46.748619+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64f904109a5f69718a32231b7c4349d474c2b8b6f90d2e9fb11be49e672c03f2",
  "url": "https://rest.uniprot.org/unisave/D1A230?format=txt&versions=77"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
