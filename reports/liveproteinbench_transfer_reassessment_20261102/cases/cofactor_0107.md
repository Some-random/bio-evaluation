# cofactor_0107

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0107.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGETTQLDLSVKAVGWGAADASGTLQPIKFYRRTPGERDVKIRVLYCGVCNFDMEMVRNKWGFTRYPYVFGHETAGEVIEVGSKVQKFKVGDKVGVGCMVGSCGKCFNCQNGMENYCPEPNMADGSVYREQQGEPSFGGCSNVMVVDEKFVLRWPENLPQDTGVPLLCAGIVVYSPMKYMGLDKPGKHIGVIGLGGLGSIAVKFIKAFGGKATVISTSKRKEKEAIEEHGADAFVVNTDTEKLQALAGTMDGVVDTTPGGRTPMSLMLNLLKFDGVVLLVGAPETLFELPVQPLILGRRKIIGSSTGGLKEYQETLDFAAQHNIVCDTEVIGIDYLSTAMERIKNLDVKYRFAIDIGNTLKYED

[Multiple Choices]
A. pantetheine 4'-phosphate
B. pyridoxal 5'-phosphate
C. cob(II)alamin
D. Zn(2+)
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

> The sequence-matched UniProt annotation identifies Zn(2+) and says the protein binds two Zn(2+) ions per subunit. This annotation is transferred by similarity from another UniProt entry, so it supports the key but is not direct experimental confirmation for this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a pronounced cluster of cysteines, including closely spaced Cys-rich segments, which provides a plausible transferable clue for metal coordination such as Zn(2+). Among the choices, that is a more meaningful sequence-based fit than the characteristic cofactor classes represented by pantetheine 4'-phosphate, PLP, or cob(II)alamin. This supports a probabilistic choice of D, not proof of binding or essentiality.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A cysteine-rich metal-binding pattern offers a credible basis for distinguishing Zn(2+) among these alternatives without requiring the exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered cofactor has a comparably strong sequence-based clue in the supplied input.


### Important caveats

