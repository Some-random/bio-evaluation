# catalytic_activity_0192

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0192.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSGNRGVVYLGPGKVEVQNIPYPKMQDPQGRQIDHGVILRVVSTNICGSDQHMVRGRTTAPEGLVLGHEITGEVVEIGRGVETMKIGDLVSVPFNVACGHCRTCKEQHTGVCLTVNPARAGGAYGYVDMGGWVGGQAEYVLVPYADFNLLKLPNREAAMEKIRDLTCLSDILPTGYHGAVTAGVGPGSTVYIAGAGPVGLAAAASARLLGAAVVIVGDVNPTRLAHAKKQGFEIADLSKDTPLHEQIAALLGEPEVDCAVDAVGFEARGHGHSGSQQEAPATVLNSLMGITRVAGKIGIPGLYVTEDPGAVDAAAKHGALSIRFGLGWAKSHSFHTGQTPVMKYNRQLMQAIMWDRIKIADIVGVEVITLDDAPKGYGEFDAGVPKKFVIDPHNLFRAA

[Multiple Choices]
A. 2-oxospirilloxanthin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = 2,2'-dioxospirilloxanthin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O
B. (2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O
C. formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)
D. 6-O-methyldeacetylisoipecoside + H2O = 6-O-methyldeacetylisoipecoside aglycone + D-glucose
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

> The sequence-matched UniProt entry annotates the formaldehyde-to-formate reaction as catalytic activity, with experimental evidence cited. This supports choice C for the supplied protein.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has features consistent with a zinc-dependent, NAD-binding medium-chain dehydrogenase: an N-terminal glycine-rich cofactor-binding region and conserved cysteine/histidine-rich metal-binding features. Transferable knowledge of this enzyme family supports NAD-dependent aldehyde oxidation. Among these options, C is the aldehyde oxidation to a carboxylate using NAD+; the other choices describe unrelated carotenoid oxidation, a hydroxy-acid dehydration, and glycoside hydrolysis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and the reaction classes in the choices meaningfully favor C without needing the exact protein's database record. This supports the choice, though sequence-family inference alone does not prove that formaldehyde is the specific aldehyde substrate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C matches the supported NAD-dependent aldehyde oxidation reaction among the offered choices.


### Important caveats

