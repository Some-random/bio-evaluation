# catalytic_activity_0134

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0134.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — L-aspartate + ATP = 4-phospho-L-aspartate + ADP

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSASTPTAPYLEDLVRNSLDQNLPWVVQKYGGTSVGKSLDNITKIVGSYIDNGSKVAIVCSARSTQTKSLGTTNLLLQASREALQPAMSSSGDGRSGSMSGTATPFYPKRVGSGFFGKDQSTSMTSSVSSLSQLESQLGRSGSPSPFQSSSSRSPPRSPATPSQDSSISQEPAFHATVDLIKKGHLEAARASLKGGPLRDELEEEIERDCESLRSFLYAAQIIDEISPRSQDSIVGTGERLACKIVAAALRDRGVDSELVVLDNIVDASMSAASEAVSVDAGDQGVAQLGQEFYDQLSFRLGERLRECGQRVPVVTGYFGPVPGSLLAQIGRGYTDLCAALCAVGLKASELQVWKEVDGIFTADPRKVPSARLVPIITPDEAAELTYYGSEVIHPFTMEQVIRARIPIRIKNVENPSGAGTVIYPDVGFPRGLDTEPPKAERIVEGVDERMPTAVTIKDEIIVLNIHSNRKTLSHGFLARIFGTLDRAGVVVDLISTSEVHVSMAMQDFLNRKRLERLVKDLEKIGEVTVSKDMAILSLVGRNMRNAIGSAGLMFASLARAMINIEMISQGASEINISCVIENKDAIKALNVIHESCLSYPRSPATEMAGLQLQ

[Multiple Choices]
A. (sulfur carrier)-H + L-cysteine = (sulfur carrier)-SH + L-alanine
B. L-aspartate + ATP = 4-phospho-L-aspartate + ADP
C. a 14alpha-methyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
D. L-proline betaine + NADPH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NADP(+) + H2O
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

> The sequence-matched UniProt records annotate this protein as aspartokinase (EC 2.7.2.4) and give the reaction in choice B. The annotation is explicitly supported by similarity to another UniProt protein (ECO:0000250), so this supports the key but is not direct experimental evidence for this exact protein's catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 615-residue sequence has features consistent with an amino-acid biosynthetic kinase, including a conserved-looking kinase catalytic region and a larger multidomain architecture. Transferable family knowledge points to aspartokinase, which uses ATP to phosphorylate L-aspartate, matching B. The alternatives describe distinct enzyme classes and reactions: sulfur transfer, steroid oxidation, or oxidative demethylation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference meaningfully distinguishes B from the offered alternatives; the model need not know this exact protein's database annotation to make that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice B matches the likely aspartokinase family and its characteristic reaction among the offered choices.


### Important caveats

