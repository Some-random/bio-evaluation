# catalytic_activity_0022

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0022.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGFAARPFHIVFSLFVLAGATQALIICPFDSIYQFGDSISDTGNYIRILPNGPAAAAANFPYGITFPGIPTGRFSDGRLIVDFIARVLGLPLLNPYLQQNASFKNGVNFAVGGATALNSSVLAAAGVQIPDIYLIPLSTQLNWFQTYLRSNCSSPTECSKKVQNSLFLIGNIGNNDVNYALPYRTIQEIEAYVPSIAKAVANATREIIRLGGRRIIVPGTFPFGCLPRNLYLFPNGDKDDLGCLRRLNDLSIYFNNLFQQALNSLRIEFPQAVIIYADYYNAFRFLLRNARALGFTSTLQSCCGIGGPYNFDLNRLCGFPGVPVCRNPREYIQWDGFHYTEAAHRHIVQYLIPDILKELKCS

[Multiple Choices]
A. 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)
B. a 5'-end (5'-triphosphoguanosine)-adenylyl-adenylyl-cytidylyl-adenosine in mRNA + 2 S-adenosyl-L-methionine = a 5'-end (N(7)-methyl 5'-triphosphoguanosine)-(2'-O-methyladenylyl)-adenylyl-cytidylyl-adenosine in mRNA + 2 S-adenosyl-L-homocysteine + H(+)
C. 2',2'-dihydroxy-2-oxospirilloxanthin = 2,2'-dioxospirilloxanthin + H2O
D. L-aspartate + ATP = 4-phospho-L-aspartate + ADP
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

> The sequence-matched UniProt entry annotates the reaction in A as catalytic activity with ECO:0000269 evidence linked to a publication. The archived entry also contains this annotation, so support is not limited to the current snapshot. The cited paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly hydrophobic N-terminal segment consistent with a signal peptide, followed by a predominantly non-membrane protein. In the offered choices, A is ester hydrolysis, compatible with an esterase; B and D require characteristic SAM-dependent methyltransferase or ATP-dependent kinase functions, respectively, for which the sequence offers no obvious signature. C concerns a specialized carotenoid transformation and is less consistent with this apparent protein architecture. These are probabilistic class-level clues, not proof of the exact substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and enzyme-class knowledge gives a meaningful basis to favor A among these alternatives. The precise norajmaline substrate specificity is not established from those clues alone, but the alternatives are distinct enough that this limitation does not make the choice lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option has comparable support from the sequence-level class clues.


### Important caveats

- The sequence clues support a probabilistic choice of reaction class, not independent confirmation of the exact substrate and products.
- The reviewer-only annotation is sequence-matched; its cited experimental evidence was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal segment consistent with a signal peptide, followed by a predominantly non-membrane protein. In the offered choices, A is ester hydrolysis, compatible with an esterase; B and D require characteristic SAM-dependent methyltransferase or ATP-dependent kinase functions, respectively, for which the sequence offers no obvious signature. C concerns a specialized carotenoid transformation and is less consistent with this apparent protein architecture. These are probabilistic class-level clues, not proof of the exact substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-class knowledge gives a meaningful basis to favor A among these alternatives. The precise norajmaline substrate specificity is not established from those clues alone, but the alternatives are distinct enough that this limitation does not make the choice lookup-dependent."
  },
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the reaction in A as catalytic activity with ECO:0000269 evidence linked to a publication. The archived entry also contains this annotation, so support is not limited to the current snapshot. The cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence clues support a probabilistic choice of reaction class, not independent confirmation of the exact substrate and products.",
    "The reviewer-only annotation is sequence-matched; its cited experimental evidence was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option has comparable support from the sequence-level class clues."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the reaction in A as catalytic activity with ECO:0000269 evidence linked to a publication. The archived entry also contains this annotation, so support is not limited to the current snapshot. The cited paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal segment consistent with a signal peptide, followed by a predominantly non-membrane protein. In the offered choices, A is ester hydrolysis, compatible with an esterase; B and D require characteristic SAM-dependent methyltransferase or ATP-dependent kinase functions, respectively, for which the sequence offers no obvious signature. C concerns a specialized carotenoid transformation and is less consistent with this apparent protein architecture. These are probabilistic class-level clues, not proof of the exact substrate.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-class knowledge gives a meaningful basis to favor A among these alternatives. The precise norajmaline substrate specificity is not established from those clues alone, but the alternatives are distinct enough that this limitation does not make the choice lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option has comparable support from the sequence-level class clues."
  },
  "important_caveats": [
    "The sequence clues support a probabilistic choice of reaction class, not independent confirmation of the exact substrate and products.",
    "The reviewer-only annotation is sequence-matched; its cited experimental evidence was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ5 (Acetylajmalan esterase 2, RsAAE2) from Rauvolfia serpentina is annotated with EC 3.1.1.80 and the exact catalytic reaction '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' with experimental evidence (ECO:0000269, PubMed:38212296). The sequence in the benchmark matches the source entry exactly (SHA-256 confirmed). The expected answer A is directly supported by experimentally verified annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains the highly conserved 'GDSISDTG' motif (approximately residues 45-52), which is the signature GDSL catalytic motif of the GDSL lipase/esterase superfamily. GDSL esterases are a large, well-characterized family of plant secretory hydrolases that cleave ester bonds. The N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC...) is consistent with plant secretory esterases. Among the four choices, only option A represents an esterase (EC 3.1.1.x) reaction: hydrolysis of an acetate ester to release acetate. Option B is a methyltransferase (cap methylation), option C is a dehydratase (carotenoid dehydration), and option D is a kinase (aspartate phosphorylation). None of these enzyme classes would contain a GDSL motif. A knowledgeable model recognizing the GDSL motif from other plant GDSL esterases can confidently assign esterase activity, which uniquely matches choice A among the offered alternatives. The specific substrate identity (norajmaline vs ajmaline) is irrelevant here since only one esterase option is presented.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GDSL motif is a well-established family-level sequence signature shared across hundreds of characterized plant esterases and lipases. Recognizing this motif and mapping it to esterase activity is legitimate transfer knowledge from other proteins. Among the four offered choices, only A is an esterase reaction, making the family-level inference sufficient to select the correct answer without needing the exact substrate annotation of this specific protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four distinct enzyme classes (esterase, methyltransferase, dehydratase, kinase). The GDSL motif unambiguously identifies the protein as an esterase, eliminating B, C, and D. No ambiguity exists among the offered alternatives.


### Important caveats

- The specific substrate (norajmaline vs. ajmaline) is not derivable from sequence alone, but this distinction is irrelevant because only one esterase option (A) is offered among the choices.
- The protein was characterized experimentally in 2024 (PubMed:38212296) and deposited in UniProt in June 2025, making it relatively recent knowledge.
- The GDSL motif identification is a family-level inference from other plant esterases; it does not require memorization of this specific protein's record.
- The UniProt entry also lists a second catalytic activity (17-O-acetylajmaline → ajmaline) inferred by similarity (ECO:0000250), but this is not among the choices and does not affect the answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains the highly conserved 'GDSISDTG' motif (approximately residues 45-52), which is the signature GDSL catalytic motif of the GDSL lipase/esterase superfamily. GDSL esterases are a large, well-characterized family of plant secretory hydrolases that cleave ester bonds. The N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC...) is consistent with plant secretory esterases. Among the four choices, only option A represents an esterase (EC 3.1.1.x) reaction: hydrolysis of an acetate ester to release acetate. Option B is a methyltransferase (cap methylation), option C is a dehydratase (carotenoid dehydration), and option D is a kinase (aspartate phosphorylation). None of these enzyme classes would contain a GDSL motif. A knowledgeable model recognizing the GDSL motif from other plant GDSL esterases can confidently assign esterase activity, which uniquely matches choice A among the offered alternatives. The specific substrate identity (norajmaline vs ajmaline) is irrelevant here since only one esterase option is presented.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GDSL motif is a well-established family-level sequence signature shared across hundreds of characterized plant esterases and lipases. Recognizing this motif and mapping it to esterase activity is legitimate transfer knowledge from other proteins. Among the four offered choices, only A is an esterase reaction, making the family-level inference sufficient to select the correct answer without needing the exact substrate annotation of this specific protein."
  },
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ5 (Acetylajmalan esterase 2, RsAAE2) from Rauvolfia serpentina is annotated with EC 3.1.1.80 and the exact catalytic reaction '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' with experimental evidence (ECO:0000269, PubMed:38212296). The sequence in the benchmark matches the source entry exactly (SHA-256 confirmed). The expected answer A is directly supported by experimentally verified annotation."
  },
  "important_caveats": [
    "The specific substrate (norajmaline vs. ajmaline) is not derivable from sequence alone, but this distinction is irrelevant because only one esterase option (A) is offered among the choices.",
    "The protein was characterized experimentally in 2024 (PubMed:38212296) and deposited in UniProt in June 2025, making it relatively recent knowledge.",
    "The GDSL motif identification is a family-level inference from other plant esterases; it does not require memorization of this specific protein's record.",
    "The UniProt entry also lists a second catalytic activity (17-O-acetylajmaline → ajmaline) inferred by similarity (ECO:0000250), but this is not among the choices and does not affect the answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (esterase, methyltransferase, dehydratase, kinase). The GDSL motif unambiguously identifies the protein as an esterase, eliminating B, C, and D. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ5 (Acetylajmalan esterase 2, RsAAE2) from Rauvolfia serpentina is annotated with EC 3.1.1.80 and the exact catalytic reaction '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' with experimental evidence (ECO:0000269, PubMed:38212296). The sequence in the benchmark matches the source entry exactly (SHA-256 confirmed). The expected answer A is directly supported by experimentally verified annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains the highly conserved 'GDSISDTG' motif (approximately residues 45-52), which is the signature GDSL catalytic motif of the GDSL lipase/esterase superfamily. GDSL esterases are a large, well-characterized family of plant secretory hydrolases that cleave ester bonds. The N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC...) is consistent with plant secretory esterases. Among the four choices, only option A represents an esterase (EC 3.1.1.x) reaction: hydrolysis of an acetate ester to release acetate. Option B is a methyltransferase (cap methylation), option C is a dehydratase (carotenoid dehydration), and option D is a kinase (aspartate phosphorylation). None of these enzyme classes would contain a GDSL motif. A knowledgeable model recognizing the GDSL motif from other plant GDSL esterases can confidently assign esterase activity, which uniquely matches choice A among the offered alternatives. The specific substrate identity (norajmaline vs ajmaline) is irrelevant here since only one esterase option is presented.",
    "missing_item_specific_fact": "",
    "reason": "The GDSL motif is a well-established family-level sequence signature shared across hundreds of characterized plant esterases and lipases. Recognizing this motif and mapping it to esterase activity is legitimate transfer knowledge from other proteins. Among the four offered choices, only A is an esterase reaction, making the family-level inference sufficient to select the correct answer without needing the exact substrate annotation of this specific protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (esterase, methyltransferase, dehydratase, kinase). The GDSL motif unambiguously identifies the protein as an esterase, eliminating B, C, and D. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The specific substrate (norajmaline vs. ajmaline) is not derivable from sequence alone, but this distinction is irrelevant because only one esterase option (A) is offered among the choices.",
    "The protein was characterized experimentally in 2024 (PubMed:38212296) and deposited in UniProt in June 2025, making it relatively recent knowledge.",
    "The GDSL motif identification is a family-level inference from other plant esterases; it does not require memorization of this specific protein's record.",
    "The UniProt entry also lists a second catalytic activity (17-O-acetylajmaline → ajmaline) inferred by similarity (ECO:0000250), but this is not among the choices and does not affect the answer."
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
  "benchmark_sequence_length": 362,
  "benchmark_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 362,
  "current_source_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
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
  "requested_accession": "P0DXJ5",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "selected_historical_source_sequence_length": 362,
  "selected_historical_source_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
  "selected_historical_version": {
    "accession": "P0DXJ5",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AAE2_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"3.1.1.80\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Acetylajmalan esterase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsAAE2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23797\"}}],\"reaction\":{\"ecNumber\":\"3.1.1.80\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"name\":\"17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23796\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77725\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3MKY2\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:22125\"}}],\"reaction\":{\"ecNumber\":\"3.1.1.80\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3MKY2\",\"source\":\"UniProtKB\"}],\"name\":\"17-O-acetylajmaline + H2O = ajmaline + acetate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:22124\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58567\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58679\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   AAE2_RAUSE              Reviewed;         362 AA.\nAC   P0DXJ5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Acetylajmalan esterase 2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsAAE2 {ECO:0000303|PubMed:38212296};\nDE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};\nDE   Flags: Precursor;\nGN   Name=AAE2 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Acetylajmalan esterase 2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsAAE2 {ECO:0000303|PubMed:38212296};\nDE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE\nRP   SPECIFICITY, AND BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+);\nCC         Xref=Rhea:RHEA:23796, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30089, ChEBI:CHEBI:77618, ChEBI:CHEBI:77725; EC=3.1.1.80;\nCC         Evidence={ECO:0000269|PubMed:38212296};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23797;\nCC         Evidence={ECO:0000269|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=17-O-acetylajmaline + H2O = ajmaline + acetate + H(+);\nCC         Xref=Rhea:RHEA:22124, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30089, ChEBI:CHEBI:58567, ChEBI:CHEBI:58679; EC=3.1.1.80;\nCC         Evidence={ECO:0000250|UniProtKB:Q3MKY2};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:22125;\nCC         Evidence={ECO:0000250|UniProtKB:Q3MKY2};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 22. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