- The source annotation also reports acetaldehyde oxidation, but that reaction is not offered as an alternative.
- The database annotation cites experimental evidence; the supplied excerpts do not independently reproduce or validate the underlying experiments.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a zinc-dependent, NAD-binding medium-chain dehydrogenase: an N-terminal glycine-rich cofactor-binding region and conserved cysteine/histidine-rich metal-binding features. Transferable knowledge of this enzyme family supports NAD-dependent aldehyde oxidation. Among these options, C is the aldehyde oxidation to a carboxylate using NAD+; the other choices describe unrelated carotenoid oxidation, a hydroxy-acid dehydration, and glycoside hydrolysis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the reaction classes in the choices meaningfully favor C without needing the exact protein's database record. This supports the choice, though sequence-family inference alone does not prove that formaldehyde is the specific aldehyde substrate."
  },
  "case_id": "catalytic_activity_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the formaldehyde-to-formate reaction as catalytic activity, with experimental evidence cited. This supports choice C for the supplied protein."
  },
  "important_caveats": [
    "The source annotation also reports acetaldehyde oxidation, but that reaction is not offered as an alternative.",
    "The database annotation cites experimental evidence; the supplied excerpts do not independently reproduce or validate the underlying experiments."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C matches the supported NAD-dependent aldehyde oxidation reaction among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the formaldehyde-to-formate reaction as catalytic activity, with experimental evidence cited. This supports choice C for the supplied protein.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has features consistent with a zinc-dependent, NAD-binding medium-chain dehydrogenase: an N-terminal glycine-rich cofactor-binding region and conserved cysteine/histidine-rich metal-binding features. Transferable knowledge of this enzyme family supports NAD-dependent aldehyde oxidation. Among these options, C is the aldehyde oxidation to a carboxylate using NAD+; the other choices describe unrelated carotenoid oxidation, a hydroxy-acid dehydration, and glycoside hydrolysis.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the reaction classes in the choices meaningfully favor C without needing the exact protein's database record. This supports the choice, though sequence-family inference alone does not prove that formaldehyde is the specific aldehyde substrate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C matches the supported NAD-dependent aldehyde oxidation reaction among the offered choices."
  },
  "important_caveats": [
    "The source annotation also reports acetaldehyde oxidation, but that reaction is not offered as an alternative.",
    "The database annotation cites experimental evidence; the supplied excerpts do not independently reproduce or validate the underlying experiments."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXZ0 (sequence exactly matched, 399 aa) is annotated as Glutathione-independent formaldehyde dehydrogenase (EC 1.2.1.46) with the catalytic reaction 'formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)' backed by experimental evidence (ECO:0000269) from two PubMed publications (23989142, 24125754). The sequence in the question matches the database entry exactly.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C1](#evidence-c1), [H5](#evidence-h5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark features of the aldehyde dehydrogenase (ALDH) superfamily: (1) A Rossmann-fold-like NAD-binding region in the N-terminal half with glycine-rich motifs (e.g., 'VIGRGVETMKIG', 'GPGSTVYIAGAGPVGLAAAASARLLGAAVVIVGDVNP') characteristic of dinucleotide-binding domains found in dehydrogenases. (2) A zinc-binding cysteine cluster ('CGHCRTCK') typical of ALDH catalytic domains. (3) The overall ~400-residue two-domain architecture (NAD-binding + catalytic) matches bacterial ALDH enzymes. Among the four choices, only C involves NAD(+) as a cofactor; A uses &#91;2Fe-2S&#93; ferredoxin (no Fe-S binding motifs present), B is a dehydratase (no cofactor), and D is a glycosidase (no NAD+ requirement). The presence of NAD-binding motifs and zinc-coordinating cysteines, combined with ALDH-family knowledge learned from other characterized ALDH enzymes, meaningfully distinguishes C as the only NAD+-dependent aldehyde oxidation reaction consistent with the observed sequence features.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of the ALDH superfamily (Rossmann-fold NAD-binding, zinc-binding Cys cluster, two-domain architecture) and the cofactor requirements of the four offered reactions allow a knowledgeable model to eliminate A (requires Fe-S clusters not present), B (dehydratase, no NAD+), and D (glycosidase, no NAD+), leaving C as the only NAD+-dependent aldehyde oxidation consistent with the sequence's dehydrogenase features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C involves NAD(+) as a cofactor, and the sequence clearly displays NAD-binding motifs. The other three choices involve fundamentally different enzyme classes (Fe-S oxygenase, dehydratase, glycosidase) with no sequence-level support. No ambiguity exists among the offered alternatives.


### Important caveats

- The specific substrate preference (formaldehyde vs. acetaldehyde) is harder to determine from sequence alone; the UniProt entry also notes acetaldehyde oxidation activity. However, among the four offered choices, only C is an aldehyde dehydrogenase reaction with NAD+, so the discrimination among the provided options does not require resolving the exact substrate preference.
- The entry was first publicly released in April 2025; the benchmark author's exact source snapshot is unknown, though the sequence matches.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark features of the aldehyde dehydrogenase (ALDH) superfamily: (1) A Rossmann-fold-like NAD-binding region in the N-terminal half with glycine-rich motifs (e.g., 'VIGRGVETMKIG', 'GPGSTVYIAGAGPVGLAAAASARLLGAAVVIVGDVNP') characteristic of dinucleotide-binding domains found in dehydrogenases. (2) A zinc-binding cysteine cluster ('CGHCRTCK') typical of ALDH catalytic domains. (3) The overall ~400-residue two-domain architecture (NAD-binding + catalytic) matches bacterial ALDH enzymes. Among the four choices, only C involves NAD(+) as a cofactor; A uses [2Fe-2S] ferredoxin (no Fe-S binding motifs present), B is a dehydratase (no cofactor), and D is a glycosidase (no NAD+ requirement). The presence of NAD-binding motifs and zinc-coordinating cysteines, combined with ALDH-family knowledge learned from other characterized ALDH enzymes, meaningfully distinguishes C as the only NAD+-dependent aldehyde oxidation reaction consistent with the observed sequence features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of the ALDH superfamily (Rossmann-fold NAD-binding, zinc-binding Cys cluster, two-domain architecture) and the cofactor requirements of the four offered reactions allow a knowledgeable model to eliminate A (requires Fe-S clusters not present), B (dehydratase, no NAD+), and D (glycosidase, no NAD+), leaving C as the only NAD+-dependent aldehyde oxidation consistent with the sequence's dehydrogenase features."
  },
  "case_id": "catalytic_activity_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C1",
      "H5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ0 (sequence exactly matched, 399 aa) is annotated as Glutathione-independent formaldehyde dehydrogenase (EC 1.2.1.46) with the catalytic reaction 'formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)' backed by experimental evidence (ECO:0000269) from two PubMed publications (23989142, 24125754). The sequence in the question matches the database entry exactly."
  },
  "important_caveats": [
    "The specific substrate preference (formaldehyde vs. acetaldehyde) is harder to determine from sequence alone; the UniProt entry also notes acetaldehyde oxidation activity. However, among the four offered choices, only C is an aldehyde dehydrogenase reaction with NAD+, so the discrimination among the provided options does not require resolving the exact substrate preference.",
    "The entry was first publicly released in April 2025; the benchmark author's exact source snapshot is unknown, though the sequence matches."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C involves NAD(+) as a cofactor, and the sequence clearly displays NAD-binding motifs. The other three choices involve fundamentally different enzyme classes (Fe-S oxygenase, dehydratase, glycosidase) with no sequence-level support. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ0 (sequence exactly matched, 399 aa) is annotated as Glutathione-independent formaldehyde dehydrogenase (EC 1.2.1.46) with the catalytic reaction 'formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)' backed by experimental evidence (ECO:0000269) from two PubMed publications (23989142, 24125754). The sequence in the question matches the database entry exactly.",
    "evidence_ids": ["C5", "C4", "C1", "H5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark features of the aldehyde dehydrogenase (ALDH) superfamily: (1) A Rossmann-fold-like NAD-binding region in the N-terminal half with glycine-rich motifs (e.g., 'VIGRGVETMKIG', 'GPGSTVYIAGAGPVGLAAAASARLLGAAVVIVGDVNP') characteristic of dinucleotide-binding domains found in dehydrogenases. (2) A zinc-binding cysteine cluster ('CGHCRTCK') typical of ALDH catalytic domains. (3) The overall ~400-residue two-domain architecture (NAD-binding + catalytic) matches bacterial ALDH enzymes. Among the four choices, only C involves NAD(+) as a cofactor; A uses [2Fe-2S] ferredoxin (no Fe-S binding motifs present), B is a dehydratase (no cofactor), and D is a glycosidase (no NAD+ requirement). The presence of NAD-binding motifs and zinc-coordinating cysteines, combined with ALDH-family knowledge learned from other characterized ALDH enzymes, meaningfully distinguishes C as the only NAD+-dependent aldehyde oxidation reaction consistent with the observed sequence features.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of the ALDH superfamily (Rossmann-fold NAD-binding, zinc-binding Cys cluster, two-domain architecture) and the cofactor requirements of the four offered reactions allow a knowledgeable model to eliminate A (requires Fe-S clusters not present), B (dehydratase, no NAD+), and D (glycosidase, no NAD+), leaving C as the only NAD+-dependent aldehyde oxidation consistent with the sequence's dehydrogenase features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C involves NAD(+) as a cofactor, and the sequence clearly displays NAD-binding motifs. The other three choices involve fundamentally different enzyme classes (Fe-S oxygenase, dehydratase, glycosidase) with no sequence-level support. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The specific substrate preference (formaldehyde vs. acetaldehyde) is harder to determine from sequence alone; the UniProt entry also notes acetaldehyde oxidation activity. However, among the four offered choices, only C is an aldehyde dehydrogenase reaction with NAD+, so the discrimination among the provided options does not require resolving the exact substrate preference.",
    "The entry was first publicly released in April 2025; the benchmark author's exact source snapshot is unknown, though the sequence matches."
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
  "benchmark_sequence_length": 399,
  "benchmark_sequence_sha256": "70214ca8ae71a433d6096ebfd9dce33a5f036f03c9ddb435d38ceca9cf7cf469",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 399,
  "current_source_sequence_sha256": "70214ca8ae71a433d6096ebfd9dce33a5f036f03c9ddb435d38ceca9cf7cf469",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXZ0",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e",
  "selected_historical_source_sequence_length": 399,
  "selected_historical_source_sequence_sha256": "70214ca8ae71a433d6096ebfd9dce33a5f036f03c9ddb435d38ceca9cf7cf469",
  "selected_historical_version": {
    "accession": "P0DXZ0",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FALDH_PSEA8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXZ0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:58.597114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:58.597114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas aeruginosa (strain LESB58)\",\"taxonId\":557722}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:58.597114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23989142\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24125754\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.46\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24125754\",\"source\":\"PubMed\"}],\"value\":\"Glutathione-independent formaldehyde dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"FALDH\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24125754\",\"source\":\"PubMed\"}],\"value\":\"FDH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:58.597114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.2.1.46\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23989142\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24125754\",\"source\":\"PubMed\"}],\"name\":\"formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:16425\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16842\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:58.597114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24125754\",\"source\":\"PubMed\"}],\"name\":\"acetaldehyde + NAD(+) + H2O = acetate + NADH + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:25294\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15343\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:58.597114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang W.\",\"Chen S.\",\"Liao Y.\",\"Wang D.\",\"Ding J.\",\"Wang Y.\",\"Ran X.\",\"Lu D.\",\"Zhu H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24125754\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.pep.2013.09.017\"}],\"citationType\":\"journal article\",\"firstPage\":\"208\",\"id\":\"24125754\",\"journal\":\"Protein Expr. Purif.\",\"lastPage\":\"213\",\"publicationDate\":\"2013\",\"title\":\"Expression, purification, and characterization of formaldehyde dehydrogenase from Pseudomonas aeruginosa.\",\"volume\":\"92\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"LESB58\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:58.597114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Liao Y.\",\"Chen S.\",\"Wang D.\",\"Zhang W.\",\"Wang S.\",\"Ding J.\",\"Wang Y.\",\"Cai L.\",\"Ran X.\",\"Wang X.\",\"Zhu H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23989142\"},{\"database\":\"DOI\",\"id\":\"10.1107/s174430911302160x\"}],\"citationType\":\"journal article\",\"firstPage\":\"967\",\"id\":\"23989142\",\"journal\":\"Acta Crystallogr. F\",\"lastPage\":\"972\",\"publicationDate\":\"2013\",\"title\":\"Structure of formaldehyde dehydrogenase from Pseudomonas aeruginosa: the binary complex with the cofactor NAD+.\",\"volume\":\"69\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4JLW\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"LESB58\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) IN COMPLEX WITH NAD AND ZINC\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:58.597114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   FALDH_PSEA8             Reviewed;         399 AA.\nAC   P0DXZ0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Glutathione-independent formaldehyde dehydrogenase {ECO:0000303|PubMed:24125754};\nDE            Short=FALDH {ECO:0000305};\nDE            Short=FDH {ECO:0000303|PubMed:24125754};\nDE            EC=1.2.1.46 {ECO:0000269|PubMed:23989142, ECO:0000269|PubMed:24125754};\nGN   Name=fdhA {ECO:0000312|EMBL:CAW30570.1};\nGN   OrderedLocusNames=PLES_58161 {ECO:0000312|EMBL:CAW30570.1};\nOS   Pseudomonas aeruginosa (strain LESB58).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=557722;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:03.050160+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e",
  "url": "https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Glutathione-independent formaldehyde dehydrogenase {ECO:0000303|PubMed:24125754};\nDE            Short=FALDH {ECO:0000305};\nDE            Short=FDH {ECO:0000303|PubMed:24125754};\nDE            EC=1.2.1.46 {ECO:0000269|PubMed:23989142, ECO:0000269|PubMed:24125754};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:03.050160+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e",
  "url": "https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRC   STRAIN=LESB58;\nRX   PubMed=24125754; DOI=10.1016/j.pep.2013.09.017;\nRA   Zhang W., Chen S., Liao Y., Wang D., Ding J., Wang Y., Ran X., Lu D.,\nRA   Zhu H.;\nRT   \"Expression, purification, and characterization of formaldehyde\nRT   dehydrogenase from Pseudomonas aeruginosa.\";\nRL   Protein Expr. Purif. 92:208-213(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:03.050160+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e",
  "url": "https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "RN   [3] {ECO:0007744|PDB:4JLW}\nRP   X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) IN COMPLEX WITH NAD AND ZINC,\nRP   CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRC   STRAIN=LESB58;\nRX   PubMed=23989142; DOI=10.1107/s174430911302160x;\nRA   Liao Y., Chen S., Wang D., Zhang W., Wang S., Ding J., Wang Y., Cai L.,\nRA   Ran X., Wang X., Zhu H.;\nRT   \"Structure of formaldehyde dehydrogenase from Pseudomonas aeruginosa: the\nRT   binary complex with the cofactor NAD+.\";\nRL   Acta Crystallogr. F 69:967-972(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:03.050160+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e",
  "url": "https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+);\nCC         Xref=Rhea:RHEA:16425, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:15740, ChEBI:CHEBI:16842, ChEBI:CHEBI:57540,\nCC         ChEBI:CHEBI:57945; EC=1.2.1.46;\nCC         Evidence={ECO:0000269|PubMed:23989142, ECO:0000269|PubMed:24125754};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:03.050160+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e",
  "url": "https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=acetaldehyde + NAD(+) + H2O = acetate + NADH + 2 H(+);\nCC         Xref=Rhea:RHEA:25294, ChEBI:CHEBI:15343, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:30089, ChEBI:CHEBI:57540,\nCC         ChEBI:CHEBI:57945; Evidence={ECO:0000269|PubMed:24125754};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:03.050160+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e",
  "url": "https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 192. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