- The supplied evidence supports the reaction through a similarity-based annotation; it does not establish direct experimental measurement of this exact protein's catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 615-residue sequence has features consistent with an amino-acid biosynthetic kinase, including a conserved-looking kinase catalytic region and a larger multidomain architecture. Transferable family knowledge points to aspartokinase, which uses ATP to phosphorylate L-aspartate, matching B. The alternatives describe distinct enzyme classes and reactions: sulfur transfer, steroid oxidation, or oxidative demethylation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully distinguishes B from the offered alternatives; the model need not know this exact protein's database annotation to make that distinction."
  },
  "case_id": "catalytic_activity_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate this protein as aspartokinase (EC 2.7.2.4) and give the reaction in choice B. The annotation is explicitly supported by similarity to another UniProt protein (ECO:0000250), so this supports the key but is not direct experimental evidence for this exact protein's catalytic activity."
  },
  "important_caveats": [
    "The supplied evidence supports the reaction through a similarity-based annotation; it does not establish direct experimental measurement of this exact protein's catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice B matches the likely aspartokinase family and its characteristic reaction among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate this protein as aspartokinase (EC 2.7.2.4) and give the reaction in choice B. The annotation is explicitly supported by similarity to another UniProt protein (ECO:0000250), so this supports the key but is not direct experimental evidence for this exact protein's catalytic activity.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 615-residue sequence has features consistent with an amino-acid biosynthetic kinase, including a conserved-looking kinase catalytic region and a larger multidomain architecture. Transferable family knowledge points to aspartokinase, which uses ATP to phosphorylate L-aspartate, matching B. The alternatives describe distinct enzyme classes and reactions: sulfur transfer, steroid oxidation, or oxidative demethylation.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully distinguishes B from the offered alternatives; the model need not know this exact protein's database annotation to make that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice B matches the likely aspartokinase family and its characteristic reaction among the offered choices."
  },
  "important_caveats": [
    "The supplied evidence supports the reaction through a similarity-based annotation; it does not establish direct experimental measurement of this exact protein's catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9VS37 (AK_CRYN9) explicitly annotates the catalytic activity as 'L-aspartate + ATP = 4-phospho-L-aspartate + ADP' (EC 2.7.2.4, Rhea:RHEA:23776), matching option B verbatim. The evidence code is ECO:0000250 (similarity to P10869), indicating computational transfer rather than direct experimental validation, but the annotation is present and unambiguous. The sequence matches the source entry exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple well-characterized amino acid kinase family (PF00696) signature motifs: 'IITPDE' (in 'LVPIITPDEAAEL'), 'VTGYFG' (in 'PVVTGYFGPVPGSLLAQ'), and 'CAALCAVGL' (in 'DLCAALCAVGLKASELQ'). These are transferable family-level signatures shared across aspartokinase, glutamate 5-kinase, and N-acetylglutamate synthase homologs. Options C and D describe cytochrome P450 monooxygenase reactions requiring a heme-binding motif (FxxGxxxCxG), which is entirely absent. Option A describes a cysteine desulfurase reaction requiring PLP-binding and a catalytic cysteine in a specific fold, also absent. Within the amino acid kinase family, fungal organisms predominantly encode aspartokinase (the threonine biosynthesis pathway is essential in fungi per PubMed:18757810), and the ~615-residue length with a C-terminal regulatory region is consistent with fungal threonine-sensitive aspartokinases. This narrows the family to EC 2.7.2.4, matching option B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The amino acid kinase family motifs (IITPDE, VTGYFG, CAALCAVGL) are well-known, transferable sequence signatures recognizable from homologs in bacteria and other fungi. The fungal context and regulatory-domain architecture further distinguish aspartokinase from other family members. The P450 and desulfurase distractors lack any corresponding structural motifs in the sequence. A model with knowledge of the amino acid kinase superfamily and fungal amino acid biosynthesis can meaningfully select B without memorizing this specific entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D require P450 heme-binding motifs absent from the sequence. Option A requires cysteine desulfurase architecture also absent. Option B uniquely matches the amino acid kinase family motifs present. No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation evidence code is ECO:0000250 (similarity to P10869), meaning the catalytic activity assignment is computational transfer rather than direct experimental measurement on this exact protein.
- The fungal aspartokinase identification relies on family-level inference; the sequence motifs confirm the amino acid kinase superfamily but distinguishing aspartokinase from glutamate 5-kinase within the family leans on the fungal biological context (aspartokinase is the predominant member in fungi).
- The reviewer-only evidence confirms sequence match and annotation, but the evaluated model did not have access to the UniProt accession or organism identity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple well-characterized amino acid kinase family (PF00696) signature motifs: 'IITPDE' (in 'LVPIITPDEAAEL'), 'VTGYFG' (in 'PVVTGYFGPVPGSLLAQ'), and 'CAALCAVGL' (in 'DLCAALCAVGLKASELQ'). These are transferable family-level signatures shared across aspartokinase, glutamate 5-kinase, and N-acetylglutamate synthase homologs. Options C and D describe cytochrome P450 monooxygenase reactions requiring a heme-binding motif (FxxGxxxCxG), which is entirely absent. Option A describes a cysteine desulfurase reaction requiring PLP-binding and a catalytic cysteine in a specific fold, also absent. Within the amino acid kinase family, fungal organisms predominantly encode aspartokinase (the threonine biosynthesis pathway is essential in fungi per PubMed:18757810), and the ~615-residue length with a C-terminal regulatory region is consistent with fungal threonine-sensitive aspartokinases. This narrows the family to EC 2.7.2.4, matching option B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The amino acid kinase family motifs (IITPDE, VTGYFG, CAALCAVGL) are well-known, transferable sequence signatures recognizable from homologs in bacteria and other fungi. The fungal context and regulatory-domain architecture further distinguish aspartokinase from other family members. The P450 and desulfurase distractors lack any corresponding structural motifs in the sequence. A model with knowledge of the amino acid kinase superfamily and fungal amino acid biosynthesis can meaningfully select B without memorizing this specific entry."
  },
  "case_id": "catalytic_activity_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry J9VS37 (AK_CRYN9) explicitly annotates the catalytic activity as 'L-aspartate + ATP = 4-phospho-L-aspartate + ADP' (EC 2.7.2.4, Rhea:RHEA:23776), matching option B verbatim. The evidence code is ECO:0000250 (similarity to P10869), indicating computational transfer rather than direct experimental validation, but the annotation is present and unambiguous. The sequence matches the source entry exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation evidence code is ECO:0000250 (similarity to P10869), meaning the catalytic activity assignment is computational transfer rather than direct experimental measurement on this exact protein.",
    "The fungal aspartokinase identification relies on family-level inference; the sequence motifs confirm the amino acid kinase superfamily but distinguishing aspartokinase from glutamate 5-kinase within the family leans on the fungal biological context (aspartokinase is the predominant member in fungi).",
    "The reviewer-only evidence confirms sequence match and annotation, but the evaluated model did not have access to the UniProt accession or organism identity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D require P450 heme-binding motifs absent from the sequence. Option A requires cysteine desulfurase architecture also absent. Option B uniquely matches the amino acid kinase family motifs present. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9VS37 (AK_CRYN9) explicitly annotates the catalytic activity as 'L-aspartate + ATP = 4-phospho-L-aspartate + ADP' (EC 2.7.2.4, Rhea:RHEA:23776), matching option B verbatim. The evidence code is ECO:0000250 (similarity to P10869), indicating computational transfer rather than direct experimental validation, but the annotation is present and unambiguous. The sequence matches the source entry exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple well-characterized amino acid kinase family (PF00696) signature motifs: 'IITPDE' (in 'LVPIITPDEAAEL'), 'VTGYFG' (in 'PVVTGYFGPVPGSLLAQ'), and 'CAALCAVGL' (in 'DLCAALCAVGLKASELQ'). These are transferable family-level signatures shared across aspartokinase, glutamate 5-kinase, and N-acetylglutamate synthase homologs. Options C and D describe cytochrome P450 monooxygenase reactions requiring a heme-binding motif (FxxGxxxCxG), which is entirely absent. Option A describes a cysteine desulfurase reaction requiring PLP-binding and a catalytic cysteine in a specific fold, also absent. Within the amino acid kinase family, fungal organisms predominantly encode aspartokinase (the threonine biosynthesis pathway is essential in fungi per PubMed:18757810), and the ~615-residue length with a C-terminal regulatory region is consistent with fungal threonine-sensitive aspartokinases. This narrows the family to EC 2.7.2.4, matching option B.",
    "missing_item_specific_fact": "",
    "reason": "The amino acid kinase family motifs (IITPDE, VTGYFG, CAALCAVGL) are well-known, transferable sequence signatures recognizable from homologs in bacteria and other fungi. The fungal context and regulatory-domain architecture further distinguish aspartokinase from other family members. The P450 and desulfurase distractors lack any corresponding structural motifs in the sequence. A model with knowledge of the amino acid kinase superfamily and fungal amino acid biosynthesis can meaningfully select B without memorizing this specific entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D require P450 heme-binding motifs absent from the sequence. Option A requires cysteine desulfurase architecture also absent. Option B uniquely matches the amino acid kinase family motifs present. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation evidence code is ECO:0000250 (similarity to P10869), meaning the catalytic activity assignment is computational transfer rather than direct experimental measurement on this exact protein.",
    "The fungal aspartokinase identification relies on family-level inference; the sequence motifs confirm the amino acid kinase superfamily but distinguishing aspartokinase from glutamate 5-kinase within the family leans on the fungal biological context (aspartokinase is the predominant member in fungi).",
    "The reviewer-only evidence confirms sequence match and annotation, but the evaluated model did not have access to the UniProt accession or organism identity."
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
  "benchmark_sequence_length": 615,
  "benchmark_sequence_sha256": "536d54264e6ff3f5d7f7604b6c1376b560b69f4005ef267570182f96dffb6a42",
  "current_entry_audit": {
    "entryVersion": 68,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 615,
  "current_source_sequence_sha256": "536d54264e6ff3f5d7f7604b6c1376b560b69f4005ef267570182f96dffb6a42",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 66,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VS37",
  "selected_historical_entry_version": 66,
  "selected_historical_record_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "selected_historical_source_sequence_length": 615,
  "selected_historical_source_sequence_sha256": "536d54264e6ff3f5d7f7604b6c1376b560b69f4005ef267570182f96dffb6a42",
  "selected_historical_version": {
    "accession": "J9VS37",
    "database": "Swiss-Prot",
    "entryVersion": 66,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AK_CRYN9",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VS37\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":68,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.2.4\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartokinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23777\"}}],\"reaction\":{\"ecNumber\":\"2.7.2.4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"name\":\"L-aspartate + ATP = 4-phospho-L-aspartate + ADP\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23776\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29991\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H1",
  "excerpt": "ID   AK_CRYN9                Reviewed;         615 AA.\nAC   J9VS37;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 66.\nDE   RecName: Full=Aspartokinase {ECO:0000305};\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\nGN   Name=HOM3 {ECO:0000303|PubMed:18757810};\nGN   ORFNames=CNAG_04347 {ECO:0000312|EMBL:AFR97078.1};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aspartokinase {ECO:0000305};\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;\nRA   Kingsbury J.M., McCusker J.H.;\nRT   \"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\";\nRL   Microbiology 154:2767-2775(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;\nCC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