- The supporting database cofactor annotation is similarity-transferred, not evidence of direct experimental measurement for this exact protein.
- The sequence motif suggests metal coordination but alone does not establish the number of bound ions or that Zn(2+) is essential for catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a pronounced cluster of cysteines, including closely spaced Cys-rich segments, which provides a plausible transferable clue for metal coordination such as Zn(2+). Among the choices, that is a more meaningful sequence-based fit than the characteristic cofactor classes represented by pantetheine 4'-phosphate, PLP, or cob(II)alamin. This supports a probabilistic choice of D, not proof of binding or essentiality.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A cysteine-rich metal-binding pattern offers a credible basis for distinguishing Zn(2+) among these alternatives without requiring the exact protein's database annotation."
  },
  "case_id": "cofactor_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies Zn(2+) and says the protein binds two Zn(2+) ions per subunit. This annotation is transferred by similarity from another UniProt entry, so it supports the key but is not direct experimental confirmation for this protein."
  },
  "important_caveats": [
    "The supporting database cofactor annotation is similarity-transferred, not evidence of direct experimental measurement for this exact protein.",
    "The sequence motif suggests metal coordination but alone does not establish the number of bound ions or that Zn(2+) is essential for catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered cofactor has a comparably strong sequence-based clue in the supplied input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies Zn(2+) and says the protein binds two Zn(2+) ions per subunit. This annotation is transferred by similarity from another UniProt entry, so it supports the key but is not direct experimental confirmation for this protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a pronounced cluster of cysteines, including closely spaced Cys-rich segments, which provides a plausible transferable clue for metal coordination such as Zn(2+). Among the choices, that is a more meaningful sequence-based fit than the characteristic cofactor classes represented by pantetheine 4'-phosphate, PLP, or cob(II)alamin. This supports a probabilistic choice of D, not proof of binding or essentiality.",
    "missing_item_specific_fact": "",
    "reason": "A cysteine-rich metal-binding pattern offers a credible basis for distinguishing Zn(2+) among these alternatives without requiring the exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered cofactor has a comparably strong sequence-based clue in the supplied input."
  },
  "important_caveats": [
    "The supporting database cofactor annotation is similarity-transferred, not evidence of direct experimental measurement for this exact protein.",
    "The sequence motif suggests metal coordination but alone does not establish the number of bound ions or that Zn(2+) is essential for catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) annotates Zn(2+) as cofactor (Binds 2 Zn(2+) ions per subunit). However, the evidence code is ECO:0000250 (inferred by similarity to P06525), making this a computational/transferred annotation rather than direct experimental measurement. The sequence itself contains clustered cysteine residues (e.g., 'GCMVGSCGKCFNCQNGMENYCPEP' and 'LYCGVCNFDM') consistent with zinc-coordinating sites, and a Rossmann-fold NAD(P)-binding motif ('IGVIGLGGLGSIAVKFIKAFGGK'), supporting the oxidoreductase-plus-zinc-metalloenzyme interpretation. The annotation is consistent with observable sequence features, though not independently experimentally verified for this exact protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD(P)-binding motif ('IGVIGLGGLGSIAVKFIKAFGGK'), identifying the protein as an oxidoreductase. Crucially, a dense cluster of cysteines appears in the region 'GCMVGSCGKCFNCQNGMENYCPEP' (at least four cysteines within ~25 residues), a pattern well-known from transferable knowledge of zinc-binding sites in metalloenzymes (tetrahedral Cys coordination). Additional cysteines in 'LYCGVCNFDM' and 'FGGCSNVM' reinforce this. Many oxidoreductases (e.g., alcohol dehydrogenases, enoyl-reductases) use Zn2+ as a catalytic Lewis acid alongside NAD(P) as cosubstrate. Against the alternatives: (B) PLP-dependent enzymes require a conserved lysine forming a Schiff base and belong to transferase/lyase classes, not oxidoreductases; no PLP-binding motif is present. (C) Cob(II)alamin-dependent enzymes contain a B12-binding-2 domain with conserved His/Asp residues; none are recognizable here. (A) Pantetheine 4'-phosphate (CoA/ACP component) is found in acyltransferases and synthetases with specific CoA-binding folds; the sequence lacks these. The combination of visible zinc-binding cysteine clusters, oxidoreductase context, and absence of motifs for the other three cofactors provides a credible transferable inference to Zn(2+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the Rossmann fold, recognize the clustered cysteine zinc-binding motif, and eliminate PLP, B12, and CoA alternatives based on the absence of their characteristic structural motifs and the enzyme's oxidoreductase class. This relies on family-level knowledge of zinc-binding patterns and cofactor-domain architecture learned from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct cofactor classes (acyl-carrier component, PLP, B12, Zn2+). The sequence features (zinc-binding cysteine clusters, Rossmann fold, absence of PLP/B12/CoA motifs) clearly favor Zn(2+) and disfavor the others. No alternative choice is equally defensible given the observable sequence.


### Important caveats

- The UniProt cofactor annotation for P0DXJ1 is based on similarity (ECO:0000250, transferred from P06525), not direct experimental determination of zinc binding for this specific protein.
- The EC number 1.3.1.36 is also assigned by similarity (to W8JWW7), not by direct enzymatic assay on this sequence.
- The Rossmann-fold region suggests NAD(P) as a cosubstrate, which is not among the choices; the question asks specifically for the catalytic cofactor/metal, which is distinct from the hydride-transfer cosubstrate.
- The sequence was matched to UniProt P0DXJ1 (365 aa, exact match), but the evaluated model did not have access to the accession or organism name.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif ('IGVIGLGGLGSIAVKFIKAFGGK'), identifying the protein as an oxidoreductase. Crucially, a dense cluster of cysteines appears in the region 'GCMVGSCGKCFNCQNGMENYCPEP' (at least four cysteines within ~25 residues), a pattern well-known from transferable knowledge of zinc-binding sites in metalloenzymes (tetrahedral Cys coordination). Additional cysteines in 'LYCGVCNFDM' and 'FGGCSNVM' reinforce this. Many oxidoreductases (e.g., alcohol dehydrogenases, enoyl-reductases) use Zn2+ as a catalytic Lewis acid alongside NAD(P) as cosubstrate. Against the alternatives: (B) PLP-dependent enzymes require a conserved lysine forming a Schiff base and belong to transferase/lyase classes, not oxidoreductases; no PLP-binding motif is present. (C) Cob(II)alamin-dependent enzymes contain a B12-binding-2 domain with conserved His/Asp residues; none are recognizable here. (A) Pantetheine 4'-phosphate (CoA/ACP component) is found in acyltransferases and synthetases with specific CoA-binding folds; the sequence lacks these. The combination of visible zinc-binding cysteine clusters, oxidoreductase context, and absence of motifs for the other three cofactors provides a credible transferable inference to Zn(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann fold, recognize the clustered cysteine zinc-binding motif, and eliminate PLP, B12, and CoA alternatives based on the absence of their characteristic structural motifs and the enzyme's oxidoreductase class. This relies on family-level knowledge of zinc-binding patterns and cofactor-domain architecture learned from other proteins."
  },
  "case_id": "cofactor_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) annotates Zn(2+) as cofactor (Binds 2 Zn(2+) ions per subunit). However, the evidence code is ECO:0000250 (inferred by similarity to P06525), making this a computational/transferred annotation rather than direct experimental measurement. The sequence itself contains clustered cysteine residues (e.g., 'GCMVGSCGKCFNCQNGMENYCPEP' and 'LYCGVCNFDM') consistent with zinc-coordinating sites, and a Rossmann-fold NAD(P)-binding motif ('IGVIGLGGLGSIAVKFIKAFGGK'), supporting the oxidoreductase-plus-zinc-metalloenzyme interpretation. The annotation is consistent with observable sequence features, though not independently experimentally verified for this exact protein."
  },
  "important_caveats": [
    "The UniProt cofactor annotation for P0DXJ1 is based on similarity (ECO:0000250, transferred from P06525), not direct experimental determination of zinc binding for this specific protein.",
    "The EC number 1.3.1.36 is also assigned by similarity (to W8JWW7), not by direct enzymatic assay on this sequence.",
    "The Rossmann-fold region suggests NAD(P) as a cosubstrate, which is not among the choices; the question asks specifically for the catalytic cofactor/metal, which is distinct from the hydride-transfer cosubstrate.",
    "The sequence was matched to UniProt P0DXJ1 (365 aa, exact match), but the evaluated model did not have access to the accession or organism name."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct cofactor classes (acyl-carrier component, PLP, B12, Zn2+). The sequence features (zinc-binding cysteine clusters, Rossmann fold, absence of PLP/B12/CoA motifs) clearly favor Zn(2+) and disfavor the others. No alternative choice is equally defensible given the observable sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) annotates Zn(2+) as cofactor (Binds 2 Zn(2+) ions per subunit). However, the evidence code is ECO:0000250 (inferred by similarity to P06525), making this a computational/transferred annotation rather than direct experimental measurement. The sequence itself contains clustered cysteine residues (e.g., 'GCMVGSCGKCFNCQNGMENYCPEP' and 'LYCGVCNFDM') consistent with zinc-coordinating sites, and a Rossmann-fold NAD(P)-binding motif ('IGVIGLGGLGSIAVKFIKAFGGK'), supporting the oxidoreductase-plus-zinc-metalloenzyme interpretation. The annotation is consistent with observable sequence features, though not independently experimentally verified for this exact protein.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif ('IGVIGLGGLGSIAVKFIKAFGGK'), identifying the protein as an oxidoreductase. Crucially, a dense cluster of cysteines appears in the region 'GCMVGSCGKCFNCQNGMENYCPEP' (at least four cysteines within ~25 residues), a pattern well-known from transferable knowledge of zinc-binding sites in metalloenzymes (tetrahedral Cys coordination). Additional cysteines in 'LYCGVCNFDM' and 'FGGCSNVM' reinforce this. Many oxidoreductases (e.g., alcohol dehydrogenases, enoyl-reductases) use Zn2+ as a catalytic Lewis acid alongside NAD(P) as cosubstrate. Against the alternatives: (B) PLP-dependent enzymes require a conserved lysine forming a Schiff base and belong to transferase/lyase classes, not oxidoreductases; no PLP-binding motif is present. (C) Cob(II)alamin-dependent enzymes contain a B12-binding-2 domain with conserved His/Asp residues; none are recognizable here. (A) Pantetheine 4'-phosphate (CoA/ACP component) is found in acyltransferases and synthetases with specific CoA-binding folds; the sequence lacks these. The combination of visible zinc-binding cysteine clusters, oxidoreductase context, and absence of motifs for the other three cofactors provides a credible transferable inference to Zn(2+).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann fold, recognize the clustered cysteine zinc-binding motif, and eliminate PLP, B12, and CoA alternatives based on the absence of their characteristic structural motifs and the enzyme's oxidoreductase class. This relies on family-level knowledge of zinc-binding patterns and cofactor-domain architecture learned from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct cofactor classes (acyl-carrier component, PLP, B12, Zn2+). The sequence features (zinc-binding cysteine clusters, Rossmann fold, absence of PLP/B12/CoA motifs) clearly favor Zn(2+) and disfavor the others. No alternative choice is equally defensible given the observable sequence."
  },
  "important_caveats": [
    "The UniProt cofactor annotation for P0DXJ1 is based on similarity (ECO:0000250, transferred from P06525), not direct experimental determination of zinc binding for this specific protein.",
    "The EC number 1.3.1.36 is also assigned by similarity (to W8JWW7), not by direct enzymatic assay on this sequence.",
    "The Rossmann-fold region suggests NAD(P) as a cosubstrate, which is not among the choices; the question asks specifically for the catalytic cofactor/metal, which is distinct from the hydride-transfer cosubstrate.",
    "The sequence was matched to UniProt P0DXJ1 (365 aa, exact match), but the evaluated model did not have access to the accession or organism name."
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
  "benchmark_sequence_length": 365,
  "benchmark_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 365,
  "current_source_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXJ1",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "selected_historical_source_sequence_length": 365,
  "selected_historical_source_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "selected_historical_version": {
    "accession": "P0DXJ1",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GS_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"W8JWW7\",\"source\":\"UniProtKB\"}],\"value\":\"1.3.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Geissoschizine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsGS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P06525\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P06525\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 2 Zn(2+) ions per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61919.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"BIOTECHNOLOGY\",\"TISSUE SPECIFICITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   GS_RAUSE                Reviewed;         365 AA.\nAC   P0DXJ1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:38212296};\nDE            Short=RsGS {ECO:0000303|PubMed:38212296};\nDE            EC=1.3.1.36 {ECO:0000250|UniProtKB:W8JWW7};\nGN   Name=GS {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:38212296};\nDE            Short=RsGS {ECO:0000303|PubMed:38212296};\nDE            EC=1.3.1.36 {ECO:0000250|UniProtKB:W8JWW7};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WKU61919.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, BIOTECHNOLOGY, TISSUE SPECIFICITY,\nRP   AND PATHWAY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:P06525};\nCC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000250|UniProtKB:P06525};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
