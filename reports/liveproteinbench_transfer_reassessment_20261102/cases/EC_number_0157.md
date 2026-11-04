# EC_number_0157

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0157.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 3.1.1.80

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
A. 3.1.3.16
B. 3.1.1.80
C. 1.1.1.12
D. 6.3.5.1
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The matched-sequence UniProt annotation assigns EC 3.1.1.80 and records the ester-hydrolysis reaction for that EC with ECO:0000269 evidence linked to a publication. This supports the key, though the primary paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a GDSIS segment matching the common GxSxG nucleophile motif of serine hydrolases, making hydrolysis of an ester a credible family-level inference. That points toward the EC 3.1.1 hydrolase option B over the phosphatase, dehydrogenase, and ligase alternatives. The motif does not by itself establish the precise substrate or EC subclass.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about serine-hydrolase motifs meaningfully distinguishes the offered ester-hydrolase choice from the alternatives, even though exact EC 3.1.1.80 activity would require more specific evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based inference favors B among the listed choices; no other offered option is comparably supported.


### Important caveats

- A serine-hydrolase motif supports an enzyme-class inference, not the exact substrate specificity or full four-digit EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GDSIS segment matching the common GxSxG nucleophile motif of serine hydrolases, making hydrolysis of an ester a credible family-level inference. That points toward the EC 3.1.1 hydrolase option B over the phosphatase, dehydrogenase, and ligase alternatives. The motif does not by itself establish the precise substrate or EC subclass.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about serine-hydrolase motifs meaningfully distinguishes the offered ester-hydrolase choice from the alternatives, even though exact EC 3.1.1.80 activity would require more specific evidence."
  },
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 3.1.1.80 and records the ester-hydrolysis reaction for that EC with ECO:0000269 evidence linked to a publication. This supports the key, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "A serine-hydrolase motif supports an enzyme-class inference, not the exact substrate specificity or full four-digit EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference favors B among the listed choices; no other offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 3.1.1.80 and records the ester-hydrolysis reaction for that EC with ECO:0000269 evidence linked to a publication. This supports the key, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a GDSIS segment matching the common GxSxG nucleophile motif of serine hydrolases, making hydrolysis of an ester a credible family-level inference. That points toward the EC 3.1.1 hydrolase option B over the phosphatase, dehydrogenase, and ligase alternatives. The motif does not by itself establish the precise substrate or EC subclass.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about serine-hydrolase motifs meaningfully distinguishes the offered ester-hydrolase choice from the alternatives, even though exact EC 3.1.1.80 activity would require more specific evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference favors B among the listed choices; no other offered option is comparably supported."
  },
  "important_caveats": [
    "A serine-hydrolase motif supports an enzyme-class inference, not the exact substrate specificity or full four-digit EC assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C4, C5, H2, H4) confirms that P0DXJ5 is annotated as 'Acetylajmalan esterase 2' with EC 3.1.1.80, supported by experimental evidence (ECO:0000269|PubMed:38212296, Nat. Commun. 2024). The catalytic reaction (17-O-acetylnorajmaline + H2O = norajmaline + acetate + H+) is a carboxylesterase reaction consistent with EC 3.1.1.80. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options span three distinct EC major classes (1=oxidoreductase, 3=hydrolase, 6=ligase) and two hydrolase subclasses (3.1.1=carboxylesterase, 3.1.3=phosphatase). Transferable reasoning: (1) Option C (1.1.1.12, alcohol dehydrogenase NADP+) requires a Rossmann-fold nucleotide-binding motif (GxGxG) and typically a zinc-binding Cys-X2-His-X3-His site; neither is present in this sequence, and the N-terminal signal peptide is atypical for cytoplasmic ADHs. (2) Option D (6.3.5.1, glutamine synthetase) requires distinctive ATP-binding motifs, a GS-like fold, and metal-coordinating residues; none are recognizable, and GS is cytoplasmic. (3) Between A (3.1.3.16, phosphatase) and B (3.1.1.80, carboxylesterase): the clear N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC) indicates a secreted/membrane-targeted protein. Plant phosphatases (EC 3.1.3.x) are overwhelmingly intracellular, whereas plant esterases involved in alkaloid/terpenoid secondary metabolism are frequently secreted or ER-localized. The ~362-aa size, hydrophobic core architecture, and absence of canonical phosphatase metal-binding motifs (DXDXD, alkaline phosphatase His/Asp clusters) further favor an α/β-hydrolase esterase over a phosphatase. While a perfect GXSXG motif is not unambiguously identifiable in this sequence, the overall domain architecture and cellular-localization logic learned from other plant secondary-metabolism esterases meaningfully favor B over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C (no Rossmann fold, no ADH motifs) and D (no GS/ligase motifs) by absence of required functional motifs. The signal-peptide-to-plant-secondary-metabolism-esterase correlation and absence of phosphatase metal-binding motifs provide a probabilistic but meaningful preference for B over A. This is a legitimate family-level and localization-pattern inference transferable from other plant esterases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span different EC major classes and subclasses. The elimination of C and D is straightforward by absence of required motifs. The A-vs-B distinction is supported by the signal peptide and absence of phosphatase motifs, though not absolutely airtight; B remains the most defensible choice given the offered alternatives.


### Important caveats

- The GXSXG catalytic motif typical of α/β-hydrolases is not unambiguously identifiable in this sequence, weakening the direct structural argument for esterase activity, though overall architecture and localization logic remain supportive.
- EC 3.1.1.80 is a highly specific 4th-digit designation (acetylajmalan esterase); however, since only one 3.1.1.x option is offered, the task effectively reduces to identifying the EC class/subclass, which is more achievable through transferable reasoning.
- The signal-peptide-to-secreted-plant-esterase correlation is a statistical/family-level pattern, not a universal rule; some phosphatases are secreted, and not all plant esterases are secreted.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options span three distinct EC major classes (1=oxidoreductase, 3=hydrolase, 6=ligase) and two hydrolase subclasses (3.1.1=carboxylesterase, 3.1.3=phosphatase). Transferable reasoning: (1) Option C (1.1.1.12, alcohol dehydrogenase NADP+) requires a Rossmann-fold nucleotide-binding motif (GxGxG) and typically a zinc-binding Cys-X2-His-X3-His site; neither is present in this sequence, and the N-terminal signal peptide is atypical for cytoplasmic ADHs. (2) Option D (6.3.5.1, glutamine synthetase) requires distinctive ATP-binding motifs, a GS-like fold, and metal-coordinating residues; none are recognizable, and GS is cytoplasmic. (3) Between A (3.1.3.16, phosphatase) and B (3.1.1.80, carboxylesterase): the clear N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC) indicates a secreted/membrane-targeted protein. Plant phosphatases (EC 3.1.3.x) are overwhelmingly intracellular, whereas plant esterases involved in alkaloid/terpenoid secondary metabolism are frequently secreted or ER-localized. The ~362-aa size, hydrophobic core architecture, and absence of canonical phosphatase metal-binding motifs (DXDXD, alkaline phosphatase His/Asp clusters) further favor an α/β-hydrolase esterase over a phosphatase. While a perfect GXSXG motif is not unambiguously identifiable in this sequence, the overall domain architecture and cellular-localization logic learned from other plant secondary-metabolism esterases meaningfully favor B over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C (no Rossmann fold, no ADH motifs) and D (no GS/ligase motifs) by absence of required functional motifs. The signal-peptide-to-plant-secondary-metabolism-esterase correlation and absence of phosphatase metal-binding motifs provide a probabilistic but meaningful preference for B over A. This is a legitimate family-level and localization-pattern inference transferable from other plant esterases."
  },
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C4, C5, H2, H4) confirms that P0DXJ5 is annotated as 'Acetylajmalan esterase 2' with EC 3.1.1.80, supported by experimental evidence (ECO:0000269|PubMed:38212296, Nat. Commun. 2024). The catalytic reaction (17-O-acetylnorajmaline + H2O = norajmaline + acetate + H+) is a carboxylesterase reaction consistent with EC 3.1.1.80. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The GXSXG catalytic motif typical of α/β-hydrolases is not unambiguously identifiable in this sequence, weakening the direct structural argument for esterase activity, though overall architecture and localization logic remain supportive.",
    "EC 3.1.1.80 is a highly specific 4th-digit designation (acetylajmalan esterase); however, since only one 3.1.1.x option is offered, the task effectively reduces to identifying the EC class/subclass, which is more achievable through transferable reasoning.",
    "The signal-peptide-to-secreted-plant-esterase correlation is a statistical/family-level pattern, not a universal rule; some phosphatases are secreted, and not all plant esterases are secreted."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span different EC major classes and subclasses. The elimination of C and D is straightforward by absence of required motifs. The A-vs-B distinction is supported by the signal peptide and absence of phosphatase motifs, though not absolutely airtight; B remains the most defensible choice given the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"EC_number_0157","expected_answer_check":{"judgment":"supported","reason":"The reviewer evidence (C4, C5, H2, H4) confirms that P0DXJ5 is annotated as 'Acetylajmalan esterase 2' with EC 3.1.1.80, supported by experimental evidence (ECO:0000269|PubMed:38212296, Nat. Commun. 2024). The catalytic reaction (17-O-acetylnorajmaline + H2O = norajmaline + acetate + H+) is a carboxylesterase reaction consistent with EC 3.1.1.80. The sequence matches the benchmark input exactly.","evidence_ids":["C4","C5","H2","H4"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The four options span three distinct EC major classes (1=oxidoreductase, 3=hydrolase, 6=ligase) and two hydrolase subclasses (3.1.1=carboxylesterase, 3.1.3=phosphatase). Transferable reasoning: (1) Option C (1.1.1.12, alcohol dehydrogenase NADP+) requires a Rossmann-fold nucleotide-binding motif (GxGxG) and typically a zinc-binding Cys-X2-His-X3-His site; neither is present in this sequence, and the N-terminal signal peptide is atypical for cytoplasmic ADHs. (2) Option D (6.3.5.1, glutamine synthetase) requires distinctive ATP-binding motifs, a GS-like fold, and metal-coordinating residues; none are recognizable, and GS is cytoplasmic. (3) Between A (3.1.3.16, phosphatase) and B (3.1.1.80, carboxylesterase): the clear N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC) indicates a secreted/membrane-targeted protein. Plant phosphatases (EC 3.1.3.x) are overwhelmingly intracellular, whereas plant esterases involved in alkaloid/terpenoid secondary metabolism are frequently secreted or ER-localized. The ~362-aa size, hydrophobic core architecture, and absence of canonical phosphatase metal-binding motifs (DXDXD, alkaline phosphatase His/Asp clusters) further favor an α/β-hydrolase esterase over a phosphatase. While a perfect GXSXG motif is not unambiguously identifiable in this sequence, the overall domain architecture and cellular-localization logic learned from other plant secondary-metabolism esterases meaningfully favor B over A.","missing_item_specific_fact":"","reason":"A knowledgeable model can eliminate C (no Rossmann fold, no ADH motifs) and D (no GS/ligase motifs) by absence of required functional motifs. The signal-peptide-to-plant-secondary-metabolism-esterase correlation and absence of phosphatase metal-binding motifs provide a probabilistic but meaningful preference for B over A. This is a legitimate family-level and localization-pattern inference transferable from other plant esterases."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"The four options span different EC major classes and subclasses. The elimination of C and D is straightforward by absence of required motifs. The A-vs-B distinction is supported by the signal peptide and absence of phosphatase motifs, though not absolutely airtight; B remains the most defensible choice given the offered alternatives."},"important_caveats":["The GXSXG catalytic motif typical of α/β-hydrolases is not unambiguously identifiable in this sequence, weakening the direct structural argument for esterase activity, though overall architecture and localization logic remain supportive.","EC 3.1.1.80 is a highly specific 4th-digit designation (acetylajmalan esterase); however, since only one 3.1.1.x option is offered, the task effectively reduces to identifying the EC class/subclass, which is more achievable through transferable reasoning.","The signal-peptide-to-secreted-plant-esterase correlation is a statistical/family-level pattern, not a universal rule; some phosphatases are secreted, and not all plant esterases are secreted."]}
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 157. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
